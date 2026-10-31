import json,copy,os
R='/home/user/Possession-Taxonomy/rebuild/'
d=json.load(open(R+'out/C1.json')); br=json.load(open(R+'out/C1_brands.json')); tr=json.load(open(R+'out/C1_traditions.json'))
def depts(n): return next(x for x in d['depts'] if x['n']==n)
def shelf(dn,sn): return next(s for s in depts(dn)['s'] if s['n']==sn)
def pop(dn,sn,kn):
    s=shelf(dn,sn)
    for i,k in enumerate(s['k']):
        if k['n']==kn: return s['k'].pop(i)
    raise KeyError(kn)
def kind(dn,sn,kn): return next(k for k in shelf(dn,sn)['k'] if k['n']==kn)
def arch(n,a,dd,mk,y,s,v=None,dt=''): return {"n":n,"a":a,"d":dd,"mk":mk,"y":y,"s":s,"v":v or [],"dt":dt}
PT,WW,GH='Power tools','Woodworking hand tools','General hand tools'
# C1-1
k=kind(PT,'Power saws','Track saw')
k['x']=[arch("Festool plunge-cut track saw","plunge saw","Festool's guide-rail circular saw whose blade plunges from a sprung housing; the maker launched the guide rail in 1962 and a patented plunge-cut saw in 1980.","Festool","1980","https://en.wikipedia.org/wiki/Track_saw",[{"n":"Guide rail","mk":"Festool","y":"1962","d":"first guide rail"}],"blade diameter · plunge depth · rail length and system")]
k['s']="https://en.wikipedia.org/wiki/Track_saw"
k=kind(PT,'Power saws','Reciprocating saw')
k['x']=[arch("Milwaukee Sawzall","Sawzall · Sawzall reciprocating saw","Milwaukee's reciprocating saw, the first portable hacksaw with a reciprocating mechanism; its name became a generic term.","Milwaukee","1951","https://en.wikipedia.org/wiki/Reciprocating_saw",[],"corded or cordless · stroke length · blade fit")]
k['s']="https://en.wikipedia.org/wiki/Reciprocating_saw"
# C1-2 jigs shelf
chis=shelf(WW,'Chisels, carving & sharpening')
hg=pop(WW,'Chisels, carving & sharpening','Honing guide'); ss=pop(WW,'Chisels, carving & sharpening','Sharpening system')
jig=[
 {"n":"Pocket-hole jig","a":"pocket hole jig · pocket-screw jig","d":"Clamping guide that drills an angled hole so a screw joins two boards with the fixing hidden from view.","t":["single-hole portable","multi-hole bench","stationary or clamp-on"],"s":"https://en.wikipedia.org/wiki/Pocket-hole_joinery","x":[arch("Kreg Jig","Kreg pocket-hole jig","The U-shaped single-hole jig developed by Craig Sommerfeld for hiding cabinet face-frame joints, which made pocket holes popular.","Kreg Tool","1989","https://learn.kregtool.com/about/history/",[{"n":"First patent","mk":"Kreg Tool","y":"1990","d":"patent issued for the Kreg Jig"},{"n":"K2000","mk":"Kreg Tool","y":"2000","d":"injection-moulded plastic instead of metal"},{"n":"K3","mk":"Kreg Tool","y":"2005","d":"patented and released"},{"n":"K4/K5 family","mk":"Kreg Tool","y":"","d":"replaced in 2021 by a new generation of pocket-hole jigs"}],"hole count · portable or bench-mounted · material thickness range")]},
 {"n":"Dovetail jig","a":"router dovetail jig","d":"Template guide that lets a router cut matching dovetail, box-joint or sliding dovetail joints.","t":["fixed-spacing template","adjustable finger template"],"s":"https://www.leightools.com/d4r-pro-overview/","x":[arch("Leigh D4R Pro","Leigh D4R · D4R Pro dovetail jig","Adjustable router jig cutting through, half-blind and sliding dovetails and box joints with variable pin and tail spacing.","Leigh","","https://www.leightools.com/d4r-pro-overview/",[],"capacity (width) · joint types · router bits")]},
 {"n":"Shooting board","a":"","d":"Flat base with a stop and fence on which a board is held and its edge or end trimmed square with a hand plane.","s":"https://en.wikipedia.org/wiki/Shooting_board"},
 {"n":"Saw set","a":"saw setter","d":"Hand tool that bends saw teeth to set the width of the cut and stop the blade binding.","t":["hammer","lever","pliers","two-handled","automated"],"s":"https://en.wikipedia.org/wiki/Saw_set"},
]
jig+= [hg,ss]
s_idx=[s['n'] for s in depts(WW)['s']].index('Braces & hand drills')+1
depts(WW)['s'].insert(s_idx,{"n":"Jigs, guides & sharpening aids","k":jig})
# C1-3 tool storage
ts=depts('Tool storage'); ts['mode']='mixed'
ts['note']=ts.get('note') or "Market-covering makers for site storage; heritage and mechanics' makers as archetypes."
k=kind('Tool storage','Toolboxes, chests & bags','Roller cabinet')
k['x']=[arch("Snap-on roll cab","Snap-on tool cabinet","Snap-on's drawered steel tool cabinet on casters, sold to mechanics through franchise vans.","Snap-on","","https://en.wikipedia.org/wiki/Snap-on",[],"width · drawer count · colour")]
k=kind('Tool storage','Toolboxes, chests & bags','Tool chest')
k['x']=[arch("Gerstner machinist's chest","Gerstner Model 52 · wooden machinist tool chest","Hardwood machinist's tool chest made by H. Gerstner & Sons in Dayton, Ohio, the maker's best-known form.","H. Gerstner & Sons","","https://en.wikipedia.org/wiki/H._Gerstner_%26_Sons",[{"n":"Model 52","mk":"H. Gerstner & Sons","y":"","d":"machinist's chest"},{"n":"92XL Ultimate Chest","mk":"H. Gerstner & Sons","y":"","d":"larger chest"}],"hardwood (oak, cherry, walnut, maple) · drawer count · width")]
# C1-4 electronics
k=kind('Welding & soldering','Soldering, brazing & consumables','Soldering iron')
k['s']="https://en.wikipedia.org/wiki/Soldering_iron"
k['x']=[arch("Weller Magnastat iron","Weller W-TCP","Weller's temperature-controlled soldering iron, patented in 1960, whose tip-and-tube layout became the model for most later irons.","Weller","1960","https://en.wikipedia.org/wiki/Soldering_iron",[{"n":"W-TCP station","mk":"Weller","y":"1967","d":"soldering station including the Magnastat"}],"tip type · wattage · station or pencil"),
 arch("Pinecil","Pinecil V2 · Pine64 soldering iron","Open-source mini soldering iron from Pine64 with a RISC-V chip, powered over USB-C (PD or QC 3.0, 12–20 V).","Pine64","","https://pine64.com/product/pinecil-smart-mini-portable-soldering-iron/",[{"n":"Version 2","mk":"Pine64","y":"","d":"RISC-V SoC, USB-C PD and QC 3.0"}],"USB-C power input · tip fit · firmware")]
shelf('Measuring & detecting','Testers, detectors & cameras')['k'].insert(1,{"n":"Bench power supply","a":"lab power supply · laboratory power supply","d":"Mains-powered supply with adjustable output voltage and a current limit, for testing and powering electronic circuits.","t":["linear","switching"],"s":"https://en.wikipedia.org/wiki/Laboratory_power_supply"})
# C1-5
bars=[pop(GH,'Hammers, punches & bars',n) for n in ['Wrecking bar','Pry bar','Nail puller','Lifting bar']]
wb=bars[0]
wb.update({"n":"Pry bar & wrecking bar","a":"crowbar · wrecking bar · flat bar · pry bar · nail puller · cat's paw · lifting bar · pinch bar","d":"Steel bar used as a lever for prising, nail pulling, demolition or lifting, in claw, flat or straight forms.","t":["gooseneck wrecking bar","flat pry bar","cat's paw (nail puller)","lifting bar (straight, pointed)"]})
sh=shelf(GH,'Hammers, punches & bars'); pos=[k['n'] for k in sh['k']].index('Punch')+1
sh['k'].insert(pos,wb)
# Estwing archetype
ch=kind(GH,'Hammers, punches & bars','Claw hammer')
ch['x']=[arch("Estwing one-piece hammer","Estwing Hammer · solid-steel hammer","Claw hammer with head and handle forged from one piece of solid steel, patented by Ernest Estwing in the 1920s.","Estwing","1923","https://www.estwing.com/company/celebrating-100-years/",[{"n":"Leather handle","mk":"Estwing","y":"1930s","d":"leather-washer grip introduced"},{"n":"Sure Strike claw hammer","mk":"Estwing","y":"","d":""},{"n":"Ultra claw hammer","mk":"Estwing","y":"","d":""}],"head weight (oz) · claw curved or straight · grip (leather, nylon-vinyl)")]
ch['m']=[m for m in ch['m'] if m[1]!='Estwing']
# C1-6
nl=shelf(PT,'Nailers, staplers & heat tools')['k']
for n in ['Brad nailer','Pin nailer']: nl.pop([k['n'] for k in nl].index(n))
fn=kind(PT,'Nailers, staplers & heat tools','Finish nailer')
fn.update({"a":"trim nailer · brad nailer · pin nailer","d":"Nailer for trim, moulding and fine woodwork, driving finish nails, thin brads or headless pins by gauge.","t":["15/16-gauge (trim and moulding)","18-gauge (brad)","23-gauge (pin, headless)","pneumatic","gas","battery"]})
# C1-7
for k in shelf('Protective equipment (PPE)','Protective clothing & gloves')['k']:
    if k['n']=='Chainsaw trousers': k['t']=["Class 1, 2 or 3 (chain speed 20, 24 or 28 m/s)","Design A (front protection)","Design C (all-round protection)","vented"]
    if k['n']=='Work gloves': k['t']=["leather rigger","coated knit (nitrile, latex or PU palm)","cut-resistant (EN 388 level A–F)","mechanic's, insulated or waterproof"]
# C1-8 Japanese by form
jp=depts(WW)['s']; jshelf=next(s for s in jp if s['n']=='Japanese woodworking tools')
jk={k['n']:k for k in jshelf['k']}
for k in jk.values():
    a=k.get('a','')
    k['a']=(a+' · ' if a else '')+'Japanese tool'
jp.remove(jshelf)
def add_after(dn,sn,after,k,end=False):
    s=shelf(dn,sn)['k']
    if end: s.append(k); return
    s.insert([x['n'] for x in s].index(after)+1,k)
add_after(WW,'Planes','Scraper',jk['Kanna (Japanese plane)'],True)
for n in ['Ryoba saw','Dozuki saw','Kataba saw','Flush-cut saw']: add_after(WW,'Hand saws','Bow saw',jk[n],True)
add_after(WW,'Chisels, carving & sharpening','Mortise chisel',jk['Nomi (Japanese chisel)'])
add_after(GH,'Hammers, punches & bars','Claw hammer',jk['Genno (Japanese hammer)'])
for n in ['Sumitsubo (ink line)',"Sashigane (carpenter's square)",'Kiridashi']: add_after('Measuring & detecting','Precision measuring & marking out','',jk[n],True)
# C1-9
mw=[pop(WW,'Hand saws','Hacksaw'),pop(WW,'Chisels, carving & sharpening','File'),pop(WW,'Chisels, carving & sharpening','Rasp')]
gs=depts(GH)['s']; gs.insert(2,{"n":"Metalwork hand tools","k":mw})
# brands
B=br['b']
def lnk(o):
    if isinstance(o,dict): return {k:lnk(v) for k,v in o.items()}
    if isinstance(o,list): return [lnk(v) for v in o]
    return "Lie-Nielsen Toolworks" if o=="Lie-Nielsen" else o
d=lnk(d)
B[:]=[b for b in B if b['n']!='Lie-Nielsen']
for b in B:
    if b['n']=='Estwing': b.update({"s":"https://en.wikipedia.org/wiki/Estwing","d":"Rockford, Illinois maker founded by Ernest Estwing; first to sell hammers forged from one piece of solid steel.","sig":["Estwing one-piece hammer"]})
def nb(n,c,f,seg,kf,dd,s,sig=None,lines=None,rel=None):
    assert n.lower() not in [x['n'].lower() for x in B],n
    B.append({"n":n,"c":c,"f":f,"seg":seg,"kf":kf,"d":dd,"lines":lines or [],"eras":[],"sig":sig or [],"sc":[],"rel":rel or [],"s":s})
nb("Kreg Tool","United States","1989","Premium","pocket-hole jigs","Iowa maker of the Kreg Jig, founded by Craig Sommerfeld.","https://learn.kregtool.com/about/history/",["Kreg Jig"])
nb("Leigh","","","Premium","dovetail jigs","Maker of the Leigh D4R Pro router dovetail jig, part of Lee Valley Tools.","https://www.leightools.com/d4r-pro-overview/",["Leigh D4R Pro"])
nb("Weller","United States","","Professional & flagship","soldering irons","Pennsylvania maker whose 1946 gun was the first instant-heating soldering gun, and whose Magnastat iron followed in 1960.","https://en.wikipedia.org/wiki/Soldering_iron",["Weller Magnastat iron"])
nb("Pine64","","","Specialist","open-source hardware","Maker of the open-source Pinecil USB-C soldering iron.","https://pine64.com/product/pinecil-smart-mini-portable-soldering-iron/",["Pinecil"])
nb("Mafell","Germany","1899","Professional & flagship","woodworking machines","German maker of portable woodworking machines, based in Oberndorf.","https://en.wikipedia.org/wiki/Mafell")
nb("HiKOKI","Japan","","Professional & flagship","power tools","Brand of Koki Holdings, formerly Hitachi Koki, bought by KKR in 2017; sold as Metabo HPT in the US.","https://en.wikipedia.org/wiki/Hitachi",rel=["Metabo"])
nb("Flex Elektrowerkzeuge","Germany","1922","Professional & flagship","angle grinders","Steinheim maker of the first angle grinder; the name 'Flex' is German slang for one.","https://en.wikipedia.org/wiki/Flex-Elektrowerkzeuge")
nb("Matco Tools","United States","1946","Professional & flagship","mechanics' tools","Franchise-sold professional hand tool and toolbox brand, owned by Vontier.","https://en.wikipedia.org/wiki/Matco_Tools")
nb("Mac Tools","United States","1938","Professional & flagship","mechanics' tools","Franchise-sold professional hand tool and storage brand owned by Stanley Black & Decker.","https://en.wikipedia.org/wiki/Mac_Tools")
nb("Stahlwille","Germany","1862","Professional & flagship","torque and hand tools","Wuppertal maker of forged hand tools for automotive, industrial and aerospace use.","https://en.wikipedia.org/wiki/Stahlwille")
nb("Hazet","Germany","1868","Professional & flagship","workshop tools","Remscheid maker of about six thousand tools, including torque tools and Assistent tool trolleys.","https://en.wikipedia.org/wiki/Hazet")
nb("H. Gerstner & Sons","United States","1906","Heritage manufactory","wooden tool chests","Family-owned Dayton, Ohio maker of wooden tool chests, including machinists' chests.","https://en.wikipedia.org/wiki/H._Gerstner_%26_Sons")
# traditions
T=tr['t']
bm=next(t for t in T if t['n']=='Banshu Miki forged blades')
T[:]=[t for t in T if t['n']!='Miki blades']
bm['forms']=bm['forms']+['Higonokami']
bm['ctr']=bm['ctr']+['Nagao Kanekoma Factory (higonokami)']
bm['p']=bm['p']+'; higonokami 1896–present'
T.append({"n":"Japanese carpentry tools (daiku dōgu)","g":"Woodwork & furniture","r":"Japan","p":"Carpentry first developed in the 12th century","d":"Hand tools of Japanese carpenters, mostly cutting on the pull stroke, used for joinery with almost no nails.","tech":"thin hard edge metal (hagane) forge-welded to softer base metal (jigane)","mat":"white and blue paper steel; hardwood bodies and handles","forms":["Kanna (Japanese plane)","Ryoba saw","Dozuki saw","Kataba saw","Flush-cut saw","Genno (Japanese hammer)","Nomi (Japanese chisel)","Sumitsubo (ink line)","Sashigane (carpenter's square)","Kiridashi"],"ctr":[],"auth":"","s":"https://en.wikipedia.org/wiki/Japanese_carpentry"})
# moves: nothing to add
for f,o in (('C1',d),('C1_brands',br),('C1_traditions',tr)):
    json.dump(o,open(R+f'work/FIX_C1/{f}.new.json','w'),ensure_ascii=False,indent=1)
