# V4_E2_OUTDOOR report (second pass)

Part file: rebuild/out/E2_parts/OUTDOOR.json (about 400 KB, validates OK, 199 kinds, 1,038 entries, 5 roles). Replaces the five outdoor departments; no renames or moves. First-pass copy kept in work/V4_E2_OUTDOOR/bak/OUTDOOR.v1.json.

## What changed
- One named level per kind. In the line kinds (rods, reels, lures, flies, tents, hammocks, mats, bags, stoves, harnesses, cams, belay devices, skis, snowboards, boards, wetsuits, kites, wings, wheels) an entry is a model line; SKU-level models became versions. Models with a per-model page (523) group by line name into line entries; models with no per-model page (398) are either versions of a line confirmed on a fetched range page or sit as versions under one maker entry ("<Maker> <kind> models", 84 of these) on the kind's retail category page. No loose models, no unsourced lines. Ranges (r) dropped.
- Model `d` templates removed (643 entries have no `d`; only facts from fetched pages kept).
- Commodity kinds (88 kinds with entries removed: camp furniture, tarps, bivvy bags, water filters, hunting aids, fish finders and alarms, helmets, chalk, slings, pulleys, ascenders, caving kit, goggles, masks, paddles, life jackets, ski helmets and goggles, avalanche kit, cycling clothing and helmets, trainers) keep only an origin entry (CamelBak, Jumar, Morey Boogie) per the icon rule. 579 named entries and models removed; the full list is rebuild/work/V4_E2_OUTDOOR/removed.json (by kind).

## Canons built from fetched pages (counts in each kind's sel)
- Artificial fly 172 patterns: Wikipedia Artificial fly plus Orvis dry, wet, streamer, bass and panfish, nymph (UK page 1 of 2) and 12 must-have pages. Orvis dry and streamer pages were truncated by the fetch (about 105 and 80 listed); not complete. Wikipedia List of fly patterns is 404.
- Reels: Shimano 18 spinning lines (Tackle Warehouse) and 5 baitcasting (Bassmaster); Daiwa 20 spinning and 7 baitcasting; Penn 5 spinning and 2 multiplier; Abu Garcia 3 spinning and 5 baitcasting (abugarcia.com).
- Tents: MSR 6, Nemo 6, Big Agnes 9, Hilleberg 16 lines (REI, MEC, Campmor, Nordic Outdoor). Packs (Osprey, Gregory, Deuter) were fetched (Osprey: Atmos, Aether, Exos, Kestrel, Farpoint and others; Gregory: Baltoro, Stout, Paragon, Zulu, Jade, Deva, Maven, Amber) but E2 has no pack kind (rucksacks belong to A4), so they are not entered here; they need adding in A4.
- Climbing: Black Diamond (belay 5, carabiner 10, Camalot 3, Stopper, harness 3), Petzl (belay 4, carabiner 11), Wild Country (Zero Friend, carabiners, quickdraws). DMM page not reached.
- Snow: Burton 14 board lines, Lib Tech 17 board and 2 split lines; skis Atomic 5, Salomon 7, Rossignol 10, K2 3. Head, Völkl, Jones range pages not fetched (Jones, Völkl entries remain from earlier pass).
- Paraglider: DHV LTF classes A to D (dhv.de). EN 926 equivalence is not on the page; EN 926 PDF returned 404.
- Surfboard, kite, kiteboard, deck, snowboard shapes, cams, belay devices: Wikipedia articles from the first pass.

## Market
Unchanged from first pass (Shimano, VF, Amer, Johnson Outdoors, Burton, Clarus, Pure Fishing, Rapala, Petzl, with years).

## Not done
- No "Complete: n of n" claim anywhere; every sel says what was read and that the kind is not a complete list.
- Head, Völkl, Jones, DMM, Deuter, Wild Country nuts and Hilleberg official pages not fetched; Daiwa/Penn rod lines and fly rods not fetched.
- Maker groups (84) rest on a retail category page, not on a per-model page.
- About 47 fetches used in this pass (Firecrawl for 403 pages: REI, MEC, Campmor and the maker shops).
