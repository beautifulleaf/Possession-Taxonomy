# DEFER_PERFUME report, 2026-10-31

Stopped after 6 Parallel calls (free tier; no rate-limit errors), well under the 60-call budget, because the yield per call was too low to justify more: web_search on the free tier uses only the first 5 of the queries in a call, returns ~12k tokens per call, and found a Fragrantica perfume page for only about 2 of 5 perfumes. Designer pages, fetched with an objective, return only excerpts without families, so they were no route to URLs. Calls are in rebuild/work/DEFER_PERFUME/sources.tsv; backup in rebuild/work/DEFER_PERFUME/bak/H4.json; H4 validates (--v3 OK).

## Moved (9), each citing the fetched Fragrantica page
- Amber fragrance (Oriental): Alien (Oriental Woody, 2005), B*Men (Oriental Woody, 2004), Chanel Allure Sensuelle (Oriental Floral, 2005), Armani Code (Oriental Spicy, 2004)
- Floral fragrance: Burberry Her (Floral Fruity Gourmand, 2018), Kenzo World (Floral, 2016)
- Citrus & eau de cologne: Mugler Cologne (Citrus Aromatic, 2001)
- Woody fragrance: Ice*Men (Woody Aromatic, 2007)
- Fougère fragrance: Jean Paul Gaultier Fleur du Male (Aromatic Fougère, 2007; the fetched page is the Portuguese-language fragrantica.com.br page)

## Checked, not moved
- Mugler Womanity (2010): page states no family.
- YSL Mon Paris: the page found is the 2016 original, the entry says 2017; skipped.

## Still unplaced
291 of the 611 perfumes remain in "Alcohol-based perfume" (coverage line updated to 291). All the other houses (Victoria's Secret, Avon, Kurkdjian, Serge Lutens, Versace, YSL, Coty, etc.) were not reached. Designer-page URLs for those houses were found (Burberry, Victoria-s-Secret, Avon, Maison-Francis-Kurkdjian, Serge-Lutens, Versace, Yves-Saint-Laurent, Chanel, Givenchy, Jean-Paul-Gaultier, Giorgio-Armani, Kenzo, Dolce-Gabbana) but perfume URLs need one search hit each. Search hits seen but not fetched: Light Blue pour Homme (page year 2007, entry 2008 - mismatch), Dolce & Gabbana L'eau The One 2008.
