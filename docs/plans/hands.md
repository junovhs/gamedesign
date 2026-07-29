# PLAN: hands — how the player moves and digs

**Question:** how does a thumb steer a creature under a lifted camera without fighting it?

Movement under the overhead hunt camera is awkward on a phone. This was true of the reference
game too, so there is no known-good answer to copy. It is the single biggest thing between the
prototype and something playable on a break. Governed by ADR-002 (the break test).

---

## HAND-1 — Spike: tap-to-go movement

**Urgency:** urgent — everything else in the hunt is tuned against controls that may change.

- **Concrete change:** add a second movement scheme behind a toggle: tap a point on the
  ground and the creature walks there and stops. Tap-and-hold near the creature digs. No
  stick on screen.
- **Main surface:** `index.html` — touch handling and `update()` movement.
- **Proof of done:** both schemes playable in the same build, switchable mid-session, tested
  on a phone for at least ten hunts each.
- **Out of scope:** removing the stick, pathfinding around obstacles, controller changes.
- **Note:** the stated worry is real — "I do like walking around and digging." Tap-to-go can
  win the hunt and still lose the exploration. Which is why this is a spike, not a swap.

## HAND-2 — Hybrid: tap to travel, stick to fuss

- **Concrete change:** if HAND-1 shows the tension is real, combine them — tap to cross the
  hunt area, stick (or drag) for the small adjustments right before a dig.
- **Main surface:** movement layer in `index.html`.
- **Proof of done:** a hunt can be played thumb-only without the camera fighting the player,
  and free roaming outside a hunt still feels like walking a creature around.
- **Out of scope:** the hunt camera itself (HAND-3).
- **Depends on:** HAND-1.

## HAND-3 — Make the hunt camera stop fighting the thumb

- **Concrete change:** try the three obvious fixes and pick by feel — (a) camera-relative
  input that re-bases as the camera swings, (b) a camera that locks to the hunt area instead
  of following the creature, (c) letting the creature turn faster than the camera does.
- **Main surface:** the camera block at the end of `update()`.
- **Proof of done:** a player can run a straight line across the hunt area on a phone without
  correcting mid-run.
- **Out of scope:** the drop-in transition, which works.

## HAND-4 — One-handed playability pass

- **Concrete change:** everything needed for a hunt must be reachable with one thumb on a
  phone held in one hand: dig, move, look, read the call.
- **Main surface:** the touch UI layout.
- **Proof of done:** a full hunt played one-handed, standing up, without dropping the phone.
- **Out of scope:** menus outside the hunt.
- **Why:** ADR-002's break test is one-handed by definition.

## HAND-5 — Controller parity

- **Concrete change:** gamepad support with the same verbs, tuned for the sit-down session.
- **Main surface:** input layer.
- **Proof of done:** a hunt plays identically well on a controller, with no on-screen buttons.
- **Out of scope:** rebinding UI, haptics.
- **Depends on:** HAND-2.
