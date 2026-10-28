# AUD3_C — cold audit: C1 (excl. Knives, multi-tools & axes), C2, C3, C5, C7, C8

All counts computed from rebuild/reader/<CODE>.json and the brand/tradition registers on 2026-10-28. Facts from my own knowledge are marked "to verify".

---

## C1 Tools & workshop (237 kinds, 244 archetypes outside the Knives dept)

**Brand mode:** mixed. Tier for power tools, welding, ladders, site kit and storage; variety for woodworking hand tools, machinist tools and vintage machines.

### Gaps for hobbyists
- **C1-1 The power-tool icons are missing.** The Power tools dept has 48 kinds and 26 archetypes, and 17 of those archetypes are battery platforms. 17 kinds have no archetype, model or range. Track saw, Reciprocating saw and Magnetic drill are fully empty, yet the Festool TS 55 track saw and the Milwaukee Sawzall (grep "Sawzall" and "TS 55": 0 hits) are the archetypes people name. Mafell, HiKOKI/Metabo HPT, Flex and AEG are absent (AEG has no C1 hits; HiKOKI has none anywhere). Fix: add 1–3 archetypes for each enthusiast kind (track saw, router, planer, mitre saw, oscillating tool) and the missing brands.
- **C1-2 There is no jigs and guides shelf.** Kreg pocket-hole jigs, Leigh dovetail jigs, doweling jigs, shooting boards and saw sets have 0 hits across reader/. Fix: add a "Jigs, guides & sharpening aids" shelf to Woodworking hand tools.
- **C1-3 Mechanics' tools and tool storage have no archetypes.** Tool storage has 7 kinds and 0 archetypes. Matco, Mac Tools and Gerstner have 0 hits, and Facom, Hazet, Stahlwille, KTC and Koken are missing (to verify). Fix: make Tool storage mixed, add Snap-on roll cabs and Gerstner chests as archetypes, and add these makers.
- **C1-4 The electronics bench is thin.** Soldering iron has no archetypes (Hakko FX-888 appears only in `m`). Pinecil, bench power supply and logic analyser have 0 hits. Fix: add archetypes for Hakko FX-888, Weller and Pinecil, plus a bench power supply kind.

### Too much detail
- **C1-5 Many near-identical bar and hammer kinds sit empty.** The Hammers shelf has 13 kinds, and 9 of them (Club, Ball-pein, Cross-pein, Sledgehammer, Brick, Slater's, Pry bar, Nail puller, Lifting bar) have no x, m or t. Fix: merge Pry bar, Wrecking bar, Nail puller and Lifting bar into one kind, and promote Estwing (now in `m`) to an archetype.
- **C1-6 Nailers are split by gauge.** Finish, brad and pin nailers are separate kinds that differ only by gauge. Fix: make them one "Finish nailer" kind with 15/16/18/23-gauge types.
- **C1-7 PPE types read like standards lists.** Chainsaw trousers have 8 types (EN ISO numbers, classes, designs) and Work gloves have 9. Fix: cut these to 3–4 buyer-level types.

### Confusing organisation
- **C1-8 The "Japanese woodworking tools" shelf sorts by tradition while every other shelf sorts by form.** Ryoba sits apart from Back saw and nomi apart from chisels, yet Kebiki and Shirabiki are already filed by form under Measuring. Fix: shelve by form, tag "Japanese", and add a daiku dōgu tradition. Merge the duplicate traditions ("Banshu Miki forged blades" and "Miki blades") and brands ("Lie-Nielsen" and "Lie-Nielsen Toolworks"). Relink the Sheffield and Solingen kitchen-knife forms to B5.
- **C1-9 Some kinds sit in the wrong shelf.** Hacksaw, File and Rasp are filed under woodworking. CNC and laser machines are in C1 while 3D printing is in D1. Fix: add a metalwork hand-tools shelf and a "Maker machines" cross-link view.

### What it would look like (Power tools)
```
Track saw
  Festool TS 55 (Festool, 1999?) to verify
    v: TS 55 EBQ → TS 55 REBQ → TSC 55 cordless
    dt: blade 160 mm · plunge depth · rail system
  Mafell MT 55 cc (Mafell)
Reciprocating saw
  Sawzall (Milwaukee, 1951) → M18 FUEL generations
Router
  ELU plunge router (kept)
```

Priority: medium
Fix size: medium

---

## C2 Garden & grounds (140 kinds, 198 archetypes)

**Brand mode:** mixed. Tier for machines, pools, soil and feed; variety for hand tools, bonsai tools and the grill/pizza-oven end.

### Gaps for hobbyists
- **C2-1 Fire pits, chimineas and patio heaters are missing everywhere.** Grep finds "fire pit" only as a C8 log description and an F4 homa pit; "chiminea" and "patio heater" have 0 hits. Solo Stove appears only in E2. Fix: add a "Fire pits & patio heating" shelf to Outdoor cooking (fire pit, fire bowl, chiminea, patio heater; Solo Stove and Breeo to verify).
- **C2-2 BBQ enthusiast kit is lumped into one kind.** "Barbecue tools & accessories" is one kind with 10 types and 0 archetypes. Meat thermometers (Thermapen, Meater) live only in B5. Kamado has 3 archetypes and Offset smoker 3; Primo, Komodo Kamado, Recteq and Lone Star Grillz have 0 hits (to verify as icons). Fix: split out Chimney starter, Grill thermometer/controller (cross-link B5) and Rotisserie, and add the missing kamado, pellet and offset makers.
- **C2-3 Bonsai pot makers are not linked.** The register lists Tokoname potters (Gyozan, Reiho, Yamaaki, Kaneshin), but the Bonsai pot archetypes are generic ("Tokoname bonsai pot"). Fix: add potter archetypes with `mk`.

### Too much detail
- **C2-4 Many empty one-word kinds.** Plant stake, Plant support frame, Trellis, Garden arch, Obelisk and Plant label are 6 kinds with no content. Window box, Cachepot and Vertical garden planter are empty too: Pots, beds & supports has 9 fully empty kinds out of 18. Soil improver, Mulch, Topsoil and grow bag are 4 empty kinds. Fix: make one "Plant support" kind and one "Compost, soil & mulch" kind with types, and fold the empty pot kinds into Plant pot types.
- **C2-5 Pool cleaners and hose fittings are split too finely.** There are four pool-cleaner kinds (robotic, suction-side, pressure-side, robotic skimmer), and Pool filter carries a "Spare parts" type. Hose connector and Hose spray gun are separate kinds. Fix: make one "Pool cleaner" kind with types, one "Hose fittings" kind, and one spare-parts entry.
- **C2-6 The "Barbecue grill" kind is a near-duplicate catch-all.** It has no types and 3 models. Fix: dissolve it into the other grill kinds.

### Confusing organisation
- **C2-7 Items and registers are duplicated across categories.** Silky Gomboy and Bahco Laplander appear both in C1 Folding saw and in C2 Pruning saw. "Barbecue fuel" (lump, briquettes, binchōtan, pellets) duplicates C8's Lump charcoal, Charcoal briquettes, Wood pellets and Smoking wood kinds. The Kishū binchōtan tradition is in both the C2 and C8 registers. ARS and ARS Corporation are two brand entries. Fix: keep fuel in C8 with a cross-link, keep folding saws in C2, and merge the duplicate register entries.
- **C2-8 Ponds sit under Watering, but koi and pond filtration are in B10.** Fix: rename the shelf "Pond liners & pumps" and cross-link B10.

### What it would look like (Outdoor cooking)
```
Kamado grill
  Big Green Egg (Big Green Egg, 1974) → sizes MiniMax…XXL
  Kamado Joe Classic Joe → I/II/III
  Primo Oval (to verify) · Komodo Kamado (to verify)
Fire pit (new)
  Solo Stove Bonfire (to verify) → 1.0 / 2.0
  dt: steel, cast iron · smokeless double-wall
Grill thermometer (new; cross-link B5 Thermapen, Meater)
```

Priority: medium
Fix size: small

---

## C3 Living plants & cultures (229 kinds, 824 archetypes)

**Brand mode:** variety (breeders and seed houses). Tier only for Christmas trees and everyday seed.

### Gaps for hobbyists
- **C3-1 Collector genera are missing.** Helleborus, Clivia, Agapanthus, Bougainvillea, Mandevilla, Fritillaria, tree ferns (Dicksonia), hardy palms (Trachycarpus), Gladiolus, Ranunculus and Freesia have 0 hits in all of reader/. Auricula appears only as a C2 pot description. Garden chrysanthemums (exhibition mums) exist only as cut flowers. Fix: add kinds with RHS/society-registered archetypes. Also add a Hedging & topiary kind (Buxus, Taxus, beech) and a dwarf conifer kind.
- **C3-2 Cannabis is lumped into one kind.** "Cannabis plant" has 6 types and a single archetype, "Autoflowering cannabis". J10 holds only "Cannabis flower" and has no strains. Fix: add landrace and strain-family archetypes (Skunk #1, Northern Lights, OG Kush; to verify), with breeders in the register (Sensi Seeds, Dutch Passion; to verify).
- **C3-3 The plants register is missing.** RULES requires a living-plants register that mirrors the breeds register, but reader/species/ holds only F6. Fix: build a C3 species register keyed to POWO or WFO and keep popular taxa in the tree.

### Too much detail
- **C3-4 Placeholder archetypes.** 12 archetypes are literally "Other …" ("Other AGM hostas", "Other basils", "Other famous heirlooms", "Other common figs"…). More are vague buckets: "US apricot cultivars", "Runner bean cultivars", "Collectors' AGM cultivars", "Variegated cultivars", "Registered Heliamphora cultivars". Fix: replace each with 2–5 named cultivars or delete it.
- **C3-5 Type lists are copy-pasted across kinds.** The same 19 bonsai style types repeat on 7 bonsai kinds; 5 Christmas-tree kinds have identical "cut; pot-grown; rooted" types and 0 archetypes; the seed kinds share the same 6 packet types. Fix: move bonsai styles to a department attribute or view, and make one "Christmas tree" kind with the species as archetypes.

### Confusing organisation
- **C3-6 Old garden rose double-counts its classes.** Its 11 classes (gallica, damask…) appear both as 11 types and as 11 archetypes. Shrub rose archetypes are groups too ("Hybrid musk roses"). Fix: make the classes types and use named roses ('Charles de Mills', 'Madame Hardy'; to verify) as archetypes.
- **C3-7 Archetype use is inconsistent.** Camellia has 1 archetype (C. japonica) while 8 named cultivars sit in `m`. Tomato and chilli cultivars are duplicated across "Tomato plant" and "Tomato seed". Fix: promote the camellia cultivars to archetypes, and keep cultivars once with a plant/seed/tuber form type or cross-link.
- **C3-8 Brand duplicate.** "Rosen Tantau" and "Tantau" are separate entries; merge them.

### What it would look like (Garden plants: Hellebore, new)
```
Hellebore (Helleborus)
  H. × hybridus (Lenten rose)
    v: Ashwood Garden Hybrids (Ashwood Nurseries; to verify) · Harvington
  H. niger (Christmas rose) → 'Potter's Wheel'
  Helleborus Gold Collection (HGC; to verify) — 'Ice N' Roses'
  dt: single, double, anemone · picotee, spotted · colour
```

Priority: medium
Fix size: medium

---

## C5 Writing & desk (96 kinds, 240 archetypes)

**Brand mode:** variety for fountain pens, inks, cult pens, notebooks and collector machines; tier for desk and filing supplies.

### Gaps for hobbyists
- **C5-1 Parker 45 and Parker 75 are not archetypes.** They sit only in `m` under the cartridge-converter kind. Chinese pens (Hero 616, Jinhao, Wing Sung) have 0 hits; they are a large enthusiast segment (to verify). Fix: promote both Parkers to archetypes and add a Chinese-makers set.
- **C5-2 Desk collectables are missing.** Inkwell and inkstand, letter opener, desk set and pencil extender have 0 hits anywhere. Fix: add a "Desk accessories & collectables" shelf with inkwells (antique period view) and desk sets.
- **C5-3 "Calligraphy desk accessories" is lumped.** It is one kind with 8 types (suiteki water dropper, bunchin, fudeoki…) and 0 archetypes, although suiteki are collected. Fix: split out Water dropper and Paperweight (bunchin) as kinds.

### Too much detail
- **C5-4 The cartridge-converter list is retail-skewed.** It has 31 `m` models, many obscure SKUs (Meister by Point Slim Liner, Kolo Tino, Nakabayashi Artnavi, E+M Contract, IWI Handscript). This is a retail-harvest skew. Fix: keep about 10 and drop shop SKUs.
- **C5-5 Cartridge and lead types are brand or SKU lists.** Fountain pen cartridge has 11 types that are really brand formats; Pencil leads has 11 size types. Desk & filing has 22 kinds and 15 of them hold only types. Fix: collapse cartridge types to international/proprietary/pigment. Merge Whiteboard, Noticeboard and Chalkboard into one "Wall board" kind. Merge Calendar with Day-by-day calendar, and Punched pocket into Folder.

### Confusing organisation
- **C5-6 Seals sit in the paper department.** The Seals & stamps shelf (hanko, seal paste, wax seals) is inside Notebooks, planners & paper. Fix: make it its own department, "Seals, stamps & sealing wax".
- **C5-7 Calligraphy is duplicated with C4.** Inkstones, sumi and seal paste are duplicated in C4 (grep: Inkstone, Duan inkstone and She inkstone are kinds in C4). Fix: keep one home and cross-link. Calligraphy as a pursuit should be a cross-link, not a department label; rename it "Brushes, ink sticks & inkstones".
- **C5-8 Inconsistent segment vocabulary.** The register mixes "Value" with "Value & basics", and "Luxury house" with "Bespoke & artisan". Fix: normalise to SEGMENTS.json.

### What it would look like (Fountain pens)
```
Cartridge-converter fountain pen
  Parker 45 (Parker, 1960) → Flighter, Classic; gold-nib versions
  Parker 75 (Parker, 1964) → Sterling Cisele, Thuya, Milleraies
  Lamy Safari (Lamy, 1980) → special editions by year
  Hero 616 (Hero; to verify) — Parker 51 homage
  dt: nib EF–B, steel/gold · finish · converter type
```

Priority: low
Fix size: small

---

## C7 Farm, smallholding & forestry (114 kinds, 63 archetypes)

**Brand mode:** tier for current machines; variety for vintage tractors and stationary engines.

### Gaps for hobbyists
- **C7-1 The lead promises beekeeping that is not here.** The lead says "apiaries … beehives are mapped to named archetypes", but C7 has no beekeeping kinds; Langstroth hives and honey extractors live in B10. Fix: correct the lead and cross-link B10.
- **C7-2 Vintage tractor icons are missing.** All 63 archetypes are in the vintage department. Minneapolis-Moline, Fordson Dexta, Massey-Harris Pony and Lamborghini tractors have 0 hits (to verify as collector icons). Allis-Chalmers has only the WC; Oliver appears only in passing. Fix: add the missing families and a "Vintage compact/garden tractor" kind (Cub Cadet, Wheel Horse, Kubota B-series; to verify).
- **C7-3 Smallholder kit is missing.** Livestock trailer, cream separator, butter churn and poultry plucker have 0 hits; sheep hand shears appear only in C2. Fix: add a "Smallholding" department (livestock trailer, hand shears, cream separator, hand grain mill), with vintage dairy as a period view.

### Too much detail
- **C7-4 The scope rule is broken.** 91 of 114 kinds carry models or ranges, including Forest harvester (6 m, 3 r), Feller buncher (5 m), Combine harvester, Sugar-beet harvester, Milking robot, centre-pivot irrigators and rice hullers. These are farm-business or contractor machines, and the rule says to keep such kinds at kind level with no models. Fix: drop the models from the Harvesting, Forest machines, Milking and Irrigation shelves, and merge the specialist harvesters (potato, beet, carrot, grape) into one "Root & speciality harvester" kind.
- **C7-5 Ground-work and earthmoving kinds are mostly empty.** Box blade, Rear grader blade, Post-hole auger, Trencher and Bund plasterer are separate kinds with almost no content. Loaders & earthmoving has 4 kinds, and 3 are fully empty. Fix: make one "Tractor ground-work implement" kind, and move earthmoving into C1 Site equipment as kinds with no models.

### Confusing organisation
- **C7-6 Departments follow a farm-production axis.** The 10 departments mirror the commercial farming calendar (tillage, seeding, harvest, hay, livestock, forestry), but the owner is a person. Fix: regroup into Compact tractors & implements · Vintage tractors & engines · Woodland & firewood · Smallholding livestock · Farm-scale machines (kind level).
- **C7-7 No tradition register.** There is no traditions/C7.json. The steam-rally and vintage-engine scenes could carry tags.

### What it would look like (Vintage tractors)
```
Vintage standard tractor
  Ferguson TE20 (Ferguson, 1946)
    v: TEA petrol · TED TVO · TEF diesel · TO-20 (US)
  Fordson Dexta (Fordson, 1957; to verify) → Super Dexta
  Massey-Harris Pony (to verify)
  dt: fuel · wheel/track · industrial or vineyard
```

Priority: high
Fix size: medium

---

## C8 Building materials & consumables (173 kinds, 105 archetypes)

**Brand mode:** tier for bulk materials, fixings, electrical and fuel; variety for heritage and reclaimed materials, wallpaper, door furniture and Li-ion cells. Paint should be mixed.

### Gaps for hobbyists
- **C8-1 Paint colours, the enthusiast axis, are absent.** Farrow & Ball, Little Greene, Benjamin Moore and Sherwin-Williams are in the register, but Wall and ceiling paint has 0 archetypes and 14 bare models. "Hague Blue" and "Elephant's Breath" have 0 hits. Fix: add named-colour archetypes per paint house (mk = house; version = finish or reformulation).
- **C8-2 Heritage ironmongery is thin.** Door handle has good design archetypes (Gropius, Wittgenstein, FSB), but Latch, Door knocker and Door hinge have none; "Suffolk latch" and "Norfolk latch" have 0 hits. Spray paint has no Montana archetypes even though Montana Cans and Montana Colors are in the register. Fix: add named archetypes for latches and knockers, and for graffiti cans.

### Too much detail
- **C8-3 Fixings and electrical are over-split.** Screws, nails & fixings has 22 kinds and 12 have no models; 7 screw kinds are separate (Wood, Decking, Drywall, Masonry, Coach, Self-tapping, Machine). Electrical supplies has 10 kinds, and 7 are fully empty (Flex, Junction box, Cable clip, Cable tie, Mains plug, Plug adaptor, Fuse). Fix: make one "Screw" kind with types; merge Bolt, Nut, Washer and Rivet; merge the 5 wall-plug kinds into "Wall fixing"; and make 3 electrical kinds (cable, accessories, leads).
- **C8-4 Leftover departments.** "Aggregates & landscaping stone" holds a single empty catch-all, "Other garden stone", and duplicates the real Aggregates, paving & landscaping stone department. "Flooring (fitted carpet & carpet tiles)" holds only "Needlepunched carpet" (5 m); the Timber note itself says flooring belongs in Home Fixtures. Fix: delete the first and move the second to G3 or B2.

### Confusing organisation
- **C8-5 Overlapping roofing and stone kinds.** Roof tile, Handmade clay roof tile and Reclaimed roof slate and tile overlap; "pantile" occurs 8 times across them. York stone appears 10 times across Natural stone paving and Reclaimed flagstone. Fix: one kind per material, with new/handmade/reclaimed as a type, and a "Reclaimed" view.
- **C8-6 Misplaced kinds.** Safety sign is under Ironmongery, Duct tape under Tiling & sealing, and Packer (shims) under Mouldings. Sandpaper duplicates C1 "Sanding sheet or disc". Charcoal and the binchōtan tradition duplicate C2 (see C2-7). Fix: move or merge each one.

### What it would look like (Paint)
```
Wall and ceiling paint
  Farrow & Ball named colours (Farrow & Ball)
    Hague Blue No. 30 · Elephant's Breath No. 229 · Railings No. 31 (to verify)
    v: Estate Emulsion · Modern Emulsion · Dead Flat
  Little Greene colours → Obsidian Green; Benjamin Moore → Hale Navy (to verify)
  dt: finish · sheen % · scrubbability class
```

Priority: medium
Fix size: medium
