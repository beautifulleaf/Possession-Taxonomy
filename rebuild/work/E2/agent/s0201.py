import sys; sys.path.insert(0,'/home/user/Possession-Taxonomy/rebuild/work/E2/agent')
from write import w
def X(n,a,d,mk,y,s,v=(),dt=""):
    return {"n":n,"a":a,"d":d,"mk":mk,"y":y,"s":s,"v":[dict(zip(("n","mk","y","d"),t)) for t in v],"dt":dt}
BW="https://www.badmintonwarehouse.com/collections/advanced-badminton-rackets"
LZ="https://sports.lazada.com.ph/yonex-astrox-vs-arcsaber-vs-nanoflare-which-racket-fits-your-style-ph/"
LN="https://thegodofsports.com/collections/li-ning-badminton-racket?page=4"
Y="Yonex"; V="Victor"; L="Li-Ning"
racket={"n":"Badminton racket","a":"","d":"Light, long-shafted racket strung for badminton; balance, weight and flex vary.",
 "t":["head-heavy","even balance","head-light","3U","4U","5U"],"s":BW,
 "x":[
  X("Yonex Astrox","Astrox","Head-heavy Yonex line for power and steep smashes, with weight spread by the Rotational Generator System.",Y,"",LZ,
    [("Astrox 100 ZZ",Y,"",""),("Astrox 99 Pro",Y,"","3rd generation"),("Astrox 88S Pro",Y,"","3rd generation"),("Astrox 88D Pro",Y,"","3rd generation"),("Astrox 77 Pro",Y,"",""),("Astrox 100VA ZZ",Y,"","")],"weight 3U–5U · colourways"),
  X("Yonex Voltric","Voltric","Head-heavy Yonex attacking line; the Voltric Z-Force II was used by Lee Chong Wei.",Y,"","https://badminton-coach.co.uk/5632/voltric-z-force-ii-badminton-racket-review/",
    [("Voltric Z-Force",Y,"","original"),("Voltric Z-Force II",Y,"2014","Lee Chong Wei"),("Voltric 80",Y,"",""),("Voltric 70",Y,"",""),("Voltric 50",Y,"","")],""),
  X("Yonex Nanoflare","Nanoflare","Head-light Yonex line for speed and quick handling, with an aerodynamic frame.",Y,"",LZ,
    [("Nanoflare 1000Z",Y,"2023",""),("Nanoflare 1000 Tour",Y,"2023",""),("Nanoflare 800 Pro",Y,"",""),("Nanoflare 700 Pro",Y,"","")],""),
  X("Yonex ArcSaber","Arcsaber","Even-balance Yonex control line whose flexing frame holds the shuttle on the string bed.",Y,"",LZ,
    [("ArcSaber 11 Pro",Y,"",""),("ArcSaber 7 Pro",Y,"","")],""),
  X("Victor Thruster","Thruster","Victor's attacking racket line, including Tai Tzu Ying signature models.",V,"",BW,
    [("Thruster TK-RYUGA",V,"",""),("Thruster TK-RYUGA II",V,"",""),("Thruster F Ultra",V,"",""),("Thruster TK-TTY A",V,"","Tai Tzu Ying signature"),("Thruster TTY Ultima",V,"","")],""),
  X("Victor Auraspeed","Auraspeed","Victor's speed-oriented racket line.",V,"",BW,
    [("Auraspeed 100X Ultra",V,"",""),("Auraspeed 90K II",V,"",""),("Auraspeed HS Plus C",V,"","")],""),
  X("Li-Ning Aeronaut","Aeronaut","Li-Ning's flagship offensive line of head-heavy, stiff-shaft frames for singles attackers.",L,"",LN,
    [("Aeronaut 9000 Combat",L,"",""),("Aeronaut 7000 Combat",L,"","")],""),
  X("Li-Ning AxForce","AxForce","Li-Ning line combining fast swing with strong repulsion for attacking players.",L,"",LN,
    [("AxForce Cannon",L,"",""),("AxForce Cannon Pro",L,"",""),("AxForce Tiger",L,"","")],""),
  X("Li-Ning Windstorm","Windstorm","Li-Ning ultralight speed frames for net and doubles players.",L,"",LN,
    [("Windstorm 72S",L,"",""),("Windstorm 75S",L,"","")],"")],
 "m":[["DriveX 12 O",V],["Jetspeed S12-II",V],["Blizzard Pro ZZ","Apacs"],["Fantala Pro 101","Apacs"],["Halbertec 6000",L],["Tectonic 9",L]]}
shuttle={"n":"Shuttlecock","a":"shuttle · birdie","d":"Feathered or plastic-skirted projectile hit in badminton.","t":["feather","nylon"],
 "s":"https://www.badmintonwarehouse.com/collections/nylon-birdies/products/sm300ym",
 "x":[X("Yonex Aerosensa","AS","Goose-feather tournament shuttlecock graded by number, used at major tournaments.",Y,"","https://www.badmintonalley.com/Yonex_Aerosensa_40_AS_40_Feather_Shuttlecock_p/shuttlecock-yonex-as40.htm",
        [("Aerosensa 50 (AS-50)",Y,"","top grade"),("Aerosensa 40 (AS-40)",Y,"","tournament"),("Aerosensa 30 (AS-30)",Y,"","")],"speed grades"),
      X("Yonex Mavis","Mavis","Nylon-skirted shuttlecock line; the Mavis 300 is described as the most popular nylon shuttle.",Y,"","https://www.badmintonwarehouse.com/collections/nylon-birdies/products/sm300ym",
        [("Mavis 300",Y,"","club and recreation"),("Mavis 350",Y,"","club and competitive practice"),("Mavis 600",Y,"",""),("Mavis 2000",Y,"","advanced training")],"yellow or white · speed (slow, medium, fast)")]}
string={"n":"Badminton string","a":"","d":"String sold to string a badminton racket, by the set or the reel.","s":BW}
net={"n":"Badminton net","a":"","d":"Net and posts or net alone sold for badminton.","t":["net only","net and posts set"],"s":BW}
sq={"n":"Squash racket","a":"squash racquet","d":"Light, long-throated racket with a small strung head made for squash.","t":["teardrop head","traditional (closed throat) head","junior"],
 "s":"https://squashmagazine.com/2018/10/best-selling-squash-racquets/",
 "x":[X("Tecnifibre Carboflex","Carboflex","Best-selling Tecnifibre squash racket line, used by Mohamed ElShorbagy and Nour El Sherbini.","Tecnifibre","","https://squashmagazine.com/2018/10/best-selling-squash-racquets/",
        [("Carboflex 125","Tecnifibre","",""),("Carboflex 125 S","Tecnifibre","",""),("Carboflex X-Speed","Tecnifibre","","updated range")],"125–130 g")],
 "m":[["Biomimetic Elite","Dunlop"],["Force Revelation Junior","Dunlop"],["Play Mini","Dunlop"],["Nano Ti 110","Head"],["i110","Head"]]}
ball={"n":"Squash ball","a":"","d":"Hollow rubber ball for squash, graded by coloured dots from slow to bouncy.",
 "t":["double yellow dot (slowest, 40 mm)","single yellow dot","red dot (42.5 mm)","blue dot (45 mm)","green dot (altitude)","white dot (glass courts)","hardball"],
 "s":"https://www.squashsource.com/squash-balls/",
 "m":[["Pro Double Yellow Dot","Dunlop"],["Competition Single Yellow Dot","Dunlop"],["Progress","Dunlop"],["Intro","Dunlop"],["Mini Squash","Dunlop"]]}
def B(n,c,f,seg,kf,d,s="knowledge",**kw):
    b={"n":n,"c":c,"f":f,"seg":seg,"kf":kf,"d":d}; b.update(kw); b["s"]=s; return b
brands=[B("Yonex","Japan","1946","Specialist","badminton & tennis","Japanese racket maker, the leading badminton brand.",lines=["Astrox","Nanoflare","ArcSaber","Voltric"],sig=["Yonex Astrox","Yonex Aerosensa"]),
 B("Victor","Taiwan","","Specialist","badminton","Taiwanese badminton equipment maker.",lines=["Thruster","Auraspeed","Jetspeed","DriveX"],sig=["Victor Thruster"]),
 B("Li-Ning","China","1990","Mainstream","badminton & sportswear","Chinese sportswear and badminton brand founded by gymnast Li Ning.",lines=["Aeronaut","AxForce","Windstorm","Halbertec","Tectonic"],sig=["Li-Ning Aeronaut"]),
 B("Tecnifibre","France","","Specialist","squash & strings","French maker of squash and tennis rackets and strings.",lines=["Carboflex"],sig=["Tecnifibre Carboflex"]),
 B("Dunlop","United Kingdom","","Mainstream","rackets & balls","British-origin sports brand of tennis and squash rackets and balls.",sig=["Dunlop Pro squash ball"])]
w('E2','02_01',{"kinds":[racket,shuttle,string,net,sq,ball],"brands":brands,"traditions":[],
 "notes":"Badminton racket: old flat list turned into archetypes (Astrox, Voltric, Nanoflare, ArcSaber, Thruster, Auraspeed; Li-Ning Aeronaut/AxForce/Windstorm added); maker 'Victor (Victor Rackets)' normalised to 'Victor'; dropped Apacs Cross Court Pro 6.2, Fantala 6.0 Speed and Victor Thruster F C Ultra X from flat list. Shuttlecock: Aerosensa (feather) and Mavis (nylon) archetypes; feather/nylon as t. String and net kept with no models (none in old data, not researched). New kinds Squash racket and Squash ball added with dot ladder as t. Prince squash lines not added: no retrieved page named them. Launch years for Yonex lines not confirmed except Voltric Z-Force II 2014 and Nanoflare 1000 models 2023."})
