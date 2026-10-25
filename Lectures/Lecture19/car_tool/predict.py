"""Stopping-distance model for a car at speed x (m/s).

mu(x) = a*x^2 + b*x + c            (quadratic mean, fitted by least squares)
sd(x) = s0 + s1*x                  (linear spread, fitted by Gaussian max. likelihood)

Fitted on 24 Measure() calls spanning x in [3, 82].
"""

import math

_A, _B, _C = 0.09636872, 1.74978205, -2.40423506
_S0, _S1 = 0.42277263, 0.36265372


def predict(x: float):
    """Return (mu, sd) of the stopping distance y (m) at speed x (m/s)."""
    x = float(x)
    mu = _A * x * x + _B * x + _C
    sd = _S0 + _S1 * x
    return mu, sd


if __name__ == "__main__":
    for v in (3, 20, 40, 60, 82):
        m, s = predict(v)
        print(f"x={v:>3}: mu={m:8.2f}  sd={s:6.2f}  95% band=[{m - 1.96*s:8.2f}, {m + 1.96*s:8.2f}]")
