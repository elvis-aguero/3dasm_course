Both models fitted per PROBLEM_STATEMENT.md (split train_test_split(row index, 0.75, random_state=1987): 37 train / 13 test; no decisions changed; source-free, 0 ground-truth evals).

Results (workspace/results/):
- M1 (D001): a=1.556792744461828, b=0.1003596848656863, sd_parameter s=27.98303080695783, coverage=0.8462 (11/13), nll=4.976149641475804, n_train=37, n_test=13.
- M2 (D002): a=1.3804030477145803, b=0.10323542514078464, sd_parameter c=0.5532310661868638, coverage=0.8462 (11/13), nll=4.503770939937342, n_train=37, n_test=13.

Deliverables: fit_M1.py, M1.csv, fit_M2.py, M2.csv, check.md.

Check (D003, independent recomputation with its own script, 1e-6 relative tolerance): PASS. All M1 and M2 values match (M2 nll differs at 2e-16 relative); CSV columns exact; one row each; split 37/13 with test indices [2, 8, 12, 19, 22, 24, 33, 34, 38, 41, 43, 46, 48].

Remaining caveats: the builder reported that fit_M1.py, M1.csv and fit_M2.py already existed in workspace/results/ when it started; it verified and re-ran them rather than writing them fresh, and the checker's independent recomputation agrees with the files. Coverage is 11/13 on 13 test points, so it is a coarse estimate. The nll is computed from the mean/sd as specified.