Two stopping-distance models fitted on the fixed 37/13 split (random_state=1987), as specified in PROBLEM_STATEMENT.md. Both were recomputed independently by the checker, which reported PASS.

| model | a | b | sd_parameter | coverage | nll | n_train | n_test |
|---|---|---|---|---|---|---|---|
| M1 | 1.556792744461828 | 0.1003596848656863 | s = 27.98303080695783 | 0.8462 (11/13) | 4.976149641475804 | 37 | 13 |
| M2 | 1.3804030477145803 | 0.10323542514078464 | c = 0.5532310661868638 | 0.8462 (11/13) | 4.503770939937342 | 37 | 13 |

Checks: the checker's recomputed a, b, s or c, coverage, nll, n_train and n_test match the files to within 1e-6 relative (M2 nll differs by 2e-16). Both CSVs have exactly the required header and one data row. Verdict: PASS for both models.

Falsification outcome: the checker's independent recomputation is the falsification step, and it found no discrepancy.

Deliverables in workspace/results/: fit_M1.py, M1.csv, fit_M2.py, M2.csv, check.md.

Remaining uncertainty: the coverage is 11/13 on only 13 test points, so the estimate is very coarse. The nll difference between M1 and M2 (about 0.47 in favour of M2) rests on the same 13 points and is not tested for significance. The setup notice asking for a canonical evaluator was not acted on: this is a data-only fit with no ground-truth evaluator, so nothing was registered. Zero ground-truth evaluations were used. About 2 minutes of the 20-minute budget were used.