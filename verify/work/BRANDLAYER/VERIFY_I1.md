# VERIFY I1 Software & Apps (lean mode, Opus)

No new research and 0 fetches. The audit had already re-fetched all 59 harvest sources raw (AUDIT_I1_tmp/raw), so every row was checked by script against those saved pages (VERIFY_I1_tmp/build.py). The two named replacement sources (Apple Design Awards on Wikipedia, Google Play Best of 2025) were both already saved, so the src2 rows were confirmed without fetching.

## Result
- 915 brand rows (493 harvest after the drop, plus 422 audit adds after deferral). 890 are shown, 25 are not.
- Shown rows by tier: quality 117, cultural 759, listed 14.
- Homonyms: 14. Deferred: 2. Alias-merge groups: 85.
- Regions: 10 (Wikipedia "Software companies of X" categories). None shows renown: the pages name companies but state no speciality.

## Rules applied mechanically
- src_mismatch (30 rows):
  - Bear (Shiny Frog) and Things (Cultured Code): src2 = Apple Design Awards, quality.
  - Skylum Luminar: src2 = Google Play Best of 2025, cultural.
  - K7 Security and NVDA: script false negatives (shown as "K7 TOTAL SECURITY" and "NonVisual Desktop Access"), so they stay shown.
  - The other 25 have no named replacement source, so shown:false (tier listed) and they are excluded at merge: Roam Research, Spark, Houdini, Keyshot, Form-Z, TopSolid, Affinity, Infinite Painter, FlipaClip, FreeTaxUSA, Path Finder, Advanced Renamer, ES File Explorer, STDU Explorer, Lotus Magellan, Nitro Pro, EAGLE, Acapela, UTAU, Smallpdf, DocHub, Apryse, PDFescape, Shade 3D, Studio One.
- Navbox rows (23): stay cultural, with the note corrected to say each is linked in the navbox at the top of the category page and is not a category member.
- Tiers by source:
  - Quality: Apple Design Awards (winners, runners-up and finalists), AV-TEST and AV-Comparatives award winners, MusicTech reviewers' picks, the Headliner review, Stiftung Warentest via BR, and The High Tech Society's hands-on test (a weak site).
  - Cultural: Google Play Best of, SOS reader awards, and eHam and KVR user reviews (treated as votes). Readdle is cultural on the coordinator's ruling.
  - Listed: Plugin Boutique customer vote (6 rows), the Nikkei share survey, the SPA news item, and list rows that have no article of their own.
- Content identity (BRIEF 2026-10-31): 2 rows moved to DEFER_I1.json.
  - NDOORS Corporation: video-game developer.
  - Lykke Studios: its 2023 Apple Design Award was for the puzzle game "stitch.".
  - Kept: emulators (they are software), and Pok Pok as a maker of digital toys.
- Homonyms (homonym:true): Deepin (Linux), EAGLE (Autodesk), Pine (email client), Spike (email), Arc (browser), Warp (terminal), Drops (language app), You.com (AI search), Peak Labs (apps), Stella (emulator), Citra (emulator), Delta (emulator), Starry Night (planetarium software), Things, Inc. (Rooms).
- alias_merges: the audit's product-to-maker list (about 100 products in 85 maker groups), plus Notion -> Notion Labs.
- Five add sources (Nikkei, SPA, Wikipedia:INDIC, Planetarium software, BR) are not saved in AUDIT_I1_tmp. Their rows keep the audit's attestation and are marked "not re-checked".

## Index cleanup (for the coordinator; register not edited)
Some I1 register rows are named after individuals or call signs. They should be renamed to their products:
- AA6YQ -> DXLab Suite
- N3FJP -> Amateur Contact Log
- Irfan Skiljan -> IrfanView
- Christian Ghisler -> Total Commander
- Kovid Goyal -> calibre
- Tobias Doerffel -> LMMS
- G0CUZ, K6REA, Alan Heckert, Bob Keller and others like them -> their respective products
