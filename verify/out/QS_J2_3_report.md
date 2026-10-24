# QS_J2_3 report (Seafood Watch since Feb 2024; MCS Good Fish Guide)

Rows: tier_entries 17 (SCH-mba-seafood-watch, test_version 2026-10-24). 11 from the National Seafood Guide page (dated 2026-02-28), 3 from the Maldives tuna search page, 1 from the sutchi catfish search page, 1 from the Pacific herring search page. The national-guide rows are 2026-02-28 and the live-page rows 2026-10-24.
Other tables: none. No new makers or named forms.

Method: the Seafood Watch site is JavaScript, so everything came through Parallel fetch. The live search page (1944 results, 10 pages) gives no pagination links, so only guide-linked searches were fetched: Maldives tuna, sablefish, sutchi catfish, Pacific herring. The Fall/Winter 2024 national guide was superseded by the Monterey Bay Aquarium National Seafood Guide page (2026-02-28). The Popular Seafood Guide page (2026-01-18) gave no new tier rows. Regional guide pages were not fetched.

Changed or new ratings (old > new):
- Sablefish, pots (national guide): Best Choice > Good Alternative (the 2026 guide lists sablefish without a gear split; the live search shows all rows Good Alternative).
- Yellowfin tuna, Maldives (pole-and-line, handline): none > Best Choice (new, April 2026).
- Yellowfin tuna, Pacific pole-and-line: none > Best Choice.
- Yellowfin tuna, Indian Ocean pole-and-line or free school, and Atlantic pole-and-line, troll or free school: none > Good Alternative.
- Pacific bluefin (troll, pole-and-line, free school): none > Good Alternative.
- Farmed rainbow trout, US: none > Best Choice. Chile Avoid is no longer in the national guide.
- Atlantic salmon farmed from Canada, Chile, Norway or Scotland: none > Avoid (guide level).
- Squid Chile or Peru Good Alternative; spiny lobster US or Mexico Good Alternative; mackerel Chile, Japan or Morocco Good Alternative (Ecuador dropped).
- Eel, imported farmed: none > Avoid. Basa/pangasius imported and Vietnam sutchi ponds: Avoid. Octopus Indonesia, Morocco or Mauritania: Avoid (country-specific, same tier as before).
- Pacific herring BC set gillnets (roe): none > Good Alternative.

Dropped from the 2026 national guide (no row written): Atlantic cod gillnet/longline/trawl Avoid, king crab Best Choice, wild oysters, pollock, imported-harpoon swordfish, Honduras for shrimp and tilapia.

Skips: skipjack, albacore, bigeye, bass, catfish, flounder, sole, mahi, Chilean seabass (no J2 kind); 3 Maldives skipjack rows counted as skip 1.

MCS Good Fish Guide: stored rows already come from the guide fetched 2026-10-24 (April 2026 update; next October 2026). No newer edition exists, so no rows. The index page gave summary ratings only. WebFetch got 403 on mcsuk.org.

Failed or partial pages: seafoodwatch.org by WebFetch (empty JS shell); Maldives story body text not returned; mcsuk.org 403.
No product missing a kind.
