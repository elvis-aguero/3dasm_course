"""Fit model M2 of the car stopping distance (see PROBLEM_STATEMENT.md).

M2: a, b by lstsq of y/x on columns [1, x] (training rows);
    c = numpy.std(residuals of y/x, ddof=0) on training rows.
    Mean = a*x + b*x**2, sd = c*x.
Assessment on test rows: coverage of mean +- 1.96*sd; nll = mean of -log normal density of y.
"""
from pathlib import Path

import numpy as np

from sklearn.model_selection import train_test_split
from f3dasm import ExperimentData

STUDY = Path(__file__).resolve().parents[2]
DATA = STUDY / "data" / "car_stopping_distance"
OUT = Path(__file__).resolve().parent / "M2.csv"


def main():
    exp = ExperimentData.from_file(DATA)
    in_df, out_df = exp.to_pandas()
    x_all = in_df["x"].to_numpy(dtype=float)
    y_all = out_df["y"].to_numpy(dtype=float)
    n = len(x_all)

    idx_train, idx_test = train_test_split(np.arange(n), train_size=0.75, random_state=1987)
    x_tr, y_tr = x_all[idx_train], y_all[idx_train]
    x_te, y_te = x_all[idx_test], y_all[idx_test]

    # M2 fit: lstsq of y/x on [1, x]
    design_tr = np.column_stack([np.ones_like(x_tr), x_tr])
    coef, *_ = np.linalg.lstsq(design_tr, y_tr / x_tr, rcond=None)
    intercept, slope = coef  # (1, x) columns
    # a, b names follow the problem statement: mean = a*x + b*x**2
    a, b = float(intercept), float(slope)

    resid = y_tr / x_tr - (intercept + slope * x_tr)
    c = float(np.std(resid, ddof=0))

    mean_te = a * x_te + b * x_te**2
    sd_te = c * x_te
    coverage = float(np.mean(np.abs(y_te - mean_te) <= 1.96 * sd_te))
    log_dens = -0.5 * np.log(2 * np.pi * sd_te**2) - 0.5 * ((y_te - mean_te) / sd_te) ** 2
    nll = float(np.mean(-log_dens))

    import pandas as pd
    row = pd.DataFrame([{
        "model": "M2", "a": a, "b": b, "sd_parameter": c,
        "coverage": coverage, "nll": nll,
        "n_train": len(idx_train), "n_test": len(idx_test),
    }])
    row.to_csv(OUT, index=False)
    print(row.to_string(index=False))


if __name__ == "__main__":
    main()
