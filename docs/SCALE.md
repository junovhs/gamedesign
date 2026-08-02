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
| Art voxel | **0.125 m** |
| Voxel density | **8 voxels per metre** |
| Structural grid (walls, floors, rooms) | 0.5 m |
| Architecture module increments | 1 m |
| Fine prop placement grid | 0.25 m |
| Vertical elevation increments | 0.25 m |
| Architecture rotation | 90° only |
| Loose-prop rotation | 45° allowed |

An object 8 voxels long is exactly 1 metre in game.

**Voxels are visual only.** Navigation, interaction radii, sound, and all gameplay logic
work in metres. Never write a rule in voxels.

## 2. Render target and camera

```
Internal render resolution   640 x 360
Upscale                      nearest-neighbour, integer where possible
Projection                   orthographic
Camera pitch                 -55deg  (35deg off straight down)   DECIDED 2026-08-02
Camera yaw                   0deg    axis-aligned, never rotated by the player
Camera roll                  0
Orthographic size            27 (vertical units; = 48 m of screen width)
Near / far                   0.05 / 200
```

> **35° was measured, not chosen.** The source brief recommended 12-15° off straight
> overhead. Rendering the first real character through the actual camera showed that at
> 15° a 1.75 m person is the top of a head and nothing else — unreadable. A body only
> resolves from about 25° and reads clearly at 35°. See the sweep that settled it.
>
> The cost is occlusion: at 35° tall walls hide a lot of what is behind them, so
> **cutaway roofs and wall-hiding are load-bearing systems, not polish.**
>
> Yaw is zero so the level grid stays axis-aligned to the screen, matching
> `docs/concept/image-ref.png`. Every asset is authored to read at this one angle.

Derived, at 640 x 360 with orthographic size 27 and 55° below horizontal:

| | |
|---|---|
| Visible ground area | **48 m wide x 33 m deep** |
| 1 m horizontally (screen X) | **13.3 px** |
| 1 m of *height* (vertical faces) | **7.7 px** — foreshortened by cos 55° |
| 1 m of ground *depth* | **10.9 px** — foreshortened by sin 55° |
| A 1.75 m character | **13 px** of body height, plus ~5 px of head top ≈ **19 px** overall |
| 1 art voxel, top face | **~1.4 px** |
| 1 art voxel, vertical face | **~1.0 px** |

> **Detail on vertical faces is nearly invisible; top faces read almost 50% larger.**
> Spend detail on what faces the sky. A 1-voxel feature on a wall is one screen pixel.

## 3. Level footprint

| | Metres | Art voxels |
|---|---|---|
| Target first-level footprint | 48 x 27 | 384 x 216 |
| Maximum that still fits the frame | 48 x 33 | 384 x 264 |

Width is the binding constraint: 48 m is exactly the screen width at orthographic size 27.
The 35 degree tilt buys depth for free — 33 m of ground fits in the same 27 units of screen
height — so a level may be deeper than it is wide-looking, but never wider than 48 m.

## 4. Character scale

| Element | Voxels | Metres |
|---|---:|---:|
| Average adult height | 14 | 1.75 |
| Short adult | 13 | 1.625 |
| Tall adult | 15 | 1.875 |
| Shoulder width | 5 | 0.625 |
| Body depth | 4 | 0.5 |
| Head | ~4 x 4 x 4 | 0.5 cube |
| Head clearance under a door | 2 | 0.25 |

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
> `wall_*_doorway_2m` = 16 voxels wide with the 8-voxel opening centred.

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

- Anything **gameplay-relevant** is at least **2 voxels thick** or carries strong colour contrast.
- 1-voxel detail is fine for handles, trim, buttons, highlights, clothing accents, signs.
- Do **not** cover surfaces in 1-voxel noise. At ~1 screen px per voxel it becomes static.
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
| Dining chair | 4 x 4 x 7 | 0.5 x 0.5 x 0.875 |
| Dining table | 8 x 12 x 6 | 1 x 1.5 x 0.75 |
| Single bed | 8 x 16 x 5 | 1 x 2 x 0.625 |
| Double bed | 12 x 16 x 5 | 1.5 x 2 x 0.625 |
| Sofa (2-seat) | 16 x 7 x 7 | 2 x 0.875 x 0.875 |
| Kitchen counter (1 m) | 8 x 5 x 7 | 1 x 0.625 x 0.875 |
| Wardrobe | 8 x 5 x 16 | 1 x 0.625 x 2 |
| Trash bin | 4 x 4 x 7 | 0.5 x 0.5 x 0.875 |
| Mailbox | 3 x 4 x 8 | 0.375 x 0.5 x 1 |
| Sedan | 14 x 32 x 12 | 1.75 x 4 x 1.5 |
| Service van | 16 x 40 x 18 | 2 x 5 x 2.25 |

The model need not fill its box, but its **declared footprint and pivot must match** the box.

---

## Axis convention

Goxel is **Z-up**. Godot is **Y-up**. The export tool applies the conversion; you never
think about it. In goxel:

- **+X** = model's width (screen-east)
- **+Y** = model's depth (screen-north)
- **+Z** = up

Author every asset facing **+Y** (its "front" points toward `-Y`, i.e. toward the camera).
