# PLAN: world — density, generation, and the map system

**Question:** how much of this world is authored, and how much is generated?

The brief calls for handcrafted areas dense with incidental things (the Freelancer
requirement). The 500-hour target and the appetite for procedural generation pull the other
way. These are not automatically in conflict, but the split has to be deliberate.

---

## WORLD-1 — Name the split: what is authored, what is generated

**Urgency:** important — it constrains the engine decision and the art pipeline.

- **Concrete change:** a written split. The working proposal to argue with: **landmarks and
  the shape of the land are authored** (because the map system depends on recognisable
  silhouettes) and **everything scattered between them is generated** (grass, rocks, small
  finds, hunt areas, the incidental density).
- **Main surface:** this document, then an ADR.
- **Proof of done:** an accepted ADR stating the split and its reasoning.
- **Out of scope:** implementing either half.
- **Why:** a procedurally generated landmark cannot be recognised from a painting, because
  nobody built a memory of it. That is the load-bearing constraint.

## WORLD-2 — Density pass on one area

- **Concrete change:** take the current field and fill it until a player can walk in any
  direction for fifteen seconds and find something worth stopping for.
- **Main surface:** the scenery and landmark tables in `index.html`.
- **Proof of done:** ten random walks, ten interesting stops.
- **Out of scope:** new mechanics — the interesting things may be purely visual for now.
- **Note:** the brief calls this the most commonly under-budgeted thing in games like this.

## WORLD-3 — Harder map pictures

- **Concrete change:** extend the map camera with the difficulty tiers from the brief —
  distant silhouettes at dusk, two features that only line up from one spot, places the
  player can see but cannot yet reach.
- **Main surface:** `makeMap()` in `index.html`.
- **Proof of done:** a set of ten maps sorted by how long they take to solve, with the hardest
  taking real thought and none being unfair.
- **Out of scope:** hint systems. There are none.

## WORLD-4 — Places that run on visible routines

- **Concrete change:** two or three simple visible routines in the field — the tide, an animal
  that visits when it rains, insects that gather over buried things at dusk.
- **Main surface:** a world-clock and a small routine table.
- **Proof of done:** a player can predict one routine after watching it once, and use it.
- **Out of scope:** naming any of it in the UI. Ever.
- **Why:** this is what makes knowing the world pay, which is the entire depth story
  (ADR-002, evening test).

## WORLD-5 — Second area, and travel between areas

- **Concrete change:** build the coast, and decide continuous-world versus separate-areas.
- **Proof of done:** an ADR on world topology, then the area.
- **Depends on:** WORLD-1, LOOK-5.
- **Note:** open question 2 in the original brief, still unanswered. Continuous supports the
  "I know where that is" feeling; separate is far cheaper.
