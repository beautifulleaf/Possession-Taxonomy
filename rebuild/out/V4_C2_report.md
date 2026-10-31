# V4_C2 report: Garden & Outdoor named-entry pass

**Method:** about 25 fetches (Wikipedia, Middleby, Traeger SEC prospectus, Report Prime, ServiceDealer). Wikidata was not used: it does not model these canons. Sources are in the pages cited on each entry and ms fact. Backups are in work/V4_C2/bak/.

**Loose models (m):** 422 removed from every kind, none kept. They were SKU-level model names with a maker (for example "Izy HRG 466 PK", "RMA 235"); no fetched page treats them as lines or variants of an entry, so none became an entry or a version.

**Named entries:** 208 before, 116 after (including 24 new brand and 35 new style entries).
- Commodity kinds outside the treated groups: 92 entries removed (billhook, scythe, machete, spade, secateur patterns, tool makers' lines, pots, watering cans, greenhouses, fire pits). Two kept under the icon rule: Original LÖWE anvil secateur and Grelinette (each stated as the first of its kind on the earlier fetched page). No design-collection or award landmark was checked, so none were added.
- Bonsai style (new kind, new shelf Trees & styles): 35 of 35 styles on Wikipedia's Bonsai styles page, grouped by its headings. Species point to C3.
- Lawn mowers: Rotary 3, Cylinder 4, Hover 1, Riding 1, Robotic 6 → 9 (added Robomow, Volta, Gardena robotic mower; Automower gains a CEORA 2022 version). Owner, tier, country added where a fetched page states them.
- Powered garden equipment brand (new): 24 brands grouped by owner (Husqvarna Group 9, Stihl 2, Toro 5, Deere 2, Honda, MTD, Briggs & Stratton, Stiga, Makita, Worx).
- Outdoor cooking: Kettle 1, Kamado 5, Bullet 1, Offset 4, Gas 5, Pellet 5, Griddle 1, Portable 5 (was 6), Pizza oven 9 → 10 (Ooni Fyra added). Open-fire grill entries (parrilla, braai, Santa Maria, hibachi, shichirin) removed as regional traditions for Culinary; Fire pit entries removed (commodity).

**Market panels (ms):**
- Lawn care: Segway Navimow no. 1 for wire-free robotic mowers by units, 2024 (Euromonitor, via ServiceDealer); Husqvarna Group revenue SEK 46.6 billion (2025) and European leader in consumer watering after Gardena (2007); Stihl largest chainsaw maker since 1971; Toro revenue USD 4.51 billion (2025); Deere USD 45.7 billion (2025); Report Prime 2024 ranking (Deere, Husqvarna, Honda, Toro, MTD), with its percentages not used because they add to 133.6 %.
- Outdoor cooking: 60 % of US households own a grill (Traeger prospectus, 2021); Traeger self-described pellet leader; Weber ownership (BDT 2010, listed 2021, private 2023); Middleby bought Kamado Joe, Masterbuilt and Char-Griller (2021); Dansons owns Pit Boss and Louisiana Grills.

**Not sourced:** brand-by-brand share figures for grills and mowers (search excerpts only, so not used); Honda page 404; Traeger and Kamado Joe Wikipedia pages 404; owners for Victa, Napoleon, Primo, Komodo, Recteq, Gozney, Blackstone, Mammotion, Segway (left blank); tier values for non-group brands are my reading of the definitions. The weights of "Global group" for Honda and Makita rest on their Report Prime top-ten placing.

**Brand register:** 25 brands and owners added to C2_brands.json (now 130). C2_renames.json and C2_moves.json unchanged. validate.py --v3: OK.
