# DP_A1K report

## Task 1: 47 decisions

13 listed candidates plus 32 garments from the GD/REG batch TSVs (no GD/REG report .md files exist).

| Decision | Rows |
|---|---|
| new_kind | 9 |
| named_form | 16 |
| covered | 12 |
| attribute | 4 |
| other_category (E2) | 6 |

**New kinds** (next free id under R-58):
- A1.1.1.05 scrub top
- A1.1.1.06 team jersey
- A1.3.1.10 co-ord set
- A1.3.2.06 firefighter suit
- A1.4.1.22 casual jacket (blouson)
- A1.4.2.10 raincoat
- A1.4.2.11 fur coat
- A1.4.2.12 lab coat
- A1.7.10 braces

**Definition changes:**
- A1.2.2.07 becomes "Trousers (tailored or casual)".
- Overcoat widens to any coat below the hip not covered elsewhere.
- Work pants names scrub trousers; shell jacket names softshell.

**Re-ties:**
- Bandhgala rows move from sherwani to blazer (length rule).
- Fur-coat rows move to the fur coat.

## Task 2: storefront rule (ready as an R-item)

A maker counts as a clothing brand when it sells clothing under its own label. A retailer that sells its own labelled clothing gets supply_role "retail own-label" and counts. A store whose stored notes or source show it only resells other makers' goods, with no own label named, is a storefront. Storefronts include department stores, multi-brand and concept stores, select shops, marketplaces, importers and second-hand shops. A storefront gets supply_role "retailer (multi-brand)", stays in the ledger, and tools/coverage.py leaves it out of the brand count (as R-91 does for manufacturers). maker_class "storefront or marketplace" alone does not exclude a maker; when unsure, it stays a brand.

**Results:**
- **100 storefronts:** GB 47, US 13, DE 12. None falls below half its expected share.
- **1,768 own-label:** 1,746 already in class "retail own-label" plus 22 from notes (Musinsa, Zalando).
- **69 kept as brands:** storefront-class rows with empty or vague notes (Macy's, Mytheresa). Listed in verify/work/DP_A1K/unsure_storefront_class.tsv.

## Resting on unverified claims

- Union suit, cambusciu, hotpants, Capri pants, kebaya, chacabana: no page in the outputs shows them.
- Fur coat as a kind rests on the CNPP fur ranking and maker notes.
- Firefighter suit rests on the CNPP firefighter ranking as REG_CN3 recorded it.
- Team jersey, co-ord set, braces: level not shown on a retailer category page.
- Storefronts are judged from notes only; a department store with an own label flips to own-label once a page shows one.
