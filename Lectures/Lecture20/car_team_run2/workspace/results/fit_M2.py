"""Model M2 of the car stopping-distance problem (see PROBLEM_STATEMENT.md).

M2: a, b by least squares of y/x on [1, x] (training rows);
    c = numpy.std of the residuals of y/x (ddof=0);
    predictive mean a*x + b*x**2, predictive sd c*x.
Assessment on test rows: coverage of mean +- 1.96 sd, and mean negative log normal density (nll).
Writes workspace/results/M2.csv (one row).
"""

from pathlib import Path

import numpy as np
import pandas as pd
from f3dasm import ExperimentData
from sklearn.model_selection import train_test_split

STUDY_DIR = Path(__file__).resolve().parents[2]
DATA_DIR = STUDY_DIR / "data" / "car_stopping_distance"
OUT_CSV = Path(__file__).resolve().parent / "M2.csv"


def main():
    ed = ExperimentData.from_file(str(DATA_DIR))
    input_df, output_df = ed.to_pandas()
    x = input_df["x"].to_numpy(dtype=float)
    y = output_df["y"].to_numpy(dtype=float)

    idx = np.arange(len(x))
    train_idx, test_idx = train_test_split(idx, train_size=0.75, random_state=1987)
    x_tr, y_tr = x[train_idx], y[train_idx]
    x_te, y_te = x[test_idx], y[test_idx]

    # M2 fit: y/x = a + b*x  ->  y = a*x + b*x**2
    design_tr = np.column_stack([np.ones_like(x_tr), x_tr])
    (a, b), *_ = np.linalg.lstsq(design_tr, y_tr / x_tr, rcond=None)
    c = np.std(y_tr / x_tr - (a + b * x_tr), ddof=0)

    # Test-set assessment
    mean_te = a * x_te + b * x_te**2
    sd_te = c * x_te
    coverage = np.mean(np.abs(y_te - mean_te) <= 1.96 * sd_te)
    log_density = -0.5 * np.log(2.0 * np.pi * sd_te**2) - (y_te - mean_te) ** 2 / (2.0 * sd_te**2)
    nll = np.mean(-log_density)

    row = {
        "model": "M2",
        "a": float(a),
        "b": float(b),
        "sd_parameter": float(c),
        "coverage": float(coverage),
        "nll": float(nll),
        "n_train": int(len(train_idx)),
        "n_test": int(len(test_idx)),
    }
    pd.DataFrame([row], columns=["model", "a", "b", "sd_parameter", "coverage", "nll", "n_train", "n_test"]).to_csv(
        OUT_CSV, index=False
    )
    print(pd.DataFrame([row]).to_string(index=False))
    print(f"wrote {OUT_CSV}")


if __name__ == "__main__":
    main()
