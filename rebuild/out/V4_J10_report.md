# V4_J10 report: named-entry pass, J10 Smoking & Vaping

Edited: rebuild/out/J10.json, J10_brands.json (renames and moves unchanged). Validator: OK (131 kinds). Backups and apply script: rebuild/work/V4_J10/. About 17 fetches used (one via Firecrawl: Pipedia returns 403 to WebFetch).

## Per kind (entries before -> after)
- **Habano (Cuban premium cigar)**: 29 line entries -> 27 marque entries, complete. Reference: Habanos Brands-Academia page (27 of 27, tiers global/high value/volume/rest in `g`). Earlier line entries became versions (vitolas) of their marque; the three loose models (Por Larranaga, Rafael Gonzalez, Sancho Panza) became an entry or version. Eleven marques have no vitola list because no page with it was fetched (not fabricated). Montecristo marked landmark.
- **Dominican / Nicaraguan / Honduran / Mexican & Brazilian**: 8/13/4/3 -> 23/18/9 (+Windsor)/4, from Wikipedia List of cigar brands (three windows, rows A to Z as summarised). Owner, tier, country on every entry; Padron, CAO, Rocky Patel, Drew Estate and others show "owner not stated" because the list gives none. Coverage line says "Covers"; country-less rows are unplaced.
- **Cigar from other countries** (new kind): 0 -> 18 (Costa Rica, Mozambique, Philippines, Indonesia, Netherlands, Greece, Australia, Iran, Belgium, US).
- **Briar pipe**: 11 -> 39; **Freehand** 6 -> 7; **Calabash** 0 -> 2. Reference: Pipedia pipe shapes navigation box (44 shapes; Chimney, Tools and Freehand excluded). "Complete: 44 of 44". Descriptions only where Pipedia's Billiard essay gives them; others say they are listed in the index. Four freehand loose models (Elephant's Foot, Fig, Olifant, Ramses) removed, no page.
- **Heated-tobacco device**: 0 entries (6 loose models) -> 13 systems (IQOS landmark, glo, Ploom, lil, Pulze, Mok, TEEPS, Premier, Eclipse, Accord, Heatbar, Cigoo, TEO) with maker, tier, year, versions. Source: Wikipedia Heated tobacco product (first 100,000 characters only; page is 226,000).
- **Vape lines**: Juul (landmark), Vuse, NJOY, Elf Bar, blu, Ruyan, eGo added with owner; 11 loose models (SMOK, Vaporesso, OXVA, VooPoo, SKE) removed, not on a fetched page. Source: Electronic cigarette (first 100,000 characters).
- **Cigarettes, RYO, kretek**: 19 existing entries got own/tier/cty from the company pages; unstated owners marked.
- **Cannabis flower**: 11 strain names removed (commodity; no canon). Other cannabis and herbal kinds untouched.

## Market panels (`ms`, with years)
Cigarettes: CNTC 47 % global volume (2025), big four just over 34 % (2025), 66 % outside China (2025), markets led PMI 38 / BAT 24 / JTI 8 / Imperial 6 of 90 (2020) from Tobacco Tactics; company revenues PMI, BAT, Imperial, Altria (2025) and JT (2012); CNTC about 96 % of China and JT 66 % of Japan (no year on page). Vaping: Juul over 72 % and Vuse under 10 % (Aug 2018), Vuse Alto about 40 % (52 weeks to 15 June 2024). Cigars: Habanos ownership.

## Not sourced
Individual PMI/BAT/JT/Imperial/Altria shares (chart only), Habanos vitola lists for 11 marques, non-Cuban owners for rows the list leaves blank, Wikipedia list tables (summariser scrambled columns, so rows are best readings), loose models remaining in untouched kinds (humidor, lighter, vaporiser, hookah, snus). Brand register +42 entries; group brand portfolios added as `lines`.
