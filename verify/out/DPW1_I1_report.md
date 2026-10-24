# DPW1_I1 report: I1 Software decision pass (offline)

## Task 1: missing kinds (11 candidates; "parental control / content filter" split in two)
Result: new_kind 10, covered 1, all other decisions 0. Each new id is the next free number under its parent (R-58):
- I1.1.1.03 Game emulator
- I1.1.3.07 File manager
- I1.1.3.08 Mod manager
- I1.2.04 Disk and file encryption software
- I1.2.05 Parental-control and content-filter software (covers "content filter")
- I1.3.06 OCR software
- I1.3.07 Input method editor
- I1.4.1.10 Desktop-publishing software
- I1.8.1.05 Game engine
- I1.11.04 Download manager

No new leaf needed (I1.2, I1.3, I1.11 stay at 12 kinds or fewer).

## Task 2: named forms (38 flagged)
- **to_line 12:**
  - Windows, macOS, Classic Mac OS and Microsoft Office are release series.
  - Adobe Creative Suite goes to the existing L-adobe-creative-suite.
  - Seven antivirus maker brands come from a Wikipedia category: Avira, Bitdefender, F-Secure, G Data, Sophos, Webroot, Intego.
- **drop 16:**
  - 11 duplicates, so each product keeps one home.
  - Lavasoft is a maker name; its product is Ad-Aware.
  - JetBrains Marketplace plugin is a category name.
  - Visual Studio Community is an edition.
  - Codex CLI is a delivery variant of Codex.
  - BMW real-time traffic information is I3 under sentence 14.
- **move_kind 10:** four rows go to the new kinds (Commander One, Free Download Manager, Xunlei, FineReader). Six go to existing kinds (Miro, Notability, Any.do, Remember the Milk, eM Client, Language Reactor).

Open (no target kind yet): Ichitaro (word processor) and DiskGenius and AOMEI Partition Assistant (partition managers).

## Task 3: navigation by shopper path
Not brand or scene, because:
- 477 of 1,266 named forms have no maker.
- 448 of 521 makers have one named form.
- Only 8 makers reach five or more kinds.
- No scene membership harvested; FOSS, self-hosting and retro are held tags.

View:
1. **What do you want to do?** Look after my computer; protect data and logins; write, plan and organise; make images, video and music; play my media; money and business; learn or look up; build software and games; design and engineer; ask an AI; get online; add-ons.
2. **Which tool?** The kinds, for example antivirus, password manager, VPN, encryption and parental controls.
3. **Which product?** Named forms, filtered by platform (C13) and price model, with an "alternatives to" switch.

A second tab shows maker lines; scene views come later.

## Rules applied
- C2(a), C2(b), C2(d), C1 and C3.
- I-21: releases are named forms, series are lines.
- C11: IME is a generic type, not a regional one.
- Memo sentences 1, 3 and 14.
- Tree precedence (AI code editor; technique inside a medium).
- R-58 ids and R-96(c).
- One home per object.

## Dagger claims
No decision rests on a † claim: all 68 kinds were attested by HV_I1_1. The new-kind sources are the harvester's URLs. The weakest are the mod-manager page and the ATOK article; confirm those before loading if R-70(d) applies.
