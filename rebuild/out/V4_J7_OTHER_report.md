# V4_J7_OTHER report

Part file: rebuild/out/J7_parts/OTHER.json (4 departments, 34 kinds, 360 entries, 11 register brands). Passes validate.py --v3. Script: rebuild/work/V4_J7_OTHER/build.py; sources: sources.tsv.

## Per department
- **Sake & rice wine.** Sake kind: 8 brand entries -> 279 breweries by prefecture, from the fetched jref.com list (all 277 on it, including SakeOne and the Gekkeikan and Ozeki US breweries, plus Takagi Shuzo and Akashi Sake Brewery kept from the old edition, stated in `sel`). Grades are versions for 16 breweries only. Style kinds are now entry-less; their products became versions. Makgeolli 5, Cheongju 4, Huangjiu 6.
- **Cider, perry & mead.** Brands carry owner and tier (Heineken, Molson Coors 2018, C&C, Brothers Drinks 2021, Accolade 2021, independents). Added designations: Cotentin, Cornouaille, Perche (INAO), Sidra de Asturias (DOP 2005), Herefordshire Perry (PGI, UK specification). New kind International cider brands. ms: Angry Orchard 60 % (2016), 50 % (2021).
- **Ready-to-drink.** Grouped by owner. ms: White Claw 60 % (2019); with Truly 85 % (2019), 75 % (2021).
- **No & low.** Rebuilt as four shelves (beer specialists, wine, zero-proof spirits and aperitifs, low-alcohol band), `alc` on every entry, ms with 8 sourced facts (IWSR via CNBC 2025, Bernstein 2023, Athletic 17 % US volume, FoodNavigator forecast, UK +30 %).

## Renames and moves
Sake (junmai, honjozo, ginjo & daiginjo) -> Sake breweries (kura); Alcohol-free beer -> Alcohol-free beer specialists. No moves.

## Dropped
- Heineken 0.0, Erdinger Alkoholfrei, Guinness 0.0 and the alcohol-free beer models (Clausthaler, Beck's Blue, Estrella Galicia 0,0 and others): **the Beer part must carry them under their parent beers.**
- Loose models without a source or outside the list: about 8 sake models, Tozai, Hawkstone, Galipette, Ace Cider, mead type models, fruit/palm/pulque brands, RTD retail models, Monteith's, Sulseam, Yangchon. Pecado Natural, Bordelet Poire Granit, Truly lines and Akashi-Tai infusions became versions. Asturian sidra natural and Three Counties perry were merged into their designations.

## Not sourced
- Sake entries have `cty` only (no owner on the list); descriptions are minimal.
- 404 or blocked: Wikipedia sake list, Kopparberg, Somersby, Stella Artois Cidre, El Gaitero, WKD, High Noon, Lyre's; Business Wire read via Firecrawl.
- `cty` omitted for Smirnoff Ice, Bacardi Breezer, Mike's (pages give no origin); Mike's owner conflicts between pages, Mark Anthony used.
- Lucky Saint `alc` (0.5 %) rests on a search excerpt; Torres Natureo on a headline; other zero-proof `alc` values follow "non-alcoholic" wording without an ABV.
- Åbro/Kopparberg tiers not explicit on fetched pages. No complete cider appellation register reached.
