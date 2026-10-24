# DPW2_I1 report: I1 Software, second decision pass (offline)

## Task 1: missing kinds (53 candidates)
Sources: the MKH_I1_ASIA, EUR and NAO lists, the five items the session-6 prompt names, and the two partition managers DPW1 left open. HV_I1_NK listed no missing kinds.
- Merged items that appear in two reports: EDA, 2D animation, DJ, mind mapping, e-book reader, word processor, ERP.
- Skipped because DPW1 decided them: desktop publishing (now I1.4.1.10) and parental control or monitoring (now I1.2.05).

| Decision | Count |
|---|---|
| new_kind | 42 |
| covered | 4: website builder to I1.8.1.06; DRM to I1.2.04; document capture to I1.3.06; slideshow maker to I1.4.2.01 |
| other_category | 5: transit search, Amap and NNG navigation, and 3CX VoIP go to I3 (step 5 note); Symbian mobile OS goes to D2 (sentence 5) |
| attribute | 2: legal and library verticals are a market tag (I-4) |

New kinds, each under the next free id per R-58 (checked against data/kinds.tsv):
- **I1.1.1:** .04 compatibility layer, .05 screen saver
- **I1.1.2:** .06 data recovery, .07 partition manager, .08 PC migration
- **I1.2:** .06 password recovery
- **I1.3:** .08 word processor, .09 spreadsheet program, .10 presentation program, .11 mind mapping, .12 speech recognition and dictation, .13 collection cataloguing
- **I1.4.1:** .11 photogrammetry, .12 diagramming
- **I1.4.2:** .04 2D animation, .05 compositing and VFX, .06 screenwriting
- **I1.4.3:** .03 DJ software, .04 singing voice synthesiser, .05 text-to-speech and AI voice generator
- **I1.5:** .03 e-book reader app, .04 show control
- **I1.6.2:** .02 survey and form, .03 digital signage
- **I1.6.3:** .02 ERP, .03 groupware, .04 time tracking, .05 workforce management
- **I1.7:** .03 typing tutor, .04 machine translation, .05 CAT tool, .06 e-learning authoring
- **I1.8.1:** .06 web design, .07 software modelling (UML)
- **I1.8.2:** .04 web and application server, .05 application and infrastructure monitoring, .06 terminal emulator, .07 business intelligence
- **I1.9:** .05 EDA and PCB design, .06 planetarium, .07 CAE and simulation
- **I1.11:** .05 peer-to-peer file-sharing client

Of the 42 new kinds, 17 carry the harvest report's URL. The other 25 have no URL in the reports, so HV_I1_NK2 must find a page for each. Each row's reason says what that page must show.

## Task 2: named forms (13 flagged)
The 140 HV_I1_NK rows are the only I1 forms added since DPW1. None has a batch-suffix id.
- **drop 6:**
  - Three duplicates of rows DPW1 had already moved into the same kind: Commander One, ABBYY FineReader, Free Download Manager.
  - DownThemAll! keeps its browser-extension home, and Konqueror keeps its web-browser home.
  - NetGenie is a network appliance (its own row note says so), so it is D1 hardware, not software.
- **move_kind 7:** these are older rows that DPW1 did not flag. They wait for their new kinds to be attested.
  - DiskGenius and AOMEI Partition Assistant go to I1.1.2.07 (this closes the DPW1 open item).
  - Ichitaro goes to I1.3.08 (this closes the DPW1 open item).
  - Visio goes to I1.4.1.12.
  - Dreamweaver goes to I1.8.1.06.
  - COMSOL goes to I1.9.07.
  - LimeWire goes to I1.11.05.
- **to_line 0.**

## Task 3: scope and wording checks
The task named none. Two things to watch:
1. **I1.3 now holds 13 kinds** (about 12 is the leaf-null limit, C5b). As in R-104(b), ids are not renumbered and the page groups them for display. A leaf split (writing and documents; planning; input) is a structure question for the owner, not taken here.
2. **The I1.6 leaves stay** Finance and accounting, Marketing and sales, and Operations. ERP, groupware, time tracking and workforce management all go to Operations. A "people and HR" leaf may be worth opening when payroll arrives.

Also noted:
- Tableau's maker tie to I1.9.03 should move to I1.8.2.07.
- HCL Notes stays an email client.

## Rules applied
- C2(a) and C2(b), C3 and C11. No candidate is regional: the singing synthesiser and the IME are generic.
- Memo 4b: a suite component becomes a kind when it is sold alone.
- Boundary sentences 1, 4, 5, 8, 10 and 12, and the step 5 notes.
- I-4: market is a tag, and business kinds are placed by function.
- Precedence: a technique inside a medium.
- R-58 ids, R-101(d) pending moves, and one home per object.

## † claims
No decision rests on a † claim from the memo. Several placements rest on general knowledge of the products, not on a fetched page: LimeWire's protocol history, COMSOL, Visio, Dreamweaver, and Frostbite as EA's in-house engine. Frostbite was not flagged, but it is worth checking whether it was ever licensed to outside studios. Attestation confirms the kinds; the moves can be checked at that point.
