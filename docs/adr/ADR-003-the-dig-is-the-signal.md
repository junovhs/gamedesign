# ADR-003 — The dig is the signal, and the creature's voice is the interface

**Status:** ACCEPTED — 2026-07-29
**Tags:** design, core-loop

## Problem

The first build communicated proximity continuously through the creature's ears and posture.
In play, that read as noise: the player wandered a vague region and dug at random, and a miss
taught them nothing. The game had no hot-and-cold loop, which is the entire verb of the
reference (Chocobo Hot and Cold).

## Decision

**Digging is the only channel that carries distance information.** Every dig ends with the
creature calling out, graded by how close the hole was to the nearest buried thing. A miss is
a measurement, not a shrug. Two or three digs triangulate.

**No number, bar, arrow, meter, or minimap ever expresses proximity.** The creature's voice
and body are the interface, and they are the only interface.

## Rule

- Any new information the player needs about what is underground must arrive as a creature
  behaviour or a creature sound, produced by an action the player took.
- Continuous passive proximity feedback stays *below* the dig in loudness, always. It sets
  mood; it does not answer "how close am I."
- The graded scale must remain readable in one play session with nothing explained.

## Alternatives rejected

- **A proximity meter or heat bar.** Rejected: violates pillar 1 and 4 of the brief, and it
  removes the skill gap between wandering and triangulating.
- **Continuous audio pitch tied to distance (hot/cold beeping).** Rejected: it makes digging
  a formality and turns the game into a stick-waving exercise.
- **Marking dug holes by grade on the ground.** Rejected for now: remembering your own
  measurements *is* the skill. Revisit only if playtests show it is unfun rather than hard.

## Consequences

- The dig must be fast enough to be a probe, not a commitment (currently ~1.15s, faster as
  the creature improves) — this interacts directly with ADR-002.
- Time is the only resource the hunt spends, so dig cost is the difficulty dial.
- The call vocabulary is a legal question, not a design one. See ADR-004.

## Operational impact

`gradeOf()` in `index.html` is the single function controlling the entire difficulty curve.
All of `docs/plans/dig-depth.md` builds on this decision.
