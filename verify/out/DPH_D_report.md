# DPH_D report: domain D structure decisions (offline, Opus)

Covers D1 and D5 (built) and D2, D3, D4 (unbuilt), from the proposals.tsv structure_flags and the session items. No web, no git, nothing written to data/ or framework/.

## Counts per decision
- **D1** (8 rows): new_kind 1, covered 1, attribute 2, display_only 2, noted 2.
- **D5** (11 rows): new_kind 3, covered 1, attribute 2, display_only 2, noted 3.
- **D2** (memo notes): display_only 2, need 1, noted 2, plus one attribute.
- **D3** (memo notes): attribute 3, noted 2.
- **D4** (memo notes): covered 2, display_only 1, need 1, noted 1.

## New kinds (R-58; to HV_D1_NK and HV_D5_NK)
- D1.3.6.06 Mouse pad or desk mat (one kind; size and surface are attributes).
- D5.2.3.07 Flight yoke.
- D5.2.3.08 Flight throttle (provisional).
- D5.5.22 Sim cockpit or wheel stand (provisional).

No merges or splits.

## Moves and groups
- NF-D5.2.3.03-007 (TCA Yoke Pack) moves to D5.2.3.07 once that kind is attested.
- G-D1-23 gains D1.3.6.06.
- G-D5-14 is renamed "Wheels, pedals and flight controls" and gains the three new D5 kinds.

## Session items
- **Desk mat:** new kind D1.3.6.06.
- **Yoke:** new kind D5.2.3.07; rudder pedals are covered by D5.2.3.02.
- **Switch technology:** an attribute. The switch kinds stay split by feel (D-7).
- **D1.9:** kept, provisional.
- **Age rating:** not stored. It rates titles (out of scope), and carrier named forms are formats; it is a future title-ledger link only.

## Attributes (15, all on named forms)
- **D1:** switch_technology, adjustable_actuation, switch_feel, laptop_use_class, pad_size_class, pad_surface.
- **D2:** update_support_years.
- **D3:** sound_signature, use, impedance_ohm, sensitivity_db.
- **D4:** sensor_format.
- **D5:** stick_technology, implementation, players_supported.

All are facets except sensitivity_db.

## Needs (30)
- **Platforms:**
  - D1 (PF_1): sockets, chipsets, memory, form factors, buses and ports, and a proposed "keyboard switch mount" type.
  - D2: OS, stores, finding networks, charging standards, radio services.
  - D3: codecs, multi-room systems, voice assistants, Matter and Thread.
  - D4 (PF_4): mounts, shoes, film formats.
  - D5 (PF_2): console platforms.
- **Standards:** 80 PLUS, Cybenetics, ATX 3.x, IEC 60268.
- **Schemes:**
  - D1: SPL tier list, Tom's Hardware, PassMark, Notebookcheck.
  - D2: DXOMARK (with an opacity note), Notebookcheck, AnTuTu.
  - D3: Stereophile, ASR, RTINGS, Crinacle.
  - D4: DXOMARK.
- **Grading scales:** Iosys, Swappa, Back Market, KEH, Map Camera, completeness, WATA, VGA.

## Thin evidence (provisional)
- **Flight throttle and sim cockpit:** from memory, no evidence URL.
- **Desk mat:** rests only on the Apos deskmat aisle (HOL_EV_6).
- **Yoke:** rests on a Wikipedia maker page.
- **D1.9 keep call and D1 level-2 groups:** no retailer tree was fetched.
- **Value lists from memory or memo:** laptop_use_class, pad_size_class, pad_surface, sensor_format, stick_technology, implementation, update_support_years. Owner names in the needs file are also from memory.
- **Markers and orders on memo only:** D2 wearables, e-readers, trackers, radios and power banks; D3 TV, projector and speaker; D4 level-1 order, lighting, support and film; D5 retail trees, Deck Verified and PEGI.
