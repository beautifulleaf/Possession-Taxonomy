# V4_B8 report (light pass, B8 Home Safety & Security)

validate.py --v3 rebuild/out/B8.json: OK (0 errors, 78 kinds).

## Commodity kinds
76 kinds lost all loose models (245 m) and ranges (37 r). Padlock (4 named entries) and Lock pick set (3) were treated as commodity: their entries were removed and the makers kept in the brand register. 45 makers not already registered were added to B8_brands.json (name only; country only for Fichet France, WEST Japan, since fetched pages say so; no founding years).

## High-security lock cylinder: 12 -> 21 entries
Reference: LockWiki "High security locks" list (18 locks) and its category page, both fetched. Grouped by mechanism (disc detainer, sidebar and pin tumbler, lever, magnetic, dimple). Kept the 12 earlier entries (including Medeco M3, Mul-T-Lock MT5+, Abloy Protec2, EVVA MCS, BiLock). Added entries: Abloy Easy, EVVA ICS, Fichet 787, Opnus Memolis, Rosengrens RKL-10, STUV Ivox 4.19.97, WEST 917, all from fetched LockWiki pages. BiLock NG added as a version of BiLock. ASSA Twin V-10/Combi and Schlage Everest 29 SL Primus XP were already versions. nl, sel, xg and g set; roles: Abloy Protec2 and EVVA MCS landmark (earlier pages).
Not added: GOAL V18 and Kromer Protector (on the list, but their LockWiki pages returned 404 and no fetched page supports a description). "Bowley" from the prompt was not found on the LockWiki list and is not included.

## Antique lock & key: 8 entries kept
nl, sel, xg (period) and g added; role origin on Egyptian pin lock and Barron lever lock (their descriptions already say ancestor/first). Sources are the earlier Wikipedia pages; not re-fetched this pass.

## Market panels
- Locks & door security: consumer smart locks, ASSA ABLOY 21 %, 2021 (Strategy Analytics via SecurityWorldMarket, fetched through Firecrawl after a WebFetch 403).
- Alarms, cameras & doorbells: US/Canada residential monitored security, ADT about 30 %, ADT's own estimate in its January 2018 S-1/A (fetched).
Not sourced: Allegion, Spectrum Brands shares (only unreliable secondary search excerpts, not used), mechanical locks, cameras, doorbells, safes.

Files edited: B8.json, B8_brands.json (B8_renames.json and B8_moves.json unchanged). Backups and sources.tsv in rebuild/work/V4_B8/. About 17 fetches used.
