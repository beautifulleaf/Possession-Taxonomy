# DPW1_F6 report (F6 Natural History & Specimens)

Inputs: the HV_F6_1 and HV_F6_2 "missing kind?" lists, split into single items, plus shop categories from the fetch logs. There is no DPMK_1_F6 file. Outputs: verify/out/DPW1_F6_kinds.tsv (52 rows) and verify/out/DPW1_F6_moves.tsv (1 row).

## Task 1: missing kinds
new_kind 41, covered 9, attribute 1, other_category 1, named_form 0. Each new id is the next free one under its parent (checked against data/kinds.tsv and TREE_F6_map.tsv), and each source is a harvester URL logged full or partial.
- **Fossils (14):** F6.3.1.06–.15, the invertebrates (coral, bivalve, brachiopod, bryozoan, crustacean, insect in rock, gastropod, graptolite, nautiloid, sponge). F6.3.2.04 mammal, F6.3.2.05 reptile/amphibian/synapsid, F6.3.3.02 plant fossil, F6.3.4.02 trace fossil.
- **Minerals (11):** F6.1.3.02 halite, F6.1.4.07 hematite, F6.1.4.08 fulgurite, F6.1.5.03 azurite, F6.1.5.04 aragonite, F6.1.8.01 turquoise, F6.1.9.03 beryl, F6.1.9.04 topaz (specimen), F6.1.9.05 lapis lazuli, F6.1.9.06 serpentine, F6.1.9.07 feldspar.
- **Rocks (2):** F6.2.1.04 rhyolite, F6.2.1.05 porphyry.
- **Meteorites (3):** F6.4.08 HED, F6.4.09 mesosiderite, F6.4.10 achondrite. The last gives aubrites and ureilites a home. The section 14 chondrite split stays.
- **Shells (4):** F6.6.1.03 murex, F6.6.1.04 volute, F6.6.4.03 dried starfish, F6.6.5.01 brachiopod shell. That one needs the **new leaf F6.6.5 Brachiopods**, a new value on the animal axis, because brachiopods are not molluscs.
- **Preserved (6):** F6.7.1.03 reptile mount, F6.7.2.06–.08 bird, reptile and fish skull, F6.7.2.09 articulated skeleton, F6.7.2.10 claw or tooth.
- **Parts (1):** F6.10.04 specimen frame case, for one specimen. A frame for several is B1.

Covered: ureilite and snake skeleton go to the new kinds. Fetal pig, dissection specimens and wet specimens go to F6.7.6.01. Bird eggs, acrylic specimens, amber insects and sea fan go to their existing kinds.

Attribute: heart and pyramid shapes (`presentation`). Other category: stone lamps (B3) and carved animals (F2 or B4).

FossilEra's unnamed "about 200 further species" are left to the harvest.

## Task 2: named forms (1 of 74 flagged)
NF-F6.5.1.01-002, Cognac diamond, moves to F6.5.1.02 fancy-colour diamond.

Kept as they are:
- Champagne diamond, which spans D-to-Z and fancy grades.
- The blue topaz trade names and star ruby (memo 4b: trade names that describe a look).
- Ruby in fuchsite and ruby-zoisite. These are rock materials, but there is no better kind; noted for the next pass.

No row is a maker, a shop or a line.

## Task 3: navigation
I confirm R-116: the way in is the natural class, then species or taxon, then the class's quality markers.
- FossilEra's category pages attested 30 of 40 kinds by class.
- GemSelect lists by species, Conchology by family, Skulls Unlimited by specimen type.
- The only makers found are seven storefront dealers, so neither brand nor scene can lead.

Sketch:
1. Minerals · Fossils and amber · Meteorites · Gemstones and pearls · Shells and coral · Rocks and teaching sets · Preserved specimens · Element samples · Domes, stands and frames.
2. Minerals species A–Z, with Strunz as a secondary grouping. Fossils by organism leaf. Gems: diamonds, coloured, pearls. Shells by animal leaf, including Brachiopods. Preserved specimens by preservation leaf. Meteorites, elements and displays go straight to their kinds.
3. Kinds, then named forms with markers and facets.

## Rules applied
C2(a)–(b), C11, S3/K-9, K-77, K-80, F-4, F-25, R-58, R-116, memo 4b and section 14.

## Resting on † claims
- The Cognac move rests on the Argyle and GIA brown scales; no page was fetched for it.
- Fulgurite's place in Oxides assumes Strunz files lechatelierite there. This is provisional, like the quartz placement (F-24).
- Bird, reptile and fish skulls are not named in the skullsunlimited.com log line, so HV_NK should confirm them.
