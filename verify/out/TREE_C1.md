# C1 Tools & Workshop Equipment: decided tree

Category: C1 Tools & Workshop Equipment (domain C, Making, Growing & Work). Membership test (key step 32, branch 1): a tool, instrument or machine made to cut, shape, join, measure, test, lift, power or repair: hand and power tools, workshop machines, ladders, building and trade measuring and testing tools, portable generators, pumps, welding and soldering equipment, pocket knives and multi-tools, sack trucks, dollies and hand carts, tool boxes, tool bags and tool storage; a self-propelled machine made to dig, lift, load or move material (excavator, skid steer, telehandler, forklift, dumper) is C1 unless it does a farm or forestry job (C7) or keeps gardens and grounds (C2) (K-194). Not here: hand-held chainsaws, pole saws, pressure washers, wheelbarrows and garden, pool and pond pumps (C2); tractor-driven splitters and chippers and field irrigation pumps (C7); fighting and hunting knives, daggers, butterfly and automatic knives, ammunition (E4); kitchen knives and scales (B5); fasteners, fittings, extension leads, lubricants, fuels and general abrasives (C8); loose standard cells (C8) and generic chargers (D1); portable power stations (B7); wet-and-dry vacuums and household brushes (B6); desks, craft tables and general shelving (B1); jewellery, craft and hobby tools, craft glue guns and glass-fusing kilns (C4); rulers and household scissors (C5); sample and laboratory instruments and rangefinding binoculars (C6); golf and hunting rangefinders (E2); protective equipment (A1); toy tool sets (E1); Unimog-type carriers, ATVs and utility vehicles (G1). Structure (Candidate B, work done first, C-1; memo sections 3 and 10): sub-family (the work done, by the verbs of the membership test, plus tool storage and the multi-use sub-family C1.11; the closing parts sub-family C1.12 is exempt from this axis, C5(d)), then leaf (the tool family in the action sub-families, so hand, powered and machine versions of a family share a leaf; elsewhere the axis stated per sub-family; C1.6, C1.10 and C1.11 store `leaf = null`, C5(b), so their kind ids carry no leaf part), then kind (the generic tool type whose form differs, one step finer for machines by construction class, with combination machines as kinds where one fetched seller lists the class, C-10). Each object gets one kind. Mechanism is never a kind: `drive` (manual, corded electric, cordless, pneumatic, hydraulic, engine) and `mount` (hand-held, bench, stationary, self-propelled) are attributes on every kind (C10, C12; CV-24, CV-28), and the retail cut Hand tools / Power tools / Workshop machinery / Cordless is a generated view. Voltage, battery platform, brand, grade (pro or DIY), material, steel, size, finish and kit against bare unit are attributes, tier entries or ledger links, never kinds. Attributes decided at the build (memo section 14, DPH): `drive`, `sold_as` (bare unit or kit, a variant attribute), `tool_holder` and `impact_energy_j`; battery platforms, SDS-plus and SDS-max tool holders (`platform_type` "tool-holder system") and stacking storage systems are C13 compatibility-ledger rows, never kinds or named forms. Toolstation's "Air Tools & Compressors" and "Site equipment" are display views (a pneumatic `drive` view; a setting view over C1.8.4, C1.9.1 and C1.9.3), not nodes. Traditional Japanese types are kinds named generically by form with the native word in brackets (pull saws, pull plane, double-faced hammer: kinds provisional until fetched sellers in two regions give each its own category, C11, CV-27; otherwise non-maker named forms under the nearest generic kind in the same leaf), or non-maker named forms under a generic kind. Maker role: owner (maker_roles.tsv, provisional: tool platforms and models carry the maker; makers enter through lines and named forms). Display groups (navigation proposal and groups.tsv, display only; the tree keeps the memo's sub-families and leaves): level 1 Cutting & sawing (G-C1-1: C1.1); Drilling & driving (G-C1-2: C1.2); Shaping, sanding & finishing (G-C1-3: C1.3); Fastening, joining & clamping (G-C1-4: C1.4, C1.5, C1.6); Measuring & testing (G-C1-5: C1.7); Ladders, lifting & site machines (G-C1-6: C1.8); Power, air & batteries (G-C1-7: C1.9); Storage, kits & extraction (G-C1-8: C1.10, C1.11); Bits, blades & accessories (G-C1-9: C1.12); level 2 shows the memo leaves (G-C1-4-1 renamed "Hammers, mallets & demolition hammers", memo section 14), with a Hand / Power / Machine / Cordless toggle from `drive` and `mount` on every group; side views: a battery-platform tab from the C13 rows and a premium hand-tool makers tab from named forms and lines. Quality markers (display): powered tools by measured performance under load (torque, drilling and driving speed), handling and ergonomics, run time and battery capacity with breadth of the platform, durability and safety, motor (brushless) and warranty, voltage last; hand tools by steel and heat treatment, machining accuracy and fit, maker or smith; machines by duty class, construction class and motor power; measuring tools by accuracy and resolution. A kind marked † is named only by the key, a decision or memo text, or rests on a claim not yet shown on a fetched page, and needs a fetched page before it enters the data (memo attestation list, section 10; section 14 for the demolition hammer).

Ids (R-58): C1.n is a sub-family and C1.n.m a leaf; a kind is C1.n.m.kk, or C1.n.kk where a sub-family has no leaf.

## C1.1 Cutting & sawing

Leaf axis: tool family (hand, powered and machine versions of a family share a leaf); kind order by `drive` and `mount`, manual hand-held to stationary machine, then size.

### C1.1.1 Saws
- C1.1.1.01 panel saw: hand saw with a stiff, single-edged tapered blade on a handle, cutting on the push stroke (Western handsaw). †
- C1.1.1.02 hacksaw: hand saw with a thin replaceable blade tensioned in a bow frame, for metal, pipe and plastic.
- C1.1.1.03 double-edged pull saw [ryoba]: thin Japanese hand saw with crosscut teeth on one edge and rip teeth on the other, cutting on the pull stroke.
- C1.1.1.04 backed pull saw [dozuki]: Japanese pull saw whose thin fine-toothed blade is stiffened by a steel back, for joinery.
- C1.1.1.05 flush-cut pull saw [azebiki, kugihiki]: Japanese pull saw with a flexible blade and unset teeth that cuts flush against a surface.
- C1.1.1.06 circular saw: hand-held power saw with a rotating toothed disc for straight cuts in timber and sheet.
- C1.1.1.07 jigsaw: hand-held power saw with a short, vertically reciprocating blade for curves and cut-outs.
- C1.1.1.08 oscillating multi-tool: hand-held power tool whose blade, pad or scraper vibrates through a small arc, for plunge cuts, sanding and scraping.
- C1.1.1.09 mitre saw: power saw whose blade is carried on a pivoting arm over a table, for crosscuts and angle cuts (sliding and compound are attributes).
- C1.1.1.10 jobsite table saw: light portable table saw with the blade rising through a small bench top, carried to site.
- C1.1.1.11 hybrid table saw: stationary table saw with a cabinet-style top on a lighter open or part-enclosed base, between jobsite and cabinet types.
- C1.1.1.12 cabinet table saw: heavy stationary table saw with an enclosed cabinet base and the mechanism hung from the top.
- C1.1.1.13 sliding table saw: table saw with a sliding carriage beside the blade for panels and sheet.
- C1.1.1.14 woodworking bandsaw: machine with a continuous toothed band running over wheels, for curves, resawing and timber cutting.
- C1.1.1.15 metal-cutting bandsaw: bandsaw built for metal, with a fine-tooth band, slow speed, clamping vise and usually coolant.
- C1.1.1.16 cold cut saw: machine with a slow-turning circular blade that cuts metal bar and tube cleanly.
- C1.1.1.17 scroll saw: bench machine with a thin reciprocating blade held in tensioned arms, for fretwork and intricate curves.

### C1.1.2 Knives & multi-tools
- C1.1.2.01 utility knife: knife with a replaceable or snap-off blade for cutting materials in a trade or workshop.
- C1.1.2.02 pocket knife: small folding or locking knife carried in a pocket for general cutting (not a weapon blade pattern). †
- C1.1.2.03 pocket multi-tool: pocket-size tool with pliers and folding implements (knife, scissors, drivers, file, saw) in its handles. †

### C1.1.3 Axes & splitting tools
- C1.1.3.01 axe: long-handled tool with a bladed head for felling, hewing or splitting wood, of any pattern.
- C1.1.3.02 splitting maul: heavy-headed tool with a wedge face on one side and a flat sledge face on the other, for splitting logs. †
- C1.1.3.03 splitting wedge: steel wedge driven into wood with a hammer or maul to split it. †
- C1.1.3.04 log splitter: machine (hydraulic or other power, not tractor-driven) that forces a log against a wedge. †

## C1.2 Drilling, driving & turning

Leaf axis: tool family; kind order by `drive` and `mount`, manual hand-held to stationary machine, then size.

### C1.2.1 Drills
- C1.2.1.01 brace: hand-cranked drill with a sweep handle and a chuck.
- C1.2.1.02 drill/driver: hand-held rotary tool with chuck and clutch for drilling and driving screws.
- C1.2.1.03 hammer drill: drill/driver with an added percussive mode and ordinary chuck, for masonry and concrete.
- C1.2.1.04 rotary hammer: hand-held tool with an electro-pneumatic hammer mechanism and an SDS-type bit holder, for heavy drilling and chiselling in masonry.
- C1.2.1.05 drill press [pillar drill]: drill on a column with a table and feed lever, bench or floor mounted.

### C1.2.2 Screwdrivers & drivers
- C1.2.2.01 screwdriver: hand tool with a handle and tip that turns screws.
- C1.2.2.02 electric screwdriver: small powered driver for light screwdriving, without an impact mechanism.
- C1.2.2.03 impact driver: hand-held power driver with an impact mechanism and a quarter-inch hex bit holder.
- C1.2.2.04 hex key: bent or T-handled bar with a hexagonal end for socket screws.

### C1.2.3 Spanners, wrenches & sockets
- C1.2.3.01 combination spanner: fixed wrench with an open end and a ring end of the same size.
- C1.2.3.02 adjustable wrench: wrench with a movable jaw set by a screw.
- C1.2.3.03 socket wrench (ratchet): ratcheting drive handle that turns interchangeable sockets; a socket set is filed as this kind.
- C1.2.3.04 torque wrench: wrench that indicates or limits the tightening torque applied. †
- C1.2.3.05 impact wrench: power wrench with an impact mechanism and square drive for sockets and heavy fasteners.

## C1.3 Shaping & finishing

Leaf axis: tool family; kind order by `drive` and `mount`, manual hand-held to stationary machine, then size.

### C1.3.1 Planes & planers
- C1.3.1.01 smoothing plane: short hand plane for final surface smoothing (Stanley No. 1 to 4-1/2 pattern).
- C1.3.1.02 jack plane: medium-length hand plane for general stock removal (No. 5, 5-1/2, 6).
- C1.3.1.03 jointer plane: long hand plane for straightening edges and faces (No. 7, 8).
- C1.3.1.04 pull plane [kanna]: Japanese plane with a wooden body and blade set into it, cutting on the pull stroke.
- C1.3.1.05 power planer: hand-held electric plane with a rotating cutter drum.
- C1.3.1.06 jointer (machine): machine with infeed and outfeed tables and a cutterhead that flattens a face and squares an edge.
- C1.3.1.07 thicknesser: machine that planes boards to an even thickness against a bed.
- C1.3.1.08 planer-thicknesser: single machine combining jointer tables and a thicknessing bed on one cutterblock.

### C1.3.2 Chisels, gouges & mortisers
- C1.3.2.01 bench (striking) chisel: chisel made to be struck with a mallet, strong tang or socket and hooped or reinforced handle.
- C1.3.2.02 paring chisel: long, thin chisel pushed by hand for fine paring.
- C1.3.2.03 mortise chisel: thick, deep-bladed chisel struck to chop mortises.
- C1.3.2.04 woodturning gouge: long-handled gouge for shaping wood on a lathe.
- C1.3.2.05 mortiser: machine that cuts square mortises with a hollow chisel and auger.

### C1.3.3 Files, rasps & sharpening
- C1.3.3.01 file: hardened steel bar with cutting ridges for removing metal or wood by hand.
- C1.3.3.02 whetstone: block of natural or synthetic abrasive used with water or oil to sharpen blades (honing guides go with it).
- C1.3.3.03 bench grinder: electric motor with grinding wheels on a stand, for sharpening and shaping.
- C1.3.3.04 sharpening system: machine or jig system for sharpening edges, such as a slow wet wheel with jigs.

### C1.3.4 Grinders, sanders & polishers
- C1.3.4.01 angle grinder: hand-held power tool with a disc on a right-angle head, for grinding and cutting.
- C1.3.4.02 die grinder: straight-bodied high-speed hand tool for burrs and mounted points.
- C1.3.4.03 rotary tool: slim hand-held high-speed motor with a collet or chuck for small accessories (engraving, cutting, sanding, polishing).
- C1.3.4.04 random-orbit sander: hand-held sander with a round pad moving in orbit and rotation.
- C1.3.4.05 belt sander: sander with a continuous abrasive belt over two rollers.
- C1.3.4.06 polisher: power tool with a soft pad or mop that rotates to polish a surface.

### C1.3.5 Routers & moulders
- C1.3.5.01 router: power tool with a bit spinning in a base, for edges, grooves and recesses.
- C1.3.5.02 spindle moulder: stationary machine with a vertical spindle and cutter for moulding profiles.
- C1.3.5.03 CNC router: computer-controlled gantry machine that routes along programmed paths.

### C1.3.6 Lathes, mills & presses
- C1.3.6.01 wood lathe: machine that turns timber between centres or on a chuck against hand-held tools.
- C1.3.6.02 metal (engineering) lathe: machine that turns metal with a fixed cutting tool on a carriage.
- C1.3.6.03 milling machine: machine that cuts metal with a rotating multi-tooth cutter against a movable table.
- C1.3.6.04 reloading press: lever-operated press that holds dies to resize, prime and seat components of ammunition cartridges. †

### C1.3.7 Surface preparation & decorating brushes
- C1.3.7.01 wire brush: brush with steel or brass wire bristles to clean or abrade surfaces before work. †
- C1.3.7.02 decorating brush: brush for applying paint, varnish or stain to a surface. †

## C1.4 Striking & fastening

Leaf axis: tool family; kind order by `drive` and `mount`, manual hand-held to stationary machine, then size.

### C1.4.1 Hammers & mallets
- C1.4.1.01 claw hammer: hammer with a striking face and a curved claw for pulling nails.
- C1.4.1.02 double-faced hammer [genno]: Japanese hammer with two striking faces, one flat and one slightly convex.
- C1.4.1.03 mallet: soft-faced or wooden-headed hammer for striking chisels and assemblies. †
- C1.4.1.04 demolition hammer (breaker): powered percussion tool that drives a chisel or point by hammer blows only, with no rotation, to break concrete, masonry and tile (jackhammer and pneumatic or petrol breakers are this kind, `drive` an attribute; provisional until a page selling demolition hammers or breakers as a type is fetched; memo section 14). †

### C1.4.2 Pry bars & wreckers
- C1.4.2.01 wrecking bar: flat or round steel bar with a curved claw end for prying and demolition.

### C1.4.3 Nailers, staplers & riveters
- C1.4.3.01 nailer [nail gun]: tool that drives collated nails, powered by air, gas or electric/battery drive.
- C1.4.3.02 staple gun: tool that fires staples into a surface.
- C1.4.3.03 rivet gun: tool that sets rivets.

## C1.5 Joining & heat

Leaf axis: joining process; kind order by `drive` and `mount`, then size.

### C1.5.1 Welders
- C1.5.1.01 MIG welder: welding machine that feeds a continuous wire electrode through a gun with shielding gas.
- C1.5.1.02 TIG welder: welding machine using a tungsten electrode and a separate filler rod under shielding gas.
- C1.5.1.03 stick welder: welding machine that burns coated rod electrodes held in a clamp.
- C1.5.1.04 multi-process welder: one welding machine set up to run more than one of the MIG, TIG and stick processes.

### C1.5.2 Soldering & brazing
- C1.5.2.01 soldering iron: hand-held heated tip for melting solder, usually in electrical and electronics work. †
- C1.5.2.02 soldering station: temperature-controlled power base with a soldering iron handpiece and stand. †

### C1.5.3 Glue & heat guns
- C1.5.3.01 glue gun: hand-held electric tool that melts and dispenses adhesive sticks.
- C1.5.3.02 heat gun: hand-held electric hot-air tool for stripping, shrinking and softening.

## C1.6 Gripping, clamping & work holding

No leaf (about 12 kinds or fewer, leaf = null, C5(b)); kind ids carry no leaf part. Secondary key: the work held, from hand-held to floor-standing.
- C1.6.01 pliers: hand tool with two pivoted jaws to grip, bend or cut.
- C1.6.02 clamp: tool that presses and holds workpieces together by a screw, bar or lever.
- C1.6.03 bench vise: jaws fixed to a bench that hold a workpiece.
- C1.6.04 workbench: work surface made for tool work, with or without vises, dog holes and storage.
- C1.6.05 sawhorse: trestle-type support pair or single frame carrying a workpiece at working height.
- C1.6.06 trestle: frame support for a board or workpiece, used in pairs. †

## C1.7 Measuring, layout & testing

Leaf axis: what is measured or marked (K-147, K-148); kind order by resolution, coarse to fine.

### C1.7.1 Length & level
- C1.7.1.01 tape measure: coiled flexible rule in a case.
- C1.7.1.02 spirit level: straight body with liquid vials showing level or plumb.
- C1.7.1.03 laser distance measurer: handheld device that measures distance with a laser, for building and trade work. †

### C1.7.2 Precision gauging
- C1.7.2.01 caliper: sliding gauge measuring outside, inside and depth dimensions.
- C1.7.2.02 micrometer: screw gauge for precise outside, inside or depth measurement.
- C1.7.2.03 dial indicator: gauge with a plunger or lever and a dial showing small displacement.
- C1.7.2.04 height gauge: gauge on a base for measuring or marking height.
- C1.7.2.05 hardness tester: instrument that tests the hardness of a material.
- C1.7.2.06 coordinate measuring machine: machine that probes a part to measure its geometry in three axes.

### C1.7.3 Marking & layout
- C1.7.3.01 marking gauge [kebiki]: tool that scribes a line parallel to an edge.
- C1.7.3.02 square: right-angle tool for marking and checking squareness, including combination squares.

### C1.7.4 Test & inspection
- C1.7.4.01 multimeter: instrument that measures several electrical quantities for trade and electronics work. †

## C1.8 Lifting, access & materials handling

Leaf axis: what is lifted, reached or moved; kind order by height or load ascending.

### C1.8.1 Ladders
- C1.8.1.01 step ladder: free-standing hinged A-frame ladder.
- C1.8.1.02 platform step ladder: step ladder with a top platform to stand on.
- C1.8.1.03 combination ladder: ladder that can be set up in more than one form (step, extension, other) from one set of rails.
- C1.8.1.04 extension ladder: ladder with sliding sections that lean against a support. †
- C1.8.1.05 telescopic ladder: ladder whose rungs and rails telescope into each other. †

### C1.8.2 Jacks, hoists & winches
- C1.8.2.01 trolley jack: wheeled hydraulic floor jack with a lifting arm. †
- C1.8.2.02 bottle jack: hydraulic jack in a vertical bottle form. †
- C1.8.2.03 axle stand: stand that supports a lifted vehicle. †
- C1.8.2.04 engine hoist: folding crane that lifts engines. †
- C1.8.2.05 chain hoist: hand or electric hoist with a chain. †
- C1.8.2.06 winch: drum and rope or cable device for pulling or lifting. †

### C1.8.3 Hand trucks & carts
- C1.8.3.01 sack truck [hand truck]: upright two-wheel carrier with a toe plate for tilting and moving loads. †
- C1.8.3.02 dolly: low platform carrier on wheels or casters. †
- C1.8.3.03 hand cart: hand-pushed multi-wheel cart or trolley for goods. †

### C1.8.4 Earth-moving & site machines
- C1.8.4.01 excavator: machine with a boom, arm and bucket on a swinging house, tracked or wheeled (mini to full size). †
- C1.8.4.02 skid steer loader: compact loader steered by skidding wheels or tracks, with a lift arm. †
- C1.8.4.03 telehandler: loader with a telescopic boom. †
- C1.8.4.04 forklift: truck that lifts loads on forks. †
- C1.8.4.05 dumper: machine with a tipping body for hauling material on site. †
- C1.8.4.06 plate compactor: vibrating plate machine that compacts soil and aggregate. †
- C1.8.4.07 cement mixer: drum machine that mixes cement, mortar or concrete. †

## C1.9 Power & air supply

Leaf axis: what is supplied; kind order by output ascending.

### C1.9.1 Generators
- C1.9.1.01 inverter generator: engine-driven generator with inverter electronics for stable output.
- C1.9.1.02 conventional (open-frame) portable generator: engine-driven generator in an open frame with a directly coupled alternator.

### C1.9.2 Compressed air
- C1.9.2.01 air compressor: machine that makes compressed air for tools, in a general workshop or site role.

### C1.9.3 Pumps
- C1.9.3.01 submersible (drainage) pump: pump that sits under water to remove or drain it.
- C1.9.3.02 transfer pump: pump that moves liquid from one container to another. †

### C1.9.4 Cordless platform batteries & chargers
- C1.9.4.01 battery pack: rechargeable pack made for a maker's cordless tool platform.
- C1.9.4.02 charger: charger made for a maker's cordless tool platform.

## C1.10 Tool storage & carrying

No leaf (about 12 kinds or fewer, leaf = null, C5(b)); kind ids carry no leaf part. Secondary key: container form, by container size; material is an attribute and stacking systems (PACKOUT, TSTAK, ToughSystem and others) are C13 platform rows, not kinds.
- C1.10.01 portable toolbox: hand-carried box for tools.
- C1.10.02 wheeled toolbox [tool trolley]: tool box on wheels with a pull handle.
- C1.10.03 modular stackable tool case: case that locks onto other cases of a system by cleats or latches.
- C1.10.04 tool bag: soft or hard-bodied bag made to carry tools. †
- C1.10.05 tool roll: flexible roll-up wrap for tools. †
- C1.10.06 roller cabinet: drawered cabinet on casters. †

## C1.11 Multi-use tools & kits

No leaf (leaf = null, C5(b), C14(c)); kind ids carry no leaf part. Secondary key: kits first, then equipment that serves several tool families.
- C1.11.01 tool kit: assorted hand tools sold, standardised and compared as one object.
- C1.11.02 dust extractor [dust collector]: extraction unit for dust from workshop machines and power tools.
- C1.11.03 fume extractor: unit that draws away soldering or welding fumes. †

## C1.12 Parts and accessories made for one tool

The closing S3 parts sub-family, exempt from the level-1 axis (C5(d), CV-17). Leaf axis: the tool family served; nothing that is not a part may sit here.

### C1.12.1 Drill and driver bits
- C1.12.1.01 drill bit: cutting bit for a drill.
- C1.12.1.02 driver bit: screwdriving bit for a drill or driver. †

### C1.12.2 Saw blades
- C1.12.2.01 saw blade: toothed blade made for a saw.

### C1.12.3 Abrasives cut for one power tool
- C1.12.3.01 grinding disc: disc cut for a grinder. †
- C1.12.3.02 sanding sheet cut for one sander: sheet or disc shaped to fit one sander. †

### C1.12.4 Welding and soldering consumables
- C1.12.4.01 welding wire: wire electrode for wire-fed welding. †
- C1.12.4.02 welding rod [electrode]: coated or bare rod for stick or TIG welding. †
- C1.12.4.03 solder: fusible alloy for soldering. †

### C1.12.5 Press tooling
- C1.12.5.01 reloading die: die for a reloading press. †

## Precedence inside C1

- Mechanism is an attribute, not a level: a manual and a powered version of the same form share one kind; a powered tool of a different form is its own kind (a circular saw C1.1.1.06 is not a panel saw C1.1.1.01; a power planer C1.3.1.05 is not a smoothing plane C1.3.1.01). Hand, power and machine versions of one tool family sit in the same leaf.
- A tool with several actions is filed by the primary action the maker names (C14, CV-31). The oscillating multi-tool goes to C1.1.1.08, the rotary tool and the angle grinder to C1.3.4 (C1.3.4.03, C1.3.4.01), the heat gun to C1.5.3.02. "Multi-tool" has two targets: the pocket multi-tool (C1.1.2.03) and the oscillating multi-tool (C1.1.1.08); "jointer" has two: the jointer plane (C1.3.1.03) and the jointer machine (C1.3.1.06).
- A combination machine or combination form is its own kind where one is named above (planer-thicknesser C1.3.1.08, combination ladder C1.8.1.03, multi-process welder C1.5.1.04), filed in the leaf of its primary action; otherwise it goes to the kind of its primary action (C-10). The multi-process welder is a kind provisional until a fetched seller page lists the class; otherwise each model files under the welder kind of its primary process (C1.5.1.01 to C1.5.1.03).
- For machines, the construction class that changes the body is a kind (jobsite, hybrid, cabinet and sliding table saws C1.1.1.10 to C1.1.1.13; wood against metal lathes C1.3.6.01, C1.3.6.02 and bandsaws C1.1.1.14, C1.1.1.15); benchtop against floor-standing and sliding against fixed are attributes.
- A powered percussion tool that only hammers a chisel or point, with no rotation (breaker, jackhammer, pneumatic or petrol breaker), is the demolition hammer C1.4.1.04; a tool that drills with a hammer action is the rotary hammer C1.2.1.04, also when it has a chisel-only mode (memo section 14, primary action).
- A set of objects of one kind is filed as that kind (a socket set is a socket wrench, C1.2.3.03). An assortment of different hand tools sold and compared as one object is a tool kit (C1.11.01) (K-1).
- Size, voltage, battery platform, grade, brand, material, steel and bare unit against kit are attributes, never kinds. A battery pack or charger made for a maker's cordless platform is C1.9.4.01 or C1.9.4.02, whatever tools or garden machines the platform runs (K-3, K-4).
- A traditional type with a native name that a generic kind covers is filed at the generic kind as a named form without a maker (an oire-nomi at bench (striking) chisel C1.3.2.01); the types with their own kind above (ryoba C1.1.1.03, dozuki C1.1.1.04, azebiki C1.1.1.05, kanna C1.3.1.04, genno C1.4.1.02) go to that kind while it holds (C11 two-region tie-break), and otherwise to the nearest generic kind in the same leaf.
- A component, bit, blade or consumable made for one tool family is a part and goes to C1.12 (welding wire C1.12.4.01, drill bit C1.12.1.01, saw blade C1.12.2.01, reloading die C1.12.5.01, a disc cut for one grinder C1.12.3.01); nothing that is a complete tool or machine sits in C1.12 (S3, K-12).
- A dust extractor serves machines in several sub-families, so it is filed in C1.11 (C1.11.02), not in C1.12 (K-18, C14(c)).
- A work surface made for tool work (workbench C1.6.04), a sawhorse (C1.6.05) and a trestle (C1.6.06) are C1.6 (K-190, C1-O1); a box, bag, case or cabinet made to hold and carry tools is C1.10.
- A reloading press is filed in C1.3.6 (C1.3.6.04) and its dies in C1.12.5 (C1.12.5.01) (K-86); sharpening stones and honing guides are C1.3.3 (whetstone C1.3.3.02) whoever sharpens what.
- Axes of every pattern, mauls, wedges and log splitters are C1.1.3 (K-173); a wire brush and a decorating brush are C1.3.7 (B6-O1).
- A tool made to service a vehicle, bicycle or machine is a tool (jacks, hoists and winches in C1.8.2; torque wrench C1.2.3.04) (K-13).
- A self-propelled machine made to dig, lift, load or move material is C1.8.4 (K-194); a hand-pushed carrier is C1.8.3.
- Pumps for drainage, transfer and general use are C1.9.3 (K-175); generators and compressors for site and workshop power are C1.9 (C1.9.1, C1.9.2.01).
