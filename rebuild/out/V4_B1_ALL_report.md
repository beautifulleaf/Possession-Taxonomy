# V4_B1_ALL report (B1 Furniture & Storage, all ten departments)

Part file: rebuild/out/B1_parts/ALL.json (196 KB; replaces all ten departments). Validates OK (119 kinds, 263 entries). About 42 fetches.

**Entries before → after (archetypes):** 191 → 263. Biggest: Dining chair 20 → 65, Upholstered lounge chair 9 → 16, Moulded/shell lounge 9 → 16, Tubular lounge 7 → 10, Office chair 11 → 14, Dining table 4 → 8, Mattress 0 → 12 (brands), Bookcase 3 → 4.

**References:** Wikipedia List of chairs (first 100,000 of 124,675 characters; rest is references), 38 Wikidata chairs with a designer, Compasso d'Oro page (five furniture winners: 683, Vertebra, Nomos, Sacco, Nahalie), maker pages (Knoll, Cassina, Fritz Hansen, Carl Hansen, Artek, Herman Miller, Kartell, Muuto). Each kind's `sel` ends "Covers n of about m" (m is approximate for chairs, unknown for other kinds).

**Market facts (ms):** IKEA €45.1 bn goods sold FY2024; Ashley US$10.3 bn 2022; Williams-Sonoma US$7.81 bn 2025; MillerKnoll US$3.84 bn FY2026 (Sofas & armchairs). Mattress industry US$28.5 bn 2018; Somnigroup US$4.930 bn 2021; Sleep Number US$1.856 bn 2021; Casper US$439 m 2019 (Beds & mattresses). Owners with years: Muuto/MillerKnoll 2018, Knoll/MillerKnoll 2021, Artek/Vitra 2013, Cassina/Poltrona Frau 2005, Sealy/Tempur 2012, Casper/Carpenter 2024, Sleep Number assets 2026. `own`/`tier`/`cty` set on entries by maker; 10 new brands in the register; brand_updates for registered makers.

**Loose models (m/r):** all removed. IKEA SKU ranges (about 70, e.g. MALM, HEMNES, BESTÅ, SAMLA) dropped as SKU-level; Billy, Poäng, Kallax, IVAR, Lack and Klippan stay as entries. Baby-gear models (about 60, Maxi-Cosi, DaVinci, TotCraft etc.), sit-stand desk, lap-desk and TV-stand models, Airbed and futon models dropped as retail SKUs. Mattress models became versions of brand entries (Simba Hybrid, TEMPUR-Adapt, Posturepedic, Leesa Reserve, Nectar Ultra Hybrid); Origin, Dormeo, Jay-Be, SleepSoul, GhostBed dropped (no fetched page). Historic regional pieces (refectory tables, byōbu, commodes) dropped as styles; Racks, boxes and Spare parts kept as commodity kinds with no entries. No moves, no renames.

**Not done / not sourced:** Emma (Wikipedia 404, no entry); Wikidata non-chair furniture query timed out; Vitra Design Museum, MoMA, V&A, Design Museum collection lists, Wikipedia furniture-design lists and makers' own collections (Vitra, Hay, &Tradition, Thonet, Muuto) were not fetched, so tables, sofas, beds and storage hold only designs named on fetched pages. Chair types and historic styles in the list (Windsor variants, Chippendale, Shaker) are see-note, not entries. No tier given for Serta and Simmons (ownership not stated). Wikipedia IKEA product list 404; IKEA lines beyond those above unsourced. Fetch budget was the limit, not size.

## Round 2 (continuation)
About 52 further fetches. Part file now 398 entries (was 263), 259 KB, validates OK.

**Design-museum canon:** MoMA's and Vitra's sites gave no furniture list (WebFetch 403; Firecrawl returned only the collection landing page and a 404). V&A search gave five chairs. The usable route was Wikidata (P195 collection MoMA, V&A, Vitra Design Museum, Design Museum): 58 rows, of which about 30 furniture pieces are entries (Pratt Chair, Selene Chair, Great Bed of Ware, Golden Bed, King Rene's Honeymoon Cabinet, Mae West Lips Sofa and others); no rows for Vitra Design Museum or Design Museum. This is not the full holdings.

**Maker and designer pages:** Wikipedia pages of 22 designers (Wegner, Jacobsen, Juhl, Panton, Eames, Aalto, Perriand, Kjaerholm, Mogensen, Nelson, Castiglioni, Ponti, Sottsass, Saarinen, Gray and others) and of B&B Italia, Ligne Roset, Poltrona Frau, Flexform and Vitsoe added about 135 designs, now also in tables, sofas, storage, shelving and stools. Wikipedia pages for Hay, &Tradition, Gubi, USM Haller, String, De Sede and Togo were 404 or disambiguation; Thonet, Muuto and Vitra pages hold no collection list. These makers' collections are still missing. Windows past 100,000 characters of List of chairs, Alvar Aalto, Gio Ponti, Hans Wegner were read (no further designs); Isamu Noguchi, Mies and Le Corbusier pages were only read in the first window.

**IKEA:** Hunker's list (fetched) gave Ektorp, Malm, Docksta, Frosta, Raskog, Klippan, Lack, Kallax, Poang, Billy; no years except Billy and Poang. Hemnes and Stockholm: no fetched page, left out.

**Emma:** sourced from tech.eu (founded 2013, Frankfurt, Haniel 50.1% April 2020): entry and register brand added.

**Still short:** no complete museum holdings list; many tables, beds and storage kinds hold only a few designs because designer pages name mostly chairs; years missing for some entries.

## Round 3
About 45 further fetches (Firecrawl JSON extraction on the museum search pages). Part file: 704 entries (was 398), 327 KB, validates OK (119 kinds).

**MoMA (Design, classification 3):** chair query 3 of 3 pages read (about 120 results); table 6 pages with content (pages 7-8 empty; most results lamps, furniture kept); sofa, stool, bench, shelf 1 page each (13, 38, 10, 5 results); cabinet, desk, bed, screen page 1 only because later results are unrelated matches (the page counter showed 546, 2026, 108909 and 72). About 230 pieces held are entries, each citing its search URL.

**Vitra Design Museum:** chair search has 1,191 results, only page 1 (30, alphabetical) read; table 24, shelf 13, bed 11, cabinet 27 read in full; sofa and stool returned 0. About 60 entries.

**V&A API:** query "chair", year from 1900: 4,267 records; page 1 was photographs and 19th-century items, no design pieces, so nothing added. Not completed.

**Wikipedia windows:** Noguchi read to 200,000 characters, Mies to 200,000, Le Corbusier to 200,000 (last 24,875 characters unread); nothing new beyond the Weissenhof, Barcelona, Brno, Tugendhat and LC chairs.

**Makers:** HAY (About A Chair, Stool, Table, Lounge), USM (Haller Tables, Kitos Desks), de Sede (DS-600 Snake, 1972, with designers), &Tradition (14 furniture families with designers) and GUBI (Totto stool, Lotus table; its page gave only two) added from their own sites. String: only a search excerpt (1949, Kajsa and Nisse Strinning), already an entry. Muuto, Thonet: no product list found. Entries were de-duplicated by name and alias across the whole part.

**Still short:** Vitra Design Museum chair results 31 to 1,191; MoMA pages beyond page 1 for cabinet, desk, bed, screen; V&A design holdings; Le Corbusier page end.
