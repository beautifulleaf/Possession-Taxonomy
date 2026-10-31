# GAP_J3 report: Dairy, Eggs & Alternatives

Validate: OK (169 kinds, 733 archetypes, was 586). About 38 fetches, all logged in rebuild/work/GAP_J3/sources.tsv. Backups in rebuild/work/GAP_J3/bak/. Files edited: J3.json, J3_brands.json.

**1. Loose models.** None remained (0 `m` kinds); nothing to do.

**2. Coverage lines.** Every kind with entries now ends its `sel` with a coverage statement: cheese kinds "Covers n of about 375 in Wikidata's cheese class"; butter "Covers 2 of 5 in Wikidata's butter class"; yoghurt, fermented-milk, ghee and tofu kinds "No complete list exists; follows ...".

**3. Partial coverage closed.**
- Wikidata cheese class Q10943 (375 items) read in full by SPARQL through WebFetch. 100 in-scope items added with Wikidata item URLs (Italian PAT and PDO cheeses, Quebec and Argentine cheeses, Caucasian, Balkan, Spanish, monastery cheeses and others). Classes, dishes, brands of companies and items with no usable description were left out.
- Wikipedia lists of German, Dutch and Italian cheeses read in full (Italian: 272,410 characters, last 72,000 are navigation only); 47 named cheeses with a stated milk, type or protected status added. Italian rows with no milk, type or status (several hundred local names) are left out as unclassifiable.
- French list read to its end (119,462 characters); its "Other cheeses" section never came back from the summariser. Belgian, Austrian and Danish list pages return 404.
- Total added: 147 entries (13 candidates were duplicates and skipped).

**4. Gaps from the earlier reports.**
- Savencia brand page: closed (Wikipedia: Saint Agur Blue, Saint Albray, Etorki, Alouette, Pié d'Angloys); Savencia added to the brand register.
- Middle East champion: closed. Almarai value shares in Saudi Arabia: fresh milk 67.5 %, fresh laban 68.2 %, zabadi 62.0 % (annual report; the page gives no period, so yr 2025 is the report's own "close of 2025" and is noted as such). Added to the Milk and Yoghurt market facts; Almarai added to the register.
- Nestlé brand page: fetched (List of Nestlé brands); it lists milk, chilled and yoghurt brands but no cheese or butter brands, so no J3 cheese or butter entries followed.
- Not closed. Searched: "US natural cheese retail market share Kraft Heinz Sargento" (only 2015 Packaged Facts figures, Kraft about 17 %, no fetched page); Amul, Yili and Mengniu Wikipedia pages (no share figures); Clover Wikipedia page 404; "Clover Danone Brazil yoghurt market share" (no Brazil or Latin American source). Retail shares for butter, yoghurt and cheese, and champions for South America and the rest of Africa, remain empty.

**5. Sections.** `xg` and `g` added to the 13 kinds over 12 entries (Fresh soft cheese, Queso fresco, Ricotta, Lactic goat, Farmhouse blue, British farmhouse hard, Italian mountain by region, Pecorino by region, Gouda, Spanish regional, Americas regional, Central European and Balkan, Brined white cheese). No kind has `role` badges: no fetched page names origins or landmarks for these entries.

**Remaining.** Newly added Wikidata entries carry only name, country and status from the item label, so their descriptions are short. No `own`/`tier` set on the new entries (no brands). Butter-like goat and chivry butter have no description to source.
