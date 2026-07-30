<!-- ishoo:begin -->
This repository is managed by Ishoo and mapped by SEMMAP. Before handling the first user request, call the `ishoo_brief` and `semmap_brief` MCP tools. Drive all issue, plan, and decision work through the `ishoo_*` MCP tools and code navigation through the `semmap_*` tools — do not substitute the Ishoo or SEMMAP command-line interfaces. If either MCP server or its brief tool is unavailable, stop and tell the user which server must be enabled before continuing.
<!-- ishoo:end -->

## DOWNSHAFT — house rules

**Right now we are building M0 — THE PUZZLE IS THE GAME (DEC-19).** Read
[`docs/current-milestone.md`](docs/current-milestone.md) first, every time. It is the only
planning document that is current. The wider plan is frozen: no 500-hour spine, no depth-band
content, no camps, no wiki site, no art importer, no crafting, clothing or shops, no Rust, until
M0 answers whether the collapse puzzle is deep. Those ideas are all recorded. File new ones;
do not start them.

**The game is DOWNSHAFT (DEC-09).** A guy in his backyard with a pickaxe, digging down, and it
gets stranger the deeper he goes. Read [`docs/design.md`](docs/design.md) before designing
anything, and [`docs/north-star-catalogue.md`](docs/north-star-catalogue.md) before proposing
content. If something in the tree contradicts an ACCEPTED ADR, it is stale — say so and fix it.

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

**One board is the atom (DEC-17).** Three minutes to pick up, five hundred hours deep — but the
unit is one compact structural board, not one descent. A session counts if the player left one
board permanently changed. Camps are rare expedition milestones, not landings every few screens.

**The board is the readout (DEC-18).** The HUD is depth, picks, distance to the next camp in
metres, a persistent inventory hotbar, money, and a designed menu control. Carried things stay
visible and usable on the board — never a bag-fullness bar that opens a separate screen. Never a
minimap, an ore radar, a stability meter or an arrow to the good stuff.

**The preview is a promise.** Before a consequential action commits, the game shows its exact
immediate result. Difficulty comes from evaluating consequences, not from fighting an opaque
simulation. Breaking that promise damages the entire game.

**No art assets (DEC-14).** Every tile is pixel data drawn by code. No image files in the
build, nothing 3-D. Authored pixel art will eventually reach the game through the importer
(TOOL-01), which is a separate page, never a build step — and is parked until M0 answers.

**Before designing anything**, read the ACCEPTED ADRs via `ishoo_decision` (`op:list`). DEC-19
(prove the board first) and DEC-15 (deeper is funnier) decide most arguments before they start.

**Verify on a phone-shaped viewport.** Headless Chrome at 844x390 and 390x844 catches layout
and control-placement problems before the designer wastes a break on them.
