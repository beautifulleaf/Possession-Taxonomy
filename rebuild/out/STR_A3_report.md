# STR_A3 report: Jewellery

**Before → after.** Departments 10 → 10. Shelves 15 → 28. Kinds 91 → 109. Archetypes 197 → 145. `validate.py --v3` prints OK. Backups are in rebuild/work/STR_A3/bak/.

**Category.** Added `ax` and a 10-step placement `key`. The lead is unchanged.

**Departments.** Each has `t` and `ax`, and shelves were regrouped to answer that question: rings by purpose, earrings by where the ornament sits, necklaces by what makes the piece, bracelets by build, brooches by what they fasten, piercing jewellery by form, traditional forms by region.

**Split.** "Ear cuff & jacket" into Ear cuff and Ear jacket; "Tiaras & crowns" into Tiara and Crown. Kanzashi, Binyeo and Fazan went from Hairpin archetypes to kinds in a new East Asian shelf.

**Added** (reference: Wikipedia pages Ring, Earring, Bracelet, Brooch, Body piercing jewellery, List of jewellery types; the same pages were the coverage check for every shelf):
- Rings: Giardinetti, Birthstone, Midi, Promise, Acrostic.
- Earrings: Chandelier, Threader.
- Bracelets: Silicone wristband.
- Brooches: Fibula, Collar pin.
- Body: Chatelaine, Crown.
- Piercing: Spiral barbell, Nipple shield.

**Generic archetypes demoted** to types or definitions:
- Signet face shapes, locket types, cameo materials, grill styles, plug and tunnel styles.
- Pearl and diamond studs, Creole hoop, Sleeper, Akoya strand.
- Ribbon choker, Viking neck ring, period charms, Diamond line and Medical ID bracelets.
- Chain-link cufflink, Flag pin, Button badge.
- Period brooches (mourning, cameo, Edwardian), Bandeau, Circlet.
- Crescent taper, Spiral, Flesh tunnel, and the duplicates Agadez cross and Hei-tiki.

**Moved to `r`.** Maker ranges for Miriam Haskell, Schiaparelli, Gorilla Glass, Kaos Softwear and Diablo Organics. Penannular brooch moved under Fibula.

**Moves.** None new. Championship ring was not added because F3 holds it; it is linked instead.

**Cross-links.** 50 `see` links, all targets checked (A3, F3, F4, F6, H1, A4, C4, D2, E2).

**Caveats.**
- Firecrawl ran out of credits partway, so WebFetch was used for the later pages.
- A few `tt` members are generic and unsourced.
- Brand-register `sig` lists still name some demoted archetypes.
- Ferronnière and Navaratna ring were not added because no page was fetched.
