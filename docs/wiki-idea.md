**Yes. Build the wiki as you build the game.** For DOWNSHAFT, it will be genuinely useful development infrastructure, not just player documentation.

Your planned game has materials, physical properties, tools, clothing, perks, creatures, residents, camps, regions, finds, recipes, collections, machines, and persistent world rules. That is exactly the kind of content-rich game where facts begin contradicting each other unless there is a searchable catalogue.

The wiki should answer:

> **What exists, what does it do, and where does it belong?**

Your `design.md` answers a different question:

> **Why is the game designed this way?**

Keep those roles separate.

## Start it inside the repository

```text
docs/
├── design.md
├── game-systems-plan.md
├── north-star-catalogue.md
└── wiki/
    ├── README.md
    ├── materials/
    ├── items/
    ├── tools/
    ├── clothing/
    ├── perks/
    ├── creatures/
    ├── residents/
    ├── regions/
    ├── camps/
    ├── finds/
    ├── machines/
    └── mechanics/
```

Do not build a polished public website yet. Build the **content database in Markdown**. It can later be published as a website without rewriting the information.

## Give every concept a stable ID

Names may change. IDs should not.

```text
material.copper
tool.chisel
item.balloon
creature.cow
resident.mole_proprietor
region.mushroom_cavern
mechanic.structural_support
```

These IDs can eventually correspond to Rust enums, save data, localization keys, test fixtures, and analytics.

For example:

```rust
enum MaterialId {
    Dirt,
    Stone,
    Copper,
    Iron,
    Ice,
    Root,
}
```

The wiki page would be `docs/wiki/materials/copper.md`, while the stable conceptual identity remains `material.copper`.

## Use a strict page template

```md
# Copper

| Field        | Value               |
| ------------ | ------------------- |
| ID           | `material.copper`   |
| Status       | Planned             |
| Category     | Structural resource |
| First region | Machinery           |
| Collectible  | Yes                 |
| Persistent   | Yes                 |

## Player-facing description

A conductive metal found in connected seams.

## Physical behavior

Copper conducts power through orthogonally connected copper cells and compatible machinery.

It is structurally stable while connected to a wall or anchor and falls normally when cut
free.

## Player uses

- Wiring
- Lamps
- Magnets
- Powered tools
- Machine repair

## Board interactions

- Completes electrical circuits
- Conducts hazards
- Can be pulled by magnets
- Becomes dangerous near exposed power

## Extraction considerations

Heavy seams may collapse as one mass. Powered copper should be disconnected before handling.

## Related concepts

- `mechanic.electricity`
- `tool.magnet`
- `machine.generator`
- `material.rubber`

## Implementation

- Prototype: not implemented
- Production type: `MaterialId::Copper`

## Open questions

- Does electricity travel through diagonal connections?
- Can copper be melted inside a board?
```

## Track status explicitly

Every page should say one of:

| Status          | Meaning                                          |
| --------------- | ------------------------------------------------ |
| **Idea**        | Recorded, not accepted                           |
| **Planned**     | Accepted as part of the design                   |
| **Prototype**   | Exists experimentally                            |
| **Implemented** | Exists in the current game                       |
| **Balanced**    | Values have received deliberate tuning           |
| **Shipped**     | Included in a released version                   |
| **Cut**         | Intentionally removed, with the reason preserved |

This prevents a speculative balloon idea from being mistaken for a committed production requirement.

## The wiki should become the content bible

Use it during development for:

- Checking whether two tools perform the same operation
- Finding every object affected by electricity
- Seeing which region introduces a mechanic
- Preventing every resource from becoming generic crafting currency
- Tracking where residents and finds appear
- Recording how an item behaves when dropped
- Defining terminology consistently
- Giving AI coding agents precise context
- Preparing tests and save migrations
- Eventually producing player documentation

It will be especially valuable when you ask an AI to implement something. Instead of saying “add copper,” you can point it to `material.copper`, where the behavior, edge cases, related systems, and implementation status are already defined.

## Do not duplicate numeric truth

The wiki may explain that a chisel has limited durability. It should not become the authoritative location for the exact durability value once that value lives in game data.

For exact numbers:

> **Game data is authoritative; the wiki explains the data.**

Later, tables containing prices, damage, stack sizes, weights, and recipe quantities should be generated from the same files the Rust game loads. Otherwise the wiki will drift.

Conceptually:

```text
game data
   ├── loaded by Rust
   ├── validated by tests
   └── used to generate wiki tables
```

## Build pages when concepts become real

Do not attempt to write a Stardew-sized wiki in advance.

Create or update a page whenever you:

- commit a mechanic;
- implement an item;
- introduce a material;
- add a resident;
- define a region;
- settle an important interaction;
- or discover an edge case during testing.

The requirement should be:

> A gameplay concept is not finished until its wiki entry reflects its actual behavior.

Your new systems table is already the index for the first wave of pages. The North Star catalogue says what the image contains. `design.md` says what the game is. The wiki will say exactly how every part of that game works.
