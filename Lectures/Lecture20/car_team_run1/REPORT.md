Both models were fitted as specified in PROBLEM_STATEMENT.md, and an independent recomputation by the checker passed for both.

Results (split: 37 train, 13 test, random_state=1987):
- M1: a=1.556792744461828, b=0.1003596848656863, sd_parameter s=27.98303080695783, coverage=0.8461538461538461 (11/13), nll=4.976149641475804
- M2: a=1.3804030477145803, b=0.10323542514078464, sd_parameter c=0.5532310661868638, coverage=0.8461538461538461 (11/13), nll=4.503770939937342

Checks: the checker (D003) recomputed everything from the data, with its own scripts and with the split indices from scikit-learn. Both CSVs have exactly the required columns and one row each. All numeric values match within 1e-9 relative tolerance; the worst difference is 2e-16. Result: PASS for the split, M1 and M2.

Deliverables in workspace/results/: fit_M1.py, M1.csv, fit_M2.py, M2.csv, check.md.

Evaluations: 0. This is a fit on stored data; no ground-truth evaluator was used. The setup notice about a missing canonical evaluator therefore does not apply to this study.

Uncertainty: the builder reported that fit_M1.py and fit_M2.py already existed when it started, and that an earlier run had failed on an input_datagroup error. The current scripts run cleanly and the checker's independent results agree with them, so this should not affect the numbers. Both models give the same coverage on 13 test rows, so coverage does not separate them; nll is lower for M2 (4.50 vs 4.98).