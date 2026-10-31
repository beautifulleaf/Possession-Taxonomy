# V4_J3 report: J3 Dairy, Eggs & Alternatives, named-entry pass (medium)

**Fetches:** 31 WebFetch pages plus 1 Firecrawl scrape (FAO brief, WebFetch returned 403) and 5 searches; all logged in rebuild/work/V4_J3/sources.tsv. One 404 (List of countries by egg production).

**Entries, before -> after:** 405 -> 586 archetypes (+181), 463 -> 467 versions. Validate: OK (169 kinds, 586 entries). Five new cheese kinds: Central European & Balkan pressed cheese, Caucasian cheese, Spanish regional cheese, Americas regional cheese, Swiss regional cheese.

**References and coverage (cheese kinds, `sel`):**
- European protected-status list (complete, 236 names): all now placed. Missing before: 45; added, including Afuega'l Pitu, Stelvio and Queijo do Pico.
- Wikipedia List of cheeses read in full (three windows, 303,824 characters). The summariser paraphrased rows, so it gave about 470 usable rows. France, Italy, Germany, the Netherlands, Belgium, Austria and Denmark sit on separate pages and are not covered. Added about 70 rows with a stated type.
- French list read to 100,000 of 119,462 characters (its "Other cheeses" section did not come back); Spanish, Swiss and Italian PDO lists complete; British list cheese rows complete (Cheddar makers and brands left out).
- The coverage line says "Covers ... " and gives these limits. Non-cheese kinds with entries (butter, ghee, yoghurt, skyr, kefir, tofu and others) say that no complete list was fetched and that the kind is not claimed complete.

**Loose models:** 500 `m` removed from all kinds (list in rebuild/work/V4_J3/removed_m.json). Baron Bigod was promoted from them via the British list; the others had no fetched page. 31 maker ranges (`r`) kept unchanged.

**Market layer:** `own`, `tier`, `cty` on 58 branded entries (own_y for siggi's 2018, Boursin 2007, Leerdammer 2021), taken from the existing brand register. Farmhouse makers are tiered Independent, because no craft overview was fetched. Department `ms` and `msum` on eight departments:
- World dairy ranking, top 20 by dairy revenue, FY 2023 (Wikipedia, citing Rabobank); this covers France, Switzerland, US, China, NZ, Denmark, Netherlands, Canada, India, UK, Germany and Mexico.
- FAO 2024: India 17 % of cattle milk; China 33 %, India 9 %, Indonesia 7 %, US 7 %, Brazil 4 % of world eggs.
- DFA about 22 % of US raw milk (2016); Cal-Maine about 20 % of US commercial eggs (2025).
- Planet Oat 35.2 % of US refrigerated oat milk (2023); Oatly revenue US$722 million (2022).
- Valio about 80 % of Finnish milk (no year). Lactalis agreed to buy Fonterra's consumer brands in August 2025.
- Group brand lists: Lactalis, Danone, Arla, FrieslandCampina, Fonterra, DFA, Saputo, Tine, Valio.

**Not sourced:** Nestlé and Savencia brand pages; retail shares for butter, yoghurt, cheese, soy and almond drinks; Africa, South America and the Middle East national champions; Amul, Yili, Mengniu, Saputo and Tine pages gave no shares. `g`/`xg` sections and `role` badges not added (no page named origins or landmarks).

**Brand register:** added DFA, Fonterra, Saputo, Cal-Maine, Kraft Heinz, Mondelez, Morinaga Nutritional Foods, Nestlé, Valio and five ranking-only groups; Lactalis description updated.

Files edited: rebuild/out/J3.json, rebuild/out/J3_brands.json (renames and moves unchanged). Backups in rebuild/work/V4_J3/bak/.
