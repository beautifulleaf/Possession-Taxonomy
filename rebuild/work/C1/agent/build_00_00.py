import json, os
W='https://en.wikipedia.org/wiki/'
def X(n,a,d,mk,y,s,v,dt): return {"n":n,"a":a,"d":d,"mk":mk,"y":y,"s":s,"v":[dict(zip(("n","mk","y","d"),t)) for t in v],"dt":dt}
xs=[
X("Makita 18V LXT","LXT · 18V Li-ion","Makita's 18V lithium-ion slide-pack platform, the first 18V Li-ion cordless tool battery.","Makita","2005",W+"Makita",
  [("BL1820B","Makita","","2.0Ah compact"),("BL1830B","Makita","","3.0Ah"),("BL1840B","Makita","","4.0Ah"),("BL1850B","Makita","","5.0Ah"),("BL1860B","Makita","","6.0Ah")],"18V · 2.0–6.0Ah · compact or full-size pack"),
X("Ryobi ONE+","ONE+ System · 18V ONE+","Ryobi's 18V DIY system in which every 18V battery fits every ONE+ tool; the first single-battery DIY range.","Ryobi","1996–2000","https://uk.ryobitools.eu/footer-links-en/information/celebrating-30-years/",
  [("Lithium+","Ryobi","2012","lithium battery generation"),("5.0Ah battery","Ryobi","2015","first 5.0Ah pack in the DIY market"),("High Energy","Ryobi","2018","longer-runtime packs"),("ONE+ HP","Ryobi","2021","upgraded batteries and electronics"),("EDGE","Ryobi","","premium battery line")],"18V · Ah capacity · Lithium+, High Energy, EDGE grades"),
X("Milwaukee M18","M18 · REDLITHIUM 18V","Milwaukee's 18V platform built on REDLITHIUM packs, with the M18 FUEL brushless line at the top.","Milwaukee",'2010',W+"Milwaukee_Electric_Tool",
  [("REDLITHIUM","Milwaukee","2010","lithium-ion pack launch"),("M18 FUEL","Milwaukee","2012","brushless top-tier tools on the same packs")],"18V · Ah capacity · standard, FORGE grades"),
X("Milwaukee M18 REDLITHIUM FORGE","FORGE","High-output M18 packs using pouch or tabless cells, compatible with all M18 tools.","Milwaukee","",
  "https://www.milwaukeetool.com.au/innovation/forge/",
  [("M18FB6","Milwaukee","","6.0Ah pouch-cell pack"),("M18FB8","Milwaukee","","8.0Ah tabless-cell pack"),("M18FB12","Milwaukee","","12.0Ah tabless-cell pack")],"18V · 6.0–12.0Ah · pouch or tabless cells"),
X("Milwaukee M12","M12 · sub-compact 12V","Milwaukee's sub-compact 12V platform of more than 50 tools sharing REDLITHIUM packs.","Milwaukee","","https://www.milwaukeetool.com/es/innovations/m12",
  [("M12 FUEL","Milwaukee","","brushless top tier")],"12V · Ah capacity"),
X("DeWalt 20V MAX / 18V XR","20V MAX · 18V XR · XR","DeWalt's main cordless platform, sold as 20V MAX in North America and 18V XR elsewhere (18V nominal).","DeWalt","",W+"DeWalt",
  [("DCB205G","DeWalt","","20V MAX 5Ah oil-resistant pack"),("DCB2108","DeWalt","","20V MAX XR 8.0Ah pack"),("POWERSTACK","DeWalt","2022","first platform packs built on pouch cells")],"20V MAX / 18V · Ah capacity · compact, XR, POWERSTACK"),
X("DeWalt FlexVolt","FLEXVOLT · 20V/60V MAX · 18V/54V","Hybrid DeWalt pack that switches between 20V and 60V wiring to run both 20V MAX and 60V MAX tools.","DeWalt","2016",W+"DeWalt",
  [("6.0Ah FLEXVOLT","DeWalt","","charges in 60 minutes on the DCB118"),("DCB609","DeWalt","","FLEXVOLT 20V/60V MAX 9Ah")],"20V/60V (18V/54V nominal) · Ah capacity"),
X("Makita 12V max CXT","CXT · 10.8V CXT","Makita's compact 12V slide-style pack platform, letting tool handles be shaped for grip.","Makita","2016","https://www.plumbermag.com/online_exclusives/2016/04/makita_releases_the_next_generation_12v_max_lithium_ion",
  [("2.0Ah CXT","Makita","2016","kit battery"),("BL1041B","Makita","2016","4.0Ah")],"12V max · 2.0 or 4.0Ah"),
X("Makita 40V max XGT","XGT","Makita's higher-voltage platform alongside LXT, with digital battery–tool communication.","Makita","2020",W+"Makita",
  [("BL4025","Makita","","2.5Ah"),("BL4040","Makita","","4.0Ah"),("BL4040F","Makita","","4.0Ah high power"),("BL4050F","Makita","","5.0Ah"),("BL4080F","Makita","","8.0Ah")],"40V max · 2.5–8.0Ah"),
X("Bosch 18V POWER FOR ALL","green Bosch 18V · Power for All Alliance","Bosch's green DIY 18V battery, compatible since 2007 and shared by about 100 tools from 10 brands.","Bosch","2007","https://www.bosch-diy.com/au/en/landing/power-for-all/power-for-all",
  [],"18V · 1.5–6.0Ah · partner brands include Gardena, Husqvarna, Gloria, Wagner, Rapid, Steinel"),
X("Bosch AMPShare","AMPShare – Powered by Bosch · Bosch Professional 18V","Multi-brand alliance built on the blue Bosch Professional 18V battery, founded with Fein and Rothenberger.","Bosch","2022","https://pressroom.boschtools.com/AMPShare",
  [("CORE18V","Bosch","","high-output pack with COOLPACK 2.0 heat management"),("AMPShare launch, US and Canada","Bosch","2023","after the EU launch in 2022")],"18V · Ah capacity · partner brands include Fein, Rothenberger, Steinel, Wagner"),
X("Metabo CAS","Cordless Alliance System · LiHD","Metabo-led 18V multi-brand battery alliance; nine makers at launch.","Metabo","2018","https://www.torque-expo.com/node/17961",
  [("LiHD","Metabo","2018","2nd-generation high-output 18V pack")],"18V · Ah capacity · partners incl. Rothenberger, Mafell, Eisenblätter, Collomix, Haaga, Starmix, Eibenstock, Steinel"),
X("Festool 18V","BP 18 Li","Festool's 18V pack system, with Bluetooth packs that switch a mobile dust extractor on and off.","Festool","","https://www.festool.com/press/product-news/bt-batteries",
  [("BP 18 Li 5.2 ASI","Festool","","5.2Ah"),("BP 18 Li 6.2 ASI","Festool","","6.2Ah"),("BP 18 Li 3.1 Ergo-I","Festool","2019","Bluetooth pack shaped into compact sanders"),("BP 18 Li 3.1 CI","Festool","2019","400 g compact Bluetooth pack")],"18V · 3.1–6.2Ah · Bluetooth or plain"),
X("Hilti Nuron","Nuron 22V","Hilti's single 22V platform for all its cordless tools, launched with 70 tools; packs log usage data.","Hilti","2022","https://www.enr.com/articles/53413-hilti-standardizes-cordless-tools-on-nuron-its-new-22v-battery-platform",
  [],"22V · Ah capacity · twin-pack heavy tools"),
X("Einhell Power X-Change","PXC","Einhell's shared DIY battery platform covering more than 350 tools.","Einhell","","https://einhell.com/press-portal/story-50c0b851ef",
  [],"Ah capacity"),
X("RIDGID 18V","RIDGID cordless","RIDGID-branded 18V cordless line, its power tools made largely by TTI.","Ridgid","",W+"Ridgid",[],"18V · Ah capacity"),
X("EGO 56V ARC Lithium","EGO Power+","56V arc-shaped garden-tool battery with phase-change cooling, interchangeable across EGO's cordless range.","EGO","","https://egopowerplus.co.uk/about-ego/technology",
  [("2.5Ah","EGO","","about 30-minute rapid charge")],"56V · Ah capacity"),
]
kinds=[
{"n":"Tool battery","a":"battery pack · power tool battery","d":"Rechargeable pack made for one maker's cordless tool platform; packs fit only that platform's tools.",
 "t":["compact","high-capacity","high-output (pouch or tabless cells)","Bluetooth / connected"],
 "s":"https://www.toolnut.com/collections/makita-18v-max-lxt-batteries","x":xs},
{"n":"Battery charger","a":"charger","d":"Charger made for a maker's cordless tool platform.",
 "t":["standard","rapid / fast (fan-cooled)","dual-port / multi-bay","charging case","vehicle (12V outlet)"],
 "s":"https://www.toolnut.com/collections/makita-18v-max-lxt-batteries",
 "m":[["DC18RC","Makita"],["DC40RA","Makita"],["DCB118","DeWalt"],["M18DBSC","Milwaukee"]]},
]
K="knowledge"
def B(n,c,f,seg,d,lines,sig,rel,s): return {"n":n,"c":c,"f":f,"seg":seg,"d":d,"lines":lines,"sig":sig,"rel":rel,"s":s}
brands=[
B("Makita","Japan","1915","Professional power tools","Japanese power-tool maker based in Anjō.",["18V LXT","40V max XGT","12V max CXT"],["Makita 18V LXT","Makita 40V max XGT"],[],W+"Makita"),
B("Ryobi","Japan","1943","DIY power tools","Japanese-origin brand; its power tools are made under licence by TTI.",["ONE+","ONE+ HP"],["Ryobi ONE+"],["Milwaukee","Ridgid"],W+"Ryobi"),
B("Milwaukee","United States","1924","Professional power tools","Brookfield, Wisconsin tool maker owned by TTI since 2005.",["M18","M18 FUEL","M12","MX FUEL"],["Milwaukee M18","Milwaukee M12"],["Ryobi"],W+"Milwaukee_Electric_Tool"),
B("DeWalt","United States","1924","Professional power tools","Stanley Black & Decker's professional power-tool brand, based in Towson, Maryland.",["20V MAX / 18V XR","FLEXVOLT","POWERSTACK"],["DeWalt 20V MAX / 18V XR","DeWalt FlexVolt"],[],W+"DeWalt"),
B("Bosch","Germany","1886","DIY (green) and professional (blue) power tools","German group whose power-tool division sells green DIY and blue Professional lines.",["18V POWER FOR ALL","AMPShare"],["Bosch 18V POWER FOR ALL","Bosch AMPShare"],["Fein"],K),
B("Metabo","Germany","1924","Professional power tools","German power-tool maker from Nürtingen, initiator of the CAS alliance.",["CAS 18V","LiHD"],["Metabo CAS"],[],K),
B("Festool","Germany","1925","Premium woodworking power tools","German maker of system-based premium tools for woodworkers.",["18V"],["Festool 18V"],[],K),
B("Hilti","Liechtenstein","1941","Construction tools","Liechtenstein maker of construction tools sold direct.",["Nuron"],["Hilti Nuron"],[],K),
B("Einhell","Germany","1964","DIY power and garden tools","German DIY tool maker based in Landau/Isar.",["Power X-Change"],["Einhell Power X-Change"],[],"https://einhell.com/press-portal/story-50c0b851ef"),
B("Ridgid","United States","1923","Pipe tools; DIY–pro power tools","Emerson-owned US tool brand from Ohio whose power tools are made largely by TTI.",["18V"],["RIDGID 18V"],["Ryobi","Milwaukee"],W+"Ridgid"),
B("EGO","China","","Cordless garden tools","Cordless outdoor power equipment brand built on a 56V battery.",["56V ARC Lithium"],["EGO 56V ARC Lithium"],[],"https://egopowerplus.co.uk/about-ego/technology"),
]
notes=("Platforms are archetypes of Tool battery; versions are generations or pack models from retrieved pages only. Left out: Makita DC18RD, DC18SF, DC18SE charger SKUs "
 "(kept as charger types dual-port / multi-bay / vehicle, one model per platform); platform ranges repeated in other power-tool kinds (live here and in the brand register). "
 "Not added for lack of a retrievable source: Makita 80V, Milwaukee MX FUEL, DeWalt Atomic/12V, Einhell 36V twin-pack, Ridgid OCTANE, Metabo/Hilti pack models, Forge launch years. "
 "Some partner pages (forconstructionpros, protoolreviews) blocked fetches and were not used. EGO founding year/country left from knowledge (country only).")
out={"kinds":kinds,"brands":brands,"traditions":[],"notes":notes}
p='/home/user/Possession-Taxonomy/rebuild/work/C1/shelves/00_00.json'
json.dump(out,open(p+'.tmp','w'),ensure_ascii=False,indent=1); os.replace(p+'.tmp',p)
