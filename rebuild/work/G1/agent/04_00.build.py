import json, os
W='https://en.wikipedia.org/wiki/'
def v(n,mk,y,d): return {"n":n,"mk":mk,"y":y,"d":d}
transit={"n":"Ford Transit","a":"Transit","d":"Ford's large van, built since 1965 in van, minibus, chassis-cab and pickup forms; a byword for vans of its size.","mk":"Ford","y":"1965–","s":W+"Ford_Transit",
 "v":[v("Mk1","Ford","1965–1977","replaced the Thames 400E; facelift 1971"),v("Mk2","Ford","1977–1986","restyled nose, plastic dashboard"),
      v("second generation (VE6)","Ford","1986–2000","one-box body; facelifts 1992 and 1994"),v("third generation","Ford","2000–2014","front- or rear-wheel drive; International Van of the Year 2001"),
      v("fourth generation","Ford","2014–","unibody; updated 2020"),v("Transit Custom","Ford","2013–","mid-size van revealed alongside the fourth generation")],
 "dt":"wheelbase · roof height · panel van, crew van, chassis cab, Luton · engine"}
sprinter={"n":"Mercedes-Benz Sprinter","a":"Dodge Sprinter · Freightliner Sprinter","d":"Large van that replaced the Mercedes-Benz T1 in 1995 and became a common base for campervans and minibuses.","mk":"Mercedes-Benz","y":"1995–","s":W+"Mercedes-Benz_Sprinter",
 "v":[v("first generation (W903)","Mercedes-Benz","1995–2006","first Mercedes-Benz with a name rather than a code"),v("second generation (W906/NCV3)","Mercedes-Benz","2006–2018","facelift 2013–2014"),
      v("third generation (W907/W910)","Mercedes-Benz","2018–","front-wheel-drive variant; eSprinter electric"),v("Volkswagen Crafter","Volkswagen","2006–2017","rebadged twin"),
      v("Dodge Sprinter","Dodge","2003–2009","North American rebadge"),v("Freightliner Sprinter","Freightliner","2001–2021","North American rebadge")],
 "dt":"wheelbase · roof height · cargo van, crew van, chassis cab · drive layout"}
hvan={"n":"Citroën H Van","a":"Type H · HY · HZ · HX · HW","d":"French front-wheel-drive van with a corrugated steel body and low flat floor; now prized as a food truck.","mk":"Citroën","y":"1947–1981","s":W+"Citro%C3%ABn_H_Van",
 "v":[v("HY","Citroën","","most common model"),v("HP","Citroën","","pickup")],"dt":"petrol or diesel · windscreen and rear-window style · conversion (food truck, camper)"}
ducato={"n":"Fiat Ducato","a":"Peugeot Boxer · Citroën Jumper · Citroën Relay · Ram ProMaster","d":"Fiat–PSA large van, sold under several badges and the most common motorhome base in Europe.","mk":"Fiat","y":"1981–","s":W+"Fiat_Ducato",
 "v":[v("first generation","Fiat","1981–1993","twins Citroën C25, Peugeot J5, Talbot Express"),v("second generation","Fiat","1993–2006","facelift 2002"),
      v("third generation","Fiat","2006–","facelifts 2014 and 2024; electric versions")],"dt":"wheelbase · roof height · van, chassis cab, motorhome base"}
trafic={"n":"Renault Trafic","a":"Vauxhall Vivaro · Nissan Primastar · Fiat Talento","d":"Renault's mid-size van, sold in several rebadged versions.","mk":"Renault","y":"1980–","s":W+"Renault_Trafic",
 "v":[v("first generation","Renault","1980–2001",""),v("second generation (X83)","Renault","2001–2015","shared with Opel/Vauxhall and Nissan"),v("third generation (X82)","Renault","2014–","")],
 "dt":"wheelbase · roof height · van, crew van, 9-seat passenger"}
berlingo={"n":"Citroën Berlingo","a":"Peugeot Partner · Vauxhall Combo · Toyota ProAce City","d":"Small car-derived van from PSA, also sold as a passenger MPV.","mk":"Citroën","y":"1996–","s":W+"Citro%C3%ABn_Berlingo",
 "v":[v("first generation (M49)","Citroën","1996–2008","incl. Multispace passenger version"),v("second generation (B9)","Citroën","2008–2018","PSA PF2 platform"),v("third generation (K9)","Citroën","2018–","EMP2 platform")],
 "dt":"length · four or five doors · panel van or passenger"}
type2={"n":"Volkswagen Type 2","a":"Kombi · Microbus · Bulli · Transporter · Caravelle · Splitty · bay-window","d":"Volkswagen's forward-control van since 1949, iconic as the Kombi and camper; later generations sold as the Transporter.","mk":"Volkswagen","y":"1949–","s":W+"Volkswagen_Type_2",
 "v":[v("T1","Volkswagen","1950–1967","split windscreen; Samba-Bus luxury model with sunroof"),v("T2","Volkswagen","1967–1979","bay window; built in Brazil until 2013"),
      v("T3","Volkswagen","1979","boxier body; Vanagon in the US, T25 in the UK"),v("T4","Volkswagen","1990","front engine, front-wheel drive; Transporter name"),
      v("T5","Volkswagen","2003","more aerodynamic"),v("T6","Volkswagen","2015","Euro 6 diesels")],
 "dt":"panel van, Kombi, bus (Caravelle), Samba, pickup, Westfalia camper · generation · colour"}
hiace={"n":"Toyota HiAce","a":"HiAce Commuter","d":"Toyota's van and minibus, built since 1967 over six generations; widely used as a high-roof Commuter minibus.","mk":"Toyota","y":"1967–","s":W+"Toyota_HiAce",
 "v":[v("first generation (H10)","Toyota","1967–1977",""),v("second generation (H11/H20/H30/H40)","Toyota","1977–1982","high-roof Commuter"),
      v("third generation (H50–H90)","Toyota","1982–2007",""),v("fourth generation (H100)","Toyota","1989–2004","high-roof 15-seat Commuter"),
      v("fifth generation (H200)","Toyota","2004–",""),v("sixth generation (H300)","Toyota","2019–","")],
 "dt":"van, wagon, Commuter · roof height · seats"}
kinds=[
 {"n":"Panel van","a":"cargo van · delivery van · LCV","d":"Goods vehicle with an enclosed windowless load box behind the cab.","t":["small (car-derived)","medium","large","short wheelbase","long wheelbase","low roof","high roof","crew van","Luton/box van","electric"],
  "s":"https://www.vansdirect.co.uk/new-vans-in-stock","x":[transit,hvan,sprinter,ducato,trafic,berlingo],
  "m":[["Master","Renault"],["Transporter","Volkswagen"]]},
 {"n":"Window van","a":"kombi · passenger van · crew bus","d":"Van with side windows and seats or space for passengers and goods.","t":["Kombi (seats plus load space)","passenger (all seats)","day van"],
  "s":"https://autoline.com/-/passenger-vans/Ford/Transit-Custom--c83tm2566m33349","x":[type2,hiace],
  "m":[["Tourneo Custom","Ford"],["Transit Custom Kombi","Ford"],["Caravelle","Volkswagen"]]},
 {"n":"Minibus","a":"microbus · minicoach · short bus","d":"Passenger vehicle seating about 12–30, larger than a minivan but smaller than a bus.","t":["9-seat","12–17 seat","high roof","wheelchair-accessible","school/community"],
  "s":"https://www.minibus.ltd.uk/minibuses-with-sat-nav/","m":[["Trafic 9 Seat Minibus","Renault"]]}]
def B(n,c,f,d,sig): return {"n":n,"c":c,"f":f,"seg":"mass-market","d":d,"lines":[],"eras":[],"sig":sig,"sc":[],"rel":[],"s":"knowledge"}
brands=[B("Ford","United States","1903","American volume carmaker with a large European van business.",["Ford Transit"]),
 B("Mercedes-Benz","Germany","1926","German maker of cars, vans and trucks.",["Mercedes-Benz Sprinter"]),
 B("Citroën","France","1919","French volume carmaker, now part of Stellantis.",["Citroën H Van","Citroën Berlingo"]),
 B("Fiat","Italy","1899","Italian volume carmaker, now part of Stellantis.",["Fiat Ducato"]),
 B("Renault","France","1899","French volume carmaker.",["Renault Trafic"]),
 B("Volkswagen","Germany","1937","German volume carmaker, core brand of the Volkswagen Group.",["Volkswagen Type 2"]),
 B("Toyota","Japan","1937","Japanese volume carmaker.",["Toyota HiAce"])]
for b in brands:
  if b["n"]=="Mercedes-Benz": b["seg"]="premium"
out={"kinds":kinds,"brands":brands,"traditions":[],"notes":"Panel van: six archetypes from retrieved Wikipedia pages; old models Sprinter, Berlingo, Transit Custom, Trafic became archetypes/versions; Master and Transporter kept in m. Window van: VW Type 2 (Kombi) and Toyota HiAce as archetypes; old Hiace folded in; Trafic 9 Seat Minibus moved to Minibus. VW T6.1/T7 and later Transporter generations left out (not confirmed on the retrieved page). Minibus kept without archetypes (no maker-specific minibus icon confirmed beyond van-based HiAce/Sprinter). No traditions."}
p='/home/user/Possession-Taxonomy/rebuild/work/G1/shelves/04_00.json'
json.dump(out,open(p+'.tmp','w'),ensure_ascii=False,indent=1); os.replace(p+'.tmp',p)
