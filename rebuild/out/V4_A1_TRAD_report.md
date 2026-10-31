# V4_A1_TRAD report (Traditional dress)

Part file: rebuild/out/A1_parts/TRAD.json (replaces "Traditional dress"; validates OK: 55 kinds, 374 entries). Build script: rebuild/work/V4_A1_TRAD/build.py.

**Cloth shelf dissolved.** "Named cloths & textiles" (13 kinds) is gone. A "Cloth" tt group (Kente, Wax print, Batik, Shweshwe, Bogolan, Adire and aso-oke, Ikat, Songket and tenun, Khadi and handloom, Faso Dan Fani, Tapa and masi, Tartan, Tweed) now sits on Sari, Dupatta, Dhoti, Kimono, Dashiki, Kaba and slit, Boubou & agbada, Southern African dress, Kebaya, Sarong, Baju kurung, Pacific island dress and Kilt. Each carries a `ve` list "Named cloths covered by the visual-art taxonomy" with the removed entries (full list in rebuild/work/V4_A1_TRAD/dropped.json). Tweed is attached to Kilt only as the nearest Highland garment. The `see` field accepts only A-J codes, so the visual-art pointer is in `sel`/`ve`, not `see`.

**Loose models.** 46 `m` and 15 `r` removed: all were brand collections or products (Manyavar, Sabyasachi, Khaadi, SOU·SOU, Tchai Kim, Carla Fernández, MOSER Trachten, Africa Imports and similar), not signature pieces of an originating brand; the brands stay in A1_brands.json. Kira and Kashmiri jamawar sari were unsourced and removed. Signature-piece entries kept with source: Pampero Bombacha de campo, Ecualama Otavalo poncho, Vlisco Angelina dashiki, Vita Kin vyshyvanka (cty added; no owner or tier facts fetched, so none given).

**Entries before → after (fetched Wikipedia lists).** Sari 16 → 98 (sectioned by region; fabrics, embroidery and print techniques left out, listed in sel); Dhoti 2 → 9 (complete); Sarong 15 → 36; Shalwar kameez 4 → 21; Kurta 5 → 13 (complete); Poncho 8 → 10; Kaftan 7 → 15; Thobe 6 → 7; Kimono 14 → 17 (+3 furisode sleeve versions); Bunad 2 → 5 (article says about 200 exist). `g` sections and `nl`/`sel`/`xg` added for these; one origin badge each on Dhoti (Antariya) and Kimono (Kosode).

**Where I stopped (not finished).**
- Sarong, Shalwar kameez, Poncho, Kaftan and Kimono pages were read only to the first 100,000 characters; later windows unread, so their coverage lines say "Covers", not "Complete". Sari read to 200,000 of 205,520.
- All other kinds (Kebaya, Hanbok, Hakama, Obi, Haori, Ao dai, Baju kurung, Lehenga, Sherwani, Dirndl, Kilt, Huipil, Pollera, African dress and the rest) keep the structure-pass entries; their Wikipedia list articles were not re-fetched, so no completeness claim and no `g` sections. Their `sel` says so.
- No `own`, `tier` or `own_y` market facts were sourced; no `ms` summary written (not a market department).
- Garment-brand Layer 2 canon (originators in Wikipedia garment articles) not checked beyond the register keyword scan, which found no further originator signature pieces for these kinds.
- Fetches used: 12 of about 60.
