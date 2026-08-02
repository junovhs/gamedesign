"""Shared loading of art/assets.json and art/palette.json."""

import json
import os

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

ART = os.path.join(ROOT, "art")
SRC = os.path.join(ART, "src")
TEMPLATES = os.path.join(ART, "templates")
MODELS = os.path.join(ROOT, "game", "assets", "models")

PIVOTS = {
    "corner": "south-west lower corner",
    "footprint_center": "centre of footprint, at floor level",
    "hinge": "hinge edge (-X), at floor level",
    "wall_rear": "centre of rear mounting face",
    "feet": "centre between the feet",
    "vehicle": "centre of footprint, at ground level",
}

VOXELS_PER_METRE = 8


def hex_to_rgba(h):
    h = h.lstrip("#")
    return (int(h[0:2], 16), int(h[2:4], 16), int(h[4:6], 16), 255)


def load_palette():
    with open(os.path.join(ART, "palette.json")) as f:
        data = json.load(f)
    return (
        {k: hex_to_rgba(v) for k, v in data["palette"].items()},
        {k: hex_to_rgba(v) for k, v in data["guide"].items()},
    )


def load_assets():
    with open(os.path.join(ART, "assets.json")) as f:
        data = json.load(f)
    assets = sorted(data["assets"], key=lambda a: (a["batch"], a["order"]))
    for a in assets:
        if a["pivot"] not in PIVOTS:
            raise SystemExit(f"{a['name']}: unknown pivot {a['pivot']!r}")
        if a["fit"] not in ("exact", "within"):
            raise SystemExit(f"{a['name']}: fit must be 'exact' or 'within'")
    return data["batches"], assets


## goxel's own format is what Ctrl+S naturally produces, so it is the preferred
## source. It cannot be written by anything but goxel (`-e out.gox` crashes), so
## guides are .vox and the build converts .gox -> .vox on the way through.
SRC_EXTENSIONS = (".gox", ".vox")


def src_path(a):
    """Where the artist's file lives — .gox if present, else the .vox guide copy."""
    for ext in SRC_EXTENSIONS:
        p = os.path.join(SRC, a["name"] + ext)
        if os.path.exists(p):
            return p
    return os.path.join(SRC, a["name"] + SRC_EXTENSIONS[0])


def guide_path(a):
    return os.path.join(TEMPLATES, a["name"] + "_guide.vox")


def model_path(a):
    return os.path.join(MODELS, a["name"] + ".gltf")


def is_built(a):
    """True once the asset has passed the build and is in the game.

    Deliberately not "a source file exists": Claude opens each task by copying
    the guide into art/src/ so Juno only has to press Ctrl+S, which means a file
    is present before any art is. The exported model is the honest signal, and
    checking it costs a stat rather than a goxel subprocess.
    """
    return os.path.exists(model_path(a))


def metres(size):
    return tuple(round(v / VOXELS_PER_METRE, 3) for v in size)
