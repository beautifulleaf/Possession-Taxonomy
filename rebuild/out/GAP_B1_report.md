# GAP_B1 report (B1 Furniture & Storage)

Edited: rebuild/out/B1.json and B1_brands.json (backups in rebuild/work/GAP_B1/bak/). Validates OK (119 kinds, 845 -> 949 archetypes). About 45 fetches.

**State found:** the gaps.md counts (loose models 61, no coverage line 47) were stale. B1.json already had no `m` models, a "Covers" line on every kind with entries, and `g` on every entry of kinds with `xg`. No kind has over 12 entries without sections. So the work was the report gaps.

**Closed**
- IKEA: IKEA Museum product-stories index (fetched) gave a dated list of 1950-2019 stories. 84 furniture entries added across 19 kinds (Hemnes 2000, Malm chest 2002, Stockholm, Klippan 1979 dated, and others). Lamps, rugs, textiles, kitchens, tableware and children's sets (Anna, Puzzel) left out of scope.
- Muuto: scandinaviandesign.com gave designers; 14 entries (Fiber chair 2014, Oslo sofa 2013 dated; the rest have designer only). Owner MillerKnoll, acquired 2018.
- Wikidata furniture class with a maker (208 rows read to the end): 7 new pieces (Allunaggio, La Chaise, Bocca, Bookworm, Theodore Roosevelt desk, S chair, Deutsche Werkstätten programme). Furniture with a creator (673 items) is mostly Catalan museum objects; no canon.
- Owners: Serta and Simmons (Serta Simmons Bedding, Advent 2012), Leesa (3Z Brands 2023), Nectar (Resident Home, Ashley 2024), Vitra, Steelcase (HNI, closed Dec 2025), La-Z-Boy, Kartell (Felofin), Emeco (Buchbinder 1998), Artifort (Lande 1998), Secretlab, Isokon, Gufram and Memphis (Italian Radical Design Group), GUBI (Augustinus 24%, 2018), Fredericia and Erik Jørgensen (2020), Graco (Newell 1999), Arflex, Vitsœ. Brand register updated, 7 owners added.
- Market: Home News Now 125 (US furniture and bedding retail 2025) added to Sofas & armchairs and Beds & mattresses; HNI-Steelcase deal to Chairs.
- Le Corbusier page end: read; furniture list only names LC4 and Grand Confort. Design Museum London object list: only Transat chair and Thonet No. 14 are furniture.

**Remaining (two attempts each)**
- Vitra Design Museum chair results 31 onwards, MoMA pages 2+ for cabinet, desk, bed, screen: JavaScript or 403; queued in firecrawl_deferred.md.
- String product timeline and owner: stringfurniture.com 403 (queued). Thonet: Wikipedia and Gebrüder Thonet page list no models; a search gave Cesca/S 32/S 64 only as excerpts. Searched: "Thonet S 32 S 64 B 9", "Thonet No. 14 designs list".
- Owners not found: Hypnos (family business per search, no owner named), Vispring (management buy-out 2000 only), Bonacina, Tecno, Tolix, BBB, De Padova, Saporiti, PP Møbler, Fritz Hansen, &Tradition, USM, Zanotta, Gavina, Gispen, de Sede, Cappellini (Wikipedia 404 or disambiguation). Searched: "&Tradition owner", "Fredericia owner", "Hypnos owner".
- Nectar owner rests on a search excerpt; the pages were 403 (queued).
- Cooper Hewitt collection moved to si.edu; not read. V&A pieces in non-plywood materials unread.
