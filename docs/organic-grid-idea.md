# Stålberg grids for the chain board

Authored by the designer, 2026-07-31, pasted into `index.html` from work and moved here.
This is the source note for the organic-mesh board.

**Yes. I think *Grindstone* would work extremely well on a Stålberg-style grid.** It would still be grid-based; the grid would simply be an **irregular graph rather than a rectangular lattice**.

At a systems level, *Grindstone* is already basically:

* each tile = a node;
* neighboring tiles = connections between nodes;
* a chain = a path through connected nodes of the same color.

None of that fundamentally requires straight rows or square cells.

## The important distinction

There are two ways to do it:

### Merely distort the existing square board

Keep exactly the same underlying neighbors, but move the tile centers and bend the cell boundaries.

```text
Regular appearance       Irregular appearance
same topology      →      same topology
```

This would preserve *Grindstone* almost perfectly. It would feel organic, but the geometry would mainly be visual.

### Use a true irregular Stålberg topology

The Townscaper-style technique creates a mesh from triangles and quadrilaterals, subdivides it and relaxes the vertices into an organic-looking grid. That can produce curved flows and much less obvious rows and columns. ([andersource][1])

Here, the actual neighbor relationships could vary:

```text
        A
      /   \
     B — C — D
     | \ |   |
     E — F — G
```

Now the shape of the board becomes mechanically meaningful. You can create:

* bottlenecks;
* circular routes;
* pockets and peninsulas;
* highly connected “junction” cells;
* isolated regions opened by keys or grindstones;
* boards shaped like caverns, creatures or terrain.

That would make individual levels considerably more distinctive.

## The main problem: *Grindstone* has diagonal adjacency

On its square board, *Grindstone* lets chains travel horizontally, vertically and diagonally, giving an ordinary interior tile up to eight possible neighbors. ([Ladies Gamers][2])

On a Stålberg grid, you must explicitly decide what “adjacent” means.

**Shared-edge only**

```text
┌─────┐
│  A  │── B is adjacent
└─────┘
```

This is visually clear, but most cells may have only around four exits. Chains would be more constrained and the game would feel closer to navigating corridors.

**Shared-edge or shared-corner**

This more closely reproduces *Grindstone’s* eight-direction movement, but irregular corners can become ambiguous. Two cells touching at a tiny point may not look obviously connected.

My recommendation is to allow both, but render the underlying connection clearly while the player drags:

* eligible neighbors brighten;
* a faint line connects cell centers;
* invalid cells dim;
* the chain snaps decisively from center to center.

The player should never have to guess whether two shapes count as adjacent.

## What would need redesigning

The chain mechanic itself needs almost no conceptual change. The surrounding systems do.

**Spawning and gravity:** A rectangular board naturally has columns and a downward direction. An organic grid does not. You would need a flow field—perhaps enemies enter from the upper boundary and travel along predefined graph connections toward empty cells.

**Line-based attacks:** Anything currently described as attacking a row, column or diagonal would need to become “follow this directional lane,” “attack all graph neighbors,” or “attack within two steps.”

**Level generation:** You could no longer balance levels using coordinates alone. You would evaluate connectivity, graph distance, bottlenecks, color clusters and reachable chain lengths.

**Cell size:** Stålberg cells can differ visually in area. Large cells must not accidentally appear more important or become much easier to select unless that is intentional.

## The version I would make

I would use a **true irregular grid**, not just warp a square one, but constrain it carefully:

* roughly 45–55 playable cells;
* most cells have six to eight selectable neighbors;
* very few unusually connected cells;
* visible connection feedback during chaining;
* an intentional entrance-to-exit flow;
* occasional narrow regions where geometry becomes part of the puzzle.

That would preserve the long, fluid chain-making pleasure while adding something the original *Grindstone* barely uses: **board topology as level design**.

The result could feel like *Grindstone* taking place across an organic cave network rather than on a spreadsheet. The mechanic would survive; it would probably become deeper.

[1]: https://andersource.dev/2020/11/06/organic-grid.html "Generating an organic grid | andersource"
[2]: https://ladiesgamers.com/grindstone-review-nintendo-switch/?utm_source=chatgpt.com "Grindstone Review (Nintendo Switch) - LadiesGamers"
