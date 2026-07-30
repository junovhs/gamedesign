## HUD and player information

| Thing                 | Class                      | Function                                                                                   | Design rule                                                                                                                                       | Priority |
| --------------------- | -------------------------- | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------- | -------- |
| Depth counter         | Information                | Shows absolute progress through the persistent hole                                        | The largest number because depth is the primary achievement                                                                                       | Core     |
| Pick icons            | Decision budget            | Shows remaining committed actions on the current board                                     | Spent picks remain visible as dark silhouettes                                                                                                    | Core     |
| Distance to next camp | Progress and navigation    | Shows physical distance to the next persistent underground base, such as `NEXT CAMP: 30 m` | Express distance in world units, not “screens remaining”; camps should feel like real places in the hole                                          | Core     |
| Inventory hotbar      | Inventory and active tools | Persistently shows carried resources, tools, consumables, and selected objects             | Items remain physically present in visible slots; the player can select, use, drop, rearrange, or swap them without opening a detached bag screen | Core     |
| Inventory capacity    | Carry constraint           | Limits what can be extracted or taken deeper                                               | Capacity should be communicated through available slots, item stacks, item size, or weight—not an abstract fullness bar                           | Core     |
| Money counter         | Currency                   | Shows spendable money using a coin icon and number                                         | Money remains separate from the physical inventory so it never consumes a slot                                                                    | Core     |
| Menu object           | Control                    | Opens pause, settings, accessibility, retreat, and save information                        | Use a bespoke object rather than a generic hamburger glyph; a literal hamburger is acceptable if it fits the game’s tone                          | Core     |

## Inventory model

| Element               | Function                                                                                 | Rule                                                                                                                                            | Priority |
| --------------------- | ---------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------- | -------- |
| Persistent hotbar     | Keeps the player’s available actions visible during play                                 | The selected item can be used directly on the board                                                                                             | Core     |
| Resource stacks       | Hold ordinary extracted materials                                                        | Common materials stack; unusual objects may not                                                                                                 | Core     |
| Tool slots            | Hold picks, chisels, ropes, balloons, explosives, and other devices                      | Tools compete for carried space unless equipped elsewhere                                                                                       | Core     |
| Large-object carrying | Represents fossils, furniture, creatures, and machinery that cannot fit in a normal slot | Large finds must be physically moved, dragged, supported, transported, or sent back separately                                                  | Core     |
| Drop action           | Places an inventory item into the current board                                          | Dropped objects become persistent physical objects and may participate in gravity or support                                                    | Core     |
| Rearrangement         | Allows the player to reorder visible slots                                               | Slot order determines quick access, not object power                                                                                            | Support  |
| Contextual use        | Applies the selected item to a valid cell, object, creature, or mechanism                | The preview must show the exact result before a consumable or limited-use device is committed                                                   | Core     |
| Overflow decision     | Resolves collecting an item when no space remains                                        | The player must leave something, drop something, consume something, or arrange transport; the game should not silently convert finds into money | Core     |
| Expanded storage      | Provides long-term storage at home and established camps                                 | Field inventory remains constrained even after storage upgrades                                                                                 | Major    |

## Surface and persistent home

| Thing                                        | Class                  | Function                                                                            | Connection to excavation                                                                | Priority |
| -------------------------------------------- | ---------------------- | ----------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------- | -------- |
| Backyard home base                           | Primary home           | The central base the player repeatedly returns to throughout the entire game        | It should remain more important, personal, and customizable than any underground camp   | Core     |
| House                                        | Service hub            | Banking, storage, crafting, equipment, wardrobe, records, and relationships         | Converts extracted resources and discoveries into long-term progression                 | Major    |
| Hole entrance                                | World connection       | Entry into the same persistent underground world                                    | It is never replaced by a conventional level-select screen                              | Core     |
| Surface lift or descent system               | Navigation             | Returns the player to sufficiently established underground routes                   | It should not erase the importance of travelling through and remembering the hole       | Major    |
| Trophy yard                                  | Collection display     | Displays objects, fossils, plants, machines, signs, and decorations recovered below | The surface becomes a visible record of this player’s particular excavation history     | Core     |
| Dog                                          | Companion              | Reacts to discoveries, returns, construction, and changes to the yard               | Primarily emotional continuity rather than an optimization system                       | Support  |
| Doghouse                                     | Home prop              | Establishes routine and ownership                                                   | May hold a small companion-related collection                                           | Dress    |
| Garden gnome                                 | Find and trophy        | Recovered underground and placed freely in the yard                                 | Demonstrates the entire find-to-display loop                                            | Major    |
| Pink flamingo                                | Decoration reward      | Bought, found, traded, or won                                                       | Valuable because the player wants it, not because it gives a statistical bonus          | Support  |
| Potted plants                                | Living trophies        | Grow or mutate according to underground biology brought home                        | Connect strange materials to visible long-term consequences                             | Support  |
| Fossil display or museum area                | Collection space       | Holds reconstructed multi-cell fossils                                              | Turns skilled preservation into permanent prestige                                      | Major    |
| Workshop area                                | Equipment space        | Builds, repairs, modifies, and displays physics tools                               | Makes new excavation verbs physically visible at home                                   | Major    |
| Player wardrobe                              | Customization          | Stores hats, boots, coats, packs, and protective equipment                          | Clothing communicates identity and available capabilities                               | Major    |
| Fence, mower, trees, house exterior, and sky | Environmental dressing | Preserve the ordinary suburban frame                                                | The surface remains recognizable while increasingly impossible objects accumulate there | Dress    |

## Camps and underground bases

| Element                 | Function                                                       | Rule                                                                                                                                         | Priority |
| ----------------------- | -------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------- | -------- |
| Camps                   | Sparse persistent underground bases                            | Camps provide storage, rest, equipment changes, selected services, and a reliable return point                                               | Core     |
| Camp spacing            | Makes reaching a new camp a major expedition milestone         | Camps should be separated by long stretches of excavation—potentially dozens or roughly a hundred screen-lengths—not placed every few boards | Core     |
| Camp distance readout   | Communicates long-term progress during a descent               | Show estimated physical distance, such as metres, to the next known camp                                                                     | Core     |
| Lateral placement       | Separates camps from the central descent path                  | Important camps can sit inside side passages or authored lateral regions that must be discovered and opened                                  | Major    |
| Camp establishment      | Allows some bases to be built rather than merely found         | Establishing a camp may require clearing a stable chamber, transporting supplies, restoring power, or helping a resident                     | Major    |
| Camp storage            | Lets the player offload inventory without returning fully home | Storage is practical but less expansive than the home-base collection and workshop systems                                                   | Major    |
| Camp loadout changes    | Supports deeper expeditions                                    | The player can swap tools and supplies stored at that camp but cannot access the entire home inventory remotely                              | Major    |
| Camp identity           | Makes each base memorable                                      | Each camp should have a resident, landmark, biome function, or story rather than being an identical checkpoint                               | Major    |
| Home-base primacy       | Preserves the meaning of returning to the backyard             | Camps extend expeditions; they never become interchangeable replacements for home                                                            | Core     |
| Temporary field shelter | Provides limited rest between major camps                      | A shelter may offer one narrow benefit but should not become a full save-and-storage base                                                    | Support  |

## World and board structure

| Element                   | Function                                                                  | Design rule                                                                                                      | Priority |
| ------------------------- | ------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------- | -------- |
| Structural board          | Compact local puzzle                                                      | Each screen presents a readable arrangement of supports, hazards, objectives, and possible collapses             | Core     |
| Persistent vertical world | Connects all boards into one excavation                                   | Damage, moved objects, dropped inventory, rescued residents, and opened routes remain changed                    | Core     |
| Lateral branches          | Contain camps, residents, resources, authored rooms, and optional puzzles | Branching should make the hole feel spatial rather than like a single linear stack of levels                     | Core     |
| Long expedition           | Creates planning beyond one board                                         | Inventory composition, available picks, camp distance, and carried finds matter across many screens              | Core     |
| Return journey            | Makes depth and preparation meaningful                                    | Reaching a camp or home with valuable physical objects should be part of the challenge                           | Major    |
| Depth measurement         | Gives the world physical scale                                            | Define a consistent approximate height per screen so metres communicate meaningful progress                      | Support  |
| Revisited board           | Supports later equipment and alternate solutions                          | Old screens remain usable routes, resource locations, unresolved puzzles, and places transformed by later events | Core     |
| Authored landmark         | Breaks up procedural or systemic boards                                   | Large rooms, residents, machines, fossils, and businesses occupy memorable fixed locations                       | Major    |

## Enterable rooms and authored encounters

| Location             | Function                                     | Relationship to the main boards                                                            | Priority |
| -------------------- | -------------------------------------------- | ------------------------------------------------------------------------------------------ | -------- |
| Skeleton room        | First inhabited discovery                    | Teaches that some spaces are authored interiors rather than terrain boards                 | Major    |
| Machine chamber      | Network puzzle                               | Uses pipes, plates, power, force, and structural terrain together                          | Major    |
| Fossil pocket        | Preservation challenge                       | Creates a board objective beyond simply descending                                         | Core     |
| Crystal alcove       | High-value destination                       | Makes the player plan a route toward a protected visible prize                             | Major    |
| First major camp     | First secondary base                         | A distant lateral milestone that materially extends expedition range                       | Core     |
| Mole Motel           | Resident-operated camp or service settlement | Can become one of the rare major underground bases rather than merely a frequent rest stop | Core     |
| Clown-mouth entrance | Door into carnival content                   | Signals that the world has become openly impossible                                        | Major    |
| Carnival chamber     | Rule-bending market and equipment region     | Introduces balloons, strange consumables, event objects, and underground spending          | Major    |
| Alien living room    | Late-game social chamber                     | Recontextualizes the descent through domestic normality                                    | Major    |
| UFO chamber          | Force-manipulation set piece                 | Uses tractor beams and the recurring cow storyline                                         | Major    |
| Rocket bay           | Endgame project or alternate exit            | Offers a destination other than returning upward                                           | Major    |

## World descent

| Region                | Dominant mechanical idea                         | Major discovery                    | Base structure                                                | Tone                        |
| --------------------- | ------------------------------------------------ | ---------------------------------- | ------------------------------------------------------------- | --------------------------- |
| Backyard              | Basic preparation, collection, and customization | The hole itself                    | Primary permanent home                                        | Entirely ordinary           |
| Topsoil               | Loose dirt and simple supports                   | Fossils beneath the lawn           | No full camp                                                  | Surprising but plausible    |
| Buried domestic layer | Fragile objects and inhabited rooms              | Skeleton having tea                | Minor shelter or service room                                 | Someone lived here          |
| Machinery layer       | Networks, plates, pressure, and power            | Skull-faced machine                | Candidate location for the first constructed camp             | Someone built systems here  |
| Mushroom cavern       | Organic growth and creature objectives           | Unexplained cow                    | Sparse natural refuge                                         | The world is alive          |
| Mole territory        | Lateral tunnelling and resident services         | Mole Motel                         | Major underground camp                                        | Society exists below        |
| Carnival              | Reversed force, events, and absurd consumables   | Clown doorway and balloons         | Specialized settlement or market, not necessarily a full camp | Physics becomes theatrical  |
| Space                 | Tractor beams and alien materials                | Alien living room, UFO, and rocket | Final distant outpost                                         | Geography no longer applies |

## Production priorities

| Order | Feature                                              | Why it earns the slot                                                                |
| ----: | ---------------------------------------------------- | ------------------------------------------------------------------------------------ |
|     1 | Structural collapse depth and exact preview          | Everything else depends on this remaining satisfying                                 |
|     2 | Persistent hotbar and physical inventory interaction | Items must be usable parts of play rather than values hidden behind a bag bar        |
|     3 | Multi-cell fragile objects                           | Creates extraction and transport puzzles without changing the game’s identity        |
|     4 | Push, anchor, lift, drop, and tether operations      | Expands the physics vocabulary beyond removal                                        |
|     5 | Sparse camp and expedition structure                 | Gives the persistent world long-range planning, geography, and meaningful milestones |
|     6 | Balloons                                             | Inverts the core rule in one instantly understandable object                         |
|     7 | TNT and sequenced force                              | Produces spectacular consequences that remain strategic                              |
|     8 | Persistent surface trophies and home customization   | Makes discoveries personally meaningful and keeps home central                       |
|     9 | Lateral branches and enterable resident rooms        | Gives camps, characters, services, and authored surprises a natural spatial home     |
|    10 | Creatures governed by board turns                    | Adds life and change without introducing generic combat                              |
|    11 | Resource properties, equipment, and crafting uses    | Creates Stardew-like breadth while continually serving excavation                    |
|    12 | Additional ore variants and environmental decoration | Valuable only after the systems they communicate exist                               |
