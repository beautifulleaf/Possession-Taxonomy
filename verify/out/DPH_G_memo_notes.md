## G1

G1 is not built: no nodes, no kinds, and the memo has no section 13. These notes bind the tree builder the way memo text does (R-118 a). Ids follow R-58 from the memo's numbering: G1.1.1 to G1.1.10, G1.2 (no leaf), G1.3.1 to G1.3.3, G1.4.1 to G1.4.2, G1.5.1 to G1.5.4.

- **Electric bikes (Cycle King has a top-level electric branch): attribute.** No new kind and no new leaf. Store `assist` (none | pedal assist | pedal assist with throttle) on bicycle named forms (G-4, C10). Build an "Electric bikes" shortcut view under the Bicycles group that filters on `assist` ≠ none. EPAC, speed pedelec and US class 1–3 are C17 rows.
- **Gravel bike, called a "commercial umbrella label" (Adventure.cc): covered, provisional.** Keep the gravel bike kind under G1.1.5 as the memo has it (Rose and Buychari list it separately). At attestation (HV_G1), record whether the fetched retailer lists gravel separately from road. If no fetched seller does, a later decision pass merges it into road bike with `geometry` = gravel (merge rows, no renumbering). Cycle King's "road and gravel" heading is not enough to merge on.
- **Autohome per-body size ladders: attribute.** `size_class` goes on car and van named forms. Each value is qualified by its scheme (Autohome car, Autohome SUV, Autohome MPV, EC segment, GB/T 3730.1). It is never a level. The region-tagged size view stays generated (G-3).
- **Euro NCAP and J.D. Power need registry rows: needs.** Euro NCAP stars (class ii, on the variant, `test_version`, `stale_after` because the protocol changes about every three years). J.D. Power IQS and VDS (class ii, lower is better, scope = model year). Listed in DPH_G_needs.tsv for the QS_ batches.
- **No specialist bike, boat, RV or aircraft shop was fetched: noted.** The markers for boats, caravans and aircraft are provisional.
- **Motorcycle kinds cruiser, sport, touring and adventure, and the centre console boat: noted (evidence confirms the memo).** The HV_G1 harvest may use the HOL_EV_9 pages (SlashGear first-motorcycle guide; YachtWay vessel types) as attestation sources. Both were fetched in full.
- **Microcar, open keelboat and cruising houseboat (narrowboat as a named form): noted.** They get ids as † kinds in the memo tree and are attested at HV_G1. If one is not attested, it waits; it is never dropped by default.
- **Light-sport airplane: noted. No id at build.** It goes to the harvest prompt as a "missing kind?" (R-96 c). The LSA certification category is a C17 row. It becomes a kind only if a fetched page shows a distinct design type sold under that name.
- **Display regrouping (proposal level-1 groups): display_only. The builder writes groups.tsv rows by node id. No id changes.**
  - Cars = G1.1.1
  - Vans, trucks and buses = G1.1.2
  - Motorcycles, scooters and powered light rides = G1.1.3
  - Bicycles and other cycles = G1.1.5 + G1.1.6, with the e-bike shortcut
  - Off-road, snow and utility vehicles = G1.1.4
  - Caravans, motorhomes and trailers = G1.1.8 then G1.1.7
  - Boats and watercraft = G1.3.1–G1.3.3
  - Aircraft = G1.4.1–G1.4.2
  - Rail and horse-drawn vehicles = G1.2 + G1.1.9
  - Prams and strollers = G1.1.10
  - Parts and accessories = G1.5

  Every leaf goes in exactly one group. The memo's Land, Rail, Water and Air sub-families stay as stored nodes but are not shown first.
- **Make tab beside the type tree: display_only.** The maker role is owner (maker_roles.tsv), so the tab lists only makers that own named forms or lines in each type. There is no standalone maker list.
- **"Camping and van life" view: display_only.** It is a generated view over G1.1.7, G1.1.8 and G2.2.4.2 (cross-link, one home kept). The "van life" scene tag is held back until it has a fetched definition source (C8).
- **Kids' bikes department view: display_only.** It uses the user tag (child, C6/C15). There is no kind.
- **Brand-status lists (eBay Exotics, CCCA Full Classics): needs.** eBay Exotics is a dated platform_tag (class vi). CCCA is an editorial list on named forms (class iii). Neither is a level.
- **Maker trim ladders and groupset ladders: needs.** The Polaris ladder is class iv on lines. Groupset ladders are class iv on component lines in G1.5 and provisional, since none was attested.
- **Design standards (CE design category A–D, ISO 4210 and 8098, EN 15194): needs (standard).** They are stored as `standard_met` through standard_values, never as kinds.
- **Parts fit rows (hitch classes, trailer sockets, ISOFIX and i-Size, EV connectors, bicycle component standards, cleat systems): needs (platform).** They are harvested in a PF_ batch once G1.5 is built, with `kinds_served` left empty until then.
- **Other stored attributes for the facet list: attribute.**
  - `propulsion` (shared, on kind, overridable on a named form)
  - `body_substyle` (G-5)
  - `geometry` (G-7)
  - `construction` (G-8)
  - `rig`
  - `hull_count`
  - `length_band` (band edges provisional)
  - `carrycot` (P14)

  Frame size is a size variant (C3), not an attributes row. Seats and mass stay attributes or C17 rows, as G-9 says. Price, new or used, year, mileage, stock and location describe a listing, are never stored (C16), and appear only as buying-guide text.

## G2

G2 is built as nodes only: 23 nodes are in data/nodes.tsv, and the 55 kind ids of memo section 13 are not yet in data/kinds.tsv. These notes bind the build.

- **SUUMO's new / pre-owned split at the top: attribute plus shortcut, not a level.** `build_history` (new build | conversion) is stored only on named forms where it holds for every object: loft = conversion, and factory-built models in G2.2.4 = new build. The "new or pre-owned" choice appears in the buying-guide box as a question, not as a tree branch (C5, C16).
- **Rental: display_only, out of scope (decided).** Only what is owned is a possession (BRIEF scope). The portals' first "buy or rent" step is not shown. Leasehold, share of freehold, strata and condominium are owned tenures and stay in the tenure guidance. A short-term rental is out.
- **Location, station, commute and the other listing filters: display_only (decided).** G2 stores no listing (C16). Its pages are buying guides over kinds and named forms. Location, rail line, commute time, price, bedrooms, bathrooms, garden, parking, balcony, pet-friendly, renovated, retirement, auction and date added are not stored and are not page filters. They appear as the "what to filter by when you search" line of each guide, in the proposal's order (location first). The pages link out to portals only through fetched portal pages. No search URL with location parameters is built (URL rule, R-110 f).
- **EPC and RICS need registry rows: needs (grading_scale).** EPC A–G is a measured-spec scale for guidance; its CO2 rating is noted. RICS survey levels 1–3 are listed with condition ratings 1–3 (the ratings are from memory and provisional). No value is ever stored for a home (C16).
- **Building and pest inspection (AU) and the LIM report (NZ): needs (standard), with no tier.** They are shown as due-diligence steps in the house and land guides.
- **Agricultural Land Classification: needs (grading_scale, classification).** It serves the arable, grazing, permanent-crop and mixed-holding kinds as guidance only. `alc_grade` is never stored on a parcel. Only the scheme row is.
- **Build standards BS 3632, BS EN 1647, HUD code, IRC Appendix Q, and RV standards for park models and tiny houses on wheels: needs (standard).** They are stored as `standard_met` on factory-built named forms. ANSI A119.5 and NFPA 1192 are provisional.
- **China Grade A and 5A offices: needs (scheme, class iii).** This is a registry row only, serving G2.3.7.1.
- **Trusted-Shops-style portal ratings: noted.** None were found, so no scheme is needed.
- **Burial places and commercial buildings have no HOL evidence: noted.** The memo's calls stand, provisional until attested.
- **The evidence is Anglosphere- and Japan-heavy: noted.** HV_G2 should fetch at least one continental European or Asian portal type list (level only, never inclusion).
- **Scoped maker role (owner for factory-built homes, garden buildings and pool shells): covered.** It is already in maker_roles.tsv (R-116 c). Price bands attach only to those makers, lines and models (C4 d).
- **Display groups: display_only, applied now as groups_changes (by node id).** The groups are:
  - Houses and flats (houses; flats and maisonettes; whole residential buildings)
  - Park, mobile and floating homes
  - Land and farms (building plots; farm land; woodland; lakes and water; mixed holdings and smallholdings)
  - Garden buildings and outbuildings (garages and carports; sheds and workshops; garden rooms and cabins; barns and stables; gazebos, pergolas, decks and patios; swimming pools)
  - Commercial buildings
  - Burial places
- **Side views: display_only.** The views are:
  - a makers' ranges tab for G2.2.4, G2.3.2 and G2.3.3 kit buildings and G2.3.6 pool shells only
  - a "by tradition" view of regional named forms (riad, finca, trullo)
  - tiny-house and liveaboard views

  The tiny-house and liveaboard scene tags need their definition sources loaded (tinyhomesnest, YSN; memo §7).
- **Stored attributes: attribute.**
  - `house_form`, `floor_position`, `construction`
  - `propulsion` (none | towed on the moored houseboat and floating home, the K-60 line)
  - `units_in_building`
  - `managed_for`
  - burial: `burial_position`, `remains`, `capacity`, `allocation`

  Each is stored only where the value holds for every object of the kind or named form (memo §10 facet schema).
- **Data defect found: noted, for a tools/ fix (not done here, no data writes).** The leaf names of nodes G2.2.1, G2.2.2, G2.2.4, G2.3.3 and G2.3.7 kept the memo's markdown and were cut at a colon. For example, name "Houses** (kind axis" and axis "attachment to neighbouring dwellings)". The names should be "Houses", "Flats and maisonettes", "Dwellings kept in place that are not buildings", "Rooms for people" and "Other buildings by function", with the kind axis moved into the axis column.
- **G2 kinds not yet loaded: noted.** The build loads the 55 ids of memo section 13 from audit/KL_G2_tree_v2.md before HV_G2 attestation. The groups above reference nodes only, so they are valid now.
