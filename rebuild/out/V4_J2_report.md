# V4_J2 report: J2 Fish & Seafood named-entry pass

Files changed: out/J2.json, out/J2_brands.json (backups in work/V4_J2/bak/). J2_moves.json and J2_renames.json unchanged. validate.py --v3: OK (171 kinds, 296 entries). Fetch budget: about 38 calls.

## Loose models
All 233 former models (`m`) are gone. Result: 51 became protected or regional-name entries, 136 became brand or maker entries (the products are versions), 13 were removed as generic descriptors or MSC-fishery labels (for example "Scandinavian gravad lax", "Florida stone crab claws", "Banco Chinchorro and Sian Ka'an Spiny Lobster"). Entries before → after: 155 → 296. Every kind with entries now has nl, sel (with a coverage line), xg and a `g` section on each entry.

## Market layer
Brand entries carry own, tier, cty and own_y only where a fetched page gives them: Chicken of the Sea (Thai Union, 2000), John West (Thai Union, 2010), Rio Mare (Bolton), StarKist (Dongwon, 2008), Century Pacific, Ortiz (family), Sea Chicken (Hagoromo, National champion), Gomes da Costa (Grupo Calvo), Aldi Süd (own label). Other brands read "owner not stated" with no tier.
Tinned & jarred fish `ms` (10 facts): US canned seafood 2022 (StarKist 33 %, Bumble Bee 25.5 %, Chicken of the Sea about 10 %, private label 13.9 %, artisanal about 11 %; Euromonitor via FoodNavigator, value or volume not stated); Bolton 38 % of Italian canned fish (2016); Jealsa first and Calvo second in Spain (Alimarket 2018, no percentages); Thai Union largest tuna canner (2010); Princes largest UK tinned-food supplier (2013).
Fresh & frozen fish `ms`: nine US online seafood services as listed by an AOL article of 3 April 2026. It is an editorial list, not a scored ranking.
Brand register: eight owners added (Thai Union, Bolton, Dongwon, FCF, Century Pacific, Princes, Grupo Calvo, Hagoromo).

## Not done, and why
- EU PDO/PGI fish list: eAmbrosia is JavaScript-only, Wikidata holds only 2 usable items under P1435, and no fetchable complete list was found. Protected names stay as harvested (about 50 plus earlier entries); coverage lines say the total could not be counted. Protected-name entries use the kind's existing source page, which for some (carp PGIs) is a retailer page; they need a register source later.
- Species canon with FAO names: not rebuilt; the existing species tree was kept.
- Certification register (MSC, ASC, BAP, Seafood Watch) as tags: no tag field fits and no register page was fetched.
- Premium fishmonger lists: Delicious magazine and Saveur returned 403 (Firecrawl also failed); the CNET/AOL 2025 URL was 404. No UK list.
- Tiers for Ramón Peña, Nuri, José Gourmet, Birds Eye, Findus and others: no fetched owner page. Market panels cover US, Italy, Spain, UK and global only, not 20 markets; Japan and Thailand shares were not found.
- Roles (origin or landmark) were not added.
