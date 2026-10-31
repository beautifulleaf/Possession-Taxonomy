# V4_C4 report: C4 Craft & Art Supplies, named-entry pass

Result: validate.py --v3 reports OK (316 kinds, 483 entries). Entries went from 284 to 483. Only C4.json, C4_brands.json and C4_renames.json were edited; C4_moves.json is unchanged (no kinds moved). Backups are in work/V4_C4/bak/.

## Canon kinds
- **Artists' pigment** (renamed from Dry pigment, recorded in C4_renames.json): 2 entries became 87 or more. It follows every row of Wikipedia's List of inorganic pigments, in colour-family sections. The page is flagged as possibly machine-written, and Realgar, Caput mortuum and Scheele's green appear twice on it and are listed once here. Wikipedia has no list of organic pigments (the URL returns 404), so the organic entries are only those with a Colour Index number on the fetched Pigment, Copper phthalocyanine, Quinacridone and Category:Organic pigments pages. That part is NOT complete. The Kremer and Sennelier ranges stay under "Makers' pigment ranges". No artists' colour makers' names for a pigment were fetched, so no pigment has versions.
- **Yarn weight class** (new kind in the Yarn shelf): 8 entries, the Craft Yarn Council weights 0 to 7 from Wikipedia's Yarn article, with fibre as an attribute (tt). The fibre-based yarn kinds keep the makers' lines. I did not restructure them around weight.
- **Papers**: Canson's families (Ingres Vidalon, "C" à Grain, 1557, Figueras) were added from the fetched Canson page. The Arches and Fabriano Wikipedia pages returned 404, so those two houses keep only the entries from the earlier pass.

## All other kinds
- Every kind that has entries now has `nl` and `sel`, and `xg`/`g` by the maker's home country (from the register; "Country not stated" otherwise). The `sel` text says plainly that no whole-space reference exists.
- Models (`m`): 459 in total. 131 became versions of the maker's line in the same kind, and 64 became entries sourced to the maker's page in the register. 260 were removed because the maker had no sourced page, so the model could not be attested. They are listed in work/V4_C4/log.json. Ranges (`r`) were kept unchanged.
- Fabric houses are makers, not entries: the 5 entries in Quilting and printed cotton, Denim and Wax-print fabric (Kona, Essex Linen, Tana Lawn, Kurabo KD-8, Vlisco) were removed, and their names went into the register as signature lines. Harris Tweed and the linen designations stay as entries.

## Market layer
- Owners sourced from fetched pages: Colart owns Winsor & Newton, Liquitex (bought 2000) and Conté (2004); the page gives 1990 for AB Wilh. Becker's purchase of Winsor & Newton, not Colart's. F.I.L.A. S.p.A. bought Canson in 2016. Newell Brands bought Sharpie (1992) and Elmer's (2015). SVP Worldwide owns Singer, Husqvarna Viking and Pfaff. Fiskars Group (Finland) owns Fiskars.
- `own` and `tier` ("Global group") are set on 34 entries. `cty` is set on 303. The new owner groups were added to C4_brands.json.
- **Not done:** there is no department-level market summary (`ms`) because no share figures were fetched. National champions, independents, craft & indie tiers and `role` badges were not assigned, since no fetched page supports them. The fetched FILA page covered the sportswear company, so it was not used for the art group. FILA ownership of Lyra, Daler-Rowney and others is unsourced and left unset.

## Cannot be sourced / open
Organic pigment canon; Arches and Fabriano family lists; the 260 removed models; owners for most brands; market shares for all markets.
