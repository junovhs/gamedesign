# THE LITTLE DIGGER — DIRECTION

*Updated 2026-07-29, after the 2-D pivot (DEC-08).*

---

## 0. THE PIVOT

The 3-D line is shelved. Q-07's phone comparator asked which look the designer preferred on
screen and voxel won, but it never asked who makes the assets. Nobody does: the art capacity
on this project is 2-D generation and hand-painting, free 3-D models are incoherent as a set,
and AI 3-D generation is not a pipeline in 2026-07. A look you cannot staff turns every
content task into a blocked task. **DEC-08** therefore supersedes DEC-06: hand-painted 2-D at
a fixed camera, and no production path may require authoring or sourcing 3-D geometry.

The reference was always 2-D. Chocobo Hot and Cold is top-down painted art and needed nothing
else, so this is not a compromise — it is the target.

Two open questions move on their own as a result:

- **Q-02 largely dissolves.** Awkward thumb steering was a camera-relative-input problem. At a
  fixed camera, thumb direction is world direction; there is nothing left to solve.
- **Q-06 gets the reference's answer.** Painted terrain is authored terrain. In FF9 the field
  is fixed and hand-drawn and only the *contents* are random — generated at the first peck, not
  at the start of the game. Arena authored, contents generated.

And the reference hands us the deep loop for free: **the progression reward is itself a
painting.** A Chocograph is a hand-painted still with a riddle in it, and finding the place it
depicts is the 500-hour layer. That makes the game's collectible currency the exact artefact
the designer is best at making, with no numbers anywhere in it (DEC-03), and it banks something
permanent inside three minutes.

The live build is now the 2-D `DOWNSHAFT` prototype, restored from `old/`. Note that its verb
is not the hunt — it is "break the vein that drops you furthest." The top-down painted hunt
arena is the next piece of work, not something that exists yet.

---

## 1. WHERE WE WERE

The 3-D prototype (now `git show iteration/3d-diorama:index.html`) covered steps 1–4 of the
build order in `brief.md`: movement, the hunt, maps-as-pictures, and the graded dig response.

It was tested on a phone and the verdict was: **pursue this.** Specifically what landed, and
what the 2-D rebuild must carry across:

- The palette and the light. The world reads bright and worth walking into.
- The creature is cute enough to carry the game.
- Controls feel good in the first minute.
- The graded dig response ("kweh." → "KWEHHH!!!!") is the thing. It is the game's voice.

And what did not:

- **Steering under the lifted hunt camera is awkward**, especially with a thumb. This was
  true of the original Chocobo game too — it is not a bug we introduced, it is an unsolved
  problem in the reference. Q-02. *Answered by DEC-08's fixed camera.*
- **Digging is too thin to carry hundreds of hours.** Right now it is: walk, press, read the
  call, repeat. There is no craft in it yet. Q-04. The reference's own strategy notes say where
  the craft lives: keeping a mental map of where you have already dug, and building a feel for
  how wide an area the creature can detect in. Spatial memory plus an internal probability
  model — free depth, and still missing from anything we have built.
- The look is placeholder. Q-01. *Answered by DEC-08.*

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

## 3. A CORRECTION ABOUT THE SHELVED PROTOTYPE'S RENDERER

*Kept for the record. Superseded by DEC-08 — the question is no longer how to add fidelity to
3-D geometry, it is that we do not author 3-D geometry at all.*

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
reason to make an engine decision. Q-01, and DEC-06 (still PROPOSED).

---

## 4. THE PILLARS, RESTATED

Unchanged from `brief.md`, and now confirmed by play:

1. **Low cognitive load at any moment.** One question in the player's head at a time.
2. **No invented vocabulary.** A map, a whistle, a rope, a hole.
3. **Nothing requires study.** Everything is taught by watching it happen once.
4. **Imply rather than state.**
5. **The core action must be fun before any reward is attached.**

New, learned from the test:

6. **The creature's voice is the interface.** Information reaches the player through what
   the creature does and says, never through a number. This is now DEC-03.
7. **Every session must bank something permanent.** Three minutes of play cannot end empty,
   because three minutes may be all a player gets that day.

---

## 5. THE OPEN QUESTIONS, IN PRIORITY ORDER

| # | Question | Issue | Status |
|---|---|---|---|
| 1 | What render style do we want? | Q-01 | Answered by DEC-08: hand-painted 2-D |
| 2 | How does the player move and dig on a phone? | Q-02 | Mostly answered — fixed camera removes the steering problem |
| 3 | What are all the v1 mechanics? | Q-03 | Open |
| 4 | What makes digging deep without becoming grind? | Q-04 | Open — the reference points at spatial memory and the detection radius |
| 5 | What is the progression spine, hour 0 to hour 500? | Q-05 | Open — candidate: paintings as the collectible currency |
| 6 | How much of the world is authored, how much generated? | Q-06 | Leaning: arena authored, contents generated per session |

They live in Ishoo, in the plan `core-questions`. Each is deliberately broad — decompose it
into real issues when we reach it. The creature's own voice (replacing the placeholder) is
governed by DEC-04, and DEC-08 now settles what a creature is made of: painted 2-D frames.

---

## 6. INDEX

- Decisions: in Ishoo — `ishoo decision list` (DEC-01..08; DEC-06 superseded by DEC-08).
- Open questions: in Ishoo — `ishoo plan show core-questions` (Q-01..06).
- Retired prototypes and shelved iterations: [`../old/README.md`](../old/README.md)
- Original brief: [`brief.md`](brief.md)
- Concept: [`concept.md`](concept.md)
