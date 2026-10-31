# GAP_D4 report: Cameras & Photography

Validator: `validate.py --v3 rebuild/out/D4.json` OK (145 kinds, 660 archetypes). Backups: rebuild/work/GAP_D4/bak/. Scripts: rebuild/work/GAP_D4/ (films.py, cams.py, years.py, cover.py). Fetch log: rebuild/work/GAP_D4/sources.tsv. About 40 fetches; no Firecrawl.

## Closed
1. **Loose models:** none left (0 `m`/`r` kinds before and after).
2. **Coverage line:** all 50 kinds with entries now carry one in `sel`. Stale text ("tail not read", "still not itemised") was removed.
3. **Film stocks (8 kinds):** the discontinued list was read to its end (291,791 characters; ends in Valca) in six windows, with per-maker prompts because the summariser refuses verbatim tables. 77 new series entries: Colour negative +26, Black-and-white +25, Slide +24, B&W reversal +2. Added makers include Azomureș, dekopan, ERA, Film Washi, Herzog, Rera, Street Candy, Svema, Tasma, Valca, Negra, Luckyfilm, Ferrania/3M/Imation lines, FPP stocks and the finer Agfa, efke, Foma, Fujifilm, Forte, Ilford, ORWO series. Kinds say "Complete" at series level. Series already present were skipped by name match (103 rows).
4. **Camera bodies:** added Alpa, Fujica X, Petri Flex, Praktina, Canon EOS film bodies (origin: EOS 650), Kowa Six, Leica S, Samsung GX, Olympus PEN E-P, Pentax K-01, Olympus Tough (the empty Rugged compact kind now has an entry) and Nikon Coolpix. Body kinds say "No complete list exists; follows the lens-mount list".
5. **Missing years:** 20 version years filled (Fujifilm X-Pro3 to X-H2S, Sony α7R V to α6600, Canon EOS-1D bodies, OM-1). Weston Master gained six dated versions (1939 to 1985).
6. **Sections:** every entry already had `g`; no kind lacked it.
7. Brand register: 13 stubs added to D4_brands.json.

## Remaining, with attempts
- **Wikidata:** COUNT query returned 105 items under camera with a manufacturer; the class breakdown shows camera models are not modelled, so it cannot serve as a canon.
- **Visoflex, DJI DL:** two searches each, no fetchable page; accessory or lens mount only, treated as out of scope.
- **Contax N1/NX, Samsung Kenox film bodies:** searches found no loadable page; left out.
- **Praktina:** amateurphotographer.com gave 403; mikeeckman.com used instead.
- **Gossen historic models and years:** gossen-photo.de lists current models only; second search found no dated page. Versions carry no years.
- **Years still empty:** Fujifilm X-E1 to X-E3, X-T10/20, GFX bodies, Panasonic GH3 to GH5S, Canon EOS M3 to M50 II, Rebel xxxD, Leica TL/SL2, Sigma fp. Comparison pages did not list them (Micro Four Thirds page read to 100,000 characters only). Searched: "Fujifilm X series release dates", "Micro Four Thirds Lumix GH release years".
- **Lens lines:** no reference lists lens lines per mount (searched lens-design and lens-line pages); the 8 lens kinds say so.
- **Film:** repackaged and expired stocks sold by the Film Photography Project appear only as grouped entries; the Wikipedia list gives no dates.
