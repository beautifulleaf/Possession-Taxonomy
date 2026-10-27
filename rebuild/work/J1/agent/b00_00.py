import json,os
W='https://en.wikipedia.org/wiki/'
WAG=W+'Wagyu'
def X(n,d,mk,y,s,v=None,dt='',a=''):
    return {"n":n,"a":a,"d":d,"mk":mk,"y":y,"s":s,"v":v or [],"dt":dt}
KBA="Kobe Beef Marketing & Distribution Promotion Association"
kinds=[
{"n":"Japanese wagyu","a":"wagyū · washu · Japanese beef","d":"Beef from the four Japanese native cattle breeds raised in Japan, graded for yield (A–C) and meat quality (1–5).",
 "t":["Japanese Black (kuroge washu)","Japanese Brown (akage washu, akaushi)","Japanese Polled (mukaku washu)","Japanese Shorthorn (nihon tankaku washu)"],
 "s":WAG,
 "x":[
  X("Kobe beef","Tajima-strain Japanese Black heifers or steers born, fed and slaughtered in Hyōgo, certified by the Kobe Beef association.",KBA,"1983",W+"Kobe_beef",
    [{"n":"Certified Kobe beef","mk":KBA,"y":"1983","d":"BMS 6 or higher, quality score 4–5, yield A or B, carcass ≤ 499.9 kg"}],
    "grade A4/A5/B4/B5 · BMS 6–12 · cut",a="Kobe-gyu"),
  X("Matsusaka beef","Beef from Japanese Black heifers only, registered under the Matsusaka Beef Management System in Mie.","","1938 (top national medal)",W+"Matsusaka_beef",[],"10-digit traceability ID · grade · cut",a="Matsusaka-ushi"),
  X("Ōmi beef","Regional wagyu from Shiga (old Ōmi Province), counted among the three great wagyu.","","Edo period",W+"%C5%8Cmi_beef",[],"grade · cut",a="Omi beef"),
  X("Yonezawa beef","Wagyu from the Yonezawa region of Yamagata, named by the prefecture among Japan's three famous beef brands.","","",W+"Yonezawa_beef",[],"grade · cut"),
  X("Tajima beef","Beef from the Tajima region of Hyōgo, the strain behind Kobe beef.","","",WAG,[],"grade · cut"),
  X("Miyazaki beef","Japanese Black beef from Miyazaki, a frequent winner of the national Wagyu Olympics.","","",WAG,[],"grade · cut"),
  X("Kagoshima Black beef","Japanese Black beef from Kagoshima, a recent Wagyu Olympics winner.","","",WAG,[],"grade · cut"),
  X("Hida beef","Wagyu brand from Gifu Prefecture.","","",WAG,[],"grade · cut"),
  X("Kumamoto Red (akaushi)","Japanese Brown beef from Kumamoto, valued as a leaner wagyu.","","",WAG,[],"cut"),
  X("Olive wagyu","Japanese Black cattle finished on olive feed; one of the rarest wagyu types.","","",WAG,[],"grade · cut",a="olive-fed wagyu"),
 ],
 "dt":"yield grade A–C · quality grade 1–5 · BMS (marbling) · cut"},
{"n":"Wagyu outside Japan","a":"Australian wagyu · American wagyu · wagyu cross","d":"Beef from wagyu-descended herds bred outside Japan, sold as fullblood or as crossbred wagyu.",
 "t":["fullblood","purebred","crossbred (F1–F4)"],
 "s":WAG,
 "x":[
  X("Australian wagyu","Fullblood and wagyu-cross cattle farmed in Australia under the Australian Wagyu Association, the largest breed body outside Japan.","Australian Wagyu Association","",WAG,[],"fullblood or cross · marbling score · cut"),
  X("American wagyu","US wagyu, usually Japanese wagyu crossed with American breeds; USDA allows the name from 46.875% wagyu genetics.","American Wagyu Association","",WAG,
    [{"n":"Snake River Farms American Wagyu","mk":"Snake River Farms","y":"1968 (Agri Beef)","d":"Japanese wagyu × American cattle, own marbling scale; Gold Plus line"}],"cross · marbling · cut"),
  X("British wagyu","Wagyu raised in the UK from a herd imported to North Yorkshire in 2008, first eaten in 2011.","","2008",WAG,[],"cross · cut"),
 ]},
{"n":"Breed-branded beef","a":"breed beef · branded beef programme","d":"Beef sold under a breed name or a breed society's certification scheme.",
 "t":["Aberdeen Angus","Hereford","Highland","Longhorn","Charolais","Limousin"],
 "s":"https://www.beefcentral.com/news/worlds-largest-beef-brand-program-cab-a-47-year-overnight-success/",
 "x":[
  X("Certified Angus Beef","The first branded beef programme: Angus-type cattle meeting ten quality specifications, marbling first.","Certified Angus Beef","1978","https://www.beefcentral.com/news/worlds-largest-beef-brand-program-cab-a-47-year-overnight-success/",[],"modest-to-high marbling · cut",a="CAB"),
  X("Hanwoo beef","Beef from Korea's brown native Hanwoo cattle, sold as a premium product; Hoengseong is the best-known source.","","herdbook 1968",W+"Hanwoo",[],"region (e.g. Hoengseong) · cut",a="Hanu · Korean native beef"),
  X("Rubia Gallega beef","Beef from the Galician blond breed, raised mainly for meat in Lugo.","","herdbook 1933",W+"Rubia_Gallega",[],"age (ternera, añojo, vaca) · cut",a="Galician Blond"),
 ]},
{"n":"Protected-origin beef","a":"PDO beef · PGI beef · AOP beef","d":"Beef sold under an EU or UK protected designation of origin or geographical indication.",
 "t":["PDO / AOP","PGI / IGP"],
 "s":"https://dubocalalassiette.fr/blog/aop-viande-bovine/",
 "x":[
  X("Scotch Beef PGI","Protected Scottish beef marketed by Quality Meat Scotland.","Quality Meat Scotland","",W+"Scotch_beef",[],"cut"),
  X("Welsh Beef PGI","Carcases or cuts from prime cattle born and reared in Wales, guarded by Hybu Cig Cymru.","Hybu Cig Cymru","","https://assets.publishing.service.gov.uk/media/60141e4a8fa8f53fc3d79978/Product_Specification_Welsh_Beef_.pdf",[],"EUROP R or better, fat 4L or leaner · cut"),
  X("Irish Grass Fed Beef PGI","Island-of-Ireland beef from cattle with at least 90% grass feed and 220 days a year at pasture.","","2023","https://ieu-monitoring.com/editorial/eu-commission-approves-irish-grass-fed-beef-as-new-island-of-ireland-pgi/422080/",[],"cut · mince and burgers"),
  X("Ternera Gallega PGI","Galician veal and young beef, mainly Rubia Gallega, certified since 1986.","Consejo Regulador Ternera Gallega","1986","https://www.guiarepsol.com/es/comer/en-el-mercado/controles-de-la-indicacion-geografica-protegida-ternera-gallega/",
    [{"n":"Ternera Gallega Suprema","mk":"","y":"","d":"under 10 months, suckled at least 7 months"},{"n":"Ternera Gallega","mk":"","y":"","d":"under 10 months"},{"n":"Añojo","mk":"","y":"","d":"10–18 months"}],"category · cut"),
  X("Vitellone Bianco dell'Appennino Centrale PGI","Beef from pure Chianina, Marchigiana and Romagnola cattle aged 12–24 months.","","","https://www.enotecaemiliaromagna.it/en/wine-tourism/typical-products/vitellone-bianco-dellappennino-centrale-white-bullock-of-the-central-appenines-pgi",
    [{"n":"Chianina","mk":"","y":"","d":"breed mark on carcass"},{"n":"Marchigiana","mk":"","y":"","d":"breed mark on carcass"},{"n":"Romagnola","mk":"","y":"","d":"breed mark on carcass"}],"breed · cut",a="White Bullock of the Central Apennines"),
  X("Taureau de Camargue AOP","Beef from Camargue cattle raised in the Camargue; the first French beef AOP.","","1996","https://dubocalalassiette.fr/blog/aop-viande-bovine/",[],"cut"),
  X("Bœuf de Charolles AOP","Charolais beef grazed until about two years old, then finished 4–6 months and cold-aged.","","","https://dubocalalassiette.fr/blog/aop-viande-bovine/",[],"cut · ageing"),
  X("Fin Gras du Mézenc AOP","Seasonal hay-finished beef from heifers (24 months+) and steers (30 months+) of the Mézenc plateau.","","2006",W+"Fin_gras_du_M%C3%A9zenc",[],"breed (Salers, Limousin, Charolais, Aubrac) · season March–June"),
 ]},
{"n":"Dry-aged beef","a":"aged beef · hung beef","d":"Beef hung or racked in a chilled room for weeks so that moisture evaporates and enzymes tenderise it.",
 "t":["dry-aged on the bone","dry-aged in a moisture-permeable bag","wet-aged (vacuum)","koji-aged"],
 "s":W+"Beef_aging"},
]
brands=[
{"n":KBA,"c":"Japan","f":"1983","seg":"Institution & issuer","kf":"Kobe beef","d":"Body that defines and certifies the Kobe beef trademark.","lines":[],"eras":[],"sig":["Kobe beef"],"sc":[],"rel":[],"s":W+"Kobe_beef"},
{"n":"Certified Angus Beef","c":"United States","f":"1978","seg":"Institution & issuer","kf":"Angus beef","d":"Not-for-profit subsidiary of the American Angus Association that licenses the CAB mark.","lines":[],"eras":[],"sig":["Certified Angus Beef"],"sc":[],"rel":["American Angus Association"],"s":"https://www.beefcentral.com/news/worlds-largest-beef-brand-program-cab-a-47-year-overnight-success/"},
{"n":"Snake River Farms","c":"United States","f":"1968","seg":"Premium","kf":"American wagyu","d":"Idaho producer of American Wagyu beef and Kurobuta pork, part of the Agri Beef family business.","lines":["American Wagyu","Kurobuta pork","Gold Plus"],"eras":[],"sig":["American wagyu"],"sc":[],"rel":["Agri Beef"],"s":"https://snakeriverfarms.com/pages/about-us"},
{"n":"Australian Wagyu Association","c":"Australia","f":"","seg":"Institution & issuer","kf":"wagyu breed society","d":"Largest wagyu breed association outside Japan.","lines":[],"eras":[],"sig":["Australian wagyu"],"sc":[],"rel":[],"s":WAG},
{"n":"American Wagyu Association","c":"United States","f":"","seg":"Institution & issuer","kf":"wagyu registry","d":"Registry for fullblood wagyu in the United States.","lines":[],"eras":[],"sig":["American wagyu"],"sc":[],"rel":[],"s":WAG},
{"n":"Quality Meat Scotland","c":"United Kingdom","f":"","seg":"Institution & issuer","kf":"Scotch Beef PGI","d":"Body that markets the Scotch Beef and Scotch Lamb PGI brands.","lines":["Scotch Beef","Scotch Lamb"],"eras":[],"sig":["Scotch Beef PGI"],"sc":[],"rel":[],"s":W+"Scotch_beef"},
{"n":"Hybu Cig Cymru","c":"United Kingdom","f":"","seg":"Institution & issuer","kf":"Welsh Beef PGI","d":"Meat Promotion Wales, the group behind the Welsh Beef and Welsh Lamb PGIs.","lines":["Welsh Beef","Welsh Lamb"],"eras":[],"sig":["Welsh Beef PGI"],"sc":[],"rel":[],"s":"https://assets.publishing.service.gov.uk/media/60141e4a8fa8f53fc3d79978/Product_Specification_Welsh_Beef_.pdf"},
{"n":"Consejo Regulador Ternera Gallega","c":"Spain","f":"","seg":"Institution & issuer","kf":"Ternera Gallega PGI","d":"Regulatory council that certifies Ternera Gallega veal and beef.","lines":[],"eras":[],"sig":["Ternera Gallega PGI"],"sc":[],"rel":[],"s":"https://www.guiarepsol.com/es/comer/en-el-mercado/controles-de-la-indicacion-geografica-protegida-ternera-gallega/"},
]
notes=("New shelf (no old kinds). Breeds link to the C3 breeds register (Japanese Black/Brown/Polled/Shorthorn, Angus, Hereford, Rubia Gallega, Chianina etc.). "
"Left out: Ozaki beef, Mishima (native population not a brand), named Australian producers, F1–F4 producer lists, Hereford/Highland/Longhorn breed schemes as archetypes (no retrieved page this session; kept as types), Kagoshima/Hida/Miyazaki own pages (wiki 404, attested via Wagyu article), vaca vieja and tallow ageing (not on a retrieved page). Wikidata entity helper returned empty, so no Wikidata sources.")
out={"kinds":kinds,"brands":brands,"traditions":[],"notes":notes}
p='/home/user/Possession-Taxonomy/rebuild/work/J1/shelves/00_00.json'
json.dump(out,open(p+'.tmp','w'),ensure_ascii=False,indent=1); os.replace(p+'.tmp',p)
