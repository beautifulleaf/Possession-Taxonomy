# AUDIT H3 Adult Objects (cold audit, doubles as harvest retry)

Data file: verify/work/BRANDLAYER/AUDIT_H3.json. Raw fetches: verify/work/BRANDLAYER/AUDIT_H3_tmp/ (xbiz_wiki.md, 20xx-xbiz-*.md, raw/*.md).

## Accuracy
25 harvest brands sampled (random.seed(7)), each checked against its raw src page: 25 shown, 25 claims supported, **0 wrong**.
Layer is the real problem: trade awards were counted as quality.
- XBIZ: winners "are voted for by XBIZ staff, industry colleagues and participating organizations" (XBIZ Awards, Wikipedia). Standing, cultural.
- ETO (UK): "All winners were chosen by the industry, using a unique democratic voting system" (erotictradeonly.com/about-eto). Standing.
- AVN O Awards: the page states no jury. The "Industry Voting" block (Outstanding Product Line, etc.) is voted outright. In the product categories, winners thank "the voters" (Aneros). Standing.
- AVN Awards pleasure/retail categories: no jury stated. Standing.
- Juried (quality): Red Dot (LELO ENIGMA Wave/SILA, Satisfyer Sunray by Eis GmbH, TENGA UNI/AERO, iroha) and German Design Award (Satisfyer Orca).
16 relabels from premium to cultural (see `relabel`).

## Caveats resolved
- Rocks-Off: the AVN press page is now fetched (ETO Best Pleasure Products Brand). XBIZ wiki gives src2: Male Sex Toy 2012, Hand Solo. Kept, as cultural.
- Oxballs, Coco de Mer and Mister B are each the same company as its A1 row. Cross-tag them.
- Homonyms: Masque → "Masque (adult products)" (vs Masque Milano, H4). Blowfish → "Blowfish (sex shop)" (vs Blowfish Malibu, A2). Lovely → qualify. Orion → "Orion (erotic retailer)". Pipedream, Shunga and Eden Fantasys have no clash.
- **Register error:** the NJOY row merges the vape maker (J10) with the steel-toy maker (H3). Split it.
- Aliases: Cyberskin = Topco Sales line; ElectraStim = Cyrex; Eis GmbH = Satisfyer group; iroha = Tenga; epi24 = Womanizer; Standard Innovation = We-Vibe; WOW Tech = group.

## Additions (195 rows)
61 cultural, 1 premium, 133 listed.
- **XBIZ 2020-2024 and Europa 2020/2022:** New York Toy Collective, ZALO (China), Crave, Nu Sensuelle, Lora DiCarlo, CB-X, Chakrubs, OmYONI, Fort Troff, Love Not War, WOW Tech, Mister B, Gangbangster, Pauline et Margot, Spiritus & Co.
- **From the XBIZ wiki:** Bathmate, Topco Sales, Empire Labs, Warm.
- **Retail winners (sellers):** Hustler Hollywood, PinkCherry, Lion's Den, Castle Megastore, Museum of Sex, Passage du Désir, La Clef des Charmes, Orion, Stag Shop.
- **Wikipedia sex-shop category rows missed by the harvest:** El Asira, Priape, Pulse and Cocktails, Romantic Depot.
- **Japan** (ja Wikipedia Category:大人のおもちゃ): Toys Heart, 4woods, Level-D, G Project, Men's Max, Teppen, Arte Tokio, Top Marshal, Life Doll, WINS, SENSBODY.
- **Germany** (de Wikipedia): Amorelie, EIS, Boutique Bizarre.
- **Spain:** Platanomelón, Diversual. **Denmark:** Sinful. **India:** IMBesharam, ThatsPersonal.
- **Premium:** Vixen Creations, an early silicone maker, attested by a peer-reviewed article.
- **WhatToy directory** (coordinator-supplied; not re-fetched by the auditor): 121 rows listed plus 12 qualified homonyms. 34 were dropped as out of scope: lubricants and enhancers (H1), condoms (H2), Cleis Press, Mötley Crüe/Motörhead licences, Dreamgirl lingerie. 33 more match existing rows.
- **WhatToy in_other checks:**
  - Cross-tag (same company): Hitachi (it made the Magic Wand, which Vibratex distributes), Durex, Kiki de Montparnasse, Oxballs.
  - Same company but out of H3 scope: Astroglide, Stud 100.
  - Different companies, given qualified new rows: Aria, Colt, Edge, Gläs, Mojo, Nexus, Revolver, Rowdy, Sola, Swan, Wellness, Zero Tolerance.
  - Vixen = Vixen Creations.

## Regions (4)
- China: "70% of the world's sex toys" are made there (Wikipedia). No brands named on the page.
- Japan, love dolls: Orient Industry.
- Guangdong (Zhongshan): WM Doll. Renown is weak.
- Japan, onahole makers: Toys Heart, which first branded the product in 1999.

## Blind spots
- No independent pages this round for:
  - Central and Eastern Europe, Southeast Asia, Africa and Latin America makers. The industry is concentrated, and regions are not quotas.
  - Rends/Vorze, Magic Eyes and NLS (own site or retailer listings only).
  - Body-safe review sites with test methods.
- No ETO yearly winners list was found.
- The 2025 XBIZ XMA page fetched empty, and Strategist/Wirecutter were not re-fetched.
- Several WhatToy names may be product lines (Pipedream: Icicles, King Cock, Fetish Fantasy; XR: Master Series, Trinity Vibes; Doc Johnson: Vac-U-Lock; Fleshlight: FleshJack). The verifier should merge them once a page confirms.
