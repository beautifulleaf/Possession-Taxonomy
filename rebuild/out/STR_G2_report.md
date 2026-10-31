# STR_G2 report: G2 Property & Structures

Resumed after a restart. G2.json was complete and valid, not half-written; only the demoted-archetype step was missing and was fixed.

**Before → after:** departments 6 → 6; shelves 11 → 19; kinds 67 → 81; archetypes 145 → 128; models in `m` 2 → 24. All 81 kinds have `tt`; 18 have `see`. validate.py --v3: OK.

**Category:** new `ax` and 7-step `key` (with a precedence note). Lead unchanged.
**Departments:** each has `t` and `ax`. Houses now has 4 shelves (town, suburban/detached, country/farm, grand). Flats has 3. Factory-built has 4. Land & estates has 4. Unusual & converted has 3 (farm/industrial, worship/civic/defence, pleasure/shelter). Burial has 1 (small).

**Kinds added (sourced):** Split-level house, A-frame house, Log cabin, Barndominium, Container home, Yurt & ger, Allotment, Treehouse, Factory & warehouse conversion, Converted school & civic building.
**Split:** Farm building → Barn, Stable block, Granary & cart shed, Field shelter, Dovecote (renames: Farm building → Barn).
**Merged / moved:** no kinds merged. Dacha, Adobe pueblo-style house, Malay house and Assam-type house moved from Detached house to Cottage (archetypes kept). Nothing added to G2_moves.json.

**Generic archetypes demoted (22 entries kept as models in `m`, with their versions):** Fortified house, Piano nobile apartment, Alpine chalet, Tenement block, Points-based vacation club, Fractional apartment share, Caribbean resort cay, Aegean private island, Whole populated island, Highland sporting estate, Kentucky bluegrass stud farm, Bordeaux first-growth château estate, Tuscan coastal tenuta, Texas cattle ranch, Outback cattle station, Residential fly-in airpark, Converted oast, Home fallout shelter, Missile silo conversion (Survival Condo kept as a model), Bournemouth beach hut, Mudeford Spit hut, Brighton bathing box. Their `s` links are not carried (models have no source field).

**References fetched (work/STR_G2/sources.tsv):** Wikipedia: List of house types, Category:House types, Category:Apartment types, Prefabricated home, Yurt, Treehouse, Allotment (gardening), Adaptive reuse, Cemetery, Category:Burial monuments and structures, Category:Real estate terminology.

**Cross-links (all targets checked):** Farmhouse, Barn and Factory & warehouse conversion within G2; G3 (Garden log cabin, Shipping container, Boathouse, Garage); G1 (Fifth-wheel caravan, Touring caravan, Houseboat, as in STR_SEE.tsv); F4 (Grave marker, Coffin, Cremation urn).

**Not sourced:** Shipping container architecture page returned HTTP 522; Container home rests on the other fetched pages. Shelves with 3 or fewer kinds have no `ax`. Per-shelf coverage used the pages above, not a specialist retailer.
