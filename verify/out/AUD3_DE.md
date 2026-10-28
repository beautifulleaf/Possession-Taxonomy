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

## D3 Audio & video
92 kinds · 232 archetypes · 144 brands.

**Brand mode:** mixed. Variety for head-fi, hi-fi loudspeakers, turntables, vintage separates and portable players; tier for TVs, soundbars, AV, smart speakers and accessories.

**Gaps for hobbyists**
- **D3-1 Vinyl icons are missing.** There are 0 hits for Shure V15, Koetsu, Lyra, Technics SP-10, EMT and Micro Seiki. Lenco appears only as a plinth type. Fix: add these as cartridge and turntable archetypes (to verify) and add an idler/broadcast deck line.
- **D3-2 Speaker icons are missing.** There are 0 hits for Yamaha NS-10. Sonus faber, Dynaudio, Wharfedale and Focal are in the brand register with no loudspeaker archetype. "Portable Bluetooth speakers" has 0 archetypes and 2 models, and JBL Flip, UE Boom and Marshall get 0 hits, so tier coverage is too thin as well. Fix: add hi-fi archetypes (Guarneri, Contour, Diamond: to verify) and 5–10 market and test-winner (RTINGS) speakers.
- **D3-3 Personal players are all Sony.** "Portable cassette player" has 2 archetypes, both Sony (6 + 2 versions). "Portable CD player" is Discman only. Fix: add Aiwa HS-P, Panasonic and Toshiba Walky (to verify). This is a maker-skew finding.

**Too much detail**
- **D3-4 Eight kinds are completely empty.** Headphone stand, On-wall speakers, Party speakers, Master clock, Multichannel power amplifier, Video processor, Projector screen and Audio cable. The "Cables & connectivity" department holds only that one empty kind. Fix: merge the 5 home-cinema speaker kinds (system, centre, surround, in-wall, on-wall) into one kind with types. Make Multichannel amp and Video processor types of AV processor. Replace the cable department with one "Audio & video cable" kind under accessories.

**Confusing organisation**
- **D3-5 Headphone kinds mix four axes.** Open-back and Closed-back are acoustic design, On-ear is fit, "Wireless noise-cancelling" is a feature, and Electrostatic is a driver. Grado SR and HD 25 could go in either of two kinds. Fix: make kinds by form (over-ear, on-ear, in-ear, earbud) and give acoustic design, driver and connectivity as `t`. Electrostatic can stay a kind only because it needs an energiser.
- **D3-6 Duplicates with E3 and D2.** The Technics SL-1200 is an archetype in D3 Turntable and in E3 DJ turntable. Ortofon Concorde and Shure M44-7 are archetypes in both D3 Phono cartridge and E3 DJ cartridge. In-ear monitors and Subwoofer exist in both D3 and E3. E3 "Studio headphones" lists HD 600 and DT 770, which are D3 archetypes. Radio scanner duplicates D2. Fix: give each object one home and cross-link.
- **D3-7 "Audio figure" (Toniebox, Yoto) sits in the collector "Portable audio" department.** Fix: tag it baby and put it with children's audio or E1, cross-linked.

**What it would look like: Turntables & vinyl playback**
```
Turntable
  Idler: Garrard 301/401 · Thorens TD 124 · Lenco L75 · EMT 927 (to verify)
  Direct drive: Technics SL-1200 → Mk2…Mk7, G, GR · Technics SP-10 → Mk1–Mk3
  Belt, suspended: AR XA · Linn LP12 → Valhalla, Lingo, Radikal eras
  Belt, rigid: Rega Planar → 2, 3, 6, 8 · Pro-Ject Debut
Phono cartridge
  MM: Shure V15 → I–V · AT95/VM95 · Ortofon 2M
  MC: Denon DL-103 → R, SA · Ortofon SPU · Koetsu · Lyra
```
Priority: medium · Fix size: medium

## D4 Cameras & photography
125 kinds · 229 archetypes · 65 brands.

**Brand mode:** mixed. Variety for film cameras, lenses and film stocks; tier for lighting, support, darkroom, bags and accessories.

**Gaps for hobbyists**
- **D4-1 No cine or cinema camera kind.** Cine stocks and cine projectors are in the tree, but there are 0 hits for Bolex H16 and Beaulieu. Nizo appears only in H1. There are 0 hits for RED, and Blackmagic appears only in I1 software. Fix: add a "Cine film camera" kind (Super 8, 8 mm, 16 mm; Bolex, Beaulieu, Nizo, Canon 514XL: to verify) and a "Cinema camera" kind (Blackmagic Pocket, RED: to verify).
- **D4-2 Film camera icons are missing.** There are 0 hits for Praktica, FED, Zorki, Canonet, Yashica Electro and Leica M3; Zenit appears only in lens text. "Film SLR" has 24 archetypes but no Eastern-bloc, Leica R or first-autofocus lines (Minolta Maxxum 7000: to verify).
- **D4-3 Digital camera history is thin.** "DSLR" has 6 archetypes, all pro bodies. There are 0 hits for Nikon D1 and Kodak DCS, and no consumer lines (Rebel/xxxD, D3xxx) or A-mount. "Compact camera" and "Camcorder" have 0 archetypes, although early digital compacts are actively collected now (to verify).
- **D4-4 Light meters have no archetypes.** "Light meter" has 0 archetypes and 7 models. Weston Master gets 0 hits, and Gossen and Sekonic appear only as models. Fix: add archetypes.

**Too much detail**
- **D4-5 The darkroom is split into 23 kinds.** Many have 1 model or none: Changing bag, Darkroom thermometer, Darkroom graduate, Film dryer, Enlarging lens, Developing tray, Print tongs, Print dryer, and the empty Print washer and Contact printing frame. Fix: about 6 kinds (Tank & reels · Chemistry · Enlarger, with lens, carrier and filter as types · Easel & focus aids · Trays, tongs & washers · Paper).
- **D4-6 Light modifiers and video support are split too finely.** Light modifiers are 11 kinds (Beauty dish and Reflector dish are near-duplicates; Snoot, Gobo and Barn doors each have 3 models or fewer). Video support is 8 kinds, two of them empty (Camera cage, Body-worn support). There are 6 empty kinds in total. Fix: about 3 kinds each.

**Confusing organisation**
- **D4-7 Two department notes are wrong.** The "Lenses & filters" note says lenses are organised by mount, but the kinds are by optical type (Prime, Zoom, Macro…) and mount is not an axis. The "Camera accessories & parts [tier]" note says "owners swap and upgrade these parts", which contradicts tier mode and the parts rule. Fix: correct both notes. Better: follow camera-wiki's mount → lens line axis.
- **D4-8 Gimbals are in three places.** D4 Handheld gimbal, D4 Pocket gimbal camera and D2 Phone gimbal are all DJI-led. Screen protector repeats in D2, D4 and E5. Fix: merge into one gimbal kind with a stabilised-camera type, and cross-link.

**What it would look like: Film cameras**
```
Film SLR
  Nikon F → F · F2 (Photomic heads) · F3 · F4 · F5 · F6
  Canon AE-1 → AE-1 · AE-1 Program
  Zenit → E · TTL · 12XP (to verify)          [new]
  Praktica → MTL · L series (to verify)         [new]
Film rangefinder
  Leica M → M3 · M2 · M4 · M6 · MP · M-A
  FED / Zorki → FED-2 · Zorki-4 (to verify)     [new]
  Fixed-lens: Canonet QL17 · Yashica Electro 35 [new]
Cine film camera → Bolex H16 · Canon 514XL · Nizo · Beaulieu [new]
```
Priority: high · Fix size: medium

## E3 Musical instruments
206 kinds · 678 archetypes · 269 brands · 36 traditions.

**Brand mode:** variety for guitars, amps, pedals, synths, orchestral and folk instruments; tier for accessories, MIDI controllers, interfaces, PA and cables.

**Gaps for hobbyists**
- **E3-1 Whole instrument families are absent.** There are 0 hits anywhere for lap steel, pedal steel, autoharp, hurdy-gurdy, steelpan, Mellotron, keytar, Omnichord, Stylophone and vocoder. Gamelan exists only in the traditions register. Fix: add kinds with archetypes, for example Fender Stringmaster, Sho-Bud, Oscar Schmidt autoharp and Mellotron M400 (to verify).
- **E3-2 Studio outboard gear is missing.** UREI 1176, LA-2A and Neve appear only as plug-in emulations in I1. "Microphone preamp and channel strip" has 0 archetypes and 1 model. There is no outboard compressor or EQ kind, and no multitrack recorder (Portastudio: 0 hits). Fix: add an "Outboard processor" kind (1176, LA-2A, Neve 1073, Pultec EQP-1A: to verify) and a "Multitrack recorder" kind (TEAC/Tascam Portastudio, reel multitrack).
- **E3-3 Thin kinds next to rich traditions entries.** Pipe organ, Erhu, Tabla, Djembe, Bansuri and Ney have 0 archetypes even though the traditions register covers them. Hichiriki is completely empty. Semi-hollow electric has only 3 archetypes; ES-345/355, Epiphone Sheraton and Gretsch Country Gentleman are missing (to verify).

**Too much detail**
- **E3-4 Cymbals repeat the same series across six kinds.** There are 6 kinds by voice with 41 archetypes, and each series reappears across them: Zildjian K 5 times, Paiste 2002, Signature and Sabian AA 4 times each, Formula 602 and HH 3 times each. Each kind also carries 14–24 `t` values mixing size, weight and finish (Ride has 24). Fix: one "Cymbal" kind, with the series as archetype (K, K Constantinople, A, 602, 2002, Signature, HH/HHX, AA, Byzance, Agop), the voice (ride, crash, hats, china, splash, FX) as version, and size, weight and finish as detail.
- **E3-5 The saxophone kinds duplicate model lines.** Alto, tenor, soprano and baritone kinds hold 36 archetype slots for 14 distinct lines. Selmer Mark VI, Conn "Naked Lady" and Series III each appear 4 times. Fix: one "Saxophone" kind, with the model line as archetype and the voice as version. Also, Line 6 Helix and EHX POG are each archetypes in two kinds.
- **E3-6 A stray cable department.** "Cables & accessories" holds only Microphone cable (3 models) and MIDI cable (2 models), which duplicate "Instrument cable" (16 models). Fix: merge into one "Cable" kind with types.

**Confusing organisation**
- **E3-7 Orchestral and folk instruments are split by musical culture rather than by object.** The concert pedal harp (Lyon & Healy, Camac) sits under "Folk & world". Balafon, Gyil and Amadinda sit under the orchestral xylophone. Banjo, mandolin and ukulele are "folk", while guitars have their own department. Under the "pursuits are out of scope" rule, departments should follow the object's family (plucked strings, bowed strings, flutes, reeds, brass, free reeds, percussion, keyboards), with the tradition as a tag and the traditions register as the view.
- **E3-8 Overlaps with D3.** In-ear monitors, Subwoofer (empty in E3), Studio headphones (whose models are D3 archetypes), DJ turntable (SL-1200) and DJ cartridge (Concorde, M44-7) all overlap D3. Fix: keep a pro/studio context here, point to the D3 archetypes, and drop the empty Subwoofer.
- **E3-9 Brand-register gaps.** 16 archetype makers are not in the register (Simmons, Vega, Fox, John Taylor, Theobald Boehm…). The register also has near-duplicate names: Marshall vs Marshall Amplification, Hercules vs Hercules DJ.

**What it would look like: Saxophones**
```
Saxophone (voice: soprano · alto · tenor · baritone as versions/t)
  Conn M series 'Naked Lady' (1930s–40s) → 6M alto · 10M tenor · 12M bari
  Selmer Balanced Action → Super Balanced Action
  Selmer Mark VI (1954–74) → alto · tenor · soprano · bari; serial eras
  Selmer Series III → Reference 54
  King Super 20 → Cleveland / Eastlake eras
  Yanagisawa 9x series · Yamaha 62 → Custom Z · Keilwerth SX90R
  detail: lacquer · silver · unlacquered; high F♯; low A
```
Priority: high · Fix size: large

## E4 Weapons & armour
171 kinds · 393 archetypes · 100 brands · 14 traditions.

**Brand mode:** variety for swords, antique arms, traditional bows and enthusiast air guns; tier for ammunition, reloading, optics, accessories, self-defence and body armour.

**Gaps for hobbyists**
- **E4-1 The "Militaria & replicas" department is a shell, even though RULES sends militaria here.** It has 2 kinds: "Decorative replica weapon" is empty and "Deactivated ordnance" has 4 models. There are 0 hits for Denix, and there is no kind for deactivated firearms or inert ordnance. Fix: add kinds for non-firing replica firearm, deactivated firearm and inert ordnance (Mills bomb, Stielhandgranate: to verify).
- **E4-2 Collector firearm icons are missing.** There are 0 hits for Springfield M1903, Kar98k, Colt 1851 Navy and Webley revolver. AK-pattern rifles appear only as bayonets, and the Nagant appears only as the Mosin–Nagant. Archetype counts are low: double-action revolver 4, single-action 2, semi-auto rifle 4.
- **E4-3 Cartridges are flat lists.** The 3 cartridge kinds have 0 archetypes and 0 types; calibres such as ".30-06 Springfield" sit in `m`. Calibres are the axis cartridge collectors use (to verify). Fix: make each calibre an archetype (designer, year), with loadings as versions. There is also no historical crossbow (arbalest: 0 hits).

**Too much detail**
- **E4-4 Ten kinds are completely empty.** Kampilan, Takoba, Shotel, Habaki, Barrel, Trigger, Suppressor, Sword cane, Plate carrier and Decorative replica weapon. "Reloading die" and "Reloading die set" are near-duplicates, as are Taser-type and Contact stun gun. Fix: merge the firearm parts (barrel, trigger, suppressor, iron sight) into one kind with types, and cut body armour from 5 kinds to 2.

**Confusing organisation**
- **E4-5 Japanese sword archetypes are individual smiths.** Masamune, Sadamune and Nagasone Kotetsu each recur across Katana, Wakizashi and Tantō, and 22 archetype makers are missing from the register. Many of the named blades are national treasures no one can own. Fix: make the archetype the school (the Gokaden traditions already in the register: Yamashiro, Yamato, Bizen, Sōshū, Mino) plus the period (kotō, shintō, shinshintō, gendaitō). Put the smiths in a smith register.
- **E4-6 Misplaced items and labels readers won't guess.** The Brown Bess, a smoothbore musket, sits under "Muzzle-loading shotgun". The tosogu kinds are named "Hilt collar and pommel cap" (fuchi-kashira), "Sword grip ornament" (menuki) and "Scabbard pocket fitting" (kozuka/kōgai), under a generic "Sword fittings & mounts" shelf. Fix: add a "Musket" kind, and use the Japanese names with English aliases in a "Japanese sword fittings (tosogu)" shelf.
- **E4-7 Night-vision overlaps E6.** Pulsar thermal sights (E4) and Pulsar viewers (E6) need cross-links.

**What it would look like: Rifles**
```
Bolt-action rifle
  Mauser 98 → Gewehr 98 · Kar98k · Mauser sporters · Brno/Zastava copies
  Springfield M1903 → M1903 · M1903A3 · M1903A4   [new]
  Lee–Enfield → MLE · SMLE No.1 Mk III · No.4 · Ishapore 2A1
  Mosin–Nagant → M1891 · M91/30 · M44
  Winchester Model 70 → pre-64 · post-64 · Classic
Musket (new) → Brown Bess · Charleville 1777 · Springfield 1861 (to verify)
Semi-automatic rifle → M1 Garand · SKS · AK-pattern (civilian) · AR-15
```
Priority: medium · Fix size: medium
