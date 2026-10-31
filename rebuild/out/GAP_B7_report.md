# GAP_B7 report (Portable Climate & Air)

validate.py --v3 out/B7.json: OK. Fetches: 7 (log: rebuild/work/GAP_B7/sources.tsv).

1. Loose models: none in out/B7.json (the reader copy still shows one; all were removed in V4_B7).
2. Coverage lines: Fan heater, Portable air conditioner and Electric fan (design & vintage) now end "No complete list exists; follows ...".
3. Partial coverage: no "Covers" kinds.
4. Report gaps:
- Portable heating panel: closed. Honeywell over 8.5 %, top five 35 % (space heaters worldwide, 2025, GMI).
- Humidifiers: tier figure added (Honeywell, Dyson, Boneco 45 % combined, 2025, Future Market Insights); no per-company shares. GMI page 404.
- Fans overall: searched "electric fan market share Midea Xiaomi Dyson Panasonic ..." and found only vendor key-player lists and a tower-fan figure (not fetched). Left empty.
- National champions and own/tier/cty fields: no entry is branded, so none added; no ranking found by the searches above.
- Brand register: country and year added for Bresser, Candy, Russell Hobbs, Vortice, Davis Instruments, Momcozy from Wikidata items. About 36 makers remain name-only (the batch query matched no business item for them).
- Design fans: MoMA holds Pirali's Electric Fan (1953) and Barman's Electric Fan Heater (c. 1934) per search results, but both pages returned 403; noted in verify/work/GEN/firecrawl_deferred.md. Not added without a fetched page.
5. Sections: all entries carry g.
