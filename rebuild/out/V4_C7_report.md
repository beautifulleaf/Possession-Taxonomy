# V4_C7 report (farm and forestry equipment, light pass)

Files changed: rebuild/out/C7.json, rebuild/out/C7_brands.json. No renames and no moves were needed. Backups: rebuild/work/V4_C7/bak/. Script: rebuild/work/V4_C7/build.py. Sources logged in rebuild/work/V4_C7/sources.tsv. validate.py --v3 out/C7.json: OK.

## Commodity kinds (Tractors, Loaders, Field, Woodland, Livestock)
All loose models (m) and ranges (r) removed from 70 kinds (about 160 rows); the kinds are now the end. The 110 makers they named were added to C7_brands.json (name, source page, kind; country and founding year left blank because no fetched page gave them). Removed as out of scope, not converted to entries.

## Vintage tractors (the canon)
Seven tractor kinds now have nl, sel, xg ("by maker") and g per entry, ordered maker, year, name. Fetched Wikipedia pages: Farmall, John Deere tractors list, Fordson, Allis-Chalmers, Massey-Harris, Lanz Bulldog, Oliver/Hart-Parr, Minneapolis-Moline, David Brown, Ferguson TE20, Case, Deutz-Fahr, Zetor (15 fetches in all). Entries before to after: early 5 to 18, hot-bulb 4 to 6, row-crop 5 to 25, standard 11 to 30, European diesel 8 to 15, crawler 5 to 6, garden 2 (unchanged). Farmall bundle split into letter-series and Hundred-series entries; David Brown, Deutz, Zetor and Hart-Parr bundles split into model lines with versions. Roles: origin = Hart-Parr Model 3, Lanz Bulldog, Deutz MTH 222; landmark = Farmall H.
Not complete: no single whole-space reference exists; the IH vehicles list returned only a paraphrase, and the Ford, Fendt, Hanomag, Eicher, SAME, Lamborghini, Caterpillar, Cletrac, Holt and Cub Cadet entries are those of the earlier pass (not re-fetched). Years are blank or approximate where the page gave none.

## Other vintage kinds
Steam engines, stationary engines, threshers, combines, horse-drawn implements: entries and models removed (commodity, no canon fetched); makers kept in the brand register.

## Market panel (Tractors & tractor fittings department)
ms: IndustryWeek U.S. 500, 2023 revenue (farm-equipment.com): Deere $61.222 billion rank 20; AGCO $14.4 billion rank 100; Alamo $1.690 billion rank 464. European farm equipment 2019 turnover ranking, 13 makers, Kuhn first at EUR 1,177 million (Farmers Weekly). Not sourced: CNH, Kubota, CLAAS, Mahindra (no fetched page gave a ranking or share), and no market-share percentages anywhere.
