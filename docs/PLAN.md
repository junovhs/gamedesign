# PLAN.md — the only planning document that is current

**Right now we are in Phase 1: the scale lab.** Nothing in Phase 2 or later gets started
until Phase 1's exit checklist passes. Ideas beyond that are recorded in
`docs/concept/new-direction.md`; file new ones there, do not start them.

---

## The game

Top-down **social stealth** in 2-D pixel art. You are a contract killer working a compact,
dense, readable neighbourhood.

The loop, which is the actual load-bearing idea:

> **observe → gain access → manipulate routines → create an opening → act → escape**

`docs/concept/image-ref.png` is the visual target of record.
`reference/shitty-hitman-concept.html` is the prototype that proved the idea was worth
chasing — it is the tone reference for readability and pacing, not for art.

## The lines that hold

- **Roll our own game systems, asset pipeline, editor tooling and level format.
  Do not roll our own engine.** Godot 4, no royalties, no engine fork.
- **This is 2-D at a fixed three-quarter top-down view.** The camera does not orbit or
  tilt; it zooms at 2x, 3x or 4x and nothing else.
- **A generation is reference, never a shipped asset.** Every pixel that ships is authored
  in our own sprite editor. Goxel and Aseprite are retired.
- **Every sprite ships on an explicit palette.** 16 colours per character by default.
- **Author modularly, place as prefabs.** A house feels like one object in the editor and
  is made of reusable parts underneath.
- **The concept image is the source for the blueprint, not the blueprint.**
- **Scale is locked before art is made.** That is what Phase 1 is.

---

## Phase 1 — the scale lab  ← WE ARE HERE

**The question:** does a 32 x 64 character on a 32 px / 1 m tile grid, viewed at 3x on a
640 x 360 native canvas, produce a level that is legible and appealing at 1920 x 1080?

> Revised 2026-08-02. The previous spec was voxel-based — 20 voxels per metre, a 36-voxel
> character, an orbiting 3-D camera. It is retired (DEC-02). The pixel direction exists
> because Juno found an authoring route he will actually use: generate a reference, then
> make it real pixel art in our own editor.

**What has to exist before the question can be answered:**

- The sprite editor, good enough to author a full character — palette, facings, frames,
  guides, export. That is the current issue queue (`ishoo plan show`).
- One complete character: three facings, a walk cycle, on the section 3 landmarks.
- A tiled ground plane, a wall, a doorway and a couple of props at SCALE.md dimensions.
- The Godot viewport on the pixel camera at all three zoom steps.

**Exit checklist.** Phase 1 ends when, looking at the lab at 3x:

- [x] **The character cell is decided: 32 x 64, 58 px standing height** (2026-08-02).
      Measured against the first authored character, not chosen.
- [x] **The resting zoom is decided: 3x** (2026-08-02). Measured — 4x shows one room, 2x
      stops reading as pixel art.
- [ ] A character reads as a person at 3x and does not look miniature.
- [ ] Two characters in different roles are distinguishable at a glance, by silhouette and
      colour alone, with no marker on them.
- [ ] A character's three facings match on the eye line, shoulder line and ground line.
- [ ] A walk cycle reads as walking and does not shimmer.
- [ ] A doorway is obvious without a marker on it.
- [ ] Furniture does not overwhelm a 4 x 5 m room.
- [ ] A repeating ground tile does not stamp a visible grid across a 12 x 12 m field.
- [ ] Individual pixels are still visible — it does not mush into smooth shapes.
- [ ] Walls do not hide the activity behind them.
- [ ] **Open: how much of a level fits on one screen, and does the camera scroll?** 3x shows
      20 x 11 m. A number goes in SCALE.md § 7 only once this is answered by looking.

Then: write the decided numbers into `docs/SCALE.md`, mark it **FROZEN**, and stop
changing them.

**If the checklist fails**, the fix is a number in `docs/SCALE.md` — most likely the zoom
step or the character cell — not a rebuild of the assets. That is the entire reason this
phase exists.

## Phase 2 — the minimum modular kit

Only after Phase 1 freezes. Ground and street tiles, boundary kit, house shell kit, prop
basics, environment basics.

Rule that survives from Phase 1: **walls carry colour variants, not new art.**

## Phase 3 — one tiny complete slice

One house, one front yard, one street section, one side path, one small backyard, one
outbuilding. Then make it *play*: one target, one guard, one civilian, one route, one
alternate route, one distraction, one social access rule, one hide spot, one escape.

This teaches more than half a neighbourhood would.

## Phase 4 — the first whole screen-sized level

Central intersection, several lots, a creek strip, side paths. Only two houses need full
interiors; the rest are shells. Its footprint depends on the open question in Phase 1.

## Phase 5 — the first complete contract

The milestone is not "all assets done". It is:

> One house, one yard, one street segment, one target routine, one alternate entrance,
> one distraction, one destructive event, and one escape — all working at the final scale.

---

## Where things live

```
docs/SCALE.md            the numbers. everything obeys this.
docs/PLAN.md             this file
docs/concept/            the source brief and the reference mockup
reference/               the original prototype, kept as tone reference
tools/show.py            put a picture on Juno's screen
game/                    the Godot project
```

The issue store holds the rest: `ishoo status` for the governing decisions,
`ishoo plan show` for what is actually next.
