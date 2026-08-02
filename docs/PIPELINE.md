# PIPELINE.md — goxel to Godot

Verified working end to end on this machine. Goxel 0.15.1, Godot 4.7.1, Python 3.

## The loop

```
make task                       # what to build, in full
goxel art/templates/<name>_guide.vox
                                # build it, save as art/src/<name>.vox
make build                      # verify + export every authored asset
make lab                        # look at it at the real camera and resolution
```

That is the whole thing. Four commands.

## What each step actually does

### 1. The guide file

`tools/make_guides.py` writes one `art/templates/<name>_guide.vox` per asset, containing:

- **magenta corner brackets** at the exact declared bounding box,
- a **cyan 1 m floor grid** under and around it,
- a **cyan 1.75 m figure** standing beside the box.

Build your model inside the brackets. **Do not delete the guides** — magenta `#ff00ff` and
cyan `#00ffff` are reserved colours and the build strips them automatically. That is also
why those two colours can never appear in real art.

Regenerate them after editing `art/assets.json`:

```
make guides
```

### 2. Authoring

Save to `art/src/<name>.vox`. **`.vox`, not `.gox`** — goxel writes single-model `.vox`
files that the build reads directly, whereas `.gox` is goxel's own container and cannot be
parsed here. If you want a layered working file, keep it anywhere you like and export
`.vox` into `art/src/` when you are done.

Load the palette once, and then never pick a colour by eye:

```
make palette        # installs art/templates/grapeghost.gpl into goxel
```

### 3. The build

`tools/build.py` for each authored asset:

1. reads the `.vox`,
2. strips the reserved guide colours,
3. **checks the bounding box against `art/assets.json`** — `fit: exact` must match on all
   three axes, `fit: within` must not exceed it,
4. warns about any colour outside `art/palette.json` (`--strict` makes that fatal),
5. normalises the model so its bounding box starts at `(0, 0, 0)`,
6. exports to glTF via `goxel <clean>.vox -e <out>.gltf`,
7. rewrites the glTF root node transform so the model arrives in Godot **at 1 unit = 1
   metre, Y-up, with the pivot the manifest declared**.

Output lands in `game/assets/models/<name>.gltf` and Godot imports it automatically.

Build one asset while iterating:

```
python3 tools/build.py chair_dining
```

### 4. Coordinates, so nobody has to think about them again

| | goxel | Godot |
|---|---|---|
| up | +Z | +Y |
| asset width | +X | +X |
| asset depth | +Y | −Z |

The exporter applies a −90° rotation about X. Consequence: **goxel +Y becomes Godot −Z**,
which is Godot's standard forward. Author every asset with its front facing goxel **−Y**,
and it will face the camera in game.

Pivots are handled by the `pivot` field in `art/assets.json`, not by where you place the
model. Build inside the brackets and the build puts the pivot where it belongs.

### 5. Verification without a human at the screen

```
godot --path game -s res://tools/capture.gd -- res://scenes/lab/scale_lab.tscn out.png 40
```

Renders the real 640 x 360 main viewport to a PNG. Use it to check a change actually
landed rather than assuming it did.

## Things that were tried and do not work

Recorded so they are not re-attempted:

- **`goxel --script` cannot see a file passed on the command line.** The script runs
  against an empty image. So post-processing an authored file inside goxel is impossible;
  that is why stripping and verification happen in Python instead.
- **`volume.save("x.gox")` crashes goxel.** `.gox` is an image-level format and the script
  API only exposes volumes. `.vox`, `.obj`, `.gltf`, `.ply` and `.png` all save fine.
- **`.glb` is not a registered export format** in this build. Use `.gltf`.
- **goxel centres the mesh on its bounding box when exporting glTF.** The build compensates;
  do not "fix" it by moving the model in goxel.

## Requirements

| Tool | Version | Where |
|---|---|---|
| goxel | 0.15.1 | `~/.local/bin/goxel` |
| Godot | 4.7.1 stable | `~/.local/bin/godot` |
| Python | 3 | system |

No other dependencies. Nothing to `pip install`.
