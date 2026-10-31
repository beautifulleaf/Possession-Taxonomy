# V4_H4_PERFUME report

Part file: rebuild/out/H4_parts/PERFUME.json (replaces department "Perfume", 206 KB, validates OK). Builder and registry: rebuild/work/V4_H4_PERFUME/ (build_part.py, registry.json, sources.tsv, m_fate.json).

## Entries before -> after
Old department held 110 named entries (plus 101 loose models). New department holds 611 named perfumes in 14 kinds (same shelves and kinds as the structure pass, so `t`, `ax`, `tt`, `see` are kept).
- Family kinds (134 entries): Floral 25, Fruity 1, Amber 20, Gourmand 6, Oud 2, Musk 6, Woody 16, Chypre 13, Leather 11, Citrus 8, Green 8, Aquatic 8, Fougere 10. A perfume sits in a family only where a fetched page states it (Wikipedia Perfume page, Fragrance wheel page, the perfume's own article intro) or where the structure pass already placed it.
- Alcohol-based perfume (shelf renamed "Family not stated"): 477 entries in launch-period sections, because no fetched page gives their family. Fragrantica and Fragrances of the World could not be read, so this is a known limit.

## References and coverage
- Wikidata SPARQL: 112 of 112 perfume items with an English Wikipedia article read; 101 are named perfumes. Left out (not perfumes): U From Uruguay, Little Trees, Automatic deodorizer dispenser, Blocki, Kolonya, Hai Karate, TAG Body Spray, StormFlower/Usher/Usher VIP (redirect pages). Wikidata has no family property.
- Wikipedia List of perfumes: all 265 rows read (table complete; the rest of the page is references).
- FiFi Award page: 318 of 318 fragrance winner rows (Women's/Men's Fragrance of the Year in Prestige, Luxury and Popular, plus the Fragrance Hall of Fame). 34 Hall of Fame perfumes carry role landmark; Good Girl, Le Male and 1 Million are landmarks per Puig's 2024 article (38 roles in 611, under one in five). Flankers (Sauvage Parfum, Elixir, Terre d'Hermes Eau Givree, Dior Homme 2020, Polo Red and others) are versions.
- Wikipedia pages of Guerlain, Chanel and Francis Kurkdjian (only rows naming a house), and 13 Osmotheque perfumes: "Covers" lines, the pages say they are not complete.
- Fragrance wheel page gave Edwards' families (1983, 2008, 2010 versions) used in the section names.

## Loose models (m)
101 listed: 12 became entries or matched an existing entry (Sunkissed Goddess, Vanilla Candy Rock Sugar 42, Bois Pacifique, Do Son, Fleur de Peau, Philosykos, Tam Dao, Portrait of a Lady and others). 89 (about 70 distinct, mostly Diptyque, Tom Ford, Maison Margiela, Miu Miu, Aesop, DedCool ranges) were removed because no fetched page attests them; the list is in work/V4_H4_PERFUME/m_fate.json. Ranges (r) were removed.

## Market facts (fetched)
- US prestige beauty 2024: fragrance 28 % of US$33.9 billion, sales up 12 %, luxury 12 % of prestige fragrance (Circana via Cosmetics Business).
- Puig 2024: 11.5 % global value share in selective fragrances, net revenue EUR 4.79 billion.
- Interparfums 2024 net sales by licence: Jimmy Choo 17 %, Montblanc 15 %, Coach 14 %, GUESS 12 %, Donna Karan/DKNY 7 %, Lacoste 6 %, Ferragamo 5 % (10-K).
- Owners and years from fetched pages: Guerlain to LVMH 1994; MFK to LVMH 2017; YSL Beaute to L'Oreal 2008; Creed to L'Oreal (completed 31 March 2026, after Kering 2023); Le Labo to Estee Lauder 2014; Frederic Malle 2015; Jo Malone 1999; Byredo to Puig 2022; Nina Ricci 1998; Penhaligon's and L'Artisan 2015; Diptyque to Manzanita Capital 2005; Amouage under Oman Perfumery LLC; Chanel via Chanel Limited. 270 entries carry own/tier (cty and own_y where a page states them); brand_updates cover 80 register brands; 8 owner groups added to brands.

## Not sourced
- Owner and tier for houses no fetched page covers (about 340 entries have none); Serge Lutens owner is not stated on its page ("owner not stated", Craft & indie).
- Estee Lauder fragrance revenue, L'Oreal Luxe and Coty fragrance shares (only search excerpts or company totals). Puig FY2024 PDF unreadable; the trade article was used.
- Prada is assigned to L'Oreal (L'Oreal page) although Puig's page lists it earlier; Donna Karan to Interparfums (10-K) not Estee Lauder.
- Wikipedia 404s: Chypre (perfume), Fougere (perfume), Inter Parfums, Kering Beaute, Maison Francis Kurkdjian.
- About 45 fetches used.
