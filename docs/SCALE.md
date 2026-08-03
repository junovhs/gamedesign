# SCALE.md — the numbers everything else obeys

**Status: PROVISIONAL (v0.2).** These numbers are locked *for the duration of the scale lab*.
When the scale lab passes its checklist (see `docs/PLAN.md` → Phase 1), this file is marked
FROZEN and stops changing. Until then, change numbers here and nowhere else.

If a number is not in this file, it is not a rule. If a number is in this file, no asset,
scene, or script may contradict it.

> **v0.2 replaced voxels with pixels** (2026-08-02, DEC-02 / DEC-07). The metre dimensions
> in sections 6–8 survived the change unaltered — they were always real-world measurements,
> and the whole point of pinning the tile at exactly 1 m is that they keep working.

---

## 1. Unit system

| Thing | Value |
|---|---|
| Art pixel | **1/32 m** |
| Tile | **32 x 32 px = 1 x 1 m** |
| Character cell | **32 x 64 px** |
| Structural grid (walls, floors, rooms) | 1 tile |
| Fine prop placement grid | 8 px = 0.25 m |
| Architecture rotation | 90° only |

**One tile is one metre is 32 pixels.** That equality is the reason every dimension below
can be stated in metres and still land on whole tiles.

**Pixels are visual only.** Navigation, interaction radii, sound, and all gameplay logic
work in metres. Never write a rule in pixels.

## 2. Render target and camera

```
Native canvas (resting)      640 x 360, scaled 3x to 1920 x 1080
Filtering                    nearest, always
Projection                   2-D top-down three-quarter
Zoom steps                   2x, 3x, 4x  — integer only, no other value
Default zoom                 3x                                DECIDED 2026-08-02
```

| Zoom | Native canvas | Art px on screen | Character height | World on screen |
|---|---|---|---|---|
| 2x — survey | 960 x 540 | 2 px | 116 px | **30 x 17 m** |
| **3x — resting** | **640 x 360** | **3 px** | **174 px** | **20 x 11 m** |
| 4x — close | 480 x 270 | 4 px | 232 px | **15 x 8 m** |

> **3x was measured, not chosen.** 4x gives the chunkiest pixel — the same chunk as
> Stardew's 16x32 characters — but shows about 15 x 8 m, roughly one room and a doorway.
> A game whose loop is *observe → find the opening* cannot be played through a keyhole.
> 2x shows a whole neighbourhood, but at 2 screen pixels per art pixel the art stops
> reading as pixel art. 3x keeps a house and its yard on screen with the chunk still there.

> **A 32x64 character stays readable at every step.** What carries it is contrast and
> silhouette, not pixel size. Chunk at 4x is a taste win, not a legibility one — so zoom is
> free to serve the gameplay rather than the look.

**No non-integer scale ever reaches the screen.** Not for zoom, not for camera easing, not
for a transition. A half-pixel is a bug.

## 3. The character cell

A character is authored on a **32 x 64 px cell**. The figure stands on the cell's ground
line and does not float.

| Landmark | Row | Metres |
|---|---:|---:|
| Hat / hair headroom | 0–5 | — |
| Top of a bare head | 6 | 1.81 |
| Eye line | 10 | 1.68 |
| Bottom of head mass | 22 | 1.30 |
| Shoulder line | 24 | 1.23 |
| Widest point of body | 28 px wide | 0.88 wide |
| Hip / leg split | 47 | 0.50 |
| **Ground line (feet)** | **63** | **0.00** |
| Standing height, bare head | **58 px** | **1.81** |

Every character in the cast shares this eye line, shoulder line and ground line. That
shared skeleton is what makes a crowd read as one game rather than a pile of sprites.

> **Measured, not invented.** These come from the first suit character authored at 32x64.
> That sprite currently stands 63 px — a 1.97 m man — and wants nudging down to 58.

**Deliberately chunky.** The head is roughly a quarter of total height and the body is
wider than a real person's. This is the reference look, not an error to be corrected.
Identity comes from **silhouette, colour and accessories** — hats, hair, collars, uniforms
— never from finer facial detail.

## 4. Facings and frames

| | |
|---|---|
| Authored facings | **down, side, up** |
| Fourth facing | side, mirrored |
| Minimum walk cycle | 6 frames per facing |
| Idle | 2 frames, or 1 if it reads |

**Every character is authored as one document holding all its facings**, sharing one palette
and the section 3 landmarks. Facings authored separately do not match, and a cast that does
not match is the most visible possible failure.

Diagonal facings are not authored. The camera does not orbit — this is 2-D.

## 5. Colour

| | |
|---|---|
| Palette per character | **16 colours** |
| Alpha | **binary** — a pixel is opaque or absent |

16 is the default *per character*, not a cap on the game. Different characters may hold
different palettes; each one is explicit, stored beside its sprite, and editable.

**No sprite with unconstrained colour enters the game.** Every sprite leaves the editor
snapped to its palette. That is what makes role recolours — guard, caterer, guest, staff —
a palette swap rather than new art, and what stops animation shimmering from frame-to-frame
colour drift.

Editing a palette slot restyles every pixel using it. Global colour changes are therefore
cheap, and that is deliberate: the look is expected to be tuned late.

## 6. Architecture

| Element | Metres | Tiles |
|---|---:|---:|
| Exterior wall thickness | 0.25 | ¼ |
| Interior wall thickness | 0.125 | ⅛ |
| Wall height | 2.75 | — |
| Standard doorway opening | 1.0 x 2.0 | 1 wide |
| Standard window opening | 1.0–1.5 | 1–1½ wide |
| Window sill height | 0.875 | — |
| Minimum corridor | 1.5 | 1½ |
| Comfortable corridor | 2.0 | 2 |
| Stair width | 1.0–1.5 | 1–1½ |

Room sizes:

| Room | Metres / tiles |
|---|---|
| Small | 3 x 3 |
| Standard | 4 x 5 |
| Large | 5 x 6 |

Nothing below 3 x 3 m except closets, toilets and utility spaces — NPC routines need room
to pass furniture without navigation fights.

> **Doorway modules are 2 m wide, not 1 m.** A 1 m module with a 1 m opening is not a wall.

## 7. Residential lot and street

| Element | Metres |
|---|---|
| Small house footprint | 7 x 9 |
| Medium house footprint | 8 x 10 |
| Lot width | 10–12 |
| Lot depth | 10–14 |
| Front setback | 2.5–4 |
| Side passage | 1.5–2 |
| Backyard depth | 3–5 |
| Garage | 4 x 6 |
| Shed | 2 x 3 |
| Vehicle lane | 3 |
| Two-lane road | 6 |
| Sidewalk | 1.5 |
| Curb height / width | 0.25 |
| Grass verge | 1–1.5 |
| Driveway | 3–3.5 |
| Crosswalk depth | 2–3 |
| Creek | 4–6 wide |
| Pedestrian bridge | 1.5–2 wide |

Canonical residential cross-section (building face to building face = **15.5 m**):

```
3.0 front yard | 1.5 sidewalk | 0.25 curb | 6.0 road | 0.25 curb | 1.5 sidewalk | 3.0 front yard
```

## 8. Reference prop dimensions

| Prop | Metres (X x Y x Z) |
|---|---|
| Dining chair | 0.5 x 0.5 x 0.9 |
| Dining table | 1 x 1.5 x 0.75 |
| Single bed | 1 x 2 x 0.65 |
| Double bed | 1.5 x 2 x 0.65 |
| Sofa (2-seat) | 2 x 0.9 x 0.9 |
| Kitchen counter (1 m) | 1 x 0.65 x 0.9 |
| Wardrobe | 1 x 0.65 x 2 |
| Trash bin | 0.5 x 0.5 x 0.9 |
| Mailbox | 0.4 x 0.5 x 1 |
| Sedan | 1.75 x 4 x 1.5 |
| Service van | 2 x 5 x 2.25 |

A sprite need not fill its cell, but its **declared footprint must match** the dimensions
above, because that footprint is what navigation and collision use.

## 9. Detail

**Detail is a budget you spend selectively, not an obligation.** 32 px per metre exists so
detail is *available* where it earns its place — a hat brim, a badge, a collar — while
everything else stays deliberately blocky.

- Anything **gameplay-relevant** reads by silhouette and colour first, detail second.
- Spend detail on: faces, hats, uniforms and insignia, anything the player must identify at
  a glance to make a decision.
- Keep blocky: walls, floors, ground, hedges, plain furniture, bulk architecture.
- Do **not** cover surfaces in single-pixel noise. It becomes static, just finer static.
- **Never put distinguishing detail inside a repeating ground tile.** Measured 2026-08-02 at
  the old density: four dark cells in a repeating grass tile stamped a plainly visible 1 m
  grid across a 12 x 12 m field, and random rotation did not break it up. A repeated tile
  can only carry flat colour. Ground variety comes from **2–3 whole-tile variants placed
  randomly**, plus scattered detail props — never from detail within the repeating unit.

## 10. Destruction

**Authored, selective, event-based. Three tiers.** This is settled; do not reopen it.

1. **Cosmetic** — bottles, lamps, windows. Swap to a broken sprite, a few particles, no
   navigation change.
2. **Gameplay** — doors, fences, furniture, weak walls. Swap to a broken prefab, spawn
   pre-built debris, update collision, possibly open a route or remove cover.
3. **Set piece** — blow up a room, collapse a garage. Hide the intact structure, reveal an
   authored destroyed one, spawn pre-made debris, add smoke and fire, update navigation and
   NPC routines.

Never simulate debris as independent per-pixel bodies. Broken variants are authored
**alongside** their intact counterparts, never months later.
