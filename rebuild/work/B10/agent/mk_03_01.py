import json, os
PS="https://www.petsathome.com/category/fish"
def X(n,d,mk,y,s,v=(),dt="",a=""):
    return {"n":n,"a":a,"d":d,"mk":mk,"y":y,"s":s,"v":[dict(zip(("n","mk","y","d"),t)) for t in v],"dt":dt}
FTA="https://fishtankadvisor.com/?p=3328"
fi={"n":"Aquarium filter","a":"fish tank filter","d":"A pump- or air-driven unit that passes tank water through mechanical, biological and chemical media.",
 "t":["canister filter","hang-on-back (power) filter","internal filter","corner filter","sponge filter","trickle (wet/dry) filter","fluidized bed filter","diatom filter"],
 "s":"https://en.wikipedia.org/wiki/Aquarium_filter","x":[
 X("Eheim classic canister","Sealed external canister with a magnet-driven pump, developed by Gunther Eheim from 1962 to replace air-driven filters.","EHEIM","1962","https://reefbuilders.com/2013/02/06/gunther-eheim/",
   [("Eheim classic","EHEIM","",""),("Eheim classicVARIO+e","EHEIM","","electronic variant"),("Eheim professionel 4+","EHEIM","","multi-basket successor line"),("Eheim professionel 5e","EHEIM","","electronic")],"canister with loose media · hoses and spray bar"),
 X("Fluval 07 series","Stacked-basket canister with AquaStop valve, Lift-Lock clamps and lift-out media baskets.","Fluval","","https://www.bulkreefsupply.com/fluval-307-canister-filter-fluval.html",
   [("Fluval 107","Fluval","",""),("Fluval 207","Fluval","",""),("Fluval 307","Fluval","","40–70 gal, 16 W"),("Fluval 407","Fluval","","")],"four sizes · quieter than the previous generation"),
 X("Oase BioMaster Thermo","Canister filter with removable EasyClean pre-filter and optional built-in heater.","Oase","","https://mcmerwe.co.za/shop/oase-biomaster-thermo/",
   [("BioMaster Thermo 250","Oase","","250 l"),("BioMaster Thermo 350","Oase","","350 l"),("BioMaster Thermo 600","Oase","","600 l"),("BioMaster Thermo 850","Oase","","850 l")],"with or without heater · Hel-X biomedia · made in Italy"),
 X("AquaClear","Hang-on-back power filter with adjustable flow and media in a basket, sold since 1978.","Rolf C. Hagen","1978",FTA,[("Hagen AquaClear","Rolf C. Hagen","","")],"sizes for 5–110 US gal"),
 X("Marineland Penguin Bio-Wheel","Hang-on-back filter with a rotating Bio-Wheel for biological filtration.","Marineland","",FTA,[],"cartridge plus wheel"),
 X("Seachem Tidal","Self-priming hang-on-back filter with in-tank pump, developed with Sicce.","Seachem","",FTA,[],"35–110 gal · adjustable flow"),
 X("Hikari Bacto-Surge","Air-driven sponge filter of soft polyether foam with uplift tube and diffuser.","Hikari","","https://hikariusa.com/water_quality_folder/bacto_surge_sponges.html",
   [("Bacto-Surge Mini","Hikari","","up to 10 gal"),("Bacto-Surge Small","Hikari","","up to 40 gal"),("Bacto-Surge Large","Hikari","","up to 75 gal"),("Bacto-Surge X-Large","Hikari","","up to 125 gal")],"needs an air pump"),
 ],
 "m":[["Fluval FX4","Fluval"],["Fluval FX6","Fluval"],["Eheim eXperience","EHEIM"],["Sicce Whale","Sicce"],["Tetra Whisper EX","Tetra"],["Aqueon QuietFlow LED Pro","Aqueon"],["Oase Biostyle Hang on Filter","Oase"],["Eheim aquaball","EHEIM"],["Eheim biopower","EHEIM"],["Juwel Bioflow","JUWEL Aquarium"],["Fluval U Series","Fluval"],["Sicce Shark PRO","Sicce"],["Tetratec Internal Filter Plus","Tetra"],["Aquael FAN Plus","Aquael"],["Dennerle Nano Corner Filter","Dennerle"]]}
sump={"n":"Aquarium sump","a":"","d":"A separate tank below the aquarium that holds filtration and equipment.","t":["baffle sump","refugium sump","filter-roller sump","wet/dry sump"],
 "s":"https://aquariumsupplyonline.com/product-category/filters-and-sumps/hang-on-filters/",
 "m":[["Trigger Systems Crystal Sump","Trigger Systems"],["Trigger Systems Sapphire Sump","Trigger Systems"],["Trigger Systems Ruby Sump","Trigger Systems"],["Eshopps Reef Sump RS-75","Eshopps"],["Eshopps Wet Dry Sump Filter","Eshopps"],["Bashsea Smart Series Sump","Bashsea"],["Bashsea PRO Series Filter Roller Sump","Bashsea"],["Bashsea Bio-Fuge Rimless Bio Refugium Sump","Bashsea"],["Reef Octopus OCTO Reef Sump","Reef Octopus"],["Pro Clear RedFlex Reef Sump","Pro Clear Aquatic Systems"],["Fiji Cube Advanced Reef Sump","Fiji Cube"],["Aquaforest AF Sump","Aquaforest"]]}
ug={"n":"Under-gravel filter","a":"undergravel filter · UGF","d":"A slotted plate under the gravel that draws water through it so the gravel acts as filter medium.",
 "s":"https://eorder.pennplax.com/cfu20","m":[["Lee's Premium Undergravel Filter","Lee's"],["Lee's Original Undergravel Filter","Lee's"],["Penn-Plax Cascade Undergravel Filter","Penn-Plax"],["Imagitarium Undergravel Filter","Imagitarium"]]}
med={"n":"Aquarium filter media","a":"filter foam · biomedia","d":"Foam, wool, ceramic or carbon material packed into an aquarium filter.",
 "t":["filter foam","filter wool","ceramic rings","sintered glass","bioballs","activated carbon","zeolite","replacement cartridge"],
 "s":"https://www.allpondsolutions.co.uk/aquarium/media-foams/","x":[
 X("Seachem Matrix","Porous inorganic biomedia whose macropores host nitrifying and denitrifying bacteria; never needs replacing.","Seachem","","https://www.bulkreefsupply.com/content/post/md-seachem-matrix-biofiltration-media-what-you-need-to-know",[],"for any canister, power filter, contactor or sump")],
 "m":[["Fluval AC BioMax insert","Fluval"],["Fluval FX2 Bio Foam Max","Fluval"],["Marineland Penguin Rite-Size C power filter cartridge","Marineland"],["Tetra Whisper Bio-Bag disposable cartridge","Tetra"],["Aqueon QuietFlow replacement cartridges","Aqueon"],["700IF+ ceramic ball media pack","AllPondSolutions"]]}
air={"n":"Aquarium air pump","a":"air pump","d":"A pump that blows air into an aquarium through a line and air stone.","t":["single outlet","dual outlet","battery backup","deep-water"],"s":PS,"x":[
 X("Tetra Whisper","Quiet diaphragm air pump with dome housing, sound-dampening chambers and suspended motor.","Tetra","","https://www.thatpetplace.com/whisper-40-aquarium-air-pump-40-gal",[("Whisper 40","Tetra","","up to 40 gal, one outlet")],"sizes 10–100 gal")],
 "m":[["Eheim Air Pump 400","EHEIM"],["Fluval A202 Air Pump","Fluval"],["Interpet AirVolution 3 Airpump","Aquagarden Interpet"],["Marina 200 Air Pump","Marina"],["Tetra APS300 Air Pump","Tetra"],["JBJ Maxum Battery Backup Air Pump","JBJ"]]}
wt={"n":"Aquarium water treatment","a":"water conditioner · dechlorinator","d":"A liquid or additive that conditions aquarium water (dechlorinator, bacterial starter, clarifier, algae control).",
 "t":["dechlorinator","bacterial starter","clarifier","algae control","pH buffer"],"s":"https://www.maxizoo.fr/c/aqua/","x":[
 X("Seachem Prime","Concentrated conditioner that removes chlorine and chloramine and detoxifies ammonia, nitrite and nitrate.","Seachem","","https://www.bulkreefsupply.com/prime-complete-concentrated-water-conditioner-seachem.html",[],"5 ml per 200 l · 100–500 ml bottles"),
 X("Tetra AquaSafe","Tap-water conditioner from Tetra's 1970s range.","Tetra","1970s","https://www.tetra.net/en-gb/company/history",[],"")],
 "m":[["API Stress Coat","API"],["Tetra SafeStart","Tetra"]]}
tk={"n":"Water test kit","a":"aquarium test kit","d":"A kit of reagents or strips for measuring aquarium water chemistry.","t":["liquid reagent kit","test strips","single-parameter kit","digital meter"],
 "s":"https://aquascaperoom.ca/api-freshwater-master-test-kit/","x":[
 X("API Master Test Kit","Liquid kit measuring pH, high-range pH, ammonia, nitrite and nitrate in glass tubes against a colour chart.","API","","https://aquascaperoom.ca/api-freshwater-master-test-kit/",
   [("API Freshwater Master Test Kit","API","","up to 800 tests"),("API Saltwater Master Test Kit","API","",""),("API Reef Master Test Kit","API","","")],"7 solutions · 4 tubes")],
 "m":[["Tetra EasyStrips Complete","Tetra"],["API 5-in-1 Test Strips","API"],["Aqueon 7-in-1 Test Strips","Aqueon"]]}
BRS="https://www.bulkreefsupply.com/content/post/7-stage-rodi-installation-instructions"
ro={"n":"RO/DI water unit","a":"reverse osmosis deionisation unit · RODI","d":"A home unit that purifies tap water by sediment, carbon, reverse-osmosis membrane and deionising resin for reef tanks.",
 "t":["RO only","4-stage","5-stage","6-stage","7-stage"],"s":BRS,"x":[
 X("BRS RO/DI system","Bracket-mounted multi-stage RO/DI unit sold by stage count, with triple DI on the top models.","Bulk Reef Supply","",BRS,
   [("BRS 7 Stage Deluxe Plus","Bulk Reef Supply","","1 sediment, 2 carbon, 1 membrane, 3 DI"),("BRS 7 Stage Pro Plus","Bulk Reef Supply","",""),("BRS 4 Stage RO/DI","Bulk Reef Supply","","")],"stage count · GPD rating")]}
ff={"n":"Fish food","a":"","d":"Prepared food for aquarium fish.","t":["flake","pellet","granule","wafer or tablet","frozen","freeze-dried","gel","holiday block"],"s":PS,"x":[
 X("TetraMin","Early industrially produced flake food for tropical fish, from Ulrich Baensch's Tetra.","Tetra","1950s","https://www.tetra.net/en-gb/company/history",[("TetraMin Granules","Tetra","",""),("TetraMin XL Flakes","Tetra","",""),("TetraMinPRO","Tetra","2000s","")],"flakes, granules")],
 "m":[["Hikari Micro Pellets","Hikari"],["Hikari Saki-Hikari","Hikari"],["Hikari Sinking Wafers","Hikari"],["New Life Spectrum AllGro","New Life Spectrum"],["New Life Spectrum Cichlid Formula","New Life Spectrum"],["Sera Vipan Nature","sera"],["Sera Granured Nature","sera"],["Sera FD Artemia Shrimps","sera"],["JBL ProNovo Guppy Flakes","JBL"],["JBL ProNovo Bel Grano","JBL"],["Fluval Bug Bites","Fluval"],["Tetra Holiday","Tetra"]]}
fd={"n":"Automatic fish feeder","a":"autofeeder","d":"A timed rim-mounted dispenser that drops portions of dry food into a tank.","t":["battery drum feeder","Wi-Fi feeder"],
 "s":"https://www.completeaquatics.co.uk/eheim-autofeeder-fish-feeder-4011708011508","x":[
 X("Eheim autofeeder","Programmable drum feeder for flakes, pellets and granules with a 100 ml drum and up to eight feeds a day.","EHEIM","","https://www.completeaquatics.co.uk/eheim-autofeeder-fish-feeder-4011708011508",[("Eheim autofeeder+","EHEIM","","")],"rim or open-top mount")]}
K="knowledge"
def B(n,c,f,seg,d,s,sig=()):
    return {"n":n,"c":c,"f":f,"seg":seg,"d":d,"lines":[],"eras":[],"sig":list(sig),"sc":[],"rel":[],"s":s}
brands=[
 B("EHEIM","Germany","1949","Aquarium filters and heaters","German maker founded by Gunther Eheim, inventor of its canister filter.","https://eheim.com/ca_CA/company/news/?p=1",["Eheim classic canister","Eheim autofeeder"]),
 B("Tetra","Germany","1951","Fish food and aquarium supplies","Founded by Ulrich Baensch in Hanover as Tropenhaus; owned by Spectrum Brands since 2005.","https://www.tetra.net/en-gb/company/history",["TetraMin","Tetra Whisper","Tetra AquaSafe"]),
 B("Fluval","Canada","","Aquarium equipment","Aquarium brand of Rolf C. Hagen.",K,["Fluval 07 series"]),
 B("Rolf C. Hagen","Canada","","Pet and aquarium supplies","Canadian pet-supply company behind Fluval and AquaClear.",K,["AquaClear"]),
 B("Oase","Germany","","Pond and aquarium equipment","German maker of pond and aquarium pumps and filters.",K,["Oase BioMaster Thermo"]),
 B("Marineland","USA","","Aquarium equipment","American aquarium filter and tank brand.",K,["Marineland Penguin Bio-Wheel"]),
 B("Seachem","USA","","Water care and filter media","American maker of aquarium water conditioners, media and filters.",K,["Seachem Prime","Seachem Matrix","Seachem Tidal"]),
 B("Hikari","Japan","","Fish food","Japanese fish-food brand.",K,["Hikari Bacto-Surge"]),
 B("API","USA","","Water care and test kits","Aquarium Pharmaceuticals, maker of test kits and water treatments.",K,["API Master Test Kit"]),
 B("Bulk Reef Supply","USA","","Reef equipment retailer and own brand","American reef retailer selling own-brand RO/DI units.",K,["BRS RO/DI system"]),
]
out={"kinds":[fi,sump,ug,med,air,wt,tk,ro,ff,fd],"brands":brands,"traditions":[],
 "notes":"All eight old kinds kept; RO/DI water unit and Automatic fish feeder added. Filter list cut from 69 flat models to archetypes plus 15; sump, media, air pump and food lists trimmed to market-covering brands. Pond foods (TetraPond, Sera Pond/Koi) left for the Ponds & koi shelf. API maker unified as 'API'. Left out: AquaClear model sizes and 1978 magnetic-impeller claim (snippets/single review); Seachem Matrix pumice claim (forum only); Lustar Hydro-Sponge (snippets only); Fluval FX series as an archetype (no retrieved page, kept as models); Oase BioMaster 2 generation; Eheim smart-feeding page (404). Brand founding years only where a retrieved page gave them."}
p="/home/user/Possession-Taxonomy/rebuild/work/B10/shelves/03_01.json"
json.dump(out,open(p+".tmp","w"),ensure_ascii=False,indent=1); os.replace(p+".tmp",p)
