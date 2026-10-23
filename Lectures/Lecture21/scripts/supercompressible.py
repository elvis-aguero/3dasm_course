"""The two Abaqus analyses of one supercompressible design, as in the datasets of the Final Project.

    files = job_files(x)          # the files of one job: the four scripts of this folder, small wrappers, steps.sh
    ... run `bash steps.sh` where Abaqus is installed (for example with oscar_helper.Oscar) ...
    outputs(x, folder)            # {"coilable", "sigma_crit", "energy"} from the results in that folder

x holds `ratio_d`, `ratio_pitch`, `ratio_top_diameter` (the 3-d problem, circular longerons) and `imperfection`, the
amplitude a in mm of the first-mode imperfection of the Riks run.

steps.sh runs, in the folder `lb/`, the linear buckling analysis and its post-processing, then, if the design is
coilable, the Riks analysis and its post-processing in `rk/`. Every file of Abaqus is kept: the models (`.cae`), the
input files (`.inp`) and the results (`.odb`), which Abaqus/CAE opens. The labels and the energy are computed by
`outputs` with numpy and scipy, with the rules of the 3-d release.
"""
import json
import math
from pathlib import Path

import numpy as np
from scipy.integrate import simpson
from scipy.interpolate import PchipInterpolator

HERE = Path(__file__).resolve().parent
SCRIPTS = ["supercompressible_lin_buckle.py", "supercompressible_lin_buckle_pp.py",
           "riks_b31_nocontact.py", "riks_pp_frames.py"]

# Constants of the 3-d datasets (Final Project statement, Bessa et al. 2019)
D1, E, N_LONG, G_E = 100.0, 3500.0, 3, 0.3677
AREA = math.pi * D1 ** 2 / 4.0          # bottom ring, mm^2
FULL, STRAIN_LIMIT = 0.90, 0.02         # "fully coiled" compression, largest strain of a reversible design

# Wrappers, run by Abaqus in the step folder (lb/ or rk/). After building a model, each saves it as a .cae file.
LB_PRE = """import json, sys
sys.path.insert(0, '../scripts')
from supercompressible_lin_buckle import main
main(json.load(open('../params.json')))
try:
    from abaqus import mdb
    mdb.saveAs(pathName='lin_buckle.cae')
except Exception as e:
    print('could not save the .cae file:', e)
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
try:
    from abaqus import mdb
    mdb.saveAs(pathName='riks.cae')
except Exception as e:
    print('could not save the .cae file:', e)
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
rm -f */*.rpy* */*.rec */*.lck  # Abaqus journals and locks only
"""


def job_files(x):
    """The files of one job: {path in the job folder: text}."""
    x = {k: float(x[k]) for k in ("ratio_d", "ratio_pitch", "ratio_top_diameter", "imperfection")}
    params = {"circular": True, "n_longerons": N_LONG, "young_modulus": E, "bottom_diameter": D1,
              "n_storeys": 1, "twist_angle": 0.0, "transition_length_ratio": 1.0, "ratio_shear_modulus": G_E, **x}
    files = {"params.json": json.dumps(params), "steps.sh": STEPS,
             "lb/lb_pre.py": LB_PRE, "lb/lb_post.py": LB_POST, "rk/rk_pre.py": RK_PRE, "rk/rk_post.py": RK_POST}
    files.update({f"scripts/{s}": (HERE / s).read_text() for s in SCRIPTS})
    return files


def _energy(strain, stress):
    """Area under the stress-strain curve up to full compression: PCHIP, then Simpson (as the release).
    Points where the strain does not increase are dropped, because the interpolation needs increasing strains."""
    k = np.r_[True, np.diff(strain) > 1e-12]; strain, stress = strain[k], stress[k]
    k = np.maximum.accumulate(strain) == strain; strain, stress = strain[k], stress[k]
    x = np.linspace(strain[0], min(strain[-1], 1.0), 2001)
    return float(simpson(PchipInterpolator(strain, stress)(x), x=x))


def outputs(x, folder):
    """coilable, sigma_crit (kPa) and energy (kJ/m^3) of one design, from the results in `folder`, with the rules of
    the 3-d release. A coilable design whose Riks run stops before full compression without passing 2% gets coilable
    NaN, because the release predicts these labels with a model (see its README)."""
    folder = Path(folder)
    if not (folder / "lb.json").exists():
        raise RuntimeError(f"linear buckling failed; see the logs in {folder / 'lb'}")
    lb = json.loads((folder / "lb.json").read_text())
    rk = json.loads((folder / "rk.json").read_text()) if (folder / "rk.json").exists() else None
    nan = float("nan")
    sigma_crit = lb["loads"][0] * 1000.0 / AREA if lb["loads"] else nan
    if not lb["coilable"]:
        return {"coilable": 0.0, "sigma_crit": sigma_crit, "energy": nan}
    if rk is None:
        return {"coilable": nan, "sigma_crit": sigma_crit, "energy": nan}
    pitch = float(x["ratio_pitch"]) * D1
    compression = -np.asarray(rk["frame_u3"], float) / pitch
    strain = np.asarray(rk["frame_strain"], float)
    upto_full = np.isfinite(compression) & (compression <= 1.0)
    peak = float(np.nanmax(strain[upto_full])) if upto_full.any() else 0.0
    reached = float(np.nanmax(compression)) if compression.size else 0.0
    energy = nan
    if reached >= FULL:
        energy = _energy(np.abs(np.asarray(rk["U"])) / pitch, np.abs(np.asarray(rk["RF"])) / AREA * 1000.0)
    coilable = 2.0 if peak > STRAIN_LIMIT else (1.0 if reached >= FULL else nan)
    return {"coilable": coilable, "sigma_crit": sigma_crit, "energy": energy}
