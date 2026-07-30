# DOWNSHAFT — DESIGN

*The one design document. Updated 2026-07-30, when the project was re-founded on DOWNSHAFT
(**DEC-09**) after a week of prototypes.*

---

## 1. WHAT IT IS

You are an ordinary guy in your backyard with a pickaxe. You dig down.

It keeps going. It gets stranger.

That is the whole pitch, and the strangeness is the point: the top of the shaft is a suburban
lawn with a dog and a plastic flamingo, and a long way below it there is a skeleton drinking
coffee, a neon-lit motel run by a mole, a clown, and a UFO abducting a cow. Depth is the
delivery mechanism for the joke (**DEC-15**).

The reference of record for the look and the tone is **[`north-star.png`](north-star.png)**.
Read it top to bottom: that ladder is the game.

## 2. THE VERB

One thumb, portrait, a grid you can see all of.

You walk a little. You look at the ground. You tap a tile and it comes apart.

What makes that a decision rather than a chore is the collapse. Everything in the shaft hangs
off the two side walls; cut a mass free of both walls and it drops, and if you are standing on
it, you drop with it. Dirt and cutlery slide on their own. Roots grow back while you work.
Burst a pipe and the water digs for you. So the question in the player's head is never "which
tile", it is *what will this do*.

That single second is the product (**DEC-16**). It ships with its impact, its particles, its
shake and its sound in the same issue that adds the mechanic — never in a later polish pass,
because polish passes get cut. Candy Crush is the bar.

## 3. THE SHAPE OF A SESSION

Three minutes to pick up, five hundred hours deep, one build, no modes (**DEC-10**).

The atom is **one descent**, about two minutes: drop some depth, bank something permanent,
close the tab. Nothing may hold the player mid-descent, nothing asks them to come back at a
particular time, and every descent ends with something kept. The shaft persists between
visits, which is what makes two minutes bankable — you are always continuing one hole, not
restarting a run.

Depth for the long game comes from *knowing the world*: what a band does, what breaks it, what
falls, how to route back down. Not from grind, and not from a content treadmill.

## 4. WHAT THE PLAYER IS TOLD

The ground is the readout (**DEC-11**). The HUD counts only what the player already owns —
depth, picks, bag, purse. Nothing summarises what is underground: no minimap, no ore radar, no
stability meter, no arrow pointing at the good stuff. A material announces itself by looking
like itself, and you find out what it does by breaking one.

This is also an art constraint: every material has to be legible at 16 px, so tile art carries
mechanics and not just mood.

## 5. WHAT EXISTS IN THE BUILD TODAY

`index.html`, live at <https://junovhs.github.io/grapeghost/>.

- **The shaft.** A 10 × 16 tile screen per depth, generated from a seed in 2 × 2 blocks and
  then stored, so a screen you carved stays carved.
- **Materials.** Dirt, stone, slate, basalt, tile, pipe, root, cutlery, meat, beams, and four
  ores. Each has a tool level, a value, and a behaviour: `loose` slides, `anchor` holds
  whatever touches it, `burst` floods, `regrow` grows back, `alive` moves.
- **Collapse.** Support is flood-filled from the walls and anchors; anything cut free falls,
  and the player falls with it. This is the strategic layer.
- **Depth bands.** THE BACKYARD → THE CUTLERY → SOMEONES FLOOR → THE UPSIDE ORCHARD →
  IT BREATHES. Each introduces one new behaviour and one new palette.
- **Finds.** Visible in the rock, worth money, and each one permanently adds a pick or bag
  space: a sprinkler head, a garden gnome, a fork, a wedding ring, a rubber duck, a doorknob,
  an apple core, a tooth, something warm.
- **Landings and the lift.** Every third screen is a landing; once reached, the lift stops
  there forever, so the trip back down is short.
- **The shop.** Iron pick, the drill, lantern, satchel, beams — bought with the purse.
- **Reset.** Filling the hole in is available and costs the purse.

Everything in that list is subject to the open questions below; none of it is sacred except
the verb.

## 6. HOW THE ART WORKS

There are no art assets (**DEC-14**). Every tile is pixel data drawn by code at runtime, which
is why destruction, lighting, damage states and per-depth palettes are cheap — the pixels are
addressable, so an effect is a transform on data rather than a stack of pre-rendered frames.
It also keeps the game one file that a phone opens from a URL.

The art is still *drawn*, not typed. Pixel art is authored outside the game and converted into
tile data by a separate importer (**TOOL-01**), which is its own page and never becomes a
build step. That tool is what makes a tile-by-tile art pass affordable, and it is the bridge
between the current placeholder palette and `north-star.png`.

Nothing 3-D, ever — not because of taste but because there is no one to model it (the finding
DEC-08 made and DEC-14 keeps).

## 7. HOW IT GETS BUILT

`index.html` is the game, not a sketch of it (**DEC-13**): one file, no dependencies, no build
step, published to GitHub Pages on push to `main`. The whole design gets built there.

The designer tests on a phone browser during the day, and that is the only testing window that
exists — so phone-native is not a porting concern, it is the definition of done (**DEC-07**).

Rust compiled to wasm comes *after* the design is proven, as a port with final art, sound and
music. It is not a rescue plan and never an excuse to defer a fix.

## 8. WHAT IS DECIDED

Full text: `ishoo decision list`, `ishoo decision show DEC-09`.

| | |
|---|---|
| **DEC-07** | Prototypes are phone-native web builds |
| **DEC-09** | DOWNSHAFT is the project: a guy in his backyard, digging down |
| **DEC-10** | Three minutes to pick up, five hundred hours deep; the atom is one descent |
| **DEC-11** | The ground is the readout; the HUD only counts what you already own |
| **DEC-12** | Borrowed placeholders are written down and never ship |
| **DEC-13** | The web build is the game; Rust/wasm is a later port of a proven design |
| **DEC-14** | All art is pixel data drawn by code; the importer is a separate tool |
| **DEC-15** | The tone is escalating absurdism, ordered by depth |
| **DEC-16** | The tap is the product: feel ships with the mechanic, not after it |

DEC-01 to DEC-06 and DEC-08 are superseded. They describe *The Little Digger*, a top-down
creature hunt this project no longer builds; the reasoning chain is kept in Ishoo and the
material is archived at the git tag `archive/little-digger`.

## 9. WHAT IS OPEN

`ishoo plan show downshaft`.

| | | |
|---|---|---|
| **Q-03** | What is the complete verb list for the v1 vertical slice? | crafting, bases, ladders, throwables, residents — in, later or cut |
| **Q-04** | What makes digging deep enough for hundreds of hours without becoming grind? | the one that decides whether this is a game |
| **Q-05** | What is the progression spine from hour zero to hour five hundred? | |
| **Q-06** | How much of the shaft is authored and how much is generated? | |
| **Q-17** | What lives at each depth band, and how does the joke escalate? | the content spine implied by `north-star.png` |
| **TOOL-01** | Build the pixel-art importer that converts drawn art into tile data | |

Ideas on the table and not yet ruled on: crafting from what you dug up, bases you place and
furnish at a depth you have reached, the Mole Motel as a rest stop or a shop, side-view rooms
that play laterally, dinosaur bones and alien junk as collections, zombies and wizards and
vampires as residents. All of it is welcome and none of it is committed — it goes through
Q-03 and Q-17.

## 10. ALSO IN THIS FOLDER

[`philosophy.md`](philosophy.md) — the designer's own preferences: what he likes in games and
why, from Stardew to Grindstone to Plants vs. Zombies. Not about DOWNSHAFT specifically, and
it outlives any one project. Read it before proposing a system.
