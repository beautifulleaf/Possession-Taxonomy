# GD_EEU3_7 report

Brands in list: 118. Tied at garment level: 114 brands, 397 maker_kinds rows (verify/out/GD_EEU3_7_maker_kinds.tsv). Not tied: 4 brands (verify/out/GD_EEU3_7_notfound.tsv).

Method: productcenter.ru catalog pages (the brands' own sources) gave producer links; each producer page was fetched (one fetch per brand, plus the 36 listing pages). All fetches are logged in verify/work/GD_EEU3_7/fetched.tsv; every URL in the output is in that log. No WebSearch was used, because the listing pages gave the links. No fetches failed or were rate-limited.

Not tied:
- Woollamb: sheep-wool vests and chuni slippers only; no A1 kind fits a wool vest.
- Tekhnoavia: only classes of work clothing (aviation, welder, security), no garment.
- VINTAGE: the page names the maker VINTAGE+ (Vintazh Plius), a different brand; not used.
- TARCMA: only tracksuits; no kind for them.

Notes:
- Vivo: two Krasnodar producers carry the name. Tied to the fabrika "Vivo" page (producers/1409); Vivostyle (producers/32028, "Vivo Style") was fetched but not used.
- Vilan: both producer pages (4003, 39852) were used.
- Some rows come from the company description text, not a listed product; notes say "(описание)".
- TU VUMEN: the page uses "ТУ ВУМЕН" as the company name and "TWS" in its text.
