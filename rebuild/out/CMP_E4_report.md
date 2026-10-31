# CMP_E4 report: completion pass, Weapons & Armour firearms and ammunition

File: `rebuild/out/E4.json` (backup `rebuild/work/CMP_E4/bak/E4.json`). `validate.py --v3` passes. Sources logged in `rebuild/work/CMP_E4/sources.tsv`; scripts and raw lists in `rebuild/work/CMP_E4/`.

## Method
Wikidata was tried first. "Firearm model" (Q22704163) has 670 items but no action type, and the revolver, pistol and bolt-action classes hold a handful of items or time out, so it could not supply the canon. All kinds were completed from Wikipedia's lists, read in 35,000 to 100,000 character windows with WebFetch offsets until each page ended. Years on the revolver, pistol and shotgun pages come back shifted by a row in some windows; I used a year only where overlapping windows agreed or I could state it, and left the rest blank. Revolver and shotgun actions are not on the pages, so each model is placed by its known action.

## Per list (before to after, reference)
- Single-action revolver 10 to 27; double-action 36 to 167; percussion 14 to 24. Reference: List of revolvers, 194,203 characters, read to the end.
- Semi-automatic pistol 38 to 495. List of semi-automatic pistols, 335,822 characters, read to the last row (Zigana). Not a verified full count: rows the extraction cut or merged are missing.
- Bolt-action rifle 50 to 75. List of bolt-action rifles, all 72 rows, now complete.
- Lever-action rifle 17 to 28. The Lever-action article is read to the end of its text (the last 56,000 characters are references).
- Shotguns: single-shot 3 to 11, side-by-side 6 to 17, over-under 10 to 19, pump 16 to 35, semi-automatic 22 to 48. List of shotguns (158,570 characters) read to Zastava LP 12 PAS. Military, combination and revolving shotguns stay out, as the earlier scope said.
- Centrefire handgun cartridge 54 to 195 (reference about 255 rows, the rest being rimfires and rifle rounds already listed elsewhere). Centrefire rifle cartridge 108 to 426. Rimfire 25 to 39. The rifle list has about 550 rows including duplicates; wildcat, nitro-express and black-powder rounds are now included, plus a new section for autocannon rounds (20 mm and over).
- Shotshell gauges 12 to 51: all 50 numbered gauges and the .410 bore, from the Gauge (firearms) table.

Each `sel` now ends with a coverage sentence.

## Still short
- Pistols and shotguns carry a "Covers" sentence, not "Complete", because the pages' own totals were not available and some rows were merged by the extraction.
- Most new firearm entries have a generic one-sentence description (country, type, maker, year); the lists give nothing more. No `role` badges were set.
- Years are blank for many pistols and revolvers (see above). Cartridge entries carry no year, since the cartridge pages give none.
- Overlapping names (for example Glock beside Glock 17) were kept; a few duplicates under different spellings may remain.
- Cartridge classes follow the nominal calibre in the name, matching the existing entries; some existing entries sit in a neighbouring class.
