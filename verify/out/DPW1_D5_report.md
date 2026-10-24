# DPW1_D5 report: D5 Video Games decision pass (offline)

## Task 1: missing kinds (9 harvest items split into 15)
Decisions: new_kind 10, covered 3, named_form 1, other_category 1, attribute 0.

Each new id is the next free number under its parent (R-58):
- D5.1.3.03 Phone VR viewer
- D5.1.5.03 Hardware upgrade add-on (32X)
- D5.2.4.04 Console mouse
- D5.2.4.05 Paddle or spinner controller
- D5.2.5.03 Game microphone
- D5.5.15 Network or modem adapter made for one console
- D5.5.16 Media add-on made for one console (media remote; TV tuner covered here)
- D5.5.17 Keyboard made for one console
- D5.5.18 Rumble pack
- D5.5.19 Arcade system board (Naomi and Atomiswave are C13 platform rows)

The other five items:
- Expansion Pak: covered by D5.5.08.
- Cleaning kit: covered by D5.5.13 (cleaning fluid sold alone is B6).
- R.O.B.: a named form under D5.2.4.03. It is one product, not a generic type.
- Console headset: other category D3 (step 24, memo 9.2).

Each new kind enters data/kinds.tsv only when an HV_NK fetch attests it (R-70(d)). Several split items share one harvester URL, so the type must be confirmed on that page.

D5.5 grows from 14 to 19 kinds, well above C5(b)'s "about 12". The structure is not reopened here; the next tree revision should consider a leaf by the part's job.

## Task 2: named forms (45 of 953 flagged)
- **to_line 4:**
  - Game Pak spans several cartridge formats.
  - Arcade1Up Full-size cabinets is a new line.
  - Head-to-head table and Counter-cade restate existing lines.
- **drop 24:**
  - 12 regional names, which become alias rows. Memo section 7 keeps one row per machine (Famicom / NES), so the Mega Drive, Super Famicom, Famicom mini and PC Engine mini names merge.
  - 9 duplicates.
  - 1 hardware revision (Xbox Wireless Controller "Series").
  - MiSTer, which is a platform project and belongs in C13.
  - A vague "ModRetro console" row.
- **move_kind 17:**
  - MIDI Pro-Adapter goes to D5.5.07.
  - Mega Key 2 and Passport Plus III go to cartridge converter, as region converters.
  - Genesis CDX goes to carrier-based console; it is standalone, not an add-on.
  - 3 standard USB charging cables go to D1.7.01 (memo 9.1).
  - 5 full-size Retro Games replicas with working keyboards go to D1.1.07, the keyboard computer.
  - 4 minis that load games from USB or SD go from dedicated to carrier-based.
  - An N64 cartridge storage tower goes to B1 under S3's never-parts rule, held until B1 is built.

Not flagged but noted:
- The M64 row's maker should be ModRetro, for the next maker pass.
- A flight yoke has no kind (the TCA Yoke sits on flight stick).
- Wii Wheel and Joy-Con Wheel are shells for one controller.

## Task 3: navigation by shopper path
Not by scene: no D5 scene tags are harvested, and the retro, competitive and emulation tags are held †.

Not by brand:
- 104 of 201 makers have one named form.
- Only the four platform holders (Nintendo 151, Sega 80, Sony 51, Microsoft 42) span four sub-families.
- Third-party makers cluster in one kind each (Anbernic, Thrustmaster, Pimax).

The memo's evidence (section 2) gives a two-step choice: form first for machines, platform first for games, controllers and accessories.

View:
1. **What are you shopping for?** Something to play on; VR headset; arcade cabinet or board; controller; games (disc, cartridge, card, key card, code, download, DLC, mod); accessories and parts.
2. **Second question:**
   - For machines: at home, on the go or both, and built-in games or load your own. Filters: os = PC, FPGA or emulation, retro.
   - For controllers, games and parts: which system? This is a platform view.
3. **Kind, then named form,** by maker and year, with region and generation filters.

A brand tab lists the platform holders and accessory makers.

**Prerequisite:** data/platforms.tsv holds no D5 rows. The "which system?" step needs C13 platform rows and platform links on named forms.

## Rules applied
- C1, C2(a), (b) and (d), and C3.
- C9 alias rows.
- C10.
- S3, S3b and K-2.
- K-153.
- Memo sections 7 and 9 and the tree precedence.
- R-58 ids and R-70(d).
- One home per object.

## † and unattested facts
None of the 51 kinds is still †; all were attested by HV_D5_1. These decisions rest on product facts not on a fetched page, and should be confirmed when fetched:
- the Retro Games replicas: full-size with a working keyboard, or loading from USB;
- X68000 Z loading from SD;
- Passport Plus III and Mega Key 2 being region converters;
- the Atari 10-in-1, Samba maracas and Power Base Converter duplicates.

**Open for the key:** Phone VR viewer follows K-153 ("whatever it is sold for"), but S3 (step 8, read first) with S3b's phone-only sentence could send it to D2. An S3b reading should settle this.
