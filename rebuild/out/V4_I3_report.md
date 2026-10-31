# V4_I3 report: named-entry and market pass, I3 Subscriptions, Memberships & Online Services

Files changed: out/I3.json, out/I3_brands.json (250 bare owner/brand names added), out/I3_renames.json (empty). I3_moves.json unchanged. Backups and script (apply.py, finalize.py): work/V4_I3/. Sources log: work/V4_I3/sources.tsv (12 fetches). validate.py --v3: OK (93 kinds).

## Market-first kinds (entries before -> after)
- Video streaming 24 -> 71. Every video row read from Wikipedia's List of streaming media services (first 100,000 of 219,000 characters), sections by home market, owner, tier, country; live-TV and sports rows stay in their kinds. Tail of the page not read.
- Music streaming 16 -> 28. Wikipedia Comparison of music streaming services, 28 of 35 rows (other seven are radio, in the radio kind). Apple Music Classical is a version.
- Cloud storage 12 -> 23. Wikipedia Comparison of file hosting services, 21 of 31 in scope plus pCloud and Sync from the earlier pass; object stores and file lockers cut.
- AI assistants 5 -> 6 (Grok added); paid plans are versions. DeepSeek left out (no paid plan fetched).
- Mobile 35 -> 45. Consumer brands of the 25 largest operators (Wikipedia), plus kept national operators and MVNOs; tier from owner structure.

## Other kinds
All remaining loose models (`m`) and ranges (`r`) became entries (about 480 in total, plan names as versions, kind source as `s`, `own` where the maker was stated). Services & staff: 17 household and staff kinds lost their company lists and are commodity kinds; jet cards and concierge keep their earlier entries plus converted ones. Every kind with entries has `nl` and `sel`.
Delivery links: meal kits -> J5, veg box -> J4/J3, producer club -> J7, curated box -> J8, replenishment -> J9. New kind Halal and kosher meat delivery (15 sellers from the HalalSpy guide, link to J1); no kosher seller was found on a fetched page.

## Market facts (department `ms`)
- US streaming share, JustWatch: Netflix 20 % (Q4 2025), Prime Video 19 %, Disney+ 14 %, Apple TV 9 % (2025). Subscriber counts above 50 million from the Wikipedia list (undated).
- Music: Spotify nearly a third of 818 million subscriptions, Tencent Music with Cloud Music 21.4 % in China (MIDiA, Q4 2024); paying users per service from the Wikipedia comparison (undated).
- AI: Similarweb web-visit shares, September 2026: ChatGPT 57.5 %, Gemini 25.7 %, Claude 9.8 %, DeepSeek 3.5 %, Grok 2.0 %, Perplexity 0.9 %, Copilot 0.6 %.
- Mobile: subscriptions of the 25 largest operators with the page's dates (China Mobile 1,003.9 million, Sep 2024) and US carriers, Q2 2026 (Verizon 147.0, T-Mobile 143.3, AT&T 121.4 million).

## Not sourced
No cloud-storage share figure; no UK, German or other national mobile shares; no role badges (origin/landmark); no Craft & indie tier; owner for Discovery+, MGM+, Tidal and several others blank; own_y not stated by any page; tiers for regional cloud services blank; plan versions only for AI, bundles and loyalty tiers. Wikidata label query was noisy (homonyms) and used only as a cross-check. Brand register additions have no country or year.
