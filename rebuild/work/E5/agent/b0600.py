import sys; sys.path.insert(0,'/home/user/Possession-Taxonomy/rebuild/work/E5/agent')
from write import w
W='https://en.wikipedia.org/wiki/'
def X(n,a,d,mk,y,s,v,dt=''):
    return {"n":n,"a":a,"d":d,"mk":mk,"y":y,"s":s,"v":[{"n":q[0],"mk":q[1],"y":q[2],"d":q[3]} for q in v],"dt":dt}
def B(n,c,f,seg,kf,d,s,sig=(),rel=()):
    b={"n":n,"c":c,"f":f,"seg":seg,"kf":kf,"d":d}
    if sig: b["sig"]=list(sig)
    if rel: b["rel"]=list(rel)
    b["s"]=s; return b
AM='https://www.arcade-museum.com/games-and-machines/cabinets'
JL=W+'List_of_Japanese_arcade_cabinets'
A1=W+'Arcade1Up'; AG=W+'AtGames_Legends_Ultimate'; II='https://www.tomshardware.com/news/iircade-arcade-cabinet'
S='Sega'; T='Taito'; N='Namco'; SN='SNK'; KO='Konami'; J='Jaleco'; C='Capcom'

up={"n":"Upright arcade cabinet","a":"standard cabinet · stand-up cabinet","d":"Coin-operated video arcade cabinet that stands upright and is played standing.","t":["dedicated","conversion","deluxe or themed"],"s":AM,"x":[
 X("SNK Neo Geo MVS upright","MVS cabinet","SNK's upright cabinets for the multi-slot Neo Geo MVS system.",SN,"",JL,
   [("SNK MV25U4-0",SN,"","25 in, 4-slot"),("SNK MV25U6-0",SN,"","25 in, 6-slot"),("SNK MV19SC-0",SN,"","19 in"),("SNK SCB-U4",SN,"","")],"screen 19–25 in · 1 to 6 slots")],
 "m":[["Sega Swing",S],["Capcom Captain IV",C],["Capcom Playzass",C],["Capcom CAV 2 OOB 60",C],["Jaleco Pony Mark II 27",J],["Konami Sauroid",KO],["Sammy Atomiswave","Sammy"]]}

candy={"n":"Candy (sit-down) arcade cabinet","a":"candy cabinet · Japanese cabinet · sit-down cabinet","d":"Japanese-style video arcade cabinet, usually white metal and plastic, played seated on a stool and rarely shipped outside East Asia.",
 "t":["versus (back-to-back) pair","large-screen theatre","widescreen LCD"],"s":JL,"x":[
 X("Sega Astro City","Aero City · New Astro City","Sega's multi-purpose 29-inch candy cabinet, successor to the Aero City and the reference Japanese cabinet.",S,"1993","https://segaretro.org/Astro_City",
   [("Sega City",S,"1986","19 in"),("Sega Aero City",S,"1988","26 in, predecessor"),("Sega Astro City",S,"1993","29 in"),("Sega New Astro City",S,"1995","Model 2 support, better screen"),("Sega Astro City II",S,"1997","")],"screen 26–29 in · panel layout · colour"),
 X("Sega Blast City","","Taller Sega candy cabinet with more room for banners and lights.",S,"1996",JL,[("Sega Blast City",S,"1996","29 in")]),
 X("Sega Versus City","New Versus City","Sega's cabinet pairs built for back-to-back versus play.",S,"1996",JL,[("Sega Versus City",S,"1996","29 in"),("Sega New Versus City",S,"1996","")]),
 X("Sega Net City","New Net City","Sega's 29-inch candy cabinet of the NAOMI era.",S,"1999",JL,[("Sega Net City",S,"1999","29 in"),("Sega New Net City",S,"","29 in")]),
 X("Taito Egret","Egret II","Taito's 29-inch candy cabinets; the Egret II is known for its rotating monitor for vertical games.",T,"1994","https://hard--candy.com/wiki/candy/Egret_II",
   [("Taito Egret 29",T,"1994","29 in"),("Taito Egret II",T,"1996","Nanao MS9-29T monitor, rotation mechanism"),("Taito Egret 3",T,"2003","29 in")]),
 X("Taito Vewlix","Vewlix F · Vewlix L","Taito's widescreen LCD candy cabinet line, built for 16:9 HD games.",T,"2007","https://hard--candy.com/wiki/candy/Vewlix_F",
   [("Taito Vewlix F",T,"2007","32 in 1080p LCD"),("Taito Vewlix L",T,"","starter version"),("Taito Vewlix C",T,"",""),("Taito Vewlix VS",T,"","")]),
 X("Namco Cyber Lead","Cyber Lead II","Namco's 29-inch candy cabinets of the late 1990s.",N,"1997",JL,[("Namco Cyber Lead",N,"1997","29 in"),("Namco Cyber Lead II",N,"2000","")]),
 X("Namco Noir","","Namco's 32-inch LCD candy cabinet.",N,"2007",JL,[("Namco Noir",N,"2007","32 in")]),
 X("SNK Neo Geo candy cabinets","Neo 29 · Super Neo 29","SNK's sit-down cabinets wired for the Neo Geo MVS.",SN,"",JL,
   [("SNK Candy 25",SN,"","25 in"),("SNK Neo 29",SN,"","29 in"),("SNK Super Neo 28 Candy",SN,"1996","33 in"),("SNK Super Neo 29",SN,"","29 in"),("SNK Super Neo 29 Type II",SN,"","29 in"),("SNK MVS-U4/29",SN,"","29 in, 4-slot"),("SNK Neo 50",SN,"","large screen")],"screen 18–33 in · slots"),
 X("Konami Windy","Windy II","Konami's 29-inch candy cabinet.",KO,"1996",JL,[("Konami Windy",KO,"1996","29 in"),("Konami Windy II",KO,"1998","29 in")]),
 X("Jaleco Pony","Pony Mark II","Jaleco's candy cabinet line.",J,"",JL,[("Jaleco Pony",J,"",""),("Jaleco Pony Mark II 19",J,"1996","19 in"),("Jaleco Pony Mark III",J,"1997",""),("Jaleco Pony Mark IV",J,"",""),("Jaleco Pony Mark V",J,"","")])],
 "m":[["Taito Canary",T],["Capcom Impress",C],["Capcom BGS-25",C],["Capcom Status 25",C],["Capcom Cute",C],["Irem Madonna","Irem"],["Sammy Atomiswave SD","Sammy"],["Sega Naomi Universal",S],["Sega Lindbergh Universal",S],["Sega ALL.Net P-ras MULTI Version 3",S],["exA-Arcadia ARC-32","exA-Arcadia"],["Sigma Game Explorer","Sigma"],["Sunsoft Rana","Sunsoft"],["Tecmo Kyotaro","Tecmo"],["River Service New Delta","River Service"],["Lucky Galaxy","Lucky"],["Konami Domy Theater 50",KO],["Sega Megalo 50",S]]}

cab={"n":"Cabaret arcade cabinet","a":"mini cabinet","d":"Smaller, narrower upright coin-operated video cabinet.","s":AM,"m":[["PAC-MAN's Pixel Bash Cabaret","Bandai Namco Entertainment"]]}
ckt={"n":"Cocktail table arcade cabinet","a":"cocktail cabinet · table cabinet","d":"Coin-operated video cabinet built as a table, played seated across or beside it.","t":["face-to-face","side-by-side"],"s":AM,
 "m":[["Sega Aero Table",S],["Jaleco Table Pony",J],["Jaleco Table Pony 25",J],["Jaleco Table Pony 25 VH",J],["SNK MV25TA-0",SN]]}
cp={"n":"Cockpit arcade cabinet","a":"environmental cabinet · deluxe motion cabinet","d":"Enclosed or motion cabinet built around the player.","t":["enclosed","motion"],"s":AM,
 "m":[["Sega R-360",S],["Sega Storm-G",S],["Sega VR-1",S],["Simuline Cycraft","Simuline"],["Discs of Tron cockpit cabinet",""],["Sinistar cockpit cabinet",""]]}
bar={"n":"Bar-top arcade cabinet","a":"counter-top cabinet · Counter-cade","d":"Small cabinet made to stand on a counter, bar or table.","s":AM,"x":[
 X("Arcade1Up Counter-cade","Counter-cade","Arcade1Up's bar-top units, usually with two to five built-in games.","Arcade1Up","",A1,
   [("Arcade1Up Pong Counter-Cade","Arcade1Up","",""),("Arcade1Up NBA Jam Counter-Cade","Arcade1Up","","")])],
 "m":[["Evercade Alpha","Blaze Entertainment"]]}
home={"n":"Home replica arcade cabinet","a":"3/4-scale cabinet · home arcade","d":"Reduced-scale or home-built arcade cabinet with an LCD and built-in games, made for homes rather than arcades.",
 "t":["3/4 scale","full size","sit-down driving","head-to-head table"],"s":A1,"x":[
 X("Arcade1Up cabinet","Arcade1Up","Arcade1Up's ready-to-assemble 3/4-scale licensed replica cabinets with LCD screens.","Arcade1Up","2018",A1,
   [("Arcade1Up 3/4-scale cabinet","Arcade1Up","2018","17 in LCD, self-assembly"),("Arcade1Up Pac-Man Cabinet (ARC7030)","Arcade1Up","",""),("Arcade1Up head-to-head table","Arcade1Up","","sit-down two-player table"),("Arcade1Up Out Run","Arcade1Up","2020","sit-down driving cabinet"),("Arcade1Up full-size cabinet","Arcade1Up","2022","19 in screen, SuzoHapp controls")],"riser · light-up marquee · Wi-Fi"),
 X("AtGames Legends Ultimate","Legends Ultimate","AtGames' home multi-game cabinet with a 24-inch 1080p screen and hundreds of licensed games.","AtGames","2019",AG,
   [("Legends Ultimate (compact)","AtGames","2019","46 in tall"),("Legends Ultimate (full size)","AtGames","2019","66 in tall")]),
 X("iiRcade","","Home cabinet mixing licensed retro titles and newer games from its own store.","iiRcade","2020",II,[])]}

K="knowledge"
br=[B(S,"Japan","1960","Professional & flagship","arcade cabinets","Japanese arcade and console maker of the City cabinet line.",K,["Sega Astro City","Sega Blast City","Sega Versus City","Sega Net City"]),
 B(T,"Japan","1953","Professional & flagship","arcade cabinets","Japanese arcade maker of the Egret and Vewlix cabinets.",K,["Taito Egret","Taito Vewlix"]),
 B(N,"Japan","1955","Professional & flagship","arcade cabinets","Japanese arcade maker, now Bandai Namco, of the Cyber Lead and Noir cabinets.",K,["Namco Cyber Lead","Namco Noir"]),
 B(SN,"Japan","1978","Professional & flagship","Neo Geo","Japanese maker of the Neo Geo MVS and its cabinets.",K,["SNK Neo Geo candy cabinets","SNK Neo Geo MVS upright"]),
 B(KO,"Japan","1969","Professional & flagship","arcade games","Japanese game maker of the Windy cabinets.",K,["Konami Windy"]),
 B(J,"Japan","1974","Specialist","arcade cabinets","Japanese arcade maker of the Pony cabinets.",K,["Jaleco Pony"]),
 B("Arcade1Up","United States","2018","Mainstream","home cabinets","Miami maker of 3/4-scale home arcade cabinets, a Tastemakers subsidiary; assets bought by Basic Fun! in 2026.",A1,["Arcade1Up cabinet","Arcade1Up Counter-cade"]),
 B("AtGames","","","Value","home arcade","Maker of the Legends Ultimate home arcade cabinet.",AG,["AtGames Legends Ultimate"]),
 B("iiRcade","","","Specialist","home arcade","Maker of the iiRcade home cabinet.",II,["iiRcade"])]

w('E5','06_00',{"kinds":[up,candy,cab,ckt,cp,bar,home],"brands":br,"traditions":[],
 "notes":"Upright: Arcade1Up uprights moved to the new Home replica kind; SNK upright SKUs grouped into one archetype. Candy: renamed from Sit-down; 93 models -> 11 archetypes + 18 models. Dropped as SKU noise or theatre-size operator units: further SNK Candy/Neo/MVS/SC sizes, Capcom CAV System 60 and OOB-50, Namco Arena Site, Dynalive, Excelcabinet, Exceleena 1/2, Taito MT2/MT5/Teatro, Sega Super Megalo 1/2, Megalo 410, Naomi 50/Deluxe Universal, Konami Domy Jr/Theater 33/Plasma, Jaleco Pony 40, Irem Madonna 33, Tecmo Urban, River Service Delta. Bar-top keeps Counter-cades; other title-named Arcade1Up SKUs (Big Buck Hunter, Centipede, Killer Instinct, Mortal Kombat, TMNT, Marvel tables etc.) dropped as title lists; Arcade1Up ranges replaced by the archetype. Blast City Sega Retro page blocked; attested via the Wikipedia list."})
