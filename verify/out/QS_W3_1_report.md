# QS_W3_1 report

Rows written (verify/out/QS_W3_1_*.tsv; check_batch.py: 0 unlogged sources): schemes 10, tier_entries 33, standards 30, standard_values 6, grading_scales 1, named_forms 39, makers 13, maker_kinds 25. No issuers, no new kinds.

Schemes and entries: Red Dot Product Design 2025 (scheme, 0 entries: winners are in an Excel attachment); Consumer NZ bed linen (1 entry); Consumer Reports cookware (1); Food Network cookware sets 2026 (8); Which? test score/Best Buy, Which? reliability survey, Which? bathroom brands (schemes only, scores behind membership); RedditRecs robot vacuums Oct 2026 (8); LPU belt ranking (scheme only); Consumer Reports security cameras 2026 (15).
Standards: FSC, GECA, OEKO-TEX 100, GoodWeave, GOTS, EN 1307, SCA Certified Home Brewer (5 values), EU energy labels (washers, dryers), ENERGY STAR, AHRI, NEEP, NSF/ANSI 42/44/53/55/58/62/177, UL 72, UL 1037, UL 687, EN 1143-1, TS 007, EN 1303 (1 value, ABUS X60), EN 14604, EN 50291-1, AS 3786, ASTM F1004, EN 3-7. Grading scale: Chairish rug weaving environment.

Failed or blocked pages: RTINGS how-we-test (members only, no method), Stiftung Warentest result tables (paywalled), Which? Best Buy lists and brand scores (members), Consumer Reports rating-methods (403), Safelincs (403), EUR-Lex summary (empty), iTeh EN 1930 (generic page).

Left out, with reason:
- B1 design-classic authenticity class: no fetched page defines reissue or reproduction (originalicons defines only licensed and replica).
- B1 ISO 12947 Martindale: ISO page gives the test, no class bands.
- B5 knife-line ladder: no maker page fetched; iv class not in the scheme scale.
- B6 RTINGS scheme: no method page readable.
- B6/B7 Stiftung Warentest vacuum, washer, heat pump: already SCH-stiftung-warentest-test, whose kinds_served lacks B6.1.1, B6.3.1, B7.1.1.16 (owner should extend it); grades locked, so no entries. Weights seen: vacuums 45/30/15/10, washers 40/20/15/15/10, heat pumps 70/25/5.
- B7 JIS APF, EU SCOP, AHRI-per-product values; B8 EN 15659, EN 1047-1, BS 3621, Sold Secure levels, BHMA A156, EN 1930 (no defining page fetched).
- EN 1930, TS 007 2-star and EN 3-7 ratings (13A, 34B) stored as pass/fail or star steps only.

Skips to other categories: 0. Unplaced products: LPU reference locks (cylinders of unstated type; missing kind?: high-security lock cylinder) and Figmint/other cookware makers carry no country.

Notes: pass/fail standards use the single step "Certified". Dates unstated on the Consumer NZ and CR cookware pages, so stale_after is blank there.
