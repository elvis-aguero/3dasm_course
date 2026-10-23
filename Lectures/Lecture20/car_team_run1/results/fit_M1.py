"""Fit model M1 of the car stopping distance and assess it on the test rows.

M1: y ~ a*x + b*x**2 (no intercept), Gaussian noise with sd s.
"""

from pathlib import Path

import numpy as np
import pandas as pd
from f3dasm import ExperimentData
from sklearn.model_selection import train_test_split

STUDY_DIR = Path(__file__).resolve().parent.parent
RESULTS_DIR = STUDY_DIR / "results"

# Data
experiment_data = ExperimentData.from_file(str(STUDY_DIR / "data" / "car_stopping_distance"))
input_df, output_df = experiment_data.to_pandas()
x = input_df["x"].to_numpy(dtype=float)
y = output_df["y"].to_numpy(dtype=float)

# Split
row_index = np.arange(len(x))
train_idx, test_idx = train_test_split(row_index, train_size=0.75, random_state=1987)
x_train, y_train = x[train_idx], y[train_idx]
x_test, y_test = x[test_idx], y[test_idx]

# Fit M1 on the training rows
design_train = np.column_stack([x_train, x_train**2])
(a, b), *_ = np.linalg.lstsq(design_train, y_train, rcond=None)
residuals_train = y_train - (a * x_train + b * x_train**2)
s = np.std(residuals_train)  # ddof=0

# Assess on the test rows
mean_test = a * x_test + b * x_test**2
coverage = np.mean(np.abs(y_test - mean_test) <= 1.96 * s)
log_density = -0.5 * np.log(2 * np.pi * s**2) - (y_test - mean_test) ** 2 / (2 * s**2)
nll = np.mean(-log_density)

row = {
    "model": "M1",
    "a": a,
    "b": b,
    "sd_parameter": s,
    "coverage": coverage,
    "nll": nll,
    "n_train": len(train_idx),
    "n_test": len(test_idx),
}

RESULTS_DIR.mkdir(parents=True, exist_ok=True)
pd.DataFrame([row]).to_csv(RESULTS_DIR / "M1.csv", index=False)
print(pd.DataFrame([row]).to_string(index=False))
