# GAP_E5 report (Video Games)

About 56 fetches (log: rebuild/work/GAP_E5/sources.tsv). validate --v3: OK (104 kinds, 698 archetypes). Entries 674 > 697. Backups in rebuild/work/GAP_E5/bak/. Firecrawl not used.

1. Loose models: none left (V4 removed all 586); nothing to do.
2. Coverage lines: every kind with entries now ends its `sel` with "Complete: n of n in ...", "Covers n of ..." or "No complete list exists; follows ...". Counts for "Complete" kinds are the entries held against the reference rows the earlier passes read.
3. Partial coverage closed:
- Standalone and Tethered VR: List of virtual reality headsets read from offset 100,000; the rest of the page is navigation text, so both are Complete (14 of 14 each).
- Arcade system board 66 > 79: read Wikipedia's categories for arcade, Capcom, Konami, Nintendo, Taito, 68k-based and Neo Geo boards and added Taito F3, NESiCAxLive, NESYS, Hyper Neo Geo 64, Atomiswave, Bubble System, PlayChoice-10, DECO Cassette System, Mega System 1 and 32, PolyGame Master, exA-Arcadia, TIA-MC-1. CPS-2 (1993) and CPS-3 (1996) years filled.
- Game disc 8 > 13: PlayStation, PlayStation 2, Xbox, Xbox 360 and Mega-CD discs.
- Cartridge converter 3 > 5: Intellivision System Changer (1983), ColecoVision Expansion Module #1.
- Flash cartridge 21 > 24: PVBackup, XG-Flash, Game Partners Classic; R4DS as a version. Now Complete against Game backup device.
- Handheld gaming PC: maker sections added; Liliputing models (Legion Go 2 and S, ROG Xbox Ally, GPD Win Mini/4/5, X1 Mini, Ayaneo 3) added as versions.
- Console memory card: PocketStation added.
4. Gaps from earlier reports: Williams WPC already held; Williams System 11 and Stern SAM/Spike remain unsourced.
5. Section axis: `g` and `xg` set on Handheld gaming PC, Tabletop electronic game, Hardware upgrade add-on. No kind over 12 entries lacks sections.

## Round 2 (about 31 fetches)
- Optical disc read from offset 100000: the tail is a navigation box with no console text. Game disc 13 > 18 from the console articles: Saturn, 3DO, CD-i, PC-FX and Neo Geo CD discs.
- Board years: Taito F3 1993 and Mega System 32 1994 (Arcade Museum), Atomiswave 2002 (Arcade Museum), Mega System 1 1988 (earliest game, P-47, May 1988). Aleck 64 (1998) added; Taito NESYS removed because it is an online network, not a board. Arcade boards now 79.
- Revisions added as versions from each platform's page: Neo Geo CD (front-loading, top-loading, CDZ 1995), FM Towns Marty 2, N64 Funtastic Series, Cybiko Classic and Xtreme, Zodiac 1 and 2, Mega Duck, Watara Supervision variants, Neo Geo X Gold. Disc facts for Saturn, 3DO, CD-i were already versions.
- The MediaWiki extracts API returns introductions only for 20 titles, so I used it to find candidates and fetched single pages for the rest. Most of the ~58 platforms FIX_E5 listed (RCA Studio II, Bridge Companion, Virtual Boy, Playdate and similar) have one model and no named revisions in their intro extracts, so they stay without versions. Xbox and N64 pages name no dated revisions beyond the above.
- Still blank: TIA-MC-1 year (searched "TIA-MC-1 Soviet arcade machine year Ekstrema": sources say mid-1980s), Mega System 1A board year beyond the first game, Stern SAM/Spike and Williams System 11.
- Deferred Firecrawl pages: gametechwiki Taito and Capcom, arcadecontrols Arcade_Systems.
