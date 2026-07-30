<!-- ishoo:begin -->
This repository is managed by Ishoo and mapped by SEMMAP. Before handling the first user request, call the `ishoo_brief` and `semmap_brief` MCP tools. Drive all issue, plan, and decision work through the `ishoo_*` MCP tools and code navigation through the `semmap_*` tools — do not substitute the Ishoo or SEMMAP command-line interfaces. If either MCP server or its brief tool is unavailable, stop and tell the user which server must be enabled before continuing.
<!-- ishoo:end -->

## DOWNSHAFT — house rules

**The game is DOWNSHAFT (DEC-09).** A guy in his backyard with a pickaxe, digging down, and it
gets stranger the deeper he goes. If you find a doc, comment or issue that talks about a
creature that smells buried treasure, a hunt, or its voice, that is *The Little Digger* — a
superseded direction archived at the git tag `archive/little-digger`. Do not build from it.
Read [`docs/design.md`](docs/design.md) before designing anything.

**Phone-native or it does not count (DEC-07).** The designer tests on a phone browser during
the day; that is the only testing opportunity that exists. Everything must be openable on a
phone at a URL and playable with thumbs. Touch controls, resolution that adapts to the screen
shape, and a frame-rate budget for phone hardware are part of building it, never a later port.
Do not propose desktop-only spikes, installs, or build steps.

**The one file (DEC-13).** `index.html` is the whole game: no dependencies, no build, no asset
fetches, published to GitHub Pages on push to `main`. It is the codebase, not a sketch — code
quality in it counts. Rust/wasm is a later port of a proven design, never a reason to defer a
fix.

**Feel ships with the mechanic (DEC-16).** A feature is not done when it works, it is done
when doing it feels good on a phone. Impact, particles, shake, sound and palette response
belong in the same change as the mechanic. There is no later polish pass. Candy Crush is the
bar.

**Deeper is funnier (DEC-15).** Every layer down is stranger than the one above. Colourful,
absurd, never grim, never horror. `docs/north-star.png` is the reference of record.

**The ground is the readout (DEC-11).** The HUD counts only what the player already owns —
depth, picks, bag, purse. Never add a minimap, an ore radar, a stability meter or an arrow to
the good stuff.

**No art assets (DEC-14).** Every tile is pixel data drawn by code. No image files in the
build, nothing 3-D. Authored pixel art reaches the game through the importer (TOOL-01), which
is a separate page and never a build step.

**Before designing anything**, read the ACCEPTED ADRs (`ishoo decision list`). DEC-10 (three
minutes to pick up, five hundred hours deep) and DEC-15 decide most arguments before they
start.

**Verify on a phone-shaped viewport.** Headless Chrome at 844x390 and 390x844 catches layout
and control-placement problems before the designer wastes a break on them.
