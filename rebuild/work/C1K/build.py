import json,os,copy
R='/home/user/Possession-Taxonomy/rebuild/out/'
d=json.load(open('/home/user/Possession-Taxonomy/rebuild/work/C1K/bak/C1.json'))
dept=[x for x in d['depts'] if x['n'].startswith('Knives')][0]
oldk={k['n']:k for s in dept['s'] for k in s['k']}
def old(kind,name):
    for a in oldk[kind]['x']:
        if a['n']==name: return copy.deepcopy(a)
    raise KeyError(name)
def V(n,mk='',y='',dd=''): return {"n":n,"mk":mk,"y":y,"d":dd}
def A(n,d_,mk,y,s,v=None,dt='',a=''): return {"n":n,"a":a,"d":d_,"mk":mk,"y":y,"s":s,"v":v or [],"dt":dt}
W='https://en.wikipedia.org/wiki/'
# --- folding knives
slip={"n":"Slip-joint pocket knife","a":"traditional pocket knife · penknife · spring-back knife","d":"Folding knife without a lock; a backspring holds the blade open and closed.",
 "t":["trapper","stockman","peanut","jack","congress","canoe","sunfish","camper/scout"],"s":W+"Pocketknife",
 "x":[old('Traditional folding knife','Barlow'),old('Traditional folding knife','Case Trapper'),old('Traditional folding knife','Sod Buster'),old('Traditional folding knife','Laguiole'),old('Traditional folding knife','Douk-Douk')]}
lag=slip['x'][3]; lag['s']=W+'Laguiole_knife'
lag['v']=[V("laguiole droit","","","earliest straight-bladed form"),V("Calmels design","","1829","first laguiole, Jean-Pierre Calmels"),V("classic form","","c. 1860","navaja-like shape"),V("with awl","","1840",""),V("with corkscrew","","c. 1880","")]
lag['dt']="one to three pieces · horn, wood or aluminium handle · bee or fly on spring · shepherd's cross · Thiers or Laguiole made"
slip['x'][0]['v']=[]  # Barlow old version was a Case model; keep simple
slip['x'][0]['v']=[V("Case Damascus Barlow","Case","","")]
fric={"n":"Friction folder & locking-collar knife","a":"no-lock folder · ring-lock knife","d":"Folding knife held open by friction or a turning collar instead of a spring lock.",
 "t":["chikiri lever","Virobloc collar"],"s":W+"Higonokami",
 "x":[
  A("Opinel No. 8","Beech-handled French folder with 8.5 cm blade and turning collar; most widely used size of the numbered Opinel range.","Opinel","1890",W+"Opinel_knife",
    [V("No. 1 (discontinued 1932) and No. 11 (1935)","Opinel","","numbered sizes now run 2–13"),V("Virobloc locking collar","Opinel","1955","patented by Marcel Opinel"),V("double-locking collar","Opinel","2000","also locks the blade closed")],
    "size No. 2–13 · XC90 carbon or Sandvik 12C27M stainless · beech, oak, walnut, olive, horn handle",a="Opinel No. 08 · Opinel knife"),
  old('Traditional folding knife','Higonokami')]}
fric['x'][1]['s']=W+'Higonokami'
fric['x'][1]['v']=[V("Nagao Kanekoma higonokami","Nagao Kanekoma","1896","only maker allowed to market knives simply as 'higonokami'; others use 'Higo' or 'Higonokami-style'")]
lock={"n":"Lockback folder","a":"back lock · spine lock · Buck knife","d":"Folding knife with a spring-loaded hook on the spine that engages a notch in the blade tang.",
 "t":["Tri-Ad lock","serrated edge","FRN or G10 handle"],"s":W+"Pocketknife",
 "x":[
  A("Buck 110 Folding Hunter","Brass-bolstered lockback hunter that made 'buck knife' a generic name for lockback folders.","Buck","1964",W+"Buck_Knives",
    [V("420HC blade steel","Buck","1993","used on most since"),V("110 LT lightweight FRN","Buck","2018","")],"wood or synthetic handle · brass bolsters · 3¾ in blade",a="Buck 110"),
  old('Folding knife','Spyderco Delica'),old('Folding knife','Spyderco Worker')]}
lock['x'][1]['s']=W+'Spyderco'
lock['x'][1]['v']=[V("Delica 4","Spyderco","","VG-10 full-flat blade, made in Japan")]
lock['x'][1]['d']="Light FRN-handled lockback with the round thumb hole; the Endura is its larger sibling."
liner={"n":"Liner-lock & frame-lock folder","a":"linerlock · framelock · integral lock","d":"Folder whose blade is held by a spring-loaded side liner, or by the handle frame itself in a frame lock.",
 "t":["assisted opening","flipper","pin-and-dimple lock","titanium handle"],"s":W+"Liner_lock",
 "x":[
  old('Folding knife','Chris Reeve Sebenza'),
  A("Walker Linerlock","Michael Walker's refined side-spring lock, trademarked as 'Linerlock' in 1990; basis of most modern liner locks.","","1980s",W+"Liner_lock",[V("Cattaraugus liner-lock patent No. 825,093","","1906","early precedent")],"custom or production; Walker held the Linerlock trademark"),
  A("Chris Reeve Umnumzaan","Large Sebenza-derived folder with a second-generation Integral Lock and an exposed glass breaker.","Chris Reeve Knives","2008",W+"Chris_Reeve_Knives",[],"titanium slabs · CPM S30V blade · 93.4 mm blade"),
  A("Chris Reeve Mnandi","Compact Integral Lock folder with cosmetic inlay, aimed at business wear.","Chris Reeve Knives","2001",W+"Chris_Reeve_Knives",[],"69.5 mm blade · inlay · Damascus option"),
  A("Chris Reeve Inkosi","Integral Lock folder with large hollow grind, twin oversized washers and ceramic-ball lock interface.","Chris Reeve Knives","2015",W+"Chris_Reeve_Knives",[],""),
  old('Folding knife','Kershaw Leek')]}
sb=liner['x'][0]
sb['s']=W+'Chris_Reeve_Knives'
sb['d']="Titanium-handled folder whose Integral Lock is the best-known frame lock."
sb['v']=[V("Sebenza 21","Chris Reeve Knives","","21st-anniversary generation; large version has 0.125 in blade stock"),V("Sebenza 25","Chris Reeve Knives","2012","ceramic-ball lockbar interface, larger pivot, 0.14 in blade stock")]
sb['dt']="small or large · titanium handle · inlays · ATS-34, S35VN or S45VN blade"
lk=liner['x'][5]; lk['s']='https://agrussell.com/ecommerce/products/view/2844'
cross={"n":"Crossbar-lock folder","a":"AXIS lock folder","d":"Folder whose blade is held by a spring-loaded crossbar sliding in slots in both handle scales.",
 "t":["manual","automatic","mini","lightweight handle"],"s":W+"Benchmade",
 "x":[
  A("Benchmade Griptilian","Benchmade's everyday AXIS-lock folder, made in full and Mini sizes.","Benchmade","",W+"Benchmade",[V("551 Griptilian","Benchmade","2014","Gear of the Year award"),V("556 Mini Griptilian","Benchmade","","smaller sibling")],"full or mini size · blade shape · handle colour",a="Griptilian · 550 · 551"),
  A("Benchmade Bugout","Slim, light AXIS-lock folder with a 535 full size and a 533 Mini.","Benchmade","",W+"Benchmade",[V("535 Bugout","Benchmade","","full size"),V("533 Mini Bugout","Benchmade","","smaller sibling")],"handle material · blade steel",a="Bugout 535"),
  A("Benchmade 940 Osborne","Benchmade AXIS-lock folder listed as the 940 Osborne.","Benchmade","",W+"Benchmade",[],"handle material · blade steel",a="940 · Osborne")]}
comp={"n":"Compression-lock folder","a":"Spyderco compression lock","d":"Folder whose blade is held by a spring-loaded insert in the handle spine, released by pressing it.",
 "t":["button lock"],"s":"https://www.knivesandtools.com/en/ct/spyderco-paramilitary-knives.htm",
 "x":[
  A("Spyderco Paramilitary 2","Spyderco folder with the strong Compression Lock and full-flat blade; slimmer, lighter and better balanced than the original Paramilitary.","Spyderco","","https://www.knivesandtools.com/en/ct/spyderco-paramilitary-knives.htm",
    [V("Paramilitary","Spyderco","","original; replaced by the Paramilitary 2")],"G10 colour · blade steel (S30V, S45VN, MagnaCut and others) · four-way clip",a="PM2 · Para 2 · C81"),
  A("Spyderco Para 3","The Paramilitary 2 rebuilt around a three-inch blade; same handle width.","Spyderco","2016","https://www.dlttrading.com/spyderco-para-3",
    [V("first run, S30V, black G10","Spyderco","2016","shipped December")],"CPM S45VN blade · 2.93 in blade · G10 or FRN handle",a="Para 3 · C223")]}
fold_k=[slip,fric,lock,liner,cross,comp]
# --- Swiss Army
sw=copy.deepcopy(oldk['Swiss Army knife']); 
sold=[a for a in sw['x'] if a['n']=='Swiss soldier\'s knife'][0]
sold['v']=[V("Modell 1890","","1891","100 mm, spear point; first 15,000 from Wester & Co., Solingen"),V("Modell 1908","","1908–1951","100 mm, clip point"),V("Modell 1951","","1951–1961","93 mm; first with stainless tools"),V("Modell 1961","","1961–2008","93 mm; anodised aluminium handle"),V("Soldatenmesser 08","Victorinox","2008","111 mm; dual liner lock")]
sold['s']=W+'Swiss_Army_knife'
off=[a for a in sw['x'] if a['n']=="Officer's knife"][0]; off['v']=[]
off['d']="Karl Elsener's two-blade knife with corkscrew, patented in 1897 as the Offiziers- und Sportmesser."
sw['x']=[sold,off,
 A("Victorinox Spartan","Base 91 mm Victorinox knife with two layers and 12 functions; other 91 mm models add tools to it.","Victorinox","","https://dwights.co.nz/products/victorinox-spartan",[],"91 mm · scale colour or wood"),
 A("Victorinox Huntsman","91 mm Victorinox knife with 15 functions including scissors and wood saw.","Victorinox","","https://dwights.co.nz/products/victorinox-huntsman",[],"91 mm · scale colour"),
 A("Victorinox Classic SD","Micro Victorinox knife about 58 mm long with seven functions, small enough for a keyring.","Victorinox","","https://hiconsumption.com/best-keychain-multi-tools/",[],"58 mm · scale colour",a="Classic"),
 A("Victorinox Cybertool","Large 91 mm Victorinox with pliers and bit holder among about 39–41 functions.","Victorinox","","https://knivesandtools.com/en/pt/-victorinox-cybertool-with-41-functions-transparent-red.htm",[],"39 or 41 functions · scale colour",a="CyberTool"),
 [a for a in sw['x'] if a['n']=='SwissChamp'][0],
 [a for a in sw['x'] if a['n']=='Wenger Giant'][0]]
sw['x'][5]['v']=[V("SwissChamp XXLT","Victorinox","2002–2005","with butane lighter"),V("SwissChamp XAVT","Victorinox","2006","80 functions")]
sw['x'][5]['d']="Victorinox's large multi-layer flagship with 33 functions; it followed the Champion as flagship in 1986."
sw['x'][5]['s']=W+'Swiss_Army_knife'
sw['x'][6]['s']=W+'Swiss_Army_knife'
sw['m']=[["Companion","Victorinox"]]
sw['t']=["58 mm","74 mm","84 mm","91 mm","111 mm","130 mm"]
# --- fixed blade
fb=copy.deepcopy(oldk['Fixed-blade bushcraft knife'])
fb['n']="Fixed-blade EDC & bushcraft knife"; fb['a']="bushcraft knife · sheath knife · outdoor knife · belt knife"
mora=fb['x'][0]; mora['v']=[V("Clipper 840/860","Morakniv","","discontinued; replaced by Companion MG"),V("Companion MG","Morakniv","","carbon or stainless"),V("Bushcraft series","Morakniv","",""),V("Garberg","Morakniv","","full tang")]
fb['x'].append(A("ESEE-4","Full-tang 1095 drop-point knife of ESEE's numbered range, between the ESEE-3 and the heavier ESEE-5.","ESEE","","https://bladereviews.com/esee-4-review/",[V("ESEE-3","ESEE","","same handle, thinner blade"),V("ESEE-5","ESEE","","heavier duty")],"4.5 in 1095 blade, powder-coated, or 440C stainless · handle scales · sheath",a="ESEE 4"))
fb['x'].append(A("Ka-Bar Becker BK2 Companion","Ethan Becker's thick 1095 Cro-Van drop-point fixed blade with plastic handle.","Ka-Bar","","https://www.messerworld.de/en/ka-bar/becker-companion-bk2.html",[V("BK22","Ka-Bar","","same knife with nylon sheath")],"13.3 cm blade, 6.4 mm thick · sheath",a="BK2 · BK22"))
fb['m']=[["162 Bushcrafter","Benchmade"]]
ut=copy.deepcopy(oldk['Utility knife']); ut['m'].append(["Quickslide Pocket Knife","Stanley"])
# --- multitools
mt=oldk['Multi-tool']
L='https://en.wikipedia.org/wiki/Leatherman'
def Lm(n,d_,y,v,dt='',a=''): return A(n,d_,'Leatherman',y,L,v,dt,a)
plier={"n":"Plier multi-tool","a":"pocket multi-tool · multitool · multi-tool pliers","d":"Pocket tool with pliers and folding implements (knife, scissors, drivers, file, saw) in its handles.",
 "t":["butterfly-opening pliers","sliding pliers","pocket size","full size","heavy duty"],"s":"https://leatherman.com/collections/leatherman-multi-tools",
 "x":[
  Lm("Leatherman PST","Tim Leatherman's folding-plier Pocket Survival Tool, the originator of the plier multi-tool.","1983",[V("PST","Leatherman","1983–2004","14 tools"),V("PST II","Leatherman","1996–2004","15 tools")],"",a="Pocket Survival Tool"),
  Lm("Leatherman Super Tool","Heavy-duty full-size Leatherman.","1994",[V("Super Tool","Leatherman","1994–2001","18 tools"),V("Super Tool 200","Leatherman","2001–2005","18 tools"),V("Super Tool 300","Leatherman","2009","19 tools")]),
  Lm("Leatherman Wave","Full-size Leatherman with outside-opening blades.","1998",[V("Wave (Original)","Leatherman","1998–2004","16 tools"),V("Wave (New)","Leatherman","2004–2018","17 tools"),V("Wave+","Leatherman","2018","18 tools")]),
  Lm("Leatherman Charge","Premium full-size Leatherman on the Wave layout.","2004",[V("Charge Ti / XTi","Leatherman","2004–2008",""),V("Charge AL / ALX / TTi","Leatherman","2007–2018",""),V("Charge+ / Charge+ TTi","Leatherman","2018","19 tools")]),
  Lm("Leatherman Surge","Heavy-duty Leatherman with 21 tools.","2005",[V("Surge (Original)","Leatherman","2005–2013",""),V("Surge (New)","Leatherman","2013","")]),
  Lm("Leatherman Skeletool","Pocket-size skeletonised Leatherman with seven tools.","2007",[V("Skeletool / Skeletool CX","Leatherman","2007",""),V("Skeletool SX","Leatherman","2013","retired"),V("Skeletool RX","Leatherman","2016","")]),
  Lm("Leatherman Rebar","Full-size Leatherman with 17 tools.","2012",[]),
  Lm("Leatherman Free","Magnet-assisted Leatherman line with P2 and P4 plier models and K and T pocketknife and tool versions.","2019",[V("Free P2","Leatherman","2019","19 tools; retired 2025"),V("Free P4","Leatherman","2019","21 tools; retired 2025")]),
  A("Gerber Multi-Plier 600","Gerber multi-tool whose plier head slides out on rails and opens one-handed; first called the Multi-Lock.","Gerber","1998","https://wiki.multitool.org/Multi-Plier+600",
    [V("Basic","Gerber","1998","original"),V("Pro Scout","Gerber","","warncliffe blade and scissors"),V("Bladeless","Gerber","","for workplaces that ban knives"),V("DET","Gerber","","explosives-disposal version"),V("Sight Tool MP600ST","Gerber","","modified frame")],"needlenose or bluntnose · wire cutters · finish",a="MP600 · Multi-Lock"),
  A("Gerber Suspension","Gerber butterfly-opening multi-tool; Truss and Suspension-NXT followed it.","Gerber","",'https://en.wikipedia.org/wiki/Gerber_Legendary_Blades',[],""),
  old('Multi-tool','Victorinox SwissTool')]}
plier['x'][-1]['s']=W+'Victorinox'
plier['x'][-1]['d']="Victorinox's plier multi-tool, with pliers and other tools folded into the grips."
key={"n":"Keychain & wearable multi-tool","a":"mini multi-tool · key-ring tool","d":"Small multi-tool carried on a keyring or the wrist, usually with scissors or a small blade rather than full pliers.",
 "t":["scissor-based","wearable bracelet"],"s":"https://hiconsumption.com/best-keychain-multi-tools/",
 "x":[
  Lm("Leatherman Micra","Keychain Leatherman with scissors, small blade and tweezers; ten tools.","1996",[V("Micra 30th anniversary","Leatherman","2013","limited edition"),V("Micra 35th anniversary","Leatherman","2018","limited edition")]),
  Lm("Leatherman Squirt","Keychain Leatherman with small pliers.","2002",[V("Squirt P4 / S4 / E4","Leatherman","2002–2010","10 tools"),V("Squirt ES4","Leatherman","2010–2021","9 tools"),V("Squirt PS4","Leatherman","2010","9 tools")]),
  Lm("Leatherman Style","Small keychain Leatherman with pliers or scissors.","2010",[V("Style","Leatherman","2010–2014","5 tools"),V("Style CS","Leatherman","2010–2021","6 tools"),V("Style PS","Leatherman","2012","8 tools")]),
  Lm("Leatherman Tread","Wearable bracelet multi-tool with 29 tools.","2015",[V("Tread / Tread Metric / Tread LT","Leatherman","2015–2021","")])]}
# --- sharpeners
shp={"n":"Pocket knife sharpener","a":"knife sharpening kit · guided sharpener · sharpening stone","d":"Stone, rod or guided kit for restoring the edge of pocket and field knives.",
 "t":["oilstone","Arkansas stone","diamond plate","ceramic rod","guided system"],"s":W+"Sharpening_stone",
 "x":[A("Spyderco Tri-Angle Sharpmaker","Ceramic-rod kit with slots setting fixed 30° or 40° angles for knives; used dry.","Spyderco","","https://varusteleka.com/en/products/spyderco-triangle-sharpmaker",[],"medium brown and fine white rods · diamond and ultra-fine rod options",a="Sharpmaker 204")]}
# --- EDC tools
pen={"n":"EDC pen","a":"tactical pen · space pen","d":"Pressurised-cartridge or machined pen carried daily, sometimes with a glass-breaker point.",
 "t":["bullet pen","retractable","glass breaker"],"s":W+"Fisher_Space_Pen",
 "x":[A("Fisher Bullet Space Pen","Short non-retractable pen that becomes full size with the cap posted; writes upside down on a pressurised cartridge.","Fisher Space Pen","",W+"Fisher_Space_Pen",[V("AG7 Astronaut pen","Fisher Space Pen","1965","patented by Paul Fisher")],"finish · cartridge ink",a="Bullet Space Pen"),
      A("Tuff-Writer Frontline","Machined aluminium tactical pen with a sharp and a round end and glass-breaking tip, using a pressurised cartridge.","Tuff-Writer","","https://soldiersystems.net/2008/10/08/tuff-writer-tactical-pens/",[],"Stealth Black, Sniper Grey or Desert Brown")]}
pry={"n":"Pry bar & keychain tool","a":"EDC pry bar · pocket tool","d":"Small one-piece steel or titanium tool for prying, screwdriving and bottle opening, carried on a key ring.",
 "t":["titanium","stainless","with blade","with clip"],"s":"https://werd.com/best-edc-pry-bars/",
 "x":[A("Gerber Shard","One-piece coated-steel keychain tool under 3 in long with pry bar, drivers, wire stripper and bottle opener.","Gerber","","https://hiconsumption.com/best-keychain-multi-tools/",[],"coating"),
      A("Gerber Prybrid","Pry bar with retractable utility blade, nail puller and bottle opener.","Gerber","","https://werd.com/best-edc-pry-bars/",[V("Prybrid X","Gerber","","paracord-wrapped handle, No. 11 scalpel blade")],""),
      A("Nite Ize DoohicKey","Budget stainless keyring tool with hex openings, ruler and bottle opener plus a built-in clip.","Nite Ize","","https://hiconsumption.com/best-keychain-multi-tools/",[],"")]}
shelves=[{"n":"Folding knives","k":fold_k},{"n":"Swiss Army knives","k":[sw]},{"n":"Fixed blades & utility knives","k":[fb,ut]},
 {"n":"Multi-tools","k":[plier,key]},{"n":"Knife sharpeners","k":[shp]},{"n":"Everyday-carry tools","k":[pen,pry]}]
axes=[s for s in dept['s'] if s['n'].startswith('Axes')]
dept['s']=shelves+axes
dept['b']=[{"m":"Lock or opening mechanism","v":"slip joint, lockback, liner or frame lock, crossbar lock, compression lock, friction","w":"The axis owners use to tell folding-knife kinds apart."}]+[x for x in dept['b'] if x['m']!='Lock and action']
# write
out=copy.deepcopy(d)
for i,x in enumerate(out['depts']):
    if x['n'].startswith('Knives'): out['depts'][i]=dept
json.dump(out,open('C1.new.json','w'),ensure_ascii=False,indent=1)
