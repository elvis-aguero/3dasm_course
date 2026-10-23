"""Fit model M2 of the car stopping distance and assess it on held-out rows.

M2: a, b from least squares of y/x on [1, x] (training rows);
    c = std of the residuals of y/x (ddof=0).
    Mean a*x + b*x**2, standard deviation c*x.
"""

from pathlib import Path

import numpy as np
import pandas as pd
from f3dasm import ExperimentData
from sklearn.model_selection import train_test_split

STUDY = Path(__file__).resolve().parent.parent
DATA = STUDY / "data" / "car_stopping_distance"
OUT = STUDY / "results" / "M2.csv"

# Load the data
inputs, outputs = ExperimentData.from_file(str(DATA)).to_pandas()
x_all = inputs["x"].to_numpy(dtype=float)
y_all = outputs["y"].to_numpy(dtype=float)
n = len(x_all)

# Split on the row index
train_idx, test_idx = train_test_split(
    np.arange(n), train_size=0.75, random_state=1987
)
x_tr, y_tr = x_all[train_idx], y_all[train_idx]
x_te, y_te = x_all[test_idx], y_all[test_idx]

# Fit M2: regress y/x on [1, x]
design_tr = np.column_stack([np.ones_like(x_tr), x_tr])
coef, *_ = np.linalg.lstsq(design_tr, y_tr / x_tr, rcond=None)
a, b = coef
c = np.std((y_tr / x_tr) - design_tr @ coef, ddof=0)

# Assess on the test rows
mean_te = a * x_te + b * x_te**2
sd_te = c * x_te
coverage = np.mean(np.abs(y_te - mean_te) <= 1.96 * sd_te)
log_density = -0.5 * np.log(2 * np.pi) - np.log(sd_te) - 0.5 * ((y_te - mean_te) / sd_te) ** 2
nll = np.mean(-log_density)

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
    ]
)
OUT.parent.mkdir(parents=True, exist_ok=True)
row.to_csv(OUT, index=False)

print(row.to_string(index=False))
print(f"wrote {OUT}")
