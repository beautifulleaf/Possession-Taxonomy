# GD_EEU3_4 report

123 Russian brands. 117 tied at garment level, 462 rows written to verify/out/GD_EEU3_4_maker_kinds.tsv. 6 not tied, in verify/out/GD_EEU3_4_notfound.tsv.

Method: all 123 brands are listed on productcenter.ru (a directory of Russian manufacturers). I fetched the 36 directory pages named in the list to get each brand's producer page link, then fetched all 123 producer pages. Every source URL is a fetched producer page, and each is logged in verify/work/GD_EEU3_4/fetched.tsv. No brand site, marketplace or retailer was reached. Pages give product lists and descriptions, not shop menus.

Not tied:
- Lady Fox and Megafox make only fur collars, trims, pompoms and pelts.
- Kuzbasskaya Poshivochnaya Fabrika makes surgical gowns, shoe covers and bedding.
- Lineya makes bedding and restaurant staff uniforms, with no garment named.
- Magnum makes a winter fishing suit.
- Mamarada makes baby slings and a sling jacket.

Judgement calls:
- Matching home and sport sets went to A1.3.1.10.
- Sarafans went to A1.3.1.02.
- Medical gowns went to A1.4.2.12 and medical suits to A1.1.1.05.
- Fur coats (shuba) went to A1.4.2.11.
- Tracksuits, jackets with no other qualifier, knit tunics, fur vests, work suits, and bandanas and scarves worn as headwear were skipped.

Notes:
- One stray fetch (productcenter.ru/producers/20143/cleo) is logged and unused.
- The Margo page shows a liquidation date of 16.01.2026.
- The LENEVA producer page is for TÜLENEVA, a Saratov sewing maker.
- The Kronolux page gives both Moscow and Tashkent.
