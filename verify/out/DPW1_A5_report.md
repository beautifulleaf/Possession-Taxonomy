# DPW1_A5: decision pass, A5 Clocks & Watches (offline)

Inputs: TREE_A5.md, the A5 memo (§4b, §6, §9, §10, §14), the A5 row of proposals.tsv, CONVENTIONS C1–C3, C5, C11, C12, D4 (R-58, R-70, R-71, R-116 b, R-121), and the 53 kinds, 99 named forms and 5 lines in data/ with verify/work/HV_A5_1/fetched.tsv. There were no HV_A5 reports (wave 2), so the candidates come from the caller's list, the "gave" column and the memo's † clock parts. Every tree kind was attested.

## Task 1: 34 candidates (verify/out/DPW1_A5_kinds.tsv)
- new_kind 9, covered 13, attribute 6, other_category 3 (multi-watch winder B1; watch box or roll B1; watchmaker's tool C1), named_form 3 (shield, chalet and carved cuckoo clocks under A5.3.3.04, none tied to a maker, with a region tag).
- **New kinds.** A5.5 now holds 17 kinds, well over C5(b)'s "about 12". So the leaf axis the tree already states (object served, CV-17; memo §10: "no leaf until a count passes about 12") is opened now:
  - **A5.5.1 Made for a watch.** The existing A5.5.01–08 move into this leaf. Their ids stay as they are (R-58: an id records where the kind was first placed and is never renumbered). New: A5.5.1.01 Watch hands, A5.5.1.02 Watch crown, A5.5.1.03 Watch clasp or buckle, A5.5.1.04 Watch spring bar.
  - **A5.5.2 Made for a clock.** A5.5.2.01 Clock movement, A5.5.2.02 Clock hands, A5.5.2.03 Clock dial, A5.5.2.04 Clock pendulum, A5.5.2.05 Clock insert (fit-up).
  - Seven of the new kinds have a harvester URL (ClockParts.com, Perrin, HoroParts). The clasp or buckle and the spring bar have none, so they wait for attestation in HV_A5_NK.
  - **For the applier:** the leaf column of A5.5.01–08 has to be set to A5.5.1. The moves file cannot express this.
- **Complications** (chronograph, GMT, perpetual calendar, minute repeater, tourbillon, moon phase) are all *covered*. They are already kinds under A-23, because buyers compare makers at that level (Chrono24 pages and shop function filters, memo §4b). Minute rattrapante is covered by the split-seconds chronograph. A tellurium display is a complication attribute.
- Clock kits are a bundle variant of the clock movement (C3). Radio-controlled "atomic" home clocks take an attribute on their placement kind. They are not A5.4.07.

## Task 2: 9 moves (verify/out/DPW1_A5_moves.tsv)
- **to_line 7.** Each of these is a range of distinct models, so it becomes a lines row (R-70 a): Casio LTP, Seiko Prospex Marinemaster and Speedtimer, Tudor Oysterdate Chronograph, Longines Evidenza, and WOLF Brogue and Earth.
- **move_kind 1.** Sky-Dweller moves to A5.1.5.02. The tree's precedence rule names it by name: calendar comes before multi-zone.
- **drop 1.** WOLF Den is a four-watch winder safe, which belongs to B1. Re-file it when B1 is built.
- **Kept on purpose:**
  - G-SHOCK 5600 is one iconic case design; its references are variants (memo §4b).
  - "Jumping Hours" (Andersen) is the maker's own collection name.
  - Calibres (6R15, NH35 and the rest) are watch-movement named forms that also need platform rows.
- **Note:** "Sport chain" looks like a generic chain type and is probably not bound to one maker (Dueber). This needs a maker_bound fix, which the moves file cannot express.

## Task 3: navigation
**Decision: scene-first, with the "watch family" as the scene, then brand (house), then model. Clocks and parts use shopper paths.**

**Reason.** The owner names watches as scene-driven, and R-116(b) already says "A5 opens by watch family then house". The harvested data agrees:
- Every one of the 47 wristwatch named forms is tied to a maker.
- The lines are house collections (Prospex, Seamaster, Portugieser, Royal Oak).
- The sources are organised brand → family (WatchBase, Chrono24's roughly 600 brands).
- Clocks and parts were harvested by type and placement (Sellingantiques, NAWCC and ClockParts counts), with no brand-led evidence.

Watch families stay design_family and maker_class values, shown for display only (§14 flags 2 and 3). The complication tree stays as the "what is it" tab.

**View sketch:**
1. **Level 1:**
   - Tool watches (dive, chronograph, GMT and world time, pilot, field and military, racing)
   - Dress and classic
   - Haute horlogerie and complications
   - Independents and microbrands
   - Tough and digital
   - Fashion and jewellery
   - Vintage and pocket
   - Clocks
   - Timing instruments
   - Straps, winders and parts
2. **Level 2:**
   - Watches: houses A–Z within the family, with tier views.
   - Clocks: by placement (floor; table and shelf; wall; portable and marine; building).
   - Parts: by object served (for a watch; for a clock).
3. **Level 3:**
   - Watches: collection (line) and then model, with reference variants below.
   - Clocks: by kind, then maker or design.
   - Parts: by part type.

## Rules applied
C2(a), C2(b), C2(d), C3, C5(b), C5(d), C11, C12(a), R-58, R-70(a), R-116(b), the A5 tree precedence lines, memo §4b, §9.7 and §10, and CV-17.

## Decisions resting on † claims
Clock parts were † in the memo. They now rest on fetched shop pages, except the watch clasp or buckle and the spring bar, which are unattested until HV_A5_NK. The clock calls are provisional, because they rest on the memo and HV_A5_1 only (§14 flag 4).
