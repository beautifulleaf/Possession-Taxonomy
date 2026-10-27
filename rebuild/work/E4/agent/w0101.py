import json, os, sys
sys.path.insert(0,'/home/user/Possession-Taxonomy/rebuild/work/E4/agent')
from w0100 import w, X, WP
BF=WP+'Butterfly_knife'; SB=WP+'Switchblade'; SH=WP+'Shuriken'; TH=WP+'Throwing_knife'
BM="Benchmade"; GS="Geo. Schrade Knife Co."; CK="Colonial Knife Co."
kinds=[
{"n":"Butterfly knife","a":"balisong · fan knife · Batangas knife","d":"Folding knife whose two handles rotate around the tang to cover or expose the blade.",
 "t":["sandwich handle","channel handle","trainer (blunt)"],"s":"https://www.bladehq.com/cat--Butterfly-Knives--70",
 "x":[X("Batangas balisong","Traditional Philippine butterfly knife named after barangay Balisong in Taal, Batangas.",BF,"","early 1900s",
        dt="latch: Batangas (bite handle) or Manila (safe handle) · pivots: bearing, bushing or washers"),
      X("Benchmade 42","Benchmade's single-edge production balisong, the reference modern design.",BF,BM,"",
        v=[("Benchmade 49",BM,"","dual-edge blade")]),
      X("Krake Raken Zenith","Dual-edge modern balisong.",BF,"Squid Industries","")],
 "m":[["Bear & Son 114B Butterfly","Bear & Son Cutlery"],["Bear & Son 117 Butterfly","Bear & Son Cutlery"],["Bear Ops Bear Song VIII","Bear Ops"],["Benchmark BM004","Benchmark Knives"],["Kershaw Lucha","Kershaw"],["Spyderco SmallFly 2","Spyderco"]]},
{"n":"Automatic knife","a":"switchblade · flick knife · OTF knife","d":"Knife whose blade opens by a spring at the press of a button or switch, side-opening or out-the-front.",
 "t":["side-opening (OTS)","out-the-front double action","out-the-front single action","gravity knife"],"s":"https://www.bladehq.com/cat--Tactical-and-Combat-Knives--2646",
 "x":[X("Italian stiletto switchblade","Slender side-opening switchblade hand-made in Maniago and other Italian cutlery towns.",SB,"","c. 1900",
        v=[("Frank Beltrame","Frank Beltrame","","family-run maker"),("AGA Campolin","AGA Campolin","","family-run maker")]),
      X("Schrade Presto","Press-button switchblade series that dominated the US market for about forty years.",SB,GS,"1906–1916 patents",
        v=[("Flying Jack",GS,"1937","low-cost"),("Pull-Ball Knife",GS,"1937","opened by pulling a ball")]),
      X("Knife, Pocket, M2","US paratrooper switchblade with a 3.125-inch clip-point blade and bail.",SB,GS,"1940",
        v=[("Parachutist's Snap Blade Knife (MIL-K-10043)",GS,"postwar","production successor")]),
      X("Fallschirmjäger-Messer","German paratrooper gravity knife with a spear-point blade and marlinspike.",SB,"","late 1930s"),
      X("MC-1 Aircrew Survival Knife","US Air Force aircrew automatic knife.",SB,"","1958",v=[("MC-1","Camillus Cutlery Co.","",""),("MC-1","Schrade-Walden","","")]),
      X("M724 Automatic Rescue Knife","Automatic knife issued in US military ejection-seat survival kits.",SB,CK,"")],
 "m":[["Heretic Pariah","Heretic Knives"],["Kershaw Launch 7","Kershaw"],["Kershaw Livewire","Kershaw"],["Smith & Wesson M&P OTF","Smith & Wesson"]],
 "r":[["Kalashnikov","Boker"],["M&P","Smith & Wesson"]]},
{"n":"Throwing knife","a":"","d":"Balanced knife made to be thrown at a target.","t":["balanced","unbalanced","adjustable-weight"],
 "s":"https://www.kultofathena.com/product-category/weapons/knives-daggers/throwing-knives-daggers/",
 "x":[X("Central African throwing knife","Multi-bladed iron knife thrown in war and hunting.",TH,"","",a="kpinga · mambele · onzil · kulbeda · trombash")],
 "m":[["Cold Steel True Flight Thrower","Cold Steel"],["Hibben Large Triple Thrower Set","United Cutlery"]]},
{"n":"Shuriken","a":"throwing star · shaken","d":"Hand-thrown Japanese spike or star with sharpened points. A toy one is in Toys & Games.",
 "s":"https://www.bladehq.com/item--Cold-Steel-Battle-Star-Shuriken--21400",
 "x":[X("Bō-shuriken","Straight four-sided iron or steel spike about 12–21 cm long.",SH,"","17th c.",a="stick shuriken"),
      X("Hira-shuriken","Thin flat metal plate with points, often with a central hole; classed by number of points.",SH,"","",a="shaken · wheel shuriken")],
 "m":[["Cold Steel Battle Star","Cold Steel"]]}]
brands=[
 {"n":BM,"c":"United States","seg":"Premium","kf":"folding and tactical knives","d":"Oregon maker of folding, butterfly and tactical knives.","sig":["Benchmade 42"],"s":"knowledge"},
 {"n":"Squid Industries","c":"United States","seg":"Specialist","kf":"butterfly knives","d":"American maker of butterfly knives and trainers.","sig":["Krake Raken Zenith"],"s":"knowledge"},
 {"n":GS,"c":"United States","f":"1893","seg":"Heritage manufactory","kf":"switchblades","d":"George Schrade's knife company, maker of the Presto switchblades and the M2 paratrooper knife.","sig":["Schrade Presto","Knife, Pocket, M2"],"s":SB},
 {"n":CK,"c":"United States","seg":"Mainstream","kf":"military and automatic knives","d":"US maker of mass-produced switchblades and the M724 rescue knife.","sig":["M724 Automatic Rescue Knife"],"s":SB}]
notes=("All 4 old kinds kept with old models; archetypes added from Wikipedia (Butterfly knife, Switchblade, Shuriken, Throwing knife). OTF vs side-opening and gravity knives are types. "
 "Geo. Schrade founding year 1893 is for the New York Press Button Knife Co. Left out: Benchmade 42 year and Bear & Son balisong history (not on retrieved pages), Gil Hibben/Harry McEvoy throwing designs (not described on retrieved page).")
if __name__=='__main__': w('01_01',{"kinds":kinds,"brands":brands,"traditions":[],"notes":notes})
