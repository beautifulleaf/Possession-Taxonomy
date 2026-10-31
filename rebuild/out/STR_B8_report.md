# STR_B8 report: Home Safety & Security

**Counts, before to after:** departments 6 to 7; shelves 16 to 20; kinds 73 to 78; archetypes 22 to 27. `validate.py --v3` prints OK.

**Category:** added `ax` and a seven-step `key` with a precedence note. The lead now states the threat-then-object order.

**Departments** (all with `t` and `ax`; shelves answer one question each):
- Locks & door security, by where the protection is fitted: door and cabinet locks, add-on security, padlocks and chains, viewers, film and deterrents.
- Locksport & lock collecting is new (a variety department). It was a shelf before: collector locks and keys, practice locks and pick sets.
- Safes & key boxes, by contents: safes and cash boxes, key boxes, post and parcel boxes.
- Alarms, cameras & doorbells: alarms and sensors, cameras and recorders, doorbells.
- Fire, gas & leak safety: detectors and alarms, fire-fighting and escape.
- Child & home safety, by hazard: stairs and doors; cupboards, appliances and furniture; sockets, cords and edges; baby monitors.
- Pest & insect control: rodents, birds and animals; insects.

**Kinds:** all 78 have hand-written `tt`. Patio door lock and Gate, garage & shutter lock moved to the add-on shelf. No kinds were split, merged or renamed, and nothing went to `_moves.json`.
- Dropped from types: spare parts (multipoint gearbox, applicator gun, bait station key, refills, coil holder) and unsourced brand names (P50, Firexo, named cutaway locks).
- The CCTV warning sign moved from Security camera to Property marking kit.

**Added kinds** (each sourced to a fetched Wikipedia page): Electronic padlock (Padlock), Diversion safe (Safe), Alarm control panel & keypad and Driveway alarm (Security alarm), Door knob cover & latch (Childproofing).

**Archetypes added to Antique lock & key:** Egyptian pin lock, Barron double-acting lever lock and Yale pin tumbler lock (Lock and key page), plus Scandinavian (Polhem) padlock and Cast heart padlock (Padlock page). The existing three are kept and sorted by date. None of the 22 existing archetypes was generic, so none was demoted.

**Coverage references** (logged in `rebuild/work/STR_B8/sources.tsv`): Wikipedia Lock and key, Padlock, Safe, Security alarm, Childproofing and Pest control. Pest control added no kinds.

**Cross-links:** 17 `see` entries. They include the two required ones, Door bolt to C8 and Insecticide to C2. The rest go to A4 Luggage lock, G3 Intruder alarm system, G3 Door phone and video intercom, B10 Pet camera, H1 Insect repellent and B1 Playpen, plus 9 within B8. Every target was checked to exist.

**Not sourced or to flag:**
- No fire-equipment page was fetched, so Fire-fighting & escape is unchecked against a list.
- The ISO 7010 sign categories, driveway-sensor types and some `tt` attributes come from general knowledge.
- `B8_moves.json` still sends Multipoint lock to G3, but the 2026-10-28 owner decision puts it in B8. I kept the kind here and left the stale entry.
