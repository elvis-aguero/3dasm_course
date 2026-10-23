"""Stopping-distance model y(x) for a car at speed x (m/s).

Measured design (30 Measure calls, x in m/s):
  - 13 speeds spread over [3, 82]: 3, 8, 14, 20, 27, 34, 41, 48, 55, 62, 69, 76, 82
  - 13 further speeds filling the gaps: 5, 11, 17, 24, 31, 38, 45, 52, 59, 66, 73, 79, 82
  - replicates at 3, 27, 41, 82 to check the spread
  The design is space-filling because the mean is a smooth curve over the whole
  range and the spread must be learned everywhere, including the high-speed end
  where the stopping distance (and its scatter) is largest.

Model:
  mu(x) = a*x^2 + b*x            (braking term a*x^2 + reaction-distance term b*x;
                                  least squares, no intercept: y -> 0 as x -> 0)
          a = 0.09686, b = 1.55569
  sd(x) = s*x                     (scatter from driver reaction time times speed;
                                  s = 0.4767 m per m/s, least squares on |residual|)

In-sample, 29 of 30 measurements lie within mu +- 1.96 sd.
"""

import math

_A = 0.09686399
_B = 1.55568597
_S = 0.4767


def predict(x: float) -> tuple[float, float]:
    """Return (mu, sd) in metres for a car at speed x in m/s."""
    x = float(x)
    mu = _A * x * x + _B * x
    sd = _S * abs(x)
    return mu, sd
