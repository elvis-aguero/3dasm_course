# Two critic reviews, in full

## Where these come from

The critic is one of five agents. It cannot write or execute anything: its tools are `Read`,
`Glob`, `Grep` and read-only access to the evaluation ledger. It is invoked when the
strategizer decides the run is finished and calls `Done(summary)`. That call does not close
the run; it requests closure. `CriticGateMixin` puts the deliverable to the critic, which
returns one of three verdicts.

| verdict | effect |
|---|---|
| `PASS` | the run may close |
| `REVISE` | the strategizer goes back to work and calls `Done()` again later |
| `REJECT` | the same, with a CRITICAL finding attached |

The deliverable under review is always `pipeline.ipynb`, the notebook the run wrote. The gate
re-executes it, so the critic reads both the prose and the code that produced the numbers, and
it quotes the claims it objects to by notebook cell id.

Across 36 runs the gate was called 135 times: **33 PASS, 73 REVISE, 22 REJECT.** No run in the
study passed on its first attempt.

Every review has the same six sections: **Actions taken**, **Findings** (each labelled
CRITICAL, MAJOR or MINOR), **Verdict**, **Numbers**, **Retrospective**, and sometimes a
**Handbook pointer** into the falsification charter.

---

## A. The better design sitting in the run's own data

`REVIEW_A_better_design_in_own_ledger.md` — run `20260729T012952`, **call 4 of 9**.

**The run.** The smallest-budget run in its batch, 93 evaluations and $23.10. It proposed no new
design family; all three of its hypotheses were refinements of two existing ones, the chiral
brace and the bistable arch. It ended with H4 falsified, H3 confounded, and H2 never tested at
all.

**What the deliverable claimed at call 4.** That *"no new mechanism was confirmed to beat, or
even to validly reach, the existing 0.7704 kPa baseline"*, and that the winner, for this run and
cumulatively across the study, was the plain run-17 rectangle.

**What the critic did.** It took the notebook's **own** `feasible_mask()` and the notebook's
**own** `seg_slenderness` formula, applied them to the ledger the notebook itself loads, and
found rows that pass every one of those tests at a higher stress: **0.825059 kPa against the
0.770352 kPa the run had just called its champion.** No external standard was imported. The
run's own criteria contradicted the run's own conclusion.

**Where it went.** Gate sequence `REVISE REVISE REVISE `**`REJECT`**` REVISE REVISE REVISE
REVISE PASS`. The run did not discard the finding: the final review, nine rounds later, records
"the best unvalidated candidate" among the two most load-bearing numeric claims it spot-checked
before passing. The design the critic surfaced was carried into the deliverable as an
acknowledged candidate rather than quietly dropped.

---

## B. A test that could not have failed

`REVIEW_B_test_that_could_not_fail.md` — run `20260814T015148`, **call 1 of 3**.

**The run.** This is the run that discovered contact had never engaged. Two mechanisms that both
depend on something touching something else: a secondary elastic "stop" meant to engage after
the primary member reaches its strain limit, and a shallow conical ground disc meant to change
where the coil bears. 33 evaluations. **All 21 finite stress values it produced were the same
number, `0.6071319332676687`, bit-identical** — the incumbent rectangle. Nothing had ever
touched, so every converged design was the baseline wearing a new pre-processor.

**What the deliverable claimed at call 1.** That an 18-point sweep of the conical disc had found
*"a completely flat, zero-effect response"*, and on that basis closed one hypothesis FALSIFIED
and its mirror SUPPORTED.

**What the critic did.** It read the sweep's own derivation. The campaign had computed its
onset-of-contact at `cone_rise_ratio = 0.19943`, applied a 0.5 safety margin, and capped the
swept range at 0.0997 — sweeping only the half of the parameter furthest from ever making
contact. At the most extreme point tested, 1.66 mm of a 3.324 mm standoff still remained, and an
independent diagnostic showed the gap never narrowed. The contact model is hard and separable,
so pressure is exactly zero until the gap reaches zero. A flat result at all 18 points was
therefore, in the critic's words, *"a mathematical certainty of the test's own construction, not
evidence"*.

**Where it went.** Gate sequence **`REJECT`** **`REJECT`** `NOTED`. The first rejection got the
verdicts corrected to inconclusive. The second caught that the notebook's own "Verdict & result"
cell still asserted the old FALSIFIED and SUPPORTED statuses, stale against the corrected
hypothesis file and against the analysis cell beneath it. The third review found no CRITICAL or
MAJOR finding but returned `NOTED` rather than `PASS`, noting that only a `Done()`-triggered
gate review can actually close a run. Both hypotheses stand as inconclusive in the study's
record.

---

## Why these two

A needs no physics: higher is better, and the answer was in the run's own spreadsheet. B needs
some contact mechanics but carries the further lesson, and one that travels well past agentic
workflows: ask whether the experiment could have come out any other way.
