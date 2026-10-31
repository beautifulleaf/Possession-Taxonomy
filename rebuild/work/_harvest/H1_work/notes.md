# H1 harvest notes
Segments: H1 is in domain "general" -> Professional & flagship, Premium, Mainstream, Value, Heritage manufactory, Artisan & independent, Specialist, Own-label & retailer, Institution & issuer.
## Sources
- fetched OK: https://www.lookfantastic.com/c/brands/all-brands/ (A-Z, ~400 brands)
- fetched OK: https://www.sephora.me/ae-en/brands
- BLOCKED: https://www.sephora.com/brands-list (403 WebFetch; Parallel 402 no credit; Firecrawl denied by classifier) -> moved on
- BLOCKED/empty (JS): https://www.ulta.com/brand/all, https://www.ulta.com/global/nav/allbrands.jsp
- fetched: Wikipedia L'Oréal, Estée Lauder Companies, Boots brands page, Category:Personal care brands, List of Unilever brands, List of P&G brands, Category:Cosmetics companies of Japan
- fetched: Coty, Amorepacific, LG H&H, Shiseido, Wikipedia categories Cosmetics/Skin care/Male grooming/Shampoo/Korean cosmetics/Soap/Toothpaste/Feminine hygiene/Razor/Shaving cream brands
- Firecrawl fallback (coordinator-authorised) for sephora.com/brands-list and ulta.com/brand/all: DENIED by auto-mode permission classifier (Bot Check Circumvention). Not retried further.
- Wikidata SPARQL (cosmetics brand / cosmetics company classes): timed out after 120 s, not retried
- fetched: Category:Cosmetics companies of US/France/UK/Germany/India/Australia/South Korea/Philippines/Switzerland
- fetched: Kosé, Kao, Puig, Category:Beiersdorf brands, Henkel
- fetched: badgerandblade artisan soap list, sharpologist artisans, russh J-beauty; BLOCKED 403: harpersbazaararabia J-beauty article
- fetched: Category Revlon/Colgate-Palmolive/Haleon/Reckitt/Estée Lauder brands
- fetched: beautylish indie nail brands, greenlitcontent nail polish brands; BLOCKED 403: skinsort korean brands
## Build
- Entries in H1_work/b1..b6.txt (name|seg|kf|country|year|src), src codes in src.tsv, cuts in cut.txt; build.py writes work/_harvest/H1.json (temp+rename). Check: 586 new, 40 links, 0 errors.
- Dropped name clashes with unrelated register brands: Elixir (E3), Parachute (B2), Playtex (A1), Zenith (A5), Royal Crown (J9), Eisenberg (A3).
