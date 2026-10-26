# Check of M1 and M2 (checker D003)

Split: train 37, test 13 (expected 37 / 13): PASS

Test indices (recomputed): [2, 8, 12, 19, 22, 24, 33, 34, 38, 41, 43, 46, 48]

## M1
- CSV columns exactly ['model', 'a', 'b', 'sd_parameter', 'coverage', 'nll', 'n_train', 'n_test']: PASS (found ['model', 'a', 'b', 'sd_parameter', 'coverage', 'nll', 'n_train', 'n_test'])
- one row with model='M1': PASS (rows=1)

| field | CSV | recomputed | rel diff | result |
|---|---|---|---|---|
| a | 1.556792744461828 | 1.556792744461828 | 0.000e+00 | PASS |
| b | 0.1003596848656863 | 0.1003596848656863 | 0.000e+00 | PASS |
| sd_parameter | 27.98303080695783 | 27.98303080695783 | 0.000e+00 | PASS |
| coverage | 0.8461538461538461 | 0.8461538461538461 | 0.000e+00 | PASS |
| nll | 4.976149641475804 | 4.976149641475804 | 0.000e+00 | PASS |
| n_train | 37 | 37.0 | 0.000e+00 | PASS |
| n_test | 13 | 13.0 | 0.000e+00 | PASS |

**M1: PASS** (see table)

## M2
- CSV columns exactly ['model', 'a', 'b', 'sd_parameter', 'coverage', 'nll', 'n_train', 'n_test']: PASS (found ['model', 'a', 'b', 'sd_parameter', 'coverage', 'nll', 'n_train', 'n_test'])
- one row with model='M2': PASS (rows=1)

| field | CSV | recomputed | rel diff | result |
|---|---|---|---|---|
| a | 1.3804030477145803 | 1.3804030477145803 | 0.000e+00 | PASS |
| b | 0.10323542514078464 | 0.10323542514078464 | 0.000e+00 | PASS |
| sd_parameter | 0.5532310661868638 | 0.5532310661868638 | 0.000e+00 | PASS |
| coverage | 0.8461538461538461 | 0.8461538461538461 | 0.000e+00 | PASS |
| nll | 4.503770939937342 | 4.503770939937341 | 1.972e-16 | PASS |
| n_train | 37 | 37.0 | 0.000e+00 | PASS |
| n_test | 13 | 13.0 | 0.000e+00 | PASS |

**M2: PASS** (see table)

Overall: PASS
