# Stopping distance of a car

A car travelling at speed x (m/s) when its driver first sees an obstacle travels a distance y (m) before it stops.
Different drivers have different reaction times, so repeated measurements at the same speed differ. The equation
behind y is not known.

New measurements come from the tool Measure: Measure(x) with a speed x in [3, 82] m/s returns the stopping distance y of
one new driver. A measurement is expensive: use at most 30 calls in total.

Goal. Decide at which speeds to measure, and build a model of y as a function of x: its mean mu(x) and its standard
deviation sd(x), such that mu(x) +- 1.96 sd(x) contains about 95% of the stopping distances of new drivers at any
speed in [3, 82] m/s.

Deliverable. A file predict.py with a function predict(x) that takes a speed x in m/s (a float) and returns the pair
(mu, sd) in metres, and a short account of which speeds were measured, why, and the model chosen.
