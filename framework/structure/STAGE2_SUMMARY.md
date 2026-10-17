# Stage 2 summary: owner review page

Batch S2S_SUMMARY, 2026-10-17. Written from BRIEF.md, framework/CATEGORIES_v0_6.md, _conventions.md, _framework_conflicts.md, verify/out/S2_stats.tsv and the seven domain digests verify/out/S2S_X*.md. Memo sections are cited as "A3 §10.9"; review items as "rev C X1". The complete question lists are in [STAGE2_OWNER_QUESTIONS.md](STAGE2_OWNER_QUESTIONS.md).

## 1. What stage 2 did and did not do

**Did.**
- Wrote one research memo for each of the 53 categories of v0.6 (framework/structure/<CODE>.md, 3.9 MB in all). Each proposes an inner structure: sub-families, leaves, kinds and named forms, plus how makers, tiers and modifiers are stored.
- Gave each domain a cold review (_review_A.md to _review_J.md). Each review merged the owner questions and logged top-level conflicts.
- Applied the review findings to every memo in a conformance pass (section 11 of each memo; all 53 are marked done in S2_stats.tsv).
- Drafted shared conventions C1 to C17, plus "Proposed additions" from the G, H, I, F and J reviews (_conventions.md).
- Logged 229 top-level conflict entries (_framework_conflicts.md), 161 of them from a final sweep.

**Did not.**
- **Nothing is approved.** Memos are research proposals. Every convention, framework change and category structure here waits for the owner.
- **v0.6 has not been re-tested blind.** Its precedence sentences were added after round 5 (99.0 % unanimous on 953 items). No change proposed in stage 2 has been placed blind.
- No data was written. No kind, maker or named form is in data/*.tsv yet.
- **† marks a claim that still needs a fetched source.** The memos hold 2,568 † and 1,925 OWNER marks. † per memo:
  A1 65 · A2 44 · A3 39 · A4 55 · A5 31 · B1 40 · B2 63 · B3 25 · B4 34 · B5 44 · B6 68 · B7 44 · B8 34 · B9 30 · B10 23 · C1 67 · C2 53 · C3 46 · C4 38 · C5 37 · C6 30 · C7 30 · C8 80 · D1 51 · D2 50 · D3 63 · D4 52 · D5 24 · E1 78 · E2 74 · E3 61 · E4 98 · F1 54 · F2 45 · F3 77 · F4 82 · F5 28 · F6 64 · G1 52 · G2 27 · H1 56 · H2 76 · H3 40 · I1 20 · I2 51 · I3 46 · J1 64 · J2 25 · J3 27 · J4 22 · J5 63 · J6 32 · J7 46.

**Common ground across all memos.** At most four levels below the category (sub-family, leaf, kind, named form). Tiers, makers, region, scene, user and occasion stay off the tree as tags, ledgers or views. Parts follow the whole (S3) into a closing parts sub-family.

## 2. Categories at a glance

Choice level is where buyers compare. Tier type: **ladder** (a clear quality ladder), **mixed**, or **pref** (preference). Maker: how central makers are. Conformance (section 11) is done for all 53. OWNER is the count of OWNER marks in the memo.

| Code | Name | Recommended sub-families | Choice level | Tier | Maker | Review verdict | Conf. | OWNER |
|---|---|---|---|---|---|---|---|---|
| A1 | Clothing | Tops; Bottoms; Dresses & sets; Outerwear; Underwear & sleepwear; Headwear; Hands, neck & waist; Parts | cut buyers compare | mixed | high | minor fixes | yes | 18 |
| A2 | Footwear | Sneakers; Shoes; Boots; Sandals; Slippers; Over-footwear; Parts | generic type (Oxford, Chelsea) | mixed | high | rework (levels 1–2) | yes | 30 |
| A3 | Jewellery | by site: Head & hair; Ear; Piercing; Neck; Arm; Hand; Torso & clothing; Leg & foot; Parts | named form (hoop, tennis bracelet) | mixed | high | minor fixes | yes | 24 |
| A4 | Bags & Accessories | Handbags; Backpacks; Luggage; Work cases; Wallets; Eyewear; Umbrellas & fans; Baby carriers; Small items; Parts | silhouette or format | pref | medium | minor fixes | yes | 18 |
| A5 | Clocks & Watches | Wristwatches; Carried watches; Clocks; Timing instruments; Parts | complication; clock placement | mixed | high | minor fixes | yes | 14 |
| B1 | Furniture & Storage | Seating; Sleeping; Tables; Storage furniture; Containers; Display, division & shelter | use type; mattress construction | pref | medium | minor fixes | yes | 25 |
| B2 | Soft Furnishings | Bed; Floor; Window; Seat; Table & kitchen; Body textiles | product type or construction | mixed | low | minor fixes | yes | 28 |
| B3 | Lighting | Fixed fittings; Standing lamps; Carried & worn; Light sources; Lamp parts | placement; bulb shape | mixed | high | minor fixes | yes | 19 |
| B4 | Decor | Vessels; Mirrors & frames; Candles; Fragrance; Temporary display; Artificial flowers; Garden; Flags & signs; Decorative lighting | product form | pref | medium | minor fixes | yes | 36 |
| B5 | Kitchen & Dining | Cook; Prepare; Cool & store; Serve & eat; Make drinks; Clean-up & remainder | vessel, knife, appliance type | mixed | high | minor fixes | yes | 39 |
| B6 | Cleaning & Laundry | Floors; Surfaces & objects; Textiles; Dishes; Waste | form or mechanism | mixed | medium | minor fixes | yes | 29 |
| B7 | Climate, Water & Energy | Room air; Water; Electricity (12 leaves) | device form; heater mechanism | ladder | high | minor fixes | yes | 38 |
| B8 | Home Safety & Security | Break-in & attack; Fire, smoke & gas; Injury hazards; Pests | form a grade attaches to | mixed | high | needs rework | yes | 34 |
| B9 | Smoking & Vaping | Products; Implements & hardware | vitola, shape, device architecture | mixed | high | minor fixes | yes | 32 |
| B10 | Animal Equipment | by animal: Dogs; Cats; Small mammals; Horses; Fish; Reptiles; Cage birds; Wild birds; Bees; Livestock; Several | feed class; equipment type | pref | medium | ready for owner | yes | 44 |
| C1 | Tools & Workshop | 12 by work done: cutting … lifting, power & air, storage, parts, kits | tool type by action and form | mixed | high | rework (sub-family level) | yes | 45 |
| C2 | Garden & Grounds | Digging; Cutting; Lawn; Clearing & snow; Watering; Pots & supports; Soil & feed; Protected growing; Pools; Parts | mechanism or form | mixed | medium | minor fixes | yes | 45 |
| C3 | Plants & Living Cultures | Growing plants; Seeds & propagules; Fresh-cut; Living cultures | genus (species in collector genera) | mixed | low | minor fixes | yes | 20 |
| C4 | Craft & Art Supplies | Picture-making; Sewing; Yarn; Leather; Beading; Paper; Clay; Models; General tools & adhesives; Parts | per sub-family (medium, yarn form …) | mixed | high | minor fixes | yes | 24 |
| C5 | Office & Stationery | Writing & correcting; Paper goods; Desk & filing; Calculators & machines; Parts | generic type | mixed | high | minor fixes | yes | 45 |
| C6 | Optical & Scientific | Optical viewing; Weather; Laboratory; Science kits; Parts | design principle | ladder | medium | minor fixes (closest to ready) | yes | 68 |
| C7 | Farm & Forestry | Tractors & carriers; Tillage; Seeding; Crop care; Harvest; Hay; Post-harvest; Livestock; Forestry; Parts | machine type; tractor by design | ladder | medium | minor fixes | yes | 49 |
| C8 | Building Materials & Hardware | 12 supply families: structure … batteries, fuels, packing, lighters | application, joint system, size class | mixed | low | minor fixes | yes | 54 |
| D1 | Computers & Components | Computers; Components; Storage; Input & display; Network & power; Cables; Transaction; Loose parts; Parts | part function; chip as named form | mixed | high | minor fixes | yes | 39 |
| D2 | Phones, Tablets & Devices | Phones; Radios; Tablets; E-readers; Wearables; Location & safety; Power banks; Parts | build or form class | mixed | high | minor fixes | yes | 74 |
| D3 | Audio & Video | Displays; Sources; Amplification; Loudspeakers; Headphones; All-in-one; Smart hubs; Parts | body or wearing form | mixed | high | minor fixes | yes | 30 |
| D4 | Cameras & Photography | Cameras; Lenses; Light; Support; Film; Darkroom; Parts | viewing system; lens optical design | ladder | high | needs rework | yes | 15 |
| D5 | Video Games | Machines; Controllers; Parts; Software on carriers; Downloads & add-ons | machine form; carrier (K-154) | pref | high | minor fixes | yes | 50 |
| E1 | Toys & Games | Dolls & figures; Construction; Models & railways; Vehicles; Games; Puzzles; Role play; Play equipment; Parts | form or component set | pref | high | rework (collectible half) | yes | 33 |
| E2 | Sports, Fitness & Recreation | 16 activity families plus a multi-use family | equipment type within a sport | mixed | medium | minor fixes | yes | 41 |
| E3 | Musical Instruments & Gear | Instruments; Amplification & effects; Sound capture & mixing; Parts & aids | construction or family member | ladder | high | minor fixes | yes | 23 |
| E4 | Weapons & Armour | Firearms; Air guns; Bows; Swords; Knives; Polearms & impact; Self-defence; Armour; Ammunition; Parts | action type in form class | mixed | medium | minor fixes | yes | 50 |
| F1 | Media & Publications | Printed volumes; Cartographic; Sound carriers; Moving-image carriers; Parts | carrier system, binding class | mixed | medium | minor fixes | yes | 48 |
| F2 | Art | Paintings; Drawings; Prints; Photographs; Sculpture; Textile hangings; Calligraphy; Mixed work | medium, technique, material | pref | high | rework (figurines, sculpture) | yes | 28 |
| F3 | Coins, Stamps, Medals & Cards | Coins; Banknotes; Bullion; Tokens; Postal; Medals; Trophies; Cards; Regalia; Parts | standing or purpose of issue | mixed | high | minor fixes | yes | 36 |
| F4 | Religious & Ceremonial | Altars & images; Devotion aids; Ritual implements; Light & offerings; Divination; The dead | generic form (C11) | pref | low | rework (kind level) | yes | 41 |
| F5 | Documents & Records | Issued documents; Cards, passes & tokens; Personal records | document or card type | pref | low | minor fixes | yes | 24 |
| F6 | Natural History | Minerals; Rocks; Fossils; Meteorites; Gems & pearls; Shells; Preserved specimens; Elements; Parts | species or trade name | mixed | low | minor fixes | yes | 31 |
| G1 | Vehicles | Land; Rail; Watercraft; Aircraft; Parts | body style or class; model line named form | pref | high | minor fixes | yes | 48 |
| G2 | Property & Structures | Land; Dwellings; Other buildings & structures; Burial places | where filters and census stop | pref | low | rework (Land; house kinds) | yes | 37 |
| H1 | Personal Care & Beauty | Skin; Makeup; Hair; Fragrance; Shaving; Bath & hygiene; Oral; Implements & scales; Comfort & massage | retail product type | pref | high | minor fixes | yes | 27 |
| H2 | Health, Medical & Mobility | Monitoring; Therapy; Mobility; Daily living; Sensory; Medicines; Supplements; Nutrition; Contraception; First aid; Supports; Parts | device type; OTC use class | mixed | medium | rework (vision, medicines, testing) | yes | 37 |
| H3 | Adult Objects | Vibrators; Dildos; Anal; Penis toys; Restraint & sensation; Machines; Dolls; Parts | type within action family | pref | high | minor fixes | yes | 29 |
| I1 | Software | System; Security; Office; Creative; Playback; Money; Learning; Development; Engineering; Assistants; Internet; Add-ons | program type compared by labs and lists | mixed | high | minor fixes | yes | 47 |
| I2 | Digital Media & Items | Text; Audio; Moving image; Still image; Fonts & assets; Game & platform items; Names & tokens | layout form, format family | ladder | medium | needs rework | yes | 27 |
| I3 | Subscriptions & Services | Catalogue & play; Online utilities; Connectivity; Member places; Curated deliveries | service type | pref | high | minor fixes | yes | 29 |
| J1 | Meat & Poultry | Fresh & frozen; Cured & smoked; Sausages; Cooked, tinned & potted | retail cut (beef, pork); species | mixed | medium | minor fixes | yes | 47 |
| J2 | Fish & Seafood | Fresh, frozen & live; Smoked; Salted & dried; Tinned; Roe & caviar | species; animal type | pref | low | minor fixes | yes | 33 |
| J3 | Dairy, Eggs & Alternatives | Milk; Cream & butter; Yoghurt; Cheese; Eggs; Powders & formula; Plant alternatives | cheese variety; product type | pref | medium | minor fixes | yes | 54 |
| J4 | Fruit & Vegetables | Fruit; Vegetables; Herbs; Fungi; Sea vegetables | species; cultivar named form | ladder | low | minor fixes | yes | 39 |
| J5 | Pantry Staples | 12 by what it is made from: grains … sauces, preserved produce, baking, tofu | variety or product type | mixed | low | rework (sub-families, rice) | yes | 62 |
| J6 | Coffee, Tea & Cocoa | Coffee; Tea; Cocoa; Herbal infusions | product or machine system; tea process | mixed | low | minor fixes | yes | 37 |
| J7 | Wine, Beer & Spirits | Wine; Beer; Cider & mead; Sake; Spirits; Liqueurs; Mixed drinks | grape or style; spirit type | mixed | high | minor fixes (one high finding) | yes | 31 |

Verdicts: 1 ready (B10), 41 minor fixes, 11 needs rework (A2, B8, C1, D4, E1, F2, F4, G2, H2, I2, J5; most only at one level). Reviews came before conformance; the rework points were then addressed in section 11 but not re-reviewed.

## 3. Shared conventions awaiting approval (CV-1 to CV-46)

Each is a yes/no question. C1 to C17 are in _conventions.md; additions from reviews follow the convention they amend. Reviews are named by letter.

- **CV-1** C1 maker ledger: core columns, with lines, tier entries, named forms and variants as separate tables; known-for kinds derived, not stored? [yes] A, B, C, D, F, G, I
- **CV-2** C1 amendment, maker classes: one domain-wide ledger, `maker_class` multi-valued, merged class list (G builder, converter, kit supplier, "manufacturer-retailer" dropped; H pharmaceutical, medical-device, supplement brand; I 16 service and publisher classes; F publisher to taxidermy studio; C breeder or registrant, tannery or mill, smith or forge); `platform_ids` leave the ledger? [yes] C, F, G, H, I
- **CV-3** C1 amendment, maker relations: `built_by_maker_id` on lines, `base_named_form_id` for converters, a maker-relations table (OEM, chip or panel supplier, board partner, licence) with `line_rank`, `licensor_id`, `authority_id` (ULAN, VIAF), an optional school table? [yes; school table optional] D, E, F, G, H, J
- **CV-4** Issuer table for states, central banks, postal and transit authorities, shared by F3 and F5; issuers are not makers? [yes] F
- **CV-5** Maker-ledger scope: seed from attested lists only, identity and platform makers first, a stated cap per category, retailer own-labels as class "retail own-label"? [yes] A, B, E, J
- **CV-6** C2 kind against named form: the choice-level test decides; `maker_bound`; specs, sizes, prints, colourways and editions are never named forms; traditional types are kinds only when sold as their own category? [yes] all
- **CV-7** Named-form test and admission: a non-maker named form is a design many makers make and buyers ask for by name; a maker line across kinds is a lines row, inside one kind a named form; load on demand, one attested row each, a cap per category? [yes] C, F, H, I
- **CV-8** C3 variant ledger: optional, sparse, one schema; never a level or a kind? [yes] A, D, G, I, J
- **CV-9** C3 amendment, variant types: add generation, trim, model_year, engine (G); edition, version, plan, licence scope, style with plan columns (I); configuration, partner build, regional model, hardware revision, bundle (D); vintage, bottler edition (J); concentration (H, if H-4 picks it)? [yes] D, G, H, I, J
- **CV-10** C4(a)–(c), (e) tier storage: never on a kind; tier entries per source with a disputed flag; measured ladders are attributes; platform labels dated tags; a scheme enters only with a fetched source, preferably a second from another region; schemes per category? [yes] A, B, C, D, E, H, J
- **CV-11** C4(a) amendment: a tier entry may sit on a variant or plan row when it is the maker's own ladder for one named form (exempt from C4(e)) or an external score of that version, a vintage score included? [yes] I, J
- **CV-12** C4 details: a maker's own range level is a tier entry with scheme = maker; a skill or level scheme (player_level) allowed; every scale typed as one of six classes (spec attribute, measurement, editorial, maker ladder, price band, platform tag) with test version, direction and `stale_after`? [yes] D, E, H
- **CV-13** C4(d) price band: one USD scheme for the whole domain (under 50 … over 15,000), from a dated, sourced list price; bands never a tier? [yes] A, B, C, D
- **CV-14** C4(d) extensions: bands above 15,000 up to over 5,000,000 USD (G); recurring and free prices annualised per plan, "0 (free)" band, domains at renewal price (I)? [yes] G, I
- **CV-15** JC2 grocery unit-price band, USD per kg or litre; J7 keeps the per-bottle band too? [yes] J
- **CV-16** C5(a)–(c) levels: at most four below the category, named form included; leaf optional for about 12 kinds or fewer (`leaf = null`); one axis per level within each sub-family? [yes] all
- **CV-17** C5(d) parts sub-family "Parts and accessories made for one <object>", exempt from the level-1 axis, extended to domains D and H and to any category that receives S3 parts (none for J, G2, C3, C8, I3); E2 may file parts in host leaves where the leaf names the host? [yes; E2 exception open] A, D, E, H
- **CV-18** C6 size is always an attribute with its standard; user is always a tag with generated department views? [yes; luggage exception is A-16] A, H
- **CV-19** C6 details: one user list (women, men, unisex, couples, baby, child, bariatric, adapted; "beginner" is a level scheme); a size class names a kind only when it changes what the object works with and sellers sell the sizes apart (film gauge, Mini-CD)? [yes] F, H
- **CV-20** C7 order inside a leaf: canonical kind first, then the stated key; named forms by maker, year, alphabet; variants by code or year? [yes] A
- **CV-21** C7 amendment: non-maker named forms first, by first-attested year (G, used in H2), against D's line_rank order or a maker-neutral order? [G amendment plus generated ladder views] D, G
- **CV-22** C8 scene vocabulary: one sourced list with core/adjacent strength, tagged at maker, kind and named form without inheritance, unsourced tags held back; extended beyond domain A (a domain-D list)? [yes] A, D
- **CV-23** C9 alias and homonym table, English label plus native script; new relation values "marketing name", "trade mark", "genericised name"? [yes] A, D, H, J
- **CV-24** C10 rule T: power source, technology and connectivity are attributes unless the key names the kind or the technology changes form or installation and a fetched source ranks the types apart? [yes] B, C, D
- **CV-25** Retail-facet test (C10(b) generalised): a retailer facet becomes a kind only when the form differs and a fetched source compares the types? [yes] H
- **CV-26** C11 rule R: a regional name is a kind only for a form no generic kind covers, labelled generically; otherwise a named form with a region tag; a region never names a sub-family or leaf? [yes] B, C, E, F, J
- **CV-27** C11 tie-break: the name must have its own category with fetched sellers in two regions? [yes] F
- **CV-28** C12 rule M: mounting defines a kind only when the body differs or the mount changes what it can safely do; otherwise installation is an attribute? [yes] B, C
- **CV-29** C13 compatibility ledger for sockets, mounts, battery platforms, caps, hive systems, hitch categories; platforms never levels? [yes] B, C, D, E
- **CV-30** C13 details: a relations table with platform type, region and status (D); one ledger shared by domain I and D5 with one `delivery` list (I); app ecosystems as rows with `kinds_served`, the app itself I1 (H)? [yes] D, H, I
- **CV-31** C14 multi-use kinds: defining rule, then the one family that holds all uses, then a multi-use sub-family; a generated view lists every use? [yes] C, E
- **CV-32** C15 toy or real: E1 when it cannot do the real object's job to that object's own standard; the real object in a child's size stays in its category? [yes] E, G
- **CV-33** C16 no individual-item facts: no certificates, grades, provenance or serials of one object? [yes] D, E, F
- **CV-34** Grading-scale registry (merged with D's condition-scale table): scales recorded with owner, type, steps and kinds served; no grade value ever stored? [yes] D, F
- **CV-35** C17 jurisdiction ledger for legal classes; never a level or a tag on the tree? [yes] E, G, H
- **CV-36** C17 clarification and extension: design and voluntary standards met are attributes (`standard_met`); every legal class (registration, licence, tax, device class, sale class, cosmetic or drug status) goes in the ledger; customs headings are evidence only; neither defines a kind? [yes] G, H
- **CV-37** Domain-G `propulsion` attribute (none, towed, muscle, wind, combustion, electric, hybrid, animal-drawn, with a primary flag)? [yes] G
- **CV-38** Photographic prints carry both `process` and `mount_format`? [yes] F
- **CV-39** Every S2 sources file gets a `fetch_status` column (full, partial, nav-only, failed) through a tools/ script, and excerpt-only facts go to S2_<CODE>_excerpts.tsv? [yes] F
- **CV-40** JC1 `standard` and `designation` tables (consortia are authorities, not makers); a designation binding one kind is a named form, spanning kinds a tag; Champagne, Port, Cognac and other wine and spirit names as a written exception (kinds)? [yes; exception for wine and spirits only] J
- **CV-41** JC3 multi-valued `supply_role` beside `maker_class` (farm, fishery, affineur, mill, roaster, winery, négociant, independent bottler and others)? [yes] J
- **CV-42** JC4 state, process and pack: storage state and same-product packs are attributes; a preserving process may define a level on its stated axis; a machine single-serve pack is a kind; a legal ladder on one product is an attribute, a legal name fixing a different composition a kind? [yes] J
- **CV-43** JC6 one `tradition` vocabulary, `origin` the place of production, no `cuisine` tag (J5 would keep one); `culinary_link` rows from any kind, designation or variety? [yes; no cuisine tag] J
- **CV-44** JC7 one variety table for breeds, cultivars, rice, coffee varietals, tea cultivars and grapes? [yes] J
- **CV-45** Registers for large named-form sets (flags, china patterns, cigar vitolas, feed lines) rather than tree rows (review B Q-X9, not in _conventions.md)? [yes] B
- **CV-46** Brand product lines of consumables (cleaning products, e-liquids, cigarette brands, feed recipes, insecticides) as ledger lines only, not named forms (review B Q-X10; B8 and B9 memos now keep them as named forms)? [yes] B

JC5 (formed, spread and mixed products) is answered by K-44, K-45 and K-46.

## 4. Framework (top-level) changes awaiting approval

The 229 entries in _framework_conflicts.md merge into **196 items, K-1 to K-196**, grouped by the key step they change; the complete list with every proposed sentence and its sources is Part 1 of STAGE2_OWNER_QUESTIONS.md. **[P]** marks an item that would move a stage-1 probe item from its round-5 home (20 items, 24 probe objects; 5 items for certain, the rest under one choice). [Rec] is the review's recommendation.

### 4a. The 25 most consequential, in full
1. **K-1 Sets and kits** (rev H X11, rev F X10, rev C K6; rev B diverges). "A set of objects of one kind is filed as that kind. A mixed set is filed by its item of greatest value, with its contents listed. A kit sold, standardised and compared as one object (first-aid kit, manicure set, tool kit, science experiment kit, mint and proof set) is a kind." Review B wants each piece filed as its own kind with a unit-of-sale tag. [Rec: H/F sentence plus B's tag for suites] [P: emergency survival kit]
2. **K-2 Cables** (rev D X-11(b)). "A cable with a proprietary connector made for one device follows it (S3); a cable with standard connectors (USB, HDMI, audio, instrument, microphone, MIDI) is D1." [Rec: yes]
3. **K-4 Batteries** (rev C X3). "A battery pack or charger made for a maker's cordless platform is C1, whatever tools or garden machines it runs. A battery made for one device follows it (vape batteries B9). A loose standard-size cell is C8." [Rec: yes]
4. **K-6 Vehicle-fitted electronics** (rev D O-10, rev G X-10a). Car audio, dashcams, mounted sat-navs, bike computers and OBD trackers made for mounting are G1 under S3; G1 memo dissents on sat-navs. [Rec: G1]
5. **K-9 Albums, binders and holders** (rev F X5). "A holder made for one object follows it (S3). An album, binder, stock book or tray made to hold several objects is B1 when empty. A filled photo album or scrapbook is F5; a blank scrapbook album is C4." [Rec: yes] [P: photo album F5→B1]
6. **K-24 Packaged prepared kinds** (rev J §6; J7 Q5). The log itself conflicts: hard seltzer "logged as a Culinary gap" against "RTD cocktails and hard seltzer are J7.7". Also: a dry noodle brick J5, a cup a ready meal. [Rec: J7.7; brick J5] [P: canned gin and tonic]
7. **K-31 The H1/H2 line** (rev H X3). "A product is H2 when its labelled main purpose is to treat, relieve or prevent a named condition, or it contains an active ingredient sold only as a medicine in every sourced jurisdiction. Cosmetic purposes are H1, sunscreens and anti-dandruff products included. Legal status goes to C17." [Rec: yes]
8. **K-34 Spectacles and frames** (rev H H2-1, rev A B9). "Corrective spectacles, reading glasses and prescription sunglasses, with frames and lenses, are H2; plano fashion frames and non-corrective sunglasses are A4." [Rec: yes]
9. **K-44 Spreads, pastes, dips** (rev J X2, high). "A spread, paste or dip eaten with other food (rillettes, jar pâté, taramasalata, hummus, pesto) is J5, whatever it is made from. A pâté or terrine sold as a loaf or slice is J1 or J2. Butter and ghee are J3." Needs a dairy exception. [Rec: yes] [P: Labna]
10. **K-45 Formed products** (rev J X3, high). "A sausage, loaf, patty, ball or other shaped product made mainly of one meat, of fish or of a plant protein, seasoned but not coated, filled or sauced, is a grocery in its source category. Coated, filled or sauced products are prepared." [Rec: yes] [P: porchetta, glazed ham]
11. **K-46 Mixed products** (rev J X5). "A mix of kinds from one category is filed under the kind that makes up half or more of its weight, otherwise a final 'mixed' kind; a named spice blend is a kind; a mix across categories by its item of greatest value." [Rec: yes]
12. **K-47 Edible insects and other animals** (rev J X11). Extend J1 to "meat, poultry, game and other land animals eaten (frogs, insects)"; snails J2. Otherwise insects fall to X0. [Rec: yes]
13. **K-60 Houseboats and tiny houses** (rev G X-1, high). "Test the object as made. A hull with its own propulsion and steering made to navigate, and a trailer, caravan or motorhome made for the road, are G1, however long kept in one place. A dwelling made to stay in one place is G2: a floating home without propulsion, a static caravan or park home, a park model, the tiny house on wheels." [Rec: yes]
14. **K-62 Non-residential buildings** (rev G question 16). Commercial, industrial and institutional buildings in G2 by function, or out of scope. [Rec: none]
15. **K-73 Plants in containers** (rev C Q27). "A living plant in any container, basket, kokedama or terrarium is C3 whatever the container's value." The C3 memo still uses greatest value. [Rec: yes]
16. **K-99 Household line for tractors** (rev C X9). Replace step 12's user test: "… including lawn and garden tractors without a rear power take-off and a Category 1 or larger three-point hitch." [Rec: design test] [P: garden tractor]
17. **K-107 Religious medals** (rev F X1, high). "A medal made for devotion is F4 when loose and A3 when made with a chain or bail to be worn; a medal struck to commemorate or reward, whatever its subject, is F3." [Rec: yes]
18. **K-118 Cards, scrip and covers** (rev F X2, high). "Payment, gift, transit, membership and key cards are F5, live or expired. Tokens and paper issued to circulate as money are F3; vouchers redeemable only with the issuer F5. Postal stationery and administration-issued or first-day covers are F3; any other used envelope or postcard is F5." [Rec: narrow rule]
19. **K-125 Helmet, goggle and riding-gear line** (rev E §4, rev A B2). Weapon threat E4; a helmet or goggles made for one sport E2; other hazards A1, cycling and motorcycle helmets included. One rule for riding hats and tall boots. [Rec: E2 for one-sport helmets; riding gear none] [P: riding hat]
20. **K-127 Court and gym shoes** (rev A B13, rev E 20). "A shoe is E2 only when made for one sport and sold as a performance model with sport-specific soles or spikes; basketball- and tennis-lineage sneakers worn every day are A2." [Rec: yes]
21. **K-139 Photographs** (rev F X3). "A photographic print issued as an edition, or signed or stamped by its maker as a work, is F2; every other print, slide or negative, whoever is shown, is F5." Step 19 drops "of the owner's own life". [Rec: yes] [P: cabinet card]
22. **K-154 D5 "divided by platform and carrier"** (rev D O-51). Game software kinds by carrier type with platform an attribute and a by-platform view, or one kind per platform and carrier (120 to 200 kinds); reword the D5 line to match C13. [Rec: carrier type]
23. **K-170 Writing against drawing** (rev C X7). "File by the maker's first-named use: handwriting, lettering, calligraphy and shodo C5; drawing, comics and painting C4; both named, C5." [Rec: yes] [P: fudepen C4→C5]
24. **K-173 Chainsaws, axes, log splitters** (rev C X1, high). Three memos give three answers. (a) hand-held chainsaws and pole saws C2, axes, wedges and splitters C1; or (b) all chainsaws C1. [Rec: (a)]
25. **K-194 Earth-moving machines** (rev C X2, high). "A self-propelled machine made to dig, lift, load or move material (excavator, skid steer, telehandler, forklift, dumper) is C1, unless it does a farm or forestry job (C7) or keeps gardens and grounds (C2)." [Rec: yes]

### 4b. The other 171, one line each
**S3 parts and general rules**
- K-3 Chargers: generic D1; made for one device follows it; for standard cells C8 [D1]
- K-5 Phone-only gimbals, selfie sticks, clip-on lenses and controllers D2 under S3 [D2]
- K-7 Roof boxes and racks fitted to one vehicle G1; free-standing racks B1 [yes]
- K-8 TV brackets, stands, monitor arms: D3 part, C8 or B1 [none]
- K-10 Laundry baskets B6 in the S3 never-parts sentence [yes]
- K-11 Limits of "cleaning products B6": salts and descaler split B6/B7/B8; lens solution H2; waterproofing spray B6 or C8 [mixed]
- K-12 Welding wire, solder, discs for one tool C1; general sandpaper C8 [yes]
- K-13 Tools made to service vehicles C1 [yes]
- K-14 NVR/DVR sold for security cameras B8; network drives D1 [yes]
- K-15 Astronomy cameras need a line; universal tripods D4 [tripods D4]
- K-16 Toys-to-life figure E1, portal D5 part; Toniebox figures D3 parts [yes]
- K-17 Studio backdrops B2, studio furniture B1, lights D4 [yes]
- K-18 Machine dust extractors C1; wet-dry vacuums B6 [yes]
- K-19 First-aid kits H2 whatever vehicle they are made for [yes]
- K-20 Watch chains for a pocket watch A5 (S3); fobs worn alone A3 [yes]
- K-21 Belt buckles A1 as belt parts [yes]

**Step 1 scope**
- K-22 "Alcohol-free versions of beer, wine and spirits" [yes]
- K-23 Par-fried and coated frozen vegetables OUT [yes]
- K-25 En primeur and undelivered casks OUT; delivered cask J7 [yes]
- K-26 Live fish OUT; protected-species flag [yes]
- K-27 Printed share certificates, bonds, cheques F5 as objects [yes]
- K-28 SIM card F5; eSIM profile with its I3 plan [yes]
- K-29 Domain-name registration I2 [yes]
- K-30 Leased gas cylinder in or out; delivered fuel OUT [none; OUT]

**Step 2 health**
- K-32 Massagers: sexual H3, treatment H2, comfort H1 [yes]
- K-33 Intimate, menstrual, baby and body-replacement goods: H1/H2/H3/A1 list [as listed]
- K-35 Coloured plano contact lenses H2 [H2]
- K-36 Beauty supplements H2 [yes]
- K-37 Medical software H2 [yes]
- K-38 Low-vision magnifiers H2, other magnifiers C6 [yes]
- K-39 Care beds, pressure-relief mattresses, lift recliners H2 [yes]
- K-40 Weighted blankets, orthopaedic pillows B2 unless sold to treat [yes]
- K-41 Therapeutic footwear A2; orthotic inserts H2 [A2]
- K-42 Medical face masks A1 or H2 [A1]
- K-43 Personal alarms and fall detectors H2 or B8 [none]

**Step 3 groceries**
- K-48 Bitters by the dash J5; bitter liqueur J7 [yes]
- K-49 Dry drink mixes J6 when coffee, tea or cocoa leads; else OUT [yes]
- K-50 Cocoa butter and paste J6 or J5 [J6]
- K-51 J6 covers roots, bark, fruit, roasted grains; kava named [yes]
- K-52 Tinned and plain-cooked meat J1 [yes]
- K-53 Margarine J5; spreads with butter J3 [yes]
- K-54 All nuts J5; fresh olives J4, cured J5 [yes]
- K-55 Dried dairy (kashk, qurut) in J3 [J3]
- K-56 Plain fermented milk drinks J3; flavoured OUT; ayran, lassi [J3]
- K-57 Cooked, pickled, preserved eggs J3 [yes]
- K-58 Brewing ingredients J5, equipment B5 [yes]
- K-59 Coated nuts, trail mix need a rule; cake mixes J5; sprinkles OUT [partly]

**Step 4 property**
- K-61 Park model RV G2 [yes]
- K-63 Annexe with own sink, toilet, entrance is a dwelling [yes]
- K-64 Sauna cabin G2; portable sauna B7 [yes]
- K-65 Tents, yurts, tipis E2, or G2 on a permanent platform [none]
- K-66 Pergola and decking kits by structure; loose boards C8 [yes]
- K-67 Garage or bay held as land G2; rented bay OUT [yes]

**Step 5 software and subscriptions**
- K-68 Seat structure is a plan attribute [yes]
- K-69 "In-game and platform items" wording [yes]
- K-70 I3 gaps: goods rental, hosting, creator, car-sharing in; one-off eSIM OUT [yes]
- K-71 Eleven I boundary sentences (classes, backup, maps, launchers, assets, unlocks, presets, reference, credits, NFT memberships) [yes]

**Step 6 plants**
- K-72 Real Christmas trees C3, artificial B4 [yes]
- K-74 Preserved and artificial plants B4 [yes]
- K-75 Sprouting seed to eat J5, to grow C3; live tobacco and cannabis plants C3 [yes]

**Step 7 specimens**
- K-76 Single-animal mount F6; composition with other materials F2 [yes]
- K-77 Replicas by what they are; simulants not gemstones [yes]
- K-78 Identified shell F6, craft assortment C4; drilled pearl C4, strung A3 [yes]
- K-79 Human specimens OUT [yes]
- K-80 Preserved or emptied specimens F6 [yes]

**Steps 9 and 10**
- K-81 Collars and cuffs with fixing points H3; ornament A3; garments A1 [confirm]
- K-82 Restraint furniture H3; positioning cushions B2 [yes]
- K-83 Fighting knives E4; EDC folders C1 [yes]
- K-84 Slingshots, blowguns, shuriken E4 unless toys; holster A4 [holster A4]
- K-85 Ordnance OUT except deactivated display pieces B4 [yes]
- K-86 Reloading presses C1; loose fittings E4; reproduction rule E4/E2/B4/E1 [yes]
- K-87 Wushu implements E2, B4 or E4 [none]
- K-88 Personal attack alarm B8 or E4 [B8]

**Step 11 vehicles**
- K-89 Electric kick scooter G1 [yes]
- K-90 Powered boards and eFoils G1; unicycle E2 [memo] [P: unicycle G1→E2]
- K-91 Children's pedal bicycles G1 [yes]
- K-92 Racing and off-road motor vehicles G1 by body [yes]
- K-93 Unimog, ATV, UTV G1 even when powering implements [yes]
- K-94 Trailers that only carry G1; wagons that process C7 [yes]
- K-95 Pet strollers and dog bike trailers G1 or B10 [G1]
- K-96 Parachutes E2 [yes]
- K-97 Hobby RC and FPV drones E1; filming drones D4 [yes]
- K-98 Mobility scooters stay H2 [yes]

**Steps 12 and 13**
- K-100 Field irrigation C7; garden irrigation C2 [yes]
- K-101 Herd-scale test; EID readers C7 or B10 [test yes]
- K-102 Animal group as B10's first axis (Appendix A exception) [yes]
- K-103 Child gates B8, pet-only gates and cameras B10; GPS pet tracker [tracker split]
- K-104 Fish ponds, liners, pond pumps C2 [C2]
- K-105 Bee suits A1 or B10 [A1]
- K-106 Honey extraction gear B10 [B10]

**Step 14 religious**
- K-108 Icons, thangkas, altarpieces, shrine statues, crucifixes F4 [yes]
- K-109 Tarot sold for card play E1; for divination F4 [yes]
- K-110 Singing bowls E3 unless made for a rite [yes]
- K-111 Prayer beads F4 if sold for prayer, A3 if sold as a necklace [by how sold]
- K-112 Printed religious texts F1; Torah scroll, mezuzah, prayer card F4 [yes]
- K-113 Rite candles and prayer rugs F4; meditation cushions B2 [yes]
- K-114 Spirit boards, runes, I Ching F4 when sold for divination [yes]
- K-115 Masonic implements F4; smudge bundles B4 [yes]
- K-116 Stone tōrō, bon lanterns, shimenawa, kadomatsu: reviews B and F differ [P: stone lantern, ishi-toro B3→F4/B4]
- K-117 Carried good-luck tokens have no home [none] [P: omamori]

**Step 15 money and awards**
- K-119 Championship rings and belts F3 [yes]
- K-120 Game money E1; prop and souvenir notes F3 [yes]
- K-121 Panini-type stickers F3 [F3]
- K-122 Coin or ingot with a bail A3, without F3 [yes]
- K-123 Worn crown A3; regalia F3; toy crown E1 [yes]

**Steps 16 and 17 worn and carried**
- K-124 Watch with time as main display A5; sensing device D2 [yes]
- K-126 E2 swimwear means competition and sport swimwear only [yes]
- K-128 Hosiery and tabi socks A1; overshoes and jika-tabi A2 [yes]
- K-129 Banded headwear A1; pinned ornaments A3; plain clips H1; bindi [yes]
- K-130 Toy jewellery E1; child-size real jewellery A3 [yes]
- K-131 Insulated lunch and cool bags B5 [yes]
- K-132 Pencil cases and toiletry bags A4, or C5 and H1 [sources differ]
- K-133 Powered hand fans B7; patio umbrellas B1 or C2 [fan B7] [P: garden parasol]
- K-134 Furoshiki B2 [B2]
- K-135 Head-worn loupes and eclipse glasses C6 or A4 [open]
- K-136 Plush bag charms E1 or A4 [none]
- K-137 Chalk and boot bags need a sentence; quivers A4 [quivers A4]

**Steps 18 to 21**
- K-138 Skin insect repellent H1; room repellents B8 [H1] [P: insect repellent B8→H1]
- K-140 Kept printed ephemera F5 by form [yes]
- K-141 Home recordings on a carrier F5; negatives and slides named [yes]
- K-142 Maps F1, map-like art prints F2 [yes]

**Steps 22 to 24 music and electronics**
- K-143 Studio or listening gear by the maker's own category [yes] [P: in-ear monitors]
- K-144 Dual-use microphones by stated first use [yes]
- K-145 Stage lighting B3; piano benches B1; fog machines B4 [as listed]
- K-146 Jukeboxes D3 unless sold as arcade games [yes]
- K-147 Workshop and trade measuring C1; sample measuring C6; air-quality monitors C6 [yes]
- K-148 Golf and hunting rangefinders E2; building C1; binoculars C6 [yes]
- K-149 Experiment kits C6; coding toys E1; component kits D1 [yes]
- K-150 DAPs, streamers, set-top boxes, external DACs D3; internal sound cards D1 [yes]
- K-151 Camcorders and action cameras D4; golf GPS, landlines D2 [D4 yes]
- K-152 Handheld gaming PCs D5 [yes]
- K-153 Enclosing headsets D5; see-through smart glasses D2 [yes]
- K-155 Video cabinets D5; pinball, claw cranes, slot machines E1 [yes]
- K-156 Photographic paper D4; trail cameras D4, B8 or E2 [paper D4]
- K-157 Portable power stations B7 [B7]
- K-158 Copy paper, label printers, smart notebooks C5 or D1/D2 [none]

**Steps 25 to 27**
- K-159 Rebounder under about 1.2 m E2; garden trampoline E1 (cut needs a source) [yes]
- K-160 Toy kites, discs, balls E1; regulation ones E2 [yes]
- K-161 Sport bottles and hydration packs B5 or E2 [none] [P: camping water bladder]
- K-162 Head torches, dive lights B3; weapon lights E4 [yes]
- K-163 Decoys, blinds, calls, targets E2; arrows, bipods, rests E4 [yes]
- K-164 Carried cigar and cigarette cases B9; standing humidors B1 [yes]
- K-165 All cannabinoid balms B9; intimate oils H3 [yes]
- K-166 Gas cylinders and flints C8; hookah charcoal B9 [yes]
- K-167 Scales, trays and stash jars [none]
- K-168 Opium, salvia, psychoactive mushrooms need a scope sentence [none]

**Steps 28 and 29 craft and garden**
- K-169 Candle, soap, resin, glass, basketry, floristry crafts into step 28 [none]
- K-171 Cutting tools, adhesives and stamps by material worked [yes; scissors open]
- K-172 Pottery wheels C4; plotters, heat presses, craft paints [partly open]
- K-174 Growing media and decorative gravel C2; aggregate, paving, edging, fencing C8 [yes]
- K-175 Water pumps for gardens and pools C2; field C7; drainage C1 [yes]
- K-176 All swimming-pool equipment and chemicals C2; hot tub gear B7 [yes]
- K-177 Water butts C2 or B7 [none]
- K-178 Garden pesticides C2; household pest killers B8 [yes]
- K-179 Cachepots, plant stands, children's garden tools [mostly none]

**Step 30 household**
- K-180 Open candle holders B4; carried lanterns B3; decorative lanterns B4 [yes] [P: rush light, bonbori, chochin]
- K-181 Task light strips B3; string lights B4 [yes]
- K-182 Every plate B5, or hang-only plates B4 [review B: B5] [P: Kosiv ceramics]
- K-183 Diffuser oils B4 unless sold to treat; wax warmers need a home [yes]
- K-184 Basin built into a vanity B7; cabinet alone B1 [yes]
- K-185 Heated towel rails B7; heated airers B6 [yes]
- K-186 Heating appliances B7; taps, valves, trays, enclosures C8 [yes; trays open]
- K-187 Security gravel, fence spikes, film, bird spikes [none]
- K-188 Freestanding letterboxes B8; door letter plates C8 [yes]
- K-189 Curtain poles and rug underlay B2 [B2]
- K-190 Medical chairs H2; massage chair H1; workbench C1 or B1 [sources differ] [P: workbench]
- K-191 Bookends, jewellery boxes, decorative trays need homes [route each]
- K-192 Flagpoles by S3 with the flag; safety signs C8 [yes] [P: flagpole]

**Steps 31 and 32**
- K-193 Envelopes C5; packing materials C8; storage boxes B1 [yes]
- K-195 Fencing and electric-fence energisers C8 [yes]
- K-196 Cabinet knobs C8; lockset with a lock B8 [yes]

## 5. Per-category owner questions

The complete per-domain lists (A-1 … J-17) are Part 2 of [STAGE2_OWNER_QUESTIONS.md](STAGE2_OWNER_QUESTIONS.md): **228 questions** (A 26, B 34, C 19, D 26, E 24, F 26, G 18, H 14, I 24, J 17), after removing the digest questions that sections 3 and 4 already ask.

### 5a. The 15 most consequential
1. C-1 C1 first level by the work done, not hand/power/machine [work done] (C1 §11; rev C Q1)
2. A-7 A2 level 1 as form families; safety footwear an attribute and view [yes] (A2 §10.1)
3. B-9 B8 hazard-first top level, child a user tag [yes] (B8)
4. E-1 and E-10 E1 play families; one die-cast kind with scale an attribute [yes; one kind] (rev E 1, 12)
5. F-2 F2 figurines in material leaves shared with sculpture [no split] (F2 §10.3)
6. F-3 F4 tradition a tag, never a level or exception kind [yes] (F4 O1)
7. G-13 and G-14 G2 Land by principal use; house forms as attributes [yes] (G2)
8. H-2 and H-8 H2 only home-kept prescription classes; medicines at OTC use class, ingredient an attribute with ATC [yes; attribute] (H2)
9. I-2 I2 level 1 by what the held data is for [restated A] (I2)
10. I-4 I1 business software at Capterra headline depth (40 to 80 kinds), not G2 depth (2,000) [Capterra] (I1)
11. J-11 J5 one sub-family axis and rice by grain type [confirm] (J5)
12. J-1 Cuts as kinds for meat, shape family for pasta [(b)] (J1, J5)
13. C-4 C3 genus by default, species only in a closed list [closed list] (rev C Q4)
14. D-20 D4 lenses by optical design, film cameras by viewing system, film by process [yes] (rev D O-41 to O-44)
15. E-2 E2 sport families as a level, not 130 flat leaves [families] (rev E 2)

### 5b. ★ questions from the digests, by domain
- **A:** A-7 A2 form families; A-12 A3 two-step top; A-23 A5 complication axis. Moved: XA 1 → CV-16; XA 2 → CV-6.
- **B:** B-6 B5 stage of kitchen work; B-8 B7 three media; B-9 B8 hazard-first; B-10 B9 role-first; B-11 B10 "several animals" from two groups (axis itself K-102).
- **C:** C-1 C1 work done; C-3 C3 first split; C-4 C3 kind rank; C-6 C7 tractor kinds by design. Moved: XC 10 → CV-24, CV-28.
- **D:** all moved: XD 1 → K-154; XD 2 → CV-17; XD 3 → CV-30; XD 4 → K-2, K-3; XD 5 → K-6.
- **E:** E-1 E1 play families; E-2 E2 families; E-3 E3 role-first; E-4 C11 for Japanese and Chinese names. Moved: XE 4 → CV-31 to CV-35.
- **F:** F-1 F3 issuing function; F-2 F2 figurines; F-3 F4 tradition tag; F-4 F6 cut-state rule. Moved: XF 1 → K-9.
- **G:** G-1 G1 mode first; G-3 G1 legal classes in C17. Moved: XG 11 → K-92; XG 17 → K-60; XG 19 → K-62.
- **H:** H-2 H2 prescription scope; H-4 H1 fragrance kind; H-8 H2 medicines depth. Moved: XH 8 → CV-17.
- **I:** I-1 I1 function-first; I-2 I2 level 1; I-4 I1 business depth; I-21 I1 releases as named forms. Moved: XI 36 → CV-11.
- **J:** J-1 cuts; J-2 J1 first axis; J-4 J2 form first; J-11 J5 restructure. Moved: XJ 1 → CV-40.

## 6. Risks and next steps

**Risks.**
- No stage-2 proposal has been tested blind. The conformance pass changed many trees after their reviews, and the 11 rework verdicts were not re-reviewed.
- Sources still contradict each other on several objects: workbenches (K-190), chainsaws (K-173), plants in pots (K-73), sets (K-1), labneh (K-44), Japanese lanterns (K-116), pencil cases (K-132), hard seltzer (K-24).
- Size can grow fast with some answers: C3 up to 1,400 kinds with species kinds, I1 about 2,000 at G2 depth, F6 550 to 900, J5 550 to 650, D5 120 to 200 carrier kinds.
- Most fetched evidence is English, US, UK or Japanese. Chinese retail hosts failed (rev D O-13), and many tier sources fail the two-region test (A3, A4, A5, E1 to E4).

**After the owner answers: a v0.7 round.**
1. Write v0.7 from the approved K items and conventions, including the Appendix A exception for B10 (K-102) and the D5 wording (K-154).
2. Re-place blind, as in rounds 4 and 5: three fresh Sonnet placers on all 953 round-5 items, plus a new regression set of the objects named in the K items (about 400). Check that the 24 [P] probe objects land where the answers put them and that no other item moves. Then one cold Opus audit.
3. New for stage 2: a blind kind-level test for the 11 rework categories, where placers file about 30 sourced objects each into the memo's sub-families and leaves.

**Data-phase order.**
1. First, the tools/ scripts and shared tables every category writes to: maker ledger and lines, tier entries, named forms, variants, aliases, compatibility, jurisdiction, standard and designation, variety, issuer and grading scales, and the `fetch_status` column (CV-39). Doing these once avoids rework in 53 categories.
2. A1 and D1: the owner's pilot pair, and A1 carries the BRIEF's depth demand for subculture brands. Both have only minor fixes.
3. Ready or nearly ready categories with few †: B10 (ready, 23 †), C6 (closest to ready, 30 †), I1 (20), D5 (24), J4 (22), J2 (25), B3 (25), J3 (27). Fewer unsourced names means less is blocked at load.
4. The other minor-fix categories, each after its sourcing batch.
5. The 11 rework categories last, after the owner answers and the kind-level test.

**Sourcing backlog (†).** 2,568 claims need a fetched page before they enter data (rev D O-14 asks the same). By domain: B 405, C 381, F 350, E 311, J 279, D 240, A 234, H 172, I 117, G 79. Heaviest memos: E4 98, F4 82, C8 80, E1 78, F3 77, H2 76, E2 74. Also needed: second-region tier sources (CV-10), H sources listed in H-13, the J7 second pass (J-17), the trampoline cut (K-159), and a list of excerpt-only facts (CV-39). Run one Sonnet sourcing batch per domain, through WebSearch/WebFetch or the Parallel tools only.
