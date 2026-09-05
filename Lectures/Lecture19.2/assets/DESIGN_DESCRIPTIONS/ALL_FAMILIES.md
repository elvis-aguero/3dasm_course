# Design families: what each one was, and what could be varied

All 46 families the campaign proposed. For each: the idea, its grounding, the free
design variables with bounds, what was held fixed, and the verdict.

Quoted from `assets/slides.md` in `bessagroup/f3dasm-agentic-benchmarks`, one idea slide per
family. Nothing is paraphrased.

---

## How to read this file

Six things will mislead you otherwise.

**`circular=N` does not mean the section is circular.** It is an integer selecting a
cross-section family, and only `circular=1` is actually a circle:

| | | | | | |
|---|---|---|---|---|---|
| 0 generalized | 1 **circular** | 2 elliptical | 3 box | 4 laced | 5 cellular |
| 6 tapered | 7 tensegrity | 8 ibeam | 9 chiral_brace | 10 chiral_serpentine | 11 chained_arch |
| 12 twisted_strip | 13 meander_fractal | 14 chiral_helix | 15 bistable_arch | 16 aperiodic_brace | 17 tape_spring |
| 18 leaf_spring | | | | | |

Worse: `circular=2`, the most common value here, is called *elliptical* but is built from
Abaqus's `RectangularProfile`, because Abaqus 2024 has no native `EllipticalProfile`. The
section is a rectangle. Two layers of misnomer on the same variable.

**`D1` is two different things.** It is the ID of the first family (pretwisted longerons) and
also the symbol for the mast's bottom diameter, fixed at 100 mm. When you read `amplitude_rel
/ D1` or `storey height / D1`, that is the diameter, not a reference to family D1.

**Three baselines appear, in different units.** `75.1 kPa/longeron` (D1) and `65.3
kPa/longeron` (D4) are from the early eigenvalue metric. `0.7704 kPa` (D24) is the later
windowed `sigma_peak` metric. **They are not comparable**; the metric was redefined on
2026-08-06.

**"Grounding: common sense" is not dismissive.** It is the study's term for a mechanistic
argument made from first principles rather than from a citation. Roughly a third of the
families are grounded that way, mostly the early ones.

**The IDs skip 45, 46 and 47.** Those were retired, not lost. 46 families, numbered 1 to 44
plus 48 and 49.

**Verdict tags** come in two slots, evidence strength then result, sometimes with a free-text
mechanism phrase after. Counts across this file:

| tag | uses |
|---|---|
| `POWERED` | 16 |
| `DEAD-END` | 13 |
| `REFUTED` | 11 |
| `INCONCLUSIVE` | 10 |
| `UNKNOWN-NO-EVIDENCE` | 6 |
| `FALSIFIED` | 6 |
| `BLOCKED` | 5 |
| `SUPPORTED` | 5 |
| `UNDERPOWERED` | 4 |
| `WEAK` | 4 |
| `FERTILE-PARAMETRIC` | 3 |
| `FERTILE-REWORK` | 3 |
| `WORKS` | 2 |
| `UNTESTABLE` | 2 |
| `VALIDATED` | 2 |
| `DISQUALIFIED` | 1 |

Read them as: *POWERED* enough evidence to conclude · *UNDERPOWERED* ran, too little ·
*BLOCKED* produced no data at all · *VALIDATED*/*SUPPORTED* the hypothesis held ·
*REFUTED*/*FALSIFIED* it did not · *WORKS* the design actually beat the incumbent ·
*FERTILE-\** worth another attempt, with new bounds or a new implementation ·
*DEAD-END* not worth returning to.

**Two pairs are not clearly distinguished by usage**, so do not read significance into which
one appears: REFUTED against FALSIFIED, and VALIDATED against SUPPORTED.

Some entries also point at "see notes", "see Timeline" or a prior family's outcome. Those
sections live in the source deck, not in this file.

---

## D1 · Pretwisted longerons

**The idea.** Added a helical pre-twist (twist_angle from π/6 up to π) to each longeron of the standard 3-longeron mast, on top of the full 7D Bessa cross-section search, to see whether twisting the legs could beat the 75.1 kPa/longeron study floor.

**Grounding.** common sense mechanistic hypothesis (not a literature citation) — the idea that a pre-twisted leg might exploit a shorter effective pitch and reach a higher coiling-mode eigenvalue.

**Design variables.**

```
twist_angle∈[0,π]. ratio_area∈[1.17e-5,4.1e-3], ratio_Ixx∈
[1e-7,1.4e-6], ratio_Iyy∈[1e-7,1.4e-6], ratio_J∈[1e-6,7.77e-6] — generalized
cross-section moments (Bessa's own 7D parametrization). ratio_pitch∈[.25,1.5],
ratio_top_diameter∈[0,.8], ratio_shear_modulus∈[.334,.45]. Fixed: n_longerons=3.
```

**Verdict.** INCONCLUSIVE · DEAD-END

---

## D2 · Extended-J hollow/cellular longeron

**The idea.** Pushed torsional-stiffness ratio_J beyond the Bessa 7D dataset's own max (7.77e-6) — hollow/cellular cross-sections (e.g. a hollow tube) unreachable by any solid Bessa-parametrized material.

**Grounding.** common-sense extrapolation of the Bessa family's torsion axis — σ_cr,nd scales with GJ, and the Bessa optimum sits at only 86% of max ratio_J.

**Design variables.**

```
twist_angle∈[0,π]. ratio_area∈[1.17e-5,4.1e-3], ratio_Ixx∈
[1e-7,1.4e-6], ratio_Iyy∈[1.13e-11,1.4e-6], ratio_J∈[1e-6,1.5e-5] — generalized
cross-section moments, ratio_J pushed beyond the Bessa 7D dataset's own max (7.77e-6).
ratio_pitch∈[.25,1.5], ratio_top_diameter∈[0,.8] — usual per-storey pitch/taper
meaning (D006's Stage-1 screen; the Stage-2 anchors D4/C4 named in Timeline below fix these at
specific points instead). Fixed: n_longerons=3, n_storeys=1.
```

**Verdict.** BLOCKED · UNKNOWN-NO-EVIDENCE · max-J Stage-2 convergence

---

## D3 · n_longerons = 5 (extended topology)

**The idea.** Increased the mast's rotational symmetry from Bessa's fixed 3 longerons to 4, 5, and 6, at the same (near-optimal) 7D cross-section, to test whether more legs raise the per-longeron critical load.

**Grounding.** common sense topology extension — Bessa's own parametrization never varies longeron count, fixing it at 3 throughout the 2019 paper.

**Design variables.**

```
twist_angle∈[0,π]. ratio_area∈[1.17e-5,4.1e-3], ratio_Ixx∈
[1e-7,1.4e-6], ratio_Iyy∈[1.13e-11,1.4e-6], ratio_J∈[1e-6,7.77e-6] — generalized
cross-section moments (Bessa's own 7D parametrization). ratio_pitch∈[.25,1.5],
ratio_top_diameter∈[0,.8] — usual per-storey pitch/taper meaning. n_longerons∈[3,6] —
the axis under test (main batch fixes it at 5; anchors also test 4, 6). Fixed: n_storeys=1.
```

**Verdict.** SUPPORTED · DEAD-END

---

## D4 · Multi-storey topology (n_storeys=2)

**The idea.** Split the mast into two stacked storeys — an intermediate rigid ring at mid-height, still 3 continuous longerons per storey — instead of Bessa's single-storey topology, to see if a shorter per-segment coiling path could beat the Bessa 2019 paper optimum (65.3 kPa/longeron).

**Grounding.** common sense topology extension of the Bessa rocking-mast concept, not drawn from an outside literature source.

**Design variables.**

```
twist_angle∈[.05,.35] rad. ratio_pitch∈[.25,1.5], ratio_top_diameter
∈[0,.8] — usual per-storey pitch/taper meaning. ratio_shear_modulus∈[.334,.45].
ratio_area∈[1.17e-5,4.1e-3], ratio_Ixx∈[1e-7,1.4e-6], ratio_Iyy∈[1e-7,1.4e-6],
ratio_J∈[1e-6,7.77e-6] — generalized cross-section moments (Bessa's own 7D
parametrization). Fixed: n_longerons=3, n_storeys=2.
```

**Verdict.** UNDERPOWERED · FERTILE-PARAMETRIC · max-J-at-half-pitch, n_storeys=2

---

## D5 · Solid Circular Longeron Family (SCLF), thick variant

**The idea.** Constrained the cross-section to a solid circle (ratio_d ∈ [0.08,0.16], else free) after the generalized Bessa optimum failed Stage 2 categorically — testing whether J/I=2 is what Stage 2 needs.

**Grounding.** follow-up to this run's H1 (generalized optimum: 9.23% Riks strain, not 90%) — circular is the shape closest to Bessa 2019's own demonstration.

**Design variables.**

```
ratio_d∈[.08,.16] (constrained solid circle; else free) — cross-section
diameter. ratio_pitch∈[.25,1.5], ratio_top_diameter∈[0,.8] — usual per-storey
pitch/taper meaning. Fixed: circular=1 (cross-section-family switch), n_longerons=3,
twist_angle=0, ratio_shear_modulus=.43681, and the generalized-optimum moments this campaign
was testing against (area=.00215, Ixx=1.35e-6, Iyy=1.24e-6, J=6.65e-6).
```

**Verdict.** SUPPORTED (RETRACTED) · DEAD-END

---

## D6 · Anisotropic rectangle, reversed orientation (run17 anchor)

**The idea.** Anisotropic `RectangularProfile` longeron, radial SHORT / tangential LONG — reverse of this run's earlier falsified orientation, at slenderness≥10, testing whether max_local_strain and sigma_crit decouple.

**Grounding.** direct extension of the elliptical-substitution idea above — mirror of this run's own H6, common sense, not a literature citation.

**Design variables.**

```
a∈[.004,.014] — radial (short) semi-axis. b∈[.01,.045] — tangential
(long) semi-axis. ratio_pitch∈[.25,1], ratio_top_diameter∈[0,.6] — usual per-storey
pitch/taper meaning. Fixed: ratio_shear_modulus=.3677, circular=2 (cross-section-family
switch), n_longerons=3, n_storeys=1, twist_angle=0.
```

**Verdict.** SUPPORTED · WORKS

---

## D7 · Square (isotropic) cross-section

**The idea.** Tested a square longeron cross-section — at matched half-width/fiber-distance, a square carries ~1.7× a circle's moment of inertia (I_square/I_circle=64/(12π)), bend axis on a flat side not a diagonal.

**Grounding.** common sense, basic section-property comparison — not a literature citation.

**Design variables.**

```
side∈[.005,.025] — square side length. ratio_pitch∈[.25,1],
ratio_top_diameter∈[0,.6] — usual per-storey pitch/taper meaning. Fixed:
ratio_shear_modulus=.3677, circular=2 (cross-section-family switch), n_longerons=3,
n_storeys=1, twist_angle=0.
```

**Verdict.** FALSIFIED · WEAK

---

## D8 · Elliptical cross-section

**The idea.** Proposed an elliptical longeron cross-section (Abaqus-native `EllipticalProfile`, `DURING_ANALYSIS` integration), oriented so its short axis lies in the plane of dominant coiling bending, to raise torsional stiffness past the circular family's strain ceiling. Free: none — untestable, see Verdict

**Grounding.** direct mechanistic extension of the SCLF (circular) family — common sense, not a literature citation.

**Design variables.** none registered (family never reached a search).

**Verdict.** INCONCLUSIVE · UNTESTABLE

---

## D9 · Radially bowed (pre-curved) longerons

**The idea.** Gave each longeron a smooth radial offset by height — zero at both rings, max inward bow at mid-height — to geometrically pre-condition the coiling path and retain high compressive strain.

**Grounding.** common sense geometric hypothesis, not a literature citation.

**Design variables.**

```
bow_amp∈[0,.2] — max inward radial bow at mid-height (zero at both rings).
a∈[.004,.02], b∈[.01,.045] — cross-section semi-axes. ratio_pitch∈[.3,1],
ratio_top_diameter∈[0,.6] — usual per-storey pitch/taper meaning. Fixed: circular=2
(cross-section-family switch), n_longerons=3, n_storeys=1, twist_angle=0,
ratio_shear_modulus=.3677.
```

**Verdict.** FALSIFIED · WEAK

---

## D10 · Elliptical top/bottom rings, phase offset

**The idea.** Replaced the mast's circular top and bottom rings with independently-parametrized ellipses plus a phase offset between the top and bottom ring's major-axis orientation, to break the rotational symmetry that forces every longeron to undergo identical peak curvature.

**Grounding.** common sense structural-symmetry-breaking hypothesis, not a literature citation.

**Design variables.**

```
ring_aspect_ratio∈[1,1.5] — ellipse major/minor axis ratio.
ring_phase_offset∈[0,.2] rad — rotation between top and bottom ring's major axis.
a∈[.004,.02], b∈[.01,.045] — longeron cross-section semi-axes. ratio_pitch∈
[.3,1], ratio_top_diameter∈[0,.6] — usual per-storey pitch/taper meaning. Fixed:
circular=2 (cross-section-family switch), n_longerons=3, n_storeys=1, twist_angle=0,
ratio_shear_modulus=.3677.
```

**Verdict.** INCONCLUSIVE · DEAD-END

---

## D11 · Heterogeneous (2 stiff + 1 compliant) longerons

**The idea.** Made the 3 longerons non-identical: 2 stiff `RectangularProfile` + 1 compliant `RectangularProfile`, same radial dimension, unchanged rings.

**Grounding.** common sense — the compliant longeron absorbs large rotations, "rescuing" compressibility while the stiff ones carry buckling load.

**Design variables.**

```
a∈[.003,.03] — radial dimension, shared by all 3 legs. b_stiff∈
[.010,.075] — the 2 stiff legs' tangential dimension. b_compliant∈[.005,.030] — the 1
compliant leg's tangential dimension. ratio_pitch∈[.25,1.5], ratio_top_diameter∈[0,.8]
— usual per-storey pitch/taper meaning. Fixed: ratio_shear_modulus=.3677.
```

**Verdict.** INCONCLUSIVE · DEAD-END

---

## D12 · BoxProfile hollow-tube cross-section

**The idea.** A closed, thin-walled rectangular hollow-tube (`BoxProfile`) longeron, motivated by mining the 50,000-point Bessa 7D dataset for high-torsion/bending-stiffness combinations no solid family could reach.

**Grounding.** dataset-mining common sense — a least-squares fit of high-performing 7D rows to box geometries had poor residuals (~98% relative L2 error), so the family was built and searched directly.

**Design variables.**

```
a_out, b_out∈[.006,.10] — outer box dimensions. t1, t3∈[.0005,.02] —
wall thicknesses. ratio_pitch∈[.25,1.5], ratio_top_diameter∈[0,.8] — usual per-storey
pitch/taper meaning. Fixed: ratio_shear_modulus=.3677, circular=3 (cross-section-family switch).
```

**Verdict.** INCONCLUSIVE · DEAD-END

---

## D13 · Flexure-hinge (piecewise stiff/thin) longeron

**The idea.** A spatially-varying longeron: thick `RectangularProfile` ends near both rings (global stiffness) with a deliberately thin mid-span "hinge" segment to cap peak bending strain.

**Grounding.** common sense — decouple average stiffness (thick ends) from peak local fibre strain (thin hinge), a DOF no uniform family could access.

**Design variables.**

```
a∈[.003,.03] — leg cross-section. b_end∈[.010,.075] — thick end-segment
depth (near the rings). b_hinge∈[.005,.030] — thin mid-span hinge depth. hinge_fraction
∈[.05,.9] — fraction of the longeron's length occupied by the thin hinge segment.
ratio_pitch∈[.25,1.5], ratio_top_diameter∈[0,.8] — usual per-storey pitch/taper
meaning. Fixed: ratio_shear_modulus=.3677 (.334-.45 also swept as a free var in some runs of
this campaign — see notes).
```

**Verdict.** INCONCLUSIVE · DEAD-END

---

## D14 · Open thin-walled L-profile (shear-centre offset)

**The idea.** An open thin-walled longeron cross-section with an inherent shear-centre-to-centroid offset (Abaqus `LProfile`) — a DOF the Bessa parametrization fixes to zero, never accessed by any prior family.

**Grounding.** parametric-space extension, tempered by a literature review (Zahn & Iwankiw 1989 flexural-torsional buckling theory) predicting AGAINST the mechanism beforehand (see notes).

**Design variables.**

```
a∈[.002,.02], b∈[.01,.06] — outer L-profile leg dimensions.
t_frac_a, t_frac_b∈[.02,.5] — wall thickness as a fraction of each leg's own outer
dimension. ratio_pitch∈[.30,1.5], ratio_top_diameter∈[0,.3] — usual per-storey
pitch/taper meaning (narrowed for this campaign). Fixed: n_longerons=3,
ratio_shear_modulus=.3677.
```

**Verdict.** FALSIFIED · DEAD-END

---

## D15 · Diagonal chiral-bracing lattice

**The idea.** Added a diagonal chiral-bracing lattice of short auxiliary beam struts between adjacent longerons, layered on the slenderness-valid rectangular family (two verified CEI-BO campaigns; see notes).

**Grounding.** common-sense — an alternative stiff load path to offload torsional/bending demand from the longerons (a later refinement drew a cable-stayed precedent, Gurfinkel & Krishnan 2017; see notes).

**Design variables.**

```
a∈[.0025,.20], b∈[.0025,.075] — longeron cross-section semi-axes.
ratio_pitch∈[.25,1.5], ratio_top_diameter∈[0,.8] — usual per-storey pitch/taper
meaning. z_brace∈[.05,.95] — axial position of the bracing lattice along the mast.
ratio_brace_area∈[0,3.5e-4] — brace strut cross-section area. brace_prestrain∈[0,.01] —
brace pre-tension strain. Fixed: circular=2 (cross-section-family switch), n_longerons=3,
n_storeys=1, twist_angle=0, ratio_shear_modulus=.3677.
```

**Verdict.** INCONCLUSIVE · DEAD-END

---

## D16 · Helical (chiral) longeron path

**The idea.** Bent each longeron into a helix winding around the mast axis (a `helix_wrap` parameter), rather than a straight line, hypothesizing a spring-like geometry predisposed to reversible coiling.

**Grounding.** common-sense mechanistic hypothesis, explicitly distinguished from pre-twist (which rotates the cross-section) and radial bowing (which is planar) — both tried and falsified in earlier runs. Not drawn from an outside literature source.

**Design variables.**

```
a∈[.003,.03], b∈[.008,.06] — cross-section semi-axes.
ratio_pitch∈[.30,1.5], ratio_top_diameter∈[0,.6] — usual per-storey pitch/taper
meaning. helix_wrap∈[0,1.5708] rad — turns wound into the longeron before compression.
Fixed: n_storeys=1, twist_angle=0, ratio_shear_modulus=.3677.
```

**Verdict.** FALSIFIED · DEAD-END

---

## D17 · Kresling/TCO two-segment bar-hinge longeron

**The idea.** Replaced each longeron with two straight beam segments meeting at an interior hinge node, offset circumferentially by angle `psi_kresling`, coupling axial compression to rigid-body strut re-orientation instead of relying purely on elastic bending.

**Grounding.** the Kresling origami folding pattern (a well-known bar-hinge/triangulated-cylinder mechanism), adapted here to this study's beam-longeron model — a real, specific geometric precedent, not a fabricated citation.

**Design variables.**

```
a∈[.006,.014], b∈[.008,.025] — cross-section semi-axes.
ratio_pitch∈[.25,1.5], ratio_top_diameter∈[0,.6] — usual per-storey pitch/taper
meaning. psi_kresling∈[0,.6] rad — hinge offset angle (0 = hinge off). ratio_hinge_height
∈[0,1] — where along the longeron's length the hinge node sits. Fixed: circular=2
(cross-section-family switch), n_storeys=1, twist_angle=0.
```

**Verdict.** INCONCLUSIVE · DEAD-END

---

## D18 · Smoothly radially-tapered ("waisted") longeron

**The idea.** Tapered a longeron's radial thickness along its arc-length — thick at both ring ends, waisted at mid-span — a fixed-volume optimal-column shape, not a uniform section.

**Grounding.** classical Lagrange-Keller / Tadjbakhsh-Keller optimal-column result, adapted to this study's longeron geometry.

**Design variables.**

```
a_end∈[.004,.02] — end (ring) cross-section radius. waist∈[.30,.98] —
mid-span radius as a fraction of a_end. b∈[.012,.06] — secondary semi-axis.
ratio_pitch∈[.4769,.8857], ratio_top_diameter∈[.0311,.0578] — usual per-storey
pitch/taper meaning, narrowed for this campaign. Fixed: circular=4 (cross-section-family
switch), n_storeys=1, twist_angle=0.
```

**Verdict.** INCONCLUSIVE · UNTESTABLE

---

## D19 · In-plane serpentine/meander longeron centerline

**The idea.** Perturbed each longeron's centerline into a periodic, small-amplitude in-plane serpentine (meander) wave instead of a straight line, aiming to distribute bending curvature along the member's length rather than concentrate it at one region.

**Grounding.** common-sense mechanistic hypothesis (a curvature-distribution argument), not drawn from an outside literature source.

**Design variables.**

```
amplitude_rel∈(0,.02] — meander amplitude relative to the mast diameter.
n_periods∈[1,6] — number of wave periods along the longeron. Fixed: host geometry =
run17_rectangle (a=.009213, b=.033238, ratio_pitch=.681277, ratio_top_diameter=.04444).
```

**Verdict.** INCONCLUSIVE · DEAD-END

---

## D20 · Laced/battened two-parallel-chord built-up longeron

**The idea.** Replaced each solid longeron with two parallel slender chords separated by a fixed gap (a laced/battened built-up member), aiming to set global bending stiffness by chord separation while peak local strain stays governed by each chord's own small radius.

**Grounding.** common-sense mechanistic hypothesis grounded in the parallel-axis theorem (2·A_f·(h/2)), not a literature citation.

**Design variables.**

```
rc∈[.001,.02] — chord radius. h∈[.01,.15] — separation between the two
chords. n_battens∈[2,8] — discrete batten count. ratio_pitch∈[.25,1.5],
ratio_top_diameter∈[0,.8] — usual per-storey pitch/taper meaning. Fixed: circular=4
(cross-section-family switch), n_storeys=1, twist_angle=0, ratio_shear_modulus=.3677.
```

**Verdict.** FALSIFIED · WEAK

---

## D21 · Class-1 tensegrity strut-and-cable longeron replacement

**The idea.** Replaced the bending longeron with a pin-jointed, prestressed Class-1 tensegrity assembly — stiffness from prestress/geometry, not beam bending.

**Grounding.** Amendola et al. (2018) tensegrity prestress-stiffness theory, contrasted with Meng (2012)/Sorrentino (2021) on bending-family strain-stiffness coupling.

**Design variables.**

```
a_strut∈[.0001,.05], slen_strut (reparametrized from ratio_b_strut∈
[.0001,.08] as pitch/(2*max(a,b))) — strut cross-section/slenderness. area_cable∈[1e-7,1e-2]
— cable cross-section area. mid_h∈[.05,.95] — mid-height ratio of the tensegrity's waist.
prestrain∈[-.05,.05] — cable pre-tension strain. ratio_pitch∈[.1,2],
ratio_top_diameter∈[0,.8] — usual per-storey pitch/taper meaning. Fixed: circular=7
(cross-section-family switch), n_longerons=3, n_storeys=1, twist_angle=0,
ratio_shear_modulus=.3677.
```

**Verdict.** SUPPORTED (DISQUALIFIED) · DEAD-END

---

## D22 · Doubly-symmetric cruciform/I-beam cross-section

**The idea.** Replaced the anisotropic-rectangular longeron cross-section with an open thin-walled cruciform/I-beam profile, chosen so torsional stiffness (J) is tunable independently of bending stiffness (Ixx/Iyy), unlike a solid rectangle where the two are coupled.

**Grounding.** classical flexural-torsional beam theory (common-sense cross-section engineering, not a specific outside citation) — the motivating idea was that decoupling J from Ixx/Iyy might let the section reach high axial stiffness without paying the local-bending-strain penalty the rectangle family pays.

**Design variables.**

```
b∈[.015,.05] — flange width. h∈[.02,.08] — section height.
tf∈[.002,.012] — flange thickness. tw∈[.0015,.008] — web thickness. ratio_pitch
∈[.3,1.5], ratio_top_diameter∈[0,.3] — usual per-storey pitch/taper meaning. Fixed:
circular=8 (cross-section-family switch), n_longerons=3, n_storeys=1, twist_angle=0,
ratio_shear_modulus=.3677.
```

**Verdict.** BLOCKED · UNKNOWN-NO-EVIDENCE · cruciform/I-beam Stage-2 convergence

---

## D23 · Chained mild pre-curved ("sub-bistable") arch-segment longeron

**The idea.** Chain of N alternating-sign pre-curved shallow-arch segments, rise-to-thickness ratio (Q) kept *below* the bistability floor (Q≈2.31) — mild repeating curvature, not genuine snap-through.

**Grounding.** follow-up to the same run's H2 (*true* bistable, Q≥2.31 chain), which hit a Riks solve-completion wall (18 coilable, only 2/18 converged); asks whether backing off avoids the wall while still beating baseline.

**Design variables.**

```
n_segments∈[2,6] — chain length (discrete). arch_rise∈[.02,.3] — per-
segment rise, kept below the Q≈2.31 bistability floor. Fixed: a=.009213, b=.033238,
ratio_pitch=.681277, ratio_top_diameter=.04444, circular=11 (cross-section-family switch).
```

**Verdict.** FALSIFIED · WEAK

---

## D24 · Single bistable shallow-arch snap segment near the ring joint

**The idea.** Spliced one bistable, shallow-arched snap-through segment near the bottom ring, jointly re-optimized with the base cross-section, to reinvest local-strain headroom into higher σ_cr,nd than 0.7704 kPa.

**Grounding.** elastic-instability/bistable-mechanism metamaterials literature; follow-on to a same-run hypothesis whose single-arch strain cut (mean ~7%, max 12.3%) fell short of a pre-registered 20% bar.

**Design variables.**

```
a∈[.007,.012], b∈[.025,.045] — base cross-section semi-axes, jointly
re-optimized with the arch. arch_rise∈[.02,.09] — bistable snap-arch height. arch_length
∈[.25,.5] — arch length along the longeron. Fixed: ratio_pitch=.681277,
ratio_top_diameter=.04444, circular=15 (cross-section-family switch), stabilization=1,
dual_arch=1.
```

**Verdict.** SUPPORTED · WORKS

---

## D25 · Thin-walled open circular-arc ("tape-spring") longeron

**The idea.** Replaced the solid B31 longeron with a thin-walled, open-arc S4R **shell** section, hypothesizing a *localized elastic fold* could escape the mast-scale coiling curvature capping every beam family.

**Grounding.** Named for Calladine inextensional shell-folding theory and Seffen–Pellegrino tape-spring mechanics.¹

**Design variables.**

```
t_tape∈[.4,1.6] — tape thickness. R_tape∈[6,400] — arc radius.
alpha_tape∈[.05,2.2] — arc angle subtended (section depth driver). beta_tape∈[0,3.14] —
section orientation. ratio_pitch∈[.25,1.5], ratio_top_diameter∈[0,.8] — usual
per-storey pitch/taper meaning. Fixed: circular=17 (cross-section-family switch), n_longerons=3,
n_storeys=1, twist_angle=0, ratio_shear_modulus=.3677.
```

**Verdict.** POWERED · REFUTED · localized elastic fold

---

## D26 · Chiral continuous-curved-shell tube

**The idea.** Replaced all n discrete straight longerons with ONE continuous, doubly-curved, multi-lobed shell tube connecting the two rigid rings, with a built-in azimuthal twist of the lobe pattern from bottom to top — chirality breaking mirror symmetry to try to couple axial compression into global rotation.

**Grounding.** Liu et al. 2025 (*Nature Communications* 16:11359), "chiral multi-curved shell metamaterials integrating compression-torsion and buckling mechanisms" — every prior family in this study keeps a discrete- member load path; this removes the discreteness entirely.

**Design variables.**

```
n_lobes∈[3,6] — discrete lobe count. A_max∈[.05,.35] — lobe amplitude.
twist_chirality∈[0,3.14] — azimuthal twist of the lobe pattern bottom-to-top. t_shell∈
[.5,2] — shell wall thickness. ratio_pitch∈[.15,.8], ratio_top_diameter∈[0,.5] — usual
per-storey pitch/taper meaning. Fixed: ratio_shear_modulus=.3677.
```

**Verdict.** POWERED · REFUTED · monocoque chirality

---

## D27 · Chiral shell vane longeron

**The idea.** Reverted to n discrete members (this study's usual sparse topology) after D26's monocoque tube suppressed coiling, but gave each discrete longeron a genuinely new, non-beam shape: a twisting, doubly-curved shell "vane" instead of a solid/thin-walled cross-section.

**Grounding.** direct empirical follow-up to D26 — its own finding (full monocoque tube too stiff against global lateral bending) predicts that restoring low overall bending stiffness via discrete members should let a coiling mode compete again, while keeping the chirality/twist mechanism.

**Design variables.**

```
t_shell∈[.2,2] — shell wall thickness. W∈[3,15] — vane width. B_max∈
[1,8] — vane curvature amplitude. twist_total∈[.2,1.5] — per-longeron twist over the mast
height. ratio_pitch∈[.3,1], ratio_top_diameter∈[0,.4] — usual per-storey pitch/taper
meaning. Fixed: n_longerons=3, ratio_shear_modulus=.3677.
```

**Verdict.** POWERED · REFUTED · discrete twisting vane

---

## D28 · Multi-leaf (leaf-spring) longeron

**The idea.** Split each longeron into `n_leaves` thin leaves stacked in the winding plane, free to slide — a leaf spring. The hope: total depth still carries load while each leaf bends at its own small depth.

**Grounding.** direct attack on this run's own H1 — coiling curvature is pinned to the ring radius, so the only free lever is the depth it acts on. Classical leaf-spring practice, not a metamaterial citation.

**Design variables.**

```
n_leaves∈{1,3,5} — discrete leaf count, not a continuous dial. a∈[.004,.014],
b∈[.01,.045] — per-leaf cross-section semi-axes. ratio_pitch∈[.25,1]. Fixed:
ratio_shear_modulus=.3677, n_longerons=3, n_storeys=1, twist_angle=0.
```

**Verdict.** UNDERPOWERED · REFUTED · leaf splitting

---

## D29 · Mandrel-confined coiling mast

**The idea.** A coaxial rigid cylinder inside the mast for the longerons to wind onto — hoping it governs the coiling curvature and adds a confined second load path once members bear on it.

**Grounding.** the run's opening hypothesis (H1/H2) — once the cross-section is capped, the only lever left is what the member coils *against*.

**Design variables.**

```
mandrel_ratio∈[0,.83] — mandrel radius as a fraction of the geometric limit
(.83). a∈[.004,.014], b∈[.01,.045] — cross-section semi-axes. ratio_pitch∈[.25,1.5].
Fixed: n_longerons=3, ratio_top_diameter=.04444, n_storeys=1.
```

**Verdict.** POWERED · REFUTED · mandrel confinement

---

## D30 · Pre-coiled (helical) longeron

**The idea.** Build the longeron already wound as a helix of `helix_wrap` turns, so coiling supplies only the *remaining* curvature.

**Grounding.** this run's own law. Strain is c × curvature **change**, not curvature — a member born at κ₀ travels only κ_max - κ₀, so the cap 0.02/Δκ relaxes.

**Design variables.**

```
helix_wrap∈[-0.3,6.0] — pre-coiled turns built into the longeron before any
compression is applied. a∈[.004,.014], b∈[.01,.045] — cross-section semi-axes.
ratio_pitch∈[.25,1.5]. Fixed: n_longerons=3, ratio_top_diameter=0, n_storeys=1,
imperfection=.067.
```

**Verdict.** POWERED · REFUTED · wrap-vs-load (accessible depths)

---

## D31 · Secondary elastic "stop" member

**The idea.** Short stocky members carrying nothing at first, **engaging only once the primary longerons near their 2%-strain limit** — a contact-triggered stiffness jump.

**Grounding.** Florijn, Coulais & van Hecke 2014, *Programmable Mechanical Metamaterials*. It attacks the kinematic law head-on: a *separate* member escapes the ring-rotation curvature compatibility (κ_max ≈ 1/R_mean) that caps one continuous longeron.

**Design variables.**

```
ratio_stop_d∈[.02,.03] — stop member diameter. stop_engagement_fraction
∈[.5,.8] — compression fraction at which the stop is meant to contact. stop_radial_ratio
∈[.4,.6] — stop's radial placement between the mast axis and the primary longerons.
n_stops∈{0,1,3} — discrete count, not a continuous dial. Fixed: primary longeron at the
incumbent.
```

**Verdict.** BLOCKED · UNKNOWN-NO-EVIDENCE · stop engagement

---

## D32 · Shaped (conical) ground-disc contact surface

**The idea.** Replace the flat rigid ground disc with a shallow axisymmetric **cone**, so the coil bears on a slope and the bearing point migrates as it descends.

**Grounding.** analogy from shell-buckling and origami-confinement literature — and the *cheap* half of the run's contact program: it changes only the rigid surface, leaving the primary member and its coupling scheme exactly as validated.

**Design variables.**

```
cone_rise_ratio∈[0,.30] — cone height as a fraction of its base radius (0 =
flat disc, the family's own control). Fixed: everything else at the incumbent (a=.00921,
b=.03324, pitch=.68128, rtd=.04444, n_long=3).
```

**Verdict.** BLOCKED · UNKNOWN-NO-EVIDENCE · cone engagement

---

## D33 · Self-contacting divergent-convergent longeron pairs

**The idea.** Replace each longeron with a **pair** of independently-anchored beams, pre-bowed to close a small gap and make frictionless surface contact partway through the coil — no shared node with the ring, unlike the closed `secondary_stop` family. Single validation point; only the contact law/solver varied (see Input space).

**Grounding.** Liu, Ennis & Coulais 2024 (measured stroke-triggered self-contact stiffening), Dharmavaram, Ebrahimi & Ghosh 2021 (soft-to-stiff contact-locking in a bending filament), Hima, Bigoni & Dal Corso 2022 (rigorous non-artefactual stiffness discontinuity at a unilateral-constraint threshold).

**Design variables.**

```
none free — a single validation point (n_corners=3, ratio_d=.02, pitch=.75,
top_d=.30, leg_offset=.05, gap0=.015); only the contact law/solver varied across delegations.
```

**Verdict.** BLOCKED · UNKNOWN-NO-EVIDENCE · self-contact load-bearing

---

## D34 · Graded, contact-decoupled two-storey mast

**The idea.** A two-storey mast where storey 1 (deliberately weaker: shorter pitch/thinner section) is physically separated from storey 2 by a gap that only closes by CONTACT — storey 2 carries zero load until storey 1 fully collapses, then absorbs compression fresh, like a second spring engaging once the first bottoms out. Contact-decoupled, unlike the closed `asym_storey` family, which rigidly ties both storeys' motion from t=0.

**Grounding.** Liu, Ennis & Coulais 2024 — the same layer-by-layer programmed buckling sequence grounding D33, applied here as discrete storeys rather than a single member's self-contact.

**Design variables.**

```
ratio_d1∈[.01,.04], ratio_pitch1∈[.13,1.04] — storey 1 (deliberately
weaker) section/pitch. ratio_d2∈[.023,.073], ratio_pitch2∈[.30,1.20] — storey 2
section/pitch. twist_angle1, twist_angle2∈[0,π/2] — per-storey pretwist.
ratio_top_diameter∈[0,.8] — whole-mast taper, same range every family uses.
stop_engagement_fraction∈[.05,.85] — solid-height at which storey 1 lands and storey 2
begins carrying load. Fixed: n_longerons∈{3,4,5,6} (categorical), ratio_shear_modulus=.3677.
```

**Verdict.** POWERED · REFUTED · this 2-storey architecture

---

## D35 · Bend-twist self-locking scale longeron

**The idea.** small rigid, plate-like "scale" panels textured onto the longeron's own surface at each of n_ribs stations, angled and spaced so consecutive scales overlap and lock against each other as the beam bends — a substrate that transitions from soft (bare beam) to stiff (locked scales) past some curvature.

**Grounding.** Dharmavaram, Ebrahimi & Ghosh 2021 (arXiv:2108.10976) — overlapping rigid scales lock past a curvature threshold, decoupling strain from bending depth the way biological scale substrates do; independently top-ranked for novelty by 3 separate literature reviews (2026-08-16/19/20) before this run resourced it.

**Design variables.**

```
ratio_a∈[.006,.02] — radial half-thickness. ratio_b∈[.01,.05] —
tangential half-width. ratio_pitch∈[.15,1.2], ratio_top_diameter∈[0,.6] — usual
per-storey pitch/taper meaning. n_ribs∈[3,10] — scale-station count.
rib_length_ratio/eta∈[1,6] (paper's own centre ~3) — scale overlap length.
rib_width_ratio/beta∈[.4,3] (paper's own centre ~1.25) — scale overlap width.
rib_embed_angle_deg/alpha0∈[0,60] (paper's own value 30) — angle each scale is set into the
beam surface. rib_rest_angle_deg/theta0∈[0,20] (paper's own value 5) — rest angle before
locking engages. t_scale∈[.1,1.0] mm — scale panel thickness. Fixed: n_longerons=3.
```

**Verdict.** POWERED · FERTILE-REWORK · rigid interlocking-panel embodiment

---

## D36 · Kirigami-cut continuous shell wall

**The idea.** discrete straight longerons replaced by ONE continuous, periodically-cut PLA shell wall — cut length `l`, ligament width `delta`, shell thickness `t_shell` free; ring radii fixed to the study's standard envelope.

**Grounding.** kirigami-cut shell metamaterials literature (cut networks that buckle/snap out-of-plane at each ligament) — the idea being that many independent ligament rotations absorb the ring's rotation-descent demand instead of one beam's curvature.

**Design variables.**

```
l∈[1,300] — cut length (mm) of each kirigami slit. delta∈[1,50] —
ligament width between adjacent cuts. t_shell∈[.3,3.5] — shell wall thickness.
helical_twist_total∈[0,2π] — total helical twist applied across the shell's height.
ratio_pitch∈[.25,1.5], ratio_top_diameter∈[0,.6] — usual per-storey pitch/taper
meaning from every other family. Fixed: ring radii held at the study's standard envelope.
```

**Verdict.** POWERED · UNKNOWN-NO-EVIDENCE · panel-vs-global mode competition

---

## D37 · Compliant kirigami-cut top ring

**The idea.** Bessa's rigid 0-D top ring replaced by an elastically-buckling, kirigami-cut annular shell — ring cut length, ligament width, thickness, and radial width free; longeron geometry unchanged from the matched circular-family control.

**Grounding.** same kirigami-cut shell grounding as D36, applied to the ring rather than the longerons — letting the effective ring radius evolve during compression instead of staying fixed.

**Design variables.**

```
t_ring∈[.3,1.5] — ring shell thickness. w_ring∈[8,25] — ring radial
width. delta_ring∈[1.5,5] — ligament width between ring cuts. l_ring∈[3,15] — ring cut
length. margin_frac_ring∈[.10,.25] — safety margin fraction on the ring's own geometric
limits. ratio_d∈[.004,.073], ratio_pitch∈[.25,1.5], ratio_top_diameter∈[0,.8] —
usual longeron/pitch/taper meaning, matched to the circular-family control. Fixed:
n_longerons∈{3,4,5,6} (categorical, searched).
```

**Verdict.** POWERED · REFUTED · ring-radius growth

---

## D38 · Helically-graded shell thickness

**The idea.** a mass-neutral, helically-graded thickness field t(θ,z) over an otherwise UNCUT, smooth conical shell wall (a=0 collapses to the study's own uniform-shell control) — grading contrast `a`, rotational order `n_eff`, helical twist, phase, pitch/taper free.

**Grounding.** graded/hierarchical architected-metamaterial literature — the idea being that reshaping the strain-vs-compression integral via a spatially-varying wall thickness could let a design reach mcs≥0.80 within the 2% strain budget at a higher σ_peak than a uniform wall permits.

**Design variables.**

```
a∈[.3,.5] — grading contrast (0 = uniform-shell control). n_eff∈[3,8]
— rotational order of the thickness field. t0∈[.5,3] — nominal (unmgraded) wall thickness.
helical_twist_total∈[-4π,4π] — including small-angle probes. helical_phase0∈[0,2π]
— twist phase offset. ratio_pitch∈[.25,1.5], ratio_top_diameter∈[0,.6] — usual
per-storey pitch/taper meaning.
```

**Verdict.** POWERED · REFUTED · twist-phase magnitude

---

## D39 · Nested double-wall with engaging backing collar

**The idea.** an outer continuous shell wall backed by an inner collar/panel that closes a gap and engages via self-contact partway through compression, meant to raise effective stiffness only after engagement — gap `g0`, collar thickness `t_in`, engagement height/preload free.

**Grounding.** direct follow-up to D36/D38's shared failure mode — instead of cutting or grading the wall itself, add a second wall that only helps once contact closes, hoping to avoid the local-buckling competition both prior shell attempts hit.

**Design variables.**

```
g0∈[0,1] — radial gap between outer shell and inner collar before
engagement. t_in∈[.2,5] — collar thickness. with_backing∈{0,1} — control switch (0 =
D38's uncut-shell control, bit-for-bit). backing_axial_extent∈[.05,1] — collar height as a
fraction of the mast. preload_fraction∈[0,1] — optional preload feeding the *BUCKLE step.
gap_taper_frac∈[0,.49], soft_contact∈{0,1} — contact-formulation controls, not searched
this diagnostic. ratio_pitch∈[.25,1.5], ratio_top_diameter∈[0,.6] — usual per-storey
pitch/taper meaning. Only 5 hand-picked configurations were run (not a DOE sweep of this box) —
see Timeline.
```

**Verdict.** UNDERPOWERED · REFUTED · backing-panel engagement

---

## D40 · Crosslinked beam bundle

**The idea.** each longeron replaced by 2-3 slender B31 sub-beams on the same envelope circle, tied at discrete axial crosslink points.

**Grounding.** Rathore & Grason 2011 — a crosslinked bundle of slender filaments carries an intrinsic torque an equivalent single member doesn't, because the crosslinks resist relative bending/twisting between sub-beams; the hope was this extra coupling raises the mast's coiling stiffness beyond a solid-longeron control at the same envelope diameter.

**Design variables.**

```
ratio_d∈[.004,.073] — sub-beam diameter relative to the envelope.
ratio_r_sub_frac∈[.05,.48] — how far off the main envelope circle each sub-beam sits (0 = on
the circle, larger = more spread within the local bundle footprint). ratio_pitch∈[.25,1.5],
ratio_top_diameter∈[0,.8] — usual per-storey-pitch/taper meaning from every other family.
n_sub_beams∈{2,3} — discrete topology choice, not a continuous dial. n_crosslinks∈{0,1,3,5}
— number of discrete axial tie points. crosslink_stiffness_ratio∈[0,1] — interpolates rigid
(1) to soft (0) connector coupling. crosslink_spacing_bias∈[-.9,.9] — shifts whether
crosslinks cluster toward the top/bottom of the mast or sit evenly spaced. twist_angle∈[0,π]
— optional pretwist, same convention as D1. Fixed: n_longerons∈{3,4,5,6} (categorical,
searched, held constant within any one design).
```

**Verdict.** POWERED · FERTILE-REWORK · Riks convergence

---

## D41 · Chiral twist-buckling mast

**The idea.** 6 rods set at an ANGLE to the mast's axis (not straight/axial), deliberately thickened past this study's usual cross-section, so rod-level TORSIONAL buckling competes with the bending-dominated coiling every straight-longeron family inherits — the question is whether each ROD twists about its OWN axis, independent of the rings' own relative rotation.

**Grounding.** Fang et al. (2025), *Nature* 639 — torsional strain energy scales ~8× more favorably with stress than bending, decoupling load capacity from every family's curvature cap. Thickened deliberately: a slender rod buckles in bending first, so torsion can't compete unless the bending threshold rises faster than the torsional one.

**Design variables.**

```
twist_angle∈[.035,1.05] rad (2°-60°, chirality pre-rotation angle
α₀). ratio_pitch∈[.5,1.5]. ratio_a, ratio_b∈[.021,.075] — rod cross-section
(elliptical/RectangularProfile substitute for Abaqus's missing native ellipse). Fixed for this
diagnostic: n_longerons=6, ratio_top_diameter=0 (R1≈R2, matching Fang et al.'s own stated
preference), ratio_shear_modulus=.3677, young_modulus=3500 MPa.
```

**Verdict.** UNDERPOWERED · FERTILE-PARAMETRIC · joint decoupling

---

## D42 · Serpentine (wavy in-plane) longeron

**The idea.** Offset each longeron's centerline from the straight ring-to-ring chord by a sinusoid in the TANGENTIAL direction — perpendicular to the mast's own coiling-bow plane, not within it — with a strongly anisotropic cross-section (stiff in-plane, compliant out-of-plane).

**Grounding.** Shi, Huang, Yu & Li (2024) — an anisotropic serpentine strip buckles OUT of its own planform via a coupled bend-twist mode (a double-eigenvalue bifurcation), a different post-buckling channel than the planar coiling every other family here shares.

**Design variables.**

```
ratio_pitch∈[.35,1.20] — storey height / D1, narrowed at the low end where
the new local-curvature gate binds hardest. ratio_top_diameter∈[0,.60] — taper, kept
non-negative so this family's result is never confounded with the already-closed "flare the
rings" lever. ratio_a∈[.003,.020] — OUT-of-plane (radial) cross-section half-dimension, kept
small so radial bending/twisting stays the compliant channel. ratio_b∈[.015,.05] — IN-plane
(tangential) half-dimension, kept large relative to ratio_a (aspect ratio spans ~1-16).
amplitude_rel∈[.01,.08] — peak tangential wave offset / D1, lower-bounded so the wave is a
genuine planform feature, not a near-straight re-test of the baseline. n_undulations — discrete
wave-period count. Fixed: n_longerons=3, n_storeys=1, twist_angle=0, ratio_shear_modulus=.3677.
```

**Verdict.** POWERED · VALIDATED · wave-driven disc contact

---

## D43 · Grain-beam (chiral sub-lattice) longeron

**The idea.** A literal, periodic B31 beam-element mesh along each longeron: repeating stiffer "grain" inclusions (locally-enlarged cross-section) connected by slender, chirally-offset bar pairs — a real discretized lattice, not a homogenized section.

**Grounding.** Pancella & D'Annibale (2025) — a periodic chiral-grain lattice carries a homogenized extension-shear/bend-twist coupling from material chirality itself (the grain-bar offset), not from centerline geometry the way serpentine's coupling is — testing whether that distinct channel keeps the lowest buckling mode GLOBAL coiling, not local grain/bar buckling, the failure mode that killed this study's prior shell-based chiral attempts (D26/D27/D38).

**Design variables.**

```
n_cells∈[3,8] — discrete grain-inclusion count. R∈[3.0,4.0] — grain
radius (relative). t∈[.40,.55] — bar thickness. w∈[2.0,3.5] — bar width. alpha∈
[1,5], beta∈[1,5] — grain/bar chirality-offset shape parameters. chirality∈{-1,+1} —
discrete handedness. Fixed: n_longerons=3, n_storeys=1, D1=100mm, ratio_shear_modulus=.3677.
```

**Verdict.** POWERED · FERTILE-REWORK · chiral-lattice embodiment

---

## D44 · Chained (multi-segment) bistable arch longeron

**The idea.** replace one longeron with N=2-6 genuinely bistable (Q=rise/thickness ≥ 2.31) shallow-arch segments chained end-to-end, so the longeron snaps through several times in a controlled sequence as it compresses, instead of buckling smoothly like an ordinary beam.

**Grounding.** Correa, Seepersad & Haberman (2015) - a chain of sequential negative-stiffness cells; a genuine connectivity change (a SEQUENCE of discrete snap-through events), not a single modified segment.

**Design variables.**

```
n_segments∈{2,...,6} - discrete chain length. arch_rise_ratio,
ratio_a, ratio_b, ratio_pitch, ratio_top_diameter - same physical meaning as every other
rectangular-cross-section family in this study. end_rise_scale∈[0,1] - how much the
TWO end segments (the ones framing directly into a ring joint) taper their own curvature down
from the interior segments' full bistable rise (1.0 = no taper, 0.0 = end segments fully
straightened). Fixed: young_modulus=3500 MPa, ratio_shear_modulus=0.3677, D1=100mm.
```

**Verdict.** POWERED · FERTILE-PARAMETRIC · joint-strain vs sustained-capacity

---

## D48 · Legged snap-chain (sequential elastic snap-through) longeron

**The idea.** abandons ring-rotation coiling entirely: rigid rings connected by three curved arches, each on two short legs so it can flip to its mirror curve without hitting the ring below - compression comes from arches snapping in sequence.

**Grounding.** Shan et al. 2015¹ - chaining bistable curved-beam units traps elastic strain via sequential snap-through, never applied to this problem before. Bistability threshold (rise/thickness ≥ ~2.31): Qiu, Lang & Slocum 2004².

**Design variables.**

```
n_levels (2-12, integer) — ring-level count. rise_ratio, t_ratio, w_ratio — arch
rise/thickness/width, each / D1. leg_ratio — leg height / arch rise (the free parameter H4, run 1,
identified as necessary at all: leg_ratio>0 is what lets the arch clear the ring below it on
full inversion). chord_half_angle — arc's own angular extent. Fixed: D1=100mm,
ratio_shear_modulus=.3677, 3 arches per level (matching this study's own 3-longeron convention).
```

**Verdict.** POWERED · VALIDATED · legged bistable snap-chain mechanism

---

## D49 · Compliant-root scale substrate (flexible flange, unilateral contact)

**The idea.** replaces D35's rigid panel clamp with a compliant flexural neck; panels touch only via unilateral, frictionless contact - tests whether a flexible root adds stiffness without D35's failure mode.

**Grounding.** D35 (rigid panels) failed for a known reason: the clamp froze curvature locally and amplified it elsewhere, closing the strain window on 0 of 64 designs. Tests whether a compliant root fixes that.

**Design variables.**

```
ratio_a, ratio_b (each / D1) - base-beam half-depths. ratio_pitch,
ratio_top_diameter - ring geometry, shared with every family in this study. n_ribs
(3-12, integer), rib_length_ratio - scale-panel count and length. neck_length_mm,
neck_thickness_mm - the compliant root's own two free dimensions, which set k_root. t_scale
 - panel thickness. rib_rest_angle_deg - panel pre-tilt (negative = pre-engaged).
rib_embed_angle_deg - panel skew relative to the mast's coiling twist (widened to
[-10,+20] mid-run once the engagement-angle gate made the original [0,20] box mostly
unreachable). face_sign, scales_enabled - continuous, thresholded, realized value reported.
Fixed: D1=100mm, n_longerons=3, ratio_shear_modulus=.3677, E=3500MPa, n_storeys=1.
```

**Verdict.** POWERED · REFUTED · flange-style stiffening from panel

---
