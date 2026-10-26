"""Fit model M2 of the car stopping distance (per PROBLEM_STATEMENT.md).

M2: a, b by lstsq of y/x on columns [1, x] (training rows).
    c = numpy.std of residuals of y/x (ddof=0).
    Predictive mean a*x + b*x**2, predictive sd c*x.
Assessment on test rows: coverage of mean +- 1.96 sd, and nll (mean of -log normal density).
"""

from pathlib import Path

import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split

from f3dasm import ExperimentData

STUDY_DIR = Path(__file__).resolve().parents[2]
DATA_DIR = STUDY_DIR / "data" / "car_stopping_distance"
OUT_CSV = Path(__file__).resolve().parent / "M2.csv"

data = ExperimentData.from_file(str(DATA_DIR))
inp, out = data.to_pandas()
x_all = inp["x"].to_numpy(dtype=float)
y_all = out["y"].to_numpy(dtype=float)
n = len(x_all)

idx_train, idx_test = train_test_split(np.arange(n), train_size=0.75, random_state=1987)
x_tr, y_tr = x_all[idx_train], y_all[idx_train]
x_te, y_te = x_all[idx_test], y_all[idx_test]

# M2 fit: y/x = a + b*x  (columns [1, x]); coef[0] = a (intercept), coef[1] = b (slope)
design_tr = np.column_stack([np.ones_like(x_tr), x_tr])
coef, *_ = np.linalg.lstsq(design_tr, y_tr / x_tr, rcond=None)
a, b = float(coef[0]), float(coef[1])

resid = y_tr / x_tr - (a + b * x_tr)
c = float(np.std(resid, ddof=0))

# Test-row assessment
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
            "n_train": int(len(idx_train)),
            "n_test": int(len(idx_test)),
        }
    ]
)
row.to_csv(OUT_CSV, index=False)

print(row.to_string(index=False))
print(f"wrote {OUT_CSV}")
