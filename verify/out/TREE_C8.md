# C8 Building Materials & Hardware: decided tree

Category: C8 Building Materials & Hardware (domain C, Making, Growing & Work). Membership test (key step 32, branch 2): a material, building product, hardware or supply: timber, bricks, roofing, windows, doors, stairs, flooring, tiles, wallpaper, paint, adhesives, fasteners, hinges and fittings, plumbing and electrical supplies, mains cables, extension leads, plugs, fuses, household batteries and chargers for them, lubricants, fuels and fuel cans, firewood, matches, firelighters, long utility and candle lighters, gas cylinders and flints, packing materials, fencing, acoustic panels, ceiling roses, chimney and flue work, shower trays and enclosures, letter plates and regulatory and safety signs. Building elements are filed by what they are, installed or not; building products are never parts (S3), and fuels are C8 whatever they are used in. Not here: buildings as a whole and land (G2); kitchen and wardrobe cabinetry and worktops, hooks and storage boxes (B1); carpets, blinds and curtains (B2); lamp cord sets (B3); signs and house numbers for decor and flagpoles (B4); cleaning products, silicone and adhesive removers included (B6); baths, showers, basins, toilets, hot tubs, boilers, stoves, hot-water cylinders and power stations (B7); locks, padlocks, safes, locksets with a lock, smoke and carbon-monoxide alarms, letterboxes, anti-climb spikes and bird spikes (B8); pocket lighters and hookah charcoal (B9); tools, ladders, platform battery packs and chargers, welding wire, solder, abrasives cut for one tool and drainage, transfer and general pumps (C1); growing media, decorative gravel and garden stone, artificial turf, plant-protection netting and garden, pool and pond pumps (C2); paint and glue made for pictures, models and crafts (C4); envelopes, mailing tubes, glue sticks and desk tape (C5); livestock handling equipment and field irrigation pumps (C7); USB, HDMI, audio and charging cables and generic USB, GaN or Qi chargers (D1); EV wall-box chargers (G1); pumped or delivered fuel (out). Structure (Candidate A, supply family first, C-7; memo sections 2, 3 and 10): sub-family (the supply family the product belongs to; 11 sub-families, lighters, matches and firelighters being the leaf Firelighting of C8.10), then leaf (the product group, one axis stated per sub-family; C8.11 has no source for a leaf axis and stores `leaf = null`, so its kind ids carry no leaf part), then kind (the generic product type at the level where buyers compare quality or makers, memo section 4b), then named form. Each object gets one kind. Size, length, gauge, material, finish, colour, drive, thread standard, property class, binder, gloss level, chemistry, rechargeability, rating, grade, pack size, trade or DIY, era (antique, reproduction) and region are attributes, modifiers or tags, never kinds; the battery size class is the one stated exception, a kind only where one size cannot replace another without different equipment (CV-19). Plug and socket types (A to O, with their national standards) and coin and button cell designations (CR2032 and the rest) are non-maker named forms held in registers; screw drives, pipe threads and cell-size standards are attribute values with C13 compatibility-ledger rows; a product line spanning several kinds (Duracell Coppertop, Energizer Max, Varta Longlife Extra) is a lines row, and a line inside one kind (Calor Patio Gas) a maker-bound named form; UNSPSC and Uniclass codes are cross-reference columns on each kind (C-19). Attributes decided at the build (memo section 14, DPH): `strength_class` (C16, C24 and further EN 338 classes) and `treatment_class` on sawn timber (structural timber is sawn timber with a grade, no new kind); `tile_material`, `pei_rating`, `slip_rating` and `water_absorption_class` on wall and floor tiles; `gloss_level` on paints (gloss and satinwood are finishes of woodwork paint, not kinds); `coat_role` on primer (primer, undercoat, primer-undercoat, sealer). Facet-derived kind sets (screw applications, paint surfaces, adhesive uses) and plumbing joint systems as kinds are provisional until a fetched page compares or ranks the types (CV-25, C-19); otherwise they fold into a `use` or `surface` attribute on the general kind. Maker role: none, confirmed (maker_roles.tsv, provisional; building materials and hardware are commodities chosen by specification): brand is a filter only, makers appear through branded products, and a product named by a test enters as a named form with its tier entry. Display groups (navigation proposal, display only; the tree keeps the memo's sub-families and leaves): level 1 Timber, boards and building products (C8.1); Floors, tiles and wall finishes (C8.2); Screws, nails and fixings (C8.3); Door, window and building hardware (C8.4); Plumbing and drainage (C8.5); Electrical supplies (C8.6); Paint and wood finishes (C8.7); Adhesives, sealants and fillers (C8.8); Batteries and chargers (C8.9); Fuels, lubricants and firelighting (C8.10); Packing and moving materials (C8.11); level 2 shows the memo leaves. Side views: project views over kinds (tiling, bathroom, decking and fencing, painting a room, barbecue and fireplace fuel) and a battery-cell finder (which cell a device takes); no maker view. Quality markers (display): timber by strength class (C16 below C24), treatment class, kiln drying and regularising, with certified sourcing (FSC, PEFC) an attribute and not a grade; tiles by material (porcelain above ceramic, natural stone apart), water absorption (impervious above vitreous above semi-vitreous above non-vitreous), PEI wear rating 0 to 5 and slip resistance (R9 to R13, DCOF 0.42 or higher for wet areas), and underfloor-heating compatibility; paint by hiding power and scrub resistance (EN 13300 classes), ease of application, low emissions, gloss level, mould resistance and spreading rate; fixings by application-matched design, material and coating (zinc below galvanised below A2 below A4 stainless) and property class (4.6 to 12.9, ISO 898-1); batteries by chemistry, capacity and the maker's line ladder; plumbing, electrical, adhesives, fuels and packing by their spec attributes only (provisional). A kind marked † is named only by the key, a decision, a builder note or a group-level source, and needs a fetched page naming it before it enters the data (memo section 10, "Sourcing still needed"; section 14 for the dowel, packer, pipe clip and cable clip).

Ids (R-58): C8.n is a sub-family and C8.n.m a leaf; a kind is C8.n.m.kk, or C8.n.kk where a sub-family has no leaf.

## C8.1 Structure, envelope & openings

Leaf axis: the building-product group a seller shelves it in (frame and boards; sections; masonry; groundworks; roof, cladding and insulation; chimney and flue; openings; boundary). Kind axis: sheet, section or product type; species, thickness, grade and treatment are attributes.

### C8.1.1 Timber & boards
- C8.1.1.01 sawn timber: timber sawn to section for building and joinery, sold by length (species, `strength_class`, `treatment_class`, kiln-dried and regularised are attributes).
- C8.1.1.02 plywood: board of thin wood veneers glued in cross-grained layers.
- C8.1.1.03 building board: manufactured sheet for building (chipboard, MDF, OSB, plasterboard, cement board), sold loose.
- C8.1.1.04 decking board: profiled timber or composite board sold loose for building a deck (K-66). †

### C8.1.2 Structural sections
- C8.1.2.01 steel section: steel bar, angle, channel, box or tube section sold by length for building and fabrication.
- C8.1.2.02 aluminium section: aluminium bar, angle, channel or tube section sold by length.

### C8.1.3 Masonry & concrete
- C8.1.3.01 cement: powdered binder mixed with water and aggregate to make concrete or mortar (ready-mix bags included).
- C8.1.3.02 concrete block: moulded block of concrete for building walls.
- C8.1.3.03 brick: fired clay or concrete unit laid in mortar to build walls. †

### C8.1.4 Groundworks & landscaping materials
- C8.1.4.01 aggregate: sand, gravel or ballast sold for concrete, mortar or sub-base (K-174).
- C8.1.4.02 paving slab: flat slab of concrete or stone laid as a path, patio or drive surface. †
- C8.1.4.03 sett: small dressed block of stone or concrete laid as paving. †
- C8.1.4.04 lawn edging: strip or border of metal, plastic, timber or stone set along a lawn or bed edge. †
- C8.1.4.05 weed membrane: permeable sheet laid under paving, gravel or mulch to suppress weeds. †

### C8.1.5 Roofing, cladding & insulation
- C8.1.5.01 roofing sheet: corrugated or profiled sheet of metal, bitumen, fibre cement or plastic laid as a roof or cladding.
- C8.1.5.02 insulation: roll, slab or board of thermal or acoustic insulating material for a building (acoustic panels included).

### C8.1.6 Chimney & flue
- C8.1.6.01 flue pipe: pipe that carries smoke and gases from a stove, boiler or fire to the outside. †
- C8.1.6.02 chimney liner: flexible or rigid liner fitted inside a chimney. †
- C8.1.6.03 chimney pot: pot or terminal set on top of a chimney stack. †

### C8.1.7 Openings
- C8.1.7.01 door: door leaf or door set for a building opening, installed or not.
- C8.1.7.02 window: window frame and glazing unit for a building opening, installed or not.

### C8.1.8 Fencing & gates
- C8.1.8.01 fence panel: prefabricated panel of timber, metal or composite fixed between posts.
- C8.1.8.02 gate: hinged or sliding barrier for an opening in a fence or wall.
- C8.1.8.03 fence post: post set in the ground to carry fence panels, rails or wire. †
- C8.1.8.04 fence wire: plain, barbed or high-tensile wire sold for fencing. †
- C8.1.8.05 stock netting: woven or welded wire mesh sold for fencing animals in or out. †
- C8.1.8.06 electric-fence energiser: unit that sends pulses of current along an electric fence (follows the fence under S3). †
- C8.1.8.07 electric-fence tape: conductive tape, rope or polywire strung as an electric fence. †
- C8.1.8.08 electric-fence insulator: insulator that holds an electric-fence wire or tape on a post. †

## C8.2 Interior finishes & floors

Leaf axis: the surface finished (wall, floor, trim). Kind axis: finish product type; tile material, PEI, slip and water-absorption ratings are attributes.

### C8.2.1 Wall
- C8.2.1.01 wallpaper: paper, vinyl or textile wall covering sold in rolls for hanging.
- C8.2.1.02 plaster: powdered plaster or skim coat mixed with water to finish walls and ceilings.
- C8.2.1.03 wall tile: tile made and rated for walls. †

### C8.2.2 Floor
- C8.2.2.01 floor tile: tile made and rated for floors (wear and slip rating on the object). †
- C8.2.2.02 laminate flooring: click-together boards with a printed decorative layer on a fibreboard core. †

### C8.2.3 Trim
- C8.2.3.01 skirting and architrave: moulded board that trims the base of a wall or the frame of a door or window. †

## C8.3 Fixings & fasteners

Leaf axis: fastener type (screw, nail and staple, bolt-nut-washer, rivet, anchor, connector). Kind axis per leaf: screws by application (what they fasten into; provisional until attested, CV-25), anchors by mechanism, the rest by form; diameter, length, drive, head, material, coating and `property_class` (ISO 898-1) are attributes.

### C8.3.1 Screws
- C8.3.1.01 wood screw: tapered, coarse-threaded screw for fixing into timber and boards.
- C8.3.1.02 decking screw: corrosion-resistant screw made to fix decking boards to joists.
- C8.3.1.03 drywall screw: fine- or coarse-threaded bugle-head screw for fixing plasterboard to studs.
- C8.3.1.04 masonry/concrete screw: hardened screw that cuts its own thread into a drilled hole in masonry or concrete.
- C8.3.1.05 self-drilling screw: screw with a drill point that drills and taps sheet metal in one pass.
- C8.3.1.06 machine screw: parallel-threaded screw for a tapped hole or a nut.

### C8.3.2 Nails & staples
- C8.3.2.01 nail: plain steel pin with a head, driven by hammer or nail gun (loose or collated).
- C8.3.2.02 concrete nail: hardened nail made to be driven into concrete or masonry.
- C8.3.2.03 staple: U-shaped wire fastener driven by a stapler or tacker.

### C8.3.3 Bolts, nuts & washers
- C8.3.3.01 bolt: externally threaded fastener with a head, used with a nut (`property_class` an attribute).
- C8.3.3.02 nut: internally threaded fastener that mates with a bolt or stud.
- C8.3.3.03 washer: flat or spring ring set under a nut or head to spread load or lock it.

### C8.3.4 Rivets
- C8.3.4.01 rivet: fastener set by deforming its tail, including blind (pop) rivets.

### C8.3.5 Anchors
- C8.3.5.01 wall plug: plastic or fibre sleeve that expands in a drilled hole to hold a screw.
- C8.3.5.02 cavity fixing: fixing that opens or grips behind a hollow wall or board.
- C8.3.5.03 chemical anchor: resin cartridge or capsule that bonds a stud or bar into a drilled hole (resin sold alone is this kind).
- C8.3.5.04 frame fixing: long plug and screw that fix a frame through to masonry in one pass.
- C8.3.5.05 steel anchor: metal expansion anchor or anchor bolt for heavy fixings in concrete or masonry.

### C8.3.6 Connectors & supports
- C8.3.6.01 timber connector: pressed-steel plate, hanger or bracket that joins timber members.
- C8.3.6.02 post support: metal shoe, spike or base that holds a post in the ground or on a surface.
- C8.3.6.03 dowel (dowel pin): wooden, plastic or metal pin set into holes to join or align two parts. †
- C8.3.6.04 packer (shim): thin plate or wedge set under or behind a frame or fixing to level or space it. †

## C8.4 Door, window & building hardware

Leaf axis: the hardware function (hinge, handle or knob, latch or bolt, bracket, plate or sign). Kind axis: hardware type; finish, material and era are attributes or tags.

### C8.4.1 Hinges
- C8.4.1.01 door hinge: hinge on which a door, gate or window leaf swings (butt and other patterns are named forms).

### C8.4.2 Handles, knobs & pulls
- C8.4.2.01 cabinet knob or pull: knob or pull handle fitted to a cabinet door or drawer (K-196).
- C8.4.2.02 door handle: lever, knob or pull handle set for a door, without a lock (a lockset with a lock is B8). †

### C8.4.3 Latches, bolts & hasps
- C8.4.3.01 latch: catch that holds a door or gate shut without a key. †
- C8.4.3.02 door bolt: sliding bolt that secures a door or gate from one side. †
- C8.4.3.03 hasp: hinged slotted plate and staple that take a padlock. †

### C8.4.4 Brackets & supports
- C8.4.4.01 bracket: general bracket or shelf support fixed to a wall or structure (not one made for one screen or speaker). †

### C8.4.5 Plates & signs
- C8.4.5.01 letter plate: letter flap and plate fitted in a door (K-188). †
- C8.4.5.02 regulatory and safety sign: sign that gives a safety, fire, hazard or legal instruction (K-192). †

## C8.5 Plumbing & drainage supplies

Leaf axis: the part of the plumbing system (joint fittings, pipe, valves and taps, waste and drainage, shower and bath surrounds). Kind axis: joint fittings by joint system with shape an attribute (C-19, provisional until a fetched source compares the joint types); pipe diameter, material and `thread_standard` are attributes.

### C8.5.1 Joint fittings
- C8.5.1.01 compression fitting: fitting that seals on a pipe by a nut squeezing an olive.
- C8.5.1.02 push-fit fitting: fitting that grips and seals a pipe pushed into it, with no tools or heat.
- C8.5.1.03 solder-ring fitting: copper fitting with an integral ring of solder, sealed by heating.
- C8.5.1.04 end-feed fitting: copper fitting sealed by solder fed into the joint while heated.
- C8.5.1.05 press-fit fitting: fitting sealed by crimping onto the pipe with a press tool.

### C8.5.2 Pipe
- C8.5.2.01 pipe: plumbing, heating, gas or water supply pipe of copper, plastic or steel, sold by length or coil.
- C8.5.2.02 pipe clip: clip or bracket that holds a pipe to a wall or joist. †

### C8.5.3 Valves & taps
- C8.5.3.01 tap: hand-operated valve that delivers water at a basin, sink, bath or outside (mixer taps included; K-186).
- C8.5.3.02 valve: valve that shuts off or controls flow in a pipe (stop cock, isolating and radiator valves).

### C8.5.4 Waste & drainage
- C8.5.4.01 waste fitting: pipe and fitting for the waste outlet of a basin, sink or bath.
- C8.5.4.02 trap: water-sealed bend under an outlet that blocks drain gases.
- C8.5.4.03 guttering: gutter and downpipe sections and fittings that carry rainwater from a roof.

### C8.5.5 Shower & bath surrounds
- C8.5.5.01 shower tray: base set under a shower that collects water to its waste (K-186). †
- C8.5.5.02 shower enclosure: glass or panel walls and door around a shower. †
- C8.5.5.03 bath panel: panel that covers the side or end of a bath. †

## C8.6 Electrical supplies

Leaf axis: the electrical function (cable and flex, wiring accessory, distribution and leads). Kind axis: device or cable family; rating, gang count, core count and cross-section are attributes, plug and socket types named forms.

### C8.6.1 Cable & flex
- C8.6.1.01 cable: fixed-wiring mains cable (twin and earth and the like).
- C8.6.1.02 flex: flexible mains cord for connecting appliances and fittings.
- C8.6.1.03 armoured cable: mains cable with a steel-wire armour layer for burial or exposed runs.
- C8.6.1.04 cable clip: clip that fixes a cable to a wall or surface. †

### C8.6.2 Wiring accessories
- C8.6.2.01 switch: wall switch for a mains circuit or light.
- C8.6.2.02 socket-outlet: wall socket that takes mains plugs (types A to O are named forms).
- C8.6.2.03 mains plug: rewireable or moulded plug for a mains flex (types A to O are named forms).
- C8.6.2.04 fuse: cartridge or rewireable fuse that breaks a circuit on overload. †
- C8.6.2.05 ceiling rose: ceiling fitting where a pendant flex joins the fixed wiring (B-18). †

### C8.6.3 Distribution & leads
- C8.6.3.01 extension lead: flex with a mains plug and one or more sockets, on a reel or not.
- C8.6.3.02 consumer unit: fuse box or board that holds a building's breakers or fuses. †

## C8.7 Paints, coatings & wood finishes

Leaf axis: the coating or preparation job (paint, wood finish, surface preparation). Kind axis: paints by surface and use (provisional until attested, CV-25); `binder` (emulsion, solvent, alkyd), EN 13300 classes, `gloss_level`, colour and special properties such as anti-mould are attributes.

### C8.7.1 Paints
- C8.7.1.01 wall and ceiling paint: interior paint for walls and ceilings (emulsion is a binder, not a kind).
- C8.7.1.02 masonry paint: exterior paint for brick, render and masonry.
- C8.7.1.03 fence paint: paint or treatment for timber fences and sheds.
- C8.7.1.04 floor paint: hard-wearing paint for concrete, wood or garage floors.
- C8.7.1.05 radiator paint: heat-resistant paint for radiators and pipes.
- C8.7.1.06 tile paint: paint made to adhere to glazed tiles.
- C8.7.1.07 furniture paint: paint made for furniture and cabinets.
- C8.7.1.08 woodwork and metal paint (trim paint): gloss, satin or eggshell paint for doors, trim and metalwork (gloss and satinwood are `gloss_level` values). †
- C8.7.1.09 spray paint: paint in an aerosol can.
- C8.7.1.10 primer: primer or undercoat, the preparatory coat under a top coat (`coat_role` primer, undercoat, primer-undercoat, sealer).

### C8.7.2 Wood finishes
- C8.7.2.01 stain: coloured finish that soaks into wood and shows its grain. †
- C8.7.2.02 varnish: clear or tinted film-forming finish for wood. †
- C8.7.2.03 wood oil: penetrating oil finish for wood (decking and furniture oils). †
- C8.7.2.04 wax: wax finish rubbed into wood. †

### C8.7.3 Surface preparation
- C8.7.3.01 sandpaper: abrasive sheet or roll for hand or general use, not cut for one sander (K-12). †

## C8.8 Adhesives, sealants & fillers

Leaf axis: the bonding or sealing job (adhesives; sealants and fillers). Kind axis: adhesives by use (provisional until attested, CV-25); `chemistry` (silicone, acrylic, polyurethane), pack size and interior or exterior are attributes.

### C8.8.1 Adhesives
- C8.8.1.01 grab adhesive: high-tack construction adhesive from a cartridge that holds on contact.
- C8.8.1.02 general adhesive or glue: general-purpose glue for household and building repairs.
- C8.8.1.03 wood glue: adhesive made to bond wood (PVA and others).
- C8.8.1.04 wallpaper adhesive: paste for hanging wallpaper.
- C8.8.1.05 tile adhesive: adhesive for fixing wall and floor tiles (C-12).

### C8.8.2 Sealants & fillers
- C8.8.2.01 sealant (caulk): flexible compound that seals joints and gaps against water and air.
- C8.8.2.02 tile grout: compound that fills the joints between tiles (C-12).

## C8.9 Batteries & chargers

Leaf axis: cell shape (cylindrical, button and coin, rectangular and block; the shape letter of the IEC designation), plus the leaf Chargers (K-3). Kind axis: the standard size class buyers ask for by name (CV-19); chemistry, `rechargeable`, voltage and capacity are attributes; coin designations are named forms, product lines are lines rows.

### C8.9.1 Cylindrical cells
- C8.9.1.01 AA cell: cylindrical cell of IEC size R6 (aliases LR6, UM-3, Mignon, penlight).
- C8.9.1.02 AAA cell: cylindrical cell of IEC size R03.
- C8.9.1.03 C cell: cylindrical cell of IEC size R14.
- C8.9.1.04 D cell: cylindrical cell of IEC size R20.
- C8.9.1.05 CR123A cell: 3 V primary lithium cylindrical cell used in lights and cameras.
- C8.9.1.06 18650 cell: lithium-ion cylindrical cell 18 mm by 65 mm, sold loose.
- C8.9.1.07 21700 cell: lithium-ion cylindrical cell 21 mm by 70 mm, sold loose.

### C8.9.2 Button & coin cells
- C8.9.2.01 coin cell: flat button or coin cell (designations such as CR2032 are named forms).

### C8.9.3 Rectangular & block batteries
- C8.9.3.01 9 V battery: rectangular 9 V battery with snap terminals (IEC 6F22 and kin).
- C8.9.3.02 sealed lead-acid block: general sealed lead-acid battery block sold loose (6 V, 12 V).

### C8.9.4 Chargers
- C8.9.4.01 battery charger for standard-size cells: charger for loose standard cells such as AA, AAA and 18650 (K-3).

## C8.10 Fuels, lubricants & firelighting

Leaf axis: the role in burning: fuel by form (bottled gas, solid fuel, liquid fuel and lubricant) or the means of lighting it (Firelighting, C-7). Kind axis: fuel form and product, or lighting means; `gas`, `valve`, bottle size, wood species, bag weight and brand are attributes.

### C8.10.1 Bottled gas
- C8.10.1.01 LPG cylinder: refillable propane or butane bottle, owned or leased (`gas` and `valve` attributes; K-30).
- C8.10.1.02 gas canister: small disposable gas canister for stoves, torches and lighters (K-30, K-166). †

### C8.10.2 Solid fuels
- C8.10.2.01 firewood logs: split logs sold for burning (kiln-dried an attribute).
- C8.10.2.02 kindling: small dry sticks for starting a fire.
- C8.10.2.03 coal: coal or manufactured smokeless fuel sold in bags.
- C8.10.2.04 charcoal briquettes: moulded briquettes of compressed charcoal for barbecues.
- C8.10.2.05 lump charcoal: natural lumpwood charcoal (binchotan included).
- C8.10.2.06 wood pellets: compressed wood pellets for pellet grills, stoves and boilers.
- C8.10.2.07 smoking chips and chunks: wood chips or chunks for smoking food, by wood species.

### C8.10.3 Liquid fuels & lubricants
- C8.10.3.01 lubricant: general oil, grease or penetrating lubricant sold in a can or tube. †
- C8.10.3.02 lighter fluid: liquid fuel for refilling lighters or lighting barbecues. †
- C8.10.3.03 fuel can: container made to carry and store fuel. †

### C8.10.4 Firelighting
- C8.10.4.01 firelighter: block, cube or bag of fuel made to start a fire.
- C8.10.4.02 match: safety or strike-anywhere match. †
- C8.10.4.03 long utility lighter: long-nozzle lighter for barbecues, stoves and fires (pocket lighters are B9). †
- C8.10.4.04 candle lighter: long lighter made to light candles. †
- C8.10.4.05 lighter flint: replacement flint for a lighter (K-166). †

## C8.11 Packing & protection materials

No leaf (no source for a leaf axis; leaf = null); kind ids carry no leaf part. Kind axis: the packing material type; all kinds provisional until attested (C-7, K-193).
- C8.11.01 parcel tape: wide adhesive tape for sealing parcels and boxes. †
- C8.11.02 bubble wrap: plastic sheet of air bubbles for cushioning goods. †
- C8.11.03 stretch film: clinging plastic film wound round goods or pallets. †
- C8.11.04 void fill: loose fill, paper or air pillows packed round goods in a box. †
- C8.11.05 packing box: cardboard box sold flat for packing or moving (boxes made for storing things are B1). †

## Precedence inside C8

- A standard-size loose cell is filed by its size class (AA C8.9.1.01 to 21700 C8.9.1.07, 9 V C8.9.3.01), whatever device it powers and whatever its chemistry; rechargeable and primary cells of one size share one kind. Every button and coin cell is C8.9.2.01, its designation a named form; a general sealed lead-acid block sold loose is C8.9.3.02; a charger for standard-size cells is C8.9.4.01, while a platform pack or charger is C1, a one-device battery follows the device and a generic USB, GaN or Qi charger is D1 (K-3, K-4, C-19).
- A refillable propane or butane bottle is the LPG cylinder C8.10.1.01, owned or leased, whatever it is used with (barbecue, patio heater, camping, caravan); a small disposable canister is C8.10.1.02. A brand line inside one kind (Calor Patio Gas) is a named form of C8.10.1.01, and bottle size is an attribute (K-30, R-18).
- Gloss and satinwood paint for doors, trim and metal is C8.7.1.08; undercoat is the primer C8.7.1.10 with `coat_role`; emulsion is a binder, so emulsion for walls is C8.7.1.01 and masonry emulsion C8.7.1.02; anti-mould and similar properties are attributes (memo section 14).
- Tile adhesive (C8.8.1.05) and tile grout (C8.8.2.02) stay in C8.8 by use; tiling is a generated view over C8.2.1.03, C8.2.2.01, C8.7.1.06, C8.8.1.05 and C8.8.2.02 (C-12). Sealant is one kind (C8.8.2.01) whatever its chemistry.
- A wall tile (C8.2.1.03) and a floor tile (C8.2.2.01) are told apart by the place the tile is made and rated for; porcelain, ceramic and stone are `tile_material` values (memo section 14).
- Structural (strength-graded) and treated timber is sawn timber C8.1.1.01 with `strength_class` and `treatment_class`; boards sold loose for a pergola, gazebo or deck are C8.1.1.04 or C8.1.1.03, while a kit is filed by the structure it makes (K-66).
- Resin cartridges and capsules for chemical anchors are C8.3.5.03; anchor studs are steel anchors (C8.3.5.05) or parts included with the resin (memo section 14).
- A clip is filed by the object it holds: a pipe clip is C8.5.2.02, a cable clip C8.6.1.04; spring and other clips wait for evidence and have no kind (memo section 14).
- A bolt is C8.3.3.01 whatever its property class; a screw is filed by what it fastens into (C8.3.1.01 to C8.3.1.06), with drive, head and material attributes; stainless is a `material` value.
- A handle set without a lock is C8.4.2.02 and a cabinet knob or pull C8.4.2.01; a lockset that includes a lock is B8 (K-196). A letter plate fitted in a door is C8.4.5.01, a freestanding or wall letterbox B8 (K-188); a regulatory or safety sign is C8.4.5.02, a decorative sign or house number B4 (K-192); a bracket made to hold one screen or speaker follows it, and a general bracket is C8.4.4.01 (K-8).
- Taps (C8.5.3.01), valves (C8.5.3.02), traps, wastes and gutters (C8.5.4), shower trays, enclosures and bath panels (C8.5.5) are C8; the bath, shower unit or head, basin and toilet are B7 (K-186). A push-fit fitting of a proprietary system (JG Speedfit) is C8.5.1.02, its system a compatibility-ledger row.
- Mains cable, flex, switches, sockets, plugs, fuses, extension leads and ceiling roses are C8.6 (C8.6.1.01 to C8.6.3.01); plug and socket types A to O are named forms of C8.6.2.03 and C8.6.2.02; a lamp cord set is B3 and a device cable D1 (B-18).
- An electric-fence energiser (C8.1.8.06), tape (C8.1.8.07) and insulator (C8.1.8.08) follow the fence (K-195); livestock handling equipment is C7.
- Sand, aggregate and ballast sold for concrete, mortar or sub-base are C8.1.4.01; gravel and stone sold as decorative ground cover are C2 (K-174, K-187).
- Chimney and flue work (C8.1.6.01 to C8.1.6.03) is C8; the stove, boiler or fire it serves is B7 (B7-O1).
- Sandpaper and abrasive sheets and rolls for general use are C8.7.3.01; a sanding sheet or disc cut for one sander or grinder is C1 (K-12).
- Matches, firelighters, long utility and candle lighters, lighter flints and lighter fluid are C8.10.4 and C8.10.3.02; a pocket lighter is B9; barbecue charcoal is C8.10.2.04 or C8.10.2.05, hookah charcoal B9 (K-166).
- Parcel tape, bubble wrap, stretch film, void fill and flat-packed cardboard boxes for packing or moving are C8.11 (C8.11.01 to C8.11.05); envelopes and mailing tubes are C5 and storage boxes B1 (K-193).
- A facet-derived kind (screw application, paint surface, adhesive use) or a plumbing joint-system kind that finds no fetched page comparing or ranking its types is folded into a `use` or `surface` attribute on the general kind of its leaf (CV-25, C-19).
