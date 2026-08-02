# PLAN.md — the only planning document that is current

**Right now we are in Phase 1: the scale lab.** Nothing in Phase 2 or later gets started
until Phase 1's exit checklist passes. Ideas beyond that are recorded in
`docs/concept/new-direction.md`; file new ones there, do not start them.

---

## The game

Top-down orthographic **social stealth**. You are a contract killer working a compact,
dense, readable neighbourhood. The whole playable level fits on one screen.

The loop, which is the actual load-bearing idea:

> **observe → gain access → manipulate routines → create an opening → act → escape**

`docs/concept/image-ref.png` is the visual target of record. `reference/shitty-hitman-concept.html`
is the prototype that proved the idea was worth chasing — it is the tone reference for
readability and pacing, not for art.

## The lines that hold

- **Roll our own game systems, asset pipeline, editor tooling and level format.
  Do not roll our own engine.** Godot 4, no royalties, no engine fork.
- **This is 3-D viewed from above, not 2-D.** The camera orbits and tilts; dollhouse angles
  are a wanted feature. No asset, shader or system may assume a fixed viewing angle.
- **Voxels are a look, not a simulation.** Destruction is authored and event-based
  (`docs/SCALE.md` has the three tiers). We are not building a destruction engine.
- **Author modularly, place as prefabs.** A house feels like one object in the editor and
  is made of reusable parts underneath. No house is ever a single unique model.
- **The concept image is the source for the blueprint, not the blueprint.** It tells us
  what *categories* of thing the game needs. It is never copied tile for tile.
- **Scale is locked before art is made.** That is what Phase 1 is.

---

## Phase 1 — the scale lab  ← WE ARE HERE

**The question:** does 20 voxels per metre, a 36-voxel character, and an orbiting overhead
orthographic camera produce a level that is legible and appealing at 1920 x 1080?

> Revised 2026-08-02. The original spec's 8 vox/m at 640 x 360 was chosen before anything
> had been rendered. It could not express a hat brim, a collar or a badge — there were no
> voxels to put them in — and its 14-voxel character was half the size of the reference art
> Juno actually wants to make. 20 vox/m makes his 36-row grid art map 1:1.

**What exists already:**

- `docs/SCALE.md` — provisional numbers for everything.
- The Godot project (`game/`) at the real render resolution and camera.
- **`scenes/lab/test_room.tscn` — the scale-lock test scene the brief asks for.** One
  assembled corner of the world at the exact SCALE.md dimensions: a 7 x 9 m house with a
  1.5 m corridor and two rooms, doorway and window openings, a staircase, furniture, the
  full street cross-section, a yard, a car, and an intact/broken wall pair. Real models
  are used where they exist; everything else is a flat box at its exact specified size, so
  the scene works now and sharpens as assets land. Renders with or without its roof, at
  any tilt and yaw.
- `scenes/lab/tile_field.tscn` — one asset laid out as a 12 x 12 m field with a subject on
  it, for judging tiling and single-asset readability.
- `scenes/lab/scale_lab.tscn` — every asset in the manifest as a ghost box at its declared
  size, useful for sanity-checking dimensions before art exists.
- The goxel → glTF pipeline, verified end to end (`docs/PIPELINE.md`).
- 24 asset guide files, one per lab asset, pre-built with brackets and a scale figure.

**What you do:** work `python3 tools/task.py next` until the lab batch is done. Each task
is one object, fully specified, with a starting file. Build it, run `tools/build.py`, look
at it in the lab.

**Exit checklist.** Phase 1 ends when, looking at the lab at 640 x 360:

- [x] A character reads as a person and does not look miniature — at 35 degrees, with body
      depth near 0.22 of height. Confirmed 2026-08-02.
- [ ] Re-confirm character readability at 20 vox/m, on art authored at that density rather
      than resampled up from the old grid.
- [ ] A dining chair is identifiable as a chair.
- [ ] A doorway is obvious without a marker on it.
- [ ] Furniture does not overwhelm a 4 x 5 m room.
- [ ] Individual voxels are still visible — it does not mush into smooth shapes.
- [ ] Uniform colours are distinguishable at character size.
- [x] **The default camera tilt is decided: 35 degrees off straight down** (2026-08-02).
      Measured, not chosen — at the brief's suggested 15 degrees a character is an
      unreadable blob. The camera is *movable* (roughly 20-65 degrees, free yaw), so this
      is a resting angle, not a lock, and assets must read from every side.
- [ ] Assets still read at a low three-quarter "dollhouse" angle, not just at the default.
- [ ] A 48 x 27 m boundary fits on screen and still reads.
- [ ] Walls do not hide the activity behind them.
- [ ] The intact/broken wall swap is convincing.

Then: write the decided numbers into `docs/SCALE.md`, mark it **FROZEN**, and stop
changing them.

**If the checklist fails**, the fix is a number in `docs/SCALE.md` — most likely voxel
density or camera tilt — not a rebuild of the assets. That is the entire reason this
phase exists and why the lab uses ghost boxes.

## Phase 2 — the minimum modular kit

Only after Phase 1 freezes. Ground and street kit, boundary kit, house shell kit, prop
basics, environment basics. Roughly the `kit` batch in `art/assets.json`, which is empty
until Phase 1 is done — populating it is the first Phase 2 job.

Rule that survives from Phase 1: **walls carry colour variants, not new meshes.** One
straight wall mesh, many paint jobs.

## Phase 3 — one tiny complete slice

One house, one front yard, one street section, one side path, one small backyard, one
outbuilding. Then make it *play*: one target, one guard, one civilian, one route, one
alternate route, one distraction, one social access rule, one hide spot, one escape.

This teaches more than half a neighbourhood would.

## Phase 4 — the first whole screen-sized level

48 x 27 m. Central intersection, four lots, a creek strip, side paths. Only two houses
need full interiors; the rest are shells.

## Phase 5 — the first complete contract

The milestone is not "all assets done". It is:

> One house, one yard, one street segment, one target routine, one alternate entrance,
> one distraction, one destructive event, and one escape — all working at the final scale.

---

## Destruction — the decision, so it stops being re-argued

**Authored, selective, event-based.** Three tiers, specified in `docs/SCALE.md`:

1. **Cosmetic** — bottles, lamps, windows. Swap to a broken mesh, a few particles, no
   navigation change.
2. **Gameplay** — doors, fences, furniture, weak walls. Swap to a broken prefab, spawn
   pre-built chunks, update collision, possibly open a route or remove cover.
3. **Set piece** — blow up a room, collapse a garage. Hide the intact structure, reveal
   an authored destroyed one, spawn 20–60 pre-fractured chunks, add smoke and fire,
   update navigation and NPC routines.

Never simulate every voxel as an independent rigid body. Debris may *look* like scattered
voxels; each moving object contains many.

Broken variants are authored **alongside** their intact counterparts, never months later —
which is why `wall_exterior_broken_a` is in the Phase 1 batch.

---

## Where things live

```
docs/SCALE.md            the numbers. everything obeys this.
docs/PIPELINE.md         goxel -> glTF -> Godot, exact commands
docs/PLAN.md             this file
docs/concept/            the source brief and the reference mockup
reference/               the original prototype, kept as tone reference
art/assets.json          every asset, its size, its brief. source of truth.
art/palette.json         32 colours, the whole game
art/templates/           generated goxel starting files, one per asset
art/src/                 your authored .vox files
tools/                   the pipeline
game/                    the Godot project
```
