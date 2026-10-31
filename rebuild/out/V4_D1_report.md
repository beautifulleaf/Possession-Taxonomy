# V4_D1 report: named-entry pass, D1 Computers & Components

Files changed: rebuild/out/D1.json, rebuild/out/D1_brands.json (backups in rebuild/work/V4_D1/bak/). D1_renames.json and D1_moves.json unchanged. validate.py --v3: OK (110 kinds, 385 entries). Build script: rebuild/work/V4_D1/apply.py (rebuilds from the backup). Fetched URLs: rebuild/work/V4_D1/sources.tsv.

## Named kinds (entries before -> after)
- Processor 13 -> 47. Microarchitecture or generation, sections Intel / AMD / Apple and other, then year. References: Wikipedia List of Intel CPU microarchitectures, List of Intel Core processors, List of AMD CPU microarchitectures, List of AMD processors. Models are versions. Itanium, XScale and server-only designs left out. Years for Bobcat to Puma, Zen 6 and several K10/Bulldozer sub-cores were not stated by the pages and are blank.
- Graphics card 4 -> 27. Architecture generations from Nvidia (NV1 to Blackwell), ATI/AMD (Rage to RDNA 4), Intel Arc (Alchemist, Battlemage), plus 3dfx Voodoo. References: List of Nvidia GPUs (read to about 200,000 characters, so RTX 20 to 50 years come from the GeForce article), GeForce, List of AMD GPUs, Intel Arc. Board-partner lines (ROG Strix, FTW and others) and the Titan range removed (Titan cards are versions).
- Home computer 17 -> 139. Every row of Wikipedia's List of home computers (read in 20,000-character windows, names and years), sections by era. Fourteen vintage-desktop entries that are on that list moved here; Vintage desktop computer keeps Altair 8800 and Apple Lisa. Entries not already in the data have a generic description and the list as source; families such as Apple IIe/IIc or Atari TT/Falcon are folded in a few places, so makers are blank where the page did not state them.
- Keyboard switches 10 -> 23. Wikipedia Keyboard technology canon (rubber dome, scissor, flat membrane, reed, Hall-effect, optical, capacitive) plus enthusiast families; 20 loose retail switches became versions of six maker families (Kailh speed, Logitech, Razer, Outemu, Drop Halo, Roccat Titan).
- Laptop and other kinds with entries (desktop lines, vintage portables, cases, coolers, 3D printers, security keys, wallets, maker boards, keyboards, kits): entries kept, `nl` and `sel` added saying no whole-space reference was found (Wikipedia's List of laptops returned 404). Laptop entries now carry a maker section.
- Removed entries (commodity peripherals, no canon): Mouse 7, Trackball 3, Pen tablet 6, Everyday keyboard 1, Macro pad 1, Mouse pad 1. Cables, storage media and networking had none.

## Loose models and ranges
About 400 loose models (`m`) were removed as out of scope (retail SKUs in commodity kinds), except the 20 switches above. Ranges `r` removed from Processor and Graphics card; kept on motherboard, memory, case, cooling and others.

## Market facts (department `ms`)
- Computers: Gartner Q1 2026 shipments (Lenovo 26.5 %, HP 19.3 %, Dell 16.5 %, Apple 10.6 %, ASUS 6.7 %, Acer 6.4 %); IDC Q3 2026 (Lenovo 23.8 %, HP 16.5 %, Dell 12.1 %, Apple 9.5 %, ASUS 8.7 %).
- PC components: Mercury Research Q2 2026 client x86 (Intel 69.7 %, AMD 30.3 %); Jon Peddie desktop add-in boards Q2 2026 (Nvidia about 90 %, AMD about 8 %, Intel about 2 %), noted as reported by a secondary page.

## Not sourced
Desktop, mobile, server and revenue CPU shares (page gave client only); JPR primary report; GPU shares from the JPR or TechSpot pages (403 or no vendor split); PC vendor shares for regions; storage, networking and peripheral market shares. Version detail for CPU/GPU generations is series level, not every model. About 55 new makers were added to D1_brands.json as bare names (no country or founding year fetched). Home computers other than the list rows (hobby, kit and school sub-lists) not extended. Tier/own fields not added (not market-led).
