#!/usr/bin/env python3
"""Deepen an asset along Y by duplicating its existing depth layers.

Characters and props authored flat read as cardboard standees at the game's 35
degree camera, where a lot of what you see is the top and front of an object.
Going from 2 voxels deep to 4 is mechanical, not artistic, so it should not cost
the artist a redraw.

Layers are duplicated in place, front-half from the front layers and back-half
from the back, so front-face detail (a face, a shirt, a tie) stays on the front
and gains thickness rather than being smeared through the model.

  python3 tools/thicken.py <asset> <depth>

Writes art/src/<asset>.vox. Because src_path picks whichever source is newest,
that becomes the file the build uses; the original .gox is left untouched.
"""

import os
import subprocess
import sys
import tempfile

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import manifest
import vox


def thicken(model, target_depth):
    w, d, h = model.extent()
    if d > target_depth:
        raise SystemExit(f"already {d} deep, cannot shrink to {target_depth}")
    if d == target_depth:
        return model

    # Map each new layer to a source layer, stretching the existing layers
    # evenly across the new depth. With d=2 -> 4 this gives 0,0,1,1.
    mapping = [min(d - 1, (y * d) // target_depth) for y in range(target_depth)]

    out = vox.Model((w, target_depth, h), {})
    for (x, y, z), colour in model.voxels.items():
        for new_y, src_y in enumerate(mapping):
            if src_y == y:
                out.voxels[(x, new_y, z)] = colour
    out.size = out.extent()
    return out, mapping


def main(argv):
    if len(argv) != 2:
        raise SystemExit(__doc__)
    name, depth = argv[0], int(argv[1])

    _, assets = manifest.load_assets()
    match = [a for a in assets if a["name"] == name]
    if not match:
        raise SystemExit(f"unknown asset: {name}")
    asset = match[0]

    src = manifest.src_path(asset)
    if not os.path.exists(src):
        raise SystemExit(f"nothing authored yet at {src}")

    tmpdir = tempfile.mkdtemp(prefix="gg-thicken-")
    if src.endswith(".gox"):
        converted = os.path.join(tmpdir, "c.vox")
        subprocess.run(["goxel", src, "-e", converted], capture_output=True, timeout=120)
        model = vox.read(converted)
    else:
        model = vox.read(src)

    _, guides = manifest.load_palette()
    art = model.without_colors(guides.values()).moved_to_origin()
    before = art.extent()

    result, mapping = thicken(art, depth)

    out = os.path.join(manifest.SRC, name + ".vox")
    vox.write(out, result)
    print(
        f"{name}: {before[0]}x{before[1]}x{before[2]} -> "
        f"{result.extent()[0]}x{result.extent()[1]}x{result.extent()[2]}"
    )
    print(f"  new layer y -> source layer y: {list(enumerate(mapping))}")
    print(f"  wrote {os.path.relpath(out, manifest.ROOT)} (now the newest source)")


if __name__ == "__main__":
    main(sys.argv[1:])
