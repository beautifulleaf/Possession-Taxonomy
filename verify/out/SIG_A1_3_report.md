# SIG_A1_3 report (resumed run)

Rows already in the output at resume: 31 (13 houses: Schuberth, Falke, Munsingwear, Crombie, London Fog, Gardeur, DAKS, Keela, Reima, Rockseri, Fila, Castelli, Cia. Hering). Not touched.
Added this run: 35 named forms (66 total) for Saint James (7), Lucy & Yak (7), Glenmuir (6), Cimalp (6), Kunert (4), Trespass (2), Jott (1), Hunter (1), Canali (1), Cordings (1).
Houses written to done.tsv as none found: all other houses in the list (see verify/work/SIG_A1_3/done.tsv). Many are "none found" because no fetchable page showed standing model names (marketplace listings, 403/404 pages, history pages only), not because the house has none.

Problems
- The 20 URLs behind the 31 earlier rows are not in fetched.tsv (no work dir existed at resume). Unless the caller logs them, R-101 drops those sources at load.
- Panam (M-panam): its named models (084 Campeon, 1967) are footwear, not A1.
- No kind problems. Breton shirts placed under A1.1.1.01 T-shirt (long-sleeve jersey).
- No new lines written; Mascot Accelerate and Kuebler Bodyforce pages showed trousers only.
- Failed or empty fetches: Ortovox product pages (404), Fruit of the Loom EU (empty), Rusty preview (403), Trespass YPC (403), Kaufland (403).
