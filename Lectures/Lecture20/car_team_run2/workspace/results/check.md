# Independent check: M1 and M2 (checker, D003)

Recomputed in `runs/20261023T191251/debug/delegations/D003/recompute.py` from `data/car_stopping_distance` (ExperimentData.from_file, to_pandas), split train_test_split(row index, train_size=0.75, random_state=1987). The fit scripts in `workspace/results/` were not imported or run. Evaluator calls: 0.

Tolerance: relative difference < 1e-6 for real values; exact equality for integer counts.

| Check | Model | Recorded (CSV) | Recomputed | Rel. diff | Result |
|---|---|---|---|---|---|
| M1.csv columns and one data row | M1 | ['model', 'a', 'b', 'sd_parameter', 'coverage', 'nll', 'n_train', 'n_test'], 1 row(s) | ['model', 'a', 'b', 'sd_parameter', 'coverage', 'nll', 'n_train', 'n_test'], 1 row | - | PASS |
| n_train | M1 | 37.0 | 37.0 | 0.00e+00 | PASS |
| n_test | M1 | 13.0 | 13.0 | 0.00e+00 | PASS |
| a | M1 | 1.556792744461828 | 1.556792744461828 | 0.00e+00 | PASS |
| b | M1 | 0.1003596848656863 | 0.1003596848656863 | 0.00e+00 | PASS |
| sd_parameter | M1 | 27.98303080695783 | 27.98303080695783 | 0.00e+00 | PASS |
| coverage | M1 | 0.8461538461538461 | 0.8461538461538461 | 0.00e+00 | PASS |
| nll | M1 | 4.976149641475804 | 4.976149641475804 | 0.00e+00 | PASS |
| M2.csv columns and one data row | M2 | ['model', 'a', 'b', 'sd_parameter', 'coverage', 'nll', 'n_train', 'n_test'], 1 row(s) | ['model', 'a', 'b', 'sd_parameter', 'coverage', 'nll', 'n_train', 'n_test'], 1 row | - | PASS |
| n_train | M2 | 37.0 | 37.0 | 0.00e+00 | PASS |
| n_test | M2 | 13.0 | 13.0 | 0.00e+00 | PASS |
| a | M2 | 1.3804030477145803 | 1.3804030477145803 | 0.00e+00 | PASS |
| b | M2 | 0.10323542514078464 | 0.10323542514078464 | 0.00e+00 | PASS |
| sd_parameter | M2 | 0.5532310661868638 | 0.5532310661868638 | 0.00e+00 | PASS |
| coverage | M2 | 0.8461538461538461 | 0.8461538461538461 | 0.00e+00 | PASS |
| nll | M2 | 4.503770939937342 | 4.503770939937341 | 1.97e-16 | PASS |

Overall: PASS
