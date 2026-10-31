# V4_J4 report: J4 Fruit & Vegetables, named-entry pass (light)

**Fetches:** 19 (all logged in rebuild/work/V4_J4/sources.tsv); 3 returned 404 (Club apple, Banana production by country, List of blueberry cultivars). No Firecrawl use.

**Kinds with entries (cultivars), entries before -> after**
- Apple 29 -> 32 (+Baldwin, Winesap, Golden Russet from Wikipedia's List of apple cultivars; the page lists over 7,500 cultivars, so the scope is cut to cultivars with a trade or collector role).
- Pear 12 -> 13 (+Seckel; List of pear cultivars, about 155 rows of over 3,000).
- Strawberry 17 -> 26 (+9 from List of strawberry cultivars, with breeder, year and parentage).
- Mango 19 -> 23 (+Totapuri, Amrapali, Badami, Palmer; List of mango cultivars, first 100,000 characters read).
- Potato 29 -> 29 (List of potato cultivars confirmed origin and year for existing entries; no new ones).
- All other kinds that have entries keep them unchanged (112 kinds with entries in total, each now with `nl` and `sel`). Where no whole-space reference was fetched, `sel` says so and names the pages cited on the entries, with "not claimed complete".
- Commodity kinds (no entries) stay as they were; `t`, `ax`, `tt`, `see` untouched.

**Loose models removed:** 763 models (`m`) from 129 kinds, no ranges existed. Most were cultivar or protected-origin names with no fetched page behind them (for example the PGI/PDO labels under Apple, Pear, Potato). Each is kept in rebuild/work/V4_J4/removed_m.json so a later pass with a reference can promote them. A few duplicates of existing entries (Beurre Hardy, Concorde) were simply dropped. No `m` carried a maker, so no maker was added from them.

**Club varieties (own, tier, cty):** Cripps Pink (owner: Department of Primary Industries and Regional Development, Western Australia; Pink Lady trade mark with APAL; Australia, 1973), SweeTango (University of Minnesota; Pepin Heights has marketing rights), Cosmic Crisp (Washington State University, patent owner), Jazz (New Zealand; owner not stated on the page, ENZA named as collaborator), Kanzi (Belgium; trade mark holder not stated). Tier "Independent" for all. `own_y` left blank: no page gave an acquisition year. Envy and Rubens not re-fetched, left as before.

**Market panels (ms, msum):**
- Tropical & subtropical fruit (bananas): top three (Chiquita, Dole, Del Monte) 36.6 % and top five 44.4 % of world exports in 2013 (FAO); Chiquita 13 %, Del Monte 12 %, Dole plc 11 %, Fyffes 6 % in 2025 (Wikipedia Banana industry, citing Bananalink).
- Temperate fruit: Pink Lady third by value in UK apples, 2012.
- Not sourced: Zespri and Fresh Del Monte pages gave no share or rank; no market panel for kiwifruit, pineapple, citrus, vegetables, salad or mushrooms. National champions and about 20 markets were not reachable in the fetch budget.

**Brand register (J4_brands.json):** updated Dole (Ireland, 1851), Chiquita (1870, owner Cutrale and Safra since 2014), Zespri (New Zealand; the page gives both 1988 and 1997, so no year), Fresh Del Monte Produce; added APAL, Pepin Heights Orchards, Washington State University, DPIRD (Western Australia); Fyffes confirmed.

**Certification:** a note that organic and fair-trade certifications are tags, not kinds, added to the `t` of the five fresh-produce departments (not Fruit gifts).

**Not done:** `g`/`xg` sections (no field axis fetched for most kinds); `role` badges (no page named origin or landmark status); versions for sports and clones.

validate.py --v3: OK (0 errors, 257 kinds, 557 entries). Files edited: rebuild/out/J4.json, rebuild/out/J4_brands.json. Moves and renames unchanged (none needed).
