# Check of M1 and M2 (checker, delegation D003)

Overall: PASS

Method: I recomputed both models from `data/car_stopping_distance` (ExperimentData.from_file, to_pandas()) with sklearn `train_test_split(row index, train_size=0.75, random_state=1987)`, numpy lstsq, numpy.std (ddof=0), and scipy `norm.logpdf`, following PROBLEM_STATEMENT.md. Recomputation script: `runs/20261025T180937/debug/delegations/D003/checker_recompute.py`. Python: `/Users/harrislab/.local/share/adda-lectures-venv/bin/python -I`. I did not import or run the scripts in `workspace/results/`; I read their source only for the spec-match check. No decisions were changed.

Data: 50 rows, no x equal to zero. Split: 37 train, 13 test.

## M1 — PASS

Spec match (fit_M1.py read against the spec): PASS. Least squares of y on [x, x**2], no intercept, training rows; s = numpy.std(training residuals, ddof=0); mean a*x + b*x**2; sd = s; coverage with 1.96 sd; nll as mean of -log normal density.

| Item | Recomputed (checker) | M1.csv | Rel. diff | Result |
|---|---|---|---|---|
| n_train | 37 | 37 | exact | PASS |
| n_test | 13 | 13 | exact | PASS |
| a | 1.556792744461828 | 1.556792744461828 | 0 | PASS |
| b | 0.1003596848656863 | 0.1003596848656863 | 0 | PASS |
| sd_parameter (s) | 27.98303080695783 | 27.98303080695783 | 0 | PASS |
| coverage | 0.8461538461538461 | 0.8461538461538461 | 0 | PASS |
| nll | 4.976149641475804 | 4.976149641475804 | 0 | PASS |

## M2 — PASS

Spec match (fit_M2.py read against the spec): PASS. Least squares of y/x on [1, x], training rows, gives a and b; c = numpy.std(residuals of y/x, ddof=0); mean a*x + b*x**2; sd = c*x; coverage with 1.96 sd; nll as mean of -log normal density.

| Item | Recomputed (checker) | M2.csv | Rel. diff | Result |
|---|---|---|---|---|
| n_train | 37 | 37 | exact | PASS |
| n_test | 13 | 13 | exact | PASS |
| a | 1.3804030477145803 | 1.3804030477145803 | 0 | PASS |
| b | 0.10323542514078464 | 0.10323542514078464 | 0 | PASS |
| sd_parameter (c) | 0.5532310661868638 | 0.5532310661868638 | 0 | PASS |
| coverage | 0.8461538461538461 | 0.8461538461538461 | 0 | PASS |
| nll | 4.503770939937341 | 4.503770939937342 | 2.0e-16 | PASS |

## CSV format — PASS

Both files have the header exactly `model,a,b,sd_parameter,coverage,nll,n_train,n_test` and exactly one data row each (M1.csv: model M1; M2.csv: model M2).

## Conclusion

Overall PASS. Both models pass spec match, CSV columns, numeric agreement (all relative differences below 1e-6), coverage, and nll.
