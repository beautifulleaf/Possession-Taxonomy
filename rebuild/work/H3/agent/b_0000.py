import sys; sys.path.insert(0,'work/I2/agent')
from put import put
U='https://en.wikipedia.org/wiki/'
O="https://www.babeland.com/sex-toys/c/3000/vibrators/"; R="https://www.orion.de/katalog/sextoys/vibratoren"
kinds=[
{"n":"Wand vibrator","a":"wand massager · 電マ · denma","d":"Long-handled vibrator with a large rounded head, for use on the outside of the body. A wand massager counts here only when its maker names sexual use; otherwise it is in Personal Care & Beauty.","t":["Corded (mains)","Rechargeable","Silicone head","Compact (mini, micro)"],
 "m":[["Magic Wand Original","Vibratex"],["Magic Wand Rechargeable","Vibratex"],["Magic Wand Plus","Vibratex"],["Magic Wand Mini","Vibratex"],["Magic Wand Micro","Vibratex"],["Doxy wand","Doxy"]],"r":[["Magic Wand","Vibratex"]],"s":O},
{"n":"Bullet vibrator","a":"pocket rocket · finger vibrator","d":"Small cylindrical vibrator with a rounded tip, for focused external stimulation.","t":["Finger-worn","Single speed","Rechargeable","Waterproof"],
 "m":[["Zee Bullet Vibrator","Dame"],["Classic Bullet Vibe","Je Joue"],["G-spot Bullet Vibe","Je Joue"],["Riot Bullet Vibrator","ROMP"],["Pocket Rocket","Doc Johnson"]],"s":O},
{"n":"Palm vibrator","a":"","d":"Vibrator shaped to rest in the palm, like a computer mouse, for external use.","t":["Silicone","Rechargeable"],"m":[["Plump Palm Vibrator","Vush"]],"s":"https://www.healthylife.com.au/products/vush-plump-palm-vibrator"},
{"n":"Flicking vibrator","a":"tongue-style vibrator","d":"Vibrator with a soft flicking tip that imitates oral stimulation.","t":["Flicking tip","Rechargeable"],"m":[["Klitty","SVAKOM"],["Oral Fun","You2Toys"]],"s":R},
{"n":"Wearable panty vibrator","a":"wearable vibrator","d":"Flat vibrator made to be worn in, or clipped to, underwear during use.","t":["Remote control","App control","Clip-on"],"s":O},
{"n":"Vibrating cushion","a":"","d":"Cushion or pad with a built-in vibrator that the user sits or lies on for stimulation on the outside of the body. A cushion that only positions the body is in Soft Furnishings.","t":["Pad","Wedge"],"s":"https://www.orion.de/katalog/sextoys/sexmoebel"},
]
def B(n,c,f,seg,kf,d,s): return {"n":n,"c":c,"f":f,"seg":seg,"kf":kf,"d":d,"s":s}
brands=[
 B("Vibratex","United States","","Specialist","Magic Wand","Napa, California firm; sole authorised US importer of the Hitachi wand since 2000, now selling it as Magic Wand.",U+"Vibratex"),
 B("Doxy","United Kingdom","2013","Premium","British-made wand","British-made mains wand brand, shown in 2013.",U+"Doxy_(vibrator)"),
 B("LELO","Sweden","2002","Premium","design-led toys","Stockholm company founded by industrial designers and an engineer.",U+"LELO"),
 B("We-Vibe","Canada","2003","Premium","couples toys","Standard Innovation brand; first app-connected model in 2014; merged with Womanizer in 2018.",U+"We-Vibe"),
 B("Womanizer","Germany","2014","Premium","air-pulse stimulation","Brand of the Lovehoney Group built on Pleasure Air Technology.",U+"Womanizer_(pressure_wave_vibrator)"),
 B("Lovehoney","United Kingdom","2002","Mainstream","own-brand range","Bath retailer with more than 400 own-brand products; Lovehoney Group since 2021.",U+"Lovehoney"),
 B("Fun Factory","Germany","1996","Premium","silicone toys","Bremen maker, taken over by Satisfyer in October 2024.",U+"Fun_Factory_(company)"),
 B("Lovense","Singapore","2010","Mainstream","app-controlled toys","Maker of remote and app-controlled devices.",U+"Lovense"),
 B("Satisfyer","Germany","","Mainstream","air-pulse stimulation","Mass-market maker; won the 2018 XBIZ Pleasure Products Company of the Year, and took over Fun Factory in 2024.","knowledge"),
]
put('H3','00_00',{"kinds":kinds,"brands":brands,"traditions":[],"notes":"Adam & Eve (3 wands) and The One (wand, bullet) padding dropped; Magic Wand line (Original, Rechargeable, Plus, Mini, Micro) kept as models under Vibratex, versions confirmed on the Hitachi Magic Wand page. Doxy added as leader with a retrieved page; Le Wand not on any retrieved page so left out. No independent test source found for wands (search gave lifestyle roundups only), so none cited. Finger vibrator is a type of Bullet vibrator. Neutral wording."})
