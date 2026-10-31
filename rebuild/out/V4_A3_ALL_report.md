# V4_A3_ALL report

Part: rebuild/out/A3_parts/ALL.json (0.18 MB). Validator OK: 133 kinds, 280 entries, 0 loose models. About 55 fetches (Firecrawl only for Cartier, Van Cleef, Bulgari, Pandora, Messika, which WebFetch could not read).

## Entries before -> after
- The ten named departments are replaced by themselves (same names) plus one new department, "Jewellery houses & collections" (11 departments). Kinds 99 -> 133; entries 145 -> 280.
- Rings gained "Stone cut" (31 cuts: 12 historic, 19 modern) from Wikipedia's Diamond cut article; Traditional gained a Native American shelf (7 kinds), Khamsa, Cross of Trarza, Tizerzai, Jadanagam.
- New department, by house country then house: France (Cartier 20 lines, Van Cleef & Arpels 9, Chaumet 10, Messika 5), Italy (Bulgari 9, Pomellato 8), United States (Tiffany 21, David Yurman 2), Switzerland (Chopard 8, Piaget 3), Denmark (Pandora 8), Austria (Swarovski 2).
- All house entries carry own, tier, cty and own_y where a page gave it (Van Cleef 1999, Chaumet 1999, Bulgari 2011, Pomellato 2013, Tiffany 2021, Piaget 1988). Existing branded entries were back-filled.

## Loose models
All 25 kinds' `m` lists were removed from the output. Cartier LOVE pendant became a version of the Love line. The rest were removed: small-maker SKUs (Chapman, Castro Smith, Digby & Iona, Foundrae, AMYO, Jennifer Behr, Oliver Brown), generic types (jet, hairwork, shell and Wedgwood cameo, settings, eternity, hei-tiki types) and maker items already held by a range (Gorilla Glass, Kaos, Diablo, Industrial Strength, Haskell, Schiaparelli). Full list in rebuild/work/V4_A3_ALL/removed_models.json.

## References and coverage
Complete lines: Cartier 15 of 15 on its collections page (three grouping pages left out), Van Cleef 9 of 9, Bulgari 8 of 8, Pandora 8 of 8, Tiffany 20 of 20, Chopard 8 of 8, Stone cut 31 of 31 as returned. Partial: Messika (5 Move lines from product links), Chaumet, Pomellato, Piaget, David Yurman, Swarovski (Wikipedia only). Existing line kinds carry "Covers n" lines.

## Market facts (fetched, with year)
Richemont jewellery maisons EUR 16.5 bn of EUR 22.4 bn (year to Mar 2026); LVMH Watches & Jewelry EUR 10.49 bn (2025); Pandora DKK 32,549 m (2025) and DKK 28.136 bn (2023); Chow Tai Fook HK$94.4 bn (FY to Mar 2026); Signet US$6.70 bn (2025); Swarovski EUR 2.7 bn (2020).

## Not sourced
- Boucheron, Buccellati, Fred, Dodo, Qeelin, Graff, Harry Winston, Mikimoto, Chow Tai Fook and Signet lines: official pages 403/404, Wikipedia gave none. Kering has no revenue figure.
- Swarovski, Chaumet and Pomellato official collection pages not retrieved.
- Wikidata not used (it does not model jewellery lines). No whole-market share figure found.
- Indian forms (Wikipedia redirect to the general Jewellery article, 300k characters) read only from a retailer guide and the first 100k characters of the Berber article.
