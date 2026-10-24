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
- G1 (10): assist, size_class (scheme-qualified), propulsion, body_substyle, geometry, construction, rig, hull_count, length_band, carrycot.
- G2 (11): build_history, house_form, floor_position, construction, propulsion, units_in_building, managed_for, and four burial attributes.
- Listing values (location, price, bedrooms, mileage) are never stored (C16).

## Needs (DPH_G_needs.tsv, 27 rows)
- G1 (16): Euro NCAP and J.D. Power IQS/VDS (class ii); eBay Exotics (vi); CCCA (iii); Polaris and groupset ladders (iv); three design standards; six parts-fit platforms.
- G2 (11): grading scales EPC, RICS and ALC; seven standards (inspections and factory-built build codes); China office grades (iii).

## Groups (DPH_G_groups_changes.tsv, 20 rows)
G2: six level-1 groups by node id (houses and flats; park, mobile and floating homes; land and farms; garden buildings and outbuildings; commercial buildings; burial places) with 14 level-2 groups. G1 has no nodes, so its eleven-group regrouping is a build note.

## Other decided calls
- G2 rental is out of scope: only owned property is shown, and the "buy or rent" step is dropped.
- G2 pages are buying guides. Location and listing filters are shown as guidance text and are never built into URLs.

## Data defect found (noted, not fixed)
In data/nodes.tsv, the leaf names of G2.2.1, G2.2.2, G2.2.4, G2.3.3 and G2.3.7 kept memo markdown and were split at a colon (for example "Houses** (kind axis"). They need a tools/ fix.

## Calls on thin evidence (provisional)
Gravel bike kept and its merge condition; boat, caravan and aircraft markers (no specialist shop fetched); J.D. Power VDS (no J.D. Power page fetched); CCCA class; groupset ladders; length_band edges; carrycot (P14); from memory: RICS ratings 1-3, AS 4349, ANSI A119.5 / NFPA 1192; all C13 parts platforms; G2 burial and commercial kinds (no HOL evidence); microcar, open keelboat, cruising houseboat († until HV_G1).
