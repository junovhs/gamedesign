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
- **Voxels are a look, not a simulation.** Destruction is authored and event-based
  (`docs/SCALE.md` has the three tiers). We are not building a destruction engine.
- **Author modularly, place as prefabs.** A house feels like one object in the editor and
  is made of reusable parts underneath. No house is ever a single unique model.
- **The concept image is the source for the blueprint, not the blueprint.** It tells us
  what *categories* of thing the game needs. It is never copied tile for tile.
- **Scale is locked before art is made.** That is what Phase 1 is.

---

## Phase 1 — the scale lab  ← WE ARE HERE

**The question:** does 8 voxels per metre, a 14-voxel character, and a near-overhead
orthographic camera produce a level that is legible and appealing at 640 x 360?

**What exists already:**

- `docs/SCALE.md` — provisional numbers for everything.
- The Godot project (`game/`) at the real render resolution and camera.
- The scale lab scene, which draws a **ghost box at the declared size for every asset in
  the manifest**, with a 1.75 m reference figure at each station. So the lab is useful
  *before any art exists* — you can already walk the board and judge whether the sizes
  are sane.
- The goxel → glTF pipeline, verified end to end (`docs/PIPELINE.md`).
- 24 asset guide files, one per lab asset, pre-built with brackets and a scale figure.

**What you do:** work `python3 tools/task.py next` until the lab batch is done. Each task
is one object, fully specified, with a starting file. Build it, run `tools/build.py`, look
at it in the lab.

**Exit checklist.** Phase 1 ends when, looking at the lab at 640 x 360:

- [ ] A character reads as a person and does not look miniature.
- [ ] A dining chair is identifiable as a chair.
- [ ] A doorway is obvious without a marker on it.
- [ ] Furniture does not overwhelm a 4 x 5 m room.
- [ ] Individual voxels are still visible — it does not mush into smooth shapes.
- [ ] Uniform colours are distinguishable at character size.
- [ ] The camera tilt is decided (sweep it with `[` and `]`).
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
