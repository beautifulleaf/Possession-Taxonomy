# STR_C7 report (Farm & Forestry Equipment)

Before -> after: departments 5 -> 6; shelves 24 -> 25; kinds 113 -> 118; archetypes 72 -> 77. validate.py --v3: OK.

**Structure.** Category ax and 6-step key written. Old "Compact tractors & implements" and "Farm-scale machines" mixed tractors, soil, crops and forestry by scale. Regrouped by job: Tractors & tractor fittings (4 shelves), Loaders & earthmoving (3), Field implements & crop machines (8, in crop-year order: ground, sow, crop care, irrigation, cut, hay, harvest), Woodland & firewood (3, by stage), Smallholding livestock (4), Vintage tractors & engines (3). Every department and shelf has t and ax; kinds ordered along each shelf's axis.

**Kinds.** All flat t lists replaced by hand-written tt groups (spare-part types of the shearing machine and milk-meter fitting dropped). Mowers and haymaking shelves split into cutting and after-cutting steps. Milking robot, parlour, bucket machine and bulk tank moved into Milking & dairy; forest machines (harvester, forwarder, skidder, feller buncher, crane) joined winch and trailer in Felling & extraction; hand grain mill moved to Harvesting & grain handling. Vintage shelf split into Vintage tractors, Stationary engines, Barn & field machinery. No kinds merged, renamed or moved out; no renames file needed. Existing _moves.json untouched.

**Added kinds (reference fetched).** Sickle-bar mower (Wikipedia Sickle bar mower), Windrower (Wikipedia Windrower), Hedge cutter (Wikipedia Hedge trimmer), Chaff cutter (Wikipedia Chaff cutter), Vintage combine harvester with 5 archetypes (Sunshine Header-Harvester, Holt, Gleaner, Massey-Harris, Claas Hercules; Wikipedia Combine harvester). Brands H. V. McKay, Gleaner Manufacturing Company, Claas added to C7_brands.json (minimal entries, no founding years).

**Coverage references.** Wikipedia Agricultural machinery (all shelves), Kubota implements page (field and hay shelves), Wikipedia Tractor (tractors). Forestry equipment Wikipedia page returned 404; woodland and livestock shelves not checked against a full reference list.

**Generic archetypes demoted.** None existed in C7 (archetypes only in vintage kinds, all named).

**Cross-links (13).** Log splitter, Wood chipper, Snow blower, Garden tiller (x2), Hedge trimmer (x2), Winch, Garden sprayer, Surface pump, Utility trailer, Riding mower, Model engine, and Rotary cutter -> C4 Rotary cutter (different object, fabric cutter; both kept). All targets verified in reader files.

**Not done.** Electric fence energiser and post driver not added (C8 holds fencing). Fetch page for livestock handling equipment not found; no retailer list checked. Founding years of new brands unsourced. Archetype versions for new combines left empty.
