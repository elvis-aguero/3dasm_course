"""Fit M1 of the car stopping-distance problem (PROBLEM_STATEMENT.md).

M1: a, b by lstsq of y on [x, x**2] (no intercept), training rows;
s = numpy.std of training residuals (ddof=0); mean a*x + b*x**2, sd s.
Assessment on test rows: coverage of mean +- 1.96 sd; nll = mean -log normal density.
"""
from pathlib import Path

import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from f3dasm import ExperimentData

STUDY = Path("/Users/harrislab/Documents/GitHub/3dasm_course/Lectures/Lecture20/car_team_run1")
DATA = STUDY / "data" / "car_stopping_distance"
OUT = STUDY / "workspace" / "results"


def main():
    ed = ExperimentData.from_file(str(DATA))
    input_df, output_df = ed.to_pandas()  # (inputs, outputs)
    x = np.asarray(input_df["x"], dtype=float).ravel()
    y = np.asarray(output_df["y"], dtype=float).ravel()
    assert len(x) == len(y) == 50, (len(x), len(y))

    idx = np.arange(len(x))
    train_idx, test_idx = train_test_split(idx, train_size=0.75, random_state=1987)
    xtr, ytr = x[train_idx], y[train_idx]
    xte, yte = x[test_idx], y[test_idx]

    A = np.column_stack([xtr, xtr ** 2])
    (a, b), *_ = np.linalg.lstsq(A, ytr, rcond=None)
    resid = ytr - (a * xtr + b * xtr ** 2)
    s = np.std(resid)  # ddof=0

    mu = a * xte + b * xte ** 2
    coverage = np.mean(np.abs(yte - mu) <= 1.96 * s)
    nll = np.mean(0.5 * np.log(2 * np.pi * s ** 2) + 0.5 * ((yte - mu) / s) ** 2)

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
    OUT.mkdir(parents=True, exist_ok=True)
    pd.DataFrame([row], columns=["model", "a", "b", "sd_parameter", "coverage", "nll", "n_train", "n_test"]).to_csv(
        OUT / "M1.csv", index=False)
    print(row)


if __name__ == "__main__":
    main()
