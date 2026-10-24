# QS_J7_1 report

Rows: schemes 5; tier_entries 359; makers 204 (new); maker_kinds 204; designations 33; standards 0.

Tier entries per scheme and edition:
- SCH-bordeaux-1855-medoc (1855 list, 61 chateaux): 61 (5 Premier, 14 Deuxieme, 14 Troisieme, 10 Quatrieme, 18 Cinquieme). Source gcc-1855.fr omits Leoville-Las Cases from its Seconds; added from the Decanter page (fetched via Parallel). Decanter also lists Dubignon as a Third Growth (gone since the 1855 merger); not entered. Mouton scope notes promotion in 1973.
- SCH-bordeaux-1855-sauternes: 27 (1 Premier Cru Superieur, 11 Premier Cru, 15 Deuxieme Cru).
- SCH-inao-saint-emilion (2022 edition, stale 2032-12-31): 85 (2 A, 12 B, 71 GCC), from Wikipedia only; INAO page returned 503. Names come from a multi-column layout, so spelling should be checked.
- SCH-inao-graves-1959: 16 (single tier; scope gives red/white).
- SCH-crus-bourgeois-medoc (2025 edition, stale 2030-12-31): 170 (14 Exceptionnel, 36 Superieur, 120 Cru Bourgeois). Official PDF read via Parallel fetch. Its Exceptionnel and Superieur blocks are jumbled in the extract; the split is inferred from the counts (14, 36) and the per-appellation counts in press excerpts. Check once against the PDF layout.
- Liv-ex Bordeaux classification: not entered; no fetched page gave it (liv-ex pages 404 or had none, Drinks Business 403).

Makers: new estates get kind J7.1.1.03 (Bordeaux red blend), Sauternes estates J7.1.6.02. Graves white-only estates (Couhins, Couhins-Lurton, Laville Haut-Brion) use J7.1.2.02 (Sauvignon Blanc). missing kind?: Bordeaux white blend (dry white). Existing estate makers were reused; Bellevue, La Commanderie (Saint-Estephe) and Martin of the Cru Bourgeois list got separate ids (-medoc, -saint-estephe) since the stored same-name ones are Saint-Emilion. Country left blank on new makers (pages do not state it).

Designations (verify/out/QS_J7_1_designations.tsv): 33 Burgundy grand crus (24 Cote de Nuits, 8 Cote de Beaune, Chablis Grand Cru as one appellation), all DES-FR-<slug>, binds tag. None were stored in data/designations.tsv, so no cru_class list for stored ones. Chablis's seven climats are named only in a search excerpt (noted as such).

Failed pages: inao.gouv.fr (503), thewinecellarinsider (403), thedrinksbusiness (403), napavalleywineacademy (no list), liv-ex (404/none), Decanter 2025 article (title only). Skips to other categories: 0.

Helper files: verify/work/QS_J7_1/ (spec.py, gen.py, fetched.tsv).
