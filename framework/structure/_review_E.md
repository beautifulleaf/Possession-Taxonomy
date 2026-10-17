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
    - Mechanical instruments (music box, barrel organ);
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

### E4 Weapons & Armour

**E4-1 (high) The sword leaves mix three axes.**
- *Evidence.* The E4.4 leaves are "Straight double-edged swords", "Single-edged swords", "Thrusting swords" and "Two-handed swords". These mix edge, use and hilt length. Wikipedia [S13] gives hilt and blade as two separate cuts. The katana is single-edged and two-handed. The Zweihänder is straight, double-edged and two-handed. The rapier is double-edged and thrusting. The nodachi and the longsword are both two-handed.
- *Fix.* Use one leaf axis, blade profile:
  - straight double-edged;
  - single-edged, straight or curved;
  - thrusting (edgeless or narrow).
  - Hilt length (one-handed, hand-and-a-half, two-handed) becomes an attribute.
  - "Greatsword" moves to straight double-edged.
  - With about 12 kinds or fewer per leaf, E4.4 may skip the leaf level under C5(b).

**E4-2 (high) C11 is applied to the sabre but not to the jian or the dao.**
- *Evidence.* Section 3 makes "sabre" "a cross-cultural kind (single-edged curved cavalry sword); national patterns are named forms". Yet the jian sits beside the longsword, and the dao beside the katana, as kinds. C11: "Where a generic kind exists, the regional name is a named form under it, tagged with the region." By the memo's own logic, the dao (liuyedao, dadao) is a regional single-edged curved sword. The memo also says the sabre and rapier lack attestation (decision 15).
- *Fix.*
  - Kinds go by generic form, with the regional names as named forms and region tags: arming sword (jian, as a named form tagged China); longsword; greatsword; sabre (dao, shamshir, kilij, talwar, cavalry sabre: named forms with region tags); cutlass; rapier; smallsword.
  - The Japanese types (katana, tachi, wakizashi, ōdachi) stay kinds, under C2(c), because fetched dealers sell and compare them as their own categories [S10][S11][S30]. Their C11 label is "katana (Japanese long sword)".
  - Owner question: accept this asymmetry, or make "Japanese sword (nihontō)" one kind with length class and mounting as attributes (see E4-3).

**E4-3 (medium) Length classes and individual-item grades.**
- *Evidence.* Katana, wakizashi and tantō are separated by blade length in shaku ("arbitrary but necessary" thresholds [S30]). C6 says size is always an attribute. The tantō then moves to a different sub-family (E4.5) from the katana. NBTHK grades (Hozon to Tokubetsu Juyo) are certificates issued to one individual blade [S10]. BRIEF puts individual unique items out. The memo nevertheless proposes a modifier `certificate_grade`.
- *Fix.* Keep katana, wakizashi and tantō as kinds and record why: the length class names a different carried object and mounting set (daishō), and it is the first browse path of the trade [S10]. That is the C2(a) comparison test, not size alone. Keep the tantō in E4.4 with the other Japanese blades, and add a sentence that a tantō is a sword kind by tradition, so that its sub-family does not depend on length. Drop `certificate_grade` from the data model, because it belongs to an individual item. School and era stay tags.

**E4-4 (medium) The knife leaves mix form, use and mounting, and axes are missing.**
- *Evidence.* The E4.5 leaves are Daggers, "Fixed fighting and hunting knives", "Folding fighting knives", Throwing knives and Bayonets. The karambit is sold both fixed and folding (Blade HQ lists it as a "style" across types [S07]). E4.6 is named "Polearms, axes and impact weapons" but has no axe kind. The tomahawk, battle axe, flail, rope dart and three-section staff (counted in section 4) are not placed. The bō staff is neither a spear nor a mace, and the tonfa overlaps with the baton.
- *Fix.*
  - E4.5 has about 12 kinds, so it takes no leaf (C5b). Kinds go by blade style: dagger, push dagger, Bowie or fighting knife, hunting knife, karambit, butterfly knife, automatic or out-the-front knife, throwing knife, bayonet. `deployment` (fixed, folding, automatic) is an attribute. The butterfly knife and the automatic knife stay kinds, because their opening mechanism is their form and the reason the key and the law name them.
  - Under E4.6, use the leaves Polearms (spear, halberd, glaive, naginata); Axes (battle axe, tomahawk made for fighting or throwing); Staffs (bō, gun staff); Impact weapons (mace, war hammer, baton, tonfa, nunchaku, kubotan); Flexible weapons (flail, rope dart, chain whip, three-section staff), the last following the Chinese 软兵器 class [S19].

**E4-5 (medium) A kind named after a brand, and leaves named by power source.**
- *Evidence.* "Taser" is a kind, sourced to "Brownells Tasers and Accessories" [S03]. TASER is Axon's trademark. The E4.7 leaves are "Chemical" and "Electric", with one and two kinds.
- *Fix.* Name the kinds "projectile electroshock weapon" (named form: TASER, maker-bound) and "contact stun gun". Drop the two leaves (C5b: E4.7 has fewer than 12 kinds). Pepper spray, pepper gel and pepper-ball launcher become kinds directly under the sub-family. The memo's "CO2 launcher" row joins them.

**E4-6 (medium) Cartridge as a kind conflicts with C6 and C13.**
- *Evidence.* E4.9 makes each cartridge, gauge or pellet calibre a kind ("9×19 mm Luger cartridge", "12-gauge shotshell"), which gives 100 to 150 kinds. The same memo makes calibre an attribute of the weapon. C6 makes sizes attributes, and C13 puts maker- or standard-set compatibility in a ledger. A cartridge is defined by a standard (CIP or SAAMI) and fixes which weapon it fits.
- *Fix.* Kinds stop at cartridge class: centrefire handgun cartridge, centrefire rifle cartridge, rimfire cartridge, shotshell, muzzle-loading projectile and propellant, air-gun pellet, arrow, crossbow bolt. Each named cartridge (9×19 mm Parabellum, .308 Winchester, 12 gauge 70 mm) is a non-maker-bound named form (C2a) and a C13 ledger row (`owner` = CIP or SAAMI). A maker's load (bullet type, weight) is a C3 variant. Buyers still browse by calibre, through the named form. This keeps four levels and makes the rule "calibre is the same field on the weapon and on the ammunition" (decision 5).

**E4-7 (medium) Overlapping kinds within firearms, and power source within air guns (C10).**
- *Evidence.* The kinds "single-action revolver" (with the Colt Dragoon, a percussion revolver) and "muzzle-loading rifle" make the muzzle-loading action a kind under rifles but not under revolvers. A percussion revolver is both. The air-rifle kinds are PCP, spring-piston and CO2. The source also lists gas (nitro) piston and multi-pump [S27]. A gas-piston break-barrel has the same body as a spring-piston one.
- *Fix.*
  - Apply C10. PCP, CO2, spring or gas piston, and multi-pump are kinds only where the powerplant changes the body or needs new fittings (PCP: a reservoir and filling equipment; CO2: a capsule housing). Spring piston and gas piston are one kind, "piston air rifle", with the piston type as an attribute.
  - For firearms, add one rule: "ignition system (flintlock, percussion, cartridge) is an attribute; 'muzzle-loading' is a kind only for long guns, where it changes the loading form". A percussion revolver is then a single-action revolver with `ignition` = percussion.

**E4-8 (medium) Choice-level evidence rests on excerpts and on US retail.**
- *Evidence.* The split of rifles by action at Euroshot, Pyramyd's powerplant split, Brownells' calibre list, Lancaster's bow types and archery styles, and NihontoWatch's Juyo share are all marked † (read from search excerpts). Section 4b admits "This batch did not fetch review-site 'best X' lists". Eighteen of the 37 sources are US-only, and three more are US or global.
- *Fix.* Before the owner approves, fetch two comparison sources per sub-family, at least one outside the US: a German or UK review of rifle actions; a UK airgun magazine's powerplant tests; a Japanese or European archery retailer; a European sword dealer naming sabre and rapier (decision 15). Replace the † details with fetched text.

**E4-9 (medium) Tier, protection level and the maker ledger (C1, C4).**
- *Evidence.* Section 5 puts `protection_level` "on the kind" and makes the "Authenticity class" a modifier. The maker ledger has "tier (preference) … platform or chambering", plus "a parallel *school and smith* table". The compatibility table for platforms is only sketched.
- *Fix.*
  - NIJ HG1 to RF3 and NIJ 0115.00 are spec attributes with their standard named (C4b) on the named form, not tiers.
  - `function_class` keeps only battle-ready and working replica. "Antique" is an era tag, and decorative or blunted objects leave E4 by the key.
  - Ledger: smiths are C1 rows with `maker_class` = artisan. Schools (Bizen, Mino, Soshu) are not makers: record them as tradition tags (C8 vocabulary), or as a separate `school` table with smiths' `parent_id` pointing to it (owner choice).
  - "Platform or chambering" moves to C13 ledger rows: AR-15 pattern, MIL-STD-1913/Picatinny and M-LOK rails, and Glock-pattern magazines. Each needs a fetched source.

**E4-10 (low) Boundaries the memo does not close, and one key conflict.**
- *Evidence.* The E2 row of section 9 lists "ear defenders for shooting", but step 17 names ear defenders in A1 (personal protective equipment against a hazard). Also unplaced: the blank-firing starting pistol (E4 leaf or E2 athletics), the flare gun (G1 under S3 for boats, or C8), the holster (S3 sends anything worn on the body to step 17, so A4?), the plate carrier (armour or part), the ballistic helmet (decision 14), slingshots, blowguns and shuriken (decision 9), reloading presses (decision 10), and quivers, archery targets and arm guards (E2 P9).
- *Fix.* Add these sentences:
  - "Ear defenders and shooting glasses are A1 (step 17), whatever the use."
  - "A blank-firing pistol made for self-defence or deterrence is E4; one made to start races is E2."
  - "A holster or belt pouch worn on the body is A4, because S3 never sends worn objects to a part; a hard case for one firearm is E4."
  - "A plate carrier is E4 armour."
  - For the rest, adopt E2's P9 jointly (cross-memo finding X3).

**E4-11 (low) Order.** Section 8 orders named forms "by introduction date or typology number". *Fix.* Follow C7 for maker-bound forms (maker, then year). For non-maker-bound forms with a published typology (Oakeshott), use typology order. Propose that as a C7 addition (section 3).

### Usability test: 20 objects per memo, filed by two builders from the memo as written

"Same" means both builders would reach the same kind. "Split" names the two homes a builder could choose. The finding that fixes each split is given in brackets.

- **E1.**
  - *Same (7):* Barbie Fashionistas doll; LEGO Technic set; Squishmallow; Nerf blaster; Ticket to Ride; Ravensburger 1000-piece jigsaw; Little Tikes Cozy Coupe.
  - *Split (13):* Hot Wheels Premium 1:64 (E1.2 collector or E1.3 toy) [E1-1]; Bburago 1:18 die-cast (same) [E1-1]; Hornby OO train set (model locomotive or toy train set) [E1-1]; Bandai HG Gunpla (scale kit or character kit) [E1-1]; S.H.Figuarts (1:12 action figure or figma-type) [E1-2]; Pop Up Parade (PVC scale or prize figure) [E1-2]; Labubu plush pendant (plush or designer vinyl) [E1-2]; Pokémon Elite Trainer Box (no kind) [E1-3]; Magic Commander deck (starter deck or booster product) [E1-3]; mahjong set (tile set or classic set) [E1-4]; Rubik's Cube (3D puzzle or mechanical puzzle; Ravensburger's "3D puzzle" is a 3D jigsaw) [state: twisty puzzles are mechanical puzzles]; garden trampoline (E1 or E2) [E1-10]; Sylvanian Families set (dolls, figures or figure-and-scene system) [state: small-figure playsets are "figure-and-scene playset", one kind].
- **E2.**
  - *Same (12):* tennis racket; shuttlecock; golf driver; iron set; football boot; cricket bat; treadmill; kettlebell; alpine ski; snowboard; climbing rope; fishing rod.
  - *Split (8):* ski helmet (alpine, snowboarding or a general leaf; and E2 or A1) [E2-1, P2]; mouthguard (boxing, rugby or hockey) [E2-1]; wetsuit worn for triathlon (water general or multisport) [E2-1]; skipping rope (boxing or cardio) [E2-1]; crampons (climbing or trekking) [E2-1, E2-6]; tennis court shoe (E2 or A2) [P4]; metal detector (no sub-family) [E2-3]; paintball marker (no sub-family) [E2-3].
- **E3.**
  - *Same (11):* Fender Player Stratocaster (solid-body); Gibson ES-335; Martin D-28; Yamaha P-125 digital piano; violin; trumpet; Boss DS-1; Yamaha HS8 studio monitor; QSC K12 PA speaker; Focusrite Scarlett interface; acoustic drum kit.
  - *Split (9):* Shure SM58 (Recording or Live) [E3-1]; Behringer X32 mixer (same) [E3-1]; Novation Launchpad (DJ or recording controller) [E3-1]; Line 6 Helix (multi-effects or amp modeller) [state: a floor modeller with amp models is "amp modeller", an Amplification kind]; Ibanez AZ (Stratocaster or ST-type named form) [E3-5]; melodica (keyboards or other winds) [E3-2]; harmonium (same) [E3-2]; Zildjian K hi-hats (kind or named form) [E3-3]; guzheng (named form of koto or own kind) [E3-9].
- **E4.**
  - *Same (11):* Glock 17; Remington 700; Beretta 686; Henry lever-action; PCP air rifle; compound bow; katana; Bowie knife; pepper spray; NIJ level IIIA soft vest; rifle scope.
  - *Split (9):* Zweihänder (two-handed or straight double-edged) [E4-1]; rapier (thrusting or double-edged) [E4-1]; dao (dao kind or sabre kind) [E4-2]; fixed karambit (folding-knife leaf or fixed) [E4-4]; tomahawk (no kind; E4 or C1) [E4-4]; bō staff (polearm or impact) [E4-4]; Colt Walker percussion revolver (single-action or muzzle-loading) [E4-7]; gas-piston break-barrel (spring kind or new kind) [E4-7]; holster (E4 part or A4) [E4-10].

## 3. Conformance to conventions C1 to C13

The conventions were drafted after these memos. The table lists, for each convention, what each memo must change to conform. "OK" means no change is needed. Cells refer to the findings above.

| Convention | E1 | E2 | E3 | E4 |
|---|---|---|---|---|
| C1 maker ledger core + lines table | Rename the columns to the C1 core. "Platform key" leaves the ledger for C13. Lines (Nendoroid, figma, Hot Wheels, Technic, Marvel Legends) go to the lines table. Banpresto gets `parent_id` = Bandai Namco [E1-2]. | The own-brand flag becomes `maker_class` = retail own-label. Series go to the lines table. Sport leaves are derived [E2-5]. | `maker_line` becomes the lines table. Maker types map to `maker_class`. Add `built_by_maker_id` [E3-6]. | Smiths are `maker_class` artisan. Schools become tags or a school table. "Platform or chambering" goes to C13 [E4-9]. |
| C2 kind vs named form, `maker_bound` | Nendoroid and figma become maker-bound named forms. Chess, go and shogi are kinds under C2(c) [E1-2, E1-4]. | "Long-nose wood" and "blacksmith iron" are non-maker-bound forms (if kept). Series are maker-bound. Add the flag. | Add the flag. Separate design families (S-type, dreadnought) from maker models [E3-5]. | AR-15 pattern and Oakeshott types are non-maker-bound. Maker models are maker-bound. Add the flag. |
| C3 variant ledger | LEGO set numbers, figure releases, card sets and prints become variants [E1-3]. | Model years and colourways become variants [E2-5]. | Reissues and model years (Vintage Guitar's "years of availability") become variants. | Ammunition loads (bullet type and weight) become variants [E4-6]. |
| C4 tier entries, spec ladders, platform tags, price band | Remove the tier tag from the kind. Tier entries go on lines. Get a second-region source (C4e) [E1-2]. | Remove tier from kinds. Flex, grade and spec bands become attributes. Maker ladders become tier entries [E2-2]. | One `tier_band` field becomes tier entries with sources. Get a second-region source [E3-6]. | `protection_level` becomes a C4(b) attribute. Drop the certificate grade [E4-3, E4-9]. |
| C4(d) USD price bands | The USD and yen figure bands map to C4(d). | BHQ price guide maps to C4(d). | Brassandwinds' USD bands map to C4(d). | Price band is a preference modifier. Map to C4(d). |
| C5 levels and axes | State the leaf axis per sub-family. Leafless sub-families store `leaf = null`. Add the parts sub-family [E1-6, E1-7]. | State the leaf axis per family. Small families skip the leaf [E2-6]. | OK on the parts sub-family (E3.5). State the leaf axis of the gear sub-families [E3-1]. | E4.5 and E4.7 skip the leaf (C5b). The sword leaf gets one axis [E4-1, E4-4, E4-5]. E4.10 is the C5(d) parts sub-family. |
| C6 size and user | Scale is an attribute (C6). Age and kidult are tags. OK otherwise. | Junior sizes and ball sizes are attributes. OK. | Fractional sizes are attributes. Voice members are kinds [E3-8]. | Calibre is an attribute on the weapon and a named form for ammunition [E4-6]. The length class needs a stated exception [E4-3]. |
| C7 order | One scale direction. Named forms by maker, then year [E1-11]. | Drop spec as a named-form sort key [E2-7]. | Maker, then year, not pure chronology [E3-7]. | Typology order for non-maker forms (C7 addition) [E4-11]. |
| C8 scene vocabulary | Scenes (anime figure collecting, designer toys, kidult, hobby board gaming, competitive TCG, scale modelling) need a definition source each. | Board culture, hickory golf, bushcraft: give each a source or hold it back. | Bluegrass, DJ, Eurorack: give each a source. | Hunting, target, HEMA, cowboy action, nihonto, wushu: give each a source. "Use" tags go to one shared list (X8). |
| C9 alias and homonym table | Klemmbausteine, Sammelfigur, プライズ, ガンプラ; foosball, kicker and baby-foot = table football. | Soccer and football; table-tennis bat and paddle; judogi. | ST and スト type; エレアコ; Konzertgitarre; upright bass, double bass and contrabass; French horn and horn. | Nihontō terms; 软兵器; Schreckschusswaffe. Homonyms across memos: X7. |
| C10 rule T | RC and slot cars pass (track and transmitter) and should say so. "Electronic toy" stays an attribute. | Motorised and manual treadmills: attribute. OK. | Digital and acoustic piano, electric and acoustic guitar, electronic and acoustic drum kit pass (form differs). USB fails [E3-4]. | Air-gun powerplants are partly kinds [E4-7]. Electric and chemical are not leaves [E4-5]. |
| C11 rule R | Regional decks become named forms. Hanafuda and mahjong stay kinds [E1-4]. | Hurley, sliotar and kendo bogu stay kinds under their sport (no generic covers them). OK. | Apply the label rule. Bayan and garmon become named forms [E3-9]. | Jian and dao become named forms. Japanese types are kinds with a stated reason [E4-2]. |
| C12 rule M | The swing seat and the swing set differ by body (a frame), so they stay kinds. OK. | Hoops, pull-up bars and tables: attribute [E2-9]. | Studio monitor against PA: body differs, so they stay kinds [E3-1]. | None. |
| C13 compatibility ledger | LEGO, Duplo, Brio, TCG systems, railway gauges (NEM, NMRA) and Toniebox [E1-8]. | Ski soles and bindings, cleats and pedals, golf adapters [E2-4]. | Eurorack, MIDI, 500-series [E3-4]. | Cartridges (CIP, SAAMI), rails, AR-15 pattern, magazine patterns [E4-6, E4-9]. |

## 4. Cross-memo consistency

**X1 (high) Maker ledger: four schemas.**
- *Evidence.* The four memos propose different columns:
  - E1: maker, known-for kinds, platform key, scene tags, tier, price band, country, era.
  - E2: adds sport leaves and an own-brand flag.
  - E3: maker type (brand owner, OEM factory, luthier, second brand), parent or designer brand, and lines with `tier_band`.
  - E4: adds platform or chambering, and a separate school-and-smith table.
- *Convention.* Use C1 for all four.
  - The platform and chambering columns move to C13.
  - Tier moves to C4 tier entries.
  - Lines (Nendoroid, Astrox, Player II, Pearl Masters, Hoyt Rx series) go to the lines table.
  - Add one core column to C1, `built_by_maker_id` on the line. E3 needs it (Boston and Kawai, Fender Japan and FujiGen), and so do A5 (movement makers) and E1 (OEM toy factories).
  - Add one optional extension for E4, a `school` table (`school_id`, name, `region`, era, sources), with smiths linked by `school_id`. This keeps schools from being entered as makers.

**X2 (high) Tier: three memos put it on the kind.**
- *Evidence.* E1 puts a figure-format tier on the kind. E2 has "a modifier on the kind or named form". E4 has `protection_level` "on the kind". E3 alone puts tier on lines, but in one field.
- *Convention.* C4 throughout.
  - Measured ladders are attributes with their standard named: NIJ, UIAA, FIE, ski-boot flex, U-weight, wetsuit thickness, cricket willow grade, piece count.
  - Maker ladders are tier entries on lines: Fender Squier to Custom Shop; adidas Elite, Pro, League and Club; Pearl Decade to Masters.
  - Generic player-level ladders share one domain-E scheme, `player_level` (starter, intermediate, advanced, professional). Every entry names its source: brassandwinds and Shar (E3), Thomann's beginner/advanced/professional text (E3), BHQ and TCOM player's frames (E2). C4(e) requires a second region before the scheme enters the data.

**X3 (medium) Boundaries the two sides do not state alike.**

| Pair | Object | E-side A says | E-side B says | Proposed sentence (both memos) |
|---|---|---|---|---|
| E1/E2 | table football, air hockey | E1 (E1 §9.1) | E1 (E2 P10) | agree; keep |
| E1/E2 | trampoline | play trampoline E1, cut open (E1 conflict f) | fitness trampoline E2 (key) | E1-10(b) |
| E1/E2 | kite, flying disc, toy ball | E1.6 if sold as toys, E2 if made for a sport (E1 Q12) | silent (kite sports "narrow") | C15 below |
| E1/E3 | toy instrument | key and E3 §9.4 send to E1 | E1 has no kind | E1-5: kind "toy instrument" |
| E1/E4 | foam LARP weapon, play sword | E1 "toy blaster" (includes play swords) | E4: foam is E1 | E1-5: kind "toy weapon" with blaster, play sword and foam replica as named forms |
| E2/E4 | arrows, quivers | E2 P9: follow the bow to E4 | E4: arrows in E4.9; quivers silent | arrows and bolts E4.9; a quiver worn on the body is A4 by S3's "never parts: anything worn on the body"; owner to confirm |
| E2/E4 | archery target, arm guard, finger tab | E2 P9: E2 | silent | E2, leaf "Archery (targets and shooter's gear)" under Golf, cue and target sports; add to E4 §9 |
| E2/E4 | airsoft and paintball markers, spearguns | key E2, but no E2 leaf | E4: E2 | E2-3 leaves |
| E2/E4 | clay throwers, decoys, game calls, hides | E2 P9 asks | silent | owner decision (section 5) |
| E2/E4 | ear defenders, shooting glasses | silent | E4 lists them in the E2 row | A1 by step 17 (E4-10) |
| E2/E4 | starting pistol | silent | E4 leaf "Blank-firing" | E4-10 sentence |
| E2/A1/E4 | helmets | E2 P2: sport helmets E2 | E4: helmets against blows or bullets E4 | adopt both: weapon threat E4 > one-sport helmet E2 > other hazard A1; and the key's order (step 10 before 17) already gives E4 first |
| E2/E3 | dance | dance shoes E2 (key); not in tree | none | E2-3 Dance leaf |
| E1/F3, E1/D3, E1/D5, E3/F4, E3/D1, E3/D3 | | outside domain E | | one-sided, logged for the D and F reviews: TCG singles (E1-10a), Toniebox, pinball and slot machines, singing bowls, cables, studio headphones |

**X4 (medium) Orphaned and duplicated kinds.**
- *Orphans*, named by the key or sent by a neighbour but placed nowhere: toy instrument, piñata, play make-up, mechanical bank (E1); airsoft marker, paintball marker, speargun, metal detector, caving gear, sledge, dance shoe (E2); slingshot, blowgun, boomerang, shuriken (E4 Q9, and silent in E1 and E2); axe kinds (E4).
- *Duplicates.* Die-cast cars and train sets (E1.2 and E1.3) [E1-1]. "Sabre" is both an E2 fencing kind and an E4 sword kind. That is legitimate, because they are different objects, but it needs a C9 homonym row (X7). The E4 "baton" and "tonfa" overlap [E4-4].
- *Proposed home for the E4 Q9 group:* slingshot and blowgun E4 (made to shoot), unless sold as a toy (E1); boomerang E2 (a throwing sport) or E1 as a toy; shuriken E4.

**X5 (medium) One toy-or-real test.** E1 (toy counterparts), E2 P10, E3 §9.4 and E4 §9 each state the cut differently.
- *Convention C15 (proposed).* "An object made for play by children that imitates a sport, music or weapon object is E1 when it cannot do the real object's job to that object's own standard (a regulation ball, a tuned instrument, a weapon that can injure). The real object made in a child's size stays in its category (size and user are attributes, C6)."
- Evidence: ISO 8124-1 includes "toys which are their counterparts" of sporting goods [E1 S32]. EU CN 9503 has headings for toy musical instruments and toy weapons [E1 S30].

**X6 (medium) Tradition-named kinds: three readings of C11.**
- *Evidence.* E1 makes German-suited decks kinds. E3 makes sitar, koto and oud kinds without a generic label. E4 makes jian and dao kinds but the sabre generic.
- *Convention for domain E (refines C11).* A tradition-named object is a kind only when both tests hold:
  - (a) a fetched source sells or compares it as its own category (C2c);
  - (b) its form (construction, tuning, length class with its own mounting, or component set) differs from every generic kind in the leaf.
- Its label is then "name (generic description)". Otherwise it is a named form under the generic kind, with a region tag. Applied:
  - Kinds: katana, wakizashi, tantō, koto, sitar, shamisen, hanafuda, mahjong set, shogi set, go set.
  - Named forms: jian (arming sword), dao (sabre), bayan (accordion), German-suited deck (playing-card deck), liuyedao (sabre).

**X7 (low) Homonyms for C9.**
- Rows to add:
  - bow (E4 bow; E3 bow for strings, an S3 part);
  - sabre (E2 fencing sabre; E4 sword);
  - bat (cricket and baseball bat E2; table-tennis bat = paddle);
  - blade (table-tennis blade, the bat without rubbers, E2; knife blade);
  - deck (card deck E1; skateboard deck E2);
  - kit (drum kit E3; model kit E1; football kit A1);
  - board (game board E1; skateboard, surfboard E2);
  - set (chess set; drum set; train set);
  - tarot (game deck E1; divination deck F4);
  - football (association; American; Australian rules).

**X8 (low) Use, discipline and market tags.** E4 has `use` (hunting, competition, self-defence). E2 has discipline (Olympic recurve, 3D). E1 has market ("home game" or "casino"). E3 has studio or stage (after E3-1). *Convention.* One `use_tags` list per category, each tag with a source, never a level. "Market" values (law-enforcement, casino) use Appendix A's market modifier.

**X9 (low) Parts sub-family (C5d).** E3 (E3.5) and E4 (E4.10) have one. E1 has none [E1-7]. E2 places parts inside the sport leaf (tennis string, ski binding, table-tennis rubber). *Convention.* C5(d) applies to E1, E3 and E4. Amend C5(d) so that a category whose leaf axis already names the host (E2: sport) may file S3 parts in the host's leaf instead, and says so in its definition.

**X10 (low) Named-form granularity agrees.** All four memos stop named forms at the line, series, system or iconic design, and hold every release, title, kit number, model year or load outside the kinds (E1 Q2, E2 Q8, E3 Q9, E4 §4). *Convention.* Adopt that, with C3 variants for the finer rows where owner-emphasis scenes need depth (figure releases, TCG sets, vintage guitar years).

**X11 (low) Individual-item facts.** NBTHK certificates (E4), "player grade vs collector grade" and originality (E3) and single named cards (E1) are facts about one particular object. *Convention C16 (proposed).* "Certificates, condition grades, provenance and serial numbers of one particular object are not stored. The data holds kinds, named forms and variants only (BRIEF: individual items are out)."

**X12 (low) Jurisdiction.** E4 proposes a per-country legal-class ledger. E1 (slot machines, gambling equipment), E2 (airsoft energy limits, mentioned at Pyramyd) and B9 meet the same need. *Convention C17 (proposed).* A jurisdiction ledger: `subject_id` (kind or named form), `jurisdiction`, `scheme` (EU 2021/555 category, UK Firearms Act section, US NFA), `class`, `criteria`, `source_url`, `date`. Never a level or a tag on the tree.

**Proposed shared conventions from this review (for _conventions.md):**
- **C14 Multi-use kinds.** A kind used in more than one sub-family or leaf goes, in this order, to:
  - (a) the leaf whose rule or standard defines it;
  - (b) the general leaf of the one family that holds all its uses;
  - (c) a category-level "multi-use" sub-family whose leaf axis is stated.
  - A generated view lists it under each use. (E2-1; it applies to every category with a use or activity axis.)
- **C15 Toy or real** (X5).
- **C16 Individual-item facts** (X11).
- **C17 Jurisdiction ledger** (X12).
- **C1 addition:** `built_by_maker_id` on lines, and an optional `school` table (X1).
- **C4 addition:** a domain-E `player_level` scheme (X2).
- **C5(d) amendment** (X9).
- **C7 addition:** non-maker-bound named forms with a published typology (Oakeshott, Japanese blade construction) go in typology order (E4-11).
- **C11 refinement for domain E** (X6).

