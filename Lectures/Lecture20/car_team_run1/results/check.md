# Independent check of M1 and M2 (checker, D003)

Recomputed from `data/car_stopping_distance` (ExperimentData.from_file, to_pandas()), split `train_test_split(row index, train_size=0.75, random_state=1987)`: n_train = 37.0, n_test = 13.0. Tolerance: relative 1e-6 on numbers, exact on counts. The CSV header must be exactly `model,a,b,sd_parameter,coverage,nll,n_train,n_test`. The script is in the delegation folder (`check_indep.py`, `compare.py`). `results/fit_M1.py` and `results/fit_M2.py` were not read.

## M1

- Column header: `model,a,b,sd_parameter,coverage,nll,n_train,n_test` -> PASS; data rows: 1 -> PASS

| quantity | independent | CSV | rel. diff | result |
|---|---|---|---|---|
| a | 1.556792744461828 | 1.556792744461828 | 0.000e+00 | PASS |
| b | 0.1003596848656863 | 0.1003596848656863 | 0.000e+00 | PASS |
| sd_parameter | 27.98303080695783 | 27.98303080695783 | 0.000e+00 | PASS |
| coverage | 0.8461538461538461 | 0.8461538461538461 | 0.000e+00 | PASS |
| nll | 4.976149641475804 | 4.976149641475804 | 0.000e+00 | PASS |
| n_train | 37.0 | 37 | exact | PASS |
| n_test | 13.0 | 13 | exact | PASS |

max relative difference (numbers): 0.000e+00; **M1: PASS**

## M2

- Column header: `model,a,b,sd_parameter,coverage,nll,n_train,n_test` -> PASS; data rows: 1 -> PASS

| quantity | independent | CSV | rel. diff | result |
|---|---|---|---|---|
| a | 1.3804030477145803 | 1.3804030477145803 | 0.000e+00 | PASS |
| b | 0.10323542514078464 | 0.10323542514078464 | 0.000e+00 | PASS |
| sd_parameter | 0.5532310661868638 | 0.5532310661868638 | 0.000e+00 | PASS |
| coverage | 0.8461538461538461 | 0.8461538461538461 | 0.000e+00 | PASS |
| nll | 4.503770939937342 | 4.503770939937342 | 0.000e+00 | PASS |
| n_train | 37.0 | 37 | exact | PASS |
| n_test | 13.0 | 13 | exact | PASS |

max relative difference (numbers): 0.000e+00; **M2: PASS**

## Overall: **PASS**
