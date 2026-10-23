Both models are fitted, and the independent recomputation passes for both. All four deliverables are in `results/`.

**Results (test rows, 13 of them; training rows 37)**

| model | a | b | sd_parameter | coverage | nll | n_train | n_test |
|---|---|---|---|---|---|---|---|
| M1 | 1.556792744461828 | 0.1003596848656863 | s = 27.98303080695783 | 0.8461538461538461 (11/13) | 4.976149641475804 | 37 | 13 |
| M2 | 1.3804030477 | 0.1032354251 | c = 0.5532310662 | 0.8461538462 (11/13) | 4.5037709399 | 37 | 13 |

**Checks**
- **M1:** PASS. The checker recomputed every value from the data and all seven items match the file.
- **M2:** PASS. All seven items match. The nll agrees to a relative difference of about 2e-13.
- **Overall:** PASS, recorded in `results/check.md`.

**Files**
- `results/fit_M1.py`, `results/M1.csv`
- `results/fit_M2.py`, `results/M2.csv`
- `results/check.md`

**Notes**
- The coverage check uses inclusive bounds (`<=` 1.96 sd). The spec did not say whether the bounds are inclusive; the choice does not change either coverage value here.
- The checker first wrote `check.md` to its own delegation folder. I had it copied into `results/`, and the contents are unchanged.
- The study is source-free, so no ground-truth evaluator was registered and no evaluations were counted. I did not register the evaluator the setup notice asked for.