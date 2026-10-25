"""Predict stopping distance y (m) of a car from its speed x (m/s).

The model is a degree-2 polynomial in x, fitted with scikit-learn to the
ExperimentData stored in data/experiment_data (30 Sobol-sampled speeds, each
paired with one driver's reaction time z ~ N(1.5, 0.5^2)).
"""
from pathlib import Path

import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import PolynomialFeatures

from f3dasm import ExperimentData

DATA_DIR = Path(__file__).resolve().parent / "data"  # store lives in data/experiment_data/


def _fit_model():
    data = ExperimentData.from_file(project_dir=DATA_DIR)
    inp, out = data.to_pandas()
    x = inp[["x"]].to_numpy(dtype=float)
    y = out["y"].to_numpy(dtype=float)
    model = make_pipeline(PolynomialFeatures(degree=2), LinearRegression())
    model.fit(x, y)
    return model


_MODEL = _fit_model()


def predict(x):
    """Return the predicted stopping distance y for speed(s) x (m/s)."""
    x_arr = np.asarray(x, dtype=float).reshape(-1, 1)
    y_hat = _MODEL.predict(x_arr)
    return float(y_hat[0]) if np.ndim(x) == 0 else y_hat


if __name__ == "__main__":
    for speed in (3.0, 40.0, 82.0):
        print(f"x = {speed:5.1f} m/s -> predicted y = {predict(speed):8.2f} m")
