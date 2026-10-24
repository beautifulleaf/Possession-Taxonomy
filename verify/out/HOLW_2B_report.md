# HOLW_2B report: display groups and markers, wave-3 C categories (offline)

Outputs: verify/out/HOLW_2B_groups.tsv (322 rows), verify/out/HOLW_2B_markers.tsv (121 rows). Helper scripts are in verify/work/HOLW_2B/. Ids: level 1 is G-<code>-1..n and level 2 is G-<code>-101 upward. Level-2 members are kind ids, and level-1 members are the leaf or sub-family nodes they draw on. No kind id was changed (R-58).

## Groups (level 1 / level 2 / kinds placed)
- C1: 9 / 39 / 220 of 220. This replaces the 48 old C1 rows. Level 2 is still the leaves, as the proposals row says. C1.4, C1.5 and C1.6 are joined in one group, and C1.10 and C1.11 are one level-2 group each.
- C2: 10 / 38 / 134. Lawn comes first. Shelf groups were made for the leafless C2.1, C2.4, C2.8 and C2.10. The aerator joins the scarifier, and the pool test kit joins water treatment.
- C3: 7 / 23 / 137. Peperomia, pilea, begonia and selaginella (leaf C3.1.11) are shown under Houseplants as "Small foliage houseplants". This is display only.
- C4: 13 / 46 / 217. Leafless crafts (papercraft, model-making, candle and soap, glass) get shelf groups. Clay is split into kiln clays and air-dry, polymer and modelling clays.
- C5: 8 / 25 / 104. Staples sit with staplers. Label tape and C5.5.8 sit under Calculators & office machines.
- C7: 10 / 38 / 110. Tillage, seeding, crop care, harvesting, hay, forestry and C7.10 fittings get shelf groups. Leaf C7.1.4 (Two-wheel) has no stored kind, so it has no group.
- C8: 11 / 45 / 185. Level 2 is the memo leaves, and packing gets two shelf groups.

**Kinds left out: none.** The script checks that every stored kind of each code sits in exactly one level-2 group, with no duplicates.

## Markers (rows; group they sit on)
- C1 (12): powered-tool markers on Drilling & driving (from the drill tests; meant to apply wherever the Power toggle is on), hand-tool steel ladder and machine duty class on Shaping, accuracy on Measuring.
- C2 (14): mower markers on Mowers, hand cutting markers on Secateurs, PPE/PPFD on grow lights, frost-hardiness on pots (provisional).
- C3 (16): named-form markers on Garden plants and Houseplants. The buying checklist is a page-only row (C16). Collector markers sit on tropical foliage, plus fruit and seed markers.
- C4 (18): artist colours, yarn, sewing machines, clay cone, leather, beads.
- C5 (18): fountain pens (7), paper (3), ink (5), calculators, shredders, desk "preference and build only".
- C7 (15): tractor markers (8), implement power and width on four implement groups, forestry markers (provisional, by analogy).
- C8 (28): timber, tiles, paint (8), screws and bolts, cells. Plumbing, electrical, adhesives and fuels carry a "spec match only" row, since there is no HOL evidence for them.

Ladders are written best first. Evidence cites the proposals row (quality_markers) and the sources or memo it names; no new facts were added.

## Notes
- The prompt names E1, G2, J7, J1, J5 and J6. None of them is in this batch, and markers.tsv has no C rows, so all markers come from the proposals rows. Only C1 had existing groups.
- C5 has 104 stored kinds.
