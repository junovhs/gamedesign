# THE LITTLE DIGGER — DIRECTION

*Updated 2026-07-29, after the first playable test on a phone.*

---

## 1. WHERE WE ARE

There is a playable prototype at `index.html` (live at <https://junovhs.github.io/gamedesign/>).
It covers steps 1–4 of the build order in `little-digger-handoff.md`: movement, the hunt,
maps-as-pictures, and the graded dig response.

It was tested on a phone and the verdict was: **pursue this.** Specifically what landed:

- The palette and the light. The world reads bright and worth walking into.
- The creature is cute enough to carry the game.
- Controls feel good in the first minute.
- The graded dig response ("kweh." → "KWEHHH!!!!") is the thing. It is the game's voice.

And what did not:

- **Steering under the lifted hunt camera is awkward**, especially with a thumb. This was
  true of the original Chocobo game too — it is not a bug we introduced, it is an unsolved
  problem in the reference. See `plans/hands.md`.
- **Digging is too thin to carry hundreds of hours.** Right now it is: walk, press, read the
  call, repeat. There is no craft in it yet. See `plans/dig-depth.md`.
- The look is placeholder. See `plans/look.md`.

---

## 2. WHAT THIS GAME IS TRYING TO BE

> A 500-hour game you can pick up and play in three minutes.

Both halves are load-bearing and they constrain each other:

- **Three minutes.** On a break, in a bathroom, one hand, phone. Open it, do one hunt,
  close it, and have gained something permanent. Nothing may require a long session:
  no timers to come back for, no session-length rewards, no "log in to collect."
- **500 hours.** With a controller, sitting down, for an evening. That depth has to come
  from *knowing the world* and *planning*, not from grind or from a content treadmill.
  The Freelancer half of the design: mastery through familiarity.

The atom of the game is one hunt. Everything else — trips, home, progression, rivals —
wraps that atom without ever making it longer.

---

## 3. A CORRECTION ABOUT THE PROTOTYPE'S RENDERER

The impression from the test was that the prototype draws "2-D planes in a 3-D world,"
possibly for performance. That is not what it does, and the difference matters for the
art-direction decision.

Everything in the prototype is a **real 3-D box** — eight corners, six faces, each face
shaded by its facing and depth-sorted per face (`box()` in `index.html`). There are no
billboards and no sprites anywhere in the scene. The creature is a stack of boxes; so are
the trees, the tower, the arch. It is, structurally, already voxel-ish.

What makes it look flat is not the geometry. It is:

1. **Flat shading with no light model** — one hardcoded brightness per face direction.
   No sun, no shadows, no ambient occlusion, no bounce.
2. **Untextured faces** — a single flat colour per face, so large surfaces read as paper.
3. **Box-only vocabulary** — no bevels, no slopes, no rounding, so nothing reads as *clay*.
4. **A painter's algorithm** — no depth buffer, which is what caps how much geometry and
   how much intersection complexity we can have.

So the move toward a voxel or clay look is **not a change of dimension, it is a change of
fidelity and lighting**, and it is mostly achievable within the same structure — up until
the point where the painter's algorithm becomes the ceiling. That ceiling is the real
reason to make an engine decision. See `plans/look.md` and `adr/ADR-006`.

---

## 4. THE PILLARS, RESTATED

Unchanged from `little-digger-handoff.md`, and now confirmed by play:

1. **Low cognitive load at any moment.** One question in the player's head at a time.
2. **No invented vocabulary.** A map, a whistle, a rope, a hole.
3. **Nothing requires study.** Everything is taught by watching it happen once.
4. **Imply rather than state.**
5. **The core action must be fun before any reward is attached.**

New, learned from the test:

6. **The creature's voice is the interface.** Information reaches the player through what
   the creature does and says, never through a number. This is now `adr/ADR-003`.
7. **Every session must bank something permanent.** Three minutes of play cannot end empty,
   because three minutes may be all a player gets that day.

---

## 5. THE OPEN QUESTIONS, IN PRIORITY ORDER

| # | Question | Where |
|---|---|---|
| 1 | How does the player move under the hunt camera, on a phone? | `plans/hands.md` |
| 2 | What makes digging deep enough for hundreds of hours? | `plans/dig-depth.md` |
| 3 | Voxel or clay — and does the current renderer survive it? | `plans/look.md` |
| 4 | How much of the world is authored and how much is generated? | `plans/world.md` |
| 5 | What does the player build, keep, and come back to? | `plans/progress.md` |
| 6 | What does the creature actually sound like, legally ours? | `plans/voice.md` |

---

## 6. INDEX

- Decisions: [`adr/`](adr/) — what is locked, and what is only proposed.
- Plans: [`plans/`](plans/) — named plans, each a list of issues with scope contracts.
- Original brief: [`../little-digger-handoff.md`](../little-digger-handoff.md)
- Concept: [`../pivot-concept.md`](../pivot-concept.md)
