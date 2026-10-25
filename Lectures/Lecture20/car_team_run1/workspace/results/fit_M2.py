"""Fit model M2 for the car stopping-distance study.

M2: a, b by lstsq of y/x on [1, x] (training rows);
    c = numpy.std of residuals of y/x (ddof=0).
    Mean a*x + b*x**2, standard deviation c*x.
Assessment on test rows: coverage of mean +- 1.96 sd, and mean negative log normal density.
"""

from pathlib import Path

import numpy as np
import pandas as pd
from f3dasm import ExperimentData
from sklearn.model_selection import train_test_split

STUDY = Path("/Users/harrislab/Documents/GitHub/3dasm_course/Lectures/Lecture20/car_team_run1")
DATA = STUDY / "data" / "car_stopping_distance"
OUT = STUDY / "workspace" / "results" / "M2.csv"

ed = ExperimentData.from_file(str(DATA))
inputs, outputs = ed.to_pandas()
x_all = inputs["x"].to_numpy(dtype=float)
y_all = outputs["y"].to_numpy(dtype=float)
assert np.all(x_all > 0), "M2 divides by x; all x must be positive"

idx = np.arange(len(x_all))
idx_train, idx_test = train_test_split(idx, train_size=0.75, random_state=1987)
n_train, n_test = len(idx_train), len(idx_test)
assert (n_train, n_test) == (37, 13), (n_train, n_test)

x_tr, y_tr = x_all[idx_train], y_all[idx_train]
x_te, y_te = x_all[idx_test], y_all[idx_test]

# Fit on training rows: y/x = a + b*x
target = y_tr / x_tr
design = np.column_stack([np.ones_like(x_tr), x_tr])
(a, b), *_ = np.linalg.lstsq(design, target, rcond=None)
c = np.std(target - design @ np.array([a, b]), ddof=0)

# Predictive distribution on test rows
mean_te = a * x_te + b * x_te**2
sd_te = c * x_te

coverage = float(np.mean(np.abs(y_te - mean_te) <= 1.96 * sd_te))
nll = float(np.mean(0.5 * np.log(2 * np.pi) + np.log(sd_te) + 0.5 * ((y_te - mean_te) / sd_te) ** 2))

row = pd.DataFrame(
    [
        {
            "model": "M2",
            "a": float(a),
            "b": float(b),
            "sd_parameter": float(c),
            "coverage": coverage,
            "nll": nll,
            "n_train": n_train,
            "n_test": n_test,
        }
    ]
)
OUT.parent.mkdir(parents=True, exist_ok=True)
row.to_csv(OUT, index=False)
print(row.to_string(index=False))
print(f"wrote {OUT}")
