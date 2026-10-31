# GAP_H4 report (Fragrance)

validate --v3: OK. Backups and scripts in rebuild/work/GAP_H4/; URLs in sources.tsv and r2hits.tsv. No Firecrawl.

## Round 1 (about 58 fetches)
Loose models: none remain. Family not stated 468 -> 444 (24 placed from Wikipedia API extracts, snippets and French Wikipedia). Coverage lines added to four kinds without one; sections (`g`, `xg`) added to the 13 family kinds.

## Round 2 (about 100 fetches)
validate --v3 rebuild/out/H4.json: OK. Backup before round 2: rebuild/work/GAP_H4/bak/H4_before_r2.json; hits in r2hits.tsv; script apply_r2.py.

**Family not stated: 444 -> 373.** 71 more perfumes moved, each with the Perfume Intelligence page that states the family in `s` and the wording in `d`.
- Method: A-Z pages hold about 50 names each and cost about 3 fetches per page for 1 to 3 hits. Perfume Intelligence house pages (/library/perfume/<letter>/houses/<House>.htm, found by site-restricted search) list a whole house with families and gave most hits: 26 houses read, from Rochas and YSL to Kenzo and Max Factor.
- Mapping rule: the page's last family noun decides (floral-oriental goes to Amber, woody chypre to Chypre, floral aldehyde to Floral). Entries with two competing descriptions (Gentleman, Blue Jeans & Red Jeans, Ysatis) were left unplaced.

**Owners.** Set from fetched pages: Dana and Tabu lines to Dana Classic Fragrances (2003, Wikipedia Tabu by Dana); Guy Laroche to L'Oréal (house page: "now part of L'Oreal group", no year); Prince Matchabelli to DeCoeur Fragrances; Gloria Vanderbilt to Selective Beauté International; Britney Spears lines to Elizabeth Arden; Rihanna's Rebelle and Rogue to Parlux Fragrances; Fame, Glowing, Celine Dion Parfums and Rise to Coty (licence holders). 

## Remains
- **373 perfumes without a family.** Guerlain (27), Tom Ford (24), Coty lines (32), Avon (7) and Victoria's Secret (12) lie on pages not read or have no family on the page read.
- **Owners still empty after two attempts each:** Houbigant (Wikipedia: only licences, no owner; PI search names Aladdin Fragrances for two ex-Houbigant scents only), Robert Piguet (Wikipedia and PI house page state none), Fabergé (Wikipedia gives the 2025 SMG Capital purchase of the jewellery company, not the fragrance line), Grès (Wikipedia: fashion house sold to Yagi Tsusho; perfume owner not stated).
