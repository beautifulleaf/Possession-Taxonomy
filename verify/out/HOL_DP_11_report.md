# HOL_DP_11 report (J1 J2 J3 J4; holistic organisation, stage 2 proposal)

Offline Opus pass on HOL_EV_11 (33 evidence rows), the memos, data/ tree and kinds, and the stored designations, varieties and grading_scales tables. Applies R-115 a: product grouped as shops group it, then what makes the best, who vouches, the named best. Outputs: HOL_DP_11_proposals.tsv, HOL_DP_11_groups.tsv (J2, J3, J4: 86 groups, all 434 kinds placed once), HOL_DP_11_markers.tsv (64 rows). The tool check in verify/work/HOL_DP_11/build.py confirms the coverage. No kind ids change.

**J1 Meat & Poultry (no built tree).** Way in: the animal for fresh meat and the product type for made meats. Whole Foods and Crowd Cow open by species; REWE lists Wurst by type. The nine level-1 groups (P-J1-1 to 9) are only a display layer over memo Candidate B. Groups 1-6 are the J1-A animal leaves, and groups 7, 8 and 9 are J1-B, J1-C and J1-D. Best markers:
- Beef: marbling and grade (USDA, JMGA/BMS), then age, breed, feeding and ageing.
- Ham: the Ibérico colour label (breed and diet), then cure time and DOP.

Maker role stays none (R-115 b), with a wagyu-by-origin view. Flags:
- The tree is not loaded.
- No J1 grading scales or meat breeds are stored.

**J2 Fish & Seafood.** The way in is how the fish is sold (fresh and frozen, smoked, cured and dried, tins and jars, roe and caviar, fish cakes). Fresh and frozen then splits into the ten counter groups. Tins split by tin type, with cannery and caviar-house tabs (R-115 a). Freshness leads (Woolworths SA; EU Extra > A > B). Next come wild or farmed, sustainability (Seafood Watch, MSC), size and the species ladders: tuna grade and fat cut, oysters, and caviar (species, then grain 000 > 00 > 0). Flags:
- Store the counter group as a kind attribute (52 finfish sit in one leaf).
- The tuna fat-cut named forms are missing.
- There is no caviar grain-grade scale and no MSC, ASC or Seafood Watch scheme rows.
- Fresh anchovy and cuttlefish kinds are missing.

**J3 Dairy, Eggs & Alternatives.** The way in is the product family, with cheese by family (Mons, Butlers, Stiftung Warentest, lecker.de). There are nine cheese display groups. What makes a cheese best: milk provenance, traditional make and rind, maturing, condition and flavour. The trusted signals are PDO, World Cheese Awards medals, the consortium marks (Parmigiano, Grana Padano, Comté) and USDA grades. Eggs are judged by housing (EU code 0 to 3), then grade. Plant milks go by base, use and ethics score; infant formula has no tier. Maker role is none, with R-115 b. Side views: by maker for cheese and butter, award winners, and goat and sheep. Flags:
- Goat and sheep cheese should be a view, not a level.
- J3.4.6.08 holds 76 designations.
- There are no award scheme rows.

**J4 Fruit & Vegetables.** The way in is fruit, vegetables, salad and herbs, or mushrooms (Instacart; brand and organic are only filters). Then produce family, then the kind. What makes it best: variety, ripeness and season, freshness, then class. The class scales are UNECE/EU Extra > I > II, USDA, CFIA and the Japanese prefectural grades. RHS AGM marks the best varieties. Maker role is none (club cultivars only). Flags:
- There is no season column (R-115 a).
- The varieties table needs taste, use and keeping fields.
- There are only 7 herb kinds.
- Sea vegetables sit under fungi.

Caveat: the evidence was thin where retailer pages were blocked. Some markers rest on the stored tables and memo sources, and each row says so.
