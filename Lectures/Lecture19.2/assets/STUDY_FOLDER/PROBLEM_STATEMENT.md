# Supercompressible Metamaterial — Open Design Space

## Problem definition

The aim is to additively manufacture a building block that achieves recoverable supercompressibility while maintaining high strength and stiffness. This concept results from a combination of a deployable mast developed for highly deformable space structures, and a thin-walled conical frustum common in impact absorption applications.
Under axial compression it buckles into a **coiling mode**: the top ring
rotates and descends while the longerons wind inward. If this mode governs, a brittle PLA
structure can compress to >80% of its height without fracture. Bessa, Glowacki & Houlder
(2019) mapped this structure's performance and found PLA-printable designs that coil and
support high loads — see **More background** below for their methodology in full.

This problem aims to develop a **NEW** design that clears the bar from Bessa et al. It must be a genuinely new geometry, or a genuinely new connectivity/storey/symmetry (topology), whatever that depart substantially from the straight-longeron idea put forward by Bessa and collaborators.
That is, an idea that is a simple perturbation from the Bessa infrastructure is not a valid design,
as it would not clear the originality contract of a breakthrough expected from a Nature Journal. Our job is to connect the dots from the literature.

**Use the whole wall-clock budget.** It is there to be spent. **A run that closes early on negative
results is not a valid run:** until both floors are met — the objective floor (2× Bessa) *and* the
novelty floor — you are expected to exhaust the time limit, regardless of how many attempts have
failed. Falsifying an idea frees budget for the next one; it does not end the run, and neither
does passing the deliverable gate. Closing early is justified by having cleared both floors, and by
nothing else. **CRITIC: REJECT a run you know has not used its time allocation and delivers a negative result. Not PASS, not
NOTED — REJECT.**

### Objective

Maximise the normalised peak compressive stress among feasible designs:

$$\sigma_{peak} = \frac{P_{max} \times 1000}{\dfrac{\pi D_1^2}{4} \times n_{longerons}} \quad \text{[kPa per longeron]}$$

where P_max is the largest axial reaction force in Newtons reached during the Stage-2
compression, **within the WHOLE evaluation window** defined below. Dividing by n_longerons removes
the trivial superposition gain from adding longerons.

**The window that bounds every number above, and how this metric came to be, are at the end
of this section** — read the window rules before you report a σ_peak.

**Feasibility — ALL criteria must hold for a design to count:**

1. Coilability: the mast reaches **max compressive strain ≥ 0.80** — it compresses to ≤ 20% of its original
   height without load reversal (Bessa et al. 2019).
2. The maximum local strain on the whole design, **up to the point where the mast reaches the
   criterion-2 compression threshold (mcs = 0.80)**, is **≤ 2%** — Bessa's own stated
   criterion, literally: *"plasticity occurs when any strain component is higher than 2%,
   i.e. we use the maximum strain yield criterion as max(ε_ij) = 2%"* (Supporting
   Information, p.9 — they separately measured a pure-torsion yield strain of ~2.8% and
   chose to apply the more conservative tension-based 2% value to every component, shear
   included, not bending alone). The design must coil to ≥ 80% compression *within* the 2%
   strain budget; strain incurred by crushing it *further* than needed does not disqualify
   it.
3. The design must be PLA-printable. This implies that the final design proposed must have
   enough predictive power to assert, beyond reasonable doubt, that the simulation is a faithful
   digital twin to the real physical system to assert the actual printing will be supercompressible


**Comparability contract:** The metric formula, D₁ = 100 mm, E = 3500 MPa, and the
feasibility criteria above are invariant across all design families. You may change geometry
and topology freely; you may not change the reference quantities the metric is normalised
to. If a proposed family makes any of these ambiguous — for instance, if `n_longerons` is
ill-defined for a novel topology — resolve the ambiguity explicitly and justify why the
resolution preserves comparability before running a single simulation.

**Apples-to-apples: same mechanism, same physics, same realizability.** The metric and the
feasibility criteria assume supercompression is achieved as an *elastic material response* of a
*printable, monolithic PLA structure* — the ring rotates and descends while continuous
longerons wind inward, storing recoverable bending strain. A design that satisfies the
numbers by a *different physical route* does **not** count, even with valid numbers:
- **No kinematic mechanisms.** If the criterion-2 compression is reached by a rigid-body /
  pin-jointed **folding** mode — struts or links rotating about joints with negligible
  material strain in the load-bearing members (mls ≈ 0) — the object is a *linkage*, not a
  supercompressible material. Criterion 2 measures global descent; it must be *earned by
  elastic straining*, not by folding rigid bars. A near-zero mls in the primary members at
  high compression is a red flag to investigate, not a pass.
- **Comparable σ.** σ_cr,nd must be a material buckling load on the same footing as the
  baseline. A buckling load set by the *prestress-stabilized geometric stiffness of an
  infinitesimal mechanism* is a different physical quantity and is not comparable.
- **Physically realizable.** The design must be realizable as the printed elastic structure
  the study targets. Idealizations that do not survive printing — frictionless pin joints,
  tension-only (or, worse, compression-carrying) prestressed cables, prestress held in a
  monolithic part — are not admissible substitutes for continuous elastic members. The B31
  slenderness check (**Standing rules**, Infrastructure section) is the *beam-family
  instance* of this principle; a non-beam family needs its own equally-strict fidelity gate,
  not a re-labelled analog that gates nothing.

**Scientific integrity of simulation results:** The infrastructure evaluates designs using
beam finite elements, which faithfully represent structures whose geometry lies within the
validity domain of beam theory. It is the agent's responsibility to ensure that any design
it proposes can be faithfully assessed by the infrastructure it runs it through. Claiming a
simulation result as evidence for a design that violates the assumptions of that simulation
— for example, proposing a geometry so far outside the slender-beam regime that the
simulator produces qualitatively wrong results — is self-contradictory and does not
constitute valid evidence. If a proposed family requires modelling assumptions beyond those
of the current infrastructure, the agent must update the infrastructure to match before
reporting any result.

**Fixed:** Young's modulus E = 3500 MPa, D₁ = 100 mm, ratio_shear_modulus = 0.3677 (G/E — PLA's actual property, not a design variable; see Background).  
**Target: 2× the Bessa point — 0.2244 kPa in the current σ_peak metric (re-derived
2026-08-06, job 4748240; it was 0.2612 kPa when the metric was the eigenvalue) — cleared
with a valid, apples-to-apples-real,
genuinely novel mechanism** — full stop. This is the actual bar. A design that clears the
numeral without clearing originality does not count, and vice versa — see *The challenge*
above for what originality means here, and *Scientific integrity of simulation results* above
for what "valid" requires physically.

**For context, not a bar to clear:** what currently holds the record changes every time a run
closes, so it is not restated here — check **`assets/slides.md`** (the living, continuously
updated record of every tested design and its verdict) and `bo/confirmed_anchors.json` (full
provenance for whichever design is currently confirmed) for the current state. The bar above
(2× Bessa, 0.2244 kPa) is fixed and does not depend on what's currently ahead of it.

### The evaluation window, and how this metric came to be

**The evaluation window.** Everything reported above is measured over Stage-2 increments up to
the FIRST of:

1. **95% compression**. Past that there is no engineering content. The solve is also capped
   there (`compression_cap`), but that is not sufficient on its own: `StaticRiksStep`
   overshoots its own `maxLPF` by 1–6%, so the window must be applied when the response is
   *read*, not only when it is solved.
2. **2% maximum local strain** — Bessa's own limit (criterion 2). Past it the material is
   outside the elastic regime this study assumes, so load carried there is not capacity.

The solve deliberately continues past the 2% strain crossing. the
response beyond the limit shows *how* a design failed, which is what lets a better one be
proposed. `windowed_metrics` returns the unwindowed `mls_full` and `strain_crossing_mcs` for
exactly that purpose. Never feed those to a feasibility check.

**σ_peak is deliberately a maximum over the whole valid window, not a reading at a fixed
point in the squash.** Two things follow:

- **Use `bo/response_metrics.py:windowed_metrics`** to compute this from a Stage-2
  `results.pkl`. Do not hand-roll it; the window rules above are easy to get subtly wrong.
- **Still report `sigma_eigenvalue` alongside it.** It costs nothing, it is what Bessa
  published, and it is the only figure available for a design that never reaches Stage 2.
  Every number in `assets/slides.md` predating 2026-08-06 is in the eigenvalue metric.

---

## More background

A rocking-mast metamaterial is a lattice of `n_longerons` slender elastic longerons arranged
symmetrically around a vertical axis, connected at top and bottom by rigid rings (diameters
bottom D₁ = 100 mm, and top D₂). Under axial compression it buckles into a **coiling mode**: the
top ring rotates and descends while the longerons wind inward, storing recoverable bending
strain rather than fracturing.

Bessa, Glowacki & Houlder (2019) mapped this structure over a 7-dimensional cross-section/geometry
space (fixed topology: one storey, three longerons, no pre-twist) — full parameter ranges and their
own methodology are in `Bessaetal2019.pdf` and its Supporting Information (see Infrastructure table
below); `ratio_shear_modulus` is fixed at 0.3677 (PLA's own G/E) throughout this study for the same
reason they fixed it — it's a material property, not a design variable. Their best
reversibly-coilable point, restricted to circular longeron cross-sections, is **0.1122 kPa/longeron**
in the current σ_peak metric (0.1306 kPa in the retired eigenvalue metric). Call this the **Bessa
point** — every target below is a multiple of it. Their 7D dataset has no strain column and is not
divided by `n_longerons`.

Several agentic runs since then have pushed past that circular-family result. The current best and
the full record of everything else that was tried along the way, including ideas that failed and
why, is in **Backlog from previous runs** at the end of this document — read it before committing to
a direction, but it's worth forming your own view of where the interesting structural territory
might be first.

---

## The challenge

Searching the Bessa 7D space more thoroughly doesn't need an LLM — any Bayesian optimisation
package already does that. What's actually being asked for is *ideation*: a mechanism nobody
has applied to this rocking-mast problem before, good enough that a metamaterials researcher
seeing it for the first time would be genuinely surprised — the kind of design you'd lead a
paper with, not a footnote. That's the result this study exists to produce. A resized
rectangle, however numerically better, is not it.

**Concrete test for "novel enough":** if this exact design were 3D-printed and shown to
genuinely supercompress as claimed, would that result — on its own, the mechanism plus the
physical demonstration — be a strong candidate for a *Nature*-caliber publication? 
A result a metamaterials researcher outside this project
would consider a real, publishable discovery. 

**State the mechanism and why you expect it to work before spending a single simulation on
it.** A literature-grounded trade-off, a first-principles argument, or a documented gap in
what's already been tried (see Backlog) all count as grounding; "this shape looks promising"
does not — that's a guess wearing a hypothesis's clothes, and the Backlog carries the cost of
ungrounded guesses being retried blind, each one re-discovering at full campaign cost what a
stated mechanism would have predicted for free. The literature-reviewer node exists to help
find and ground such a mechanism, and to sanity-check that it's actually novel before you spend
compute on it.

If your design combines a new mechanism with a component already known to clear the floor on its
own — rectangular cross-section currently does (see *The kinematic depth cap*, below) — neither
"the combination clears the bar" nor "the combination beats that same component with the
mechanism removed" counts as evidence: the component alone can already sit near a hard physical
ceiling (rectangular does, 99.7% of one), where no addition can show a measurable gain and a
matched-control test can't tell the difference. **The one test that counts: the mechanism,
attached to Bessa's own circular cross-section, must itself beat the circular Bessa point** —
owed before the result is reported, not after. Mechanisms that don't ride on an already-strong
component have no such confound and no such requirement; test them on whatever cross-section they
need.

Look in the **elastic-instability** half of the metamaterials literature.
Stay out of the **kinematic-mechanism** half — tensegrity, rigid-panel
origami, pentamode lattices — whose large deformation is pin-jointed *folding* with ~0
material strain. A folding linkage is arguably very hard to 3D print. 

**Iterate until your time runs out.** If a family falls clearly short with no upward trend,
call it a dead end and move to the next idea rather than polishing a losing hypothesis.
Evaluate in parallel, off-node (see *Evaluation dispatch*), running Riks only on designs that
clear Stage 1 — but block on any result your next decision genuinely depends on rather than
firing work off and drifting away from it.

---

## Infrastructure

| Resource | Location |
|---|---|
| Linear buckling pre-processor | `scripts/supercompressible_lin_buckle_pretwist.py` |
| Linear buckling post-processor | `scripts/supercompressible_lin_buckle_pp.py` |
| Riks pre-processor | `scripts/supercompressible_riks_pretwist.py` |
| Riks post-processor | `scripts/supercompressible_riks_pp.py` |
| Bessa 2019 paper | `Bessaetal2019.pdf` |
| Bessa 2019 Supporting Information (SI) | `adma201904845-sup-0001-suppmat (1).pdf` |
| **End-of-campaign statistics — use this instead of hand-rolling one** | `bo/campaign_summary.py` — `render(summarize(...))` |
| Imperfection sampling (Bessa's lognormal), deterministic in `seed` | `bo/oracle_circular.py` — `sample_imperfections(n, seed)` |
| Oracle contract + result validator | `bo/oracle_template.py` — `check_result` (non-raising) / `validate_result` |
| Free geometric pre-filters and feasible-set sampling | `bo/prefilter.py` |
| Constrained BO finder (generic, literature-audited) | `bo/cei_core.py` — `run_cei_bo` (sync) / `run_cei_bo_async` (rolling) |
| **Default search strategy — 3-phase shrinking-zoom wrapper around `cei_core`** (matched or beat every alternative tested: plain single-phase CEI-BO, single-region TuRBO, TuRBO-m — see below) | `bo/zoom_core.py` — `run_zoom_bo` |
| Async rolling off-node dispatcher (default, 16-wide — use for any multi-round campaign) | `bo/async_dispatch.py` (`SlurmAsyncPool`) — see Simulator behaviour |
| Synchronous off-node array dispatcher (single-batch only, superseded for adaptive campaigns) | `bo/slurm_batch.py` |
| Bessa 7D generalized cross-section dataset (50,000 pts, **not strain-verified**, and its σ_critical is computed **without geometric imperfections** — Bessa SI, so it is directly comparable to our `sigma_eig` and NOT to `sigma_peak`) | `data/{input,output}.csv` |
| **Response metrics — σ_peak / E_absorbed / the evaluation window** (use this, do not hand-roll the windowing) | `bo/response_metrics.py` — `windowed_metrics` |
| **Reference oracle for a design family — copy this to wire a new family** (contact on, cap lifted, full objective set, feasibility on the WINDOWED mcs/mls, pre-solve geometric gate, never raises) | `bo/oracle_circular.py` — `evaluate(x)` |
| **End-to-end template check** — recovers the known circular optimum through the whole gold stack; run it after changing any of scripts/, bo/, or the metric | `bo/run_recovery_circular.py` + `.sbatch` |
| Joint restrained-warping/bending check (analytic + linear-local 3D, checks whether a B31 beam's peak-strain reading survives real joint physics — no artificial cut boundary) | `validation/warping_check/` — see README there, and Standing rules below. Supersedes the earlier nonlinear FE submodel approach, archived at `validation/archive/continuum_submodel_fe_v1/` (kept for its reusable mesh-building technique, not as the recommended tool). |

The pre-processors above are the default path, which covers the circular, anisotropic-rectangular
(`RectangularProfile`), and generalized cross-section families; the hollow box-tube family uses
`scripts/supercompressible_{lin_buckle,riks}_box.py`. A new family normally starts by copying and
adapting the pre-processor closest to its geometry.

### Evaluation dispatch — parallel by default, async by default

Every oracle evaluation is a separate ~75 s Abaqus solve, but the real distribution is
heavy-tailed (p50 ≈53 s, p90 ≈309 s, occasional grinders to a 30-min cap). **For any
multi-round adaptive campaign (i.e. any real BO search), dispatch via the async rolling
pool, `bo/async_dispatch.py` + `cei_core.run_cei_bo_async` — this is the gold primitive,
not `bo/slurm_batch.py`:**

```python
import sys; sys.path.insert(0, "bo")            # bo/ is flat on sys.path
from async_dispatch import SlurmAsyncPool
from cei_core import run_cei_bo_async

pool = SlurmAsyncPool("my_campaign:evaluate_point",   # 'module:callable', item -> result dict
                       account="mbessa-condo", sys_path=[str(campaign_dir)])
result = run_cei_bo_async(bounds, constraints, "sigma_crit", pool,
                          n_doe=..., max_evals=..., concurrency=16)  # size to your dimensionality, see below
```

**Why this, not the synchronous batch dispatcher.** A synchronous round (`slurm_array_batch`,
still available below) is parallel *within* a round but has a hard barrier *between* rounds —
every round blocks on its slowest solve, so a round of 8 typically finishes ~6 fast solves in
~2 min then idles those slots for ~28 min on 1–2 stragglers (measured live: time-averaged
concurrency ~0.8/8, i.e. ~18 evals/hour against ~90 the allocation could sustain). The async
pool keeps `concurrency` solves in flight continuously — the instant any one returns, it's
ingested, GPs refit, and a fresh candidate dispatched into the freed slot; no slot ever idles
waiting on a straggler, and every solve carries a hard per-solve timeout (auto-`scancel`). Use
this for every multi-round campaign — `bo/slurm_batch.py`'s `slurm_array_batch` is superseded
for that use case (kept, and still marked as such in its own module docstring, only for a
**single one-shot batch with no adaptive loop**, e.g. a fixed Sobol DoE sweep or the one
per-run anchor reconfirm below).

### Per-solve time budget — 10 minutes by DEFAULT, and you may move it

`bo/oracle_circular.py` sets `MAX_SOLVE_SECONDS = 600`. A Stage-2 solve exceeding it is
terminated and reported as not-evaluable (`timed_out=1`, NaN objective).

**This is a default against wasted compute, not a property of the world.** It exists because an
uncapped campaign is unbounded and because a runaway solve holds licence tokens other solves
need. Neither says anything about which physics is worth simulating — **if your idea needs a
longer solve, raise the cap for that idea and say what it bought:** the new value, how many
designs you spent it on, and what you learned. A deliberate, reported cap change is ordinary
practice, not a transgression, and an idea that genuinely needs an expensive solver regime is
not thereby a bad idea — **"it does not fit the default cap" is not a finding about the design
space.** Measured solve costs across families, and the per-family cost ratio to budget an
escalation from, are in `docs/EVALUATION_UNDER_CONTACT.md` §4.

**You can watch and revoke a solve instead of betting on it.** `SlurmAsyncPool` takes an
optional `promise_dir`; with it set, every submitted solve gets a row in its own f3dasm
`ExperimentData` and gains two verbs — `pool.cancel(h)` leaves the point re-drawable,
`pool.abandon(h)` closes it. **Neither costs eval budget: only FINISHED work counts** — that is
what makes raising the cap safe rather than merely permitted. Off by default so a normal run
leaves no store that could be mistaken for the evaluation ledger; see `bo/promises.py` and the
commented lines in `bo/run_campaign_tape_spring.py`.

**Target concurrency = 16** (`bo/async_dispatch.DEFAULT_CONCURRENCY`) — this is the **hard
licence ceiling, not a safety margin**: a Riks solve checks out 2 QAE tokens against a pool of
32, so 16 concurrent solves already consumes the entire licence with zero headroom for any other
job on this server. Do not raise concurrency above 16 without first confirming nothing else
needs a token at the same time; validated end-to-end via `bo/smoke_async_recover.py`. Raising
the per-solve cap costs you *time*; raising concurrency past 16 starves everyone else. Trade
wall clock freely, trade tokens never.

**Eval budget is not infra-enforced — size it to how many free dimensions you're searching, not
to a fixed round number that happened to work for a different family.** Neither `bo/cei_core.py`
nor `bo/zoom_core.py` has a built-in dimension-aware default. Prefer `bo/zoom_core.py`'s 3-phase
shrinking-zoom wrapper over a single flat `cei_core` pass — a flat pass reliably under-recovers a
known optimum at a matched budget (numbers in the Infrastructure table and
`docs/self_contact_spec.md`'s search-layer table).

⚠️ **`bo/experiments/_real_3d_oracle*.py` (five variants) and `bo/experiments/real_designs/*`
are SUPERSEDED and unported.** They compute σ from the Stage-1 eigenvalue, never call
`response_metrics`, and predate ground contact and the lifted compression cap. Start from
`bo/oracle_circular.py`.

**Reserve `gen.call(data, mode="sequential")` for a SINGLE point** (e.g. the one per-run
wiring check below) — a multi-point campaign run sequentially wastes ~N×75 s of wall for no
reason.

**Record where each ODB lands.** The oracle writes the ODB path into each sim's `results.pkl`
(`lin_buckle_odb` for Stage 1, `riks_odb` for Stage 2). Surface these in your ledger — e.g.
`domain.add_output("riks_odb")` — so later mode-shape audits or re-inspection can retrieve the
exact ODB directly instead of brute-force-matching parameters across thousands of scratch dirs.

> ⚠️ **Never use `gen.call(mode="parallel", nodes=N)`.** It falls through to f3dasm's
> `mp.Pool(N)`, which spawns N Abaqus solves as **local subprocesses on the run's 4-core /
> 16 GB orchestration node** — CPU oversubscription and OOM that kills the run. Parallelism
> is ONLY safe as one-solve-per-SLURM-array-task, never a local pool.

### Confirmed anchors — do not re-solve

`bo/confirmed_anchors.json` holds gold-verified reference designs (inputs + confirmed
σ_cr,nd / mcs / mls / slenderness + provenance). **Treat these as this-run-valid feasible
baselines; do NOT re-solve them per delegation** — a re-solve of a known point is pure
wasted budget. The strategizer runs **exactly one** oracle-wiring check per run: re-solve a
*single* anchor and confirm it reproduces its `sigma_crit` within ±1%. If it reproduces, the
whole seed is validated for this run and every anchor value may be cited directly. (This one
check is cheap insurance — it has caught oracle-wiring drift before, e.g. a reference point
failing to reproduce its expected mcs.) Downstream delegations **read the file, never
re-solve.** New confirmed bests are appended only after the run's critic gate passes.

You may read, modify, or replace any of the Abaqus scripts. A new design family will almost
certainly require changes to the pre-processor. If your geometry needs a different element
type, mesh strategy, or boundary condition, implement it.

**Abaqus:** `module load abaqus/2024-mbessa-pskx` · `export LANG=en_US.UTF-8`

**`bo/cei_core.py` is a template handed to you, not a finished pipeline.** It's a generic
constrained Bayesian optimization core (Constrained Expected Improvement, Gardner et al. 2014;
Constant-Liar batch proposals, Ginsbourger et al. 2010 — read the module docstring for which
parts are ported from the cited papers and which are standard practice), problem-agnostic — you
supply `bounds`, an `evaluate(x)` callback, and a `ConstraintSpec` list. Wrap it with
`bo/zoom_core.py`'s 3-phase shrinking-zoom by default rather than calling it flat/single-phase
(see the Infrastructure table and Eval budget section above for why). Use either as a starting
point once a family is parameterized, adapt it, or write something else entirely: you're
expected to work efficiently and be scientifically grounded.

### Simulator behaviour

The oracle runs a two-stage Abaqus analysis on B31 beam elements: Stage 1 is linear-eigenvalue
buckling (`sigma_crit`, `coilable`); Stage 2, run only for coilable designs, traces the
post-buckling coil (`max_compressive_strain`, `max_local_strain`). **Stage 2 is energy-free by
default** — a `StaticRiksStep` arc-length solve, matching Bessa (2019 SI: pure arc-length, no
damping), which traverses the coiling limit point without dissipating artificial energy.
**Automatic stabilization is an opt-in** (`stabilization=True` in the design params): it swaps in
a general `STATIC` step with `DISSIPATED_ENERGY_FRACTION` damping for designs whose coil has a
genuine *snap* instability that arc-length cannot cross energy-free (e.g. a bar-hinge / Kresling
lattice). When used, it is gated: a design is accepted only if its dissipated-stabilization /
strain-energy ratio `max(ALLSD)/max(ALLSE)` stays below 0.05, so a collapse coaxed through by
artificial energy is flagged rather than counted. 
**Stabilization is a DIAGNOSTIC, not a production setting.** Run energy-free by default. If a
solve does not complete, that is a *result*: record it and move on — do not switch stabilization
on across a campaign to make non-converging designs converge (measured: it can cost 20× the
solve time for a fraction more of the load path and still not finish; see the deck's
`Run 20260809T230403` summary speaker notes for the measured numbers). Legitimate uses:
understanding why ONE design fails, and reproducing a known anchor (`test_nocontact_anchors.py`
needs it for two of the four — a regression check, not a search). When used it stays gated on
physics as well as cost: a result counts only if `max(ALLSD)/max(ALLSE) < 0.05`.

**A non-converged solve costs a BO campaign nothing.** `bo/oracle_circular.py` returns NaN for
the objective and `bo/cei_core.py` drops non-finite objectives from the objective GP while still
training the constraint models on that point — designed behaviour, not a gap. See
`docs/TRAPS.md` §3 for what goes wrong when a non-converged result is instead compared as if it
were 0.0, or silently passes a threshold check.

**Contact — the default, and what is left to you (rewritten 2026-08-06).** In
`scripts/supercompressible_riks_pretwist.py`, longeron material contacts **the ground / bottom
disc face** and **the top disc's underside**. Both are **on by default**, and both are
**frictionless and separable**: they slide without friction, carry compression only, and may
separate freely at any time. Model it this way unless you have a stated, justified reason to do
otherwise. Bessa et al. (2019) modelled the ground (SI Figure S11: "an early contact event
between the longerons and the ground", caption "the gray plane represents the ground") and
their support rings are rigid bodies, so this is fidelity, not embellishment — the ground plane
had in fact been present all along and was removed on 2026-07-16 on a **misidentification** of
the surface as an artificial "central plane" (see `docs/self_contact_spec.md` Part 7).

Only the **inward-facing** faces of the two discs are modelled — the top face of the bottom
disc and the underside of the top disc — because longerons attach at the disc perimeter and
coil inward, so those are the only faces they can reach. That is what lets the discs be
contactable **without inventing a disc thickness or radial width** Bessa never specified: a
zero-thickness rigid face at a plane the model already has adds no structural material, it only
stops penetration. Confirmed inert for the reference designs (σ and strain unchanged to 4 s.f.).

**Contact is not the same thing as the attachment.** How a longeron *end* is joined to its ring
— pinned, fully fixed, or otherwise — is a per-design boundary condition that remains yours to
choose, state explicitly, and justify. Nothing above constrains it.

**Longeron-to-longeron contact is still NOT modelled**, but you can now CHECK whether your design
silently relied on it. `scripts/self_clearance.py` walks each longeron's deformed centreline
straight from the ODB's own `COORD` output — the same read `ring_passthrough` uses — and reports
the minimum clearance between different longerons at every frame, at **zero extra solve cost**.
Opt in per solve by setting `SC_TIER1_RADII` (JSON, per-longeron circumscribing radius) and
`SC_TIER1_NLONG`; results arrive as `self_clearance_series` on the Riks result. Validated on the
Bessa anchor: no interference, 58.9 mm minimum clearance. **A design whose coil interpenetrates
has not been simulated — it has been simulated in a world where matter passes through itself**,
which is the same failure `ring_passthrough` exists to catch one level up.

**Longeron-to-longeron contact — the modelling itself — is excluded** exactly as in Bessa, who
excluded it explicitly *and designed around it* (their taper exists "to create space in order to avoid
self-contact", and they used 10 longerons where 11 fit "to ensure no contact among longerons").
A family whose mechanism depends on members bearing on each other must add it and justify the
settings — and read `docs/self_contact_spec.md` Part 2 first, because a naive attempt already
cost this study a campaign: HARD, no-separation contact took Stage-2 convergence from 64% to
9.5%.

⚠️ **Contact migration status varies by family and changes over time — do not trust a list of
migrated/unmigrated families in any document, including this one.** Check the family's own
pre-processor script directly for `ground_contact` and a `SurfaceToSurfaceContactStd` call
before assuming its numbers are (or aren't) comparable to a contact-migrated family. Migrate the
one you use before comparing if it isn't already, and say that you did.

`ring_passthrough` (see **Standing rules**, below) remains the post-hoc check for material
routed through a ring's footprint, computed by `scripts/supercompressible_riks_pp.py` from the
Riks ODB's `COORD` field output. Its meaning has changed for the two migrated discs: contact now
*prevents* that physically, so a passthrough there indicates a contact-setup fault rather than
an unmodelled physical event. It is still load-bearing for any family whose pre-processor has
not been migrated.

The rules below are the current oracle contract. Each was learned the hard way in a prior
run, but you only need the rule:

- **`ratio_shear_modulus` guard:** guard every sample for rsm > 1/3 (≈ 0.334) before
  dispatch — an isotropic material with ν ≥ 0.5 makes Abaqus abort during input-file
  processing.
- **Do not retry a non-converging solve (`n_retries=1`).** Riks/Static non-convergence is
  deterministic — retrying re-runs the identical failure and writes a duplicate ledger row.
  Record `converged=False` with whatever partial result exists (the salvage path) and move
  on. Reserve retries for genuinely transient failures (e.g. a killed licence checkout).
- **Do not set `delete_temp_files=True` on `AbaqusSimulator`.** It deletes the `.log` that
  `abaqus2py`'s completion-polling and driver-crash detection read to know the job finished.
  Clean up disk yourself instead.
- **Death detection is stall-based** (`max_stall_time`, set by `workspace/data_generator.py`
  to 60 s for linear-buckle and 120 s for Riks): it fails only after true file-silence, so a
  slow-but-alive job under high concurrency is never mistaken for dead. On timeout the
  simulator calls `abaqus terminate` to release the licence token and scans the completed
  job's `.msg` for `***ERROR` before post-processing. Driver crashes (a Python `Traceback` in
  the `.log`) now fail fast — extend `DRIVER_FAILURE_MARKERS` in
  `abaqus2py/src/abaqus2py/_src/abaqus_simulator.py` if you hit a new class that isn't a
  `Traceback`.

### What contact changed about how you must EVALUATE (added 2026-08-09)

Enabling contact was not a fidelity tidy-up. Bessa's floor was measured **without** the ground
plane; turning ground and disc contact on is a wager that designs exist whose **second
configuration** — the one they find after buckling and after landing on a surface — carries load
the first cannot. That comes with a heavier solve, a longer tail, and a nonlinear branch that is
imperfection-sensitive. Four consequences:

1. **σ_crit is unchanged by contact; σ_peak is not — and the gap is where the new physics lives.**
   `*BUCKLE` linearises about a base state where nothing is touching, so the eigenvalue is
   untouched for every design, deductively. **σ_eig screens, it never concludes** — it cannot see
   80% compression, the 2% strain limit, ring pass-through, or energy absorbed, and it ranks far
   better within a family than across families. Never rank two families on σ_eig.

2. **A contact-mediated design owes a sampled imperfection study, not one solve.** With contact
   there is more than one post-buckling configuration available and the imperfection selects
   between them. Classify cheaply — solve once with contact off; if the answer moves, escalate to
   5–10 draws (`sample_imperfections(n, seed)`) and report the distribution and the full curve.
   **σ_peak is intrinsically imperfection-dependent** (a point on a curve, not a number with
   scatter), and **zero imperfection is not an available setting** — a perfectly symmetric mast
   has no symmetry-breaking trigger and the Riks solve fails outright. On a contact-mediated
   design the imperfection can select *which configuration forms*, not just nudge the magnitude —
   sample when it can change the mechanism, not merely the number.

3. **There is no single cost ratio; using one is how a plan goes wrong.** Stage 1 is far cheaper
   than Stage 2 on average, but the worst observed single design is an order of magnitude above
   that average, and the solve cap censors the tail so that is a lower bound. Budget a *sweep*
   from the mean; budget an *escalation* from the tail, because a design that reaches a new
   configuration is by definition one that did not die early.

4. **Cheaper than Stage 1 is no solve at all.** Anything decidable from the parameters belongs in
   `bo/prefilter.py` at microseconds, not in Abaqus. Sample log-uniformly over any parameter
   spanning more than a decade — a uniform draw over a 60×+ range puts most samples far from the
   interesting end.

The worked evidence, the measured tables (including the exact cost ratios and imperfection
sensitivity exponents), and the escalation protocol in full: **`docs/EVALUATION_UNDER_CONTACT.md`**.

### Standing rules and examples of previous failure modes to avoid

1. A good, cheap, first proxy for supercompressibility is the first Abaqus buckling mode
   being a coiling mode (`coilable = True`) checked via linear eigenvalue analysis.
2. **Faithful simulations.** Consider every assumption baked into the infrastructure you build.
   Most of it uses B31 beam elements, valid only above slenderness = `ratio_pitch / (2 × d_max)` ≥ 10
   (`d_max` = largest cross-sectional half-dimension; Meza et al. 2017; Portela et al. 2018) —
   enforced in `bo/prefilter.py`'s `slenderness()` / `passes_slenderness()`, which is where a
   non-beam family's own fidelity gate belongs too.
3. Always test programatically the cheaper conditions first, to avoid wasting compute time.
4. **Ring-passthrough.** Previous infrastructure, mimicking Bessa et al, used the no-contact mode of Abaqus.
   The top and bottom rigid rings are modelled as 0-D reference
   points, kinematically coupled to the longeron end joints. Nothing in the model stops a longeron's own material
   from swinging straight through a ring's nominal footprint as the mast coils, which a
   real printed ring — solid material — would physically block. `ring_passthrough`
   (`scripts/supercompressible_riks_pp.py`) checks every Riks frame for a longeron node
   that ends up on the far side of either ring's current z-plane while still within
   that ring's own radius; `True` means a result is not valid evidence, same as any other
   feasibility failure. Not a hinge-specific quirk — **any longeron with more than one
   rigid/compound member** (a hinge, or separate chords + rungs) has the geometric freedom to
   fold this way; a plain single continuously-bending beam does not.

5. **A beam-theory strain reading at a rigid joint is not automatically trustworthy — check it
   against a real 3D model before trusting a close call.** The rectangular-family incumbent's own
   strain reading at the ring joint was challenged and then resolved exactly this way. Full story,
   method, and current per-design validity status: `bo/confirmed_anchors.json`'s `run17_rectangle`
   entry and the deck's D24 speaker notes. `validation/warping_check/` is the tool — run it on any
   new design whose winning margin rides on a joint-adjacent strain reading.

6. **See *The challenge*, above, for the compound-design rule** (a component already known to
   help on its own must not get credit for a new mechanism's headline number). Concrete case this
   study already hit: a bistable arch segment spliced into an otherwise-unmodified longeron
   cleared σ_peak, but the splice was not the reason — its one large, imperfection-sensitive
   snap-through spike sits far above the rest of the curve, and the design's sustained post-snap
   capacity actually sits below what the unmodified baseline alone scores. The splice made things
   worse, not better.
7. **Beat D42, don't refine it** — a tuned serpentine-wave perturbation is not a new mechanism.

These are what the default infrastructure already checks for you — a starting point, not a
ceiling. You may modify or replace any of it for a new family, provided you can still argue
the result is faithful, not an artifact (see "Scientific integrity of simulation results" above).

---

## Expected output

- The winning design family: key parameters and the physical mechanism behind the improvement
  in one sentence.
- For the winning design: σ_cr,nd value, coilable status, and Riks max compressive strain.
- The sequence of all families explored, with a one-line verdict on each.
- **For every campaign you run: the output of `bo/campaign_summary.py`.** One call, at the end:

      from campaign_summary import render, summarize
      print(render(summarize(X, results, PARAM_NAMES, objective="sigma_peak",
                             bounds=BOUNDS, floor=<current incumbent, see
                             bo/confirmed_anchors.json>, target=0.2244)))

  It gives, at a glance, the funnel on the decided denominator, **which criterion binds and by
  what factor** (which separates "the idea is wrong" from "the idea is badly tuned" — different
  next moves), and **which free parameter actually moved the blocker**, rank-correlated and
  corrected for the number of parameters you tested.

  **Do not write your own.** Not a style preference — every hand-rolled version of this in the
  study's history has reproduced at least one of the same errors (the `NaN < 0.90` trap covered in
  `docs/TRAPS.md` §3 is the one that matters most), and the reviews caught them after the
  conclusions were already written. The module handles the decided-vs-attempted denominator, empty
  responses, statistics the reporting window saturates, and the objective being incomparable to the
  floor when nothing was feasible. Extend it if it is missing something; do not replace it.

---

## Backlog from previous runs

Every idea tried across this study's closed runs — precisely what was tried, where it came
from, the stats, and the verdict — now lives in **`assets/slides.md`** (a Slidev deck), one
slide per genuinely new idea, anti-chronological (most recent run first), plus a summary slide
per run listing every hypothesis tested (including refinements/retries, which don't earn their
own slide but are recorded there). **Read it before proposing a new family** — a mechanism you
think is novel may already have a verdict there. View it with `pnpm run dev` inside `assets/`
(or read the markdown directly if you don't need the rendered form).

Two things to know about how to read it. First, each idea slide may carry a **`Seed:`** bullet,
which says whether the *idea* can still generate a new design — independent of whether that
*experiment* worked. `FERTILE` names a perturbation nobody has tried; `BARREN` means no
perturbation reaches the blocker, which includes the case of a design that succeeded and became
the floor (re-deriving it is not a contribution). Second, the **re-study slides** near the front
record five families re-examined after ground contact was restored, and they distinguish sharply
between a family that was *tested* and one whose infrastructure merely now *exists* — three of
the five are the latter.

And before your first campaign, read **`docs/TRAPS.md`**. It is the list of things that have
already cost this study a campaign apiece — Abaqus invocation rules, contact settings that look
harmless and are not, statistics that are saturated by construction, and the standing rule for
how much a single observation is worth (short version: a tooling fact is settled by one clean
observation; a claim about how a *family behaves* is settled by none). Its companion
**`docs/FLAKY_DESIGNS.md`** lists the designs and families that misbehave numerically, and every
row states how many observations it rests on — most say one, which makes them warnings to budget
for rather than verdicts to cite.

### The kinematic depth cap — read this before proposing a cross-section (measured 2026-08-12)

Run `20260812T014026` measured the law that explains why 28 idea families produced one incumbent.
**Do not re-derive it, and do not search against it.**

**κ_max, the coiling curvature, is a KINEMATIC INVARIANT set by the ring geometry — not by the
member.** Measured `mls_full / c` = 0.021600, 0.021658, 0.021641, 0.021714 across a **2× change in
depth**, and within ±15% of its median over a 24-point LHS, with the residual tracking taper
(Spearman 0.786) exactly as κ ≈ 1/R_mean predicts. Two consequences:

- The 2% strain criterion is therefore a **pure geometric cap on the winding-plane half-depth**:
  `c ≤ 0.02/κ ≈ 0.92 mm`. No design at or above c = 1.00 mm reaches 80% compression inside the
  strain budget, whatever you do with width, storey height, or taper (H7, SUPPORTED).
- **σ_peak ∝ E·w·c³/L², where c is capped kinematically and w is capped by the slenderness ≥ 10
  fidelity gate.** Every family that varies the *member* inherits both caps. That is the whole
  explanation of the backlog.

**`run17_rectangle` sits at 99.7% of that cap.** The incumbent is not a lucky design — it is the
design that reached the ceiling. A new cross-section, taper, or storey height cannot beat it by
more than the 0.3% of headroom the cap leaves.

**So a design that beats the incumbent must move the wall, not search under it.** Two levers move
it. Both have been measured, both are closed, and **neither is the answer** — read them as tools
for raising the floor under a new mechanism, not as candidate mechanisms:

1. **Flare the rings** (negative `ratio_top_diameter`). The cap is `0.02/κ_max` and κ_max falls as
   the mean ring radius grows, so flaring raises the cap in proportion (SUPPORTED, run
   `20260812T014026` H9). Cheap, and it works. **It is not a novel mechanism, and this is not an
   open question:** `ratio_top_diameter` is one of Bessa's own seven variables, and flaring extends
   it negative on unchanged topology — the definition at the top of this document excludes exactly
   that ("a simple perturbation from the Bessa infrastructure is not a valid design"). A run that
   re-adjudicates this has spent budget on a question the contract already answers.
2. **Pre-coil the member** (`bo/oracle_helical.py`, built — do not rebuild it). Strain is c × the
   curvature **CHANGE** from the as-manufactured shape, so a longeron manufactured already-curved
   starts with κ₀ and supplies only `κ_max − κ₀`: wrap 4.5 at c = 2 mm reaches **61.5% compression
   at 0.445% strain** (see the deck's D30 speaker notes). The relief
   is real and **it does not buy load** — over 36 decided designs ρ(wrap, σ_peak) = **−0.392**,
   larger in magnitude than the taper's +0.287 and *negative* (run `20260812T222030` H2,
   FALSIFIED). It is also a known-mechanism transplant: intrinsic-curvature strain relief is
   settled Kirchhoff-rod theory. Two caveats: neither correlation survives Holm at p < 0.05, and
   the deep-wrap region (|wrap| 2–5) where relief is largest is **numerically inaccessible** — 0 of
   107 rows reached a coiling mode, 19/19 Stage-2 solves crashed. That is an open *solver* problem,
   not a design lead.

**The deliverable is a mechanism, and exhausting the leads above does not produce one.** Both
levers were handed to you already measured; confirming or re-litigating them is the cheap move and
it is not the task. A run that falsifies its leads and then closes with most of its budget unspent
and no new candidate mechanism on the table has not finished the job — it has established that the
easy directions are still closed, which was already known. Ideation is the expensive part and it is
the part being asked for.

### The current baseline

The target is **2× Bessa (0.2244 kPa in the σ_peak metric) plus genuine mechanism novelty** (see
Objective, above). Whatever currently holds the record is context, not the bar, and it changes
as runs close — see `assets/slides.md` and `bo/confirmed_anchors.json` for the current state and
full provenance, not this document.

### For raw evidence beyond the deck

The deck's speaker notes carry most of what used to be written out here directly, but for
anything deeper: each run's `debug/strategizer_notes/hypotheses.json` (full status history and
the evidence behind every verdict, including cases where an initial verdict was later
corrected under adversarial review), `debug/retrospectives.jsonl` (first-person CONSISTENCY /
DECISION / FRICTION / BLOCKED entries — the DECISION entries explain why families were declared
dead ends), and `debug/delegations/<ID>/` (raw sub-task driver scripts and logs) remain the
ground truth underneath every deck slide. `data/idea_odbs/` holds a permanent, non-scratch
archive of the solved simulation (ODB) for every genuinely-new idea that has one — see its own
`MANIFEST.md` for the full classification and provenance trail.
