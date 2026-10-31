# VERIFY H3 Adult Objects (Opus verifier)

Data file: verify/work/BRANDLAYER/VERIFY_H3.json (status complete). Helpers: VERIFY_H3_tmp/ (build.py, texts.py, pages.json, raw/).

## Sources
- **Fetched this pass** (raw full_content):
  - en Wikipedia categories: Sex toy manufacturers, Sex shops, Vibrators
  - ja Category:大人のおもちゃ; de Kategorien Unternehmen der Sexindustrie and Sexspielzeug; de Orion (Erotik)
  - AVN 2025 and 2026 O Awards, and the AVN Rocks-Off press page
  - Red Dot (ENIGMA Wave, Sunray, TENGA UNI) and German Design Award (Orca)
  - t-online (Fun Factory), ET Retail, MarketingDirecto, Vogue Scandinavia, Información 2024 (Diversual), electrastim.com terms
- **Re-read, not re-fetched:** the auditor's raw saves from today (AUDIT_H3_tmp).
  - XBIZ Awards wiki, and the XBIZ 2020-2024 and Europa 2020/2022 winner pages
  - El Asira, Priape, Pulse and Cocktails, Romantic Depot, Hitachi Magic Wand, Sex doll, Sex toy industry in China, Toys Heart (ja)
  - Japan Times, and the Sexualities article
- **WhatToy:** the owner's paste (verify/retail/whattoy.txt) counts as the fetched page. Not fetched again.
- **ABC 2022 (Diversual):** fetched empty. Información 2024 is the second source (src2).

## Result
- 259 rows checked, 0 not shown.
- By tier: cultural 123, quality 5, seller 3, listed 128.
- Regions: 11. One has renown (China). Ten do not.

## Audit applied
- **Trade votes:** 16 harvest "premium" rows relabelled cultural. These are AVN, XBIZ and ETO wins, which are industry votes:
  - Hot Octopuss, Jimmyjane, Clandestine Devices, COTR
  - Cyrex (now ElectraStim), Laid, The Stockroom, Evolved Novelties
  - Like A Kitten, Our Erotic Journey, Maia Toys, Maxtasy
  - Honey Play Box, Snail Vibe, Luxxxe, Rocks-Off
- **Quality (juried):**
  - LELO: Red Dot 2024, ENIGMA Wave.
  - Satisfyer: Red Dot 2022 Sunray (manufacturer Eis GmbH) and German Design Award (Orca).
  - TENGA: Red Dot 2024, TENGA UNI.
  - Also quality: Fun Factory (t-online: high-quality products, medical silicone) and Vixen Creations (Sexualities article: handmade silicone, early maker).
- **Rocks-Off:** cultural. src is the AVN press page (ETO 2015, "voted for"). src2 is the XBIZ wiki (2012, Hand Solo).
- **Cross-tags (same company):** Oxballs, Coco de Mer and Mister B (A1 rows); Hitachi (made the Magic Wand); Durex (H2); Kiki de Montparnasse (A1).
- **Homonyms (qualified, 17):**
  - Masque (adult products), Blowfish (sex shop), Lovely (vibrator brand), Orion (erotic retailer), NJOY (steel toys)
  - The 12 WhatToy names that belong to different companies: Aria, Colt, Edge, Gläs, Mojo, Nexus, Revolver, Rowdy, Sola, Swan, Wellness, Zero Tolerance.
  - The auditor also gave a qualifier to 20 generic WhatToy words (Avant, Neo, Luxe and others). These match no register row, so they are not flagged as homonyms.
- **Aliases (one row each):**

  | Row | Aliases |
  |---|---|
  | Topco Sales | Topco, Cyberskin (XBIZ wiki: "CyberSkin Twerking Butt (Topco Sales)") |
  | ElectraStim | Cyrex, Cyrex Ltd. Cyrex is the trademark owner and sells under ElectraStim, so the row takes the sold name. |
  | Satisfyer | Eis GmbH. The EIS (eis.de) shop keeps its own row because it trades under its own name. |
  | TENGA | iroha (AVN 2025: "Tenga/Iroha") |
  | Womanizer | epi24 |
  | We-Vibe | Standard Innovation |

  WOW Tech is a parent group, not a brand sold under its own name. It is recorded as a rel note on the We-Vibe and Womanizer rows, with no row of its own.
- **Product lines merged:** each was confirmed on the XBIZ wiki.
  - Into Pipedream Products: Icicles, King Cock, Fetish Fantasy, Pipedream Extreme Toyz.
  - Master Series → XR Brands.
  - Vac-U-Lock → Doc Johnson.
  - FleshJack → Fleshlight.
- **Not confirmed, kept as separate listed rows:**
  - Trinity Vibes, Uprize, Optimale, Kink Industries, Arcwave
  - Fantasy C-Ringz, Fantasy For Her, Fantasy X-Tensions
- **Other WhatToy duplicates merged as aliases:** Adam and Eve, BMS, Cal Exotics, Clone A Willy (Empire Labs), HUSTLER, Lovely Inc., NassToys, NSNovelties, Shots and others.
  - Two of these are probable merges, not confirmed on a page: Vixen → Vixen Creations, and CB Chastity Devices → CB-X.
- **Out of scope (not added):**
  - Lubricants and enhancers (H1)
  - Condoms (H2)
  - Cleis Press
  - Mötley Crüe and Motörhead licences
  - Dreamgirl lingerie (A1)
- **Diversual:** second source is Información 2024 ("una referencia en el sector"). Kept cultural on press standing.
- **Sinful, IMBesharam, ThatsPersonal:** tier set to seller. Their pages name them as sellers of adult toys but give no encyclopedia or register standing.

## Regions
- **China — renown true.** Quote: "the largest in the world, with 70% of the world's sex toys being manufactured there". The page names no brands.
- **Renown false, quote present but at maker level only:**
  - Japan (love dolls): Orient Industry.
  - Guangdong (Zhongshan): WM Doll.
  - Japan (onahole makers): Toys Heart, origin claim only.
- **Renown false, the 7 harvest regions:** their sources are category or award lists with no renown statement. The brands kept are those shown on each source; these were dropped as not shown:
  - Satisfyer (Germany)
  - Orient Industry (Japan)
  - Je Joue (UK)
  - Evolved Novelties (North America)
  - Come as You Are and Venus Envy (Canada)
  - SVAKOM and Hismith (East Asia)
  - Bijoux Indiscrets (Western Europe)
- No brand carries a region field.

## Index cleanup
- **NJOY:** the register row mixes the vape maker NJOY (J10) with the stainless-steel toy maker (H3). Split it. This verify supplies the H3 half as "NJOY (steel toys)", a WhatToy row marked homonym.
- **Satisfyer and EIS (eis.de):** both belong to one company group (Eis GmbH / Triple A). Add a rel between the two rows; do not merge them.
