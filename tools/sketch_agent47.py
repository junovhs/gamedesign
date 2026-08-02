#!/usr/bin/env python3
"""Claude's first pass at the base character, as an Agent 47 blockout.

Kept because it is a worked example of the density budget in docs/SCALE.md: the
detail goes on the face, collar, tie, hands and the barcode, while the suit,
legs and shoes stay plain blocks. It is scaffolding for Juno to draw over, not
shipped art — he owns the character.

Written against art/src/char_civilian_base.vox at 14 x 8 x 36.
"""
import sys
sys.path.insert(0, '/home/juno/grapeghost/tools')
import vox, manifest

P, _ = manifest.load_palette()
SUIT, SEAM = P['grey_dark'], P['ink']
TROUSE, SHIRT, TIE = P['ink'], P['white'], P['red']
SKIN, SHADE = P['skin_light'], P['skin_mid']

W, D, H = 14, 8, 36
m = vox.Model((W, D, H), {})

def fill(x0, x1, y0, y1, z0, z1, c):
    for x in range(x0, x1 + 1):
        for y in range(y0, y1 + 1):
            for z in range(z0, z1 + 1):
                m.voxels[(x, y, z)] = c

def clear(x0, x1, y0, y1, z0, z1):
    for x in range(x0, x1 + 1):
        for y in range(y0, y1 + 1):
            for z in range(z0, z1 + 1):
                m.voxels.pop((x, y, z), None)

# ---- head: 7 cube, bald ----------------------------------------------
fill(4, 10, 1, 7, 29, 35, SKIN)
fill(4, 10, 1, 7, 29, 29, SHADE)              # jaw underside
m.voxels[(5, 1, 32)] = SEAM                   # eyes, single voxels
m.voxels[(9, 1, 32)] = SEAM
m.voxels[(7, 1, 31)] = SHADE                  # nose shadow
for x in (5, 6, 8):                           # barcode on the back of the skull
    fill(x, x, 7, 7, 30, 31, SEAM)
fill(6, 8, 3, 5, 28, 28, SHADE)               # neck

# ---- torso: 8 wide, with sloped shoulders ----------------------------
fill(3, 10, 0, 7, 16, 27, SUIT)
fill(4, 9, 0, 7, 28, 28, SUIT)                # shoulder crown either side of the neck
clear(6, 8, 3, 5, 28, 28)
fill(6, 8, 3, 5, 28, 28, SHADE)

# ---- arms held off the body, with real air between ------------------
for x0, x1 in ((0, 1), (12, 13)):
    fill(x0, x1, 2, 5, 17, 26, SUIT)          # sleeve
    fill(x0, x1, 2, 5, 13, 16, SKIN)          # bare hand and wrist
# shoulders bridge across to the torso only at the very top
fill(2, 2, 2, 5, 25, 27, SUIT)
fill(11, 11, 2, 5, 25, 27, SUIT)
# everything between arm and torso below the shoulder stays empty
clear(2, 2, 0, 7, 13, 24)
clear(11, 11, 0, 7, 13, 24)

# ---- shirt and tie, front face only ---------------------------------
fill(5, 9, 0, 1, 27, 27, SHIRT)               # collar spread
fill(6, 8, 0, 1, 19, 26, SHIRT)
fill(7, 7, 0, 1, 18, 26, TIE)

fill(3, 10, 0, 7, 15, 15, TROUSE)             # belt

# ---- legs with a gap, and shoes ------------------------------------
fill(3, 5, 1, 6, 2, 14, TROUSE)
fill(8, 10, 1, 6, 2, 14, TROUSE)
fill(3, 5, 0, 6, 0, 1, SEAM)
fill(8, 10, 0, 6, 0, 1, SEAM)

m.size = m.extent()
vox.write('/home/juno/grapeghost/art/src/char_civilian_base.vox', m.moved_to_origin())
print('extent', m.extent(), 'voxels', len(m))
