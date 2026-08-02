#!/usr/bin/env python3
"""Generate the chunky base character block-in.

Deliberately dumb: solid head, slab limbs, two eye voxels. A sculpted face was
tried and rejected — it is fiddly to author and fights the blocky architecture.
Identity comes from modular pieces added on top, never from carving this.

Symmetric about column 7 of a 15-wide box, so the tie lands on one centre column.

  python3 tools/sketch_base_body.py
"""

import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import manifest
import vox

W, D, H = 15, 9, 36


def main():
    P, _ = manifest.load_palette()
    suit, dark = P["grey_dark"], P["ink"]
    shirt, tie, skin = P["white"], P["red"], P["skin_light"]

    m = vox.Model((W, D, H), {})

    def fill(x0, x1, y0, y1, z0, z1, c):
        for x in range(x0, x1 + 1):
            for y in range(y0, y1 + 1):
                for z in range(z0, z1 + 1):
                    m.voxels[(x, y, z)] = c

    fill(3, 11, 0, 8, 27, 35, skin)          # head: one solid 9 cube
    m.voxels[(5, 0, 32)] = dark              # eyes, and nothing else
    m.voxels[(9, 0, 32)] = dark
    fill(6, 8, 3, 5, 26, 26, skin)           # neck

    fill(4, 10, 0, 7, 15, 25, suit)          # torso slab
    for x0, x1 in ((0, 2), (12, 14)):        # arms, outboard
        fill(x0, x1, 2, 5, 16, 25, suit)
        fill(x0, x1, 2, 5, 13, 15, skin)     # hands
    fill(3, 3, 2, 5, 24, 25, suit)           # shoulders bridge at the top only
    fill(11, 11, 2, 5, 24, 25, suit)

    fill(6, 8, 0, 0, 25, 25, shirt)          # collar
    fill(6, 8, 0, 0, 18, 24, shirt)
    fill(7, 7, 0, 0, 17, 24, tie)

    fill(4, 10, 0, 7, 14, 14, dark)          # belt
    fill(4, 6, 1, 6, 2, 13, dark)            # legs
    fill(8, 10, 1, 6, 2, 13, dark)
    fill(4, 6, 0, 6, 0, 1, dark)             # shoes
    fill(8, 10, 0, 6, 0, 1, dark)

    m.size = m.extent()
    out = os.path.join(manifest.SRC, "char_civilian_base.vox")
    vox.write(out, m.moved_to_origin())
    print(f"{m.extent()}  {len(m)} voxels -> {os.path.relpath(out, manifest.ROOT)}")


if __name__ == "__main__":
    main()
