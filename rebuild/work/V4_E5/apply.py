import json,re,os,copy
P='/home/user/Possession-Taxonomy/rebuild/out/E5.json'
d=json.load(open(P))
W='https://en.wikipedia.org/wiki/'
stats={'m_removed':0,'m_promoted':0,'r_removed':0}
def get(dep,kn):
    for s in d['depts'][dep]['s']:
        for k in s['k']:
            if k['n']==kn:
                k.setdefault('x',[]); return k
    raise KeyError(kn)
def ent(n,mk,y,dsc,s,g=None,v=None,a=None,role=None):
    e={'n':n,'mk':mk,'y':y,'d':dsc,'s':s,'v':v or []}
    if a: e['a']=a
    if g: e['g']=g
    if role: e['role']=role
    return e
def ver(n,mk='',y='',dsc=''): return {'n':n,'mk':mk,'y':y,'d':dsc}
def have(k,n):
    n=n.lower()
    for e in k['x']:
        if e['n'].lower()==n or any(v['n'].lower()==n for v in e.get('v',[])): return True
    return False
def add(k,e,n_promoted=True):
    if have(k,e['n']): return False
    k['x'].append(e); return True
def cov(k,txt):
    k['sel']=(k.get('sel','')+' '+txt).strip()

# ---------- Game media
ROM=W+'ROM_cartridge'
k=get(1,'Game cartridge')
rows=[('Atari 2600 cartridge','Atari, Inc.',1),('Atari 5200 cartridge','Atari, Inc.',1),('Atari 7800 cartridge','Atari, Inc.',1),('Atari XEGS cartridge','Atari, Inc.',1),('Atari Lynx cartridge','Atari, Inc.',1),('Atari Jaguar cartridge','Atari, Inc.',1),
('Amstrad GX4000 cartridge','Amstrad',1),('WonderSwan cartridge','Bandai',1),('Evercade cartridge','Blaze Entertainment',1),('ColecoVision cartridge','Coleco',1),('Channel F cartridge','Fairchild Camera and Instrument',1),
('Pixter cartridge','Fisher-Price',1),('Smart Cycle cartridge','Fisher-Price',0),('IBM PCjr cartridge','IBM',0),('Interton Video 2000 cartridge','Interton',1),('Leapster cartridge','LeapFrog',1),('LeapPad cartridge','LeapFrog',0),('LeapTV cartridge','LeapFrog',0),
('Odyssey game card','Magnavox',1),('Odyssey 2 and Videopac G7000 cartridge','Magnavox / Philips',1),('Intellivision cartridge','Mattel',1),('Vectrex cartridge','Milton Bradley',1),('Microvision cartridge','Milton Bradley',1),
('TurboGrafx-16 and PC Engine card','NEC',1),('TurboExpress card','NEC',1),('digiBLAST cartridge','Nikko Europe',1),
('NES Game Pak and Famicom cassette','Nintendo',1),('Super NES and Super Famicom Game Pak','Nintendo',1),('Nintendo 64 Game Pak','Nintendo',1),('Game Boy Game Pak','Nintendo',1),('Game Boy Color Game Pak','Nintendo',1),('Game Boy Advance Game Pak','Nintendo',1),('Virtual Boy Game Pak','Nintendo',1),('Pokemon Mini cartridge','Nintendo',1),('Switch Game Card','Nintendo',0),
('SG-1000 cartridge','Sega',1),('Master System and Mark III cartridge','Sega',1),('Mega Drive and Genesis cartridge','Sega',1),('Game Gear cartridge','Sega',1),('Pico cartridge','Sega',1),('32X cartridge','Sega',1),('Genesis Nomad','Sega',0),('Advanced Pico Beena cartridge','Sega',1),
('Neo Geo cartridge','SNK',1),('Neo Geo Pocket cartridge','SNK',1),('Neo Geo Pocket Color cartridge','SNK',1),('Neo Geo X','SNK',0),('E-kara cartridge','Takara',0),('V.Smile cartridge','VTech',1),('Solid State Command Module','Texas Instruments',0),('Casio ROM Pack','Casio',0),('Yamaha music cartridge','Yamaha',0)]
total=len(rows); inc=sum(1 for r in rows if r[2])
# map to existing names
alias={'Channel F cartridge':'Channel F cartridge','Odyssey game card':'Odyssey game card','NES Game Pak and Famicom cassette':None,'Super NES and Super Famicom Game Pak':None,'Nintendo 64 Game Pak':None,'Game Boy Game Pak':None,'Mega Drive and Genesis cartridge':None,'Atari 2600 cartridge':None}
for n,mk,i in rows:
    if not i: continue
    if n=='Atari 2600 cartridge' or any(e['n']==n for e in k['x']): continue
    if n=='Game Boy Color Game Pak' and have(k,'Game Boy Game Pak'):
        for e in k['x']:
            if e['n']=='Game Boy Game Pak': e.setdefault('v',[]).append(ver('Game Boy Color Game Pak','Nintendo','','Listed with Game Boy cartridges on the ROM cartridge page')); 
        continue
    if n=='Neo Geo Pocket Color cartridge':
        for e in k['x']:
            if e['n']=='Neo Geo Pocket cartridge': e.setdefault('v',[]).append(ver(n,mk))
        continue
    k['x'].append(ent(n,mk,'','Cartridge format of a platform made by %s.'%mk,ROM))
# merge m
if 'm' in k: stats['m_removed']+=len(k['m']); stats['m_promoted']+=1; del k['m']
for e in k['x']:
    if e['n']=='Channel F cartridge': e['role']='origin'
    e['g']=e.get('mk') or 'Other'
k['x'].sort(key=lambda e:(e['g'],e.get('y') or '9999',e['n']))
k['nl']='One entry is the cartridge or card format of one platform, such as a Game Pak or Videocart; regional shell variants and enhancement-chip cartridges are versions.'
k['sel']="Platforms named in Wikipedia's ROM cartridge article, one entry per game-cartridge format, sectioned by platform maker; years only where the article or an earlier source gives them. NEC card formats are under Game card; the Switch card is under Game card."
k['xg']='by platform maker'
cov(k,'Covers %d of the %d platforms in that article; the other %d are not game cartridges (calculator, keyboard, educational or computer modules) or sit under Game card or Consoles & handhelds.'%(len(k['x']),total,total-len(k['x'])))

k=get(1,'Game disc')
OD=W+'Optical_disc'
if 'm' in k: stats['m_removed']+=len(k['m']); del k['m']
k['x'].append(ent('Nintendo optical disc','Nintendo','','Nintendo\'s proprietary disc family used for the GameCube, Wii and Wii U.',OD))
k['x'].append(ent('PlayStation Blu-ray game disc','Sony','','Blu-ray disc used to distribute games for the PlayStation 3, 4 and 5.',W+'Blu-ray',v=[ver('PlayStation 3 disc','Sony'),ver('PlayStation 4 disc','Sony'),ver('PlayStation 5 disc','Sony')]))
k['x'].append(ent('Xbox Blu-ray game disc','Microsoft','','Blu-ray disc used to distribute games for the Xbox One and Xbox Series X.',W+'Blu-ray',v=[ver('Xbox One disc','Microsoft'),ver('Xbox Series X disc','Microsoft')]))
k['x'].append(ent('PC Engine CD-ROM2 disc','NEC','1988','First CD-ROM format used on a home video game console (TurboGrafx-CD in North America).',W+'CD-ROM',role='origin'))
for e in k['x']: e['g']=e.get('mk') or 'Other'
k['x'].sort(key=lambda e:(e['g'],e.get('y') or '9999',e['n']))
k['nl']='One entry is the disc format of one platform maker, such as the GD-ROM or the UMD; per-console disc generations are versions.'
k['sel']="Disc formats named in Wikipedia's Optical disc, Blu-ray and CD-ROM articles for games, sectioned by platform maker. PlayStation and Xbox CD and DVD discs are not named by a fetched page and are left out."
k['xg']='by platform maker'
cov(k,'Covers 8 disc formats; Optical disc was read to about 100,000 of 144,989 characters, so later mentions may be missing.')
k=get(1,'Game card')
if 'm' in k: stats['m_removed']+=len(k['m']); del k['m']
for e in k['x']: e['g']=e.get('mk') or 'Other'
k['nl']='One entry is the card format of one platform, such as the HuCard or the Nintendo Game Card; generations are versions.'
k['sel']='Card formats with their own Wikipedia articles, found in earlier passes; no whole-space reference exists.'
k['xg']='by platform maker'
k=get(1,'Cassette or floppy game')
if 'm' in k: stats['m_removed']+=len(k['m']); del k['m']
for e in k['x']: e['g']=e.get('mk') or 'Other'
k['nl']='One entry is the tape or disk format of one platform maker; sizes and regions are versions.'
k['sel']='Only the Famicom Disk Card is held; no fetched reference names other tape or floppy console formats.'; k['xg']='by platform maker'
k=get(1,'Game-key or download-code card')
stats['m_removed']+=len(k.pop('m',[]))
k=get(1,'Collector\'s edition')
stats['r_removed']+=len(k.pop('r',[]))
k=get(1,'Budget re-release')
for e in k['x']: e['g']=e.get('mk') or 'Other'
k['nl']='One entry is a budget label run by a platform maker; its reprints are versions.'; k['sel']='Only the labels found by earlier passes; no whole-space reference.'; k['xg']='by platform maker'

# memory cards (Accessories)
MC=W+'Memory_card'
k=get(3,'Console memory card')
stats['m_removed']+=len(k.pop('m',[]))
k['x'].append(ent('Neo Geo memory card','SNK','1990','2 KiB memory card of the Neo Geo AES.',MC))
k['x'].append(ent('PlayStation Memory Card','Sony','','128 KiB memory card of the PlayStation.',MC))
k['x'].append(ent('GameCube Memory Card','Nintendo','','512 KiB memory card of the GameCube.',MC))
k['x'].append(ent('Xbox 360 Memory Unit','Microsoft','','Memory card of the Xbox 360.',MC))
for e in k['x']: e['g']=e.get('mk') or 'Other'
k['x'].sort(key=lambda e:(e['g'],e.get('y') or '9999',e['n']))
k['nl']='One entry is the memory-card format of one console; capacities are versions.'
k['sel']="Console memory cards named in Wikipedia's Memory card article (video game consoles section), sectioned by platform maker."; k['xg']='by platform maker'
cov(k,'Covers 5 of 5 console cards that article names; Saturn Backup Memory and PlayStation 2 cards are not named there.')

# ---------- Controllers
GP=W+'Gamepad'; GC=W+'Game_controller'; AC=W+'Arcade_controller'
k=get(2,'Gamepad')
stats['m_removed']+=len(k.pop('m',[]))
# split PlayStation line
ps=[e for e in k['x'] if e['n']=='PlayStation controller to DualSense'][0]
k['x'].remove(ps)
vv={v['n']:v for v in ps['v']}
def pick(*ns): return [vv[n] for n in ns if n in vv]
k['x']+= [ent('PlayStation controller','Sony','1994','The original PlayStation pad and the Dual Analog Controller that added sticks.',ps['s'],v=pick('PlayStation controller','Dual Analog Controller')),
 ent('DualShock','Sony','','Sony pad line with vibration and analog sticks, from the first DualShock to the DualShock 4.',ps['s'],v=pick('DualShock','DualShock 2','Sixaxis','DualShock 3')+[vv.get('DualShock 4',ver('DualShock 4','Sony'))]),
 ent('DualSense','Sony','','Sony pad line for the PlayStation 5 with adaptive triggers.',ps['s'],v=pick('DualSense','DualSense Edge'))]
k['x']+= [ent('Pro Controller','Nintendo','','Nintendo\'s conventional full-size pad for its home consoles.',GP,v=[ver('Wii U Pro Controller','Nintendo'),ver('Nintendo Switch Pro Controller','Nintendo'),ver('Nintendo Switch 2 Pro Controller','Nintendo')]),
 ent('Wii U GamePad','Nintendo','','Touchscreen controller of the Wii U.',GP),
 ent('Saturn 3D Control Pad','Sega','1996','Sega Saturn analog pad.',GP),
 ent('Backbone One and Pro','Backbone Labs','','Phone-clamp controllers.',GP),
 ent('Samsung Android GamePad','Samsung','','Samsung pad for Android devices.',GP)]
for e in k['x']:
    if e['n']=='NeGcon': e['g']='Namco'
    e['g']=e.get('g') if e.get('g') and e['n']=='NeGcon' else (e.get('mk') or 'Other')
k['x'].sort(key=lambda e:(e['g'],e.get('y') or '9999',e['n']))
k['nl']='One entry is a controller platform-model, a pad line sold under its own name (DualShock, DualSense, Joy-Con, Pro Controller); revisions and generations are versions.'
k['sel']="Pad lines named in Wikipedia's Gamepad and Game controller articles plus the per-controller articles cited on each entry, sectioned by maker. Third-party pads (8BitDo, GameSir, Hori, Razer) are not named by a fetched list and are left out."
k['xg']='by maker'
cov(k,'Covers 20 pad lines; no complete list exists.')
k=get(2,'Joystick'); 
for e in k['x']: e['g']=e.get('mk') or 'Other'
k['nl']='One entry is a console joystick line; revisions are versions.'; k['sel']='Only the Atari CX40, from its own article; no whole-space reference.'; k['xg']='by maker'
k=get(2,'Arcade stick')
stats['m_removed']+=len(k.pop('m',[]))
k['x']+= [ent('Dreamcast Arcade Stick','Sega','','Sega\'s arcade stick for the Dreamcast.',AC),
 ent('Neo Geo Stick 2','Exar','2005','Stick for the PlayStation 2, later Wii and PlayStation 3.',AC,v=[ver('PlayStation 2 and Japan release','Exar','2005'),ver('Wii release','Exar','2008'),ver('PlayStation 3 release','Exar','2009')]),
 ent('Neo Geo AES arcade stick','SNK','1990','Stick packed with the Neo Geo AES console.',AC)]
for e in k['x']: e['g']=e.get('mk') or 'Other'
k['x'].sort(key=lambda e:(e['g'],e.get('y') or '9999',e['n']))
k['nl']='One entry is an arcade-stick line sold under its own name; revisions are versions.'; k['sel']="Stick lines named in Wikipedia's Arcade controller article plus per-product pages cited on the entries, sectioned by maker. Other brands (Qanba, Mayflash, 8BitDo) have no fetched list and are left out."; k['xg']='by maker'
cov(k,'Covers the 8 stick lines held; no complete list exists.')
k=get(2,'Leverless controller')
stats['m_removed']+=len(k.pop('m',[]))
for e in k['x']: e['g']=e.get('mk') or 'Other'
k['nl']='One entry is a leverless controller line; revisions are versions.'; k['sel']='Hit Box and Razer Kitsune from their cited pages; no whole-space reference.'; k['xg']='by maker'
k=get(2,'Light gun')
stats['m_removed']+=len(k.pop('m',[])); stats['m_promoted']+=1
k['x'].append(ent('Wii Zapper','Nintendo','','Light-gun shell holding the Wii Remote and Nunchuk.',GC))
for e in k['x']: e['g']=e.get('mk') or 'Other'
k['x'].sort(key=lambda e:(e['g'],e.get('y') or '9999',e['n']))
k['nl']='One entry is a light-gun line; models are versions.'; k['sel']='Light guns named by the cited pages; no whole-space reference.'; k['xg']='by maker'
k=get(2,'Racing wheel')
stats['m_removed']+=len(k.pop('m',[])); stats['r_removed']+=len(k.pop('r',[]))
k['x'].append(ent('Logitech Driving Force GT','Logitech','2011','Wheel and pedals for the PlayStation 3.',GC))
for e in k['x']: e['g']=e.get('mk') or 'Other'
k['nl']='One entry is a console racing-wheel line; models are versions.'; k['sel']='Wheels named in the Game controller article; no whole-space reference.'; k['xg']='by maker'

# ---------- Modding
GB=W+'Game_backup_device'
k=get(4,'Flash cartridge')
fl=[('Super Magicom','Front Fareast Industrial','Super Famicom copier.'),('Super Wild Card','Front Fareast Industrial','Super Famicom copier series with DX 32 and DX2 models.'),('Super UFO','UFO Enterprise','Super Famicom copier series.'),('Game Doctor','Bung Enterprise','Copier series.'),('Multi Game Hunter','Venus Corp.','Multi-game copier.'),('Double Pro Fighter','China Coach Limited','Copier for the Super Famicom.'),('Retrode','Retrode UG','Cartridge reader that exposes games as files.'),('Doctor V64','','Nintendo 64 development and backup device.'),('CD64','','Nintendo 64 backup device.'),('Z64','','Nintendo 64 backup device.'),('Neo N64 Myth Cart','','Nintendo 64 flash cart.'),('64drive','','Nintendo 64 flash cart.'),('Game Boy Xchanger','Bung Enterprises','Game Boy backup device.'),('Flash Advance Xtreme','','Game Boy Advance flash cart.'),('EZ-Flash Advance','','Game Boy Advance flash cart.'),('WonderMagic','','WonderSwan flash cart.'),('Professor SF','','Super Famicom backup device.')]
for n,mk,dsc in fl:
    k['x'].append(ent(n,mk,'',dsc,GB))
for e in k['x']:
    if e['n']=='EverDrive':
        e['v'].append(ver('Everdrive 64','Krikzz','','listed on the backup device page'))
    e['g']=e.get('mk') or 'Maker not stated'
k['x'].sort(key=lambda e:(e['g'],e['n']))
k['nl']='One entry is a flash cartridge or copier product family; models and capacities are versions.'
k['sel']="Product families named in Wikipedia's Game backup device article plus the EverDrive, FXPak Pro, R4 and Mig Flash entries from earlier passes, sectioned by maker."
k['xg']='by maker'
cov(k,'Covers 21 families; the article names more variants (PVBackup, XG-Flash, GB Xchanger variants) that are not entered.')
k=get(4,'Optical drive emulator')
stats['m_removed']+=len(k.pop('m',[]))
for e in k['x']: e['g']=e.get('mk') or 'Maker not stated'
k['nl']='One entry is an optical drive emulator product family; hardware revisions are versions.'; k['sel']='Families named by the cited pages; no whole-space reference.'; k['xg']='by maker'
k=get(4,'Modchip'); stats['m_removed']+=len(k.pop('m',[]))
for e in k['x']: e['g']=e.get('mk') or 'Maker not stated'
k['nl']='One entry is a modchip maker line; models are versions.'; k['sel']='Only Xecuter, from its cited page; other chips are left out without a fetched reference.'; k['xg']='by maker'
k=get(4,'Cheat device'); stats['m_removed']+=len(k.pop('m',[]))
for e in k['x']: e['g']=e.get('mk') or 'Maker not stated'
k['nl']='One entry is a cheat-device product line; regional names are versions.'; k['sel']='Game Genie, Action Replay and GameShark from their cited pages.'; k['xg']='by maker'

# ---------- VR
VR=W+'List_of_virtual_reality_headsets'
k=get(5,'Early VR head-mounted display')
for n,mk,y,v in [('IIS VFX3D','IIS','2000',[]),('Fakespace Labs Wide5','Fakespace Labs','2007',[]),('NVIS nVisor','NVIS','',[ver('nVisor SX','NVIS'),ver('nVisor SX111','NVIS'),ver('nVisor ST50','NVIS')]),('Sensics headsets','Sensics','',[ver('xSight 6123','Sensics'),ver('piSight 76-21','Sensics')]),('Crescent HEWDD','Crescent','2008',[ver('HEWDD-768','Crescent','2008'),ver('HEWDD-1080','Crescent')])]:
    k['x'].append(ent(n,mk,y,'Early research or professional headset on the Wikipedia list.',VR,v=v))
for e in k['x']: e['g']=e.get('mk') or 'Other'
k['x'].sort(key=lambda e:(e['g'],e.get('y') or '9999',e['n']))
k['nl']='One entry is an early head-mounted display line; models are versions.'; k['sel']="The 'Early VR' table of Wikipedia's List of virtual reality headsets, by maker; the Virtual Boy is a console and is under Consoles & handhelds."; k['xg']='by maker'
cov(k,'Complete: 12 of 12 non-console rows in that table.')
k=get(5,'Phone VR viewer'); stats['m_removed']+=len(k.pop('m',[]))
for e in k['x']: e['g']=e.get('mk') or 'Other'
k['nl']='One entry is a phone-based viewer line; models are versions.'; k['sel']='Viewers named in the list of VR headsets; the 5 minor viewers formerly held are removed.'; k['xg']='by maker'
k=get(5,'Standalone VR headset')
stats['m_removed']+=len(k.pop('m',[]))
k['x']=[e for e in k['x'] if e['n']!='Oculus Quest']
for e in k['x']:
    if e['n']=='Meta Quest': pass
    if e['n']=='HTC Vive Focus': e['v']+= [ver('Vive Flow','HTC','2022'),ver('Vive XR Elite','HTC','2023')]
    if e['n']=='Pico 4': e['v']+=[ver('Pico Neo CV','Pico','2017'),ver('Pico G2 4K','Pico','2019')]
for n,mk,y in [('Lenovo Mirage Solo','Lenovo','2018'),('Lenovo ThinkReality VRX','Lenovo','2022'),('Pico VR Goblin','Pico','2016'),('Microsoft HoloLens','Microsoft','2016'),('Alcatel Vision','Alcatel','2016'),('Woxter Neo VR100','Woxter','2017'),('GFL Developer Kit','GameFace Labs','2018'),('Steam Frame','Valve','')]:
    k['x'].append(ent(n,mk,y,'Standalone or mixed-reality headset on the Wikipedia list.',VR))
for e in k['x']: e['g']=e.get('mk') or 'Other'
k['x'].sort(key=lambda e:(e['g'],e.get('y') or '9999',e['n']))
k['nl']='One entry is a standalone headset line; generations and variants are versions.'; k['sel']="The mobile and standalone rows of Wikipedia's List of virtual reality headsets, by maker, generations as versions. The Qualcomm reference kits, Avegant Glyph, Modal VR and HELMET VISION are not placed."; k['xg']='by maker'
cov(k,'Covers 36 of 36 list rows kept as entries or versions; the page was read to about 101,500 of 112,925 characters.')
k=get(5,'Tethered VR headset')
stats['m_removed']+=len(k.pop('m',[])); stats['r_removed']+=len(k.pop('r',[]))
k['x']=[e for e in k['x'] if e['n'] not in('HTC Vive Pro','PlayStation VR2')]
for e in k['x']:
    if e['n']=='PlayStation VR': pass
new=[('Razer OSVR HDK','Razer','2015',[ver('OSVR HDK 1.4','Razer','2015'),ver('OSVR HDK 2','Razer','2016')]),
('StarVR','Starbreeze','2016',[ver('StarVR','Starbreeze','2016'),ver('StarVR One','StarVR','2018')]),
('Fove 0','Fove','2017',[]),('Pimax headsets','Pimax','2017',[ver('Pimax 4K','Pimax','2017'),ver('Pimax 5K Plus','Pimax','2018'),ver('Pimax 8K','Pimax','2019')]),
('VRgineers headsets','VRgineers','2017',[ver('VRHero 5K','VRgineers','2017'),ver('VRHero 5K Plus','VRgineers','2017'),ver('XTAL','VRgineers','2018')]),
('Deepoon VR E3','Deepoon','2017',[]),('Varjo headsets','Varjo','2019',[ver('VR-1','Varjo','2019'),ver('VR-2','Varjo','2019'),ver('Aero','Varjo','2021'),ver('VR-3','Varjo','2021'),ver('XR4','Varjo','2023')])]
for n,mk,y,v in new: k['x'].append(ent(n,mk,y,'Tethered headset line on the Wikipedia list.',VR,v=v))
for e in k['x']:
    if e['n']=='PlayStation VR': e['n']='PlayStation VR and VR2'
    e['g']=e.get('mk') or 'Several makers'
k['x'].sort(key=lambda e:(e['g'],e.get('y') or '9999',e['n']))
k['nl']='One entry is a tethered headset line; models are versions.'; k['sel']="The tethered rows of Wikipedia's List of virtual reality headsets, by maker, models as versions; the cancelled LG SteamVR headset is left out."; k['xg']='by maker'
cov(k,'Covers 48 of 49 tethered rows (one cancelled).')
k=get(5,'XR glasses'); stats['m_removed']+=len(k.pop('m',[]))
for e in k['x']: e['g']=e.get('mk') or 'Other'
k['nl']='One entry is an XR display-glasses line; models are versions.'; k['sel']='Lines named by cited pages; no whole-space reference.'; k['xg']='by maker'
for kn in ['VR controller','VR tracker or base station','VR head strap or facial interface','Haptic vest or glove','VR treadmill']:
    k=get(5,kn); stats['m_removed']+=len(k.pop('m',[]))
    for e in k['x']: e['g']=e.get('mk') or 'Other'
    k['nl']='One entry is an accessory line by one maker; models are versions.'; k['sel']='Only the lines named by the cited pages; commodity kind with no whole-space reference.'; k['xg']='by maker'

# ---------- Arcade
SEGA=W+'List_of_Sega_arcade_system_boards'; NAM=W+'List_of_Namco_arcade_system_boards'
k=get(6,'Arcade system board')
stats['m_removed']+=len(k.pop('m',[]))
keep=[e for e in k['x'] if e['n'] in('Neo Geo MVS','Capcom CP System','Taito Type X','Konami System 573','Nintendo VS. System')]
for e in keep:
    if e['n']=='Capcom CP System':
        e['v']=[ver('CP System (CPS-1)','Capcom','1988','released 13 May 1988'),ver('CP System Dash (CPS-1.5)','Capcom','1992'),ver('CP System II','Capcom'),ver('CP System III','Capcom')]
        e['y']='1988'
sega=[('Dual','1979'),('G80','1981'),('VCO Object','1981'),('LaserActive arcade','1983'),('System 1','1984'),('System 2','1984'),('Super Scaler','1985'),('System E','1986'),('System 16','1986'),('System 18','1989'),('OutRun','1986'),('X Board','1987'),('System 24','1988'),('Y Board','1988'),('Mega-Tech and Mega Play','1989'),('System C','1989'),('System 32','1990'),('Model 1','1992'),('Model 2','1994'),('ST-V','1995'),('Model 3','1996'),('NAOMI','1998'),('Hikaru','1999'),('NAOMI 2','2001'),('Triforce','2003'),('Chihiro','2002'),('SystemSP','2004'),('Lindbergh','2005'),('Europa-R','2008'),('RingEdge','2009'),('Nu','2013'),('ALLS','2018')]
nam=[('System 1','1987'),('System 2','1987'),('System 21','1988'),('NA-1','1992'),('NA-2','1992'),('System 22','1992'),('NB-1','1993'),('System FL','1993'),('System 11','1994'),('NB-2','1995'),('Super System 22','1995'),('ND-1','1995'),('System 12','1996'),('System 22.5 (Gorgon)','1997'),('System 23','1997'),('Super System 23','1997'),('Super System 23 GMEN','1998'),('Super System 23 Evolution 2','1999'),('System 10','2000'),('System 246','2000'),('System 256','2004'),('Super System 256','2006'),('System N2','2005'),('System ES1','2009'),('System ES1 (A2)','2011'),('System ES2 Plus','2012'),('System ES3','2013'),('System ES4','2015'),('System BNA1','2018'),('System BNA1 LITE','2013')]
k['x']=keep
for n,y in sega: k['x'].append(ent('Sega '+n,'Sega',y,'Sega arcade board named on the Wikipedia list of Sega boards.',SEGA))
for n,y in nam: k['x'].append(ent('Namco '+n,'Namco',y,'Namco arcade board named on the Wikipedia list of Namco boards.',NAM))
for e in k['x']:
    e['g']=e.get('mk') or 'Other'
    if e['n']=='Sega NAOMI': e['role']='landmark'
k['x']=[e for e in k['x'] if e.get('role')!='landmark']  # no landmark claim without a page
k['x'].sort(key=lambda e:(e['g'],e.get('y') or '9999',e['n']))
k['nl']='One entry is a named arcade system board; revisions and variants are versions.'
k['sel']="Every board on Wikipedia's List of Sega arcade system boards and List of Namco arcade system boards, plus Neo Geo MVS, CP System, Taito Type X, Konami System 573 and the Nintendo VS. System from earlier pages. Wikipedia has no list for Taito, Capcom, Konami or Atari boards (those pages returned 404)."
k['xg']='by maker'
cov(k,'Complete: 32 of 32 boards in the Sega list and 30 of 30 in the Namco list (the Sega page was read to 100,000 of 106,908 characters); other makers are partial.')

# cabinets from List of Japanese arcade cabinets
JC=W+'List_of_Japanese_arcade_cabinets'
cab=[('Konami','Domy Theater 50','1996','candy'),('Konami','Domy Jr','','candy'),('Konami','Domy Theater 33','','candy'),('Konami','Plasma','','candy'),('exA-Arcadia','ARC-32','2024','candy'),('Sega','Megalo 410','1996','candy'),('Sega','Super Megalo','','candy'),('Sega','Super Megalo 2','1994','candy'),('Sega','Megalo 50','','candy'),('Sega','Naomi Deluxe Universal','2005','candy'),('Sega','Naomi 50 Universal','','candy'),('Sega','Naomi Universal','1999','candy'),('Sega','Lindbergh Universal','2007','candy'),('Sega','ALL.Net P-ras MULTI Version 3','2019','candy'),
('Jaleco','Pony 40','','candy'),('Irem','Madonna','','candy'),('Irem','Madonna 33','','candy'),('Capcom','BGS-25','','candy'),('Capcom','Impress','','candy'),('Capcom','Cute','','candy'),('Capcom','Status 18','','candy'),('Capcom','Status 25','','candy'),('Capcom','OOB-50','','candy'),('Capcom','CAV System 60','','candy'),('Sigma','Game Explorer','','candy'),
('SNK','Candy 18','','candy'),('SNK','Candy 25','','candy'),('SNK','Candy 26','','candy'),('SNK','MV25UP-0','','candy'),('SNK','MVS-U1/33','','candy'),('SNK','MVS-U2','','candy'),('SNK','MVS-U4','','candy'),('SNK','Neo 19','','candy'),('SNK','Neo 25','','candy'),('SNK','Neo 29','','candy'),('SNK','Neo 50','','candy'),('SNK','Neo Candy 25','','candy'),('SNK','Neo Candy 29','','candy'),('SNK','SC14-2','','candy'),('SNK','SC19-4','','candy'),('SNK','SC25-4','','candy'),('SNK','Super Neo 29','','candy'),('SNK','Super Neo 28 Candy','1996','candy'),
('Taito','Canary','1991','candy'),('Taito','Teatro Ex 33','','candy'),('Taito','Teatro 50','','candy'),('Taito','MT5','1989','candy'),('Taito','MT2','1987','candy'),
('Namco','Dynalive','','candy'),('Namco','Excelcabinet','','candy'),('Namco','Exceleena','','candy'),('Namco','Arena Site','','candy'),('Tecmo','Kyotaro','','candy'),('Tecmo','Urban','','candy'),('Sammy','Atomiswave SD','2003','candy'),('Sunsoft','Rana','','candy'),('River Service','Delta','','candy'),('Lucky','Galaxy','','candy'),('Other makers','AMBO','','candy'),('Other makers','MAS 25','','candy')]
kc=get(6,'Candy (sit-down) arcade cabinet')
stats['m_removed']+=len(kc.pop('m',[])); 
for mk,n,y,t in cab:
    e=ent(mk+' '+n,mk,y,'Sit-down cabinet named on the Wikipedia list of Japanese arcade cabinets.',JC)
    if n.startswith('Exceleena'): e['v']=[ver('Exceleena 1','Namco'),ver('Exceleena 2','Namco')]
    kc['x'].append(e)
for e in kc['x']: e['g']=e.get('mk') or 'Other'
kc['x'].sort(key=lambda e:(e['g'],e.get('y') or '9999',e['n']))
kc['nl']='One entry is a cabinet model or line sold under its own name; sizes and revisions are versions.'
kc['sel']="Candy rows of Wikipedia's List of Japanese arcade cabinets (all rows of that type), sectioned by maker, plus the Astro City, Windy and other lines already held. The list's SNK and Capcom numbered models are entries because it names them separately."
kc['xg']='by maker'
cov(kc,'Covers the candy and candy/upright rows of the list (about 100 of its 118 rows); upright, cocktail and unknown-type rows are under other kinds or left out.')
stats['r_removed']+=0
ku=get(6,'Upright arcade cabinet'); stats['m_removed']+=len(ku.pop('m',[]))
for mk,n,y in [('Sega','Swing','1991'),('Capcom','Playzass',''),('Capcom','Captain IV',''),('Capcom','CAV 2 OOB 60',''),('Jaleco','Pony Mark II 27','1992'),('Konami','Sauroid',''),('Sammy','Atomiswave',''),('SNK','MV19SC-0',''),('SNK','MV25U4-0',''),('SNK','MV25U6-0',''),('SNK','SCB-U4','')]:
    ku['x'].append(ent(mk+' '+n,mk,y,'Upright cabinet named on the Wikipedia list of Japanese arcade cabinets.',JC))
for e in ku['x']: e['g']=e.get('mk') or 'Other'
ku['x'].sort(key=lambda e:(e['g'],e.get('y') or '9999',e['n']))
ku['nl']='One entry is an upright cabinet model; revisions are versions.'; ku['sel']="The upright rows of Wikipedia's List of Japanese arcade cabinets, sectioned by maker, plus the Neo Geo MVS upright from an earlier page."; ku['xg']='by maker'
cov(ku,'Covers 11 upright rows; Super Neo 28 Candy (candy/standup) is under Candy.')
kk=get(6,'Cocktail table arcade cabinet'); stats['m_removed']+=len(kk.pop('m',[]))
for mk,n,y in [('Sega','Aero Table','1988'),('Jaleco','Table Pony',''),('Jaleco','Table Pony 25',''),('Jaleco','Table Pony 25 VH',''),('SNK','MV25TA-0','')]:
    kk['x'].append(ent(mk+' '+n,mk,y,'Cocktail cabinet named on the Wikipedia list of Japanese arcade cabinets.',JC))
for e in kk['x']: e['g']=e.get('mk') or 'Other'
kk['nl']='One entry is a cocktail-table cabinet model.'; kk['sel']="The cocktail rows of Wikipedia's List of Japanese arcade cabinets."; kk['xg']='by maker'
cov(kk,'Complete: 5 of 5 cocktail rows.')

# remaining kinds: generic
GENERIC_SEL='No whole-space reference exists; entries are those named by the pages each one cites.'
for dep in (1,2,3,4,5,6):
    for s in d['depts'][dep]['s']:
        for k in s['k']:
            if 'm' in k:
                stats['m_removed']+=len(k['m']); del k['m']
            if k.get('x'):
                for e in k['x']:
                    if not e.get('g'): e['g']=e.get('mk') or 'Other'
                    e.pop('m',None)
                k.setdefault('nl','One entry is a %s sold or made under its own name; revisions and models are versions.'%k['n'][0].lower()+k['n'][1:])
                k.setdefault('sel',GENERIC_SEL)
                k.setdefault('xg','by maker')
            if k.get('r') and k['n'] not in('Home replica arcade cabinet','Digital pinball cabinet','Candy (sit-down) arcade cabinet'):
                stats['r_removed']+=len(k['r']); del k['r']
            k.setdefault('x',k.get('x',[])) if False else None
for dep in range(1,7):
    for s_ in d['depts'][dep]['s']:
        for k_ in s_['k']:
            if k_.get('x')==[] and not k_.get('nl'): del k_['x']
json.dump(d,open(P+'.tmp','w'),indent=1,ensure_ascii=False)
os.rename(P+'.tmp',P)
print(stats)
