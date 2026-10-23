## ⚠ UNGATED RUN

This run is NOT validated: the run terminated WITHOUT an accepted Done() — the final conclusions did NOT pass the adversarial critic gate.
Treat all conclusions below as unaudited.

---

`predict.py` is written, and the model is fitted from 58 measurements: the 50 already in `data/car_stopping_distance` plus 8 new evaluator calls.

**Which speeds were measured.** I spent 8 of the 30 calls, all at the two ends of the range: four replicates at x = 82 and four at x = 3. The existing data had almost nothing at those ends (one point near 3, none at 82), and the ±1.96 sd band has to hold "at any speed in [3, 82]", so the edges are where the model is least constrained. The replicates agreed with the model at x = 82 (mean ≈ 798 vs. 794 predicted), and at x = 3 they showed more spread than the simple model predicted, which is why I added a constant term to the sd. I did not measure the middle of the range, because the 50 existing points already cover it densely.

**Model.**
- Mean: μ(x) = 1.4301·x + 0.10058·x². This is the shape of reaction distance plus braking distance. The linear coefficient corresponds to about 1.4 s of reaction time, and the quadratic coefficient to a braking friction of about 0.5 if g = 9.81. Those readings are interpretations, not something the fit proves.
- Spread: sd(x) = 0.801 + 0.531·x m. It grows with speed, which fits driver-to-driver reaction-time variation. The constant term is what the low-speed replicates pushed for.
- Band check: 93% of the 58 points fall inside μ ± 1.96·sd, against a nominal 95%. The standardized residuals have sd ≈ 1.0 in each speed band.

**Assumptions to check.**
- I counted the 50 existing points as data outside the 30-call budget. They are not in `workspace/calls.csv`, and there are more of them than the budget allows, so they cannot be calls from this study. If you count them differently, tell me.
- The Gaussian band is a simplification. The residuals are slightly right-skewed (skew ≈ 0.35), and a log-normal noise model fits marginally better (about one log-likelihood unit). I kept the Gaussian form because the task asks for a mean and an sd.
- The sd at x = 3 rests on very few points, so the band there is the least certain part of the model.

**Files** (in `Lectures/Lecture19/car_solo/`):
- `predict.py`: `predict(x)` returns `(mu, sd)` in metres, with the fitted constants hard-coded. It runs without the data.
- `fit_model.py`: reproduces the fit from the data and `workspace/calls.csv`.