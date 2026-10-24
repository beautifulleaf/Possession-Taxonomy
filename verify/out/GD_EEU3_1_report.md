# GD_EEU3_1 report

Batch of 123 Russian roster-only clothing brands (all sourced from productcenter.ru catalog pages).

- Tied at garment level: 106 brands, 230 maker_kinds rows (verify/out/GD_EEU3_1_maker_kinds.tsv).
- Not found: 17 brands (verify/out/GD_EEU3_1_notfound.tsv): ALFIN uni, 2NEEDLES, 40 Nedel, ANTAR, Beform, AGASI, AIR-VITA, ADEL, Anzhelika, ARI, Aliya, Bushick, Angarskaya, ATRIUM, ARNVALD, Barmariska, Bazis.
- Method: the 37 productcenter.ru category listing pages were fetched first (R-87), then each brand's own productcenter "products" page, reached through links on the fetched listing pages. Product names and category labels on those pages gave the garments. Fetch log: verify/work/GD_EEU3_1/fetched.tsv (every source URL logged full).
- No WebSearch was needed. No fetch failed.
- Weaker ties to review: rows from category labels only (Arion dress; Basia T-shirt and dress; Belirini dress; Assana T-shirt and blouse); Apparel (the page lists it as "Аппарель", matched by transliteration); Boevoy Trikotazh thermal base layer (listing text only); jacket rows filed as casual jacket (A1.4.1.22) where the page says only "куртка"; fur coats from mouton (Bagira, AS FURS).
- Skipped as having no kind: aprons, uniforms, work and medical suits, welder suits, pillows, plaids.
