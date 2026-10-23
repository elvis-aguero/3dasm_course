"""Fit model M1 (mean a*x + b*x**2, constant sd s) to the car stopping-distance data."""
import os

import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from f3dasm import ExperimentData

STUDY = "/Users/harrislab/Documents/GitHub/3dasm_course/Lectures/Lecture20/car_team_run1"
DATA = os.path.join(STUDY, "data", "car_stopping_distance")
OUT = os.path.join(STUDY, "workspace", "results")


def main():
    ed = ExperimentData.from_file(DATA)
    inp = ed.to_pandas()[0]
    out = ed.to_pandas()[1]
    x = np.asarray(inp["x"], dtype=float).ravel()
    y = np.asarray(out["y"], dtype=float).ravel()
    assert len(x) == len(y) == 50, (len(x), len(y))

    idx = np.arange(len(x))
    idx_train, idx_test = train_test_split(idx, train_size=0.75, random_state=1987)
    assert len(idx_train) == 37 and len(idx_test) == 13

    xtr, ytr = x[idx_train], y[idx_train]
    xte, yte = x[idx_test], y[idx_test]

    A = np.column_stack([xtr, xtr ** 2])
    (a, b), *_ = np.linalg.lstsq(A, ytr, rcond=None)
    resid = ytr - (a * xtr + b * xtr ** 2)
    s = float(np.std(resid, ddof=0))

    mu = a * xte + b * xte ** 2
    coverage = float(np.mean(np.abs(yte - mu) <= 1.96 * s))
    nll = float(np.mean(0.5 * np.log(2 * np.pi * s ** 2) + 0.5 * ((yte - mu) / s) ** 2))

    row = pd.DataFrame([{
        "model": "M1", "a": float(a), "b": float(b), "sd_parameter": s,
        "coverage": coverage, "nll": nll,
        "n_train": len(idx_train), "n_test": len(idx_test),
    }], columns=["model", "a", "b", "sd_parameter", "coverage", "nll", "n_train", "n_test"])
    os.makedirs(OUT, exist_ok=True)
    row.to_csv(os.path.join(OUT, "M1.csv"), index=False)
    print(row.to_string(index=False))


if __name__ == "__main__":
    main()
