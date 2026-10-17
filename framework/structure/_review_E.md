# Stage 2 domain review: E Play, Sport & Music (E1 to E4)

*Batch S2R_E. Cold, offline review (no web, no git) of memos framework/structure/E1.md to E4.md and their sources files verify/out/S2_E1_sources.tsv to S2_E4_sources.tsv, against BRIEF.md, framework/CATEGORIES_v0_6.md, framework/STAGE2_MEMO_TEMPLATE.md and the draft shared conventions C1 to C13 in framework/structure/_conventions.md. The conventions were written after these memos, so every memo is also checked against them and the changes it needs are listed (section 3). This is a reviewer's judgement, not an owner decision. Severity: **high** = breaks a shared rule (BRIEF, Appendix A, a convention) or would file the same object in two places across many objects; **medium** = one rule break, one contradiction or a clear split; **low** = wording, evidence or tidy-up.*

**Mechanical checks.**
- *Sources match.* E1 cites S1 to S36, and the TSV has 36 rows in the same order. E2 uses 31 source tags (DEC-UK to NMAH), and the TSV has 31 rows, one per tag. The memo has no URL key, so a tag must be matched to its host by hand. E3 cites full URLs inline, and all 37 are in its TSV. E4 has a key table S01 to S37 with full URLs, and they match the TSV.
- *Depth and genre.* All four memos recommend at most four levels below the category (sub-family, leaf, kind, named form). None divides by content genre. E1 keeps BGG Type, theme and franchise off the tree.
- *Excerpt labelling.* Each memo labels what it read from search excerpts. E2 writes "(search excerpt only)", E4 uses a dagger mark (†), and E1 and E3 say they did not use unfetched hosts. E4 uses excerpts for structural claims more than the others (finding E4-8).
- *Owner interest.* Every memo puts brand depth in named forms and a maker ledger and never makes the maker a level. Three memos (E1, E2, E4) still attach a tier to a kind, which C4(a) now forbids.

## 1. Verdict table

| Code | Verdict | Top three issues |
|---|---|---|
| E1 Toys & Games | needs rework (the collectible half: figures, models, die-cast, trains) | (1) E1.2 splits "Model kits" from "Built models", which is the Appendix A modifier "how acquired" (the key says "built or not, ready-made or not"). Die-cast and train objects are split between E1.2 and E1.3 by market (collector or child). (2) The figure kinds mix three axes (scale class, sales channel such as prize figures, and single maker lines such as Nendoroid and figma), and a `tier` tag sits on the kind, against C4(a). (3) The trading-card kinds are packaging formats (booster pack, booster box, starter deck), although the memo calls blind boxes a sales-format tag. Objects the key names (toy instruments, piñatas, toy crowns and wands, play make-up) have no kind. |
| E2 Sports, Fitness & Recreation | minor fixes | (1) There is no rule for a kind used in sports from more than one family (helmet, mouthguard, knee pad, wetsuit, skipping rope, punch bag), so these objects split. (2) Tiers sit "on the kind", and ski-boot flex (a measured spec) is called a consensus tier, against C4(a) and C4(b). Platform pockets are unsourced and not in a C13 ledger. (3) Objects the key names have no sub-family (metal detectors, airsoft and paintball markers, caving and navigation gear, sledges, spearguns, dance shoes), and the "Camping" leaf contradicts the key's "'camping' is a setting". |
| E3 Musical Instruments & Music Gear | minor fixes | (1) "Recording & monitoring" and "Live sound & DJ" are split by setting, so one dynamic microphone, mixer or speaker has two homes. (2) "Church organ" is a kind named by setting (the memo itself calls church a setting modifier). Residual leaves ("Other winds", "Other plucked & fretted strings", "Mechanical & unusual") leave the accordion, harmonium, melodica and kalimba without a predictable home. (3) The cymbal types are kinds in 4b but named forms in the tree. "USB microphone" is a kind defined by connectivity (C10). Stratocaster and the generic "ST-type" overlap without a `maker_bound` rule (C2a). |
| E4 Weapons & Armour | minor fixes | (1) The sword leaves mix three axes (edge, hilt length, thrusting use), so a Zweihänder, a rapier or a katana fits two leaves. The kind list applies C11 to the sabre but not to the jian or the dao. (2) The knife leaves mix fixed or folding, use (hunting, throwing) and mounting (bayonet). The karambit exists in fixed and folding forms, and there is no axe kind although "axes" names the sub-family. (3) "Taser" is a kind named after a brand. Treating each cartridge as a kind conflicts with C6 and C13. NBTHK certificate grade belongs to one individual blade, which BRIEF puts out of scope. |

## 2. Findings by memo

Each finding gives severity, memo, evidence and an exact proposed fix. "Conforms to" names the convention that the fix applies.

### E1 Toys & Games

**E1-1 (high) Leaves and kinds split by how the object was acquired, by subject and by market.**
- *Evidence.* The E1.2 leaves are "Model kits" and "Built models". Step 25 of the key says "scale models, model kits and miniatures (built or not, ready-made or not)", and Appendix A lists "how acquired (bought ready-made, built from a kit, handmade)" as a modifier. The model-kit kinds also split by subject: "Plastic scale model kit" (Airfix, Tamiya), "Plastic car model kit" (AMT) and "Character plastic kit" (Gundam). Yet section 7 says "subject genre never a level". "Die-cast collector car" (E1.2) and "Die-cast toy car, 1:64" (E1.3) differ only by the maker's market, and the memo says so ("The line is the maker's market, which is not a test"). "Model locomotive" (E1.2) and "Toy train set" (E1.3) split in the same way.
- *Objects that would split.* A Hot Wheels Premium or Mini GT 1:64 car; a Bburago 1:18 car; a Hornby OO train set; a Bandai HG 1/144 Gunpla kit (scale kit or character kit); a Tamiya 1/24 car kit; a pre-built Airfix model.
- *Fix.* Merge models into one sub-family, "Scale models & model railways", whose leaf axis is the object modelled at scale, by its form: model vehicles (cars, aircraft, ships and armour, sold as kits or built); model railways (locomotive, rolling stock, track, train set, scenery kit); figure kits (garage kits, plastic figure kits). Within model vehicles, kinds are "scale model vehicle kit" and "die-cast scale model" (die-cast is the form, because a die-cast model is made only built). Built or kit, subject (car, aircraft, character), material and scale are attributes. E1.3 keeps only play vehicles that are not to scale (push-along, pull-back, wooden and plastic toy vehicles, ride-ons, RC and slot cars). Hot Wheels and Matchbox 1:64 become named forms under "die-cast scale model" with the scale attribute "1:64". A "toy" view is generated from `user` tags and the scale. A "Train set (starter set)" is one kind under model railways. A wooden toy railway (Brio) stays in E1.3 as "wooden toy railway", because it is not built to a scale and its track system is a C13 platform.

**E1-2 (high) The figure kinds mix scale class, sales channel and single maker lines, and a tier sits on the kind.**
- *Evidence.* The figure kinds are 1:12 action figure, 1:6 collectible figure and statue scale (a scale class); PVC scale figure 1/7–1/10 (a scale class with a "pre-posed" form); prize figure (a sales channel: "arcade/Ichiban Kuji origin"); "Chibi figure with swap parts (Nendoroid)" and "Poseable character figure, 20+ joints (figma)" (each the product line of one maker, Good Smile/Max Factory); and designer vinyl figure (a material and a scene). Section 5 then proposes "a tier tag on the kind (entry, mid, premium, statue)". C4(a) says "A `tier` never sits on a kind". Channel is close to the Appendix A modifier "how acquired". The ladder rests on three small commercial blogs (heroalterego.com, prexhobby.com, yosimarket.com) and nowhere else.
- *Objects that would split.* Bandai S.H.Figuarts (about 1:12, highly articulated: action figure 1:12, or the figma-type kind); Good Smile Pop Up Parade (non-scale and low price: PVC scale figure or prize figure); Nendoroid Petite and Kotobukiya Cu-poche (Nendoroid-type or not); a Banpresto prize figure at 1/7; a Pop Mart Labubu (plush with a vinyl face: plush toy or designer vinyl figure).
- *Fix.* Use one axis per leaf (C5c). Leaf "Figures", with kinds by articulation and form: articulated action figure; static pre-posed figure (statue and scale figure together); chibi or super-deformed figure; designer or art-toy figure; toy animal and toy soldier figure; bobblehead. Scale (1:12, 1:6, 1/7, 1/4) is a required attribute (C6). "Prize" is a `sales_channel` attribute. Nendoroid, figma, S.H.Figuarts, Pop Up Parade and Marvel Legends become maker-bound named forms (C2a), held in C1's lines table under Good Smile, Max Factory, Bandai and Hasbro. The price ladder becomes C4 tier entries on those lines (scheme "collector format ladder", with the three blogs as sources), and C4(e) requires a second region's source before it enters the data.

**E1-3 (medium) The trading-card kinds are packaging formats, and the memo misreads BRIEF on single cards.**
- *Evidence.* The kinds are "booster pack", "booster box" and "starter or structure deck", from one UK shop (WooCards [S12]). Section 7 treats a blind box as "a sales format, a tag", yet a booster pack is a sealed random assortment in the same way. WooCards' own list also has Elite Trainer Box, Ultra Premium Box, tins and collector chests, which the tree does not place. The memo says "single cards are individual items, out under BRIEF". BRIEF puts out "individual unique items (a particular card…)". That rules out the particular card. It does not rule out the generic kind "trading-card-game card (single)", which owners hold by the thousand and which F3 also has to meet.
- *Objects that would split.* A Pokémon Elite Trainer Box; a Magic Commander precon deck; a One Piece double pack; a Yu-Gi-Oh! tin.
- *Fix.* Make two kinds under leaf "Trading card games": "trading-card-game sealed product", with `product_form` (booster pack, booster box, starter or structure deck, collection box, tin) as an attribute, and "trading-card-game single card". Each card or set is a C3 variant (`variant_type` = print or set) and never a kind. The game system (Pokémon TCG, Magic: The Gathering, Yu-Gi-Oh!, One Piece) is a maker-bound named form and a C13 platform, because its cards play only in that system. Correct the BRIEF reading in section 4b. Add a matching sentence on the F3 side (E1-10).

**E1-4 (medium) The games leaves mix axes, and the classic-game kinds are not consistent.**
- *Evidence.* The E1.4 leaves are "Board and classic sets", "Cards and tiles", "Trading card games, sealed product only", "Table-action and tabletop" and "Gambling equipment". These mix component form, product status and the purpose of play for stakes. "Table-action and tabletop" holds both table football and the Warhammer starter set. Rummikub sits under "Domino or tile set", while UNO, an equally proprietary game, gets its own "Proprietary card game" kind. Section 4b makes "deck pattern (French-suited, German-suited)" a kind. C11 makes a regional pattern a named form under a generic kind. Hanafuda, mahjong, carrom, crokinole and marble runs are not placed.
- *Fix.* Put the leaves on one axis, the component set owned (C5c): Board games (boxed board game, chess set, go set, shogi set, backgammon set, Othello set); Card games (standard playing-card deck, proprietary card game, flower-card deck *hanafuda*); Tile and dice games (domino set, mahjong set, proprietary tile game, dice set); Trading card games (E1-3); Miniatures games (starter set, army or unit box); Table and cabinet games (table football, air hockey, pinball machine, carrom board, crokinole board); Casino and gaming equipment. Under C11, French-, German-, Spanish- and Italian-suited decks and regional tarock packs are named forms of "standard playing-card deck", tagged with their region. Hanafuda and mahjong stay kinds (C11: no generic kind covers a 48-card flower deck or a 136- or 144-tile set), labelled "flower-card deck (hanafuda)" and "mahjong tile set". Rummikub moves to "proprietary tile game". State that the chess, go and shogi sets are kinds (not named forms) because they are sold and compared as their own categories (C2c; [S14][S27]).

**E1-5 (medium) Objects the key names have no kind, and E1.6 is a catch-all.**
- *Evidence.* Step 25 names toy instruments (also the step 22 note), piñatas, "dress-up accessories made as toys (toy crowns, wands, play make-up)", gambling equipment and coin-operated games. The tree has no kind for toy instruments, piñatas, play make-up or mechanical banks (which the Strong lists [S35]). E1.6 "Pretend, Action & Novelty Toys" holds an infant play mat, a spinning top and a fidget toy, which share no stated axis. Kites, flying discs, toy balls and bubble toys are left as an open question.
- *Fix.* Split E1.6 into "Role play & dress-up" (play kitchen, toy shop and tool sets, toy dress-up accessory, play make-up set, toy weapon: blaster, play sword, foam replica), "Musical & sound toys" (toy instrument, musical pull-toy), "Infant & early play" renamed by form, not age, as "Rattles, stackers & activity toys" (rattle, stacking toy, activity play mat, shape sorter), "Skill & motion toys" (spinning top, yo-yo, fidget toy, kite, flying disc, toy ball, bubble toy, water toy) and "Party & novelty toys" (piñata, magic set, mechanical bank). The E2 side states the toy/sport cut for kites, discs and balls (cross-memo finding X5).

**E1-6 (medium) The level-1 axis is stated as play action, but the sub-families are named by form.**
- *Evidence.* The level-1 axis is "what the owner does with it", but E1.1 "Dolls, Figures & Plush" and E1.3 "Toy Vehicles & Ride-ons" are object forms. A dollhouse sits in the leaf "Soft toys and playsets".
- *Fix.* Restate the level-1 axis as "play family (the form-and-play group buyers shop first: dolls and figures, construction, models, play vehicles, games, puzzles, role play, play equipment)". That is what Hamleys, Galaxus and Circana show [S1][S5][S29]. Move the dollhouse to a leaf "Dolls' houses & doll accessories" under Dolls.

**E1-7 (medium) Parts and accessories have no sub-family (C5d).**
- *Evidence.* S3 sends doll clothes, dolls' prams, TCG sleeves and binders, poker-chip cases and railway controllers to E1. The memo mentions them only in passing.
- *Fix.* Add a closing sub-family "E1.9 Parts and accessories made for one toy or game" (doll clothes and shoes, dolls' pram, card sleeve, deck box, card binder, poker-chip case, model-railway controller, replacement game pieces), exempt from the level-1 axis (C5d). Model-railway track stays a kind under model railways, because it is a part of the railway itself.

**E1-8 (medium) The material kind and the platform field.**
- *Evidence.* Section 7 makes "porcelain" a doll kind, but material is a modifier "unless it is the form". The "platform key" is a field on the kind or named form, not the C13 ledger. Scale and gauge (OO, N, HO, O) are "required platform attributes".
- *Fix.* "Porcelain doll" becomes "bisque or porcelain doll" only if the owner accepts that the material is the form (head and body cast as one, as for antique bisque dolls). Otherwise "collector doll" takes material as an attribute. Put LEGO System, Duplo, Technic, Brio track, Playmobil, Toniebox, each TCG system and each railway scale and gauge in the C13 ledger (`platform_id`, `owner`, `kinds_served`, `standard_ref`: NEM 010 and NMRA S-1 for gauges, which still need fetched sources). Named forms link to the ledger.

**E1-9 (low) Evidence that rests on one source or one region.**
- The TCG product forms come from one UK shop [S12]. Casino equipment comes from two US suppliers [S13][S14]. Doll types come from one blog [S26]. Model-railway scales come from one UK shop [S22]. China is represented by Pop Mart alone. *Fix.* Before harvest, attest each with a second source from another region: a Japanese TCG shop (Yuyutei), a European casino supplier, NEM/NMRA pages, and a Chinese or Korean toy retailer.

**E1-10 (low) Boundary sentences to complete.**
- *Fix.* (a) Add to section 9 (with F3): "A trading-card-game single card is E1 as the kind; a card made for collecting with no game is F3; the particular card is an individual item and out." (b) For trampolines (with E2): "A trampoline with a frame of about 1.2 m or less, with or without a handlebar, sold for exercise (rebounder) is E2; a garden or play trampoline is E1." This needs a fetched source for the cut. (c) Hobby-grade RC and FPV drones: E1 when sold as RC toys or hobby models, D4 when made for filming (step 24, D4 branch).

**E1-11 (low) Order.** Section 8 orders figure scale large to small (statue, 1:6, 1:12) and railway scale small to large. *Fix.* Use one direction (smallest ratio first) and state it as the secondary key (C7). Named forms go by maker, then first year (C7). That is already the memo's practice.

### E2 Sports, Fitness & Recreation

**E2-1 (high) A kind used across sport families has no single home.**
- *Evidence.* Section 3 fixes only kinds shared within one family: "each family may have a 'general (any sport in this family)' leaf". Many E2 kinds cross families: helmets (skiing, climbing, ice hockey, horse riding), mouthguards (boxing, rugby, hockey), knee pads (volleyball, skateboarding, goalkeeping), shin guards (football, field hockey, kickboxing), wetsuits (surfing, diving, triathlon, kayaking, which is G1), goggles (swimming, triathlon), skipping ropes and punch bags (boxing and fitness), crampons (mountaineering, ice climbing, hiking), snowshoes (hiking, winter sports), gymnastic rings (gymnastics, strength training). Two builders would put each of these in different leaves.
- *Fix.* Add a tie-break to section 3 and to the shared conventions (proposed C14, section 3 below):
  - (1) A kind goes to the leaf of the sport whose rules or standard define it, if there is one (fencing mask: FIE; climbing helmet: UIAA 106 and EN 12492, a source to fetch).
  - (2) Otherwise it goes to the family "general" leaf when all its sports are in one family (ski goggles: Snow and ice, general).
  - (3) Otherwise it goes to a category-level sub-family "Multisport, fitness and protective gear", with leaves by body region protected or by function (mouthguard, knee pad, shin guard, sports goggles, skipping rope, punch bag).
  - A generated view lists the kind under every sport that uses it.

**E2-2 (high) Tiers sit on kinds, and measured specs are called tiers (C4a, C4b).**
- *Evidence.* Section 5 records tiers "as a modifier on the kind or named form". It calls ski-boot flex a consensus tier, although flex is a number measured on the object ("not standardized between boot manufacturers", EVO-SKI). Cricket-bat Grades 1 to 4 rest on one Australian retailer (PSC) and are judged on grain count and blemishes, which can be checked on the object. Golf-iron categories are a convention that GL and MGS both say overlaps. The cricket-bat line in the tree reads "grade 1 to 4 tier", which puts a tier on the kind.
- *Fix.*
  - Measured specs are attributes with their scale named (C4b): racket head size and weight, badminton U-weight, ski width and radius, ski-boot flex index ("maker scale", not comparable across makers), wetsuit thickness, rod power and action, cricket willow grade ("retailer convention", source PSC plus a second source). Golf-iron category is an attribute with two sources.
  - Maker ladders (adidas Elite, Pro, League and Club; Yonex series) are C4 tier entries on lines in C1's lines table (scheme = maker).
  - FIE homologation and UIAA standards are `certified_to` attributes, not tier entries.
  - Delete "tier" from the cricket-bat line.

**E2-3 (medium) Objects the key names have no sub-family, and "Camping" contradicts the key.**
- *Evidence.* Step 26 names metal detectors, caving and navigation gear, sledges, kick scooters, hang gliders and paragliders, spearguns, airsoft and paintball markers, fitness trampolines, combat-sport implements and dance shoes. The 15 proposed sub-families have no home for metal detecting, airsoft and paintball, caving or navigation. Dance appears in the family list ("athletics, gymnastics and dance") but not in the tree. Spearguns have no fishing leaf. The step 26 note says "'camping' is a setting", yet "Camping" is a leaf.
- *Fix.*
  - Add these leaves: "Airsoft & paintball" under Combat sports, renamed "Combat & target-shooting sports" (airsoft marker, paintball marker, mask, hopper); "Spearfishing" under Fishing; "Caving" and "Orienteering & navigation" (compass, map case) under Climbing & mountaineering, renamed "Climbing, caving & navigation"; "Metal detecting" under Hiking, camping & trail (metal detector, pinpointer, digging tool); "Sledging" under Snow & ice; "Dance" under Athletics, gymnastics & dance (ballet shoe, pointe shoe, tap shoe, dance practice wear); "Air sports" (hang glider, paraglider, harness, reserve parachute).
  - Rename the leaf "Camping" to "Shelter & sleep" (tent, tarp shelter, bivvy bag, sleeping bag, sleeping mat), so that the leaf is named for the objects' job and not the setting.

**E2-4 (medium) Platform pockets are unsourced and are not in the C13 ledger.**
- *Evidence.* Section 6: "Platform pockets (not attested by a fetched page in this batch …): ski boot sole standards against binding type, cycling cleat systems against pedals, golf shaft-to-head fit … belongs in an attribute of the part".
- *Fix.* Record them in the C13 compatibility ledger, not as attributes. Rows: ISO 5355 alpine sole, ISO 9523 touring sole, GripWalk, Tech/pin touring inserts (bindings and boots); SPD, SPD-SL, Look Kéo (cleats, pedals and shoes, with the pedals in G1 and the shoes in E2); golf adapter-sleeve systems by maker. Each row needs a fetched source before use (S6).

**E2-5 (medium) Maker ledger, lines and variants (C1, C3).**
- *Evidence.* The memo's columns are "maker, known-for kinds, sport leaves, scene tags, tier (consensus), price band, country, era, own-brand-of-retailer flag". Series (Astrox, Predator) are named forms, and the model year is "a view or an attribute".
- *Fix.* Adopt the C1 core. The own-brand flag becomes `maker_class` = retail own-label (Decathlon's Kipsta, Quechua and Kalenji become maker rows with `parent_id` = Decathlon). "Sport leaves" is derived from `known_for_kinds`. Series go to the lines table (`line_id`, `maker_id`, kinds spanned, tier entries). A model year or colourway is a C3 variant (`variant_type` = reference or colourway, `year`).

**E2-6 (medium) Two families, and the general leaf, are underspecified.**
- *Evidence.* (a) "Hiking, camping and trail" and "Climbing and mountaineering" share crampons, ice axes and helmets. (b) "Water sports" has a general leaf (wetsuit), and its SUP, bodyboard and kite-sport kinds have no stated home (kite sports are listed as "narrow"). (c) The memo admits the family level is "an editorial choice" ("No two sources use the same families").
- *Fix.* State the leaf axis of each sub-family in its definition (C5c), and list the general leaf as the first leaf of each family. Put kitesurf and wing-foil kites under "Water sports: kite & wind sports" and land kites (for traction kiting) under Air sports. Under C5(b), a family of about 12 kinds or fewer (for example Equestrian, after B10 takes tack) skips the leaf level.

**E2-7 (low) Order of named forms differs from C7.** Section 8 orders named forms "by maker series, then spec order where a number exists, then year", and puts "the certified form first". *Fix.* Follow C7: maker, then first-introduction year, then alphabetical. Spec order becomes a sort option in generated views. The memo's role-in-play order of kinds (implement, ball, fixture, protection, garment, footwear, aids) can stay as the stated secondary key.

**E2-8 (low) Evidence.**
- Several structural claims rest on excerpts or single sources:
  - SidelineSwap's category lists (excerpt only);
  - GolfWRX forum sections (excerpt only);
  - GS1 GPC (excerpt only, and not used);
  - ski use classes (one Czech rental shop, SKI-CZ);
  - cricket grades (one Australian retailer);
  - rod power and action, ski-boot flex and wetsuit thickness (one US source each).
- The Google taxonomy was read through a third-party mirror (wisepim.com), not Google's own file.
- The memo cites tags, not URLs.
- *Fix.* Add a URL key table, as E4 has. Give each spec scale used as an attribute a second source (for example a European retailer for wetsuits, a Japanese shop for rods). Fetch Google's own taxonomy file if the owner allows it.

**E2-9 (low) Installation and mounting (C12).** Basketball hoops (in-ground, wall-mounted, portable), pull-up bars (doorway, wall) and table-tennis tables (indoor, outdoor) are the same body with different fixings or settings. *Fix.* State that mounting and setting are attributes here (C12), so that none becomes a kind.

### E3 Musical Instruments & Music Gear

**E3-1 (high) Two gear sub-families are split by setting.**
- *Evidence.* E3.3 "Recording & monitoring" holds microphones, audio interfaces and studio monitors. E3.4 "Live sound & DJ" holds PA speakers, DJ controllers and DJ turntables. The memo itself notes "Studio monitor and PA speaker differ by setting". Appendix A lists setting as a modifier.
- *Objects that would split.* A Shure SM58 dynamic microphone (stage and studio); a Behringer X32 or Yamaha MG mixer; a wireless microphone system; in-ear monitors; a powered speaker used for both; a Novation Launchpad or Akai MPC (controller or instrument).
- *Fix.* Replace E3.3 and E3.4 with one sub-family, "Sound capture, mixing & reproduction". Its leaves go by job: Microphones & wireless systems; Mixers & audio interfaces; Loudspeakers & monitors; Headphones & in-ear monitors; Signal processors (rack compressors, EQs and DI boxes); DJ equipment (DJ turntable, DJ controller, DJ mixer, CDJ-type media player); Controllers (MIDI keyboard controller, pad controller, control surface). Studio monitor and PA speaker stay two kinds under Loudspeakers, because their bodies differ (near-field cabinet against pole-mount or flown cabinet), as C12(a) allows. The use (studio, stage) becomes a `use` tag.

**E3-2 (medium) A kind named by setting, and residual leaves.**
- *Evidence.* "Church organ" is a kind, although section 7 says "Church and sacred: setting modifier". The residual leaves "Other winds" (harmonica, bagpipes, accordion), "Other plucked & fretted strings" (ukulele, banjo, oud, sitar, koto; the koto is a zither and the oud is fretless) and "Mechanical & unusual" (music box, musical saw) leave these unplaced: melodica, harmonium, shruti box, concertina, kalimba, mbira, theremin, Hammond organ.
- *Fix.*
  - Rename the kind "church organ" to "pipe organ", and add "electronic organ" and "tonewheel organ" (Hammond) under Keyboards.
  - Make the leaf axis under Instruments the playing family stated by sound production and interface. Leaves:
    - Keyboards (piano, harpsichord, organs, digital piano, stage piano);
    - Synthesizers & electronic instruments (keyboard synth, desktop synth, modular synth module, drum machine, sampler, groovebox, theremin);
    - Guitars & basses;
    - Lutes & other plucked strings (ukulele, banjo, mandolin, oud, sitar, shamisen);
    - Zithers & harps (koto, guzheng, hammered dulcimer, harp, autoharp);
    - Bowed strings;
    - Woodwinds (with bagpipes);
    - Brass;
    - Free-reed instruments (harmonica, accordion, concertina, bandoneon, harmonium, melodica, shruti box);
    - Drums & percussion;
    - Mechanical instruments (music box, player piano roll mechanism);
    - Other idiophones, including the musical saw.
  - A free-reed leaf ends the accordion dispute in decision 6 on a sound-source rule that customs (HS 9205) and H-S already use.

**E3-3 (medium) Cymbal types are kinds in 4b but named forms in the tree.**
- *Evidence.* Section 4b says "cymbal types (ride, crash, hi-hat, China, splash) are the one place the type is itself compared and sold". Section 3B's example reads "Drums & percussion > cymbal > hi-hat", and the tree has one kind, "cymbal".
- *Fix.* Make crash, ride, hi-hat pair, splash and China cymbal kinds. Zildjian A, K and Sabian AAX become named forms (C1 lines).

**E3-4 (medium) Kinds defined by connectivity or format (C10, C13).**
- *Evidence.* Section 4b lists "USB" as a microphone construction type. The kind "modular synthesizer (Eurorack)" names a format standard. The effect kinds are named "overdrive pedal" and "delay pedal", although 4b says "format (pedal vs rack)" is an attribute.
- *Fix.*
  - USB output is a connectivity attribute: a USB condenser microphone is a condenser microphone with `connectivity` = USB (C10). Its E3/D1 home follows the step 22 note (made for music against made for speech or streaming).
  - Rename the kind "modular synthesizer module" and record Eurorack, Buchla 4U and Moog 5U in the C13 ledger (also MIDI DIN/TRS and API 500-series modules).
  - Rename the effect kinds "overdrive effect", "delay effect" and so on, with `format` (pedal, rack, desktop) as an attribute.

**E3-5 (medium) Maker-bound named forms overlap with generic design families (C2a).**
- *Evidence.* The tree puts *Stratocaster*, *Telecaster*, *Les Paul* and *SG* under solid-body electric guitar. Ishibashi and Digimart file by generic design family ("ST type", "TL type", "Les Paul type"), which many makers build [Ishibashi, Digimart]. *Dreadnought* is a non-maker-bound form. A Squier, an Ibanez AZ or a Suhr Classic S would be filed as "Stratocaster" by one builder and as "ST-type" by another.
- *Fix.* Record two named forms where both exist: "S-type double-cutaway solid body" (`maker_bound: no`, originator Fender, alias スト/ST type in C9) and "Fender Stratocaster" (`maker_bound: yes`, in C1's lines table, linked to the design family by a `design_family_id`). C7 ordering then applies to each.

**E3-6 (medium) Tier fields and the maker types do not yet match C1 and C4.**
- *Evidence.* Section 5 proposes one `tier_band` field (starter, intermediate, professional, flagship or boutique) and one `maker_line` field. The pianobrands.org and pianoanswers.com ladders disagree, and every tier source is US-based (a1guitar.com, vintagevinylnews.com, brassandwinds.com, sharmusic.com). Section 6 proposes "maker type (brand owner, OEM factory, individual luthier, house or second brand), parent or designer brand". The memo's own evidence shows that "designed by" and "built by" are separate facts (Boston designed by Steinway and built by Kawai; Fender Japan built by FujiGen).
- *Fix.*
  - `maker_line` becomes C1's lines table.
  - `tier_band` becomes C4 tier entries (several per line, each with scheme and source, and the computed `disputed` flag).
  - The generic ladder gets a second-region source (C4e), for example a Japanese or German retailer's beginner/advanced/pro labels.
  - Map the maker types onto C1's `maker_class`: OEM factory = supplier; second brand = licensee or diffusion, with `parent_id`; individual luthier = artisan or atelier.
  - Propose a C1 extension for E3 (and for A5 and others): `built_by_maker_id` on the line, so that designer and builder are both recorded.
  - Country of build is a line attribute, not a tag.

**E3-7 (low) Order of named forms.** Section 8 orders named forms "by year of introduction" and rejects maker order. *Fix.* Follow C7: maker, then first year. Non-maker-bound design families (dreadnought, S-type) go by first attested year.

**E3-8 (low) Voice and size (C6).** The memo leaves open whether alto and tenor saxophone are kinds, while violin, viola and cello are kinds. *Fix.* Make voice or pitch members that are separate instruments kinds (soprano, alto, tenor and baritone saxophone; B-flat and bass clarinet; violin, viola, cello). Each has its own body, mouthpiece and reeds or strings, and Digimart lists them separately. Fractional sizes (3/4 violin, 1/2 guitar) are a size attribute (C6).

**E3-9 (low) Tradition-named kinds and C11.** Koto, sitar, oud, shamisen, djembe and cajon are kinds with region tags. *Fix.* Apply C11's label rule: "koto (Japanese long zither)", "sitar (North Indian long-necked lute)". Regional variants of one form become named forms with a region tag: bayan and garmon under accordion; Irish and Highland bagpipes under bagpipes. Instruments that buyers compare as their own category (guzheng, koto, gayageum: separate shops and tunings) stay separate kinds, and the reason is recorded (C2c). See cross-memo finding X6.

**E3-10 (low) Boundary sentences.**
- (a) Cables: the key files "cables … made to connect electronic devices (USB, HDMI, audio and charging cables, whatever device they serve)" in D1. The memo's sentence "an instrument cable is E3 only if it is made for one instrument" adds a test the key does not have. *Fix.* Instrument, microphone and patch cables are D1 by the key, unless the owner adds an exception (decision list below).
- (b) Fog and haze machines: the memo leaves them open. Proposed: B4 (decorative effects) or a new note. Owner question.
- (c) Classroom Orff instruments: E3 when tuned and made to be played as instruments; E1 when sold as toys (with E1-5).
- (d) Evidence gaps: tiers are US-only, and there is no Chinese or Indian retailer (the memo says so). Fetch one each before harvest.

