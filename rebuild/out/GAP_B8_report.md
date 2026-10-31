# GAP_B8 report (Home Safety & Security)

validate.py --v3 out/B8.json: OK. Fetches: about 22 (log: rebuild/work/GAP_B8/sources.tsv).

1. Loose models: none in out/B8.json.
2. Coverage lines: all three kinds with entries now have one. High-security lock cylinder: "Complete: 18 of 18 ... and 15 of 15 ..."; Antique lock & key and Baby monitor: "No complete list exists; follows ...".
3. Partial coverage: High-security lock cylinder went 19 -> 31 entries. Added from the LockWiki list: GOAL V18, Kromer Protector (Wikipedia Protector lock; its LockWiki page 404s). Added from the LockWiki category: Abloy Profile, ASSA dp4400, DOM ix TwinStar, DOM ix Saturn, MIWA 3800, Fichet F3D, Corbin Emhart, DOM RS 8, Hi-Shear LK 1200, Sargent & Greenleaf 951. New sections Pin tumbler and Wafer. Reference exhausted; the list's "Bowley" is not on it.
4. Report gaps:
- Allegion share: closed. Cylindrical door locks, Allegion over 28.5 %, top five 68.3 % (2025, GMI); mechanical locks, ASSA ABLOY + Allegion + dormakaba 50 % (2025, Future Market Insights; its tier tables conflict, noted).
- Spectrum Brands share: searched "Allegion market share residential door locks ... Spectrum Brands"; no figure. Left empty.
- Cameras, doorbells, safes, mechanical-lock leaders per country: not found in the same searches; left empty.
- Brand register: country/year added for Syngenta, Spectrum Brands (country), Allegion, Amerex, Raid, and Kromer; seven lock makers added. About 38 makers remain name-only (Wikidata batch matched none).
- Antique lock entries were not re-fetched (sources are the Wikipedia pages already cited).
5. Sections: all entries carry g.
