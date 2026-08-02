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


def src_path(a):
    return os.path.join(SRC, a["name"] + ".vox")


def guide_path(a):
    return os.path.join(TEMPLATES, a["name"] + "_guide.vox")


def model_path(a):
    return os.path.join(MODELS, a["name"] + ".gltf")


def is_built(a):
    """True once real art exists — not merely because a file is present.

    Claude opens each task by copying the guide to its final path in art/src/ so
    Juno only ever has to press Ctrl+S. That means "the file exists" says nothing.
    An asset counts as built when it holds voxels that are not guide colours.
    """
    path = src_path(a)
    if not os.path.exists(path):
        return False
    import vox  # local import: manifest is imported by tools that never read .vox

    try:
        model = vox.read(path)
    except (vox.VoxError, OSError):
        return False
    _, guides = load_palette()
    return len(model.without_colors(guides.values())) > 0


def metres(size):
    return tuple(round(v / VOXELS_PER_METRE, 3) for v in size)
