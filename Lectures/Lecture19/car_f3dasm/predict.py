"""Degree-2 polynomial surrogate for the car stopping distance y(x).

Fitted on the 30-driver Sobol experiment stored in data/ (see make_data.py).
The reaction time z varies per driver, so the fit describes the average
stopping distance over drivers.
"""
from pathlib import Path

import numpy as np
from f3dasm import ExperimentData
from sklearn.linear_model import LinearRegression
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import PolynomialFeatures

_DATA_DIR = Path(__file__).resolve().parent / "data"

_data = ExperimentData.from_file(project_dir=_DATA_DIR)
_x_df, _y_df = _data.to_pandas()
_X = _x_df[["x"]].to_numpy(dtype=float)
_y = _y_df["y"].to_numpy(dtype=float)

_model = make_pipeline(PolynomialFeatures(degree=2), LinearRegression())
_model.fit(_X, _y)


def predict(x):
    """Predicted stopping distance y (m) for speed x (m/s).

    Accepts a scalar or array-like of speeds; returns a float for a scalar
    input and a 1-D numpy array otherwise.
    """
    x_arr = np.asarray(x, dtype=float)
    scalar = x_arr.ndim == 0
    y_hat = _model.predict(x_arr.reshape(-1, 1)).ravel()
    return float(y_hat[0]) if scalar else y_hat


if __name__ == "__main__":
    for speed in (3.0, 40.0, 82.0):
        print(f"x={speed:5.1f} m/s -> y={predict(speed):8.2f} m")
