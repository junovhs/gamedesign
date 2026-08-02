# Grapeghost — house rules

**Read [`docs/PLAN.md`](docs/PLAN.md) first, every time.** It names the current phase.
Only the current phase is live; everything else is recorded, not started.

**[`docs/SCALE.md`](docs/SCALE.md) is the authority on every dimension.** If a number
appears in code, a scene, or an asset and contradicts SCALE.md, SCALE.md wins and the
other thing is a bug. If a number is not in SCALE.md, it is not a rule — add it there
before relying on it.

**We are in Phase 1: the scale lab.** Its only job is to decide whether the numbers in
SCALE.md produce a legible game. Do not build kit assets, levels, NPC systems, disguises,
routines, destruction systems or editor tooling until Phase 1's exit checklist passes.
File the idea in `docs/concept/`; do not start it.

**Juno draws. Claude runs every tool.** This is the operating model and it is not
negotiable. Juno does not open goxel, does not open Godot, does not run `make`, and does
not type commands. He has said outright he is never going to.

- To hand over an art task: `python3 tools/open_task.py <name>` — it copies the guide to
  its final path in `art/src/` and spawns the goxel window on `DISPLAY=:1`. Juno draws
  inside the magenta cage and presses **Ctrl+S**. No save-as dialog, ever.
- Then Claude runs `tools/build.py`, renders, and **shows him a picture**. If you want him
  to look at something, produce an image and put it in front of him. Never say "open the
  lab and have a look".
- Screenshot a running GUI with `DISPLAY=:1 import -window $(DISPLAY=:1 xdotool search
  --name goxel | head -1) out.png` to check what he is actually seeing.
- Never `pkill -f "goxel art/"` or similar — the pattern matches the launching shell's own
  command line and kills the script mid-run. Match on the pid instead.

Asset work is handed over **one object at a time** through `art/assets.json`, fully
specified. If a task cannot be stated as one object with exact numbers, the task is wrong;
split it.

**Godot 4, never a custom engine.** We roll our own game systems, asset pipeline, editor
tooling and level format. We never roll our own renderer, physics, importer or scene
serialisation. Rust is not on the table.

**No art assets in the build that were not authored in goxel.** Every model is voxel data
exported through `tools/build.py`. No downloaded meshes, no textures, no image files
outside `docs/concept/`.

**Destruction is authored and event-based, in three tiers** (SCALE.md § destruction).
Never a per-voxel rigid-body simulation. This decision is settled; do not reopen it.

**Author modularly, place as prefabs.** No house, room or yard is ever a single unique
model. Walls take colour variants, not new meshes.

**The concept image is a brief, not a blueprint.** `docs/concept/image-ref.png` says what
*categories* of thing the game needs. It is never reproduced tile for tile, and its
proportions are not production scale.

**Verify by rendering, not by assuming.** `godot --path game -s res://tools/capture.gd --
<scene> <out.png>` renders the real 640 x 360 viewport to a PNG. Use it before claiming a
visual change works.

**Reserved colours.** `#ff00ff` and `#00ffff` are build guides and are stripped at export.
They can never appear in real art, and nothing may repurpose them.

**Things already proven not to work** are listed at the bottom of `docs/PIPELINE.md`.
Read that before debugging the goxel pipeline; do not rediscover them.
