import json, os
W='https://en.wikipedia.org/wiki/'
def X(n,a,d,mk,y,s,v,dt): return {"n":n,"a":a,"d":d,"mk":mk,"y":y,"s":s,"v":[dict(zip(("n","mk","y","d"),t)) for t in v],"dt":dt}
ROUT=W+"Router_(woodworking)"
kinds=[
{"n":"Router","a":"plunge router · trim router","d":"Power tool with a bit spinning in a base, for edges, grooves and recesses.",
 "t":["plunge","fixed-base","compact / trim (laminate trimmer)","palm","cordless","collet 1/4 in, 8 mm, 1/2 in"],
 "s":"https://www.toolstation.com/power-tools/routers-planers/c725",
 "x":[
  X("ELU plunge router","plunge router","Router whose motor slides down on spring-loaded columns so the bit can enter the work mid-board.","ELU","c. 1949",ROUT,[],"collet size · power · plunge depth"),
  X("Festool OF 1400","OF 1400 EQ","German-made 1400 W mid-size plunge router with 70 mm plunge stroke and fine depth adjustment.","Festool","","https://www.toolnut.com/products/festool-574692-of-1400-eq-router-imperial",
    [("OF 1400 EQ-F-Plus 576213","Festool","","120 V version")],"1/4 in, 8 mm, 1/2 in collets · 110/120/230 V"),
  X("Trend T11","T11EK","Heavy 2000 W half-inch plunge router with 80 mm plunge, used with worktop jigs.","Trend","","https://www.tooled-up.com/trend-t11ek-1-2-plunge-router/prod/234553",
    [("T11EK","Trend","","2000 W, 0–80 mm plunge; delisted")],"1/2 in standard, optional 6–12 mm collets · 110/230 V"),
  X("Makita RT0701C","Makita compact router","1-1/4 HP compact router with quick-change bases (fixed, trimmer, plunge, tilt, offset).","Makita","","https://makitatools.com/products/details/RT0701C",
    [("RT0701C","Makita","","corded, 1/4 in collet, fixed and trimmer bases"),("RT0701CX3","Makita","","kit with 3 extra bases"),("XTR01T7","Makita","","18V LXT brushless compact router kit")],"base set · corded or 18V LXT"),
  X("Bosch Colt","PR20EVS · Colt palm router","1 HP palm router with variable speed and optional plunge, offset and tilt bases.","Bosch","","https://www.boschtools.com/us/en/products/pr20evs-060160A71A",
    [("PR20EVS","Bosch","","fixed base, 16,000–35,000 rpm")],"base set · 1/4 in collet"),
 ],
 "m":[["GOF 20-12","Bosch"],["DCW604","DeWalt"],["M18FR12","Milwaukee"],["M18FTR","Milwaukee"],["T4","Trend"],["T1 Trimmer","Trend"]]},
{"n":"Oscillating multi-tool","a":"multi-tool · multitool · oscillating tool","d":"Hand-held power tool whose blade, pad or scraper vibrates through a small arc, for plunge cuts, sanding and scraping.",
 "t":["corded","cordless","accessory fit: Starlock, OIS, universal"],
 "s":"https://toolstation.com/power-tools/multi-tools/c446",
 "x":[X("Fein MultiMaster","Multi-Master · MULTIMASTER","Fein's original oscillating tool, grown from a 1967 plaster-cast saw; rivals followed when its patent expired in 2008.","Fein","2007","https://fein.com/en_us/blog/history-of-the-fein-multimaster/",
   [("Plaster cast saw","Fein","1967","oscillating-blade forerunner"),("MULTIMASTER with QuickIN","Fein","2007","launch for trades"),("Starlock fitting","Fein","2016","accessory standard with Bosch"),("Cordless MULTIMASTER on AMPShare","Fein","2022","switch to Bosch 18V batteries"),
    ("Dremel Multi-Max","Dremel","","post-patent rival"),("Bosch PS50 Multi-X","Bosch","","post-patent rival")],"corded or cordless · oscillation angle · accessory fit")],
 "m":[["DCS356","DeWalt"],["DWE315","DeWalt"],["DTM51","Makita"],["CP100D","Makita"],["M18FMT","Milwaukee"],["C12MT","Milwaukee"],["RMT18","Ryobi"],["WX686 Sonicrafter","Worx"]]},
{"n":"Rotary tool","a":"Dremel-type tool · Dremel","d":"Slim hand-held high-speed motor with a collet or chuck for small accessories (engraving, cutting, sanding, polishing).",
 "t":["corded","cordless","pen-style"],
 "s":"https://www.toolstation.com/hand-tools/sander-accessories/c1205",
 "x":[X("Dremel Moto-Tool","Dremel rotary tool","The first hand-held high-speed rotary tool, introduced by Dremel in Racine, Wisconsin.","Dremel","1935",W+"Dremel",
   [("Moto-Tool","Dremel","1935","original"),("Dremel 3000","Dremel","","corded series"),("Dremel 3200","Dremel","",""),("Dremel 4000","Dremel","","corded high-performance series"),("Dremel 4250","Dremel","",""),
    ("Dremel 8200","Dremel","","cordless series"),("Dremel 8220","Dremel","2012","12V MAX cordless, replaced the 8200"),("Dremel 8240","Dremel","",""),("Dremel 8150","Dremel","",""),("Dremel Lite","Dremel","",""),("Dremel Stylo+","Dremel","","pen-style")],
   "corded or cordless · speed range · accessory kit")],
 "m":[["M12BLROT","Milwaukee"]]},
{"n":"Power planer","a":"electric plane","d":"Hand-held electric plane with a rotating cutter drum.",
 "t":["corded","cordless"],
 "s":"https://www.toolstation.com/power-tools/planer-thicknessers/c265",
 "m":[["GHO 12-V","Bosch"],["GHO 18V-26","Bosch"],["D26500K","DeWalt"],["DCP580","DeWalt"],["M12BLP","Milwaukee"],["M18BP","Milwaukee"]]},
{"n":"Biscuit jointer","a":"biscuit joiner · plate joiner","d":"Hand-held power tool that plunges a small circular blade sideways to cut slots for joining biscuits.",
 "t":["corded","cordless"],
 "s":"https://www.toolstation.com/power-tools/workshop-tools/c721",
 "x":[X("Lamello biscuit joiner","Lamello system","Hermann Steiner's system of beech biscuits in 4 mm grooves, made by his Lamello company.","Lamello","1956",W+"Biscuit_joiner",
   [("Classic X","Lamello","","the original-system joiner, 4 mm groove"),("Classic X Cordless","Lamello","","18V version")],"biscuit No. 0, 10, 20 · corded or 18V")]},
{"n":"Loose-tenon joiner","a":"Domino joiner · mortise joiner","d":"Hand-held tool whose oscillating cutter plunges a mortise for a glued loose tenon.",
 "s":"https://www.core77.com/posts/31384/Tools-That-Change-the-Way-We-Design-namp-Build-The-Festool-Domino",
 "x":[X("Festool Domino","Domino","Loose-tenon mortiser devised by cabinetmaker Vitus Rommel at Festool; cutter oscillates sideways to form the mortise.","Festool","2007 (US)","https://www.core77.com/posts/31384/Tools-That-Change-the-Way-We-Design-namp-Build-The-Festool-Domino",
   [("DF 500","Festool","","tenons 4–10 mm thick"),("DF 700 XL","Festool","","tenons 8–14 mm thick")],"tenon thickness · cross-stop, trim-stop accessories")]},
]
K="knowledge"
def B(n,c,f,seg,d,lines,sig,rel,s): return {"n":n,"c":c,"f":f,"seg":seg,"d":d,"lines":lines,"sig":sig,"rel":rel,"s":s}
brands=[
B("Festool","Germany","1925","Premium woodworking power tools","German maker of system-based premium tools for woodworkers.",["Domino","OF routers"],["Festool Domino","Festool OF 1400"],[],"https://www.core77.com/posts/31384/Tools-That-Change-the-Way-We-Design-namp-Build-The-Festool-Domino"),
B("Lamello","Switzerland","","Joinery tools","Swiss company founded by Hermann Steiner, inventor of the biscuit joint.",["Classic X"],["Lamello biscuit joiner"],[],W+"Biscuit_joiner"),
B("Dremel","United States","1932","Rotary and hobby tools","Racine-founded rotary-tool brand owned by Bosch since 1993.",["Moto-Tool","3000","4000","8200"],["Dremel Moto-Tool"],["Bosch"],W+"Dremel"),
B("Fein","Germany","1867","Professional power tools","German power-tool maker, originator of the oscillating multi-tool.",["MULTIMASTER"],["Fein MultiMaster"],["Bosch"],"https://fein.com/en_us/blog/history-of-the-fein-multimaster/"),
B("Makita","Japan","1915","Professional power tools","Japanese power-tool maker based in Anjō.",["18V LXT"],["Makita RT0701C"],[],W+"Makita"),
B("Bosch","Germany","1886","DIY (green) and professional (blue) power tools","German group whose power-tool division sells green DIY and blue Professional lines.",["Colt","GOF"],["Bosch Colt"],["Dremel","Fein"],K),
B("Trend","United Kingdom","","Routers and router cutters","British router and cutter specialist.",["T-series routers"],["Trend T11"],[],K),
B("ELU","Germany","","Power tools (historic)","German maker credited with the plunge router, now part of DeWalt.",[],["ELU plunge router"],["DeWalt"],ROUT),
]
notes=("Dropped from flat lists: Trend T7, T8, T12; DeWalt DCW620; DeWalt DCS355, DCS358 (trim of SKU lists); ranges (18V XR, M18 FUEL, LXT, CXT, ONE+) removed as they live in the battery-platform shelf and brand register. "
 "Old Dremel models became versions of the Moto-Tool archetype. Not added for lack of a retrievable source: Lamello Top 21 and early portable joiner dates, Fein MultiMaster model numbers, Domino launch year in Europe (US 2007 used), Trend T11 year. "
 "lamello.com (redirect loop) and protoolreviews (403) not used. Kelley 1906 portable router mentioned on the Router page but not added as an archetype.")
out={"kinds":kinds,"brands":brands,"traditions":[],"notes":notes}
p='/home/user/Possession-Taxonomy/rebuild/work/C1/shelves/00_04.json'
json.dump(out,open(p+'.tmp','w'),ensure_ascii=False,indent=1); os.replace(p+'.tmp',p)
