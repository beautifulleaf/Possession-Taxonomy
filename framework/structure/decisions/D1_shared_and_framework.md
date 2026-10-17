# D1. Stage-2 decisions: shared conventions and framework items

**Decided by:** Claude (batch S2D_1), on the owner's delegation of 2026-10-17 ("Your judgment for the answers"). Every line is a decision delegated by the owner and made by Claude; the owner may overturn any of them, and until then they bind like owner decisions (BRIEF.md, "Owner decisions on stage 2").
**Date:** 2026-10-17.
**Questions:** CV-1 to CV-46 (STAGE2_SUMMARY.md §3) and K-1 to K-196 (STAGE2_OWNER_QUESTIONS.md part 1).
**Rules used, in order:** (1) BRIEF binds, with its standing preferences and the two stage-2 owner rules: the **depth-and-breadth rule** (no caps on maker ledgers, lines or named forms; makers, artisans, houses, workshops, perfumers and schools in ledgers off the tree, never as extra kinds; scene tags wherever communities exist; no boundary decision may drop a maker community) and the **one-source rule** (one fetched page showing that a thing is or was made or sold proves it exists; a second source or region never decides inclusion, only level or tier weight). (2) Test the object, not the motive (S5); legal classes go to the C17 ledger. (3) Adopt the recommendation unless it breaks (1) or (2), hangs a home on a fact nobody can check on the object, or adds kinds or levels buyers do not compare; with no recommendation, take the simpler one-sentence rule that keeps the round-5 placements stable. (4) Attributes over kinds, fewer levels, one shared rule, a written precedence sentence over a silent gap. (5) No sourcing pass: a decision that rests on an unverified fact is marked provisional.
**Prior rulings** given in verify/in/S2D_COMMON.txt are recorded as "adopted (ruling)" and were not decided again.
**Format:** `- **ID** decision. adopted | departed: reason. provisional until attested: … (if any)`. "No rec" means no source gave a recommendation; the choice follows rule 3's fallback.

## Shared conventions (CV-1 to CV-46)

- **CV-1** Yes: C1 core maker columns; lines, tier entries, named forms and variants in separate tables; `known_for_kinds` derived from the named-form ledger, not stored. adopted
- **CV-2** Yes: one domain-wide maker ledger, multi-valued `maker_class`, merged G/H/I/F/C class list, `platform_ids` out; add class `perfumer or composer` (a person) so noses are recorded. departed: owner depth-and-breadth rule (perfumer class added)
- **CV-3** Yes: `built_by_maker_id`, `base_named_form_id`, maker-relations table (OEM, supplier, board partner, licence, plus `composed by` for perfumers), `line_rank`, `licensor_id`, `authority_id`; the school table is standing, not optional. departed: owner depth-and-breadth rule (school table kept; composer relation added)
- **CV-4** Yes: one issuer table for states, central banks, postal and transit authorities, shared by F3 and F5; issuers are not makers. adopted
- **CV-5** Seed maker ledgers from attested pages and grow without a cap; identity and platform makers first only as an ordering rule; one fetched page admits a maker; own-labels are class "retail own-label". departed: owner depth-and-breadth rule (no cap) and owner one-source rule
- **CV-6** Yes: the choice-level test decides kind against named form; `maker_bound`; specs, sizes, prints, colourways and editions are never named forms; traditional types are kinds only when sold as their own category. adopted
- **CV-7** Yes to the named-form test and the line/named-form split; admission: one attested row each, harvested in stage 3 and grown without a cap (no "load on demand only", no per-category cap). departed: owner depth-and-breadth rule
- **CV-8** Yes: one optional variant schema, never a level or a kind; filled wherever a community compares variants (sneakers, denim, watch references, fragrance concentrations and editions, vehicles), not only owner-emphasis scenes. departed: owner depth-and-breadth rule (wider fill)
- **CV-9** Yes: add the G, I, D and J variant types; add `concentration` only if the H-4 decision (batch D3) makes it a variant. adopted
- **CV-10** Yes: tiers never on a kind; per-source tier entries with a `disputed` flag; measured ladders attributes; platform labels dated tags; a scheme enters on one fetched source; a second region only adds weight. departed: owner one-source rule (C4(e) second-region preference no longer gates entry)
- **CV-11** Yes: a tier entry may sit on a variant or plan row for a maker's own ladder of one named form (exempt from C4(e)) or an external score of that version, vintage scores included. adopted
- **CV-12** Yes: maker range levels as tier entries with scheme = maker; skill-level schemes allowed; six scale classes with test version, direction and `stale_after`; a reviewer's grade enters on one source (the H "second region before entry" clause dropped). departed: owner one-source rule
- **CV-13** Yes: one USD price-band scheme for the domain (under 50 … over 15,000), from a dated, sourced list price; a band is never a tier. adopted
- **CV-14** Yes: bands above 15,000 up to over 5,000,000 USD; recurring prices annualised per plan, "0 (free)" band, domain names at renewal price. adopted
- **CV-15** Yes: JC2 grocery `unit_price_band` in USD per kg or litre; J7 also keeps the per-bottle C4(d) band. adopted
- **CV-16** Yes: at most four levels below the category, named form included; leaf optional for about 12 kinds or fewer (`leaf = null`); one axis per level within each sub-family. adopted
- **CV-17** Yes: closing sub-family "Parts and accessories made for one <object>" (leaf axis = object served) in every category that receives S3 parts, none for J, G2, C3, C8, I3; no E2 exception: E2 parts go there too. adopted (E2 exception: no rec; one shared rule, rule 4)
- **CV-18** Yes: size always an attribute with its standard; user always a tag with generated department views (the luggage size exception is decided under A-16, batch D2). adopted
- **CV-19** Yes: one user list (women, men, unisex, couples, baby, child, bariatric, adapted; "beginner" a level scheme); a size class names a kind only when it changes what the object works with and sellers sell the sizes apart. adopted
- **CV-20** Yes: canonical kind first, then the sub-family's stated key; variants by code or year; named-form order as amended by CV-21. adopted
- **CV-21** Option: G amendment (non-maker named forms first by first-attested year, then maker-bound by maker, year, alphabet), with generated ladder views for D's `line_rank` order. adopted
- **CV-22** Yes: one sourced scene vocabulary with core/adjacent strength, tagged at maker, kind and named form without inheritance; extended to every domain where communities exist (fashion, fragrance, puzzles, knives, watches, audio, others), each tag with a definition source. departed: owner depth-and-breadth rule (all domains, not A and D only)
- **CV-23** Yes: one C9 alias and homonym table, English label plus native script; add relations "marketing name", "trade mark", "genericised name". adopted
- **CV-24** Yes: rule T as C10 states it (power, technology and connectivity attributes unless the key names the kind, or form or installation changes and a fetched source ranks the types apart). adopted
- **CV-25** Yes: "A retailer facet becomes a kind only when the object's form differs and a fetched source compares or ranks the types separately." adopted
- **CV-26** Yes: rule R as C11 states it; a region never names a sub-family or a leaf. adopted
- **CV-27** Yes: a regional name becomes a kind only with its own category at fetched sellers in two regions and no generic kind covering its form; otherwise a named form (still in). adopted (two regions decide level only, consistent with the one-source rule)
- **CV-28** Yes: rule M as C12 states it. adopted
- **CV-29** Yes: one C13 compatibility ledger; platforms never levels. adopted
- **CV-30** Yes: relations with platform type, region and status; one ledger for domain I and D5 with one `delivery` list; app ecosystems as rows with `kinds_served`, the app itself I1. adopted
- **CV-31** Yes: C14 order (defining rule, the one family holding all uses, a multi-use sub-family) with a generated view of every use. adopted
- **CV-32** Yes: C15 toy-or-real test; the real object in a child's size stays in its category. adopted
- **CV-33** Yes: C16, no certificates, grades, provenance or serials of one particular object. adopted
- **CV-34** Yes: one grading-scale registry (merged with D's condition scales); no grade value ever stored. adopted
- **CV-35** Yes: C17 jurisdiction ledger for legal classes; never a level or a tag on the tree. adopted
- **CV-36** Yes: design and voluntary standards met are the attribute `standard_met`; every legal class goes to C17; customs headings are evidence only; neither defines a kind. adopted
- **CV-37** Yes: domain-G `propulsion` attribute with its eight values and a primary flag. adopted
- **CV-38** Yes: photographic prints carry `process` and `mount_format`. adopted
- **CV-39** Yes: a tools/ script adds `fetch_status` (full, partial, nav-only, failed) to every S2 sources TSV; excerpt-only facts go to S2_<CODE>_excerpts.tsv. adopted
- **CV-40** Yes: JC1 `standard` and `designation` tables (consortia are authorities); one-kind designation a named form, multi-kind a tag; written exception: wine and spirit designations (Champagne, Port, Cognac and similar) are kinds. adopted
- **CV-41** Yes: multi-valued J `supply_role` beside `maker_class`. adopted
- **CV-42** Yes: JC4 as written (state and same-product packs attributes; a preserving process may define a level on its stated axis; machine single-serve pack a kind; legal ladder an attribute; a legal name fixing a different composition a kind). adopted
- **CV-43** Yes: one J `tradition` vocabulary; `origin` is the place of production; no `cuisine` tag anywhere (J5 included); `culinary_link` rows from any kind, designation or variety row. adopted
- **CV-44** Yes: one variety table for breeds, cultivars, rice, coffee varietals, tea cultivars and grapes. adopted
- **CV-45** Yes: large named-form sets (flags, china patterns, cigar vitolas, feed lines) live in registers, not tree rows, uncapped. adopted
- **CV-46** Yes: brand product lines of everyday consumables (cleaning products, e-liquids, cigarette brands, feed recipes, insecticides) are ledger lines, not named forms; fragrances, cigars, teas and wines keep named forms. adopted

## Framework items (K-1 to K-196)

### General rules: S3 parts, sets, tests
- **K-1** Add the H/F sets sentence; a furniture suite or set sold as one unit is filed by its pieces with a unit-of-sale attribute; no suite kinds. adopted (ruling)
- **K-2** Add "A cable with a proprietary connector made for one device follows it (S3); a cable with standard connectors (USB, HDMI, audio, instrument, microphone, patch, MIDI) is D1." adopted (ruling)
- **K-3** Add "A generic charger (USB, GaN, Qi) is D1; a charger made for one device follows it (S3); a charger for standard-size cells is C8; a cordless-platform charger is C1." adopted (ruling)
- **K-4** Add the K-4 battery sentence as proposed (platform packs C1; one-device batteries follow it, vape batteries B9; loose standard cells, 18650 included, C8). adopted (ruling)
- **K-5** Add "Gimbals, selfie sticks, clip-on lenses, battery cases and clip-on game controllers made only for phones are D2 (S3); one made for cameras, consoles or computers that also takes a phone stays there." adopted (ruling)
- **K-6** Add "Electronics made to be fitted to a vehicle (car audio, dashcam, mounted sat-nav, bike computer, OBD tracker) are G1 (S3); a portable sat-nav is D2." adopted (ruling)
- **K-7** Add "A roof box or rack made to be fitted to one vehicle is G1; a free-standing rack is B1." adopted
- **K-8** Add "A bracket, arm or mount made to hold one screen or speaker follows it (S3: D3, monitors D1); a stand with shelves or storage is B1." adopted (no rec; S3 already reads so)
- **K-9** Add the K-9 holder sentence as proposed (one-object holders S3; empty multi-object albums, binders, stock books, boxes and trays B1; filled photo album or scrapbook F5; blank scrapbook album C4). adopted (ruling)
- **K-10** Add "laundry baskets are B6" to the S3 never-parts sentence. adopted
- **K-11** (a) dishwasher salt, descaler, cleaning tablets B6; softener salt, filter cartridges, moisture absorbers B7; mothballs B8; (b) lens solution H2; (c) shoe and textile waterproofing and care sprays B6; (d) sex-toy cleaners B6. adopted ((c): memo B6, care products kept together)
- **K-12** Add "Welding wire and rods, solder, a grinding disc or a sanding sheet cut for one sander is C1 under S3; sandpaper and abrasive sheets and rolls for general use are C8." adopted
- **K-13** Add "Tools made to service a vehicle, bicycle or machine are C1; only parts, attachments and consumables follow the vehicle under S3." adopted
- **K-14** Add "A recorder sold only to run security cameras follows them (B8); a general network drive is D1." adopted
- **K-15** Add "A universal tripod is D4. A camera made only to fit a telescope is C6 (S3); a camera made for general photography as well is D4." adopted (tripods; cameras: no rec, S3 reading)
- **K-16** Add "A toys-to-life figure is E1; its portal or reader is a D5 part. Toniebox-type figures are D3 parts under S3." adopted
- **K-17** Add "Studio backdrops are B2 and studio furniture B1; studio lights, stands and flashes are D4." adopted
- **K-18** Add "A dust extractor made for workshop machines is C1; a wet-and-dry vacuum is B6." adopted
- **K-19** Add "First-aid kits are H2 whatever vehicle, workplace or place they are made for." adopted
- **K-20** Add the W1 sentence (watch chain, Albert or fob chain for a pocket watch A5 under S3; decorative fob, seal or charm worn without a watch A3). adopted
- **K-21** Add "A belt buckle, plain or decorative, is a part of a belt and is A1 under S3." adopted

### Step 1: scope and prepared food
- **K-22** Reword step 1 to "alcohol-free versions of beer, wine and spirits". adopted
- **K-23** Add "Par-fried or coated frozen vegetables (chips, hash browns) are prepared (OUT)." adopted
- **K-24** Sealed ready-to-drink alcoholic drinks (RTD cocktails, hard seltzer, canned gin and tonic) are J7; a dry noodle brick is J5; a noodle cup or pot is a ready meal (OUT). adopted (ruling)
- **K-25** Add "En primeur offers and casks held in bond are OUT until delivered; a delivered cask is J7." adopted
- **K-26** Live fish sold to eat stay OUT; shark fin, CITES and protected-species status go to the C17 ledger, not a flag on the tree. departed: legal status belongs in C17 (rule 2), not a tree attribute
- **K-27** Add "A printed share or bond certificate, cheque, traveller's cheque or postal order kept as an object is F5." adopted
- **K-28** Add "A physical SIM card is F5; an eSIM profile is part of its I3 plan." adopted
- **K-29** Add "A domain-name registration is I2, not a right." adopted
- **K-30** Add "Fuel bought in its own container (gas cylinder, canister) is C8, owned or leased; fuel pumped or delivered into a vehicle or fixed tank is energy supply (OUT)." adopted (cylinder: no rec; lease is how-acquired, a modifier)

### Step 2: health and medical
- **K-31** Replace "licensed as a medicine" with the X3 H1/H2 sentence as proposed. adopted (ruling)
- **K-32** Add "A powered massager is H3 when its maker names sexual use; H2 when made to treat a condition (TENS, EMS units sold for pain); H1 for comfort, percussion and neck massagers included." departed: "a specialist retailer lists it" dropped, a fact not on the object
- **K-33** Add the X5 list as proposed (lubricants, menstrual, nappies H1; condoms, incontinence, stoma H2; period underwear A1; pelvic-floor and ED devices H2 if medical purpose stated, else H3; wigs H1; breast forms H2). adopted
- **K-34** Add "Spectacles that correct vision, ready-made reading glasses and prescription sunglasses, with their frames and lenses, are H2; frames with plano lenses sold as fashion, and non-corrective sunglasses, are A4." adopted (ruling)
- **K-35** Add "contact lenses of every kind are H2" to step 2; coloured plano lenses carry `corrective: no`. adopted
- **K-36** Add "Supplements sold for skin, hair or nails, collagen drinks included, are H2." adopted
- **K-37** Add "software made to diagnose, treat or monitor a condition, such as a regulated medical app, is H2". adopted
- **K-38** Add "A magnifier made and sold as a low-vision aid is H2; any other magnifier is C6." adopted
- **K-39** Add "A bed, mattress or chair made to treat or manage a condition is H2; an ordinary bed or recliner in an adapted form is B1." adopted
- **K-40** Add "Weighted blankets and orthopaedic pillows are B2 unless made to treat a stated condition (H2)." adopted
- **K-41** Add "Therapeutic and diabetic footwear is A2; orthotic inserts and braces are H2." adopted
- **K-42** Medical and surgical face masks are A1 as PPE; add them to the A1 PPE list. adopted
- **K-43** Add "A worn alarm made to call help after a fall or medical event (fall detector, care pendant, wandering detector) is H2; an alarm made to deter attack or intrusion is B8." adopted (no rec; function test on the object)

### Step 3: groceries
- **K-44** Add the X2 spreads sentence as proposed, with the dairy exception: spreads and fresh cheeses made from milk (labneh, cream cheese, butter, ghee) are J3. adopted (ruling)
- **K-45** Add the X3 formed-products sentence; a whole cut cooked, cured, glazed or herb-rolled and sold to slice (glazed ham, porchetta) is J1; "coated" = breaded or battered; "filled" = pastry, dumpling or stuffed dish. adopted (ruling)
- **K-46** Add the X5 mixed-products sentence as proposed (half-weight kind, else "mixed <class>"; named spice blend a kind; cross-category mix by item of greatest value). adopted (ruling)
- **K-47** Reword J1 to "meat, poultry, game and other land animals eaten (frogs, insects)"; snails are J2 molluscs. adopted (ruling)
- **K-48** Add "Bitters sold as a flavouring by the dash are J5; a bitter liqueur sold to drink by the glass is J7." adopted
- **K-49** Add "A dry mix for a drink is J6 when coffee, tea or cocoa is its main ingredient by weight; a mix led by sugar, creamer or malt is a prepared drink (OUT)." adopted
- **K-50** Cocoa butter and cocoa paste are J6 cocoa products; couverture and baking chocolate stay J5. adopted
- **K-51** Reword J6 to "other plant parts brewed as infusions (leaves, flowers, fruit, roots, bark, roasted grains)" and name kava. adopted
- **K-52** Tinned and plain-cooked meat is J1 ("Cooked, tinned & potted meats"); pastrami and corned brisket pieces in J1. adopted
- **K-53** Add "Margarine and plant-only fat spreads are J5; a spread containing butter is J3." adopted
- **K-54** Add "Every nut, chestnut and coconut is J5; fresh olives are J4; cured table olives are J5." adopted
- **K-55** Add a J3 note: dried and preserved dairy (aaruul, qurut, chhurpi, kashk, jameed) is J3 cheese. adopted provisional until attested: sellers listing these as a cheese class (for a tenth cheese leaf)
- **K-56** Add "Plain fermented milk drinks (kefir, drinking yoghurt, buttermilk, ayran, plain lassi) are J3; sweetened or flavoured milk drinks are OUT." adopted
- **K-57** Cooked, pickled and preserved eggs stay J3 (plain cooking or curing of one ingredient). adopted
- **K-58** Add "Home-brewing and winemaking ingredients are J5; their equipment is B5." adopted
- **K-59** Add "Cake and baking mixes are J5; sprinkles are OUT; nuts coated in chocolate, sugar or batter are OUT; trail mix follows K-46." adopted (cake mixes, sprinkles; coated nuts and trail mix: no rec, existing rules applied)

### Step 4: property and structures
- **K-60** Add the X-1 step-4 note as proposed (test the object as made); the narrowboat is G1; the tiny house on wheels is G2. adopted (ruling)
- **K-61** Add "A park model RV is G2." adopted
- **K-62** Commercial, industrial and institutional buildings are in G2 as one leaf "other buildings by function" with a few kinds; no market sub-family. adopted (ruling)
- **K-63** Add "A unit with its own sink, toilet and entrance is a dwelling; otherwise it is a garden room." adopted
- **K-64** Add "A sauna cabin that stands as a building is G2; a portable sauna is B7." adopted
- **K-65** Add "Tents, yurts and tipis are E2 as made, whatever platform they stand on; a platform or deck built for them is G2." adopted (no rec; "set as a dwelling" is a use test, rule 2)
- **K-66** Add "A pergola, gazebo or decking kit is filed by the structure it makes; boards sold loose are C8." adopted
- **K-67** Add "A garage building or a parking bay held as land is G2; a rented bay or a permit is OUT." adopted

### Step 5: software, digital items, subscriptions
- **K-68** Delete "the seat structure (individual, family, student)" from the step-5 note; add "seat structure is a plan attribute". adopted
- **K-69** The I2 branch and D5 note read "in-game and platform items". adopted
- **K-70** Goods-rental subscriptions I3.5; personal hosting plans I3.2; creator memberships I3.1; car-sharing memberships I3.4; travel eSIM and one-off packs OUT unless they renew. adopted
- **K-71** Add boundary sentences (a) to (c) and (e) to (k) as proposed; game launchers and their free accounts not filed (their makers stay in the ledger); (d) and (l) need none. adopted

### Step 6: plants
- **K-72** Add "Real Christmas trees, cut or potted, are C3; artificial ones are B4." adopted
- **K-73** Add "A living plant in any container, basket, kokedama or terrarium is C3 whatever the container's value." adopted (ruling)
- **K-74** Add "Preserved (stabilised) plants and artificial plants of every kind are B4." adopted
- **K-75** Add "Sprouting seed sold to eat is J5, to grow C3; living tobacco and cannabis plants are C3." adopted

### Step 7: natural history
- **K-76** Add "A mount of one animal prepared as in life is F6 however it is presented; a work that combines animal parts with other materials is F2." adopted
- **K-77** Add "A cast, replica or carved figure is filed by what it is (F2 sculpture, E1 toy or kit); a gem simulant is not a gemstone (A3 or C4 by form)." adopted
- **K-78** Add the shells-pearls-beads sentence as proposed (identified shell F6; craft assortment C4; drilled bead C4; strung A3; undrilled loose F6). adopted
- **K-79** Add "human specimens are OUT"; ivory and CITES goods stay in, their status recorded in the C17 ledger, not as a tree flag. departed: legal status belongs in C17 (rule 2)
- **K-80** Add "A preserved or emptied specimen kept as a specimen is F6." adopted

### Step 9: adult objects
- **K-81** Add the H3-6 sentence as proposed (restraint collars, cuffs, armbinders, harnesses H3; ornament collar A3; garments A1; eye-only blindfold H3); a leash made to clip to a restraint is H3. adopted (leash: S3 reading)
- **K-82** Add "Furniture made to restrain or suspend is H3; positioning cushions are B2." adopted

### Step 10: weapons and armour
- **K-83** Add the K-83 knives sentence as proposed (fighting, hunting, butterfly, automatic E4; EDC locking folders C1 unless a weapon kind); baton and tonfa E4. adopted (knife-maker communities kept in the ledger)
- **K-84** Add "Holsters are A4; plate carriers are E4 armour; slingshots, blowguns and shuriken are E4 unless toys (E1); boomerangs E2; distress flare pistols and flares E2." adopted (holster rec; rest no rec, C15 and function)
- **K-85** Add "Bombs, grenades, mines and artillery are OUT, except deactivated display pieces (B4)." adopted
- **K-86** Add the K-86 sentence as proposed (reloading presses C1; components E4; loose tsuba, menuki, armour pieces E4 under S3; reproductions E4/E2/B4/E1 by state). adopted
- **K-87** Add "Blunt or unsharpened wushu implements made for practice or competition are E2; decorative ones B4; sharpened ones E4." adopted (no rec; extends the step-10 combat-sport note)
- **K-88** A personal attack alarm is not a weapon; it is B8. adopted

### Step 11: vehicles
- **K-89** Add "an electric kick scooter is G1". adopted
- **K-90** Add "Powered boards, hoverboards, electric unicycles and eFoils are G1; an unpowered unicycle is E2." Probe: unicycle G1 → E2. adopted
- **K-91** Add "Children's pedal bicycles are G1 (C15); balance bikes and tricycles stay E1." adopted
- **K-92** Add "Motor vehicles made for racing or off-road sport (racing cars, karts, motocross bikes, dune buggies) are G1, filed by body." adopted
- **K-93** Add "A vehicle made mainly to carry people or goods (Unimog, ATV, quad, utility vehicle) is G1 even when it powers implements"; tool-carrier tractors C7. adopted
- **K-94** Add the K-94 trailer sentence as proposed (carry-only trailers and wagons G1; wagons that load, mix, spread or process C7). adopted
- **K-95** Pet strollers and dog bike trailers are G1, in a hand-pushed and towed carriers leaf. adopted
- **K-96** Add "Parachutes and skydiving rigs are E2, like hang gliders." adopted
- **K-97** Add "An RC or FPV drone sold as a hobby model is E1; one made for filming is D4"; camera-less toy drones and combustion hobby RC cars E1. adopted
- **K-98** Mobility scooters stay H2. adopted

### Steps 12 and 13: farm, forestry and animals
- **K-99** Amend the step-12 note to "… including lawn and garden tractors without a rear power take-off and a Category 1 or larger three-point hitch"; two-wheel tractors by the same test. adopted (ruling)
- **K-100** Add the X5 irrigation sentence as proposed (field-crop irrigation C7; gardens, glasshouses, allotments, grounds C2). adopted
- **K-101** Add "Equipment made for herds or flocks (handling systems, milking, feed mixers, commercial hatchers, livestock EID stick readers) is C7; pet microchip scanners and small incubators are B10." adopted (test; readers: no rec) provisional until attested: EID stick readers sold for herd recording
- **K-102** Allow the animal group as B10's first axis, written into the key as an Appendix A exception. adopted (ruling)
- **K-103** Add "A gate sold for stairs and doorways for children, or children and pets, is B8; a gate, pen or camera sold only for pets is B10; a GPS pet tracker is B10." adopted
- **K-104** Garden fish ponds, pond liners and pond pumps are C2. adopted
- **K-105** Bee suits, veils and gloves are A1 PPE. adopted
- **K-106** Honey extraction and bottling gear is B10 with beekeeping equipment. adopted

### Step 14: religious and ceremonial
- **K-107** Add the X1 religious-medal sentence as proposed (devotional medal loose F4, with chain or bail A3; commemorative or award medal F3). adopted (ruling)
- **K-108** Add the X4 devotional-image sentence as proposed (icons, thangkas, altarpieces, shrine statues, crucifixes F4; other religious-subject works F2 or B4). adopted
- **K-109** Add "A pack sold for card play (tarock, French tarot) is E1; a deck sold for divination is F4." adopted
- **K-110** Add "Singing bowls and meditation instruments are E3 unless made for a rite (F4)." adopted
- **K-111** Add "A strand made for counting prayers (with counter, tassel or guru bead) is F4; a necklace of the same beads made as jewellery is A3." adopted
- **K-112** Add the K-112 sentence as proposed (printed religious text F1; Torah scroll, mezuzah, prayer card F4; ketubah or baptism certificate F5, or F2 when made as a picture). adopted
- **K-113** Add "A candle made for a rite or devotion, grave lights included, and a rug made as a prayer rug are F4; a meditation cushion or mat is B2." adopted
- **K-114** Add "Spirit boards, pendulums, runes and I Ching sets are F4 when made for divination, E1 when made as a board game." adopted
- **K-115** Add "Worn Masonic and fraternal regalia follow A1 and A3; their ritual implements are F4; smudge bundles are B4 unless made for a named rite (F4)." adopted
- **K-116** Japanese stone lantern (tōrō) is B4 garden decor; F4 only for a lantern made as a shrine offering by its form (votive inscription and shape). Probe: stone lantern, ishi-toro B3 → B4. adopted (ruling)
- **K-117** Add "A token or charm made to bring luck or protection and carried, not worn (omamori, carried evil-eye charm), is F4; worn, A3; issued for money, F3." adopted (no rec; keeps omamori F4)

### Step 15: money, stamps, awards
- **K-118** Add the X2 narrow rule; a cover that passed through the post and is neither administration-issued nor first-day is F5. adopted (ruling)
- **K-119** Name championship rings and belts in the step-15 award list (F3). adopted
- **K-120** Add "Game money is E1; prop and souvenir notes are F3." adopted
- **K-121** Collectible sticker series (Panini type) are F3 with the non-game card kinds. adopted
- **K-122** Add "A coin or ingot made or mounted with a bail, loop or bezel to be worn is A3; one without a mount is F3" (the object as it is now). adopted
- **K-123** Add "A crown or tiara made to be worn as an ornament is A3; a crown that is regalia of an office is F3; a toy crown is E1." adopted

### Steps 16 and 17: timepieces, worn and carried
- **K-124** Add "A watch whose main display is the time is A5 whatever sensors it has; a device whose main function is sensing or navigation is D2." adopted
- **K-125** Weapon-threat helmets E4; a helmet or goggles made for one sport E2 (equestrian riding hat E2); other hazard helmets A1, cycling and motorcycle included; riding boots A2. adopted (ruling)
- **K-126** Restrict E2 "swimming costumes" to competition and sport swimwear (racing suits, wetsuits); bikinis, trunks and beachwear stay A1. adopted
- **K-127** Add "A shoe is E2 only when it is made for the demands of one sport and is sold as a performance model with sport-specific soles or spikes; basketball- and tennis-lineage sneakers worn every day are A2." adopted (ruling)
- **K-128** Add the K-128 hosiery sentence as proposed (hosiery and tabi socks A1; spats, galoshes, overshoes, rubber-soled jika-tabi A2). adopted
- **K-129** Add the H1 head-ornament sentence as proposed; a stick-on bindi is A3; kumkum and other powder or paint applied to the skin is H1. adopted (bindi: no rec; ornament test)
- **K-130** Add to step 17 "an accessory made as a toy is E1; a real ornament in a child's size stays A3". adopted
- **K-131** Add "insulated lunch bags and cool bags are B5" to the A4 note. adopted
- **K-132** Add "A case made for the small items of one task follows the task: pencil case C5, toiletry and make-up bag H1, tool bag C1." adopted (pencil case ruling; toiletry bag by the same rule)
- **K-133** Add "a powered hand-held or neck fan is B7" to step 17; a standing beach or patio umbrella is B1. Probe: garden parasol stays B1. adopted (fan rec; umbrella no rec, keeps placement)
- **K-134** Furoshiki and other carry cloths are B2, with an A4 cross-reference. adopted
- **K-135** Add "head-worn magnifiers, binocular loupes, opera glasses and eclipse glasses are C6" to the A4 note. adopted (no rec; written precedence, designed function)
- **K-136** Add "A plush or figure pendant with a clip or chain is E1; any other bag charm or keyring is A4." adopted (no rec; form test; keeps designer-figure makers in E1)
- **K-137** Add "A bag made for one piece or pair of sport equipment follows it (S3, E2); any other bag, chalk bags and quivers included, is A4." adopted

### Steps 18 to 21: body care, documents, art, media
- **K-138** Add "Repellent applied to the skin is H1; sprays, coils and traps for rooms are B8." Probe: insect repellent B8 → H1. adopted
- **K-139** Add the X3 photographs sentence as proposed; step 19 drops "of the owner's own life". adopted (ruling)
- **K-140** Add "and other kept printed ephemera" (menus, invitations, trade cards, receipts, labels, bookplates) to step 19; types become kinds only by the C2 choice-level test, otherwise named forms. adopted
- **K-141** Reword the F1 note to "home recordings on a physical carrier are F5"; add "developed negatives and slides" to step 19. adopted
- **K-142** Add "A map, including a single sheet from an atlas or a pictorial wall map, is F1; a print made as art that depicts a place is F2." adopted

### Steps 22 to 24: music, instruments, electronics
- **K-143** Add "Studio or listening gear is filed by the maker's own product category; a stage in-ear kit with a transmitter pack is E3." Probe (may): in-ear monitors E3 → D3. adopted
- **K-144** Add "A microphone sold for both music recording and speech is filed by the maker's stated first use." adopted
- **K-145** Stage lighting B3; piano benches and racks B1; fog and haze machines B4. adopted (fog: listed option)
- **K-146** Add "A jukebox is D3 unless sold as an arcade or coin-operated game." adopted
- **K-147** Add the X11 measuring sentence as proposed (building, trade, workshop, electronics instruments C1; sample instruments C6); air-quality monitors C6. adopted
- **K-148** Add "Golf and hunting laser rangefinders are E2, building laser measurers C1, rangefinding binoculars C6." adopted
- **K-149** Add the K-149 science-kit sentence as proposed (experiment kits C6; play robots and coding toys E1; component kits without an experiment programme D1). adopted
- **K-150** Name digital audio players, streamers and set-top boxes in D3; add the K-150 audio-converter sentence as proposed. adopted
- **K-151** Name camcorders, action and 360 cameras in D4; name golf GPS units and landline, cordless and DECT phones in D2. adopted (landlines: no rec; phones D2)
- **K-152** Handheld gaming PCs (Steam Deck, ROG Ally) are D5 with a PC operating-system attribute. adopted
- **K-153** Add "A headset that encloses the eyes (VR or mixed reality) is D5 whatever it is sold for; glasses with a see-through display, camera or speakers are D2." adopted
- **K-154** D5 game software kinds by carrier type; platform an attribute and a C13 row with a by-platform view; reword the D5 line to match. adopted (ruling)
- **K-155** Coin-operated video cabinets D5; pinball, claw cranes and redemption games E1; casino slot machines E1 as gambling equipment. adopted
- **K-156** Photographic paper is D4; wildlife trail cameras are D4 (a camera; setting and use are modifiers). adopted (paper rec; trail cameras no rec, rule 2)
- **K-157** Add "A portable power station (battery and inverter in one box) is B7, with the home battery." adopted
- **K-158** Add "Copy and printer paper, label makers and label printers of any connection, and reusable paper notebooks are C5; an electronic writing tablet is D2." adopted (no rec; step 31 "connected or not")

### Steps 25 to 27: play, sport, smoking
- **K-159** Add "A trampoline with a frame of about 1.2 m or less, sold for exercise (rebounder), is E2; a garden or play trampoline is E1." adopted provisional until attested: the 1.2 m frame cut
- **K-160** Add the C15 kites-discs-balls sentence as proposed (toy versions E1; regulation ball or sport kite in a child's size E2). adopted
- **K-161** Add to the step-26 note "drink bottles and bladders, for sport or not, are B5; a hydration pack sold with its bag is A4". Probe: camping water bladder stays B5. adopted (no rec; keeps placement)
- **K-162** Add "Head torches and dive lights are B3 like lanterns; a weapon-mounted light is E4; a toy light is E1." adopted
- **K-163** Add the K-163 hunting and archery sentence as proposed (decoys, blinds, calls, clay throwers, targets, arm guards, tabs E2; arrows, bolts, bipods, rests E4). adopted
- **K-164** Add "A case made to carry smoking products on the person (cigarette case, cigar case, travel humidor, tobacco pouch) is B9; a humidor, tobacco jar or cabinet that stands in a room is B1." adopted
- **K-165** Add the K-165 cannabinoid sentence as proposed (cannabinoid products B9; skin care without cannabinoid H1; intimate oils H3). adopted
- **K-166** Gas cylinders and flints are C8; hookah charcoal is B9. adopted
- **K-167** Add "Rolling trays are B9; stash jars and boxes are B1 (S3 storage); a scale goes with its task (B5, C5, C6), a pocket scale B5." adopted (no rec; existing S3 and step-23 rules)
- **K-168** Add to step 27 "every plant or fungus product taken for a psychoactive effect (opium, salvia, psychoactive mushrooms) is B9 whatever its legal status; kava is J6; living plants and fungi C3". adopted (no rec; legal status to C17)

### Steps 28 and 29: craft, garden and grounds
- **K-169** Add "candle and soap making, resin, glass and mosaic, basketry and floristry" to step 28; tools for shaping wood stay C1. adopted (no rec; keeps these maker communities in C4)
- **K-170** Add "File by the maker's first-named use: handwriting, lettering, calligraphy and shodo C5; drawing, comics and painting C4; both named, C5." Probe: fudepen C4 → C5. adopted (ruling)
- **K-171** Add the X8 material-worked sentence as proposed; office stamps C5, decorative stamps C4; general household scissors C5. adopted (scissors: no rec; paper and desk work)
- **K-172** Pottery wheels, slab rollers, pugmills C4; easels C4, art-studio furniture B1; cutting plotters and heat presses C4; paint for pictures, models and crafts C4, for walls, woodwork and furniture C8. adopted (easels rec; rest no rec)
- **K-173** Option (a): hand-held chainsaws and pole saws C2; axes, wedges and log splitters C1; tractor-driven splitters and chippers C7. adopted (ruling)
- **K-174** Add the X4 landscaping sentence as proposed (growing media and decorative ground cover C2; construction aggregates, paving, edging, membrane, fencing, gates C8). adopted
- **K-175** Add the X13 pump sentence as proposed (water-moving pumps for gardens, pools, ponds C2; field irrigation C7; drainage, transfer, sump, general C1). adopted
- **K-176** All equipment and chemicals made for a swimming pool are C2, pool heat pumps included; hot-tub equipment follows the hot tub to B7. adopted
- **K-177** Add "Water butts and rain tanks are C2." adopted (no rec; step 29 before step 30)
- **K-178** Add "Made to protect plants or kill weeds is C2; made to kill household pests is B8." adopted
- **K-179** Cachepots C2; plant stands B1 as the key names them; a children's garden tool set is E1 when it cannot do the job (C15), C2 otherwise. adopted (cachepot rec; rest no rec, existing rules)

### Step 30: household
- **K-180** Add the K-180 candle-holder and lantern sentence as proposed. Probe (may): rush light, bonbori, chochin B3 → B4 unless made to be carried. adopted
- **K-181** Add "A light strip sold to light a space is B3; string, fairy and novelty lights made mainly as decoration are B4." adopted
- **K-182** Option (a): every plate and tray made to hold food is B5; display is a tag (S5). Probe: Kosiv painted ceramics B4 → B5 (plates). adopted (sources split; S5 names the commemorative plate)
- **K-183** Add "An essential oil sold for a diffuser or fragrance burner is B4 unless sold to treat a condition (H2)"; wax warmers and electric diffusers are B4. adopted
- **K-184** Add "A washbasin sold built into its cabinet is B7; a vanity cabinet sold without a basin is B1." adopted
- **K-185** Add the K-185 sentence as proposed (heated towel rail B7; free-standing heated airer B6; ceiling drying unit B6). adopted
- **K-186** Add the K-186 sentence as proposed, shower trays with enclosures in C8. adopted (trays: no rec; follows the proposed sentence)
- **K-187** Add "Gravel of any kind is stone (K-174); anti-climb spikes, security window film and bird spikes are B8; netting made to protect plants is C2." adopted (no rec; designed function)
- **K-188** Freestanding and wall letterboxes are B8; letter plates fitted in a door are C8. adopted
- **K-189** Curtain poles, rails and rings, and rug underlay are B2. adopted
- **K-190** Workbench C1 ("a work surface made for tool work"); hospital bed, examination table, dentist chair H2; barber and massage chairs H1; desk and craft table B1. Probe: workbench B1 → C1. adopted (workbench ruling; barber chair H1 by grooming)
- **K-191** Bookends B1; jewellery boxes B1; a tray made to serve B5, one made to hold small items on a surface B1; candle-making supplies C4 (K-169). adopted
- **K-192** A flagpole made for a flag follows the flag (S3, B4); regulatory and safety signs are C8. Probe: flagpole stays B4. adopted

### Steps 31 and 32: stationery, tools, materials
- **K-193** Add the X10 envelopes sentence as proposed (post envelopes and tubes C5; packing materials C8; storage boxes B1). adopted
- **K-194** Add the X2 earth-moving sentence as proposed (self-propelled dig, lift, load, move machines C1 unless farm or forestry C7 or grounds C2). adopted (ruling)
- **K-195** Add "Fence panels, posts, wire, netting, gates and electric-fence energisers, tape and insulators are C8." adopted
- **K-196** Cabinet knobs and pulls are C8; a lockset that includes a lock is B8. adopted

## Departures from recommendations
- **CV-2** perfumer or composer class added to the maker classes. Owner depth-and-breadth rule.
- **CV-3** school table made standing (not optional); `composed by` relation added. Owner depth-and-breadth rule.
- **CV-5** no per-category cap; seed from attested pages and grow; identity and platform makers first only as ordering; one page admits a maker. Owner depth-and-breadth rule; owner one-source rule.
- **CV-7** no cap and no "load on demand only"; named forms harvested in stage 3 and grown without a cap. Owner depth-and-breadth rule.
- **CV-8** variants filled wherever a community compares them, not only in owner-emphasis scenes. Owner depth-and-breadth rule.
- **CV-10** a tier scheme enters on one fetched source; a second region adds weight only. Owner one-source rule.
- **CV-12** the H clause "a reviewer's grade needs a second source from another region before entry" is dropped. Owner one-source rule.
- **CV-22** scene vocabulary extended to every domain where communities exist, not only A and D. Owner depth-and-breadth rule.
- **K-26** protected-species and CITES status go to the C17 ledger, not a flag attribute on the tree. Legal classes belong in C17 (rule 2).
- **K-32** "or a specialist retailer lists it" dropped from the H3 massager test. A retailer's listing is not a fact on the object (rule 3).
- **K-79** ivory and CITES goods recorded in the C17 ledger, not with a tree flag. Legal classes belong in C17 (rule 2).

## Decisions that need attestation
- **K-55** that sellers list dried and preserved dairy (aaruul, qurut, chhurpi, kashk, jameed) as a cheese class, before a tenth J3 cheese leaf is opened.
- **K-101** that livestock EID stick readers are made and sold for herd recording, apart from pet microchip scanners.
- **K-159** the 1.2 m frame cut between exercise rebounders and garden trampolines.
