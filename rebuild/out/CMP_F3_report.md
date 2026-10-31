# CMP_F3 report

Validation OK (108 kinds). Backup, merge.py and sources.tsv are in rebuild/work/CMP_F3/.

## Per list, before -> after
- Circulation coin 63 -> 83 and Circulation banknote 41 -> 61: Turkey, Saudi Arabia, Egypt, Nigeria, South Korea, Argentina, Indonesia added from their Wikipedia currency articles (first 100,000 characters each, which hold the coin and note tables). Commemorative banknote 6 -> 9 (Saudi 2020 and 2021, Indonesia 2020). Reference total: not a bounded list; each issuer's article is the reference. Covers all seven, with series grouped by issue; old pre-1925 and colonial issues of these countries are not covered.
- Campaign medal 31 -> 138: 86 UK medals from Wikipedia's British campaign medals article (1794 to 2024), plus 21 US Navy, Air Force, Coast Guard and foreign campaign awards.
- Gallantry and merit decoration 63 -> 111, Long-service 6 -> 19, Orders 61 -> 83: Navy, Air Force, Coast Guard, unofficial and foreign sections of Wikipedia's US armed forces awards article, read with WebFetch offsets 100000 to 295367 (page end). Method: WebFetch windows, no Wikidata (no suitable class query).
- Base card 45 -> 118: Topps flagship baseball set for every year 1951 to 2024 (74 of 74 in Cardboard Connection's timeline), card counts from Baseball Almanac where it lists the year.

## Still short
- Wikipedia pages passed through the summariser, so some table rows may be dropped; the UK article was read once, not in windows.
- US Army and Joint award sections (offsets before 100,000 were read in the earlier pass) were not re-read; marksmanship, recruiting and training ribbons are left out as out of scope.
- Beckett's Topps page returned 404; Topps counts exist for only about 40 years. Wikidata SPARQL timed out once and was not retried.
- Coverage sentences were appended to each edited kind's sel. Brand register F3_brands.json not updated for the new central banks.
