"""Fit model M2 of the car stopping distance and write results/M2.csv.

M2: a, b by lstsq of y/x on [1, x] (training rows); c = std (ddof=0) of the
residuals of y/x. Mean a*x + b*x**2, standard deviation c*x.
"""
from pathlib import Path

import numpy as np
import pandas as pd
from scipy.stats import norm  # noqa: F401  (kept for clarity; density computed explicitly below)
from sklearn.model_selection import train_test_split
from f3dasm import ExperimentData

STUDY = Path(__file__).resolve().parent.parent
DATA = STUDY / "data" / "car_stopping_distance"
OUT = Path(__file__).resolve().parent / "M2.csv"

ed = ExperimentData.from_file(str(DATA))
input_df = ed.to_pandas()[0]
output_df = ed.to_pandas()[1]
x_all = np.asarray(input_df["x"], dtype=float).ravel()
y_all = np.asarray(output_df["y"], dtype=float).ravel()
assert len(x_all) == len(y_all) == 50, (len(x_all), len(y_all))

idx = np.arange(len(x_all))
train_idx, test_idx = train_test_split(idx, train_size=0.75, random_state=1987)
assert len(train_idx) == 37 and len(test_idx) == 13

x_tr, y_tr = x_all[train_idx], y_all[train_idx]
x_te, y_te = x_all[test_idx], y_all[test_idx]

# M2 fit: y/x regressed on [1, x]
A_tr = np.column_stack([np.ones_like(x_tr), x_tr])
coef, *_ = np.linalg.lstsq(A_tr, y_tr / x_tr, rcond=None)
a, b = float(coef[0]), float(coef[1])
resid = y_tr / x_tr - A_tr @ coef
c = float(np.std(resid))  # ddof=0

# Test-set assessment
mu = a * x_te + b * x_te**2
sd = c * x_te
coverage = float(np.mean((y_te >= mu - 1.96 * sd) & (y_te <= mu + 1.96 * sd)))
log_dens = -0.5 * np.log(2 * np.pi) - np.log(sd) - 0.5 * ((y_te - mu) / sd) ** 2
nll = float(np.mean(-log_dens))

row = pd.DataFrame(
    [{
        "model": "M2",
        "a": a,
        "b": b,
        "sd_parameter": c,
        "coverage": coverage,
        "nll": nll,
        "n_train": int(len(train_idx)),
        "n_test": int(len(test_idx)),
    }]
)
row.to_csv(OUT, index=False)
print(row.to_string(index=False))
print("wrote", OUT)
