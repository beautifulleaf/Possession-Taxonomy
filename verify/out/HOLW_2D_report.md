# HOLW_2D: display groups and quality markers, wave 3 (offline)

Outputs: verify/out/HOLW_2D_groups.tsv (321 rows), HOLW_2D_markers.tsv (167) and HOLW_2D_groups_changes.tsv (12 J7 rows). Helpers are in verify/work/HOLW_2D/. Level 1 follows the proposals row and the DPW1 sketch; level 2 regroups the stored leaves the way shops shelve them. Ids are flat (G-<code>-<n>), and no kind id changes (R-58).

The E1 and G2 rows replace their old groups.tsv sets. Neither code had markers, so nothing needed re-pointing. C1 is not in this batch; its stored groups already place all 220 kinds.

## Groups (L1 / L2 / kinds)
- **E1** 9/32/118: construction, vehicles, puzzles, outdoor and parts are split into shop shelves.
- **E2** 17/63/206: sports in shopper order. Cycling and Equestrian show their kinds directly. The empty Caving leaf is left out.
- **E4** 10/31/130: arrows, bolts and archery parts sit under Bows, and pellets and CO2 under Air guns, as the shops shelve them. Armour is split into body armour, historical armour and shields.
- **G1** 11/38/145: motor boats are grouped by use. Parts (G1.5) has no kinds yet and holds only its node.
- **G2** 6/15/66: new group "Leisure, energy and parking land" (G2.1.8).
- **H2** 12/58/157: vision is split three ways; peak flow has its own group.
- **H3** 8/11/59: five groups show their kinds directly.
- **J7**: move_members on 12 existing groups places 33 unplaced kinds, including J7.3.1.06, J7.4.04 and J7.4.06. Each row gives the full member list.

**Kinds left out: none.** A script checked every stored kind against exactly one terminal group. G1, G2 and H2 kinds loaded during the run, and the final run includes them.

## Markers (from the quality_markers in proposals.tsv; no new facts)
- **E1** 20: safety is a gate on every group, plus kit, figure-format and game-component markers.
- **E2** 27: certification gate, fitness machines, boot and shoe order, and rackets by player level.
- **E4** 31: knives (tang ladder), bows, rifles, NIJ armour levels, nihonto papers, HEMA makers.
- **G1** 19: cars (reliability, Euro NCAP stars), bicycles and motorcycles. Boats, caravans and aircraft are provisional.
- **G2** 12: homes (tenure and EPC ladders), land (ALC grades), factory-built homes, burial places.
- **H2** 23: blood-pressure monitors, mobility, supplements, sports nutrition, medicines, hearing aids.
- **H3** 35: a body-safe material ladder on every product group, powered and size markers, and restraints.
- **J7**: stored markers kept; group ids unchanged, so no re-pointing.
