# STR_D1 report (Computers & Components)

Validation: `validate.py --v3 out/D1.json` prints OK.

**Counts, before to after.** Departments 10 to 12, shelves 23 to 33, kinds 100 to 110, archetypes 227 to 224 (15 demoted, 12 added).

**Structure.** Category `ax` and a 12-step `key` added; lead kept. Every department has `t` and `ax`; every shelf has `t` (and `ax` above 3 kinds). New department "Vintage & retro computing" (period machines, re-creations, period peripherals). "Monitors & peripherals" split into "Monitors & desk setup" and "Pointing & input devices". Storage reshaped to internal, external and network. Networking split into internet entry, wireless coverage, wired network. Cables split into cables, hubs and docks, power. Maker boards, kits and components are separate shelves.

**Kinds.** Added (all sourced): Convertible laptop, Netbook, Workstation (split from Tower PC), External trackpad, Label printer, 3D scanner, Wrist rest, Keyboard PCB, Keyboard case, Switch tester. Renamed: "Home computer (keyboard computer)" to Home computer; "Keyboard" to Mechanical keyboard (see D1_renames.json). No kind was merged or moved to another category; D1_moves.json is unchanged. All 110 kinds now carry hand-written `tt` groups.

**Archetypes.** Demoted to ranges (`r`): four motherboard lines, five memory lines, three artisan keycap makers, EK custom loop parts, Yubico Security Key, Apple mouse. Added: IBM ThinkPad 360P, Asus Eee PC 700, Compaq Concerto (promoted from models), Commodore 128, Acorn Atom, IBM PCjr, Tandy 1000, Amstrad PC1512, Odroid, Banana Pi, Pine64 boards, Brother P-touch. Brands added: Hardkernel, Shenzhen SINOVOIP, Pine64, Brother.

**References per shelf (fetched).** Laptops: Wikipedia Netbook, 2-in-1 PC. Desktops and servers: Workstation. Vintage: Home computer. Components: Computer hardware, Scan category page. Storage: Computer data storage. Desk and input: Computer hardware, Touchpad. Enthusiast keyboards: KBDfans navigation (Candykeys redirected away and was not used). Printing: Computer printer, Image scanner, Label printer, 3D scanning, 3DJake navigation. Networking: Networking hardware, Wireless access point. Maker boards: Single-board computer, ODROID, Banana Pi. Cables and power: no listing page found; kept at kind level.

**Cross-links.** About 30 `see` entries, all targets checked against reader files (E5, D2, D3, E3, I1, B3, C1, A4, B8, C8).

**Not sourced or left.** Years for Commodore 128, Acorn Atom and Pine64 left blank (not on fetched pages). Cables, hubs and power coverage not checked against a listing. Firecrawl and Parallel were unavailable; WebFetch only. Sources logged in work/STR_D1/sources.tsv.
