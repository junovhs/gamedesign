#!/usr/bin/env python3
"""Resample an asset to a different voxel density.

When the grid changes under an asset that is already authored, the shape is
still correct — only the sampling is wrong. Nearest-neighbour resampling gives
back a model of the right size with the right silhouette and colours, as a
starting point to refine rather than a redraw from nothing.

It is a starting point, not a result: a 2.5x resample lands some features on
half-voxels and thickens others unevenly. Expect to clean it up.

  python3 tools/rescale.py <asset> <factor>       # e.g. 2.5 for 8 -> 20 vox/m
  python3 tools/rescale.py <asset> --to-spec      # resample to the manifest size

Writes art/src/<asset>.vox, which becomes the newest source.
"""

import os
import subprocess
import sys
import tempfile

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import manifest
import vox


def resample(model, target):
    """Nearest-neighbour resample of the occupied box to `target` dimensions."""
    src = model.extent()
    out = vox.Model(tuple(target), {})
    for x in range(target[0]):
        for y in range(target[1]):
            for z in range(target[2]):
                sx = min(src[0] - 1, int(x * src[0] / target[0]))
                sy = min(src[1] - 1, int(y * src[1] / target[1]))
                sz = min(src[2] - 1, int(z * src[2] / target[2]))
                colour = model.voxels.get((sx, sy, sz))
                if colour is not None:
                    out.voxels[(x, y, z)] = colour
    out.size = out.extent()
    return out


def load(asset, tmpdir):
    src = manifest.src_path(asset)
    if not os.path.exists(src):
        raise SystemExit(f"nothing authored yet at {src}")
    if src.endswith(".gox"):
        converted = os.path.join(tmpdir, "c.vox")
        subprocess.run(["goxel", src, "-e", converted], capture_output=True, timeout=120)
        return vox.read(converted)
    return vox.read(src)


def main(argv):
    if len(argv) != 2:
        raise SystemExit(__doc__)
    name, spec = argv

    _, assets = manifest.load_assets()
    match = [a for a in assets if a["name"] == name]
    if not match:
        raise SystemExit(f"unknown asset: {name}")
    asset = match[0]

    tmpdir = tempfile.mkdtemp(prefix="gg-rescale-")
    model = load(asset, tmpdir)
    _, guides = manifest.load_palette()
    art = model.without_colors(guides.values()).moved_to_origin()
    before = art.extent()

    if spec == "--to-spec":
        target = list(asset["size"])
    else:
        factor = float(spec)
        target = [max(1, round(v * factor)) for v in before]

    result = resample(art, target)
    out = os.path.join(manifest.SRC, name + ".vox")
    vox.write(out, result)
    print(
        f"{name}: {before[0]}x{before[1]}x{before[2]} -> "
        f"{result.extent()[0]}x{result.extent()[1]}x{result.extent()[2]}  "
        f"({len(result)} voxels)"
    )
    print(f"  wrote {os.path.relpath(out, manifest.ROOT)} — refine, do not ship as-is")


if __name__ == "__main__":
    main(sys.argv[1:])
