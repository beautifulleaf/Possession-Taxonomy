# V4_B3 Lighting named-entry pass (final)

**Result:** 297 named entries (was 144 after the first pass; 141 added here). validate.py --v3: OK. Sources logged in work/V4_B3/sources.tsv.

**Canon kinds** (Table, Floor, Desk, Pendant, Chandelier, Wall, plus Flush ceiling and Lamp shade for museum landmarks): sections by decade of design.
- MoMA Design classification, search "lamp": 191 results, all four pages read (Firecrawl; WebFetch gets 403).
- Vitra Design Museum online collection: Floor lamp 5, Table lamp 8, Pendant lamp 1, keyword "lamp" 28 (Firecrawl, script-driven page).
- V&A: museum search API, lamp records from 1900, pages 1 to 5 of 6 (about 80 usable lamp records; untitled, stage-design and non-lamp records skipped).
- Design Museum London: Anglepoise holdings (versions of Anglepoise 1227).
- ADI Design Museum: item pages for Eclisse, Lola, Tolomeo, Counterbalance, Mix, IN-EI, Ascent, Metropoli, Shuttle fetched.
- Lightology: 23 of 41 lamps (type stated).

**Not obtainable:** the full ADI Compasso lighting list. The ADI site's category filter is script-driven, the English Wikipedia page has no winners table, the Italian edition page is 404. Winners found are listed above plus those on Wikipedia and Casa di Luce. MoMA Product design and Furniture classifications were not searched. Page 6 of the V&A results was not read.

**LIFX:** Wikipedia returned 404; entry added from a 9to5mac article (Feit Electric bought it in 2022; previous owner not named). Founding year and country are not on fetched pages.

**Owners (step 6):** fetched pages do not name owners. Artemide (Italy, privately held), Louis Poulsen (Denmark, privately held) and Fritz Hansen (Denmark, privately held) have `cty` set and are in the brand register with no owner. Flos, Foscarini, Anglepoise, Vitra and Gubi pages were 404, disambiguation pages or silent on ownership. Design Holding, Investindustrial and Diesel are therefore not recorded.

**Loose models (m):** of 392 removed in pass 1, 16 are restored as entries or versions (Lumiere, Buds, Bon Jour, Lampadina, Birdie, Magneto, Gregg, Aplomb, Spokes, Caboche Plus, Topolino, Twiggy, Orbital, Gibigiana, Taraxacum88, Nanoleaf One, Zettel'z). The other 376 stay removed because I found no fetched page naming the design and designer within the fetch budget; they are listed in work/V4_B3/m_removed_status.json (mostly retail SKUs of IKEA, Eglo, Lindby, Lucande, Hinkley and torch/headlamp models of Nitecore, Olight, Fenix, Streamlight, Petzl, Ledlenser). This part is not finished.

**Market panel and torches:** unchanged from the first report.
