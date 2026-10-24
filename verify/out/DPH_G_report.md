# DPH_G report: structure decisions for domain G (G1 Vehicles, G2 Property & Structures)

Opus pass, offline: no web, no git, no writes to data/ or framework/. Neither category is built. G1 has no nodes or kinds. G2 has 23 nodes and no kinds. So there is no kinds or moves file. The decisions are build notes (verify/out/DPH_G_memo_notes.md) plus the attribute, needs and groups files.

## Counts per decision

| Decision | G1 | G2 |
|---|---|---|
| attribute | 3 | 2 |
| covered | 1 | 1 |
| display_only | 4 | 4 |
| needs (scheme, standard, grading scale, platform) | 6 | 5 |
| noted | 4 | 5 |
| new_kind, merge, split, named_form, other_category | 0 | 0 |
| **points** | **18** | **17** |

## New kinds, merges, splits
None.
- E-bikes stay bicycles with `assist` (G-4, C10).
- The gravel bike kind stays (provisional). It merges into road bike with `geometry` = gravel only if no fetched seller lists it apart at attestation.
- The light-sport airplane gets no id at build. It is a "missing kind?" for the harvest, and its certification category is a C17 row.

## Attributes (DPH_G_attributes.tsv, 21 rows)
- G1: `assist`, `size_class` (scheme-qualified: Autohome car, SUV, MPV; EC segment), `propulsion`, `body_substyle`, `geometry`, `construction`, `rig`, `hull_count`, `length_band`, `carrycot`.
- G2: `build_history` (new build | conversion, only where it holds for every object), `house_form`, `floor_position`, `construction`, `propulsion` (none | towed), `units_in_building`, `managed_for`, `burial_position`, `remains`, `capacity`, `allocation`.
- Listing values (location, price, bedrooms, mileage) are never stored (C16).

## Needs (DPH_G_needs.tsv, 27 rows)
- **G1 schemes:**
  - Euro NCAP (ii)
  - J.D. Power IQS and VDS (ii)
  - eBay Exotics (vi)
  - CCCA Full Classics (iii)
  - Polaris trim ladder (iv)
  - bicycle groupset ladders (iv)
- **G1 standards:** CE design category, ISO 4210/8098, EN 15194.
- **G1 platforms:** hitch classes, trailer sockets, ISOFIX/i-Size, EV connectors, bicycle component standards, cleat systems.
- **G2 grading scales:** EPC A–G, RICS levels and condition ratings, ALC grades.
- **G2 standards:** AU building and pest inspection, NZ LIM, BS 3632, BS EN 1647, HUD code, IRC Appendix Q, RV standards for park models and tiny houses on wheels.
- **G2 scheme:** China Grade A/5A offices.

## Groups (DPH_G_groups_changes.tsv, 20 rows)
G2 gets six level-1 groups by node id, with 14 level-2 groups under them:
- Houses and flats
- Park, mobile and floating homes
- Land and farms
- Garden buildings and outbuildings
- Commercial buildings
- Burial places

G1 has no nodes, so its eleven-group regrouping is a build note.

## Other decided calls
- G2 rental is out of scope: only owned property is shown, and the "buy or rent" step is dropped.
- G2 pages are buying guides. Location and listing filters are shown as guidance text and are never built into URLs.

## Data defect found (noted, not fixed)
In data/nodes.tsv, the leaf names of G2.2.1, G2.2.2, G2.2.4, G2.3.3 and G2.3.7 kept memo markdown and were split at a colon (for example "Houses** (kind axis"). They need a tools/ fix.

## Calls on thin evidence (provisional)
- The gravel bike kind kept, and its merge condition.
- All boat, caravan and aircraft quality markers: no specialist shop was fetched.
- J.D. Power VDS: no J.D. Power page was fetched (it is named only on the AAA page).
- CCCA scale class.
- The groupset ladders.
- The band edges of `length_band`.
- `carrycot` (P14).
- From memory: the RICS condition ratings 1–3, AS 4349 numbering, and the ANSI A119.5 / NFPA 1192 numbers.
- All C13 parts platforms (memo candidates, unsourced).
- G2 burial and commercial kinds: no HOL evidence.
- The memo's microcar, open keelboat and cruising houseboat († until HV_G1).
