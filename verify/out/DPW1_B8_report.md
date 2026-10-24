# DPW1_B8 report (B8, wave 3; offline)

All 88 tree kinds are in data. Each new id is the next free id under its parent (R-58).

## Task 1: missing kinds (38 candidates)
**new_kind 16:**
- B8.1.1.10 Rim cylinder
- B8.1.1.11 Mortice latch
- B8.1.1.12 Gate lock
- B8.1.1.13 Cabinet or cam lock
- B8.1.1.14 Shutter or garage door lock
- B8.1.2.4 Garage door defender (no page; HV_NK attests it)
- B8.1.3.7 Locking bar
- B8.1.6.8 Door viewer
- B8.2.2.9 Lithium-battery extinguisher
- B8.4.1.4 Rodent glue trap
- B8.4.1.5 Electronic rodent trap
- B8.4.4.3 Chemical pest repellent
- B8.4.6.5 Ledge bird deterrent
- B8.6.4 Bait station key
- B8.6.5 Bait applicator gun
- B8.6.6 Multipoint lock gearbox

**Other decisions:** named_form 8 (four of them Bird Barrier products under B8.4.6.5), covered 8, attribute 6, other_category 0.

**Rules applied:**
- C2 and C3; C6 for sizes.
- C10: sensing and activation are attributes.
- C12(a): gate and shutter locks.
- C5(d) parts.
- K-138.
- Memo 4b agent axis and memo 9.6 (a latch is B8).

Smoke and CO (B8.2.1.4) is not reopened. Insect bait B8.4.2.3 should read "gel, paste or granule".

**Caution:** apply_dp loads a new kind as attested when its URL is a full fetch in the log. Nine new kinds rest on the harvester's note, not on the log summary: mortice latch, cam lock, shutter lock, locking bar, door viewer, bait gun, electronic trap, chemical repellent and ledge deterrent. Spot-check them first.

## Task 2: named forms (185 reviewed, 8 flagged)
**to_line 4:**
- ABUS 83WP (two rows): duplicate the existing line L-abus-83wp.
- Master Lock Pro Series: L-master-lock-pro-series.
- Architectural Mailboxes Oasis: L-architectural-mailboxes-oasis.

**drop 2:** KryptoFlex 1004 and OnGuard Terrier are bicycle cables, so G1 (memo 9.1).

**move_kind 2:**
- Jackloc Pro 5 restrictor: to window guard B8.3.4.1.
- JT Eaton Double Jeopardy: to B8.4.1.4, pending until that kind is attested.

**Kept:** the Liberty series, Chubbsafes Consul and the ABUS hasp series. Their members differ by size, which is a C3 variant, and memo §6 says a safe line inside one kind is a named form.

## Task 3: navigation
**R-116 is confirmed: hazard, then device, then rated grade.**
- The harvested shops navigate this way: Lock & Key, Safelincs, Zoro, Globe Pest, Target.
- Grades sit on the models: EN 1143-1, UL72, Sold Secure, BHMA.
- About 65 makers each touch only one or two kinds, so the owner role holds.

Refinement (display only, no id change): in Pest control, show target pest first.

**Sketch:**
1. Break-in and theft › 8 device leaves › kinds by grade
2. Fire, smoke and gas › alarms by signal, suppression by agent › kinds by rating
3. Injuries at home › 5 leaves › kinds by standard met
4. Pest control › target pest › method kinds
5. Water leaks › detector
6. Parts and refills › by object served

## † claims
None decides a call. Garage door defender is provisional until attested. The Pro Series line rests on the series name alone.
