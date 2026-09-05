# D9 · Radially bowed (pre-curved) longerons

**Hypothesis `H5`** &nbsp;·&nbsp; prior **0.35**

## Statement

> Radially pre-curved (bowed) longerons -- each of the 3 longerons follows a smooth radial offset as a function of height (zero at both rigid-ring attachments, maximum inward bow at mid-height), preserving circular rings and 3-fold rotational symmetry -- geometrically pre-conditions the coiling deformation path, allowing a stiffer cross-section (larger ratio_b) to retain Riks max_compressive_strain>=0.90 where it currently collapses, thereby clearing sigma_cr,nd>=0.7288 kPa.

## Registered prediction

> At a fixed larger ratio_b (e.g. 0.03-0.05) that currently fails max_compressive_strain>=0.90 at bow_amplitude=0, increasing bow_amplitude restores max_compressive_strain above 0.90 while sigma_crit stays well above baseline, and at least one such design clears the 0.7288 kPa floor with max_local_strain<=0.02.

## Falsification criterion

> A joint search (>=40 oracle evals) over bow_amplitude (0 to ~0.15*D1) combined with ratio_a/ratio_b/ratio_pitch/ratio_top_diameter finds no design meeting all 3 feasibility criteria with sigma_cr,nd>=0.7288 kPa, and max_compressive_strain does not improve with bow_amplitude at matched (larger than 0.0188) ratio_b relative to bow_amplitude=0.

## Status log

### `OPEN`  &nbsp;·&nbsp; posterior 0.35  &nbsp;·&nbsp; 2026-07-07

initial proposal

### `FALSIFIED`  &nbsp;·&nbsp; posterior 0.04  &nbsp;·&nbsp; 2026-07-07

Two lines of evidence, together adequate under Charter Sec2/Sec3. (1) MECHANISM (the registered claim's causal core -- "increasing bow_amplitude restores max_compressive_strain"): D011's validation ran a CLEAN, CONFOUND-FREE, matched-conditions diagnostic -- a single-variable dose-response sweep of bow_amplitude in {0,0.05,0.10,0.15} at FIXED ratio_b=0.03 (a stiffer cross-section chosen specifically because it fails mcs at bow=0), plus a second matched point at the winning cross-section (ratio_b=0.018754) with bow=0.05. Both show max_compressive_strain DECREASING monotonically and substantially with bow_amplitude (0.5846->0.3040 at ratio_b=0.03, a 48% relative drop; 0.9999->0.5007 at the winning cross-section) -- the exact OPPOSITE of the registered prediction. This is a controlled, directed comparison (not a surrogate-guided search) and needs no CV check to be adequate -- it is a designed experiment directly testing the causal claim, analogous to the prior run's accepted H6/H4 decorrelated 1D-sweep mechanism falsifications. (2) EXISTENCE (corroborating, not required for the verdict): D012's follow-up 48-eval joint 5D constrained-BO search (bow_amplitude, ratio_a, ratio_b, ratio_pitch, ratio_top_diameter) found only 1/48 feasible design, at sigma_crit=0.0756 kPa -- far below both baseline and floor -- and the bow_amplitude-vs-mcs correlation across this noisier joint sample remains negative (Spearman rho=-0.163), consistent with (2) direction even though not itself significant due to confounding by the other 4 free dimensions. The sigma_crit objective GP was clearly above chance (mean-fold R^2=0.995) confirming the search was not blind; the constraint surrogates were not above chance (an expected consequence of the same near-empty-feasible-region signature seen in H3), but this does not undermine the verdict since the verdict rests on (1)'s clean, surrogate-free, directly causal mechanism test, not on (2)'s search-based existence coverage. Per Charter Sec3/Sec4: adequate test of the exact registered mechanism, prediction directly and decisively contradicted -> FALSIFIED.

```
{
  "delegation": "D011",
  "numbers": {
    "mcs_at_ratio_b_0.03_bow_0.00": 0.5846,
    "mcs_at_ratio_b_0.03_bow_0.15": 0.304,
    "mcs_at_winning_bow_0.00": 0.9999199046081476,
    "mcs_at_winning_bow_0.05": 0.5007
  }
}
```

*Verdict validator:* validated: no charter concern

## The design table

`D9_bowed_longerons_48designs.csv` — 48 rows, delegation D012, run `20260706T204732`. Design variables plus the four measured outputs.
