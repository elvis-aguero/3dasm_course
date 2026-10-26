"""Fit model M1 for the car stopping distance problem (see PROBLEM_STATEMENT.md).

M1: a, b by least squares of y on [x, x**2] (no intercept), training rows.
s = numpy.std of training residuals (ddof=0). Predictive mean a*x + b*x**2, sd s.
Assessment on test rows: coverage of mean +- 1.96 sd, and mean negative log normal density.
"""
import os

import numpy as np
from sklearn.model_selection import train_test_split
from f3dasm import ExperimentData

STUDY = "/Users/harrislab/Documents/GitHub/3dasm_course/Lectures/Lecture20/car_team_run1"
DATA = os.path.join(STUDY, "data", "car_stopping_distance")
OUT_DIR = os.path.join(STUDY, "workspace", "results")

data = ExperimentData.from_file(DATA)
inp, out = data.to_pandas()  # (input table, output table)

x = inp["x"].to_numpy(dtype=float)
y = out["y"].to_numpy(dtype=float)
n = len(x)
assert n == 50, f"expected 50 stops, got {n}"

idx = np.arange(n)
train_idx, test_idx = train_test_split(idx, train_size=0.75, random_state=1987)
assert len(train_idx) == 37 and len(test_idx) == 13

x_tr, y_tr = x[train_idx], y[train_idx]
x_te, y_te = x[test_idx], y[test_idx]

# Fit a, b by least squares of y on [x, x^2], no intercept
X_tr = np.column_stack([x_tr, x_tr ** 2])
(a, b), *_ = np.linalg.lstsq(X_tr, y_tr, rcond=None)

resid_tr = y_tr - (a * x_tr + b * x_tr ** 2)
s = np.std(resid_tr)  # ddof=0

mu_te = a * x_te + b * x_te ** 2
sd_te = np.full_like(mu_te, s)

coverage = float(np.mean(np.abs(y_te - mu_te) <= 1.96 * sd_te))
nll = float(np.mean(0.5 * np.log(2 * np.pi * sd_te ** 2) + 0.5 * ((y_te - mu_te) / sd_te) ** 2))

row = {
    "model": "M1",
    "a": float(a),
    "b": float(b),
    "sd_parameter": float(s),
    "coverage": coverage,
    "nll": nll,
    "n_train": int(len(train_idx)),
    "n_test": int(len(test_idx)),
}

if __name__ == "__main__":
    import pandas as pd

    os.makedirs(OUT_DIR, exist_ok=True)
    pd.DataFrame([row], columns=list(row.keys())).to_csv(os.path.join(OUT_DIR, "M1.csv"), index=False)
    for k, v in row.items():
        print(f"{k}: {v}")
