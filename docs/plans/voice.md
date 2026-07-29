# PLAN: voice — what the creature actually sounds like

**Question:** what is our version of the call, and what else are we borrowing?

Governed by ADR-004. This plan exists so the list of placeholders lives somewhere other than
in someone's memory.

---

## The borrowed list (things that must be replaced before anything ships)

| Placeholder | Where | Status |
|---|---|---|
| "kweh" / "KWEHHH!!!!" as the dig response | `cry()` in `index.html` | must replace |
| The five-step escalation shape itself | design | **ours** — mechanism, not surface |
| Colour-change-as-progression conceit | design | needs its own treatment (VOICE-3) |

Add to this table the moment anything else is borrowed for testing.

---

## VOICE-1 — Design the call

- **Concrete change:** an original vocalisation with five legible steps, from a flat
  disinterested version to an unmistakable eruption. Made from a real recorded source, not a
  synth approximation, so it has character.
- **Main surface:** audio assets plus the grading in `cry()`.
- **Proof of done:** a new player reads all five steps correctly within one hunt, with nothing
  explained — the same bar the placeholder clears today.
- **Out of scope:** the rest of the audio direction.

## VOICE-2 — Written form on screen

- **Concrete change:** decide whether the call appears as text at all, and if so what the
  spelling is. The prototype floats "kweh?" above the creature and it works, but it may be a
  crutch that the audio alone could carry.
- **Proof of done:** an A/B on a phone, with sound off and sound on. Note that phones are
  frequently played muted — which is an argument for keeping text.
- **Out of scope:** localisation.

## VOICE-3 — Progression visible on the creature

- **Concrete change:** find our own answer to "you can tell how far in someone is from one
  screenshot of their creature," without copying the reference's colours.
- **Proof of done:** three stages of creature, recognisable side by side, none of which reads
  as the reference.
- **Depends on:** LOOK-5, because it depends on what a creature is made of.

## VOICE-4 — Music that drives the hunt

- **Concrete change:** real music for the hunt — starts on entry, builds, goes wild on a big
  find, silence outside hunts so entering means something.
- **Main surface:** replaces the procedural synth loop currently in the prototype.
- **Proof of done:** the music makes the last twenty seconds of a hunt feel worse (in the
  good way).
- **Out of scope:** a full soundtrack.
