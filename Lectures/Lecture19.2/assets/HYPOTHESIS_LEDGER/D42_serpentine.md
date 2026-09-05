# D42 · Serpentine (wavy in-plane) longeron

**Hypothesis `H3`** &nbsp;·&nbsp; prior **0.35**

## Statement

> A serpentine (S/wavy-path) longeron centerline geometry -- replacing the straight longeron's centerline with a smooth in-plane wavy path -- couples in-plane bending to an out-of-plane bend-twist buckling mode via a double-eigenvalue bifurcation (Shi, Huang, Yu and Li 2024), accessing a different, higher-capacity post-buckling energy-storage channel than a single continuously-bending straight member, and can therefore exceed sigma_peak >= 0.2244 kPa at a feasible (mcs>=0.80, windowed mls<=2%, non-folding, no ring-passthrough), beam-valid (slenderness>=10), PLA-printable point.

## Registered prediction

> Best-found feasible sigma_peak in the serpentine family's campaign >= 0.2244 kPa, with a measurable out-of-plane/twist energy fraction confirming the coupled-mode mechanism (not plain bending) is what is being exploited.

## Falsification criterion

> An adequately-powered exploration (BO/DoE sized to the family's free-parameter dimensionality: wave amplitude, wavelength/number of undulations, cross-section, taper, storey pitch; pre-committed budget) finds no feasible design reaching sigma_peak >= 0.2244 kPa, or finds the mechanism collapses to ordinary in-plane bending (out-of-plane/twist mode fraction near zero) rather than engaging the coupled bend-twist channel the mechanism claims.

## Status log

### `OPEN`  &nbsp;·&nbsp; posterior 0.35  &nbsp;·&nbsp; 2026-08-26

initial proposal

### `SUPPORTED`  &nbsp;·&nbsp; posterior 0.75  &nbsp;·&nbsp; 2026-08-26

Adequate test: D005 ran the pre-committed 80-Stage-2-eval zoom-BO campaign (dimensionality-sized to the 6 free serpentine params) over the full parameter box. Neither disqualifying condition in the falsification criterion triggered: (1) 15/24 converged designs are strictly feasible (oracle feasible=True, self_clearance>0, non-near-zero mls) and the best reaches sigma_peak=0.56388 kPa = 2.51x the 0.2244 target; (2) all 15 feasible designs show serpentine_out_of_plane_fraction in [0.1565,0.1592] -- consistently non-zero, confirming the coupled bend-twist channel is genuinely engaged, not degenerating to plain in-plane bending. Residual uncertainty carried forward, not hidden: (a) the best feasible point sits at 0.93x the incumbent run17_rectangle floor (0.6077 kPa), so it clears the 2x-Bessa objective floor decisively but has not yet beaten the study's best; (b) within the feasible set, out-of-plane fraction does NOT rank-correlate with sigma_peak (all cluster ~0.16 despite objective spread 0.044-0.564), so the evidence that MORE coupling drives higher capacity is weak -- the mechanism is engaged, but its magnitude is not yet shown to be the causal lever; (c) best design sits near the ratio_b/ratio_a lower bound, flagged by campaign_summary as unmeasured territory, not a mapped optimum.

```
{
  "delegation": "D005",
  "numbers": {
    "best_feasible_sigma_peak": 0.563879,
    "n_strict_feasible": 15,
    "n_stage2_converged": 24,
    "out_of_plane_fraction_range": [
      0.1565,
      0.1592
    ],
    "target_0.2244_cleared": true,
    "floor_0.6077_cleared": false
  }
}
```

*Verdict validator:* validated: no charter concern

### `SUPPORTED`  &nbsp;·&nbsp; posterior 0.7  &nbsp;·&nbsp; 2026-08-26

CALIBRATION REFINEMENT (post adversarial review): the falsification criterion (feasible design >=0.2244 kPa with non-degenerate out-of-plane fraction) remains met and SUPPORTED stands. However, D005's own report notes that within the feasible set, out-of-plane fraction does NOT rank-correlate with sigma_peak (all cluster ~0.16 despite objective spread 0.044-0.564) -- so while the coupled bend-twist mode is genuinely engaged (satisfying the registered prediction), the STRONGER unregistered claim that coupling MAGNITUDE causally drives the performance gain is not demonstrated by a dose-response relationship in this data, and an alternative explanation (ordinary BO tuning of the already-anisotropic cross-section) cannot be ruled out. Posterior lowered slightly to reflect this calibration; the notebook (hypotheses/verdict cells) now discloses this explicitly rather than overclaiming a proven causal mechanism.

```
{
  "delegation": "D005",
  "numbers": {
    "out_of_plane_fraction_range": [
      0.1565,
      0.1592
    ],
    "objective_spread_feasible": [
      0.044,
      0.564
    ]
  }
}
```

*Verdict validator:* validated: no charter concern


---

# D42 (continued) · H6, the extended parameter box

**Hypothesis `H6`** &nbsp;·&nbsp; prior **0.25**

## Statement

> Extending the serpentine family's parameter box toward smaller ratio_a/ratio_b (thinner cross-section, informed by D005's finding that its best feasible design sits at the tested box's lower boundary) and a wider amplitude_rel range can find a serpentine design that meets or exceeds the incumbent run17_rectangle floor of 0.6077 kPa while remaining feasible (mcs>=0.80, windowed mls<=2%) and non-folding.

## Registered prediction

> Best-found feasible sigma_peak in the extended-box campaign >= 0.6077 kPa.

## Falsification criterion

> An adequately-powered follow-up search (budget sized to the 6 free params, pre-committed ~60 evals) over the extended box finds no feasible design reaching sigma_peak >= 0.6077 kPa.

## Status log

### `OPEN`  &nbsp;·&nbsp; posterior 0.25  &nbsp;·&nbsp; 2026-08-26

initial proposal

### `SUPPORTED`  &nbsp;·&nbsp; posterior 0.9  &nbsp;·&nbsp; 2026-08-26

Adequate test: D008 ran the pre-committed 60-new-eval extended-box zoom-BO follow-up (seeded with D005's 80 rows, dispatched via SlurmAsyncPool/zoom_core through get_evaluator(namespace='serpentine')). Prediction directly confirmed: best feasible design now reaches sigma_peak=0.64605 kPa (mcs=0.9286>=0.80, mls=0.0190<=0.02, converged, feasible, ring_passthrough=False, self_clearance=38.5mm) -- 1.06x the 0.6077 kPa incumbent floor and 2.88x the 0.2244 target. Notably the winning point (ratio_pitch=0.5327, ratio_top_diameter=0.1298, ratio_a=0.006221, ratio_b=0.020331, amplitude_rel=0.03164, n_undulations=2) sits INSIDE D005's original box -- the gain came from more targeted zoom-BO exploitation around the seeded incumbent, not from the newly-opened boundary; 8 candidates did probe the extended boundary and none beat 0.23 kPa, an informative negative on the extension itself (reported honestly, not hidden). The serpentine mechanism (H1/H3's genuinely novel bend-twist coupled longeron) is now the run's best-found design overall, beating the historical incumbent run17_rectangle.

```
{
  "delegation": "D008",
  "numbers": {
    "best_objective_sigma_peak": 0.64605,
    "best_vs_floor_ratio": 1.063,
    "best_vs_target_ratio": 2.879,
    "n_strict_feasible_new": 36
  }
}
```

*Verdict validator:* validated: no charter concern


## The design table

`D42_serpentine_140designs.csv` — 140 rows: delegation **D005** (80, seed campaign, H3) and **D008** (60, extended box, H6). 15 + 36 = 51 feasible.

The run's store holds 158 serpentine rows. The extra 18 are **D009 (9)** and **D011 (9)**: imperfection-robustness draws, the same design re-solved under different random imperfections, not new designs. They are in `D42_serpentine_18imperfection_draws.csv`.
