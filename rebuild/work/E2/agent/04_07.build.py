import json,os
CO="https://www.chronofhorse.com/article/virginia-tech-releases-highly-anticipated-helmet-ratings"
BETA="https://beta-uk.org/wp-content/uploads/2025/10/Body-Protector-Manufacturers-Leaflet-2018-Standard-Oct-25.pdf"
YH="https://www.yourhorse.co.uk/buying-guides/air-jackets/"
HR="https://www.horseandrideruk.com/gear-guide/buying-guides/rider-wear-and-accessories/body-protection/reviews/airowear-airmesh2"
K=lambda b,d:dict(b,**d)
kinds=[
 {"n":"Riding hat","a":"riding helmet · equestrian helmet","d":"Helmet made for horse riding, certified to an equestrian helmet standard.",
  "t":["skull cap","peaked helmet","MIPS / rotational system","standard: VG1, PAS 015, ASTM F1163"],
  "s":"https://www.doversaddlery.com/collections/riding-helmets",
  "m":[["Revolve X-Air MIPS","Champion"],["AYR8 Plus","Charles Owen"],["My PS","Charles Owen"],["Kylo","Charles Owen"],
       ["Shadowmatt 2.0","Samshield"],["Miss Shield 2.0","Samshield"],["Star Lady Hunter","Kask"],["Sport 2.0","Troxel"],["Spirit","Troxel"],
       ["Defender","One K"],["Avance","One K"],["Sync","Ovation"],["Sportage Hybrid","Tipperary"],["Pardus","Trauma Void"],
       ["Equi-Lite DFS","IRH"],["Carbon Fiber","TuffRider"],["Crown MIPS","Equinavia"]]},
 {"n":"Equestrian body protector","a":"riding body protector · air jacket · air vest","d":"Padded vest or airbag jacket worn by a rider to protect the torso and spine in a fall.",
  "t":["foam body protector (BETA 2018 Level 1–3)","air vest / air jacket","shoulder protector"],"s":BETA,
  "m":[["RS 2010","Racesafe"],["Motion","Racesafe"],["AirMesh2","Airowear"],["Shadow","Airowear"],["Ti22","Champion"],
       ["Superflex","Gatehouse"],["X'Air Safe","Freejump"],["Faze","Fomo"],["Equine Proair","Point Two"],["Zip'In 2","Helite"],["Airbag Vest","Horse Pilot"]]},
 {"n":"Shin guard","a":"shin pad","d":"Rigid or padded guard worn over the shin in sport.","s":"https://www.galaxus.ch/en/s3/producttype/football-shin-guards-1351",
  "t":["slip-in","ankle-guard","sleeve"],"m":[["Mercurial Lite","Nike"],["Tiro Match","adidas"]]},
 {"n":"Knee pad","a":"","d":"Padded guard worn over the knee to protect it in sport.","s":"https://www.academy.com/p/mizuno-elite-9-sl2-volleyball-knee-pads",
  "m":[["Elite 9 SL2","Mizuno"]]},
 {"n":"Mouthguard","a":"gum shield","d":"Moulded guard worn over the teeth to protect them in contact sports.","t":["boil-and-bite","self-fit","custom (dentist-made)"],
  "s":"https://www.gilbertrugby.com/blogs/news/the-new-gilbert-rugby-ball-range-for-2026",
  "m":[["Self-Fit Gold","OPRO"],["Max 2.4","SISU"],["Shock Doctor Pro","Shock Doctor"],["Academy Mouthguard","Gilbert"],["Intro","SAFEJAWZ"],["Predator","Venum"]]},
 {"n":"Protective cup","a":"athletic cup · box","d":"Rigid cup worn over the groin, alone or in a jock or jill supporter, to protect it in contact and ball sports.",
  "s":"https://www.hockeymonkey.com/ice-hockey/jock-jill/mens/shock-doctor-hockey-jock-ultra-pro-carbon-flex-cup-sr.html",
  "m":[["Ultra Pro Carbon Flex Cup","Shock Doctor"]]},
]
def B(n,c,seg,kf,d,f="",s="knowledge"):
  b={"n":n,"c":c,"seg":seg,"kf":kf,"d":d,"s":s}
  if f:b["f"]=f
  return b
brands=[
 B("Charles Owen","United Kingdom","Heritage manufactory","riding hats","Welsh maker of riding hats and, through Airowear, body protectors.","1911"),
 B("Samshield","France","Premium","riding helmets","French maker of premium customisable riding helmets."),
 B("Kask","Italy","Premium","helmets","Italian helmet maker for cycling, riding, skiing and industry.","2004"),
 B("Champion","United Kingdom","Mainstream","riding hats","British maker of riding hats and body protectors; its Revolve X-Air MIPS topped Virginia Tech's first equestrian helmet ratings.",s=CO),
 B("Troxel","United States","Mainstream","riding helmets","American maker of everyday riding helmets."),
 B("IRH","United States","Value","riding helmets","American riding-helmet brand; its Equi-Lite placed in the top three of Virginia Tech's first equestrian helmet ratings.",s=CO),
 B("TuffRider","United States","Value","riding wear","American equestrian apparel brand; its Carbon Fiber helmet placed in the top three of Virginia Tech's first ratings.",s=CO),
 B("Racesafe","United Kingdom","Specialist","body protectors","British maker of BETA Level 3 racing and riding body protectors.",s=BETA),
 B("Airowear","United Kingdom","Specialist","body protectors","Body-protector brand of Charles Owen.",s=BETA),
 B("Point Two","United Kingdom","Specialist","air jackets","Maker of inflating air jackets for riders.",s=YH),
 B("Helite","France","Specialist","airbag vests","French maker of airbag vests for riders and motorcyclists.",s=YH),
 B("Shock Doctor","United States","Mainstream","mouthguards","American maker of sports mouthguards, cups and protective gear."),
 B("OPRO","United Kingdom","Mainstream","mouthguards","British maker of self-fit and custom mouthguards."),
 B("SISU","Denmark","Specialist","thin mouthguards","Maker of thin, mouldable sports mouthguards.")]
notes=("All five old kinds kept; Equestrian body protector added (BETA 2018 manufacturer list, air-jacket and Airowear review pages). "
 "Riding hat cut from 25 to 17 models: kept main lines of Charles Owen, Samshield, Kask, Troxel, One K, Ovation, Tipperary, Trauma Void, Equinavia and added the Virginia Tech top three "
 "(Champion Revolve X-Air MIPS, TuffRider Carbon Fiber, IRH Equi-Lite); dropped duplicate older lines (Halo, JR8 Plus, CCS, Deluxe Schooler, M Class, Royal, Sportage 8500, Windsor, Lynx, TuffRider Starter). "
 "No Uvex or Gatehouse helmet models (no retrieved page named one). Shin-guard tier stays thin (Nike, adidas only; no SISU/OPRO shin-guard model retrieved). Brand facts marked knowledge where well known; uncertain founding years omitted.")
out={"kinds":kinds,"brands":brands,"traditions":[],"notes":notes}
p="work/E2/shelves/04_07.json";json.dump(out,open(p+".tmp","w"),ensure_ascii=False,indent=1);os.replace(p+".tmp",p)
