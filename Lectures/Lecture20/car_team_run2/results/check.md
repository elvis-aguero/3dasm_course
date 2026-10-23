# Independent check of M1 and M2 (checker, D003)

Recomputed in `runs/20261023T165208/debug/delegations/D003/recompute.py` from `data/car_stopping_distance` (ExperimentData.from_file, to_pandas). Split: train_test_split(row index 0..49, train_size=0.75, random_state=1987) -> n_train=37, n_test=13. No ground-truth evaluator used; `results/fit_M1.py` and `results/fit_M2.py` not run.

Tolerance: relative difference below 1e-6 (np.isclose rtol=1e-6).

## M1

- CSV columns exactly `model, a, b, sd_parameter, coverage, nll, n_train, n_test`: PASS
- CSV has exactly one data row: PASS

| quantity | recomputed | CSV | abs diff | rel diff | within 1e-6 |
|---|---|---|---|---|---|
| a | 1.556792744461828 | 1.556792744461828 | 0.000e+00 | 0.000e+00 | yes |
| b | 0.1003596848656863 | 0.1003596848656863 | 0.000e+00 | 0.000e+00 | yes |
| sd_parameter (s) | 27.98303080695783 | 27.98303080695783 | 0.000e+00 | 0.000e+00 | yes |
| coverage | 0.8461538461538461 | 0.8461538461538461 | 0.000e+00 | 0.000e+00 | yes |
| nll | 4.976149641475804 | 4.976149641475804 | 0.000e+00 | 0.000e+00 | yes |
| n_train | 37.0 | 37.0 | 0.000e+00 | 0.000e+00 | yes |
| n_test | 13.0 | 13.0 | 0.000e+00 | 0.000e+00 | yes |

**M1 verdict: PASS**

## M2

- CSV columns exactly `model, a, b, sd_parameter, coverage, nll, n_train, n_test`: PASS
- CSV has exactly one data row: PASS

| quantity | recomputed | CSV | abs diff | rel diff | within 1e-6 |
|---|---|---|---|---|---|
| a | 1.3804030477145803 | 1.3804030477145803 | 0.000e+00 | 0.000e+00 | yes |
| b | 0.10323542514078464 | 0.10323542514078464 | 0.000e+00 | 0.000e+00 | yes |
| sd_parameter (c) | 0.5532310661868638 | 0.5532310661868638 | 0.000e+00 | 0.000e+00 | yes |
| coverage | 0.8461538461538461 | 0.8461538461538461 | 0.000e+00 | 0.000e+00 | yes |
| nll | 4.503770939937341 | 4.503770939937342 | 8.882e-16 | 1.972e-16 | yes |
| n_train | 37.0 | 37.0 | 0.000e+00 | 0.000e+00 | yes |
| n_test | 13.0 | 13.0 | 0.000e+00 | 0.000e+00 | yes |

**M2 verdict: PASS**

**Overall verdict: PASS**
