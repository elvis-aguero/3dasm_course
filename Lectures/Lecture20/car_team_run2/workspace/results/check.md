# Check of M1 and M2

Checker: independent recompute (D003/compare.py), from PROBLEM_STATEMENT.md decisions. Split: train_test_split(row index, train_size=0.75, random_state=1987): 37 train, 13 test rows (of 50). Formulas: M1 lstsq y on [x, x^2] (no intercept), s=std ddof=0 of train residuals, mean a x + b x^2, sd s. M2 lstsq y/x on [1, x], c=std ddof=0 of residuals of y/x, mean a x + b x^2, sd c x. Coverage = fraction of test y in mean +- 1.96 sd; nll = mean of -log normal density. Tolerance rel 1e-6.

Checks performed: row counts of train/test; CSV column names exact; one data row each; a, b, sd_parameter, coverage, nll, n_train, n_test compared.

## Verdict

- M1: PASS
- M2: PASS

## M1

- Header check (exact `model,a,b,sd_parameter,coverage,nll,n_train,n_test`): PASS (file: `model,a,b,sd_parameter,coverage,nll,n_train,n_test`)
- Row count: 1 data row(s): PASS

| Item | File | Recomputed | Rel diff | Result |
|---|---|---|---|---|
| a | 1.556792744461828 | 1.556792744461828 | 0.00e+00 | PASS |
| b | 0.1003596848656863 | 0.1003596848656863 | 0.00e+00 | PASS |
| sd_parameter | 27.98303080695783 | 27.98303080695783 | 0.00e+00 | PASS |
| coverage | 0.8461538461538461 | 0.8461538461538461 | 0.00e+00 | PASS |
| nll | 4.976149641475804 | 4.976149641475804 | 0.00e+00 | PASS |
| n_train | 37.0 | 37.0 | 0.00e+00 | PASS |
| n_test | 13.0 | 13.0 | 0.00e+00 | PASS |

**M1 overall: PASS**

## M2

- Header check (exact `model,a,b,sd_parameter,coverage,nll,n_train,n_test`): PASS (file: `model,a,b,sd_parameter,coverage,nll,n_train,n_test`)
- Row count: 1 data row(s): PASS

| Item | File | Recomputed | Rel diff | Result |
|---|---|---|---|---|
| a | 1.3804030477145803 | 1.3804030477145803 | 0.00e+00 | PASS |
| b | 0.10323542514078464 | 0.10323542514078464 | 0.00e+00 | PASS |
| sd_parameter | 0.5532310661868638 | 0.5532310661868638 | 0.00e+00 | PASS |
| coverage | 0.8461538461538461 | 0.8461538461538461 | 0.00e+00 | PASS |
| nll | 4.503770939937342 | 4.503770939937341 | 1.97e-16 | PASS |
| n_train | 37.0 | 37.0 | 0.00e+00 | PASS |
| n_test | 13.0 | 13.0 | 0.00e+00 | PASS |

**M2 overall: PASS**

