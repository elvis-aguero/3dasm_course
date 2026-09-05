# Two critic reviews, in full

Both are `REJECT`. Both are the run's own adversarial reviewer, reading the run's own
deliverable. Every review in this study has the same six sections: **Actions taken**,
**Findings** (each labelled CRITICAL / MAJOR / MINOR), **Verdict**, **Numbers**, and a
**Retrospective**; some add a **Handbook pointer**.

## A. The better design sitting in the run's own data

`REVIEW_A_better_design_in_own_ledger.md` — run `20260729T012952`, call 4 of 9.

The deliverable concluded that *"no new mechanism was confirmed to beat, or even to validly
reach, the existing 0.7704 kPa baseline"*, and named the plain run-17 rectangle as the winner.

The critic applied **the notebook's own `feasible_mask()`** and **the notebook's own
`seg_slenderness` formula** to **the ledger the notebook itself loads**, and found rows that
pass every one of those tests at a higher stress: **0.825059 kPa against the 0.770352 kPa it
called the champion.** No external standard was imported. The run's own criteria contradicted
the run's own conclusion.

Gate sequence for that run: REVISE, REVISE, REVISE, **REJECT**, REVISE, REVISE, REVISE,
REVISE, PASS.

## B. A test that could not have failed

`REVIEW_B_test_that_could_not_fail.md` — run `20260814T015148`, call 1 of 3.

The deliverable reported an 18-point sweep of a cone-shaped ground disc that found *"a
completely flat, zero-effect response"*, and closed one hypothesis FALSIFIED and its mirror
SUPPORTED on that basis.

The critic showed the sweep had derived its own onset-of-contact at `cone_rise_ratio = 0.19943`
and then applied a 0.5 safety margin, capping the range at 0.0997 — sweeping only the half of
the parameter furthest from ever making contact. At the most extreme point tested, a 1.66 mm
gap remained of a 3.324 mm standoff, and an independent diagnostic showed it never narrowed.
The contact model is hard and separable, so pressure is exactly zero until the gap reaches
zero. Therefore a flat result at all 18 points was, in the critic's words, *"a mathematical
certainty of the test's own construction, not evidence"*.

Gate sequence: **REJECT**, **REJECT**, PASS.

## Why these two

A needs no physics: higher is better, and the answer was in the run's own spreadsheet. B needs
some contact mechanics but carries the deeper lesson, and it is one that travels well past
agentic workflows: ask whether the experiment could have come out any other way.
