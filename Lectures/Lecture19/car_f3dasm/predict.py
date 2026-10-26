"""Predict the stopping distance y (m) of a car from its speed x (m/s).

A degree-2 polynomial is fitted with scikit-learn to the f3dasm experiment
data in data/ (30 drivers, each with their own reaction time z).
"""

from functools import lru_cache
from pathlib import Path

import numpy as np
from f3dasm import ExperimentData
from sklearn.linear_model import LinearRegression
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import PolynomialFeatures

DATA_DIR = Path(__file__).resolve().parent / "data"


@lru_cache(maxsize=None)
def _fit_model():
    """Fit y ~ poly2(x) on the stored experiments (fitted once, then cached)."""
    inputs, outputs = ExperimentData.from_file(project_dir=DATA_DIR).to_pandas()
    x = inputs[["x"]].to_numpy(dtype=float)
    y = outputs["y"].to_numpy(dtype=float)
    model = make_pipeline(PolynomialFeatures(degree=2), LinearRegression())
    model.fit(x, y)
    return model


def predict(x):
    """Return the predicted stopping distance y (m) for speed(s) x (m/s).

    A scalar gives a float; an array-like gives a numpy array of the same shape.
    """
    x_arr = np.asarray(x, dtype=float)
    y_hat = _fit_model().predict(x_arr.reshape(-1, 1)).reshape(x_arr.shape)
    return float(y_hat) if x_arr.ndim == 0 else y_hat


if __name__ == "__main__":
    for speed in (3.0, 20.0, 50.0, 82.0):
        print(f"x = {speed:5.1f} m/s -> y = {predict(speed):8.2f} m")
