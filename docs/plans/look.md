# PLAN: look — voxel, clay, or lit boxes

**Question:** what does this game actually look like, and what does that cost?

Governed by the proposed ADR-006, which stays PROPOSED until this plan reports. Read
`docs/direction.md` §3 first — the prototype is already volumetric geometry; what is missing
is light, texture, form vocabulary, and a depth buffer.

---

## LOOK-1 — Cheapest experiment first: put a sun in the current renderer

**Urgency:** urgent — it is a day of work and it may change what the other options are worth.

- **Concrete change:** add a directional light with a real normal-based term, cheap ambient
  occlusion in the corners where boxes meet, and a warm/cool split between lit and shadowed
  faces. Same geometry, same file.
- **Main surface:** `box()` shading and the ground shading in `index.html`.
- **Proof of done:** a side-by-side screenshot pair, before and after, judged on the phone.
- **Out of scope:** shadows cast between objects (the painter's algorithm cannot).
- **Why:** if flat shading is the whole problem, this answers the art direction for a day of
  work instead of a month.

## LOOK-2 — Spike: voxel

- **Concrete change:** rebuild one landmark and a patch of ground as true voxels in an engine
  with a depth buffer, with diggable terrain.
- **Main surface:** a throwaway project outside this repository.
- **Proof of done:** the crooked tree and one hunt area, in voxels, on a phone, at frame rate,
  with a hole the player dug still visible in the ground.
- **Out of scope:** tooling, editors, pipelines. This is a look, not a workflow.

## LOOK-3 — Spike: clay

- **Concrete change:** the same landmark and ground patch, in soft sculpted forms with
  bevelled edges and a warm light model.
- **Main surface:** a throwaway project.
- **Proof of done:** same comparison shots, same phone, same frame rate target.
- **Out of scope:** procedural generation of clay forms — assume hand-made for the spike.
- **Note:** the risk to name honestly is that clay is beautiful and hostile to procedural
  generation, which `world.md` may need.

## LOOK-4 — The map test on every candidate

- **Concrete change:** render the map picture (posterised still from a second camera) in each
  candidate style and check it is still recognisable.
- **Main surface:** the map generator, ported to each spike.
- **Proof of done:** a person who has seen the area can name the location from the picture in
  each style. A style that fails this is disqualified, however good it looks.
- **Depends on:** LOOK-1, LOOK-2, LOOK-3.
- **Why:** the map system is the difference between a 25-hour game and a 500-hour one, and it
  is entirely dependent on art direction being legible.

## LOOK-5 — Decide, and write the engine ADR

- **Concrete change:** accept or reject ADR-006, then write the engine decision it implies.
- **Proof of done:** two ADRs — art direction ACCEPTED or superseded, and an engine ADR.
- **Depends on:** LOOK-4.
