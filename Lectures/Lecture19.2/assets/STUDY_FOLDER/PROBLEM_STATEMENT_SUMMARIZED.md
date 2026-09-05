# Supercompressible metamaterial — the brief, in one page

*A faithful summary of `PROBLEM_STATEMENT.md` (666 lines). Nothing here is new; the
long version governs. Quotations are verbatim.*

## The structure

A building block that must **compress to a fraction of its height and spring back**, while
still carrying load. It is a deployable mast crossed with a thin-walled conical frustum: two
rings joined by slender longerons. Under axial compression it buckles into a **coiling mode**,
the top ring rotating and descending while the longerons wind inward. If that mode governs, a
brittle PLA structure survives past 80% compression without fracturing. Bessa, Glowacki &
Houlder (2019) mapped this space and found printable designs that coil and carry load.

## What is being asked for

Not a better point in Bessa's box. A **new mechanism**.

> "Searching the Bessa 7D space more thoroughly doesn't need an LLM — any Bayesian
> optimisation package already does that. What's actually being asked for is *ideation*: a
> mechanism nobody has applied to this rocking-mast problem before."

The operational test for novelty is concrete: if the design were printed and shown to
supercompress as claimed, would that be a credible *Nature*-caliber result on its own? A
resized rectangle is not.

## Objective

Maximise the peak compressive stress, per longeron:

    sigma_peak = P_max * 1000 / ( (pi * D1^2 / 4) * n_longerons )      [kPa per longeron]

`P_max` is the largest axial reaction force reached during Stage-2 compression, inside a
defined evaluation window. Dividing by `n_longerons` removes the trivial gain from simply
adding more of them.

## Feasible means all three

1. **Coilability** — max compressive strain >= 0.80, i.e. it compresses to 20% of its height
   without the load reversing.
2. **Strain** — max local strain <= 2% anywhere, up to that point. Bessa's own criterion.
3. **Printable** — realizable as a monolithic PLA part.

Fixed for every design: `E = 3500 MPa`, `D1 = 100 mm`, `ratio_shear_modulus = 0.3677`.

## The bar

**2x the Bessa point = 0.2244 kPa, *and* genuine mechanism novelty.** Both, or it does not
count. Whatever currently holds the record is context, not the target.

## Two rules that shape agent behaviour

**State the mechanism before spending a simulation.** Literature grounding, a
first-principles argument, or a documented gap all count. "This shape looks promising" does
not — "that's a guess wearing a hypothesis's clothes."

**Spend the whole budget.** A run that closes early on negative results is not a valid run.
The statement instructs the critic directly, in capitals, to REJECT one that does.

## What a run must hand back

The winning family and its mechanism in one sentence; that design's stress, coilability and
Riks strain; **every family tried, with a one-line verdict each**; and the output of the
shared `campaign_summary.py`, which reports which criterion binds and by how much.
