# DEFER_PERFUME report, 2026-10-31 (updated after round 2)

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

## Round 2 (coordinator asked to continue)
Calls 7 to 19 (20 Parallel calls in total across both rounds, no rate-limit errors; all in sources.tsv). 22 more perfumes moved, 31 in total; 269 remain in Alcohol-based perfume (coverage line updated). Each page was fetched and states the family (first word of the label).
- Amber: Yves Saint Laurent Nu (Oriental Spicy), Serge Lutens Encens et Lavande (Oriental Fougere), Serge Lutens Chergui (Oriental Spicy), Hermes Ambre Narguile (Oriental Spicy), Cartier Must de Cartier (Oriental), Carolina Herrera Good Girl (Oriental Floral)
- Woody: YSL L'Homme, La Nuit de l'Homme (Woody Spicy), Y 2017 (Woody Aromatic); Versace Man (Woody Spicy), Versense; Serge Lutens Bois de Violette; Givenchy Xeryus, Gentleman 1974 (Woody Aromatic); Davidoff Echo (Woody Spicy)
- Floral: Versace V/S Versus, Crystal Bright (page: Bright Crystal, Floral Fruity); Chanel Gabrielle, 28 La Pausa
- Chypre: YSL Yvresse (Chypre Fruity), Givenchy Ysatis (Chypre Floral)
- Leather: Tom Ford Fucking Fabulous 2017 (page: Fabulous, Leather)
Skipped for year mismatch: Victoria's Secret Pink (page 2001 vs 2002), Very Sexy Platinum for Him (2013 vs 2014), Forever Sexy (2015 vs 2016), YSL Baby Doll (2000 vs 1999), Versus Time for Pleasure(s) (2003 vs 2002), Dior Cologne Blanche and Eau Noire (2004 vs 2005), Chanel Sycomore (Les Exclusifs 2008 vs 1930), Lancome Idole (2019 vs 2020), Light Blue pour Homme (2007 vs 2008), Tom Ford Oud Minerale (2017 vs 2018). No family stated on page: Estee Lauder Beyond Paradise (excerpt fetched without a label). Tom Ford Fabulous (2018 entry) is a second entry for the same perfume, left in place.
Why only 20 calls: each search call costs about 12k tokens of output for roughly 2 usable hits, so context ran out well before the call budget. Victoria's Secret, Avon, Kurkdjian (searches returned no perfume page) and Coty Prestige remain unreached; their entries are mostly flankers or generic names.
