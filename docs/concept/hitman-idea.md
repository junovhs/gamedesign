[historical artifact, decided to develop essentially a full 2d hitman game, and then just change some names and stuff at the end of dev]

Make this: Room Service

A top-down pixel-art social-stealth game set entirely in one large, run-down luxury hotel.

You play a freelance contract killer during a chaotic three-day convention. Every contract gives you a target, optional conditions, limited starting gear, and several escape routes.

You enter through the lobby, but guests cannot access staff areas, therefore you steal or borrow a uniform. But the head housekeeper recognizes every employee, therefore you avoid her or create a problem that pulls her elsewhere. You reach the target, but they rarely stay alone, therefore you manipulate the hotel until their routine changes.

That is Hitman’s actual core:

Observe → gain access → manipulate routines → create an opening → act → escape

The entire game is one building

Not one tiny room. One dense, reusable location:

Lobby and bar
Kitchen and restaurant
Guest-room hallway
Six usable hotel rooms
Maintenance basement
Security office
Laundry room
Roof
Rear alley

The map should feel bigger than it is because doors, elevators, stairs, staff passages, windows, dumbwaiters, and locked rooms connect it in different ways.

Use top-down pixel art with cutaway interiors. You need one tileset, one shared character body, modular clothing, and a controlled number of props.

The toy

Before making the campaign, build the social-stealth toy:

NPCs follow visible routines.
Clothing grants access to particular areas.
NPCs investigate sounds and disruptions.
Objects can distract, poison, disable, unlock, conceal, or cause accidents.
Actions change schedules.
The player can watch a situation develop and interfere at the right moment.

A good five-minute toy might be:

A guest repeatedly leaves their room to get ice.
You can break the ice machine, therefore they call maintenance.
The maintenance worker enters their room, therefore you can take his uniform or hide inside his tool cart.
But the guest complains to management, therefore security begins walking through the hallway.

That chain is the game. The murder is just the final punctuation.

A practical cast

Start with about 14 active NPCs:

Hotel manager
Receptionist
Bartender
Cook
Waiter
Housekeeper
Maintenance worker
Security guard
Five guests
One target

Each NPC only needs:

A home location
A short routine
An access level
A few reactions
Recognition rules
One or two personal hooks

You do not need realistic artificial intelligence. You need readable clockwork.

Reusable systems

Build roughly eight systems that overlap:

Electricity
Water
Fire alarms
Food and drinks
Phones and room service
Doors, keys, and staff access
Security cameras
NPC schedules

One action should affect several systems.

For example, cutting electricity disables a camera, but it also summons maintenance and causes guests to leave dark rooms. That creates both an opportunity and a new obstacle.

Contract content

The hotel can support 10–20 hours if contracts meaningfully change the situation.

Authored campaign

Around 10 main contracts, each lasting 20–45 minutes:

Eliminate a guest without entering their room.
Kill two targets during a secret meeting.
Make a death appear accidental.
Recover blackmail material before leaving.
Eliminate the target while wearing a particular disguise.
Avoid harming hotel staff.
Complete the contract after security has been warned about you.
Kill a target who changes rooms whenever something suspicious happens.

Contracts can change:

Which rooms are occupied
Who attends the hotel
Which doors are locked
Which employees are working
Target routines
Security placement
Available tools
Special events in the restaurant or ballroom
Freelancer-style mode

After the campaign, remix the authored pieces:

Random target
One complication
One optional condition
Limited equipment
Equipment lost on failure
Money used to buy starting tools

Do not generate entire levels. Recombine tested people, routes, objects, and conditions.

Five disguises are enough
Guest
Housekeeping
Kitchen staff
Maintenance
Security

Each changes access, but also creates risks.

Maintenance can enter utility rooms, but cannot loiter in guest rooms. Security can carry weapons, but staff members notice unfamiliar guards. Housekeeping can enter rooms, but the head housekeeper can expose you.

That is cheaper and more interesting than producing twenty costumes.

Six tools are enough
Lockpick
Wrench
Sedative
Poison
Noise maker
Wire or compact weapon

Most special eliminations should use objects already in the hotel:

Bathtub
Elevator
Stove
Chandelier
Laundry machinery
Faulty wiring
Rooftop water tank
Food service cart

This reduces asset work because the environment itself is your weapon set.

What to cut

Do not include:

Gunfights as a full combat system
Hundreds of NPCs
Advanced dialogue trees
Physics simulation
Fully dynamic destruction
Procedurally generated architecture
Dozens of weapons
Realistic line-of-sight simulation
Large outdoor areas

When exposed, the player can shove, stun, hide, or flee. They are not meant to clear the building with a rifle.

First playable version

Build only:

Lobby
Hallway
Two hotel rooms
Maintenance closet
Six NPCs
Two disguises
One target
One accident
One direct method
One hidden route
One escape

The target moves between their room and the bar.

The player can:

Steal a housekeeping uniform
Enter the target’s room
poison room service
cause an electrical accident
distract the guard
escape through the alley

Make that one contract highly readable and satisfying. Then replay it with three different target routines and restrictions.

The test is:

After completing the contract once, does knowing the hotel make the player eager to try a cleaner, stranger, or riskier solution?

That is the smallest version of Hitman that still feels like Hitman.
