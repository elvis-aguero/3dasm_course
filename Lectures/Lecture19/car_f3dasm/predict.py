"""Degree-2 polynomial surrogate for the car stopping distance y(x).

The stored data (data/) contains one row per driver: speed x, reaction time z,
and stopping distance y = z*x + 0.1*x**2. Since z varies per driver, the fit is
of y on x alone, which estimates the expected stopping distance E[y | x].

Usage:
    from predict import predict
    predict(50.0)            # -> predicted stopping distance (m)
    predict([10, 40, 80])    # -> array of predictions
"""

from pathlib import Path

import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import PolynomialFeatures

from f3dasm import ExperimentData

DATA_DIR = Path(__file__).parent / "data"
DEGREE = 2


def _fit_model():
    data = ExperimentData.from_file(project_dir=DATA_DIR)
    inputs, outputs = data.to_pandas()
    X = inputs[["x"]].to_numpy()
    y = outputs["y"].to_numpy()
    model = make_pipeline(PolynomialFeatures(degree=DEGREE), LinearRegression())
    model.fit(X, y)
    return model


_model = _fit_model()


def predict(x):
    """Predict stopping distance y (m) for speed x (m/s).

    Accepts a scalar or array-like. Returns a float for scalar input and a
    numpy array otherwise.
    """
    x_arr = np.atleast_1d(np.asarray(x, dtype=float))
    y_pred = _model.predict(x_arr.reshape(-1, 1))
    if np.ndim(x) == 0:
        return float(y_pred[0])
    return y_pred


if __name__ == "__main__":
    for speed in (3, 20, 50, 82):
        print(f"x = {speed:>3} m/s  ->  predicted y = {predict(speed):.2f} m")
