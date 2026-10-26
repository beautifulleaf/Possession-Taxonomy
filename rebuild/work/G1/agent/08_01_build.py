import json, os
W='https://en.wikipedia.org/wiki/'
AS='Alexander Schleicher'; SH='Schempp-Hirth'; CB='Cameron Balloons'
def X(n,a,d,mk,y,s,v,dt): return {"n":n,"a":a,"d":d,"mk":mk,"y":y,"s":s,"v":[{"n":a1,"mk":b,"y":c,"d":e} for a1,b,c,e in v],"dt":dt}
glider={"n":"Glider","a":"sailplane","d":"Unpowered fixed-wing aircraft that flies by soaring.",
 "t":["Standard Class","15-metre Class","18-metre Class","Open Class","Club Class","two-seater","vintage wooden"],
 "s":"https://www.schempp-hirth.com/en/sailplanes","x":[
 X("ASK 21","","Glassfibre two-seat trainer for first solo, cross-country and aerobatic training; over 1,000 built.",AS,"1979",W+"Schleicher_ASK_21",
   [("ASK 21",AS,"1979","original"),("ASK 21 Mi",AS,"2004","self-launching, retractable rotary engine"),("ASK 21B",AS,"2018","automatic control connections, revised canopy")],"tandem seating · club livery · instruments"),
 X("L-13 Blaník","Blanik · TG-10","Czechoslovak two-seat trainer; more than 2,650 built from 1958 to 1978.","Let Kunovice","1956",W+"LET_L-13_Blaník",
   [("L-13",'Let Kunovice',"1956","original"),("L-13 AC","Let Kunovice","","aerobatic, L-23 wings"),("L-13 A1","","","Llewellyn life-extension modification"),("L-13 Vivat","Aerotechnik","","side-by-side touring motor-glider derivative")],"airframe life status · instruments"),
 X("Discus","","Standard Class single-seater designed by Klaus Holighaus.",SH,"1984",W+"Schempp-Hirth_Discus",
   [("Discus a",SH,"","small cockpit"),("Discus b",SH,"","standard production"),("Discus bT",SH,"","sustainer motor"),("Discus CS",SH,"","licence-built in the Czech Republic"),("Discus-2",SH,"","successor")],"span · winglets · water ballast"),
 X("Ventus","","Flapped 15-metre racing single-seater by Klaus Holighaus; about 613 built 1980–1994.",SH,"1980",W+"Schempp-Hirth_Ventus",
   [("Ventus A",SH,"","narrow cockpit"),("Ventus B",SH,"","larger cockpit"),("Ventus C",SH,"","17.6 m tips, separate airbrakes"),("Ventus CT / CM",SH,"","sustainer / self-launching"),("Ventus 2",SH,"1995","replacement"),("Ventus 3",SH,"","current")],"span 15–18 m · motor option"),
 X("Nimbus","HS-3","Long-span Open Class sailplane family.",SH,"1969",W+"Schempp-Hirth_Nimbus",
   [("Nimbus (HS-3)",SH,"1969","original"),("Nimbus-2",SH,"","production version"),("Mini-Nimbus",SH,"",""),("Nimbus-3",SH,"",""),("Nimbus-4",SH,"","")],"span · single or two-seat · motor option"),
 X("Duo Discus","","Tandem two-seat sailplane for training and cross-country flying.",SH,"1993",W+"Schempp-Hirth_Duo_Discus",
   [("Duo Discus",SH,"1993","original"),("Duo Discus X",SH,"2005","winglets, revised undercarriage"),("Duo Discus XL",SH,"","10 cm longer cockpit"),("Duo Discus XLT",SH,"","sustainer motor")],"winglets · motor option"),
 X("Arcus","","Flapped 20 m two-seater sharing its fuselage with the Duo Discus XL.",SH,"2009",W+"Schempp-Hirth_Arcus",
   [("Arcus",SH,"2009","pure glider"),("Arcus T",SH,"","sustainer"),("Arcus M",SH,"","self-launching"),("Arcus E",SH,"","electric self-launch")],"engine option"),
 X("ASG 29","ASW 27-18","15/18 m flapped racing single-seater refined from the ASW 27, later replaced by the AS 33.",AS,"2005",W+"Schleicher_ASG_29",
   [("ASG 29",AS,"2005","pure glider"),("ASG 29 E",AS,"2008","SOLO 2350 sustainer")],"15 or 18 m span · sustainer"),
 X("ASW 28","","Standard Class single-seater that replaced the ASW 24.",AS,"2000",W+"Schleicher_ASW_28",
   [("ASW 28",AS,"2000","15 m"),("ASW 28-18",AS,"","15 or 18 m"),("ASW 28-18 E",AS,"","sustainer")],"span · sustainer"),
 X("DG-1000","DG-1001 · TG-16A","Two-seat 18/20 m trainer and cross-country sailplane from Bruchsal.","DG Flugzeugbau","2000",W+"Glaser-Dirks_DG-1000",
   [("DG-1000S","DG Flugzeugbau","","unpowered"),("DG-1000T","DG Flugzeugbau","","retractable sustainer"),("DG-1001","DG Flugzeugbau","","electric gear retraction"),("DG-1001e neo","DG Flugzeugbau","2020","front electric sustainer")],"span · engine option"),
 X("Grob Astir","G102 · Speed Astir","Glassfibre Club Class single-seater; over 1,240 built.","Grob Aircraft","1974",W+"Grob_G102_Astir",
   [("Astir CS","Grob Aircraft","1975","536 built"),("Astir CS77","Grob Aircraft","1977","revised fuselage"),("Astir CS Jeans","Grob Aircraft","","fixed wheel, Club Class"),("Club / Standard Astir III","Grob Aircraft","","early 1980s"),("Speed Astir (G104)","Grob Aircraft","","flapped")],"variant · gear"),
 X("Ka 8","K 8","Rudolf Kaiser's single-seat club trainer; over 1,100 built.",AS,"1957",W+"Schleicher_Ka_8",
   [("K 8",AS,"1957","small canopy"),("K 8B",AS,"","blown canopy, most numerous"),("K 8C",AS,"","longer nose, bigger wheel")],"canopy · restoration"),
 X("Slingsby T.21","Sedbergh","Open-cockpit side-by-side trainer flown by clubs and RAF air cadets.","Slingsby Aviation","1944",W+"Slingsby_T.21",
   [("T.21B","Slingsby Aviation","1947","production; RAF Sedbergh TX.1")],"restoration · open cockpit"),
 X("Schweizer 1-26","SGS 1-26","American one-design single-seater with its own racing class; 700 built.","Schweizer Aircraft","1954",W+"Schweizer_SGS_1-26",
   [("1-26",'Schweizer Aircraft',"1954","steel tube, 22 built"),("1-26A","Schweizer Aircraft","","owner-built kit"),("1-26B","Schweizer Aircraft","1956","metal-covered wings"),("1-26D","Schweizer Aircraft","1968","monocoque nose"),("1-26E","Schweizer Aircraft","1971","all-metal monocoque")],"factory or kit-built · tail shape")],
 "m":[["AS 33",AS]]}
motor={"n":"Motor-glider","a":"self-launching sailplane · touring motor glider · TMG","d":"Glider with an engine for take-off or sustaining flight.",
 "t":["self-launching","sustainer (turbo)","touring motor glider","electric","front electric sustainer"],
 "s":"https://wingsandwheels.com/pipistrel-taurus-5031396970372.html","x":[
 X("Scheibe Falke","SF 25","Side-by-side touring motor glider developed from the Bergfalke; over 1,200 built.","Scheibe Flugzeugbau","1963",W+"Scheibe_SF_25_Falke",
   [("SF-25A Motor Falke","Scheibe Flugzeugbau","1963","56 built"),("SF-25B Falke","Scheibe Flugzeugbau","","Stamo engine, 372 built"),("SF-25C Falke","Scheibe Flugzeugbau","","electric starter"),("SF-25E Super Falke","Scheibe Flugzeugbau","1974","extended wing")],"engine · canopy"),
 X("Grob G 109","Vigilant","Glassfibre side-by-side self-launching touring motor glider; 476 built.","Grob Aircraft","1980",W+"Grob_G_109",
   [("G 109A","Grob Aircraft","1980","Limbach engine"),("G 109B","Grob Aircraft","1984","longer span, Grob engine"),("Vigilant T1","Grob Aircraft","1991","RAF cadet version")],"engine"),
 X("Stemme S10","TG-11A","Side-by-side self-launching motor glider with a nose propeller that folds away in flight.","Stemme","1986",W+"Stemme_S10",
   [("S10","Stemme","1986","standard"),("S10V","Stemme","","variable-pitch propeller"),("S10-VT","Stemme","","turbocharged Rotax 914")],"engine · propeller"),
 X("Pipistrel Taurus","","Slovenian side-by-side self-launching glider, built with piston or electric power.","Pipistrel","2004",W+"Pipistrel_Taurus",
   [("Taurus M","Pipistrel","2004","Rotax 503 pop-up engine"),("Taurus PureGlider","Pipistrel","2006","unpowered"),("Taurus Electro G2","Pipistrel","2011","40 kW electric")],"power unit"),
 X("Lange Antares","","18–23 m single-seater offered as pure glider, petrol sustainer or electric self-launcher.","Lange Aviation","2003",W+"Lange_Antares",
   [("Antares 20E","Lange Aviation","2003","electric self-launch"),("Antares 18T","Lange Aviation","","Solo 2350 sustainer"),("Antares 23E","Lange Aviation","","23 m, electric")],"span · power")],
 "m":[["ASK 21 Mi",AS],["ASH 31 Mi",AS],["ASG 32 Mi",AS],["AS 34 Me",AS],["AS 35 Mi",AS],["S12","Stemme"]]}
hab={"n":"Hot-air balloon","a":"montgolfière","d":"Lighter-than-air aircraft lifted by heated air in an envelope.",
 "t":["hopper (solo)","sport","passenger","special shape","envelope, basket and burner"],
 "s":"https://ultramagic.com/hot-air-balloons/envelopes/z-series","x":[
 X("Cameron Z-type","","Horizontally cut, near-smooth envelope suited to artwork; over 1,100 built in 30 sizes.",CB,"",'https://www.cameronballoons.co.uk/z-type',
   [("Z-31 Hopper",CB,"","solo pilot"),("Z-425LW",CB,"","light weight"),("Z-750",CB,"","largest, pilot + 32")],"size · artwork · basket"),
 X("Cameron A-type","","Twenty-gore semi-bulbous passenger envelope, the long-running work horse of ride operators.",CB,"",'https://www.cameronballoons.co.uk/a-type',
   [("A-105",CB,"","pilot + 3–4"),("A-210",CB,"","pilot + 9–10"),("A-425lw",CB,"","pilot + 16–20"),("A-530lw",CB,"","pilot + 28")],"size · basket compartments"),
 X("Cameron Sport series","","Sixteen-gore lightweight envelope for training, syndicates and leisure flying.",CB,"",'https://cameronballoons.co.uk/sport-series',
   [("Sport-50",CB,"","50,000 cu ft"),("Sport-90",CB,"","90,000 cu ft"),("Sport-105",CB,"","105,000 cu ft")],"size · RipStop or Superlight fabric"),
 X("Ultramagic M- and N-series","","Ultramagic's sport (M) and passenger (N) envelope families.","Ultramagic","",W+"Ultramagic",
   [("M-77","Ultramagic","","3–4 people"),("M-130","Ultramagic","","6 people"),("N-210","Ultramagic","","11 people"),("N-355","Ultramagic","","20 people"),("N-500","Ultramagic","","up to 27")],"size · colours"),
 X("Ultramagic Z-series","","Diamond-cut 16-gore semi-bulbous envelope allowing free colour combinations.","Ultramagic","",'https://ultramagic.com/hot-air-balloons/envelopes/z-series',
   [("Z-90","Ultramagic","","")],"22 colours · Nomex scoop · windows"),
 X("Kubíček BB series","","Czech envelopes from a maker that weaves, coats and colours its own fabric.","Kubicek Balloons","",W+"Kubicek_Balloons",
   [("BB-20XR","Kubicek Balloons","",""),("BB26Z","Kubicek Balloons","","")],"size · rattan basket")],
 "m":[["O-31",CB]]}
gas={"n":"Gas balloon","a":"charlière · Rozière (hybrid)","d":"Lighter-than-air aircraft lifted by a light gas, without propulsion.",
 "t":["hydrogen","helium","Rozière hybrid"],"s":"https://cameronballoons.co.uk/gb1000-gas-balloon","x":[
 X("Cameron GB1000","","Sealed hydrogen racing and long-duration balloon; won the 2018 Gordon Bennett race.",CB,"2010",'https://cameronballoons.co.uk/gb1000-gas-balloon',[],"envelope · basket"),
 X("Rozière balloon","","Hybrid with separate gas and hot-air cells, used for record long-distance flights.","","1785",W+"Rozière_balloon",
   [("Cameron R-77",CB,"1992","Atlantic crossings"),("Breitling Orbiter 3",CB,"1999","first non-stop circumnavigation")],"size · gas cell")]}
air={"n":"Airship","a":"blimp · dirigible","d":"Powered, steerable lighter-than-air aircraft.","t":["helium semi-rigid","blimp","hot-air (thermal) airship"],
 "s":"https://www.airships.net/zeppelin-nt/","x":[
 X("Hot-air airship","thermal airship","Powered, steerable craft lifted by heated air rather than gas.",CB,"1973",W+"Thermal_airship",
   [("D-96",CB,"1973","first public flight")],"envelope size · engine"),
 X("Zeppelin NT","","Helium semi-rigid airship from Friedrichshafen used for sightseeing, advertising and research.","Zeppelin Luftschifftechnik","1997",W+"Zeppelin_NT",
   [("N07-100","Zeppelin Luftschifftechnik","1997","original"),("N07-101","Zeppelin Luftschifftechnik","2011","up to 14 passengers")],"livery · role")]}
def B(n,c,f,seg,d,sig,s,rel=(),lines=()): return {"n":n,"c":c,"f":f,"seg":seg,"d":d,"lines":list(lines),"eras":[],"sig":sig,"sc":[],"rel":list(rel),"s":s}
brands=[
 B(AS,"Germany","1927","Gliders and motor-gliders","Glider maker in Poppenhausen founded by Alexander Schleicher.",["ASK 21","ASG 29","Ka 8"],W+"Alexander_Schleicher_GmbH_%26_Co",[SH,"DG Flugzeugbau"]),
 B(SH,"Germany","1935","Gliders and motor-gliders","Kirchheim unter Teck glider maker founded by Martin Schempp with Wolf Hirth.",["Discus","Ventus","Nimbus","Duo Discus","Arcus"],W+"Schempp-Hirth",[AS,"DG Flugzeugbau"]),
 B("DG Flugzeugbau","Germany","1973","Gliders and motor-gliders","Bruchsal maker founded as Glaser-Dirks by Gerhard Glaser and Wilhelm Dirks.",["DG-1000"],W+"DG_Flugzeugbau",[AS,SH]),
 B("Slingsby Aviation","United Kingdom","1931","Gliders (historic)","Kirkbymoorside firm founded by Fred Slingsby, which built gliders until 1982.",["Slingsby T.21"],W+"Slingsby_Aviation"),
 B("Schweizer Aircraft","United States","","Gliders (historic)","Elmira, New York maker of American training and one-design gliders.",["Schweizer 1-26"],W+"Schweizer_SGS_1-26"),
 B("Let Kunovice","Czech Republic","","Gliders and light aircraft","Czech aircraft factory that built the L-13 Blaník.",["L-13 Blaník"],"https://en.wikipedia.org/wiki/LET_L-13_Blaník"),
 B("Grob Aircraft","Germany","","Gliders, motor-gliders and trainers","Mindelheim aircraft maker founded by Burkhart Grob.",["Grob Astir","Grob G 109"],W+"Grob_G_109"),
 B("Scheibe Flugzeugbau","Germany","","Motor-gliders","West German maker of the Falke touring motor glider, run by Scheibe Aircraft GmbH since 2006.",["Scheibe Falke"],W+"Scheibe_SF_25_Falke"),
 B("Stemme","Germany","","Motor-gliders","Strausberg maker of side-by-side self-launching motor gliders.",["Stemme S10"],W+"Stemme_S10"),
 B("Pipistrel","Slovenia","","Light aircraft and motor-gliders","Slovenian maker of light and electric aircraft.",["Pipistrel Taurus"],W+"Pipistrel_Taurus"),
 B("Lange Aviation","Germany","","Electric motor-gliders","German maker of the Antares electric self-launching glider.",["Lange Antares"],W+"Lange_Antares"),
 B(CB,"United Kingdom","1971","Hot-air and gas balloons","Bristol balloon maker founded by Don Cameron; the largest share of UK-registered balloons.",["Cameron Z-type","Cameron A-type","Cameron GB1000","Hot-air airship"],W+"Cameron_Balloons",["Lindstrand Balloons","Ultramagic","Kubicek Balloons"]),
 B("Lindstrand Balloons","United Kingdom","1978","Hot-air balloons (defunct)","Oswestry maker founded by Per Lindstrand as Colt Balloons; closed in 2015.",[],W+"Lindstrand_Balloons",[CB]),
 B("Ultramagic","Spain","","Hot-air balloons","Catalan balloon maker at Igualada-Òdena, Spain's only one and second worldwide.",["Ultramagic M- and N-series","Ultramagic Z-series"],W+"Ultramagic",[CB,"Kubicek Balloons"]),
 B("Kubicek Balloons","Czech Republic","1991","Hot-air balloons and airships","Brno balloon maker founded by Aleš Kubíček that makes its own envelope fabric.",["Kubíček BB series"],W+"Kubicek_Balloons",[CB,"Ultramagic"]),
 B("Zeppelin Luftschifftechnik","Germany","","Airships","Friedrichshafen builder of the Zeppelin NT.",["Zeppelin NT"],W+"Zeppelin_NT"),
]
notes=("All five planned kinds kept. Schleicher skew trimmed: AS 33 kept as flat model; Schleicher self-launchers (ASK 21 Mi, ASH 31 Mi, ASG 32 Mi, AS 34 Me, AS 35 Mi) kept as flat models in Motor-glider for lack of retrieved pages. "
 "Old Discus-2/Duo Discus/Ventus/Arcus/ASK 21/ASW 28 became archetypes; Taurus, S10 became archetypes; A-425 recorded as A-425lw per Cameron's A-type page; Z-90 under Ultramagic Z-series; GB1000 archetype. "
 "Left out: Cameron O-type archetype (only a search snippet; O-31 kept flat), Lindstrand models (no range page; brand stub only), Stemme S12 details, Nimbus-3/4 years, Ventus 3 year, Skyacht personal blimp and Gefa-Flug airships (no model details), Goodyear blimps (corporate). "
 "Founding years left blank where pages did not give them.")
out={"kinds":[glider,motor,hab,gas,air],"brands":brands,"traditions":[],"notes":notes}
p='/home/user/Possession-Taxonomy/rebuild/work/G1/shelves/08_01.json'
json.dump(out,open(p+'.tmp','w'),ensure_ascii=False,indent=1); os.replace(p+'.tmp',p)
