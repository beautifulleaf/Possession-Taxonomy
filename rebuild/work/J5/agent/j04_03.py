from lib import *
L=W+"List_of_edible_salts"
kinds=[
{"n":"Table salt","a":"","d":"Refined, free-flowing salt of 97-99% sodium chloride, usually with an anti-caking agent.","t":["iodised","non-iodised","low-sodium (blended with potassium chloride or minerals)"],"s":W+"Salt","m":[["Saxa Fine Salt","Saxa"]]},
{"n":"Sea salt","a":"bay salt · solar salt","d":"Salt evaporated from sea water, fine or coarse; flake salt and fleur de sel are separate kinds.","t":["fine","coarse","grey (sel gris)","mineral-coloured"],"s":W+"Sea_salt",
 "x":[X("Alaea salt","Hawaiian red salt","Unrefined sea salt mixed with red iron-rich Hawaiian volcanic clay (ʻalaea).",W+"Alaea_salt",[],"brick-red colour"),
      X("Bamboo salt","jukyeom · jugyeom","Korean sea salt packed in bamboo, sealed with clay and roasted nine times, the last above 1,000 °C.",W+"Bamboo_salt",[V("Purple bamboo salt","","","Salt baked above 1,500 °C, regarded as the best")],"roasted nine times")]},
{"n":"Flake salt","a":"finishing salt","d":"Thin hollow or pyramid flakes used to finish dishes.","t":["smoked","flavoured"],"s":W+"Maldon_Sea_Salt","m":[["Maldon Sea Salt Flakes","Maldon Salt"]],
 "x":[X("Maldon Sea Salt Flakes","Maldon salt","Pyramid-shaped flakes from the Blackwater estuary at Maldon, Essex, made by evaporating brine over gas-fired brick flues.",W+"Maldon_Sea_Salt",[V("Original flakes","Maldon Salt"),V("Smoked","Maldon Salt"),V("Chilli","Maldon Salt"),V("Garlic","Maldon Salt")],"flake size · smoked and flavoured versions",mk="Maldon Salt",y="company named 1882"),
      X("Jacobsen Netarts Bay salt","","Flake sea salt harvested from Netarts Bay on the Oregon coast by Jacobsen Salt Company.",L,[],"flake",mk="Jacobsen Salt Co",y="company 2011")]},
{"n":"Fleur de sel","a":"flower of salt","d":"The fine crust of sea salt skimmed by hand from the pans.","t":["hand-raked","finishing use"],"s":W+"Fleur_de_sel","m":[["Fleur de sel de Guérande IGP",""]],
 "x":[X("Fleur de sel de Guérande","Sel de Guérande","Fleur de sel from the Guérande marshes in Brittany, the traditional French source; Guérande salt has PGI protection.",L,[],"hand-raked by paludiers",y="PGI"),
      X("Fleur de sel de Noirmoutier and Île de Ré","","Other traditional French fleur de sel sources named alongside Guérande.",W+"Fleur_de_sel",[],"Atlantic coast"),
      X("Halen Môn sea salt","Anglesey sea salt","Welsh fleur de sel from the Menai Strait, Anglesey, with Protected Designation of Origin; company founded in 1997.",W+"Halen_M%C3%B4n",[],"flaky sea salt",mk="Halen Môn",y="1997")]},
{"n":"Kosher salt","a":"","d":"Coarse, large-grained non-iodised cooking salt with flat or hollow pyramid crystals.","t":["flat crystal (Morton)","pyramid crystal (Diamond Crystal)"],"s":W+"Kosher_salt","m":[["Diamond Crystal Kosher Salt","Diamond Crystal"]],
 "x":[X("Diamond Crystal kosher salt","","Pyramid-crystal kosher salt made by evaporation (Alberger process) by Cargill in St. Clair, Michigan.",W+"Kosher_salt",[],"hollow pyramid crystal"),
      X("Morton kosher salt","","Flat-crystal kosher salt made by rolling cubic crystals; Morton Salt is based in Chicago.",W+"Kosher_salt",[],"flat plate crystal",mk="Morton Salt")]},
{"n":"Rock salt","a":"halite","d":"Mined halite sold coarse for grinders or cooking, including pink Himalayan salt and Persian blue salt.","t":["coarse","grinder","pink","blue"],"s":W+"Himalayan_salt",
 "x":[X("Himalayan pink salt","","Rock salt mined at Khewra in Pakistan's Punjab; trace minerals give pink to red tones.",W+"Himalayan_salt",[],"coarse · fine · blocks"),
      X("Persian blue salt","","Rock salt from a mine in Semnan, Iran, whose blue tint comes from how its crystals refract light.",L,[],"crystals")]},
{"n":"Black salt","a":"kala namak","d":"South Asian kiln-fired rock salt with a sulphurous, egg-like smell, key to chaat masala.","t":["lump","powder"],"s":W+"Kala_namak"},
{"n":"Smoked and flavoured salt","a":"","d":"Salt smoked over bark-free woods for up to 14 days, or blended with flavours; smoke-flavoured salt uses an additive.","t":["alder","apple","hickory","mesquite","oak","smoke-flavoured (additive)","infused"],"s":W+"Smoked_salt"},
]
brands=[
{"n":"Maldon Salt","c":"United Kingdom","f":"1882","seg":"Specialist","kf":"flake salt","d":"Maldon, Essex producer of pyramid sea salt flakes, distributed to over 60 countries.","lines":["Sea Salt Flakes","Smoked","Chilli","Garlic"],"eras":[],"sig":["Maldon Sea Salt Flakes"],"sc":[],"rel":[],"s":W+"Maldon_Sea_Salt"},
{"n":"Halen Môn","c":"United Kingdom","f":"1997","seg":"Artisan & independent","kf":"Anglesey sea salt","d":"Anglesey producer of PDO sea salt from the Menai Strait, founded by Alison and David Lea-Wilson.","lines":[],"eras":[],"sig":["Halen Môn sea salt"],"sc":[],"rel":[],"s":W+"Halen_M%C3%B4n"},
{"n":"Jacobsen Salt Co","c":"United States","f":"2011","seg":"Artisan & independent","kf":"Oregon flake salt","d":"Oregon company harvesting flake sea salt from Netarts Bay.","lines":[],"eras":[],"sig":["Jacobsen Netarts Bay salt"],"sc":[],"rel":[],"s":L},
{"n":"Morton Salt","c":"United States","f":"","seg":"Mainstream","kf":"table and kosher salt","d":"Chicago salt maker whose kosher salt has flat crystals.","lines":[],"eras":[],"sig":[],"sc":[],"rel":[],"s":W+"Kosher_salt"},
]
notes="Cornish Sea Salt, Camargue fleur de sel and Île de Ré as separate items: not on retrieved pages (Île de Ré merged with Noirmoutier as named on the fleur de sel page; Camargue left out). Low-sodium salt merged into table salt as t; rock salt kept separate from black salt. Persian blue and Jacobsen sourced to the List of edible salts. Ocean/Guérande PGI per the List of edible salts."
write("04_03",kinds,brands,[],notes)
