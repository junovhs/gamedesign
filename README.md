# Grapeghost

Top-down social stealth in 2-D pixel art. One compact, dense neighbourhood; a contract
killer; the loop is observe, gain access, manipulate routines, create an opening, escape.
Godot 4. No engine fork, no royalties.

**Read [`docs/PLAN.md`](docs/PLAN.md) first.** It says what phase we are in and what is
frozen. Then [`docs/SCALE.md`](docs/SCALE.md), which is the numbers everything obeys, and
`ishoo status` for the decisions that govern the work.

## How art gets made

Juno prompts an image generator for a character, drops the result into our own sprite
editor, and works it into real pixel art — fit to the grid, snapped to a 16-colour palette,
then transformed, liquified and painted. **A generation is reference; the pixels that ship
are authored in the editor.** Goxel and Aseprite are retired.

## Where things are

| Path | What |
|---|---|
| `docs/PLAN.md` | current phase, what is frozen, what comes next |
| `docs/SCALE.md` | every dimension in the game. the authority. |
| `docs/concept/` | the source brief and the reference mockup |
| `reference/` | the original browser prototype, kept for tone |
| `image-to-sprite-editor-liquify-v2.html` | the sprite editor, until TOOL-03 makes it a real app |
| `tools/show.py` | put a picture on Juno's screen |
| `game/` | the Godot project |

## History

This repo was a testing ground before the pivot to Grapeghost. Everything from before lives
on the `archive/downshaft-and-earlier` branch and the `archive/pre-pivot-2026-08-02` tag,
and the pre-pivot issue store is archived at `refs/ishoo-archive/downshaft`. None of it is
current; do not mine it for design decisions.

The voxel pipeline — goxel, `.vox` sources, glTF export — was retired on 2026-08-02 and is
recoverable from history before commit `c4a83e3`.
