"""Fit model M2 of the car stopping distance, as specified in PROBLEM_STATEMENT.md.

M2: a, b by lstsq of y/x on [1, x] (training rows); c = std(residuals of y/x, ddof=0).
Mean a*x + b*x**2, standard deviation c*x.
Assessment on test rows: coverage of mean +- 1.96 sd; nll = mean of -log normal density of y.
"""
from pathlib import Path

import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split

from f3dasm import ExperimentData

STUDY = Path("/Users/harrislab/Documents/GitHub/3dasm_course/Lectures/Lecture20/car_team_run2")
DATA = STUDY / "data" / "car_stopping_distance"
OUT = STUDY / "workspace" / "results" / "M2.csv"

ed = ExperimentData.from_file(project_dir=DATA)
inp = ed.to_pandas()[0]
out = ed.to_pandas()[1]

x_all = inp["x"].to_numpy(dtype=float)
y_all = out["y"].to_numpy(dtype=float)
idx = np.arange(len(x_all))

train_idx, test_idx = train_test_split(idx, train_size=0.75, random_state=1987)
n_train, n_test = len(train_idx), len(test_idx)

x_tr, y_tr = x_all[train_idx], y_all[train_idx]
x_te, y_te = x_all[test_idx], y_all[test_idx]

# M2 coefficients: regress y/x on [1, x]
X_tr = np.column_stack([np.ones_like(x_tr), x_tr])
coef, *_ = np.linalg.lstsq(X_tr, y_tr / x_tr, rcond=None)
b0, b1 = coef  # intercept, slope of y/x on x
# the statement's a, b: a = intercept, b = slope
a, b = float(b0), float(b1)

resid = y_tr / x_tr - (a + b * x_tr)
c = float(np.std(resid, ddof=0))

# Mean a*x + b*x**2 with standard deviation c*x
mu_te = a * x_te + b * x_te**2
sd_te = c * x_te

coverage = float(np.mean(np.abs(y_te - mu_te) <= 1.96 * sd_te))
log_dens = -0.5 * np.log(2 * np.pi) - np.log(sd_te) - 0.5 * ((y_te - mu_te) / sd_te) ** 2
nll = float(np.mean(-log_dens))

OUT.parent.mkdir(parents=True, exist_ok=True)

row = pd.DataFrame([{
    "model": "M2",
    "a": a,
    "b": b,
    "sd_parameter": c,
    "coverage": coverage,
    "nll": nll,
    "n_train": n_train,
    "n_test": n_test,
}])
row.to_csv(OUT, index=False)

print(row.to_string(index=False))
print(f"wrote {OUT}")
