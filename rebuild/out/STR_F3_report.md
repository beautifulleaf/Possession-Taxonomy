# STR_F3 report: Coins, Stamps, Medals & Trading Cards

validate.py --v3: OK. Departments 10 to 10; shelves 15 to 27; kinds 95 to 107; archetypes 435 to 409.

Category has a new `ax` and 10-step `key`; every department and shelf has `t` and `ax`; kinds use hand-written `tt`.

Regrouped:
- Coins: 2 shelves to 5 (modern by purpose; errors, trials and imitations; ancient; Byzantine, medieval and Islamic; Asian and traditional).
- Banknotes: 1 to 3 (official; private, emergency and military; specimens, errors and copies).
- Stamps: 2 to 4 (by purpose; sheets, booklets and varieties; covers; stationery).
- Trading cards: 2 to 4 (sports; issued with goods; games, non-sports and stickers; sealed).
- Exonumia: 2 to 3 (tokens; altered coins; medals). Elongated coin moved to altered coins.
- Holders: sealed slabs apart from open holders. Albums: books apart from trays, boxes and cabinets.

Split or renamed (in F3_renames.json): Grading slab became Graded coin slab, Graded banknote holder and Graded card slab; Odd and curious money became Commodity and primitive money. Nothing moved to other categories.

Added (10, each from a fetched page): Achaemenid Persian coin, Postage due stamp, Official stamp, Life-saving medal, Wound badge, Sealed trading-card game product, Jeton and gaming counter, Geocoin, Storage box, Display case and stand. Scripophily and traveller's cheques were left out: F5 already holds share, bond and cheque kinds.

References: Wikipedia Coin collecting (coins), Exonumia (tokens, altered coins, medals), Military awards and decorations (honours), Booster pack and Non-sports trading card (cards), Postage due, Official mail and Czech Post stationery types (stamps), BullionStar supplies (storage). No banknote reference could be fetched (IBNS, British Notes, Numisview blocked); that department was checked only against Exonumia and Coin collecting.

Generic archetypes demoted to models: 31 (for example Euro definitive coins, Regional tribal coinage, Slogan postmark, Stampless letter, both challenge-coin entries). Duplicates removed: Allen & Ginter under Cigarette and trade card; Young Guns folded into Upper Deck Young Guns.

Cross-links (10): E1 Trading card single and Trading card packs & boxes, F5 Postcard album, Picture postcard and Share certificate, F4 Devotional medal, F1 Single-issue comic and Comic storage box. Targets checked; STR_SEE.tsv has no F3 pairs.

Thin: Collector banknote and Error note have no archetypes.
