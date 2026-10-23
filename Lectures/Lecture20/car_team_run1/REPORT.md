Both models were fit as specified in PROBLEM_STATEMENT.md, with the 37/13 split (train_test_split, random_state=1987). An independent recomputation by the checker (D003) matched both CSVs exactly (max relative difference 0), so the check is PASS for M1 and for M2.

Rows (results/M1.csv and results/M2.csv):
- M1: a=1.556792744461828, b=0.1003596848656863, sd_parameter s=27.98303080695783, coverage=0.8461538461538461 (11/13), nll=4.976149641475804, n_train=37, n_test=13
- M2: a=1.3804030477145803, b=0.10323542514078464, sd_parameter c=0.5532310661868638, coverage=0.8461538461538461 (11/13), nll=4.503770939937342, n_train=37, n_test=13

Deliverables: results/fit_M1.py, results/M1.csv, results/fit_M2.py, results/M2.csv, results/check.md. Each CSV has exactly the specified columns and one data row.

Caveats: the test set is only 13 rows, so coverage (11/13 for both models) is coarse and below the nominal 0.95. The two models are compared on the same 13 test rows. M1's residual sd (about 28 m) is much larger than M2's implied sd at typical speeds (c*x with c≈0.55), so the nll values, which are close, are not strongly separated by this split. No ground-truth evaluator was registered: this is a fixed-dataset fit, and no evaluations were performed. Builder reports mention pre-existing fit_M1.py/M1.csv from an earlier attempt; the current files were re-run and match the checker's independent numbers. A falsification step beyond the checker's independent recomputation was not run, since the spec is a fixed decision set.