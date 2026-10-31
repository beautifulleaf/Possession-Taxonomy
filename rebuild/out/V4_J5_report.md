# V4_J5 report: Pantry Staples named-entry pass

Result: out/J5.json validates (0 errors, 277 kinds, 377 → 943 named entries). Backups in work/V4_J5/bak/. Script: work/V4_J5/build_j5.py. About 33 fetches used. J5_renames.json and J5_moves.json unchanged.

## Per list (entries before → after)
- **Pasta shapes** (8 pasta kinds, 87 → 220 incl. gnocchi): Wikipedia List of pasta, read in three windows to the page end (214,864 characters). Complete: 182 of 182 rows as returned by the page reader; 48 matched existing entries, section stored as g. New kind "Pasta brands" (5, Barilla portfolio).
- **Rice cultivars** (7 rice kinds, 28 → 173): Wikipedia List of rice cultivars. Covers 163 of about 1,000: complete national lists for Italy, Spain, Japan, California, Carolina, Louisiana, Australia, Portugal, Thailand, Vietnam, India. Not added: Bangladeshi, Indonesian, Pakistani, Philippine, Nepali, Greek and regional Indian landrace lists (West Bengal alone has 282).
- **Spice blends**: Wikipedia Spice mix. 28 blends added in four new regional kinds plus the existing barbecue/seasoning kind. Blends that already have their own kind (garam masala, baharat and so on) were not duplicated. The page reader may have dropped rows.
- **Protected pantry products**: Wikipedia List of Protected Designation of Origin products by country (352,187 characters, four windows). Added 5: Aprutino Pescarese, Bruzio, Terre Tarentine, Latvian grey peas, Paprika Žitava. Not complete: the page reader returned no Spanish, Greek or French oil rows, eAmbrosia is JavaScript-only and the Wikidata query timed out. Existing PDO entries were kept.
- **Market layer**: 80 branded entries now carry own, tier, cty and own_y where a fetched page states them (Kraft Heinz, Unilever, Nestlé, Conagra, McCormick, Ajinomoto, Kikkoman, Mizkan, Barilla, Lee Kum Kee, Kewpie, plus 14 instant-noodle makers). New kinds "Spice and seasoning brands" (10) and "Pasta brands". Brand register +12 owners.
- **Former models**: 212 flat models handled: 158 became entries (grouped by maker as versions where one maker had several), 31 merged into existing entries as versions, 10 dropped as generic or duplicate (for example Elbows, Medium shells, Dried soup, Infant cereal). Their source is the kind's page from the earlier pass.

## Market facts (ms)
Italian pasta, Barilla 24.5 % (2021, the page cites a May 2021 source); Thai instant noodles, YumYum 20–21 % (2019); Indian instant noodles, Maggi 60 % (2018); Malaysian, Maggi 39 % (2018); ramen, Demae Iccho about 60 % (2016); soy sauce, Kikkoman largest producer worldwide (2002, no percentage). National champions are marked on entries for Japan, South Korea, Indonesia, Thailand, Philippines, Italy and Hong Kong, and global-group brands for 14 more countries.

## Could not be sourced
- Share figures with no year on the page (MAMA, Maruchan, Sapporo Ichiban, Wai Wai, Knorr and Maggi in Pakistan, Vifon in Poland) were left out of ms.
- No US or European category shares (ketchup, soup, frozen meals): the Ketchup page has none and the Campbell's page returned 404.
- Owners of many local brands (Campbell's, Nutella, Dolmio, Marmite country and others) are not stated on fetched pages, so own and tier are left empty.
- Dishes, craft and indie sauce lists, and sub-brand versions were not covered within the fetch budget.
