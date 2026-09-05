# Hypothesis ledger: two designs, prediction to verdict

For each design: what was registered *before* the data, what the search returned, and the
verdict with the evidence it cites. Straight from `debug/strategizer_notes/hypotheses.json`.

| file | what it is |
|---|---|
| `D9_bowed_longerons.md` | Hypothesis H5, run `20260706T204732`. Prior 0.35, verdict **FALSIFIED** at posterior 0.04. |
| `D9_bowed_longerons_48designs.csv` | The 48 designs, delegation D012. Geometry in, four measured outputs out. |
| `D42_serpentine.md` | Hypotheses H3 and H6, run `20260826T012550`. Both **SUPPORTED**. |
| `D42_serpentine_140designs.csv` | The 140 designs: D005 (80, seed) + D008 (60, extended box). 51 feasible. |
| `D42_serpentine_18imperfection_draws.csv` | The other 18 rows in the store: the same designs re-solved under different random imperfections, not new designs. |

Two things worth knowing before reading the numbers.

**The output contract changed between them.** July's bowed table reports `sigma_crit` from the
Stage-1 eigenvalue. August's serpentine table reports `sigma_peak`, windowed over the Stage-2
response, plus feasibility channels that did not exist in July. The two stress columns are not
the same quantity and should not be compared directly.

**`riks_odb` has been removed** from the CSVs; it held absolute cluster paths.
