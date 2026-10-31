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

# Round 2

Fetches: 94 MediaWiki API intro extracts (20 titles per call), logged in progress.md; decisions in rebuild/work/GAP_G1/dec2_cars.tsv and dec2_moto.tsv. Validation: OK (0 errors, 247 kinds, 12,870 entries).

1. **Article titles finished.** Cars from Plymouth to the end of the alphabet and motorcycles from Yamaha to the end were read.
2. **List and category entries.** About 1,260 car names were tried as titles with redirects; roughly 40 % resolved, mostly to the same model. Redirects to a different model (for example Chevrolet Aska to Isuzu Aska) were applied only for true rebadges. About 100 motorcycle names from Kawasaki, Harley-Davidson, Triumph, Peugeot and Bimota gave almost no pages (model-code rows have no article), so that route was stopped.
3. **Totals.** "Car, body style not stated": 2,155 to 1,780 (about 375 moved on a stated body style; 625 of the remaining 1,780 still lack a year). "Motorcycle, type not stated": 1,996 to 1,966 (1,128 of them without a year). Blank years across G1: 7,003 to 6,704.
4. **Step 5 (sections).** Nothing to do: every entry in every kind already carries `g`, and every kind with entries has `xg` except Utility coupé (7 entries) and Full-face helmet (1).
5. **Coverage lines** on the two unstated kinds and the 26 car kinds updated to the new counts.

Still open: about 1,780 cars and 1,966 motorcycles without a stated type. The searched titles that returned "missing" are the evidence that no Wikipedia article exists; the remaining model-code rows (Kawasaki, Benelli, BSA, Norton, Moto Guzzi, Laverda, Greeves lists) were not tried in bulk because the sample gave no pages. Unread list batches: Toyota rebadges (Reiz onward), some Mazda numerals, and Lada VAZ codes.
