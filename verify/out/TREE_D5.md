# D5 Video Games: decided tree

Category: D5 Video Games (domain D, Electronics). Membership test: a games console, handheld (handheld gaming PCs such as the Steam Deck and ROG Ally included, with a PC operating-system attribute), controller, VR or mixed-reality headset (any headset that encloses the eyes), coin-operated video arcade machine, or a video game on any carrier or as a download, or a game-key card. Expansions, add-on packs and mods that add to one game are D5 with the game; in-game and platform items are I2 and game subscriptions and passes are I3; pinball machines, claw cranes, redemption games and casino slot machines are E1. Structure: sub-family (role of the object: machine, controller, game software on a carrier, downloadable content, part or accessory made for one game machine; the parts sub-family closes the list), then leaf (only in D5.1 and D5.2; D5.3, D5.4 and D5.5 store leaf = null), then kind (the physical or functional class buyers compare). Platform (PlayStation, Xbox, Switch and the rest) is never a level: it is the console model itself or an attribute held in the compatibility ledger. Game software is divided by carrier type and never by genre; game titles are not in the tree. Implementation (original hardware, emulation, FPGA), operating system, era, region, edition, colour, bundle and price band are attributes, variants, tags or views, not kinds.

Ids (R-58): D5.n is a sub-family and D5.n.m a leaf; a kind is D5.n.m.kk, or D5.n.kk where a sub-family has no leaf.

## D5.1 Game machines

Leaf axis: form of the machine (home, handheld, VR headset, arcade cabinet style, console add-on).

### D5.1.1 Home consoles

- D5.1.1.01 Carrier-based home console: home console on which the owner loads different games from a carrier, card, download or storage.
- D5.1.1.02 Dedicated home console: home console with built-in games that the owner cannot load (includes plug-and-play minis).

### D5.1.2 Handheld consoles

- D5.1.2.01 Carrier-based handheld: handheld in which games are loaded, not built in; the operating system is an attribute, so a handheld gaming PC is a named form of this kind with os = PC.
- D5.1.2.02 Hybrid console: console that works both docked to a TV and as a handheld.
- D5.1.2.03 Dedicated LCD handheld: handheld with its game built in on an LCD.

### D5.1.3 VR headsets

- D5.1.3.01 Standalone VR or mixed-reality headset: headset that encloses the eyes and has its own compute and battery. †
- D5.1.3.02 Tethered VR headset: headset that encloses the eyes and needs a console or PC as its host (host platform is an attribute). †

### D5.1.4 Arcade machines

- D5.1.4.01 Upright cabinet: coin-operated video arcade cabinet that stands upright, played standing.
- D5.1.4.02 Cabaret (mini) cabinet: smaller upright coin-operated video cabinet.
- D5.1.4.03 Cocktail table cabinet: coin-operated video cabinet built as a table, played seated across or beside it.
- D5.1.4.04 Sit-down cabinet (candy cabinet): coin-operated video cabinet with a seat for the player.
- D5.1.4.05 Cockpit or environmental cabinet: enclosed or motion cabinet built around the player.
- D5.1.4.06 Counter-top or bar-top cabinet: small cabinet made to stand on a counter or bar.

### D5.1.5 Console add-ons

- D5.1.5.01 Disk-drive add-on: unit that adds a disk drive to a console.
- D5.1.5.02 Cartridge converter: unit that lets a console play cartridges of another system or region.

## D5.2 Controllers and input devices

Leaf axis: type of input (the physical form of the controller).

### D5.2.1 Gamepads

- D5.2.1.01 Gamepad: hand-held controller with a directional pad, buttons and sticks or triggers, held in both hands.
- D5.2.1.02 Detachable split controller: controller made as two detachable halves that can be used apart.

### D5.2.2 Arcade sticks

- D5.2.2.01 Levered arcade stick: arcade-style controller with a joystick lever and buttons.
- D5.2.2.02 Leverless (all-button) controller: arcade-style controller with all-button directional input and no lever.

### D5.2.3 Wheels, pedals and sticks

- D5.2.3.01 Racing wheel: steering-wheel controller for driving games.
- D5.2.3.02 Pedal set: set of foot pedals sold as a controller.
- D5.2.3.03 Flight stick: joystick controller for flight games.

### D5.2.4 Pointing, motion and camera input

- D5.2.4.01 Light gun: gun-shaped pointing controller.
- D5.2.4.02 Motion controller: controller that senses its own movement in the player's hand.
- D5.2.4.03 Console camera: camera made to track the player as game input.

### D5.2.5 Music and body

- D5.2.5.01 Rhythm instrument controller: controller shaped like a musical instrument, made to control a game.
- D5.2.5.02 Dance or balance mat: floor mat or board that reads the player's steps or weight as game input.

## D5.3 Game software on physical carriers

No leaf (leaf = null). Kind axis: carrier type. The platform is a required attribute, never a kind; a platform's standard carrier format is a named form of its carrier-type kind.

- D5.3.01 Game disc: game on an optical disc.
- D5.3.02 Game cartridge: game on a cartridge holding memory chips.
- D5.3.03 Game card: game on a small flash-memory card.
- D5.3.04 Magnetic game media: game on a cassette, floppy or disk-system card. †
- D5.3.05 Game-key card: physical card that holds only a key to a game, not the game.
- D5.3.06 Download-code card or voucher: card or box that unlocks one game as a download.

## D5.4 Downloadable games and add-on content

No leaf (leaf = null). Kind axis: the content role relative to the base game.

- D5.4.01 Digital game licence: full game downloaded on a console or PC store, held with no carrier.
- D5.4.02 Expansion: downloadable content that adds a large part to a base game.
- D5.4.03 Add-on pack: downloadable maps, levels, characters, artbook or wallpaper content for a game.
- D5.4.04 Game mod: modification that adds to or changes one game. †

## D5.5 Parts and accessories made for one game machine

No leaf (leaf = null). Kind axis: shop class, in the order of the part's job (protection, power, storage, mounting and video, utility). The machine form served is the attribute serves and the fits relation.

- D5.5.01 Case or pouch: case or pouch made to hold or protect one game machine.
- D5.5.02 Screen protector film: film for the screen of one game machine.
- D5.5.03 Faceplate, skin or decal: cover plate, skin or decal that changes the outside of one game machine or controller.
- D5.5.04 Battery pack made for one machine: rechargeable battery pack made for one game machine or controller.
- D5.5.05 AC adapter: power adapter made for one game machine.
- D5.5.06 Charging stand or dock (charging only): stand or dock that only charges the machine or controller.
- D5.5.07 Proprietary cable or adapter: cable or adapter with a proprietary connector made for one console.
- D5.5.08 Proprietary memory card or expansion: memory card, drive or expansion in a format made only for one console.
- D5.5.09 TV dock: dock that gives video output to a TV as well as charging. †
- D5.5.10 Stand or mount: stand or mount made to hold one game machine.
- D5.5.11 Multitap: unit that adds controller ports to a console.
- D5.5.12 Cheat device: cartridge or unit that alters a game (Game Genie type).
- D5.5.13 Replacement part or repair tool: spare part or tool for repairing a game machine or controller.
- D5.5.14 Toys-to-Life portal or reader: portal or reader that reads Toys-to-Life figures for a game. †

## Precedence inside D5

- A Steam Deck, ROG Ally or other handheld gaming PC is a carrier-based handheld (D5.1.2.01) with the operating-system attribute os = PC.
- Any headset that encloses the eyes (VR or mixed reality, Apple Vision Pro included) is a VR headset: standalone (D5.1.3.01) when it has its own compute and battery, tethered (D5.1.3.02) when it needs a console or PC host.
- A console-and-game bundle, limited-colour console or collector's edition is the console (or game) itself; colour, limited edition and bundle are variants, not kinds. A disc and a Digital Edition of one console are the same kind.
- A machine with built-in games that the owner cannot load is a dedicated home console (D5.1.1.02) or a dedicated LCD handheld (D5.1.2.03); a machine that loads different games is carrier-based (D5.1.1.01, D5.1.2.01), whatever its implementation (original hardware, emulation, FPGA). A machine that works docked and handheld is a hybrid console (D5.1.2.02), not a home console.
- Form factor is a kind boundary where buyers never compare across it (home against handheld); it is an attribute where buyers compare across it inside one kind.
- A coin-operated video cabinet is an arcade machine (D5.1.4); a home replica cabinet such as an Arcade1Up model is an upright (D5.1.4.01) or counter-top (D5.1.4.06) cabinet with coin mechanism = no.
- A game-key card is a game-key card (D5.3.05) even though publishers count it as a digital sale: the kind follows the physical card. A card or box that unlocks one game is a download-code card or voucher (D5.3.06); a downloaded licence with no carrier is a digital game licence (D5.4.01).
- Game software is divided by carrier type, never by genre or platform; a platform's standard carrier format (PlayStation 5 Blu-ray, NES cartridge, Switch 2 game card) is a named form of its carrier-type kind (D5.3.01, D5.3.02, D5.3.03). Game titles are not kinds.
- A Kinect or other console camera is a controller (D5.2.4.03), not a part (D5.5). A controller shaped like an instrument, a dance mat or a balance board made to control a game is D5.2.5.
- A Game Genie or GameShark cheat cartridge is a cheat device (D5.5.12), not software.
- A memory card, drive or charging dock in a format made only for one console is a D5 part (D5.5.08, D5.5.06); a cable with a proprietary connector made for one console is D5.5.07; a charger made for one console is an AC adapter (D5.5.05). A dock that also gives video output is a TV dock (D5.5.09), not a charging stand.
- A Toys-to-Life figure is E1; its portal or reader is a part (D5.5.14).
- An expansion or add-on pack that adds to one game is D5.4.02 or D5.4.03, and a mod is D5.4.04; in-game and platform items (cosmetics, consumables, currencies) are I2.
- Phone clip-on controllers and other accessories made only for one phone are D2 parts, not D5.5; a clip-on or accessory made for consoles or computers that also takes a phone stays in D5.
- Emulation and FPGA machines, and every platform, are attributes or ledger rows; none is a kind.
