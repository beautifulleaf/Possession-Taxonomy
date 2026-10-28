# FIX_B8 report
Before: 73 kinds, 15 archetypes, 97 brands. After: 71 kinds, 22 archetypes, 98 brands (validate OK).

- **B8-1 done (partly):** Padlock gains 4 archetypes (Master Lock No. 3, American Lock 1100, ABUS Granit 37, Abloy PL362); new kind "Antique lock & key" (Bramah lock, Chubb detector lock, Roman padlock; period types). Brands added: American Lock, Bramah. Not added (no fetched source): puzzle/trick padlocks, Abloy PL350/PL358, 37/80 etc. Padlock `s` filled.
- **B8-2 done:** 11 kinds with 10+ models cut to 6 (brand-diverse; I could not verify test winners); Union mortice codes became one range; Kidde fire-blanket SKUs became one range; Dummy camera removed and added as a type of Security camera (kinds -1).
- **B8-3 partly:** Locking bar, Garage door defender and Ground anchor merged into "Shed & garage security" (kinds -2, +1). Skipped: empty Cabinet lock, Security chain, Cable lock, Key cabinet stay as kind-level entries with types (an owner can plausibly hold one; no sourced models).
- **B8-4 partly:** "Abus" normalised to ABUS; Yale Home merged into Yale (brands -1). Skipped Honeywell/Honeywell Home and Philips/Philips Hue: they are different companies/licensees (Resideo, Signify), not renames.
- **B8-5 done by owner decision:** door and window locks stay in B8; lead no longer says multipoint locks live in Home Fixtures. Duplicates kept: Wireless alarm kit / Video doorbell vs G3 Intruder alarm system / Door phone (portable add-ons vs installed; noted only).
- **B8-6 done:** new "Monitors" shelf (Baby monitor) in Child & home safety; department renamed "Pest & insect control".

**Conflict for the coordinator:** B8_moves.json still has "out" entries sending Multipoint lock and Multipoint lock gearbox to G3. They contradict the owner decision (multipoint lock now moves to B8) and I could not remove entries. Window guard, Intruder alarm system and Door phone entries stay. Multipoint lock arrives in "Door locks" at merge; I did not create it.
