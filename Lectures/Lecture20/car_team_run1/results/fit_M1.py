"""Fit model M1 (quadratic mean without intercept, constant sd) to the car stopping-distance data."""
import csv
import os

import numpy as np
from sklearn.model_selection import train_test_split
from f3dasm import ExperimentData

HERE = os.path.dirname(os.path.abspath(__file__))
STUDY = os.path.dirname(HERE)
DATA = os.path.join(STUDY, "data", "car_stopping_distance")
OUT = os.path.join(HERE, "M1.csv")

exp = ExperimentData.from_file(DATA)
df_in, df_out = exp.to_pandas()
x_all = np.asarray(df_in["x"], dtype=float)
y_all = np.asarray(df_out["y"], dtype=float)

idx = np.arange(len(x_all))
train_idx, test_idx = train_test_split(idx, train_size=0.75, random_state=1987)
x_tr, y_tr = x_all[train_idx], y_all[train_idx]
x_te, y_te = x_all[test_idx], y_all[test_idx]

X_tr = np.column_stack([x_tr, x_tr ** 2])
(a, b), *_ = np.linalg.lstsq(X_tr, y_tr, rcond=None)
resid = y_tr - (a * x_tr + b * x_tr ** 2)
s = np.std(resid, ddof=0)

mu_te = a * x_te + b * x_te ** 2
coverage = np.mean(np.abs(y_te - mu_te) <= 1.96 * s)
nll = np.mean(0.5 * np.log(2 * np.pi * s ** 2) + (y_te - mu_te) ** 2 / (2 * s ** 2))

row = {
    "model": "M1", "a": a, "b": b, "sd_parameter": s,
    "coverage": coverage, "nll": nll,
    "n_train": len(train_idx), "n_test": len(test_idx),
}
with open(OUT, "w", newline="") as f:
    w = csv.DictWriter(f, fieldnames=list(row.keys()))
    w.writeheader()
    w.writerow(row)
print(row)
