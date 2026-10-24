# DPW2_D5 report: D5 Video Games, second decision pass (offline)

## Task 1: missing kinds (19 items)
From MKH_D5_ASIA/EUR/NAO and the session items. Skipped as decided: phone VR headset, arcade system board, gaming headset.

new_kind 6, covered 7, attribute 3, other_category 3.

New kinds (next free id, R-58; to HV_D5_NK2):
- D5.5.20 Controller converter (covers the fighting board)
- D5.2.3.04 Gear shifter
- D5.2.3.05 Handbrake controller
- D5.2.3.06 Racing wheelbase (base without rim; drive type is an attribute, C10)
- D5.1.1.03 Tabletop electronic game (Grandstand VFD type; E1 boundary checked at attestation)
- D5.5.21 Cooling unit made for one console

Session items: gaming chair to B1 (memo 9.9); sim-racing pedals covered by D5.2.3.02.

Other calls:
- Covered:
  - a rim sold alone by D5.2.3.01;
  - the Odyssey 2 speech and chess modules by D5.1.5.03 (definition adds "sound");
  - a chat audio adapter by D5.5.07.
- Attributes: handheld gaming PC (K-152), Famiclone, clone or FPGA console.
- Other categories: Subor keyboard Famiclone to D1.1.07 (provisional, as DPW1's keyboard replicas); Hyperkin Smart Boy to D2 (K-5).

## Task 2: named forms added since DPW1 (176 reviewed: 141 MKH_D5_ASIA -K rows, 35 HV_D5_NK rows)
- **drop 128**: duplicates of stored rows. 81 arcade cabinets, 25 handhelds and VR headsets, 22 controllers and input devices. Pimax Crystal was filed under a second kind.
- **move_kind 2**:
  - Pimax Portal (an Android handheld) goes to D5.1.2.01.
  - The stored Fanatec CSL DD (a wheel base, by its notes) goes to D5.2.3.06 and waits for attestation.
- No to_line.

Noted, not flagged:
- Retroid appears under both M-retroid and M-goretroid.
- Pimax Crystal sits under tethered although it has a standalone mode.
- Pimax Portal View (a shell with no compute) may belong in D5.1.3.03.
- Flight yokes and sim-racing cockpits have no kind.

## Task 3: scope and wording
- **Alias rows owed** (R-104 b): 14 attribute rows in DPW2_D5_kinds.tsv.
  - 12 are DPW1's regional names: NES Controller, Famicom Controller, Mega Drive Control Pad, Mega Drive 6-Button Controller, Mega Drive 2, Super Nintendo Classic Mini, Nintendo Classic Mini: Super Famicom, Nintendo Classic Mini: Family Computer, Sega Mega Drive Mini, TurboGrafx-16 Mini, PC Engine CoreGrafx Mini, Power Base Converter.
  - 2 were counted as duplicates by DPW1: Zapper Light Gun and Family Fun Fitness.
- **Move waiting for B1**: NF-D5.5.01-005, the N64 Game Storage Tower, stays pending.
  - It waits for the B1 tree to load and for an attested B1 kind that stores several media items: media storage in B1.4.2, or a rack in B1.5.2.
  - The B1 memo has no such kind yet; re-apply with tools/apply_dp.py once one exists.

## Rules applied
C2(a), C3, C9, C10, C11, C5(b) (D5.5 now 21 kinds: display grouping, R-104 b); S3, K-5, K-152; memo D5 sections 4b, 6, 7 and 9; R-58, R-70(d), R-101(d).

## From memory, to confirm (R-104 c)
Pimax Portal, CSL DD as a base only, Subor keyboard body, Odyssey 2 module functions.
