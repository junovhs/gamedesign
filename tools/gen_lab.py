#!/usr/bin/env python3
"""Publish the asset manifest into the Godot project.

art/assets.json is the source of truth; the Godot scale lab reads a trimmed copy
at game/assets/manifest.json. Run this after editing art/assets.json.

Usage:  python3 tools/gen_lab.py
"""

import json
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import manifest

CAMERA_TILT_DEGREES = 15.0  # keep in step with docs/SCALE.md section 2


def main():
    batches, assets = manifest.load_assets()
    out = {
        "_generated_by": "tools/gen_lab.py — do not edit, edit art/assets.json",
        "voxels_per_metre": manifest.VOXELS_PER_METRE,
        "camera_tilt_degrees": CAMERA_TILT_DEGREES,
        "batches": batches,
        "assets": [
            {
                "name": a["name"],
                "title": a["title"],
                "batch": a["batch"],
                "order": a["order"],
                "size": a["size"],
                "pivot": a["pivot"],
                "fit": a["fit"],
            }
            for a in assets
        ],
    }
    path = os.path.join(manifest.ROOT, "game", "assets", "manifest.json")
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w") as f:
        json.dump(out, f, indent=1)
    print(f"wrote {os.path.relpath(path, manifest.ROOT)} ({len(assets)} assets)")


if __name__ == "__main__":
    main()
