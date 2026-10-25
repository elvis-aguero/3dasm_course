"""Fit model M1 of the car stopping distance per PROBLEM_STATEMENT.md.

M1: mean = a*x + b*x**2 (least squares on [x, x**2], no intercept), sd = s
(numpy.std of training residuals, ddof=0). Assessed on the 13 test rows.
"""
import os
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from f3dasm import ExperimentData

STUDY = "/Users/harrislab/Documents/GitHub/3dasm_course/Lectures/Lecture20/car_team_run1"
DATA = os.path.join(STUDY, "data", "car_stopping_distance")
OUT_DIR = os.path.join(STUDY, "workspace", "results")

inp, out = ExperimentData.from_file(DATA).to_pandas()
x = inp["x"].to_numpy(dtype=float)
y = out["y"].to_numpy(dtype=float)
n = len(x)

idx_train, idx_test = train_test_split(np.arange(n), train_size=0.75, random_state=1987)
x_tr, y_tr = x[idx_train], y[idx_train]
x_te, y_te = x[idx_test], y[idx_test]

A = np.column_stack([x_tr, x_tr ** 2])
(a, b), *_ = np.linalg.lstsq(A, y_tr, rcond=None)
resid = y_tr - (a * x_tr + b * x_tr ** 2)
s = np.std(resid)  # ddof=0

mu_te = a * x_te + b * x_te ** 2
coverage = np.mean(np.abs(y_te - mu_te) <= 1.96 * s)
nll = np.mean(0.5 * np.log(2 * np.pi * s ** 2) + (y_te - mu_te) ** 2 / (2 * s ** 2))

row = pd.DataFrame([{
    "model": "M1", "a": a, "b": b, "sd_parameter": s,
    "coverage": coverage, "nll": nll,
    "n_train": len(idx_train), "n_test": len(idx_test),
}])
os.makedirs(OUT_DIR, exist_ok=True)
row.to_csv(os.path.join(OUT_DIR, "M1.csv"), index=False)
print(row.to_string(index=False))
