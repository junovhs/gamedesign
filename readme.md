# THE LITTLE DIGGER

A small creature that can smell buried treasure. You take it somewhere, music starts, a clock
starts, and you dig where you think the signal is strongest. Most holes have something small.
Sometimes there's a map — and a map is a *picture* of a place, which sends you somewhere else.

**Play it on your phone:** <https://junovhs.github.io/gamedesign/>

No install, no build, no server. One file, `index.html`, published on push to `main`.

---

## What is at that URL right now

**`DOWNSHAFT`** — the 2-D pixel prototype, restored as the live build after the 2-D pivot
(**DEC-08**). It is not the hunt. Its verb is: you are a miner on a rope, you break a vein of
ore, the rubble above it drops into the hole, and you drop with it. Pick the vein that drops
you furthest. Buried finds, a lamp that runs down, a depot to bank at, a small shop.

Tap a tile to dig it. One thumb, portrait.

The top-down painted hunt arena — the actual game — is the next piece of work and does not
exist yet.

## The 2-D pivot

The 3-D line is shelved. It looked best in the Q-07 phone comparator, but that test never
asked who makes the assets: there is no 3-D modelling capacity on this project, free models
are incoherent as a set, and AI 3-D generation is not a pipeline. **DEC-08** supersedes DEC-06
— hand-painted 2-D at a fixed camera, nothing that requires authoring 3-D geometry. The
reference, Chocobo Hot and Cold, is top-down painted art and needed nothing else.

The shelved 3-D build is kept as a git tag, not a file:

```sh
git show iteration/3d-diorama:index.html > /tmp/meadow.html
```

What it proved, and what the 2-D rebuild has to carry across, is in
[`docs/direction.md`](docs/direction.md) — chiefly the graded dig call (`kweh.` up to
`KWEHHH!!!!`, no meter or number ever, DEC-03) and maps-as-pictures.

## Repository

| | |
|---|---|
| `index.html` | the game. one file. currently `DOWNSHAFT`. |
| `docs/` | [direction](docs/direction.md), the original [brief](docs/brief.md), [concept](docs/concept.md), [philosophy](docs/philosophy.md) |
| `old/` | retired prototypes and shelved iterations — [see the index](old/README.md). read-only history, do not extend them (DEC-01). |

## Decisions and open questions

They live in Ishoo, not in markdown:

```
ishoo decision list             # DEC-01..08 (DEC-06 superseded by DEC-08)
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

Prototype, mid-pivot. The render question is settled (DEC-08, hand-painted 2-D) and the fixed
camera removes most of the phone-steering problem. What is still open is the one that matters:
digging is not yet deep enough to carry hundreds of hours — Q-04.

The creature's `kweh` is a testing placeholder and does not ship (DEC-04).
