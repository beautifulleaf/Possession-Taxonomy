# GAP_J5 report (Pantry Staples)

out/J5.json validates (0 errors, 279 kinds). Entries now 2,299 (validator count; +1,356 added, mostly rice). About 40 fetches. Backups in work/GAP_J5/bak/, scripts gap_merge.py and gap_market.py, sources in work/GAP_J5/sources.tsv. Only J5.json and J5_brands.json were edited.

## Gaps and what closed them
- **Loose models:** none left (0 kinds with `m`); nothing removed.
- **Coverage line:** every kind with entries now ends its `sel` with a Complete, Covers or "No complete list exists; follows ..." line (148 kinds got the last form).
- **Rice (Covers 163 of about 1,000):** read List of rice cultivars to its end. New kind "Rice cultivars by country" holds 944 further cultivars (Bangladesh, Indonesia, Pakistan, Philippines, Nepal, Sri Lanka, Malaysia, Iran, Greece, Africa, Texas, Louisiana, Kerala, Tamil Nadu, West Bengal and other Indian states and so on). Complete. Not entered: group labels, wild rice (Zizania), repeats.
- **Instant noodles (20 of about 70):** all 70 table rows plus country-section brands with a stated maker: 85 entries. Complete.
- **Spice blends:** Spice mix page re-read; 8 blends added that had no kind (Adjika, Bouquet garni, Persillade, Powder-douce, Cinnamon sugar, Crab boil, Recado rojo, Idli podi). The rest already have their own kind.
- **Paprika, Split pulses:** wrong copied `sel` text replaced. Paprika +9 (five Hungarian grades, Spanish pimentón types); Split pulses +14 dal types (Wikipedia, Dal). Complete.
- **Hops (no list claimed):** List of hop varieties, +79, Complete. Also complete: Hot sauce (+21, 52 rows), Olive cultivars (new kind, 83), Frozen ready meals (+46) and Frozen pizza (+11), Kimchi (+21 varieties).
- **Covers (out of scope stated):** Dates 36 of about 370 (rest are local oasis names with no note); Dried chilli 33 of about 84 (fresh-pod cultivars belong to J4 Chilli).
- **Market facts:** Heinz US ketchup 61 % and global 25 % (2013, SEC prospectus) added as `ms`. Owners added: Campbell's (The Campbell's Company), Nutella (Ferrero International SpA), Vegemite (Bega Group, 2017), Dolmio (Mars, Incorporated); four brand-register rows.
- **Axis:** `xg` set on kinds whose entries carry sections.

## Remains (searches tried)
- **Olive oil PDOs:** 5 of about 104. eAmbrosia is JavaScript-only; Wikidata class probe returned 0; the French AOP page names none. Searched "Protected Designation of Origin olive oil list Spain Greece France Italy Portugal PDO oils register".
- **Pasta brands:** no list page (List of pasta brands 404; italyweloveyou page empty). Searched "Wikipedia list of pasta manufacturers companies brands Italy". Marked "No complete list exists".
- **Soup, frozen meal shares:** none on Campbell's page. Searched "ketchup market share Heinz United States percent" (found the 2013 figure only).
- **Frozen brands:** the page gives no country or owner, so none recorded.
- **Hops/rice/etc. descriptions:** one line each from the list; no per-entry pages read.
- **Not reached:** Mustard, Ketchup, Honey, Peanut butter brand lists, Stock cubes, Soy sauce brands have no whole-space page; marked "No complete list exists".
