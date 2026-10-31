# V4_F1 report (F1 Media & Publications, named-entry pass, medium group)

Validation: `validate.py --v3 out/F1.json` OK (174 kinds, 340 entries). 127 → 174 kinds; entries 215 → 340. About 38 fetches (one Firecrawl, for Goldmine, which WebFetch got 403 on). Sources are in rebuild/work/V4_F1/sources.tsv. Backups are in work/V4_F1/bak/.

## Per kind (entries before → after, reference, coverage)
- **Private press book** 2 → 48. Wikipedia Private press, every named press, grouped by country. Complete: 48 of 48. Kelmscott Chaucer and Doves Bible removed as titles.
- **Edition class** (new, Books) 0 → 13. Wikipedia Edition (book). Complete: 13 of 13 in scope. Book club edition stays its own kind; e-dition and Sustainers' Edition left out.
- **Western sheet format** (new) 0 → 9 and **Japanese book format** (new) 0 → 13. Wikipedia Book size. Complete: 9 of 9 and 13 of 13.
- **Open-reel videotape** 0 → 11, **Broadcast and professional videotape cassette** 0 → 23, **Minor consumer videotape cassette** 0 → 14. Wikipedia Videotape, 70 rows. 10 rows were already kinds; 12 file-based or disc rows (AVCHD, XAVC, P2 and similar) are left to cameras.
- **Specialist and archival optical disc** (new) 0 → 23. Wikipedia Optical disc overview table. Complete: 23 of 23 rows not already kinds. Page read 100,000 of 144,989 characters (table included).
- **Large and widescreen film format** (new) 0 → 13. Wikipedia Film format. New kinds 17.5 mm print and 70 mm print.
- **LP record** (9 entries kept): coverage line added. Phonograph record size and speed table: all 10 rows are kinds. New kinds 16⅔ rpm background-music record and V-Disc. Page read 100,000 of 219,400 characters.
- **Tape**: new kinds RCA tape cartridge and Endless tape cartridge. Covers 9 of 17 rows of Magnetic tape sound recording; the other 8 are pre-1950 experimental or studio tapes.
- **Compact cassette** 8 → 1. Blank-tape brand lines removed under the icon rule; Philips Compact Cassette kept as origin.
- **Collector lines added**: Folio Society, Easton Press (with nine series as versions), Criterion Collection and Arrow Video (new kind Boutique label edition). Owner, tier, country and acquisition year are set only where the fetched page states them (Criterion: Steven Rales 2024; Easton: MBI, Inc.; MFSL: Music Direct 2001; Analogue Productions: Acoustic Sounds, Inc.; Library of America; Penguin Classics: Penguin Random House). 8 owners and 40 or so presses were added to F1_brands.json.
- **Grading registers** (dept notes): Goldmine grades (Goldmine page) in Records & audio; CGC scale and label colours (Wikipedia) in Comics & manga.

## Market panel (Records & audio, `ms`)
US 2024 (RIAA year-end PDF): LP/EP $1,442.9 million (43.6 million units), CD $541.1 million (32.9 million units), total $17.7 billion. UK 2024 (Official Charts Company): vinyl albums £196 million, CD albums £126.2 million.

## Not sourced or still short
- BPI's own pages gave no 2024 format figures; the BPI share could not be fetched. Global (IFPI) format shares not found.
- All other existing entries (comics lines, maps, atlases, antique globes, miniature scores, cylinders and similar) carry a generic `nl` and a `sel` saying no complete canon was fetched; they need a later pass.
- Bookbinding types, remaining Phonograph record text and Penguin Classics detail not read in full.
- Data-storage discs (WORM, MOD, UDO and others) probably belong with computer storage; no moves written (F1_moves.json and F1_renames.json unchanged).
- No `role` badges set: no fetched page called any of these entries first or defining, except Philips Compact Cassette (origin, kept).
