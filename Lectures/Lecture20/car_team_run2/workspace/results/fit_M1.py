import numpy as np
import pandas as pd
from scipy.stats import norm
from sklearn.model_selection import train_test_split
from f3dasm import ExperimentData

STUDY = "/Users/harrislab/Documents/GitHub/3dasm_course/Lectures/Lecture20/car_team_run2"
data = ExperimentData.from_file(project_dir=f"{STUDY}/data/car_stopping_distance")
out = data.to_pandas()
if isinstance(out, tuple):
    inp, outp = out[0], out[1]
else:
    raise RuntimeError("unexpected to_pandas() return")
df = pd.concat([inp.reset_index(drop=True), outp.reset_index(drop=True)], axis=1)
x_all = df["x"].to_numpy(dtype=float)
y_all = df["y"].to_numpy(dtype=float)

idx = np.arange(len(df))
tr, te = train_test_split(idx, train_size=0.75, random_state=1987)
x_tr, y_tr = x_all[tr], y_all[tr]
x_te, y_te = x_all[te], y_all[te]

A = np.column_stack([x_tr, x_tr**2])
(a, b), *_ = np.linalg.lstsq(A, y_tr, rcond=None)
resid = y_tr - (a * x_tr + b * x_tr**2)
s = np.std(resid, ddof=0)

mu_te = a * x_te + b * x_te**2
coverage = float(np.mean(np.abs(y_te - mu_te) <= 1.96 * s))
nll = float(np.mean(-norm.logpdf(y_te, loc=mu_te, scale=s)))

row = pd.DataFrame([{
    "model": "M1", "a": a, "b": b, "sd_parameter": s,
    "coverage": coverage, "nll": nll,
    "n_train": len(tr), "n_test": len(te),
}])
row.to_csv(f"{STUDY}/workspace/results/M1.csv", index=False)
print(row.to_string(index=False))
