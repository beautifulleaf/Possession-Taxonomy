# GAP_E4 report

File: rebuild/out/E4.json (validates OK, 2,341 archetypes). Backups in rebuild/work/GAP_E4/bak/. Sources in rebuild/work/GAP_E4/sources.tsv. About 20 fetches used.

## Closed
1. Loose models: none left (no kind keeps `m`).
2. Coverage lines: every kind with entries now ends with "Complete", "Covers n of about m" or "No complete list exists; follows the overviews named above".
3. Partial coverage:
   - Semi-automatic pistol: list re-read by names in six windows (all 335,822 characters). Eight missing rows added (Erika, Raven MP-25, Ruger Security-9, Type 70, Type 80, Type 64 and 67 silenced, Claridge Hi-Tec); the rest of the page's rows were already entries or are merged range rows. Now stated as Complete.
   - Shotguns: list of shotguns re-read in full by names. Added pump (Remington 870, Stevens 520/620, Norinco HP9-1, MAG-7, NeoStead 2000), semi-automatic (Atchisson, AAI CAWS, USAS-12, HK CAWS, SPAS-12 and SPAS-15 as dual-mode, Fabarm SDASS, Jackhammer) and five combination guns. The earlier exclusion of tactical and military pump and semi-automatic guns is lifted.
   - Plate carrier (+6) and Ballistic helmet (+26): List of armour types read to its end; both now stated against that page.
4. Report gaps: Denix founded 1967 (denix.es, fetched; brand file updated); Shinto (1596 to 1781) and Shinshinto (1781 to 1876) dates and schools added to the Sword tradition `sel` (japanesesword.net, fetched). Two blank years filled from Wikidata.

## Remains
- Shotguns: about 90 page rows are not placed. The page has no action column and I would not guess: bolt-action (Mossberg 183/185, Marlin 55 and 25MG), lever-action (Winchester 1887/1901), revolving (Striker, Six12, Pentagun, Becker), and rows whose action I could not state (IZh, MTs and TOZ models, Bekas-M, Safir T-14, Hunt MH12, K12 PUMA, GEN-12 and others). Searched: the page by names in two windows. A Wikidata action property does not exist for this class.
- Most firearm entries have no year: Wikidata's firearm-model class gave years for only a few matching names, and years from the Wikipedia windows are scrambled.
- Barra 270z (PCP placement) not confirmed: retailer page returned 403; the entry is not in the file, so nothing depends on it. Logged in firecrawl_deferred.md.
- No `role` badges: no fetched page names a first or best-selling entry.
- Armour: Kelly gang armour, Brewster Body Shield and Steel Bib left out of Plate carrier (historic one-offs, not carriers).
- Sections: every kind over 12 entries already has the section axis; no `g` missing.
