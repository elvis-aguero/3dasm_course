"""Model M1 of the car stopping distance: quadratic-no-intercept mean, constant sd.

Mean: a*x + b*x**2 (a, b by least squares of y on [x, x**2], training rows).
SD:   s = numpy.std of training residuals (ddof=0).
Assessed on test rows: 95% coverage and mean negative log normal density.
"""
import os

import numpy as np
from sklearn.model_selection import train_test_split
from f3dasm import ExperimentData

HERE = os.path.dirname(os.path.abspath(__file__))
STUDY = os.path.dirname(HERE)
DATA = os.path.join(STUDY, "data", "car_stopping_distance")
OUT = os.path.join(HERE, "M1.csv")

exp = ExperimentData.from_file(DATA)
df_in, df_out = exp.to_pandas()
x = np.asarray(df_in["x"], dtype=float).ravel()
y = np.asarray(df_out["y"], dtype=float).ravel()
assert x.shape == y.shape and x.size == 50, (x.shape, y.shape)

idx = np.arange(x.size)
idx_train, idx_test = train_test_split(idx, train_size=0.75, random_state=1987)
n_train, n_test = len(idx_train), len(idx_test)
assert (n_train, n_test) == (37, 13), (n_train, n_test)

xt, yt = x[idx_train], y[idx_train]
X = np.column_stack([xt, xt ** 2])
(a, b), *_ = np.linalg.lstsq(X, yt, rcond=None)
a, b = float(a), float(b)
s = float(np.std(yt - (a * xt + b * xt ** 2), ddof=0))

xe, ye = x[idx_test], y[idx_test]
mu = a * xe + b * xe ** 2
coverage = float(np.mean(np.abs(ye - mu) <= 1.96 * s))
nll = float(np.mean(0.5 * np.log(2 * np.pi * s ** 2) + 0.5 * ((ye - mu) / s) ** 2))

os.makedirs(HERE, exist_ok=True)
with open(OUT, "w") as f:
    f.write("model,a,b,sd_parameter,coverage,nll,n_train,n_test\n")
    f.write(f"M1,{a!r},{b!r},{s!r},{coverage!r},{nll!r},{n_train},{n_test}\n")
print(open(OUT).read())
