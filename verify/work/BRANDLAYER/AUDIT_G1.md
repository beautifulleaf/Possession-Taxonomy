# AUDIT G1 Vehicles (cold, Opus)

**Accuracy:** 2/25 wrong (seed 7). *Pakistan* is a navbox link. *Legor Cicli* is marked premium on a directory listing, which only shows existence. Three correct rows still need merging: Beijing Automobile Works into BAIC, Toyota Canada into Toyota, and Sundown Motos into Brasil & Movimento.

## Whole-file checks (scripts in AUDIT_G1_tmp/scripts, run against the saved raw pages in G1_tmp)
1. **Navbox and footer rows**: 70 rows from List of car brands come from the 'Automotive industry' navbox (v/t/e, countries, topics, trade bodies). There are also 4 Coachbuilder image captions, 3 framebuilding schools, and Diana (tractors). All 78 are dropped.
2. **No own article**: 19 rows link to a model, a person or a parent company, and ChienThang links only to an image. These rows become listed.
3. **Merges**: 63 rows duplicate register brands under longer or national-subsidiary names (Volvo Cars, Geely (Jili), Ram Trucks, Toyota/Honda/Ford/GM Canada, Trek Bicycle Corporation, Malibu Boats ...). 34 more are duplicates inside the harvest.
4. **Homonym masking**: the harvest skipped every list name already in the register under any category. The audit proposes 101 qualified homonym rows (Mercedes-AMG, Prince Motor Company, Kaiser Motors, ČZ Strakonice, Shark/Bell/Simpson/Scorpion helmets ...). It also proposes 23 cross_tags where the register row is the same company (Panasonic, Kettler, Tunturi, Radio Flyer, Razor, Sinclair Research, Sidi, TCX, Altberg, Uvex ...).
5. **Defunct makers**: these are kept, because classic vehicles are still traded. No maker of rail-network or airline vehicles alone was found.
6. **Sources that only show existence**: 341 TheFramebuilders rows become listed. Cherubim stays premium, re-sourced to Velo, and Level becomes cultural via Wikipedia Keirin. All 36 SHARP rows become listed, because the page shows no stars, and 11 generic names get qualifiers. Practical Caravan: Elddis, Knaus and Lunar become cultural (survey only), and Hobby, Mink, Go-Pod, Freedom and Camperlands become listed.
7. **MOVES**: Sugino, Smittybilt and Blaupunkt do not overlap the harvest. Blaupunkt is a cross_tag of the D3 register row.
8. **Country field**: it is wrong on all 718 car rows ('Active'/'Former') and on 276 bike rows (A-Z letter). The fix is in country_fix.json.

## Additions: 70 brands, 8 regions
- **Canoes and kayaks (25)**: Swift, Wenonah, Esquif, Nova Craft, Souris River, Northstar, Clipper, Hornbeck, H2O, Stellar, Dagger, Jackson, Pyranha, AIRE, Liquidlogic, Waka, Zet, Prijon, Lettmann, P&H, RTM, Roto, Gumotex, Nortik, Native.
- **Gliders, balloons and light aircraft**: Jonker, LAK, Allstar PZL, HpH, AMS Flight, Tecnam, CubCrafters.
- **Prams**: iCandy, Joie.
- **Wooden-boat yards**: Spirit Yachts, Ben Harris, Pendennis, Cockwells, A & R Way, Brooklin, Woodbridge & Waldringfield, Dennetts, Abbey Boat Builder, William Fife, Artisan Boatworks.
- **Venice**: 4 squeri and 3 remeri.
- **Sur dhow yards**: Juma Hassoon, Rajab Khamis, Saleh Al Shahri.
- **Horse-drawn (Mifflinburg buggies)**: Heiss, Mifflinburg Buggy Co.
- **Heritage rail**: Dampflokwerk Meiningen, Tyseley.
- **Keirin builders**: Makino, Kalavinka, Samson.
- **Other**: Dallara; Daytona boots; car care (Soft99, Sonax, Angelwax, Simoniz); Pakistani truck art (Barkat Ali body maker, Hassan Autos).
- **Regions**: Sur/Ashkara; Motor Valley; Coventry; Mifflinburg; British wooden-boat yards; Venice (extended); Pakistan truck art; Bulukumba pinisi (no brand: only one holding's SEO sites).

## Register issues
Some register rows mix different companies: Jaguar (A5 Festina watches), Ferrari (J7 Ferrari Trento), Yeti, Bell, Sunbeam, Imperial, Alpina, Suzuki, Proton, Benelli, Singer. Koenigsegg is listed twice.

## Blind spots still open
- Thai tuk-tuk builders: none is named on a reliable page.
- Amish buggy makers: none is named.
- Pinisi yards: none is named on an independent page.
- Practical Caravan Awards (quality) need the awards pages themselves, beyond the best-makes guide.
- Much of the Wikipedia car list is obscure defunct marques with thin cultural standing.
