# DOWNSHAFT

You are a guy in your backyard with a pickaxe. You dig down.

It keeps going, and it gets stranger. Somewhere under the lawn there are dinosaur bones, a
skeleton drinking coffee, a motel run by a mole, and eventually a UFO abducting a cow.

**Play it on your phone:** <https://junovhs.github.io/grapeghost/>

No install, no build, no server. One file, `index.html`, published on push to `main`.

![the north star](docs/north-star.png)

---

## The verb

One thumb, portrait, a grid you can see all of. You walk a little, you look at the ground, you
tap a tile and it comes apart.

Everything in the shaft hangs off the two side walls. Cut a mass free of both and it drops —
and if you are standing on it, you drop with it. Dirt slides on its own. Roots grow back while
you work. Burst a pipe and the water digs for you. So the question is never *which tile*, it
is *what will this do*.

Three minutes to pick up, five hundred hours deep. One descent is about two minutes and always
banks something permanent, and the shaft stays carved between visits.

## Repository

| | |
|---|---|
| `index.html` | the game. one file. no dependencies, no build step. |
| `docs/design.md` | the design document — read this first |
| `docs/north-star.png` | the art and tone reference of record |
| `docs/north-star-catalogue.md` | every object in that image, with the role it plays |
| `docs/philosophy.md` | the designer's own game preferences, project-independent |

## Decisions and open questions

They live in Ishoo, not in markdown:

```
ishoo decision list          # DEC-07 and DEC-09..DEC-16 are live; DEC-01..06 and DEC-08 are superseded
ishoo plan show downshaft    # the open questions
ishoo status                 # what to do next
```

Four rules worth knowing before touching anything:

- **DEC-07 — phone-native or it does not count.** The designer tests on a phone browser during
  the day and that is the only testing window there is. If it cannot be opened at a URL and
  played with thumbs, it is not built.
- **DEC-10 — three minutes to pick up, five hundred hours deep.** Every feature has to bank a
  permanent gain inside three minutes *and* get more interesting the more you know the world.
- **DEC-15 — the tone is escalating absurdism.** Every layer down is stranger and funnier than
  the one above. Colourful, never grim, never horror.
- **DEC-16 — the tap is the product.** A mechanic ships with its impact, particles, shake and
  sound in the same change that adds it. There is no later polish pass.

## Status

Playable prototype. The shaft, the collapse, five depth bands, finds, landings, the lift and a
shop all exist. The art is placeholder pixel work moving toward `north-star.png`, via an
importer that does not exist yet (TOOL-01).

The question that decides whether this is a game is Q-04: whether digging is deep enough to
carry hundreds of hours without turning into grind.
