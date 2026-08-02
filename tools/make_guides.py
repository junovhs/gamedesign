#!/usr/bin/env python3
"""Generate a goxel starting file for every asset in the manifest.

Each guide .vox contains, in magenta and cyan:

  * eight corner brackets marking the asset's exact declared bounding box
  * a metre grid on the floor plane under the box
  * a 14-voxel human silhouette standing beside the box for scale

Guide colours are reserved and `tools/build.py` strips them automatically, so
there is nothing to clean up before saving. Open the guide, build inside the
brackets, save over art/src/<name>.vox.

Usage:  python3 tools/make_guides.py [name ...]
"""

import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import manifest
import vox

# The scale mannequin: 5 wide, 4 deep, 14 tall. Drawn as a filled silhouette so
# it reads instantly rather than as a wireframe that competes with the brackets.
# Each row is one Z level, top (z=13) first, one character per X.
HUMAN = [
    ".###.",  # 13 head
    ".###.",  # 12
    ".###.",  # 11
    "..#..",  # 10 neck
    "#####",  # 9  shoulders
    "#####",  # 8
    "#####",  # 7
    "#####",  # 6
    "#####",  # 5
    ".###.",  # 4  hips
    ".#.#.",  # 3  legs
    ".#.#.",  # 2
    ".#.#.",  # 1
    ".#.#.",  # 0  feet
]

GAP = 3  # voxels between the asset box and the mannequin


def bracket_len(size):
    """Corner brackets scale with the box so they never swallow a small asset."""
    return max(1, min(3, min(size) // 3))


def build_guide(size, guide_a, guide_b):
    w, d, h = size
    m = vox.Model((1, 1, 1), {})
    n = bracket_len(size)

    # Corner brackets: from each of the 8 corners, run n voxels along each axis.
    for cx, ex in ((0, 1), (w - 1, -1)):
        for cy, ey in ((0, 1), (d - 1, -1)):
            for cz, ez in ((0, 1), (h - 1, -1)):
                for i in range(n):
                    for p in (
                        (cx + ex * i, cy, cz),
                        (cx, cy + ey * i, cz),
                        (cx, cy, cz + ez * i),
                    ):
                        m.voxels[p] = guide_a

    # Metre grid on the floor plane, one level below the box, extending a little
    # past it so the asset's footprint can be read against whole metres.
    pad = manifest.VOXELS_PER_METRE
    for x in range(-pad, w + pad):
        for y in range(-pad, d + pad):
            on_line = x % manifest.VOXELS_PER_METRE == 0 or y % manifest.VOXELS_PER_METRE == 0
            if on_line:
                m.voxels[(x, y, -1)] = guide_b

    # Mannequin, standing on the same floor plane, clear of the box in +X.
    ox = w + GAP
    oy = max(0, d // 2 - 2)
    for row, line in enumerate(HUMAN):
        z = len(HUMAN) - 1 - row
        for x, ch in enumerate(line):
            if ch == "#":
                for y in range(2):
                    m.voxels[(ox + x, oy + y, z)] = guide_b

    # .vox coordinates are unsigned bytes, so shift everything positive.
    lo = tuple(min(p[i] for p in m.voxels) for i in range(3))
    m = m.translated(-lo[0], -lo[1], -lo[2])
    m.size = m.extent()

    # Report where the asset's own origin ended up after that shift.
    return m, (-lo[0], -lo[1], -lo[2])


def write_gpl():
    """Emit a GIMP palette goxel can load, so the 32 colours are one click away."""
    palette, guides = manifest.load_palette()
    path = os.path.join(manifest.TEMPLATES, "grapeghost.gpl")
    with open(path, "w") as f:
        f.write("GIMP Palette\nName: Grapeghost\nColumns: 8\n#\n")
        for name, (r, g, b, _) in palette.items():
            f.write(f"{r:>3} {g:>3} {b:>3}\t{name}\n")
        for name, (r, g, b, _) in guides.items():
            f.write(f"{r:>3} {g:>3} {b:>3}\tGUIDE-{name}\n")
    return path


def main(argv):
    _, assets = manifest.load_assets()
    _, guides = manifest.load_palette()
    a_col, b_col = guides["guide_primary"], guides["guide_secondary"]

    wanted = set(argv)
    if wanted:
        assets = [a for a in assets if a["name"] in wanted]
        missing = wanted - {a["name"] for a in assets}
        if missing:
            raise SystemExit("unknown asset(s): " + ", ".join(sorted(missing)))

    os.makedirs(manifest.TEMPLATES, exist_ok=True)
    for a in assets:
        model, origin = build_guide(a["size"], a_col, b_col)
        path = manifest.guide_path(a)
        vox.write(path, model)
        print(
            f"{a['name']:<28} box {a['size'][0]}x{a['size'][1]}x{a['size'][2]}"
            f"  origin at {origin}  -> {os.path.relpath(path, manifest.ROOT)}"
        )
    gpl = write_gpl()
    print(f"\n{len(assets)} guide(s) written.")
    print(f"palette -> {os.path.relpath(gpl, manifest.ROOT)}")
    print("install it for goxel with:  make palette")


if __name__ == "__main__":
    main(sys.argv[1:])
