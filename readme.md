# PACKHOUSE

A small packing-floor puzzle. One gesture, four rules, and a floor that never dead-ends.

**Play:** open `index.html` in any browser. Desktop or phone. No install, no build, no server.

---

## The rule, in one sentence

Press a group of touching, matching produce; the packed item settles in the **column you pressed**, and if it lands touching another match it packs again.

## Controls

| Do this | Get this |
| :--- | :--- |
| **Press and hold** a piece | The plan: its group, the exact landing cell, what it will chain with, the score |
| **Release** on the same piece | Pack it |
| **Drag away** before releasing | Cancel |
| **Drag onto a neighbour** | Crane swap (costs a load, only within the crane's reach) |
| **Press a truck** | Send it out — it collects every piece of its crop |
| **Tap an order** | Swap it for a different one (once per shift) |

## The ladder

produce → basket → crate → truck. Five or more at once packs a **bulk order** and skips a size. Two trucks side by side leave together and clear the entire floor.

## Crops

Before each shift you choose which crops turn up. Each bends exactly one rule:

- **Redland Apples** — nothing. Utterly predictable.
- **Sunfield Oranges** — arrive in pairs.
- **Stone Pears** — pear crates sink to the floor of their column.
- **Frost Berries** — berry baskets hang in mid air; nothing falls past them.
- **Twin Dragonfruit** — connect diagonally, but never bulk-pack.
- **Cider Lemons** — a bulk order leaves one lemon behind.

They combine. Frost + Stone is a vertical-control kit. Dragonfruit + Oranges sprawls.

## Stamps

How a package was made leaves a mark, and orders ask for marks. There is always more than one route to the same order.

- **FRESH** — packed as part of a chain
- **BUMPER** — packed from five or more
- **HANDLED** — the crane touched something that went in
- **DEEP** — settled in the bottom two rows

Stamps are inherited. A crate made from two handled baskets is handled.

## Setups

A move that makes no chain but leaves one ready is a **setup**. The floor says LINED UP. Cash setups in on later turns and they pay you crane loads.

## Gear

After every shift you take one item from the locker. Three slots, one item each, swap them any time from KIT & CROPS on the title screen.

---

## Design notes

- No move limit, no fail state, no energy. The floor guarantees at least one chain is always available and repairs itself if it ever runs dry.
- Difficulty widens rather than steepens: later shifts add crops, gear and order types, not a higher bar.
- Three layers that never touch: **crops** bend the floor's physics, **gear** bends the crane's vocabulary, **stamps** are read-only labels that change no rule at all.

Progress saves to local storage. START OVER on the title screen wipes it.
