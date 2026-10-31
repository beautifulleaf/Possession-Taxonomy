# GAP_C1 report (Tools & Workshop Equipment)

About 47 fetches, none via Firecrawl. validate.py --v3 prints OK (305 kinds, 461 archetypes). Backups in rebuild/work/GAP_C1/bak/, sources in sources.tsv. gaps.md for C1 was out of date: out/C1.json already had no `m` and 22 kinds with entries.

**1. Loose models.** None left (V4 removed all 416). Nothing to do.

**2. Coverage lines.** All 22 entry kinds now end in Complete / Covers / No complete list exists. Added to Tool battery, Plier multi-tool, Keychain multi-tool; Lockback and Power tool brand changed to "No complete list exists".

**3. Partial coverage.**
- Leatherman: the model table re-read in full. 35 plier lines + 4 keychain/wearable lines now Complete (39 of 39); retirement years and about 60 model versions added (Charge, Wave, Super Tool, Surge, Free, Juice, Skeletool, Squirt, Style, Tread, PST II). Limited editions left out; Crater is a folding knife.
- Swiss Army knife: 17 → 192 entries from the SAKWiki pages for 58, 84 (1 to 4 layer), 91, 93, 100 and 111 mm. Still "Covers": pages for 65, 74, 75, 130 mm, the 84 mm five-layer page and the Wenger/Delemont 85 mm pages were not read (fetch budget).
- Stanley planes: all 14 kinds now Complete. Nos. 14, 53 and 91 checked on supertool pages: never assigned (53 is a spokeshave). Lie-Nielsen No. 95 (1981) added as a version.
- Power tool brands 9 → 13 (Porter-Cable US 1906, bought 2004; Metabo; Einhell; Ridgid). Black+Decker founding year 1910. Battery platforms: Metabo, Einhell, Ridgid and EGO owners filled.

**4. Gaps.** Closed: brand register entries for ESEE (1997), Nite Ize (c. 1989), Cold Steel, Ontario Knife Company, Facom, KTC, Ko-ken, Porter-Cable. New kinds: Circlip pliers, Pipe bender, Thermal imaging camera (each with a fetched page).

**5. Sections.** `xg` added to every kind with entries over about 12 entries and to those with `g` (planes by Stanley series, batteries and brands by owner, Leatherman by size class, Swiss knives by handle length).

**Remains (searched):**
- Mora years: Mora knife article and a second search give none.
- Lock types for Delica, Worker, Kershaw Leek, Buck 112, Cold Steel Voyager; RAT-1 (not in OKC article): Wikipedia (Spyderco, Kershaw, Cold Steel, Buck, Lock knife, OKC) and one search each; not stated.
- Record and Veritas plane versions: no fetched page ties them to a number (Veritas guess URL 404).
- EGO/Chervon country, founding and platform launch years; Victorinox gallery years: not on fetched pages. AEG, Irwin, Lenox: no country/year page.
- Hakko FX-888D, Festool TS 55, Mafell MT 55, Sawzall generations, Facom/KTC/Ko-ken as entries: only brand-register facts; soldering irons and track saws are commodity kinds with no entries under the V4 rule. Facom's Stanley purchase year is unresolved (2005 to 2010 across pages; Stanley Works article says 2005 and 2006).
- Doweling jig: no fetched page defines it. Machine Mart/Lee Valley not retried; no independent Site equipment list found.
- KTC founding: its history page implies 1947, a search says 1950; left empty. Ko-ken: 1946 vs 1940; left empty. Two Wikipedia URLs guessed (ESEE, Nite Ize) returned 404 and were replaced by searched pages.

## Round 2 (about 36 fetches, none via Firecrawl)
validate.py --v3 OK (305 kinds, 653 archetypes). Backup bak/C1_r2.json.

**1. Swiss Army knife: now Complete, 192 → 380 entries.** Read SAKWiki Victorinox 74 mm, 58 mm layer pages, 93 mm and 111 mm layer pages, and Wenger 65 mm, 85 mm (1, 2, 3, 4, 5, 6+ layers) and 130 mm (1 to 4 layers) pages, plus the Delémont 85 mm page. Delémont models are re-badged Wenger models, so they sit under "85 mm (Wenger and Delémont)". Handle lengths added to the axis. SAKWiki has no 75 mm page (it uses 74 mm) and no 84/85 mm five-layer Victorinox page. Delémont 65 and 130 mm pages were not read (same Wenger numbering). Years remain empty: SAKWiki gives none for these models.

**2. Veritas.** Lee Valley pages returned 429 twice (logged in firecrawl_deferred.md). Instead, a Machine Atlas review states the Veritas Router Plane is based on the Stanley No. 71: added as a version. Popular Woodworking ties the Veritas Small Plow Plane to the Record 044, not a Stanley number, so not added. Other Veritas planes: not sourced.

**3. Lock types.** Added to Lockback folder (now with maker sections): Buck 112 Ranger (lockback), Spyderco Delica (back lock, line 1990, Delica 4 in 2006), Cold Steel Recon 1 (2000; Tri-Ad lock, a back lock with stop pin) and Voyager (Tri-Ad). Kershaw Leek: one retailer says frame lock, others liner lock, so not placed. Spyderco Worker: catalogue URLs found by search returned 404 twice; Wikipedia gives 1981 first folder but no lock. Left out.

**4. Mora.** Morakniv's own history page gives no model years for Companion, Basic, Garberg, Kansbol or Bushcraft. It dates the Mora 2000 to 1991, now set on that entry. Other Mora years remain empty (searched four times).
