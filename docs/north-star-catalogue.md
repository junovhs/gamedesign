# THE NORTH STAR, ITEM BY ITEM

Everything in [`north-star.png`](north-star.png), read top to bottom, with a role assigned to
each thing. The image is treated as **one screen holding a sample of the entire game** — not a
level, a catalogue. This file is the shopping list.

**Status column:** `BUILT` exists in `index.html` today · `NEW` the image is asking for
something the build does not have · `DRESS` pure scenery, no rules attached.

---

## 0. THE READOUT

The HUD in the image is stricter than the one in the build, and better. It says four things
and all four are things you own (DEC-18).

| # | In the image | Kind | Role | Status |
|---|---|---|---|---|
| 1 | `DEPTH 42` in big amber numerals | readout | How far down you are. The only number that is allowed to be large — it is the score, the progress bar and the brag. | BUILT |
| 2 | Six pickaxe icons, five jade-green, one dark | readout | Picks remaining **as objects, not a number**. You read your budget as a row of tools, and the spent one stays visible as a greyed ghost. | NEW |
| 3 | `1 TO LAND` | readout | Screens remaining until the next landing. The build already has landings every third screen but never tells you one is coming — this is the "one more" hook, and it is legal because it counts a distance you have already earned. | NEW |
| 4 | `BAG` bar, amber, about 70 % full | readout | Carry capacity. A bar, not a fraction: you read fullness at a glance and never do arithmetic. | BUILT (as text) |
| 5 | Coin icon + `173` | readout | Purse. The coin glyph carries the meaning so the word "gold" is never needed. | BUILT |
| 6 | Hamburger button, top right | control | Menu. Already reserved space on the canvas. | BUILT |

Nothing else is on screen. No minimap, no ore counter, no stability meter. Keep it that way.

---

## 1. THE BACKYARD (surface)

The surface strip is not scenery — it is **the home screen**, and every object in it is a
candidate for a placeable trophy. This is where a five-hundred-hour player displays what they
dug up.

| # | In the image | Kind | Role | Status |
|---|---|---|---|---|
| 7 | Blue doghouse | prop | Home fixture. Candidate: the dog sleeps here when it is not following you. | NEW |
| 8 | Brown-and-white dog, red collar | resident | The one character who is *yours*. Follows along the surface, reacts when you surface with a haul, barks at the hole. Pure feel, zero mechanics — and worth building for that alone (DEC-16). | NEW |
| 9 | Wooden picket fence | prop | Backyard boundary. Defines the play area of the surface. | DRESS |
| 10 | House with a red roof and a window | prop | Yours. Candidate later use: the door is where you bank, sell or sleep. | NEW |
| 11 | Potted spiky plant, blue pot | prop | Placeable decoration. | DRESS |
| 12 | Sky, clouds, distant treeline | backdrop | Daylight. If a day/night cycle ever exists, this is where it shows. | DRESS |
| 13 | **Pink flamingo** | trophy | Lawn ornament. Perfect shop or find reward: costs money, does nothing, and every player will want one. | NEW |
| 14 | **Garden gnome**, red hat | trophy / find | Already a find in the build (`GARDEN GNOME`, +3 satchel). In the image he is standing on the lawn — so a find you dig up should be **placeable on the surface afterwards**. That is the whole collection loop in one object. | BUILT as find, NEW as placement |
| 15 | Red-and-black lawn mower | prop | Backyard fixture. Candidate: the thing you were supposed to be doing instead of digging. | DRESS |
| 16 | Hedges and trees | backdrop | Frames the yard. | DRESS |
| 17 | Grass-topped soil strip | tile | The surface layer. Reads as the boundary between normal and not. | BUILT |
| 18 | **The player**: yellow hard hat, orange shirt, blue trousers, pickaxe over the shoulder | actor | You. An ordinary guy in safety gear, no fantasy costume. Keep him plain — the world escalates, he does not. | BUILT |

---

## 2. TOPSOIL AND FOSSILS

| # | In the image | Kind | Role | Status |
|---|---|---|---|---|
| 19 | Plain brown dirt tile | tile | `DIRT`. Loose: slides, will not hold a ceiling. | BUILT |
| 20 | Gold nuggets scattered loosely in dirt | tile variant | Low-grade ore *speckled into* a bulk tile rather than being its own tile. Gives a rich band without changing the material. | NEW |
| 21 | **Large bone** | find | Collectible. First piece of the dinosaur set. | NEW |
| 22 | **T-rex skull**, spanning several tiles | multi-tile find | A fossil is bigger than one tile, so excavating it is its own small puzzle: clear around it without dropping it. Feeds a bone collection displayed at home. This is the single strongest idea in the picture. | NEW |
| 23 | Copper pipework running down the left wall | tile / structure | `PIPE`. Burst it and water digs for you. | BUILT |
| 24 | Red lantern, glowing, wall-mounted | prop / light | Placeable light source. Candidate: place a lantern to keep a screen lit permanently. | NEW |
| 25 | Grey cobble / gravel tile | tile | `STONE`. Structural, holds a ceiling. | BUILT |
| 26 | Dense gold-in-brown tile | ore | `GOLD`. Needs an iron pick. | BUILT |
| 27 | Gold-flecked dirt tile | ore | A cheap ore in a cheap material — the early "yes!" | BUILT |
| 28 | `I ♥ DIRT` poster | prop | Wall sign, played straight. Comedy comes from someone having lived down here. | NEW |
| 29 | Green enamel hanging lamp | prop / light | Marks an inhabited room. Where you see one, someone lives. | NEW |
| 30 | **Skeleton sitting in a wooden chair** | resident | The first joke of the descent: a guy who came down and stayed. Candidate role: he is a shop, a hint, or just there. He does not attack — nothing in this game attacks like that. | NEW |
| 31 | Side table with a mug of utensils | prop | Sells the room as lived-in. The build already has a `CUTLERY` layer — this is where that gag comes from. | DRESS |
| 32 | Wooden ladder, full height, right edge | structure | Re-entry. Visual language for the lift. | BUILT (as lift) |
| 33 | Stone-brick shaft walls, left and right | structure | The unbreakable frame everything hangs from. This is the load-bearing rule of the whole game and the art already states it. | BUILT |
| 34 | Grey rat | critter | Ambient life. Scurries, is startled by a break, drops nothing. Cheap, and enormous for feel. | NEW |
| 35 | Green corner brackets around a 2×2 of tiles | UI | The cluster the next tap will take. The build's most important piece of feedback, drawn as four corners rather than a fill so you can still see the tiles. | BUILT |
| 36 | Small white sparkle marks | UI / VFX | Glints on freshly exposed faces. | BUILT-ish |

---

## 3. STONE, MACHINERY AND THE ORE SET

The middle of the image is mostly **tiles**, and it says something important: the ores are the
only saturated things on screen and each one has a distinct *shape*, not just a distinct hue.

| # | In the image | Kind | Role | Status |
|---|---|---|---|---|
| 37 | Magenta star-crystal tile | ore | Deep-band ore. | BUILT-ish |
| 38 | Steel plate with a riveted ring | tile | Hatch / machined plate. Structural, needs the drill. | NEW |
| 39 | Orange-red ore in dark rock | ore | Fire-coloured ore for the hot band. | NEW |
| 40 | **Blue-and-gold treasure chest embedded in the wall** | container | Not a tile — a container you break open for a roll. The one place a random reward is honest. | NEW |
| 41 | Grey stone with white quartz flecks | tile | Bulk rock variant, keeps big stone areas from reading flat. | NEW |
| 42 | **Golden block with a smiling face** | tile / event | An idol block. Breaking it should *do* something — the face is a promise. Candidate: it laughs and the whole screen drops. | NEW |
| 43 | **TNT block** | tile / tool | Detonates a radius. The obvious verb the build is missing, and it slots straight into the collapse rules. | NEW |
| 44 | Clockwork tile: gears and bolts | tile | Machine-band bulk material. | NEW |
| 45 | Blue diamond tile | ore | High-value deep ore. | NEW |
| 46 | Red gem tile | ore | | NEW |
| 47 | **Red block with a gold `?`** | tile / event | Mystery block: break it and one random thing happens, good or comic. Absurdism needs a slot machine and this is it. | NEW |
| 48 | Pink gem tile | ore | | NEW |
| 49 | Purple amethyst tile | ore | | BUILT-ish |
| 50 | Small green figure with red bulbs | prop / creature | Reads as a little plant idol. Candidate: a sprout that regrows the `ROOT` material around it. | NEW |
| 51 | **Large magenta crystal in a carved alcove** | set-piece | A geode: authored pocket, big single prize, worth routing toward. | NEW |
| 52 | Spider on a web | critter | Ambient. Webs could slow a fall — a soft landing. | NEW |
| 53 | **Machine with a skull face and red eyes**, pipes and boiler, left wall | set-piece | The band's landmark. Someone built a machine down here and gave it a face. Candidate: it is the elevator's motor, or it wants ore fed to it. | NEW |
| 54 | Stone column / pillar | structure | Load-bearing column: an anchor tile you can see. Reads as "this holds things up" without a word. | BUILT (`BEAM`) |

---

## 4. THE CAVERN AND THE MOLE MOTEL

| # | In the image | Kind | Role | Status |
|---|---|---|---|---|
| 55 | Green emerald tile | ore | | NEW |
| 56 | Two ice tiles with a diagonal shine | tile | Slippery: you slide along it, and it should be the tile that makes falling *fun* rather than punishing. | NEW |
| 57 | Large teal gem tile | ore | | NEW |
| 58 | Small grey bolt tile | tile | Machined filler. | NEW |
| 59 | **`MOLE MOTEL` neon sign with an arrow** | signage | Points at an authored room. Neon underground is the tone in one object: someone is running a *business* down here. | NEW |
| 60 | Pink glowing mushroom cluster | prop / light | Bioluminescent dressing. Free light and free colour in the dark bands. | NEW |
| 61 | Potted purple flowers | prop | Someone's houseplant, in a cave. | DRESS |
| 62 | **Cow, standing on a ledge** | resident | A cow. Down here. No explanation offered — and it appears again at the bottom being abducted, which makes it the running gag of the whole game. Candidate: you can find one and get it home. | NEW |
| 63 | Grey plate with concentric squares | tile | Vault plate / pressure plate. | NEW |
| 64 | Ruby cluster tiles | ore | | NEW |
| 65 | Embossed circuit-like tile | tile | Machine-band variant. | NEW |
| 66 | **Mole in bed wearing sunglasses** | resident | The motel's proprietor, indoors, at leisure, in shades. The best character in the picture. Candidate: rest to restore picks, or a shop that only stocks what that band produces. | NEW |
| 67 | Lit bedside lamp | prop | | DRESS |
| 68 | Blue nightstand / dresser | prop | | DRESS |
| 69 | Wooden chair | prop | | DRESS |
| 70 | Purple plank wall, interior | structure | Authored-room wall material: interiors are *built*, the shaft is dug. The two must never look alike. | NEW |

---

## 5. THE CARNIVAL

The strangest band, and the one that most needs rules, or it is just decoration.

| # | In the image | Kind | Role | Status |
|---|---|---|---|---|
| 71 | Purple pipework | tile / structure | | BUILT (recoloured) |
| 72 | Purple machine with a red joystick | prop / device | An arcade cabinet, or a lever that does one absurd thing. | NEW |
| 73 | Glowing gem seams — yellow, magenta, green diamonds — in near-black rock | ore | Deep ore reads as *light* rather than colour. The palette rule for the bottom of the game. | NEW |
| 74 | **Balloons**: orange, blue, red, purple, magenta | prop / mechanic | The inversion the collapse system is begging for: tie a balloon to a mass and it goes **up** instead of down. Absurd, legible in one look, and it makes the core physics run backwards. Strongest new mechanic in the picture. | NEW |
| 75 | Empty dark picture frame | prop | | DRESS |
| 76 | Framed picture of a goldfish | prop | Someone decorated. | DRESS |
| 77 | Pink segmented worm / caterpillar | creature | A tunneller. Candidate: it digs its own passages through the screen, which you can follow or get surprised by. | NEW |
| 78 | **Clown face whose open mouth is a doorway** | structure / entrance | The entrance to a room you walk *into*. This is the strongest argument for a side-view interior mode: the shaft is vertical, but a door is a promise of somewhere else. | NEW |
| 79 | `WE ♥ HOLES` wooden sign | signage | The band's greeting. | NEW |
| 80 | Giant cupcake with a cherry | prop / consumable | Food. Candidate: restores picks. | NEW |
| 81 | Round lollipop | prop / consumable | | NEW |
| 82 | **Pink vending machine with a face, dispensing pizza** | device | A vending machine that is also a creature. Spend coins underground instead of hauling everything to the surface — a real economic decision inside a descent. | NEW |
| 83 | Green leaves growing out of the wall | prop | | DRESS |
| 84 | Dark blue brick wall | structure | Band wall colour. | BUILT (as `wall`) |
| 85 | Wooden ladder | structure | | BUILT (as lift) |

---

## 6. SPACE

| # | In the image | Kind | Role | Status |
|---|---|---|---|---|
| 86 | **UFO with a green tractor beam** | set-piece | The bottom-of-the-world landmark. | NEW |
| 87 | **Cow inside the beam, being abducted** | set-piece / gag | The cow from the mushroom cave, resolved. If the player can bring a cow down here, this is the punchline of a five-hundred-hour joke. | NEW |
| 88 | Blue crystal | ore | | NEW |
| 89 | Magenta gem floating on a string | prop | Reads as a gem balloon — ties the carnival band to this one. | NEW |
| 90 | **Alien in a purple armchair** | resident | Sitting down, relaxed, indoors. The deepest character in the game is the most comfortable. | NEW |
| 91 | Cocktail glass with a cherry | prop | He has a drink. | DRESS |
| 92 | **CRT television showing a surface scene** | prop / gag | He is watching the world you came from. One object that says the whole descent was a journey away from home. | NEW |
| 93 | White-and-red rocket | set-piece | The way out that is not up the shaft. Candidate end-of-band reward, or the prestige button. | NEW |
| 94 | Star-flecked black rock wall | tile | Space band bulk material: the rock itself has stars in it. | NEW |
| 95 | Glowing magma strip in the ceiling bricks | structure | Light from above, coloured per band. | NEW |
| 96 | Purple and dark-blue brick walls | structure | | BUILT |

---

## WHAT THE PICTURE IS ASKING FOR

Reading the catalogue back, the image demands seven things the build does not have. In rough
order of how much game they add per unit of work:

1. **Multi-tile finds** (fossils). Excavating something larger than a tile without dropping it
   is a new puzzle built entirely out of rules that already exist.
2. **Balloons.** Make a mass rise instead of fall. Inverts the core system for free.
3. **TNT and the mystery block.** Two verbs, both one-tap, both immediately funny.
4. **Residents.** Skeleton, mole, alien — one per band, each in a lit room with furniture,
   none of them hostile. They are what makes depth feel *inhabited* rather than empty.
5. **Placeable trophies on the surface.** The gnome you dig up stands on your lawn. This is
   the collection loop and the reason to keep a find rather than sell it.
6. **Rooms you enter** (the clown door, the motel). A break from vertical, and the natural
   home for shops, rest and set-pieces.
7. **Critters.** Rat, spider, worm, cow. Ambient life, cheap to draw, enormous for feel.

And two rules the art states without saying them:

- **Interiors are built, shafts are dug.** Plank walls, wallpaper and lamps versus rock. The
  player must never be confused about which one they are standing in.
- **Deep ore is light, not colour.** Near the surface, ore is a bright mineral in brown dirt.
  At the bottom, the rock is black and the ore *glows*. The palette itself tracks depth.

## THE LADDER THE IMAGE IMPLIES

Top to bottom, this is the band order the picture is drawn in. It is the input to Q-17, not
the answer to it.

| | Band | The joke |
|---|---|---|
| 0 | The backyard | An ordinary afternoon. Nothing is wrong yet. |
| 1 | Topsoil and fossils | There is a dinosaur under your lawn. |
| 2 | Somebody's basement | A skeleton is having coffee. He put up a poster. |
| 3 | Stone and machinery | Someone built a machine down here and gave it a face. |
| 4 | The mushroom cavern | There is a cow. No one will explain the cow. |
| 5 | The Mole Motel | There is a hospitality industry down here, and it has neon. |
| 6 | The carnival | A clown's mouth is a door, and the vending machine is alive. |
| 7 | Space | You dug far enough down to arrive in space, and the alien is fine. |
