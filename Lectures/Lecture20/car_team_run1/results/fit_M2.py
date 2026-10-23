"""Fit model M2 of the car stopping distance and assess it on the test rows.

M2: mean a*x + b*x**2, standard deviation c*x.
a, b come from least squares of y/x on [1, x] over the training rows;
c is the population std (ddof=0) of the residuals of y/x.
"""

import csv
from pathlib import Path

import numpy as np
from f3dasm import ExperimentData
from sklearn.model_selection import train_test_split

study_dir = Path(__file__).resolve().parent.parent
data_path = study_dir / "data" / "car_stopping_distance"
out_path = study_dir / "results" / "M2.csv"

inputs, outputs = ExperimentData.from_file(data_path).to_pandas()
x = inputs["x"].to_numpy(dtype=float)
y = outputs["y"].to_numpy(dtype=float)

row_index = np.arange(len(x))
train_idx, test_idx = train_test_split(row_index, train_size=0.75, random_state=1987)

x_tr, y_tr = x[train_idx], y[train_idx]
x_te, y_te = x[test_idx], y[test_idx]

# Least squares of y/x on [1, x]: y/x ~ a + b*x, so x*(a + b*x) = a*x + b*x**2
design_tr = np.column_stack([np.ones_like(x_tr), x_tr])
a, b = np.linalg.lstsq(design_tr, y_tr / x_tr, rcond=None)[0]

c = np.std(y_tr / x_tr - (a + b * x_tr), ddof=0)

mean_te = a * x_te + b * x_te**2
sd_te = c * x_te

coverage = np.mean(np.abs(y_te - mean_te) <= 1.96 * sd_te)
nll = np.mean(0.5 * np.log(2 * np.pi) + np.log(sd_te) + 0.5 * ((y_te - mean_te) / sd_te) ** 2)

row = {
    "model": "M2",
    "a": a,
    "b": b,
    "sd_parameter": c,
    "coverage": coverage,
    "nll": nll,
    "n_train": len(train_idx),
    "n_test": len(test_idx),
}

out_path.parent.mkdir(parents=True, exist_ok=True)
with open(out_path, "w", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=list(row))
    writer.writeheader()
    writer.writerow(row)

print(row)
