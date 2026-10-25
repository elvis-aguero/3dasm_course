Both models fitted and independently checked. Deliverables in workspace/results/: fit_M1.py, M1.csv, fit_M2.py, M2.csv, check.md.

Rows (split: 37 train, 13 test, train_test_split random_state=1987):
- M1: a=1.556793, b=0.100360, s=27.983031, coverage=0.846154 (11/13), nll=4.976150, n_train=37, n_test=13
- M2: a=1.380403, b=0.103235, c=0.553231, coverage=0.846154 (11/13), nll=4.503771, n_train=37, n_test=13

Checks: builder reran both scripts (identical output). Checker recomputed both from scratch: PASS for M1 and M2 (spec match, CSV columns, numeric agreement to ~1e-16 relative). Overall PASS.

Falsification: the independent recomputation by the checker is the falsification step; it found no discrepancy. Evaluations used: 0 (no ground-truth evaluator calls; no canonical evaluator registered).

Remaining uncertainty: with only 13 test points, coverage (11/13) is a coarse estimate. Coverage 0.846 is below the nominal 0.95 for both models. The two models are indistinguishable on coverage; M2 has the lower nll (4.504 vs 4.976) on the same 13 test rows. Model choice from this single split is tentative. Some builder/checker reports contained narrative about earlier replies and tool-call errors that I could not verify; the numerical outputs were consistent across builder and checker.