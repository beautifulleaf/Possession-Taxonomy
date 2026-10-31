# CMP_PLANTS report: J4 Fruit & Vegetables and C3 Plants, completion pass

Backups and rerunnable scripts (apply_j4.py, apply_c3.py): rebuild/work/CMP_PLANTS/. Both files pass validate.py --v3. Every edited kind's `sel` carries a Complete/Covers line.

## Method
- Wikidata SPARQL through WebFetch. Name lookups of the removed names (chunks 0-1 of 9 run; yield was thin for non-apple names). Then enumeration by class label (apple cultivar, mango cultivar, potato variety, banana, pear, orange, cherry, tomato, strawberry, plum, peach, avocado, blackberry, olive, dahlia, rose cultivar, strain of cannabis and others), limited to items with an English Wikipedia article. Each entry cites its Wikidata item.
- Protected-origin names: Wikipedia's List of Italian food and drink products with protected status (fruit, vegetables and cereals section, read in full; 60 names placed as entries) and the FreshPlaza EU fresh produce PDO/PGI article (12 names). They were added as named entries, not versions, because they have no parent cultivar.
- Wikidata does not model EU PDO/PGI products (57 items in all), so French, Spanish, Greek, Polish, Asian and Indian GI names could not be bulk-verified.

## Counts (entries, before to after)
- J4: 557 to 1,051 (+494). Apple 32 to 249; Mango 23 to 93; Potato 29 to 64; Banana 4 to 26; Pear 13 to 29; Cherry 6 to 20; Tomato 22 to 33; Orange 8 to 17; Strawberry 26 to 31; Sour cherry 3 to 12; the rest +1 to +10.
- C3: 1,440 to 1,647 (+207). Seven rose kinds +132 (Wikidata rose cultivar list, 230 rows, 132 with a stated group); Cannabis plant +28; Olive tree +29; Dahlia tuber +11; Apple tree +3; Clematis, Lily bulb, Rhododendron, Seed potato +1 each.
- Reference totals: Wikidata apple cultivar items 2,809 (245 with an article; Wikipedia's list over 7,500); mango 89 of 89; potato 51; olive 37; dahlia 12 of 12.

## Removed names
Of 763 J4 names, 108 are now present (re-added or already an entry); 655 stay out, listed in rebuild/work/CMP_PLANTS/unconfirmed.json. Many are generic types or non-Western GI labels. Of C3's 60, Ben Davis, Cortland, Empire and Red Pontiac were re-added; Camellia, Cymbidium, Crassula, Kalanchoe, Supertunia, yeast, grow-kit and wreath names were not found.

## Still short
Name lookup chunks 2-8 were not run (the enumeration superseded them). Citrus, grape, chilli, persimmon, sweet potato, onion and brassica cultivar canons stay short: Wikidata has few such items with an article. Non-Italian protected-origin names are mostly unverified. Rose items without a stated group (about 98) were left out.
