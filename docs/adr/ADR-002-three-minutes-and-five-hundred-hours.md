# ADR-002 — Three minutes to pick up, five hundred hours deep

**Status:** ACCEPTED — 2026-07-29
**Tags:** direction, scope, design-constraint

## Problem

"A big game" and "a game you can play on a break" usually pull in opposite directions.
Without stating the target shape, every future feature argument (session length, energy
systems, save structure, progression pacing) has to be re-litigated from scratch.

## Decision

The game targets **a three-minute pickup and a five-hundred-hour depth, in the same build,
with no separate modes**. One hunt is the atom of play: roughly two minutes, self-contained,
and it banks something permanent every time.

Depth comes from *knowing the world* — where things are, when they happen, how to plan a
route — not from grind, not from a content treadmill, and not from longer sessions.

## Rule

Any proposed feature must pass both tests:

1. **The break test.** Can a player open the game, gain something permanent, and close it,
   in three minutes, one-handed, on a phone? A feature that requires a longer session to be
   worth using fails.
2. **The evening test.** Does the feature get more interesting the more the player knows
   about the world? A feature that is equally interesting at hour 1 and hour 100 is content,
   not depth, and will not carry 500 hours.

Anything that fails test 1 is cut or restructured. Anything that fails test 2 is allowed but
does not count toward depth, and must be cheap.

## Alternatives rejected

- **Session-length rewards, daily logins, energy, timers to return for.** Rejected outright:
  they punish the three-minute player, who is the primary player.
- **A separate "quick mode."** Rejected: two modes means two balance problems and halves the
  meaning of every unlock.

## Consequences

- Progression must be granular enough that two minutes moves it visibly.
- No system may hold the player hostage mid-hunt (no unskippable sequences, no state that
  is lost by closing the app).
- Saves must be continuous and instant.

## Operational impact

Constrains ADR-003 (the dig must resolve fast), and every issue in `docs/plans/progress.md`.
