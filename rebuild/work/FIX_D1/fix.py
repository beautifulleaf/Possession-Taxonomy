import json,copy,os
P='/home/user/Possession-Taxonomy/rebuild/out/'
d=json.load(open(P+'D1.json')); br=json.load(open(P+'D1_brands.json')); mv=json.load(open(P+'D1_moves.json'))
def loc(n):
    for di,dp in enumerate(d['depts']):
        for si,s in enumerate(dp['s']):
            for ki,k in enumerate(s['k']):
                if k['n']==n: return dp,s,k
def pop(n):
    dp,s,k=loc(n); s['k'].remove(k); return k
def arch(k,n):
    for a in k['x']:
        if a['n']==n: return a
def popA(k,n):
    a=arch(k,n); k['x'].remove(a); return a
def V(n,y='',dd='',mk=''):
    v={'n':n}
    if mk:v['mk']=mk
    if y:v['y']=y
    if dd:v['d']=dd
    return v
W='https://en.wikipedia.org/wiki/'
# D1-1 vintage platforms
hc=loc('Home computer (keyboard computer)')[2]
hc['x']+= [
 {'n':'TI-99/4A','a':'TI-99/4','d':'Texas Instruments home computer with a full-travel keyboard and cartridge port.','mk':'Texas Instruments','y':'1981','s':W+'TI-99/4A','v':[V('TI-99/4','1979','Calculator-style keyboard'),V('TI-99/4A','1981','Full-travel keyboard'),V('QI-99/4A','1983','Quality-improved board, some with cartridge lockout chip')],'dt':'case black with aluminium trim, later beige'},
 {'n':'Sinclair QL','a':'Quantum Leap','d':'Sinclair business and home computer with a Motorola 68008 and Microdrives.','mk':'Sinclair Research','y':'1984','s':W+'Sinclair_QL','v':[V('Sinclair QL','1984','Early units had firmware on an external ROM cartridge'),V('ICL One Per Desk','','QL-based office telephone computer'),V('Thor','','Compatible systems made after Amstrad dropped the QL')]},
 {'n':'Dragon 32 / 64','a':'Dragon Data','d':'Welsh-built home computer compatible with the Tandy Color Computer.','mk':'Dragon Data','y':'1982','s':W+'Dragon_32/64','v':[V('Dragon 32','1982','32 KB, beige case'),V('Dragon 64','1983','64 KB, serial port, light grey case'),V('Dragon 200','','Eurohard case redesign'),V('Tano Dragon','','US-market version')]},
]
vd=loc('Vintage desktop computer')[2]
vd['x']+=[
 {'n':'Apple Lisa','a':'','d':'Apple office computer with a graphical interface and a built-in screen.','mk':'Apple','y':'1983','s':W+'Apple_Lisa','v':[V('Lisa 1','1983','Two Twiggy floppy drives'),V('Lisa 2','1984','Single 400K microfloppy; 2/5 and 2/10 with ProFile'),V('Macintosh XL','1985','Lisa 2/10 rebranded')]},
 {'n':'Sharp X68000','a':'X68k','d':'Sharp Japan-only 16-bit home computer known for arcade-quality ports.','mk':'Sharp Corporation','y':'1987','s':W+'Sharp_X68000','v':[V('X68000','1987','CZ-600C'),V('X68000 ACE','1988','CZ-601C'),V('X68000 EXPERT','1989','CZ-602C'),V('X68000 SUPER','1991','CZ-604C'),V('X68000 XVI','1991','CZ-634C'),V('X68000 Compact','1992','CZ-674C'),V('X68030','1993','CZ-500')]},
]
# D1-7 platform merges
amk=popA(hc,'Commodore Amiga (keyboard models)'); abb=popA(vd,'Amiga big-box')
am=amk; am['n']='Commodore Amiga'; am['d']='Commodore 16/32-bit computer line, in keyboard-case and big-box desktop forms.'
am['v']=[V('Amiga 1000','1985','Big-box')]+[V(x,'', 'Keyboard case') for x in ['Amiga 500','Amiga 500+','Amiga 600','Amiga 1200']]+[V(x,'','Big-box') for x in ['Amiga 2000','Amiga 1500 / 2500','Amiga 3000','Amiga 4000']]
am['y']='1985'; am['dt']='form factor: keyboard case or big-box'
hc['x'].append(am)
st=arch(hc,'Atari ST'); mega=popA(vd,'Atari Mega ST and TT')
st['v']+=[V(x,'','Desktop/tower form') for x in ['Mega ST','Mega STE','TT030']]; st['dt']='form factor: keyboard case or separate desktop'
# vintage laptops to portable kind
lp=loc('Laptop')[2]; port=loc('Luggable & vintage portable')[2]
for n in ['Toshiba T1100','Compaq LTE','IBM ThinkPad 700C']:
    port['x'].append(popA(lp,n))
dyn=arch(lp,'DynaBook'); dyn['y']='1989'
port['x'].append(copy.deepcopy(dyn))   # DynaBook J-3100 (1989) vintage; keep modern lines in Laptop
port['x'][-1]['v']=[v for v in port['x'][-1]['v'] if v['n']=='DynaBook J-3100']
dyn['v']=[v for v in dyn['v'] if v['n']!='DynaBook J-3100']
# NeXTcube -> workstation
ws={'n':'Vintage workstation','a':'Unix workstation · RISC workstation','d':'1980s–90s Unix workstation, usually a pizza-box or cube desktop, from Sun, SGI or NeXT.','t':['pizza-box','cube','tower'],'s':W+'SPARCstation','x':[]}
nc=popA(vd,'NeXTcube')
ws['x']=[
 {'n':'Sun SPARCstation','a':'','d':'Sun Microsystems SPARC pizza-box workstation line.','mk':'Sun Microsystems','y':'1989','s':W+'SPARCstation','v':[V('SPARCstation 1','1989','Sun 4/60'),V('SPARCstation 2','1990','Sun 4/75'),V('SPARCstation 10','1992'),V('SPARCstation 5','1994'),V('SPARCstation 20','1994')]},
 {'n':'SGI Indy','a':'','d':'Silicon Graphics entry MIPS workstation with built-in camera and graphics.','mk':'Silicon Graphics','y':'1993','s':W+'SGI_Indy','v':[V('Indy (R4000/R4400)','1993'),V('Indy R4400 150 MHz','1994'),V('Indy Modeler','1995','R4600 133 MHz')],'dt':'CPU R4000–R5000 · graphics 8-bit XL, 24-bit XL, XZ'},
 {'n':'NeXTstation','a':'','d':'NeXT desktop workstation, the slab-case successor to the NeXTcube.','mk':'NeXT','y':'1990','s':W+'NeXTstation','v':[V('NeXTstation','1990','Greyscale'),V('NeXTstation Color','1990'),V('NeXTstation Turbo','1992','33 MHz'),V('NeXTstation Turbo Color','1992')]},
 nc]
vdp,vds,_=loc('Vintage desktop computer'); vds['k'].insert(vds['k'].index(vd)+1,ws)
# D1-2 CRT monitor
crt={'n':'CRT monitor','a':'cathode-ray tube monitor','d':'Tube display used with vintage and retro computers, prized for 15 kHz RGB or high-end Trinitron picture quality.','t':['15 kHz RGB','VGA','Trinitron'],'s':'https://www.c64-wiki.com/wiki/Commodore_1084','x':[
 {'n':'Commodore 1084','a':'1084S','d':'14-inch RGB colour monitor made for the Amiga and also used with the C64.','mk':'Commodore','y':'','s':'https://www.c64-wiki.com/wiki/Commodore_1084','v':[V('Commodore 1084','','Mono sound'),V('Commodore 1084S','','Stereo sound, headphone socket')]},
 {'n':'Sony GDM-FW900','a':'FW900','d':'24-inch 16:10 widescreen FD Trinitron monitor, sought after by CRT enthusiasts.','mk':'Sony','y':'','s':'https://bgr.com/2109466/robin-williams-24-inch-sony-trinitron-rare-monitor/','dt':'24-inch · 2304x1440 maximum · 80 Hz native'}]}
fl=loc('Floppy disk drive')[2]; vds['k'].insert(vds['k'].index(fl),crt)
# D1-3 artisan makers
ak=loc('Artisan keycap')[2]
mk=lambda n,src:{'n':n,'a':'','d':'Artisan keycap maker selling limited resin or cast keycaps.','mk':n,'y':'','s':'https://mechanicalkeyboards.com/collections/Artisan-Keycaps?page=1','v':[V(x[0]) for x in ak['m'] if x[1]==n]}
ak['x']=[mk('Hot Keys Project',0),mk('Dwarf Factory',0),mk('Varmilo',0)]
for a in ak['x']:
    a['v']=[V(v['n'].replace('HKP ','') if a['mk']=='Hot Keys Project' else v['n']) for v in a['v']]
ak['m']=[]
# D1-4 components merge
def merge(names,newn,defn,al):
    ks=[pop(n) for n in names]; t=[];m=[]
    for k in ks:
        t+=['%s: %s'%(k['n'].lower() if k['n'] not in('LED',) else 'LED',x) for x in k.get('t',[])] or [k['n'].lower()]
        m+=k.get('m',[])
    return {'n':newn,'a':al,'d':defn,'t':t,'s':ks[0]['s'],'m':m}
dp,sh,_=loc('Sensor')
anchor=sh['k'].index(loc('Resistor')[2])
k1=merge(['Resistor','Capacitor','Inductor & transformer','Crystal or oscillator'],'Passive components','Loose resistors, capacitors, inductors and frequency parts for building or repairing circuits.','resistor · capacitor · inductor')
k2=merge(['Transistor','Diode','LED','Microcontroller chip'],'Semiconductors & LEDs','Loose transistors, diodes, LEDs and chips for circuits. A lamp or bulb is in Lighting.','transistor · diode · LED · IC')
k3=merge(['Sensor','Relay','Component connector','Blank RFID tag or card'],'Connectors, relays & modules','Loose sensors, relays, connectors and blank RFID tags for circuits. An issued card is in Documents & Personal Records.','sensor · relay · header')
sh['k'][anchor:anchor]=[k1,k2,k3]
# D1-5 folds
def fold(src,dst,tname,extra_t=True):
    s=pop(src); k=loc(dst)[2]; k.setdefault('t',[]).append(tname); k.setdefault('m',[]).extend(s.get('m',[])); return k
fold('M.2 heatsink','Thermal paste & pads','M.2 SSD heatsink')
fold('PoE injector','Network switch','PoE injector')
fold('Memory-card reader','Drive enclosure','memory-card reader')
ls=pop('Laptop stand'); lc=pop('Laptop cooler'); lsl=pop('Laptop sleeve or case')
dp,sh,_=loc('Monitor arm or stand')
la={'n':'Laptop accessory','a':'laptop stand · laptop cooler · laptop sleeve','d':'Stand, cooling pad or sleeve made to hold, cool or protect a laptop.','t':['stand (no fans)','cooling pad (fans)','sleeve','hard-shell case'],'s':ls['s'],'m':ls['m']+lc['m']+lsl['m']}
sh['k'].append(la)
# D1-6 PSU
psu=loc('PC power supply')[2]; psu['m']=[]
psu['r']+= [['Toughpower GF','Thermaltake'],['ROG Thor','ASUS'],['Ion','Fractal Design'],['Edge','Lian Li'],['MAG A-GL','MSI']]
# D1-8 reorganise
kb=loc('Keyboard')[2]
mag=popA(kb,'Apple Magic Keyboard')
npad=pop('Numeric keypad'); mp=pop('Macro pad')
mdp,msh,_=loc('Mouse'); 
ev={'n':'Everyday keyboards & keypads','k':[]}
# plain keyboard kind holding Magic Keyboard + existing everyday models
ek={'n':'Everyday keyboard','a':'office keyboard · wireless keyboard','d':'Membrane or low-profile keyboard for office and home use rather than enthusiast building.','t':['wired','wireless','low-profile','compact'],'s':kb['s'],'x':[mag],'m':kb['m']}
kb['m']=[]
ev['k']=[ek,npad,mp]
mdp['s'].append(ev)
sec=pop('Security key'); wal=pop('Hardware wallet')
# remove emptied shelf
for dp in d['depts']:
    dp['s']=[s for s in dp['s'] if s['k'] or s['n']=='Security keys & hardware wallets' and False]
d['depts'].insert([x['n'] for x in d['depts']].index('Monitors & peripherals')+1,{'n':'Security & crypto hardware','mode':'mixed','s':[{'n':'Security keys & hardware wallets','k':[sec,wal]}]})
# brands
B=[
 ('Texas Instruments','United States','1930','Mainstream','TI-99/4A','TI home computer maker.','TI-99/4A',W+'TI-99/4A'),
 ('Dragon Data','United Kingdom','1982','Specialist','Dragon 32','Welsh maker of the Dragon 32 and 64.','Dragon 32',W+'Dragon_32/64'),
 ('Sun Microsystems','United States','1982','Professional & flagship','SPARCstation','Unix workstation maker.','SPARCstation',W+'SPARCstation'),
 ('Silicon Graphics','United States','1981','Professional & flagship','Indy workstation','Maker of MIPS graphics workstations.','SGI Indy',W+'SGI_Indy'),
 ('Sony','Japan','1946','Mainstream','Trinitron','Maker of Trinitron monitors.','GDM-FW900','https://bgr.com/2109466/robin-williams-24-inch-sony-trinitron-rare-monitor/'),
 ('Hot Keys Project','United States','','Artisan & independent','Artisan keycaps','Artisan keycap maker.','Hannya',  'https://mechanicalkeyboards.com/collections/Artisan-Keycaps?page=1'),
 ('Dwarf Factory','','','Artisan & independent','Artisan keycaps','Artisan keycap maker.','Rainbow Llama','https://mechanicalkeyboards.com/collections/Artisan-Keycaps?page=1'),
 ('Varmilo','','','Specialist','Keyboards, artisan caps','Keyboard brand that also sells artisan keycaps.','Siamese Kitty Paw','https://mechanicalkeyboards.com/collections/Artisan-Keycaps?page=1')]
have={x['n'].lower() for x in br['b']}
for n,c,f,seg,kf,dd,sig,s in B:
    if n.lower() in have: continue
    e={'n':n,'seg':seg,'kf':kf,'d':dd,'sig':[sig],'s':s}
    if c:e['c']=c
    if f:e['f']=f
    br['b'].append(e)
# moves: THEC64 note, none added
json.dump(d,open(P+'D1.json.tmp','w'),indent=1,ensure_ascii=False); os.replace(P+'D1.json.tmp',P+'D1.json')
json.dump(br,open(P+'D1_brands.json.tmp','w'),indent=1,ensure_ascii=False); os.replace(P+'D1_brands.json.tmp',P+'D1_brands.json')
k=sum(len(k) for dp in d['depts'] for s in dp['s'] for k in [s['k']]); a=sum(len(k.get('x',[])) for dp in d['depts'] for s in dp['s'] for k in s['k'])
print(k,a,len(br['b']))
