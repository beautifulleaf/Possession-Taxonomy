# DPH_D report: domain D structure decisions (offline, Opus)

The five domain D categories are covered: D1 and D5 are built, D2, D3 and D4 are not. The points came from the proposals.tsv structure_flags of each category, plus the session items. No web, no git, nothing written to data/ or framework/.

## Counts per decision
- **D1** (8 rows in kinds.tsv): new_kind 1, covered 1, attribute 2, display_only 2, noted 2.
- **D5** (11 rows): new_kind 3, covered 1, attribute 2, display_only 2, noted 3.
- **D2** (memo notes): display_only 2 (budget filter, help-me-choose view), need 1 (DXOMARK), noted 2. One attribute was added.
- **D3** (memo notes): attribute 3 (sound_signature, use, impedance and sensitivity), noted 2.
- **D4** (memo notes): covered 2 (Micro Four Thirds, bridge), display_only 1 (phone-enough intro), need 1 (C13 rows loaded with the tree), noted 1.

## New kinds (next free id, R-58; to HV_D1_NK and HV_D5_NK attestation)
- **D1.3.6.06 Mouse pad or desk mat.** One kind; size and surface are attributes.
- **D5.2.3.07 Flight yoke.**
- **D5.2.3.08 Flight throttle** (provisional).
- **D5.5.22 Sim cockpit or wheel stand** (provisional).

There are no merges or splits.

## Moves
- NF-D5.2.3.03-007, the Thrustmaster TCA Yoke Pack, moves from flight stick to D5.2.3.07. It waits for the kind's attestation.

## Display groups
- G-D1-23 gains D1.3.6.06.
- G-D5-14 is renamed "Wheels, pedals and flight controls" and gains D5.2.3.07, D5.2.3.08 and D5.5.22.

## Session items
- **Desk mat or mouse pad:** new kind D1.3.6.06.
- **Flight yoke:** new kind D5.2.3.07. Rudder pedals are covered by D5.2.3.02.
- **D1 switch technology:** the switch kinds stay split by feel (D-7). switch_technology becomes an attribute and facet. Keyboards also get switch_feel and adjustable_actuation.
- **D1.9:** kept as it is (ids and group G-D1-49), provisional.
- **D5 age rating:** not stored. ESRB and PEGI rate titles, which are out of scope. Carrier named forms are formats, so age rating is only a future title-ledger link.

## Attributes (15)
- **D1:** switch_technology, adjustable_actuation, switch_feel, laptop_use_class, pad_size_class, pad_surface.
- **D2:** update_support_years.
- **D3:** sound_signature, use, impedance_ohm, sensitivity_db.
- **D4:** sensor_format.
- **D5:** stick_technology, implementation, players_supported.

All are named-form attributes, and all but sensitivity_db are facets.

## Needs (30)
- **Platforms:**
  - D1 (PF_1): sockets, chipsets, memory, form factors, buses and ports, keyboard switch mounts. "Keyboard switch mount" is a proposed new platform_type.
  - D2: OS, stores, finding networks, charging standards, radio services.
  - D3: codecs, multi-room systems, voice assistants, Matter and Thread, eARC.
  - D4 (PF_4): lens mounts, flash shoes, film formats, modifier mounts, battery platforms.
  - D5 (PF_2): console platforms with backward-compatibility relations.
- **Standards:**
  - D1: 80 PLUS, Cybenetics, ATX 3.x / 12V-2x6.
  - D3: IEC 60268.
- **Schemes:**
  - D1: SPL tier list, Tom's Hardware hierarchy, PassMark, Notebookcheck.
  - D2: DXOMARK (with an opacity note), Notebookcheck, AnTuTu.
  - D3: Stereophile, ASR SINAD, RTINGS, Crinacle.
  - D4: DXOMARK.
- **Grading scales:**
  - D2: Iosys, Swappa, Back Market.
  - D4: KEH, Map Camera.
  - D5: completeness, WATA, VGA.

## Thin evidence (provisional)
- **D5.2.3.08 Flight throttle and D5.5.22 Sim cockpit:** no evidence URL. These rest on memory and need an attesting page each.
- **D1.3.6.06:** its only evidence is the deskmat aisle in the Apos navigation (HOL_EV_6), not a product page.
- **D5.2.3.07:** rests on a Wikipedia maker page listing the TCA Yoke Pack.
- **D1.9 keep call and D1 level-2 groups:** no retailer tree was fetched.
- **Value lists:** these come from memory and the memos, and are checked when rows are filled from fetched sources. They are laptop_use_class (the Notebookcheck classes), pad_size_class and pad_surface, sensor_format, stick_technology, implementation and update_support_years.
- **Unfetched evidence:** D2 wearables, e-readers, trackers, radios and power banks; D3 TV, projector and speaker markers; D4 level-1 order and lighting, support and film markers; D5 retail trees, Deck Verified and PEGI. All stay provisional on the memos.
- **Owner names in the needs file:** these are from memory, for example PriceCharting for the completeness scale and SPL for the PSU tier list.

## Files
verify/out/DPH_D_kinds.tsv, DPH_D_moves.tsv, DPH_D_attributes.tsv, DPH_D_needs.tsv, DPH_D_groups_changes.tsv, DPH_D_memo_notes.md, DPH_D_report.md.
