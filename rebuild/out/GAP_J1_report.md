# GAP_J1 report (Meat & Poultry)

Files edited: out/J1.json, out/J1_brands.json (backups in work/GAP_J1/bak/). validate.py --v3: OK (168 kinds, 448 entries; was 343). About 40 fetches, logged in work/GAP_J1/sources.tsv. No Firecrawl.

**Closed**
- Loose models: none remained.
- Coverage line: all 80 kinds with entries now end with "Complete", "Covers" or "No complete list exists; follows ...". The 71 "Not claimed complete" lines were rewritten.
- Regional dry-cured hams 21 -> 26 and Smoked raw ham 6 -> 6: List of hams read whole. Both now Complete (24 of 24 dry-cured rows outside Italy and Spain, plus Kraški pršut and Barrancos; 6 of 6 smoked rows). Added Jambon de Luxeuil, Savoie, Périgord, Pyrénées and Smithfield ham. Cooked, glazed and city hams, York, Wiltshire, Bradenham and Prague (Cooked ham) and Limerick (a method) are out of scope.
- Spanish names: Pernil Cerretà (Jamón serrano) and Chistorra de Navarra (Fresh chorizo) added from fetched pages.
- Black pudding 13 -> 52 (Blood sausage page read whole; Covers 52 of about 110 rows, the rest are aliases, sweet puddings, non-sausage dishes). Kielbasa & smoked sausage 13 -> 25 (Polish PGI/TSG, Hungarian and Ukrainian rows). Head cheese 10 -> 47 (Covers 47 of about 105). Bratwurst: Complete, 10 of 10. These four have `xg` country and a `g` on every entry.
- Japanese wagyu: Maesawa added; Covers 11 of about 320 brands (page names 12).
- Meat box: 8 UK premium butchers (mob.co.uk, 2021) and The Kosher Express (2011) added; 11 -> 19 entries.
- New kinds: Lamb neck, breast & saddle (Cut of lamb), Water buffalo, Yak, Emu.
- `role`: Kobe beef origin (page: first wagyu to gain a reputation, 1860s); Prosciutto di Parma landmark (page: "most prized").
- Market panels: Brazil 36 % of world chicken exports 2024 (USDA projection via Datamar); India about 43 % of buffalo meat (no year on page); world meat output 2023 (China 97.5, US 47.5, Brazil 31.6 Mt).
- Brand register +18: halal certifiers (JAKIM, BPJPH 2017, MUIS, IFANCA, ICCV, AHF, CHB, HMC, SANHA), UK butchers, The Kosher Express.

**Remains (two attempts each)**
- Current UK premium-butcher and kosher-delivery rankings: Delicious (403) and Good Web Guide (403) blocked, listed in firecrawl_deferred.md; searches "best kosher meat delivery online 2026", "best online butchers UK 2026" gave vendor pages only. The Kosher Express page is from 2011.
- Australian approved halal body list: 503 twice; deferred. A certifier register is therefore a handful of named bodies, not complete.
- Market shares for about 20 markets: searched "global meat processors market share UK beef pork Brazil China", "UK bacon sausage market share", "Brazil chicken exports share"; only the facts above were fetched. WH Group's page gives no share.
- Origin/landmark badges for other kinds: Spam, Prosciutto pages state no first or best-selling claim.
- Cut of poultry reference not fetched; yak and emu rest on brief Wikipedia passages.
- eAmbrosia (French, Spanish, UK registers) needs script; deferred.
