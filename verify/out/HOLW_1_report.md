# HOLW_1: display groups and quality markers, wave 2 and wave 3 (offline)

Outputs: verify/out/HOLW_1_groups.tsv (314 rows), verify/out/HOLW_1_markers.tsv (196 rows). Helpers: verify/work/HOLW_1/build.py, markers.py. Level-1 groups follow each proposals row and DPW1 decision. Level-2 groups regroup stored kinds the way shops shelve them. No kind ids are changed (R-58).

## Groups (L1 / L2 / kinds grouped)
- **A2** 7/11/63: the style tab, which DPW1 opens first. Sneakers are split into lifestyle and performance. Boots are grouped by style, not shaft height; the engineer boot sits under western and biker. The scene and use doors are generated views.
- **A3** 9/20/57: the piece tab. Level 2 is the memo leaves. The waist chain shows under anklets and body chains. The house, bridal and vintage views sit beside.
- **A4** 9/16/74: luggage, packs (everyday and school, travel, outdoor), handbags by silhouette, and the rest.
- **A5** 10/14/60: the watch worlds. Independents and Fashion have no members; they are maker_class views. Clocks are grouped by placement and parts by the object they serve.
- **B9** 10/21/122: parejos and figurados, pipes and pipe tobacco, vapes, oral, cannabis, hookah, accessories. Kinds marked "also shown" stay in their main display group.
- **E3** 11/28/122: the 11 groups from the proposals row.
- **H1** 10/32/119: the memo leaves. Hair tools are split into appliances and manual tools.
- **J7** 6/20/116: added Porter and stout (G-J7-28), Traditional and mixed beers (G-J7-29) and Mixed wine cases (G-J7-27). Aromatised wine shows with fortified.
- **J1** 10/16/87: the P-J1 ids became G-J1. Game now includes other meats. Added Mixed meat boxes (G-J1-10).
- **J5** 9/25/134: the proposals ids. G-J5-32 Syrups has no stored kinds, so it holds only node J5.7.3.
- **J6** 4/16/41: the proposals ids.

**Kinds left out: none.** Every stored kind sits in exactly one level-2 group, or in a level-1 group that has no level 2. A script checked this.

## Markers
- **J7 18, J1 12, J5 24, J6 19:** these are the stored rows, kept word for word. The only change is J1's P-J1-n ids, re-pointed to G-J1-n.
- **New rows**, all taken from the proposals rows' quality_markers and cited to that row and its sources:
  - **A2 (19):** construction ladder, leather, last, grade line and value for shoes and boots; sneaker and running markers.
  - **A3 (10):** the 4Cs and certificate, fineness ladder, solid against plated, signed against unsigned.
  - **A4 (15):** fabric, construction, hardware, design and warranty for luggage and packs; five luxury-handbag markers.
  - **A5 (10):** movement through value retention, with the COSC and Superlative accuracy ladder and the crystal ladder. ISO 6425 is on dive watches.
  - **B9 (24):** cigar score ladder and the cigar markers; pipe tobacco, pipes, the cannabis COA, and vapes, e-liquids and pouches (provisional).
  - **E3 (22):** guitars, pianos, synths, interfaces, and the band and orchestral build ladder.
  - **H1 (23):** skincare and makeup, blade shaving, hair dryers, toothbrushes, and fragrance (provisional).

No markers were written for clocks, umbrellas, baby carriers, sunglasses or the H1 groups 8 to 10, because the proposals rows give none.

## Notes
- Some rows apply to the whole category, for example "(all watch groups)" on G-A5-1. They sit on the first level-1 group, as J5 already does.
- Kinds a DPW1 pass proposed but that are not yet stored (for example the new A3 kinds) are not grouped.
