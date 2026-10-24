# E1 Toys & Games: decided tree

Category: E1 Toys & Games (domain E, Play, Sport & Music). Membership test (CATEGORIES_v0_7, step 25): made for play, or for a game of skill or chance played at a table, on a board or floor, or with cards, dice, tiles or tokens: toys, dolls, figures, puzzles, board, card, dice and tile games (including trading card games), tabletop and coin-operated games without a screen, casino and poker chips and other gambling equipment, toy vehicles and ride-on toys, scale models, model kits and miniatures (built or not), model railways, dress-up accessories made as toys, piñatas and children's play equipment; parts made for one toy or game follow it here (S3, sub-family E1.9). Structure (Candidate A, E-1): sub-family by play family (nine; E1.9 is the parts sub-family, exempt from the axis), then a leaf on one axis stated per sub-family (18 leaves in E1.1, E1.3, E1.5 and E1.7; E1.2, E1.4, E1.6, E1.8 and E1.9 have no leaf), then kind, then named form. Scale, subject, material, power source, `assembly` (kit or built), `sales_channel` (prize, blind box), age, character, franchise and licence are attributes or tags, never levels or kinds. Games are divided by the component set owned (E-9): mechanism, BGG Type and Category, theme, audience labels and complexity weight are at most an Interactive Entertainment link field; printed player count (`player_count`), playing time (`playing_time_min`) and box age (`min_age`, on every E1 named form) are attributes (section 14, E1-1 to E1-3); `faction` is an attribute of miniatures named forms (E1-4). Display groups follow framework/structure/navigation/groups.tsv (display only; the tree keeps the memo's sub-families and leaves). Memo kind numbers 21, 27 and 106 are retired (E-14, E-10, K-9) and have no id.

Ids (R-58): E1.n is a sub-family and E1.n.m a leaf; a kind is E1.n.m.kk, or E1.n.kk where a sub-family has no leaf.

## E1.1 Dolls, figures & soft toys
Leaf axis: the form of the figure played with or displayed. Display group: Dolls, figures & soft toys.

### E1.1.1 Dolls
Display group: Dolls.
- E1.1.1.01 Fashion doll: a styled doll with a slim adult-like or teen body, made to be dressed and posed.
- E1.1.1.02 Baby doll: a doll made to look like an infant or toddler, for nurturing play.
- E1.1.1.03 Ball-jointed doll: a doll whose limbs and torso are joined by ball joints on elastic or string, made for posing and customising.
- E1.1.1.04 Bisque or porcelain doll: a doll with head and body cast as one in porcelain or bisque, so that the material makes the form (E-14).

### E1.1.2 Figures
Kinds by articulation and form; scale is a required attribute; `sales_channel` (prize) and `assembly` (kit or built) are attributes (E-14). Display group: Figures (action, scale, chibi, designer, toy animals).
- E1.1.2.01 Articulated action figure: a figure with many joints made to be posed and played with or displayed in varied poses, in any scale.
- E1.1.2.02 Static pre-posed figure: a figure fixed in one pose, in any scale including statue scale, sold finished or as an unpainted figure kit to assemble and paint (`assembly: kit`); includes prize figures and loose miniatures sold outside a game-system box (E-11, E-14).
- E1.1.2.03 Chibi or super-deformed figure: a figure with an oversized head and small body, usually with swappable faces or parts.
- E1.1.2.04 Designer or art-toy figure: a figure made as a collectible art object, often vinyl, from a designer's or brand's own character, often blind-packed.
- E1.1.2.05 Toy animal or toy soldier figure: a small moulded figure of an animal or soldier made for pretend play.
- E1.1.2.06 Bobblehead: a figure with a head on a spring or pin so that it nods.

### E1.1.3 Soft toys
Display group: Soft toys & puppets.
- E1.1.3.01 Plush toy: a stuffed fabric toy, including teddy bears, plush pendants with a clip or chain, and figures with a stuffed fabric body even with a vinyl face (K-136).
- E1.1.3.02 Puppet: a figure worked by the hand, rods or strings to act out play.

### E1.1.4 Dolls' houses & playsets
Display group: Dolls' houses & playsets.
- E1.1.4.01 Dolls' house: a house or building made at doll scale to be furnished and played in.
- E1.1.4.02 Figure-and-scene playset: small figures sold with a scene, building or set of accessories for pretend play.

## E1.2 Construction toys
No leaf (`leaf = null`); kinds by system class, the way the pieces join; robot and coding toys sit here too (R-22). Display group: Building & construction (Bricks, construction sets, robot & coding toys).
- E1.2.01 Interlocking brick set: a set of plastic bricks or blocks that clip together by studs or tubes.
- E1.2.02 Metal construction set: a set of perforated metal strips and plates joined by nuts and bolts.
- E1.2.03 Wooden construction set: a set of wooden blocks, rods or boards for building.
- E1.2.04 Marble-run construction set: a set of parts that join into a track or tower for rolling balls.
- E1.2.05 Toy robot: a robot made as a toy for play (a kit made to teach science through experiments is C6; K-149, R-22). †
- E1.2.06 Coding toy: a toy made for play that teaches or plays programming by commands (K-149, R-22). †

## E1.3 Scale models & model railways
Leaf axis: the object modelled at scale, by its form (two leaves). Kit or built (`assembly`), subject, material and scale are attributes (E-7, E-14). Display group: Models, kits & model railways.

### E1.3.1 Model vehicles & machines
Cars, aircraft, ships, armour, mecha, and structures, terrain or dioramas for scale models or miniatures (section 14, E1-7). Display group: Model kits & die-cast models.
- E1.3.1.01 Assembly scale model: a model of a vehicle, machine or structure in plastic, resin or card, sold as a kit to assemble or pre-built; includes building, ruin, terrain and diorama kits sold for scale models or miniatures (`subject` = structure, terrain or diorama; E1-7).
- E1.3.1.02 Die-cast scale model: a metal model of a vehicle at any scale, from 1:64 pocket cars to 1:18 display models (E-10).

### E1.3.2 Model railways
Scale and gauge are required attributes and C13 platforms. Display group: Model railways.
- E1.3.2.01 Model locomotive: a powered model railway engine.
- E1.3.2.02 Model rolling stock: an unpowered model railway wagon, coach or carriage.
- E1.3.2.03 Model railway track: rails and points for a model railway.
- E1.3.2.04 Model railway train set: a starter set of locomotive, stock and track sold together. †
- E1.3.2.05 Model railway scenery kit: buildings, scenery or lineside accessories sold for a model railway (gauge or railway scale stated; not widened, E1-7).

## E1.4 Play vehicles & ride-ons
No leaf (`leaf = null`); play vehicles other than die-cast scale models, plus ride-ons, by how the child moves them. Display group: Play vehicles, RC & ride-ons (Toy vehicles, RC, slot cars & ride-ons); E1.4.03 and E1.4.04 are also shown on the Models group's hobby shelf (generated, home unchanged).
- E1.4.01 Push-along or pull-back toy vehicle: a plastic or wooden vehicle the child pushes or that runs by pull-back or friction.
- E1.4.02 Wooden toy railway: a wooden toy train with its wooden track system.
- E1.4.03 Radio-controlled vehicle: a car, boat, aircraft or hobby drone controlled by radio, sold as an RC toy or hobby model; includes combustion-engined hobby cars and camera-less toy drones (K-97, E-11).
- E1.4.04 Slot-car racing set: a toy car racing set with grooved track and hand controllers.
- E1.4.05 Ride-on car: a child-sized car pushed, pedalled or powered, that the child sits in.
- E1.4.06 Balance bike: a child's bike without pedals, pushed along with the feet.
- E1.4.07 Children's tricycle: a three-wheeled pedalled cycle for a young child (a children's pedal bicycle is G1, K-91).

## E1.5 Games
Leaf axis: the component set owned (E-9). Every published board, card, tile, dice or tabletop game is a maker-bound named form of its kind, publisher the maker, held in a C2(g) register (E-6, CV-45). Display group: Board, card & tabletop games.

### E1.5.1 Board games
Display group: Board games & classic board sets.
- E1.5.1.01 Boxed board game: a published game on a board or in a box with its own pieces; includes a spirit board made as a board game (K-114).
- E1.5.1.02 Chess set: a board and pieces for chess.
- E1.5.1.03 Go set: a board and stones for go (kind provisional until a seller category in a second region attests it, CV-27).
- E1.5.1.04 Shogi set: a board and pieces for shogi (kind provisional until a seller category in a second region attests it, CV-27).
- E1.5.1.05 Backgammon set: a board with checkers and dice for backgammon.
- E1.5.1.06 Reversi set: a board and two-sided discs for reversi; Othello is a maker-bound named form (R-23). †
- E1.5.1.07 Draughts set: a board and discs for draughts (checkers). †

### E1.5.2 Card games
Display group: Card games & playing cards.
- E1.5.2.01 Standard playing-card deck: a deck of regional-pattern playing cards (French-, German-, Spanish- or Italian-suited, tarock and French-tarot packs) sold for card play; size is an attribute (E-4, K-109).
- E1.5.2.02 Proprietary card game: a published card game with its own special cards.
- E1.5.2.03 Flower-card deck [hanafuda]: a 48-card Japanese or Korean flower-card deck (E-4). †

### E1.5.3 Tile and dice games
Display group: Tile & dice games.
- E1.5.3.01 Domino set: a set of domino tiles.
- E1.5.3.02 Mahjong tile set: a set of mahjong tiles (E-4). †
- E1.5.3.03 Proprietary tile game: a published game played with its own tiles.
- E1.5.3.04 Proprietary dice game: a published game played mainly with its own dice.
- E1.5.3.05 Dice set: a set of polyhedral or ordinary dice sold as a set. †

### E1.5.4 Trading card games
Display group: Trading card games.
- E1.5.4.01 Trading-card-game sealed product: a sealed pack, box, tin or ready-made deck of a trading card game; `product_form` (booster pack, booster box, collection box, tin, starter or structure deck) is an attribute.
- E1.5.4.02 Trading-card-game single card: a single card of a trading card game, as a kind; a graded card stays here, and a particular card is an individual item and out (C16, CV-33, F3-O3).

### E1.5.5 Miniatures games
Miniatures sold in a game-system box (E-11); `faction` is an attribute of their named forms (E1-4). Display group: Miniatures games.
- E1.5.5.01 Miniatures-game starter set: a box with miniatures, rules and accessories to start a miniatures game.
- E1.5.5.02 Miniatures-game army or unit box: a box of miniatures making up a unit or army for a miniatures game; faction boxes are its named forms (E1-5). †

### E1.5.6 Table, cabinet & dexterity games
Games of physical skill or chance played on a table or cabinet, with no screen (K-155). Display group: Table, cabinet & dexterity games.
- E1.5.6.01 Table football: a table with rods of players for a game of football.
- E1.5.6.02 Air hockey table: a table with an air cushion for a puck game.
- E1.5.6.03 Pinball machine: a coin-operated or home machine with flippers and a ball.
- E1.5.6.04 Claw crane, redemption game or other coin-operated game without a screen: a coin-operated amusement machine played without a screen (K-155).
- E1.5.6.05 Carrom board: a square board with pockets, played by flicking discs. †
- E1.5.6.06 Crokinole board: a round board with a central hole, played by flicking discs. †
- E1.5.6.07 Dexterity game: a game of physical skill with its own pieces (stacking, balancing, flicking).

### E1.5.7 Casino & gaming equipment
Equipment made for a casino game; "home game" or "casino" is a market modifier; legal classes go to the C17 ledger. Display group: Casino & poker equipment.
- E1.5.7.01 Poker chip set: chips sold as a set for poker or casino play.
- E1.5.7.02 Roulette wheel: a roulette wheel for casino or home play.
- E1.5.7.03 Gaming table: a table made for poker, blackjack, craps or baccarat.
- E1.5.7.04 Card shoe or shuffler: a dealing shoe or card shuffler.
- E1.5.7.05 Prize wheel: a spinning wheel for prizes or chance.
- E1.5.7.06 Raffle drum: a rotating drum for drawing raffle tickets.
- E1.5.7.07 Bingo set: bingo cards, balls, a cage or a caller sold for bingo.
- E1.5.7.08 Slot machine: a casino or skill-stop slot machine, whatever display it uses (K-155).

## E1.6 Puzzles
No leaf (`leaf = null`); kinds by puzzle form. Piece count, format and material are attributes. Display group: Puzzles (Jigsaw, 3D & mechanical puzzles).
- E1.6.01 Jigsaw puzzle: a flat picture cut into interlocking pieces.
- E1.6.02 Three-dimensional jigsaw puzzle: interlocking pieces that assemble into a solid shape.
- E1.6.03 Mechanical puzzle: a puzzle solved by manipulating its parts, including twisty, interlocking and disentanglement puzzles and puzzle boxes.

## E1.7 Role play & other toys
Leaf axis: the kind of play the toy is made for (pretend, sound, early handling, skill and motion, party and novelty); infant and preschool are user tags, not a leaf. Display group: Pretend play & other toys.

### E1.7.1 Role play & dress-up
Display group: Role play & dress-up.
- E1.7.1.01 Play kitchen: a child's kitchen with hob, oven or sink for pretend cooking.
- E1.7.1.02 Toy shop or tool set: a child's play shop, tool bench, tool set or similar pretend-work set, including play money sold for pretend play and a children's garden tool set that cannot do the job (K-120, K-179).
- E1.7.1.03 Toy dress-up accessory: a toy crown, wand, wings or similar piece made as a toy (K-123, K-130).
- E1.7.1.04 Play make-up set: make-up made as a toy.
- E1.7.1.05 Toy weapon: a foam dart blaster, water blaster, toy gun, play sword or foam replica, or a slingshot or blowgun made as a toy (K-84, K-86).

### E1.7.2 Musical & sound toys
Display group: Musical & sound toys.
- E1.7.2.01 Toy musical instrument: an instrument made as a toy that cannot do a real, tuned instrument's job (C15).
- E1.7.2.02 Musical pull-toy: a toy that plays a tune when pulled or pushed. †

### E1.7.3 Rattles, stackers & activity toys
Display group: Baby & activity toys.
- E1.7.3.01 Rattle: a handheld toy that rattles, for an infant. †
- E1.7.3.02 Stacking toy: rings, cups or blocks that stack. †
- E1.7.3.03 Shape sorter: a toy with shaped holes and matching pieces. †
- E1.7.3.04 Activity play mat: a mat with toys or a gym for floor play.
- E1.7.3.05 Bath toy: a toy made to float or splash in the bath.

### E1.7.4 Skill & motion toys
Display group: Skill & motion toys.
- E1.7.4.01 Spinning top: a top spun by hand, string or launcher, including battle tops.
- E1.7.4.02 Yo-yo: a spool on a string, spun down and back up by the hand. †
- E1.7.4.03 Fidget toy: a small handheld toy for fidgeting; shape variants do not make kinds.
- E1.7.4.04 Kite: a kite made as a toy that cannot do a sport kite's job (K-160). †
- E1.7.4.05 Toy flying disc: a disc thrown as a toy (K-160).
- E1.7.4.06 Toy ball: a ball made as a toy, not to a regulation standard (K-160). †
- E1.7.4.07 Bubble toy: a bubble-blowing toy.
- E1.7.4.08 Water play toy: a pool, beach or water toy. †

### E1.7.5 Party & novelty toys
Display group: Party & novelty toys.
- E1.7.5.01 Piñata: a hollow figure filled with sweets, broken at a party.
- E1.7.5.02 Magic set: a set of tricks and props for conjuring. †
- E1.7.5.03 Mechanical bank: a money bank with a mechanical action.
- E1.7.5.04 Toy light: a torch or nightlight shaped as a toy (K-162, R-22). †

## E1.8 Play equipment
No leaf (`leaf = null`); kinds by structure type (EN 71-8). Display group: Outdoor play equipment (Swings, slides, playhouses, trampolines & pools).
- E1.8.01 Swing set: a frame with swing seats.
- E1.8.02 Swing seat: a swing seat or hanging seat sold alone, without a frame.
- E1.8.03 Slide or climbing frame: a slide or climbing structure for children.
- E1.8.04 Playhouse: a rigid play house or treehouse for children.
- E1.8.05 Garden or play trampoline: a trampoline for play, larger than an exercise rebounder (K-159; the 1.2 m frame cut provisional until attested).
- E1.8.06 Paddling pool: a shallow pool made for play, up to 400 mm of water depth (EN 71-8, E-13).
- E1.8.07 Inflatable activity toy: an inflatable play structure or bouncer.

## E1.9 Parts and accessories made for one toy or game
No leaf; exempt from the sub-family axis (C5d, CV-17). A part made for one kind of toy or game follows it and goes here (S3), as does a display container made for one figure (a cabinet, shelf, box or tray for several is B1, K-9). Display group: Parts & accessories for one toy or game (Doll, card, casino, railway & game accessories).
- E1.9.01 Doll clothes and shoes: clothes or shoes made for dolls.
- E1.9.02 Dolls' pram: a pram or pushchair for dolls.
- E1.9.03 Card sleeve: a protective sleeve for individual playing or trading cards.
- E1.9.04 Deck box: a box made to hold a deck of cards. †
- E1.9.05 Poker-chip case: a case made to hold poker chips.
- E1.9.06 Casino table layout: a printed cloth layout for a casino game table.
- E1.9.07 Model-railway controller: a hand or digital controller for a model railway. †
- E1.9.08 Replacement game pieces and game accessories: spare or add-on pieces made for a game, including game money sold for one game (K-120).

## Precedence inside E1

1. Games are filed by the physical component set the owner holds (a board with pieces, a standard deck, a domino set, dice, a sealed trading-card product, a miniatures starter box, a wheel or table), never by mechanism, theme, audience or complexity; printed player count, playing time and box age are attributes of the game's named form, never kinds (E-9, section 14 E1-1 to E1-3).
2. Chess, go, shogi, backgammon, reversi and draughts sets are their own kinds (E1.5.1.02 to E1.5.1.07); every other published boxed game is a boxed board game (E1.5.1.01), and Othello is a named form of the reversi set (E1.5.1.06).
3. Hot Wheels, Matchbox and every other die-cast car are one kind, the die-cast scale model (E1.3.1.02), at every scale; there is no separate die-cast toy vehicle kind (E-10).
4. A figure kit (an unpainted figure to assemble and paint) is a static pre-posed figure (E1.1.2.02) with `assembly: kit`; a model of a vehicle or machine sold as a kit is an assembly scale model (E1.3.1.01). Kit or built does not change the kind (E-14).
5. Miniatures sold in a game-system box are miniatures games (E1.5.5.01, E1.5.5.02); loose miniatures sold outside a game-system box are static pre-posed figures (E1.1.2.02) (E-11).
6. A building, ruin, terrain or diorama kit sold for scale models or miniatures is an assembly scale model (E1.3.1.01, `subject` = structure, terrain or diorama); scenery sold for a model railway (gauge or railway scale stated) is a model railway scenery kit (E1.3.2.05); terrain packed in a game-system starter box is part of that box (E1.5.5.01) (section 14, E1-7).
7. A plush pendant with a clip or chain is a plush toy (E1.1.3.01); a figure pendant is filed by the figure kind of its form (E1.1.2); a figure with a stuffed fabric body is a plush toy even if its face is vinyl (K-136).
8. A trading-card-game pack, box, tin or ready-made deck is sealed product (E1.5.4.01); a single card, graded or not, is a single card (E1.5.4.02); a card sleeve (E1.9.03) or deck box (E1.9.04) follows the cards into the parts sub-family; a binder holding several cards is outside E1 (B1, K-9).
9. A pack sold for card play (tarock, French tarot, German-suited and other regional patterns) is a standard playing-card deck (E1.5.2.01); a flower-card deck is its own kind (E1.5.2.03) (E-4, K-109).
10. A spirit board made as a board game is a boxed board game (E1.5.1.01) (K-114).
11. Model-railway track is a model railway kind (E1.3.2.03), not a part; a part made for one toy or game (doll clothes, sleeves, deck boxes, chip cases, table layouts, railway controllers, a display container for one figure) goes to the parts sub-family E1.9.
12. A slot-car racing set (E1.4.04) is its own kind; a wooden toy railway with its wooden track (E1.4.02) is its own kind; a radio-controlled vehicle (E1.4.03) is its own kind whatever it models, including hobby drones and combustion-engined hobby cars.
13. A toy robot (E1.2.05) or coding toy (E1.2.06) made for play is E1.2; a toy that is a torch or nightlight is a toy light (E1.7.5.04) (K-149, K-162, R-22).
14. Pinball machines (E1.5.6.03), claw cranes and redemption games without a screen (E1.5.6.04) are table, cabinet and dexterity games; casino slot and skill-stop machines are gaming equipment (E1.5.7.08) whatever display they use (K-155).
15. A swing set (frame with seats, E1.8.01) and a swing seat sold alone (E1.8.02) are two kinds; a garden or play trampoline (E1.8.05) and a paddling pool for play (E1.8.06) are play equipment.
16. A toy made to imitate a sport, music or weapon object belongs here (for example E1.7.1.05, E1.7.2.01, E1.7.4.04 to E1.7.4.06) when it cannot do the real object's job to that object's own standard (C15).
