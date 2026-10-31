# AUDIT I2 Digital Media & Items (cold audit + retry round)

Accuracy: 25 checked (random.seed(7)), 0 wrong (all names shown raw; all 'says' true). Layer over-tag: 21/25 'premium' rest on directory rows only (Atlas of Type, Type Design Class) and must be 'listed'.

Additions: 139 brands (55 fonts, 27 sample/instrument makers, 26 sewing-pattern makers, 22 e-book/game stores, 4 3D marketplaces, 3 stock, 2 NFT); 3 regions (Japan extended, Thailand, Nigeria); 31 upgrades of harvest rows to juried-award evidence; 4 fetched cross-tags plus 16 register-only cross-tag candidates; 6 drops (5 Wikipedia subcategory/list rows, 1 duplicate).

Main finding: HOMONYM MASKING. The harvest dedupe stripped suffixes (type, foundry, studio, design, co) and matched 29 foundries to unrelated register brands (Storm Type Foundry -> Storm bowling balls, Indian Type Foundry -> Indian motorcycles, Black Foundry -> Black energy drink, Signal, Sharp Type, Nova, Atlas, Neubau ...), so they were silently skipped. They are re-added with homonym_masked:true; qualifiers given where the bare names collide (Atlas (type foundry), Neubau (type foundry), Iwata (fonts), Tlab (fonts), JAMO (type)).

Blind spots: see "blind_spots" in AUDIT_I2.json.
