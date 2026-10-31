# GAP_E1 report (Toys & games)

About 58 fetches (sources.tsv in rebuild/work/GAP_E1/). Backups in rebuild/work/GAP_E1/bak/. Validate: OK (201 kinds). Firecrawl not used. Entries 1,364 before this pass, about 1,510 after.

## Closed
- **Loose models:** none left (V4 removed them all); checked again, no kind keeps `m`.
- **Coverage lines:** all 128 kinds without one now have one. 97 stale "starting list, not yet had the canon pass" sentences were replaced by "No complete list exists; follows the pages cited on each entry."
- **Construction kinds** (Wikipedia Construction set, read in full): Complete for Rod-and-connector (7 of 7, Interlocking disks added), Magnetic (1 of 1), Wooden (8 of 8), Hinged (5 of 5); Covers for Brick set (15 of 17), Metal (9 of 10), Girder (5 of 6), with the rest held in other kinds. Sections added from the article's own connection-method headings.
- **Twisty puzzles** (Combination puzzle, read in full): 8 cuboids, Gigaminx, Teraminx, Petaminx, Orb-It and three navigation-box puzzles added; coverage lines say Complete.
- **Mechanical puzzle article and Category:Mechanical puzzles (60 pages):** 12 entries added across Put-together, Interlocking, Sequential, Disentanglement, Folding and Dexterity; ten kinds carry a Covers line.
- **Toy soldiers:** List of toy soldiers brands read in full (136 names); 107 maker entries added. Covers 117 of 136; the other 19 are scale-kit makers held in Scale model kit. Sections are initial-letter bands because the list gives no other axis; the list gives no country or year.
- **Model railway scales:** Rail transport modelling scales read to its end; seven scales added (Nn2, HOn30, HOm, Sn3, American OO, 4 mm, 7 mm). Complete.
- **Sections:** Fashion doll and Teddy bear now by home country ("Country not stated" where no page gave it).
- **Owners and origins** from fetched pages: Hama (Malte Haaning Plastic, Denmark, 1961/1971), Lionel (Lionel Brands Group, 2026), Marble King (1949), Gund (Spin Master, 2018), Britains (Tomy, 2011), Merrythought, Schleich (Partners Group, 2019), Ty, BABY born (MGA, 2024), Cabbage Patch Kids, Webkinz, Care Bears, Kyosho, Traxxas, McFarlane, Action Man, Tonies, Katamino designer (André Perriolat). A Wikidata label query supplied country and year for about 35 dolls, bears and construction makers.
- **Market:** Circana 2024 (Toy Association page): US market about US$42.0 billion, -0.3 %; building sets +16 %. Added as `ms` on Building and Action figures. 13 owners added to the brand register.

## Remains (searches tried)
- **Market shares by company:** none published on any fetched page (Circana, Toy Association, Statista; searched "Circana US toy industry 2024 sales share Mattel Hasbro LEGO"). Left empty.
- **Estes Alpha and Saturn V years:** Wikipedia gives only "by 1969" (photo); searches gave 1967 from retailer pages, not fetched. Left empty.
- **Tenyo, Centuri, Quest kit makers:** Tenyo founding unsettled (1960 or 1931 in search excerpts, no fetched page); not added.
- **Lundby, Madame Alexander, Blythe owners:** pages state no current owner or conflict (Takara Tomy, Hasbro); left "owner not stated".
- **Wikidata matches:** ambiguous labels (Oxford, Coco, Trix, Blythe) were ignored; Medicom Toy page 404.
- **Not reached:** Neocube, Giiker, Pelikan, Nice Cube year, fidget pad, haptic-coin makers, Roco/Lima rolling stock, countries for the 385 kit makers and 240 die-cast brands (about 130 brands still "owner not stated").
- Playing cards, scale kits, die-cast: references unchanged and already Complete.

# Round 2

About 45 fetches (MediaWiki extracts API, link lists, Roco and Lima pages, ruwix). Validate: OK.

- **Method:** the list pages' own links (API prop=links) gave the exact article titles; guessing titles from entry names mostly returned wrong or missing pages. The kit list links about 180 articles, the model-car list about 500, the toy-soldier list 50; about 220 maker intros were read (20 per call).
- **Countries:** kits 378 of 385, die-cast 179 of 240 (from the list's own country sections plus article intros). Toy soldiers: 18 of 119 have a country; the other 101 have no Wikipedia article ("Country not stated"). Letter bands removed; all five big kinds (kits, die-cast, toy soldiers, Fashion doll, Teddy bear) are sectioned by country, with "Country not stated" last.
- **Owners:** 43 new owners with years (Hornby for Corgi, Humbrol, Pocher; Mattel for Matchbox, Tyco, Mebetoys; Simba Dickie for Majorette, Schuco, Solido; May Cheong for Bburago, Maisto, Martoys; Round 2 for Johnny Lightning, Racing Champions, Hawk, MPC; Hasbro for Tonka, Action Man, Super Soaker; and others). Kits now 13 owned, die-cast 30.
- **Added:** NeoCube; Giiker Cube, Rubik's Touch, Futuro Cube, Rubik's Spark (ruwix electronic cubes page); Lima (Italy 1946, Hornby 2004, six versions) and Roco (Austria 1960; its page names no rolling-stock series, only Lionel HO 1974-75 as a version).
- **Not closed:** most obscure makers have no article, so about 60 die-cast and 120 kit makers keep no country or owner ("searched" via the API; Redbox resolved to a DVD-kiosk article and was discarded). Brand owners for the other ~100 "owner not stated" brands were not reached (budget); Giiker maker and year are not on the ruwix page; NeoCube inventor conflicts across news pages and is left out.
