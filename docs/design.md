# DOWNSHAFT — DESIGN

_The authoritative design document._

_Updated 2026-07-30 after the project was reframed as a persistent structural puzzle-RPG:
compact physics boards, one continuous underground world, a permanent home, sparse camps,
physical inventory, and a production target of Rust compiled to WebAssembly._

---

## 1. THE PITCH

You are an ordinary guy in your backyard with a pickaxe.

You dig down.

Under the lawn are dinosaur bones, buried rooms, impossible machines, a motel run by a mole,
a subterranean carnival, and eventually a UFO abducting a cow.

The world starts mundane and becomes stranger with depth. Nothing becomes grim. Nothing turns
into horror. The absurdity escalates, but the world treats all of it as normal.

The visual and tonal reference of record is
**[`north-star.png`](north-star.png)**.

Read it from top to bottom. That descent is the game.

---

## 2. WHAT THE GAME IS

**DOWNSHAFT is a persistent puzzle-RPG about engineering collapses.**

It is not a free-form mining game.

The underground is divided into compact spatial problems. Each screen is closer to an
individual Candy Crush, Critter Crunch, Grindstone or puzzle-game level than to a continuous
sandbox.

A screen presents a legible arrangement of:

- structural rock;
- loose material;
- supports and anchors;
- resources;
- objects;
- creatures;
- machinery;
- hazards;
- routes;
- and one or more things worth preserving, reaching, moving or extracting.

The screens are not selected from a level menu and discarded after completion. They are
connected sections of one persistent underground world.

What the player breaks stays broken.

What falls stays where it lands.

Items can be dropped and recovered later. Creatures can move into excavated spaces. Old routes
remain useful. Unsolved objects remain underground. Equipment acquired much later can create
new solutions to old screens.

The player is not clearing levels.

The player is excavating a place.

---

## 3. THE CORE QUESTION

Everything in the shaft is structurally connected to the two side walls.

Rock connected to either wall is stable.

Cut a formation free of both walls and the unsupported mass collapses.

Stand on the mass and you ride it down.

Stand beneath it and you are buried.

Other materials modify that rule:

- dirt slides;
- ice carries things sideways;
- roots regrow;
- webs catch falling objects;
- pipes release water, steam, gas or pressure;
- beams anchor structures;
- balloons make masses rise;
- machinery pushes, pulls or transforms material;
- explosives remove broad areas and threaten everything nearby.

Before the player commits an action, the game previews its exact immediate result.

The challenge is not discovering what the simulation means after losing. The challenge is
choosing the most useful consequence.

The question in the player’s head should always be:

> What happens if I cut this?

That question is the product.

---

## 4. THE ATOM OF PLAY

The atom is **one compact structural board**, not one complete descent.

A board should usually take between one and three minutes to understand and change
meaningfully. A player opening the game for three minutes should be able to:

- solve a board;
- create a useful route;
- extract an object;
- reach a side room;
- move closer to a camp;
- alter a persistent structure;
- or make another permanent contribution to the world.

The player does not need to return home every few minutes for the session to count.

Progress can be banked as:

- changed terrain;
- opened routes;
- moved objects;
- collected resources;
- reached landmarks;
- discovered rooms;
- activated machinery;
- established camps;
- rescued residents;
- or knowledge of the world.

The game must support both a three-minute phone session and a long expedition without dividing
itself into separate modes.

---

## 5. THE BOARD LOOP

A typical board works like this:

1. Enter a compact section of the shaft.
2. Read its supports, materials, valuables, hazards and exits.
3. Move into position.
4. Select a tool or carried object.
5. Preview the exact consequence of the action.
6. Commit.
7. Ride, evade, redirect or exploit the resulting movement.
8. Collect, use, drop, preserve or transport what remains.
9. Leave the board permanently changed.
10. Continue downward, return through an old route, or enter a lateral branch.

Picks are a decision budget, not a real-time fuel meter.

Every committed cut should accomplish something. It should release a mass, expose a route,
preserve a find, trigger a device, move an object, rescue a creature, or create a position from
which the next action becomes possible.

Repeatedly removing blocks for no strategic reason is failure.

---

## 6. THE PHYSICS VOCABULARY

Progression should give the player new operations, not merely larger damage numbers.

| Operation | What it changes                                  | Example tools or objects              |
| --------- | ------------------------------------------------ | ------------------------------------- |
| Remove    | Deletes selected material                        | Pickaxe, chisel, drill, acid          |
| Push      | Moves a mass laterally                           | Sledgehammer, piston, blast           |
| Pull      | Draws an object toward a point                   | Magnet, winch, tractor beam           |
| Lift      | Moves an object or mass upward                   | Jack, balloon, inflatable bag         |
| Anchor    | Makes a structure stable                         | Beam, clamp, web, roots               |
| Tether    | Connects the player or an object to an anchor    | Rope, chain, cable                    |
| Trigger   | Activates a remote or connected mechanism        | Plate, lever, fuse, gear              |
| Transform | Changes the physical state of a material         | Furnace, water, electricity, freezing |
| Preserve  | Protects a fragile object from impact            | Foam, crate, suspension rig           |
| Reveal    | Improves the information available before acting | Lamp, scanner, map, specialist        |

Many objects can share an underlying operation.

A balloon, anti-gravity crystal and tractor beam can all use the same lift rule while feeling
different because of their availability, presentation, scale and consequences.

The game should achieve variety by recombining a strong set of physical rules, not by creating
hundreds of unrelated one-off mechanics.

---

## 7. RESOURCES

Resources are not interchangeable colors with different sale prices.

Every important material needs three identities:

1. **Physical:** how it behaves inside a structural board.
2. **Economic:** why the player wants to extract it.
3. **World-facing:** what it builds, unlocks, decorates or changes.

Examples:

| Resource    | Underground identity                                | Long-term use                                |
| ----------- | --------------------------------------------------- | -------------------------------------------- |
| Copper      | Conducts power through connected cells              | Wiring, lamps, powered tools                 |
| Iron        | Heavy and structurally strong                       | Beams, tools, machinery                      |
| Gold        | Valuable, heavy and tempting to destabilize         | Expensive upgrades and decoration            |
| Ice         | Causes sliding and preserves frozen objects         | Cooling devices and protective clothing      |
| Crystal     | Stores, emits or redirects energy                   | Scanners, teleporters and advanced equipment |
| Roots       | Regrow through available space                      | Medicine, cultivation and organic tools      |
| Fossils     | Fragile multi-cell objects                          | Collections, research and prestige           |
| Alien alloy | Resists ordinary tools and may be unnaturally light | Endgame force-manipulation devices           |

A resource should be interesting when encountered, difficult or satisfying to extract, and
meaningful after it reaches home.

---

## 8. FINDS AND EXTRACTION

Important finds should not all be single collectible tiles.

Large fossils, furniture, machinery, statues, creatures and strange artifacts can occupy
multiple cells. Extracting them becomes a structural objective:

- expose the object;
- keep it supported;
- avoid crushing it;
- create a route;
- move or lower it safely;
- transport it to a camp or the surface.

A dinosaur skull should not be awarded because the player tapped it.

The player should excavate it.

Multi-cell fragile finds are one of the main ways the game turns its existing collapse rules
into varied objectives.

---

## 9. INVENTORY

The player has a persistently visible inventory hotbar.

The inventory is not represented by an abstract bag-fullness meter hidden behind another
screen. Carried things should remain visible and actionable during play.

The player can:

- select an item;
- use it on the board;
- drop it;
- rearrange it;
- swap it;
- consume it;
- leave it behind;
- or carry it to another location.

Common materials may stack. Tools, consumables and unusual finds may occupy individual slots.

Large objects do not disappear into ordinary inventory slots. They must be moved, dragged,
lowered, tethered, carried by machinery or transported through another explicit system.

When the inventory is full, collecting another item requires a real decision:

- leave it;
- drop something;
- consume something;
- move it to nearby storage;
- or arrange transportation.

The game should never silently turn an unwanted object into money.

Money remains separate from physical inventory.

---

## 10. EQUIPMENT, CLOTHING AND PERKS

Equipment should change how the player solves boards.

Examples:

| Equipment        | New capability                                    |
| ---------------- | ------------------------------------------------- |
| Pickaxe          | Removes a connected cluster                       |
| Chisel           | Removes one exact cell                            |
| Drill            | Cuts a narrow line through hard material          |
| Sledgehammer     | Pushes a mass instead of destroying it            |
| Support beam     | Permanently anchors a structure                   |
| Rope             | Tethers the player or an object                   |
| Jack             | Raises a mass one cell                            |
| Magnet           | Pulls metal through open space                    |
| Balloon          | Reverses gravity for one object or mass           |
| TNT              | Removes a large area and threatens nearby objects |
| Foam             | Creates temporary support                         |
| Remote detonator | Sequences multiple explosions                     |

Clothing changes the risks the player can tolerate rather than supplying meaningless armor
numbers.

Examples:

- a hard hat survives one small falling impact;
- climbing gloves extend the ability to ride a falling mass;
- steel-toed boots resist sliding or pushing;
- a rubber suit protects against powered conductive structures;
- fireproof clothing permits access to heated regions;
- a tool belt changes the usable inventory layout;
- a miner’s lamp reveals hidden cavities or internal material properties.

Perks should primarily affect:

- removal;
- force;
- support;
- information;
- carrying;
- preservation;
- survival;
- or the economics of extraction.

---

## 11. CREATURES AND CONFLICT

Creatures belong inside the structural puzzle.

They should act after committed moves, react to collapses, or modify terrain. They should not
start a separate reflex-combat game.

Examples:

| Creature            | Structural role                                               |
| ------------------- | ------------------------------------------------------------- |
| Mouse               | Moves through open tunnels and may reveal routes or valuables |
| Spider              | Builds webs that catch falling objects                        |
| Worm                | Removes cells and creates new passages                        |
| Mole                | Digs, pushes material or reshapes a board                     |
| Cow                 | Large fragile rescue and transportation objective             |
| Living plant        | Regrows roots and changes support                             |
| Mechanical creature | Pushes, pulls or activates connected devices                  |

Weapons should also behave as physics tools.

A shotgun applies directional force. A freeze device creates temporary support. A net pins a
creature or object to a wall. A flare attracts living things. A sonic device loosens one kind
of material.

The interesting question is:

> What will attacking this cause?

Not:

> How quickly can I empty its health bar?

---

## 12. HOME

The backyard is the center of the game.

It remains the player’s primary home throughout the entire experience.

The house and yard provide:

- long-term storage;
- equipment preparation;
- crafting and repair;
- wardrobe and customization;
- collections;
- records;
- relationships;
- and visible evidence of progress.

Recovered objects can be displayed physically.

The garden gnome dug out of the shaft can stand on the lawn. Fossils can be reconstructed.
Impossible plants can grow in pots. Underground signs, machinery, furniture and trophies can
accumulate around the house.

The surface becomes a visual record of this particular player’s excavation.

It should begin as an ordinary backyard and slowly become a museum of impossible things.

---

## 13. CAMPS

Underground camps are rare, persistent and widely separated.

They are not automatic landings every few screens.

Reaching or establishing a camp should feel like a major expedition milestone. A camp may be
dozens of boards from the previous safe base and may sit inside a lateral branch rather than
directly on the central shaft.

A camp can provide some combination of:

- storage;
- rest;
- equipment changes;
- a resident service;
- a shop;
- local information;
- power;
- and a reliable return point.

Camps extend the range of an expedition.

They do not replace home.

Each camp must have a distinct identity. A camp should be a memorable place with a resident,
biome function, landmark or story—not a repeated checkpoint template.

The Mole Motel is a natural candidate for a major underground camp.

---

## 14. WORLD STRUCTURE

The world consists of:

- compact structural boards;
- a persistent central descent;
- lateral branches;
- authored interiors;
- rare camps;
- resident spaces;
- machinery networks;
- large extraction sites;
- and fixed landmarks.

Lateral branches are essential. They prevent the world from feeling like a simple vertical
stack and give natural homes to:

- camps;
- shops;
- residents;
- puzzles;
- machinery;
- fossils;
- optional resources;
- and strange rooms.

Old areas remain relevant because they can contain:

- unresolved finds;
- alternate routes;
- resources that previously could not be extracted;
- devices requiring later equipment;
- objects left in storage;
- and consequences of earlier actions.

The player should learn the geography of the hole.

---

## 15. THE DESCENT

The broad tonal and mechanical progression is:

| Region         | Mechanical emphasis                                    | Major discovery                    | Tone                             |
| -------------- | ------------------------------------------------------ | ---------------------------------- | -------------------------------- |
| Backyard       | Preparation, collection and customization              | The hole itself                    | Entirely ordinary                |
| Topsoil        | Loose dirt, simple support and fossils                 | Dinosaur remains beneath the lawn  | Surprising but plausible         |
| Buried rooms   | Fragile objects and domestic interiors                 | A skeleton drinking coffee         | Someone lived here               |
| Machinery      | Pipes, pressure, plates, power and heavy material      | A machine with a skull face        | Someone built systems here       |
| Caverns        | Organic growth and creature objectives                 | An unexplained cow                 | The underground is alive         |
| Mole territory | Lateral tunnels, residents and services                | The Mole Motel                     | Society exists below             |
| Carnival       | Reversed forces, event objects and absurd consumables  | Balloons and a clown-mouth doorway | Physics becomes theatrical       |
| Space          | Tractor beams, alien material and impossible geography | Alien living room, UFO and rocket  | Down no longer means underground |

The progression is not a binding list of eight levels. It is the direction of escalation.

The further down the player travels:

- ordinary rock becomes stranger;
- objects become less explainable;
- built spaces become more elaborate;
- resources emit more light;
- the world becomes more inhabited;
- and physical rules gain more unusual inversions.

Deep ore should increasingly read as light against dark material rather than merely as a
brightly colored patch.

---

## 16. TONE

The humor is escalating absurdism played completely straight.

The mole really operates a motel.

The skeleton really has a coffee table.

The clown’s mouth really is a doorway.

The alien really watches surface television in an armchair.

Nobody stops to deliver a lore explanation for why these things are beneath the backyard.

The player remains visually ordinary while the world becomes impossible.

DOWNSHAFT is colorful, warm, strange and funny.

It is never grimdark and never horror.

---

## 17. WHAT THE PLAYER IS TOLD

The HUD shows only information the player owns or can act upon:

- depth;
- remaining picks or actions;
- distance to the next known camp;
- visible inventory slots;
- selected item;
- money;
- and access to the menu.

Distance to a camp should be expressed as physical distance, such as:

`NEXT CAMP: 30 m`

It should not say how many abstract screens remain.

The menu control should be deliberately designed. It should not remain a generic hamburger
symbol unless it is literally represented as a hamburger.

The game does not provide:

- a minimap that solves navigation;
- an ore radar;
- a generic stability meter;
- arrows toward valuable objects;
- or unexplained strategic summaries.

The board itself is the primary readout.

Materials announce their behavior through:

- shape;
- color;
- texture;
- animation;
- connected structure;
- sound;
- and response to interaction.

Every relevant object must remain legible on a portrait phone screen.

---

## 18. THE PREVIEW

The preview is a promise.

Before a consequential action is committed, the game should show as precisely as possible:

- which cells will be removed;
- which masses will become unsupported;
- which direction they will move;
- whether the player will ride or be struck;
- what object will be pushed, pulled or lifted;
- and what limited item will be consumed.

Difficulty comes from evaluating consequences, not from fighting an opaque simulation.

The preview does not need to reveal every secondary reaction several turns into the future,
but it must accurately represent the immediate committed result.

Breaking that promise damages the entire game.

---

## 19. FEEL

The tap is the product.

A mechanic is not finished when the state transition works.

It ships with:

- anticipation;
- impact;
- displacement;
- particles;
- screen shake;
- sound;
- readable timing;
- and a satisfying settled state.

There is no hypothetical later polish pass.

A collapse must feel heavy. A crystal must feel sharp. Dirt must feel loose. A balloon must
feel buoyant. A fossil breaking must feel awful.

Feedback is part of the rule because feedback is how the player understands the rule.

---

## 20. ART

The game uses authored pixel art represented as data.

The absence of ordinary runtime image assets is not an excuse for placeholder art. Tiles,
objects and characters are still deliberately drawn by an artist or designer, then converted
into a code-readable representation.

Keeping the art data-driven supports:

- palette changes;
- material-specific particles;
- destructible objects;
- procedural damage;
- dynamic exposed faces;
- lighting;
- animation;
- equipment variants;
- and interaction between visuals and simulation.

Pixel art should be authored in a proper editor and exported through a separate tool.

The importer or exporter is not part of the game’s runtime build process. It converts authored
art into the project’s indexed sprite or tile representation.

Nothing is 3-D.

The entire visual language is based on readable 2-D pixel art.

---

## 21. TECHNOLOGY

The current prototype is a single `index.html` file written in JavaScript.

That prototype exists to discover the game quickly and keep phone testing immediate.

The intended production implementation is Rust compiled to WebAssembly.

Rust is not being chosen because the current simulation requires more performance. It is being
chosen because the finished game will contain a large persistent state space, interacting
materials, inventory, equipment, save migrations, procedural content and many structural
rules. Strong types, explicit state transitions and compiler-enforced invariants are valuable
for that system.

The production architecture should keep:

- world state;
- structural simulation;
- materials;
- items;
- inventory;
- procedural generation;
- save validation;
- and deterministic rules

inside Rust.

Browser integration remains responsible for:

- the canvas;
- input;
- audio;
- storage;
- page lifecycle;
- and platform-specific behavior.

The JavaScript prototype should not be allowed to become a constraint on the production
architecture.

The production port begins after the central design is proven. It is not a reason to defer
fixing prototype problems, and it should not be a blind line-for-line translation.

---

## 22. PHONE-NATIVE

Phone-native or it does not count.

The designer tests in a phone browser during the day. That is the actual development and
testing environment, not a secondary port target.

The game is designed around:

- portrait orientation;
- one-thumb interaction;
- large readable targets;
- short interruption-safe play;
- clear visual previews;
- and immediate loading from a URL.

Desktop support is welcome, but the game must never depend on a mouse, keyboard shortcuts,
large monitor, hover state or dense text interface.

---

## 23. CURRENT PROTOTYPE

The current live prototype is:

<https://junovhs.github.io/grapeghost/>

It currently contains:

- a 10 × 16 tile shaft;
- seeded persistent screens;
- structural support calculated from walls and anchors;
- collapsing unsupported masses;
- player riding and burial;
- loose materials;
- pipes;
- roots;
- living materials;
- several depth bands;
- finds;
- a lift;
- an early shop;
- and a reset system.

The current build also contains assumptions that are no longer the intended final design:

- frequent landings;
- a bag-capacity readout;
- the complete descent as the session atom;
- and JavaScript as the final implementation.

Those systems are prototype evidence, not sacred architecture.

Only the central verb is sacred.

---

## 24. DESIGN LAWS

### The collapse system carries the game

The structural puzzle must remain deep enough that content enriches it rather than conceals
its weakness.

### Every addition returns to the board or the world

A resource, item, resident, room or progression system must do at least one of two things:

1. change how the player reads, manipulates, survives, preserves or profits from a structural
   board; or
2. make the persistent world worth caring about.

### New tools create new verbs

Progression should expand possibility rather than increase a damage statistic.

### The world remembers

Terrain, objects, rooms, camps and important consequences persist.

### Home remains home

Underground camps support expeditions. They do not replace the backyard.

### Interiors are built; shafts are dug

Authored rooms use constructed walls, furniture, lighting and clean boundaries. Excavation
spaces remain rough, geological and structurally legible.

### Deep resources emit light

Near the surface, ore is color inside earth. At great depth, the world darkens and valuable
material increasingly glows.

### The ordinary player enters an extraordinary world

The player remains a recognizable person in practical clothes. The absurdity belongs to the
world.

### No separate generic combat game

Conflict must interact with force, structure, terrain, movement or preservation.

### Decoration is allowed to be decoration

Not every object requires a mechanic. Atmosphere and visual storytelling are valuable, but
they should not be confused with systemic depth.

---

## 25. PRODUCTION PRIORITIES

In order:

1. Make structural collapse, support and preview consistently satisfying.
2. Establish the persistent board and world model.
3. Build the visible, usable physical inventory.
4. Add multi-cell fragile objects and extraction.
5. Add push, anchor, lift, tether and directional force.
6. Add sparse camps and long expedition structure.
7. Add surface trophies and home customization.
8. Add lateral branches and authored resident rooms.
9. Add creatures governed by board turns and physics.
10. Add resources with real physical and long-term identities.
11. Add equipment, clothing, crafting and progression around those rules.
12. Expand depth bands, residents, visual variety and decoration.

Additional ore colors are not a substitute for additional interaction.

Additional content is not a substitute for a deeper verb.

---

## 26. DECISION ALIGNMENT

The project was founded on DOWNSHAFT under **DEC-09**, but several recorded decisions now need
to be amended or superseded in Ishoo.

| Decision   | Current direction                                                                           |
| ---------- | ------------------------------------------------------------------------------------------- |
| **DEC-07** | Still valid: development and testing are phone-native                                       |
| **DEC-09** | Still valid: DOWNSHAFT is the project                                                       |
| **DEC-10** | Revise: the atom is one compact board or meaningful persistent action, not one full descent |
| **DEC-11** | Revise: the HUD includes a persistent actionable inventory and distance to sparse camps     |
| **DEC-12** | Still valid: borrowed placeholders are recorded and never ship                              |
| **DEC-13** | Supersede: JavaScript is the prototype; Rust/Wasm is the intended production implementation |
| **DEC-14** | Clarify: art remains authored pixel data, independent of implementation language            |
| **DEC-15** | Still valid: tone escalates into absurdity with depth                                       |
| **DEC-16** | Still valid: feel ships with the mechanic                                                   |

The Ishoo decisions should be updated so the tracker and this document do not disagree.

---

## 27. OPEN QUESTIONS

The largest unresolved questions are:

| Question                                                               | Why it matters                                        |
| ---------------------------------------------------------------------- | ----------------------------------------------------- |
| What is the complete v1 physics vocabulary?                            | Determines the real puzzle depth                      |
| What makes structural play remain interesting for hundreds of hours?   | Decides whether the game exists beyond its premise    |
| What is the progression spine from the backyard to the deepest region? | Connects tools, resources, camps and world escalation |
| How are boards authored, generated and recombined?                     | Determines replayability and content cost             |
| How far apart are camps?                                               | Determines expedition pressure and world scale        |
| How does the player transport large finds?                             | Central to fossils, creatures and machinery           |
| What persists when a board is left unresolved?                         | Defines the world-state model                         |
| How much information does the preview guarantee?                       | Defines fairness and technical scope                  |
| What belongs in the first complete vertical slice?                     | Prevents the RPG breadth from burying the core        |
| What is the production Rust/Wasm architecture?                         | Determines the final implementation and save model    |
| What lives in each depth region?                                       | Defines the content and tonal spine                   |
| What is the pixel-art export pipeline?                                 | Makes final art production sustainable                |

These should be represented in Ishoo rather than accumulating contradictory answers in
multiple markdown files.

---

## 28. RELATED DOCUMENTS

[`game-systems-plan.md`](game-systems-plan.md)

The current systems inventory, world structure, content classes and production priorities.

[`north-star-catalogue.md`](north-star-catalogue.md)

A literal catalogue of every object shown in `north-star.png`, including what exists in the
prototype and what the image suggests.

This document preserves the source image’s observations. It is not the authoritative systems
specification.

[`philosophy.md`](philosophy.md)

The designer’s project-independent preferences: what he values in games and why. It should be
consulted before proposing systems, but it is not specific to DOWNSHAFT.

[`north-star.png`](north-star.png)

The visual and tonal reference of record.
