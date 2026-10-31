import json, os
def X(n,d,mk,y,s,v,dt,a=""):
    return {"n":n,"a":a,"d":d,"mk":mk,"y":y,"s":s,"v":[{"n":a_,"mk":b,"y":c,"d":e} for a_,b,c,e in v],"dt":dt}
W="https://en.wikipedia.org/wiki/"
L="https://www.lathes.co.uk/"
kinds=[
 {"n":"Metal lathe","a":"engineering lathe · model engineer's lathe","d":"Machine that turns metal with a fixed cutting tool on a carriage.",
  "t":["Micro / miniature lathe","Mini lathe","Bench lathe","Toolroom lathe","Gap-bed lathe"],
  "s":"https://www.grizzly.com/metal-lathes-and-mills",
  "x":[
   X("Myford ML7","British 3.5-inch model engineer's lathe; the archetypal home-workshop lathe.","Myford","1946",L.replace("www.","")+"myford-ml7",
     [["ML7","Myford","1946","designed by Ted Barrs; made until 1979"],["ML7B","Myford","","screwcutting gearbox"],
      ["Super 7","Myford","1953","successor with spindle clutch"],["ML7-R","Myford","","Super 7 basis without clutch"]],
     "3.5 in centre height · 20 in between centres · gearbox"),
   X("South Bend 9-inch","American home-workshop lathe with industrial accuracy; Boxford based its lathes on South Bend.","South Bend","1939",
     "https://collections.ingenium.ca/item/2001.0432.001/",
     [["Precision 9-inch Model A (444Z)","South Bend","1939","quick-change gearbox, power feeds"]],"bed length · drive · gearbox"),
   X("Atlas 10-inch","Kalamazoo-built hobby lathe, also sold by Sears as Craftsman.","Atlas","1934",L+"atlas",
     [["10-inch (first)","Atlas","1934",""],["10-D","Atlas","1936",""],["10-F","Atlas","1937","power cross-feed"],
      ["6-inch","Atlas","1937","made into the early 1980s"],["Craftsman 10-inch / 6-inch","Atlas","","sold by Sears, Roebuck"]],
     "swing 6–12 in · bed length"),
   X("Boxford lathe","Halifax-built South Bend-derived lathe, a fixture of British school workshops.","Boxford","1946",W+"Boxford_Lathe",
     [["A / AUD","Boxford","1946–1977","screw-cutting gearbox; UD = under-drive"],["B / BUD","Boxford","1948–1977","power cross-feed"],
      ["C / CUD","Boxford","1950–1977","manual cross-feed"],["ME10","Boxford","",""]],"drive mount · gearbox"),
   X("Hardinge HLV","Narrow-bed super-precision toolroom lathe, a coveted home-shop find.","Hardinge","late 1940s",L+"hardinge",
     [["HLV","Hardinge","late 1940s–c.1959","also built in Feltham, UK"],["HLV-H","Hardinge","c.1959","US serials 1960–1972"],["DV-59","Hardinge","","Five-Nine model shop lathe"]],
     "5.5 in centre height · 18 in between centres"),
   X("Unimat","Austrian miniature multi-purpose machine tool, about 300,000 made.","Emco","1953",L+"unimat/index.html",
     [["Unimat DB200","Emco","1953","US name"],["Unimat SL1000","Emco","","European name"],["Unimat 3","Emco","1977","successor"]],
     "iron or zamak base · accessories"),
   X("Sherline lathe","Aluminium-extrusion desktop lathe designed in Australia and made in the USA.","Sherline","1971",
     "https://sherline.com/sherline-history/",
     [["Model 1000","Sherline","1971","Ron Sher, Australia; designed by Harold Clisby"],["Model 4000","Sherline","late 1970s","Joe Martin, USA"]],
     "bed length · inch or metric · CNC-ready"),
   X("Taig micro lathe","2.25 x 9.75 in miniature lathe on a concrete-filled aluminium base.","Taig","",L+"taig",
     [["Taig lathe","Taig","",""],["Peatol","Taig","","UK name"],["Grimberg","Taig","","Netherlands name"]],"micro size · accessories")],
  "m":[["G0602","Grizzly"],["G0745","Grizzly"],["G8688","Grizzly"],["M1015","Shop Fox"]]},
 {"n":"Milling machine","a":"mill · knee mill · mini mill","d":"Machine that cuts metal with a rotating multi-tooth cutter against a movable table.",
  "t":["Turret (knee) mill","Bench mill","Mini mill","Mill-drill","CNC mill"],
  "s":"https://www.grizzly.com/metal-lathes-and-mills",
  "x":[
   X("Bridgeport turret mill","Vertical knee mill with turret, ram and quill head; originator of the turret mill.","Bridgeport","1938",W+"Bridgeport_(machine_tool_brand)",
     [["Serial No. 1","Bridgeport","1938","shipped to Precision Castings Corp."],["J-head","Bridgeport","",""],["2J head","Bridgeport","",""],["Series II","Bridgeport","","4 hp variable speed"]],
     "head type · table length · DRO or CNC"),
   X("Sieg X2 mini mill","Shanghai-built bench mini mill sold under many importer brands.","Sieg","",
     "https://makezine.com/article/digital-fabrication/machining/the-sieg-mini-mill-one-manufacturer-many-brands/",
     [["Central Machinery 44991","Sieg","","Harbor Freight; R8 spindle"],["Homier 03947","Sieg","","R8 spindle"],
      ["Grizzly G8689","Grizzly","","very similar; MT3 spindle"]],
     "spindle taper · R8 or MT3 · motor")],
  "m":[["G0731","Grizzly"],["WM14","Warco"],["WM16","Warco"]]},
 {"n":"Lathe-mill","a":"combination lathe-mill · 3-in-1 machine","d":"Metal lathe with a milling head on a column over the bed, one machine for turning and milling.",
  "s":"https://www.grizzly.com/metal-lathes-and-mills"},
 {"n":"Metal-cutting bandsaw","a":"horizontal bandsaw","d":"Bandsaw built for metal, with a fine-tooth band, slow speed, clamping vise and usually coolant.",
  "t":["Horizontal","Vertical (contour)","Portable"],"s":"https://www.axminstertools.com/machinery/saws/bandsaws",
  "m":[["AP125MB","Axminster"]],"r":[["Axminster Professional","Axminster"]]},
 {"n":"Cold cut saw","a":"cold saw","d":"Machine with a slow-turning circular blade that cuts metal bar and tube cleanly.",
  "s":"https://www.warco.co.uk/metal-bandsaws-metalworking-saws/303433-cs-250-cold-saw.html",
  "m":[["CS 250 Circular Cold Saw","Warco"]]},
 {"n":"Anvil","a":"","d":"Heavy hardened-steel block with face, horn and hardy hole on which hot metal is forged.",
  "t":["Wrought iron with steel face","Cast steel","Forged steel","Cast iron (unsuitable)"],
  "s":W+"Anvil",
  "x":[
   X("London pattern anvil","Single-horn English anvil with step and heel; most US anvils follow it.","","mid-19th century",W+"Anvil",
     [["Peter Wright solid anvil","Peter Wright","1852","Dudley; the shape widely copied"]],"weight · face width · hardy and pritchel holes"),
   X("Double-horn anvil","Mainly European anvil with one round and one square horn.","","",W+"Anvil",
     [["Bavarian pattern","","","sloped brow; Söding Halbach, Holthaus"]],"weight · side shelf · upsetting block"),
   X("Farrier's anvil","Anvil shaped for horseshoeing work.","","",W+"Anvil",[],"weight · clip horn · turning cams")]},
 {"n":"Forge","a":"blacksmith's forge · hearth","d":"Hearth heating metal to forging temperature with coal, coke, charcoal or gas.",
  "t":["Coal forge","Coke forge","Charcoal forge","Gas (propane) forge"],"s":W+"Forge"},
]
brands=[
 {"n":"Myford","c":"United Kingdom","f":"1934","seg":"Heritage manufactory","kf":"Model engineering lathes","d":"Founded by Cecil Moore in Beeston, Nottinghamshire; since 2011 Myford Ltd of Mytholmroyd.","lines":["ML7","Super 7","ML8","Speed 10"],"eras":["Cecil Moore, 1934","Myford Ltd (Dickinson family), 2011–"],"sig":["Myford ML7"],"sc":[],"rel":[],"s":W+"Myford"},
 {"n":"South Bend","c":"United States","f":"1906","seg":"Heritage manufactory","kf":"Lathes","d":"South Bend Lathe Works of South Bend, Indiana.","lines":["9-inch Model A"],"eras":[],"sig":["South Bend 9-inch"],"sc":[],"rel":["Boxford"],"s":"https://collections.ingenium.ca/item/2001.0432.001/"},
 {"n":"Atlas","c":"United States","f":"","seg":"Mainstream","kf":"Hobby lathes","d":"Atlas Press Company of Kalamazoo, Michigan; made Craftsman lathes for Sears until 1981.","lines":["10-inch","6-inch","12-inch"],"eras":[],"sig":["Atlas 10-inch"],"sc":[],"rel":["Craftsman"],"s":L+"atlas"},
 {"n":"Boxford","c":"United Kingdom","f":"1946","seg":"Heritage manufactory","kf":"Lathes","d":"Box-Ford lathes from Box Tree Mills, Halifax, begun by Denford Machine Tools.","lines":["A","B","C","ME10"],"eras":["Denford, 1946–1952","T.S. Harrison, 1952–"],"sig":["Boxford lathe"],"sc":[],"rel":["South Bend"],"s":W+"Boxford_Lathe"},
 {"n":"Hardinge","c":"United States","f":"1890","seg":"Professional & flagship","kf":"Precision lathes","d":"American precision lathe maker, early machines sold as Cataract; owner of Bridgeport from 2004.","lines":["Cataract","HLV","HLV-H"],"eras":[],"sig":["Hardinge HLV"],"sc":[],"rel":["Bridgeport"],"s":L+"hardinge"},
 {"n":"Emco","c":"Austria","f":"","seg":"Mainstream","kf":"Small machine tools","d":"Maier & Co. of Austria, maker of the Unimat miniature machine tool.","lines":["Unimat"],"eras":[],"sig":["Unimat"],"sc":[],"rel":[],"s":L+"unimat/index.html"},
 {"n":"Sherline","c":"United States","f":"1974","seg":"Specialist","kf":"Desktop lathes and mills","d":"Sherline Products, incorporated in the USA by Joe Martin; design from Australia's Harold Clisby and Ron Sher.","lines":["Model 4000 lathe","Model 5000 mill"],"eras":["Ron Sher, Australia, 1971","Joe Martin, USA, 1974–"],"sig":["Sherline lathe"],"sc":[],"rel":["Taig"],"s":"https://sherline.com/sherline-history/"},
 {"n":"Taig","c":"United States","f":"","seg":"Specialist","kf":"Micro lathes","d":"US maker of the Taig micro lathe and mill, sold in the UK as Peatol.","lines":["Peatol","Grimberg"],"eras":[],"sig":["Taig micro lathe"],"sc":[],"rel":["Sherline"],"s":L+"taig"},
 {"n":"Bridgeport","c":"United States","f":"1938","seg":"Professional & flagship","kf":"Milling machines","d":"Bridgeport, Connecticut maker of the turret mill; Textron from 1968, Hardinge from 2004.","lines":["Series I","Series II"],"eras":["Rudolph Bannow and Magnus Wahlstrom, 1938–","Textron, 1968–2004","Hardinge, 2004–2023","InCompass, 2023–"],"sig":["Bridgeport turret mill"],"sc":[],"rel":["Hardinge"],"s":W+"Bridgeport_(machine_tool_brand)"},
 {"n":"Sieg","c":"China","f":"","seg":"Value","kf":"Mini lathes and mills","d":"SIEG Industrial Group of Shanghai, maker of most mini mills sold under importer brands.","lines":["X1","X2"],"eras":[],"sig":["Sieg X2 mini mill"],"sc":[],"rel":["Grizzly"],"s":"https://makezine.com/article/digital-fabrication/machining/the-sieg-mini-mill-one-manufacturer-many-brands/"},
 {"n":"Peter Wright","c":"United Kingdom","f":"","seg":"Heritage manufactory","kf":"Anvils and vices","d":"Peter Wright and Sons of Dudley and Oldbury, anvil and vice makers; solid anvil 1852.","lines":[],"eras":["Peter Wright, 1803–1874"],"sig":["London pattern anvil"],"sc":[],"rel":[],"s":"https://www.gracesguide.co.uk/Peter_Wright"},
]
notes=("No archetypes for Hay-Budden, Fisher, Refflinghaus, Vaughan Brooks (forum/library pages blocked 403), Sieg C3 mini lathe, Warco (no fetched page), "
 "or forge makers; forge kept with fuel types. Grizzly/Shop Fox/Warco SKUs kept flat (few). Grizzly G8689 listed as near-identical X2 version per mini-lathe.com. "
 "Anvil and Forge NEW kinds sourced to Wikipedia.")
out={"kinds":kinds,"brands":brands,"traditions":[],"notes":notes}
p="work/C1/shelves/04_02.json"; t=p+".tmp"; json.dump(out,open(t,"w"),ensure_ascii=False,indent=1); os.replace(t,p)
