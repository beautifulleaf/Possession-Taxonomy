import json,os
U=dict(aql="https://en.wikipedia.org/wiki/Aqua-Lung",bpw="https://en.wikipedia.org/wiki/Backplate_and_wing",orca="https://en.wikipedia.org/wiki/Orca_Edge",
 jet="https://divernet.com/scuba-gear/scubapro-jet-fin-now-in-camouflage/",sw="https://en.wikipedia.org/wiki/Shearwater_Research",dc="https://en.wikipedia.org/wiki/Dive_computer",
 bcd="https://en.wikipedia.org/wiki/Buoyancy_compensator_(diving)",reg="https://en.wikipedia.org/wiki/Diving_regulator",cyl="https://en.wikipedia.org/wiki/Diving_cylinder",
 gar="https://www.garmin.com/en-US/blog/outdoor/introducing-the-descent-mk1-our-first-dive-computer/",aq4="https://www.scuba.com/p-mrsfa4xobrg/mares-avanti-quattro-4x-open-heel-fins-orange-black-regular",
 riffe="https://www.picketfencemedia.com/sanclementetimes/archives/shoot-to-thrill/article_f22a78e2-b8e8-578b-bdc7-37bc5669d54d.html",ra="https://www.divein.com/review/rob-allen-tuna-railgun/")
OLD="https://skipro.com/products/cobra_ultra_swipe_mirr_goggle"
def X(n,d,mk,y,s,v=(),a="",dt=""):
  return {"n":n,"a":a,"d":d,"mk":mk,"y":y,"s":U[s],"v":[dict(zip(("n","mk","y","d"),t)) for t in v],"dt":dt}
kinds=[
 {"n":"Diving mask","a":"dive mask · snorkelling mask","d":"Mask with a glass lens and nose pocket made for diving and snorkelling.",
  "t":["single lens","twin lens","frameless","low-volume freediving","prescription lenses","full-face snorkel mask"],"s":"https://oceanicdivecenter.com/dive-gear/masks-snorkels/masks",
  "m":[["Crystal Vu","Scubapro"],["Frameless (Gorilla)","Scubapro"],["Solo","Scubapro"],["Fino","Scubapro"],["F-Dual","Cressi"],["Zero 3","Omer"],["Alien","Omer"],
       ["Covert","Deep Blue"],["Angel","Seac Sub"],["Boss","Seac Sub"],["Iena","Seac Sub"]]},
 {"n":"Snorkel","a":"","d":"Breathing tube with mouthpiece for swimming face-down at the surface.","t":["J-type","flexible","dry-top","semi-dry","freediving"],"s":OLD},
 {"n":"Swim fins","a":"fins · flippers","d":"Rubber, plastic or composite fins worn on the feet for swimming, snorkelling or diving.",
  "t":["full-foot","open-heel with boot","spring strap","vented","channel","split","long-blade freediving","monofin"],"s":OLD,
  "x":[X("Scubapro Jet Fin","Heavy vented open-heel rubber fin, unchanged in essentials since 1965 and favoured by technical and military divers.","Scubapro","1965","jet",
        [("Jet Fin","Scubapro","1965",""),("Jet Fin with spring strap","Scubapro","","stainless steel spring strap"),("Jet Fin camouflage","Scubapro","","")],dt="sizes M–2XL · colours"),
       X("Mares Avanti Quattro","Open-heel fin whose blade has four channels to guide water.","Mares","","aq4",
        [("Quattro","Mares","",""),("Quattro+","Mares","",""),("Avanti Quattro 4X","Mares","","")])]},
 {"n":"Regulator","a":"scuba regulator · demand valve","d":"Valve set that cuts high cylinder pressure down to breathable pressure on demand.",
  "t":["single-hose two-stage","twin-hose","piston or diaphragm first stage","balanced or unbalanced","environmentally sealed (cold water)","DIN or yoke","octopus","sidemount set"],"s":U["reg"],
  "x":[X("Aqua-Lung","Cousteau and Gagnan's demand regulator, the foundation of all scuba regulators.","Aqualung","1943","aql",
        [("Aqua-Lung prototype","","1943","twin-hose, patented 1943"),("CG45","Aqualung","1945","first sold as Aqua-Lung, made by La Spirotechnique"),("Mistral","Aqualung","1955","twin-hose"),("Mistral (modern)","Aqualung","2005","re-issued twin-hose")],a="scaphandre autonome"),
       X("Porpoise","Early two-stage single-hose regulator from Australia.","","1948–52","reg",[("Porpoise","","1948–52","Ted Eldred")])],
  "m":[["TX100","Apeks"],["Cyklon 5000","Poseidon"]]},
 {"n":"BCD","a":"buoyancy compensator · BC · stab jacket · wing","d":"Inflatable jacket or wing that lets a diver adjust buoyancy underwater and float at the surface.",
  "t":["jacket (stab)","back-inflation","backplate and wing","sidemount","horse-collar","weight-integrated","travel"],"s":U["bcd"],
  "x":[X("Fenzy ABLJ","Horse-collar adjustable buoyancy life jacket, the first widely used buoyancy compensator.","","1961","bcd",[("ABLJ","","1961","Maurice Fenzy; later with own inflation cylinder")],a="horse-collar"),
       X("Control Buoyancy Jacket","Early jacket-style buoyancy compensator.","","1969","bcd",[("CBJ","","1969","Waverly Air Products, Chemung, NY")]),
       X("Backplate and wing","Modular rig of steel or aluminium plate, harness, wing bladder and cam bands, from Florida cave diving.","","1979","bpw",
        [("Flanagan backplate","","1979","Greg Flanagan"),("Hogarthian rig","","","William Hogarth Main, Woodville Karst Plain Project")],a="BP/W",dt="plate steel, aluminium or carbon · single or twin wing")]},
 {"n":"Dive computer","a":"decompression computer","d":"Wrist or console instrument that tracks depth and time and shows the diver's decompression status.",
  "t":["watch-style","wrist","console","air-integrated (hose or wireless)","technical / trimix","freediving mode"],"s":U["dc"],
  "x":[X("Orca Edge","The first commercially viable personal decompression computer.","Orca","1983","orca",[("Edge","Orca","1983","12-tissue bar display")]),
       X("Shearwater Perdix","Wrist-mounted technical dive computer from Shearwater.","Shearwater","2015","sw",[("Petrel","Shearwater","c.2013",""),("Perdix","Shearwater","2015",""),("Teric","Shearwater","2018","first watch format"),("Peregrine","Shearwater","","")]),
       X("Garmin Descent","Watch-style dive computer with surface GPS, Garmin's first.","Garmin","2017","gar",[("Descent Mk1","Garmin","2017","steel or titanium; up to six gases")])],
  "m":[["D9","Suunto"],["iX3M","Ratio"]]},
 {"n":"Dive cylinder","a":"scuba tank · diving cylinder · bottle","d":"High-pressure steel or aluminium bottle holding the diver's breathing gas.",
  "t":["aluminium (Al80)","steel","12 L / 15 L","232 or 300 bar","DIN or yoke valve","twin set (manifolded or independent)","pony / stage"],"s":U["cyl"]},
 {"n":"Speargun","a":"","d":"Underwater gun powered by rubber bands or compressed air that fires a spear at fish.",
  "t":["band-powered (arbalete)","pneumatic","wooden","railgun","roller","reel"],"s":"https://www.divein.com/diving/speargun/",
  "x":[X("Riffe wooden speargun","Speargun with a resin-glued teak stock, built in San Clemente by Jay Riffe.","Riffe","1980","riffe",[("Bluewater Elite","Riffe","","")],dt="teak stock · band count · length"),
       X("Rob Allen Railgun","South African band speargun with an aircraft-grade aluminium barrel.","Rob Allen","","ra",[("Tuna Railgun","Rob Allen","","five lengths, 80–140 cm")])],
  "m":[["Mahogany Special","A.B. Biller"],["Espadon Sport","Beuchat"],["Comanche","Cressi"],["SL Star","Cressi"],["Evolution 2","Hammerhead Spearguns"],["Carbine D7","JBL Spearguns"],
       ["Battle Axe 48","Koah"],["Cyrano 1.1 HFT","Mares"],["Sten Pneumatic","Mares"],["Viper Pro","Mares"],["Sniper Roller","Pathos"]]}]
def B(n,c,seg,kf,d,f="",s="knowledge"):
  b={"n":n,"c":c,"seg":seg,"kf":kf,"d":d,"s":s}
  if f:b["f"]=f
  return b
brands=[B("Aqualung","France","Heritage manufactory","regulators","Diving-gear maker descended from La Spirotechnique, Air Liquide's division that made the Cousteau–Gagnan Aqua-Lung.",s=U["aql"]),
 B("Scubapro","United States","Professional & flagship","regulators, fins","American diving-equipment maker, maker of the Jet Fin.",s=U["jet"]),
 B("Mares","Italy","Mainstream","dive gear","Italian diving and spearfishing equipment maker."),
 B("Cressi","Italy","Mainstream","masks, fins","Italian diving and snorkelling equipment maker."),
 B("Apeks","United Kingdom","Specialist","regulators","British regulator maker."),
 B("Orca","United States","Specialist","dive computers","Maker of the Orca Edge dive computer.",s=U["orca"]),
 B("Shearwater","Canada","Specialist","dive computers","Dive-computer maker founded by Bruce Partridge in Richmond, British Columbia.","2004",s=U["sw"]),
 B("Suunto","Finland","Professional & flagship","dive computers, compasses","Finnish instrument maker of dive computers and sports watches."),
 B("Garmin","United States","Professional & flagship","GPS and sonar","Navigation-electronics maker; its first dive computer was the Descent Mk1.",s=U["gar"]),
 B("Riffe","United States","Specialist","wooden spearguns","Speargun maker started in a San Clemente garage by Jay Riffe.","1980",s=U["riffe"]),
 B("Rob Allen","South Africa","Specialist","railgun spearguns","South African speargun maker.",s=U["ra"]),
 B("Pathos","Italy","Specialist","spearguns","Italian spearfishing equipment maker.")]
notes=("All 8 planned kinds kept or created (4 new: Regulator, BCD, Dive computer, Dive cylinder, sourced to Wikipedia). No retrieved page for Scubapro/Apeks/Atomic regulator families, Suunto dive-computer history, "
 "Mares Avanti Quattro dates, Beuchat Jetfin origin or Pathos, so those stay as models or are omitted. Old speargun list kept as models; Tuna Railgun and Bluewater Elite became versions.")
out={"kinds":kinds,"brands":brands,"traditions":[],"notes":notes}
p="work/E2/shelves/10_01.json";json.dump(out,open(p+".tmp","w"),ensure_ascii=False,indent=1);os.replace(p+".tmp",p)
