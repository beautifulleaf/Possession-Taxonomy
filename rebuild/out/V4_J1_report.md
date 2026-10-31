# V4_J1 report: J1 Meat & Poultry, named-entry pass (medium)

**Fetches:** about 31 (logged in rebuild/work/V4_J1/sources.tsv). WebFetch only; no Firecrawl. Failed: Delicious magazine UK butchers list (403), Australian government halal body list (503), Wikipedia "Danish Crown" (disambiguation only). Wikidata was not used: no class models protected meat names.

**Entries before -> after (343 entries in total, was 297):**
- Prosciutto crudo 10 -> 19 and Regional dry-cured hams 11 -> 21 (List of hams, Italian protected-status list; Italian hams: complete, 11 of 11 PDO/PGI names).
- Italian salame 11 -> 16 (7 of 7 salame names in the Italian list); Cotechino 0 -> 2; Italian sausage 1 -> 2; Smoked raw ham 4 -> 6; Cured shoulder 2 -> 3.
- Lamb 5 -> 7 (Agnello di Sardegna, Cordero manchego); Whole chicken 4 -> 7; Turkey 2 -> 3.
- Sausage kinds that were empty or thin gained names from Wikipedia's List of sausages (Toulouse, Merguez, Boerewors, Weisswurst, Cervelat, Saveloy, Chả lụa, Pepperoni, Bockwurst, Kranjska klobasa, Debrecener, Rookworst, Thai, Lao and Philippine sausages).
- All 80 kinds with entries now carry `nl` and `sel`. Where no whole-space reference exists, `sel` says "Not claimed complete".
- Meat box 0 -> 10 supplier entries.

**Reference limits:** the List of sausages was read to character 100,000 of 168,504; the remainder is sidebar. The Italian list was read to character 100,000 of 106,491. The ham list is about 64 rows; unprotected and cooked-ham rows (glazed, city, torchon) were left out as dishes or methods. French, Spanish and UK registers were not fetched whole (eAmbrosia needs script); Spanish names came from a partial list, so Pernil Cerretà and Chistorra de Navarra (search excerpts only) were not added.

**Loose models:** 62 `m` removed (kept in work/V4_J1/removed_m.json): promoted SPAM (3 versions), Tulip luncheon meat, and Boerewors (4 versions); the rest (Beyond, Impossible, Libby's, Princes, Kirkland and similar product names, locust species) had no fetched page and are removed for a later pass.

**Market layer:** `own`/`tier`/`cty` on brand entries: Ball Park and Jimmy Dean (Tyson, 2014), Pilgrim's Pride (JBS, 2010), Jennie-O (Hormel, 1986), SPAM (Hormel), Tulip (Danish Crown), Perdue, plus earlier brands (Beyond, Impossible, Quorn owner not stated). Panels (`ms`): US beef 85 % (JBS, Tyson, Cargill, Marfrig; 2021 article), US pork 66 %, German processed pork two thirds, US chicken 51 % (all same article), 2025 Top 100 net sales (ten processors), JBS revenue US$86.2bn and Tyson US$54.4bn (2025), Hormel US$12.1bn. Not found: shares outside the US and Germany, national champions for about 20 markets.

**Certification and supplier layer:** welfare, kosher and halal certifiers are added to the brand register (OU 1923, OK 1935, Star-K, KOF-K, CRC, Certified Humane 2003, RSPCA Assured 1994, GAP 2008); a Certification tags criterion is on the category and a tag note on each department. Suppliers under Meat box come from Fortune (2026, six US services) and HalalSpy (2026, four UK halal services), linked to I3. No kosher delivery list or UK premium-butcher ranking was fetched.

**Not done:** `role` badges (no page named origin/landmark), `g` sections beyond hams, a halal certifier register (Australian list failed).

validate.py --v3: OK (0 errors, 164 kinds, 343 entries). Files edited: out/J1.json, out/J1_brands.json (renames and moves unchanged).
