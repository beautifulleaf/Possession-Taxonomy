import json, os, sys
OUT = '/home/user/Possession-Taxonomy/rebuild/work/G3/shelves'
def K(n, a, d, s, t=None, m=None, r=None):
    k = {"n": n, "a": a, "d": d}
    if t: k["t"] = t
    k["s"] = s
    def cl(lst):
        o = []
        for mo, mk in lst:
            if mk and mo.startswith(mk + ' '): mo = mo[len(mk) + 1:]
            o.append([mo, mk])
        return o
    if m: k["m"] = cl(m)
    if r: k["r"] = cl(r)
    return k
J = {}
J['03_02'] = ([
 K("Wood flooring", "Real wood flooring · hardwood floor", "Solid or engineered wood boards laid as a floor.",
   "https://www.woodandbeyond.com/real-wood-flooring/shopby/product-edging:beveled/product-room:kitchen.html",
   t=["solid wood", "engineered wood", "plank", "parquet (herringbone, chevron)", "oiled finish", "lacquered finish"]),
 K("Laminate flooring", "", "Click-together boards with a printed decorative layer on a fibreboard core.",
   "https://www.wickes.co.uk/Products/Flooring/Laminate-Flooring/c/1000887",
   t=["standard", "water-resistant", "laminate parquet pattern"]),
 K("Vinyl flooring", "LVT · luxury vinyl tile", "Vinyl planks, tiles or sheet laid as a floor.",
   "https://travisperkins.co.uk/product/timber-and-sheet-materials/flooring/luxury-vinyl-flooring/c/1560000/",
   t=["click LVT", "glue-down LVT", "rigid-core plank", "sheet vinyl"]),
], "Restraint only: three kinds kept as planned, no models in the old data; construction and finish moved into types. Nothing dropped.")

J['04_03'] = ([
 K("Split air conditioner", "Mini-split heat pump · 挂机 · 柜机", "Indoor unit linked by refrigerant lines to an outdoor unit, cooling and often heating one room.",
   "https://kakaku.com/kaden/aircon", t=["wall-mounted", "floor-standing", "ceiling cassette", "cooling only", "heat-pump (reverse cycle)"],
   m=[["Urusara X", "Daikin"], ["risora", "Daikin"], ["huu", "Haier"]],
   r=[["Kirigamine", "Mitsubishi Electric"], ["Eolia", "Panasonic"], ["Shirokuma-kun", "Hitachi"], ["Daiseikai", "Toshiba"], ["ReLaLa", "Corona"]]),
 K("Central air conditioning system", "Ducted system · 中央空调", "Multi-split or ducted plant that cools, and often heats, several rooms.",
   "https://www.mitsubishicomfort.com/products/ducted-solutions", t=["ducted", "multi-split", "ducted heat pump"],
   m=[["intelli-HEAT", "Mitsubishi Electric Trane HVAC US"], ["PVA Multi-position Air Handler", "Mitsubishi Electric Trane HVAC US"],
      ["SVZ Multi-position Air Handler", "Mitsubishi Electric Trane HVAC US"], ["Low-static Horizontal-ducted Indoor Unit SEZ", "Mitsubishi Electric Trane HVAC US"]]),
 K("Air-to-water heat pump", "Hydronic heat pump", "Heat pump that takes heat from outdoor air to heat water for radiators, a floor or taps.",
   "https://www.screwfix.com/c/heating-plumbing/heat-pumps/cat14210001", t=["monobloc", "split"],
   m=[["Therma V R32 S Series", "LG"]]),
 K("Ground-source heat pump", "Geothermal heat pump", "Heat pump that draws heat from a loop buried in the ground.",
   "https://www.waterfurnace.com/residential/products/geothermal-heat-pumps/compare-units",
   t=["horizontal ground loop", "vertical borehole", "water-to-air", "water-to-water (hydronic)"],
   r=[["7 Series", "WaterFurnace"], ["5 Series", "WaterFurnace"], ["3 Series", "WaterFurnace"]]),
], "Restraint only: wall, floor-standing and ceiling-cassette splits merged into Split air conditioner (types). WaterFurnace SKU list collapsed to its 3/5/7 Series ranges. No models added beyond the old data, so brief brands without old models (Fujitsu, LG/Samsung splits, Vaillant aroTHERM, Kensa) are not listed.")

J['04_04'] = ([
 K("Storage water heater", "Tank water heater", "Water heater that heats and holds water in its own tank.",
   "https://hdsupplysolutions.com/ns/rheem", t=["electric", "gas"]),
 K("Tankless water heater", "Instant water heater · combi-style water heater", "Water heater that heats water on demand as it flows.",
   "https://www.navieninc.com/residential/water-heaters", t=["gas condensing", "gas non-condensing", "electric whole-house"],
   m=[["NPE-A2 Series", "Navien"], ["NPE-S2 Series", "Navien"], ["NPN-E Series", "Navien"], ["NHW-AE Series", "Navien"], ["CF Plus", "Stiebel Eltron"]],
   r=[["NPE and NHW tankless series", "Navien"]]),
 K("Hot-water cylinder", "", "Tank heated by a boiler or heat pump coil, with no heat source of its own.",
   "https://www.cityplumbing.co.uk/Product/Heating/Hot-Water-Cylinders/Unvented-Cylinders/c/1806005",
   t=["unvented", "vented", "indirect", "buffer"],
   m=[["Megaflo Eco", "Heatrae Sadia"], ["Stainless Lite Plus", "Gledhill"], ["Esprit", "Gledhill"], ["ThermaQ Evocyl", "Therma Q"]]),
 K("Heat-pump water heater", "", "Water heater that heats water with a compressor heat pump.",
   "https://www.navieninc.com/residential/water-heaters", t=["integrated tank", "split"],
   m=[["NWP500 Series", "Navien"]]),
 K("Point-of-use water heater", "Mini-tank water heater", "Small water heater fitted at one tap or outlet.",
   "https://www.supplyhouse.com/Bosch-ES2-5-ES2-5-Tronic-3000T-Ariston-Point-of-Use-Electric-Mini-Tank-Water-Heater",
   t=["mini tank", "instantaneous"],
   m=[["Tronic 3000T", "Bosch"], ["SHC mini tank", "Stiebel Eltron"]]),
 K("Solar water heater", "Solar thermal system", "System that heats household water from solar collectors.",
   "https://www.siliconsolar.com/product-category/solar-hot-water-heaters/thermosyphon-solar-hot-water/",
   t=["thermosiphon", "pumped", "flat-plate collector", "evacuated-tube collector", "collector sold on its own"]),
], "Restraint only: Solar thermal collector merged into Solar water heater as types. Navien SKU list trimmed to four series; ranges duplicating models dropped (point-of-use). The blank-maker model ThermoPower VTS became the thermosiphon type.")

J['04_05'] = ([
 K("Water softener", "", "Unit that removes hardness from the home water supply.",
   "https://thesolarstore.com/collections/waterdrop", t=["salt-based ion exchange", "salt-free conditioner"],
   m=[["WHR01", "Waterdrop"]]),
 K("Whole-house water filter", "Main-line filter", "Filter on the main supply that treats water for every tap and appliance.",
   "https://www.uk-water-filters.co.uk/pages/all-types-of-water-filters", t=["sediment", "carbon", "multi-stage"],
   m=[["WHF21-PG", "Waterdrop"]]),
 K("Under-sink water filter", "", "Filter under the kitchen sink, or fitted to the tap, that treats drinking water.",
   "https://www.uk-water-filters.co.uk/pages/all-types-of-water-filters", t=["under-sink", "tap-mounted"],
   m=[["TSU-W", "Waterdrop"]]),
 K("Reverse-osmosis system", "RO system", "Unit that purifies water through a reverse-osmosis membrane.",
   "https://thesolarstore.com/collections/waterdrop", t=["tankless", "with storage tank", "remineralising"],
   m=[["G3P800", "Waterdrop"], ["G3P600", "Waterdrop"], ["C1S CoreRO", "Waterdrop"]], r=[["X Series RO", "Waterdrop"]]),
 K("UV water treatment system", "", "Unit that disinfects water with ultraviolet light.",
   "https://www.freshwatersystems.com/products/viqua-s8q-pa-silver-series-uv-system-powered-by-sterilight-10-gpm",
   m=[["VH200 Cobalt Series", "Viqua"], ["S8Q-PA Silver Series", "Viqua"]]),
 K("Filter cartridges and softener salt", "Replacement filter cartridge · softener salt", "Replacement cartridges and salt used up by water filters and softeners.",
   "https://www.homedepot.com/p/Aquasana-Replacement-Post-Filter-Cartridge-for-Aquasana-Whole-House-Water-Filtration-Systems-with-a-10-in-Post-Filter-THD-PFC-35/304964828",
   t=["filter cartridge", "softener salt"],
   m=[["whole house post-filter cartridge", "Aquasana"], ["Bright & Soft", "Diamond Crystal"]]),
], "Restraint only: 'Other plumbed water filters' dissolved; WHF21-PG to Whole-house, TSU-W and tap-mounted filters to Under-sink (shower filters live in Bath & wellness, jug filters in Kitchen & Dining). Cartridges and softener salt merged into one consumables entry (dishwasher salt stays in Cleaning & Laundry).")

J['04_06'] = ([
 K("Ventilation unit", "MVHR · PIV unit", "Fan unit that ventilates a room or whole home, with or without heat recovery.",
   "https://bpcventilation.com/collections/mvhr-units",
   t=["mechanical ventilation with heat recovery (MVHR)", "positive input ventilation (PIV)", "mechanical extract ventilation (MEV)", "single-room heat recovery"],
   m=[["ComfoAir Q", "Zehnder"], ["Sentinel Kinetic", "Vent-Axia"], ["MRXBOXAB-ECO", "Nuaire"], ["Lossnay VL", "Mitsubishi Electric"],
      ["DucoBox Energy Comfort Plus", "Duco"], ["Adroit", "Airflow"], ["HRX-E HERA", "Domus"], ["NOTUS", "BSK"]],
   r=[["Sentinel", "Vent-Axia"]]),
 K("Extractor fan", "Ventilating fan", "Fan fitted to draw stale air out of a room.",
   "https://www.screwfix.com/c/heating-plumbing/extractor-fans/cat840510", t=["axial", "centrifugal", "inline", "humidistat or timer"],
   m=[["Gold Standard", "Manrose"], ["Airline", "Xpelair"]]),
 K("Whole-house dehumidifier", "", "Dehumidifier installed to treat a whole home, usually ducted.",
   "https://shop.aprilaire.com/products/aprilaire-e130-130-pint-whole-house-dehumidifier", m=[["E130", "AprilAire"]]),
 K("Central vacuum system", "Ducted vacuum", "Vacuum unit installed in a home and used through hose inlets linked by fixed piping.",
   "https://www.homedepot.com/c/ab/types-of-vacuum-cleaners/9ba683603be9fa5395fab904367448b", t=["bagged", "cyclonic", "hose and inlet kit"],
   m=[["Model 3600", "BEAM"], ["Cana-Vac Signature 790", "Cana-Vac"], ["CVS-11", "CentralVac International"]],
   r=[["Signature", "Cana-Vac"], ["CVS power units", "CentralVac International"]]),
], "Restraint only: MVHR/PIV/MEV are types of Ventilation unit; ventilation list trimmed to one model per maker (dropped HRXE-AURA, Integra Plus EC, Sentinel Econiq, Himpel); central-vacuum SKU list trimmed to one model per maker, ranges kept.")

J['04_07'] = ([
 K("Solar panel", "PV module", "Photovoltaic module that turns sunlight into electricity.",
   "https://thesolarstore.com/collections?page=4", t=["monocrystalline", "polycrystalline", "thin-film", "bifacial"]),
 K("Home battery", "", "Rechargeable battery that stores electricity for a home; a portable power station is the carried version.",
   "https://thesolarstore.com/collections?page=2", t=["AC-coupled", "DC-coupled", "plug-in balcony battery"],
   m=[["SOLIX Solarbank 3 E2700 Pro", "Anker"], ["SOLIX Solarbank 4 E5000 Pro", "Anker"], ["SolarFlow 800 Pro", "Zendure"],
      ["HiBattery 1920 AC", "Hoymiles"], ["HiBattery 4020 X", "Hoymiles"]]),
 K("Inverter", "Solar inverter · grid-tie inverter · inverter-charger", "Device that converts DC from panels or batteries to household AC.",
   "https://solarboss.ie/collections/solar-inverters", t=["string (grid-tie)", "hybrid (battery-ready)", "microinverter", "off-grid inverter-charger"],
   m=[["Primo GEN24 Plus", "Fronius"], ["Home Hub", "SolarEdge"], ["MultiPlus-II", "Victron Energy"], ["MultiPlus Compact", "Victron Energy"],
      ["Phoenix Inverter", "Victron Energy"], ["12000XP", "EG4 Electronics"], ["6000XP", "EG4 Electronics"], ["Radian", "OutBack Power"],
      ["FXR Series", "OutBack Power"], ["MS Series", "Magnum Energy"], ["Rosie", "Midnite Solar"]]),
 K("Plug-in balcony solar kit", "Balkonkraftwerk", "Panel plus micro-inverter sold as one set that plugs into a home socket and feeds the grid, with no storage.",
   "https://www.balkonstrom.com/pages/balkonkraftwerk-anbieter"),
 K("Off-grid solar kit", "", "Panels, a charge controller or inverter and usually a battery sold as one kit to power a place with no grid, such as a van, boat or cabin.",
   "https://thesolarstore.com/collections/all-solar-panel-kits", t=["cabin kit", "van or boat kit (see Vehicles)"]),
 K("Solar system parts", "Charge controller · battery enclosure · panel mount", "Charge controllers, battery-bank chargers, enclosures and mounts bought to build or extend a solar system.",
   "https://thesolarstore.com/collections/charge-controllers", t=["MPPT charge controller", "PWM charge controller", "battery-bank charger", "battery enclosure", "panel mount"],
   m=[["SmartSolar MPPT", "Victron Energy"], ["BlueSolar MPPT", "Victron Energy"], ["TriStar", "Morningstar"], ["SunSaver", "Morningstar"],
      ["FLEXmax", "OutBack Power"], ["Classic", "Midnite Solar"], ["Solar Boost", "Blue Sky Energy"], ["Chargeverter GC 48V", "EG4 Electronics"],
      ["MNBE-D Steel Battery Box Enclosure", "Midnite Solar"], ["DPW Standard Roof/Ground Mount", "Solar Rackworks"], ["Power Fab Top of Pole Mount", "Solar Rackworks"]]),
 K("Small wind turbine", "", "Wind turbine sized to generate power for a home or site.",
   "https://thesolarstore.com/collections/wind-turbines",
   m=[["Air X", "Ryse Energy"], ["Air Breeze", "Ryse Energy"], ["Air 40", "Ryse Energy"], ["Silent X", "Ryse Energy"], ["Whisper 200", "Southwest Windpower"]],
   r=[["Air", "Ryse Energy"], ["Whisper", "Southwest Windpower"]]),
], "Restraint only: Other inverters, string, hybrid, micro and off-grid inverters merged into Inverter (types); dropped VFX Series and Little Rosie as duplicates of kept lines. Charge controller, battery-bank charger, battery enclosure and panel mount merged into Solar system parts; mount SKUs trimmed. Blank-maker SunGold kit became types of Off-grid solar kit (van/boat use cross-links Vehicles G1).")

J['05_01'] = ([
 K("Garden shed", "", "A small outbuilding for tools and garden storage that a person can enter.",
   "https://www.radnoroak.co.uk/product/oak-framed-garden-shed-fs2005", t=["timber apex", "timber pent", "metal", "plastic", "oak-framed", "potting shed"],
   m=[["Overlord Potting Shed", "Dunster House"], ["Security Apex Shed", "Shire GB"], ["Atlas Shed", "Shire GB"], ["Premier", "Absco Sheds"],
      ["Space Saver", "Absco Sheds"], ["Store Prime", "Keter"], ["Stronghold", "Keter"], ["Darwin", "Keter"], ["FS2005 Garden Shed", "Radnor Oak"]],
   r=[["Overlord", "Dunster House"]]),
 K("Summerhouse", "", "A garden building for sitting and relaxing in.",
   "https://dunsterhouse.co.uk/help-centre/what-products-do-you-sell", t=["apex", "pent", "corner"],
   m=[["Vantage Modern", "Dunster House"], ["Ghostflower", "Dunster House"], ["Alnwick Summerhouse", "Shire GB"], ["Chatsworth Summerhouse", "Shire GB"],
      ["Windsor Summerhouse", "Shire GB"], ["Badminton Summerhouse", "Shire GB"]]),
 K("Garden office", "Garden room", "An insulated garden building made to work in.",
   "https://dunsterhouse.co.uk/help-centre/what-products-do-you-sell", t=["insulated timber frame", "log-walled", "panel (SIP)"],
   m=[["Dominator", "Dunster House"], ["The Aura Express", "Tiger Sheds"], ["The Delta", "Tiger Sheds"], ["The Omega", "Tiger Sheds"], ["The Stella", "Tiger Sheds"]]),
 K("Garden log cabin", "", "A log-walled garden building made as a general room or retreat, not fitted for one purpose.",
   "https://dunsterhouse.co.uk/help-centre/what-products-do-you-sell", t=["single-skin log", "insulated log", "apex", "pent"],
   m=[["Severn", "Dunster House"], ["Terminator", "Dunster House"], ["Coronet", "Dunster House"], ["Argyll Log Cabin", "Shire GB"],
      ["Sherwood Log Cabin", "Shire GB"], ["Twyford Log Cabin", "Shire GB"], ["Camelot Log Cabin", "Shire GB"]]),
 K("Shepherd's hut", "", "A small timber or tin-clad hut on wheels, made to stand in a garden or field as a room.",
   "https://www.landsale.co.uk/", t=["timber-clad", "tin-clad"]),
 K("Garden bar", "", "A garden building fitted as a bar, with a bar counter or serving hatch.",
   "https://dunsterhouse.co.uk/help-centre/what-products-do-you-sell",
   m=[["Leviathan Bar", "Dunster House"], ["Signature Garden Bar", "Keter"], ["Bar Shed", "Keter"]], r=[["Leviathan", "Dunster House"]]),
 K("Workshop", "", "A garden or outbuilding made for repair or craft work.",
   "https://dunsterhouse.co.uk/help-centre/what-products-do-you-sell",
   m=[["Demon", "Dunster House"], ["BLS004 Store/Workshop", "Radnor Oak"], ["Bison Workshop", "Shire GB"]]),
 K("Garage", "", "An enclosed building for vehicles, attached or freestanding.",
   "https://www.radnoroak.co.uk/product/oak-framed-garden-shed-fs2005", t=["attached", "detached", "timber", "oak-framed", "masonry", "steel"],
   m=[["Deore", "Dunster House"], ["The Kinsham", "Radnor Oak"], ["The Byton High Ridge", "Radnor Oak"], ["The Lucton", "Radnor Oak"]]),
 K("Carport", "", "A roofed, open-sided shelter for vehicles.",
   "https://dunsterhouse.co.uk/help-centre/what-products-do-you-sell", t=["freestanding", "lean-to"],
   m=[["Atlas Carport", "Dunster House"], ["Optima carport", "WEKA Holzbau"]]),
 K("Shipping container", "Container kept in place", "A shipping container fixed on a site as a store or room.",
   "https://bobscontainers.com/store-category/container-homes", t=["storage", "converted room"]),
 K("Boathouse", "", "A building for keeping boats, on or beside water.",
   "https://kellyyachtsales.com/boats-for-sale/boathouse-in-ladysmith"),
], "Restraint only: all eleven kinds kept. Long Shire GB, Tiger Sheds and Dunster House lists trimmed to a few models per maker (shed 26 to 9, summerhouse 17 to 6, office 17 to 5, log cabin 26 to 7, garage 8 to 4). Dropped mismatched old ranges (Overlord on Summerhouse, Leviathan on Carport). Tiny house on wheels sentence removed from Shepherd's hut (belongs elsewhere).")

jobs = sys.argv[1:] or list(J)
for j in jobs:
    kinds, notes = J[j]
    p = os.path.join(OUT, j + '.json'); tmp = p + '.tmp'
    json.dump({"kinds": kinds, "brands": [], "traditions": [], "notes": notes}, open(tmp, 'w'), ensure_ascii=False, indent=1)
    os.replace(tmp, p)
    print('wrote', p)
