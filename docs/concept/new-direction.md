Yes — **this is a good way to plan**.

That image is actually a very useful kind of planning artifact **if you use it for the right things**.

## What it is good for

That kind of mockup is great for:

* deciding the **overall footprint**
* deciding the **number of spaces**
* seeing what kinds of **props and architecture** repeat
* spotting what the **core asset families** are
* checking if the map feels **readable**
* thinking about **routes**, **sightlines**, and **interaction points**
* figuring out what the player can probably do

It is basically a **visual design brief** for the level.

## What it is *not* good for

It should **not** be treated as exact build data.

Do **not** do this:

* “This image is the level, now I’ll copy it literally tile for tile.”
* “Every object I see here must be built uniquely.”
* “The proportions in the image are automatically the final production scale.”

Instead do this:

> **Use the image to derive the kit.**

That is the important shift.

---

# My honest recommendation

## Use Godot.

And I mean that pretty strongly.

Use **Godot as the engine**, and build **your own game**, **your own tooling**, and **your own asset pipeline** on top of it.

That is the sweet spot.

## I do **not** recommend rolling your own engine

Not for this project.

Because if you roll your own, you are signing up for:

* rendering
* import pipeline
* scene serialization
* camera systems
* collision
* nav/pathfinding
* input
* audio
* animation support
* tooling/editor
* debug tools
* save/load
* UI
* asset management
* build/export process

That is a massive amount of invisible work before you even get to the actual game.

And your game already has real complexity:

* social stealth
* routines
* disguises
* access rules
* interactable environment
* level authoring
* visibility and obstruction
* maybe destruction
* maybe particles
* maybe chunk swapping
* maybe tool-assisted level assembly

That is already enough.

So my recommendation is:

> **Do not roll your own engine. Roll your own systems.**

That is the right line.

---

# On the money question

If you use **Godot**, you do **not** owe them royalties for shipping your game.

In practice, the reason so many indies like it is:

* it’s open source
* no royalty cut
* no engine revenue share
* no “pay us after X sales” thing

So on your “I don’t wanna pay them shit” criterion:

> **Godot passes.**

You can donate if you want. You do not have to.

---

# The big caveat: voxels and destruction

This is the one area where your instinct is both **good** and **dangerous**.

Because yes:

> **voxels do make destruction much more imaginable**

And destruction in your game **could be amazing**.

A house explosion in a social stealth game is very strong fantasy.

But you need to decide **what kind of destruction** you want.

There are two very different versions:

---

## Version A: “movie destruction”

This is the one I recommend.

A house can be blown up, but it is **authored destruction**.

Meaning:

* the house exists intact
* a trigger happens
* the intact house swaps to a **destroyed version**
* debris chunks fly outward
* particles and smoke spawn
* maybe some rigidbody pieces scatter
* navigation updates
* NPCs panic
* fire may spread or block paths
* maybe one wall collapses, opening a new route

This gives you the fantasy of destruction **without** requiring a fully dynamic simulation of the whole world.

This is the smart version.

---

## Version B: “every voxel in the world is fully destructible”

This is the dangerous version.

That means you now need to solve:

* performance
* chunking
* save state for destroyed terrain
* navigation updates
* AI reacting to changed geometry
* collision updates
* debris cleanup
* lighting changes
* networking maybe later
* interactions with doors, furniture, walls, stairs, roofs, fire, bodies, hiding places

That becomes a **destruction engine project**, not a stealth game.

If the whole pitch of the game was “totally destructible social stealth sandbox,” then maybe. But for your project, I think that would be scope poison.

So my recommendation is:

> **Use voxels visually, but make destruction selective, authored, and event-based.**

That will still feel awesome.

---

# Best production strategy

## Use AI mockups to define the kit

That image you showed is a great starting point for asking:

### 1. What are the recurring environment families?

For that level, I immediately see:

* road
* sidewalk
* curb
* crosswalk
* grass
* hedges
* fences
* trees
* small houses
* cutaway rooms
* driveways
* sheds / outbuildings
* creek / water edge
* bridge / crossing

### 2. What are the recurring room families?

* kitchen
* living room
* bedroom
* bathroom
* garage
* utility/storage room

### 3. What are the recurring prop families?

* tables
* chairs
* beds
* counters
* sinks
* toilets
* sofas
* shelves
* crates
* bins
* cars
* benches
* ladders
* signs
* planters
* grills

### 4. What are the gameplay object families?

* open window
* climbable fence
* closets
* crates
* bushes
* construction site
* possible hidden route
* cover spots
* maybe fuse box
* maybe poisonable food/drink
* maybe guard distraction items

That is the correct way to read the concept image.

Not “I need this whole level first.”

Instead:

> **This image tells me what categories of things the game needs.**

---

# The order I would build in

This is the order I would strongly recommend.

## Phase 1: lock the visual and physical scale

Before anything else:

* decide **1 world unit = 1 meter**
* decide your camera
* decide your voxel density
* decide character height
* decide doorway width
* decide standard room dimensions
* decide wall thickness
* decide road width
* decide sidewalk width

You were absolutely right to worry about this.
This really does need to be locked early.

## My suggested scale

Still, I think this is a good default:

* **1 engine unit = 1 meter**
* **8 art voxels = 1 meter**
* character height: **~14 voxels**
* door width: **~8 voxels**
* wall thickness: **2 voxels**
* room dimensions snap to **1 meter grid**
* fine prop placement can snap to **0.25 m**

That is a very sane starting point.

---

## Phase 2: build a scale lab

Not a level.

A test scene with:

* one character
* one chair
* one table
* one bed
* one doorway
* one hall
* one room
* one car
* one tree
* one fence
* one wall
* one staircase
* one cutaway roof/wall setup

This scene exists only to answer:

* does this scale read?
* do interiors feel right?
* does the camera show enough?
* are props too small or too big?
* do characters read clearly?

Only after this works should you make real assets.

---

## Phase 3: build the **minimum modular kit**

I would start with the most reusable boring pieces first:

### Ground / layout kit

* floor tile
* road tile
* sidewalk tile
* grass tile
* water edge tile
* driveway tile

### Boundary kit

* straight wall
* inside corner
* outside corner
* doorway wall
* window wall
* fence
* hedge
* gate

### House shell kit

* room floor
* stairs
* porch
* roofless room walls
* maybe garage opening
* maybe interior partition

### Prop basics

* chair
* table
* bed
* counter
* sofa
* shelf
* crate
* bin
* door
* closet

### Environment basics

* tree
* bush
* lamp post
* mailbox
* bench
* parked car

That kit gets you very far, very fast.

---

## Phase 4: build one tiny complete slice

Not the full dream level.

For example:

* one house
* one front yard
* one street section
* one side path
* one small backyard
* one adjacent outbuilding or garage

And then get this working with:

* one target
* one guard/observer
* one civilian
* one route
* one alternate route
* one distraction
* one social access rule
* one hide spot
* one escape route

That will teach you more than building half a neighborhood.

---

## Phase 5: only then build a whole screen-sized level

Once the kit works.

---

# Should houses be one thing or modular?

My answer is:

> **Author modularly, place as prefabs.**

So:

* walls modular
* windows modular
* floors modular
* props modular

Then assemble those into:

* house A
* house B
* garage A
* kitchen A
* bathroom A
* yard A

So in the editor, a house can feel like “one thing,” but under the hood it is built from reusable parts.

That is the right compromise.

If you make every house as one giant unique asset, you’ll lose flexibility fast.

---

# If you want destruction, this matters even more

Because for destruction, modular structure helps enormously.

For example:

## House can be split into logical destructible chunks

* roof chunk
* front wall chunk
* side wall chunk
* porch chunk
* interior furniture cluster
* window set
* staircase chunk

Then when the house explodes:

* spawn debris pieces
* swap in broken wall states
* remove cover here
* add cover there
* block one path
* open another

That feels destructible without requiring “simulate every cube always.”

---

# What kind of Godot setup I’d use

I would not use a “full voxel engine” unless later you prove you truly need it.

I would use:

* Godot 4
* 3D scene
* orthographic camera
* voxel-style meshes
* low-res rendering
* pixelated upscale
* custom editor tooling
* grid-based placement
* your own level data format
* your own gameplay logic

So visually it is voxel, but technologically it is mostly:

> **stylized 3D with modular blocky assets**

That is simpler and more controllable.

---

# Very important distinction

There are really **three layers** here:

## 1. Concept layer

AI-generated 2D map like the one you showed.

This answers:

* what kinds of spaces?
* what vibe?
* what recurring assets?
* what route ideas?

## 2. Build layer

Modular voxel assets and prefabs.

This answers:

* what do I actually need to model?
* how can it repeat?
* what dimensions do I use?

## 3. Game layer

NPC logic, disguises, routines, sound reactions, destruction triggers, etc.

This answers:

* what makes it fun?

Do not confuse layer 1 with layer 2.
The concept image is not the final construction blueprint.
It is the **source for the blueprint**.

---

# So: should you roll your own system?

## My final answer:

* **Roll your own game systems?** yes
* **Roll your own asset pipeline?** yes
* **Roll your own editor tools?** yes
* **Roll your own level format?** yes
* **Roll your own engine?** no

That’s the line I’d hold.

---

# My recommendation in one sentence

> **Use Godot, lock scale early, use AI top-down mockups as asset-planning references, build a reusable modular voxel kit, and treat destruction as selective authored set-piece destruction rather than fully dynamic world-wide voxel simulation.**

---

If you want, the next really useful thing I can do is either:

1. make you a **concrete voxel scale spec sheet**
   *(character size, door size, wall thickness, room sizes, road sizes, etc.)*

or

2. make you a **first-pass modular asset list** for a Whittleton Creek–style test level.


****


Below is a practical **v0.1 production specification**. Treat these numbers as provisional until the scale-test scene is rendered, then freeze them before making the real asset library.

# 1. Voxel scale specification

## Core unit system

| System                         |                      Scale |
| ------------------------------ | -------------------------: |
| Godot world unit               |           1 unit = 1 meter |
| Art voxel                      |                    0.125 m |
| Voxel density                  |         8 voxels per meter |
| Structural grid                |                      0.5 m |
| Preferred architecture modules |             1 m increments |
| Fine prop placement grid       |                     0.25 m |
| Vertical elevation increments  |                     0.25 m |
| Architecture rotation          |             90° increments |
| Loose-prop rotation            | 45° increments when needed |

An object that is 8 voxels long occupies exactly 1 meter in the game.

The art voxels are only visual units. NPC navigation, interactions, sound, and gameplay logic should use meters—not individual voxels.

## Target screen and map size

Use a low internal rendering resolution:

```text
640 × 360
nearest-neighbor upscale
fixed orthographic camera
```

Recommended first-level footprint:

```text
48 m × 27 m
384 × 216 art voxels
```

Hard upper limit for a single-screen level:

```text
56 m × 31.5 m
448 × 252 art voxels
```

At 48 × 27 meters on a 640 × 360 render:

* 1 meter occupies about 13 screen pixels.
* A 1.75-meter character appears roughly 23 pixels tall.
* One art voxel occupies roughly 1.6 screen pixels before camera-angle effects.

That is a strong balance: chunky voxels remain visible, but the whole level fits on screen.

## Camera

Recommended production camera:

```text
Orthographic projection
Fixed orientation
Grid aligned horizontally and vertically
Approximately 12–15° away from straight overhead
No perspective distortion
No player-controlled rotation
```

The slight angle reveals the fronts of characters, counters, beds, cars, and walls. Keep it close enough to overhead that the level remains immediately understandable.

Use automatic cutaways:

* Roofs disappear over accessible interiors.
* Foreground walls lower or hide when obscuring important activity.
* Tall trees and props fade when covering the player or target.
* Interactive characters can receive a subtle silhouette when obstructed.

## Character scale

| Element                   |           Voxels |          World size |
| ------------------------- | ---------------: | ------------------: |
| Average adult height      |               14 |              1.75 m |
| Short adult               |               13 |             1.625 m |
| Tall adult                |               15 |             1.875 m |
| Shoulder width            |              4–5 |         0.5–0.625 m |
| Body depth                |              3–4 |         0.375–0.5 m |
| Head                      | approximately 4³ | 0.5 m cube visually |
| Door clearance above head |                2 |              0.25 m |

All characters should use one shared rig or animation skeleton. Clothing, hats, hair, bags, tools, and uniforms should be modular attachments.

Suggested first outfit set:

* Player/default civilian
* Resident
* Security/police
* Gardener
* Maintenance/construction
* Food service or domestic staff

## Architecture dimensions

| Element                 |            Recommended size |
| ----------------------- | --------------------------: |
| Exterior wall thickness |           2 voxels / 0.25 m |
| Interior wall thickness |   1–2 voxels / 0.125–0.25 m |
| Wall height             |          22 voxels / 2.75 m |
| Floor slab              |           2 voxels / 0.25 m |
| Standard doorway        |     8 × 16 voxels / 1 × 2 m |
| Narrow doorway          | 7 × 16 voxels / 0.875 × 2 m |
| Standard window         |            8–12 voxels wide |
| Window sill height      |          7 voxels / 0.875 m |
| Minimum corridor        |           12 voxels / 1.5 m |
| Comfortable corridor    |             16 voxels / 2 m |
| Small room              |    24 × 24 voxels / 3 × 3 m |
| Standard room           |    32 × 40 voxels / 4 × 5 m |
| Large room              |    40 × 48 voxels / 5 × 6 m |
| Stair width             |       8–12 voxels / 1–1.5 m |

Avoid rooms smaller than 3 × 3 meters unless they are closets, toilets, or utility spaces. NPC routines need enough room for characters to pass furniture without constant navigation conflicts.

## Residential lot dimensions

For a compact suburban level:

| Element                | Recommended size |
| ---------------------- | ---------------: |
| Small house footprint  |          7 × 9 m |
| Medium house footprint |         8 × 10 m |
| Lot width              |          10–12 m |
| Lot depth              |          10–14 m |
| Front setback          |          2.5–4 m |
| Side passage           |          1.5–2 m |
| Backyard depth         |            3–5 m |
| Garage                 |          4 × 6 m |
| Shed                   |          2 × 3 m |

A house should not be one giant source model. Assemble it from modular architecture, then save the assembly as a reusable prefab.

## Street dimensions

| Element           | Recommended size |
| ----------------- | ---------------: |
| Vehicle lane      |              3 m |
| Two-lane road     |              6 m |
| Sidewalk          |            1.5 m |
| Curb              |           0.25 m |
| Grass verge       |          1–1.5 m |
| Driveway          |          3–3.5 m |
| Crosswalk         |       2–3 m deep |
| Creek             |       4–6 m wide |
| Pedestrian bridge |     1.5–2 m wide |

A useful compact residential cross-section is:

```text
3 m front yard
1.5 m sidewalk
0.25 m curb
6 m roadway
0.25 m curb
1.5 m sidewalk
3 m front yard
```

Total building-to-building distance: approximately 15.5 meters.

## Common prop dimensions

| Prop            | Voxel dimensions | Approximate meters |
| --------------- | ---------------: | -----------------: |
| Dining chair    |        4 × 4 × 7 |  0.5 × 0.5 × 0.875 |
| Dining table    |       8 × 12 × 6 |     1 × 1.5 × 0.75 |
| Single bed      |       8 × 16 × 5 |      1 × 2 × 0.625 |
| Double bed      |      12 × 16 × 5 |    1.5 × 2 × 0.625 |
| Sofa            |       16 × 7 × 7 |  2 × 0.875 × 0.875 |
| Kitchen counter |        4 × 8 × 7 |    0.5 × 1 × 0.875 |
| Wardrobe/closet |       8 × 5 × 16 |      1 × 0.625 × 2 |
| Trash bin       |        4 × 4 × 7 |  0.5 × 0.5 × 0.875 |
| Mailbox         |        3 × 4 × 8 |    0.375 × 0.5 × 1 |
| Sedan           |     14 × 32 × 12 |     1.75 × 4 × 1.5 |
| Service van     |     16 × 40 × 18 |       2 × 5 × 2.25 |

Do not force every prop to fill the exact bounding box, but its pivot and declared footprint must match it.

# Asset-authoring rules

## Pivots

Use consistent pivots from the beginning:

* Floor and structural modules: southwest lower corner.
* Furniture and freestanding props: center of footprint at floor level.
* Doors and gates: hinge at floor level.
* Wall-mounted objects: center of rear mounting face.
* Characters: center between feet.
* Vehicles: footprint center at ground level.

Bad pivots will cause more rework than slightly imperfect modeling.

## Visual-detail rule

Gameplay-relevant features should generally be at least **two voxels thick** or have strong color contrast.

One-voxel details are acceptable for:

* Handles
* Trim
* Buttons
* Small highlights
* Clothing accents
* Signs and markings

Do not cover every surface in single-voxel noise. The camera will turn it into visual static.

## Materials

Start with approximately:

* 24–32 primary palette colors
* 8–12 material families
* Minimal metallic materials
* High roughness
* Restrained specular highlights
* One main sunlight source
* Soft ambient illumination
* Moderate ambient occlusion

Material families might include:

```text
painted wood
bare wood
brick
concrete
asphalt
grass
foliage
water
glass
metal
fabric
skin
```

# Destruction specification

Do not simulate every voxel as an independent rigid body.

Use three destruction tiers.

## Tier 1: Cosmetic breakage

Examples:

* Bottles
* Lamps
* Dishes
* Windows
* Small decorations

Implementation:

* Replace intact mesh with broken version.
* Spawn 3–10 lightweight debris particles.
* No permanent navigation change.

## Tier 2: Gameplay breakage

Examples:

* Doors
* Fences
* Furniture
* Utility panels
* Weak walls
* Machinery

Implementation:

* Swap to a broken prefab.
* Spawn 5–20 prebuilt chunks.
* Update collision.
* Potentially create a route, remove cover, or produce noise.

## Tier 3: Set-piece structural destruction

Examples:

* Blowing up a room
* Collapsing a garage
* Destroying a bridge
* Blowing apart part of a house

Implementation:

1. Hide the intact structure.
2. Reveal an authored destroyed structure.
3. Spawn 20–60 pre-fractured rigid chunks.
4. Add smoke, dust, sparks, fire, and sound.
5. Change navigation and NPC routines.
6. Preserve only a limited number of settled debris pieces.

The visible debris can resemble scattered voxels, but each moving object should usually contain many voxels.

For a house explosion, divide the house into logical chunks:

```text
front wall
rear wall
side walls
porch
roof sections
window sections
interior furniture clusters
small debris particles
```

That will look destructive without making the game engine manage thousands of physical cubes.

# Scale-lock test scene

Before producing final assets, build one scene containing:

* One 14-voxel character
* One 8 × 16-voxel door
* One 4 × 5-meter room
* One 1.5-meter corridor
* Chair, table, bed, sofa, counter
* Exterior wall and interior wall
* One sedan
* Sidewalk and two-lane road
* Tree, hedge, fence, mailbox
* Staircase
* Intact and broken wall
* Cutaway-wall test

Render it at 640 × 360 with the intended camera. Verify:

* Uniforms are distinguishable.
* Doorways are obvious.
* Characters do not look miniature.
* Furniture does not overwhelm rooms.
* Individual voxels remain visible.
* The full 48 × 27-meter test boundary fits on screen.
* Walls do not obscure important activity.

After that test passes, save the values in `SCALE.md` and stop changing them.

---

# 2. First modular asset list

This kit is intended to build a compact Whittleton Creek-style neighborhood: central road, several residential lots, accessible interiors, a creek edge, and a maintenance or construction area.

## A. Terrain and ground kit

Start with these 15 source assets:

```text
ground_grass_1x1m
ground_grass_2x2m
ground_dirt_1x1m
ground_garden_soil_1x1m
ground_asphalt_1x1m
ground_concrete_1x1m
sidewalk_straight_1m
sidewalk_inside_corner
sidewalk_outside_corner
curb_straight_1m
curb_inside_corner
curb_outside_corner
curb_driveway_ramp
crosswalk_3m
storm_drain
```

Most ground variation should come from recoloring, decals, and scattered detail props rather than dozens of unique tiles.

## B. Creek and landscape kit

```text
creek_water_straight_2m
creek_water_bend_inner
creek_water_bend_outer
creek_bank_straight
creek_bank_inner_corner
creek_bank_outer_corner
pedestrian_bridge_2m
tree_deciduous_small
tree_deciduous_large
bush_small
bush_large
hedge_straight_1m
hedge_corner
hedge_end
flowerbed_1x1m
```

Keep trees composed of a trunk mesh and one or two foliage masses. Avoid modeling every leaf.

## C. Residential structure kit

Build the house system from approximately 20 structural pieces:

```text
floor_wood_1x1m
floor_tile_1x1m
floor_carpet_1x1m
floor_concrete_1x1m

wall_exterior_straight_1m
wall_exterior_straight_2m
wall_exterior_inside_corner
wall_exterior_outside_corner
wall_exterior_doorway_1m
wall_exterior_window_1m

wall_interior_straight_1m
wall_interior_straight_2m
wall_interior_corner
wall_interior_doorway_1m

porch_floor_1x1m
porch_step_1m
stairs_straight_1m
garage_door_frame_3m
foundation_edge_1m
chimney
```

The walls should support material or color variants rather than requiring a separate mesh for every paint color.

## D. Doors, windows, fences, and access pieces

```text
door_interior
door_exterior
door_security
door_garage
window_standard
window_open
window_broken

fence_wood_straight_1m
fence_wood_corner
fence_wood_gate
fence_chainlink_straight_1m
fence_chainlink_gate
garden_gate
ladder_short
ladder_tall
```

Doors, windows, and gates should remain separate interactive objects, even when the surrounding wall is static.

## E. Core residential furniture

Build these before decorative objects:

```text
chair_dining
chair_armchair
table_dining_small
table_side
sofa_two_seat
bed_single
bed_double
wardrobe
bookshelf
desk
desk_chair
kitchen_counter_1m
kitchen_counter_corner
kitchen_sink
stove
refrigerator
toilet
bathroom_sink
bathtub
shower
```

A house can already feel convincing with these pieces and material variants.

## F. Exterior neighborhood props

```text
mailbox
trash_bin
recycling_bin
park_bench
street_lamp
garden_chair
garden_table
patio_umbrella
barbecue_grill
propane_tank
lawn_mower
wheelbarrow
garden_tools
plant_pot_small
plant_pot_large
wood_pile
traffic_cone
construction_barrier
road_sign
```

## G. Vehicles

Start with only three:

```text
car_sedan
car_suv
van_service
```

Use recolored materials for variation. Do not build ten unique cars yet.

Separate pieces:

```text
vehicle_door_chunk
vehicle_glass_debris
vehicle_tire_debris
```

These can be reused in accidents and destruction.

## H. Gameplay objects

These should have explicit metadata and interaction hooks:

```text
closet_hiding
large_bush_hiding
trash_bin_hiding
crate_climbable
window_climbable
fence_climbable
fuse_box
security_camera
alarm_panel
telephone
toolbox
poisonable_food
poisonable_drink
gas_grill
propane_tank
electrical_panel
water_valve
generator
```

Each gameplay object should declare:

```text
interaction type
required tool
noise level
access requirement
intact state
disabled state
broken state
NPC reaction category
```

## I. Character kit

One shared body:

```text
body_base
head_base
hands_base
shoes_base
```

Modular clothing:

```text
torso_civilian
torso_resident
torso_security
torso_gardener
torso_maintenance
torso_service

legs_civilian
legs_uniform
legs_workwear

hat_security
hat_gardener
hat_construction
hair_short_a
hair_short_b
hair_long_a
hair_long_b

accessory_radio
accessory_toolbelt
accessory_apron
accessory_bag
```

Do not begin with unique character models. Build role identity from colors, silhouettes, and accessories.

## J. Destruction kit

Build these alongside the intact assets—not months afterward:

```text
wall_exterior_broken_a
wall_exterior_broken_b
wall_interior_broken
door_broken
window_shattered
fence_broken
furniture_debris_small
wood_debris_set
masonry_debris_set
glass_debris_set
dust_burst
smoke_column
spark_burst
small_fire
```

For the first house explosion test:

```text
house_wall_chunk_large
house_wall_chunk_medium
roof_chunk
window_frame_chunk
porch_chunk
interior_debris_cluster
destroyed_house_shell
```

# Recommended prefab assemblies

Do not make these as indivisible source models. Assemble them from the kit and save them as prefabs:

```text
house_small_7x9m
house_medium_8x10m
garage_workshop_4x6m
shed_2x3m
front_yard_10x5m
backyard_party_10x5m
construction_area_6x6m
street_intersection_14x14m
creek_crossing_8x5m
```

A prefab should remain editable internally while behaving like one object when placed in the level.

# First test-level composition

A sensible first neighborhood map at 48 × 27 meters:

```text
Central road/intersection: 14 × 14 m
Northwest residential lot: 10 × 11 m
Northeast target lot: 11 × 11 m
Southwest smaller lot: 9 × 10 m
Southeast construction/garage lot: 10 × 10 m
Creek strip along one edge: 4–5 m deep
Side paths around outer edges: 1.5–2 m wide
```

Only two houses need full interiors initially. The others can be simplified exterior shells or partially accessible spaces.

# Production order

Build in this order:

1. Character, doorway, walls, floor, chair, table, car and tree for the scale lab.
2. Ground, street, curb and sidewalk pieces.
3. Exterior house shell pieces.
4. Doors, windows, fences and hedges.
5. One complete kitchen and living room.
6. Gameplay objects: hiding place, fuse box, grill, camera and climbable window.
7. One small-house prefab.
8. One yard and street prefab.
9. Intact/broken wall and explosion test.
10. First complete social-stealth contract.

The first milestone is not “all neighborhood assets complete.” It is:

> One house, one yard, one street segment, one target routine, one alternate entrance, one distraction, one destructive event, and one escape—all working at the final scale.



***

Prompt to chatgpt that generated @image-ref.png (use this template to mockup levels)

SUBJECT: The whittleton creek level of hitman world of assassination Create a 16:9 pixel-art level mockup based on the subject above. Use a fixed orthographic top-down gameplay view. Show the entire playable level on screen at once. Keep it small, compact, and self-contained, like a classic 2D stealth-game map. Use roofless cutaway interiors viewed almost directly from above. Keep architecture grid-aligned, rectangular, and easy to read. It should feel like a small indie game. Include only a few connected areas, a handful of NPCs, one target, one player character, and a few clear stealth routes.
