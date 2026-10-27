import json,os
W="https://en.wikipedia.org/wiki/"
def A(n,d,s,mk="",y="",dt="",a="",v=None):
    x={"n":n,"a":a,"d":d,"mk":mk,"y":y,"s":s,"dt":dt}
    if v: x["v"]=v
    return x
K=[
{"n":"Lobster","a":"Homarus · clawed lobster · lobster tails","d":"Whole clawed lobster, American or European, sold live, cooked or as frozen tails.","t":["American lobster","European lobster","live","cooked","tails","hard-shell","soft-shell"],"s":"https://www.weee.com/en/grocery-near-me/lang-en/explore/lobster",
 "x":[
 A("Maine lobster","American lobster Homarus americanus from the Gulf of Maine and Atlantic Canada, taken in traps and sold live.",W+"American_lobster",dt="hard-shell or soft-shell · Maine landing limits",a="Atlantic lobster · northern lobster · Canadian Reds"),
 A("Brittany blue lobster","European lobster Homarus gammarus, blue in life, sold as homard bleu or homard breton.","https://www.fishipedia.fr/crustacea/homarus-gammarus",dt="25 to 65 cm · deep blue shell",a="homard bleu · homard breton"),
 A("Eastern Scheldt lobster","Lobster of the isolated Eastern Scheldt estuary in Zeeland, said to have DNA distinct from other European lobsters.","https://kivi.nl/en/communities/regional-divisions/zeeland/activities/oosterschelde-and-the-osterschelde-lobster",dt="Zeeland, Netherlands · salty with a sweeter aftertaste",a="Oosterschelde kreeft · Zeeuwse kreeft")
 ]},
{"n":"Spiny lobster","a":"rock lobster · langouste · langosta · crayfish (Australia) · Palinuridae","d":"Clawless warm-water lobsters whose tails are the main retail form, sold frozen or live.","t":["tails","whole","live","frozen","cooked"],"s":W+"Spiny_lobster",
 "x":[A("Western Australian rock lobster","Panulirus cygnus, basis of Australia's most valuable fishery, MSC-certified, fished from Hamelin Bay to North West Cape.",W+"Panulirus_cygnus",dt="catch 8,000 to 15,000 tonnes",a="western rock lobster · Panulirus cygnus")],
 "m":[["Banco Chinchorro and Sian Ka’an Spiny Lobster",""]]},
{"n":"Langoustine","a":"Norway lobster · Dublin Bay prawn · scampi · Nephrops norvegicus","d":"Small clawed lobster Nephrops norvegicus, sold whole or as tails.","t":["whole","tails","raw","cooked","frozen"],"s":"https://www.thefishsociety.co.uk/collections/langoustine",
 "x":[A("Creel-caught langoustine","Langoustine taken in traps rather than trawls, priced three to four times higher according to Wikipedia.",W+"Nephrops_norvegicus",dt="live or tails")]},
{"n":"King crab","a":"Alaskan king crab · red king crab · Paralithodes camtschaticus","d":"King crab legs and clusters, usually sold cooked and frozen.","t":["legs","clusters","red","brown","golden"],"s":"https://www.alaskankingcrab.com/collections/all-products",
 "x":[A("Red king crab","Largest and most coveted king crab, fished in the Bering Sea and introduced to the Barents Sea by the Soviet Union in the 1960s.",W+"Red_king_crab",dt="Alaska and Norway · named for colour when cooked",a="Alaskan red king crab · Norwegian king crab · tarabagani")]},
{"n":"Snow crab","a":"Chionoecetes opilio · opilio · zuwaigani · matsubagani","d":"Snow crab legs, clusters and claws.","t":["legs","clusters","claws","whole"],"s":"https://www.alaskankingcrab.com/collections/all-products",
 "x":[
 A("Echizen-gani","Snow crab landed live at Fukui Prefecture ports; Japanese GI no. 69, with a yellow origin tag used since 1997.","https://www.maff.go.jp/e/policies/intel/gi_act/register/s69.html",dt="male crabs · Fukui · boiled or live",a="Echizen crab · 越前がに"),
 A("Matsuba-gani","Snow crab of Tottori and Shimane in the San'in region, name meaning pine needles for the slender legs.","https://www.nippon.com/en/japan-topics/b01732/",dt="male crabs · season opens 6 November · origin and quality tags",a="松葉ガニ")
 ]},
{"n":"Brown crab","a":"edible crab · Cancer pagurus","d":"Edible crab sold whole, or as white and brown meat.","t":["whole","dressed","white meat","brown meat","cock","hen"],"s":"https://www.weee.com/en/grocery-near-me/lang-en/explore/dungeness-crab",
 "x":[A("British Isles brown crab","Cancer pagurus from the largest crab fishery in Western Europe, mostly exported live to France and Spain.",W+"Cancer_pagurus",dt="cock sweeter and whiter · hen richer brown meat")]},
{"n":"Dungeness crab","a":"Metacarcinus magister","d":"Dungeness crab whole, in clusters or as legs.","t":["whole","clusters","legs","cooked","live"],"s":"https://www.alaskankingcrab.com/collections/all-products",
 "x":[A("Pacific coast Dungeness crab","West-coast North American crab fished in baited pots from the Aleutians to Point Conception.",W+"Dungeness_crab",dt="season from November or December · males only in most areas")]},
{"n":"Blue crab","a":"Callinectes sapidus · soft-shell crab · peeler","d":"Blue crab live, steamed, soft-shell or as picked meat.","t":["live","steamed","soft-shell","peeler","picked meat"],"s":"https://theshrimpnet.com/crabs",
 "x":[A("Chesapeake blue crab","Blue crab of Chesapeake Bay, its most valuable fishery, sold hard or as soft-shell after moulting.","https://www.fisheries.noaa.gov/species/blue-crab",dt="peeler, buster, soft-shell moult stages",a="Maryland blue crab")]},
{"n":"Chinese mitten crab","a":"hairy crab · dazhaxie · 大闸蟹 · Eriocheir sinensis","d":"Autumn freshwater crab prized for its roe, sold live and tied.","t":["live","male","female","roe"],"s":W+"Chinese_mitten_crab",
 "x":[A("Yangcheng Lake hairy crab","Prized Yangcheng Lake crabs with sweeter meat; around 3,000 tonnes harvested in 2012 against over 100,000 tonnes sold under the name.",W+"Chinese_mitten_crab",dt="female roe ripens in the ninth lunar month, male in the tenth · laser tags against fakes",a="阳澄湖大闸蟹")],
 "m":[["七里海河蟹 GI",""]]},
{"n":"Mud crab","a":"Scylla serrata · green mud crab · mangrove crab","d":"Large mangrove crab sold live in Asia and Australia.","t":["live","male","female","cooked"],"s":"https://marinewaters.fish.wa.gov.au/resource/fact-sheet-green-mud-crab/"},
{"n":"Stone crab","a":"stone crab claws · Menippe mercenaria","d":"Stone crab claws.","t":["medium","large","jumbo","colossal","cooked","frozen"],"s":"https://www.alaskankingcrab.com/collections/all-products",
 "x":[A("Florida stone crab claws","Claws removed from live crabs which are returned to sea; harvest runs 15 October to 15 May.",W+"Florida_stone_crab",dt="sold medium, large, jumbo, colossal",v=[{"n":"Medium","mk":"","y":"","d":"size grade"},{"n":"Large","mk":"","y":"","d":"size grade"},{"n":"Jumbo","mk":"","y":"","d":"size grade"},{"n":"Colossal","mk":"","y":"","d":"size grade"}])]},
{"n":"Crayfish","a":"crawfish","d":"Freshwater crayfish (Procambarus, Astacus and relatives) sold whole or as tail meat.","t":["whole","tail meat","live","cooked","frozen"],"s":"https://www.weee.com/en/grocery-near-me/lang-en/explore/frozen-crawfish-tails"},
{"n":"Squat lobster","a":"langostino","d":"Squat lobster (Munida, Pleuroncodes, Cervimunida) sold as langostino tails, raw or cooked.","t":["tails","raw","cooked"],"s":"https://www.seafoodwatch.org/globalassets/sfw/pdf/whats-new/seafood-watch-complete-recommendation-list.pdf"}
]
out={"kinds":K,"brands":[],"traditions":[],"notes":"Lobster tails folded into Lobster as a type; Other crab renamed Brown crab; Banco Chinchorro spiny lobster moved to Spiny lobster and Qilihai GI crab to Chinese mitten crab (kept as flat models, no retrieved page). Added new kinds Spiny lobster, Chinese mitten crab, Mud crab. No archetypes for Crayfish, Squat lobster, Mud crab (no sourced named origins). Western Australian rock lobster used instead of other origins; Maine/Brittany/Scheldt sourced from Wikipedia, fishipedia and KIVI. No brand entries."}
p='work/J2/shelves/01_01.json'
json.dump(out,open(p+'.tmp','w'),ensure_ascii=False,indent=1);os.replace(p+'.tmp',p)
