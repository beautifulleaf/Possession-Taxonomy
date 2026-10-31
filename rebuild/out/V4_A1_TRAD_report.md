# V4_A1_TRAD report (Traditional dress), round 3

Part: rebuild/out/A1_parts/TRAD.json (replaces "Traditional dress"; validates OK; 55 kinds, 694 entries, 3 origin badges). Scripts: rebuild/work/V4_A1_TRAD/build.py to build4.py.

**Cloth shelf dissolved.** The 13 cloth kinds are now values of a "Cloth" tt group on the garments that use them (Sari, Dupatta, Dhoti, Kimono, Yukata, Dashiki, Kaba and slit, Boubou, Southern African dress, Kebaya, Sarong, Baju kurung, Pacific dress, Kilt). Each has a `ve` list "Named cloths covered by the visual-art taxonomy"; `see` takes only A-J codes, so the pointer sits in `sel` and `ve`. Tweed is on Kilt only.

**Loose models.** 46 `m` and 15 `r` removed (brand collections, not signature pieces; brands stay in the register). Kept: Pampero bombacha, Ecualama poncho, Vlisco Angelina dashiki, Vita Kin vyshyvanka. Kira and Kashmiri jamawar sari were unsourced.

**Entries before → after** (Wikipedia pages read to their end; each `sel` ends "Complete: n of n"): Sari 16 → 98, Bunad 2 → 151 (19 counties, List of national costumes of Norway), Sarong 15 → 37, Kebaya 13 → 31, Hanbok 6 → 27, Shalwar kameez 4 → 23, Obi 8 → 19, Dirndl 2 → 17, Huipil 3 → 17, Kimono 14 → 17, Kaftan 7 → 16, Ao dai 7 → 15, Kurta 5 → 13, Kilt 4 → 10, Beizi 5 → 10, Pacific dress 7 → 10, Dhoti 2 → 9, Hakama 8 → 9, Mamianqun 1 → 9, Southern African dress 1 → 8 (Basotho blanket with 13 named blankets as versions), Lehenga 1 → 8, Habesha kemis 1 → 8, Poncho 8 → 10, and smaller lists for the rest. Zhongshan suit 1 → 2, Toub 1 → 5. Yukata 2 → 0: its entries were dyeing methods (now Cloth values). Entries carry `g` sections.

**Round 3 changes.** Tails of Kimono, Obi, Barong tagalog, Kilt, Vyshyvanka, Mamianqun and Hanbok (to 267,384 characters) read; none held further types beyond five Hanbok garments. Bunad list taken county by county through the page summariser.

**Still short.**
- Southern African dress: Folk costume article read to 100,000 of 257,837 characters only (coverage says "Covers").
- Bunad: complete against the Wikipedia list; the article estimates about 200 bunads.
- No Wikipedia article found by search for Trachtenjanker, Kaba and slit or bombachas; those kinds keep primary-page entries (Kaba and slit now cites the V&A record). The Clothing in Sudan page (Toub) carries a machine-generated-text notice.
- Sporran, Kilt pin and Sgian-dubh have no entries.
- No market fields or `ms`, as instructed.
