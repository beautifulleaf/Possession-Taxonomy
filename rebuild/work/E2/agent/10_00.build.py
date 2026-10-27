import json,os
U=dict(lzr="https://en.wikipedia.org/wiki/LZR_Racer",cs="https://en.wikipedia.org/wiki/Competitive_swimwear",
 malm="https://www.worldaquatics.com/news/3704436/taming-a-swimmers-wake-a-look-into-the-history-and-innovative-spirit-of-malmstem-ab",
 dry="https://en.wikipedia.org/wiki/Dryrobe",arena="https://en.wikipedia.org/wiki/Arena_(swimwear)",cobra="https://www.yourswimlog.com/?p=31719",
 aqua="https://collections.sea.museum/objects/19653/speedo-aquablade-goggles")
OLD="https://skipro.com/products/cobra_ultra_swipe_mirr_goggle"
def X(n,d,mk,y,s,v=(),a="",dt=""):
  return {"n":n,"a":a,"d":d,"mk":mk,"y":y,"s":U[s],"v":[dict(zip(("n","mk","y","d"),t)) for t in v],"dt":dt}
kinds=[
 {"n":"Swim goggles","a":"goggles","d":"Watertight goggles worn to protect the eyes and see clearly when swimming.",
  "t":["racing (low-profile)","training","open-water / triathlon (wide view)","Swedish (no gasket)","mirrored, tinted or clear lens","prescription","anti-fog"],"s":OLD,
  "x":[X("Swedish goggles","Gasket-free goggle without neoprene, adjusted by the user to fit the face; still made from the original moulds.","Malmsten","early 1970s","malm",a="Swedes"),
       X("Arena Cobra","Low-profile racing goggle with very thin lenses; later Swipe models renew the anti-fog coating by wiping the lens.","Arena","","cobra",
        [("Cobra","Arena","","original pool racing goggle"),("Cobra Ultra Swipe","Arena","",""),("Cobra Swipe","Arena","",""),("Cobra Swipe Tri","Arena","","open water"),("Cobra Edge Swipe","Arena","","")]),
       X("Speedo Aquablade","Racing goggle with leak-proof Futura gaskets and anti-fog metallic-coated lenses.","Speedo","c.1996","aqua")],
  "m":[["Python","Arena"],["Speed Socket 2.0","Speedo"],["Vanquisher 3.0","Speedo"],["S2","Sporti"],["Swimple","TYR"]]},
 {"n":"Competition swimsuit","a":"racing suit · tech suit","d":"Racing suit made for competitive swimming. Bikinis, trunks and beachwear are in Clothing.",
  "t":["tech suit","jammer","kneeskin","racing brief","open-back racing suit","training suit","drag suit"],"s":"https://www.allensswimwear.co.uk/racing-swimwear",
  "x":[X("Speedo LZR Racer","Polyurethane-panelled full-body racing suit; won most Beijing 2008 races and led to the 2010 ban on non-textile suits.","Speedo","2008","lzr",
        [("LZR Pro","Speedo","2008",""),("LZR Elite","Speedo","2008",""),("LZR Elite 2","Speedo","2014",""),("LZR X","Speedo","2015",""),
         ("Fastskin LZR Pure Intent 2.0","Speedo","","men's textile suit"),("Fastskin LZR Pure Valor 2.0","Speedo","","")],a="LZR",dt="kneeskin, jammer · open or closed back"),
       X("Arena Powerskin","Arena's racing kneeskin and jammer line.","Arena","","cs",
        [("Powerskin Carbon-AIR2","Arena","",""),("Powerskin Air 3","Arena","",""),("Powerskin Primo","Arena","",""),("Powerskin Veloce","Arena","","")])],
  "r":[["Fastskin","Speedo"],["Powerskin","Arena"]]},
 {"n":"Swim cap","a":"swimming cap","d":"Silicone, latex or fabric cap worn for swimming.","t":["silicone","latex","lycra","dome racing cap","long-hair cap"],"s":OLD},
 {"n":"Kickboard","a":"float","d":"Foam board held in front for kick-only swim training.","s":OLD},
 {"n":"Pull buoy","a":"","d":"Foam float held between the legs for arm-only swim training.","s":OLD},
 {"n":"Changing robe","a":"change robe · dryrobe","d":"Oversized hooded robe, often with a waterproof shell and fleece or towelling lining, for changing and keeping warm outdoors.",
  "t":["long or short sleeve","waterproof shell","towelling robe","poncho"],"s":"https://diveshoponline.co.uk/product/dryrobe-advance-long-sleeve-changing-robe-burgundy-grey/",
  "x":[X("Dryrobe Advance","Waterproof, lined changing robe made popular by surfers; the brand name became the general word for the type.","Dryrobe","2010","dry",
        [("Dryrobe Advance","Dryrobe","2010",""),("Dryrobe Lite","Dryrobe","2023","for triathletes")])],
  "m":[["EVO Pro","Red Original"],["Pursuit","Red Original"]]}]
def B(n,c,seg,kf,d,f="",s="knowledge"):
  b={"n":n,"c":c,"seg":seg,"kf":kf,"d":d,"s":s}
  if f:b["f"]=f
  return b
brands=[B("Speedo","Australia","Professional & flagship","swimwear","Swimwear brand, maker of the LZR Racer and Fastskin suits."),
 B("Arena","Italy","Professional & flagship","competition swimwear","Swimwear maker founded by Horst Dassler, based in Tolentino, owned by Descente.","1973",s=U["arena"]),
 B("TYR","United States","Mainstream","swimwear","American swimwear and goggle brand."),
 B("Malmsten","Sweden","Heritage manufactory","Swedish goggles, lane lines","Family firm in Åhus making Swedish goggles and racing lane lines.",s=U["malm"]),
 B("Dryrobe","United Kingdom","Specialist","changing robes","Changing-robe maker founded by surfer Gideon Bright, based in Barnstaple.","2010",s=U["dry"]),
 B("Red Original","United Kingdom","Mainstream","changing robes, paddleboards","British paddle-sports brand of Red Paddle Co.")]
notes=("All 6 planned kinds kept. No retrieved page for Speedo Biofuse, Mizuno, Finisterre or Charlie McLeod robes, Arena Carbon year, Red Original robe history, so these stay out or as plain models. "
 "Swim cap, kickboard and pull buoy are QoL kinds with types only. Speedo founding facts left out of register (knowledge entry kept minimal).")
out={"kinds":kinds,"brands":brands,"traditions":[],"notes":notes}
p="work/E2/shelves/10_00.json";json.dump(out,open(p+".tmp","w"),ensure_ascii=False,indent=1);os.replace(p+".tmp",p)
