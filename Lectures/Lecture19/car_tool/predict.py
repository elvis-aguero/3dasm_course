"""Stopping-distance model for a car at speed x (m/s), x in [3, 82].

Fitted to 30 Measure() calls (no replicate-free design; 30 is the full budget).

Mean:   mu(x) = a*x^2 + b*x + c          (weighted least squares, weights ~ 1/mu)
Spread: sd(x) = s0 + s1*mu(x)            (fitted to |residual| * sqrt(pi/2))

Empirically the residual spread grows with the mean; the linear-in-mu sd
covers ~93% of the measured points within mu +- 1.96 sd (rms z ~ 1.0).
"""

import math

_A, _B, _C = 0.10003033, 1.33274935, 1.49047205
_S0, _S1 = 3.28606857, 0.04296981


def predict(x):
    """Return (mu, sd) of the stopping distance y (m) at speed x (m/s)."""
    x = float(x)
    mu = _A * x * x + _B * x + _C
    sd = _S0 + _S1 * mu
    return mu, max(sd, 1e-6)


if __name__ == "__main__":
    for v in (3, 10, 30, 60, 82):
        m, s = predict(v)
        print(f"x={v:>3}  mu={m:8.2f}  sd={s:6.2f}  95%: [{m - 1.96 * s:8.2f}, {m + 1.96 * s:8.2f}]")
