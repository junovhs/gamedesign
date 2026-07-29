# ADR-004 — The placeholder voice must not ship

**Status:** ACCEPTED — 2026-07-29
**Tags:** legal, audio, direction

## Problem

The prototype's graded dig response uses "kweh," which is the Chocobo call from Final
Fantasy. It works perfectly as a testing vocabulary — it is instantly legible and it proves
the mechanic — and it is not ours.

## Decision

"Kweh" is a **testing placeholder only.** It may live in prototypes and internal builds. It
must not appear in any public build, store page, trailer, screenshot, or marketing material.
The creature gets its own call before anything ships.

## Rule

- Any build shared outside the team must use the original call vocabulary.
- The same rule applies to the creature's silhouette, the colour-progression conceit, and any
  other element carried over from the reference for testing: translate the *mechanism*, never
  the surface.
- Track every placeholder that is knowingly borrowed in `docs/plans/voice.md`, so the list of
  things to replace is never held only in someone's head.

## Alternatives rejected

- **Replace it immediately.** Rejected for now: the placeholder is doing real work — it is
  legible enough that playtesters read the mechanic instantly, which is exactly what a
  prototype needs. Replacing it before the mechanic is settled would test the wrong thing.
- **Assume a short, generic bird call is safe.** Rejected as an assumption to rely on
  silently: the replacement is a design task with a real brief (see `plans/voice.md`), not a
  find-and-replace.

## Consequences

- A public release is gated on the voice work. This is now a tracked dependency, not a
  surprise at the end.
- Any accidental public build is a problem to fix immediately, not to argue about.

## Operational impact

`index.html` is published to GitHub Pages, which is technically public. It is a development
build with no marketing around it, and the placeholder is acceptable there for now; it must
be replaced before the game is presented as a product anywhere.
