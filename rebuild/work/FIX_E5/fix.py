import json,copy,shutil,os
P='out/E5.json'
d=json.load(open('work/FIX_E5/bak/E5.json'))
bd=json.load(open('work/FIX_E5/bak/E5_brands.json'))
def find(n):
    for dp in d['depts']:
        for s in dp['s']:
            for k in s['k']:
                if k['n']==n: return k,s,dp
    raise KeyError(n)
def A(n,mk,y,dsc,s,v=None,dt='',a=''):
    return {"n":n,"a":a,"d":dsc,"mk":mk,"y":y,"s":s,"v":v or [],"dt":dt}
def V(n,mk,y='',dsc=''): return {"n":n,"mk":mk,"y":y,"d":dsc}
W='https://en.wikipedia.org/wiki/'
def promote(kind,after,arch,rm):
    k=find(kind)[0]
    k['m']=[m for m in k['m'] if m[0] not in rm]
    names=[a['n'] for a in k['x']]
    k['x'].insert(names.index(after)+1 if after else len(names),arch)
    return k
# ---- E5-1 handhelds
promote('Handheld console','Sega Nomad',A('Virtual Boy','Nintendo','1995',"Nintendo's 32-bit console, re-engineered from a headset into a stand-mounted viewer with an M-shaped controller.",W+'Virtual_Boy',[V('Virtual Boy','Nintendo','1995','slide-on battery or AC adapter attachment; link cable and harness never sold')],'' ,'VUE-001'),[])
promote('Handheld console','Neo Geo Pocket',A('Game.com','Tiger Electronics','1997',"Tiger's touchscreen handheld with a link-up internet modem option.",W+'Game.com',[V('Game.com','Tiger Electronics','1997','US September 1997'),V('Game.com Pocket Pro','Tiger Electronics','1999','smaller revision')],'','Game.com'),['Game.com'])
k=promote('Handheld console','Game Boy Advance',A('N-Gage','Nokia','2003',"Nokia's combined mobile phone and handheld game system.",W+'N-Gage',[V('N-Gage','Nokia','2003','7 October 2003; MP3, FM radio and USB'),V('N-Gage QD','Nokia','2004','smaller redesign; cartridge slot at the bottom; no MP3, radio or USB')],'','N-Gage · QD'),['N-Gage','N-Gage QD'])
promote('Handheld console','N-Gage',A('Pokémon mini','Nintendo','2001',"Nintendo's tiny cartridge handheld made with The Pokémon Company.",W+'Pok%C3%A9mon_Mini',[V('Wooper Blue','Nintendo','2001','North America 16 November 2001'),V('Chikorita Green','Nintendo','2001',''),V('Smoochum Purple','Nintendo','2001','')],'colour','Pokemon mini'),['Pokemon mini'])
promote('Handheld console','PlayStation Portable',A('Gizmondo','Tiger Telematics','2005',"Tiger Telematics' Windows CE handheld with camera, GPS and phone connectivity.",W+'Gizmondo',[V('Gizmondo','Tiger Telematics','2005','launched in Britain 19 March 2005'),V('Gizmondo Smart Adds','Tiger Telematics','2005','advertising-subsidised version')],'',''),['Gizmondo'])
# ---- home consoles
promote('Home console','Atari 7800',A('Atari XEGS','Atari','1987',"Atari's console redesign of the 65XE computer; plays as a console or, with keyboard, a computer.",W+'Atari_XEGS',[V('XEGS basic set','Atari','1987','console and CX40 joystick'),V('XEGS deluxe set','Atari','1987','adds keyboard and XG-1 light gun')],'','XE Video Game System'),['Atari XEGS'])
promote('Home console','Neo Geo AES',A('Amstrad GX4000','Amstrad','1990',"Amstrad's only console, a CPC Plus-based system sold only in Europe.",W+'GX4000',[V('GX4000','Amstrad','1990','September 1990; Britain, France, Spain, Italy')],'','GX4000'),['GX4000'])
promote('Home console','CD-i',A('Pioneer LaserActive','Pioneer','1993',"Pioneer's modular LaserDisc player that plays console games through swappable PAC modules.",W+'LaserActive',[V('LaserActive CLD-A100','Pioneer','1993','Japan August 1993, North America September 1993'),V('NEC LD-ROM² System PCE-LD1','NEC','1993','NEC-branded, takes the same PACs')],'PAC modules: Mega-LD (PAC-S1/S10) · LD-ROM² (PAC-N1/N10) · PC Engine (PCE-LP1) · Karaoke (PAC-K1) · Computer Interface (PAC-PC1)','LaserActive'),['Pioneer LaserActive'])
k=find('Home console')[0]
promote('Home console','Sega Pico',A('PC-FX','NEC','1994',"NEC and Hudson Soft's tower-shaped 32-bit CD console, successor to the PC Engine, sold only in Japan.",W+'PC-FX',[V('PC-FX','NEC','1994','December 1994'),V('PC-FXGA','NEC','','game accelerator card for PC-9800 and DOS/V computers')],'','Japan only'),['PC-FX'])
promote('Home console','PC-FX',A('Casio Loopy','Casio','1995',"Casio's 32-bit console aimed at girls and women, with a built-in thermal sticker printer.",W+'Casio_Loopy',[V('Loopy My Seal Computer SV-100','Casio','1995','October 1995, Japan only')],'optional Magical Shop video capture','Loopy'),['Casio Loopy'])
promote('Home console','Casio Loopy',A('Apple Pippin','Apple','1996',"Apple's multimedia platform licensed to Bandai, built on the Macintosh architecture.",W+'Apple_Pippin',[V('Pippin Atmark','Bandai','1996','white, Japan, March 1996'),V('Pippin @WORLD','Bandai','1996','black, United States, June 1996'),V('Katz Media Player 2000','Katz Media','1997','KMP 2000, Europe and Canada')],'','Pippin · @World'),['Pippin'])
# ---- E5-3 pinball
k=find('Solid-state pinball machine')[0]
old={a['n']:a for a in k['x']}
def ver(n,var):
    v=copy.deepcopy(old[n]['v']); 
    if var not in v[0]['d']: v[0]['d']=(var+'; '+v[0]['d']).strip('; ')
    return v
WP=W+'Williams_Pinball_Controller'
vers=[V('FunHouse','Williams','1990','first production WPC game; alphanumeric'),
 *ver('The Addams Family','Fliptronics'),
 *ver('Twilight Zone','Fliptronics'),
 *ver('Indiana Jones: The Pinball Adventure','DCS'),
 V('Star Trek: The Next Generation','Williams','1993','DCS'),
 *ver('Attack from Mars','WPC-95'),
 V('Scared Stiff','Bally','1996','WPC-95'),
 *ver('Medieval Madness','WPC-95'),
 V('Cirqus Voltaire','Bally','1997','WPC-95'),
 *ver('Monster Bash','WPC-95')]
wpc=A('Williams WPC','Williams','1990',"Williams Pinball Controller, the board platform behind Williams and Midway machines from 1990 to 1999, successor to System 11.",WP,vers,'alphanumeric · dot matrix · Fliptronics · DCS · WPC-S (security) · WPC-95',"WPC")
g80=A('Gottlieb System 80','Gottlieb','1980',"Gottlieb's solid-state board family: System 80, 80A and 80B.",W+'Gottlieb',[V('Black Hole','Gottlieb','1981','System 80'),V('Haunted House','Gottlieb','1982','System 80')],'System 80 (1980–82) · 80A (1982–85) · 80B (1985–89)','System 80')
g1=A('Gottlieb System 1','Gottlieb','1977',"Gottlieb's first solid-state board, used 1977 to 1980.",W+'Gottlieb',[V('Cleopatra','Gottlieb','1977',''),V('Sinbad','Gottlieb','1978',''),V('Buck Rogers','Gottlieb','1980','')],'','System 1')
k['x']=[wpc,g80,g1]
k['m']=[m for m in k['m'] if m[0] not in ('FunHouse','Star Trek: The Next Generation','Cirqus Voltaire','Scared Stiff','Black Hole','Haunted House')]
# ---- E5-2 retro accessories
k=find('Console memory card')[0]
k['x']=[A('Dreamcast VMU','Sega','1998',"Sega's Visual Memory Unit, the Dreamcast memory card with its own small screen.",W+'VMU',[V('Visual Memory Unit','Sega','1998',''),V('VMU Godzilla edition','Sega','1998','Japan, 30 July 1998'),V('4x Memory Card','Sega','','larger capacity')],'','VMU · Visual Memory System'),
        A('Nintendo 64 Controller Pak','Nintendo','1996','Nintendo\'s 256-kilobit (32 KB) save pack that plugs into the N64 controller.',W+'Nintendo_64_accessories',[V('Controller Pak','Nintendo','1996','256 kilobits')],'','Controller Pak')]
k['m']=[m for m in k['m'] if m[0] not in ('Dreamcast VMU','Nintendo 64 Controller Pak','Nintendo 64 Expansion Pak')]
k=find('Rumble pack')[0]
k['x']=[A('Nintendo 64 Rumble Pak','Nintendo','1997','Nintendo\'s vibration add-on that plugs into the N64 controller.',W+'Rumble_Pak',[V('Rumble Pak','Nintendo','1997','')],'','Rumble Pak')]
k['m']=[m for m in k['m'] if m[0]!='Nintendo 64 Rumble Pak']
# ---- E5-4 accessories merge
def merge(names,newname,alias,dsc,types,shelf):
    ks=[find(n)[0] for n in names]; sh=find(names[0])[1]
    nk={"n":newname,"a":alias,"d":dsc,"t":types,"s":ks[0]['s'],"m":[m for x in ks for m in x['m']]}
    for x in ks:
        if x.get('x'): nk.setdefault('x',[]).extend(x['x'])
    pos=sh['k'].index(ks[0])
    for x in ks[1:]:
        for s in [find(x['n'])[1]]: s['k'].remove(x)
    sh['k'][pos]=nk
    return nk
merge(['Case or pouch','Screen protector','Faceplate, skin or decal'],'Case, screen protector or skin','carry case · tempered glass · decal','Case, pouch, screen cover or skin made to protect or restyle one game machine or controller.',['carry case','soft pouch','tempered glass','film','faceplate','skin','decal'],None)
merge(['Replacement battery pack','AC adapter','Charging stand','TV dock'],'Power, charging & dock','battery pack · power supply · charging dock','Battery, power adapter, charging stand or TV dock made for one game machine or controller.',['replacement battery pack','AC adapter','charging stand','TV dock'],None)
merge(['Console stand or mount','Console cooling unit'],'Console stand, mount or cooler','vertical stand · cooling fan','Stand, mount or external cooler made to hold or cool one game machine.',['vertical stand','horizontal stand','wall mount','cooling stand','clip-on fan'],None)
cc=merge(['Console cable or adapter','Controller converter','Console network adapter'],'Console cable or adapter','proprietary cable · AV cable · link cable · controller converter · modem adapter','Cable, converter or network adapter with a connector made for one console or controller.',['RF','composite','S-Video','RGB SCART','component','VGA','HDMI','link cable','controller converter','modem or network adapter'],None)
merge(['Console keyboard','Console media add-on'],'Console keyboard or media add-on','chatpad · media remote · TV tuner','Keyboard, remote control or TV tuner made to add typing or media functions to one console.',['full keyboard','controller clip-on chatpad','media remote','TV tuner'],None)
# ---- E5-5 game media
sh=find('Game-key card')[1]
gk,dc=find('Game-key card')[0],find('Download-code card')[0]
nk={"n":"Game-key or download-code card","a":"download-code voucher · game-key card","d":"Physical card or box that holds only a key or code to download a game, not the game itself.","t":["game-key card","download-code card"],"s":gk['s'],"m":gk['m']+dc['m']}
i=sh['k'].index(gk); sh['k'][i]=nk; sh['k'].remove(dc)
dp=find('Digital game')[2]
sh2=find('Digital game')[1]
dp['s'].remove(sh2)
dp['note']='Digital-only games, DLC and mods are not objects here; see the Interactive Entertainment taxonomy.'
# ---- E5-6 phone controller type
g=find('Gamepad')[0]
if 'phone clip-on or clamp' not in g['t']: g['t'].append('phone clip-on or clamp')
# ---- E5-8 XREAL
def fix(o):
    if isinstance(o,dict):
        for kk,v in o.items():
            if kk=='mk' and v=='Xreal': o[kk]='XREAL'
            else: fix(v)
    elif isinstance(o,list):
        for v in o: fix(v)
fix(d)
for b in bd['b']:
    if b['n']=='Xreal': b['n']='XREAL'
# brands
have={b['n'] for b in bd['b']}
def B(n,c,f,seg,kf,dsc,s):
    if n not in have: bd['b'].append({"n":n,"c":c,"f":f,"seg":seg,"kf":kf,"d":dsc,"s":s,"lines":[],"eras":[],"sc":[],"rel":[]})
B('Amstrad','United Kingdom','','Value','affordable computers','British electronics firm that made the GX4000 console.',W+'GX4000')
B('Casio','Japan','','Mainstream','electronics','Japanese electronics firm that made the Loopy console.',W+'Casio_Loopy')
B('Nokia','Finland','','Mainstream','mobile phones','Finnish phone maker that made the N-Gage.',W+'N-Gage')
B('Pioneer','Japan','','Mainstream','receivers','Japanese electronics firm that made the LaserActive.',W+'LaserActive')
B('Tiger Telematics','','','Specialist','Gizmondo','Maker of the Gizmondo handheld, liquidated in 2006.',W+'Gizmondo')
bd['b'].sort(key=lambda b:b['n'].lower()) if False else None
json.dump(d,open('work/FIX_E5/E5.tmp','w'),indent=1,ensure_ascii=False)
json.dump(bd,open('work/FIX_E5/E5_brands.tmp','w'),indent=1,ensure_ascii=False)
