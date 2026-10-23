"""Fit model M1 (no-intercept quadratic mean, constant sd) to the car stopping distance data.

M1: mean = a*x + b*x**2, sd = s (constant), with a, b from least squares on the training rows
and s the population std (ddof=0) of the training residuals.
"""

from pathlib import Path

import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split

from f3dasm import ExperimentData

STUDY = Path(__file__).resolve().parent.parent
DATA = STUDY / "data" / "car_stopping_distance"
OUT = Path(__file__).resolve().parent / "M1.csv"

# Load data
data = ExperimentData.from_file(str(DATA))
input_df, output_df = data.to_pandas()
x_all = input_df["x"].to_numpy(dtype=float)
y_all = output_df["y"].to_numpy(dtype=float)

# Split (row index)
idx = np.arange(len(x_all))
idx_train, idx_test = train_test_split(idx, train_size=0.75, random_state=1987)

x_tr, y_tr = x_all[idx_train], y_all[idx_train]
x_te, y_te = x_all[idx_test], y_all[idx_test]

# Fit a, b by least squares of y on [x, x**2], no intercept
X_tr = np.column_stack([x_tr, x_tr**2])
(a, b), *_ = np.linalg.lstsq(X_tr, y_tr, rcond=None)

# Constant sd from training residuals (ddof=0)
resid_tr = y_tr - (a * x_tr + b * x_tr**2)
s = np.std(resid_tr)

# Assess on test rows
mu_te = a * x_te + b * x_te**2
coverage = np.mean(np.abs(y_te - mu_te) <= 1.96 * s)
nll = np.mean(0.5 * np.log(2 * np.pi * s**2) + 0.5 * ((y_te - mu_te) / s) ** 2)

row = pd.DataFrame(
    [
        {
            "model": "M1",
            "a": a,
            "b": b,
            "sd_parameter": s,
            "coverage": coverage,
            "nll": nll,
            "n_train": len(idx_train),
            "n_test": len(idx_test),
        }
    ]
)
row.to_csv(OUT, index=False)
print(row.to_string(index=False))
print(f"wrote {OUT}")
