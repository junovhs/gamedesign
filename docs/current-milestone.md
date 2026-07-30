# M0 — THE PUZZLE IS THE GAME

_The only planning document that is read regularly. Everything else in `docs/` is reference._

---

## PURPOSE

> Prove that a small set of structural rules can produce many distinct, readable and satisfying
> problems on a phone.

The board is where the game lives. Roughly **80% of playtime belongs inside structural boards**
and 20% in home, inventory, residents, camps, dialogue, crafting and travel. Above ~90% the
surrounding world is decorative; below ~70% it is no longer the collapse-puzzle game.

So the board is proved first. Not a shallow version of every RPG system — a rich, representative
puzzle laboratory containing the smallest set of mechanics that can show whether the central play
is actually deep.

**Boards are handcrafted for the whole of M0.** A generator would hide whether the design itself
is good: a bad result reads as a bad seed. Deliberate arrangements are needed to test specific
ideas.

Governed by **DEC-19**. Not started until M0 answers: the 500-hour spine, the depth-band content
ladder, camps, the wiki site, the art importer, crafting, clothing, shops, Rust. Every document
about them is kept. None of them expands.

---

## THE MECHANIC LIST

Twelve categories, one representative each. Enough breadth to test the promise; no more.

| Category                       | Representative                                        | Issue |
| ------------------------------ | ----------------------------------------------------- | ----- |
| Structural removal             | Pickaxe                                               | LAB-01 |
| Gravity                        | Unsupported rock collapses                            | LAB-01 |
| Player relationship to gravity | Ride versus burial                                    | LAB-04 |
| Loose material                 | Dirt                                                  | LAB-04 |
| Information                    | Exact consequence preview                             | LAB-03 |
| Persistent object use          | Visible inventory item that can be dropped and used   | LAB-05 |
| Deliberate support             | Placeable beam                                        | LAB-06 |
| Reversed force                 | Balloon                                               | LAB-07 |
| Environmental transformation   | Pipe releasing water                                  | LAB-08 |
| Fragile objective              | Multi-cell fossil                                     | LAB-09 |
| Active entity                  | Worm that removes one cell after each action          | LAB-10 |
| Area destruction               | TNT                                                   | LAB-11 |

Twenty ores, six regions, five residents and a complete economy are not needed to find out
whether the puzzle system is rich. Representative mechanics that combine are.

**Q-03 freezes this list** — each representative's rule, cost, preview contract and one named
combination — before any of it is built.

---

## THE TWELVE BOARDS

Built in this order. Authored by hand in the LAB-02 board format.

| Board | What it proves                                            |
| ----: | --------------------------------------------------------- |
|     1 | Cutting support causes a predictable collapse             |
|     2 | The player can intentionally ride a mass                  |
|     3 | Positioning incorrectly causes burial                     |
|     4 | Loose dirt changes the result after rock settles          |
|     5 | A beam preserves part of a formation while the rest falls |
|     6 | A balloon lifts an object or mass upward                  |
|     7 | Water released from a pipe changes terrain indirectly     |
|     8 | A fossil must be exposed without being crushed            |
|     9 | A worm changes the board after each committed action      |
|    10 | TNT solves a route while threatening the objective        |
|    11 | Three previously introduced mechanics interact            |
|    12 | A capstone allowing several genuinely different solutions |

Boards 1–9 teach one concept at a time, without a tutorial screen.

**Boards 10–12 are the actual test.** They decide whether the concepts produce combinatorial
depth. If the mechanics are only interesting in isolation, the game will not support hundreds of
hours — and that is worth knowing before the world is built on top of them.

---

## THE ISSUES

| Issue | Title | Blocked by |
| ----- | ----- | ---------- |
| **DOCS-03** | Write `docs/current-milestone.md` and give every other doc exactly one job | — |
| **Q-03**  | What is the complete verb list for the M0 puzzle laboratory? | — |
| **LAB-01** | Define the board-state and action-resolution contract | Q-03 |
| **LAB-02** | Build the laboratory: handcrafted board format, level select, instant restart | LAB-01 |
| **LAB-03** | Make the consequence preview match the committed result exactly | LAB-01 |
| **LAB-04** | Finalise riding, falling, landing and burial | LAB-01 |
| **LAB-05** | Build the persistent inventory hotbar: select, use, drop, swap | LAB-03, LAB-04 |
| **LAB-06** | Implement placeable structural beams | LAB-05 |
| **LAB-07** | Implement balloons and upward movement | LAB-05 |
| **LAB-08** | Implement the pipe and water interaction | LAB-03, LAB-04 |
| **LAB-09** | Implement rigid multi-cell fragile objects: the fossil | LAB-03, LAB-04 |
| **LAB-10** | Implement one turn-driven creature: the worm | LAB-03, LAB-04 |
| **LAB-11** | Implement TNT and area-force consequences | LAB-05, LAB-09 |
| **LAB-12** | Author and playtest the twelve M0 boards | LAB-02, 06, 07, 08, 10, 11 |
| **Q-04**  | Does the M0 board system have combinatorial depth? Answer it in writing. | LAB-12 |

Ishoo is authoritative. This table is the map; `ishoo_show <id>` is the territory.

Do not break these into forty sub-issues until one is actively being implemented.

**Parked, not lost:** Q-05 (the 500-hour progression spine), Q-06 (authored versus generated),
Q-17 (depth-band content), Q-18 (structure above one shaft, and what a reset earns), TOOL-01 (the
pixel-art importer). Q-06 waits because a generator cannot be designed intelligently before it is
known what a good authored board looks like. Q-17 waits because content cannot rescue a weak
puzzle system. TOOL-01 waits because final art cannot answer whether the rules are deep.

---

## COMPLETION CRITERIA

M0 is done when these ten statements have been answered in writing, each with the board number,
action and observed result that produced the answer. **Q-04 is that answer.** A NO is a finding,
not a failure — it gets recorded and filed.

1. The preview never lies about the immediate result.
2. Riding and burial create intentional positioning decisions.
3. At least four boards have multiple credible solutions.
4. Combining mechanics produces consequences that are understandable but not obvious.
5. The fossil creates genuine preservation decisions.
6. Balloons and beams create new solution spaces rather than acting as keys for predefined locks.
7. Replaying a board with a different plan is enjoyable.
8. A thirty-minute session of boards remains engaging without shops, story or progression
   carrying it.
9. Fifty more boards are imaginable from these rules without immediately needing twenty new
   mechanics.
10. The designer personally keeps thinking about alternative solutions after closing the game.

---

## WHAT COMES AFTER

If M0 succeeds, the next milestone proves the 80/20 structure — one complete world slice:

```text
Backyard
→ 12-board descent
→ one lateral room
→ one resident
→ one camp
→ return home
→ place the recovered fossil in the yard
```

Not before.

---

## THE OTHER DOCUMENTS

Each has exactly one job.

| Document                                                     | Job                                             |
| ------------------------------------------------------------ | ----------------------------------------------- |
| [`design.md`](design.md)                                     | What the game is                                |
| [`game-system-plan.md`](game-system-plan.md)                 | The larger planned system space                 |
| [`north-star-catalogue.md`](north-star-catalogue.md)         | What the image contains                         |
| [`north-star.png`](north-star.png)                           | The visual and tonal reference of record        |
| [`wiki-idea.md`](wiki-idea.md)                               | How the future reference system will work       |
| Ishoo                                                        | Decisions, open questions and current milestone |
| Ishoo issues                                                 | Work being executed now                         |
