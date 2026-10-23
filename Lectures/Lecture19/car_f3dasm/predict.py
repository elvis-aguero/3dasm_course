"""Predict stopping distance y (m) from speed x (m/s).

A degree-2 polynomial is fitted with scikit-learn to the 30 driver
experiments stored in data/ (see generate_data.py). Each driver has an
individual reaction time z, so the fit targets the average stopping
distance over drivers.
"""

from pathlib import Path

import numpy as np
from f3dasm import ExperimentData
from sklearn.linear_model import LinearRegression
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import PolynomialFeatures

DATA_DIR = Path(__file__).resolve().parent / "data"

_data = ExperimentData.from_file(project_dir=DATA_DIR)
_inputs, _outputs = _data.to_pandas()
_x_train = _inputs[["x"]].to_numpy()
_y_train = _outputs["y"].to_numpy()

_model = make_pipeline(PolynomialFeatures(degree=2), LinearRegression())
_model.fit(_x_train, _y_train)


def predict(x):
    """Return the predicted stopping distance y (m) for speed x (m/s).

    Parameters
    ----------
    x : float or array-like
        Speed in m/s.

    Returns
    -------
    float or numpy.ndarray
        Predicted stopping distance(s) in metres. A scalar input gives a
        float; an array-like input gives an array of the same length.
    """
    scalar = np.isscalar(x)
    x_arr = np.atleast_1d(np.asarray(x, dtype=float)).reshape(-1, 1)
    y_hat = _model.predict(x_arr)
    return float(y_hat[0]) if scalar else y_hat


if __name__ == "__main__":
    for speed in (5.0, 30.0, 60.0, 82.0):
        print(f"x = {speed:5.1f} m/s -> predicted y = {predict(speed):8.2f} m")
