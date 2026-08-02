#!/usr/bin/env python3
"""Hand out one asset job at a time.

  python3 tools/task.py            # the next unbuilt asset, in full
  python3 tools/task.py next       # same
  python3 tools/task.py <name>     # a specific asset's brief
  python3 tools/task.py list       # the whole board with status
  python3 tools/task.py status     # one-line progress per batch
"""

import os
import subprocess
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import manifest

BAR = "=" * 72


def rel(p):
    return os.path.relpath(p, manifest.ROOT)


def show(a, batches):
    w, d, h = a["size"]
    mw, md, mh = manifest.metres(a["size"])
    built = manifest.is_built(a)

    print(BAR)
    print(f"  {a['title'].upper()}")
    print(f"  {a['name']}   [{a['batch']} #{a['order']}]   "
          f"{'ALREADY BUILT' if built else 'NOT STARTED'}")
    print(BAR)
    print()
    print(f"  SIZE      {w} x {d} x {h} voxels   ({mw} x {md} x {mh} m)")
    print(f"            X = width, Y = depth, Z = up.  {manifest.VOXELS_PER_METRE} voxels = 1 metre.")
    print(f"  FIT       {a['fit']}", end="")
    if a["fit"] == "exact":
        print("  — must fill the box on all three axes, no more, no less")
    else:
        print("  — must not exceed the box; smaller is allowed")
    print(f"  PIVOT     {a['pivot']} ({manifest.PIVOTS[a['pivot']]})")
    print(f"            Handled automatically at build time. Just build inside the brackets.")
    print(f"  FACING    front faces -Y (toward the camera)")
    print()
    print("  WHAT IT IS")
    for line in wrap(a["brief"], 68):
        print(f"    {line}")
    print()
    print("  MUST")
    for m in a["must"]:
        for i, line in enumerate(wrap(m, 64)):
            print(f"    {'- ' if i == 0 else '  '}{line}")
    print()
    if a.get("palette_hint"):
        print("  PALETTE   " + ", ".join(a["palette_hint"]))
        print("            (names from art/palette.json — load the .gpl in goxel)")
        print()
    print("  JUNO DRAWS. CLAUDE RUNS EVERYTHING ELSE.")
    print("  Juno never opens goxel or Godot himself — Claude spawns the window")
    print("  already loaded with the right file, and Claude reports back with")
    print("  rendered pictures. Never hand Juno a command to type.")
    print()
    print("  CLAUDE: open the window for him")
    print(f"    goxel {rel(manifest.guide_path(a))} &")
    print()
    print("  JUNO: draw it")
    print(f"    Build inside the magenta brackets. The cyan figure beside the box")
    print(f"    is 1.8 m tall; the cyan floor lines are 1 m apart. Leave the guide")
    print(f"    colours alone — they are stripped automatically.")
    print(f"    Save over:  {rel(manifest.src_path(a))}")
    print()
    print("  CLAUDE: build it and show him")
    print(f"    python3 tools/build.py {a['name']}")
    print(f"    make shot          # renders to lab.png, then show him the image")
    print(BAR)


def wrap(text, width):
    words, lines, cur = text.split(), [], ""
    for word in words:
        if len(cur) + len(word) + 1 > width and cur:
            lines.append(cur)
            cur = word
        else:
            cur = f"{cur} {word}".strip()
    if cur:
        lines.append(cur)
    return lines


def main(argv):
    batches, assets = manifest.load_assets()
    cmd = argv[0] if argv else "next"

    if cmd == "list":
        current = None
        for a in assets:
            if a["batch"] != current:
                current = a["batch"]
                print(f"\n  {current.upper()} — {batches.get(current, '')}\n")
            mark = "[x]" if manifest.is_built(a) else "[ ]"
            w, d, h = a["size"]
            print(f"    {mark} {a['order']:>2}. {a['name']:<28} {w}x{d}x{h}")
        print()
        return 0

    if cmd == "status":
        for b, desc in batches.items():
            in_b = [a for a in assets if a["batch"] == b]
            done = sum(1 for a in in_b if manifest.is_built(a))
            print(f"  {b:<8} {done:>2}/{len(in_b):<3} {desc}")
        return 0

    if cmd == "next":
        todo = [a for a in assets if not manifest.is_built(a)]
        if not todo:
            print("  Every asset in the manifest is built. Add more to art/assets.json.")
            return 0
        show(todo[0], batches)
        remaining = len(todo) - 1
        print(f"\n  {remaining} asset(s) left after this one in the whole manifest.\n")
        return 0

    match = [a for a in assets if a["name"] == cmd]
    if not match:
        print(f"  No asset named {cmd!r}. Try: python3 tools/task.py list")
        return 1
    show(match[0], batches)
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
