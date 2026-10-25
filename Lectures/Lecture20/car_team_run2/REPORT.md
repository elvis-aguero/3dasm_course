Both models fitted per PROBLEM_STATEMENT.md (37 train / 13 test, split random_state=1987) and independently rechecked: checker verdict PASS for M1 and M2.

Rows (workspace/results/M1.csv, M2.csv):
- M1: a=1.556793, b=0.100360, s=27.983031, coverage=0.846154 (11/13), nll=4.976150, n_train=37, n_test=13
- M2: a=1.380403, b=0.103235, c=0.553231, coverage=0.846154 (11/13), nll=4.503771, n_train=37, n_test=13

Checks: builder reran both scripts (exit 0). Checker recomputed from scratch without reusing the scripts; all values match the CSVs (M2 nll differs by 2e-16 relative). Column headers and one-row format confirmed.

Falsification: the independent recomputation serves as the check; no further falsification attempted. Evaluations used: 0.

Remaining uncertainty: coverage is based on only 13 test points, so 11/13 has a wide sampling error and cannot separate M1 from M2. The nll gap (M2 lower by about 0.47) comes from one split only and was not tested across seeds.

Deliverables: workspace/results/fit_M1.py, fit_M2.py, M1.csv, M2.csv, check.md.