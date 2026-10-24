# DEP_F3_3 report

Task: banknote series and named notes worldwide (F3.2.1.01, F3.2.1.02, F3.2.2.01, F3.2.3.01, F3.4.4.01).

- Kinds: all five already in data/kinds.tsv, so no kind rows written (no _kinds.tsv). No missing kinds found.
- Named forms: 126 rows in DEP_F3_3_named_forms.tsv (F3.2.1.01 74, F3.2.1.02 5, F3.2.2.01 5, F3.2.3.01 22, F3.4.4.01 20), all non-maker, ids NF-<kind>-Z3nnn, notes start "issuer I-<slug>;".
- Issuers: 40 rows in DEP_F3_3_issuers.tsv (data/issuers.tsv was empty).
- Makers: none written. F3 role is owner only and no banknote printer owns a named form here (De La Rue, Canadian Bank Note Company, Townsend & Son, PWPW appear only in notes).
- Continents: Europe (BoE, euro, SNB, Scotland, NBP, Notgeld), N America (Canada, US, Mexico), S America (Argentina), Asia (Japan, China, Philippines, Korea, Thailand, Hong Kong, Israel), Africa (South Africa, Zimbabwe), Oceania (Australia, NZ).
- Sources: Wikipedia, central bank pages (ECB, SNB, BCRA, HKMA), Bank of Canada Museum, Banknote World, Planet Banknote, Littleton, Chula Vista Coins. Numista, PMG and Banknote World catalogues were not reached; 4 fetches failed (403/503).
- Weak spots: Thai Series 1/2 issuer is assumed, not stated; Thai Series 16/17 cut off; Swiss/Zimbabwe tables partly read; Polish 2014 note legal-tender status unstated (placed non-circulating); US fractional currency and French chamber-of-commerce notes only in search excerpts, so not recorded; Nigeria N100 commemoratives not fetched.
- Excluded: Hell bank note (F4). Not placed: Series 1937/1935 duplicates none.
