# DPW1_B6 report: B6 Cleaning & Laundry (offline, wave 3)

## Task 1: missing kinds (50 rows)
Inputs: both harvest lists, split, plus four types from the fetched.tsv "gave" column. No DPMK_1_B6 file exists.

- **Counts:** new_kind 29, covered 11, attribute 7, other_category 2, named_form 1.
- **Other categories:** push sweeper to C2 (step 29); rubber gloves to A1 (step 17).
- **Named form:** Finish glass protector, under B6.4.03.

New kinds (all go to HV_NK; dryer sheet and crease spray have no logged page, so their source_url is empty):
- B6.1.1.09 ash vacuum; B6.1.3.09 electric mop, .10 string mop
- B6.2.1.05 cleaning wipe; B6.2.2.04 toilet brush; B6.2.4.08 drain unblocker; B6.2.5.08 soleplate cleaner
- B6.3.4.04 peg bag; B6.3.5.04 detergent sheet; B6.3.6.08 dryer sheet, .09 crease-release spray
- B6.4.05 dishwasher cleaner, .06 dishwasher freshener; B6.5.1.05 sack holder
- B6.6.1.06–.10: hose, brush roll, motor, wheel, wand
- B6.6.2.05–.13: drain pump, drum paddle, carbon brush, heater element, door lock, condenser container, vent hose, pedestal, stacking kit
- New leaf B6.6.4 Ironing-board parts: .01 ironing board cover

Notes:
- "Wet mop" names both B6.1.3.02 and the string mop (an alias clash).
- B6.3.6.07 should read "spray or wash-in".
- Twin-tub now has sellers in two regions (Japan, LG Africa), so its level holds under C11. The bathroom dryer and bedding dryer stay provisional.

## Task 2: named forms (20 of 244 flagged)
- **to_line (7):** Beko EnergySpin, Tide Plus A Touch of Downy, Tide Free and Gentle, Fairy Original, Fairy Platinum, Febreze Fabric, Addis eco.
- **drop (13):** 11 names that only repeat the kind with a maker, size or attribute added (OXO caddy, Novax, CleanFreak, Libman mop, squeegee and five brushes), plus 2 variants (Libman Large broom, Doc Johnson Natural).
- **move_kind:** none.
- **Makers or shops filed as named forms:** none.

Noted: several lines cover one kind only (Kärcher WD, Tineco FLOOR ONE); C2(d) would make them named forms.

## Task 3: navigation
I confirm R-116: **type of object, grouped by cleaning job.**
- The best harvest sources were shop category pages, organised by type.
- No maker dominates: 78 makers own 244 forms; the top one, Kärcher, has 12 %.
- Consumable brands were harvested as lines.

The vacuum brand tab stays a side view.

View:
1. **Level 1:** Vacuums and floor machines; Mops, brooms and floor tools; Washing machines and dryers; Irons, steamers and drying; Laundry detergents and care; Household cleaners; Cloths, sponges, brushes, window and steam; Dishwashing products; Bins and bin bags; Bags, filters and spare parts.
2. **Level 2:** the leaf (for example, Vacuum cleaners and Floor machines).
3. **Level 3:** the kind by form (upright … backpack, ash), with use-case filters at this level.

## Rules applied
R-35, R-58, R-116, R-122 c, C2, C3, C10, C11, S3, boundary 16, memo section 14.

## Resting on † claims
- The Beko, Tide and Fairy line spans come from product knowledge.
- The soleplate cleaner and sack holder are not confirmed in the gave column.
- The glass protector as a one-maker product.
