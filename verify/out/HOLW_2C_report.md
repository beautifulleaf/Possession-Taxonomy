# HOLW_2C: display groups and quality markers (offline)

Outputs: verify/out/HOLW_2C_groups.tsv (244 rows) and verify/out/HOLW_2C_markers.tsv (242 rows). Helpers are in verify/work/HOLW_2C/ (config.py, build.py, markers_src). Level 1 follows each proposals row and the DPW1 navigation sketch. Level 2 uses the memo leaves, renamed for shoppers. Sub-families without leaves show their kinds directly at level 1. No kind ids change (R-58). None of these ten codes had groups.tsv or markers.tsv rows, so nothing was replaced or re-pointed.

## Groups (L1 / L2 / kinds)
- **D2** 8/10/55: phones first. Wearables, tablets, power banks, radios and accessories show their kinds directly.
- **D3** 8/17/82: headphones first. Smart speakers and parts show their kinds directly.
- **D4** 7/11/124: cameras, lighting and darkroom use their leaves.
- **I2** 7/11/53: purpose groups. Create, Game items and Register use their leaves.
- **I3** 10/4/45: groups by medium. Asset library sits under Online services. Memberships use their four leaves.
- **F1** 10/11/77: carrier groups. Pre-recorded players sit with CDs. Maps, Films and video, and Sleeves use their leaves.
- **F2** 9/20/72: Prints, Photographs and Sculpture use their leaves. I added a level-1 group for plinths (F2.9). The Figurines group is left as a generated view, so no kind gets a second home.
- **F3** 9/30/68: field, then standing. Bullion and trophies show their kinds directly.
- **F4** 7/24/76: the 25 leaves under use groups. The proposals' cross-lists (ihai beside butsudan, candles with incense) stay generated views.
- **F6** 9/22/119: minerals A–Z with no level 2; Strunz order is a secondary view. The empty "Other molluscs" leaf is left out.

**Kinds left out: none.** A script checked every stored kind against exactly one terminal group. data/kinds.tsv grew during the run (D4 109 to 124, F4 70 to 76, F6 116 to 119), and the final check covers the file as it stands now.

## Markers (from each proposals row's quality_markers; no new facts)
- **D2 26:** smartphones (Notebookcheck weights, OLED > LCD, IP68 > IP67 > IP54), tablets, e-readers, wearables and trackers, power banks. The last three are provisional.
- **D3 24:** the headphone scorecard; Stereophile class and SINAD for speakers and separates. TVs, projectors and turntables are provisional.
- **D4 20:** sensor-size ladder, lenses (DXOMARK), film. Lighting and support are provisional.
- **I2 17:** rights state, labelled "all media files"; audio and video quality ladders; audiobooks, fonts, domains, game items.
- **I3 20:** seven streaming markers, labelled "all streaming and catalogue groups", sit on Watch; seven connectivity markers. Memberships and boxes are provisional.
- **F1 27:** collectible and new books, comics, records (Goldmine ladder), CDs, video discs.
- **F2 16:** five markers labelled "all art" on Paintings, plus painting, print (CAA proofs) and photograph markers.
- **F3 30:** Sheldon ladder, stamps (gum and centering ladders, Japanese order), cards, bullion, banknotes, medals. Tokens and trophies are chosen by preference.
- **F4 32:** scroll goods, mezuzah case, prayer beads, rugs, statues and altars, Judaica, coffins and urns.
- **F6 30:** minerals, fossils, meteorites, coloured gemstones, diamonds and pearls (from the memo).

Groups with no markers in the proposals have none.
