# GAP_C3 report: Plants & Living Cultures

Validator: OK (312 kinds, 1746 archetypes; +99 entries). Backups: rebuild/work/GAP_C3/bak/. Script: rebuild/work/GAP_C3/apply.py. Fetches: 10 (9 Wikipedia genus pages, 1 Wikidata count query), logged in sources.tsv.

## Closed
- Loose models: none remained (0 `m`).
- Coverage line: all 249 kinds with entries now carry a standard line in `sel`. The old "representative set" wording is replaced.
- Completed from the reference, to the end of its species table:
  - Astrophytum 6 of 6; Ariocarpus 7 of 7; Clivia 6 of 6; Miltoniopsis (Pansy orchid) 5 of 5.
  - Lithops (Living stones) 6 -> 37 of 37.
  - Epipremnum (Pothos) 2 -> 15 of 15.
  - Sarracenia (North American pitcher plant) 20 -> 42: all 11 species, all 20 named hybrids and the RHS AGM cultivars. The last 1,199 characters of that page were not read.
  - Heliamphora (Sun pitcher) 23 of 24 species (H. tyleri is named outside the table).
  - Phragmipedium 18 of 18 table species; six further names with debated status are not listed.

## Remaining (not done, honest)
- About 235 kinds say "Covers n entries named on the cited pages; no complete register was fetched". These are genera and cultivar groups (Philodendron, Anthurium, Alocasia, Hoya, Mammillaria, Nepenthes, Drosera, Cattleya, the rose classes, the seed and fruit cultivar kinds and others). Finishing them needs hundreds of fetches against the 60-fetch budget.
- Wikidata genus counts (for example Mammillaria 720, Astrophytum 52 against 6 accepted) include synonyms, so they were not used as "about m" totals. Cultivar kinds (roses, tomato, apple, potato, dahlia) have no bounded whole-space list.
- Not attempted: market facts (no plant-breeder market list fetched), roles, missing sections.
- Section axis (`xg`/`g`): no kind has `xg`; the kinds over 12 entries (roses, olive, tomato, beans, cannabis and others) were not sectioned. Searched: none run.
- Dried flowers (404 in STR pass) and Dwarf conifer (404 in FIX pass) were not retried.
- No brands, renames or moves files changed. Nothing deferred to Firecrawl.
