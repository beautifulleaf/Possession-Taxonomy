# D1R: D1 rebuilt to shopper paths (R-71)

Offline; no data changed. Outputs: verify/out/TREE_D1_v2.md, verify/out/D1R_crosswalk.tsv (119 rows, 101 ids changed), framework/structure/D1.md (sections 3, 12, 13; backup in verify/work/D1R/).

## New structure (119 kinds)

- D1.1 Computers (9, no leaf)
- D1.2 PC parts (25), with leaves in PCPartPicker order:
  - Processors 1, Cooling 8, Motherboards 2, Memory 2, Internal storage 2
  - Graphics cards 2, Cases 1, Power supplies 1, Expansion cards 5, Internal cables 1
- D1.3 Peripherals and desk setup (22): Keyboards 3, Keyboard kits and parts 7, Mice and pointing 3, Monitors 1, Webcams, microphones and capture 3, Docks and desk accessories 5
- D1.4 Printing and scanning (8, no leaf)
- D1.5 External storage and media (9, no leaf)
- D1.6 Networking and backup power (8, no leaf)
- D1.7 Cables, adapters and chargers (10, no leaf)
- D1.8 Electronics and maker parts (19; leaves unchanged)
- D1.9 Point of sale and security devices (6, no leaf)
- D1.10 Parts made for one computer or peripheral (3, no leaf)

**D1.9 is not one of the owner's eight paths.** Added because none of the eight holds point-of-sale or security devices. Owner queue: keep it?

## Moves and why

- Single-board computer to Computers (owner shape).
- Internal SSD and HDD to PC parts (a build slot).
- Optical and floppy drives to External storage, bay or USB alike.
- Dock, KVM switch, monitor arm, laptop stand and cooler to Docks and desk accessories.
- Keyboard kit, switches, keycaps, plate and stabiliser to Keyboard kits and parts.
- Ink, toner and filament to Printing.
- HAT/shield board to Maker boards; barcode scanner to Point of sale; UPS to Networking.
- D1.10 keeps only the laptop AC adapter, battery and sleeve (C5(d)).
- Seven definitions were reworded; no cross-category home changed.

Old and new ids overlap (D1.2.3.01 was DIMM and is now the motherboard), so the data move must apply the crosswalk in one pass.

## Judgment calls (test items)

Single-board computer (Computers or maker parts); board with CPU fitted against single-board computer; bay-fitted optical drive; UPS; barcode scanner; USB-C hub with pass-through charging against dock; KVM switch; monitor arm; laptop stand or cooler against sleeve; keyboard kit against keyboard; HAT; external GPU enclosure; external capture device against capture card; laptop AC adapter against generic charger; macro pad against numeric keypad.
