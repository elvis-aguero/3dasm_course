"""Simulate supercompressible designs with Abaqus on Oscar, from a notebook on your own computer.

`OscarAbaqus` is an f3dasm `DataGenerator`. For each open experiment it sends one Slurm job to Oscar that runs the
same two Abaqus analyses as the datasets of the Final Project (linear buckling, then Riks if the design is coilable),
copies the results back, and stores `coilable`, `sigma_crit` and `energy` with the rules of the release:

    from oscar_helper import OscarAbaqus
    experimentdata = OscarAbaqus().call(experimentdata)

Requirements
    * `ssh oscar-campus` works from a terminal without typing a password (on campus or on the VPN; see the notes of
      Lecture 21 for the `ControlMaster` lines of `~/.ssh/config`), and your account can load the Abaqus module.
    * The inputs `ratio_d`, `ratio_pitch`, `ratio_top_diameter` (the 3-d problem, circular longerons) and
      `imperfection` (the amplitude a in mm of the first-mode imperfection of the Riks run).

On Oscar only Abaqus runs: the job checks that it is on the compute node Slurm gave it, runs the four scripts of
`scripts/`, and writes small JSON files. The labels and the energy are computed here, with numpy and scipy.
"""
import io
import json
import math
import os
import subprocess
import tarfile
import time
from pathlib import Path

import numpy as np
from f3dasm.datageneration import DataGenerator
from scipy.integrate import simpson
from scipy.interpolate import PchipInterpolator

HERE = Path(__file__).resolve().parent
SCRIPTS = ["supercompressible_lin_buckle.py", "supercompressible_lin_buckle_pp.py",
           "riks_b31_nocontact.py", "riks_pp_frames.py"]

# Constants of the 3-d datasets (Final Project statement, Bessa et al. 2019)
D1, E, N_LONG, G_E = 100.0, 3500.0, 3, 0.3677
AREA = math.pi * D1 ** 2 / 4.0          # bottom ring, mm^2
FULL, STRAIN_LIMIT = 0.90, 0.02         # "fully coiled" compression, largest strain of a reversible design

# Abaqus wrappers: each runs inside Abaqus, in its own step folder (lb/ or rk/) of the job folder
LB_PRE = """import json, sys
sys.path.insert(0, '../scripts')
from supercompressible_lin_buckle import main
main(json.load(open('../params.json')))
"""
LB_POST = """import glob, json, os, pickle, sys
from abaqus import session
sys.path.insert(0, '../scripts')
from supercompressible_lin_buckle_pp import main
main(session.openOdb(name=os.path.abspath(glob.glob('*.odb')[0])))
r = pickle.load(open('results.pkl', 'rb'))
json.dump({'loads': [float(v) for v in r['loads']], 'coilable': int(r['coilable'])}, open('../lb.json', 'w'))
p = json.load(open('../params.json'))
p.update(max_disps=[float(v) for v in r['max_disps']], lin_buckle_odb=r['lin_buckle_odb'])
json.dump(p, open('../rk_params.json', 'w'))
open('../coilable', 'w').write(str(int(r['coilable'])))
"""
RK_PRE = """import json, sys
sys.path.insert(0, '../scripts')
from riks_b31_nocontact import main
main(json.load(open('../rk_params.json')))
"""
RK_POST = """import glob, json, os, pickle, sys
from abaqus import session
sys.path.insert(0, '../scripts')
from riks_pp_frames import main
main(session.openOdb(name=os.path.abspath(glob.glob('*.odb')[0])))
r = pickle.load(open('results.pkl', 'rb'))
out = {k: [float(v) for v in r[k][2]] for k in ('U', 'RF')}
out.update({k: [float(v) for v in r[k]] for k in ('frame_u3', 'frame_strain')})
json.dump(out, open('../rk.json', 'w'))
"""

JOB = """#!/bin/bash
#SBATCH --job-name={name}
#SBATCH --partition={partition}
#SBATCH --time={walltime}
#SBATCH --mem=4G
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
module load {module}
export LANG=en_US.UTF-8
srun --ntasks=1 bash steps.sh
"""

STEPS = """set -u
run() {  # $1 = step folder, $2 = pre script, $3 = post script
  cd "$1"
  abaqus cae noGUI=$2 -mesa > pre.log 2>&1
  inp=$(ls *.inp 2>/dev/null | head -1)
  [ -n "$inp" ] && abaqus job=${inp%.inp} cpus=1 interactive > job.log 2>&1  # Riks ends with an error once it can no longer advance: still post-process
  [ -n "$inp" ] && abaqus cae noGUI=$3 -mesa > post.log 2>&1
  cd ..
}
run lb lb_pre.py lb_post.py
[ "$(cat coilable 2>/dev/null)" = "1" ] && run rk rk_pre.py rk_post.py
rm -f */*.odb */*.res */*.mdl */*.stt */*.prt */*.sim */*.rpy* */*.rec */*.023 */*.lck */*.SMA*
echo DONE > done
"""


def _energy(strain, stress):
    """Area under the stress-strain curve up to full compression: PCHIP, then Simpson (as the release).
    Points where the strain does not increase are dropped, because the interpolation needs increasing strains."""
    k = np.r_[True, np.diff(strain) > 1e-12]; strain, stress = strain[k], stress[k]
    k = np.maximum.accumulate(strain) == strain; strain, stress = strain[k], stress[k]
    x = np.linspace(strain[0], min(strain[-1], 1.0), 2001)
    return float(simpson(PchipInterpolator(strain, stress)(x), x=x))


def outputs(x, lb, rk):
    """coilable, sigma_crit (kPa) and energy (kJ/m^3) of one design from the Abaqus results, with the rules of the
    3-d release. Returns also a short status. A coilable design whose Riks run stops before full compression without
    passing 2% gets coilable NaN: the release predicts these labels with a model (resimulation README)."""
    sigma_crit = lb["loads"][0] * 1000.0 / AREA if lb["loads"] else float("nan")
    if not lb["coilable"]:
        return 0.0, sigma_crit, float("nan"), "not coilable (linear buckling)"
    if rk is None:
        return float("nan"), sigma_crit, float("nan"), "Riks failed"
    pitch = x["ratio_pitch"] * D1
    compression = -np.asarray(rk["frame_u3"], float) / pitch
    strain = np.asarray(rk["frame_strain"], float)
    upto_full = np.isfinite(compression) & (compression <= 1.0)
    peak = float(np.nanmax(strain[upto_full])) if upto_full.any() else 0.0
    reached = float(np.nanmax(compression)) if compression.size else 0.0
    energy = float("nan")
    if reached >= FULL:
        energy = _energy(np.abs(np.asarray(rk["U"])) / pitch, np.abs(np.asarray(rk["RF"])) / AREA * 1000.0)
    if peak > STRAIN_LIMIT:
        return 2.0, sigma_crit, energy, f"coils but yields (largest strain {peak:.2%})"
    if reached >= FULL:
        return 1.0, sigma_crit, energy, f"reversibly coilable (largest strain {peak:.2%})"
    return float("nan"), sigma_crit, energy, f"Riks stopped at {reached:.0%} compression, below 2% strain"


class OscarAbaqus(DataGenerator):
    """f3dasm data generator that simulates each open experiment with Abaqus on Oscar (one Slurm job each).

    host        the ssh alias of Oscar in ~/.ssh/config
    remote_dir  folder on Oscar for the jobs (one subfolder per job; your scratch is cleaned after 30 days)
    module      the Abaqus module to load
    partition   the Slurm partition ('batch'; 'debug' often starts sooner, up to 30 minutes)
    timeout     seconds to wait for one job before cancelling it
    """

    def __init__(self, host="oscar-campus", remote_dir="~/scratch/3dasm_lecture21",
                 module="abaqus/2024-mbessa-pskx", partition="batch", timeout=1800):
        self.host, self.remote_dir, self.module = host, remote_dir.rstrip("/"), module
        self.partition, self.timeout = partition, timeout

    # ---------------------------------------------------------------- ssh
    def _ssh(self, command, stdin=None):
        """Run a command on Oscar and return its standard output (Oscar's login messages go to stderr)."""
        r = subprocess.run(["ssh", "-o", "BatchMode=yes", "-o", "ConnectTimeout=15", self.host, command],
                           input=stdin, capture_output=True)
        if r.returncode == 255:
            raise ConnectionError(f"ssh {self.host} failed. Open a terminal, run `ssh {self.host}` once "
                                  f"(on campus or on the VPN), then try again.")
        return r.stdout.decode()

    # ---------------------------------------------------------------- one design
    def execute(self, experiment_sample, **kwargs):
        x = {k: float(experiment_sample.input_data[k])
             for k in ("ratio_d", "ratio_pitch", "ratio_top_diameter", "imperfection")}
        name = f"l21_{time.strftime('%Y%m%dT%H%M%S')}_{os.getpid()}"
        folder = f"{self.remote_dir}/{name}"
        params = {"circular": True, "n_longerons": N_LONG, "young_modulus": E, "bottom_diameter": D1,
                  "n_storeys": 1, "twist_angle": 0.0, "transition_length_ratio": 1.0, "ratio_shear_modulus": G_E,
                  **x}

        # the job folder, sent as one tar archive through ssh
        buffer = io.BytesIO()
        with tarfile.open(fileobj=buffer, mode="w:gz") as tar:
            def add(path, text):
                data = text.encode()
                info = tarfile.TarInfo(path); info.size = len(data)
                tar.addfile(info, io.BytesIO(data))
            add("params.json", json.dumps(params))
            add("job.sh", JOB.format(name=name, partition=self.partition, module=self.module,
                                     walltime=time.strftime("%H:%M:%S", time.gmtime(self.timeout))))
            add("steps.sh", STEPS)
            for step, pre, post in (("lb", LB_PRE, LB_POST), ("rk", RK_PRE, RK_POST)):
                add(f"{step}/{step}_pre.py", pre)
                add(f"{step}/{step}_post.py", post)
            for script in SCRIPTS:
                add(f"scripts/{script}", (HERE / "scripts" / script).read_text())
        out = self._ssh(f"mkdir -p {folder} && tar xzf - -C {folder} && cd {folder} && sbatch --parsable job.sh",
                        stdin=buffer.getvalue())
        job_id = out.strip().split(";")[0]
        if not job_id.isdigit():
            raise RuntimeError(f"sbatch did not return a job id: {out!r}")
        print(f"Submitted Slurm job {job_id} ({name}) for {x}")

        # wait for the job: queued, then running, then done
        t0, last = time.time(), ""
        while True:
            state = self._ssh(f"sacct -n -X -P -j {job_id} -o State 2>/dev/null | head -1").strip() or "PENDING"
            if state != last:
                print(f"  {time.time() - t0:5.0f} s  {state}")
                last = state
            if not state.startswith(("PENDING", "RUNNING", "REQUEUED", "CONFIGURING", "COMPLETING")):
                break
            if time.time() - t0 > self.timeout:
                self._ssh(f"scancel {job_id}")  # only the job submitted here
                raise TimeoutError(f"job {job_id} did not finish in {self.timeout} s and was cancelled")
            time.sleep(10)

        files = json.loads(self._ssh(
            f"cd {folder} && python3 -c \"import json,os; print(json.dumps({{f: open(f).read() for f in "
            f"('lb.json','rk.json','slurm.out','done') if os.path.exists(f)}}))\""))
        if "lb.json" not in files:
            raise RuntimeError(f"linear buckling failed (job {job_id}, state {state}); see {folder} on Oscar:\n"
                               + files.get("slurm.out", ""))
        lb = json.loads(files["lb.json"])
        rk = json.loads(files["rk.json"]) if "rk.json" in files else None
        coilable, sigma_crit, energy, status = outputs(x, lb, rk)
        print(f"  {status}: coilable {coilable}, sigma_crit {sigma_crit:.4g} kPa, energy {energy:.4g} kJ/m^3")
        experiment_sample.store("coilable", coilable)
        experiment_sample.store("sigma_crit", sigma_crit)
        experiment_sample.store("energy", energy)
        return experiment_sample
