import json,copy
P='/home/user/Possession-Taxonomy/rebuild/out/'
d=json.load(open(P+'D4.json'))
W='https://en.wikipedia.org/wiki/'
def A(n,mk,y,s,dd,v=None,dt=None,a=''):
    x={"n":n,"a":a,"d":dd,"mk":mk,"y":y,"s":s}
    if v: x["v"]=[{"n":i[0],"mk":mk,"y":i[1] if len(i)>1 else "", **({"d":i[2]} if len(i)>2 else {})} for i in v]
    if dt: x["dt"]=dt
    return x
def find(n):
    for dp in d['depts']:
        for s in dp['s']:
            for k in s['k']:
                if k['n']==n: return dp,s,k
    raise KeyError(n)
def dept(n): return [x for x in d['depts'] if x['n']==n][0]
def shelf(dp,n): return [x for x in dp['s'] if x['n']==n][0]
def rm(n):
    dp,s,k=find(n); s['k'].remove(k); return k
def merge(names,newname,alias,defn,shelfname,pos_after=None,types=None):
    ks=[rm(n) for n in names]
    m=[];r=[];t=[]
    for k in ks:
        for i in k.get('m',[]):
            if i not in m: m.append(i)
        for i in k.get('r',[]):
            if i not in r: r.append(i)
    for k in ks:
        t.append(k['n'][0].lower()+k['n'][1:])
        for i in k.get('t',[]):
            if i not in t: t.append(i)
    if types is not None: t=types
    new={"n":newname,"a":alias,"d":defn,"t":t,"s":next(k['s'] for k in ks if k.get('s'))}
    if m:new["m"]=m
    if r:new["r"]=r
    return new,ks
# --- D4-1 cine film camera
fa=dept('Film cameras')
fa['s'].append({"n":"Cine film cameras","k":[{
 "n":"Cine film camera","a":"movie camera · Super 8 camera · 16 mm camera · cine camera",
 "d":"Hand-held motion-picture camera shooting 8 mm, Super 8 or 16 mm film, mostly spring-wound or battery-driven.",
 "t":["Super 8 (cartridge)","Double 8 / 8 mm","16 mm","9.5 mm","silent","sound"],
 "s":W+"Bolex",
 "x":[
  A("Bolex H16","Bolex","1935",W+"Bolex","Swiss spring-wound 16 mm camera with a three-lens turret; the reference amateur and artist 16 mm body.",[["H16","1935"],["H16 Reflex","1956","first H16 with a reflex viewfinder"],["H16 RX-5","1966"]],"mount C · turret or Reflex · spring or electric motor"),
  A("Bolex H8","Bolex","1936",W+"Bolex","Smaller 8 mm sibling of the H16 on the same spring-motor layout.",[["H8S","1936"],["H8RX","1963"]],"8 mm · Double-8 from 1938"),
  A("Beaulieu R16","Beaulieu","1958",W+"Beaulieu_(company)","French 16 mm reflex camera with removable lenses, offered in spring-motor and electric versions.",[["R16","1958","spring motor"],["R16 Electric","1965"]],"C-mount lenses · reflex viewfinder"),
  A("Beaulieu 4008","Beaulieu","1960s",W+"Beaulieu_(company)","Super 8 reflex camera line that followed the 2008 S (1965), the maker's first Super 8 model.",[["2008 S","1965","first Beaulieu Super 8"],["4008 ZM"],["4008 ZM2"],["4008 ZM3"],["4008 ZM4","","silent Super 8 model"]],"reflex mirror shutter · removable C-mount lenses"),
  A("Canon 514XL","Canon","1975","https://global.canon/en/c-museum/product/cine292.html","Super 8 cartridge camera with a 9–45 mm f/1.4 zoom lens; still widely shot on film.",None,"5x zoom · manual focus from 1.2 m"),
  A("Nizo Super 8","Nizo","",  "https://www.filmkorn.org/super8data/database/cameras_list/cameras_nizo/cameras_nizo.htm","Braun Nizo Super 8 cameras, prized for their lenses and exposure control.",[["6080 Sound"],["4080 Sound"],["801"],["561"],["481"],["156"]],"sound or silent · macro versions · silver or black"),
 ]}]})
# --- D4-2 film SLR / rangefinder
_,_,k=find('Film SLR camera')
k['x']+= [
 A("Zenit","KMZ","1952",W+"Zenit_(camera)","Soviet 35 mm SLR made in vast numbers, based on the Zorki rangefinder.",[["Zenit-E","","external selenium meter, over 12 million made with subtypes"],["Zenit-TTL","","through-the-lens metering"],["Zenit 12XP","","sold with Helios 58 mm f/2"],["Zenit-122K / 212K","","Pentax K mount"]],"M42 thread mount (earlier M39) · KMZ or BelOMO"),
 A("Praktica","Pentacon","1949",W+"Praktica","East German M42 SLR line from Dresden, from 1949 to 1990 under Pentacon.",[["L series","1969","first generation 1969–1978"],["MTL 3","1978","1978–1984"],["MTL 5","1983"],["MTL 5B","1985"],["B series","1979","B 200 to BMS"],["BX series","1987","BX 20 to BX 20 S"]],"M42 thread mount · generations L, MTL, B, BX"),
 A("Minolta Maxxum 7000","Minolta","1985",W+"Minolta_Maxxum_7000","First SLR with integrated autofocus and motorised film advance; introduced the A lens mount.",None,"Maxxum in North America, Alpha 7000 in Japan · A-mount"),
 A("Leica R","Leica","1976",W+"Leica_R3","Leica manual-focus SLR line on the R bayonet, from the Minolta-based R3 to the R8 and R9.",[["R3","1976"],["R4","1980"],["R5","1987"],["R6","1988"],["R7","1992"],["R8"],["R9"]],"R bayonet mount"),
]
_,_,k=find('Film rangefinder camera')
k['x']+= [
 A("FED","FED","1934",W+"FED_(camera)","Soviet Leica II copy in 39 mm screw mount, made in Kharkiv from 1934.",[["FED 1","1934","made 1934–1955"],["FED 2","1955"],["FED 3"],["FED 4","1964","selenium meter"]],"Leica-type M39 screw mount"),
 A("Zorki","KMZ","1948",W+"Zorki","Soviet Leica II copy from Krasnogorsk, made 1948 to 1978.",[["Zorki","1948","1948–1956"],["Zorki 4","1956","over 2 million made"],["Zorki 4K","1972","advance lever"]],"Leica-type M39 screw mount"),
 A("Canonet QL17","Canon","1960s",W+"Canon_Canonet","Fixed-lens 35 mm rangefinder for enthusiasts on a budget, with quick-loading film.",[["Canonet QL17"],["Canonet QL17 New"],["Canonet QL17-L New"],["Canonet QL17 GIII"],["Canonet QL19","","wider f/1.9 lens"]],"fixed lens · shutter-priority auto exposure"),
 A("Yashica Electro 35","Yashica","1966",W+"Yashica_Electro_35","Fixed-lens rangefinder with electronic aperture-priority exposure.",[["Electro 35","1966"],["Electro 35 G","1968"],["Electro 35 GT","1969","black body"],["Electro 35 GS / GT","1970","gold-plated contacts"],["Electro 35 GSN / GTN","1973","hot shoe added"]],"fixed lens · satin chrome or black"),
]
# --- D4-3 digital
_,_,k=find('DSLR camera')
k['x']+= [
 A("Nikon D1","Nikon","1999",W+"Nikon_D1","First Nikon-designed digital SLR, 2.7 MP DX CCD on the F mount.",[["D1","1999"],["D1H","","5 frames per second"],["D1X","","5.3 MP interpolated"]],"DX format · F mount"),
 A("Kodak DCS","Kodak","1991",W+"Kodak_DCS","Kodak digital backs on Nikon and Canon bodies, the first commercial DSLRs.",[["DCS 100","1991","on Nikon F3"],["DCS 200","1992"],["DCS 400 series","1994"],["DCS 520 / 560","1998","on Canon EOS-1n"],["DCS 620 / 660","1999","on Nikon F5"],["DCS 700 series","2001"],["DCS Pro 14n","2002","full frame"]],"Nikon F or Canon EF base body"),
 A("Canon EOS Rebel (xxxD)","Canon","2003",W+"Canon_EOS_300D","Entry-level Canon DSLR line, sold as Rebel in the Americas and xxxD elsewhere.",[["EOS 300D","2003","Digital Rebel; first with EF-S mount"],["EOS 350D"],["EOS 400D"],["EOS 450D"]],"APS-C · EF-S mount"),
 A("Nikon D3000 series","Nikon","2009",W+"Nikon_D3000","Entry-level Nikon DX DSLRs; the D3000 was the last Nikon DSLR with a CCD.",[["D3000","2009"],["D3100","2010"]],"DX format · F mount"),
 A("Sony A-mount DSLR","Sony","2006",W+"Sony_Alpha_100","Sony Alpha DSLRs on the Minolta A mount from 1985, so Minolta AF lenses still fit.",[["α100","2006"],["α700","2007"],["α900","2008","full frame"],["α77","2011","SLT"],["α99 II","2016","SLT, full frame"]],"A-mount · APS-C and full frame"),
]
_,_,k=find('Compact camera')
k['x']=[
 A("Canon IXUS / ELPH","Canon","2000",W+"Canon_Digital_IXUS","Slim Canon digital compacts, sold as IXUS, IXY Digital or PowerShot ELPH.",[["Digital IXUS","2000"],["IXUS 800 IS","2006","first with stabilisation"],["IXUS 900 Ti","2006","titanium body"],["IXUS 300 HS","2010","first CMOS"]],"regional names IXUS, IXY, ELPH"),
 A("Canon PowerShot G","Canon","2000",W+"Canon_PowerShot_G","Enthusiast compacts with manual control, from the G1 to the 1-inch G7 X.",[["G1","2000"],["G9","2007","RAW restored"],["G7 X","2014","1-inch sensor"]],"vari-angle screen on early models"),
 A("Fujifilm FinePix","Fujifilm","1998",W+"Fujifilm_FinePix","Fujifilm digital compact range that began with the MX-700.",[["MX-700","1998"],["A series","2001"],["Z series","2005"]],"A, E, Z, F and T series"),
 A("Sony Cyber-shot","Sony","1996",W+"Sony_Cyber-shot","Sony digital compact brand introduced in 1996, later home of the RX100 pocket compact.",None,"DSC code · Carl Zeiss lens on many models"),
]
_,_,k=find('Camcorder')
k['x']=[A("Sony Handycam","Sony","1985",W+"Handycam","Sony consumer camcorder brand from the first Video8 model, through Hi8 and Digital8 to 4K.",[["Video8","1985"],["Hi8","1989"],["Digital8","1999"]],"tape format · later DV, HDV, card and 4K")]
# --- D4-4 light meter
_,_,k=find('Light meter')
k['x']=[
 A("Weston Master","Weston","","https://camera-wiki.org/wiki/weston","Selenium-cell exposure meter, the standard hand meter for decades; cine version sold as Bolexmeter.",[["Master","","Weston 715 / S74"],["Master II","","Weston 735"],["Master III","","Weston 737"],["Master IV","","Weston 745"],["Master V","","Weston 748"]],"selenium cell · Invercone dome"),
 A("Gossen Lunasix","Gossen","1961","https://camera-wiki.org/wiki/Gossen","Gossen's first professional meter, sold as Luna Pro; ambient light only.",[["Lunasix","1961"],["Profisix","1977","ambient and flash"],["Mastersix","1983","microprocessor-controlled"]],"CdS or silicon cell · Luna Pro in some markets"),
 A("Sekonic L-398","Sekonic","1976","https://camera-wiki.org/wiki/Sekonic_L-398","Analogue incident-light meter with a dome, still in production.",[["L-398 Studio Deluxe","1976"],["L-398M Studio Deluxe II","1989"],["L-398A Studio Deluxe III","2006","amorphous photocell"]],"dome and flat diffuser · gold editions"),
]
# --- D4-5 darkroom
dr=dept('Film & darkroom')
dev=shelf(dr,'Film developing'); enl=shelf(dr,'Enlarging & printing')
defs=[
 (['Developing tank','Developing reel','Changing bag','Darkroom thermometer','Darkroom graduate','Film dryer'],'Tanks, reels & film handling','developing tank · film reel · changing bag','Tank, reels and handling tools used to load, develop and dry film.',dev),
 (['Film developer','Stop bath and fixer','Paper developer'],'Darkroom chemistry','film developer · fixer · paper developer','Developer, stop bath and fixer for film and paper.',dev),
 (['Enlarger','Enlarging lens','Negative carrier','Enlarger filter'],'Enlarger','enlarging lens · negative carrier','Projector that exposes a negative onto paper; sold with lens, carrier and filters.',enl),
 (['Enlarging easel','Focus finder','Contact printing frame','Darkroom timer'],'Easel & focus aids','print easel · grain focuser · contact frame','Easel, focus finder, contact frame and timer for positioning and exposing prints.',enl),
 (['Developing tray','Print tongs','Print washer','Print dryer','Safelight'],'Trays, tongs & washers','trays · tongs · print washer','Trays, tongs, washers, dryers and safelights for processing prints.',enl),
]
# paper keep as is
for names,nn,al,df,sh in defs:
    dpn,sold,_=find(names[0])
    new,ks=merge(names,nn,al,df,sh.get('n'))
    # place at index of first removed kind's shelf -> append to target shelf
    sh['k'].append(new)
# order shelves: keep paper last in enl
pap=[k for k in enl['k'] if k['n']=='Photographic paper'][0]; enl['k'].remove(pap); enl['k'].append(pap)
# --- D4-6 modifiers
lt=dept('Flash & studio lighting'); mod=shelf(lt,'Light modifiers')
for names,nn,al,df in [
 (['Softbox','Umbrella'],'Softbox & umbrella','softbox · umbrella · diffuser','Fabric light modifier that softens and spreads flash or continuous light.'),
 (['Portable reflector','Beauty dish','Reflector dish'],'Reflectors & dishes','reflector · beauty dish','Reflector or dish that bounces or focuses light on the subject.'),
 (['Grid','Snoot','Barn doors','Colour gel','Gobo','Flag, net or overhead frame'],'Beam shapers & gels','grid · snoot · barn doors · gel · gobo · flag','Attachments that narrow, block or colour the light beam.'),
]:
    new,_=merge(names,nn,al,df,'Light modifiers'); mod['k'].append(new)
# gimbals & video support
vs=shelf(dept('Tripods & camera support'),'Video support & motion')
pg=rm('Pocket gimbal camera'); hg=rm('Handheld gimbal')
gm=hg['m']+[i for i in pg.get('m',[]) if i not in hg['m']]
gimbal={"n":"Gimbal stabiliser","a":"handheld gimbal · gimbal camera · pocket gimbal camera","d":"Motorised handheld stabiliser that keeps a camera level; some models have the camera built in.","t":["handheld gimbal for camera","phone gimbal (see D2)","pocket gimbal camera (built-in camera)"],"s":hg['s'],"m":gm,"r":pg.get('r',[])}
new,_=merge(['Camera cage','Camera rig','Camera clamp','Body-worn camera support'],'Camera rig & cage','cage · rig · clamp · body-worn support','Frame, rig, clamp or harness that holds a camera and accessories.','')
new2,_=merge(['Camera slider','Camera dolly','Camera crane'],'Slider, dolly & crane','slider · dolly · jib','Track, wheeled or arm support that moves a camera smoothly through a shot.','')
vs['k']=[gimbal,new,new2]
# --- D4-7 notes
dept('Lenses & filters')['note']="Lenses are grouped by optical type (prime, zoom, macro and so on); mount is a detail on each archetype, not a grouping axis. Filters and adapters are tier."
dept('Camera accessories & parts')['note']="Tier mode: kinds and market-covering makers only, no archetypes. Listed by kind, not by SKU."
json.dump(d,open(P+'D4.json.tmp','w'),ensure_ascii=False,indent=1)
