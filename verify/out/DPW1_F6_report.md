# DPW1_F6 report (F6 Natural History & Specimens)

Inputs: the "missing kind?" lists of HV_F6_1 and HV_F6_2, split into single items, plus shop categories from the "gave" column of both fetch logs. No DPMK_1_F6 file exists. Outputs: verify/out/DPW1_F6_kinds.tsv (52 rows) and verify/out/DPW1_F6_moves.tsv (1 row).

## Task 1: missing kinds
Decisions: new_kind 41, covered 9, attribute 1, other_category 1, named_form 0.

New kinds. Each takes the next free id under its parent, checked against data/kinds.tsv and TREE_F6_map.tsv. Each source is a harvester URL logged as full or partial.
- **Fossils (14):** F6.3.1.06–.15: coral, bivalve, brachiopod, bryozoan, crustacean, insect in rock, gastropod, graptolite, nautiloid, sponge. F6.3.2.04 mammal; F6.3.2.05 reptile, amphibian or synapsid; F6.3.3.02 plant fossil; F6.3.4.02 trace fossil.
- **Minerals (11):** F6.1.3.02 halite; F6.1.4.07 hematite; F6.1.4.08 fulgurite; F6.1.5.03 azurite; F6.1.5.04 aragonite; F6.1.8.01 turquoise; F6.1.9.03 beryl; F6.1.9.04 topaz (specimen); F6.1.9.05 lapis lazuli; F6.1.9.06 serpentine; F6.1.9.07 feldspar.
- **Rocks (2):** F6.2.1.04 rhyolite; F6.2.1.05 porphyry.
- **Meteorites (3):** F6.4.08 HED; F6.4.09 mesosiderite; F6.4.10 achondrite (other groups). Without the last kind, an aubrite or ureilite has no home. Section 14's chondrite split is unchanged.
- **Shells (4):** F6.6.1.03 murex; F6.6.1.04 volute; F6.6.4.03 dried starfish; F6.6.5.01 brachiopod shell. The last needs a **new leaf, F6.6.5 Brachiopods**: it adds a value to the stated animal axis, since brachiopods are not molluscs.
- **Preserved specimens (6):** F6.7.1.03 reptile mount; F6.7.2.06–.08 bird, reptile and fish skull; F6.7.2.09 articulated skeleton; F6.7.2.10 claw or tooth.
- **Parts (1):** F6.10.04 specimen frame case (holds one specimen; a Riker tray that holds several is B1).

Covered: ureilite and snake skeleton go to the new kinds. The fetal pig, dissection specimens and Wet Specimens go to F6.7.6.01. Bird Eggs go to F6.7.2.03, acrylic specimens to F6.7.5.01, amber insects to F6.3.5.01, and sea fan to F6.6.4.01. Attribute: the presentation shapes (hearts, pyramids). Other category: stone lamps (B3) and carved animals (F2 or B4).

FossilEra's "about 200 further mineral species" were not named one by one, so they stay as harvest work.

## Task 2: named forms (1 of 74 flagged)
- NF-F6.5.1.01-002 Cognac diamond moves to F6.5.1.02 Fancy-colour diamond. This is a move_kind, not a drop.
- Kept:
  - Champagne diamond: it spans D-to-Z and fancy grades.
  - The topaz trade colours (London, Swiss, Sky Blue): look-describing trade names stay named forms (memo 4b).
  - Star ruby.
  - Ruby in fuchsite and ruby-zoisite. These are rock materials more than ruby, but no better kind exists, so they are noted for the next pass.
- No row is a maker, a shop or a line. Every row is a variety, trade name, taxon or named fall, as the "none" maker role requires.

## Task 3: navigation
I confirm R-116: the way in is the natural class, then the species or taxon, then the class's own quality markers. The harvested data agrees:
- FossilEra's three category pages attested 30 of 40 kinds by class.
- GemSelect opens by species A to Z.
- Conchology opens by family, and Skulls Unlimited by specimen type.
- The only makers met are seven storefront dealers, so a brand or scene entry has nothing to stand on.

The first three levels:
1. Minerals and crystals · Fossils and amber · Meteorites and impact glass · Gemstones and pearls (unset) · Shells and coral · Rocks and teaching sets · Taxidermy, bones and preserved specimens · Element samples · Display domes, stands and frames.
2. Minerals: species A to Z, with the Strunz class as a secondary grouping. Fossils: invertebrates, vertebrates, plants, trace and microbial, resin. Gems: diamonds, coloured, pearls. Shells: gastropods, bivalves, other molluscs, brachiopods, echinoderms and coral. Preserved: mounts, skeletal, pinned, pressed, encased, fluid. Meteorites, elements and displays open straight onto their kinds.
3. Kinds, then named forms (varieties, taxa, named falls, trade names) with markers and facets (presentation, size class, locality, treatment).

## Rules applied
C2(a)–(b), C5(b), C11, S3/K-9, K-77, K-80, F-4, F-23, F-25, R-58, R-116, R-119, memo sections 4b and 14, and the TREE_F6 precedence rules.

## Decisions resting on † claims
- The move of Cognac diamond rests on the Argyle and GIA brown-colour scales. No page for it was fetched.
- Fulgurite in Oxides assumes that the Strunz scheme files lechatelierite there, which was not read. The placement is provisional, like the quartz-family placement (F-24).
- The fetch log does not name the skull groups (bird, reptile, fish) on skullsunlimited.com, so the attestation pass (HV_NK) should confirm each one.
