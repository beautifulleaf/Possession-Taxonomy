# HOLW_1: display groups and quality markers (offline)

Outputs: verify/out/HOLW_1_groups.tsv (314 rows) and verify/out/HOLW_1_markers.tsv (196 rows). Helper scripts are in verify/work/HOLW_1/. Level 1 follows the proposals row and the DPW1 decision. Level 2 regroups stored kinds the way shops shelve them. No kind ids change (R-58).

## Groups (L1 / L2 / kinds)
- **A2** 7/11/63: style tab. Sneakers split into lifestyle and performance; boots grouped by style. Scene and use doors are views.
- **A3** 9/20/57: piece tab, on the memo leaves. The waist chain shows with anklets.
- **A4** 9/16/74: luggage, packs, handbags by silhouette, and the rest.
- **A5** 10/14/60: watch worlds. Independents and Fashion are empty maker views.
- **B9** 10/21/122: the ten shopper groups. Parejos and figurados split.
- **E3** 11/28/122: the proposals' 11 groups.
- **H1** 10/32/119: memo leaves. Hair tools split into appliances and manual tools.
- **J7** 6/20/116: added G-J7-27 (mixed wine), G-J7-28 (porter and stout) and G-J7-29 (traditional and mixed beer).
- **J1** 10/16/87: P-J1 renamed G-J1. Added G-J1-10 (mixed boxes).
- **J5** 9/25/134: proposals ids. G-J5-32 (syrups) has no stored kinds yet.
- **J6** 4/16/41: proposals ids.

**Kinds left out: none.** A script checked that every stored kind sits in exactly one terminal group.

## Markers
- **J7 18, J1 12, J5 24, J6 19:** the stored rows, unchanged. J1 is re-pointed from P-J1 to G-J1.
- **New rows**, from the proposals rows' quality_markers:
  - **A2 (19):** construction, leather, last, grade line and value; sneaker and running markers.
  - **A3 (10):** the 4Cs, certificate, fineness ladder, plated or solid, signed or unsigned.
  - **A4 (15):** fabric, construction, hardware, design and warranty; luxury handbags.
  - **A5 (10):** movement, accuracy ladder, crystal ladder; ISO 6425 for divers.
  - **B9 (24):** cigar score; pipes and pipe tobacco; cannabis COA; vapes, e-liquids and pouches, provisional.
  - **E3 (22):** guitars, pianos, synths, interfaces; band build ladder.
  - **H1 (23):** skin and makeup, blade shaving, hair dryers, toothbrushes; fragrance provisional.

Groups with no proposal markers have none: clocks, umbrellas, sunglasses and the H1 groups 8 to 10. Category-wide rows sit on the first level-1 group and are labelled "(all ... groups)".
