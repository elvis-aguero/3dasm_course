# Check of M1 and M2 (checker, independent recomputation)

Recomputation script: `runs/20261025T194431/debug/delegations/D003/recompute.py` (run with `-I`). It reads only
`data/car_stopping_distance` and the two CSVs. It does not import or run anything from `workspace/results/`.

Procedure, per PROBLEM_STATEMENT.md: `train_test_split(arange(50), train_size=0.75, random_state=1987)`;
M1 lstsq of y on [x, x²] (no intercept); M2 lstsq of y/x on [1, x]; both `std` with ddof=0; coverage on
test rows with mean ± 1.96 sd; nll = mean of −log normal density. PASS means relative difference < 1e-9
(tolerance 1e-9 relative, as the brief requires).

## Split

| Item | Recomputed | CSV M1 | CSV M2 | Result |
|---|---|---|---|---|
| n_train | 37 | 37 | 37 | PASS |
| n_test | 13 | 13 | 13 | PASS |

## Structure of CSVs

| File | Columns | Rows | Result |
|---|---|---|---|
| M1.csv | model,a,b,sd_parameter,coverage,nll,n_train,n_test | 1 | PASS |
| M2.csv | model,a,b,sd_parameter,coverage,nll,n_train,n_test | 1 | PASS |

## M1

| Quantity | Recomputed | CSV | Rel. diff | Result |
|---|---|---|---|---|
| a | 1.556792744461828 | 1.556792744461828 | 0 | PASS |
| b | 0.1003596848656863 | 0.1003596848656863 | 0 | PASS |
| sd_parameter (s) | 27.98303080695783 | 27.98303080695783 | 0 | PASS |
| coverage | 0.8461538461538461 | 0.8461538461538461 | 0 | PASS |
| nll | 4.976149641475804 | 4.976149641475804 | 0 | PASS |

**M1 overall: PASS**

## M2

| Quantity | Recomputed | CSV | Rel. diff | Result |
|---|---|---|---|---|
| a | 1.3804030477145803 | 1.3804030477145803 | 0 | PASS |
| b | 0.10323542514078464 | 0.10323542514078464 | 0 | PASS |
| sd_parameter (c) | 0.5532310661868638 | 0.5532310661868638 | 0 | PASS |
| coverage | 0.8461538461538461 | 0.8461538461538461 | 0 | PASS |
| nll | 4.503770939937342 | 4.503770939937342 | 2.0e-16 | PASS |

**M2 overall: PASS**

## Scripts

- `fit_M1.py` and `fit_M2.py` exist. Both parse as valid Python (`ast.parse`, read only).
- **Not executed.** The coordinator instructed the checker not to run the scripts in `workspace/results/`, so
  "runs" is not verified here. The numerical match above does not depend on them.

## Overall

**PASS (M1), PASS (M2)**. Every quantity matches to floating-point agreement (relative difference at most 2e-16).
No ledgered evaluator calls were made by this check.
