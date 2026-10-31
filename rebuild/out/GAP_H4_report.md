# GAP_H4 report (Fragrance)

validate --v3 rebuild/out/H4.json: OK. Backups in rebuild/work/GAP_H4/bak/; scripts apply.py, apply2.py, apply3.py; URLs in sources.tsv. About 58 fetches, no Firecrawl.

## Closed
- **Loose models:** none remain (the earlier V4 pass converted or removed them all); nothing to do.
- **Family not stated (biggest gap): 468 -> 444.** 24 perfumes moved because a fetched page names the family.
  - Floral: Estée, Blue Grass, Norell, Private Collection, Charlie, White Shoulders, Chanel No. 22, Anaïs Anaïs, Eden.
  - Chypre: Halston, Polo, Fidji (French Wikipedia).
  - Amber: Oscar, Classique, Ambre Antique and L'Origan (French Wikipedia), Old Spice, LouLou.
  - Gourmand: A*Men, Lolita Lempicka, Euphoria (Wikipedia Gourmand page).
  - Fruity: Fantasy. Fougère: Chaz. Aquatic: Escape (Calvin Klein page).
  - Each `d` now opens with the family words and `s` is the page that states them.
- **Coverage lines** added to Collectible perfume bottle, Bulb atomiser, Absolute & CO2 extract and Animalic & resin material. The Alcohol-based perfume line now reads "Covers 444 of the 611".
- **Sections (step 5):** the 13 family kinds now have `g` (launch period) and `xg`, entries sorted by period, year, name.

## Method and what it showed
MediaWiki API: category listing, 20-title intro extracts, existence checks (50 titles per call), search snippets by family term; French Wikipedia; house pages (Caron, Rochas, Givenchy, Kenzo, Burberry, Versace, Ralph Lauren, Victoria's Secret, Elizabeth Arden, Mugler, Tom Ford, Calvin Klein, Cacharel). English Wikipedia has an article for only about one in ten of these perfumes, and house pages almost never state families. The summariser also gave no verbatim text, so only statements it quoted were used.

## Remains (searched)
- **444 perfumes without a fetched family.** Searches: "<family> fragrance released" variants (floral, chypre, oriental, woody, fougère, aquatic, green, fruity, leather, musk), fr.wikipedia "famille olfactive", Bois de Jasmin decade series.
- **Lead for a later pass:** Perfume Intelligence (perfumeintelligence.co.uk/library, A-Z pages) states a family for most perfumes ("a fresh floral white flower bouquet"). Pages hold about 50 names each and chapters run to many pages, so it needs about 100 fetches; not possible in this budget.
- Unplaced because a page gave only part of the name or a paraphrase: White Diamonds (floral, paraphrase only), The One (page covers both versions), Liberté (a Cacharel perfume not in the list).
- Owners not stated for Fabergé, Grès, Guy Laroche, Dana, Piguet, Houbigant and celebrity lines: not retried.
- Jean Paul Gaultier brand page: 404, no other page tried.
