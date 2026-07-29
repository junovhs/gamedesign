# THE LITTLE DIGGER — DOCS

Play it: <https://junovhs.github.io/gamedesign/> · source: [`../index.html`](../index.html)

**[direction.md](direction.md)** — where the project is, what it is trying to be, and the
correction about what the prototype's renderer actually does.

Decisions and issues live in **Ishoo**, not in this folder. Ask an agent for `ishoo status`,
or run:

```
ishoo decision list      # the ADRs
ishoo list               # the open questions
ishoo plan show core-questions
```

## Decisions

| id | title | status |
|---|---|---|
| DEC-01 | The Little Digger is the project | ACCEPTED |
| DEC-02 | Three minutes to pick up, five hundred hours deep | ACCEPTED |
| DEC-03 | The dig is the signal; the creature's voice is the interface | ACCEPTED |
| DEC-04 | The placeholder voice must not ship | ACCEPTED |
| DEC-05 | The browser prototype is a design instrument, not the codebase | ACCEPTED |
| DEC-06 | Art direction moves toward volume (voxel or clay) | **PROPOSED** — not binding |

## Plan: core-questions

Six questions, deliberately broad. Each gets decomposed into real issues when we reach it.

| id | question |
|---|---|
| Q-01 | What render style do we want — voxel, clay, or lit boxes? |
| Q-02 | How does the player move and dig on a phone? |
| Q-03 | What are all the v1 mechanics — the complete verb list? |
| Q-04 | What makes digging deep enough for hundreds of hours without becoming grind? |
| Q-05 | What is the progression spine from hour zero to hour five hundred? |
| Q-06 | How much of the world is authored and how much is generated? |

Q-01 and Q-02 are urgent: they are underneath everything else, and tuning anything before
they settle is wasted work.

## Background

- [../little-digger-handoff.md](../little-digger-handoff.md) — the original build brief.
- [../pivot-concept.md](../pivot-concept.md) — the concept document.
- [../spencer_game_design_philosophy.md](../spencer_game_design_philosophy.md)
