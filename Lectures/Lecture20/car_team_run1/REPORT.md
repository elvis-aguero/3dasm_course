Both models were fitted per PROBLEM_STATEMENT.md and independently rechecked by the checker. The checker's recomputation matches both CSVs to about 2e-16 relative, well inside the 1e-9 tolerance.

Results (split 37 train / 13 test):
- M1: a = 1.556792744461828, b = 0.1003596848656863, s = 27.98303080695783, coverage = 0.8462 (11/13), nll = 4.976149641475804. Check: PASS.
- M2: a = 1.3804030477145803, b = 0.10323542514078464, c = 0.5532310661868638, coverage = 0.8462 (11/13), nll = 4.503770939937342. Check: PASS.

Files are in workspace/results/: fit_M1.py, M1.csv, fit_M2.py, M2.csv, check.md. Both CSVs have exactly the required columns and one row each. Evaluations used: 0.

Caveats:
1. The checker parsed fit_M1.py and fit_M2.py with ast only and did not run them, so it is not verified that the scripts execute from scratch. The builders did run them, and the M1 and M2 builder outputs agree with the checker's recomputation.
2. The M2 builder overwrote an existing fit_M2.py and M2.csv, and the checker overwrote check.md. The current files are the ones these agents wrote this run.
3. Coverage is 11/13 for both models on only 13 test points, so it is a coarse estimate.

Falsification outcome: no separate falsification was run. The checker's independent recomputation is the only cross-check. Remaining uncertainty is the unrun scripts in caveat 1.