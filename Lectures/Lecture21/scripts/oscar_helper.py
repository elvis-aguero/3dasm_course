"""Run one job on Oscar, Brown's computing cluster, from a notebook on your own computer.

    from scripts.oscar_helper import Oscar
    oscar = Oscar(modules=["abaqus/2024-mbessa-pskx"])
    folder = oscar.run({"hello.sh": "hostname"}, "bash hello.sh", fetch_to="my_runs")

`run` sends the files to a new folder on Oscar, runs the command there as one Slurm job, waits for it, and copies the
whole folder back. It knows nothing about what the command does.

Requirements: `ssh oscar-campus` works from a terminal without typing a password (on campus or on the VPN; see the
notes of Lecture 21 for the `ControlMaster` lines of `~/.ssh/config`).

Safety: the job runs its command with `srun` on the compute node that Slurm gave it, and stops before any work if it is
not there (never on a login node, which everybody shares). The only job this file ever cancels is the one it submitted,
by its job id, when it takes longer than `timeout`.
"""
import io
import os
import subprocess
import tarfile
import time
from pathlib import Path

JOB = """#!/bin/bash
#SBATCH --job-name={name}
#SBATCH --partition={partition}
#SBATCH --time={walltime}
#SBATCH --mem={mem}
#SBATCH --cpus-per-task=1
#SBATCH --output=slurm.out
cd "$SLURM_SUBMIT_DIR"

# Stop before any work unless this runs on the compute node that Slurm gave the job (never on a login node)
host=$(hostname -s)
echo "host=$host allocated=${{SLURMD_NODENAME:-}} job=$SLURM_JOB_ID"
if [ -z "${{SLURMD_NODENAME:-}}" ] || [ "$host" != "$SLURMD_NODENAME" ] || [[ "$host" == login* ]]; then
  echo "ABORT: not on the allocated compute node"; exit 1
fi
module purge
{modules}
export LANG=en_US.UTF-8
srun --ntasks=1 bash -c {command}
"""


class Oscar:
    """One Slurm job at a time on Oscar, through ssh.

    host        the ssh alias of Oscar in ~/.ssh/config
    remote_dir  folder on Oscar for the jobs, one subfolder each (your scratch is cleaned after 30 days)
    modules     the modules the job loads (`module load ...`)
    partition   the Slurm partition ('batch'; 'debug' often starts sooner, up to 30 minutes)
    mem         the memory of the job
    timeout     seconds to wait for the job before cancelling it (also its Slurm time limit)
    """

    def __init__(self, host="oscar-campus", remote_dir="~/scratch/3dasm", modules=(), partition="batch",
                 mem="4G", timeout=1800):
        self.host, self.remote_dir, self.modules = host, remote_dir.rstrip("/"), list(modules)
        self.partition, self.mem, self.timeout = partition, mem, timeout

    def ssh(self, command, stdin=None):
        """Run a command on Oscar and return its standard output as bytes (Oscar's login messages go to stderr)."""
        r = subprocess.run(["ssh", "-o", "BatchMode=yes", "-o", "ConnectTimeout=15", self.host, command],
                           input=stdin, capture_output=True)
        if r.returncode == 255:
            raise ConnectionError(f"ssh {self.host} failed. Open a terminal, run `ssh {self.host}` once "
                                  f"(on campus or on the VPN), then try again.")
        return r.stdout

    def run(self, files, command, name=None, fetch_to="oscar_runs"):
        """Send `files` ({path: text}) to a new folder on Oscar, run `command` in it as one Slurm job, wait, and copy
        the folder back to `fetch_to`/<name>. Returns the local folder."""
        name = name or f"job_{time.strftime('%Y%m%dT%H%M%S')}_{os.getpid()}"
        folder = f"{self.remote_dir}/{name}"
        files = {**files, "job.sh": JOB.format(
            name=name, partition=self.partition, mem=self.mem, command=_quote(command),
            walltime=time.strftime("%H:%M:%S", time.gmtime(self.timeout)),
            modules="\n".join(f"module load {m}" for m in self.modules))}

        buffer = io.BytesIO()  # the files, sent as one tar archive through ssh
        with tarfile.open(fileobj=buffer, mode="w:gz") as tar:
            for path, text in files.items():
                data = text.encode() if isinstance(text, str) else text
                info = tarfile.TarInfo(path); info.size = len(data)
                tar.addfile(info, io.BytesIO(data))
        out = self.ssh(f"mkdir -p {folder} && tar xzf - -C {folder} && cd {folder} && sbatch --parsable job.sh",
                       stdin=buffer.getvalue()).decode()
        job_id = out.strip().split(";")[0]
        if not job_id.isdigit():
            raise RuntimeError(f"sbatch did not return a job id: {out!r}")
        print(f"Submitted Slurm job {job_id} ({name})")

        t0, last = time.time(), ""
        while True:  # queued, then running, then done
            state = self.ssh(f"sacct -n -X -P -j {job_id} -o State 2>/dev/null | head -1").decode().strip() or "PENDING"
            if state != last:
                print(f"  {time.time() - t0:5.0f} s  {state}")
                last = state
            if not state.startswith(("PENDING", "RUNNING", "REQUEUED", "CONFIGURING", "COMPLETING")):
                break
            if time.time() - t0 > self.timeout:
                self.ssh(f"scancel {job_id}")  # only the job submitted here
                raise TimeoutError(f"job {job_id} did not finish in {self.timeout} s and was cancelled")
            time.sleep(10)

        local = Path(fetch_to) / name
        local.mkdir(parents=True, exist_ok=True)
        with tarfile.open(fileobj=io.BytesIO(self.ssh(f"tar czf - -C {folder} .")), mode="r:gz") as tar:
            tar.extractall(local, filter="data")
        if not state.startswith("COMPLETED"):
            raise RuntimeError(f"job {job_id} ended {state}; see {local / 'slurm.out'}")
        return local


def _quote(command):
    """The command as one single-quoted word for bash."""
    return "'" + command.replace("'", "'\\''") + "'"
