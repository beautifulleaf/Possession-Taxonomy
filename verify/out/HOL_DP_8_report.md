# HOL_DP_8 report (F1 to F6; evidence HOL_EV_8)

This was an offline proposal pass. It wrote verify/out/HOL_DP_8_proposals.tsv (6 rows) and no groups file, because none of F1 to F6 is on the built list. F2 and F4 have trees in data/nodes.tsv but no kinds in data/kinds.tsv, so their groups are mapped to node and memo ids in `level2_note`. All 47 evidence rows are cited. The retailer evidence is thin: Waterstones, Fnac, HMV, Amazon, Saatchi, APMEX, NGC, Discogs and Numista were blocked, and no community page was fetched. Calls marked provisional rest mostly on the memos.

**F1 Media & Publications (provisional).** Way in: the carrier and format, as at Acoustic Sounds, AbeBooks and Hugendubel. Genre-led shops (Tower, Disk Union) are not followed, because BRIEF bars genre. Ladder: carrier > format > best edition or pressing, then condition. Signals: Goldmine grades, with disc and jacket graded separately, and Disk Union's S to C scale as a platform label. Maker role stays owner, with a labels and imprints tab. Flags:
- a `mastering` attribute
- a decision on UHQR
- a maker class for pressing plants
- a component field for two-part grades
- an audiobooks view

**F2 Art.** Way in: medium, as at Artfinder, Singulart and eBay.de, with the artist as a co-equal tab. Maker role stays way in. Ladder: discipline > technique > whether the work is an original, an edition or a reproduction. Quality runs authenticity > condition > artist. For prints it runs edition size > signature > technique. CAA proof rules become a classification row. Condition and certificates of one work are never stored (C16). Flags: make `authenticity_class` a first filter; tradition stays a tag; nihonga's kind status is still provisional.

**F3 Coins, Stamps, Medals & Trading Cards.** Way in: the collecting field (Huntington), then how the item was issued (Otakaraya), then grade. Country is a filter only. Signals: Sheldon 70, NGC and PCGS; PSA, BGS, SGC and CGC for cards; stamp scales for centering and for gum, which are now fetched. Maker role stays owner, with tabs for mint or refiner and for card brand. Flags: TCG cards are E1, but the grader scales serve both F3.8 and E1; Stempelglanz needs an alias row.

**F4 Religious & Ceremonial Objects.** Way in: the role the object plays in the rite (Rakuten Kyoto, Exotic India, Holyart). Tradition is an optional first filter, never a level. What makes the best differs by object:
- scrolls: the scribe's certification first
- prayer beads: use, then material, then craftsmanship
- prayer mats: padding

Maker role stays owner, with a tarot publisher tab. Flags: religious jewellery is A3 (cross-link only); attributes for rug padding and for treated bead material; scribes need maker rows. Thin, so provisional.

**F5 Documents & Personal Records (provisional).** Way in: the type of paper (Richmond, AbeBooks, Yahoo). The memo's function leaves are regrouped into eight display groups. Signals: the ALS to cut-signature document classes as a classification row; no grade scale exists. Maker role stays none. Flags:
- a `print_process` attribute for postcards
- whether an autograph letter becomes a named form of letter
- a candidate kind for printed advertisements

**F6 Natural History & Specimens.** Way in: the natural class, then the species (FossilEra, Peltram, Gem Rock, GemSelect). What makes the best has its own order for each class:
- minerals: colour > form > condition > luster > locality > size
- fossils: authenticity > completeness > restoration disclosed
- gems: identity > treatment > origin > visual quality

Signals: lab reports from GIA, SSEF, Gübelin and AGL, and the Meteoritical Society names. Maker role stays none, except for labs and taxidermy studios. Flags: whether F6.5 has a gemstone kind for cut opal; a value list for treatments.
