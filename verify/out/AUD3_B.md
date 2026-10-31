# AUD3_B — cold audit: B1 B2 B3 B4 B5 B6 B7 B8 B10 G3

Counts are computed from rebuild/reader/<CODE>.json and the brands/traditions registers (2026-10-28). "m+r" = model plus range entries. Absence claims were checked with grep across all rebuild/reader/*.json.

---

## B1 Furniture & storage

**Brand mode:** mixed. Tier for everyday upholstery, mattresses, flat-pack storage, racks and nursery pieces. Variety for design classics, writing furniture and period or craft furniture.

107 kinds, 191 archetypes, 51 kinds carry archetypes. Brands: 73. Traditions: 17.

### Gaps for hobbyists
- **B1-1 Lumped "Lounge chair".** The most-collected furniture form sits in one kind: 21 archetypes and no types (Eames Lounge, Barcelona, LC2/LC3, Wassily, Egg, Swan, Womb, Paimio, Red and Blue, Ball, Tongue, Ribbon, Mushroom, Coconut, Diamond, Platner, Safari, Papa Bear, Shell, CH25, Ox). **Fix:** split it into three kinds by construction: upholstered/sculptural lounge chair, tubular and wire-frame chair, and moulded/bentwood/shell chair. Order archetypes by significance, and add licensed maker, vintage and replica versions where they are missing (Paimio, Tongue, Mushroom and Coconut have none).
- **B1-2 Missing icons.** None of these appear anywhere in the reader files: Pierre Jeanneret's Chandigarh chair, Prouvé's Standard chair, the Cherner chair and the BKF (Butterfly) chair. Eames LCW/DCW does not appear in B1 (the only hit is in C4). Eileen Gray appears only as the Brick Screen; there is no E1027 table. **Fix:** add these as archetypes with licensed-maker versions (Vitra, Cassina, Knoll, Cherner Chair Co., Classicon).
- **B1-3 Brand register is thin at the design end.** Fredericia, Molteni&C, Minotti, Cappellini, Moroso and &Tradition are absent everywhere (to verify which of them are Premium versus Designer). **Fix:** add them so the archetype `mk` fields can resolve.

### Too much detail
- **B1-4 IKEA retail skew.** IKEA accounts for 183 of 295 m+r entries (62%). The whole "Racks, boxes & organisers" department uses IKEA ranges only. The same range is often listed twice in one kind, as both m and r (Bed frame: MALM, BRIMNES, TONSTAD; Sideboard: BESTÅ, HAVSTA, HAUGA). **Fix:** keep at most two IKEA ranges per kind, remove the m/r duplicates, and add market-covering brands and test winners.
- **B1-5 Data error.** Dressing table lists 8 sit-stand desks as its models (UPLIFT V3, FlexiSpot EN1/Comhar, IDÅSEN…), copied from Sit-stand desk. **Fix:** clear them.
- **B1-6 Empty or attribute-only kinds.** Slipper chair, Locker, Umbrella stand and Magazine rack have no types, archetypes or models. Club chair is an armchair shape, and Chair bed holds one SKU. Futon sofa lists marketplace SKUs (Twillery "Stratford Full-Size Futon Frame"). **Fix:** fold these into Armchair, Storage cabinet and Sofa bed as types.
- **B1-7 Duplicate brands.** "Gillows" and "Gillows of Lancaster and London" are both in the register. **Fix:** merge them.

### Confusing organisation
- **B1-8 Misplaced types.** Gaming chair includes "simulator cockpit seat" and "force-feedback chair" (sim-racing rigs belong with Video Games hardware, E5). Game table includes "poker table" and "convertible pool-dining table" (games and sports). High chair and booster seat sit under "Beds & mattresses → Nursery furniture", but they are not beds. **Fix:** cross-link the sim seats and tables to E5/E1/E2, and make "Nursery & children's furniture" its own department, or a shelf renamed to match.
- **B1-9 Mixed axes in Sofa types.** The 13 types mix arm style (Lawson, tuxedo, camelback), period (Art Deco, mid-century) and cover (leather, velvet). Period is a view under the rules. **Fix:** keep the form types and move period and cover into `dt`.

### What it would look like (Sofas & armchairs → lounge chairs)
```
Moulded, shell & bentwood lounge chair
  Paimio chair (Aalto, 1932) → Artek original · vintage
  Ball chair (Aarnio, 1963) → Asko · Eero Aarnio Originals
Tubular & wire-frame lounge chair
  Barcelona chair (Mies, 1929) → Knoll licensed · vintage Knoll · replica
  Wassily (Breuer, 1925) → Standard-Möbel · Gavina · Knoll
  Diamond (Bertoia, 1952) → Knoll; detail: full or seat pad cover
Upholstered lounge chair
  Eames Lounge (1956) → Herman Miller/Vitra · vintage rosewood · tall
```
**Priority:** high · **Fix size:** medium

---

## B2 Home textiles

**Brand mode:** mixed. Variety for hand-made rugs, quilts, heritage blankets and luxury linen houses. Tier for machine-made rugs, bedding basics, curtains, blinds and mats.

78 kinds, 165 archetypes. Brands: 59. Traditions: 37.

### Gaps for hobbyists
- **B2-1 Thin rug archetypes.** The rug department is strong in breadth (Persian rug has 25 archetypes, Anatolian 16), but most archetypes have no versions. Caucasian rug has 7 archetypes and 0 versions; Chinese rug has 4 and 1. Named sub-groups collectors argue about are missing as versions (Kazak → Fachralo, Karachov, Chelaberd "eagle"; Shirvan → Marasali; to verify). **Fix:** add versions from a rug reference (e.g. Hali or auction-house categories) and keep the antique, new and reproduction axis.
- **B2-2 Missing textile traditions.** Suzani appears nowhere in the reader files. Ikat appears only in apparel/textile categories (A1, E3, E4) and not as a home textile. There is no Scandinavian design-textile line (Marimekko is a register brand with no kind; Svenskt Tenn/Josef Frank is absent). There is no toile de Jouy (it appears only in C8). **Fix:** add a "Printed & embroidered furnishing textile" kind (suzani, ikat, toile, Josef Frank prints) and link it to traditions.
- **B2-3 Brand names used as archetypes.** "Designer rug" archetypes are brand names (Kasthall rugs, The Rug Company rugs, nanimarquina rugs), not patterns. **Fix:** use named designs as archetypes (e.g. Märta Måås-Fjetterström "Bruna heden"; to verify) and keep the houses in the register.

### Too much detail
- **B2-4 Near-duplicate and empty kinds.** Featherbed, Mattress pad, Headboard cover, Sheer curtain, Panel blind, Tie-up shade, Scatter cushion and Cushion cover all have no types and no models. Comforter (US) duplicates Duvet (UK). Pillowcase, Duvet cover and Valance are pieces of the bed-linen set. **Fix:** merge Comforter into Duvet, fold the toppers and pads into Mattress topper as types, and make the curtain and blind leftovers types of their neighbours.
- **B2-5 Meditation gear.** Meditation cushion and Meditation mat are separate kinds holding Monastery Store SKUs, and "zabuton" is also a type of Floor cushion. **Fix:** make them one Floor cushion type, cross-linked to the Spiritual pursuits taxonomy.

### Confusing organisation
- **B2-6 Leftover brief note.** The "Table & kitchen linen" department note reads "Trim the IKEA-only lists; add linen houses and table-linen traditions", but all 5 kinds still carry a single IKEA model. **Fix:** do the trim, then replace the note.
- **B2-7 Kotatsu futon and Heated low table are split.** Kotatsu futon is in B2 and Heated low table is in B1, so the two halves of one object live in different categories. **Fix:** cross-link them, or keep the futon as a type of the B1 kind.

### What it would look like (Rugs → Caucasian)
```
Caucasian rug
  Kazak (village, SW Caucasus) → Fachralo · Karachov · Chelaberd (eagle) · Lori-Pambak
  Shirvan → Marasali prayer rug · Akstafa
  Kuba → Perepedil · Zeykhur · Konaghend
  Karabagh → Chondzoresk (cloudband) · Kasim Ushag
  Detail: age (pre-1900, 1900–1930, new) · dyes · condition
```
**Priority:** medium · **Fix size:** medium

---

## B3 Lighting

**Brand mode:** mixed. Variety for design lamps, chandeliers and torches/lanterns, which is an enthusiast hobby. Tier for fitted ceiling lights, outdoor lights, bulbs and parts.

61 kinds, 150 archetypes. Brands: 72. Traditions: 7.

### Gaps for hobbyists
- **B3-1 Flat SKU lists in the torch hobby.** The torch department holds 205 model entries next to 63 archetypes: EDC flashlight m=40, Keychain light m=36 (mostly Nitecore variants: TIKI, Tiki GITD, TINI 2, Tini 3, TIP SE, TUP, TUP2…), Thrower m=28 (mostly Sofirn), Headlamp m=26, Tactical m=23. Olight (37), Fenix (28) and Streamlight (25) dominate the whole file. **Fix:** convert families into archetypes with versions (Nitecore TIKI/TINI, Sofirn SP/IF/SC, Fenix TK/PD, Ledlenser P-series, Streamlight Stylus, Petzl Tikka), and drop the leftover SKUs.
- **B3-2 Missing collectable lamp forms.** There are no miner's lamps: no Davy/safety lamp and no carbide lamp (carbide appears only in unrelated categories). There are no vintage holiday string lights (String light is empty). Design icons are missing: Santa & Cole Cesta, Gubi Gräshoppa, Prouvé Potence (only a wall-light archetype exists), and Flos Snoopy and Glo-Ball sit in `m` rather than as archetypes. **Fix:** add a "Safety & miner's lamp" kind, and promote the Flos and Artemide `m` icons to archetypes.

### Too much detail
- **B3-3 Trade-level bulbs and fittings.** Compact fluorescent bulb lists 11 pin-base trade SKUs (PL-C, PL-S, Dulux D/S/L/T). Panel light (troffer) and Tube light are office fittings. Party & DJ light lists stage gear (PAR can, moving head). **Fix:** reduce CFL to a type of Tube light and Panel light to a type of Flush ceiling light, and move stage lighting next to B4 fog machines as one "Party effects" shelf.
- **B3-4 Long tier lists.** Flush ceiling light, Ceiling spotlight and Path light each list 12 models. **Fix:** cut to about 6 market-covering ranges.

### Confusing organisation
- **B3-5 Built-in lighting sits in a movables category.** Recessed downlight, Track lighting, Under-cabinet light and Step & plinth light are fixed to the building, and G3 has no lighting at all. **Fix:** ask the owner whether fixed lighting goes to G3 "Home systems → Lighting"; the "decorative lighting merges into Lighting" rule does not settle it (OWNER QUEUE).
- **B3-6 Split and duplicate placements.** Paper lanterns appear in two places: the "Paper lantern shade" and "Akari pendant" archetypes under Pendant, and the Paper lantern kind (chōchin) under Torches & lanterns. Mirror ball is a Pendant archetype, a B3 Party light type and a B4 kind. Work light and Dive light are tools or sport kit placed among torches. **Fix:** give Akari/chōchin one home with cross-links, and cross-link Dive light to Sports (water) and Work light to Tools.

### What it would look like (Torches → Keychain light)
```
Keychain light
  Maglite Solitaire (1984) → 1×AAA incandescent · LED
  Nitecore TIKI (2021) → TIKI · TIKI LE · TIKI GITD
  Nitecore TINI → TINI · TINI 2 · TINI 3
  Olight i3E EOS → brass · copper · Ti
  Detail: cell (button, AAA, 10440, built-in) · body metal · lumens
```
**Priority:** medium · **Fix size:** medium

---

## B4 Home decor

**Brand mode:** mixed. Variety for art glass, folk collectables, Christmas collectables, incense and fragrance houses. Tier for candles, frames, artificial plants, flags and fireworks.

100 kinds, 162 archetypes. Brands: 95. Traditions: 24.

### Gaps for hobbyists
- **B4-1 Seasonal decor is Christmas-only.** "Seasonal, festive & folk decor" has a 10-kind Christmas shelf and nothing for Halloween (the only B4 hit is the Department 56 "Snow Village Halloween" version), Easter, Diwali, Lunar New Year or Day of the Dead. Some religious-festival objects exist in F4 (menorah, fanous). **Fix:** add shelves for Halloween (vintage Beistle die-cuts and blow moulds are a collecting field; to verify), Easter (pysanky, Easter trees) and Lunar New Year, with cross-links to F4.
- **B4-2 Mid-century decorative glass and pottery are absent.** Fenton, Blenko, Whitefriars, carnival glass, Depression glass, West German "Fat Lava" pottery, Bitossi and Holmegaard (outside E4) appear nowhere. **Fix:** add archetypes under Vase and Decorative bowl, linked to the F2 art-glass kinds. Choose one home for overlaps: Venini Fazzoletto is an archetype in both B4 and F2.

### Too much detail
- **B4-3 Fireworks as a SKU list.** Firework cake lists 19 consumer SKUs, 14 of them from Brothers Pyrotechnics (one retailer's catalogue). Fireworks get 11 kinds, and Aerial shell's 13 "archetypes" (Peony, Willow, Palm…) are effects that repeat Firework cake's types. **Fix:** collapse to about 5 kinds (cake/barrage, rocket, shell, ground effects, handheld), keep the effects as `t`, and keep brands only in the register.
- **B4-4 Empty or near-duplicate kinds.** Votive candle, Floating candle, Potpourri, Scented sachet, Pennant, Feather banner (commercial signage) and Decorative windsock have no types or models. Pillar, Taper and Tealight each hold a single IKEA SKU. **Fix:** fold these into Candle as types and Flag as types, and drop Feather banner (trade).

### Confusing organisation
- **B4-5 Fireworks and fog machines are not decor.** A reader looking for fireworks or a fog machine would not look under "Seasonal, festive & folk decor". **Fix:** make one department, "Party & celebration effects", holding fireworks, fog/haze machines, mirror ball and B3's party lights.
- **B4-6 Cross-category duplicates.** Bird bath is a kind in both B4 (Garden ornaments) and B10 (Wild bird food, baths & nest boxes). The Lauscha glass tradition is registered twice. Nambu tekki is in both the B4 and B5 registers. Kōdō utensil set describes an incense practice. **Fix:** keep one Bird bath (B4) and cross-link it, merge the duplicate traditions, and keep Kōdō as objects cross-linked to the pursuit taxonomy.

### What it would look like (Seasonal → Halloween)
```
Halloween decoration
  Beistle die-cut (1920s–) → embossed German · US Beistle · reproduction
  Jack-o'-lantern candy container → German papier-mâché · US pulp
  Blow-mould figure → Empire · Union Products · Don Featherstone era
  Detail: material · era · condition · maker marks
```
**Priority:** medium · **Fix size:** medium

---

## B5 Kitchen & dining

**Brand mode:** mixed. Variety for coffee, tea ware, Japanese knives, tableware patterns, glassware, bar tools and brewing. Tier for utensils, small and large appliances, and food storage.

216 kinds, 485 archetypes; 155 kinds carry archetypes. Brands: 332. Traditions: 50.

### Gaps for hobbyists
- **B5-1 Tableware patterns are lumped and scattered.** Twenty-five patterns sit under one kind, "Dinner service" (Blue Fluted, Willow, Flora Danica, Fiesta, Cornishware, Kilta/Teema…). Old Country Roses appears twice, under both Cup and saucer and Teapot, and Polka Dot sits under Mug. This breaks the department's own "house → pattern → piece" note. Collected lines are missing: Hornsea, Midwinter, Susie Cooper, vintage Pyrex patterns and Fire-King Jadeite (the only "Jadeite" hit is the F6 mineral). **Fix:** create a "China pattern" kind with house → pattern → piece (pieces as `t`), and add the missing lines (to verify the pattern names).
- **B5-2 Missing hobby objects.** There is no home coffee roaster (green coffee is in J6, but no roaster object exists) and no tortilla press. **Fix:** add a "Home coffee roaster" kind (Behmor, Gene Café, Kaffelogic; to verify).

### Too much detail
- **B5-3 SKU lists for everyday utensils.** Spatula lists 9 SKUs, Cooking spoon 8, Ladle 7, Whisk 7 and Rolling pin 7 (OXO 28 overall). Dishwasher, Wine fridge and Freestanding cooker list appliance model numbers (SHE53C85N, FGWC5233TS…). **Fix:** use ranges for utensils, and cut appliances to market-covering ranges plus test winners.
- **B5-4 Repeated attributes and ranges.** All 9 Japanese knife kinds repeat the same steel/construction string as types. Wüsthof Classic, Classic Ikon and Victorinox Fibrox are repeated as `r` across 6 Western knife kinds (a "brand ranges repeated across kinds" finding). **Fix:** move steel and construction into a department `b` criterion or `dt`, and hold knife lines once in the register.
- **B5-5 Duplicates.** The traditions register has 8 duplicate pairs: Arita, Banko, Nambu ironware/Nambu tekki, Sheffield, Solingen, Thiers, Tsubame-Sanjo and Villedieu. Brands Griswold and Griswold Manufacturing are both listed. "Coffee and spice grinder (blade)" duplicates the "blade grinder" type of Electric coffee grinder. Weck jar is an archetype of both Kitchen canister and Preserving jar. "Teapot and coffee pot (tableware)" duplicates Teapot. **Fix:** merge each pair.

### Confusing organisation
- **B5-6 Broken department name.** A brief instruction became a department: "Kitchen & Dining — water & drinks appliances (countertop distiller beside jug filters)", holding one empty kind, Water distiller. **Fix:** move Water distiller into "Kettles, water & soda" and delete the department.
- **B5-7 Cross-category duplicates with G3.** AGA, La Cornue, Lacanche and Falcon are archetypes in both B5 Freestanding cooker and G3 Range cooker / Heat-storage range cooker. EuroCave appears in both B5 Wine fridge and G3. **Fix:** freestanding range cookers stay in B5 (they are movable), G3 keeps only fitted units, and the two cross-link.

### What it would look like (Tableware → patterns)
```
China pattern (house → pattern → piece)
  Royal Copenhagen Blue Fluted (1775) → Plain · Half Lace · Full Lace · Mega
  Meissen Blue Onion (1739) → crossed-swords marks by era
  Arabia Paratiisi (Esteri Tomula, 1969) → black · coloured
  Hornsea Saffron / Midwinter Stonehenge (to verify)
  Pieces (t): dinner plate · cup and saucer · teapot · tureen
```
**Priority:** high · **Fix size:** large

---

## B6 Cleaning & laundry

**Brand mode:** tier throughout. The only enthusiast corner is vintage vacuums (the Kirby/Electrolux collector niche; to verify).

83 kinds, 1 archetype (Corby trouser press). Brands: 85. No traditions file.

### Gaps for hobbyists
- **B6-1 Appliance icons are listed as models, not archetypes.** The first Roomba (2002), Dyson DC01, Hoover Model O, the Black+Decker Dustbuster, Numatic Henry and the Electrolux Trilobite all sit in `m`, so the file has no archetypes for the icons it already names. Kirby, Vorwerk Kobold and Rainbow/Rexair (to verify) are absent as vacuums. **Fix:** promote about 8 icons to archetypes with generations (Henry HVR160/200; Dyson DC01 → DC07 → V-series), as a small "Design & collectable" layer.

### Too much detail
- **B6-2 Model-number lists for a quality-of-life category.** There are 359 models across 83 kinds, and 15 kinds have 10 or more. Examples: washer model codes (WT7900HBA, WGB256A1GB, WKEX200HBA); 10 Finish and Cascade dishwasher-detergent SKUs plus 6 ranges; Multi-purpose cleaner listing 7 models and the same 7 brands again as ranges. **Fix:** keep brand ranges plus independent test winners at no more than 6 per kind, and drop m/r duplication.
- **B6-3 Attribute-only kinds.** Dishwasher rinse aid (2 SKUs), Dishwasher salt (1 SKU), Spin mop system (overlaps Wet mop), Dust mop, Waste-paper basket and Hard-floor scrubber-polisher (trade; empty). **Fix:** fold them into Dishwasher detergent, Wet mop and Kitchen bin as types, and drop the trade polisher.

### Confusing organisation
- **B6-4 Not a spare part.** "Laundry pedestal and stacking kit" sits under Spare parts & consumables but is an accessory. Washers list "integrated (built-in)" as a type, and Trash compactor is usually under-counter, while the rule sends built-ins to G3. **Fix:** move the pedestal kit to Washing machines as a type, and cross-link the built-in variants to G3.
- **B6-5 Missing everyday kinds a reader would expect.** There are no vacuum storage bags (absent everywhere) and no shoe-care kit in this category (only A2). The clothing-care cabinet (LG Styler) appears only in G1/H1/I1. **Fix:** cross-link these from Ironing & drying rather than adding depth.

### What it would look like (Vacuums → Cylinder vacuum)
```
Cylinder vacuum cleaner (tier)
  Henry (Numatic, 1981) → HVR160 · HVR200 · Hetty/James variants
  Miele C-series → Classic C1 · Complete C3 · Boost CX1 (bagless)
  SEBO Airbelt → K · D series
  Detail: bagged/bagless · powered head · cord length
```
**Priority:** medium · **Fix size:** small

---

## B7 Portable climate & air

**Brand mode:** tier. A small vintage-fan collector scene exists (Emerson, GE and Westinghouse brass-blade fans; to verify) but is not represented.

26 kinds, 0 archetypes. Brands: 70. No traditions file.

### Gaps for hobbyists
- **B7-1 No design or collectable layer.** The category has no archetypes at all, though it lists icons as plain models: Dyson AM06/AM07 (the Air Multiplier line), Balmuda GreenFan, Vornado and the Toyotomi Rainbow kerosene heater. Antique and vintage fans (Emerson, Westinghouse, GE, Vornado 1940s), the Braun HL 1 fan (the only "HL 1" hit is in C1) and Aladdin Blue Flame heaters (to verify) are absent. **Fix:** add a short "Design & vintage fans and heaters" shelf with about 8 archetypes.

### Too much detail
- **B7-2 Duplicate air-quality monitor kinds.** "Indoor air quality monitor" (5 models) in Air quality & humidity and "Air-quality monitor" (26 models) in its own one-kind department, "Air quality monitoring", overlap; View Plus and Aranet4 are in both. The 26-model list includes Temtop ×3, PurpleAir ×3, Qingping ×3, Airthings ×5 and Kestrel DROP pocket weather meters. **Fix:** merge into one kind with about 8 models and remove the extra department.
- **B7-3 Model codes.** Seven kinds list 10 or more models, with trade codes (MAW12V1QWT, LW8024IVSM, RHPANH2006…). Replacement air filter lists filter variants. **Fix:** cut to ranges plus test winners, and make filters one spare-parts entry per appliance.

### Confusing organisation
- **B7-4 Electric fireplace placement.** Electric fireplace (freestanding) is in B7, while G3 holds "Flueless fire" with "electric – mist flame effect" and Optiflame as an archetype (Dimplex Opti-myst/Optiflame appears in both). **Fix:** freestanding electric stoves stay in B7, inset and wall units go to G3, and the two cross-link.
- **B7-5 The fan split is fine, but Handheld fan includes "neck air conditioner".** **Fix:** keep it as a type; no action beyond trimming SKUs.

### What it would look like (Cooling & fans → design & vintage)
```
Electric fan (design & vintage)
  Emerson Trojan / Northwind (US, 1900s–1930s) → brass blade · steel blade
  Vornado (1945) → original · 630 circulator reissue
  Braun HL 1 (Rams, 1961) → HL 70 successor
  Dyson Air Multiplier (2009) → AM01 · AM06 · AM07
  Balmuda GreenFan (2010) → GreenFan · GreenFan C2
```
**Priority:** low · **Fix size:** small

---

## B8 Home safety & security

**Brand mode:** tier, with variety at the locksport and high-security end.

73 kinds, 15 archetypes, all of them on High-security lock cylinder and Lock pick set. Brands: 97. No traditions file.

### Gaps for hobbyists
- **B8-1 Locksport is thin on padlocks and antique locks.** High-security cylinders are well done (12 archetypes, including Abloy Protec2, Medeco M3, EVVA MCS and BiLock), but the padlocks that locksport ranks have no archetypes: ABUS Granit 37 sits in `m`, and the Master Lock No. 3, American Lock 1100 and Abloy PL362 are absent (to verify). Antique and collector locks (Bramah, Chubb detector lock, puzzle and trick padlocks) appear nowhere in B8. **Fix:** add a "Padlock (locksport & collector)" archetype set and an "Antique lock & key" kind with a period view.

### Too much detail
- **B8-2 UK and US trade codes.** There are 322 models, and 11 kinds have 10 or more. Examples: Union 3G114E/3K74E/2134E, fire-blanket sizes as SKUs (Kidde KFB1010/1212/1218), and dummy cameras from marketplace sellers (Wali, BNT). **Fix:** keep ranges and test winners only (≤6), and cut dummy camera to a type of Security camera.
- **B8-3 Empty or split kinds.** Cabinet lock, Security chain, Cable lock and Key cabinet have no models. Locking bar, Garage door defender and Ground anchor overlap. **Fix:** merge them into "Shed & garage security" with types.
- **B8-4 Duplicate brands.** Yale/Yale Home, Honeywell/Honeywell Home and Philips/Philips Hue are separate register entries, and Padlock `m` uses "Abus" where the register has "ABUS". **Fix:** merge them and normalise the names.

### Confusing organisation
- **B8-5 Fitted door hardware sits with movables.** Night latch, Mortice lock, Deadbolt, Lock cylinder, Keyed lockset, Patio door lock and Window lock are fitted to the door, as is G3's Multipoint lock, and the B8 lead says built-in security lives in G3. Intruder alarm system and Door phone in G3 duplicate B8's wireless alarm kit and video doorbell (SimpliSafe and Ring are archetypes in G3 and models in B8). **Fix:** a clear rule is needed: either all door and window locks go to G3 "Doors, windows & locks" with B8 keeping padlocks, portable and smart add-ons, or the reverse. Raise this in the OWNER QUEUE.
- **B8-6 Wrong shelf names.** Baby monitor sits under "Gates, latches & guards", and Pest control is a department of a "safety" category. **Fix:** add a "Monitors" shelf, and rename the department "Pest & insect control" so readers find it.

### What it would look like (Locks → Locksport & high security)
```
High-security cylinder  (as now, 12 archetypes)
Padlock (locksport & collector)
  ABUS Granit 37 → 37/55 · 37RK/80
  Master Lock No. 3 (laminated, 1921) → No. 1 · No. 5
  Abloy PL362 → PL350 · PL358
Antique lock & key
  Bramah lock (1784) · Chubb detector lock (1818) → period view
```
**Priority:** medium · **Fix size:** medium

---

## B10 Pet & animal supplies

**Brand mode:** mixed. Tier for food, litter, bedding and stable supplies. Variety for aquascaping and reef, saddlery and bits, falconry, pigeon racing, beekeeping hives and vivaria.

241 kinds, 271 archetypes; 86 kinds carry archetypes. Brands: 181. Traditions: 6. m+r: 1,481 (Zoo Med 47, Exo Terra 26, Shires 25).

### Gaps for hobbyists
- **B10-1 Aquarium gaps.** There is no aquarium controller (Neptune Apex and GHL Profilux; the only "Apex" hit is a nest-box name), no gravel cleaner/siphon, no algae magnet and no fish net. Pond and koi equipment is solid, but koi varieties have no browse link. **Fix:** add these kinds, and cross-link koi to the species register.
- **B10-2 Horse yard objects are missing.** There is no tack trunk, saddle or bridle rack, mounting block, or home-arena show jumps/cavaletti. Horsebox/trailer appears only in G1. **Fix:** add a "Yard & tack room" shelf.
- **B10-3 Thin traditions.** There are 6 traditions for a category with Western, English and Australian saddlery, falconry and skep-making. Western saddle-making centres (e.g. Sheridan-style tooling; to verify) and Japanese koi breeding (Niigata) are missing. **Fix:** add about 6 traditions.

### Too much detail
- **B10-4 Pet food as many kinds with long lists.** Dogs have 8 food and treat kinds (Dry, Wet, Fresh/raw, Freeze-dried, Veterinary, Treats, Dental chews with 0 types and 9 SKUs, Long-lasting chews), each with 6–16 SKUs. Horses list 19 compound feeds, 16 girths and 14 saddle pads. Horses total 319 m+r and Aquariums 219. **Fix:** make one Dog food kind and one Dog treats & chews kind with forms as types and ≤8 market and test picks, and cut stable-supply SKUs to ranges.
- **B10-5 Inconsistent toy axis.** Dogs have 5 toy kinds (two of them, Plush and Rope, have 0 types), while Cats have one "Cat toy" kind with types. Reptiles have Deep heat projector and Ceramic heat emitter as type-less one-archetype kinds. **Fix:** use "Dog toy" with types, and "Reptile heat lamp" with types.
- **B10-6 Duplicate brands.** "ADA" and "Aqua Design Amano" are both in the register, and archetype `mk` uses both. **Fix:** merge them.

### Confusing organisation
- **B10-7 Bird bath duplicates B4.** **Fix:** keep it in B4 Garden ornaments and cross-link from Wild birds.
- **B10-8 Pursuit shelves.** Falconry, Pigeon racing, Dog agility and Gundog training qualify under the rule as distinct equipment shopped that way. Agility's 8 obstacle "archetypes" (A-frame, weave poles…) are generic course elements, not named patterns. **Fix:** make them types of "Agility equipment" and cross-link to the Physical pursuits taxonomy.

### What it would look like (Aquariums → controllers & maintenance)
```
Aquarium controller
  Neptune Apex (2008) → Apex Classic · Apex EL · Apex 2016 · A3
  GHL ProfiLux → 3 · 4 · 5
  Detail: probes (pH, ORP, temp) · outlets · dosing modules
Aquarium maintenance tool (t: gravel siphon · algae magnet · scraper · net)
```
**Priority:** medium · **Fix size:** medium

---

## G3 Home fixtures & features

**Brand mode:** mixed. Variety for luxury kitchens, bathroom fittings, sauna, design switches, radiators and stoves. Tier for plant (boilers, heat pumps, water heaters, solar) and structural items.

155 kinds, 192 archetypes. Brands: 128. Traditions: 8.

### Confusing organisation (the main problem)
- **G3-1 Thirteen broken leftover departments.** Rebuild instructions became department names, for example "Home systems — water treatment (dissolve this catch-all into k58/k59/k60)", "Bath & wellness — toilets & bidets (cut TOTO WASHLET SKU list)", "Home systems — solar & energy (collapse all inverter kinds into one Inverter kind with types)" and "… (type of Inverter)". Between them they hold 22 kinds that duplicate the main departments:
  - Flued stove/Flued fire repeat the Stovax and Valor models.
  - Wall-mounted split air conditioner repeats Split air conditioner.
  - Bidet seat lists 23 SKUs against Shower toilet and bidet seat.
  - Charge controller and the four inverter kinds repeat Solar system parts and Inverter.
  - Door phone, Underfloor heating kit and Solar thermal collector repeat existing kinds.
  - Other plumbed water filters is a catch-all.

  **Fix:** apply the instructions those names describe, delete all 13 departments, and check that no kind remains outside the six zones.
- **G3-2 Empty duplicates inside the main departments.** The empty duplicates are Tap (beside Bath and basin tap), Wall switch (beside Wall switch and dimmer), Garden kitchen (beside Outdoor kitchen), Kitchen cabinet (beside Fitted kitchen), Door frame (also a Door type), and Shower enclosure plus Bath or shower screen (beside Shower enclosure or screen). Oven duplicates Built-in oven (same Bosch Series 8 range), and Bath panel duplicates a Bathtub item. **Fix:** delete or merge each one.
- **G3-3 Cross-category duplicates.** Range cookers and AGA duplicate B5 (see B5-7). Intruder alarm system and Door phone duplicate B8 (see B8-5). Built-in wine cabinet overlaps B5 (EuroCave). **Fix:** apply the movable-versus-fitted rule and cross-link.

### Too much detail
- **G3-4 Attribute and SKU overload.** Wall socket has 21 types, one per world plug standard (A–N), which is reference data rather than a choice. Hard-shell hot tub lists 8 Hot Spring models and 11 ranges. Dunster House has 19 entries across 10 garden-building kinds. Built-in coffee machine and Warming drawer each list 4 Miele codes. **Fix:** reduce plug types to "UK / EU Schuko / US / other" with a link to a reference, cut hot tubs and garden buildings to ranges, and remove the retail skew.

### Gaps for hobbyists
- **G3-5 Fitted features enthusiasts plan.** There are no fitted wardrobes or dressing room, no home cinema room as a built feature (only the TV lift), and no built-in wine cellar (wine cellar appears only in J7). Staircase has 13 types but 0 archetypes (no spiral-stair or cantilever icons). Decorative tiles (zellige, encaustic, Delft, Minton) live only in C8. Architectural door furniture (the FSB 1020 handle, door knockers) is also only in C8. **Fix:** add the three built-in kinds, and cross-link the tile and ironmongery traditions from C8 into G3 zones.

### What it would look like (Home systems → Solar & energy, after cleanup)
```
Inverter (t: string · hybrid · microinverter · off-grid inverter-charger)
  Fronius Primo GEN24 · SolarEdge Home Hub · Enphase IQ8 (to verify) · Victron MultiPlus-II
Solar system parts (t: MPPT/PWM controller · battery-bank charger · enclosure · mounts)
Home battery (t: AC-coupled · DC-coupled · balcony)
Solar panel · Solar water heater (absorbs Solar thermal collector)
Plug-in balcony solar kit · Off-grid solar kit · Small wind turbine
```
**Priority:** high · **Fix size:** medium
