"""Fit model M1 for the car stopping-distance data and assess it on held-out rows.

M1: mean = a*x + b*x**2 (no intercept, fit by least squares on training rows),
    standard deviation = s = numpy.std(training residuals, ddof=0).
Assessment on test rows: coverage of mean +- 1.96*sd, and mean negative log normal density.
"""
import os
import numpy as np
import pandas as pd
from scipy.stats import norm
from sklearn.model_selection import train_test_split
from f3dasm import ExperimentData

STUDY = "/Users/harrislab/Documents/GitHub/3dasm_course/Lectures/Lecture20/car_team_run1"
DATA = os.path.join(STUDY, "data", "car_stopping_distance")
OUT_DIR = os.path.join(STUDY, "workspace", "results")

inp, outp = ExperimentData.from_file(DATA).to_pandas()
x_all = inp["x"].to_numpy(dtype=float)
y_all = outp["y"].to_numpy(dtype=float)

idx = np.arange(len(x_all))
train_idx, test_idx = train_test_split(idx, train_size=0.75, random_state=1987)

x_tr, y_tr = x_all[train_idx], y_all[train_idx]
x_te, y_te = x_all[test_idx], y_all[test_idx]

# Least squares of y on [x, x**2], no intercept
X_tr = np.column_stack([x_tr, x_tr ** 2])
(a, b), *_ = np.linalg.lstsq(X_tr, y_tr, rcond=None)

resid_tr = y_tr - (a * x_tr + b * x_tr ** 2)
s = float(np.std(resid_tr, ddof=0))

mu_te = a * x_te + b * x_te ** 2
sd_te = np.full_like(mu_te, s)

lower = mu_te - 1.96 * sd_te
upper = mu_te + 1.96 * sd_te
coverage = float(np.mean((y_te >= lower) & (y_te <= upper)))
nll = float(np.mean(-norm.logpdf(y_te, loc=mu_te, scale=sd_te)))

row = {
    "model": "M1",
    "a": float(a),
    "b": float(b),
    "sd_parameter": s,
    "coverage": coverage,
    "nll": nll,
    "n_train": int(len(train_idx)),
    "n_test": int(len(test_idx)),
}

os.makedirs(OUT_DIR, exist_ok=True)
pd.DataFrame([row], columns=["model", "a", "b", "sd_parameter", "coverage", "nll", "n_train", "n_test"]).to_csv(
    os.path.join(OUT_DIR, "M1.csv"), index=False
)
print(pd.DataFrame([row]).to_string(index=False))
