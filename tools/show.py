#!/usr/bin/env python3
"""Put an image on Juno's screen.

Markdown image links in the terminal show him nothing — he cannot see any render
unless it is opened in a window. So every time there is something to look at,
open it here rather than describing it or citing a path.

Several images are combined into one labelled contact sheet, so he gets a single
window instead of a stack of them. Labels come from `path:caption` arguments.

  python3 tools/show.py shot.png
  python3 tools/show.py a.png:before b.png:after
  python3 tools/show.py --title "camera sweep" a.png:15deg b.png:35deg
"""

import os
import shutil
import subprocess
import sys
import tempfile

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import manifest

RENDERS = os.path.join(manifest.ROOT, "renders")
BG = "#0f1115"
PANEL = "#1a1c22"


def _label(path, caption, workdir, index):
    """One panel: the image, bordered, with its caption underneath."""
    out = os.path.join(workdir, f"panel{index}.png")
    cmd = ["convert", path, "-resize", "900x900>", "-bordercolor", PANEL, "-border", "6"]
    if caption:
        cmd += [
            "-background", PANEL, "-fill", "white", "-pointsize", "22",
            f"label:{caption}", "-gravity", "center", "-append",
        ]
    cmd.append(out)
    subprocess.run(cmd, check=True)
    return out


def build_sheet(items, title, workdir):
    panels = [_label(p, c, workdir, i) for i, (p, c) in enumerate(items)]
    if len(panels) == 1 and not title:
        return panels[0]

    sheet = os.path.join(workdir, "sheet.png")
    cols = min(len(panels), 3)
    subprocess.run(
        ["montage", *panels, "-tile", f"{cols}x", "-geometry", "+10+10",
         "-background", BG, sheet],
        check=True,
    )
    if title:
        subprocess.run(
            ["convert", "-background", BG, "-fill", "white", "-pointsize", "30",
             f"label:{title}", sheet, "-append", "-background", BG, sheet],
            check=True,
        )
    return sheet


def main(argv):
    title = ""
    if "--title" in argv:
        i = argv.index("--title")
        title = argv[i + 1]
        argv = argv[:i] + argv[i + 2:]
    if not argv:
        raise SystemExit(__doc__)

    items = []
    for arg in argv:
        # Split on the last colon so absolute paths still work.
        if ":" in arg and not os.path.exists(arg):
            path, caption = arg.rsplit(":", 1)
        else:
            path, caption = arg, ""
        if not os.path.exists(path):
            raise SystemExit(f"no such image: {path}")
        items.append((path, caption))

    os.makedirs(RENDERS, exist_ok=True)
    workdir = tempfile.mkdtemp(prefix="gg-show-")
    try:
        sheet = build_sheet(items, title, workdir)
        final = os.path.join(RENDERS, "latest.png")
        shutil.copyfile(sheet, final)
    finally:
        shutil.rmtree(workdir, ignore_errors=True)

    # Detached, or the viewer dies with this process.
    subprocess.Popen(
        ["eog", final],
        start_new_session=True,
        stdin=subprocess.DEVNULL,
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
        env={**os.environ, "DISPLAY": os.environ.get("DISPLAY", ":1")},
    )
    print(f"showing {len(items)} image(s) -> {os.path.relpath(final, manifest.ROOT)}")


if __name__ == "__main__":
    main(sys.argv[1:])
