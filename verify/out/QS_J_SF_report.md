# QS_J_SF report
Result: 0 rows written in every table (no schemes, tier_entries, named_forms, makers, maker_kinds). No output TSVs created.
Reason: no Slow Food Presidium page could be fetched, so nothing could be attested.
- 6 WebFetch calls, all failed (logged in verify/work/QS_J_SF/fetched.tsv): fondazioneslowfood.com project page, Lombardy region page, fish category page (settori-presidi/fish-sea-food-and-fish-products-en), Noli Gulf presidium page, France nation page, and the 2014 presidia PDF all returned empty content (JavaScript-rendered or blocked); slowfood.com press release returned HTTP 403.
- 2 WebSearches located category/nation/region URLs (e.g. settori-presidi/fish-sea-food-and-fish-products-en, nazioni-presidi/*, regioni-presidi/*, slow-food-presidia/*) but excerpts only locate items; they do not attest.
- Skips to other categories: none counted (no list obtained). Unplaced products: none.
- Proxy status checked: healthy, so the failure is on the site side, not the proxy.
Next step: need a working fetch route for fondazioneslowfood.com (Parallel tools out of credit, WebFetch returns empty), or the owner supplying saved list pages.
