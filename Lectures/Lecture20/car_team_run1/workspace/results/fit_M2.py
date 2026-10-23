"""Fit model M2 for the car stopping-distance study (see PROBLEM_STATEMENT.md).

M2: a, b by least squares of y/x on [1, x] (training rows); c = std(residuals of y/x, ddof=0).
Mean a*x + b*x**2, standard deviation c*x.
Assessment on test rows: coverage of mean +- 1.96 sd, and mean negative log normal density.
"""
from pathlib import Path

import numpy as np
import pandas as pd
from f3dasm import ExperimentData
from sklearn.model_selection import train_test_split

HERE = Path(__file__).resolve().parent
STUDY = HERE.parent.parent
DATA = STUDY / "data" / "car_stopping_distance"
OUT = HERE / "M2.csv"

ed = ExperimentData.from_file(str(DATA))
x_df, y_df = ed.to_pandas()
x = x_df["x"].to_numpy(dtype=float)
y = y_df["y"].to_numpy(dtype=float)
assert len(x) == 50 and len(y) == 50, "expected 50 stops"
assert np.all(x > 0), "y/x requires x > 0"

idx = np.arange(len(x))
train_idx, test_idx = train_test_split(idx, train_size=0.75, random_state=1987)
assert len(train_idx) == 37 and len(test_idx) == 13

x_tr, y_tr = x[train_idx], y[train_idx]
x_te, y_te = x[test_idx], y[test_idx]

# M2 fit: regress y/x on [1, x]; coefficient order is (intercept, slope) -> (a, b)
design_tr = np.column_stack([np.ones_like(x_tr), x_tr])
coef, *_ = np.linalg.lstsq(design_tr, y_tr / x_tr, rcond=None)
a, b = float(coef[0]), float(coef[1])

resid_tr = y_tr / x_tr - (a + b * x_tr)
c = float(np.std(resid_tr, ddof=0))

# Test-set assessment with per-point mean a*x + b*x**2 and sd c*x
mu_te = a * x_te + b * x_te**2
sd_te = c * x_te
coverage = float(np.mean(np.abs(y_te - mu_te) <= 1.96 * sd_te))
log_density = -0.5 * np.log(2.0 * np.pi * sd_te**2) - 0.5 * ((y_te - mu_te) / sd_te) ** 2
nll = float(-np.mean(log_density))

row = pd.DataFrame(
    [
        {
            "model": "M2",
            "a": a,
            "b": b,
            "sd_parameter": c,
            "coverage": coverage,
            "nll": nll,
            "n_train": len(train_idx),
            "n_test": len(test_idx),
        }
    ],
    columns=["model", "a", "b", "sd_parameter", "coverage", "nll", "n_train", "n_test"],
)
row.to_csv(OUT, index=False)

print(row.to_string(index=False))
print(f"wrote {OUT}")
