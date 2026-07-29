<!-- ishoo:begin -->
This repository is managed by Ishoo and mapped by SEMMAP. Before handling the first user request, call the `ishoo_brief` and `semmap_brief` MCP tools. Drive all issue, plan, and decision work through the `ishoo_*` MCP tools and code navigation through the `semmap_*` tools — do not substitute the Ishoo or SEMMAP command-line interfaces. If either MCP server or its brief tool is unavailable, stop and tell the user which server must be enabled before continuing.
<!-- ishoo:end -->

## THE LITTLE DIGGER — house rules

**Phone-native or it does not count (DEC-07).** The designer tests on a phone browser during
the day; that is the only testing opportunity that exists. Every prototype must be openable
on a phone at a URL and playable with thumbs. Touch controls, resolution that adapts to the
screen shape, and a frame-rate budget for phone hardware are part of building it, never a
later port. Do not propose desktop-only spikes, installs, or build steps. Rust/wasm later is
fine — it keeps the phone path.

**The one file.** `index.html` is the whole game: no dependencies, no build, published to
GitHub Pages on push to `main`. Keep it that way; it is why testing at work is possible.

**Before designing anything**, read the ACCEPTED ADRs (`ishoo decision list`). DEC-02 (three
minutes to pick up, five hundred hours deep) and DEC-03 (the dig is the only proximity
signal — no meters, ever) decide most arguments before they start.

**Verify on a phone-shaped viewport.** Headless Chrome at 844x390 and 390x844 catches layout
and control-placement problems before the designer wastes a break on them.
