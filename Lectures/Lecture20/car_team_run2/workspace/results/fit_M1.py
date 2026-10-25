"""Fit model M1 of the car stopping-distance problem (see PROBLEM_STATEMENT.md)."""
import os

import numpy as np
import pandas as pd
from f3dasm import ExperimentData
from sklearn.model_selection import train_test_split

STUDY = "/Users/harrislab/Documents/GitHub/3dasm_course/Lectures/Lecture20/car_team_run2"
DATA = os.path.join(STUDY, "data", "car_stopping_distance")
OUT = os.path.join(STUDY, "workspace", "results")

exp = ExperimentData.from_file(DATA)
inp, out = exp.to_pandas()
x = inp["x"].to_numpy(dtype=float)
y = out["y"].to_numpy(dtype=float)
n = len(x)

idx = np.arange(n)
tr, te = train_test_split(idx, train_size=0.75, random_state=1987)
n_train, n_test = len(tr), len(te)

X = np.column_stack([x, x**2])
coef, *_ = np.linalg.lstsq(X[tr], y[tr], rcond=None)
a, b = float(coef[0]), float(coef[1])
resid = y[tr] - (a * x[tr] + b * x[tr] ** 2)
s = float(np.std(resid, ddof=0))

mu = a * x[te] + b * x[te] ** 2
yt = y[te]
coverage = float(np.mean(np.abs(yt - mu) <= 1.96 * s))
logpdf = -0.5 * np.log(2 * np.pi * s**2) - (yt - mu) ** 2 / (2 * s**2)
nll = float(-np.mean(logpdf))

row = pd.DataFrame([{
    "model": "M1", "a": a, "b": b, "sd_parameter": s,
    "coverage": coverage, "nll": nll, "n_train": n_train, "n_test": n_test,
}])
os.makedirs(OUT, exist_ok=True)
row.to_csv(os.path.join(OUT, "M1.csv"), index=False)
print(row.to_string(index=False))
print("n rows total:", n, "train:", n_train, "test:", n_test)
