#!/usr/bin/env python3
"""Open an asset in goxel, ready to draw.

Juno never opens goxel himself. Claude runs this, the window appears on his
screen already loaded with the right guide, and he only ever presses Ctrl+S —
the file is already sitting at its final path in art/src/.

  python3 tools/open_task.py           # the next unbuilt asset
  python3 tools/open_task.py <name>    # a specific one

Passing --reset throws away work in progress and starts from the clean guide.
"""

import os
import shutil
import subprocess
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import manifest


def open_asset(asset, reset=False):
    guide = manifest.guide_path(asset)
    if not os.path.exists(guide):
        raise SystemExit(f"no guide at {guide} — run: python3 tools/make_guides.py")

    os.makedirs(manifest.SRC, exist_ok=True)
    gox = os.path.join(manifest.SRC, asset["name"] + ".gox")
    fresh = os.path.join(manifest.SRC, asset["name"] + ".vox")

    # Guides are .vox because goxel crashes writing .gox, so a fresh working
    # copy must keep the .vox extension — goxel picks its parser by extension
    # and hands you a blank document if the name lies about the contents.
    # Once Juno has saved real work as .gox, that becomes the file to reopen.
    if reset or (not os.path.exists(gox) and not os.path.exists(fresh)):
        shutil.copyfile(guide, fresh)
    src = gox if os.path.exists(gox) and not reset else fresh

    # setsid so the window outlives this process. Without it goxel dies with the
    # shell that launched it. Note also: never `pkill -f "goxel art/"` to close
    # one — that pattern matches the launching shell's own command line and
    # kills it mid-script.
    subprocess.Popen(
        ["goxel", os.path.abspath(src)],
        start_new_session=True,
        stdin=subprocess.DEVNULL,
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
        env={**os.environ, "DISPLAY": os.environ.get("DISPLAY", ":1")},
    )
    print(f"opened {asset['name']} -> {os.path.relpath(src, manifest.ROOT)}")
    print("Juno draws inside the magenta cage, then Ctrl+S. No save-as needed.")


def main(argv):
    reset = "--reset" in argv
    names = [a for a in argv if not a.startswith("--")]
    _, assets = manifest.load_assets()

    if names:
        match = [a for a in assets if a["name"] == names[0]]
        if not match:
            raise SystemExit(f"unknown asset: {names[0]}")
        target = match[0]
    else:
        todo = [a for a in assets if not manifest.is_built(a)]
        if not todo:
            print("Everything in the manifest is built.")
            return 0
        target = todo[0]

    open_asset(target, reset)
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
