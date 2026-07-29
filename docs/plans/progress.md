# PLAN: progress — what the player keeps

**Question:** what does three minutes of play leave behind, and what does an evening build?

Governed by ADR-002. Everything here must bank instantly and survive failure.

---

## PROG-1 — Abilities that change the map you already know

**Urgency:** important.

- **Concrete change:** implement the first ability — swimming — as an always-on change to the
  creature, visible on its body.
- **Main surface:** movement, creature drawing, a small persistence layer.
- **Proof of done:** the brief's own test — on gaining it, the player immediately remembers
  three places they could not reach.
- **Out of scope:** an ability menu. There is never a loadout screen with more than one
  choice on it.

## PROG-2 — Persistence that survives closing the tab mid-hunt

- **Concrete change:** continuous local save. Permanent things (abilities, tools, home, places
  reached, collections) persist; the current trip's loose haul does not.
- **Main surface:** a save layer in `index.html`, later the engine equivalent.
- **Proof of done:** kill the app mid-dig, reopen, and nothing permanent is lost.
- **Out of scope:** cloud saves, accounts.
- **Why:** ADR-002 — a three-minute player may be interrupted by the end of their break.

## PROG-3 — Home that grows from what you dug up

- **Concrete change:** one place that visibly changes as finds come in. A repaired bridge, a
  shelf that fills, a garden. No workers, no timers, no research, no second currency.
- **Main surface:** a home area plus a table from find to visible change.
- **Proof of done:** a screenshot of home tells you roughly how far in the player is.
- **Out of scope:** management systems of any kind. This is the line the brief draws hardest.
- **Note on base building:** the appetite for base building is real and the anti-goal list is
  also real. They are compatible in exactly one way — building that is *placement and display*
  of things you found, not production. Anything with a rate of production fails ADR-002's
  break test, because rates reward long sessions and scheduled returns.

## PROG-4 — The trip: three stops, escalating, bank at the end

- **Concrete change:** the Freelancer run structure — pick a chain of stops, stakes escalate,
  loot banks at the end, quitting early is always allowed.
- **Main surface:** a run controller wrapping the hunt.
- **Proof of done:** a playtester says "one more trip."
- **Out of scope:** rivals (they come with the trip but are their own plan).
- **Tension to watch:** a three-stop trip may exceed three minutes. If it does, the trip must
  be resumable or the stops must shrink. ADR-002 wins that argument.

## PROG-5 — Rivals

- **Concrete change:** one rival with a visible routine and at least three ways to remove
  them: stealth, distraction, environment.
- **Proof of done:** the area is more fun with them in it than without. If not, cut them.
- **Out of scope:** anything lethal. Nobody dies in this game.
- **Open question for the designer:** how much of a bastard is the player? Gentle mischief or
  full slapstick? It changes the whole tone and it is still unanswered.
