# FIX_G3 report

Counts: kinds 123 -> 125 (+3 new, -1 moved to B8); archetypes 192 -> 193.

- G3-1 (13 leftover departments): already resolved in rebuild/out/G3.json (6 zones only, no instruction-named departments, no kind outside the zones). No change.
- G3-2 (empty duplicates: Tap, Wall switch, Garden kitchen, Kitchen cabinet, Door frame, Oven, Bath panel, duplicate shower screens): none exist in the current file; skipped as already done.
- G3-3: partly. Multipoint lock sent to B8 via G3_moves.json (owner decision: locks stay in B8) and removed. Range cooker, Heat-storage range cooker (AGA, La Cornue, Lacanche, Falcon), Built-in wine cabinet (EuroCave), Intruder alarm system and Door phone remain in G3 as duplicates of B5/B8 (not clearly homed by RULES.md); B5/B8 fixers should resolve and cross-link.
- G3-4: done. Wall socket types cut from 15 plug letters to UK / EU Schuko / US / other; Hard-shell hot tub models removed (ranges kept); all Dunster House models removed from 10 kinds (ranges Leviathan, Utopia, Overlord kept); Built-in coffee machine and Warming drawer cut from 4 Miele codes to 1 each. Adding other market brands to those two was not done (no fetched source).
- G3-5: partly. Added Fitted wardrobe (Structure & circulation, new shelf Fitted storage), Home cinema room, Wine cellar (Wikipedia sources fetched). Staircase gains a Spiral staircase archetype (Wikipedia). Not done: cantilever/floating stair archetype (no fetched page confirming it), and cross-linking C8 tile and ironmongery traditions (no cross-link field in schema; left to C8).
- Owner decision on built-in lighting: nothing created; the B3 fixer will send those kinds; no "Built-in lighting" department added yet (empty departments invalid).

Validation: OK (0 errors).
