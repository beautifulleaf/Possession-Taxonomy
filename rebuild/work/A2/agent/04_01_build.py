import json, os
W='https://en.wikipedia.org/wiki/'
SD='https://www.stitchdown.com/brands/'
GP='https://www.gearpatrol.com/style/a519286/northwestern-boot-makers-wesco-nicks-whites-boots/'
ASME='https://www.asme.org/topics-resources/content/engineers-get-the-boot'
def X(n,d,mk,y,s,v=(),dt='',a=''):
    return {"n":n,"a":a,"d":d,"mk":mk,"y":y,"s":s,"v":[dict(zip(("n","mk","y","d"),t)) for t in v],"dt":dt}
kinds=[
 {"n":"Service boot","a":"dress lace-up boot · cap-toe work boot","d":"Ankle-height lace-up boot on a plain, sleeker last, often with a toe cap, without a heavy lugged or wedge work sole.",
  "t":["plain toe","cap toe","double toe cap"],"s":"https://bespokeunit.com/shoes/boots",
  "x":[
   X("1000 Mile","Plain-toe lace-up boot introduced as the '1000 Mile Shoe', named for at least a thousand miles of wear.","Wolverine","1914","https://silodrome.com/wolverine-1000-mile-boot/",
     [("1000 Mile Shoe (original)","Wolverine","1914","first shoe sold under the Wolverine name"),("1000 Mile revival","Wolverine","2009","Horween Chromexcel upper, Goodyear welt, leather sole, Vibram heel")],
     "plain toe · Chromexcel black, brown · Goodyear welt, resoleable"),
   X("Iron Ranger","Cap-toe service boot with a double-layered toe cap, first intended for iron ore miners of Minnesota's Mesabi range.","Red Wing","","https://therake.com/us/stories/invest-red-wing-iron-ranger-8111-boots",
     [("8111","Red Wing","","Amber Harness leather, nitrile cork sole")],"6-inch shaft · double toe cap · harness leathers · nitrile cork sole"),
   X("Beckman","Six-inch plain-toe Red Wing Heritage boot named after company founder Charles Beckman, on a Gro-Cord outsole.","Red Wing","","https://www.redwingshoes.com/heritage/beckman/",
     [("9423","Red Wing","","Black Excalibur leather"),("9419","Red Wing","","Black Cherry Excalibur leather"),("9422","Red Wing","","Cigar Excalibur leather")],
     "6-inch · plain toe · Excalibur leathers · Gro-Cord (Vibram) outsole"),
   X("Indy","Goodyear-welted plain-toe work boot sold as the 405 and renamed after Harrison Ford wore it in Raiders of the Lost Ark.","Alden","","https://www.stitchdown.com/brands/alden/alden-indy-boot-three-year-review/",
     [("405","Alden","","original work-boot number worn by Harrison Ford"),("403","Alden","","classic version, brown Chromexcel, neoprene cork sole"),("403C","Alden","","antique welt and commando outsole")],
     "Trubalance last · Chromexcel and other leathers · cork or commando sole", a="405"),
   X("Service Boot","Viberg's first style, a military-pattern lace-up boot later rebuilt in stitchdown construction on slimmer lasts.","Viberg","1931","https://www.stitchdown.com/brands/viberg-boots/viberg-service-complete-history/",
     [("2030 last","Viberg","2010","slimmed from a Canadian military parade-shoe last"),("310 last","Viberg","","combines a Springline last with a Dayton Toughie toe")],
     "lasts 2030, 310 · stitchdown · many leathers"),
   X("Diesel","Round-toed lace-up boot with a 360-degree welt that leans smart casual rather than rugged.","Grant Stone","","https://theshoesnobblog.com/grant-stone-diesel-boot-review/",
     [],"round last · 360-degree welt · Chromexcel, kangaroo and other leathers"),
  ],
  "m":[["Dalton","Allen Edmonds"],["Dowler","Beckett Simonon"],["Mambia","Loake"],["Saint","Taft"],["Stow","Tricker's"]]},
 {"n":"Moc-toe boot","a":"moc toe · moccasin-toe work boot","d":"Lace-up work boot with a moccasin-style stitched apron toe, usually on a wedge sole.",
  "t":["6-inch","8-inch","wedge sole","lug sole"],"s":"https://silodrome.com/red-wing-classic-moc/",
  "x":[X("Classic Moc","Moc-toe boot on a white Traction Tred wedge sole, first developed for hunters and sportsmen and in production since the early 1950s.","Red Wing","early 1950s","https://silodrome.com/red-wing-classic-moc/",
     [("875","Red Wing","","6-inch, oiled Oro Legacy leather, Traction Tred wedge")],"6-inch and taller · Oro Legacy and other leathers · white wedge sole")],
  "m":[["Tempe Moc Toe","Timberland PRO"]]},
 {"n":"Logger boot","a":"caulk boot · calk boot · timber boot · logging boot","d":"Tall lace-up boot with a high heel and a heavy sole, sometimes spiked with calks, made for timber work.",
  "t":["calked (spiked) sole","lug sole","steel toe"],"s":W+"Caulk_boots",
  "x":[
   X("Smoke Jumper","Logger-heeled boot made for wildland firefighters; the first version was worn by Forest Service smokejumper Francis Lufkin.","White's","1939","https://whitesboots.com/pages/our-legacy",
     [("First Smokejumper","White's","1939","worn by Francis Lufkin"),("335","White's","1951","promoted in dealer catalogues as the boot worn by Region 1 smokejumpers"),("Vibram-soled Smokejumper","White's","1963","new model on the Vibram sole")],
     "tall shaft · logger heel · hand-sewn, rebuildable"),
   X("Jobmaster","All-purpose Wesco work boot rooted in the Oregon timber trade, built with full-grain leather on a Vibram sole.","Wesco","","https://www.gearpatrol.com/style/a519286/northwestern-boot-makers-wesco-nicks-whites-boots/",
     [("ST208100","Wesco","","8-inch shaft, steel toe, Vibram sole, 7-ounce leather")],"shaft heights · steel or soft toe · stock and custom sizes"),
   X("Robert","Six-inch pared-down version of the Nicks Ranger work boot with a Dogger heel, named after Robert Mowe.","Nicks","","https://nicksboots.com/blogs/blog/nicks-history-from-start-to-finish",
     [],"6-inch · Dogger heel · stitchdown, fully rebuildable"),
  ],
  "m":[["Logger","Red Wing"]]},
 {"n":"Engineer boot","a":"","d":"Pull-on boot with a strap and buckle at the instep and the top, no laces.","s":W+"Engineer_boot",
  "x":[
   X("Boss","Wesco engineer boot whose 1939 ancestor was bought by Portland shipyard welders who needed to kick boots off quickly.","Wesco","1939",ASME,[],"tall shaft · buckle straps · stitchdown"),
   X("Chippewa engineer boot","Stovepipe-shafted pull-on boot based on the English riding boot, believed to be the first engineer boot.","Chippewa","late 1930s",ASME,[],""),
   X("Engineer 2268","Steel-toe Red Wing engineer boot first designed in 1936 for railroad engineers.","Red Wing","1936","https://www.redwingberlin.com/en/engineer-2268_11747",
     [("2268 Steel Toe Engineer","Red Wing","","Black Chrome leather, neoprene cord sole")],"steel toe · Black Chrome leather · minimal stitching"),
  ],
  "m":[["Engineer Boot","John Lofgren Bootmaker"]]},
 {"n":"Combat & military boot","a":"combat boot · military boot · service boot (army)","d":"Lace-up boot made to a military service pattern, or a civilian boot in that style.",
  "t":["smooth black","rough-out tan","jungle (canvas)","side-zip"],"s":"https://www.dillards.com/p/danner-mens-tachyon-8-military-boots/521185729",
  "x":[
   X("1460","Eight-eyelet boot in cherry-red smooth leather on the air-cushioned sole, the first UK Dr. Martens boot.","Dr. Martens","1960",W+"Dr._Martens",
     [("1460 (original)","Dr. Martens","1960","launched 1 April 1960, cherry-red smooth leather, yellow welt stitching")],"eight eyelets · smooth and other leathers · air-cushioned sole"),
   X("Jump boot","Paratrooper boot with lacing extended to the calf and a reinforced toe cap; known as 'Corcorans' after a maker.","","1941",W+"Jump_boot",
     [("Boots, Parachute Jumper M1942","","1942","US pattern designed by William P. Yarborough"),("Corcoran jump boot","Corcoran","","maker whose name became a byword"),("M57 Jump Boot","","1958","Dutch, dark brown, stitched soles"),("Bottes de saut Mle 50","","1950s","French pattern")],
     "smooth black leather · toe cap and heel counter for high shine"),
   X("Jungle boot","Hot-weather boot with a canvas or nylon upper, drain eyelets and a cleated rubber sole.","","1942",W+"Jungle_boot",
     [("M-1942","","1942","canvas and rubber, developed with the U.S. Rubber Company"),("M-1945 Tropical Combat Boot","","1945",""),("M-1966 Jungle Boot","","1966","cotton upper, leather toe and heel, steel anti-punji plate"),("Panama-sole jungle boot","","1969","Dobie's mud-shedding Panama sole")],
     "black leather lower · olive canvas or nylon upper · Vibram or Panama sole"),
   X("M-1943 double-buckle boot","WWII 'Boots, Combat Service': a service shoe with a high leather cuff closed by two buckles.","","1943",W+"Combat_boot",[],"two-buckle cuff · rough-out leather"),
   X("M-43 service shoe","WWII US Army boondocker service boot built on the Munson last, now reproduced by heritage makers.","","WWII","https://blueowl.us/products/m43-service-shoe-boot-in-horween-chromexcel-natural-roughout",
     [("M-43 Service Shoe LK-017","John Lofgren","","Munson last, Horween Chromexcel roughout, Goodyear welt, Vibram 700, made in Japan")],"6-inch shaft · roughout leather · Munson last"),
   X("Army Combat Boot","Tan rough-out boot introduced with the US Army Combat Uniform.","","2002",W+"Combat_boot",[],"tan rough-out · makers include Altama, Bates, Belleville, McRae, Rocky, Wellco"),
  ],
  "m":[["Tachyon","Danner"],["Marine Corps Combat Boot","Danner"],["Combat Boot","John Lofgren Bootmaker"]]},
 {"n":"Work boot","a":"lace-up work boot","d":"Lace-up boot with a heavy lugged or wedge outsole made for labour, usually Goodyear-welted, stitch-down or moulded.",
  "t":["6-inch","8-inch","steel toe","waterproof"],"s":"https://www.dsw.com/product/timberland-pro-tempe-moc-toe-6-waterproof-work-boot---mens/625655",
  "x":[X("6-inch boot","Waterproof lace-up boot with the sole injection-moulded to the leather upper, padded collar and lug sole; the 'Yellow Boot'.","Timberland","1973","https://www.stuartslondon.com/blogs/blog/the-timberland-6-inch-boot-a-brief-history",
     [("Premium 6 Inch Waterproof Boot","Timberland","","current version")],"6-inch · nubuck in many colours · padded collar · lug sole", a="Yellow Boot · Timbs")],
  "m":[["Farmer/Rancher","White's"]]},
 {"n":"Split-toe work boot","a":"jika-tabi","d":"Boot with a separated big toe and a rubber sole, fastened by hooks or a zip up the lower leg.","s":"https://www.alexcious.com/brands/detail182.html",
  "x":[X("Rubber-soled jika-tabi","Mid-calf split-toe outdoor tabi on a rubber sole, closed at the back with metal kohaze hooks.","","1922",W+"Jika-tabi",[],"kohaze hook count · fabric upper · rubber sole")],
  "m":[["Air Jog V","Marugo"]]},
]
def B(n,c,f,seg,d,s,sig=(),lines=(),rel=()):
    return {"n":n,"c":c,"f":f,"seg":seg,"d":d,"lines":list(lines),"eras":[],"sig":list(sig),"sc":[],"rel":list(rel),"s":s}
brands=[
 B("Red Wing","United States","1905","Heritage work boots","Minnesota bootmaker founded by Charles H. Beckman; its Heritage line dates from 2008.",W+"Red_Wing_Shoes",["Iron Ranger","Beckman","Classic Moc","Engineer 2268"],["Heritage"]),
 B("Wolverine","United States","1883","Work boots","Grand Rapids, Michigan footwear firm (Wolverine World Wide) behind the 1000 Mile boot.",W+"Wolverine_World_Wide",["1000 Mile"]),
 B("Alden","United States","1884","Goodyear-welted shoes and boots","Massachusetts shoemaker founded by Charles H. Alden, still family run.","https://www.stitchdown.com/brands/alden/alden-indy-boot-three-year-review/",["Indy"]),
 B("Viberg","Canada","1931","Heritage boots","Canadian bootmaker started by Edwin Viberg in Saskatchewan; known for stitchdown boots.","https://www.stitchdown.com/brands/viberg-boots/viberg-service-complete-history/",["Service Boot"]),
 B("Grant Stone","United States","","Heritage boots","American heritage boot brand.","knowledge",["Diesel"]),
 B("White's","United States","1853","Handmade work and logger boots","Spokane, Washington bootmaker known for boots for wildland firefighters; owned by LaCrosse Footwear since 2014.","https://whitesboots.com/pages/our-legacy",["Smoke Jumper"],rel=["Danner","Nicks"]),
 B("Nicks","United States","1964","Handmade work and logger boots","Spokane bootmaker founded by Nikolai Blahuczyn, a former White's bootmaker.","https://nicksboots.com/blogs/blog/nicks-history-from-start-to-finish",["Robert"],rel=["White's"]),
 B("Wesco","United States","1918","Handmade work and engineer boots","West Coast Shoe Company, founded by John Henry Shoemaker in Oregon; later based in Scappoose.",GP,["Boss","Jobmaster"]),
 B("Chippewa","United States","","Work boots","Chippewa Falls, Wisconsin bootmaker believed to have originated the engineer boot.",ASME,["Chippewa engineer boot"]),
 B("Timberland","United States","1952","Outdoor and work boots","Abington, Massachusetts company, renamed The Timberland Company in 1978; its Yellow Boot dates from 1973.",W+"Timberland_(company)",["6-inch boot"],["Timberland PRO"]),
 B("Dr. Martens","United Kingdom","1947","Boots and shoes","Air-cushioned sole by Klaus Märtens and Herbert Funck, made in Britain by R. Griggs from 1960.",W+"Dr._Martens",["1460"]),
 B("John Lofgren","Japan","","Heritage boots and reproductions","Bootmaker whose products are made exclusively in Japan, known for reproductions of US military patterns.","https://blueowl.us/products/m43-service-shoe-boot-in-horween-chromexcel-natural-roughout",["M-43 service shoe"]),
 B("Danner","United States","1932","Outdoor, work and military boots","Bootmaker founded by Charles Danner, first for loggers; supplied US forces in WWII.","https://www.stuartslondon.com/blogs/blog/behind-the-iconic-danner-boots",rel=["White's"]),
 B("Corcoran","United States","","Military boots","J. F. Corcoran Shoe Company, whose name became a byword for US jump boots.",W+"Jump_boot",["Jump boot"]),
]
notes=("All 5 old kinds kept (Combat boot renamed Combat & military boot); Moc-toe and Logger boot added. Old Work boot models redistributed: Iron Ranger to Service boot, Logger and Robert/Jobmaster to Logger boot, Tempe Moc Toe to Moc-toe boot. "
 "Dropped Red Wing 'Heritage' range (repeated brand range; lives in brand register). M-43 Service Shoe moved from Service boot to Combat & military as an archetype with the Lofgren version. "
 "Left out (no retrievable source this session; patinaproject and alexcious returned 403, russellmoccasin 404, Wikipedia API 429, Firecrawl/Parallel out of credit): Thorogood and Russell moc-toes, Red Wing Logger as archetype, Iron Ranger origin decade, Wolverine 1000 Mile cap-toe, Marugo brand entry. "
 "Grant Stone brand from knowledge (country only). No tradition entry: jika-tabi tradition belongs to the Traditional footwear shelf.")
out={"kinds":kinds,"brands":brands,"traditions":[],"notes":notes}
p='work/A2/shelves/04_01.json'; os.makedirs('work/A2/shelves',exist_ok=True)
json.dump(out,open(p+'.tmp','w'),ensure_ascii=False,indent=1); os.replace(p+'.tmp',p); print('written')
