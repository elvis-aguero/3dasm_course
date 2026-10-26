import os
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from scipy.stats import norm
from f3dasm import ExperimentData

STUDY = "/Users/harrislab/Documents/GitHub/3dasm_course/Lectures/Lecture20/car_team_run2"
HERE = os.path.dirname(os.path.abspath(__file__))

data = ExperimentData.from_file(os.path.join(STUDY, "data", "car_stopping_distance"))
df_in, df_out = data.to_pandas()
x_all = np.asarray(df_in["x"], dtype=float).ravel()
y_all = np.asarray(df_out["y"], dtype=float).ravel()
n = len(x_all)
assert n == 50, n

idx = np.arange(n)
idx_train, idx_test = train_test_split(idx, train_size=0.75, random_state=1987)
x_tr, y_tr = x_all[idx_train], y_all[idx_train]
x_te, y_te = x_all[idx_test], y_all[idx_test]

A = np.column_stack([x_tr, x_tr**2])
(a, b), *_ = np.linalg.lstsq(A, y_tr, rcond=None)
resid = y_tr - (a * x_tr + b * x_tr**2)
s = np.std(resid)  # ddof=0

mu_te = a * x_te + b * x_te**2
coverage = float(np.mean(np.abs(y_te - mu_te) <= 1.96 * s))
nll = float(np.mean(-norm.logpdf(y_te, loc=mu_te, scale=s)))

row = pd.DataFrame([{
    "model": "M1",
    "a": float(a),
    "b": float(b),
    "sd_parameter": float(s),
    "coverage": coverage,
    "nll": nll,
    "n_train": int(len(idx_train)),
    "n_test": int(len(idx_test)),
}])
row.to_csv(os.path.join(HERE, "M1.csv"), index=False)
print(row.to_string(index=False))
