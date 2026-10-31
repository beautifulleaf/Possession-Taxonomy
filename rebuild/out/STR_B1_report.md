# STR_B1 report (B1 Furniture & Storage)

**Counts, before to after:** departments 9 to 10 (new Garden furniture); shelves 17 to 26; kinds 102 to 119; archetypes 197 to 170 (32 generic ones demoted, 5 named classics added). Validator: OK with --v3.

**Category:** added `ax` and a 10-step `key` with a precedence note. Lead unchanged (it already followed RULES.md).

**Departments and shelves:** every department has `t` and `ax`; every shelf has `t`, and `ax` where it has more than 3 kinds. Sofas & armchairs now splits into sofas, armchairs and design lounge chairs, and reclining/rocking/hanging seats. Outdoor seating left it for Garden furniture. Tables gained "Specialist tables"; Beds split into frames, space-saving/portable, mattresses; Nursery into cots and sleepers, and changing/feeding/play; Storage into four shelves plus regional chests; Racks and Screens each got two shelves.

**Kinds:** all 119 now carry hand-written `tt` (grouped by named axes such as Mattress construction, Firmness, Size). Added (source: Wikipedia List of furniture types, or Garden furniture): Headboard, Toddler bed, Drop-leaf table, Chabudai, Sewing table, Washstand, Monks bench, Plan chest, Hoosier cabinet, Pie safe, Hutch, Baker's rack, Umbrella stand, Clothes valet, Garden bench, Picnic table, Patio set. Moved between shelves: Ottoman to stools; Filing cabinet to drawers; Drafting table, Dressing table, Game table to Specialist tables; Tansu and Bandaji to their own shelf; Hammock, Sun lounger, Adirondack chair to Garden furniture. No kinds merged, renamed or removed; none sent to moves (B1_moves.json untouched).

**Generic archetypes demoted to types (32):** Racing-seat PC gaming chair, Sleigh bed, Medieval–Tudor curtained tester bed, Dome-top/Steamer/Wardrobe trunk, China cabinet, Curio cabinet, Chinese hardwood display cabinet, Pedestal/Partners/Rolltop desk, Refectory/Trestle table, Highboy, Commode, Mule chest, Art Deco cocktail cabinet, Danish modern sideboard, Round-corner cabinet, Boulle marquetry cabinet, Bureau bookcase, Secrétaire à abattant, Cylinder secretary, Mission drop-front desk, Milking stool, Byōbu, Byeongpung, Moroccan leather pouf, Iron rocker, Fan-back Adirondack chair, Ladder-back chair. Secretlab Titan/Omega moved to `r`.

**Archetypes added (List of chairs):** Peacock chair, The Round Chair, Grand Prix chair, Brno chair, Djinn chair (maker left blank where unsure).

**Cross-links:** about 40 `see` entries, all targets checked: E2 Camp bed/chair/table/hammock, G3 Fitted wardrobe and Built-in wine cabinet, H2 Bed rail/Care bed/Pressure-relief mattress, H1 Massage chair/Changing mat, B2 covers and toppers, A4 Travel trunk, F2 screen and stand, F3 Coin cabinet, E1 Poker table, D3 TV stands, plus within-B1 pairs.

**References for coverage:** Wikipedia List of furniture types (all furniture shelves), Garden furniture, List of chairs (first 100k characters), IKEA UK storage page. Not sourced: nursery shelf coverage (John Lewis page 404; Firecrawl out of credits), so nursery kinds rest on Wikipedia's list plus existing data. Coverage left unchecked against a specialist retailer for Racks and Screens.
