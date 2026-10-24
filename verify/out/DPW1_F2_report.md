# DPW1_F2 report (F2 Art)

Inputs: HV_F2_1 "missing kind?" lists (9 items split) plus 10 from the fetch log and harvested rows; no DPMK_1_F2 file. Outputs: verify/out/DPW1_F2_kinds.tsv (19 rows) and verify/out/DPW1_F2_moves.tsv (3 rows).

## Task 1: missing kinds
Decisions: new_kind 4, named_form 5, attribute 4, covered 5, other_category 1.

New kinds take the next free id (data/kinds.tsv and tree map checked); each has a fully fetched harvester URL.
- **F2.1.14 lacquer painting**: no binder kind covers lacquer. Singulart (France) and Zhongyi (China) both sell it as its own class (C11).
- **F2.4.4.04 ambrotype**: a collodion positive on glass, sold by name (1stDibs).
- **F2.3.5.04 embossed print**: an impression in relief made mainly without ink (Motokawa; AAT lists it apart).
- **F2.8.03 paper cut**: the image is cut, not pasted, so it is not a collage (Artsy).

The other decisions:
- Named forms: Polaroid (F2.4.5.02), luminogram (F2.4.5.01), Murano glass (F2.5.5.01), stumpwork (F2.6.02), root carving (F2.5.3.01).
- Covered: graffiti (F2.1.11), photomontage (F2.8.01), digital print (F2.3.6.01), needlepoint (F2.6.02), Shoushan stone seal (F2.7.02).
- Attributes: gilding, enamel paint, jacquard, hanging scroll.
- Other category: taxidermy goes to F6 (key step 7).

## Task 2: named forms (3 of 77 flagged)
All three are drops:
- "Gobelin tapestry": gobelin is the Dutch word for tapestry, so it is an alias (C9).
- "Verdure tapestry": verdure is a subject, and subjects are attributes.
- "Lu-graph": a printing system, so it is an attribute (C10).

No row needs to_line or move_kind. The Swarovski rows are models inside the six lines already stored. No row is really a maker or a shop.

## Task 3: navigation
I confirm R-116. The way in is by type of object (discipline, then medium or technique), with the artist as a co-equal tab. Every catalogue that worked opens by medium: Singulart's filters, 1stDibs material pages, Motokawa's technique list, and RiseArt's Drawings > Charcoal. The maker leads only inside figurines, where shops go manufactory → series.

The first three levels:
1. Paintings · Prints · Photographs · Sculpture and figurines · Drawings · Textile and fibre art · Calligraphy · Collage, mosaic and mixed work, with an Artists tab and the "Original or edition?" filter beside them.
2. Kinds for the sub-families without leaves (lacquer painting joins Paintings, paper cut joins Collage). Leaves for Prints, Photographs and Sculpture, plus a Figurines group.
3. Kinds inside each leaf, then named forms and artists. Under Figurines: manufactory → line → model (Swarovski → Idyllia → Hedgehog).

## Rules applied
C2(a)–(c), C9, C10, C11, R-58, R-62, R-70, R-116, the TREE_F2 precedence rules, and memo sections 6, 7 and 14.

## Decisions resting on † claims
- Lacquer painting's second region is Zhongyi, cited in the memo but not fetched in HV_F2_1.
- Murano glass and Polaroid were † named forms in the memo; harvested pages now back them.
- No page showed vitreous enamel plaques, so they stay a "missing kind?" for a later harvest.
- No page states the material of the Royal Doulton figures HN1–HN20. They stay at F2.5.4.03 until a page shows otherwise.
