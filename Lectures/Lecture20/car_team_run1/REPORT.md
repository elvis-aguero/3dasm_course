Both models were fit as specified in PROBLEM_STATEMENT.md, and the checker independently recomputed both and got PASS for each.

Rows (workspace/results/):
- M1: a=1.556792744461828, b=0.1003596848656863, s=27.98303080695783, coverage=0.846154 (11/13), nll=4.976149641475804, n_train=37, n_test=13.
- M2: a=1.3804030477145803, b=0.10323542514078464, c=0.5532310661868638, coverage=0.846154 (11/13), nll=4.503770939937342, n_train=37, n_test=13.

Checks: the checker recomputed from scratch and matched every value in both CSVs with relative difference 0 (tolerance 1e-6). Column names, one-row shape, model labels, and the presence of fit_M1.py and fit_M2.py also passed. The verdict is written in check.md.

Deliverables: fit_M1.py, M1.csv, fit_M2.py, M2.csv, check.md, all in workspace/results/. No evaluator calls were made, so there is no ledger to reconcile.

Uncertainties:
- The spec says M2's mean is a*x + b*x**2, but a and b come from a fit of y/x on [1, x]. Read literally, that mixes two different parametrisations. The code follows the text exactly. The checker's remark that this is "the mapping the spec implies" is an interpretation, not a verified fact. Please confirm this is intended.
- Coverage is 11/13 for both models. With 13 test points this is a coarse estimate, and the two models cannot be separated on coverage.
- The builder reran scripts that already existed in the folder rather than writing them fresh. The checker's independent recomputation covers this.