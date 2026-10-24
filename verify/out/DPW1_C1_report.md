# DPW1_C1 report: C1 Tools & Workshop Equipment (offline)

## Task 1: missing kinds (116 rows)
new_kind 70, named_form 24, covered 17, attribute 4, other_category 1 (the piercing saw goes to C4, step 28). There was no DPMK_1_C1 file to skip against. Ids are the next free number under each parent (R-58).

New kinds:
- **Saws:** C1.1.1.18–.28 back saw, coping saw, vertical panel saw, reciprocating saw, plunge saw, cut-off saw, contractor table saw, straight-line rip saw, kataba, keyhole saw, bow saw
- **Axes & splitting:** C1.1.3.05 kindling splitter
- **Drills:** C1.2.1.06 magnetic drill, .07 hand drill
- **Spanners & wrenches:** C1.2.3.06–.08 pipe wrench, basin wrench, box spanner
- **Planes:** C1.3.1.09–.12 block, shoulder, router and plough planes
- **Files & rasps:** C1.3.3.05 rasp
- **Grinders & sanders:** C1.3.4.07–.12 sheet, detail, drywall, spindle and belt-disc sanders, wall chaser
- **Routers:** C1.3.5.04 biscuit jointer
- **Lathes & mills:** C1.3.6.05 combination lathe-mill
- **Hammers:** C1.4.1.05–.11 club, brick, ball-pein, cross-pein and slater's hammers, sledgehammer, punch
- **Pry bars:** C1.4.2.02–.04 pry bar, nail puller, lifting bar
- **Welding & soldering:** C1.5.1.05 plasma cutter, C1.5.2.03 gas soldering torch
- **Work holding:** C1.6.07 router table, .08 saw stand
- **Measuring:** C1.7.1.04–.06 line laser, rotary laser, optical level; C1.7.3.03 angle finder; C1.7.4.02–.08 detector, moisture meter, IR thermometer, inspection camera, sound level meter, clamp meter, oscilloscope
- **Ladders & lifting:** C1.8.1.06–.08 single, roof and tripod ladders; C1.8.2.07–.09 engine stand, transmission jack, scissor jack
- **Handling & site machines:** C1.8.3.04 pallet truck; C1.8.4.08 backhoe loader
- **Pumps:** C1.9.3.03 surface pressure pump
- **Tool storage:** C1.10.07–.09 tool chest, site chest, tool pouch
- **Welding consumables:** C1.12.4.04–.06 tungsten electrode, brazing rod, flux

Every new kind has a harvester URL logged full or partial, ready for HV_C1_NK. The structure is not reopened: C1.6 now holds 8 kinds and C1.10 holds 9.

## Task 2: named forms (66 rows)
- **move_kind (2):** M18 FMDP to the magnetic drill; Shinto saw rasp to the rasp.
- **to_line (3):** ESAB Sureweld, Irwin Vise-Grip (pliers and clamps), Thor Thorex.
- **drop (61):** names that only repeat the kind, with a maker, size, grade, material or spec added and no model name or code. Examples: "Torque Wrench", "Japanese Waterstones", "Domestic Extension Ladder". This follows DPW1_C2.

None is a maker or a shop. Same-name maker pairs (M-axminster/-tools, M-milwaukee/-tool, M-roughneck/-tools, M-sip/-tools, M-c-k/M-ck-tools, M-stanley/-black-decker) need a merge pass.

## Task 3: navigation
I confirm R-116: the way in is **type of object (tool family by job)**.
- No scenes were harvested.
- 488 forms spread over 124 kinds and 122 makers; 48 of these makers hold a single form.
- DeWalt, Milwaukee and Makita cross dozens of kinds.
- The harvested shops open on tool type.
- Brand goes to a battery-platform tab and a premium hand-tool makers tab.

View:
1. **Level 1:** the nine groups, from Cutting & sawing to Bits, blades & accessories.
2. **Level 2:** the leaves; Drilling & driving has Drills, Screwdrivers & drivers, Spanners & sockets.
3. **Level 3:** the kinds; Drills runs brace, hand drill, drill/driver, hammer drill, rotary hammer, drill press, magnetic drill.

A Hand / Power / Machine / Cordless toggle sits on every group.

## Rules applied
R-58, R-60c, R-116, C2, C5(b), C10, C11, C12(a), C-10, K-12, K-13, K-132, K-147, K-171, K-173, K-175, K-190, K-194.

## Resting on † claims
- The plough plane is not in its page's logged text.
- I read "scissor stand" as a scissor jack and "garden ladder" as a tripod ladder.
- The plasma cutter's leaf and flux under K-12 are by analogy.
- The kataba is provisional (two regions).
- The Makita CP100D may not be an oscillating tool; I left it in place.
