"""Stopping-distance model for a car at speed x (m/s), x in [3, 82].

Fitted to 30 Measure() calls (stratified design over [3, 82]).

Mean:  mu(x) = a*x + b*x^2           (reaction distance + braking distance, no intercept)
Sd:    sd(x) = c0 + c1*sqrt(x)       (fitted to |residual| * sqrt(pi/2))

Coefficients were chosen by leave-one-out Gaussian NLL among
{quadratic, cubic, quadratic+intercept} x {const, linear, sqrt} sd forms.
"""

import math

A = 1.09771097
B = 0.10455989
C0 = -4.69233329
C1 = 3.69957215

SD_FLOOR = 0.5  # metres; keeps the interval from collapsing numerically


def predict(x):
    """Return (mu, sd) of the stopping distance in metres at speed x in m/s."""
    x = float(x)
    mu = A * x + B * x * x
    sd = C0 + C1 * math.sqrt(x)
    return mu, max(sd, SD_FLOOR)
