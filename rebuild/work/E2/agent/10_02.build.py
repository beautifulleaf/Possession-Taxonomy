import json,os
U=dict(types="https://www.surfertoday.com/surfing/the-most-common-types-of-surfboards",thr="https://www.surfertoday.com/surfing/thruster-the-three-fin-surfboard-design-by-simon-anderson",
 fish="https://surfsimply.com/magazine/history-surfboard-design-fish",morey="https://www.surfertoday.com/bodyboarding/the-story-of-the-original-morey-boogie-board",
 oneill="https://www.surfertoday.com/surfing/jack-oneill-the-father-of-the-modern-wetsuit-dies-at-94",ws="https://www.surfersjournal.com/editorial/riders-of-the-storm/",
 fcs="https://en.wikipedia.org/wiki/FCS_(fins)",wax="https://en.wikipedia.org/wiki/Mr._Zog%27s_Sex_Wax",ci="https://shacc.emuseum.com/objects/7942/channel-islands-glass-slipper-model-board")
OLD="https://www.ridershack.com/collections/mens-wetsuits"
def X(n,d,mk,y,s,v=(),a="",dt=""):
  return {"n":n,"a":a,"d":d,"mk":mk,"y":y,"s":U[s],"v":[dict(zip(("n","mk","y","d"),t)) for t in v],"dt":dt}
kinds=[
 {"n":"Surfboard","a":"board","d":"Board ridden standing on breaking waves.",
  "t":["PU/polyester","epoxy","wooden","soft-top","single, twin, thruster or quad fins","round, squash, swallow or pin tail"],"s":"https://www.ridershack.com/collections/surfboards",
  "x":[X("Longboard","Long board, typically over 9 ft; the first surfboard of the modern era.","","","types",dt="length 9 ft and over · single fin or 2+1"),
       X("Malibu / funboard","Blend of longboard and shortboard, typically 6–8 ft.","","","types",a="mini-mal"),
       X("Shortboard","Board of about 5 ft 5 in to 6 ft 5 in born of the shortboard revolution of McTavish, Nat Young and Dick Brewer.","","","types"),
       X("Thruster","Square-tailed board with three like-sized fins; planes like a twin fin with the grip of a single fin.","Simon Anderson","1980","thr",
        [("Energy Surfboards thruster","Simon Anderson","1980","won Bells Beach and the Coca-Cola Surfabout in 1981")],a="tri-fin"),
       X("Fish","Short, wide, thick board with flat rocker, split tail and two keel fins, first a kneeboard design.","Steve Lis","1967","fish",
        [("Lis fish kneeboard","Steve Lis","1967","San Diego"),("MR twin fin","Mark Richards","","longer, narrower tail, upright twin fins"),("Lost modern fish","Lost Surfboards","1990s","Matt Biolos")]),
       X("Gun","Large narrow board shaped for big waves, 7–12 ft.","","","types"),
       X("Tow-in board","Short, narrow, low-area board for jet-ski-assisted big-wave surfing.","","","types"),
       X("Wavestorm","8 ft foam soft-top with a hard bottom, sold cheaply through Costco; called the world's best-selling surfboard.","Wavestorm","","ws",a="Costco board"),
       X("Channel Islands Glass Slipper","Al Merrick shortboard model with a very thin, turned-up nose.","Channel Islands","c.1990","ci")],
  "m":[["Power Tiger","Pyzel"],["Tiger Twin","Pyzel"],["Fish Mako","Torq"],["Long Classic","Torq"]]},
 {"n":"Wetsuit","a":"steamer · shorty","d":"Neoprene suit that insulates the wearer in water, for surfing, diving, triathlon and paddling; comes in different thicknesses.",
  "t":["full suit","spring suit / shorty","3/2, 4/3, 5/4 mm","chest zip, back zip or zipless","hooded","natural-rubber (Yulex)"],"s":"https://www.ridershack.com/collections/mens-wetsuits",
  "x":[X("O'Neill wetsuit","Cold-water surfing wetsuit from the Santa Cruz brand of Jack O'Neill, father of the modern wetsuit.","O'Neill","1952","oneill",
        [("Psycho Tech","O'Neill","",""),("Hyperfreak","O'Neill","",""),("Hyperfreak Fire","O'Neill","",""),("Epic","O'Neill","",""),("Heat","O'Neill","","")])],
  "m":[["Flash Bomb","Rip Curl"],["Flash Bomb Fusion","Rip Curl"],["E-Bomb","Rip Curl"],["Dawn Patrol","Rip Curl"],["Omega","Rip Curl"]]},
 {"n":"Bodyboard","a":"boogie board","d":"Short foam board ridden lying prone on waves.","t":["crescent or bat tail","PE, PP or EPS core","drop-knee","kids' board"],
  "s":"https://www.ebodyboarding.com/products/morey-pro-series-plc-mach-7-7-bodyboard",
  "x":[X("Morey Boogie","The first bodyboard, cut from polyethylene packing foam in Hawaii; first called S.N.A.K.E.","Morey","1971","morey",
        [("Original Boogie","Morey","1971",""),("Mach 7-7","Morey","","Pro Series")])]},
 {"n":"Surf fin","a":"fin","d":"Fin fitted to a surfboard's fin box.","t":["single","twin","thruster set","quad","keel","glass-on","fin box: FCS, FCS II, Futures, US box"],"s":OLD,
  "x":[X("FCS","Removable fin system with two-tab fins set in flush plugs, the de facto standard; designed by Brian Whitty.","FCS","1995","fcs",
        [("FCS","FCS","1995","screw-in, patented 7 Nov 1995"),("FCS Fusion","FCS","","pre-glass, for epoxy boards"),("FCS II","FCS","2013","tool-free")])]},
 {"n":"Surf leash","a":"leg rope · leash","d":"Cord that ties a surfboard to the rider's ankle.","t":["comp","regular","big-wave","longboard calf or knee leash"],"s":OLD,
  "x":[X("O'Neill leash","Surf leash developed by Pat O'Neill, son of Jack O'Neill.","O'Neill","","oneill")]},
 {"n":"Surf wax","a":"board wax","d":"Wax rubbed on a surfboard deck for grip.","t":["base coat","tropical","warm","cool","cold water"],"s":OLD,
  "x":[X("Sex Wax","Surf wax developed by Frederick 'Zog' Herzog and chemist Nate Skinner in Carpinteria, California.","Mr. Zog's Sex Wax","1972","wax",
        [("Quick Humps","Mr. Zog's Sex Wax","",""),("Really Tacky","Mr. Zog's Sex Wax","","")])]}]
def B(n,c,seg,kf,d,f="",s="knowledge"):
  b={"n":n,"c":c,"seg":seg,"kf":kf,"d":d,"s":s}
  if f:b["f"]=f
  return b
brands=[B("O'Neill","United States","Heritage manufactory","wetsuits","Santa Cruz surf brand of Jack O'Neill, pioneer of the cold-water wetsuit.","1952",s=U["oneill"]),
 B("Rip Curl","Australia","Mainstream","wetsuits","Australian surf brand from Torquay."),
 B("Morey","United States","Heritage manufactory","bodyboards","Tom Morey's Boogie brand, maker of the first bodyboard.",s=U["morey"]),
 B("FCS","Australia","Specialist","surf fins","Removable fin system company, part of Surf Hardware International.","1995",s=U["fcs"]),
 B("Mr. Zog's Sex Wax","United States","Heritage manufactory","surf wax","Surf-wax maker of Carpinteria, California.","1972",s=U["wax"]),
 B("Wavestorm","United States","Value","soft-top surfboards","Soft-top surfboard brand of AGIT, Irvine, California.",s=U["ws"]),
 B("Channel Islands","United States","Artisan & independent","shortboards","Santa Barbara surfboard label of shaper Al Merrick.",s=U["ci"]),
 B("Pyzel","United States","Artisan & independent","performance surfboards","Surfboard label of shaper Jon Pyzel."),
 B("Torq","","Value","epoxy surfboards","Moulded epoxy surfboard brand.")]
notes=("All 6 planned kinds kept. Shapes are maker-free archetypes except where an originator is attested. Not added for lack of a retrieved page: Lost/Mayhem, JS, Firewire, Hayden Shapes, Bing, Hobie, Donald Takayama, "
 "Patagonia Yulex, Billabong, Xcel, C-Skins, Futures, Sticky Bumps. Thruster/Fish mk hold originating shapers (no register entries for persons).")
out={"kinds":kinds,"brands":brands,"traditions":[],"notes":notes}
p="work/E2/shelves/10_02.json";json.dump(out,open(p+".tmp","w"),ensure_ascii=False,indent=1);os.replace(p+".tmp",p)
