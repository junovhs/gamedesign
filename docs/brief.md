# THE LITTLE DIGGER — BUILD HANDOFF

*For whoever builds this next. Read all of it before writing code.*

---

## 0. THE HARD RULES

These come directly from the designer and override anything else in this document.

1. **Low cognitive load at any one moment.** The player should almost never be holding more than one question in their head. "Where is it?" or "How do I get up there?" — not both plus an inventory plus a hunger bar.
2. **No invented vocabulary.** Do not name systems. There is no "Expedition Protocol" or "Resonance Meter." There is a map, a whistle, a rope, your friend, a hole. If a thing needs a proper noun to be explained, it is designed wrong.
3. **Nothing should require study.** No codex, no tutorial wall, no mechanics the player must read about. Everything is taught by watching it happen once.
4. **Imply rather than state.** If the tide goes out in the evening, the player sees the tide go out. Nobody announces a tide system.
5. **The core action must be fun before any reward is attached.** If running around digging holes isn't enjoyable with the rewards switched off, stop and fix that first.

---

## 1. WHAT THE GAME IS

A third-person adventure about a small creature that can smell buried treasure.

You take it somewhere. Music starts, a clock starts. You run around reading its excitement, you dig, and you hope. Most holes have something small. Sometimes there's a map — and a map is a *picture* of a place, which sends you somewhere else in the world.

Finds make the creature more capable, which opens terrain you have already seen and could not reach. The world gets bigger, stranger, and prettier the further you get. It ends above the clouds.

Running alongside that: other treasure hunters want the same things you do, and getting them out of your way is half the fun.

---

## 2. THE TWO REFERENCES, TRANSLATED

The designer's two touchstones. Translate the *mechanism*, not the surface.

### Chocobo Hot and Cold (FF9)

What actually works there and must be preserved:

- You start plain and cute. Progress is **visible on the creature itself** — new colours, new shapes.
- The dig hunt is **short, musical, and frantic**. Urgency comes from a clock, not from danger.
- Finding something mid-hunt is a **rush**. Finding two big things in one hunt is a story you tell people.
- Rewards are **new places and new ways to move**, not statistics.
- It builds toward somewhere spectacular. The clouds. Meet the king.

### Hitman: Freelancer

What actually works there and must be preserved:

- One rich space with **enormous amounts of incidental stuff everywhere**. The feeling that you can go anywhere and find something interesting.
- Early confusion turning into **mastery through familiarity** — the joy is *knowing* where everything is and being able to plan.
- **Creative combinations** of the environment and your kit. Disguises, hiding, timing, being sneaky, being powerful.
- A **run structure** with escalating stakes across several stops.
- **Persistent unlocks that survive failure.** Dying costs you the trip, not the campaign. "I'm unlocking things that make the next one easier" is the addiction.

The synthesis: *Chocobo's hunt is the verb. Freelancer is the container it lives in.*

---

## 3. THE CREATURE

The emotional centre. Budget accordingly — this is where the charm lives.

- Cute, curious, clumsy, full of personality. Idles constantly: chases bugs, shakes off dirt, stares at distant things, naps badly.
- **Its treasure sense is communicated only through animation and sound.** No meter, no arrow, no number, ever.
  - Far: occasional uncertain chirp, wanders.
  - Nearer: ears up, orients, trots toward it.
  - Close: can't hold still, circles, whines.
  - On top of it: unmistakable eruption.
- The player must be able to read it in under a minute of play without being told anything.
- **Movement must feel good on its own.** Weight and momentum, leans into turns, skids on loose ground, braces before a dig, tumbles on a big landing, recovers fast. Test this with no treasure in the world at all.
- Abilities change its appearance visibly. A player should be able to tell how far someone is into the game from one screenshot of their creature.

---

## 4. THE HUNT (moment to moment)

The core loop. Get this right and the game exists.

- Triggered by entering a hunt area. **Music starts, a clock starts.** 90–120 seconds.
- The player runs around reading the creature and digs where they think it's strongest.
- **Digging costs time** (~1.5s per hole). This is what makes it a route problem instead of a search. Time is the only resource.
- A dig that misses is **not wasted** — it narrows things down. The creature's reaction after a miss should tell you roughly which way to go. Beginners follow the loudest signal and wander; good players triangulate off two or three holes and go straight there. *This skill gap must exist, and it must never be explained.*
- Ends when the clock runs out. You keep what you dug up.

**Target: a hunt should be replayable hundreds of times.** If it isn't fun on hunt #50 with rewards disabled, the design has failed and no amount of content fixes it.

### Variation by place, not by rules

Same verb everywhere; the surroundings change the problem.

- Beach: waves periodically cover part of the ground.
- Garden: you must not be seen digging.
- Cave: sound bounces, the signal is less precise.
- Something moving: the whole search area slowly shifts.
- Clouds: treasure drifts instead of staying put.

---

## 5. WHAT'S IN THE HOLES

Most holes: coins, food, junk, a tool, a piece of a collection, something funny.

**Tuning targets** (adjust by playtest, but these are the intended feelings):

| Outcome | Rough frequency | Feeling |
|---|---|---|
| Something small and useful | most holes | steady drip |
| Something notable | ~1 per hunt, guaranteed | the hunt was worth doing |
| A map | ~30% of hunts | *rush* |
| Two maps in one hunt | ~5% of hunts | **the story you tell people** |

The double-map jackpot is a deliberate design target, not an accident. Build the odds so it happens rarely enough to stay special and often enough that players chase it. When it happens, the game should lose its mind — music swell, the creature going berserk, the whole screen celebrating.

Add a quiet pity mechanism so a player never goes many hunts with nothing. Never expose it.

---

## 6. MAPS ARE PICTURES

The single most important idea in the game.

A map is an **image of a place**. A crooked tree beside a bridge. A tower during a storm. An island under a big moon. The player looks at it, thinks *"wait, I know where that is,"* and goes there.

No coordinates. No marker. No quest entry. The puzzle happens in the player's head.

### Generate them from the world

**Do not hand-draw these.** Put a camera in the actual game world at the target location, choose an angle, a time of day, and weather, render it, and run it through a painterly filter. The result is guaranteed accurate, automatically shows landmarks from unusual angles, and costs almost nothing per map.

Difficulty is then just camera choice:

- Easy: familiar landmark, clear daylight, straight-on, close.
- Medium: unusual angle, or a time of day the player rarely sees there.
- Hard: distant silhouette at dusk; two features that only line up from one spot; a place the player has seen but cannot yet reach.

This is what turns a finite authored reward into an endless one. It is the difference between a 25-hour game and a 500-hour game. **Prioritise it.**

---

## 7. RIVALS

This is where the Freelancer satisfaction comes from. Do not treat it as set dressing.

Other treasure hunters work the same areas. They have routines, they are looking for the same things, and they will get there first if you let them.

Getting rid of one should feel **powerful, creative, and funny** — the game is not about killing anything. Roll them down a hill in a barrel. Drop a beehive. Get them stuck in sticky sap. Feed the big animal so it sits on their dig site. Steal their shovel. Trigger something that clears the whole area at once.

Requirements:

- Multiple valid approaches to every rival: stealth, distraction, speed, environment, straight slapstick.
- Removal is **temporary and non-fatal**. They come back next visit. Nobody dies in this game.
- Being caught yourself is a problem, not an ending: thrown out of the area, lose time, drop loose treasure, have to escape.
- Disguises, hiding places, and timing should all be viable, because that combination is specifically what the designer loves.

---

## 8. THE RUN (Freelancer's shape)

Wraps the hunts and supplies the addiction.

- From home, the player picks a **trip**: a chain of 3–5 stops.
- Each stop is an area with a hunt, some rivals, and local conditions.
- **Stakes escalate along the chain.** Later stops have better odds of maps and more opposition.
- Loot is only banked **when the trip ends**. Quitting early is always allowed and always a real choice.
- Getting caught badly ends the trip. **You lose the trip's haul. You keep everything permanent.**

Permanent across all failure:

- Creature abilities
- Tools unlocked
- Home improvements
- Completed collections
- Places already reached, and everything you now know

That last line is the whole engine: *"even if I die it's not so bad, I'm still unlocking things that make the next one easier."*

---

## 9. PROGRESSION

### Abilities (the Chocobo colours)

A small number of big, obvious ones. **Always on — never selected from a menu.** Once it can swim, it swims. Each visibly changes the creature.

Swim → Climb → Move through plants → Glide → Fly.

Each one should make the player immediately remember three places they couldn't reach.

### Tools

You bring **one** on a trip. Each has several uses that the player discovers rather than reads.

Fruit (attracts, weighs, distracts, leaves a scent). Rope (connects two points). Something noisy. Something smoky. A light. A disguise. Something for opening old machines.

Never present a loadout screen with more than a single choice on it.

### Home

One place, returned to constantly, that **visibly grows** from what you find. A repaired bridge, a shop, a boat, a garden, a working machine, a tower. New characters move in. Collections appear physically on shelves.

**Not a management game.** No workers, no timers, no research, no second currency. Discoveries change the home automatically or through one obvious choice.

---

## 10. THE WORLD

Several large handcrafted areas, connected: **fields → coast → forest → mountains → deep water → strange moving places → floating islands → clouds.** It ends above the clouds, at the home of enormous ancient creatures related to your small one. The last ability. Everything connects.

Every area must be **dense with incidental interesting things** — this is the Freelancer requirement, and it is the most commonly under-budgeted thing in games like this. The player should feel they can walk anywhere and find something.

Every area shows the player things it does not explain: a chest under clear water, a cave up a cliff, a locked garden, a machine missing a part, an island drifting past, a signal coming from behind a wall, a door built for something enormous.

Places run on simple visible routines: a guard takes lunch, the tide goes out, an animal visits the river when it rains, a cart moves between floors, glowing insects gather over buried things. Nothing is ever named as a system.

---

## 11. ANTI-GOALS

Do not build any of these. They break rule #1.

- Crafting trees, skill trees, tech trees
- Hunger, thirst, temperature, stamina bars
- More than one currency
- Inventory management or weight limits
- A lore codex, journal, or collectible text
- Named mechanics shown in the UI
- Loadout screens with multiple simultaneous choices
- Anything requiring a tutorial longer than one sentence
- Permadeath or any failure that erases hours

---

## 12. ART AND AUDIO

- **3D, third person, pixel-art texturing.** Chunky, readable, saturated. Bright and whimsical — explicitly *not* brown, not gritty, not a mine.
- Every area needs a silhouette and a colour identity strong enough that a painted picture of it is recognisable. **The map system depends on this.** Art direction is load-bearing, not decoration.
- Juice: dirt sprays, dust, camera shake on landings, the creature's body follow-through, squash and stretch, sound with material character.
- Music drives the hunt. It starts, it builds, it goes wild on a big find. Silence outside hunts so the music entering means something.

---

## 13. BUILD ORDER

Each step answers one falsifiable question. **Do not proceed until the current question is answered yes.**

**Step 1 — Does moving feel good?**
One flat field. The creature. Run, jump, skid, dig animation. No treasure at all. *Is it fun to just run around?*

**Step 2 — Is the hunt fun?**
Add buried things, the creature's four-stage reaction, a 100-second clock, digs that cost time. Rewards are placeholder text. *Is hunt #20 still fun?*

**Step 3 — Does the picture work?**
Render a map image from a real spot in the field and hand it to the player. *Do they immediately want to go find it?* **This is the highest-risk step in the whole project — do it early, not late.**

**Step 4 — Is the rush real?**
Tune the find tables. Make the double-map moment. *Does the player make a noise out loud when it happens?*

**Step 5 — Does a rival make it better or worse?**
One rival with a routine, three ways to remove them. *Is the area more fun with them in it?*

**Step 6 — Does the run structure hook?**
Chain 3 stops, escalating, bank at the end, keep unlocks on failure. *Does the player say "one more trip"?*

**Step 7 — Does an ability transform the world?**
Add swimming. *Does the player immediately remember somewhere they couldn't go?*

Only after all seven: build the second area.

---

## 14. TECH

Recommendation: **Godot 4**. Free, good 3D, excellent for pixel-art-textured 3D, fast iteration, exports to PC and console. Render to a low internal resolution and upscale with nearest-neighbour so the pixel look is enforced by the pipeline rather than by hand.

For the map-picture system, use a second camera rendering to a texture, then a shader for the painted treatment. This is straightforward in Godot and is the reason to prefer a real engine over a browser prototype.

If instant in-browser playtesting matters more than shipping, Three.js can carry steps 1–4, but expect to port.

Prior prototypes in this repo (`deep.html`, `pov.html`) are a first-person voxel raycaster and are **not** the basis for this game. They are only useful as evidence that low-resolution rendering with a fixed palette reads convincingly as pixel art in 3D. Do not try to extend them.

---

## 15. OPEN DECISIONS

Not yet settled. Ask the designer rather than guessing.

1. **How much of a bastard is the player?** Rivals are non-lethal, but the tone can run from gentle mischief to full slapstick cruelty. Affects everything.
2. **Is the world one continuous space or separate areas you travel between?** Continuous supports the "I know where that is" feeling better; separate is far cheaper.
3. **Does the creature ever get hurt?** There is currently no health of any kind. Consider keeping it that way — the clock and the rivals may be enough pressure.
4. **Story weight.** The doc implies a light one ending in the clouds. Confirm whether there are characters and dialogue or whether it stays wordless.
5. **How many areas ship in v1?** The full list is a multi-year scope. A vertical slice is two areas plus home.

---

## 16. THE ONE-LINE TEST

If at any point you cannot explain what the player is doing right now in a single plain sentence with no invented words, you have drifted.

*A cute creature. A beautiful place. Something buried nearby. One more place to reach.*
