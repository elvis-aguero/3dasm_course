"""Fit the stopping-distance model y | x ~ Normal(mu(x), sd(x)).

mu(x) = a*x + b*x**2           (reaction distance + braking distance)
sd(x) = s0 + s1*x              (spread from driver-to-driver reaction time)

Data: the 50 earlier measurements in data/car_stopping_distance plus every
evaluator call logged in workspace/calls.csv. Prints the maximum-likelihood
parameters to paste into predict.py.
"""
from pathlib import Path

import numpy as np
from scipy import optimize, stats

HERE = Path(__file__).resolve().parent
EXP = HERE.parents[1] / "data" / "car_stopping_distance" / "experiment_data"

x0 = np.genfromtxt(EXP / "input.csv", delimiter=",", skip_header=1, usecols=1)
y0 = np.genfromtxt(EXP / "output.csv", delimiter=",", skip_header=1, usecols=1)
calls = np.genfromtxt(HERE / "workspace" / "calls.csv", delimiter=",")
x = np.r_[x0, calls[:, 0]]
y = np.r_[y0, calls[:, 1]]


def neg_log_lik(q):
    a, b, log_s0, log_s1 = q
    mu = a * x + b * x**2
    sd = np.exp(log_s0) + np.exp(log_s1) * x
    return -stats.norm.logpdf(y, mu, sd).sum()


fit = optimize.minimize(
    neg_log_lik,
    [1.4, 0.1, 0.0, -0.6],
    method="Nelder-Mead",
    options={"maxiter": 60000, "xatol": 1e-10, "fatol": 1e-10},
)
a, b = fit.x[:2]
s0, s1 = np.exp(fit.x[2:])
print(f"n = {len(x)} measurements")
print(f"a = {a:.6f}, b = {b:.6f}, s0 = {s0:.6f}, s1 = {s1:.6f}, nll = {fit.fun:.3f}")

z = (y - (a * x + b * x**2)) / (s0 + s1 * x)
print(f"fraction inside mu +- 1.96 sd: {np.mean(np.abs(z) < 1.96):.3f}")
