# Grapeghost — house rules

**Read [`docs/PLAN.md`](docs/PLAN.md) first, every time.** It names the current phase.
Only the current phase is live; everything else is recorded, not started.

**[`docs/SCALE.md`](docs/SCALE.md) is the authority on every dimension.** If a number
appears in code, a scene, or an asset and contradicts SCALE.md, SCALE.md wins and the
other thing is a bug. If a number is not in SCALE.md, it is not a rule — add it there
before relying on it.

**The issue store is the other authority.** `ishoo status` names the accepted decisions
that govern the work. Read them before making a call they already settle.

**We are in Phase 1: the scale lab.** Its only job is to decide whether the numbers in
SCALE.md produce a legible game. Do not build kit assets, levels, NPC systems, disguises,
routines, destruction systems or editor tooling beyond the sprite editor until Phase 1's
exit checklist passes. File the idea in `docs/concept/`; do not start it.

## The game

Top-down **social stealth** in 2-D pixel art. You are a contract killer working a compact,
dense, readable neighbourhood. The loop is:

> **observe → gain access → manipulate routines → create an opening → act → escape**

**This is 2-D.** The camera does not orbit or tilt. It is a fixed three-quarter top-down
view at one of three integer zoom steps. Never author an asset or system that assumes
otherwise, and never reintroduce a 3-D camera.

## Art

**Juno draws. Claude runs every tool.** This is the operating model and it is not
negotiable. Juno does not run builds, does not open a terminal, and does not type commands.
He has said outright he is never going to.

The authoring loop, and the only one:

1. Juno prompts an image generator for a character or prop, referencing an existing pixel
   sprite at a stated size.
2. He drops the result into **our sprite editor**, fits it to the grid, and works it — the
   transform, the liquify brush, the palette, the pencil — until it is real pixel art.
3. Claude exports it into the game.

**A generation is reference material, never a shipped asset.** The pixels that ship are the
ones authored in the editor. No downloaded art, no external tool output, nothing from
goxel or Aseprite — both are retired and neither is coming back.

**Every sprite ships on an explicit palette**, 16 colours per character by default, stored
beside it. Nothing with unconstrained colour enters the game. This is what makes role
recolours a palette swap instead of new art.

**Show him the picture.** `python3 tools/show.py <img>:<caption> ...` builds a labelled
contact sheet and opens it in his image viewer.
**Markdown image links in the terminal show him nothing.** Embedding `![](path)` in a reply
is the same as showing him nothing at all, and citing a file path is worse — he is not
going to go and open it. If there is something to look at, `tools/show.py` it. Never say
"open the editor and have a look".

## Engineering

**Godot 4, never a custom engine.** We roll our own game systems, asset pipeline, editor
tooling and level format. We never roll our own renderer, physics, importer or scene
serialisation. Rust is not on the table.

**The sprite editor is ours, lives in this repo, and is the only art tool.** It is
load-bearing: if it cannot express an edit, the art cannot be made. Its feature set is a
production constraint, not tooling polish.

**Author modularly, place as prefabs.** No house, room or yard is ever a single unique
asset. Walls take colour variants, not new art.

**Destruction is authored and event-based, in three tiers** (SCALE.md § 10). Never a
per-pixel simulation. This decision is settled; do not reopen it.

**The concept image is a brief, not a blueprint.** `docs/concept/image-ref.png` says what
*categories* of thing the game needs. It is never reproduced tile for tile, and its
proportions are not production scale.

**Verify by rendering, not by assuming.** Capture the real viewport to a PNG before
claiming a visual change works, and show it.

**Integer scale, always.** 2x, 3x, 4x and nothing else — not for zoom, not for easing, not
for a transition. A half-pixel on screen is a bug.
