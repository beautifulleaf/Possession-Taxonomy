import json, os
W='/home/user/Possession-Taxonomy/rebuild/work/C1/'
SW='https://en.wikipedia.org/wiki/'
PEL='https://www.sylprotec.com/en/8_3m-peltor'
kinds=[
{"n":"Safety glasses","a":"safety spectacles · safety specs · protective eyewear","d":"Eyewear made to protect the eyes from a hazard.",
 "t":["wraparound","over-glasses (OTG)","reader / bifocal","tinted or amber lenses","anti-fog coating","prescription safety"],
 "s":"https://www.discountsafetygear.com/pyramex-safety.html?page=6",
 "x":[{"n":"Uvex pheos","a":"Pheos","d":"Frameless, metal-free safety glasses with duo-spherical lenses, integrated brow guard and thin dual-material temples.","mk":"Uvex","y":"2012","s":"https://ishn.com/articles/94500-honeywell-safety-products-unveils-uvex-pheos-safety-eyewear",
   "v":[{"n":"pheos","mk":"Uvex","y":"2012","d":"Regular size"},{"n":"pheos S","mk":"Uvex","y":"2012","d":"Slim size"}],"dt":"clear, grey or amber lens · Dura-streme anti-fog/anti-scratch coating"}],
 "m":[["Intruder","Pyramex"],["Ztek IR","Pyramex"],["Emerge Full Reader","Pyramex"],["PMXTREME Reader Bifocal","Pyramex"],["Vallejo","Venture Gear"]]},
{"n":"Ear defenders","a":"earmuffs · ear protectors · hearing protectors","d":"Ear muffs made to reduce noise reaching the ears.",
 "t":["passive","electronic level-dependent","Bluetooth / radio","helmet-mounted","neckband","welding (flame-resistant)"],
 "s":"https://www.hillas.com/Categories/Peltor-Hearing-Protection/",
 "x":[
  {"n":"Peltor Optime","a":"3M Peltor Optime","d":"Peltor's passive earmuff family with liquid- or foam-filled seals, graded by attenuation.","mk":"3M","y":"","s":PEL,
   "v":[{"n":"Optime 95","mk":"3M","y":"","d":"lightest attenuation"},{"n":"Optime 98","mk":"3M","y":"","d":""},{"n":"Optime 101","mk":"3M","y":"","d":""},{"n":"Optime 105","mk":"3M","y":"","d":"highest attenuation"}],"dt":"headband, neckband or helmet attachment · colour coded by grade"},
  {"n":"Peltor ProTac","a":"3M Peltor ProTac III","d":"Peltor's electronic level-dependent earmuff that passes safe ambient sound while blocking loud noise.","mk":"3M","y":"","s":PEL,
   "v":[{"n":"ProTac III","mk":"3M","y":"","d":"active hearing protector"},{"n":"ProTac Bluetooth headset","mk":"3M","y":"","d":"with Bluetooth"}],"dt":"headband or hard-hat attached"}],
 "m":[["Venture Gear Amp BT","Pyramex"]]},
{"n":"Earplugs","a":"ear plugs","d":"Plugs worn in the ear canal to reduce noise reaching the ears.",
 "t":["disposable foam","reusable pre-moulded (flanged)","corded","banded","custom moulded"],
 "s":"https://www.hillas.com/Categories/Peltor-Hearing-Protection/",
 "m":[["Tri-Flange Cloth Corded Earplugs","3M"]]},
{"n":"Respirator","a":"dust mask · half mask · FFP mask · N95","d":"Face-worn device made to filter or supply air against dust, fumes or gas.",
 "t":["disposable filtering facepiece (FFP1–3, N95)","valved","reusable half mask","full-face mask","powered air-purifying (PAPR)","particulate, gas and vapour or combination filters"],
 "s":"https://fishersci.ca/shop/products/3m-6000-series-resuable-half-facepiece-respirators-replaceable-p100-filters-3/p-56487",
 "x":[
  {"n":"3M 6000 Series half facepiece","a":"3M 6200","d":"Reusable rubber half mask taking twin filters or cartridges on a quarter-turn bayonet.","mk":"3M","y":"","s":"https://pksafety.com/3m-6000-series-half-facepiece-respirator",
   "v":[{"n":"6100","mk":"3M","y":"","d":"small"},{"n":"6200","mk":"3M","y":"","d":"medium"},{"n":"6300","mk":"3M","y":"","d":"large"}],"dt":"filters: P100 2091, organic vapour 6001, combination 2097"},
  {"n":"3M Aura","a":"Aura 9300+ · Aura 9200","d":"Flat-fold three-panel disposable respirator that moves with the face when speaking.","mk":"3M","y":"","s":"https://dsmedical.co.uk/first-aid/infection-control/3m-9332-aura-ffp3-valved-disposable-respirator-mask/",
   "v":[{"n":"9332+","mk":"3M","y":"","d":"FFP3 with Cool Flow valve"},{"n":"Aura 9200 Series N95","mk":"3M","y":"","d":"N95 version (old data)"}],"dt":"FFP1–FFP3 or N95 · valved or unvalved"}],
 "m":[["7500 Series half mask","3M"],["North 7700 Series","Honeywell North"],["7000 Series","Moldex"]]},
{"n":"Hard hat","a":"safety helmet · construction helmet","d":"Rigid helmet made to protect the head at work from falling objects and impact.",
 "t":["cap style","full brim","climbing-style with chinstrap","vented","Type I / Type II","electrical class E, G or C"],
 "s":"https://www.discountsafetygear.com/msa-hard-hats.html",
 "x":[
  {"n":"Bullard Hard-Boiled hat","a":"Hard Boiled hat","d":"Steam-moulded canvas, glue and paint hat patented by E.W. Bullard; the first commercial hard hat.","mk":"Bullard","y":"1919","s":SW+"Hard_hat","v":[],"dt":"canvas and resin shell · later internal suspension"},
  {"n":"MSA Skullgard","a":"","d":"Non-conductive Bakelite helmet tolerating heat to 350 °F; MSA's best-known early hard hat.","mk":"MSA","y":"1930","s":SW+"Hard_hat","v":[],"dt":"cap or full brim"},
  {"n":"MSA V-Gard","a":"V-Gard","d":"MSA's polyethylene hard hat with the V-shaped crown ridge, said to be the most widely used in the US.","mk":"MSA","y":"1962","s":SW+"Hard_hat",
   "v":[{"n":"V-Gard 500","mk":"MSA","y":"","d":"vented and non-vented"},{"n":"V-Gard C1","mk":"MSA","y":"","d":""},{"n":"V-Gard H2","mk":"MSA","y":"","d":"climbing-style"}],"dt":"cap or full brim · suspension · colour"},
  {"n":"Petzl Vertex","a":"VERTEX","d":"Climbing-style work-at-height helmet with six-point textile suspension and two-position chinstrap (EN 12492 / EN 397).","mk":"Petzl","y":"","s":"https://swthingenieria.com/en/petzl-vertex-helmet/",
   "v":[{"n":"VERTEX VENT","mk":"Petzl","y":"","d":"sliding ventilation shutters"},{"n":"VERTEX HI-VIZ","mk":"Petzl","y":"","d":"fluorescent shell with reflective tape"}],"dt":"seven colours · visor and earmuff accessories"}],
 "m":[["Super-V","MSA"],["Ridgeline","Pyramex"],["SL Series Sleek 4-Point Ratchet","Pyramex"]],
 "r":[["V-Gard","MSA"]]},
{"n":"Welding helmet","a":"welding mask · welder's hood","d":"Helmet with a darkening visor made to protect the face and eyes of a welder.",
 "t":["passive (fixed shade)","auto-darkening, fixed or variable shade","grind mode","air-fed / PAPR"],
 "s":"https://www.airgas.com/Safety-Products/Head%2C-Eye-%26-Face-Protection/Welding-Helmets/Welding-Helmet---Auto-Darkening/category/422",
 "x":[
  {"n":"Speedglas","a":"3M Speedglas","d":"The first auto-darkening welding filter: an LCD shutter that darkens when sensors detect the arc, from Sweden's Hornell.","mk":"3M","y":"1981","s":SW+"Welding_helmet",
   "v":[{"n":"Speedglas RS-500","mk":"3M","y":"","d":"from the old data"},{"n":"Speedglas RS-700","mk":"3M","y":"","d":"from the old data"}],"dt":"shade range · viewing area · air-fed options"},
  {"n":"Lincoln VIKING","a":"VIKING 3350","d":"Lincoln Electric's auto-darkening helmet line; the 3350 has the line's largest view and 4C lens.","mk":"Lincoln Electric","y":"","s":"https://canadaweldingsupply.ca/products/lincoln-viking-3350-welding-helmet",
   "v":[{"n":"VIKING 3350","mk":"Lincoln Electric","y":"","d":"95 × 85 mm view, 4C lens, X6 headgear (K3034-4)"},{"n":"VIKING 2450","mk":"Lincoln Electric","y":"","d":"from the old data"}],"dt":"shell graphics · 1/1/1/1 optical class"},
  {"n":"Miller Digital Infinity","a":"","d":"Miller's top auto-darkening helmet, with weld, cut, grind and X-Mode electromagnetic arc sensing.","mk":"Miller","y":"","s":"https://weldingsuppliesfromioc.com/products/miller-digital-infinity-black-welding-helmet-w-clearlight-4x-lens-296786",
   "v":[{"n":"ClearLight 4X","mk":"Miller","y":"","d":"13.4 sq in view, shades 5–13"},{"n":"ClearLight 2.0","mk":"Miller","y":"","d":"earlier lens"}],"dt":"shell graphics · lens"}],
 "m":[["Digital Elite","Miller"],["Digital Performance","Miller"],["Sentinel A60","ESAB"],["HSL 100","Jackson Safety"]],
 "r":[["Classic Series","Miller"]]},
{"n":"Face shield","a":"visor · face guard","d":"Clear visor on a headband or hard-hat mount that protects the whole face from impact or splash.",
 "t":["polycarbonate visor","mesh (forestry)","headband-mounted","hard-hat-mounted","chin guard"],
 "s":"https://www.discountsafetygear.com/msa-hard-hats.html"}
]
brands=[
 {"n":"3M","c":"United States","f":"1902","seg":"Industrial and safety","d":"Minnesota conglomerate whose safety arm owns Peltor hearing protection, Speedglas welding filters and Aura/6000 respirators.","lines":["Peltor","Speedglas","Aura"],"sig":["Peltor Optime","Speedglas","3M 6000 Series half facepiece"],"rel":["Honeywell","MSA"],"s":SW+"3M"},
 {"n":"MSA","c":"United States","f":"1914","seg":"Safety equipment","d":"Mine Safety Appliances, founded by John T. Ryan Sr. and George Deike; now MSA Safety of Cranberry Township, Pennsylvania.","lines":["V-Gard","Skullgard"],"sig":["MSA V-Gard","MSA Skullgard"],"rel":["Bullard","3M"],"s":SW+"MSA_Safety"},
 {"n":"Bullard","c":"United States","f":"1898","seg":"Safety equipment","d":"Californian mining-equipment firm whose 1919 Hard-Boiled hat began the hard hat.","sig":["Bullard Hard-Boiled hat"],"rel":["MSA"],"s":SW+"Hard_hat"},
 {"n":"Petzl","c":"France","seg":"Climbing and work-at-height","d":"French maker of climbing and work-at-height equipment and headlamps.","sig":["Petzl Vertex"],"s":SW+"Petzl"},
 {"n":"Uvex","c":"Germany","f":"1926","seg":"Safety and sports eyewear","d":"Fürth maker of goggles and safety eyewear; sold in the Americas through Honeywell.","sig":["Uvex pheos"],"rel":["Bollé"],"s":"knowledge"},
 {"n":"Bollé","c":"France","f":"1888","seg":"Safety and sports eyewear","d":"Oyonnax eyewear maker founded by Séraphin Bollé; Bollé Safety is part of Bollé Brands.","rel":["Uvex"],"s":SW+"Boll%C3%A9_Brands"},
 {"n":"Lincoln Electric","c":"United States","f":"1895","seg":"Welding equipment","d":"Cleveland, Ohio welding-equipment maker.","lines":["VIKING"],"sig":["Lincoln VIKING"],"rel":["Miller","ESAB"],"s":"knowledge"},
 {"n":"Miller","c":"United States","f":"1929","seg":"Welding equipment","d":"Miller Electric of Appleton, Wisconsin, welding-equipment maker owned by ITW.","lines":["Digital Infinity","Digital Elite","Classic Series"],"sig":["Miller Digital Infinity"],"rel":["Lincoln Electric"],"s":"knowledge"},
 {"n":"Pyramex","c":"United States","seg":"Safety equipment","d":"US maker of budget safety glasses, hard hats and hearing protection; Venture Gear is its outdoor line.","lines":["Venture Gear"],"s":"knowledge"},
 {"n":"Honeywell","c":"United States","seg":"Industrial and safety","d":"Conglomerate whose safety division sells North respirators and Uvex eyewear in the Americas.","lines":["North","Uvex (Americas)"],"s":"knowledge"},
 {"n":"Moldex","c":"United States","seg":"Respiratory and hearing protection","d":"US maker of disposable and reusable respirators and earplugs.","s":"knowledge"},
 {"n":"ESAB","c":"Sweden","f":"1904","seg":"Welding equipment","d":"Swedish welding and cutting equipment maker.","rel":["Lincoln Electric"],"s":"knowledge"}
]
notes=("Kept all 7 planned kinds. Pyramex safety-glasses list cut from 15 models to 5 (generic 'Over-glasses (OTG)' moved to t); 'Welding earmuffs' moved to t; generic respirator and hard-hat style entries moved to t. "
 "Bollé kept as brand only: no specific Bollé model page retrieved. Left out the 3M 7500 Series as an archetype (only confirmed as a mask name on a retailer page, kept in m) and ProTac/Optime launch years (none found). "
 "The petzl.com Vertex page could not be retrieved; Vertex sourced from a distributor article. Speedglas RS-500/RS-700 (sold as 'RADNOR by 3M' in old data) recorded under maker 3M.")
out={"kinds":kinds,"brands":brands,"traditions":[],"notes":notes}
tmp=W+'shelves/10_00.json.tmp'; json.dump(out,open(tmp,'w'),ensure_ascii=False,indent=1); os.replace(tmp,W+'shelves/10_00.json')
