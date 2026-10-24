# C2 Garden & Grounds: decided tree

Category: C2 Garden & Grounds (domain C, Making, Growing & Work). Membership test (key step 29): made for growing plants or keeping gardens, grounds, paths, pools and drives, powered or not: garden tools, mowers and ride-on mowers, trimmers, leaf blowers, pressure washers, snow clearers, wheelbarrows, planters and plant pots, plant care products, grow lights, irrigation, greenhouses and polytunnels, compost bins, artificial turf, garden stone, above-ground and inflatable swimming pools, pool cleaning equipment, test kits and pumps, together with parts, attachments and consumables made for one kind of C2 machine (S3). Not here: garden furniture and plant stands (B1); garden ornaments, statues, gnomes, fountains and stone lanterns (B4); bird baths (B10); paddling pools made for play and garden trampolines (E1); seeds, bulbs, living plants, sod and live moss (C3); axes, wedges, log splitters, sack trucks, tool storage, platform batteries and chargers, and drainage, transfer, sump and general pumps (C1); tractor-driven splitters and chippers, farm tractors with a rear power take-off and a Category 1 or larger three-point hitch, and field-crop irrigation (C7); aggregate, paving, edging, membrane, fencing, gates and fuels (C8); household pest killers, traps, bird spikes and letterboxes (B8); hot tubs and their equipment (B7); in-ground pools and garden buildings (G2); gardening wear (A1, A2); weather instruments (C6). Structure (Candidate A, job-first, C-2; memo sections 3 and 10): sub-family (the garden job the object serves; the closing parts sub-family C2.10 is exempt from this axis, C5(d)), then leaf (the axis stated per sub-family; C2.1, C2.4 and C2.8 hold about 12 kinds or fewer and store `leaf = null`, C5(b), so their kind ids carry no leaf part, and the memo's reading groups there are display only), then kind (the generic type, distinguished by form or mechanism where buyers compare within it: cylinder against rotary mower, sand against cartridge filter). Each object gets one kind. Power source (`drive`: manual, corded electric, cordless, petrol, pneumatic, PTO), mounting (`mount`: hand-held, wall, free-standing, ride-on, trailed), setting, market, material (except where it makes the form, fabric grow pot), brand, price band and region are attributes, tags, ledgers or views, never kinds (C-1, CV-24, CV-28); a manual and a powered version of the same form share one kind, and a powered tool of a different form is its own kind. Attributes decided at the build (memo section 14, DPH): `lawn_area_suited` on mower named forms (the mowers page asks lawn size before mower type), `hand_size` on secateurs and loppers named forms, `cutting_action` (bypass, anvil, ratchet) confirmed as an attribute, `spare_battery_available` on cordless machine named forms linked to the battery platform row; grow lights are one kind with lamp technology an attribute (C-14). Platforms and shaft systems (Gardena combisystem and Micro-Drip, Stihl AK, Stihl KombiSystem, Ryobi Expand-It, hitch categories) are rows of the compatibility ledger (C13), never kinds or named forms; brand product lines of everyday consumables are lines rows (CV-46); the EU product-function class is a row of the jurisdiction ledger (C17). Maker role: owner (maker_roles.tsv, provisional: garden equipment models carry the maker; brand is the last step for machines, and for secateurs and Japanese hand tools the maker line is what is compared, carried by named forms). Display groups (navigation proposal, display only; C2 is not built, so no group ids are issued): level 1 shows the ten sub-families re-ordered with lawn first: Lawn care (C2.3); Cutting, pruning & hedges (C2.2); Digging & planting (C2.1); Clearing, cleaning & snow (C2.4); Watering, irrigation & ponds (C2.5); Pots, beds & plant supports (C2.6); Soil, feed & plant protection (C2.7); Greenhouses & indoor growing (C2.8); Pools & pool care (C2.9); Parts & spares (C2.10); level 2 shows the memo leaves; side views: a battery platform tab shared with C1 and a hand-tool makers tab for pruning tools. Quality markers (display): machines by cut quality, ease of use, battery run time and spare-battery availability, reliability and durability, noise, build and deck material, energy; hand cutting tools by blade sharpness and steel, clean cut, durability and spare parts, balance and fit to hand size, warranty; grow lights by PPE and PPFD; pots by frost-hardiness and drainage (provisional). A kind marked † is named only by the key, a decision or a category heading, or rests on a claim not yet shown on a fetched page, and needs a fetched page before it enters the data (memo attestation list, section 10; section 14 for the garden multi-tool).

Ids (R-58): C2.n is a sub-family and C2.n.m a leaf; a kind is C2.n.m.kk, or C2.n.kk where a sub-family has no leaf.

## C2.1 Digging, planting & cultivating tools

No leaf (about 12 kinds or fewer, leaf = null); kind ids carry no leaf part. Reading groups in job sequence (display only): digging (01 to 04), planting (05, 06), cultivating (07 to 09), sifting (10). Kind axis: tool family; handle length, blade and the maker system (C13) are attributes. Choice level provisional (no "best spade" list fetched).
- C2.1.01 Garden spade: long-handled tool with a flat, sharp-edged blade pushed in by foot to dig and cut soil.
- C2.1.02 Garden fork: long-handled tool with stout tines to dig, loosen and turn soil.
- C2.1.03 Shovel: long-handled tool with a broad, dished blade to lift and move loose soil or material.
- C2.1.04 Mattock: swung tool with a heavy head carrying an adze blade, used to break hard ground and cut roots.
- C2.1.05 Hand trowel: short-handled scoop-shaped blade for digging small planting holes. †
- C2.1.06 Bulb planter: tool that cuts and lifts a plug of soil to make a hole for a bulb.
- C2.1.07 Hoe: long-handled tool with a blade drawn or pushed through the soil surface to weed and loosen it.
- C2.1.08 Hand cultivator: tined tool, hand-held or on a handle, that breaks up and aerates the soil surface.
- C2.1.09 Garden rake (soil rake): rake with short rigid teeth on a straight head to level and break soil.
- C2.1.10 Garden sieve: framed mesh riddle that sifts soil or compost.

## C2.2 Cutting & pruning

Leaf axis: the thing cut (branches, hedges, grass and brush). Kind axis: tool or machine form, in order of working scale; `drive`, cutting action, capacity and the battery system (a C13 row) are attributes.

### C2.2.1 Pruners & branch cutters
- C2.2.1.01 Secateurs: one-handed scissor-action pruning shears for stems and small branches, manual or powered; bypass, anvil and ratchet are the attribute `cutting_action`.
- C2.2.1.02 Loppers: long-handled two-handed pruning shears for thicker branches.
- C2.2.1.03 Pruning saw: hand saw with a toothed blade made to cut living branches.
- C2.2.1.04 Pole pruner (high-branch shears): pruning head on a long pole, worked from the ground to cut high branches.
- C2.2.1.05 Chainsaw: hand-held saw with a powered toothed chain running round a guide bar, for felling, pruning and cutting wood (`drive` petrol, cordless or corded; K-173).
- C2.2.1.06 Pole saw: powered saw head on a long pole for cutting high branches from the ground (K-173). †

### C2.2.2 Hedge cutters
- C2.2.2.01 Hedge shears: two-handed long-bladed shears for clipping hedges and shrubs.
- C2.2.2.02 Hedge trimmer: powered tool with a reciprocating toothed blade bar for cutting hedges.

### C2.2.3 Grass, brush & scrub cutters
- C2.2.3.01 Sickle: one-handed curved blade for cutting grass and crops.
- C2.2.3.02 Scythe: long-shafted two-handed tool with a long curved blade swung to mow grass.
- C2.2.3.03 Brush cutter: powered shaft machine with a metal blade or line head for clearing brush, scrub and long grass.
- C2.2.3.04 Billhook: hooked chopping blade on a short handle for cutting brush, hedge laying and coppice work.
- C2.2.3.05 Machete: long heavy-bladed knife swung to cut vegetation.
- C2.2.3.06 Garden multi-tool (split-shaft powerhead): powered handle and motor unit that takes interchangeable cutting attachments (grass trimmer, hedge trimmer, pole pruner, brush cutter); provisional until a harvested seller page shows the class (memo section 14, C-10). †

## C2.3 Lawn, turf & ground cover

Leaf axis: the lawn operation (mow, edge, renovate, feed and roll), then the surface laid. Kind axis: machine or product form, in operation order, then size; `drive`, propulsion, cutting width, mulching and collecting are attributes, `lawn_area_suited` an attribute of mower named forms.

### C2.3.1 Mowers
- C2.3.1.01 Cylinder mower: mower that cuts with a rotating reel of blades against a fixed bottom blade.
- C2.3.1.02 Rotary mower: wheeled mower that cuts with a blade spinning horizontally under a deck.
- C2.3.1.03 Hover mower: rotary mower that floats on a cushion of air instead of wheels.
- C2.3.1.04 Robotic mower: self-guided battery mower that mows a set area on its own (a kind under C10(b)).
- C2.3.1.05 Ride-on mower: mower that carries its seated operator while it cuts.
- C2.3.1.06 Lawn tractor: lawn or garden tractor with a mowing deck, without a rear power take-off and a Category 1 or larger three-point hitch (with both it is C7; K-99). †

### C2.3.2 Edging and trimming
- C2.3.2.01 Lawn trimmer / string trimmer: powered tool that cuts grass at lawn edges and around obstacles with a spinning line or light blade.

### C2.3.3 Renovation
- C2.3.3.01 Scarifier: machine or tool that rakes thatch and moss out of a lawn with blades or tines.

### C2.3.4 Lawn feeding & rolling
- C2.3.4.01 Broadcast spreader: wheeled or hand-held hopper that spreads seed or granular feed over a lawn.
- C2.3.4.02 Lawn roller: weighted drum pushed or pulled to firm and level a lawn.
- C2.3.4.03 Lawn aerator: tool or machine that spikes or cores a lawn to let air and water into the soil.

### C2.3.5 Ground cover
- C2.3.5.01 Artificial turf: synthetic grass surface sold in rolls or tiles to lay as a lawn. †
- C2.3.5.02 Garden stone: stone, gravel included, and bark sold as decorative ground cover (K-174, K-187).

## C2.4 Clearing, cleaning, hauling & snow

No leaf (about 12 kinds or fewer, leaf = null); kind ids carry no leaf part. Reading groups (display only): raking and blowing (01, 02), shredding (03, 04), washing (05), hauling (06), snow and ice clearing (07, 08). Kind axis: tool or machine form, by working scale; `drive` and the battery system are attributes.
- C2.4.01 Leaf rake: wide fan-shaped rake with springy tines for gathering leaves and debris.
- C2.4.02 Leaf blower: powered machine that blows leaves and debris into heaps; a blower-vac that also sucks and shreds is this kind with the vacuum function an attribute.
- C2.4.03 Garden shredder: machine that shreds garden prunings and green waste into small pieces.
- C2.4.04 Wood chipper: chipper for branches and brush that is not tractor-driven, towed or self-propelled, for tree surgery and grounds (C7-O1). †
- C2.4.05 Pressure washer: powered pump that sprays water at high pressure to clean paths, drives, patios and vehicles.
- C2.4.06 Wheelbarrow: wheeled container with handles for carrying soil, waste and materials in a garden; a garden cart is this kind.
- C2.4.07 Snow shovel / pusher: wide-bladed hand shovel or pusher for clearing snow.
- C2.4.08 Snow blower: powered machine that gathers snow and throws it clear of a path or drive. †

## C2.5 Watering & irrigation

Leaf axis: the role in the water path (carry, spray, control, hand-water, pump, hold), from source to plant. Kind axis: component or device type; sprinkler head type and the system line are attributes or lines, the system platform a C13 row.

### C2.5.1 Hoses and reels
- C2.5.1.01 Garden hose: flexible hose for carrying water in a garden.
- C2.5.1.02 Hose reel: reel or cart on which a garden hose is wound and stored.

### C2.5.2 Sprinklers
- C2.5.2.01 Lawn sprinkler: device that sprays water over an area of lawn or bed; pop-up, oscillating and rotary heads are attributes.

### C2.5.3 Systems and controls
- C2.5.3.01 Drip irrigation kit: set of pipe, drippers and fittings that delivers water drop by drop to plants (balcony and terrace set sizes are variants).
- C2.5.3.02 Soaker hose: porous hose that seeps water along its length into the soil. †
- C2.5.3.03 Irrigation controller: timer or controller that switches the water supply to a garden irrigation system.

### C2.5.4 Hand watering
- C2.5.4.01 Watering can: hand-carried vessel with a spout, often with a rose, for watering plants.

### C2.5.5 Pumping
- C2.5.5.01 Garden water pump: pump made to move water for watering and irrigation in a garden (K-175).
- C2.5.5.02 Pond and fountain pump: pump made to circulate water in a garden pond, fountain or water feature (K-175, K-104, B4-O1). †

### C2.5.6 Water storage and ponds
- C2.5.6.01 Water butt / rain tank: container that collects and stores rainwater for garden use (K-177). †
- C2.5.6.02 Pond liner: flexible waterproof sheet laid to form a garden pond (K-104). †
- C2.5.6.03 Preformed pond: rigid moulded pond shell set into the ground (K-104). †

## C2.6 Pots, containers, supports & covers

Leaf axis: what it does for the plant (hold the roots, support the shoot, cover the plant). Kind axis: container or support form, by size; material, colour, volume and frost-hardiness are attributes, except where the material makes the form. Choice level provisional (no "best pot" list fetched).

### C2.6.1 Pots and planters
- C2.6.1.01 Plant pot: container with drainage in which a plant grows.
- C2.6.1.02 Window box: long narrow planter made to sit on or hang from a window sill or railing.
- C2.6.1.03 Hanging basket: basket or container hung from a bracket or chain to grow plants in.
- C2.6.1.04 Bonsai pot: shallow glazed or unglazed pot with drainage and wire holes, made for growing bonsai.
- C2.6.1.05 Fabric grow pot / grow bag: pot made of breathable fabric that air-prunes roots.
- C2.6.1.06 Plant saucer: shallow dish set under a pot to catch drained water.
- C2.6.1.07 Cachepot (overpot): decorative outer container without drainage that holds a potted plant (K-179).
- C2.6.1.08 Self-watering planter: planter with a built-in reservoir that feeds water to the roots. †

### C2.6.2 Beds
- C2.6.2.01 Raised bed: framed bed standing above ground level, filled with soil to grow plants in.

### C2.6.3 Plant supports & covers
- C2.6.3.01 Plant stake (cane): rod or cane pushed into the soil to hold up a plant.
- C2.6.3.02 Plant tie: tie, twine or clip that fastens a plant to its support.
- C2.6.3.03 Plant label: tag or marker that names a plant in a pot or bed.
- C2.6.3.04 Plant netting: netting made to support climbing plants or protect crops from birds and pests (K-187).
- C2.6.3.05 Horticultural fleece: light non-woven fabric laid over plants to protect them from frost and pests. †
- C2.6.3.06 Cloche: small transparent cover placed over plants to shelter and warm them. †
- C2.6.3.07 Trellis: open lattice panel on which climbing plants are trained (B4-O1). †
- C2.6.3.08 Garden arch: arched frame over a path on which climbing plants are grown (B4-O1). †
- C2.6.3.09 Obelisk: free-standing tapering frame on which climbing plants are grown (B4-O1). †

## C2.7 Soil, feed & plant protection

Leaf axis: the product function (growing medium, feed, plant protection, applicator or test, composting), in function order. Kind axis: product function; formulation, nutrient ratio and organic or peat-free status are attributes, brand product lines are lines rows (CV-46). Choice level provisional (no "best fertiliser" list fetched).

### C2.7.1 Growing media
- C2.7.1.01 Potting compost: prepared growing medium for pots and containers.
- C2.7.1.02 Mulch: material spread on the soil surface to hold moisture and suppress weeds, bark mulch included (K-174).
- C2.7.1.03 Topsoil: screened upper soil sold for beds, lawns and filling. †
- C2.7.1.04 Soil improver: material dug into soil to improve its structure or fertility (K-174). †

### C2.7.2 Feeds
- C2.7.2.01 Fertiliser: product that supplies plant nutrients, granular, liquid or slow-release.

### C2.7.3 Plant protection
- C2.7.3.01 Herbicide: weed killer made to kill or control unwanted plants (K-178).
- C2.7.3.02 Insecticide (pest killer): product that kills or repels insects and other pests on plants (K-178).
- C2.7.3.03 Fungicide: product that prevents or treats fungal disease on plants. †

### C2.7.4 Applicators and tests
- C2.7.4.01 Garden sprayer (pump sprayer): hand-pumped or powered sprayer for applying liquid feeds and plant-protection products.
- C2.7.4.02 Soil test kit: kit for testing garden soil for pH or nutrients. †

### C2.7.5 Composting
- C2.7.5.01 Compost bin: container in which garden and kitchen waste is composted.

## C2.8 Protected & indoor growing

No leaf (about 12 kinds or fewer, leaf = null); kind ids carry no leaf part. Reading groups (display only): structures (01 to 03), light and climate (04, 05), propagation and hydroponics (06, 07). Kind axis: structure or device type, by size; frame, glazing, lean-to or freestanding, and lamp technology are attributes. The cloche is in C2.6 (C2.6.3.06).
- C2.8.01 Greenhouse: glazed framed structure in which plants are grown under shelter.
- C2.8.02 Polytunnel: hoop-framed tunnel covered in polythene film for growing plants under cover. †
- C2.8.03 Cold frame: low glazed box that shelters plants and seedlings outdoors.
- C2.8.04 Grow light: lamp made to give light for plant growth; LED, HPS, CMH and fluorescent are the attribute lamp technology (C-14).
- C2.8.05 Grow tent: lightproof reflective fabric tent on a frame for growing plants indoors under lights. †
- C2.8.06 Propagator: covered tray, heated or not, for raising seeds and cuttings. †
- C2.8.07 Hydroponic system: system that grows plants without soil, roots fed by a nutrient solution. †

## C2.9 Pools & pool equipment

Leaf axis: the function in the pool (the pool, water handling, heating, cleaning and covers, water treatment). Kind axis: pool form or equipment mechanism, by pool size or flow; pump speed class, filter area and cord length are attributes. All equipment and chemicals made for a swimming pool are here, in-ground pool or not (K-176).

### C2.9.1 Pools
- C2.9.1.01 Above-ground pool: framed swimming pool that stands on the ground.
- C2.9.1.02 Soft-sided pool: swimming pool with flexible walls, held by an inflatable ring or by the water (the alias "inflatable pool" is † until attested).

### C2.9.2 Water handling
- C2.9.2.01 Pool pump: pump that circulates pool water through the filter.
- C2.9.2.02 Sand filter: pool filter that traps dirt in a bed of sand or glass media.
- C2.9.2.03 Cartridge filter: pool filter that traps dirt in a pleated cartridge.
- C2.9.2.04 DE filter: pool filter that traps dirt on grids coated with diatomaceous earth.
- C2.9.2.05 Salt chlorinator (salt cell): device that makes chlorine from salt dissolved in the pool water by electrolysis.

### C2.9.3 Heating
- C2.9.3.01 Pool heater: gas, electric or solar heater that warms pool water.
- C2.9.3.02 Pool heat pump: heat pump that warms pool water with heat drawn from the air (K-176).

### C2.9.4 Cleaning and covers
- C2.9.4.01 Robotic pool cleaner: self-powered cleaner with its own motor that scrubs and vacuums the pool.
- C2.9.4.02 Suction-side pool cleaner: cleaner driven by the suction of the pool pump.
- C2.9.4.03 Pressure-side pool cleaner: cleaner driven by water pressure from the pool's return line or a booster pump.
- C2.9.4.04 Pool cover: cover laid over a pool to keep out debris, hold heat or make it safe.
- C2.9.4.05 Pool test kit: kit for testing pool water for chlorine, pH and other values (K-176). †

### C2.9.5 Water treatment
- C2.9.5.01 Pool sanitiser: chemical that disinfects pool water, chlorine tablets and granules included (K-176). †

## C2.10 Parts, accessories & consumables made for one machine

No leaf (closing parts sub-family, leaf = null; exempt from the level-1 axis, C5(d), CV-17). Axis, held as the attribute fits: the machine served (S3). The memo enters no kind yet and names three candidates, all †; nothing that is not made for one kind of machine may sit here (hoses, fittings and fuels do not).
- C2.10.01 Mower blade: replacement cutting blade made for a mower (S3). †
- C2.10.02 Trimmer line: replacement cutting line made for a string trimmer or brush cutter head (S3). †
- C2.10.03 Pool-filter cartridge element: replacement pleated element made for a pool cartridge filter (S3). †

## Precedence inside C2

- A cutter made to trim grass at a lawn edge (string trimmer, lawn edger) is C2.3.2.01; a cutter made to clear brush, scrub or long grass is a brush cutter (C2.2.3.03), also when supplied with a line head (edge object 1).
- Power source is never a kind: battery secateurs are secateurs (C2.2.1.01, `drive = cordless`), a cordless hedge trimmer is C2.2.2.02 and a petrol, mains or manual cylinder mower is C2.3.1.01; a powered tool of a different form from the hand tool is its own kind (hedge trimmer against hedge shears). Bypass, anvil and ratchet secateurs are one kind with `cutting_action` an attribute; a blower-vac is a leaf blower (C2.4.02).
- A powered handle and motor unit that takes interchangeable cutting attachments is the garden multi-tool (C2.2.3.06), filed by its primary action (C-10). An attachment sold alone goes to C2.10 (made for one machine); the shaft systems (Stihl KombiSystem, Ryobi Expand-It) are C13 platform rows; a Gardena combisystem manual handle stays a hand tool, with its heads in C2.1 and C2.2 (memo section 14).
- Hand-held chainsaws and pole saws are C2.2.1.05 and C2.2.1.06; axes (felling axes included), mauls, wedges and log splitters are C1; tractor-driven splitters and chippers are C7; a wood chipper that is not tractor-driven, towed or self-propelled is C2.4.04, and a garden shredder C2.4.03 (K-173, C7-O1). Billhook (C2.2.3.04), machete (C2.2.3.05) and sickle (C2.2.3.01) are C2 as cutters of vegetation (applied by default).
- A ride-on mower is C2.3.1.05; a lawn or garden tractor without a rear power take-off and a Category 1 or larger three-point hitch is C2.3.1.06, one with both is C7, whoever buys it; two-wheel tractors follow the same test (K-99). A self-propelled machine made to dig, lift, load or move material is C1 unless it keeps gardens and grounds (C2) or does a farm or forestry job (C7) (K-194).
- Stone, gravel of any kind and bark sold as decorative ground cover are C2.3.5.02; mulch and bark mulch sold for the soil are C2.7.1.02; growing media and soil improvers are C2.7.1 (K-174, K-187); aggregate, paving, lawn edging, weed membrane and fencing are C8. Artificial turf is C2.3.5.01; cultivated turf (sod) and live moss are C3.
- A pump made to move water for watering or irrigation is C2.5.5.01, and one made for a pond, fountain or water feature C2.5.5.02; a pool pump is C2.9.2.01 (K-175, K-176); drainage, transfer, sump and general-purpose pumps are C1 and field irrigation pumps C7. A water butt or rain tank is C2.5.6.01 (K-177). Garden fish ponds are C2: pond liner C2.5.6.02, preformed pond C2.5.6.03; other pond equipment made for a garden pond (filter, aerator) follows the pond into C2.5.6 (S3); the fountain itself is B4.
- Irrigation for gardens, glasshouses, allotments and grounds is C2.5; irrigation made for field crops is C7 (K-100). Irrigation-system parts are kept in C2.5 by the designed-function test, against the plumbing fittings and valves that K-186 gives to C8 (memo reading until the harvest shows what sellers do).
- A pot, planter or window box made to hold a growing plant is C2.6.1; a cachepot or overpot is C2.6.1.07 (K-179); a plant stand, shelf or bench that holds pots is B1 and a vase for cut flowers B4. An arch, obelisk or trellis made for climbing plants is C2.6.3.08, C2.6.3.09 or C2.6.3.07 (B4-O1). A cloche is C2.6.3.06, not C2.8. Netting made to protect plants or crops is C2.6.3.04; bird netting for buildings is B8 and fence netting C8 (K-187, K-195).
- A product made to protect plants or kill weeds is C2.7.3 (K-178); poisons and repellents made to keep pests out of a home, and mouse, rat and insect traps, are B8 (R-6). A product made only to clean a surface (patio cleaner, decking algae remover) is B6.
- A living plant, seed or bulb is C3 even when sold in a pot, basket or kit with compost; the empty container, the compost and the feed are C2 (K-73). A set of objects of one kind is that kind; a mixed set with no living plant (a grow tent sold with light and fan) is filed by its item of greatest value, with a unit-of-sale attribute (K-1).
- A grow light is C2.8.04 whatever its lamp technology (C-14); a lamp made to light a garden path is B3.
- An above-ground pool (C2.9.1.01) or a soft-sided or inflatable pool made for swimming (C2.9.1.02) is C2; an in-ground pool is G2; a paddling pool made for play is E1 (cut point EN 71-8, water depth 400 mm, E-13, provisional until attested); a hot tub, inflatable or not, and its equipment are B7 (B-26). A pool filter is filed by its media (C2.9.2.02 to C2.9.2.04) and a pool cleaner by its mechanism (C2.9.4.01 to C2.9.4.03).
- Parts follow the whole (S3): a part, attachment or consumable made for one kind of C2 machine (mower blade, trimmer line, pool-filter cartridge element) is C2.10; fuels and lubricants are C8 whatever machine they serve; a battery pack or charger for a maker's cordless platform is C1 and a loose standard cell C8, while a battery made for one device follows it (K-3, K-4).
- A pool test kit (C2.9.4.05) and a soil test kit (C2.7.4.02) are C2; rain gauges and other weather instruments are C6.
- A children's garden tool set is E1 when it cannot do the real tool's job and C2 otherwise; a real tool in a child's size stays in its C2 kind with size and user as attributes (K-179, C15, CV-32).
