# GD_MENA3_1 report

Tied at garment level: 26 of 134 brands (all Turkey), 89 maker_kinds rows in verify/out/GD_MENA3_1_maker_kinds.tsv. Not found: 108 brands, listed with what was tried in verify/out/GD_MENA3_1_notfound.tsv. Fetch log: verify/work/GD_MENA3_1/fetched.tsv.

Brands tied: Burce Bekrek, Cashmere in Love, Daymod, Dilek Susluer, Ece Kavran, Fimka, Hanife Cetiner, Heva, Imannoor, Incity, Integral Jeans, Intersivin, Kadir Buyukkaya, Maraton Sportswear, Merve Bayindir, Nefeli, Neslihan Yargici, Ozmoz, Sansim Adali (Sudi Etuz), Serdar Uzuntas, Siyah Inci, Terzi Dukkani, Tugba Atasoy, White Posture, YXL Collection, Bunyamin Aydin (Les Benjamins).

Method notes:
- The IFCO fair exhibitor pages (ifco.com.tr) were the best multi-brand source. Each exhibitor's /detail page lists "Product Class" garment types. I reached /detail from the on-page Details link seen on the Intersivin and Incity pages; slugs came from the fetched exhibitor list pages 1 to 7.
- IFCO generic words were mapped as: Pants to A1.2.2.07, Shirt to A1.1.2.01, Jacket to A1.4.1.22, Coats to A1.4.2.06. Tracksuit, Vest, Sports bra and knitwear were left unmapped.
- Trendyol, Akakce, n11, Ciceksepeti, Faire, Wolf and Badger all refuse or 403 WebFetch. Search excerpts were never used as attestation.
- Many names are people (Cem Hakko, Yasemin Ergene, Gul Golge) or non-Turkish or non-clothing entities (Madame Coco is home goods, David Catalan is Spanish). Most others have no indexed brand page.
