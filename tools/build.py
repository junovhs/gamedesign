#!/usr/bin/env python3
"""Build authored .vox files into Godot-ready .gltf models.

For each asset with a file in art/src/ this:

  1. reads the .vox,
  2. strips the reserved guide colours,
  3. checks the bounding box against the manifest and the colours against the
     palette,
  4. normalises the model so its bounding box starts at (0, 0, 0),
  5. exports through goxel to glTF, and
  6. rewrites the glTF root transform so the model arrives in Godot at 1 unit =
     1 metre, Y-up, with the pivot the manifest asked for.

Usage:  python3 tools/build.py [name ...] [--strict] [--quiet]
"""

import json
import math
import os
import shutil
import subprocess
import sys
import tempfile

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import manifest
import vox

VOX = manifest.VOXELS_PER_METRE
SCALE = 1.0 / VOX

# -90 degrees about X, taking goxel's Z-up (x, y, z) to Godot's Y-up (x, z, -y).
ROT_QUAT = [-math.sqrt(0.5), 0.0, 0.0, math.sqrt(0.5)]


def rotate(v):
    x, y, z = v
    return (x, z, -y)


def pivot_offset(kind, size):
    """Where the pivot sits, in voxel coords within the normalised bounding box."""
    w, d, h = size
    return {
        "corner": (0.0, 0.0, 0.0),
        "footprint_center": (w / 2.0, d / 2.0, 0.0),
        "hinge": (0.0, d / 2.0, 0.0),
        "wall_rear": (w / 2.0, float(d), h / 2.0),
        "feet": (w / 2.0, d / 2.0, 0.0),
        "vehicle": (w / 2.0, d / 2.0, 0.0),
    }[kind]


class Problem(Exception):
    pass


def check(asset, model, palette, strict):
    """Return a list of warnings; raise Problem on anything disqualifying."""
    warnings = []
    name = asset["name"]

    if len(model) == 0:
        raise Problem("contains no voxels once guide colours are stripped")

    got = model.extent()
    want = tuple(asset["size"])
    axes = "XYZ"

    if asset["fit"] == "exact":
        if got != want:
            raise Problem(
                f"size is {got[0]}x{got[1]}x{got[2]}, manifest requires exactly "
                f"{want[0]}x{want[1]}x{want[2]} (fit: exact). "
                + ", ".join(
                    f"{axes[i]} is {'over' if got[i] > want[i] else 'under'} by "
                    f"{abs(got[i] - want[i])}"
                    for i in range(3)
                    if got[i] != want[i]
                )
            )
    else:
        over = [i for i in range(3) if got[i] > want[i]]
        if over:
            raise Problem(
                f"size is {got[0]}x{got[1]}x{got[2]}, exceeds the manifest box "
                f"{want[0]}x{want[1]}x{want[2]} on "
                + ", ".join(f"{axes[i]} (by {got[i] - want[i]})" for i in over)
            )
        slack = [i for i in range(3) if got[i] < want[i]]
        if slack:
            warnings.append(
                "smaller than its box on "
                + ", ".join(f"{axes[i]} ({got[i]} of {want[i]})" for i in slack)
                + " — fine if intentional"
            )

    known = {c[:3] for c in palette.values()}
    strays = {c for c in model.color_histogram() if c not in known}
    if strays:
        listed = ", ".join(
            "#%02x%02x%02x" % c for c in sorted(strays)[:8]
        ) + (" ..." if len(strays) > 8 else "")
        msg = f"{len(strays)} colour(s) outside art/palette.json: {listed}"
        if strict:
            raise Problem(msg)
        warnings.append(msg)

    if name == "char_civilian_base" and got[2] != 14:
        raise Problem(f"character is {got[2]} voxels tall; it must be exactly 14")

    return warnings


def patch_gltf(path, asset, size):
    """Wrap the exported scene in a root node carrying scale, axis fix and pivot."""
    with open(path) as f:
        doc = json.load(f)

    w, d, h = size
    centre = (w / 2.0, d / 2.0, h / 2.0)
    p = pivot_offset(asset["pivot"], size)
    # goxel centres the mesh on its bounding box, so a vertex at voxel v lands at
    # (v - centre). We want (v - pivot) * SCALE, then the axis rotation.
    delta = tuple((centre[i] - p[i]) * SCALE for i in range(3))
    translation = list(rotate(delta))

    scene = doc.get("scene", 0)
    roots = doc["scenes"][scene].get("nodes", [])

    root = {
        "name": asset["name"],
        "translation": translation,
        "rotation": ROT_QUAT,
        "scale": [SCALE, SCALE, SCALE],
    }
    if roots:
        root["children"] = roots

    doc.setdefault("nodes", []).append(root)
    doc["scenes"][scene]["nodes"] = [len(doc["nodes"]) - 1]

    with open(path, "w") as f:
        json.dump(doc, f, indent=1)


def build_one(asset, palette, strict, quiet):
    src = manifest.src_path(asset)
    _, guides = manifest.load_palette()

    model = vox.read(src)
    model = model.without_colors(guides.values())
    warnings = check(asset, model, palette, strict)
    model = model.moved_to_origin()

    out = manifest.model_path(asset)
    os.makedirs(os.path.dirname(out), exist_ok=True)

    tmpdir = tempfile.mkdtemp(prefix="gg-build-")
    try:
        clean = os.path.join(tmpdir, asset["name"] + ".vox")
        vox.write(clean, model)
        r = subprocess.run(
            ["goxel", clean, "-e", out],
            capture_output=True,
            text=True,
            timeout=120,
        )
        if r.returncode != 0 or not os.path.exists(out):
            raise Problem(f"goxel export failed:\n{r.stderr.strip() or r.stdout.strip()}")
    finally:
        shutil.rmtree(tmpdir, ignore_errors=True)

    patch_gltf(out, asset, model.extent())

    if not quiet:
        e = model.extent()
        m = manifest.metres(e)
        print(
            f"  built {asset['name']:<28} {e[0]}x{e[1]}x{e[2]} vox "
            f"({m[0]} x {m[1]} x {m[2]} m)  {len(model)} voxels  "
            f"pivot: {asset['pivot']}"
        )
    for w in warnings:
        print(f"    warning: {w}")
    return warnings


def main(argv):
    strict = "--strict" in argv
    quiet = "--quiet" in argv
    names = [a for a in argv if not a.startswith("--")]

    if not shutil.which("goxel"):
        raise SystemExit("goxel is not on PATH — see docs/PIPELINE.md")

    _, assets = manifest.load_assets()
    palette, _ = manifest.load_palette()

    if names:
        wanted = set(names)
        assets = [a for a in assets if a["name"] in wanted]
        missing = wanted - {a["name"] for a in assets}
        if missing:
            raise SystemExit("unknown asset(s): " + ", ".join(sorted(missing)))
    else:
        assets = [a for a in assets if manifest.is_built(a)]

    if not assets:
        print("Nothing to build — art/src/ is empty. Run: python3 tools/task.py next")
        return 0

    ok, failed = 0, []
    for a in assets:
        if not os.path.exists(manifest.src_path(a)):
            failed.append((a["name"], "no file at " + os.path.relpath(manifest.src_path(a), manifest.ROOT)))
            continue
        try:
            build_one(a, palette, strict, quiet)
            ok += 1
        except (Problem, vox.VoxError) as e:
            failed.append((a["name"], str(e)))

    print(f"\n{ok} built, {len(failed)} failed.")
    for name, why in failed:
        print(f"\n  FAILED {name}\n    {why}")
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
