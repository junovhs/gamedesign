# Grapeghost

Top-down orthographic social stealth. Voxel art, 640 x 360, one screen per level.
Godot 4. No engine fork, no royalties, no dependencies beyond goxel, Godot and Python 3.

**Read [`docs/PLAN.md`](docs/PLAN.md) first.** It says what phase we are in and what is
frozen. Then [`docs/SCALE.md`](docs/SCALE.md), which is the numbers everything obeys.

## Start working

```
make task     # your next job, fully specified
make build    # verify and export everything you have authored
make lab      # look at it at the real camera and resolution
```

`make help` lists the rest.

## Where things are

| Path | What |
|---|---|
| `docs/PLAN.md` | current phase, what is frozen, what comes next |
| `docs/SCALE.md` | every dimension in the game. the authority. |
| `docs/PIPELINE.md` | goxel → glTF → Godot, and what does not work |
| `docs/concept/` | the source brief and the reference mockup |
| `reference/` | the original browser prototype, kept for tone |
| `art/assets.json` | every asset, its size, its brief — source of truth |
| `art/palette.json` | 32 colours, the whole game |
| `art/templates/` | generated goxel starting files (do not edit by hand) |
| `art/src/` | your authored `.vox` files |
| `tools/` | the pipeline |
| `game/` | the Godot project |

## History

This repo was a testing ground before this pivot. Everything from before lives on the
`archive/downshaft-and-earlier` branch and the `archive/pre-pivot-2026-08-02` tag. None of
it is current; do not mine it for design decisions.
