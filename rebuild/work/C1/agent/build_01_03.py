import json, os
W='https://en.wikipedia.org/wiki/'
CH=W+'Chisel'; GO=W+'Gouge_(chisel)'; FI=W+'File_(tool)'; SS=W+'Sharpening_stone'; NO=W+'Norton_Abrasives'
TO='https://www.tormek.com/en/inspiration/the-tormek-story'
AU='https://popularwoodworking.com/techniques/auriou-french-rasp-maker-since-1856-closes-its-doors-2'
PF='https://www.woodcraft.com/blog_entries/pfeil-tools-chart'
VG='https://woodcraft.com/products/veritas-mk-ii-honing-guide'
SW='https://finewoodworking.com/2011/04/07/sweetheart-chisels-750-series-review'
LN='https://finewoodworking.com/2008/09/01/bench-chisel-review-3'
RS='https://robert-sorby.co.uk/'
AI='https://workshopheaven.com/ashley-iles/'
NS='https://www.knivesandtools.co.uk/en/ct/naniwa-vs-shapton.htm'
FX='https://www.knivesandtools.com/en/ct/flexcut.htm'
DM='https://dmtsharp.com/pages/dmthistory'
WS='https://worksharptools.com/products/woodworking-tool-sharpener-ws3000'
KI='https://www.timbecon.com.au/products/kirschen-two-cherries-7-bent-gouge-wood-carving-chisel'
WCC='https://www.woodcraft.com/collections/chisels'
AX='https://www.axminstertools.com/hand-tools/files-rasps'
AXS='https://www.axminstertools.com/activities/sharpening/sharpening-stones'
def X(n,d,s,mk='',a='',y='',v=None,dt=''): return {"n":n,"a":a,"d":d,"mk":mk,"y":y,"s":s,"v":v or [],"dt":dt}
def V(n,mk='',d='',y=''): return {"n":n,"mk":mk,"y":y,"d":d}
kinds=[
 {"n":"Bench chisel","a":"striking chisel · bevel-edge chisel · firmer chisel","d":"General woodworking chisel with a strong tang or socket and a handle that can be struck with a mallet.","s":WCC,
  "t":["bevel-edge","firmer (rectangular section)","butt (short)","dovetail","socket","tang","A2, O1 or PM-V11 steel"],
  "x":[X("Stanley No. 750 socket chisel","Bevel-edge socket chisel with a 30° factory bevel and replaceable hornbeam handle; the pattern copied by modern premium makers.",SW,mk="Stanley",a="Sweetheart 750",
        v=[V("No. 750 (original)","Stanley","US-made; discontinued decades before 2011"),V("Sweetheart 750 (revival)","Stanley","made in Sheffield, high-carbon chrome steel, hornbeam handles"),V("Bevel Edge Socket Chisel","Lie-Nielsen","patterned on the Stanley 750; A2 steel")],
        dt="width 1/8–2 in · steel · handle wood"),
       X("Ashley Iles cabinetmaker's chisel","Sheffield-pattern bench chisel forged from O1 tool steel, hardened to RC60-61 and hand ground.",AI,mk="Ashley Iles",
        v=[V("Butt chisel","Ashley Iles"),V("Dovetail chisel","Ashley Iles")])]},
 {"n":"Paring chisel","a":"","d":"Long, thin chisel pushed by hand, never struck, for fine paring and reaching into grooves.","s":WCC,
  "t":["straight","cranked (offset neck)","slick (large, timber framing)","corner chisel"]},
 {"n":"Mortise chisel","a":"mortice chisel","d":"Thick, deep-bladed chisel with a straight edge, struck to chop mortises.","s":WCC,
  "t":["registered mortise chisel","sash mortise chisel"]},
 {"n":"Carving gouge","a":"carving chisel · woodcarving gouge","d":"Hand-carving gouge or chisel specified by sweep number (blade curve) and width, e.g. #7-20 mm.","s":GO,
  "t":["sweep #1 (flat) to #9 (semicircle)","#11 U-gouge or veiner","V-tool / parting tool","straight","spoon-bent","back-bent","fishtail","crank-neck","incannel or outcannel bevel"],
  "x":[X("Pfeil Swiss Made carving tool","Swiss carving tools marked 'Swiss Made' with sweep/width numbers, forged alloy tool steel, octagonal hardwood handle.",PF,mk="Pfeil",dt="sweep · width · profile (straight, bent, fishtail, V)"),
       X("Two Cherries carving tool","Hand-forged German carving tools hardened to 61 Rc with octagonal hornbeam handles.",KI,mk="Kirschen",a="Kirschen",
        v=[V("#7 bent gouge","Kirschen","shank bent along its whole length")]),
       X("Flexcut carving tool","Carving tools made from thin high-carbon spring steel that can flex into recesses.",FX,mk="Flexcut",y="1992",
        v=[V("Craft Carver","Flexcut","interchangeable blades"),V("Pro Series knives","Flexcut","1095 steel")])]},
 {"n":"Turning gouge","a":"woodturning gouge","d":"Long-handled gouge for shaping wood on a lathe.","s":"https://www.axminstertools.com/hand-tools/chisels/woodturning-tools/woodturning-gouges",
  "t":["bowl gouge","spindle gouge","roughing gouge","HSS or cryogenic steel"],
  "m":[["David Ellsworth Signature Bowl Gouge","Crown"],["Razor Edge Bowl Gouge","Crown"]],"r":[["Cryo","Crown"],["Sovereign System","Robert Sorby"]]},
 {"n":"File","a":"","d":"Hardened steel bar with cutting ridges for removing metal or wood by hand on the push stroke.","s":AX,
  "t":["single cut","double cut","rough to dead smooth (bastard, second cut, smooth)","flat, half-round, round, triangular, square, knife","mill file","needle file","riffler","diamond file","escapement file"],
  "x":[X("Swiss-pattern file","Precision file with shallower teeth graded by number (No. 1 coarser than No. 2).",FI,dt="cut number · shape · length")]},
 {"n":"Rasp","a":"","d":"Steel bar or blade with individually raised teeth, for fast shaping of wood and soft materials.","s":AX,
  "t":["cabinet rasp","modeller's rasp","riffler","saw rasp"],
  "x":[X("Auriou hand-cut rasp","French rasps whose teeth were raised by hand, made in Saint-Juéry since 1856.",AU,mk="Auriou",y="1856")],
  "m":[["Japanese Saw Rasp","Shinto"]]},
 {"n":"Whetstone","a":"sharpening stone · waterstone · oilstone · bench stone","d":"Block of natural or synthetic abrasive used with water or oil to sharpen blades.","s":AXS,
  "t":["waterstone","oilstone","natural stone","diamond plate","ceramic","grit 120 to 30,000"],
  "x":[X("Arkansas stone","Natural quartz oilstone from the Ouachita Mountains, fine enough for late-stage sharpening.",SS),
       X("Coticule","Natural Belgian whetstone from the Ardennes, prized for its edge; Belgian Blue stone is found alongside it.",SS),
       X("Japanese natural stone","Natural waterstone (tennen toishi) used wet; the Honyama mines near Kyoto closed in 1967.",SS,a="tennen toishi"),
       X("India stone","Synthetic aluminium oxide oilstone.",SS,v=[V("MB8 India Oilstone","Norton")]),
       X("Shapton Glass HR","Hard, fast-cutting waterstone bonded to tempered glass, used without soaking, up to 16,000 grit.",NS,mk="Shapton"),
       X("Naniwa Professional","Thick soaking waterstone (about 2 cm), up to 10,000 grit.",NS,mk="Naniwa"),
       X("DMT diamond plate","Steel plate with electroplated diamond grit, also used to flatten waterstones.",DM,mk="DMT",
        v=[V("Dia-Sharp","DMT","continuous diamond surface"),V("DuoSharp","DMT","two-sided bench stone"),V("Diafold","DMT","folding pocket sharpener")])],
  "m":[["SJ-250 Japanese Waterstone","Tormek"]]},
 {"n":"Honing guide","a":"sharpening jig · honing jig","d":"Clamp on a roller that holds a chisel or plane blade at a set angle while it is honed on a stone.","s":VG,
  "t":["side-clamping","top-clamping","with angle-setting jig","micro-bevel roller"],
  "x":[X("Veritas Mk.II honing guide","Honing guide setting bevels of 15–54° and back bevels of 10–20° for blades 1/2 to 2-7/8 in wide, with a three-position micro-bevel roller.",VG,mk="Veritas",a="Mk II")]},
 {"n":"Sharpening system","a":"wet grinder · sharpening machine","d":"Machine or jig system for sharpening edges, such as a slow wet wheel with jigs or a dry abrasive disc.","s":AXS,
  "t":["slow wet grinder","dry abrasive disc","belt sharpener","jig-guided"],
  "x":[X("Tormek wet grinder","Slow-turning water-cooled grindstone with a Universal Support for jigs, developed by Torgny Jansson in Sweden.",TO,mk="Tormek",y="1973",
        v=[V("First self-powered model","Tormek","",y="1981"),V("Universal Support","Tormek","basis of the jig system",y="1984"),V("SG-250 Original Grindstone system","Tormek","vitrified aluminium oxide stone, replacing original Gotland sandstone")]),
       X("Work Sharp WS3000","Dry bench sharpener with tempered-glass abrasive wheels and preset 20–35° bevel angles; now retired.",WS,mk="Work Sharp"),
       X("ProEdge","Robert Sorby's sharpening system.",RS,mk="Robert Sorby")]},
]
brands=[
 ("Stanley","USA","","Heritage manufactory","hand tools","US hand-tool maker whose No. 750 socket chisel set the bevel-edge pattern.","knowledge"),
 ("Lie-Nielsen","USA","","Premium","hand tools","Lie-Nielsen Toolworks, maker of premium hand tools in classic patterns.","knowledge"),
 ("Ashley Iles","United Kingdom","1949","Artisan & independent","chisels and carving tools","Founded in Sheffield by pattern maker Ashley Iles; now a family firm in Lincolnshire.",AI),
 ("Pfeil","Switzerland","","Specialist","carving tools","Swiss maker of carving tools sold as 'Swiss Made'.",PF),
 ("Kirschen","Germany","","Heritage manufactory","carving tools","Remscheid family firm whose tools carry the Two Cherries mark.",KI),
 ("Flexcut","USA","1986","Specialist","carving tools","Erie, Pennsylvania maker founded as Falls Run Woodcarving; tools from 1992.",FX),
 ("Robert Sorby","United Kingdom","1828","Heritage manufactory","woodturning tools","Sheffield edge-tool maker first registered in Union Street in 1828.",RS),
 ("Auriou","France","1856","Heritage manufactory","rasps","Saint-Juéry maker of hand-cut rasps and rifflers; factory closed in 2007.",AU),
 ("Norton","USA","","Mainstream","abrasives","Worcester, Massachusetts abrasives maker, owned by Saint-Gobain since 1990.",NO),
 ("Shapton","Japan","","Specialist","waterstones","Japanese maker of glass-backed and other ceramic waterstones.","knowledge"),
 ("Naniwa","Japan","","Specialist","waterstones","Japanese waterstone maker.","knowledge"),
 ("DMT","USA","1976","Specialist","diamond sharpeners","Diamond Machining Technology, Marlborough, Massachusetts maker of diamond plates.",DM),
 ("Veritas","Canada","","Premium","hand tools","Lee Valley's own tool brand.","knowledge"),
 ("Tormek","Sweden","1973","Specialist","sharpening systems","Swedish wet-grinder maker founded by Torgny Jansson.",TO),
 ("Work Sharp","USA","","Mainstream","sharpening systems","Sharpener brand of Darex, made in Ashland, Oregon.",WS),
 ("Narex","Czech Republic","","Mainstream","chisels","Czech maker of chisels and woodworking hand tools.","knowledge"),
 ("Crown","United Kingdom","","Specialist","woodturning tools","Sheffield maker of woodturning tools.","knowledge"),
]
brands=[{"n":n,"c":c,"f":f,"seg":seg,"kf":kf,"d":d,"lines":[],"eras":[],"sig":[],"sc":["woodworking"],"rel":[],"s":s} for n,c,f,seg,kf,d,s in brands]
trads=[{"n":"Japanese natural whetstones","g":"Metal & blades","r":"Kyoto area, Japan","p":"","d":"Natural Japanese waterstones (tennen toishi) quarried for finishing blades, used wet.","tech":"quarried and cut stone used with water","mat":"natural sedimentary stone",
 "forms":["Whetstone"],"ctr":["Honyama mines near Kyoto (closed 1967)"],"auth":"","s":SS}]
notes=("All eight old kinds kept; Carving gouge and Honing guide new. Left out for lack of a retrievable source this session: Marples/Irwin Blue Chip, Veritas PM-V11 chisels (Lee Valley 429), "
 "Narex chisel details (page 403 on refetch; brand from knowledge), Eclipse honing guide, King stones, Atoma, Hamlet, Grobet/Vallorbe and Nicholson files, Sheffield vs Swiss sweep-number comparison. Crown models kept from old data.")
out={"kinds":kinds,"brands":brands,"traditions":trads,"notes":notes}
p='work/C1/shelves/01_03.json'; json.dump(out,open(p+'.tmp','w'),ensure_ascii=False,indent=1); os.replace(p+'.tmp',p)
