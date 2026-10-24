# G2 Property & Structures: decided tree

Category: G2 Property & Structures (domain G, Vehicles & Property). Membership test (key step 4): land; a building or other permanent structure made to be occupied, entered or enclosed (house, flat, garage, barn, stable block, shed, garden room, summerhouse, carport, in-ground pool, pergola, gazebo, decking, patio); shipping containers and portable cabins kept in place as stores or rooms; a vehicle or vessel made to stay in one place as a dwelling (moored houseboat without propulsion, floating home, static caravan, lodge or park home, park model, tiny house on wheels); a burial plot, crypt or niche, however it is held. A building is filed as a whole; its elements and products, installed or not, are filed by what they are. Not here: structural, envelope and finishing products, fencing, decking boards and paving sold loose (C8); kitchen and wardrobe cabinetry, garden storage boxes and pop-up gazebos (B1); carpets, blinds and curtains (B2); baths, showers, basins, toilets, hot tubs and portable saunas (B7); greenhouses, polytunnels, above-ground and inflatable pools and pool equipment and chemicals (C2); hutches, coops, kennels, stalls inside a building and bird boxes (B10); treehouses and playhouses (E1); tents, yurts and tipis (E2); a hull with its own propulsion and steering made to navigate (narrowboat, Dutch barge, cruising or pontoon houseboat), touring caravans, motorhomes and trailers (G1); caskets, urns, headstones and grave markers (F4); deeds and certificates (F5); tenancies, timeshares, moorings, berths, rented parking bays, permits and other use rights (OUT). Structure (Candidate 3A, what is held first; memo sections 3, 4b and 10): sub-family (what kind of thing is held: land, a home, another building or structure, a place for the dead; four sub-families, no Parts-and-accessories sub-family, CV-17), then leaf (one axis stated per sub-family; Burial places has no leaf level, C5b, so its kind ids carry no leaf part), then kind (where the sources' search filters and census or survey categories stop; a legal or licence class alone never makes a kind, G-12), then named form. Each object gets one kind. Tenure, region, era, price, size, floor and plot area, bedrooms, storeys, style, regional name, build standard, site licence, build history (new or pre-owned), location and market (domestic, commercial) are facets, named forms, C17 jurisdiction rows or views, never kinds; G2 stores no value for any one particular property (C16). Attributes decided at the build (memo section 14, DPH): `house_form`, `floor_position`, `construction`, `propulsion` (none or towed on the moored houseboat and floating home, the K-60 line), `units_in_building`, `managed_for`, and for burial places `burial_position`, `remains`, `capacity` and `allocation`, each stored only where the value holds for every object of the kind or named form; `build_history` is stored only on named forms where it holds for every object (loft = conversion; factory-built models in G2.2.4 = new build), and the new or pre-owned choice is a buying-guide question, not a branch. Rental is out of scope (only what is owned is a possession); location, rail line, commute, price, bedrooms and the other listing filters are display only, shown as the "what to filter by" line of each guide. Registry rows needed (not kinds): EPC A to G and RICS survey levels (grading scales), Agricultural Land Classification (grading scale; `alc_grade` never stored on a parcel), building and pest inspection (AU) and LIM report (NZ) as standards, BS 3632, BS EN 1647, HUD code, IRC Appendix Q and RV standards as `standard_met` on factory-built named forms, and China Grade A and 5A offices as a scheme serving G2.3.7.1. Maker role (maker_roles.tsv, provisional): none for land, houses, flats and burial places, where property is chosen by type and place; owner for factory-built homes, garden buildings and pool shells, where models carry the builder; price bands attach only to those makers, lines and models (C4(d)). Display groups (navigation proposal, display only; the tree keeps the memo's sub-families and leaves): level 1 Houses and flats (G2.2.1, G2.2.2, G2.2.3); Park, mobile and floating homes (G2.2.4); Land and farms (G2.1); Garden buildings and outbuildings (G2.3.1 to G2.3.6); Commercial buildings (G2.3.7); Burial places (G2.4); level 2 Houses, Flats and maisonettes, Whole residential buildings; Building plots, Farm land, Woodland, Lakes and water, Mixed holdings and smallholdings; Garages and carports, Sheds and workshops, Garden rooms and cabins, Barns and stables, Gazebos, pergolas, decks and patios, Swimming pools. Side views: a makers' ranges tab for G2.2.4, G2.3.2 and G2.3.3 kit buildings and G2.3.6 pool shells only; a "by tradition" view of regional named forms; tiny-house and liveaboard views. Quality markers (display): homes by location and neighbourhood, then structural condition, then legal title and tenure (freehold above share of freehold above leasehold), then energy performance (EPC A to G) and orientation, then fit to the household; land by principal use and land quality (ALC grade 1 > 2 > 3a > 3b > 4 > 5), then access and water, then area; factory-built homes and garden buildings by build standard (residential BS 3632 against holiday BS EN 1647, HUD code), then the maker's range and materials (provisional); burial places by position and capacity (provisional).

Ids (R-58): G2.n is a sub-family and G2.n.m a leaf; a kind is G2.n.m.kk, or G2.n.kk where a sub-family has no leaf. G2's builder ids were adopted as built (R-58; memo section 13, frozen tree audit/KL_G2_tree_v2.md) and are kept exactly, with single-digit kind numbers.

## G2.1 Land

Leaf axis: land cover and principal use. Land is filed by its principal land use whether or not it carries buildings; dwellings and farm buildings on it are the facet `improvements`. Kind axis: crop, cover or holding.

### G2.1.1 Building land
- G2.1.1.1 building plot: a parcel of land sold to build on, with or without planning permission.

### G2.1.2 Cropland
- G2.1.2.1 arable land: land used or sold for growing field crops such as cereals, roots or oilseeds.

### G2.1.3 Grassland
- G2.1.3.1 grazing land: pasture, paddock or meadow held for livestock or horses.

### G2.1.4 Permanent crops
- G2.1.4.1 orchard: land planted with fruit or nut trees.
- G2.1.4.2 vineyard: land planted with grape vines.

### G2.1.5 Woodland
- G2.1.5.1 woodland: land under trees, whether managed for timber, amenity or conservation (`managed_for`).

### G2.1.6 Water and wetland
- G2.1.6.1 lake: a body of water, pond, fishery or wetland held as the property.

### G2.1.7 Mixed holdings
- G2.1.7.1 mixed holding: a holding with no single principal use (no one use covers more than half the area, or areas are not given and several uses are combined with none sold as the main one); area (`plot_area`) and enterprises (`enterprises`) are attributes.

## G2.2 Dwellings

Leaf axis: what is owned against the building around it (a whole house; a unit inside a building; a whole building of two or more dwellings; a dwelling kept in place that is not a building).

### G2.2.1 Houses
Kind axis: attachment to neighbouring dwellings.
- G2.2.1.1 detached house: a whole house standing free of neighbours; a factory-built home on a permanent foundation and a unit that meets the dwelling test are filed here.
- G2.2.1.2 semi-detached house: a house joined to one neighbour on one side.
- G2.2.1.3 terraced house: a house in a row, joined to neighbours on both sides or, at the end of the row, on one side.

### G2.2.2 Flats and maisonettes
Kind axis: levels in the unit.
- G2.2.2.1 flat: one dwelling unit on a single level inside a larger building.
- G2.2.2.2 maisonette: one dwelling unit whose rooms are on two or more full levels inside a larger building.

### G2.2.3 Multi-unit residential buildings
Kind axis: one kind (`units_in_building` is the facet).
- G2.2.3.1 multi-unit residential building: a whole building of two or more dwellings held as one object.

### G2.2.4 Dwellings kept in place that are not buildings
Kind axis: physical form, listed from least to most fixed. Build standard and site licence are `standard_met` and C17 rows, never the test.
- G2.2.4.1 moored houseboat: a hull without its own propulsion and steering, made to stay moored as a dwelling.
- G2.2.4.2 tiny house on wheels: a small dwelling built on a trailer chassis, however often it is towed.
- G2.2.4.3 park model: a single-section dwelling or cabin built on an RV trailer chassis and sold as a park model RV.
- G2.2.4.4 static caravan: a home made as one section on a chassis, whatever its width, kept on one pitch and not built as a park model RV.
- G2.2.4.5 lodge or park home: a factory-built home made as two or more sections joined on the pitch (twin-unit), for holiday or residential use.
- G2.2.4.6 floating home: a dwelling on a float or hull moored in a slip, connected to shore utilities, not made to navigate.

## G2.3 Other buildings & structures

Leaf axis: what the building or structure is for. Kind axis: the use-named building or structure; roof shape, material, wall construction, size and attached or freestanding (C12) are attributes.

### G2.3.1 Vehicle shelter
- G2.3.1.1 garage: an enclosed building for vehicles, attached or freestanding.
- G2.3.1.2 carport: a roofed, open-sided shelter for vehicles.
- G2.3.1.3 cart shed: an open-fronted farm building for carts and farm machinery.
- G2.3.1.4 boathouse: a building for keeping boats, on or beside water. †

### G2.3.2 Storage and work
- G2.3.2.1 garden shed: a small outbuilding for tools and garden storage that a person can enter.
- G2.3.2.2 workshop: a building made for repair or craft work, domestic or commercial. †
- G2.3.2.3 shipping container (kept in place): a shipping container fixed on a site as a store or room.

### G2.3.3 Rooms for people
Garden buildings that lack their own sink, toilet or entrance (K-63); a log-walled building fitted for one purpose is filed by that purpose.
- G2.3.3.1 summerhouse: a garden building for sitting and relaxing in.
- G2.3.3.2 garden office: an insulated garden building made to work in.
- G2.3.3.3 garden log cabin: a log-walled garden building made as a general room or retreat, not fitted for one purpose.
- G2.3.3.4 garden bar: a garden building fitted as a bar, with a bar counter or serving hatch, whatever its walls.
- G2.3.3.5 sauna cabin: a sauna that stands as a building.

### G2.3.4 Animal and crop buildings
- G2.3.4.1 barn: a large farm building with an open interior for hay, grain, machinery or loose-housed livestock.
- G2.3.4.2 stable block: a building whose floor is laid out mainly as stalls or loose boxes, even when sold as a horse barn or built with a hay loft or tack room.
- G2.3.4.3 granary: a building for storing grain that a person can stand in.
- G2.3.4.4 dovecote: a building for housing doves or pigeons that a person can enter.

### G2.3.5 Shade and surface structures
- G2.3.5.1 gazebo: a freestanding, open-sided structure with a roof (boarded, shingled, tiled or a fixed canopy).
- G2.3.5.2 pergola: an open frame of posts and beams or rafters whose top is open, slatted or planted.
- G2.3.5.3 decking: a raised timber or composite platform built in place, including one built for a tent, yurt or tipi.
- G2.3.5.4 patio: a laid paved or hard surface outside a building.
- G2.3.5.5 jetty or pontoon: a fixed or floating structure for mooring or access over water, held as a structure (not a mooring right). †

### G2.3.6 Pools
Kind axis: one kind; construction (fibreglass, vinyl liner, concrete or gunite) is the attribute `construction` (G-17, provisional until a non-US seller is attested).
- G2.3.6.1 in-ground swimming pool: a swimming pool built into the ground.

### G2.3.7 Other buildings by function
Kind axis: the function the building is made for (K-62); market never divides them, and finer functions are named forms.
- G2.3.7.1 office building: a building made for offices.
- G2.3.7.2 shop: a building made for retail trade. †
- G2.3.7.3 warehouse: a building made for storing goods in bulk. †
- G2.3.7.4 industrial unit: a building made for producing goods (manufacturing, processing, assembly). †
- G2.3.7.5 hotel: a building made for letting rooms to guests. †

## G2.4 Burial places

No leaf level (C5b). Kind axis: interment structure and position; capacity, depth, position, remains, allocation and perpetual care are attributes.
- G2.4.1 ground burial plot: an in-ground grave space for a casket, of single, companion or family capacity.
- G2.4.2 cremation (urn) plot: an in-ground plot for cremated remains.
- G2.4.3 lawn crypt: an underground pre-built vault set in a lawn section.
- G2.4.4 mausoleum crypt: an above-ground chamber for a casket inside a community mausoleum.
- G2.4.5 private mausoleum: a freestanding building holding crypts for one family.
- G2.4.6 columbarium niche: a compartment in a wall, stele or building for an urn.
- G2.4.7 green burial plot: one person's or one family's own grave space in a natural setting, including one of several sites at a shared tree.
- G2.4.8 communal grave space [goshi-bo, 合祀墓]: a shared burial space where the remains of many people are placed together, with no separate site for each.

## Precedence inside G2

1. File what is owned: a whole building of two or more dwellings is G2.2.3.1; one dwelling of a pair or row is G2.2.1.2 or G2.2.1.3; one unit in a block is G2.2.2.1 or G2.2.2.2.
2. A unit whose rooms are on two or more full floors is a maisonette (G2.2.2.2), whatever its position (penthouse) or history (loft conversion); one on a single floor is a flat (G2.2.2.1) (G-15).
3. Land is filed by its principal land use, the use that covers more than half of the holding's area, whether or not it carries buildings; the dwelling and farm buildings on it are the facet `improvements`. A house whose land is garden and grounds, or mostly so, is filed as the dwelling. A holding where no one use covers more than half, or where areas are not given and several uses are combined with none sold as the main one, is a mixed holding (G2.1.7.1) (G-13).
4. A unit with its own sink, toilet and entrance is a dwelling, a detached house (G2.2.1.1), whatever it is sold as (garden room, garden office, log cabin, summerhouse); without any one of the three it is a garden building (G2.3.3) (K-63).
5. "Log cabin" names two objects: a garden log cabin is G2.3.3.3; a log house that meets the dwelling test is a detached house (G2.2.1.1) with `construction` = log. A log-walled garden building fitted for one purpose (bar G2.3.3.4, office G2.3.3.2, sauna G2.3.3.5, garage G2.3.1.1) is filed by that purpose; log walls are an attribute.
6. An integral garage is part of the house, which is filed as a whole; a garage building of its own is G2.3.1.1, attached or freestanding (C12).
7. A factory-built home set on a permanent foundation is a detached house (G2.2.1.1) with `construction` = manufactured or modular; one kept on its chassis or on a pitch is a static caravan (G2.2.4.4) or a lodge or park home (G2.2.4.5) (G-16).
8. Test the object as made (S5). A hull with its own propulsion and steering made to navigate (narrowboat, Dutch barge, cruising or pontoon houseboat), and a trailer, caravan or motorhome made for road towing or driving, are G1, however long they are kept in one place and whether or not someone lives in them. A dwelling made to stay in one place is G2: a floating home (G2.2.4.6) or house barge without propulsion (G2.2.4.1), a static caravan (G2.2.4.4), a lodge or park home (G2.2.4.5), a park model RV (G2.2.4.3), and a tiny house on wheels (G2.2.4.2) however often it is towed (K-60, K-61).
9. Among dwellings kept in place on a chassis or a pitch, the build decides: one made as one section is a static caravan (G2.2.4.4), unless it is built on an RV trailer chassis and sold as a park model RV (G2.2.4.3); one made as two or more sections joined on the pitch is a lodge or park home (G2.2.4.5). Width, build standard and holiday or residential use are attributes or C17 rows, never the test.
10. A shipping container kept in place as a store or room is G2.3.2.3; one on a trailer or used to ship goods is G1 or C8 by what it is made for.
11. A pergola, gazebo or decking kit is filed by the structure it makes (G2.3.5.2, G2.3.5.1, G2.3.5.3); a shed or cabin sold as a kit is filed as the building; boards, panels and canopies sold loose are C8 (K-66). Shed and garden-building accessories are C8, B1 or C1; nothing is received under S3.
12. Decking (G2.3.5.3) and patio (G2.3.5.4) laid are G2; decking boards and paving stones are C8. Tents, yurts and tipis are E2 as made, whatever platform they stand on; a platform or deck built for them is decking (G2.3.5.3) (K-65).
13. A sauna cabin that stands as a building is G2.3.3.5; a portable sauna is B7; a hot tub is B7 (K-64).
14. A greenhouse and an above-ground pool are C2; an in-ground pool (G2.3.6.1) and a stable block a person can stand in (G2.3.4.2) are G2; a treehouse and a playhouse are E1; a hutch, coop or kennel is B10; a pop-up gazebo is B1. Equipment and chemicals made for a swimming pool are C2 (K-176).
15. A dovecote (G2.3.4.4) or granary (G2.3.4.3) that is a building a person can stand in is G2; a bird box or feeder is B10.
16. A shed a person can enter (G2.3.2.1) is G2; a garden storage box that holds several objects and stands outdoors is B1.
17. The plot, crypt or niche (G2.4.1 to G2.4.8) is G2; the casket, urn, headstone and marker placed in or on it are F4; the deed or certificate is F5.
18. A burial place is G2 however it is held (owned, leased or held on a use right); a mooring, berth, allotment or parking permit is a right and OUT. A share or membership that grants only use of a slip, pitch or space is OUT; the floating home (G2.2.4.6), static caravan (G2.2.4.4) or lodge (G2.2.4.5) standing on it is G2 (G-18).
19. A garage building (G2.3.1.1) or a parking bay held as land is G2 (the freehold bay is G2.1 Land, its kind not yet settled †); a rented bay or a permit is OUT (K-67).
20. Commercial, industrial and institutional buildings are filed by what the building is made for in G2.3.7; market never divides them. A flat in a commercial building is still a flat (G2.2.2.1) (K-62).
21. Bungalow, courtyard, cave, castle or château and barn-type are `house_form` values, not kinds; style and regional names are named forms under the attachment kind their source shows, else under detached house (G2.2.1.1) (G-14).
22. A gazebo (G2.3.5.1) has a roof over open sides; a pergola's (G2.3.5.2) top is open or slatted, and side curtains or screens do not make it a gazebo.
23. A building whose floor is laid out mainly as stalls or loose boxes is a stable block (G2.3.4.2), even when sold as a horse barn or built with a hay loft or tack room; a barn (G2.3.4.1) has an open interior for hay, grain, machinery or loose-housed livestock.
24. A building made for repair or craft work is a workshop (G2.3.2.2), domestic or commercial; one made for producing goods (manufacturing, processing, assembly) is an industrial unit (G2.3.7.4). Rule 20 does not move a workshop into G2.3.7.
25. A green burial plot (G2.4.7) is one person's or one family's own site in a natural setting, even one of several sites at a shared tree; a communal grave space (G2.4.8) holds the remains of many people together with no separate site each.
26. A private mausoleum is filed in Burial places (G2.4.5), not in Other buildings & structures, because buyers choose it as an interment option.
