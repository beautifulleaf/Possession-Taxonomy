# Retailer directories: how they feed the brand registers

Owner pastes of single-category retailer brand lists (verify/retail/<site>.txt, name<TAB>slug), matched by match.py
against rebuild/reader/_brand_index.json. One enrichment pass (Sonnet, batches of ~100) runs after the pastes.

Rules for the enrichment pass:
- Source per brand: the per-brand retailer link from the paste, or the brand's own page; the category comes from what a fetched page states. Unresolved stays in the retailer's default category, marked "category from retailer listing".
- in_other with homonym_check: decide same company (add the category) or a different company with the same name (new entry).
- prefix_match: confirm the shortened name is the same brand.
- Merge spelling variants; record "X for Y" as a designer–house link, not a new brand; sub-lines link to the parent.
- Drop placeholders and store pages (Unbranded, Hand Made, Estate Jewelry, Contact dealer, various, Replica, Our Brands, Sephora Favorites, Ulta Beauty Rewards, Reglazing, SmartBuy Collection...).
- Shops (Macy's, Saks, Neiman Marcus, Harrods) are retailers, not makers.
- Traditions (owner 2026-10-31): a bare tradition label (Navajo, Zuni) is not a brand and belongs to the VE handover; named makers, workshops, trading posts and brands selling work in a tradition ARE brands, tagged with the tradition (e.g. Melanie Yazzie, Richard Chavez; Mexican silver: Spratling, Los Castillo).
- Artists who made jewellery stay as makers with a link to F2/VE.
- Audit lessons (wave 1): (1) region brand lists built from search excerpts failed 4 of 25 checks in A3 — every region list is re-verified against its raw source before merge; (2) a directory listing proves existence, not quality: names whose only source is an A–Z directory (The World of Shoes, The International Man, Optician Now, Markenkoffer and similar) go in as "listed" stubs unless a second page states quality, cultural standing or regional renown; (3) a maker's own website proves existence and products, not quality or renown (owner to confirm).
- Harvest rounds per category are capped at two (first pass + one continuation). What remains goes to the category's Opus cold audit; then a VERIFY pass re-fetches raw every name whose source is marked excerpt, partial or search-only, and every regional brand list, before anything is merged.
- Encyclopedia evidence (A5 audit: ~540 of 631 watch names rest on one list row): a brand counts as culturally relevant when it has an encyclopedia article of its own (category members always do; a list row only when the row links to the brand's own article). A list row without its own article, or a directory row, proves existence only: such names are kept as "listed" entries, not shown in the cultural or quality layers, unless a second page supports them. The VERIFY pass records has_article for every encyclopedia-sourced name.
- SELLER PRAISE: a shop's or dealer's praise of a brand it stocks (product page, brand page, shop blog) is not independent; tier such a brand "listed" unless another independent page supports quality. (applied by coordinator to B5 and B10, 2026-10-31)
- INDEX CLEANUP (coordinator, after the brand layer): corporate owners tagged as brands in reader/_brand_index (e.g. Lion Capital, Newell Brands, ACCO Brands in C4; BDT Capital Partners, Middleby in C2): demote to `rel` notes on their brands. Wrong-sense category tags (Halls, Viking in C2) to remove.
- CROSS-TAG REVIEW (coordinator, later): C2 overlaps flagged by VERIFY_C2 — Kingsford/Big K (barbecue fuel), Kubota, BCS, Gravely, Pellenc (garden machinery), Keter (planters): add C2 tags if their C2 products are confirmed.
- MOVES: verify agents may write MOVES_<C>.json ({"to":{CODE:[verified brands]}}) for brands that belong in another category; feed them to that category's harvest as ALREADY KNOWN and merge them with its verify (C8 → G3 sanitaryware/taps/flooring, B8 locks).
- INDEX CLEANUP: Ferrari (cars/fragrance) and Deutz (champagne) rows carry a C7 tag meant for the tractor makers; remove it (VERIFY_C7 creates Ferrari (tractors) and Deutz-Fahr).
- C5 open questions (coordinator, index cleanup): Uni-ball vs Mitsubishi Pencil rows (brand of that maker: add rel), Helix (now Maped), Wahl-Eversharp vs Eversharp, Camlin vs Camel (same Kokuyo Camlin company: link with rel).
- INDEX CLEANUP: register row 'Garrard' mixes the crown jeweller with the turntable maker (D3 tag) — split (VERIFY_D3 creates Garrard (turntables)).
- INDEX CLEANUP (E2, from AUDIT_E2): wrong-sense E2 tags on Fischer (fixings), Bell (helicopters), Fox (sweets), Stiga (garden machinery), Castellani (jewellery), eB, Kirkland Signature; Select mixes trading cards (F3) with the football maker; Mongoose, Lynx → G1; Adidas and Nike E2 rows carry watch descriptions.
- INDEX CLEANUP (E4, from AUDIT_E4): multi-sense rows whose E4 description is another product's — Excalibur, Walther, Remington, Zeiss, Wham-O; split or fix descriptions per category.
- HOMONYM MASKING (found in AUDIT_E3): harvest dedupe skipped names already in the register under another category, so a same-name brand of THIS category may be missing (different company) or lack this category's tag (same company). After the brand layer, re-scan each harvest's 'already known' skips against the register's categories and resolve (cross-tag or qualified new row).
- INDEX CLEANUP (E4): also Browning ('gun safes') and Wilkinson Sword ('razors') rows carry wrong E4 descriptions.
- INDEX CLEANUP (E6): 'Fischer' row mixes fixings company with the barometer maker — split into Fischer (barometers). Open: Apogee Instruments vs Apogee Imaging Systems.
- INDEX CLEANUP (F1): register 'Linn' row carries E3 (likely Roger Linn's drum machines, a different company) — split.
- INDEX CLEANUP (E3): register 'King' row tagged J8 (crisps) and E3 — split.
- H1 and H4 final rounds run as parallel parts writing separate files (H1_trad/H1_quality/H1_portfolio.json; H4.json + H4_countries.json); the audit reads all parts.
- INDEX CLEANUP (G1): rows mixing different companies — Jaguar (A5 Festina watches), Ferrari (J7 Ferrari Trento), Yeti, Bell, Sunbeam, Imperial, Alpina, Suzuki, Proton, Benelli, Singer; Koenigsegg duplicated.
- INDEX CLEANUP (G3): merge 'Vitra (tiles)' (C8) and 'VitrA (sanitaryware)' (G3) — same Turkish company.
- INDEX CLEANUP (H3): NJOY row merges a vape maker (J10) with a stainless-steel toy maker (H3) — split.
- INDEX CLEANUP (G2): 'Bentley' row mixes the car maker (G1, now G2 too) with an E3 Bentley — split.
