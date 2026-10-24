# B7 Climate, Water & Energy: decided tree

Category: B7 Climate, Water & Energy (domain B, Home). Membership test (placement key step 30, third branch): made to heat, cool, ventilate, purify or humidify air; to heat, soften, filter or supply water for bathing and washing, or take away waste; or to generate, store or meter electricity for the home (heaters, fans and ceiling fans, air conditioners, heat pumps, dehumidifiers, air purifiers, thermostats, water heaters, softeners and filters, baths, showers, basins, toilets and bidets, hot tubs and portable saunas, solar panels and inverters, home batteries and portable power stations, small wind turbines, energy meters), and the parts and consumables made for one B7 object. Structure (B-8, Candidate A): sub-family (what the equipment acts on: room air, water, electricity; then the closing parts sub-family, exempt from that axis, CV-17), then leaf (the job done to the air, the water or the electricity; parts by the object served), then kind (the device type buyers compare on quality or maker), with named forms below the kind (lines and iconic designs). Each object gets one kind. Fuel and power source, efficiency grade (stored as scheme plus value with its standard named, never normalised and never a tier, B7-O2), capacity class (BTU, kW, horsepower, tatami, litres, go number, pints per day, kWh, panel watts), installation and mounting, form factor, smart or plain, inverter or fixed-speed, refrigerant, heat source, cold-climate listing, grid connection, standard met (NSF/ANSI, UL, ETL, CSA, UL9540), certification (ENERGY STAR, EU energy label, China and Japan grades), noise, warranty, maker, era, condition, region, market, user, setting and price band are attributes, tags or views, never kinds. Section 14 adds the attributes `heat_pump_configuration` (hybrid or dual-fuel) and `heat_pump_drive` (absorption), each a kind only if a fetched source ranks it apart (C10(b), provisional). Makers (maker_roles.tsv B7, owner, provisional): the type leads; makers enter through named forms and lines (Kirigamine, Washlet, ProTerra) and the OEM relations of rebadged mini-splits; there is no maker tab. Display only (proposals.tsv row B7): the level-1 groups (Heating; Heat pumps and air conditioning; Fans and ventilation; Air purifiers, humidifiers and dehumidifiers; Thermostats and controls; Water heating; Water treatment; Baths, showers, toilets and basins; Hot tubs and saunas; Solar panels, inverters and batteries; Filters, salt and spare parts) regroup the memo's leaves for shoppers and never move a home or an id; each leaf names its group, and the cross-leaf group "Heat pumps and air conditioning" gathers B7.1.1.16, B7.1.1.17, every B7.1.2 kind and B7.2.1.03 (section 14). A kind marked † is named only by the key, a decision or a neighbour memo and needs a fetched page before it enters the data; several kinds are provisional (noted in their lines).

Ids (R-58): B7.n is a sub-family and B7.n.m a leaf; a kind is B7.n.m.kk, or B7.n.kk where a sub-family has no leaf.

## B7.1 Room air
Leaf axis: the job done to the air (heat, cool, move, treat, control).

### B7.1.1 Heating
Kind axis: how the heat is made and emitted; fuel is a tag; flue and installation separate the stove, fire and flueless kinds (C10(b)); delivery medium for heat pumps (B-24). Display group: Heating; B7.1.1.16 and B7.1.1.17 display in Heat pumps and air conditioning.
- B7.1.1.01 Central-heating boiler: appliance that heats water for a home's radiators or underfloor circuit; heating-only or combi is a function attribute, fuel a tag, and a combi boiler pack is a unit-of-sale attribute (section 14).
- B7.1.1.02 Furnace: warm-air heating plant that heats air and sends it through ducts; fuel is a tag (B7-O1).
- B7.1.1.03 Panel radiator: flat-panel heat emitter, usually fed by hot water.
- B7.1.1.04 Column radiator: heat emitter built of upright columns or sections; material and era are attributes.
- B7.1.1.05 Towel radiator [Badheizkörper]: heated rail made to warm and dry towels in a bathroom; hot-water or electric is a power attribute.
- B7.1.1.06 Fan heater: room heater that blows air over a heating element; fuel is a tag.
- B7.1.1.07 Convector heater: room heater that warms air by natural convection over an element. †
- B7.1.1.08 Oil-filled radiator: portable electric heater with sealed oil-filled fins.
- B7.1.1.09 Radiant heater: heater with an exposed bar, quartz or halogen element and reflector (split from the panel heater by form, provisional).
- B7.1.1.10 Infrared panel heater: flat wall- or ceiling-hung panel that heats by infrared radiation; picture-motif prints are variants.
- B7.1.1.11 Infrared heat lamp: lamp sold as a heater, not a bulb sold as a part. †
- B7.1.1.12 Flued stove: solid-fuel stove with a firebox vented through a flue (rule T(b), provisional until a fetched source ranks it apart).
- B7.1.1.13 Flueless room heater: kerosene or gas room heater with no flue (rule T(b), provisional as above).
- B7.1.1.14 Flued fire: inset or wall-hung fire vented through a flue; fuel is a tag (B7-O1; rule T(b), provisional). †
- B7.1.1.15 Underfloor heating kit: electric mat or hydronic pipe kit sold to heat a floor (B7-O1). †
- B7.1.1.16 Hydronic heat pump: air-to-water heat pump that heats water for radiators or a floor; heat source is an attribute.
- B7.1.1.17 Ground-source heat pump: heat pump drawing heat from a ground loop, a kind whatever it delivers (B-24).

### B7.1.2 Cooling
Kind axis: form and install position (C12(a)); reversible, inverter, refrigerant and cold-region are attributes. Display group: Heat pumps and air conditioning.
- B7.1.2.01 Wall-mounted split air conditioner [mini-split heat pump; 挂机]: indoor wall unit linked by refrigerant lines to an outdoor unit; reversible is a tag.
- B7.1.2.02 Floor-standing air conditioner [柜机]: split air conditioner whose indoor unit stands on the floor as a cabinet.
- B7.1.2.03 Ceiling-cassette air conditioner: split air conditioner whose indoor unit is set into the ceiling.
- B7.1.2.04 Window air conditioner: single-box unit fitted in a window or wall opening.
- B7.1.2.05 Portable air conditioner: movable single-box unit venting through a hose.
- B7.1.2.06 Ducted or central system [中央空调]: multi-split or ducted plant cooling several rooms, a ducted heat pump included.

### B7.1.3 Air movement and ventilation
Kind axis: fan body form, or the duct for ventilation. Display group: Fans and ventilation.
- B7.1.3.01 Desk fan: small fan made to stand on a desk or table.
- B7.1.3.02 Stationary fan [pedestal fan]: fan on a stand or pedestal of adjustable height.
- B7.1.3.03 Tower fan: tall, narrow fan blowing through a vertical grille.
- B7.1.3.04 Wall or clip fan: fan made to mount on a wall or clip to an edge (body test against the desk fan provisional, C12(a)).
- B7.1.3.05 Handheld fan: powered hand-held or neck fan; a manual hand fan is A4 (K-133).
- B7.1.3.06 Air circulator: fan made to move air round a whole room in a focused stream.
- B7.1.3.07 Ceiling fan: fan hung from the ceiling, with or without a light.
- B7.1.3.08 Ventilating fan [extractor fan]: fan fitted to draw stale air out of a room.
- B7.1.3.09 Ventilation unit: ventilation unit for a room or home, with or without heat recovery.

### B7.1.4 Air treatment
Kind axis: the treatment performed (particles, moisture added or removed, odour, ions); dehumidifier classes by C10(b). Display group: Air purifiers, humidifiers and dehumidifiers.
- B7.1.4.01 Air purifier: appliance that filters particles and pollutants from room air; tower or desktop and filter grade are attributes.
- B7.1.4.02 Humidifier: appliance that adds moisture to room air; mechanism (ultrasonic, evaporative, warm mist) is an attribute (B-25).
- B7.1.4.03 Portable dehumidifier: movable appliance that draws moisture from room air.
- B7.1.4.04 Whole-house dehumidifier: dehumidifier installed to treat a whole home, usually ducted.
- B7.1.4.05 Mini dehumidifier: small-capacity dehumidifier; Peltier is a technology attribute.
- B7.1.4.06 Deodoriser: appliance made to remove odours from room air.
- B7.1.4.07 Ion generator: appliance that releases ions into room air.
- B7.1.4.08 Desiccant moisture absorber: unpowered container of desiccant that absorbs room moisture (K-11). †

### B7.1.5 Climate control
Kind axis: the control device. Display group: Thermostats and controls.
- B7.1.5.01 Thermostat: device that switches heating or cooling to hold a set temperature; smart or plain is a connectivity attribute, and a smart radiator head is filed here.

## B7.2 Water
Leaf axis: the job done to the water (heat, treat, bathe and take away waste).

### B7.2.1 Water heating
Kind axis: heater type by storage and source (rule T(b)); gas or electric is a tag. Display group: Water heating; B7.2.1.03 also displays in Heat pumps and air conditioning.
- B7.2.1.01 Storage water heater [tank water heater]: water heater that heats and holds water in its own tank.
- B7.2.1.02 Tankless water heater [instant water heater]: water heater that heats water on demand as it flows.
- B7.2.1.03 Heat-pump water heater: water heater that heats water with a compressor heat pump (C10(b), CV-24).
- B7.2.1.04 Solar water heater: system that heats household water from solar collectors.
- B7.2.1.05 Solar thermal collector: flat-plate or evacuated-tube collector sold on its own (B7-O1). †
- B7.2.1.06 Point-of-use water heater: small water heater fitted at one tap or outlet.
- B7.2.1.07 Hot-water cylinder: indirect or buffer tank heated by a boiler, with no heat source of its own (B7-O1; provisional until attested as a retail kind).

### B7.2.2 Water treatment
Kind axis: treatment technology class (C10(b), as NSF certifies them); standard met is an attribute. Display group: Water treatment.
- B7.2.2.01 Water softener: unit that removes hardness from the home supply; salt-based or salt-free is a technology attribute.
- B7.2.2.02 Plumbed water filter: filter plumbed to the supply or fitted to a tap; whole-house, under-sink, shower or tap-mounted is an installation attribute (a jug filter is B5).
- B7.2.2.03 Reverse-osmosis system: unit that purifies water through a reverse-osmosis membrane.
- B7.2.2.04 UV water treatment system: unit that disinfects water with ultraviolet light.
- B7.2.2.05 Distiller: appliance that purifies water by boiling and condensing it.

### B7.2.3 Bathing and sanitary
Kind axis: the fixture with its flush, function or body type; installation is an attribute. Display group: Baths, showers, toilets and basins; B7.2.3.08 to B7.2.3.11 display in Hot tubs and saunas.
- B7.2.3.01 Bathtub: fixed or freestanding tub for bathing in; era and material are attributes.
- B7.2.3.02 Shower: shower unit or set for washing under running water; power source is an attribute (electric shower provisional as a kind only on a ranking source).
- B7.2.3.03 Washbasin: basin for washing hands and face; sold built into its cabinet is an attribute (K-184).
- B7.2.3.04 Cistern-flush toilet [water closet]: toilet flushed by water from a cistern.
- B7.2.3.05 Waterless or composting toilet: toilet that uses no flush water, composting or storing the waste.
- B7.2.3.06 Bidet: separate low basin for washing the lower body.
- B7.2.3.07 Warm-water toilet seat [bidet seat; Washlet]: powered toilet seat with a warm-water wash (rule R, C11).
- B7.2.3.08 Hard-shell hot tub: hot tub with a moulded rigid shell and built-in heater and pumps; construction material is an attribute (B-26; provisional).
- B7.2.3.09 Inflatable hot tub: portable hot tub with an inflatable body and plug-in heater pump (B-26; provisional).
- B7.2.3.10 Wood-fired hot tub: wooden tub heated by a wood-burning stove (B-26; provisional, mapping checked at harvest).
- B7.2.3.11 Portable sauna: sauna that is set up or folded inside a home, not a cabin standing as a building (K-64). †

## B7.3 Electricity
Leaf axis: the job done to the electricity (generate, convert, store, meter).

### B7.3.1 Generation
Kind axis: collector form, or the kit sold as one object (S3a). Display group: Solar panels, inverters and batteries.
- B7.3.1.01 Solar panel: photovoltaic module that turns sunlight into electricity.
- B7.3.1.02 Plug-in balcony solar kit [Balkonkraftwerk]: panel plus micro-inverter sold as one set to plug into a home socket and feed the grid, with no storage (B-25, S3a).
- B7.3.1.03 Off-grid solar kit: panels, charge controller or inverter and usually a battery, sold as one kit to power a place without a grid connection; RV, van, boat and cabin are use tags (section 14; provisional until the kit page itself is fetched).
- B7.3.1.04 Small wind turbine: wind turbine sized to generate power for a home or site.

### B7.3.2 Conversion
Kind axis: component class; hybrid or off-grid is a type attribute. Display group: Solar panels, inverters and batteries.
- B7.3.2.01 Inverter: device that converts DC from panels or batteries to household AC.
- B7.3.2.02 Charge controller: device that regulates charging of a battery from solar panels.

### B7.3.3 Storage
Kind axis: component class; form factor (rack, wall, all-in-one, portable), chemistry and kWh are attributes. Display group: Solar panels, inverters and batteries.
- B7.3.3.01 Home battery: rechargeable battery that stores electricity for a home; the portable power station (battery and inverter in one carried box) is its portable form (K-157; provisional as a retail kind).

### B7.3.4 Metering
Kind axis: meter or monitor. Display group: not named in proposals.tsv; shown with Solar panels, inverters and batteries.
- B7.3.4.01 Energy meter or monitor: device that measures and shows a home's electricity use or generation. †

## B7.4 Parts and accessories made for one object
Leaf axis: the object served (CV-17); kinds carry `fits` (C13). Display group: Filters, salt and spare parts.

### B7.4.1 Air-treatment equipment
Kind axis: kind of part or consumable.
- B7.4.1.01 Replacement air filter: filter made to fit a purifier, humidifier or dehumidifier (S3). †

### B7.4.2 Water-treatment equipment
Kind axis: kind of part or consumable.
- B7.4.2.01 Softener salt: salt used up in a water softener (S3, K-11; dishwasher salt is B6). †
- B7.4.2.02 Replacement filter cartridge: cartridge made to fit a water filter or treatment unit (S3, K-11). †

### B7.4.3 Solar equipment
Kind axis: kind of part.
- B7.4.3.01 Solar panel mount: mounting frame or bracket made for solar panels (S3).

## Precedence inside B7

- Medium first: equipment that acts on room air is B7.1, on water B7.2, on electricity B7.3; a part or consumable made for one B7 object is B7.4.
- A heat pump is filed by the medium delivered at its output, and by that rule alone: a reversible air-to-air wall split is the wall-mounted split air conditioner (B7.1.2.01), "mini-split heat pump" its synonym and heating mode a tag; an air-to-water heat pump is the hydronic heat pump (B7.1.1.16); a ducted heat pump is the ducted or central system (B7.1.2.06); a ground-source heat pump is B7.1.1.17 whatever it delivers; a heat pump heating household water is B7.2.1.03 (B-24). Hybrid (dual-fuel) and absorption heat pumps are attributes (`heat_pump_configuration`, `heat_pump_drive`) of these kinds. The "Heat pumps and air conditioning" group is display only and moves no id.
- A combi boiler is the central-heating boiler (B7.1.1.01) with the function attribute combi, and a combi boiler pack is its unit-of-sale attribute; a hot-water cylinder heated by a boiler is B7.2.1.07.
- A purifier, fan and heater in one body (Dyson Purifier Hot+Cool) is filed by the maker's own name for it, as a named form under the air purifier (B7.1.4.01), with the other functions tagged; it is never entered under two kinds.
- A hybrid inverter with a built-in battery is a home battery (B7.3.3.01) if sold and rated by kWh storage, an inverter (B7.3.2.01) if rated by kW conversion.
- A towel radiator, or any heated rail made to warm and dry towels in a bathroom, plumbed or wired, is B7.1.1.05; a free-standing heated airer and a ceiling unit made to dry laundry are B6 (K-185).
- A wall-hung infrared panel, picture-motif prints included, is the infrared panel heater (B7.1.1.10); the radiant heater (B7.1.1.09) is the exposed-element heater; the micathermic panel is a named form of B7.1.1.10 and a print motif is a variant.
- A space heater is filed by its mechanism, fuel a tag (B7.1.1.06 to B7.1.1.10); kerosene and gas heaters with no flue are B7.1.1.13; if no fetched source ranks the flued and flueless types apart, B7.1.1.12 to B7.1.1.14 become attributes of the fan heater and radiant heater.
- A washbasin sold built into its cabinet is B7.2.3.03; a vanity cabinet sold without a basin is B1 (K-184).
- A water heater, softener or filter plumbed to the home supply, or a filter fitted to a tap, is B7 (B7.2.1, B7.2.2.01, B7.2.2.02); a kettle, instant-boiling tap, drinking-water dispenser, or jug or bottle filter is B5 (B-33).
- Softener salt and filter cartridges are B7.4.2.01 and B7.4.2.02, and a replacement air filter is B7.4.1.01 (S3, K-11); dishwasher salt and a general descaler are B6. A desiccant moisture absorber is B7.1.4.08, not a part (K-11). A washing machine or dryer is B6 even if it uses a heat pump.
- A battery and inverter in one carried box (portable power station) is the home battery (B7.3.3.01) in its portable form (K-157); a portable generator is C1, a UPS for computers D1 and a power bank D2.
- An off-grid or RV solar kit sold as one is B7.3.1.03; a kit that plugs into a home socket and feeds the grid is B7.3.1.02; a rack and a wall battery are one kind (B7.3.3.01).
- A powered hand-held or neck fan is B7.1.3.05; a manual hand fan is A4 (K-133). A ceiling fan with a light is B7.1.3.07 (branch order).
- A lamp sold as a heater is B7.1.1.11; a bulb sold as a part for a light fitting is B3.
- A smart thermostat and a smart radiator head are B7.1.5.01 by their task, not B8 because connected; a plumbed radiator valve is C8; a thermostat or heater made for an animal enclosure is B10; a carbon-monoxide alarm and a leak sensor are B8.
- Baths, showers, basins, toilets, bidets, radiators and hot tubs are B7; taps, pipes, valves, traps, waste fittings, fixed wiring, tiles, shower trays, enclosures and bath panels, and chimney and flue work, are C8 (K-186, B7-O1). Boilers, furnaces, stoves, underfloor heating kits, hot-water cylinders and solar thermal collectors are B7 (B7-O1).
- An inflatable hot tub is B7.2.3.09 while an inflatable swimming pool is C2; hot-tub equipment follows the hot tub to B7, while all swimming-pool equipment and chemicals, pool heat pumps included, are C2 (K-176). A portable sauna is B7.2.3.11; a sauna cabin that stands as a building is G2 (K-64).
- An air-quality monitor is C6 (K-147); a purifier or dehumidifier with a built-in sensor is B7.1.4. A wall-box EV charger is G1 and a vehicle or caravan heater is a part of the vehicle. A kotatsu is B1; an electric blanket, heated throw, bath mat or shower curtain is B2.
