"""Fit model M2 of the car stopping distance and assess it on the test rows.

Split: train_test_split(row index, train_size=0.75, random_state=1987).
M2: a, b by numpy.linalg.lstsq of y/x on the columns [1, x] (training rows);
    c = numpy.std of the training residuals of y/x (ddof=0).
    Mean a*x + b*x**2, standard deviation c*x.
Assessment on test rows: coverage of mean +- 1.96 sd; nll = mean of -log normal density of y.
"""
import csv
from pathlib import Path

import numpy as np
from f3dasm import ExperimentData
from sklearn.model_selection import train_test_split

STUDY = Path("/Users/harrislab/Documents/GitHub/3dasm_course/Lectures/Lecture20/car_team_run1")
DATA = STUDY / "data" / "car_stopping_distance"
OUT = STUDY / "workspace" / "results"

ed = ExperimentData.from_file(DATA)
inp_df, out_df = ed.to_pandas()
x_all = inp_df["x"].to_numpy(dtype=float)
y_all = out_df["y"].to_numpy(dtype=float)
assert len(x_all) == len(y_all) == 50
assert np.all(x_all != 0), "M2 divides by x; x must be nonzero"

idx = np.arange(len(x_all))
train_idx, test_idx = train_test_split(idx, train_size=0.75, random_state=1987)
n_train, n_test = len(train_idx), len(test_idx)

x_tr, y_tr = x_all[train_idx], y_all[train_idx]
x_te, y_te = x_all[test_idx], y_all[test_idx]

# M2 fit: y/x ~ a + b*x  (so y ~ a*x + b*x**2)
A = np.column_stack([np.ones_like(x_tr), x_tr])
coef, *_ = np.linalg.lstsq(A, y_tr / x_tr, rcond=None)
a_coef, b_coef = float(coef[0]), float(coef[1])
resid = y_tr / x_tr - A @ coef
c = float(np.std(resid))  # ddof=0

# Assessment on test rows
mean_te = a_coef * x_te + b_coef * x_te**2
sd_te = c * x_te
coverage = float(np.mean(np.abs(y_te - mean_te) <= 1.96 * sd_te))
nll = float(np.mean(0.5 * np.log(2 * np.pi * sd_te**2) + (y_te - mean_te) ** 2 / (2 * sd_te**2)))

row = {
    "model": "M2",
    "a": a_coef,
    "b": b_coef,
    "sd_parameter": c,
    "coverage": coverage,
    "nll": nll,
    "n_train": n_train,
    "n_test": n_test,
}
OUT.mkdir(parents=True, exist_ok=True)
with open(OUT / "M2.csv", "w", newline="") as fh:
    writer = csv.DictWriter(fh, fieldnames=list(row.keys()))
    writer.writeheader()
    writer.writerow(row)

print(row)
