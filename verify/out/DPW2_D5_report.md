# DPW2_D5 report: D5 Video Games, second decision pass (offline)

## Task 1: missing kinds (19 items)
Sources: MKH_D5_ASIA, EUR and NAO, plus the four items the session prompt names. HV_D5_NK raised none. Three items were skipped because DPW1 already decided them: the phone VR headset (now D5.1.3.03), the arcade system board (D5.5.19) and the gaming headset (D3).

Counts: new_kind 6, covered 7, attribute 3, other_category 3.

New kinds (next free id under each parent, R-58; all wait for HV_D5_NK2):
- **D5.5.20 Controller converter**: Brook Wingman and Mayflash Magic type. The Brook fighting board is covered by it.
- **D5.2.3.04 Gear shifter**
- **D5.2.3.05 Handbrake controller**
- **D5.2.3.06 Racing wheelbase**: a motor base sold without a rim. Direct, belt or gear drive is an attribute (C10).
- **D5.1.1.03 Tabletop electronic game**: Grandstand VFD type. It is placed under home consoles because it is neither handheld nor linked to a TV. The E1 boundary is checked at attestation.
- **D5.5.21 Cooling unit made for one console**: Nyko Intercooler type.

Session items:
- Gaming chair: B1 (memo 9.9; B1.1.5 work and task seating).
- Sim-racing pedals: covered by D5.2.3.02.
- Wheelbase: new kind D5.2.3.06.
- Controller converter: new kind D5.5.20.

Other calls:
- A wheel rim sold alone is covered by D5.2.3.01.
- The Odyssey 2 speech and chess modules are covered by D5.1.5.03. Its definition should read "processors, sound, graphics or memory hardware" (wording only, id unchanged).
- A chat audio adapter is covered by D5.5.07.
- Attributes, not kinds: the handheld gaming PC (K-152, os = PC), Famiclone and clone or FPGA consoles (implementation, licence relation).
- Other categories: a Famiclone with a keyboard (Subor learning machine) goes to D1.1.07, provisionally, as DPW1 did with keyboard replicas. Hyperkin Smart Boy goes to D2 (K-5, a phone part).

## Task 2: named forms added since DPW1 (176 reviewed: 141 -K rows from MKH_D5_ASIA, 35 HV_D5_NK rows)
- **drop 128**: MKH_D5_ASIA mostly re-harvested rows already stored:
  - 66 arcade cabinets;
  - 26 controllers and light guns;
  - 23 handhelds and VR headsets, among them Pimax Crystal filed under a second kind (one home per object);
  - NES controller and DK Bongos.
- **move_kind 2**:
  - Pimax Portal is an Android handheld that docks into the Portal View shell, so it goes to D5.1.2.01.
  - The stored Fanatec CSL DD (a wheel base by its own notes) goes to the new D5.2.3.06 and waits for attestation.
- No to_line.
- The 35 HV_D5_NK rows are fine.

13 -K rows are new and stay: Ayaneo Next, Air and Kun, Retroid Pocket Flip 2, Anbernic WIN600, Miyoo Mini, Miyoo A30, HTC Vive Focus, ROG Ally X, Mayflash F700 wireless and F500 FLAT, and iPega D11.

Noted, not flagged:
- Retroid appears under both M-retroid and M-goretroid; a maker merge is owed.
- Pimax Crystal sits under tethered VR although it has a standalone mode.
- Pimax Portal View is a shell with no compute and may belong in D5.1.3.03.
- NAOMI and Atomiswave boards could be D5.5.19 named forms beside their C13 rows.
- Flight yokes still have no kind (DPW1).
- Sim-racing cockpits and rigs were not raised; they are probably B1 or a D5.5 part.

## Task 3: scope and wording
- **Alias rows owed** (R-104 b): written as 14 attribute rows in DPW2_D5_kinds.tsv. Each gives the term, the target named form and the region in its reason, with the HV_D5_1 source. 12 are DPW1's regional names:
  - NES Controller and Famicom Controller;
  - Mega Drive Control Pad and Mega Drive 6-Button Controller;
  - Mega Drive 2;
  - Super Nintendo Classic Mini;
  - Nintendo Classic Mini: Super Famicom and Nintendo Classic Mini: Family Computer;
  - Sega Mega Drive Mini;
  - TurboGrafx-16 Mini and PC Engine CoreGrafx Mini;
  - Power Base Converter.

  Two more are aliases DPW1 counted as duplicates: Zapper Light Gun (JP Famicom Light Gun) and Family Fun Fitness. They become C9 rows (relation regional name or alias) once the alias table loads.
- **Move waiting for B1**: NF-D5.5.01-005, the Nintendo 64 Game Storage Tower (verify/out/DPW1_D5_moves_pending.tsv), stays pending. data/kinds.tsv has no B1 kinds. The move waits for the B1 tree to be loaded and for an attested B1 kind that holds several media items. The B1 memo has no such kind; candidates are media storage in B1.4.2 beside the TV unit, or a rack in B1.5.2 (Google lists "media storage"). B1 has to add that kind first. The move is then re-applied with tools/apply_dp.py.
- Navigation unchanged (R-104).

## Rules applied
- C2(a), C2(d), C3, C9, C10, C11; C5(b) (D5.5 now 21 kinds, so display grouping applies, R-104 b).
- S3, K-5, K-152; memo D5 sections 4b, 6, 7 and 9.
- R-58, R-70(d), R-101(d), R-104.

## Facts from memory to confirm (R-104 c)
- What the Pimax Portal is.
- That the Fanatec CSL DD is a base only.
- That Subor machines have a keyboard body.
- The Odyssey 2 module functions.
