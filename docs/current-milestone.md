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

**Frozen by Q-03.** Twelve categories, one representative each. Enough breadth to test the
promise; no more. Twenty ores, six regions, five residents and a complete economy are not needed
to find out whether the puzzle system is rich — representative mechanics that combine are.

Nothing outside this table is built during M0. Everything outside it is ruled in
[RULINGS](#rulings-on-every-other-verb) below.

---

**1 · STRUCTURAL REMOVAL — the pickaxe** · LAB-01

- **Rule:** one swing removes up to six orthogonally-connected cells of the same material,
  breadth-first from the tapped cell, within reach of where the player stands.
- **Cost:** one pick from the board's budget. The six-cell cap is the design: a big seam is
  several decisions instead of one free room-clear, and *where* in a mass you swing is a choice.
- **Preview:** the exact cells to be removed, outlined, plus the full collapse that follows.
- **Combines with:** the fossil (LAB-09) — the cluster cap is precisely why a fossil cannot be
  freed in one tap, so exposure order becomes the puzzle.

**2 · GRAVITY — unsupported rock collapses** · LAB-01

- **Rule:** structural material is held by orthogonal connection to either side wall, or to an
  anchor. Cut a mass free of both and the whole mass falls, one row per step, until it rests.
- **Cost:** none — it is a consequence, not an action. That is what makes it the core verb.
- **Preview:** every mass that loses support, and the row each one comes to rest on.
- **Combines with:** the beam (LAB-06) — a beam is nothing but an anchor, so it is defined
  entirely in terms of this rule.

**3 · PLAYER RELATIONSHIP TO GRAVITY — ride versus burial** · LAB-04

- **Rule:** standing on top of a mass that loses support means riding it down and surviving.
  Standing beneath it means burial. One column decides which.
- **Cost:** a ride is free and is the cheapest way down. Burial costs a dig-out.
- **Preview:** ride, struck, or buried — stated in words before the commit, not inferred.
- **Combines with:** the balloon (LAB-07) — riding upward is this same rule inverted, which is
  why the balloon needs no new player rule of its own.

**4 · LOOSE MATERIAL — dirt** · LAB-04

- **Rule:** loose material is held only by the tile directly beneath it. It has no lateral
  support at all, so it cannot hold a ceiling and it slumps to fill what opens under it.
- **Cost:** none. Its value is that it makes the board resolve in two stages — rock settles,
  then dirt slumps into the result — so the same cut reads differently with dirt present.
- **Preview:** the settled state after slumping, not the state immediately after the cut.
- **Combines with:** water (LAB-08) — water is defined as the thing that turns held material
  into slumping material, so this rule is what gives water its consequence.

**5 · INFORMATION — the exact consequence preview** · LAB-03

- **Rule:** before a consequential action commits, the game resolves it against a cloned board
  and shows the immediate result to its settled state. Preview and commit share one code path,
  so they cannot drift.
- **Cost:** free and always on. It is not an upgrade, a lamp, or a resource.
- **Preview:** it *is* the preview. It promises removed cells, every mass that loses support and
  where it lands, the player's ride/struck/buried outcome, objects pushed or destroyed, and the
  item consumed.
- **Combines with:** the worm (LAB-10) — the worm is where the promise deliberately ends, and
  that boundary is stated on screen rather than discovered by losing.

**6 · PERSISTENT OBJECT USE — the hotbar item** · LAB-05

- **Rule:** carried things occupy visible slots that stay on screen during play. A selected item
  is used on a tapped cell, or dropped into the board, where it becomes a real object subject to
  gravity and support and can be picked up again.
- **Cost:** a slot. Slots are the carry constraint; there is no fullness bar. Consumables are
  spent on use.
- **Preview:** using an item previews exactly like a cut, and names which limited item is
  consumed before it is spent.
- **Combines with:** TNT (LAB-11) — placement is the whole decision, so TNT is only a verb once
  the player can hold one and choose where it goes.

**7 · DELIBERATE SUPPORT — the placeable beam** · LAB-06

- **Rule:** placed into an empty cell, a beam is an anchor. Structural material orthogonally
  connected to it is supported, so part of a formation survives while the rest falls.
- **Cost:** one beam from a slot. Recovery terms are LAB-06's to settle.
- **Preview:** exactly which cells the beam will hold and which will still fall — the split,
  before the cut that tests it.
- **Combines with:** the pickaxe (LAB-01) — a beam is only interesting because it changes what a
  subsequent cut does, never on its own.

**8 · REVERSED FORCE — the balloon** · LAB-07

- **Rule:** attached to a mass or object, it rises instead of falling, resolving through the same
  fixed-point settle as a collapse, until it is obstructed.
- **Cost:** one balloon. It can be popped, and what it was holding drops the instant it is.
- **Preview:** the destination, plus any secondary collapse the rise causes on the way.
- **Combines with:** the fossil (LAB-09) — lifting a fragile object out is the alternative to
  lowering it, and the two are different solutions to the same board.

**9 · ENVIRONMENTAL TRANSFORMATION — pipe releasing water** · LAB-08

- **Rule:** breaking a pipe releases water, which flows down and levels sideways to a fixed point
  inside the same committed action, converting material it reaches.
- **Cost:** one pick to break the pipe — and it is irreversible, which is the point. This is the
  verb whose real consequence is something the board does, not something the pick does.
- **Preview:** the flood extent and every material change, to the settled state.
- **Combines with:** dirt (LAB-04) — the transformation is only legible because loose material
  already behaves visibly differently from held material.

**10 · FRAGILE OBJECTIVE — the multi-cell fossil** · LAB-09

- **Rule:** a rigid body occupying several cells, moving as one. It never moves a cell at a time.
  It breaks if dropped beyond a stated distance, crushed, or caught in a blast.
- **Cost:** carelessness destroys it. It is the objective, so the cost of failure is the board.
- **Preview:** destruction is shown before the tap that would cause it — this is the single most
  load-bearing case of the preview promise.
- **Combines with:** the beam (LAB-06) and the balloon (LAB-07) — hold it up, or lift it out.

**11 · ACTIVE ENTITY — the worm** · LAB-10

- **Rule:** strictly after each committed action resolves, the worm removes exactly one cell, by
  a rule the player can learn by watching rather than by being told.
- **Cost:** it spends the player's *time* — every action the player takes costs a cell of board.
  It must be blockable, trappable or redirectable, or it is an obstacle rather than a puzzle.
- **Preview:** the worm's next move is **not** previewed. This is the stated boundary of the
  promise, and the game says so the first time a worm board is entered.
- **Combines with:** all of them — it is the clock that makes an otherwise static board urgent.

**12 · AREA DESTRUCTION — TNT** · LAB-11

- **Rule:** removes a broad area in one commit and applies force to what remains.
- **Cost:** one TNT, and it threatens the objective as much as the obstacle. A board where TNT is
  strictly good is a board where TNT is not a decision.
- **Preview:** the full chain — removed area, every resulting collapse, the player's outcome, and
  any object destroyed.
- **Combines with:** the fossil (LAB-09) — the same blast that opens the route is the one that
  can shatter the prize.

---

## RULINGS ON EVERY OTHER VERB

Every operation in `design.md` §6, every item in §10, and every verb in the current build, ruled.
**M0** is in the list above. **LATER** is recorded and blocked behind Q-04. **CUT** is not coming
back without a new argument.

### design.md §6 — operations

| Operation | Ruling | Reason |
| --------- | ------ | ------ |
| Remove    | **M0** | The pickaxe. |
| Lift      | **M0** | The balloon. |
| Anchor    | **M0** | The beam. |
| Transform | **M0** | Water. |
| Reveal    | **M0** | The preview *is* the reveal, and it is free. Lamps and scanners are LATER. |
| Push      | LATER  | A second force verb before the first one is proven adds cost, not evidence. |
| Pull      | LATER  | Same rule as push, mirrored; nothing new is learned by having both. |
| Tether    | LATER  | Needs a rope model and a player-attachment model, neither of which M0 tests. |
| Trigger   | LATER  | Remote activation needs machinery networks, which DEC-19 parks. |
| Preserve  | LATER  | The fossil tests preservation *as an objective*; a preserve tool would remove the tension it exists to create. |

### design.md §10 — equipment

| Item | Ruling | Reason |
| ---- | ------ | ------ |
| Pickaxe          | **M0** | The removal representative. |
| Support beam     | **M0** | The anchor representative. |
| Balloon          | **M0** | The reversed-force representative. |
| TNT              | **M0** | The area-destruction representative. |
| Chisel           | LATER | One exact cell is a parameter of the pickaxe, not a new idea. |
| Drill            | LATER | A narrow line is another removal shape; same category, no new evidence. |
| Sledgehammer     | LATER | Push, deferred with push. |
| Rope             | LATER | Tether, deferred with tether. |
| Jack             | LATER | Raises a mass one cell — the balloon already represents lift. |
| Magnet           | LATER | Pull, deferred with pull, and needs a metal-material model. |
| Foam             | LATER | Temporary support — the beam already represents anchor. |
| Remote detonator | LATER | Sequenced explosions are a second-order TNT problem; prove the first order. |

Clothing (§10) and perks (§10) are **LATER** in full: DEC-19 parks equipment, clothing and
progression, and none of them can make a shallow board deep.

### Verbs in the current build

| In the build today | Ruling | Reason |
| ------------------ | ------ | ------ |
| Walk to a standable cell in reach | **M0** | Positioning is half of ride-versus-burial. |
| Tap a tile to break a cluster     | **M0** | This is the pickaxe. |
| Ride a collapse down              | **M0** | Category 3. |
| Burst a pipe                      | **M0** | Becomes LAB-08's water. |
| Pick up a find                    | **M0**, re-formed | A find becomes a hotbar item (LAB-05), not a number silently added to a bag. |
| Place a beam                      | **M0**, re-formed | Becomes a hotbar item (LAB-06), not a purchased counter. |
| The bag-capacity bar              | **CUT** | DEC-18. Replaced by slots. |
| The landing panel every 3rd screen| **CUT** | DEC-17. Camps are rare; landings are not a thing. |
| The lift                          | **CUT** from M0 | Descent infrastructure; the laboratory is a level select. |
| The shop                          | **CUT** from M0 | DEC-19 parks shops. M0 boards are authored with what they need. |
| The wipe / reset system           | **CUT** from M0 | LAB-02's instant restart replaces it inside the laboratory. |
| Ore values and selling            | **CUT** from M0 | Q-04 criterion 8 requires the boards to hold up with no economy carrying them. |
| Tool hardness tiers               | LATER | Gating material behind an upgrade is progression, which DEC-19 parks. |
| Roots that regrow                 | LATER | A second entity. The worm is the one representative. |
| Living / breathing material       | LATER | Same — and it is tone, which M0 is not testing. |
| Depth bands and biomes            | LATER | Q-17. Content cannot rescue a weak puzzle system. |

### Materials M0 needs

`DIRT` (loose), `STONE` (structural), `BEAM` (anchor), `PIPE`, `WATER`, plus the fossil, the
worm, the balloon and the TNT as objects rather than materials. Every other entry in the current
`MAT` table — copper, iron, slate, silver, basalt, gold, cutlery, tile, root, meat — stays in the
file as terrain variety but carries **no M0 behaviour and no value**. Their hardness, ore and
value fields are inert for the duration.

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
