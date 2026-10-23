"""Fit model M2 of the car stopping distance and assess it on held-out rows.

M2: a, b by lstsq of y/x on [1, x] (training rows); c = std of residuals of y/x (ddof=0);
mean = a*x + b*x**2; sd = c*x. Assessment on test rows: coverage of mean +- 1.96 sd, and
nll = mean of -log normal density of y.
"""

import csv
import os

import numpy as np
from sklearn.model_selection import train_test_split

from f3dasm import ExperimentData

HERE = os.path.dirname(os.path.abspath(__file__))
STUDY = os.path.abspath(os.path.join(HERE, "..", ".."))
DATA = os.path.join(STUDY, "data", "car_stopping_distance")
OUT = os.path.join(HERE, "M2.csv")

exp = ExperimentData.from_file(DATA)
inp, out = exp.to_pandas()  # (input table with x, output table with y)

x = np.asarray(inp["x"], dtype=float).ravel()
y = np.asarray(out["y"], dtype=float).ravel()
assert x.shape == y.shape and x.size == 50, (x.shape, y.shape)

idx = np.arange(x.size)
train_idx, test_idx = train_test_split(idx, train_size=0.75, random_state=1987)
assert len(train_idx) == 37 and len(test_idx) == 13, (len(train_idx), len(test_idx))

xtr, ytr = x[train_idx], y[train_idx]
xte, yte = x[test_idx], y[test_idx]

# a, b: least squares of y/x on [1, x]
A_tr = np.column_stack([np.ones_like(xtr), xtr])
coef, *_ = np.linalg.lstsq(A_tr, ytr / xtr, rcond=None)
a, b = float(coef[0]), float(coef[1])

# c: std (ddof=0) of training residuals of y/x
resid_ratio = ytr / xtr - A_tr @ coef
c = float(np.std(resid_ratio, ddof=0))

# Predictive distribution on test rows (as specified: mean uses the a, b of the y/x fit)
mean_te = a * xte + b * xte**2
sd_te = c * xte

coverage = float(np.mean(np.abs(yte - mean_te) <= 1.96 * sd_te))
log_density = -0.5 * np.log(2 * np.pi) - np.log(sd_te) - 0.5 * ((yte - mean_te) / sd_te) ** 2
nll = float(np.mean(-log_density))

row = {
    "model": "M2",
    "a": a,
    "b": b,
    "sd_parameter": c,
    "coverage": coverage,
    "nll": nll,
    "n_train": int(len(train_idx)),
    "n_test": int(len(test_idx)),
}

with open(OUT, "w", newline="") as fh:
    writer = csv.DictWriter(fh, fieldnames=list(row.keys()))
    writer.writeheader()
    writer.writerow(row)

for k, v in row.items():
    print(f"{k}={v}")
print("wrote", OUT)
