"""Minimal MagicaVoxel .vox reader/writer.

Goxel writes single-model .vox files: MAIN > (SIZE, XYZI, RGBA). That is all we
need, so this module deliberately does not implement the scene-graph chunks
(nTRN/nGRP/nSHP) that MagicaVoxel itself emits. If a file with those ever shows
up, `read` raises rather than silently dropping geometry.

Coordinates are voxel-space and Z-up, matching goxel. Colours are (r, g, b, a).
"""

import struct
from collections import Counter

MAGIC = b"VOX "


class VoxError(Exception):
    pass


class Model:
    """A voxel model: a size, and a {(x, y, z): (r, g, b, a)} dict."""

    def __init__(self, size=(1, 1, 1), voxels=None):
        self.size = tuple(size)
        self.voxels = dict(voxels or {})

    # -- geometry ---------------------------------------------------------

    def bounds(self):
        """Inclusive (min, max) corners of the occupied voxels, or None if empty."""
        if not self.voxels:
            return None
        xs, ys, zs = zip(*self.voxels)
        return (min(xs), min(ys), min(zs)), (max(xs), max(ys), max(zs))

    def extent(self):
        """(w, d, h) of the occupied voxels, or (0, 0, 0) if empty."""
        b = self.bounds()
        if b is None:
            return (0, 0, 0)
        lo, hi = b
        return tuple(hi[i] - lo[i] + 1 for i in range(3))

    def translated(self, dx, dy, dz):
        return Model(
            self.size,
            {(x + dx, y + dy, z + dz): c for (x, y, z), c in self.voxels.items()},
        )

    def moved_to_origin(self):
        """Shift so the occupied bounding box starts at (0, 0, 0)."""
        b = self.bounds()
        if b is None:
            return Model(self.size, {})
        lo, _ = b
        m = self.translated(-lo[0], -lo[1], -lo[2])
        m.size = m.extent()
        return m

    def without_colors(self, colors):
        """Drop every voxel whose RGB matches one of `colors` (RGB triples)."""
        drop = {tuple(c[:3]) for c in colors}
        return Model(
            self.size,
            {p: c for p, c in self.voxels.items() if tuple(c[:3]) not in drop},
        )

    def merged(self, other):
        v = dict(self.voxels)
        v.update(other.voxels)
        m = Model(self.size, v)
        m.size = tuple(max(self.size[i], other.size[i]) for i in range(3))
        return m

    def color_histogram(self):
        return Counter(tuple(c[:3]) for c in self.voxels.values())

    def fill_box(self, lo, hi, color):
        """Fill an inclusive box. Mutates."""
        for x in range(lo[0], hi[0] + 1):
            for y in range(lo[1], hi[1] + 1):
                for z in range(lo[2], hi[2] + 1):
                    self.voxels[(x, y, z)] = color
        self.size = tuple(max(self.size[i], hi[i] + 1) for i in range(3))

    def __len__(self):
        return len(self.voxels)


# -- file io ---------------------------------------------------------------


def _chunks(data, start, end):
    i = start
    while i < end:
        cid = data[i : i + 4].decode("ascii")
        n_content, n_children = struct.unpack("<ii", data[i + 4 : i + 12])
        i += 12
        yield cid, data[i : i + n_content], i + n_content, i + n_content + n_children
        i += n_content + n_children


def read(path):
    with open(path, "rb") as f:
        data = f.read()
    if data[:4] != MAGIC:
        raise VoxError(f"{path}: not a .vox file")

    size = None
    xyzi = None
    palette = None
    for cid, content, ch_start, ch_end in _chunks(data, 8, len(data)):
        if cid != "MAIN":
            continue
        for sub, body, _, _ in _chunks(data, ch_start, ch_end):
            if sub == "SIZE":
                if size is not None:
                    raise VoxError(f"{path}: multi-model .vox is not supported")
                size = struct.unpack("<III", body[:12])
            elif sub == "XYZI":
                xyzi = body
            elif sub == "RGBA":
                palette = body
            elif sub in ("nTRN", "nGRP", "nSHP"):
                raise VoxError(f"{path}: scene-graph .vox is not supported")

    if size is None or xyzi is None:
        raise VoxError(f"{path}: missing SIZE or XYZI chunk")

    # Default MagicaVoxel palette is only needed if RGBA is absent; goxel always
    # writes one, so treat its absence as an error rather than guessing.
    if palette is None:
        raise VoxError(f"{path}: missing RGBA chunk")
    # Palette index i (1..255) maps to bytes [(i-1)*4 : i*4].
    pal = [tuple(palette[j * 4 : j * 4 + 4]) for j in range(256)]

    (count,) = struct.unpack("<I", xyzi[:4])
    voxels = {}
    for k in range(count):
        x, y, z, idx = xyzi[4 + k * 4 : 8 + k * 4]
        voxels[(x, y, z)] = pal[idx - 1]

    return Model(size, voxels)


def write(path, model):
    colors = sorted({c for c in model.voxels.values()})
    if len(colors) > 255:
        raise VoxError(
            f"{path}: {len(colors)} distinct colours, .vox allows 255. "
            "Reduce the palette (see docs/SCALE.md section 9)."
        )
    index = {c: i + 1 for i, c in enumerate(colors)}

    size = struct.pack("<III", *model.size)

    body = struct.pack("<I", len(model.voxels))
    for (x, y, z), c in sorted(model.voxels.items()):
        body += bytes((x, y, z, index[c]))

    pal = b""
    for i in range(256):
        pal += bytes(colors[i]) if i < len(colors) else b"\x00\x00\x00\x00"

    def chunk(cid, content, children=b""):
        return (
            cid.encode("ascii")
            + struct.pack("<ii", len(content), len(children))
            + content
            + children
        )

    children = chunk("SIZE", size) + chunk("XYZI", body) + chunk("RGBA", pal)
    out = MAGIC + struct.pack("<i", 150) + chunk("MAIN", b"", children)
    with open(path, "wb") as f:
        f.write(out)
