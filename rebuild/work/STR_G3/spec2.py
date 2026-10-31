# -*- coding: utf-8 -*-
# structure: dept -> [(shelf, [kind or (kind,[absorbed])])]
STRUCT=[
("Kitchen",[
 ("Units, worktops & sinks",[("Fitted kitchen",[]),"Kitchen cabinet","Worktop","Kitchen sink","Kitchen tap","Waste disposal unit"]),
 ("Cooking & extraction",["Range cooker","Heat-storage range cooker",("Built-in oven",["Oven"]),"Steam and combination oven","Hob","Cooker hood","Warming drawer","Built-in coffee machine"]),
 ("Cold storage & wine",["Built-in refrigerator","Built-in wine cabinet","Wine cellar"]),
]),
("Bath & wellness",[
 ("Baths & showers",[("Bathtub",["Bath panel"]),"Shower",("Shower enclosure or screen",["Shower enclosure","Bath or shower screen"]),"Shower tray","Shower wall panel","Shower filter"]),
 ("Basins, toilets & taps",["Washbasin","Bathroom vanity cabinet",("Bath and basin tap",["Tap"]),"Flush toilet",("Shower toilet and bidet seat",["Bidet seat"]),"Bidet","Waterless or composting toilet"]),
 ("Bathroom comfort & safety",["Heated towel rail","Bathroom clothes dryer","Grab bar"]),
 ("Saunas & steam rooms",["Sauna cabin","Sauna heater","Portable sauna","Steam room"]),
 ("Hot tubs & plunge pools",["Hard-shell hot tub","Inflatable hot tub","Wood-fired hot tub","Swim spa","Cold plunge tub"]),
]),
("Living & entertainment",[
 ("Fireplaces & stoves",[("Wood-burning stove",["Flued stove"]),"Pellet stove","Masonry heater",("Inset and wall-hung fire",["Flued fire"]),"Flueless fire","Fireplace surround and mantel"]),
 ("Ceiling fans & built-in media",["Ceiling fan","In-wall and in-ceiling speaker","Motorised TV lift and projection screen","Home cinema room"]),
]),
("Structure & circulation",[
 ("Doors & windows",[("Door",["Door frame"]),"Window","Roof window","Garage door","Window guard"]),
 ("Stairs & lifts",["Staircase","Stairlift","Home lift"]),
 ("Flooring",["Wood flooring","Laminate flooring","Vinyl flooring"]),
 ("Fitted storage",["Fitted wardrobe"]),
]),
("Home systems",[
 ("Heating & radiators",["Central heating boiler","Furnace","Storage heater","Panel radiator","Column radiator","Designer radiator",("Underfloor heating",["Underfloor heating kit"])]),
 ("Heat pumps & air conditioning",[("Split air conditioner",["Wall-mounted split air conditioner","Floor-standing air conditioner","Ceiling cassette air conditioner"]),"Central air conditioning system","Air-to-water heat pump","Ground-source heat pump"]),
 ("Hot water",["Storage water heater","Tankless water heater","Hot-water cylinder","Immersion heater","Heat-pump water heater","Point-of-use water heater",("Solar water heater",["Solar thermal collector"])]),
 ("Water treatment",["Water softener","Whole-house water filter","Under-sink water filter","Reverse-osmosis system","UV water treatment system",("Filter cartridges and softener salt",["Water filter cartridge","Softener salt"])]),
 ("Ventilation & central vacuum",["Ventilation unit","Extractor fan","Whole-house dehumidifier","Central vacuum system"]),
 ("Switches, sockets & wiring",[("Wall switch and dimmer",["Wall switch"]),"Wall socket","Ceiling rose","Consumer unit","Circuit breaker"]),
 ("Solar & home energy",["Solar panel","Plug-in balcony solar kit","Off-grid solar kit","Home battery","Inverter",("Solar system parts",["Charge controller","Battery-bank charger","Battery enclosure","Solar panel mount"]),"Small wind turbine"]),
 ("Smart home & controls",["Home automation system","Lighting control system","Motorised blinds and shading","Thermostat","Energy monitor","Intruder alarm system",("Door phone and video intercom",["Door phone"])]),
]),
("Outdoor & grounds",[
 ("Pools & water edges",["In-ground swimming pool","Jetty"]),
 ("Outdoor rooms & kitchens",["Pergola","Gazebo","Patio cover",("Outdoor kitchen",["Garden kitchen"])]),
 ("Decks & paving",["Decking","Patio"]),
 ("Garden buildings",["Garden shed","Summerhouse","Orangery","Garden office","Garden log cabin","Shepherd's hut","Garden bar","Workshop","Shipping container"]),
 ("Garages & shelters",["Garage","Carport","Boathouse"]),
]),
("Built-in lighting",[
 ("Built-in lighting",["Recessed downlight","Track lighting","Under-cabinet light","Step & plinth light","Cove lighting"]),
]),
]
NEW={
"Orangery":dict(a="conservatory-style garden room",d="Glazed garden building with a part-solid roof and masonry piers, used as a bright room attached to or near the house.",s="https://en.wikipedia.org/wiki/Garden_buildings",tt=[["Roof",["glazed lantern","part-solid flat roof","fully glazed"]],["Frame",["timber","aluminium","hardwood"]],["Position",["attached to house","freestanding"]]]),
"Storage heater":dict(a="night storage heater",d="Electric heater that stores off-peak heat in bricks and releases it through the day.",s="https://www.designingbuildings.co.uk/wiki/Domestic_heater",tt=[["Control",["manual output","automatic charge control","smart or app-controlled"]],["Core",["ceramic brick","high-heat-retention brick"]],["Heat release",["natural convection","fan-assisted"]]]),
"Immersion heater":dict(a="electric immersion element",d="Electric element fitted in a hot-water cylinder to heat the stored water.",s="https://www.designingbuildings.co.uk/wiki/Domestic_heater",tt=[["Fitting",["top-entry","side-entry"]],["Element length",["short (about 27 in)","standard","long"]],["Control",["single thermostat","dual element","timer or smart"]]]),
"Cove lighting":dict(a="cove light · indirect lighting",d="Concealed strip or tube light set in a ledge or recess so it washes the ceiling or wall; not a visible fitting.",s="https://en.wikipedia.org/wiki/Cove_light",tt=[["Light source",["LED strip","linear tube","fluorescent tube"]],["Light direction",["up to ceiling","down a wall","both"]],["Control",["dimmable","colour-changing","fixed"]]]),
}
DEMOTE={ # sourced archetypes that are generic descriptions: kept as models in m
"Franke stainless sink","Moen single-lever mixer","Wolf dual-fuel range","Falcon range cooker","ESSE wood-burning range cooker","Electric ESSE",
"Enamelled steel bath","Stone-resin freestanding bath","Wall-hung toilet with concealed cistern","Bidet shower","Self-contained composting toilet","Urine-diverting dry toilet",
"Single-lever mixer tap","Thermostatic shower valve","Electric shower","Digital shower","Adjustable hand shower","Rain shower head","Ladder towel rail","Swivel towel rail",
"Infrared sauna cabin","Barrel sauna","Finnish wood-stove sauna","Heat-storage stove","Infrared tent sauna","Redwood hot tub","Adam-style mantel","Bi-fold door",
"Sash window","Casement window","Sectional overhead door","Up-and-over garage door","Spiral staircase","Quick-break switch","Toggle switch","Push-button switch","Australian rocker",
"Victorian ornate cast-iron radiator","Self-contained composting toilet"}
