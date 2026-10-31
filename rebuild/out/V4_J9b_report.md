# V4_J9b report: J9 restructured market-first

Files: rebuild/out/J9.json, J9_brands.json, J9_renames.json (J9_moves.json unchanged). Backups in rebuild/work/V4_J9b/bak/; script restructure_j9b.py. `validate.py --v3`: OK (105 kinds, 960 entries; the pilot's 973 minus 13 merged duplicates).

## Shape
Eight departments, each with a market `ax`, rewritten `t`, and shelves: Global groups (one kind per owner: Coca-Cola, PepsiCo, Keurig Dr Pepper, Nestlé, Danone, Suntory), National & regional brands (one kind per world region), Independents (per region, or one kind if small), Craft & indie, Own label. All flavour kinds (Cola, Lemon-lime, Fruit soda ...) are gone; the old kind survives as the start of each entry's `dt`. J9_renames.json maps all 95 old kinds (including the earlier renames) to the new kind that took most of their brands; empty commodity kinds map to the first kind of their department. Kind-level `see`, `m`, `r`, `tt` of the dropped kinds went with them.

## Entries per tier
Global groups 192; National & regional 422; Independents 314; Craft & indie 22; Own label 10.
By region (national / independents / craft / own label): Europe 177 / 126 / 3 / 7; Latin America & Caribbean 69 / 36; North America 54 / 39 / 18 / 2; South & Southeast Asia 32 / 43; Africa 27 / 3; East Asia 25 / 32; Middle East 20 / 24; Oceania 11 / 11 / 1 / 1; origin not stated 7.
Rule used: owner stated and in a global group goes to Global groups; owner stated and not global goes to Independents; no owner stated goes to National & regional. Craft follows the two fetched craft overviews; own label follows the list's retailer owners. Kofola, Kinnie, Almdudler, Rivella, Irn-Bru, Inca Kola and Thums Up sit in National & regional with `role` = landmark and `tier` = National champion, each on a fetched page's statement. Coca-Cola is landmark in Global groups.

## Brands looked up (own page fetched)
Jarritos, Guaraná Antarctica, Vimto, Cheerwine, Faygo, Almdudler, Kinnie, Kofola, Fanta, Sprite, Postobón, Orangina, Club-Mate, Rivella: 14 brands. Owners found: Novamex, Ambev (as manufacturer), Nichols plc, Carolina Beverage Corporation, National Beverage, Klein family, Simonds Farsons Cisk, Kofola ČeskoSlovensko, Grupo Mariposa, Suntory (Orangina, from 2009), Brauerei Loscher, Rivella SA. About 80 flavours and variants were added as versions (Jarritos 16, Kofola 14, Faygo 15, Fanta 9, Sprite 7 and others). Manaos: no page found (Wikipedia result was the city), so it keeps only its list data.

## Market facts added (department `ms`)
US carbonated soft drinks, first three quarters of 2024 (Beverage Digest, quoted on a fetched page): Coca-Cola 40 %, PepsiCo 27 %, Keurig Dr Pepper 24.5 %. US brand shares 2024 (TipRanks): Coca-Cola 19.1 %, Dr Pepper 8.3 %, Sprite 8.03 %, Pepsi 7.97 %. UK 2019: Coca-Cola European Partners 31 % by value, 21 % by volume of non-alcoholic ready-to-drink (company claim). Switzerland 2013: Rivella 15.3 % by value. Austria: Almdudler second to Coca-Cola, no figure. The 2008 to 2018 facts from V4_J9 are kept. `msum` for Sodas updated.

## Gaps
- Most of the 960 brands were not looked up individually: 528 have a stated owner, 432 have none (own left blank); only the 14 above gained flavours, so most national brands have no versions yet.
- No fetched page gave current shares for Germany, Brazil (Abir 2008 and 2009 figures appeared only in search excerpts; investe.sp.gov.br is blocked from this session), India, China or Mexico (Just Drinks paywalled; 2009 Datamonitor only in an excerpt). Statista pages return masked values.
- Independents is large because every stated non-global owner lands there, including local bottlers; a finer test of "established" was not possible from the lists.
- Fanta: two list entries collapsed into one. Firecrawl was used once (BusinessWire, WebFetch 403); it held no share figures.
