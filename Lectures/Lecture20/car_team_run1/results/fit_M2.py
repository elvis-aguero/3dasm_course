"""Fit model M2 of the car stopping-distance study and write results/M2.csv.

M2: a, b by lstsq of y/x on [1, x] (training rows); c = std (ddof=0) of the
residuals of y/x. Mean a*x + b*x**2, sd c*x. Assessed on the test rows.
"""
from pathlib import Path

import numpy as np
from sklearn.model_selection import train_test_split
from f3dasm import ExperimentData

STUDY = Path(__file__).resolve().parent.parent
DATA = STUDY / "data" / "car_stopping_distance"
OUT = STUDY / "results" / "M2.csv"

exp = ExperimentData.from_file(DATA)
inp = exp.to_pandas()[0]
out = exp.to_pandas()[1]
x = np.asarray(inp["x"], dtype=float).ravel()
y = np.asarray(out["y"], dtype=float).ravel()
assert len(x) == len(y) == 50

idx = np.arange(len(x))
train_idx, test_idx = train_test_split(idx, train_size=0.75, random_state=1987)
n_train, n_test = len(train_idx), len(test_idx)

xtr, ytr = x[train_idx], y[train_idx]
xte, yte = x[test_idx], y[test_idx]

# M2 fit on training rows
A = np.column_stack([np.ones_like(xtr), xtr])
coef, *_ = np.linalg.lstsq(A, ytr / xtr, rcond=None)
a, b = float(coef[0]), float(coef[1])
resid = ytr / xtr - (a + b * xtr)
c = float(np.std(resid, ddof=0))

# Predictive distribution on test rows
mu = a * xte + b * xte**2
sd = c * xte
coverage = float(np.mean(np.abs(yte - mu) <= 1.96 * sd))
logpdf = -0.5 * np.log(2 * np.pi * sd**2) - 0.5 * ((yte - mu) / sd) ** 2
nll = float(np.mean(-logpdf))

OUT.parent.mkdir(parents=True, exist_ok=True)
header = "model,a,b,sd_parameter,coverage,nll,n_train,n_test"
row = f"M2,{a!r},{b!r},{c!r},{coverage!r},{nll!r},{n_train},{n_test}"
OUT.write_text(header + "\n" + row + "\n")
print(header)
print(row)
