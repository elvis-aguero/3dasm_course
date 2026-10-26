"""Model M2 for the car stopping distance study (see PROBLEM_STATEMENT.md).

M2: a, b by lstsq of y/x on [1, x] (training rows); c = std(residuals of y/x, ddof=0).
Mean a*x + b*x**2, standard deviation c*x.
Assessment on test rows: coverage of mean +- 1.96 sd, and mean negative log normal density of y.
"""
from pathlib import Path

import numpy as np
from f3dasm import ExperimentData
from sklearn.model_selection import train_test_split
import pandas as pd

STUDY = Path(__file__).resolve().parents[2]
DATA = STUDY / "data" / "car_stopping_distance"
OUT = Path(__file__).resolve().parent / "M2.csv"


def main():
    exp = ExperimentData.from_file(str(DATA))
    inputs, outputs = exp.to_pandas()
    x = inputs["x"].to_numpy(dtype=float)
    y = outputs["y"].to_numpy(dtype=float)
    n = len(x)

    idx_train, idx_test = train_test_split(
        np.arange(n), train_size=0.75, random_state=1987
    )
    assert len(idx_train) == 37 and len(idx_test) == 13, (len(idx_train), len(idx_test))

    xtr, ytr = x[idx_train], y[idx_train]
    xte, yte = x[idx_test], y[idx_test]

    # M2: fit y/x = a + b*x by least squares on training rows
    design_tr = np.column_stack([np.ones_like(xtr), xtr])
    coef, *_ = np.linalg.lstsq(design_tr, ytr / xtr, rcond=None)
    a, b = float(coef[0]), float(coef[1])

    resid_tr = ytr / xtr - (a + b * xtr)
    c = float(np.std(resid_tr, ddof=0))

    # Test-set assessment
    mu_te = a * xte + b * xte**2
    sd_te = c * xte
    coverage = float(np.mean(np.abs(yte - mu_te) <= 1.96 * sd_te))
    log_pdf = -0.5 * np.log(2 * np.pi * sd_te**2) - 0.5 * ((yte - mu_te) / sd_te) ** 2
    nll = float(np.mean(-log_pdf))

    row = pd.DataFrame(
        [
            {
                "model": "M2",
                "a": a,
                "b": b,
                "sd_parameter": c,
                "coverage": coverage,
                "nll": nll,
                "n_train": int(len(idx_train)),
                "n_test": int(len(idx_test)),
            }
        ]
    )
    row.to_csv(OUT, index=False)
    print(row.to_string(index=False))
    print(f"wrote {OUT}")


if __name__ == "__main__":
    main()
