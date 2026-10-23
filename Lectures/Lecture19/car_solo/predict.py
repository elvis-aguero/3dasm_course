"""Stopping distance of a car as a function of speed.

mu(x) = a*x + b*x**2       mean stopping distance (m), x in m/s
sd(x) = s0 + s1*x          driver-to-driver standard deviation (m)

Fitted by maximum likelihood on 58 measurements (see fit_model.py).
"""

A = 1.430091
B = 0.100576
S0 = 0.801150
S1 = 0.531129


def predict(x):
    """Return (mu, sd) in metres for a speed x in m/s."""
    x = float(x)
    mu = A * x + B * x**2
    sd = S0 + S1 * x
    return mu, sd
