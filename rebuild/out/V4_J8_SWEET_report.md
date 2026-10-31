# V4_J8_SWEET report (round 2)

Part file `rebuild/out/J8_parts/SWEET.json` (533 KB), validates OK: 78 kinds, 1,134 entries. Replaces Chocolate; Sweets & confectionery; Biscuits & crackers; Ice cream. All kinds reappear; no renames or moves. About 100 fetches in total (round 2: about 50).

**Entries before (structure pass) -> after:** Chocolate 73 -> 417, Sweets 129 -> 221, Biscuits 79 -> 300, Ice cream 52 -> 196. Entries carry `own`, `tier`, `cty`, `own_y` where a page gives them; sections by tier and owner, named traditional forms by country.

**Round 2 follow-ups**
1. Cookie list: every row of Wikipedia's List of biscuits and cookies is an entry, an alias or a version, except Biscuit, Wafer and Biscotti (these are kinds). Sectioned "Traditional forms: <country>".
2. Protected names: EU–Mercosur annex 13-B and the EU list sent to New Zealand (2018), read from the PDFs with pdftotext. Added Nürnberger Lebkuchen, Polvorones de Estepa, Ovos Moles de Aveiro, Bergamote(s) de Nancy, Glyko Triantafyllo Agrou, Kritiko Paximadi; annotated Jijona, Turrón de Alicante, Lübecker Marzipan, Loukoumi Geroskipou, Cantucci. Not found on a fetched list: Nougat de Montélimar, Calisson d'Aix, Gaziantep baklava (kept from earlier entries). eAmbrosia and the Canada CETA annex were not readable (503/JavaScript); no Wikipedia per-country protected-food list was fetched.
3. Portfolios: Meiji (own brand-site list via Firecrawl, 25 sweets and ice brands), Lotte Japan (own catalogue pages), Morinaga, Glico (own product pages), Orion and Haitai (own product pages plus Wikipedia). Left out: snacks (Karl, Pretz, Pocachip) and licences (Pokémon, Calpis, Dole).
4. National shares added: US chocolate (Euromonitor via ConfectioneryNews, Jan 2018), Japan (Meiji 17.9%, 2013 article), China (Mars 39.8%, Ferrero 17.8%, 2017; China Briefing 2024 undated), UK chocolate (Mondelēz over a quarter, 2020; market US$6,168 m), US ice cream 2024 (category US$8.65 bn; private label US$1.6 bn; Ben & Jerry's US$1.02 bn), China biscuits Orion (two-thirds, 2006). Still missing: Germany and France (Circana, Lebensmittel Zeitung, Statista and Autorité decisions are paywalled or redacted; a 46.3% Haribo France figure on businesscoot could not be fetched), UK biscuits, Japan current shares.
5. `d` lines: 315 generic or templated lines were dropped; the remaining new ones state a fact from the cited page (origin, year, market, list membership).

**Unchanged limits:** tier "National champion" only where a page states leadership; Meiji Milk Chocolate (1926, "leading chocolate brand in Japan") now qualifies. Roles only Reese's and Digestive. Ice cream list excludes parlour chains and defunct brands.
