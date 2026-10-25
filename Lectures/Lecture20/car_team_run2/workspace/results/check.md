# Check of M1 and M2 (checker, D003)

Recomputed independently in `runs/20261025T181150/debug/delegations/D003/recompute.py` (no import or run of fit_M1.py / fit_M2.py). Data loaded with `ExperimentData.from_file("data/car_stopping_distance")` and `to_pandas()`. Split: `train_test_split(row index, train_size=0.75, random_state=1987)`. Tolerance: relative difference below 1e-6.

Rows: recomputed n_train = 37, n_test = 13 (50 stops in total).

## M1

| item | file (CSV) | recomputed | rel. diff | verdict |
|---|---|---|---|---|
| a | 1.556792744461828 | 1.556792744461828 | 0.00e+00 | PASS |
| b | 0.1003596848656863 | 0.1003596848656863 | 0.00e+00 | PASS |
| sd_parameter (s) | 27.98303080695783 | 27.98303080695783 | 0.00e+00 | PASS |
| coverage | 0.8461538461538461 | 0.8461538461538461 | 0.00e+00 | PASS |
| nll | 4.976149641475804 | 4.976149641475804 | 0.00e+00 | PASS |
| n_train | 37 | 37 | - | PASS |
| n_test | 13 | 13 | - | PASS |

Column/format check for `M1.csv`: header = `model,a,b,sd_parameter,coverage,nll,n_train,n_test` (matches the required header exactly); data rows = 1; model label = `M1`. Result: PASS.

**M1 verdict: PASS**

## M2

| item | file (CSV) | recomputed | rel. diff | verdict |
|---|---|---|---|---|
| a | 1.3804030477145803 | 1.3804030477145803 | 0.00e+00 | PASS |
| b | 0.10323542514078464 | 0.10323542514078464 | 0.00e+00 | PASS |
| sd_parameter (c) | 0.5532310661868638 | 0.5532310661868638 | 0.00e+00 | PASS |
| coverage | 0.8461538461538461 | 0.8461538461538461 | 0.00e+00 | PASS |
| nll | 4.503770939937342 | 4.503770939937341 | 1.97e-16 | PASS |
| n_train | 37 | 37 | - | PASS |
| n_test | 13 | 13 | - | PASS |

Column/format check for `M2.csv`: header = `model,a,b,sd_parameter,coverage,nll,n_train,n_test` (matches exactly); data rows = 1; model label = `M2`. Result: PASS.

**M2 verdict: PASS**

## Overall verdict: PASS
