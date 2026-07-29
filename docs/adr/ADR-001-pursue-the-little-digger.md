# ADR-001 — The Little Digger is the project

**Status:** ACCEPTED — 2026-07-29
**Tags:** direction, scope

## Problem

This repository holds several unrelated prototypes (`old/downshaft.html`, `deep.html`,
`pov.html`, `old/caving.html`, `packhouse.html`). Effort was spread across ideas with no
committed direction, and each new prototype restarted the question of what we are building.

## Decision

The Little Digger is the project. Other prototypes in this repository are archived
references, not candidates. New work goes to The Little Digger unless an ADR supersedes
this one.

## Rule

Prototypes in `old/` and the loose `*.html` experiments are read-only history. Do not extend
them. Do not port their systems in without an explicit decision.

## Alternatives rejected

- **Keep exploring in parallel.** Rejected: the first playable test of The Little Digger
  produced a clear "this is the most promising thing so far," and parallel exploration is
  what has kept every idea shallow.
- **Restart in an engine before committing.** Rejected: the browser prototype answered the
  design questions faster than an engine port would have. See ADR-005.

## Consequences

- One direction to fund with attention; everything else is on ice.
- The handoff document `little-digger-handoff.md` remains the design brief of record, and
  `docs/direction.md` is its living update.

## Operational impact

`index.html` at the repository root is The Little Digger, published to GitHub Pages. The
previous root page (DOWNSHAFT) now lives at `old/downshaft.html`.
