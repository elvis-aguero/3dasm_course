# Check of M1 and M2 (checker, independent recomputation)

Recomputation script: `runs/20261025T194713/debug/delegations/D003/recompute.py`, run with `python -I`.
It was written from PROBLEM_STATEMENT.md and did not import anything from `workspace/results/`.
Data: `data/car_stopping_distance` via `ExperimentData.from_file(project_dir=...)`, tables via `to_pandas()`
(a tuple: input table with `x`, output table with `y`; row order checked equal).
Split: `train_test_split(row index, train_size=0.75, random_state=1987)`.
Tolerance: relative difference below 1e-6 (floats).

## Row counts
- Recomputed: n_train = 37, n_test = 13 (50 rows in total).
- M1.csv: n_train = 37, n_test = 13. PASS
- M2.csv: n_train = 37, n_test = 13. PASS

## M1 (PASS)
| item | file (M1.csv) | recomputed | rel. diff | verdict |
|---|---|---|---|---|
| a | 1.556792744461828 | 1.556792744461828 | 0 | PASS |
| b | 0.1003596848656863 | 0.1003596848656863 | 0 | PASS |
| sd_parameter (s) | 27.98303080695783 | 27.98303080695783 | 0 | PASS |
| coverage | 0.8461538461538461 | 0.8461538461538461 | 0 | PASS |
| nll | 4.976149641475804 | 4.976149641475804 | 0 | PASS |

**M1: PASS**

## M2 (PASS)
| item | file (M2.csv) | recomputed | rel. diff | verdict |
|---|---|---|---|---|
| a | 1.3804030477145803 | 1.3804030477145803 | 0 | PASS |
| b | 0.10323542514078464 | 0.10323542514078464 | 0 | PASS |
| sd_parameter (c) | 0.5532310661868638 | 0.5532310661868638 | 0 | PASS |
| coverage | 0.8461538461538461 | 0.8461538461538461 | 0 | PASS |
| nll | 4.503770939937342 | 4.503770939937341 | 2.0e-16 | PASS |

**M2: PASS**

## Column and row structure (PASS)
- M1.csv header: `model,a,b,sd_parameter,coverage,nll,n_train,n_test`, exactly the required columns, one data row, model = `M1`. PASS
- M2.csv header: `model,a,b,sd_parameter,coverage,nll,n_train,n_test`, exactly the required columns, one data row, model = `M2`. PASS

## Files (PASS)
- `workspace/results/fit_M1.py` exists. PASS
- `workspace/results/fit_M2.py` exists. PASS

## M2 follows the statement literally (PASS)
`fit_M2.py` regresses y/x on [1, x] by `np.linalg.lstsq` over training rows; a = intercept, b = slope.
c = `np.std` (ddof=0) of the y/x residuals. Mean = a*x + b*x**2, sd = c*x. Coverage uses mean +- 1.96 sd on test rows.
nll is the mean of -log normal density of y. All of this matches the statement.

## Overall
Both models PASS. No decisions were changed. The checker ran no evaluations (0).
