"""Stopping-distance model: mean and standard deviation of y (m) at speed x (m/s).

Fitted on 30 Measure() calls over x in [3, 82]:
  mu(x)      = a*x + b*x^2                  (least squares, no intercept)
  sd(x)^2    = c0 + c1*mu(x)                (least squares on squared residuals)
Leave-one-out check on the 30 points: 93% of held-out y fall inside mu +- 1.96 sd.
"""
import math

A_MEAN = 1.44665771
B_MEAN = 0.09940101
C0_VAR = 1.69086126
C1_VAR = 1.48442145


def predict(x):
    """Return (mu, sd) of stopping distance y in metres at speed x in m/s."""
    x = float(x)
    mu = A_MEAN * x + B_MEAN * x * x
    var = C0_VAR + C1_VAR * mu
    sd = math.sqrt(max(var, 1e-6))
    return mu, sd


if __name__ == "__main__":
    for speed in (3, 10, 30, 50, 70, 82):
        m, s = predict(speed)
        print(f"x={speed:5.1f}  mu={m:8.2f}  sd={s:6.2f}  95% band=[{m - 1.96 * s:8.2f}, {m + 1.96 * s:8.2f}]")
