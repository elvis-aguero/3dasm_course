# Independent check of M1 and M2 (checker, D003)

Recomputed from `data/car_stopping_distance` (ExperimentData.from_file, then to_pandas, which returns an (x, y) pair of frames) with the decisions of PROBLEM_STATEMENT.md:
split `train_test_split(row index, train_size=0.75, random_state=1987)`; M1 = lstsq of y on [x, x²] (no intercept), s = ddof=0 std of training residuals; M2 = lstsq of y/x on [1, x], c = ddof=0 std of residuals of y/x, sd = c·x; coverage = fraction of test y within mean ± 1.96 sd; nll = mean of −log normal density of test y.
The builder's scripts were not run or imported. My script: `runs/20261025T212037/debug/delegations/D003/recompute.py`. Tolerance: relative difference below 1e-6.

## Row counts

| Check | Recomputed | File | Verdict |
|---|---|---|---|
| n_train | 37 | 37 (M1.csv and M2.csv) | PASS |
| n_test | 13 | 13 (M1.csv and M2.csv) | PASS |

## Shape and column checks

| Check | Recomputed | File | Verdict |
|---|---|---|---|
| M1.csv columns | model,a,b,sd_parameter,coverage,nll,n_train,n_test | same | PASS |
| M2.csv columns | model,a,b,sd_parameter,coverage,nll,n_train,n_test | same | PASS |
| M1.csv shape | one data row (1×8) | (1, 8) | PASS |
| M2.csv shape | one data row (1×8) | (1, 8) | PASS |
| model label | M1 / M2 | 'M1' / 'M2' | PASS |
| fit_M1.py exists in workspace/results/ | — | present | PASS |
| fit_M2.py exists in workspace/results/ | — | present | PASS |

## M1

| Quantity | Recomputed | File (M1.csv) | Rel. diff | Verdict |
|---|---|---|---|---|
| a | 1.556792744461828 | 1.556792744461828 | 0 | PASS |
| b | 0.1003596848656863 | 0.1003596848656863 | 0 | PASS |
| sd_parameter (s) | 27.98303080695783 | 27.98303080695783 | 0 | PASS |
| coverage | 0.8461538461538461 | 0.8461538461538461 | 0 | PASS |
| nll | 4.976149641475804 | 4.976149641475804 | 0 | PASS |

**M1: PASS**

## M2

| Quantity | Recomputed | File (M2.csv) | Rel. diff | Verdict |
|---|---|---|---|---|
| a | 1.3804030477145803 | 1.3804030477145803 | 0 | PASS |
| b | 0.10323542514078464 | 0.10323542514078464 | 0 | PASS |
| sd_parameter (c) | 0.5532310661868638 | 0.5532310661868638 | 0 | PASS |
| coverage | 0.8461538461538461 | 0.8461538461538461 | 0 | PASS |
| nll | 4.503770939937342 | 4.503770939937342 | 0 | PASS |

**M2: PASS**

Note on M2 mapping: the regression of y/x on [1, x] gives intercept p and slope q with y/x = p + q·x, i.e. y = p·x + q·x². So a = p (intercept) and b = q (slope), which is the mapping used in both my recomputation and the file.

## Discrepancies

None between the recomputed values and the files. All compared values agree with relative difference 0 in this run, well inside 1e-6.
A previous version of this report quoted the M2 file nll as 4.503770939937341; the current M2.csv contains 4.503770939937342, which matches the recomputation exactly.

## Verdict

**Overall: PASS** (M1 PASS, M2 PASS, row-count, shape, column and file-existence checks PASS).
