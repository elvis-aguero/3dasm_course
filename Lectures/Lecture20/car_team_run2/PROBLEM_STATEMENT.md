# Two models of the stopping distance of a car

Data: `data/car_stopping_distance`, an f3dasm ExperimentData of 50 stops (input `x`, speed in m/s; output `y`,
stopping distance in m). Load it with `ExperimentData.from_file`, and take the tables with `to_pandas()`.

| Item | Decision |
|---|---|
| Split | `train_test_split(row index, train_size=0.75, random_state=1987)` from scikit-learn: 37 training rows, 13 test rows |
| M1 | `a, b` by `numpy.linalg.lstsq` of `y` on the columns `[x, x**2]` (no intercept), training rows. `s` = `numpy.std` of the training residuals (ddof=0). Mean `a*x + b*x**2`, standard deviation `s` |
| M2 | `a, b` by `numpy.linalg.lstsq` of `y/x` on the columns `[1, x]`, training rows. `c` = `numpy.std` of the residuals of `y/x` (ddof=0). Mean `a*x + b*x**2`, standard deviation `c*x` |
| Assessment | On the test rows: `coverage`, the fraction of `y` inside mean +- 1.96 standard deviation; `nll`, the mean of minus the log of the normal density of `y` |

## Deliverables (folder `results/`)

- `fit_M1.py` and `M1.csv`, `fit_M2.py` and `M2.csv`. Each CSV has one row and exactly the columns `model`, `a`, `b`,
  `sd_parameter` (`s` for M1, `c` for M2), `coverage`, `nll`, `n_train`, `n_test`.
- `check.md`
