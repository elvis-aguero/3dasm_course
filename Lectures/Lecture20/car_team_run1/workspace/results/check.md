# Check of M1 and M2 (checker)

Independent recomputation from `data/car_stopping_distance` (split `train_test_split(row index, train_size=0.75, random_state=1987)`, 37 train / 13 test), compared with `workspace/results/M1.csv` and `workspace/results/M2.csv`. Tolerance: relative difference below 1e-6. Script: `runs/20261023T191030/debug/delegations/D003/recompute.py` (did not import or run anything in `workspace/results/`).

## M1

| quantity | recomputed | file | rel. diff | verdict |
|---|---|---|---|---|
| a | 1.556792744461828 | 1.556792744461828 | 0.00e+00 | PASS |
| b | 0.1003596848656863 | 0.1003596848656863 | 0.00e+00 | PASS |
| sd_parameter (s) | 27.98303080695783 | 27.98303080695783 | 0.00e+00 | PASS |
| coverage | 0.8461538461538461 | 0.8461538461538461 | 0.00e+00 | PASS |
| nll | 4.976149641475804 | 4.976149641475804 | 0.00e+00 | PASS |
| n_train | 37 | 37 | exact | PASS |
| n_test | 13 | 13 | exact | PASS |

- Schema (header exactly `model,a,b,sd_parameter,coverage,nll,n_train,n_test`, one data row): PASS
- **M1 verdict: PASS**

## M2

| quantity | recomputed | file | rel. diff | verdict |
|---|---|---|---|---|
| a | 1.3804030477145803 | 1.3804030477145803 | 0.00e+00 | PASS |
| b | 0.10323542514078464 | 0.10323542514078464 | 0.00e+00 | PASS |
| sd_parameter (c) | 0.5532310661868638 | 0.5532310661868638 | 0.00e+00 | PASS |
| coverage | 0.8461538461538461 | 0.8461538461538461 | 0.00e+00 | PASS |
| nll | 4.503770939937341 | 4.503770939937342 | 1.97e-16 | PASS |
| n_train | 37 | 37 | exact | PASS |
| n_test | 13 | 13 | exact | PASS |

- Schema (header exactly `model,a,b,sd_parameter,coverage,nll,n_train,n_test`, one data row): PASS
- **M2 verdict: PASS**

## Overall: PASS
