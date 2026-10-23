"""Fit model M1 for the car stopping distance data and write results/M1.csv."""
from pathlib import Path

import numpy as np
import pandas as pd
from f3dasm import ExperimentData
from scipy.stats import norm
from sklearn.model_selection import train_test_split

STUDY = Path("/Users/harrislab/Documents/GitHub/3dasm_course/Lectures/Lecture20/car_team_run2")
DATA = STUDY / "data" / "car_stopping_distance"
OUT = STUDY / "workspace" / "results" / "M1.csv"

exp = ExperimentData.from_file(DATA)
input_df, output_df = exp.to_pandas()
x = input_df["x"].to_numpy(dtype=float)
y = output_df["y"].to_numpy(dtype=float)

idx = np.arange(len(x))
train_idx, test_idx = train_test_split(idx, train_size=0.75, random_state=1987)
n_train, n_test = len(train_idx), len(test_idx)

# M1: least squares on [x, x**2], no intercept
X_train = np.column_stack([x[train_idx], x[train_idx] ** 2])
(a, b), *_ = np.linalg.lstsq(X_train, y[train_idx], rcond=None)
resid_train = y[train_idx] - (a * x[train_idx] + b * x[train_idx] ** 2)
s = np.std(resid_train, ddof=0)

# Assessment on test rows
xt, yt = x[test_idx], y[test_idx]
mean_t = a * xt + b * xt ** 2
sd_t = s
coverage = np.mean(np.abs(yt - mean_t) <= 1.96 * sd_t)
nll = np.mean(-norm.logpdf(yt, loc=mean_t, scale=sd_t))

OUT.parent.mkdir(parents=True, exist_ok=True)
row = pd.DataFrame([{
    "model": "M1", "a": a, "b": b, "sd_parameter": s,
    "coverage": coverage, "nll": nll, "n_train": n_train, "n_test": n_test,
}])
row.to_csv(OUT, index=False)
print(row.to_string(index=False))
