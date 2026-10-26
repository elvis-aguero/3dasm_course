Both models were fitted to the stopping-distance data as specified in PROBLEM_STATEMENT.md. The split is 37 train and 13 test rows, and no decisions were changed.

Results (workspace/results/):
- M1: a=1.556792744461828, b=0.1003596848656863, s=27.98303080695783, coverage=0.8462 (11/13), nll=4.976149641475804, n_train=37, n_test=13.
- M2: a=1.3804030477145803, b=0.10323542514078464, c=0.5532310661868638, coverage=0.8462 (11/13), nll=4.503770939937342, n_train=37, n_test=13.

Files: fit_M1.py, M1.csv, fit_M2.py, M2.csv, check.md.

Checker (independent recomputation, D003): M1 PASS and M2 PASS. Every value matched within relative tolerance 1e-6, and the column headers and row counts were correct. The M2 nll differs from the file only in the last digit.

Evaluations: 0. This is a data-only study, so no ground-truth evaluator was needed. The SETUP notice about a canonical source was not acted on.

Remaining uncertainty: with only 13 test rows, coverage (11/13) and nll are noisy, so the two models cannot be separated on this test split alone. The nll values are not directly comparable across the two models' parametrizations.