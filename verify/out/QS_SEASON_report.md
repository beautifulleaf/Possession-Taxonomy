# QS_SEASON report

Output: verify/out/QS_SEASON_attributes.tsv, 360 rows (357 kind, 3 variety: NZ Gala, Braeburn, Granny Smith). No other tables. Fetch log: verify/work/QS_SEASON/fetched.tsv. Generator: verify/work/QS_SEASON/build.py.

Rows by source region:
- northern; UK 92: Hubbub month lists (produce, 53 kinds; no peak marked, so lists of months in season) and Direct Seafoods chart (fish; dark cells = abundant and best value).
- northern; US 66 (USDA SNAP-Ed guide as reproduced by US Foods, peak months); US (Mississippi) 41 (MSU Extension); US (Northern California) 11 and US (Virginia) 2 (fish).
- southern; New Zealand 68 (5+ A Day chart, plentiful months only).
- southern; Australia (Western Australia) 29 (LiveLighter, season quarters converted to months) and Australia (NSW) 5 (Sydney Fish Market article).
- northern; Japan (Tohoku, Sendai basis) 36 (MAFF, quarter-level only) and Japan (Shimane) 10 (prefectural fish list).

Method notes: chart PDFs (Direct Seafoods, 5+ A Day, US Foods, Foodwise, LiveLighter) came back unreadable from WebFetch; I read the locally saved copy of each fetched PDF as a rendered image and sampled cell colours, then checked a few rows by eye. Colour classification was not hand-verified for every cell. Where a source gave sub-items not in varieties.tsv (Navel/Valencia, melons, cucumbers, potatoes) the months are unioned on the kind and the note says so.

Failed or unusable fetches: olivemagazine seasonal calendar (grid icons unmappable), foodanddrink.scot PDF (graphic only), Funabashi (table flattened), Kanagawa fish calendar (symbols empty), PickYourOwn AU (403), FRDC 1997 seafood calendar (403), satofull (403), Maine Sea Grant (503), SFM summer article (404), MSU Michigan guide (empty), snaped.fns.usda.gov (DNS). betterfood.co.uk fetched but too ambiguous, not used.

Gaps: no Australian or New Zealand fish chart fetched (only barramundi Feb-May wild appeared in a search excerpt, not a fetched page); no Japanese fruit chart by month (quarter-level only); Japanese fish only for items Shimane lists. No Japan/AU rows for most J2 shellfish.

Skips (no kind in J2/J4; "missing kind?"): missing kind?: parsnip, swede, celeriac, Jerusalem artichoke, salsify (root vegetables); missing kind?: chard / silver beet, pak choi, Asian greens; missing kind?: gooseberry, greengage, damson, redcurrant, quince, elderberry; missing kind?: broad bean; missing kind?: komatsuna, mizuna, napa cabbage, Welsh onion (negi); missing kind?: Japanese sea bream (madai), yellowtail (buri), conger eel. Skipped fish with only light (should be available) cells: anchovies, ling, skate, sea trout; no J2 kind for skrei, brown shrimp, sprats, dabs, whiting, pouting. Non-listed items from other categories were not added.
