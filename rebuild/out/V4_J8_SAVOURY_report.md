# V4_J8_SAVOURY report (restructured)

Part file: rebuild/out/J8_parts/SAVOURY.json (about 345 KB; validates OK, 64 kinds). Built by rebuild/work/V4_J8_SAVOURY/build2.py; the first version is in work/.../bak/SAVOURY_v1.json. Replaces Bread & bakery; Crisps & savoury snacks; Snack nuts & bars.

**Structure.** Tier shelves are gone. Every brand sits in the product kind of its flagship product (Lay's in Potato crisps, Pringles in Stackable crisps, Doritos in Tortilla chips, Bimbo and Warburtons in Sliced & tin loaf, KIND in Fruit & nut bar). `g` is the owner group for global-group brands, otherwise the tier name; `xg` is "by owner group, then tier". Own, tier, cty and own_y remain for the market view. Protected names are entries in their product kinds (Pane di Altamura in Italian bread, Lebkuchen in Gingerbread & Lebkuchen, Pastel de Tentúgal in Turnover & strudel), with g "Protected name". Shelf "Bakeries" holds kind "Artisan bakery".

**Entries.** Bread & bakery 129 → 315 (218 bakeries); Crisps & savoury snacks 47 → 157; Snack nuts & bars 0 → 33 (four nut brands moved here from crisps). Brand register: 468 new, 31 updated. Where a page did not state a brand's flagship product the nearest kind was used.

**Gaps filled.**
- Loaf Mark: the page states a total of 219 (205 UK, 14 outside); all 219 are in. The earlier "about 250" was a summariser estimate. One exact duplicate merged.
- Protected names: now 27, from the Italian protected-status list on Wikipedia (six bakery rows with dates), Wikidata, and EU registration regulations (Bayerische Brezel, Štramberské uši, Alfajor de Medina Sidonia, Skalický trdelník, Gâche vendéenne, Salzwedeler Baumkuchen, Dresdner Stollen, Daujėnų naminė duona, Liers vlaaike, Valašský frgál, Zagorski mlinci, Poljički soparnik). No per-country Wikipedia list of bakery names exists except Italy; the EU register (eAmbrosia) is JavaScript-only. Not entered: wafer and confectionery names (Hořické trubičky, Andruty kaliskie, Loukoumi Geroskipou), and Brioche vendéenne, Piadina's regulation, Mantecados de Estepa, Mazapán de Toledo, Lesachtaler Brot and Pan de Alfacar (regulation pages empty or unfetched).
- Market figures added: Harry-Brot over 40% of German pre-packaged bread (2025); Intersnack 22% of German sweets and salty snacks by packs (2024); France 2005 Lorenz Bahlsen 17.63% and Pepsi 14.95% of sweet and savoury snacks; Lay's 59% of US savoury snacks (2012); Sabritas about 80% of Mexico (undated). Brazil: Bimbo's Wickbold deal (September 2024) but no share found for bread or snacks; France bread: none.
- Africa and Middle East: PepsiCo's Simba (South Africa, 1957, bought 1995), NikNaks and Ghost Pops added, plus Albany, Tinkies and SASKO earlier. No Middle East snack or bakery champion could be sourced.
- Brazil brands added from the Elma Chips page: Cebolitos, Zambinos, Ovinhos, Fofura; Wickbold and Seven Boys under Bimbo.

**Removed as unsourced (earlier list unchanged):** Mother's Pride, Schär, Mission, Krispy Kreme, Dunkin', Tim Hortons, Mr Kipling, Golden Wonder, Torres, Terra, Grenade, Barebells, Nakd, Eat Natural, Beer Nuts and similar.

Fetch count in this pass: about 40 (EU regulation pages count). Sources: rebuild/work/V4_J8_SAVOURY/sources.tsv.
