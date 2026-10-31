# V4_A5_WRIST report

Part file: `rebuild/out/A5_parts/WRIST.json` (replaces "Wristwatches"). Validator OK: 28 kinds, 277 entries, about 244 KB.

**Entries before → after (all kinds):** 184 → 277. Largest: Digital watch 11 → 38 (G-Shock series from the G-Shock page), Dress watch 24 → 39, Dive 30 → 32, Chronograph 23 → 30, Pilot 11 → 20. Each kind has `nl`, `sel` with coverage line, `xg` (maker country, maker, year); each entry has `g`, `own`, `cty`, and `tier`/`own_y` where a fetched page supports them. About 8 role badges (origin or landmark), each per a fetched page.

**References:** Wikipedia pages of 26 makers/lines (Rolex, Omega, Seiko, G-Shock, Grand Seiko, Patek, AP, Cartier, Breitling, TAG Heuer, IWC, JLC, Longines, Tudor, Hamilton, Zenith, Tissot, Panerai, Vacheron, Swatch, Bulova, Lange, Hublot, Junghans, Citizen, Casio); Category:Watch models and its Rolex (15 of 15), Omega (10), Casio (11), Timex (4) subcategories; Wikidata instances of watch (Q178794, 141 items, about 50 named wristwatch models, rest are museum objects).

**Loose models (51 `m`):** converted to versions where the line is an entry (Royal Oak Perpetual Calendar and Repeater Supersonnerie, Code 11.59 RD#4, Octo Finissimo Ultra Tourbillon, Portugieser Grande Complication); promoted to entries (Omega Bullhead, IWC Grande Complication 3770); the rest removed as single-SKU pieces of independents with no page fetched this session (Mr Jones, Ming, Voutilainen, Kudoke, MeisterSinger, Laurent Ferrier, Andersen, Daniel Roth, Chopard, Dior, Genta and others; list in `work/V4_A5_WRIST/removed.json`).

**Market layer:** `ms` has 17 facts: Swiss exports CHF 25,552 million in 2025 (-1.7 %), US about 17 %; Morgan Stanley/LuxeConsult shares for 2024 (Rolex about 32 %, Big Four 47 %, LVMH just under 6 %) and 2025 turnover (Rolex about CHF 11 bn, Cartier 3.5 to 3.6, AP 2.6, Patek 2.5, Omega 2.2, Richard Mille 1.7); group revenue for Swatch Group, Richemont, Citizen, Seiko, Casio, Fossil, Movado; Patek and AP output. Owner years: Longines 1983, Blancpain 1992, Breguet 1999, Vacheron 1996, IWC/JLC/Lange 2000, TAG Heuer/Zenith 1999, Hublot 2008, Bulgari 2011, Bulova 2008, Zodiac 2001, Breitling 2022, Patek (Stern) 1932, Junghans 2008. Tiers: Global group = Swatch, Richemont, LVMH; National champion = Seiko, Grand Seiko, Citizen, Casio; others Independent. 12 brand-register entries added, 35 brand updates.

**Not sourced / short:**
- Watchbase was not tried (blocked per earlier report); makers without a fetched page (Sinn, Oris, Nomos, Orient, Richard Mille, F.P. Journe, MB&F, Urwerk and others) keep earlier entries, with `own` "owner not stated" and no tier.
- Richard Mille, Tour de l'Île, Rodina watch II pages returned 404; Hamilton's SSIH sale date conflicts (1971 or 1974), so no `own_y`.
- Swatch Group and Richemont maker-share percentages appeared only in search snippets, so are not used.
- No movement kind: calibres are named in entry text only where a fetched page gives them (Spring Drive, El Primero, Miyota); ETA 2824, Valjoux 7750, NH35 were not fetched.
- Trench watch and Skeleton watch kinds have no entries. Fossil Wrist PDA and I'm Watch (smartwatches) are not moved; no D2 kind was named for them.
- About 62 fetches including 2 Wikidata queries; Firecrawl not used.
