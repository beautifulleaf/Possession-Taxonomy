# AUD3_DE — cold audit of D1 D2 D3 D4 E3 E4 E5 E6 (2026-10-28)

Counts below come from rebuild/reader/<CODE>.json and brands/traditions registers. Facts from my own knowledge are marked "to verify". "0 hits" means a grep of all rebuild/reader/*.json found nothing.

## D1 Computers & peripherals
111 kinds · 215 archetypes · 126 brands · no traditions register.

**Brand mode:** mixed. Tier for storage, networking, cables, printers and monitors; variety for vintage computers, enthusiast keyboards, CPU/GPU lines, maker boards and 3D printing.

**Gaps for hobbyists**
- **D1-1 Vintage platforms are missing.** There are 0 hits for Apple Lisa, TI-99/4A, Sinclair QL, SGI/Silicon Graphics or Sun SPARC. There is no kind for vintage Unix/RISC workstations: NeXTcube is the only one, and it sits in "Vintage desktop computer". Fix: add archetypes for Lisa, TI-99/4A, QL, Tandy CoCo, Dragon 32 and Sharp X68000 (to verify). Add a "Vintage workstation" kind (Sun SPARCstation, SGI Indy/O2, NeXTstation).
- **D1-2 No CRT computer monitor.** "Monitor" has 0 archetypes and Trinitron appears only as a TV in D3. Retro collectors seek the Commodore 1084S and Sony GDM-FW900 (to verify). Fix: add a "CRT monitor" kind under Vintage computers and cross-link to D3 and the E5 arcade monitor.
- **D1-3 Keycaps are thin.** "Keycap set" has only 3 archetypes (GMK, SA, MT3) and "Artisan keycap" has 0 (6 flat models). The community organises keycaps by profile/maker, then named set, then colourway. Fix: make named GMK/SA sets the versions, and make artisan makers archetypes.

**Too much detail**
- **D1-4 The "Electronic components" shelf is split into 12 tiny kinds.** Resistor, Capacitor, Inductor, Crystal, Transistor, Diode, LED, MCU chip, Sensor, Relay, Connector and RFID tag each have 0 archetypes and at most 3 models. Fix: merge them into 3 kinds: Passive components · Semiconductors & LEDs · Connectors, relays & modules.
- **D1-5 Attribute-only kinds and near-duplicates.** "M.2 heatsink" (2 models), "PoE injector" (1 model), "Memory-card reader" (3 models, no types), and separate Laptop stand, Laptop cooler and Laptop sleeve kinds (each 4 models or fewer). Fix: fold them into types of Thermal, Network switch, Drive enclosure, and one "Laptop accessory" kind.
- **D1-6 SKU noise in "PC power supply".** Its 16 models include part numbers such as "RPS0110 (CP-9020188) (RM850x)" and "SRP-FGX851-A5A32SF". Fix: cut to model lines (RM, Focus, Prime, Dark Power, Leadex).

**Confusing organisation**
- **D1-7 One platform is spread across several vintage kinds.** The Amiga sits in two kinds ("keyboard models" vs "big-box"), as do the Atari ST and Mega ST/TT. The pre-1995 laptops (T1100, Compaq LTE, DynaBook, ThinkPad 700C) sit in the current "Laptop" kind. Fix: follow E5's platform → revision axis, with form factor as a version and period as a view.
- **D1-8 Everyday items sit in the enthusiast keyboards department.** Apple Magic Keyboard, Numeric keypad and Stream Deck are in "Enthusiast keyboards". Security keys and hardware wallets sit under "Monitors & peripherals". Fix: put plain keyboards and keypads in an everyday peripherals shelf, and give "Security & crypto hardware" its own shelf.
- **D1-9 Overlaps with other categories.** "Microphone" (Blue Yeti, Shure MV7) overlaps E3 microphones. THEC64 is an archetype in both D1 "Retro computer re-creation" and E5 "Plug-and-play & mini console". Fix: give each object one home and cross-link from the other.

**What it would look like: Vintage computers**
```
Vintage computers
  Home computer → Commodore 64 → C64 breadbin · C64C · SX-64 → PAL/NTSC, case colour
               → ZX Spectrum → 16K/48K · + · 128 · +2/+3
  Workstation → Sun SPARCstation → 1 · 2 · 5 · 20 (to verify)
              → SGI Indy / O2 / Octane
  Portable → Compaq Portable · Toshiba T1100 · ThinkPad 700C (moved from Laptop)
  CRT monitor → Commodore 1084S · Sony GDM-FW900
  Floppy drive → Disk II · 1541 · Gotek
```
Priority: medium · Fix size: medium

## D2 Phones, tablets & personal devices
63 kinds · 186 archetypes · 106 brands.

**Brand mode:** mixed. Tier for power, cases, navigation and licence-free radio; variety for classic phones, PDAs, e-readers and ham radio.

**Gaps for hobbyists**
- **D2-1 Phone generations are listed patchily.** The iPhone archetype has 12 versions but skips 3GS, 7, XR, 11 and 13–15. Galaxy S skips S5, S6, S9, S10, S21, S23 and S24. Pixel skips 3, 4, 5 and 7. Fix: list every generation (or name the selection rule), as D1 does for the ThinkPad X1 Carbon (Gen 1–14).
- **D2-2 Missing icons.** There are 0 hits for Nokia N900, Lumia, Palm Pre, HTC Dream/T-Mobile G1 and Moto 360. "Keypad phone", the biggest collector field, has only 5 archetypes (3310, 5110, 1100, N-Gage, W800). Fix: add Nokia 6110/7110/8210/8810, Sony Ericsson T68i, Siemens and Samsung SGH icons (to verify), plus a smartwatch history (Moto 360, Sony SmartWatch, Microsoft SPOT).
- **D2-3 Ham radio stops at transceivers.** "Amateur antenna" has 8 types and 0 archetypes. "Linear amplifier" has 10 models and 0 archetypes (collectors know the Heathkit SB-200 and Ameritron AL-811; to verify). There is no communications receiver: 0 hits for Hallicrafters or Collins R-390A. There is also no antenna analyser (NanoVNA, 0 hits). Fix: add "Communications receiver" and "Antenna analyser & SWR meter" kinds, plus amplifier and antenna archetypes.
- **D2-4 Luxury phone is Vertu-only (4 archetypes).** Fix: add Mobiado, TAG Heuer Meridiist and Porsche Design (to verify).

**Too much detail**
- **D2-5 Empty and near-empty kinds.** "Translator earbuds" and "Phone microphone" are completely empty. Electronic dictionary, Screen protector, Watch strap, Selfie stick and Clip-on lens each have 1 model. Fix: merge the 4 "creator add-on" kinds into one, and the 3 translator kinds into one.
- **D2-6 SKU-level names in "Charging dock".** Its 8 models are SKU strings such as "BoostCharge Pro 2-in-1 Wireless Charging Dock with MagSafe 15W". It also duplicates D1 "Multi-device charger". Fix: list brands and lines, and give chargers one home.

**Confusing organisation**
- **D2-7 Duplicates across categories.** "Radio scanner" is in D2 (3 archetypes) and again in D3 (9 models, including the same BCD436HP and SDS100). "Smart glasses" includes XREAL Air, which E5 also lists as "XR display glasses". Fix: keep scanners in D2 and display glasses in E5 VR & XR, with cross-links.
- **D2-8 "Satellite phone" is shelved with landlines.** Fix: put it with satellite messenger and hotspot in a "Satellite & safety" shelf. Five departments (Tablets, Wearables, Navigation, Power, Cases) have no mode note.

**What it would look like: Feature & classic phones**
```
Keypad phone
  Nokia 3310 → 3310 · 3315 · 3330 · 3310 (2017) → covers (Xpress-on)
  Nokia 6110 → 6110 · 6150 · 5110 (to verify)
  Nokia 8210 / 8850 / 8810 (premium line)
  Sony Ericsson T68i → T68 · T68i
  Siemens S/C/ME series (to verify)
Flip phone → StarTAC · MicroTAC · RAZR V3 (+ V3i, V3xx)
Slider → Nokia 8110 · N95 · Sony Ericsson W910
```
Priority: medium · Fix size: medium
