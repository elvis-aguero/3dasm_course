"""Fit model M2 of the car stopping-distance problem and write M2.csv.

M2: a, b = lstsq of y/x on [1, x] (training rows); c = std(residuals of y/x, ddof=0).
Mean a*x + b*x**2, standard deviation c*x. Assessed on the test rows.
"""
from pathlib import Path

import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from f3dasm import ExperimentData

STUDY = Path("/Users/harrislab/Documents/GitHub/3dasm_course/Lectures/Lecture20/car_team_run1")
DATA = STUDY / "data" / "car_stopping_distance"
OUT_DIR = STUDY / "workspace" / "results"

exp = ExperimentData.from_file(DATA)
inp = exp.to_pandas()
input_df, output_df = inp[0], inp[1]
x_all = np.asarray(input_df["x"], dtype=float).ravel()
y_all = np.asarray(output_df["y"], dtype=float).ravel()
n = len(x_all)

idx = np.arange(n)
train_idx, test_idx = train_test_split(idx, train_size=0.75, random_state=1987)
x_tr, y_tr = x_all[train_idx], y_all[train_idx]
x_te, y_te = x_all[test_idx], y_all[test_idx]
n_train, n_test = len(train_idx), len(test_idx)

# Fit a, b: regress y/x on [1, x] over training rows
A = np.column_stack([np.ones_like(x_tr), x_tr])
coef, *_ = np.linalg.lstsq(A, y_tr / x_tr, rcond=None)
# The mean formula of the problem statement uses a*x + b*x**2
a, b = float(coef[0]), float(coef[1])
# c: std (ddof=0) of training residuals of y/x around the fitted regression on [1, x]
resid_ratio = y_tr / x_tr - A @ coef
c = float(np.std(resid_ratio, ddof=0))

# Assessment on test rows
mu_te = a * x_te + b * x_te**2
sd_te = c * x_te
coverage = float(np.mean(np.abs(y_te - mu_te) <= 1.96 * sd_te))
nll = float(np.mean(0.5 * np.log(2 * np.pi) + np.log(sd_te) + 0.5 * ((y_te - mu_te) / sd_te) ** 2))

row = pd.DataFrame([{
    "model": "M2", "a": a, "b": b, "sd_parameter": c,
    "coverage": coverage, "nll": nll, "n_train": n_train, "n_test": n_test,
}])
OUT_DIR.mkdir(parents=True, exist_ok=True)
row.to_csv(OUT_DIR / "M2.csv", index=False)
print(row.to_string(index=False))
