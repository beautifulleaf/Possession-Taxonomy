import json, os
def w(code, job, obj):
    p = f'/home/user/Possession-Taxonomy/rebuild/work/{code}/shelves/{job}.json'
    t = p + '.tmp'; json.dump(obj, open(t, 'w'), ensure_ascii=False, indent=1); os.replace(t, p)
def X(n,d,mk,y,s,v=(),dt="",a=""):
    return {"n":n,"a":a,"d":d,"mk":mk,"y":y,"s":s,"v":[{"n":a1,"mk":b,"y":c,"d":e} for a1,b,c,e in v],"dt":dt}
IK="https://www.iksurfmag.com/?p="
PK="https://en.wikipedia.org/wiki/Power_kite"
WF="https://en.wikipedia.org/wiki/Wing_foiling"
WS="https://en.wikipedia.org/wiki/Windsurfing"
AR="https://realwatersports.com/blogs/news/what-is-the-best-armstrong-foil-for-wing-surfing"
kinds=[
 {"n":"Kitesurf kite","a":"kiteboarding kite · LEI kite","d":"Large steerable kite made to pull a rider on a board across water.",
  "t":["leading-edge inflatable (LEI)","foil (ram-air) kite","delta / C / bow / hybrid shape","3-strut, 1-strut or strutless","4- or 5-line"],
  "s":"https://www.kitemana.com/kite?sz=1000",
  "x":[
   X("Leading-edge inflatable kite","Single-skin kite held in shape by an inflated tube along the leading edge and ribs; keeps its shape when wet.","","1984",PK,
     [("inflatable kite patent","Bruno and Dominique Legaignoux","1984","patented November 1984")],"tube count · canopy cloth · line count"),
   X("Bandit","Delta C-shape kite built for depower, stability and easy relaunch; widely copied by other brands.","F-One","2008",IK+"22565",
     [("Bandit","F-One","2008","first delta-style kite"),("Bandit Dos","F-One","2009","more C-kite feel, wider wind range")],"sizes · canopy cloth"),
   X("Switchblade","Moderate-aspect allround kite designed by Pat Goodman; among the best-selling kite models.","Cabrinha","",
     "https://www.mackiteboarding.com/news/brazilian-brothers-cabrinha-2026-switchblade-kite-review/",
     [("Switchblade Apex","Cabrinha","",""),("Switchblade","Cabrinha","2026","")],"sizes · bar system"),
   X("Evo","Allround kite designed by Ralf Grösel, first aimed at schools and beginners.","Duotone","2008",
     "https://www.duotonesports.com/en/ch/kiteboarding/stories/stories/interview-with-the-evo-kite-designer-ralf-groesel",
     [("Evo","Duotone","2008","original"),("Evo SLS","Duotone","","Penta TX construction"),("Evo D/LAB","Duotone","2023","Aluula construction")],"sizes · construction (standard, SLS, D/LAB)"),
   X("Edge","Ozone's longest-running kite: a fast boosting freeride, big-air and race kite designed by Rob Whittall.","Ozone","2007",IK+"170784",
     [("Instinct Edge","Ozone","2007","five-line, active fifth line"),("Edge V11","Ozone","2022","")],"sizes · version number"),
   X("RPM","Open-C, short-bridle crossover kite between Slingshot's Fuel and Rev; won freestyle world titles.","Slingshot","2009",IK+"22419",
     [("RPM","Slingshot","2009","")],"sizes"),
   X("Orbit","Big-air kite with swept wingtips and a flatter canopy.","North","",
     "https://www.mackiteboarding.com/news/2021-north-kites-overview/",[("Orbit","North","2021","more balanced low end")],"sizes"),
   X("Reach","Allround kite for surfing, big air, foiling and freeride.","North","",
     "https://www.mackiteboarding.com/news/2021-north-kites-overview/",[("Reach","North","2021","")],"sizes"),
  ],
  "m":[["Pace PRO","Core Kiteboarding"],["XR8","Core Kiteboarding"],["Rebel D/LAB","Duotone"],["Vegas","Duotone"],["Trigger","F-One"],
       ["Heli","Flysurfer"],["Hybrid","Flysurfer"],["Flow","Harlem Kitesurfing"],["Pivot","Naish"],["Carve","North"],
       ["Enduro V5","Ozone"],["Vortex V2","Ozone"],["Super Model","Reedin Kiteboarding"],["RS","Eleveight"]]},
 {"n":"Kiteboard","a":"twin-tip · kite surfboard","d":"Twin-tip or directional board ridden while pulled by a kite.",
  "t":["twin-tip","directional (kite surfboard)","freestyle / wakestyle","light-wind"],"s":"https://oceanaddicts.com.au/?p=8062"},
 {"n":"Kite control bar","a":"control bar · bar and lines","d":"Bar with lines and safety release used to steer one kite.",
  "t":["4-line","5-line","quick-release safety","fixed or adjustable bar length"],"s":"https://oceanaddicts.com.au/?p=8062"},
 {"n":"Kite harness","a":"","d":"Waist or seat harness that hooks the rider to the kite bar.",
  "t":["waist harness","seat harness","hard-shell waist harness","spreader bar or hook"],"s":"https://oceanaddicts.com.au/?p=8062"},
 {"n":"Traction kite","a":"power kite · land kite · trainer kite","d":"Steerable kite made to pull a rider on land (on a buggy, board or skis) or to train for kite sports.",
  "t":["ram-air foil","two-line or four-line","fixed-bridle or depowerable","trainer kite","snowkite"],"s":"http://www.powerkiter.fr/en/7-powerkites",
  "x":[
   X("Flexifoil","Two-line ram-air foil stunt and power kite with a carbon spar in the leading edge, invented by Ray Merry and Andrew Jones.","Flexifoil","1972",
     "https://my-best-kite.com/flexifoil.html",
     [("Hot Shot 4","Flexifoil","","4 ft span"),("Stacker 6","Flexifoil","","original design in modern materials, 6 ft span"),
      ("Pro-Team 8","Flexifoil","","8 ft span"),("Super 10","Flexifoil","","10 ft span")],"span in feet (number in name)"),
   X("Arc kite","Bridleless arch-shaped ram-air kite with valves that keep it inflated, for kiteboarding, buggying and snowkiting.","Peter Lynn","1999",
     "https://en.wikipedia.org/wiki/Peter_Lynn",[],"sizes"),
  ],
  "m":[["Wing X1","Aeryn"],["Hype Play","Cross Kites"],["Quattro","Cross Kites"],["Peak","Flysurfer"],["Pow","Flysurfer"],["Tao","Flysurfer"],
       ["Rush 5 Pro","HQ"],["Ignition V3","Ozone"],["Hornet","Peter Lynn"],["Twister","Peter Lynn"],["Ibex","Peter Lynn"]]},
 {"n":"Wing-foil wing","a":"wing · foil wing · wing surfer","d":"Hand-held inflatable wing that powers a rider on a foil board.",
  "t":["inflatable leading edge and strut","handles or boom","with or without windows"],"s":"https://www.kblsports.com.au/wind-wings/",
  "x":[
   X("Foilwing","First marketed inflatable wing, designed by Ken Winner after Flash Austin's 2018 tests in Maui.","Duotone","2019",WF,
     [("Unit","Duotone","",""),("Float","Duotone","",""),("Ventis","Duotone","",""),("Stash","Duotone","","")],"sizes 2.2–9 m²"),
   X("Slingwing","Wing developed from Tony Logosz's 2011 prototypes, tested on a windfoil board in the Columbia Gorge.","Slingshot","2011",WF,
     [("Slingwing","Slingshot","","")],"sizes"),
   X("Strike","Stiffer, more structured successor to F-One's first wing, the Swing, with two long handles.","F-One","2021","https://www.tonicmag.com/?p=37362",
     [("Swing","F-One","","predecessor, multiple hand positions"),("Strike","F-One","2021","")],"sizes"),
  ],
  "m":[["X-Wing","Armstrong"],["XPS MkII","Armstrong"],["Mantis","Cabrinha"],["ADX Nvision","Naish"],["Mode Pro","North"],["Nova Pro","North"],
       ["Flux","Ozone"],["Supernatural","Reedin Kiteboarding"]]},
 {"n":"Hydrofoil","a":"foil · foil set","d":"Mast, fuselage and wings fitted under a foilboard.",
  "t":["front wing (low or high aspect)","stabiliser (tail)","mast length","fuselage length","aluminium or carbon"],"s":"https://oceanaddicts.com.au/?p=8062",
  "x":[
   X("Armstrong HS","High-speed front-wing series balancing speed, turning, pumping and low-speed lift.","Armstrong","",AR,
     [("HS1850","Armstrong","",""),("HS1550 v2","Armstrong","",""),("HS1250","Armstrong","",""),("HS1050","Armstrong","",""),("HS850","Armstrong","","")],"wing area cm² (number in name)"),
   X("Armstrong CF","Low-aspect carving freeride series with plenty of low-speed lift; easy to learn on.","Armstrong","",AR,
     [("CF2400 v2","Armstrong","","beginner")],"wing area cm²"),
   X("Armstrong HA","High-aspect series for glide, upwind and downwind speed.","Armstrong","",AR,[],"wing area cm²"),
  ]},
 {"n":"Foilboard","a":"foil board","d":"Short buoyant board made to carry a hydrofoil for wing, kite or surf foiling.",
  "t":["wing foil board","kite foil board","surf / prone foil board","downwind board","mid-length"],"s":"https://oceanaddicts.com.au/?p=8062"},
 {"n":"Windsurf board","a":"sailboard · windsurfer","d":"Board carrying a free-pivoting mast and sail that the rider stands on and steers.",
  "t":["longboard (daggerboard)","beginner / funboard","freeride","slalom","speed","Formula","freestyle","wave","windfoil"],"s":WS,
  "x":[
   X("Windsurfer","Original sailboard of Jim Drake and Hoyle Schweitzer, basis of a one-design class.","Windsurfing International","1968",WS,
     [("Windsurfer LT","","","")],""),
   X("Mistral One Design","One-design board chosen as the Olympic class in 1992.","Mistral","1992",WS,[],""),
   X("RS:X","Olympic one-design board and rig designed by Jean Bouldoires and Robert Stroj; Olympic class 2008–2020.","NeilPryde","2004",
     "https://en.wikipedia.org/wiki/RS:X",[],"286 × 93 cm, 231 L · sail 9.5 m² (men), 8.5 m² (women)"),
   X("iSonic","Starboard's slalom racing board range.","Starboard","","https://www.windsurf.co.uk/test/starboard-isonic-carbon-reflex-107l-2016-test-review",
     [("iSonic 107","Starboard","2016","Carbon Reflex or Wood construction")],"volume (litres) · construction"),
  ]},
 {"n":"Windsurf sail","a":"rig · sail","d":"Battened sail with mast sleeve and boom attachment that powers a windsurf board.",
  "t":["camber-induced","rotational (RAF)","wave","freestyle","freeride","race"],"s":WS,
  "x":[
   X("V8","NeilPryde race sail whose shape the Olympic RS:X sail is based on.","NeilPryde","","https://en.wikipedia.org/wiki/RS:X",
     [("RS:X sail","NeilPryde","2004","one-design Olympic sail")],"sail area m²"),
   X("Blade","Control-oriented five-batten all-round wave sail.","Severne","","https://www.windsurf.co.uk/?p=5353",
     [("Blade","Severne","2013","lighter and stronger; Spiderfibre strips")],"sizes · luff · boom length"),
  ]},
]
K="knowledge"
brands=[
 {"n":"Duotone","c":"Germany","seg":"Professional & flagship","kf":"kites, wings","d":"Kite, wing and windsurf brand of the Boards & More group, formerly North Kiteboarding.","sig":["Evo","Foilwing"],"rel":["North"],"s":K},
 {"n":"Cabrinha","c":"United States","seg":"Premium","kf":"kites","d":"Kiteboarding brand owned by Neil Pryde Ltd.","sig":["Switchblade"],"rel":["NeilPryde"],"s":"https://en.wikipedia.org/wiki/Neil_Pryde_Ltd."},
 {"n":"F-One","c":"France","seg":"Premium","kf":"kites, wings","d":"French kite, wing and foil brand founded by Raphaël Salles.","sig":["Bandit","Strike"],"s":K},
 {"n":"Slingshot","c":"United States","seg":"Premium","kf":"kites, wings","d":"Kite, wake and foil brand co-founded by Tony Logosz.","sig":["RPM","Slingwing"],"s":WF},
 {"n":"Ozone","c":"France","seg":"Premium","kf":"kites, paragliders","d":"Paraglider maker whose kite division (Ozone Kites) followed in 2001.","sig":["Edge"],"s":K},
 {"n":"North","seg":"Premium","kf":"kites","d":"North Kiteboarding, relaunched kite brand of the North name.","sig":["Orbit","Reach"],"rel":["Duotone"],"s":K},
 {"n":"Flexifoil","c":"United Kingdom","f":"1972","seg":"Specialist","kf":"power kites","d":"British power-kite brand built on the Merry and Jones foil kite.","sig":["Flexifoil"],"s":"https://my-best-kite.com/flexifoil.html"},
 {"n":"Peter Lynn","c":"New Zealand","f":"1971","seg":"Specialist","kf":"traction kites, buggies","d":"Kite maker founded by Peter and Elwyn Lynn in Ashburton; pioneer of kite buggying.","sig":["Arc kite"],"s":"https://en.wikipedia.org/wiki/Peter_Lynn"},
 {"n":"Armstrong","c":"New Zealand","seg":"Premium","kf":"hydrofoils","d":"Armstrong Foils, hydrofoil and wing maker founded by Armie Armstrong.","sig":["Armstrong HS","Armstrong CF"],"s":AR},
 {"n":"Windsurfing International","c":"United States","f":"1968","seg":"Heritage manufactory","kf":"original sailboard","d":"Company of Jim Drake and Hoyle Schweitzer that made the original Windsurfer.","sig":["Windsurfer"],"s":WS},
 {"n":"Mistral","c":"Switzerland","seg":"Heritage manufactory","kf":"windsurf boards","d":"Windsurf board maker whose One Design was the Olympic class from 1992.","sig":["Mistral One Design"],"s":K},
 {"n":"NeilPryde","c":"Hong Kong","seg":"Professional & flagship","kf":"windsurf sails","d":"Windsurf sail brand of Hong Kong-based Neil Pryde Ltd, maker of the Olympic RS:X.","sig":["RS:X","V8"],"rel":["Cabrinha","JP-Australia"],"s":"https://en.wikipedia.org/wiki/Neil_Pryde_Ltd."},
 {"n":"Starboard","c":"Thailand","f":"1994","seg":"Professional & flagship","kf":"windsurf boards, SUP","d":"Windsurf and paddleboard maker founded by Svein Rasmussen in Thailand.","sig":["iSonic"],"s":"https://en.wikipedia.org/wiki/Svein_Rasmussen"},
 {"n":"Severne","c":"Australia","seg":"Premium","kf":"windsurf sails","d":"Windsurf sail maker.","sig":["Blade"],"s":K},
]
notes=("All 8 old kinds kept; 2 new kinds (Windsurf board, Windsurf sail) sourced to Wikipedia Windsurfing. Kitesurf kite: 28 flat models cut to archetypes + 14 models "
 "(dropped Hadlow Pro, Boxer, Hunt, Psycho, Hyper/Master/Whisper Model, FS, Stratos, WS as long-tail SKUs; Bandit, Switchblade Apex, Evo D/LAB, Orbit moved into archetypes). "
 "Traction kite: Impulse, Hype dropped (long tail). Wing: Unit, Float, Stash, Ventis, Strike, Swing, Slingwing moved into archetypes. "
 "Not done: Duotone Rebel/Neo, Core, Axis and Lift foils, F-One foils, JP/Fanatic boards, GA Sails as archetypes - no retrieved page gave line facts (Axis forum page had no series names; thekitemag F-One feature 403). "
 "Brand founding years left out where unsure;")
w('E2','10_03',{"kinds":kinds,"brands":brands,"traditions":[],"notes":notes})
