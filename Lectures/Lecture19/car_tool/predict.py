"""Stopping-distance model for a car at speed x (m/s), x in [3, 82].

Mean:   mu(x) = a*x + b*x^2
        a = 1.581 s   (effective reaction time: distance covered before braking)
        b = 0.0982 s^2/m (braking term; implied deceleration 1/(2b) ~ 5.1 m/s^2)
Spread: sd(x) = k*x,  k = 0.418 (proportional to speed, maximum-likelihood fit)

Coefficients were fitted by least squares (mean) and maximum likelihood (spread)
to 30 Measure() evaluations spread over [3, 82].
"""

import math

A_REACTION = 1.58126704
B_BRAKING = 0.09821271
K_SPREAD = 0.41802353


def predict(x):
    """Return (mu, sd) of the stopping distance y (metres) at speed x (m/s)."""
    x = float(x)
    mu = A_REACTION * x + B_BRAKING * x * x
    sd = K_SPREAD * x
    return mu, sd


if __name__ == "__main__":
    for v in (3, 20, 50, 82):
        mu, sd = predict(v)
        print(f"x={v:>3}: mu={mu:8.2f} m, sd={sd:6.2f} m, 95% band=[{mu - 1.96 * sd:8.2f}, {mu + 1.96 * sd:8.2f}]")
