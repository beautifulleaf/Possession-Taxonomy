import sys; sys.path.insert(0,'/home/user/Possession-Taxonomy/rebuild/work/E2/agent')
from write import w
def X(n,a,d,mk,y,s,v=(),dt=""):
    return {"n":n,"a":a,"d":d,"mk":mk,"y":y,"s":s,"v":[dict(zip(("n","mk","y","d"),t)) for t in v],"dt":dt}
BR="https://bladerubber.net/blog/viscaria-alternatives"; S="Stiga"; BF="Butterfly"
bat={"n":"Table tennis bat","a":"table tennis racket · ping-pong paddle","d":"Wooden blade, with or without rubbers, used to hit the ball in table tennis; the grip is shakehand or penholder.",
 "t":["blade","pre-assembled bat","shakehand grip","penhold grip","all-wood","carbon composite"],"s":"https://revspin.net/shop/14-blades",
 "x":[
  X("Stiga Clipper","Clipper","Seven-ply all-wood offensive blade, first released in 1981; well over a million sold.",S,"1981","https://tabletennis-reference.com/racket/detail/104/all",
    [("Clipper Wood",S,"1981","original"),("Clipper Classic",S,"",""),("Clipper WRB",S,"",""),("Clipper CR WRB",S,"","")],"7 plies · about 7 mm · handle shapes"),
  X("Butterfly Viscaria","Viscaria","Butterfly's first Arylate-Carbon blade: five wood plies with two ALC layers under koto outer plies.",BF,"early 1990s",BR,
    [("Viscaria",BF,"","")],"5 wood + 2 ALC · about 5.7–5.8 mm"),
  X("Butterfly Timo Boll ALC","Timo Boll ALC","Koto–ALC–ayous–kiri offensive blade of the Viscaria family, made with Timo Boll.",BF,"",BR,
    [("Timo Boll Spirit",BF,"","older sibling"),("Timo Boll ALC",BF,"",""),("Zhang Jike ALC",BF,"","same layup"),("Fan Zhendong ALC",BF,"","same layup")],"5 wood + 2 ALC"),
  X("DHS Hurricane blade","Hurricane Long","DHS Hurricane family of offensive blades; the Hurricane Long 5 is a 5+2 ALC blade.","DHS","","https://tabletennis-reference.com/racket/detail/935/all",
    [("Hurricane Long 5","DHS","","5+2 ALC, 5.9 mm, about 89 g"),("Hurricane Hao","DHS","",""),("Hurricane Hao 2","DHS","",""),("Hurricane Hao 3","DHS","",""),("Hurricane XIA","DHS","","")],"")],
 "m":[["Allround Classic",S],["Allround Evolution",S],["Arctic Wood",S],["Carbonado 45",S],["Carbonado 90",S],["Carbonado 245",S],["Celero",S],["Defensive Pro",S],["Carbo 7.6 WRB",S],
      ["Expert 3.0","Palio"],["Legend 3.0","Palio"],["A4002","DHS"],["Pro Carbon",S],["JET800","Killerspin"]],
 "r":[["Carbonado",S]]}
rubber={"n":"Table tennis rubber","a":"","d":"Rubber sheet, with or without sponge, glued to a table tennis bat; the surface is inverted, pimples-out or long pimples.",
 "t":["inverted","short pimples","long pimples","anti-spin","tacky (Chinese)","tensor (European/Japanese)"],"s":"https://www.megaspin.net/store/default.asp?cid=rubbers&type=All",
 "x":[
  X("Butterfly Tenergy","Tenergy 05","High Tension topsheet on Spring Sponge; Tenergy 05 was the gold-standard non-tacky rubber from its 2008 launch.",BF,"2008","https://www.megaspin.net/articles/578/butterfly_dignics_09c_vs_butterfly_tenergy_05",
    [("Tenergy 05",BF,"2008","")],"thickness · sponge colour"),
  X("Butterfly Dignics","Dignics","Successor to Tenergy with Spring Sponge X; Dignics 09C adds a high-friction tacky topsheet.",BF,"","https://www.megaspin.net/articles/578/butterfly_dignics_09c_vs_butterfly_tenergy_05",
    [("Dignics 05",BF,"",""),("Dignics 09C",BF,"","hard Spring Sponge X, high friction")],""),
  X("DHS Hurricane 3","Hurricane 3, H3","Tacky, hard-sponge Chinese rubber prized for spin and control, often boosted for speed.","DHS","","https://www.tabletennisdaily.com/equipment/hurricane-3.1356/reviews",
    [("Hurricane 3","DHS","","commercial"),("Neo Hurricane 3","DHS","",""),("Hurricane 3 National","DHS","","")],"sponge hardness · thickness"),
  X("Tibhar Evolution","Evolution MX-P","Tibhar's tensor rubber series; the MX-P has been the best-selling rubber for several years.","Tibhar","","https://tabletennis11.com/eu/blog/post/tibhar-evolution-mx-p",
    [("Evolution MX-P","Tibhar","","47.5° sponge"),("Evolution MX-P 50°","Tibhar","","harder sponge"),("Evolution MX-S","Tibhar","","")],"")]}
ball={"n":"Table tennis ball","a":"ping-pong ball","d":"40 mm celluloid-free plastic ball made for table tennis; comes with a star rating.","t":["3-star (competition)","training"],"s":"https://revspin.net/shop/14-blades"}
table={"n":"Table tennis table","a":"ping-pong table","d":"Regulation-surface table with a net made for table tennis; indoor or outdoor models.","t":["indoor","outdoor","rollaway (folding)"],
 "s":"https://www.tenniswarehouse.com.au/table-tennis/tables/shop/cornilleau.html",
 "m":[["Centrefold 25",BF],["Garden 6000",BF],["Space Saver 22",BF],["Tour 2500","JOOLA"],["Inside","JOOLA"],["Advantage Pro25",S],["510 Campus Outdoor","Cornilleau"],["100X Outdoor","Cornilleau"],["500X Outdoor","Cornilleau"],["700X Outdoor","Cornilleau"],["Revolution","Killerspin"],["Waldner Premium 30","Donic"]],
 "r":[["Cornilleau X outdoor","Cornilleau"]]}
robot={"n":"Table tennis robot","a":"","d":"Ball-throwing machine that feeds table-tennis balls for practice.","s":"https://racketinsight.com/table-tennis/robots/best-table-tennis-robots/",
 "m":[["Amicus Prime",BF],["Amicus Professional",BF],["Robo-Pong 3050XL","Newgy"],["Nova S Pro","PongBot"],["Omega","Power Pong"],["Trainer Motion","iPong"]],"r":[["Amicus",BF]]}
def B(n,c,f,seg,kf,d,s="knowledge",**kw):
    b={"n":n,"c":c,"f":f,"seg":seg,"kf":kf,"d":d}; b.update(kw); b["s"]=s; return b
brands=[B(BF,"Japan","1950","Professional & flagship","table tennis","Japanese table tennis brand (Tamasu), maker of Tenergy and Dignics rubbers and ALC blades.",lines=["Tenergy","Dignics","Viscaria","Amicus"],sig=["Butterfly Viscaria","Butterfly Tenergy"]),
 B(S,"Sweden","","Mainstream","table tennis","Swedish table tennis maker of blades, bats and tables.",lines=["Clipper","Carbonado","Allround"],sig=["Stiga Clipper"]),
 B("DHS","China","","Mainstream","table tennis","Chinese table tennis maker of Hurricane rubbers and blades, supplier to the Chinese team.",lines=["Hurricane"],sig=["DHS Hurricane 3","DHS Hurricane blade"]),
 B("Tibhar","Germany","","Specialist","table tennis rubbers","German table tennis brand known for the Evolution rubber series.",sig=["Tibhar Evolution"]),
 B("Cornilleau","France","","Mainstream","table tennis tables","French maker of indoor and outdoor table tennis tables."),
 B("JOOLA","Germany","","Mainstream","table tennis","German table tennis brand of tables, bats and balls."),
 B("Newgy","United States","","Specialist","table tennis robots","American maker of Robo-Pong table tennis robots.")]
w('E2','02_02',{"kinds":[bat,rubber,ball,table,robot],"brands":brands,"traditions":[],
 "notes":"Bat: blade and pre-assembled bat as t; Clipper, Viscaria, Timo Boll ALC and DHS Hurricane blade as archetypes; old Stiga Clipper models became versions; other old Stiga blades kept flat; pre-assembled bats added from Expert Table Tennis list (Palio Expert 3.0, Legend 3.0, DHS A4002, Stiga Pro Carbon, Killerspin JET800). Rubber: Tenergy, Dignics, Hurricane 3, Evolution archetypes. Ball kept without models (none in old data; not researched). Tables: tier list from Racket Insight plus old Cornilleau. Robots: Amicus, Robo-Pong, PongBot etc. from Racket Insight. Release years left blank where no fetched page confirmed them."})
