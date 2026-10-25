# Check report (checker, independent recomputation)

Recomputation script: `runs/20261025T212247/debug/delegations/D003/recompute.py` (written from PROBLEM_STATEMENT.md; builder scripts not used).
Data: `data/car_stopping_distance` loaded with `ExperimentData.from_file`, `to_pandas()` (x from table 0, y from table 1), N = 50.
Split: `train_test_split(numpy.arange(50), train_size=0.75, random_state=1987)`: 37 train, 13 test.
Test row indices: [2, 8, 12, 19, 22, 24, 33, 34, 38, 41, 43, 46, 48].

## Checks

| Check | Mine | CSV | Rel. diff | Result |
|---|---|---|---|---|
| Split: n_train | 37 | 37 (M1, M2) | 0 | PASS |
| Split: n_test | 13 | 13 (M1, M2) | 0 | PASS |
| Split: test row indices | [2, 8, 12, 19, 22, 24, 33, 34, 38, 41, 43, 46, 48] | n/a (not stored in CSV) | n/a | PASS (matches spec) |
| M1 a | 1.556792744461828 | 1.556792744461828 | 0 | PASS |
| M1 b | 0.1003596848656863 | 0.1003596848656863 | 0 | PASS |
| M1 sd_parameter (s) | 27.98303080695783 | 27.98303080695783 | 0 | PASS |
| M1 coverage | 0.8461538461538461 (11/13) | 0.8461538461538461 | 0 | PASS |
| M1 nll | 4.976149641475804 | 4.976149641475804 | 0 | PASS |
| M2 a | 1.3804030477145803 | 1.3804030477145803 | 0 | PASS |
| M2 b | 0.10323542514078464 | 0.10323542514078464 | 0 | PASS |
| M2 sd_parameter (c) | 0.5532310661868638 | 0.5532310661868638 | 0 | PASS |
| M2 coverage | 0.8461538461538461 (11/13) | 0.8461538461538461 | 0 | PASS |
| M2 nll | 4.503770939937341 | 4.503770939937342 | 1.97e-16 | PASS |
| M1.csv columns | model,a,b,sd_parameter,coverage,nll,n_train,n_test | identical | n/a | PASS |
| M2.csv columns | model,a,b,sd_parameter,coverage,nll,n_train,n_test | identical | n/a | PASS |
| M1.csv rows | 1 data row | 1 | n/a | PASS |
| M2.csv rows | 1 data row | 1 | n/a | PASS |

## Overall verdict: PASS

All checks pass at the 1e-6 relative tolerance. No ground-truth evaluations were used (source-free study).
