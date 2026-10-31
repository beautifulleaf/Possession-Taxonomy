# GAP_G1 report

Budget used: 59 WebFetch calls, all MediaWiki API intro extracts (20 titles per call), logged in rebuild/work/GAP_G1/sources.tsv. Decisions are in rebuild/work/GAP_G1/dec_cars.tsv and dec_moto.tsv; applied by apply.py. Validation: OK (0 errors, 247 kinds, 12,870 entries). Backup: rebuild/work/GAP_G1/bak/G1.json.

## 1. Loose models
No kind holds `m` (checked: 0).

## Priority 1: unstated body style and type
- Car, body style not stated: 2,348 to 2,155. About 193 models moved on the body style the intro states (Saloon, Luxury saloon, Hatchback, Estate, MPV, SUV, Coupé, Convertible, Roadster, Sports car, Grand tourer, Limousine, Muscle car, Supercar, Hypercar, Microcar, City car, Off-roader, Kit car, Track and racing car, Three-wheeled car, Taxi, Panel van). Only a stated word was used; "compact executive car", "large car" and similar were not mapped.
- Motorcycle, type not stated: 2,134 to 1,996. About 138 moved (Sport, Standard, Touring, Cruiser, Adventure, Dual-sport, Enduro, Motocross, Supermoto, Scooter, Moped, Mini bike, Trike, Scrambler, Café racer, Quad bike). Racing prototypes stay put, since no kind holds them.
- Read: about 660 car and 480 motorcycle titles of the 1,088 and 592 that have a Wikipedia article page in `s`. Not read: the later alphabet (Plymouth onward for cars, Yamaha onward for motorcycles) and every entry whose `s` is a category or list page (1,260 cars, 1,540 motorcycles). Budget ran out.

## Priority 2: first years
179 car and 135 motorcycle years were set from intros (year ranges as stated; a single "introduced" year where no end was given). Blank `y` overall: 7,003 entries remain; the unread titles above hold most of them.

## Priority 3: coverage lines
Added or corrected on 46 kinds: 16 small motorcycle types, Utility coupé, Full-face helmet, Locomotive ("No complete list exists; ..."), the 26 car kinds whose counts were stale ("Covers n of about 7,585 ..."), and the two unstated kinds.

## Not done
- Steps 3 to 5 of the common brief (partial-coverage reading, report gaps from V4/CMP/STR reports, section axis for kinds with `xg`) were not reached.
- Redirect hazard: the API follows redirects, so some returned pages differ from the entry (e.g. Chrysler Shadow to Dodge Shadow). Only pairs that are the same model (rebadges) were applied; doubtful ones were skipped.
- No Firecrawl calls; no 403s met.
