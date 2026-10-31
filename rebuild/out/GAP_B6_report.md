# GAP_B6 report (Cleaning & Laundry)

validate.py --v3 out/B6.json: OK. Fetches: 7 (Wikidata batch, Euromonitor Germany, GMI x2 (one 410), Mordor, Wikipedia Henkel, Arm & Hammer). Log: rebuild/work/GAP_B6/sources.tsv.

1. Loose models: none left in out/B6.json (all removed in V4); nothing to resolve. Removals were listed in V4_B6_report.
2. Coverage lines: the four kinds with entries (Cylinder, Upright, Robot, Wet and dry vacuum cleaner) now end "No complete list exists; follows the design-collection and award pages named here."
3. Partial coverage: none ("Covers" kinds: 0). A search for further vacuum cleaners in the ADI Compasso d'Oro collection found only the Bidone Lavatutto, already held.
4. Report gaps:
- Household cleaning shares: closed at global level. P&G 12.1 %, Unilever 5.6 % (2025, GMI); added to Cleaning products. The page gives two different top-five totals; noted. Dishwashing-only shares: searched "household cleaning products market share P&G Reckitt Unilever SC Johnson Clorox"; only one vendor, no dishwashing split.
- Regional leaders: Germany vacuums, Dyson 18 % and Miele 9 % (2025, Euromonitor). Other regions: searched "European vacuum cleaner market share Miele Bosch Vorwerk Dyson Electrolux ranking"; only satisfaction surveys and a UK Statista figure seen in an excerpt, not fetched.
- Dryers: Europe leaders named (BSH, Miele, Electrolux, Beko, Haier Europe; combined below 50 %, 2025, Mordor); no brand shares. Searched "tumble dryer market share Europe Bosch Miele Electrolux Beko". Irons: not searched beyond this (no ranking found in the first query).
- Brand register: country/year added from Wikidata items or Wikipedia for Henkel (Germany, 1876), Aldi, AEG, Kenmore, Downy, Febreze, OxiClean, Swiffer, Pledge, O-Cedar, Magic Chef, OXO, Ewbank, Arm & Hammer (year withheld: Wikipedia 1846 and Wikidata 1867 disagree). About 42 makers remain name-only; the one Wikidata batch matched ambiguous labels for the rest.
5. Sections/axis: all four entries carry g; no kind has over 12 entries.
