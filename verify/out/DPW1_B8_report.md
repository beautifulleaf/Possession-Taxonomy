# DPW1_B8 report (B8, wave 3; offline)

There is no DPMK_1_B8 file and no B8 groups rows. All 88 tree kinds are in data, so each new id below is the next free id under its parent (R-58).

## Task 1: missing kinds (38 candidates)
- **new_kind 16**:
  - Locks and restraints: B8.1.1.10 Rim cylinder; B8.1.1.11 Mortice latch; B8.1.1.12 Gate lock; B8.1.1.13 Cabinet or cam lock; B8.1.1.14 Shutter or garage door lock; B8.1.2.4 Garage door defender (no page, so source_url is empty and HV_NK attests it); B8.1.3.7 Locking bar.
  - Door, fire and pests: B8.1.6.8 Door viewer; B8.2.2.9 Lithium-battery extinguisher; B8.4.1.4 Rodent glue trap; B8.4.1.5 Electronic rodent trap; B8.4.4.3 Chemical pest repellent; B8.4.6.5 Ledge bird deterrent.
  - Parts: B8.6.4 Bait station key; B8.6.5 Bait applicator gun; B8.6.6 Multipoint lock gearbox.
- **named_form 8**: euro-profile nightlatch, bathroom lock, cabin or gate hook, First Alert GCO1, and four Bird Barrier products under B8.4.6.5.
- **covered 8** and **attribute 6**: for example, a floor safe, a Class D powder, multi-sensor alarms, heat plus CO, automatic release and a wheeled size. **other_category 0.**

Rules applied:
- C2(a)/(b), C3 and C6.
- C10 rule T: sensing and activation are attributes.
- C12(a): gate and shutter locks have bodies made only for that mount.
- The S3/C5(d) parts sub-family covers the key, gun and gearbox.
- K-138, the memo 4b agent axis, and memo 9.6 (a lock, latch or bolt is B8).
- Smoke and CO (B8.2.1.4) is not reopened.
- Polish: insect bait B8.4.2.3 should read "gel, paste or granule".

**Caution.** apply_dp loads a new kind as attested when its URL is a logged full fetch. Nine of the new kinds rest on the harvester's note, not on the fetch-log summary: mortice latch, cam lock, shutter lock, locking bar, door viewer, bait gun, electronic trap, chemical repellent and ledge deterrent. Spot-check them before applying.

## Task 2: named forms (185 reviewed, 8 flagged)
- **to_line 4**:
  - The two ABUS 83WP rows duplicate the line L-abus-83wp.
  - Master Lock Pro Series becomes L-master-lock-pro-series.
  - Architectural Mailboxes Oasis becomes L-architectural-mailboxes-oasis.
- **drop 2**: KryptoFlex 1004 and OnGuard Terrier are bicycle cables, which go to G1 (memo 9.1).
- **move_kind 2**:
  - The Jackloc Pro 5 restrictor moves to window guard B8.3.4.1.
  - JT Eaton Double Jeopardy moves to B8.4.1.4 and stays pending until that kind is attested.

Kept on purpose: Liberty series, Chubbsafes Consul and the ABUS hasp series. Their members differ only by size, which is a C3 variant, and memo section 6 makes single-kind safe lines named forms. Liberty security levels can become a maker-ladder tier entry (C4(c)(iv)). No shop or maker names were found among the named forms.

## Task 3: navigation
**R-116 is confirmed: hazard, then device, then rated grade.**
- The harvested shops follow this path, for example Lock & Key, Safelincs, Zoro and Globe Pest, and Target.
- Grades sit on the models: EN 1143-1, UL72, Sold Secure, BHMA and the Liberty levels.
- About 65 makers each touch only one or two kinds, so the owner role holds.

One display refinement, with no id change: in Pest control, show target pest first, as pest shops do.

Sketch:
1. Break-in and theft › 8 device leaves (locks to anti-climb) › kinds sorted by grade.
2. Fire, smoke and gas › alarms by signal; suppression by agent › kinds sorted by fire rating.
3. Injuries at home › gates, latches, guards, window and door guards, monitors › kinds filtered by standard met.
4. Pest control › target pest › method kinds.
5. Water leaks › detector.
6. Parts and refills › by the object served.

## † claims
None decides a call. Garage door defender is provisional until attested. The Pro Series line rests on the series name alone.
