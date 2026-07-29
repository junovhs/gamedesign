# ADR-006 — Art direction moves toward volume (voxel or clay)

**Status:** PROPOSED — 2026-07-29 (do not treat as binding)
**Tags:** art, tech

## Problem

The prototype's look is placeholder and reads flat. The stated instinct after the first test
is to pursue "some sort of voxel or clay 3-D vibe." Before that becomes binding, two things
need to be true: we need to know what specifically is flat about the current look, and we
need to know what a volumetric look costs.

For the record, and contrary to first impression, the prototype is **not** drawing 2-D planes
in a 3-D world — every object is a real six-faced box. See `docs/direction.md` §3. What reads
as flat is the absence of a light model, the absence of texture, a box-only vocabulary, and
a painter's algorithm with no depth buffer.

## Decision (proposed)

Pursue a volumetric look — chunky forms with real light on them, in the direction of voxel or
sculpted clay — and treat "flat-shaded low-poly" as the thing we are leaving behind, not the
destination.

## Rule (proposed)

Every area must survive the map test: a painted still of it from an unusual angle, at an
unusual time of day, must be recognisable. Art direction is load-bearing for the map system,
so any style that cannot produce a legible silhouette and colour identity is disqualified
regardless of how good it looks in motion.

## Alternatives to weigh in the spike

- **Voxel proper** — everything on a grid, destructible/diggable geometry for free, strong
  identity, heavy tooling cost, risks looking like every other voxel game.
- **Clay / sculpted** — soft bevelled forms, hand-modelled, warm and distinctive, expensive
  per asset, weak fit for procedural generation.
- **Keep chunky boxes, add a real light model** — cheapest path by far, and it may get 80% of
  the perceived quality; genuinely untested.

## Consequences if accepted

- Chooses the engine (see ADR-005), because a depth buffer and a real light model are the
  first requirements.
- Sets the terrain representation, which in turn constrains digging (`plans/dig-depth.md`)
  and world generation (`plans/world.md`).

## Status note

This ADR stays PROPOSED until `plans/look.md` reports. Do not build on it yet.
