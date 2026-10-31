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
