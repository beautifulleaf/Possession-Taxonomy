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
LP=W+'List_of_pinball_machines'; LM=W+'List_of_pinball_manufacturers'
BA='Bally'; WI='Williams'; GO='Gottlieb'; ST='Stern Pinball'; JJ='Jersey Jack Pinball'; SP='Spooky Pinball'; CG='Chicago Gaming Company'; AP='American Pinball'

ss={"n":"Solid-state pinball machine","a":"SS pinball · DMD pinball · modern pinball","d":"Pinball machine run by electronic boards and software, from the late-1970s microprocessor games to today's LCD machines.",
 "t":["alphanumeric display","dot-matrix display (DMD)","LCD display","widebody","Pro, Premium and Limited Edition trims","remake"],"s":LP,"x":[
 X("The Addams Family","TAF","Pat Lawlor and Larry DeMar's machine, the best-selling solid-state pinball of all time.",BA,"1992",W+"The_Addams_Family_(pinball)",
   [("The Addams Family",BA,"1992","Midway, 20,270 made, WPC Fliptronics"),("The Addams Family Special Collectors Edition",BA,"1994","'Gold', 1,000 numbered")]),
 X("Twilight Zone","TZ","Widebody Pat Lawlor machine with a gumball machine, working clock and ceramic Powerball; first of the SuperPin line.",BA,"1993",W+"Twilight_Zone_(pinball)",
   [("Twilight Zone",BA,"1993","Midway, 15,235 made")]),
 X("Medieval Madness","MM","Brian Eddy's castle-siege machine, often ranked among the greatest ever made and later remade under licence.",WI,"1997",W+"Medieval_Madness",
   [("Medieval Madness",WI,"1997","4,016 made"),("Medieval Madness remake",CG,"2015","standard and 1,000 limited edition with shaker"),("Medieval Madness Classic, Special and Royal",CG,"2019","Royal adds shaker, mirrors, topper"),("Medieval Madness Merlin edition",CG,"2025","")]),
 X("Attack from Mars","AFM","Bally-brand WPC-95 machine, remade by Chicago Gaming.",BA,"1995",LP,
   [("Attack from Mars",BA,"1995","Midway"),("Attack from Mars remake",CG,"2017","")]),
 X("Monster Bash","","Williams WPC-95 machine, remade by Chicago Gaming.",WI,"1998",LP,
   [("Monster Bash",WI,"1998",""),("Monster Bash remake",CG,"2018","")]),
 X("Indiana Jones: The Pinball Adventure","IJ","Williams machine that opened the WPC DCS sound era.",WI,"1993",W+"Williams_Pinball_Controller",
   [("Indiana Jones: The Pinball Adventure",WI,"1993","first WPC DCS machine")])],
 "m":[["FunHouse",WI],["Star Trek: The Next Generation",WI],["Black Knight",WI],["Firepower",WI],["High Speed",WI],["Pin-Bot",WI],["Eight Ball Deluxe",BA],["Paragon",BA],["Black Hole",GO],["Haunted House",GO],["Cirqus Voltaire",BA],["Scared Stiff",BA],
  ["Star Wars",ST],["Godzilla",ST],["Jurassic Park",ST],["The Mandalorian",ST],["Rush",ST],["Metallica",ST],["Stranger Things",ST],["Foo Fighters",ST],["Jaws",ST],
  ["The Wizard of Oz",JJ],["Pirates of the Caribbean",JJ],["Guns N' Roses",JJ],["The Godfather",JJ],
  ["America's Most Haunted",SP],["Halloween",SP],["Evil Dead",SP],["Cactus Canyon remake",CG],["Pulp Fiction",CG],["Houdini: Master of Mystery",AP],["Hot Wheels",AP]]}

em={"n":"Electromechanical pinball machine","a":"EM pinball · wedgehead · flipper","d":"Pinball machine worked by relays, motors and score reels rather than electronics, made from the 1930s to the late 1970s.",
 "t":["wedgehead","single-player","multi-player","add-a-ball","replay"],"s":W+"Gottlieb","x":[
 X("Humpty Dumpty","","Harry Mabs's Gottlieb machine that introduced player-operated flippers.",GO,"1947",W+"Gottlieb",[("Humpty Dumpty",GO,"1947","six outward-facing flippers")]),
 X("Fireball","","Bally electromechanical machine.",BA,"1972",LP,[("Fireball",BA,"1972","")])],
 "m":[["Ace High",GO],["Slick Chick",GO],["Kings & Queens",GO],["Central Park",GO],["Sky Jump",GO],["Spirit of 76",GO],["Fun House",WI],["Jive Time",WI],["Gold Rush",WI],["Fan-Tas-Tic",WI],["Big Ben",WI],["Grand Prix",WI],["Space Mission",WI]]}

dg={"n":"Digital pinball cabinet","a":"virtual pinball · VPin","d":"Pinball-shaped cabinet with a screen for a playfield that plays software tables, bought ready-made or built at home.",
 "t":["ready-made cabinet","home-built VPin","3/4 scale","full size"],"s":"https://zenstudios.com/news/zen-studios-atgames-the-ultimate-pinball-experience/","x":[
 X("AtGames Legends Pinball","Legends Pinball 4KP","AtGames' digital pinball cabinets running Zen Studios tables with real nudge sensing.","AtGames","2023","https://zenstudios.com/news/zen-studios-atgames-the-ultimate-pinball-experience/",
   [("Legends Pinball 4KP","AtGames","2023","32 in 4K playfield, 24 in backglass, 8 in DMD, G-sensor")]),
 X("Arcade1Up pinball","","Arcade1Up's 3/4-scale digital pinball machines with Zen Studios software.","Arcade1Up","2020",W+"Arcade1Up",[])]}

md={"n":"Pinball mod or topper","a":"pinball mod · topper · shaker","d":"Aftermarket part that changes the look, sound or feel of a pinball machine, from toppers and lighting to playfield toys and protectors.",
 "t":["topper","shaker motor","LED lighting kit","colour display","playfield toy","side blade","shooter rod or knob","playfield protector"],"s":"https://pu-parts.com/modifications",
 "m":[["ColorDMD","ColorDMD"],["Medieval Madness King of Payne topper",CG]]}

ema={"n":"Electromechanical arcade game","a":"EM arcade game · coin-op game","d":"Coin-operated arcade machine worked by motors, lights and relays rather than a video screen, such as submarine, gun and driving games.",
 "t":["shooting or gun","driving","submarine or periscope","sports"],"s":W+"Periscope_(arcade_game)","x":[
 X("Periscope","Torpedo Launcher","Submarine game fired through a periscope at moving ships; its US version set the 25-cent price of play.","Sega","1966",W+"Periscope_(arcade_game)",
   [("Torpedo Launcher","Nakamura Manufacturing","1965","the first version"),("Periscope","Sega","1966","three-player"),("Periscope (single-player)","Sega","1968","")])],
 "m":[["Missile","Sega"],["Jet Rocket","Sega"],["Sea Raider","Midway"],["Sea Devil","Midway"]]}

K="knowledge"
br=[B(BA,"United States","1932","Heritage manufactory","pinball","Chicago pinball and coin-op maker; from 1988 a brand of Williams and Midway.",LM,["The Addams Family","Twilight Zone","Attack from Mars","Fireball"],[WI]),
 B(WI,"United States","1943","Heritage manufactory","pinball","Chicago pinball maker of the WPC era, active until 1999.",LM,["Medieval Madness","Monster Bash","Indiana Jones: The Pinball Adventure"],[BA]),
 B(GO,"United States","1927","Heritage manufactory","pinball","David Gottlieb's Chicago company that introduced flippers; continued as Premier until 1996.",W+"Gottlieb",["Humpty Dumpty"]),
 B(ST,"United States","1999","Professional & flagship","pinball","Gary Stern's company formed from Sega Pinball, for years the only maker of new pinball machines.",LM,[]),
 B(JJ,"United States","2011","Premium","pinball","Jack Guarnieri's pinball maker, now in Elk Grove Village, Illinois.",W+"Jersey_Jack_Pinball",[]),
 B(SP,"United States","2013","Artisan & independent","pinball","Charlie Emery's small pinball maker in Benton, Wisconsin.",W+"Spooky_Pinball",[]),
 B(CG,"United States","2001","Specialist","pinball remakes","Maker of licensed remakes of Williams and Bally machines.",LM,["Medieval Madness"]),
 B(AP,"United States","2015","Specialist","pinball","Maker of Houdini and Hot Wheels pinball machines.",LM,[]),
 B("Sega","Japan","1960","Professional & flagship","arcade games","Japanese arcade maker whose early electromechanical games included Periscope.",K,["Periscope"]),
 B("AtGames","","","Value","home arcade","Maker of Legends home arcade and digital pinball cabinets.","https://zenstudios.com/news/zen-studios-atgames-the-ultimate-pinball-experience/",["AtGames Legends Pinball"]),
 B("Arcade1Up","United States","2018","Mainstream","home cabinets","Miami maker of 3/4-scale home arcade and pinball cabinets, a Tastemakers subsidiary.",W+"Arcade1Up",["Arcade1Up pinball"])]

w('E5','06_02',{"kinds":[ss,em,dg,md,ema],"brands":br,"traditions":[],
 "notes":"All kinds new (no old data). Pinball machines are physical named machines, not entertainment titles. Solid-state: 6 archetypes (WPC icons and their Chicago Gaming remakes) + 32 models across Williams, Bally, Gottlieb, Stern, JJP, Spooky, Chicago Gaming and American Pinball, all from the Wikipedia list; Theatre of Magic, Terminator 2 and Xenon were not on the retrieved part of the list and are left out. IPDB/Pinside not fetched. EM: Humpty Dumpty and Fireball archetypes + 13 Gottlieb/Williams models from the list (EM status of later 1970s Williams models taken from their dates). Mods: kind-level with types; only ColorDMD and the MM topper named. EM arcade: Periscope family plus Sega and Midway missile games; no EM gun or driving machines attested."})
