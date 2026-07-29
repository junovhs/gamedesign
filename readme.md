# THE LITTLE DIGGER

A small creature that can smell buried treasure. You take it somewhere, music starts, a clock
starts, and you dig where you think the signal is strongest. Most holes have something small.
Sometimes there's a map — and a map is a *picture* of a place, which sends you somewhere else.

**Play it on your phone:** <https://junovhs.github.io/gamedesign/>

No install, no build, no server. One file, `index.html`, published on push to `main`.

---

## Controls

**Phone** — left thumb walks, right thumb looks, **DIG** and **^** (jump) bottom right.
Tap the picture in the corner to flip between maps you're holding.

**Desktop** — `wasd` move, mouse look, `space` jump, `e` dig, `tab` flip pictures.

## What's in the prototype

Steps 1–4 of the build order in [`docs/brief.md`](docs/brief.md):

- **Movement** with momentum, skid, lean, squash on landing.
- **The hunt** — walk into the drifting insects, the camera lifts and looks down, a clock
  starts, six things are buried, digging costs time.
- **Hot and cold.** Every dig ends in a graded call from the creature — `kweh.` when there's
  nothing out here, up to `KWEHHH!!!!` on a find. A miss is a measurement. Two or three digs
  triangulate. No meter, no arrow, no number, ever.
- **Maps are pictures.** A second camera renders a real landmark from a random angle at a
  random time of day, posterised onto paper. You recognise the place, you go there, you dig.

The whole thing is a dependency-free software 3-D renderer written for this prototype: real
six-faced boxes, painter-sorted, at a low internal resolution scaled to the screen shape.

## Repository

| | |
|---|---|
| `index.html` | the game. one file. |
| `docs/` | [direction](docs/direction.md), the original [brief](docs/brief.md), [concept](docs/concept.md), [philosophy](docs/philosophy.md) |
| `old/` | earlier unrelated prototypes. read-only history — do not extend them (DEC-01). |

## Decisions and open questions

They live in Ishoo, not in markdown:

```
ishoo decision list             # DEC-01..07
ishoo plan show core-questions  # Q-01..06, the six open questions
ishoo status                    # what to do next
```

Two rules worth knowing before touching anything:

- **DEC-07 — prototypes are phone-native web builds.** If it can't be opened on a phone and
  played with thumbs, it isn't built. Touch, screen-shape-adaptive resolution and a phone
  frame-rate budget are part of the prototype, not a later port.
- **DEC-02 — three minutes to pick up, five hundred hours deep.** Every feature has to earn
  a permanent gain inside three minutes *and* get more interesting the more you know the
  world.

## Status

Prototype. The look is placeholder, digging is not yet deep enough to carry hundreds of
hours, and steering under the hunt camera needs work — those are Q-01, Q-04 and Q-02.

The creature's `kweh` is a testing placeholder and does not ship (DEC-04).
