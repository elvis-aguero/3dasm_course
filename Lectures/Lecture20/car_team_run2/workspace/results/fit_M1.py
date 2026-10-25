"""Fit model M1 for the car stopping distance study (PROBLEM_STATEMENT.md).

M1: a, b by least squares of y on [x, x**2] (no intercept) on training rows.
s = numpy.std of training residuals (ddof=0). Mean = a*x + b*x**2, sd = s.
Assessment on test rows: coverage of mean +- 1.96*sd, and mean negative log normal density.
"""
from pathlib import Path

import numpy as np
from sklearn.model_selection import train_test_split
from scipy.stats import norm
from f3dasm import ExperimentData
import pandas as pd

STUDY = Path("/Users/harrislab/Documents/GitHub/3dasm_course/Lectures/Lecture20/car_team_run2")
DATA = STUDY / "data" / "car_stopping_distance"
OUT = STUDY / "workspace" / "results"


def main() -> None:
    exp = ExperimentData.from_file(DATA)
    inp, out = exp.to_pandas()
    x = inp["x"].to_numpy(dtype=float)
    y = out["y"].to_numpy(dtype=float)

    idx = np.arange(len(x))
    train_idx, test_idx = train_test_split(idx, train_size=0.75, random_state=1987)
    assert len(train_idx) == 37 and len(test_idx) == 13

    xtr, ytr = x[train_idx], y[train_idx]
    xte, yte = x[test_idx], y[test_idx]

    design_tr = np.column_stack([xtr, xtr**2])
    (a, b), *_ = np.linalg.lstsq(design_tr, ytr, rcond=None)
    resid_tr = ytr - (a * xtr + b * xtr**2)
    s = np.std(resid_tr, ddof=0)

    mu_te = a * xte + b * xte**2
    coverage = np.mean(np.abs(yte - mu_te) <= 1.96 * s)
    nll = np.mean(-norm.logpdf(yte, loc=mu_te, scale=s))

    row = pd.DataFrame([{
        "model": "M1",
        "a": a,
        "b": b,
        "sd_parameter": s,
        "coverage": coverage,
        "nll": nll,
        "n_train": len(train_idx),
        "n_test": len(test_idx),
    }])
    OUT.mkdir(parents=True, exist_ok=True)
    row.to_csv(OUT / "M1.csv", index=False)
    print(row.to_string(index=False))


if __name__ == "__main__":
    main()
