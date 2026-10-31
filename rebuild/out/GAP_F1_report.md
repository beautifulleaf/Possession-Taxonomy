# GAP_F1 report (Media & Publications), passes 1 and 2

Validation: `validate.py --v3 out/F1.json` OK (174 kinds). Backups in work/GAP_F1/bak/. About 40 fetches in all (sources.tsv).

## Pass 1
- All 351 loose `m` rows resolved: 155 entries and 93 versions restored with their fetched source; 54 removed (24 storage SKUs, 29 unsourced lines, one attribute row). Rescued by fetch: Essential Marvel, Showcase Presents, Harper Torchbooks.
- Coverage line on every kind with entries. Manga anthology magazine 3 -> 179 (Wikipedia list read to the end; 7 adult-content magazines out of scope). Private press duplicates merged; Edition class and LP record sectioned.

## Pass 2
1. **Commodity check of the restored entries.** Removed again, not origin or landmark: Recordable and Prerecorded MiniDisc; Wire recorder spool and Dictabelt (Wire recording now has no entries); Ampex pre-recorded tape; Pre-recorded musicassette; Olympus "Microcassette" (duplicate of the kind); Steelbook edition; Newsstand bookazine and the five Future/Imagine bookazine series; Dover full-score reprint; Novello octavo; the three Tin Pan Alley size rows. Collector kinds (private press, bindings, labels, prints, globes) keep theirs.
2. **Whole-space references.**
   - Pulp magazine 3 -> 885 (882 titles plus 3 genre families): StorytellingDB's list, third-party, read in six windows to row 882. Complete: 882 of 882. Sectioned by decade.
   - Antique atlas and Atlas: Wikipedia List of atlases. Antique atlas 7 -> 23 (15th to 19th century), Atlas 4 -> 12 (20th century, every printed atlas; 8 digital map services and the Piri Reis Map left out). Sectioned by century.
   - Antique globe 4 -> 69 and Desktop globe 4 -> 30: Omniterrum's globe makers list, sectioned by country (Archimedes left out; his page row is not a maker of surviving globes).
   - Oxford World's Classics added to Paperback book.
3. **Records & audio market panel**, five facts added: IFPI 2024 (physical 16.4 % of global revenue per Music Business Worldwide; vinyl up 4.6 %; total US$29.6 billion), BPI UK vinyl LP 5.9 million units and CD nearly 11 million units (2023, provisional), BPI cassette 195,000 units (2022).

## Not closed (searched)
- Comics: no general Wikipedia list of imprints (only DC and Dark Horse lists; the DC reprint page lists title volumes, content). Searched "list of comic book imprints publishers". Marvel and DC reprint lines (Premier Collection, Marvel-Verse, DC Finest and others) stay out.
- Maps: no list of map series exists; searched "Ordnance Survey ... list of map series" (retail pages only). OS, IGN and USGS series stay as entries without a canon.
- Sheet music: IMSLP's publisher table is thousands of historic firms (first window A to M read), not an edition canon; Wikipedia has no list. Not added.
- Books: no "list of book series" page for collector series; searched "list of book series paperback collector series".
- BPI 2024 and IFPI 2024 vinyl/CD value figures: BPI's 2024 pages fetched held no format figures; IFPI gives them only in its paid edition. Search excerpts quoted vinyl 6.7 million units and £145.7 million (BPI) but no fetched page confirms them, so they are not used.
