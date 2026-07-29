# PLAN: dig-depth — make digging worth hundreds of hours

**Question:** what turns "walk, press, read the call" into a craft?

Digging currently has one decision in it: where to put the next hole. That is enough to be
fun for an hour and not enough for ADR-002's evening test. Everything here must preserve
ADR-003: the dig is the signal, and no meters.

---

## DIG-1 — Give the calls more to say

**Urgency:** important.

- **Concrete change:** extend the response beyond distance alone. Candidates, to test one at
  a time: the call hints at *depth* as well as distance; a different colour of call for a
  different kind of thing underground; a call that reacts to how many things are near, not
  just the nearest one.
- **Main surface:** `gradeOf()` and `cry()` in `index.html`.
- **Proof of done:** a player who has learned the extra dimension is measurably faster than
  one who has not, and neither was told about it.
- **Out of scope:** any UI. Any explanation.
- **Governed by:** ADR-003.

## DIG-2 — Depth: dig down, not just around

- **Concrete change:** buried things sit at a depth as well as a position. A dig goes one
  layer down; continuing costs more time. The call distinguishes "beside you" from "beneath
  you."
- **Main surface:** hole state, dig resolution, the call grading.
- **Proof of done:** a hunt where the correct play is sometimes to keep digging the same hole
  and sometimes to abandon it, and good players know which.
- **Out of scope:** terrain deformation (that is `look.md` / the engine decision).
- **Why:** it adds a second axis to every measurement without adding a single UI element.

## DIG-3 — Things that resist being dug up

- **Concrete change:** some finds do not simply pop out — roots, stone, something that pulls
  back, something that needs two goes. The creature's animation and call carry the struggle.
- **Main surface:** dig resolution.
- **Proof of done:** at least three distinct "this one is a fight" moments that a player can
  recognise before committing.
- **Out of scope:** tools (that is `progress.md`).

## DIG-4 — Ground that changes the problem

- **Concrete change:** the surface underfoot changes the dig — soft ground is fast, stony
  ground is slow and muffles the call, wet ground collapses holes over time.
- **Main surface:** terrain sampling at the dig point.
- **Proof of done:** a player routes around bad ground without being told it is bad.
- **Out of scope:** biome art.
- **Note:** this is the "variation by place, not by rules" principle from the brief, applied
  to the verb instead of the scenery.

## DIG-5 — The hunt as a route problem

- **Concrete change:** tune time, dig cost, and area size until the interesting question is
  "which three holes do I have time for," not "how fast can I dig ten."
- **Main surface:** hunt constants.
- **Proof of done:** hunt #50 with rewards switched off is still interesting. (The brief's own
  test, still unrun.)
- **Out of scope:** rewards, which are exactly what this test disables.
- **Depends on:** DIG-1, DIG-2.

## DIG-6 — Prove the skill gap exists

- **Concrete change:** instrument the prototype to log dig positions and times, then compare
  a first session to a tenth.
- **Main surface:** a debug log, off by default.
- **Proof of done:** measurable improvement in digs-per-find across sessions, with no tutorial
  and no explanation given.
- **Out of scope:** analytics in any shipped build.
- **Why:** the brief asserts a skill gap between wandering and triangulating. If it is not
  measurable, it is not there, and 500 hours is not there either.
