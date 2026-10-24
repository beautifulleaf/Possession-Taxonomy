# DPW1_C7: C7 Farm & Forestry Equipment decision pass (offline)

## Task 1: missing kinds (24 items)
Sources: the HV_C7_1 and HV_C7_2 lists, split into single items; "gave"-column shop categories; and generic types that the harvested rows show. There is no DPMK_1_C7 file.

Decisions: covered 12, new_kind 8, other_category 2, named_form 1, attribute 1.

**New kinds** (R-58: next free id, checked against data and TREE_C7_map). Each has a harvester URL logged full.
- C7.1.3.03 Four-track tractor (9RX, Quadtrac, Xerion TRAC TS, 8RX). The crawler kind needs two full tracks and the articulated kind needs wheels, so neither definition holds these.
- C7.2.2.07 Stone picker and collector.
- C7.3.06 Seed potato cutter.
- C7.8.3.03 Cattle race and handling system (K-101).
- C7.8.5.02 Livestock EID panel reader.
- C7.10.1.08 Front ballast weight (suitcase weights).
- New leaf C7.10.3 Forest machine fittings, with C7.10.3.01 Forestry crane and C7.10.3.02 Log grapple and rotator (S3: no job away from the host machine).

**Other decisions**
- Other category: post-and-rail pens go to C8 (K-195); sawmills go to C1 (step 12).
- Named form: the check basin former is a non-maker form under the bund plasterer C7.2.2.05 (C11, region IN).
- Attribute: parlour stall layout.

## Task 2: named forms (25 of 471 flagged)
- **to_line 9:**
  - STX Steiger (covers two kinds), Rainstar, CHOPSTAR, AEROSTAR, Balfor BF E range, JD 9000 Series forage harvesters, Claas Lexion and Jaguar: each covers several models, per the row's own notes.
  - Titan Economy Series (a price tier).
- **drop 1:** Big Dutchman "Feed Cart", which is a generic type word.
- **move_kind 15:**
  - 5 four-track rows go to C7.1.3.03, pending attestation.
  - 4 Aebi Terratrac rows go to the slope tractor C7.1.1.05.
  - Forestry misfilings from Mascus categories: JD 1270G and Ponsse Ergo 6WD go to the harvester; JD H270 and Komatsu C144 go to the harvester head; Link-Belt 240 LX and Kobelco SK300LC-10 go to the forestry excavator.
- **Line fixes with no move action:** the JD 8 Series and 9 Series lines should add C7.1.3.03.
- **Maker fix with no action:** the Clipex and Nugent crushes sit under M-teemore-engineering, but the page does not name who owns those brands.
- Model families that differ only by size (Juwel, Pronto, BB12) stay named forms (C3).

## Task 3: navigation
This confirms R-116: the main way in is **the type of object, by the job the machine does**. Maker role stays "owner".
- Every catalogue the harvest used opens on machine type: Landwirt.com categories, Mascus forestry categories, AllMachines, and Kuhn's menus (hay-forage, mowers, tedders, rakes).
- 471 named forms spread over 113 makers and 88 kinds. Kuhn (78), Deere (27), Krone (24) and Waratah (23) lead, but no maker dominates the category.
- A maker tab for tractors and forestry machines stays as a side view.

Sketch of the first three levels:
1. **What job?** Tractors and carriers · Soil tillage · Seeding and planting · Spreading, spraying and irrigation · Harvesting · Hay and forage · Grain and post-harvest · Livestock and dairy · Forestry machines · Loaders, tyres and tractor fittings.
2. **Which family?** For example, Tractors and carriers → Wheeled · Articulated 4WD · Tracked · Two-wheel · Carrier. Livestock → Milking · Cooling · Handling · Weighing · Identification · Shearing · Slaughter · Poultry · Feeding.
3. **Which machine?** For example, Wheeled → Standard · Row-crop · Narrow orchard and vineyard · High-clearance · Slope · Forestry.

After that come filters (size class, PTO hp, hitch category, carrier, working width), then maker and model. Views: size class (cross-links to C2), crop, vintage, precision.

## Rules applied
R-58, R-70 a, R-116, R-118 a, R-119, R-122 c; C2 (a, b, d), C3, C6, C9, C11, C12 a, C14 b, S3; K-101, K-195, K-194; memo §3, §4b, §14; TREE_C7 precedence.

## † claims and weak evidence
- **Model knowledge, not on a fetched page:** the forestry move_kinds (1270G, Ergo 6WD, H270, C144, 240 LX, SK300LC-10), the four-track layout of 9RX, 8RX, Quadtrac and Xerion, and Terratrac as a slope tractor. Aebi's page URL does say "slope-tractors".
- **Weak pages:**
  - The seed potato cutter rests only on the harvester's report of the Dewulf page; its "gave" column does not name it.
  - The panel reader rests on the report's XRP2 note.
- **Tree kinds still unattested:** C7.1.3.02 half-track, C7.1.4.01 two-wheel, C7.2.2.05 bund plasterer. The Deere India page (check basin former) may attest a bund-forming implement.
