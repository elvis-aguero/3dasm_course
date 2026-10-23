Both models are fitted and the independent check passed for both. Deliverables are in `results/`.

| Model | a | b | sd_parameter | coverage | nll | n_train | n_test |
|---|---|---|---|---|---|---|---|
| M1 | 1.556792744461828 | 0.1003596848656863 | s = 27.98303080695783 | 0.8461538 (11/13) | 4.976149641475804 | 37 | 13 |
| M2 | 1.3804030477145803 | 0.10323542514078464 | c = 0.5532310661868638 | 0.8461538 (11/13) | 4.503770939937342 | 37 | 13 |

**Checks:**
- **M1: PASS.** The checker recomputed every value from the data and matched the file to within 1e-6 relative, with the same column set and 37/13 rows.
- **M2: PASS.** Same result: all values match, with one NLL difference of 2.2e-16.
- **Overall: PASS.** The checker's verdict is in `results/check.md`.

Both models cover 11 of 13 test stops, below the nominal 95%. With 13 test rows this gap is not conclusive. On NLL, M2 (4.50) scores better than M1 (4.98) on the same 13 test stops.

The run used 0 ground-truth evaluations. The setup notice asking for an evaluator registration does not apply: this is a data fit, not an evaluation, so I did not register one.