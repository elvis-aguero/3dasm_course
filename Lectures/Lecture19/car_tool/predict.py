"""Stopping-distance model for a new driver.

Mean:  mu(x) = a*x + b*x**2           (reaction-distance + braking-distance shape)
Scale: sd(x) = c + d*x                (noise standard deviation grows with speed)

Fitted on 30 Measure() calls (x in [3, 82]; 4 replicates at x=14, 3 each at x=50 and x=82).
Coverage: mu +- 1.96*sd is intended to contain ~95% of drivers for x in [3, 82].
"""

import math

A_LIN = 1.73226001
B_QUAD = 0.09520235
C_SD0 = 3.99123636
D_SD1 = 0.30362472


def predict(x):
    """Return (mu, sd) of the stopping distance y (m) at speed x (m/s)."""
    x = float(x)
    mu = A_LIN * x + B_QUAD * x * x
    sd = C_SD0 + D_SD1 * x
    return mu, max(sd, 0.5)


if __name__ == "__main__":
    for v in (3, 14, 50, 82):
        m, s = predict(v)
        print(f"x={v:>3}: mu={m:8.2f} m  sd={s:6.2f} m  95% band=[{m - 1.96 * s:8.2f}, {m + 1.96 * s:8.2f}]")
