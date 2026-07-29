# THE LITTLE DIGGER — DOCS

Play it: <https://junovhs.github.io/gamedesign/> · source: [`../index.html`](../index.html)

Start here: **[direction.md](direction.md)** — where the project is, what it is trying to be,
and the open questions in priority order.

---

## Decisions (ADRs)

Locked unless superseded. A PROPOSED ADR is not binding and must not be built on.

| ADR | Title | Status |
|---|---|---|
| [001](adr/ADR-001-pursue-the-little-digger.md) | The Little Digger is the project | ACCEPTED |
| [002](adr/ADR-002-three-minutes-and-five-hundred-hours.md) | Three minutes to pick up, five hundred hours deep | ACCEPTED |
| [003](adr/ADR-003-the-dig-is-the-signal.md) | The dig is the signal, and the creature's voice is the interface | ACCEPTED |
| [004](adr/ADR-004-placeholder-vocabulary-must-not-ship.md) | The placeholder voice must not ship | ACCEPTED |
| [005](adr/ADR-005-prototype-is-an-instrument.md) | The browser prototype is a design instrument, not the codebase | ACCEPTED |
| [006](adr/ADR-006-volumetric-art-direction.md) | Art direction moves toward volume (voxel or clay) | **PROPOSED** |

## Plans

Each plan is one question, broken into issues with scope contracts.

| Plan | The question | First issue |
|---|---|---|
| [hands](plans/hands.md) | How does a thumb steer under a lifted camera? | HAND-1 — spike tap-to-go |
| [dig-depth](plans/dig-depth.md) | What makes digging a craft? | DIG-1 — give the calls more to say |
| [look](plans/look.md) | Voxel, clay, or lit boxes? | LOOK-1 — put a sun in the current renderer |
| [world](plans/world.md) | Authored or generated? | WORLD-1 — name the split |
| [progress](plans/progress.md) | What does the player keep? | PROG-1 — the first ability |
| [voice](plans/voice.md) | What does the creature sound like, legally ours? | VOICE-1 — design the call |

## Suggested order

1. **LOOK-1** — a day of work that may answer the whole art question, or reframe it.
2. **HAND-1** — controls are underneath everything else; tune nothing until they settle.
3. **DIG-1 / DIG-2** — depth in the verb, which is where the 500 hours has to come from.
4. **LOOK-2 / LOOK-3 → LOOK-5** — the spikes, then the engine decision.
5. Everything else follows the engine decision.

## Background

- [../little-digger-handoff.md](../little-digger-handoff.md) — the original build brief.
- [../pivot-concept.md](../pivot-concept.md) — the concept document.
- [../spencer_game_design_philosophy.md](../spencer_game_design_philosophy.md)

## Porting these into Ishoo

This repository has Ishoo wired up but no store (`.ishoo/` holds only a cache). Run
`ishoo enable` (or `ishoo init`) in the repository root and these plans and ADRs can be
imported as real issues and decisions — they are written in Ishoo's Scope Contract shape
(concrete change / main surface / proof of done / out of scope / depends on) so the import is
mechanical.
