import json,os
W='https://en.wikipedia.org/wiki/'
def B(n,c,f,seg,kf,d,s): return {"n":n,"c":c,"f":f,"seg":seg,"kf":kf,"d":d,"lines":[],"eras":[],"sig":[],"sc":[],"rel":[],"s":s}
b=[
B("Zebco","USA","","Mainstream","spincast reels","Maker of the Zebco 33 spincast reel, sold from 1954.","https://www.zebco.com/about-us/history"),
B("Mitchell Reel Company","France","","Heritage manufactory","spinning reels","Maker of the Mitchell 300 spinning reel from Cluses.",W+"Fishing_reel"),
B("Primus","Sweden","1892","Heritage manufactory","pressure stoves","Introduced the first pressurised-burner portable stove in 1892.",W+"Camping_stove"),
B("Esbit","Germany","","Specialist","solid-fuel stoves","Maker of folding hexamine-tablet stoves.",W+"Camping_stove"),
B("Kelly Kettle","Ireland","","Specialist","storm kettles","Produced the storm kettle design from the early 1900s.",W+"Kelly_Kettle"),
B("George Marris & Co","UK","","Heritage manufactory","volcano kettles","Birmingham firm that produced the Sirram Volcano Kettle in the 1920s.",W+"Kelly_Kettle"),
B("Eydon Kettle Company","UK","","Specialist","storm kettles","Sold the modified Storm Kettle from the early 1970s.",W+"Kelly_Kettle"),
B("Thermette","New Zealand","1929","Specialist","boiling kettles","Kettle registered by John Ashley Hart in 1929.",W+"Kelly_Kettle"),
B("EB","France","1950","Heritage manufactory","climbing shoes","Boot maker of Edmond Bourdonneau, who bought Pierre Allain's company in 1950.",W+"Climbing_shoe"),
B("Troll","UK","","Heritage manufactory","climbing harnesses","Climbing-equipment makers formed by Waterhouse, Seddon and Howard in the 1960s.",W+"Climbing_harness"),
B("Airtec","Germany","","Specialist","AADs","Maker of the CYPRES automatic activation device.",W+"Automatic_activation_device"),
B("Advanced Aerospace Designs","","","Specialist","AADs","Maker of the Vigil automatic activation device.",W+"Automatic_activation_device"),
B("Aviacom","","","Specialist","AADs","Maker of the Argus automatic activation device.",W+"Automatic_activation_device"),
B("FXC","","","Specialist","AADs","Maker of the Astra automatic activation device.",W+"Automatic_activation_device"),
B("BirdMan","","1999","Specialist","wingsuits","Wingsuit maker founded by Robert Pečnik and Jari Kuosma, in production from 1999.",W+"Wingsuit_flying"),
B("Campbell Brothers","USA","","Artisan & independent","bonzer surfboards","Designers of the Bonzer multi-fin surfboard.",W+"Surfboard"),
B("Beuchat","France","1953","Heritage manufactory","diving","Georges Beuchat's 1953 Pêche-Sport isothermic suit.",W+"Wetsuit"),
B("Body Glove","USA","","Mainstream","wetsuits","Company that grew from Bob and Bill Meistrell's neoprene experiments from about 1953.",W+"Wetsuit"),
B("Gul","UK","","Mainstream","wetsuits","Pioneered the one-piece steamer wetsuit in the early 1970s.",W+"Wetsuit"),
B("Poseidon","Sweden","","Premium","regulators","Regulator maker: Cyklon, Jetstream and Xstream.",W+"Diving_regulator"),
B("Uwatec","Switzerland","","Premium","dive computers","Maker of the Aladin dive computers, later part of Scubapro.",W+"Dive_computer"),
B("Lange","USA","","Specialist","plastic ski boots","Maker of Bob Lange's polyurethane plastic ski boot.",W+"Ski_boot"),
B("Henke","Switzerland","","Heritage manufactory","ski boots","Swiss factory that introduced buckle ski boots in 1956.",W+"Ski_boot"),
B("Rosemount","USA","","Specialist","ski boots","Maker of the 1965 side-entry ski boot.",W+"Ski_boot"),
B("Raichle","Switzerland","","Heritage manufactory","ski boots","Maker of the Flexon three-piece boot of 1979.",W+"Ski_boot"),
B("Rottefella","Norway","1927","Heritage manufactory","Nordic bindings","Maker of Nordic Norm, NNN and NTN bindings; first binding by Bror With in 1927.",W+"Ski_binding"),
B("Cubco","USA","","Heritage manufactory","ski bindings","Maker of the 1950 heel-and-toe binding.",W+"Ski_binding"),
B("Brunswick","USA","","Mainstream","Snurfer licence","Licensed the Snurfer in 1966.",W+"Snurfer"),
B("Winterstick","USA","1972","Specialist","early snowboards","Dimitrije Milovich's swallowtail snowboard company.",W+"Snowboard"),
B("Penny Skateboards","Australia","2010","Mainstream","plastic cruisers","Brand founded by Ben Mackay for the plastic Penny board.",W+"Penny_board"),
B("Tech Deck","","","Mainstream","toy fingerboards","Toy fingerboard brand with licensed skate graphics.",W+"Tech_Deck"),
B("Somerville International","","","Specialist","fingerboards","First to mass-produce fingerboards not made for figurines.",W+"Tech_Deck"),
B("Blackriver Ramps","Germany","1999","Premium","pro fingerboards","Founded by Martin Ehrenberger; known for parks and trucks.",W+"Tech_Deck"),
B("Flatface Fingerboards","USA","2003","Premium","fingerboards","Founded by Mike Schneider; also a US distributor of Blackriver.",W+"Tech_Deck"),
]
json.dump({"b":b},open('/home/user/Possession-Taxonomy/rebuild/out/E2B_brands.json.tmp','w'),ensure_ascii=False,indent=1)
os.replace('/home/user/Possession-Taxonomy/rebuild/out/E2B_brands.json.tmp','/home/user/Possession-Taxonomy/rebuild/out/E2B_brands.json')
print(len(b))
