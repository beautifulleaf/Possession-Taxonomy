# V4_A1_TRAD report (Traditional dress), second pass

Part file: rebuild/out/A1_parts/TRAD.json (replaces "Traditional dress"; validates OK: 55 kinds, 531 entries, 3 origin badges). Scripts: rebuild/work/V4_A1_TRAD/build.py, build2.py, build3.py; dropped items in dropped.json. About 63 fetches used.

**Cloth shelf dissolved.** "Named cloths & textiles" (13 kinds) is gone. A "Cloth" tt group (Kente, Wax print, Batik, Shweshwe, Bogolan, Adire and aso-oke, Ikat, Songket and tenun, Khadi and handloom, Faso Dan Fani, Tapa and masi, Tartan, Tweed; Yukata gets its two dyeing methods) sits on the garments that use them. Each has a `ve` list "Named cloths covered by the visual-art taxonomy" with the removed entries. `see` only accepts A-J codes, so the visual-art pointer is in `sel` and `ve`. Tweed is on Kilt only.

**Loose models.** 46 `m` and 15 `r` removed: brand collections, not signature pieces (brands stay in A1_brands.json). Kira and Kashmiri jamawar sari were unsourced. Kept signature entries: Pampero bombacha de campo, Ecualama Otavalo poncho, Vlisco Angelina dashiki, Vita Kin vyshyvanka (cty only; no ownership facts fetched, so no own/tier).

**Coverage, entries before → after** (every page below read to its end unless noted; "Complete: n of n" is in each kind's `sel`):
Sari 16 → 98; Sarong 15 → 37; Shalwar kameez 4 → 23; Kurta 5 → 13; Dhoti 2 → 9; Kaftan 7 → 16; Poncho 8 → 10; Thobe 6 → 7; Kebaya 13 → 31; Obi 8 → 19; Hakama 8 → 9; Haori 5 → 7; Ao dai 7 → 15; Baju kurung 7 → 8; Sherwani 2 → 4; Bandhgala 2 → 5; Lehenga choli 1 → 8; Dirndl 2 → 17; Lederhosen 2 → 3; Huipil 3 → 17; Pollera 3 → 7; Boubou 3 → 6; Dashiki 1 → 2; Habesha kemis 1 → 8; Abaya 2 → 5; Charro 2 → 5; Guayabera 2 → 5; Qipao 3 → 4; Ruqun 7 → 8; Beizi 5 → 10; Tang jacket 2 → 3; Mamianqun 1 → 9; Wrap robe 3 → 6; Pacific 7 → 10; Dupatta 4 → 7; Kilt 4 → 10; Bunad 2 → 5; Flamenca 2 → 2; Terno 5 → 5; Gákti 2 → 2 (article names no types); Yukata 2 → 0 (dyeing methods moved to Cloth).
Most entries now carry `g` sections; versions added for Furisode sleeve lengths, Hyderabadi kurta, Pollera de gala, Dashiki suit, Durumagi, Chapan.

**Still short (exact).**
- "Covers", not "Complete": Kimono (read to 200,000 of 217,652; tail unread), Obi (last 1,237 characters unread), Barong tagalog (last 4,085), Kilt (last 26,472), Vyshyvanka (last 26,069), Mamianqun (last 31,292), Hanbok (read 100,000 of 267,384; headwear and later sections unread), Bunad (about 200 exist; article names 5).
- Not re-checked in this pass, so no completeness claim: Zhongshan suit, Toub, Kaba and slit, Southern African dress, Trachtenjanker, Bombachas & gaucho dress (one or two structure-pass entries each, now with `g`). Sporran, Kilt pin and Sgian-dubh have no entries.
- No market facts (own, tier, own_y) sourced; no `ms` (not a market department).
