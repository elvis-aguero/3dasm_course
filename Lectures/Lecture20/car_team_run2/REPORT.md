Both models fitted per PROBLEM_STATEMENT.md, no decisions changed; 0 ground-truth evals (data-fitting only).

Rows (workspace/results/M1.csv, M2.csv):
- M1: a=1.556792744, b=0.100359685, s=27.98303081, coverage=0.846154 (11/13), nll=4.976150, n_train=37, n_test=13
- M2: a=1.380403048, b=0.103235425, c=0.553231066, coverage=0.846154 (11/13), nll=4.503771, n_train=37, n_test=13

Checks (workspace/results/check.md, checker D003): independent recomputation matched every field of both CSVs within 1e-6 relative (max diff 2e-16); CSV structure correct (one row, required columns); both fit scripts present. Overall: PASS.

Remaining uncertainty: both models give identical coverage on 13 test points, so the test set cannot separate them on coverage; M2 has the lower nll (4.50 vs 4.98), but on 13 points this difference is small. M2's mean uses a,b from the y/x fit, as the spec states. Budget: no evaluations used; the run was a fixed-spec computation, so no further experiment would change these results.