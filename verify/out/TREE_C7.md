# C7 Farm & Forestry Equipment: decided tree

Category: C7 Farm & Forestry Equipment (domain C, Making, Growing & Work). Membership test (key step 12): made for agricultural or forestry production: tractors and anything made to be drawn by, mounted on or driven from a tractor; self-propelled farm and forestry machines; livestock handling, milking, shearing and slaughter equipment for herds and flocks; commercial crop, poultry and dairy equipment. Not here: lawn and garden tractors, ride-on mowers and walk-behind tractors and tillers without a rear power take-off and a Category 1 or larger three-point hitch, and implements made only for them (C2, K-99); hand-held chainsaws, pole saws, brush cutters, tree-surgery chippers and garden shredders, garden and grounds irrigation (C2; K-173, C7-O1, K-100); axes, wedges, mauls and hand or engine log splitters, plain excavators, wheel loaders, skid steers, telehandlers and forklifts, generators, compressors and drainage, transfer and general pumps, tools made to service a farm machine (C1; K-173, K-194, K-175, K-13); carry-only trailers, tippers and livestock trailers, Unimog trucks, ATVs, quads and utility vehicles (G1; K-93, K-94); fencing and electric-fence energisers (C8, K-195); silos, grain bins and parlour buildings a person can enter (G2); animal housing furniture, fixed feeders, drinkers, tack, ear tags, microchips, pet microchip scanners, small incubators, veterinary goods and animal feed (B10, K-101); handheld GPS units (D2); model tractors (E1). Structure (Candidate A, memo section 10): sub-family (the job the machine does in the farm and forest cycle; C7.1 holds the machines whose job is to power and carry implements, and the closing parts sub-family C7.10 is exempt from the job axis, C5(d), CV-17), then leaf (stated per sub-family: running gear for tractors, operation on the ground for tillage, stage of the herd, flock or dairy chain for livestock, the machine served for parts; C7.3 to C7.7 and C7.9 store `leaf = null`, C5(b), so their kind ids carry no leaf part), then kind (the machine type buyers compare; for wheeled tractors the design for a task, C-6; for livestock equipment the herd-scale function and installation form), with maker-bound named forms (models and model lines) below the kind. Each object gets one kind. Size and power are attributes, never kinds (`hitch_category`, `engine_hp`, `pto_hp`, operating weight, lift capacity); `carrier` (mounted, trailed, self-propelled) is an attribute, and a self-propelled machine is its own kind only where no mounted or trailed machine does the same job (C12); working width, reversible against fixed, `threshing_type`, `boom_type`, `rows`, `units_per_stalls` and `stall_layout` are attributes. Attribute decided at the build (memo section 14, DPH): `size_class`, the maker's size label on tractor named forms (sub-compact, compact, utility, agricultural), shown in a generated size-class view that cross-links C2 lawn tractors and ride-on mowers for display only, each keeping its C2 home (K-99). Section 14 adds no kind: Landwirt "Spezial- und Kleintraktoren" are the standard four-wheel tractor (C7.1.1.01) or the narrow orchard and vineyard tractor (C7.1.1.03) with a size label, and "Mäh- und Bergtraks" are the slope tractor (C7.1.1.05); the chainsaw evidence goes to C2. Hitch categories (AD730, Limited Category I, iMatch) and PTO rows are C13 compatibility-ledger rows; EU 167/2013 classes go to the jurisdiction ledger (C17); crop, market, era, region, precision farming, forestry system and size class are generated views or tags, never levels. Maker role: owner (maker_roles.tsv, provisional: machinery models carry the maker; shoppers pick the machine type and power first, then maker and model). Display groups (navigation proposal, display only; C7 is not built, so no group ids are issued; the tree keeps the memo's sub-families): Tractors and carriers (C7.1); Soil tillage (C7.2); Seeding and planting (C7.3); Spreading, spraying and irrigation (C7.4); Harvesting (C7.5); Hay and forage (C7.6); Grain and post-harvest (C7.7); Livestock and dairy (C7.8); Forestry machines (C7.9); Loaders, tyres and tractor fittings (C7.10); side views: a maker tab for tractors and forestry machines, and views for size class, crop, vintage and precision farming. Quality markers (display): fit to the job (measured PTO and drawbar power against need, hitch category and implement compatibility), lift and hydraulic capacity, fuel efficiency, dealer proximity, service and parts, reliability and repair frequency, operator comfort and noise (cab, sound level), transmission and drive, stability and tyres; implements by required tractor power and working width; forestry machines by cutting performance, handling and maintenance access (provisional). A kind marked † rests on the key, a group heading or a search excerpt only and needs a fetched attestation at the harvest (memo section 10).

Ids (R-58): C7.n is a sub-family and C7.n.m a leaf; a kind is C7.n.m.kk, or C7.n.kk where a sub-family has no leaf.

## C7.1 Tractors & carriers
Leaf axis: running gear. Kind axis: design for a task, canonical form first, then by increasing specialisation; size and power are attributes (C-6). Display group: Tractors and carriers.

### C7.1.1 Wheeled tractors
- C7.1.1.01 Standard four-wheel tractor: general-purpose wheeled tractor with a rear power take-off and a Category 1 or larger three-point hitch, made to draw, carry and drive implements; the maker's size label (sub-compact, compact, utility) is `size_class` on the named form.
- C7.1.1.02 Row-crop tractor: wheeled tractor built with adjustable track and clearance to work between crop rows.
- C7.1.1.03 Narrow orchard and vineyard tractor [tracteur fruitier, tracteur vigneron, Schmalspurtraktor]: wheeled tractor with a narrow track and low profile, made to work between rows of vines and fruit trees.
- C7.1.1.04 High-clearance (straddle) tractor [enjambeur]: tractor with high ground clearance that straddles rows of vines or crops.
- C7.1.1.05 Slope (mower-carrier) tractor [Mähtrak, Bergtrak]: low, wide tractor with a low centre of gravity, made to carry mowers and implements on steep ground.
- C7.1.1.06 Forestry tractor [tracteur forestier, Forsttraktor]: wheeled tractor built and guarded for forest work such as winching and skidding; filed here by C14(b) and shown in Forestry by a view.

### C7.1.2 Articulated 4WD
- C7.1.2.01 Articulated four-wheel-drive tractor: large tractor with four equal driven wheels that steers by bending at a central pivot.

### C7.1.3 Tracked
- C7.1.3.01 Crawler (full-track) tractor: tractor running on two full-length tracks instead of wheels.
- C7.1.3.02 Half-track tractor (delta tractor): tractor with front tyres and rear crawler tracks.

### C7.1.4 Two-wheel
- C7.1.4.01 Two-wheel (walk-behind) tractor (power tiller): single-axle tractor steered from behind by handles, in C7 only with a rear power take-off and a Category 1 or larger three-point hitch; any other walk-behind tractor or tiller is C2 (K-99).

### C7.1.5 Carrier
- C7.1.5.01 Implement carrier (tool-carrier tractor, no load body): self-propelled carrier made to carry and drive implements, with no load body; a Unimog with a load bed is G1 (K-93).

## C7.2 Soil tillage
Leaf axis: operation on the ground. Kind axis: implement type, most generic first; working width, mounted or trailed and reversible or fixed are attributes. Display group: Soil tillage.

### C7.2.1 Tillage and seedbed
- C7.2.1.01 Mouldboard plough: plough whose curved mouldboards cut and turn the soil over.
- C7.2.1.02 Chisel and tine cultivator: implement with rigid or sprung tines that loosen the soil without turning it.
- C7.2.1.03 Disc harrow: implement with gangs of concave discs that cut and mix the surface soil.
- C7.2.1.04 Power harrow: PTO-driven harrow whose rotating vertical tines break clods into a seedbed.
- C7.2.1.05 Rotary tiller (rotavator): PTO-driven implement whose blades on a horizontal rotor churn the soil.
- C7.2.1.06 Subsoiler and deep ripper: implement with heavy legs that break compacted layers below plough depth.
- C7.2.1.07 Land roller and packer: roller or packer that firms and levels the soil surface.
- C7.2.1.08 Spading machine: PTO-driven implement whose spades dig and turn the soil.
- C7.2.1.09 Puddling harrow (rice paddy): implement that churns flooded paddy soil into a puddle before transplanting. †
- C7.2.1.10 Seedbed combination: implement that combines tines, levelling bars and rollers to make a seedbed in one pass.

### C7.2.2 Ground shaping and clearing
- C7.2.2.01 Box blade: tractor-mounted open box with a blade and scarifier teeth, for grading and moving soil. †
- C7.2.2.02 Rear grader blade and land leveller: rear-mounted blade or levelling frame for grading, levelling and ditching. †
- C7.2.2.03 Post-hole auger: tractor-driven auger that bores holes for posts and planting. †
- C7.2.2.04 Trencher: tractor-driven implement that cuts narrow trenches. †
- C7.2.2.05 Bund plasterer (rice paddy): implement that forms and smooths the earth bunds round paddy fields. †
- C7.2.2.06 Tractor snow blade and snow blower: snow blade or blower made to be mounted on or driven from a tractor; C7 whoever buys it (K-99).

## C7.3 Seeding and planting (no leaf)
Kind axis: machine type. Display group: Seeding and planting.
- C7.3.01 Seed drill: implement that sows seed in rows at a set rate and depth; tine, disc and no-till coulters are attributes.
- C7.3.02 Precision single-seed planter: planter that places single seeds at a set spacing in the row.
- C7.3.03 Potato planter: implement that plants seed potatoes in ridges.
- C7.3.04 Transplanter: implement that sets seedlings or young plants into the field.
- C7.3.05 Rice transplanter: machine that plants rice seedlings into a flooded paddy; `rows` (4 to 8) is an attribute.

## C7.4 Crop care (no leaf)
Kind axis: machine type; `carrier` is an attribute. Display group: Spreading, spraying and irrigation.
- C7.4.01 Fertiliser spreader: implement that broadcasts or places granular fertiliser.
- C7.4.02 Manure spreader: wagon that shreds and spreads solid manure.
- C7.4.03 Slurry tanker: tank that carries and spreads liquid slurry.
- C7.4.04 Slurry injector: implement that places slurry into the soil.
- C7.4.05 Crop sprayer: sprayer that applies crop-protection liquids through a boom; `carrier` (mounted, trailed, self-propelled) is an attribute.
- C7.4.06 Inter-row hoe and tine weeder: implement that weeds mechanically between and within crop rows.
- C7.4.07 Irrigation reel and sprinkler set: hose reel and field sprinkler line made for field-crop irrigation (K-100).
- C7.4.08 Centre-pivot and linear-move irrigation machine: self-moving span of sprinkler pipe that irrigates a field in a circle or a strip (K-100). †
- C7.4.09 Field irrigation pump: pump made to move water for field irrigation (K-175). †

## C7.5 Harvesting (no leaf)
Kind axis: machine type; a header or head that does a job of its own is its own kind. Display group: Harvesting.
- C7.5.01 Combine harvester [moissonneuse-batteuse, Mähdrescher, colheitadeira]: self-propelled machine that reaps, threshes and cleans grain; `threshing_type` (head-feeding, conventional, axial rotor) is an attribute.
- C7.5.02 Combine header [plataforma colheitadeira]: interchangeable front cutting or pick-up unit for a combine harvester.
- C7.5.03 Forage harvester [ensileuse]: machine that cuts and chops forage crops for silage; `carrier` (self-propelled, trailed) is an attribute.
- C7.5.04 Potato harvester: machine that lifts potatoes and separates them from soil and haulm.
- C7.5.05 Sugar-beet harvester: machine that tops, lifts and cleans sugar or fodder beet.
- C7.5.06 Grape harvester: machine that straddles vine rows and shakes off the grapes.
- C7.5.07 Carrot harvester: machine that lifts carrots by their tops.

## C7.6 Hay and forage (no leaf)
Kind axis: machine type. Display group: Hay and forage.
- C7.6.01 Disc and drum mower: mower whose rotating discs or drums cut grass for hay or silage.
- C7.6.02 Hay tedder: implement with rotating tines that spreads and turns cut grass to dry.
- C7.6.03 Hay rake and windrower: implement that gathers cut grass into windrows.
- C7.6.04 Baler: machine that picks up hay, straw or silage and presses it into round or square bales.
- C7.6.05 Bale wrapper: machine that wraps bales in stretch film for silage.
- C7.6.06 Rotary cutter and flail mower (mulcher): implement that cuts and shreds standing vegetation on grassland, verges, vineyards and scrub; C7 whoever buys it (K-99).
- C7.6.07 Loader and forage wagon: wagon that picks up, cuts and carries grass or silage.

## C7.7 Post-harvest handling (no leaf)
Kind axis: machine type. Display group: Grain and post-harvest.
- C7.7.01 Grain dryer: installation that dries harvested grain.
- C7.7.02 Grain cleaner: machine that separates grain from chaff, weed seed and dirt.
- C7.7.03 Grain conveyor: auger, belt or elevator that moves grain.
- C7.7.04 Rice huller: machine that removes the husk from paddy rice.

## C7.8 Livestock and dairy
Leaf axis: stage of the herd, flock or dairy chain. Kind axis: herd-scale function and installation form. Display group: Livestock and dairy.

### C7.8.1 Milking installations
- C7.8.1.01 Bucket milking machine: portable milking unit that milks into a bucket.
- C7.8.1.02 Pipeline milking installation: milking system that carries the milk from the stalls through a pipeline to the dairy.
- C7.8.1.03 Static milking parlour: fixed parlour in which cows stand in stalls to be milked; `units_per_stalls` (one per two stalls, one per stall) and `stall_layout` (abreast, herringbone; provisional) are attributes.
- C7.8.1.04 Rotary milking parlour: parlour whose stalls ride on a rotating platform.
- C7.8.1.05 Trigon milking parlour: parlour with stalls on three sides of the milker's pit.
- C7.8.1.06 Polygon milking parlour: parlour with stalls on four sides of the milker's pit.
- C7.8.1.07 Milking robot: automatic milking system that attaches the cups and milks without a milker.

### C7.8.2 Milk cooling and metering
- C7.8.2.01 Bulk milk cooling tank: refrigerated tank that cools and holds the milk on the farm.
- C7.8.2.02 Milk meter: meter that measures each cow's milk yield.

### C7.8.3 Handling
- C7.8.3.01 Cattle crush and headgate: crate or gate that restrains one animal for treatment.
- C7.8.3.02 Sheep handler and drafter: race unit that holds, turns or sorts sheep into pens.

### C7.8.4 Weighing
- C7.8.4.01 Livestock weigh-scale indicator: electronic indicator that reads, shows and records livestock weights from load bars or a platform.
- C7.8.4.02 Livestock weigh platform and load bars: platform or pair of load bars on which animals are weighed.

### C7.8.5 Identification and recording
- C7.8.5.01 Livestock EID stick reader: handheld reader for livestock electronic ear tags, sold for herd recording; pet microchip scanners are B10 (K-101). †

### C7.8.6 Shearing
- C7.8.6.01 Shearing machine: powered machine with its motor and drive that runs a shearing handpiece, for flock-scale shearing. †

### C7.8.7 Slaughter and stunning
- C7.8.7.01 Captive-bolt stunner: tool that stuns livestock by driving a bolt into the skull. †
- C7.8.7.02 Scalder: tank or machine that scalds slaughtered pigs or poultry to loosen hair or feathers. †

### C7.8.8 Poultry
- C7.8.8.01 Poultry feeding line: automatic feed line for a commercial poultry house. †
- C7.8.8.02 Egg collection system: belt or conveyor system that collects eggs in a commercial laying house. †
- C7.8.8.03 Commercial hatching incubator: commercial hatcher for eggs at flock scale; small incubators are B10 (K-101). †

### C7.8.9 Feeding
- C7.8.9.01 Feed mixer wagon: wagon that mixes and dispenses a feed ration.
- C7.8.9.02 Silage block cutter: tractor implement that cuts and carries blocks from a silage clamp.
- C7.8.9.03 Bedding spreader: machine that spreads straw or other bedding in housing.

## C7.9 Forestry (no leaf)
Kind axis: machine type; `boom_type` and the forestry system (cut-to-length against whole-tree) are an attribute and a view. Forestry holds 14 kinds with `leaf = null` (CV-16, A-21). Display group: Forestry machines.
- C7.9.01 Forest harvester: self-propelled machine that fells, delimbs and cuts trees to length.
- C7.9.02 Forwarder: self-propelled machine that carries cut logs clear of the ground on its own load bed.
- C7.9.03 Skidder: machine that drags felled trees or logs to the roadside.
- C7.9.04 Feller buncher: machine that fells trees and gathers them into bunches; `boom_type` (drive-to-tree, swing-boom) is an attribute.
- C7.9.05 Harvester head: felling, delimbing and cross-cutting head made for a forest harvester or excavator base.
- C7.9.06 Wood chipper: chipper that is tractor-driven (PTO or mounted) or part of a forest machine; a towed or self-propelled tree-surgery chipper is C2 (C7-O1).
- C7.9.07 Forestry mulcher: heavy mulcher that shreds trees, brush and stumps on forest and clearing land.
- C7.9.08 Stump grinder: machine that grinds tree stumps below ground level.
- C7.9.09 Forestry winch: tractor-mounted winch for pulling felled trees and logs.
- C7.9.10 Harwarder: combined forest machine that both harvests trees and forwards the logs.
- C7.9.11 Delimber: machine that strips the limbs from felled trees.
- C7.9.12 Forestry knuckleboom loader: loader with a jointed boom and grapple for lifting and loading logs.
- C7.9.13 Forestry excavator: excavator-based machine built for a forestry job (K-194).
- C7.9.14 Log splitter, tractor-driven (PTO or mounted): log splitter driven from or mounted on a tractor; hand and engine log splitters are C1 (K-173).

## C7.10 Parts and accessories made for one machine
Leaf axis: the machine served (exempt from the job axis, C5(d), CV-17). A fitting with no job of its own away from its host machine is here; an attachment that does a job of its own keeps its job sub-family. Display group: Loaders, tyres and tractor fittings.

### C7.10.1 Tractor fittings
- C7.10.1.01 Front-end loader: loader arms and frame made to be fitted to a tractor.
- C7.10.1.02 Loader attachment (pallet forks, bucket, bale spike): tool made to be fitted to a tractor's front loader. †
- C7.10.1.03 Wheel weight: ballast weight fitted to a tractor wheel.
- C7.10.1.04 Tractor tyre: tyre made for a tractor.
- C7.10.1.05 Tractor rim and complete wheel: rim or tyred wheel made for a tractor.
- C7.10.1.06 Rubber track unit: rubber track system fitted to a tractor in place of wheels.
- C7.10.1.07 Guidance and auto-steer system: guidance receiver, display or auto-steer kit made for a tractor or farm machine.

### C7.10.2 Shearing machine parts
- C7.10.2.01 Shearing handpiece: handpiece that holds and drives the comb and cutter, made for a shearing machine. †
- C7.10.2.02 Shearing comb and cutter: comb and cutter blades made for a shearing handpiece. †

## Precedence inside C7

- Job first: a machine is filed by the job it does in the farm and forest cycle (tillage C7.2, seeding and planting C7.3, crop care C7.4, harvesting C7.5, hay and forage C7.6, post-harvest C7.7, livestock and dairy C7.8, forestry C7.9); a machine whose job is to power and carry implements is C7.1, and a fitting made for one machine is C7.10. The display groups are display only and move no id.
- Tractor kinds are designs for a task (C7.1.1.01 to C7.1.5.01); size, power and hitch category are attributes, never kinds, and a model keeps its maker's size label as `size_class` (C-6, section 14). Small special tractors are C7.1.1.01 or C7.1.1.03 with a size label; Mäh- und Bergtraks are C7.1.1.05.
- A tractor with a rear power take-off and a Category 1 (or Limited Category 1) or larger three-point hitch is C7 whatever its size or buyer; a lawn or garden tractor, ride-on or zero-turn mower without them is C2. A two-wheel tractor is C7.1.4.01 only with that PTO and hitch; any other walk-behind tractor or tiller is C2 (K-99, P1).
- An implement made to be drawn by, mounted on or driven from a tractor is C7 whoever buys it, including a rotary cutter (C7.6.06), box blade (C7.2.2.01), snow blade (C7.2.2.06), post-hole auger (C7.2.2.03) or front loader (C7.10.1.01) bought for a small plot; one made only for a lawn or garden tractor that fails the P1 test follows that tractor into C2 (K-99, P2).
- Carrier is an attribute: mounted, trailed and self-propelled versions of one job are one kind (crop sprayer C7.4.05, forage harvester C7.5.03); a self-propelled machine is its own kind only where no mounted or trailed machine does the same job (combine harvester C7.5.01, forest harvester C7.9.01, forwarder C7.9.02, skidder C7.9.03, feller buncher C7.9.04) (C12).
- A kind used in several places goes to the one family that holds all its uses (C14(b)): the rotary cutter and flail mower is C7.6.06 whether used on grassland, vineyard, verge or municipal land, and the forestry tractor is C7.1.1.06, shown in Forestry by a view; the forestry mulcher (C7.9.07) and stump grinder (C7.9.08) are separate forestry kinds ("mulcher" is a homonym of both C7.6.06 and C7.9.07).
- A fitting with no job of its own away from its host machine (front loader C7.10.1.01, loader attachment C7.10.1.02, wheel weight C7.10.1.03, tyre C7.10.1.04, rim and wheel C7.10.1.05, rubber tracks C7.10.1.06, guidance kit C7.10.1.07, shearing handpiece C7.10.2.01, comb and cutter C7.10.2.02) is C7.10; an attachment that does a job of its own keeps its job sub-family (combine header C7.5.02, harvester head C7.9.05, a plough C7.2.1.01) (S3, K7).
- A wagon or tank that loads, mixes, spreads or processes what it carries is C7 (loader and forage wagon C7.6.07, feed mixer wagon C7.8.9.01, slurry tanker C7.4.03, manure spreader C7.4.02, bale wrapper C7.6.05); a trailer, tipper or wagon made only to carry goods or animals is G1 (K-94, P5). A slurry tanker is filed under spreading (C7.4.03), not transport.
- A vehicle made mainly to carry people or goods (Unimog truck, ATV, quad, utility vehicle) is G1 even when it powers implements; an implement carrier without a load body is C7.1.5.01 (K-93, P6).
- A self-propelled machine that does farm or forestry work is C7; a machine built for a forestry job on an excavator or loader base is C7 (forestry excavator C7.9.13, forestry knuckleboom loader C7.9.12, harwarder C7.9.10); a plain excavator, wheel loader, skid steer, telehandler or forklift is C1 even on a farm, and the only loader in C7 is the front loader made for a tractor (C7.10.1.01) (K-194, P7).
- A wood chipper that is tractor-driven or part of a forest machine is C7.9.06; a towed or self-propelled tree-surgery or grounds chipper and a garden shredder are C2. A tractor-driven log splitter is C7.9.14; hand-held chainsaws, pole saws and brush cutters are C2, and axes, wedges, mauls and hand or engine log splitters are C1 (K-173, C7-O1, P3, P4).
- Field irrigation is C7 (irrigation reel and sprinkler set C7.4.07, centre pivot and linear move C7.4.08), and a pump made to move water for field irrigation is C7.4.09; garden, glasshouse and grounds irrigation and garden, pool and pond pumps are C2; drainage, transfer, sump and general pumps, generators and compressors are C1 (K-100, K-175, P8, P13).
- Equipment that restrains, handles, sorts, weighs, milks, cools milk, shears or stuns animals at herd or flock scale is C7.8; housing furniture, fixed feeders, drinkers, tack, identification tags and microchips and veterinary goods are B10 whatever the scale (K-101, P9). A tractor-drawn feed mixer wagon (C7.8.9.01), silage block cutter (C7.8.9.02) or bedding spreader (C7.8.9.03) is C7; a fixed calf-feeding automat or concentrate feeder in a barn is B10 (P10).
- A livestock EID stick reader is C7.8.5.01 (provisional until attested as sold for herd recording); pet microchip scanners, ear tags and implanted microchips are B10. A commercial hatching incubator is C7.8.8.03; small incubators and backyard hens are B10 (K-101).
- Milking installations are kinds by installation form (bucket C7.8.1.01, pipeline C7.8.1.02, static parlour C7.8.1.03, rotary C7.8.1.04, trigon C7.8.1.05, polygon C7.8.1.06, robot C7.8.1.07); stall layout inside a static parlour is an attribute. The stalls and milking units inside a parlour building are C7, the building a person can enter is G2 (P12).
- A fence-monitoring system or livestock weigher sold by a fencing maker follows its own function (weighing C7.8.4); fence panels, posts, wire, gates and electric-fence energisers are C8 (K-195, P11).
- A guidance receiver, display or auto-steer kit made for a tractor or farm machine is C7.10.1.07 (S3); a handheld GPS unit is D2. Precision and autonomous technology on a machine is a tag on its named form.
- Threshing type of a combine (C7.5.01), boom type of a feller buncher (C7.9.04), rows of a rice transplanter (C7.3.05) and units per stalls of a static parlour (C7.8.1.03) are attributes, never kinds.
- Regional types are named by generic form with a region tag (half-track tractor C7.1.3.02, two-wheel tractor C7.1.4.01, puddling harrow C7.2.1.09, bund plasterer C7.2.2.05, rice transplanter C7.3.05); "delta tractor", "power tiller", "rotavator" and the French, German and Portuguese marketplace words are aliases (C11, C9).
- Model tractors are E1 (C15); tools made to service a tractor or farm machine are C1 (K-13).
