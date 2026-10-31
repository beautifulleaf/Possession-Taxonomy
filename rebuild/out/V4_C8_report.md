# V4_C8 report (Building Materials & Hardware, light pass)

Result: all 185 kinds are now commodity kinds; validate.py --v3 gives OK (0 errors, 0 archetypes).

Per kind (before -> after):
- 211 loose models (m) and 27 ranges (r) removed from 50-odd kinds (paint, fixings, adhesives, batteries, fuel, plumbing, ironmongery, aggregates, fencing).
- 95 named entries (x) removed from 27 kinds, as the batch prompt says heritage materials are commodity too. These were: Roof tile and slate (6), Lime mortar and render (2), the tile kinds and other heritage kinds (encaustic, Delft, azulejo, cement, zellige, Talavera, terracotta, reclaimed brick and flooring, chimney pot, salvage), garden gravel and stone kinds, Wall and ceiling paint (5 colours), Furniture paint, Wallpaper (17), Door handle (6), Door knocker, Latch, Lithium-ion cell (9), lump charcoal and briquettes.
- Full removed content is kept in rebuild/work/V4_C8/removed.json; originals are in rebuild/work/V4_C8/bak/. Heritage traditions remain in C8_traditions.json.
- No kind keeps or gains named entries, so no nl/sel/xg was needed. t, ax, tt and see are unchanged.

Brand register (C8_brands.json): 51 -> 146. 95 makers added, taken from the removed models, ranges and entries. Only the ones below carry country and founding year, each from a fetched Wikipedia page: PPG Industries (US, 1883), AkzoNobel (Netherlands, 1994), Nippon Paint Holdings (Japan, 1881), RPM International (US, 1947), Axalta (US, 1866 as the page states), Asian Paints (India, 1942), Kansai Paint (Japan, 1918), Jotun (Norway, no year on the page). The rest are name-only with a one-line description.

Market panel (Paint & decorating, ms + msum):
- Global top 10 by coatings sales, 2025 (Asian Paints and Kansai: FY to March 2026): Sherwin-Williams about $19.8bn, PPG $15.9bn, AkzoNobel about $11.48bn, Nippon Paint about $9.63bn, RPM $7.37bn, Axalta $5.117bn, BASF Coatings about $4.63bn, Asian Paints about $4.08bn, Kansai about $3.94bn, Jotun about $3.31bn. Source: PCI 2026 Global Top 10.
- North America top 7, 2025: Sherwin-Williams, PPG, RPM, Axalta, Behr (about $2.34bn), Benjamin Moore (about $2.0bn), Pittsburgh Paints (about $1.88bn, PCI estimate). Source: PCI 2026 PCI 25.
- These are sales figures, not market shares; the panel says so.

Not sourced: market shares for any other market; each group's brand portfolio (Dulux, Crown and others have no fetched owner page); country and year for the 87 name-only makers. Power-tool batteries are already in C1, so no panel was added here.

Fetches: about 13 (WebFetch only; logged in rebuild/work/V4_C8/sources.tsv, though the eight Wikipedia founding-year fetches are listed only in this report).
