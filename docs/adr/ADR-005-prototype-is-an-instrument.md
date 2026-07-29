# ADR-005 — The browser prototype is a design instrument, not the codebase

**Status:** ACCEPTED — 2026-07-29
**Tags:** tech, process

## Problem

The browser prototype is now good enough to be tempting as a foundation: it runs on a phone,
it deploys in one push, and it answered four design questions in a day. It is also a
dependency-free software renderer with a painter's algorithm and no depth buffer, which is a
poor foundation for the game described in the brief.

## Decision

The browser build is a **design instrument**. Its job is to answer questions about feel as
fast as possible, and it is allowed to be thrown away. No effort is spent making it
architecturally sound, and no design decision is constrained by what is easy in it.

The shipping engine is **not yet chosen**. Godot 4 remains the working assumption from the
brief, and the decision is deferred until the art-direction spike (`plans/look.md`) has run,
because the renderer requirements are what should choose the engine.

## Rule

- Keep the prototype a single file with no dependencies, so it stays instantly deployable and
  instantly disposable.
- Do not refactor it toward being "the real thing." If a change only makes sense for a
  shipping codebase, it belongs in the shipping codebase, which does not exist yet.
- Every question the prototype answers gets written down in `docs/`, because the code will
  not survive to carry the answer.

## Alternatives rejected

- **Commit to the web build as the product.** Rejected: the painter's algorithm caps scene
  complexity, and the brief calls for a dense world with a serious art direction.
- **Stop prototyping and port to an engine now.** Rejected: iteration speed is the reason
  this project moved at all, and the open questions are still about feel, not about tech.

## Consequences

- Expect to rewrite. Budget for it. The value is in the answers, not the file.
- The engine decision gets its own ADR once `plans/look.md` reports.

## Operational impact

`index.html`, one file, no build step, published on push to `main`.
