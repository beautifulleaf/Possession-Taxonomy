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
