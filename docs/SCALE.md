# SCALE.md — the numbers everything else obeys

**Status: PROVISIONAL (v0.1).** These numbers are locked *for the duration of the scale lab*.
When the scale lab passes its checklist (see `docs/PLAN.md` → Phase 1), this file is marked
FROZEN and stops changing. Until then, change numbers here and nowhere else.

If a number is not in this file, it is not a rule. If a number is in this file, no asset,
scene, or script may contradict it.

---

## 1. Unit system

| Thing | Value |
|---|---|
| Godot world unit | **1 unit = 1 metre** |
| Art voxel | **0.05 m** |
| Voxel density | **20 voxels per metre** |
| Structural grid (walls, floors, rooms) | 0.5 m = 10 vox |
| Architecture module increments | 1 m = 20 vox |
| Fine prop placement grid | 0.25 m = 5 vox |
| Vertical elevation increments | 0.25 m = 5 vox |
| Architecture rotation | 90° only |
| Loose-prop rotation | 45° allowed |

An object 20 voxels long is exactly 1 metre in game.

> **20 was chosen to match the artist's grid.** Juno's reference characters are 36 rows
> tall (2026-08-02); at 20 vox/m that is exactly 1.8 m, so pixel-grid art maps to voxels
> 1:1 with no re-derivation. 16 and 24 vox/m were both checked: 16 gives only a 28-voxel
> character, and 24 cannot express 1.8 m in whole voxels. The one casualty is the old
> 0.125 m interior wall, which becomes 0.15 m (3 voxels).

**Voxels are visual only.** Navigation, interaction radii, sound, and all gameplay logic
work in metres. Never write a rule in voxels.

## 2. Render target and camera

```
Internal render resolution   1920 x 1080  (native; no pixel-art downsample)
Anti-aliasing                MSAA 4x
Projection                   orthographic
Default camera pitch         -55deg  (35deg off straight down)   DECIDED 2026-08-02
Pitch range                  -70deg .. -25deg  (20deg .. 65deg off straight down)
Yaw                          free; snaps to 90deg steps for level authoring
Roll                         0, always
Default orthographic size    18 (= 32 m of screen width)
Zoom range                   12 .. 27 (21 m .. 48 m of screen width)
Near / far                   0.05 / 200
```

**The camera moves.** This is a 3-D game viewed from above, not a 2-D game. The player can
orbit and tilt — dollhouse angles are expected, and looking into a house from a low,
three-quarter angle is a thing we want. 35° is the *default resting* angle, not a lock.

> **35° as the default was measured, not chosen.** The source brief recommended 12-15° off
> straight overhead. Rendering the first real character through the actual camera showed
> that at 15° a 1.75 m person is the top of a head and nothing else — unreadable. A body
> resolves from about 25° and reads clearly at 35°.
>
> The cost is occlusion, and it grows as the camera drops: **cutaway roofs and wall-hiding
> are load-bearing systems, not polish.**

### What a movable camera means for authoring

- **Every asset must read from all four sides and from above.** There is no "back you never
  see". Backs may be simpler than fronts, but they may not be unfinished.
- Author with the asset's front facing goxel **-Y** so orientation is consistent, but do not
  treat the other five faces as throwaway.
- **Nothing may depend on a single viewing angle** — no painted-on fake perspective, no
  detail that only lines up at 35°.
- Judge assets at the default 35° *and* at a low three-quarter angle before accepting them.
  `tools/` renders any tilt; use it.

Derived **at the default camera** (1920 x 1080, orthographic size 18, 55° below horizontal).
These shift as the camera zooms and tilts, so treat them as the resting case:

| | |
|---|---|
| Visible ground area | **32 m wide x 22 m deep** |
| 1 m horizontally (screen X) | **60 px** |
| 1 m of *height* (vertical faces) | **34 px** — foreshortened by cos 55° |
| 1 m of ground *depth* | **49 px** — foreshortened by sin 55° |
| A 1.8 m character | **62 px** of body height, plus the head top |
| 1 art voxel, top face | **~2.5 px** |
| 1 art voxel, vertical face | **~1.7 px** |

> **Resolution and density only pay off together, and only if the camera comes closer.**
> Raising density 2.5x and resolution 3x while still showing 48 m of level would have left
> voxels at ~2 px — barely different from before. The default view is therefore **32 m
> wide, not 48**. The full 48 m level still fits when zoomed out (orthographic size 27);
> that is a survey view, not the resting one.

> **At the default angle, top faces read almost 50% larger than vertical ones** — a
> 1-voxel feature on a wall is one screen pixel. So the *first* place to spend detail is
> what faces the sky. But the camera drops to 65° off vertical, where that reverses and
> walls dominate the frame, so vertical faces still have to hold up. Cheap, readable
> blocking on the sides; the expensive detail on top.

## 3. Level footprint

| | Metres | Art voxels |
|---|---|---|
| Target first-level footprint | 48 x 27 | 960 x 540 |
| Default *view* (orthographic size 18) | 32 x 22 | 640 x 440 |
| Survey view, whole level (orthographic size 27) | 48 x 33 | 960 x 660 |

Width is the binding constraint: 48 m is exactly the screen width at orthographic size 27.
The 35 degree default tilt buys depth for free — 33 m of ground fits in the same 27 units of
screen height. A level may therefore be deeper than it looks wide, but never wider than 48 m.
Tilting the camera down shows less ground depth, so a level sized to 33 m deep will not fit
entirely on screen at low angles. That is acceptable: low angles are for looking *into*
things, not for surveying the whole board.

## 4. Character scale

| Element | Voxels | Metres |
|---|---:|---:|
| Average adult height | **36** | 1.80 |
| Short adult | 34 | 1.70 |
| Tall adult | 38 | 1.90 |
| Shoulder width | 14 | 0.70 |
| Body depth | **8** | 0.40 |
| Head | ~8 x 8 x 8 | 0.40 cube |
| Head clearance under a door | 5 | 0.25 |

Body depth is **8, about 0.22 of height**. That ratio was found the hard way at the old
density: 4-in-14 made the legs read as slabs, 3-in-14 was right. Keep the ratio, not the
old number.

One shared body and one shared skeleton for every character in the game. Role identity
comes from **colour, silhouette and accessories** — never from a unique body model.

## 5. Architecture

| Element | Voxels | Metres |
|---|---:|---:|
| Exterior wall thickness | 2 | 0.25 |
| Interior wall thickness | 1 | 0.125 |
| Wall height | 22 | 2.75 |
| Floor slab thickness | 2 | 0.25 |
| Standard doorway opening | 8 w x 16 h | 1.0 x 2.0 |
| Narrow doorway opening | 7 w x 16 h | 0.875 x 2.0 |
| Standard window opening | 8–12 w x 10 h | 1.0–1.5 x 1.25 |
| Window sill height | 7 | 0.875 |
| Minimum corridor | 12 | 1.5 |
| Comfortable corridor | 16 | 2.0 |
| Stair width | 8–12 | 1.0–1.5 |
| Stair rise / run per step | 2 / 2.5 | 0.25 / 0.3125 |

Room sizes:

| Room | Metres |
|---|---|
| Small | 3 x 3 |
| Standard | 4 x 5 |
| Large | 5 x 6 |

Nothing below 3 x 3 m except closets, toilets and utility spaces — NPC routines need room
to pass furniture without navigation fights.

> **Doorway modules are 2 m wide, not 1 m.** A 1 m module with a 1 m opening is not a wall.
> `wall_*_doorway_2m` = 40 voxels wide with the 20-voxel opening centred.

## 6. Residential lot

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

## 7. Street

| Element | Metres |
|---|---|
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

## 8. Pivots — get these right or you will rebuild everything

Goxel has no pivot control, so the pivot is defined by **where the model sits in the goxel
grid**. `tools/build.py` reads the model's bounding box and applies the rule below. Build
inside the guide cage and the build does the rest.

| Asset class | Pivot |
|---|---|
| Floor / structural modules | south-west lower corner |
| Furniture, freestanding props | centre of footprint, at floor level |
| Doors and gates | hinge edge, at floor level |
| Wall-mounted objects | centre of rear mounting face |
| Characters | centre between the feet |
| Vehicles | centre of footprint, at ground level |

The class is declared per asset in `art/assets.json`; the build reads it.

## 9. Detail and materials

**Density is a budget you spend selectively, not an obligation.** 20 vox/m exists so that
detail is *available* where it earns its place — a hat brim with a curve, a badge, a
collar, a door handle — while everything else stays deliberately blocky. A chunky wall next
to a finely-made hat is the intended look, not an inconsistency. Resist the urge to detail
a surface just because there is now room to.

- Anything **gameplay-relevant** reads by silhouette and colour first, detail second.
- Spend detail on: faces, hats, uniforms and insignia, door furniture, anything the player
  must identify at a glance to make a decision.
- Keep blocky: walls, floors, ground, hedges, plain furniture, bulk architecture.
- Do **not** cover surfaces in 1-voxel noise. It still becomes static, just finer static.
- **Never put distinguishing detail inside a 1 m ground tile.** Measured 2026-08-02: four
  dark voxels in an 8x8 grass tile stamped a plainly visible 1 m grid across a 12 x 12 m
  field, and random 90-degree rotation did not break it up. A repeated tile can only carry
  flat colour. Ground variety comes from **2-3 whole-tile variants placed randomly**, plus
  scattered detail props and decals — never from detail within the repeating unit.
- Palette: **~32 colours total, for the whole game.** See `art/palette.json`.
- Material families: painted wood, bare wood, brick, concrete, asphalt, grass, foliage,
  water, glass, metal, fabric, skin. 8–12 total.
- One sun, soft ambient, moderate AO, high roughness, minimal metal, restrained specular.

## 10. Reference prop dimensions

| Prop | Voxels (X x Y x Z) | Metres |
|---|---:|---:|
| Dining chair | 10 x 10 x 18 | 0.5 x 0.5 x 0.9 |
| Dining table | 20 x 30 x 15 | 1 x 1.5 x 0.75 |
| Single bed | 20 x 40 x 13 | 1 x 2 x 0.65 |
| Double bed | 30 x 40 x 13 | 1.5 x 2 x 0.65 |
| Sofa (2-seat) | 40 x 18 x 18 | 2 x 0.9 x 0.9 |
| Kitchen counter (1 m) | 20 x 13 x 18 | 1 x 0.65 x 0.9 |
| Wardrobe | 20 x 13 x 40 | 1 x 0.65 x 2 |
| Trash bin | 10 x 10 x 18 | 0.5 x 0.5 x 0.9 |
| Mailbox | 8 x 10 x 20 | 0.4 x 0.5 x 1 |
| Sedan | 35 x 80 x 30 | 1.75 x 4 x 1.5 |
| Service van | 40 x 100 x 45 | 2 x 5 x 2.25 |

The model need not fill its box, but its **declared footprint and pivot must match** the box.

---

## Axis convention

Goxel is **Z-up**. Godot is **Y-up**. The export tool applies the conversion; you never
think about it. In goxel:

- **+X** = model's width (screen-east)
- **+Y** = model's depth (screen-north)
- **+Z** = up

Author every asset facing **+Y** (its "front" points toward `-Y`, i.e. toward the camera).
