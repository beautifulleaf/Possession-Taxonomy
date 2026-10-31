# GAP_F1 report (Media & Publications)

Validation: `validate.py --v3 out/F1.json` OK (174 kinds). Backups in work/GAP_F1/bak/. About 9 fetches and 6 searches (sources.tsv).

## 1. Loose models (351 `m` rows, none left)
- 155 became entries and 93 became versions, recovered with their fetched source, description and year from the earlier pre-demotion data (work/STR_F1/bak). Examples: Replogle and Bellerby lines, Criterion and Arrow lines, Aldine, Elzevir and Baskerville editions, Dutch map houses.
- 54 removed: 24 storage-product SKUs (BCW, Gerber, Brodart and similar bags, boards, sleeves, boxes), and 30 named lines with no fetched source. "Term coined" dropped as an attribute.
- Rescued by fetch: Essential Marvel (1996-2013), Showcase Presents (2005-2016), Harper Torchbooks (1956).
- Still removed, no fetched page: Kadokawa Shinsho, Ace D/G/S, Pocket Poets, Harper's Perennial, Panther Crime Circle and Crimeband, HDAD, Marvel Premier Collection, Marvel-Verse, DC Compact Comics, Kadokawa Comics Ace, DC Finest, DC Deluxe Hardcovers, Dynamite Definitive, Atlas Artist Edition, Marvel Gallery Editions, Fjallkartan, TOP 250, Discoverer, Veikart, AA and Philip's and A-Z atlases, Bildkarten and A-Z wall maps, Duo Azzurro Imperator, Sherbrooke II, Suspension Old World Globe.
  Searched: "Harper Torchbooks Wikipedia" (publishinghistory page only), "Ordnance Survey Explorer Landranger Discoverer ... Wikipedia" (retail pages only), "HDAD ... Classic Records" (forum and Stereophile excerpts, no fetch).

## 2. Coverage lines
93 kinds gained "No complete list exists; follows ..." naming the page their entries cite. Every kind with entries now has a coverage line.

## 3. Partial coverage
- Manga anthology magazine 3 -> 179: Complete, 179 of 186 rows in Wikipedia's List of manga magazines (read to the end); 7 adult-content magazines out of scope. Sectioned by readership demographic.
- Private press book: 10 duplicate "X book" entries merged into the press entries (versions kept); 50 entries.

## 4. Gaps not closed
- No whole-space reference was found or fetched for: books (hardback, paperback, novelty), records (78 rpm, cylinder, transcription), films, comics lines, maps, atlases, globes, sheet music. "List of pulp magazines" has no Wikipedia page; only a third-party list (storytellingdb) turned up and was not fetched.
- BPI and IFPI format figures (market panel) still not found.

## 5. Sections
Edition class (by purpose), Private press book (Cranach, Grabhorn), LP record (by kind of release) now sectioned. Other kinds are under 13 entries.
