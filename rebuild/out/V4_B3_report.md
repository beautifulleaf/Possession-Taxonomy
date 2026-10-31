# V4_B3 Lighting named-entry pass

**Method:** about 40 fetches (Wikipedia pages, Casa di Luce, Lightology, ADI Design Museum, MoMA artist page via Firecrawl because WebFetch got 403). Wikidata: Compasso d'Oro query returned only 3 lamps; museum-holdings query failed (502). Log: rebuild/work/V4_B3/sources.tsv.

**Canon kinds (Table lamp, Floor lamp, Desk lamp, Pendant light, Chandelier, Wall light):** entries now carry nl, sel with coverage line, xg "Decade of design" and g per decade. Added from fetched pages: MoMA Castiglioni lamps (complete, 6 of 6: Luminator, Viscontea, Toio, Arco, Taraxacum, Snoopy), Compasso d'Oro lighting winners (Luminator, Eclisse, Atollo, Parentesi, Tolomeo, Lola, Mite, Counterbalance, Ascent, Discovery, Spider; Arco career award 2020) as landmarks, and 23 of 41 Lightology lamps whose type the page states. Counts before → after (entries): Table 16→26, Floor 5→7, Desk 10→13, Pendant 18→21, Chandelier 13→14, Wall 11→12.

**Not covered:** the full ADI Compasso list (no fetchable list), Design Museum, V&A and Vitra Design Museum holdings (pages not fetched), 18 Lightology lamps of unstated type. Tizio's 1979 Compasso rests on one source, so it carries no badge.

**Bulbs and strips:** origin icons Edison 1879 (first practical, per Friedel and Israel), Toshiba white LED lamp 2007, GE Lumiline fluorescent 1938; Swan 1881; smart systems Philips Hue (gens 2012, 2015, 2016) and Nanoleaf One/Essentials. LIFX page not found, so LIFX is missing. Market panel (ms): Signify revenue EUR 6.14 bn (2024), GE Lighting about USD 3 bn (2011), ams OSRAM history (2020). No share figures were on the fetched pages; Osram Sylvania's "largest North American share" has no year and is only in a note.

**Torches and lanterns:** modern LED-torch entries cut to Maglite, SureFire, Kel-Lite, Fulton MX-991/U (headlamps, clip-on, thrower, penlight emptied). Coleman lantern has own Newell Brands (2015). Historic lantern kinds kept. Monitor light bar entry (BenQ) removed as commodity.

**Loose models (m):** 392 removed from every kind. Became entries or versions: Gibigiana, Orbital (entries), Taraxacum88 (version of Taraxacum), Nanoleaf One (entry). All others removed as out of scope (retail SKUs, unfetched models); list in rebuild/work/V4_B3/m_removed.json. Ranges (r) dropped from commodity kinds and kept only for PH lamps.

**Brand register:** added Signify, ams OSRAM, GE Lighting, Savant Systems, Newell Brands, Nanoleaf, Toshiba. No moves or renames. validate.py --v3: OK.
