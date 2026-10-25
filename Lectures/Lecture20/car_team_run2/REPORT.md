Both models were fitted per PROBLEM_STATEMENT.md (split 37 train / 13 test, random_state=1987), and the checker independently recomputed both with PASS.

Results (workspace/results/):
- M1: a=1.556793, b=0.100360, s=27.983031, coverage=0.846154 (11/13), nll=4.976150, n_train=37, n_test=13
- M2: a=1.380403, b=0.103235, c=0.553231, coverage=0.846154 (11/13), nll=4.503771, n_train=37, n_test=13

Checks (D003): M1 PASS and M2 PASS. All recomputed values match the files to rel. 2e-16. Both CSVs have exactly the required header and one row. fit_M1.py and fit_M2.py are present. The M2 fit follows the spec literally.

Note: the builder flagged that M2's mean a*x+b*x^2 is inconsistent with the y/x regression. It is not: y/x = a + b*x implies y = a*x + b*x^2, so the mean is consistent. No decisions were changed. 0 ground-truth evaluations were used; this is an analytic study with no evaluator. Remaining uncertainty: n_test=13 is small, so coverage (11/13) and nll are noisy. The two models share the same coverage on this split.