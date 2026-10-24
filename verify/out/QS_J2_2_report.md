# QS_J2_2 report

Rows: schemes 3 (SCH-msc-certified-fishery, SCH-asc-certified-farm, SCH-gff-great-taste); tier_entries 44; named_forms 5; makers 4 (Anchoas Hazas reused as M-anchoas-hazas); maker_kinds 4. No standards, standard_values or attributes.

By scheme:
- MSC: 36 entries from 25 fishery pages (current certificates, date = certified since, stale_after = certificate expiry). Species: haddock, hake, saithe/pollock, cod, herring, sockeye/coho/chinook/chum, sardine, plaice, yellowfin tuna, northern prawn, brown and pink shrimp (fallback kind J2.1.2.01), langoustine, lobster, mussel, oyster, scallop. Page-level dates apply to the whole fishery, not per species (Barents saithe was certified 2016 per the page).
- ASC: 3 entries (Bakkafrost Atlantic salmon, Taylor Shellfish oyster and mussel). The ASC news pages give no certification date; date is the article date and the scope says so. ASC Find-a-Farm was not reachable (no URL from a search or page).
- Great Taste: 5 entries. 2025: East Neuk Kilnhouse hot smoked mackerel (Golden Fork Scotland, Supreme Champion), Goatsbridge Fish Processors hot smoked trout, Conservera Castreña anchovy fillets (nominees). 2026: Kuopion Perinnetuote cold smoked trout (Golden Fork winner), Anchoas Hazas anchovies in spicy butter (nominee). The fetched pages do not state "3-star" for these; 3-star is inferred from Golden Fork nomination (flagged in scope). Only the East Neuk win and the Kuopion win are attested as wins; Goatsbridge, Castreña and Hazas are nominees only.

Failed or unusable pages: gff.co.uk (all 403), yorkshirepost, seafoodsource, tasteatlas (403), hwchamber (404), the 2025 EU media-alert PDF (unreadable), fishfarmermagazine (paywall teaser). Procedure slip: I fetched https://fishfarmermagazine.com/?p=146884, which is a search-result URL with "www." dropped; it is logged as failed and nothing was used.

No Great Taste 3-star caviar, tinned sardine or other tinned/smoked salmon winners of 2025 or 2026 could be attested from fetchable pages; the full winners directory is blocked.

Skips and gaps:
- missing kind?: skipjack tuna (TUNACONS, TTV), albacore tuna (AAFA North Pacific), pink salmon (Alaska salmon), fresh European anchovy (Cantabrian purse seine, certified 2015-03-24), cockle (DFPO). Not entered.
- No currently certified MSC mackerel (NE Atlantic units withdrawn), crab (Dungeness withdrawn) or Maine lobster (withdrawn) found.
- Search-only, not fetched: Danish/Scottish haddock, other tuna and prawn fisheries. Many more MSC fisheries exist; coverage is partial.
Work files: verify/work/QS_J2_2/fetched.tsv, build.py.
