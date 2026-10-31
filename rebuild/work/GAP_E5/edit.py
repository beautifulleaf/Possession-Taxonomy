import json,os,re
P='rebuild/out/E5.json'
d=json.load(open(P))
def kind(n):
    for dp in d['depts']:
        for s in dp['s']:
            for k in s['k']:
                if k['n']==n: return k
    raise KeyError(n)
def ent(k,n):
    for e in k['x']:
        if e['n']==n: return e
def add(k,e):
    if ent(k,e['n']): return
    e.setdefault('a',''); e.setdefault('dt','')
    k['x'].append(e)
    k['x'].sort(key=lambda e:(e.get('g',''),e.get('y') or '9999',e['n']))
W='https://en.wikipedia.org/wiki/'
# ---- arcade boards
k=kind('Arcade system board')
for n,m,y,s,desc in [
 ('Taito F3 System','Taito','',"https://www.pixelatedarcade.com/tech_attributes/overview/arcade/taito-f3-system/",'Taito 32-bit arcade board with swappable ROM cartridges, sold in North America as Cybercore.'),
 ('Taito NESiCAxLive','Taito','2010',W+'NESiCAxLive','Taito download-based arcade system launched in Japan in 2010 and in the United States in 2015.'),
 ('Taito NESYS','Taito','',W+'NESYS','Taito arcade system; the article gives no release year.'),
 ('Hyper Neo Geo 64','SNK','1997',W+'Hyper_Neo_Geo_64',"SNK's arcade-only successor to the Neo Geo and its only board able to render 3D graphics."),
 ('Atomiswave','Sammy','',W+'Atomiswave','Sammy arcade board and cabinet built on Dreamcast hardware, with swappable game cartridges.'),
 ('Konami Bubble System','Konami','1985',W+'Bubble_System','Konami modular arcade platform that stored games on swappable bubble-memory cartridges.'),
 ('Nintendo PlayChoice-10','Nintendo','1986',W+'PlayChoice-10','Nintendo arcade system that let players sample up to ten NES games, one at a time.'),
 ('DECO Cassette System','Data East','1980',W+'DECO_Cassette_System','Data East base cabinet that ran different games from cassette tapes, the first standard arcade system with swappable games.'),
 ('Mega System 1','Jaleco','',W+'Mega_System_1','Jaleco arcade board; the article gives no release year.'),
 ('Mega System 32','Jaleco','',W+'Mega_System_32','Jaleco arcade board; the article gives no release year.'),
 ('PolyGame Master','IGS','1997',W+'PolyGame_Master','Arcade board released by the Taiwanese company IGS in 1997.'),
 ('exA-Arcadia','exA-Arcadia','2019',W+'ExA-Arcadia','Arcade system board released in 2019.'),
 ('TIA-MC-1','Ekstrema-Ukraina','',W+'TIA-MC-1','Soviet arcade board developed in the mid-1980s and built by the Terminal association and other factories.'),
]:
    add(k,{'n':n,'d':desc,'mk':m,'y':y,'s':s,'v':[],'g':m})
cp=ent(k,'Capcom CP System')
for v in cp['v']:
    if v['n']=='CP System II': v['y']='1993'
    if v['n']=='CP System III': v['y']='1996'
k['sel']=("Every board on Wikipedia's List of Sega arcade system boards (32 of 32) and List of Namco arcade system boards (30 of 30), plus every board in Wikipedia's arcade-board categories (Arcade system boards, Capcom, Konami, Nintendo, Taito, 68k-based, Neo Geo) except the Williams Pinball Controller (pinball) and Data Carddass and Photon (not boards), plus Neo Geo MVS, Taito Type X, Konami System 573 and the Nintendo VS. System from earlier pages. "
 "Covers 80 boards; Wikipedia has no list for Atari, Irem, Data East, Cave, Konami's later boards or Taito's earlier boards (the Konami GX and Taito F3 articles gave 404), so those makers are partial.")
# ---- game disc
k=kind('Game disc')
for n,m,y,s,desc in [
 ('PlayStation CD-ROM game disc','Sony','1994',W+'PlayStation_(console)','CD-ROM disc used for PlayStation games from the Japanese launch in 1994.'),
 ('PlayStation 2 game disc','Sony','2000',W+'PlayStation_2','Mostly DVD-ROM, with earlier titles on blue-tinted CD-ROM; the console launched in Japan in 2000.'),
 ('Xbox DVD-ROM game disc','Microsoft','2001',W+'Xbox_(console)','DVD-ROM disc read by the original Xbox, launched in North America in 2001.'),
 ('Xbox 360 game disc','Microsoft','',W+'Xbox_360','DVD disc for the Xbox 360; the article lists its media as DVD, CD and digital distribution.'),
 ('Mega-CD and Sega CD disc','Sega','1991',W+'Sega_CD','CD-ROM disc for the Mega-CD add-on, launched in Japan in 1991.'),
]:
    add(k,{'n':n,'d':desc,'mk':m,'y':y,'s':s,'v':[],'g':m})
k['sel']=("Disc formats named in Wikipedia's Optical disc and Blu-ray articles and in the console articles for PlayStation, PlayStation 2, Xbox, Xbox 360 and Sega CD, sectioned by platform maker. "
 "No complete list exists; follows those overviews. Saturn, 3DO and other CD consoles are not entered because no fetched page names a disc format for them.")
# ---- converters
k=kind('Cartridge converter')
add(k,{'n':'Intellivision System Changer','d':'Accessory that lets the Intellivision play Atari 2600 cartridges and use Atari-compatible joysticks.','mk':'Mattel','y':'1983','s':W+'Intellivision','v':[],'g':'Mattel'})
add(k,{'n':'ColecoVision Expansion Module #1','d':'Module with its own 2600-equivalent electronics that lets the ColecoVision run Atari 2600 cartridges and controllers.','mk':'Coleco','y':'','s':W+'ColecoVision','v':[],'g':'Coleco'})
k['sel']=("Official converters named on their own pages (Power Base Converter, Super Game Boy, Game Boy Player, Intellivision System Changer, ColecoVision Expansion Module #1). "
 "No complete list exists; follows those console articles. Third-party converters are not listed because no fetched reference covers them.")
# ---- handheld PC
k=kind('Handheld gaming PC')
for n,m,s,desc in [
 ('GPD Win Mini','GPD',"https://liliputing.com/compare-handheld-gaming-pc-specs-anbernic-ayn-aya-gpd-onexplayer-and-valve/",'Compact GPD handheld PC named in the Liliputing comparison.'),
]: pass
gm={'GPD Win':'GPD','Ayaneo':'Ayaneo','Steam Deck':'Valve','Legion Go':'Lenovo','ROG Ally':'Asus','MSI Claw':'MSI','ONEXPLAYER':'OneXPlayer'}
for e in k['x']: e['g']=gm[e['n']]; e['mk']=e.get('mk') or gm[e['n']]
k['xg']='by maker'
k['sel']=k['sel'].replace('; ordered by release year.','; sections by maker, ordered by release year.')+(" Liliputing's comparison adds models (ROG Xbox Ally, Legion Go 2 and Go S, GPD Win Mini, Win 4 and Win 5, ONEXPLAYER X1 Mini, Ayaneo 3) as versions of these lines. "
 "No complete list exists; follows Wikipedia's handheld list and the Liliputing comparison, whose table is an image and gives no years.")
liv="https://liliputing.com/compare-handheld-gaming-pc-specs-anbernic-ayn-aya-gpd-onexplayer-and-valve/"
def addv(kn,en,vs):
    e=ent(kind(kn),en); e.setdefault('v',[])
    have={v['n'] for v in e['v']}
    for vn,y,dd in vs:
        if vn not in have: e['v'].append({'n':vn,'mk':e.get('mk',''),'y':y,'d':dd})
addv('Handheld gaming PC','Legion Go',[('Legion Go 2','','named in Liliputing comparison'),('Legion Go S','','named in Liliputing comparison')])
addv('Handheld gaming PC','ROG Ally',[('ROG Xbox Ally','','named in Liliputing comparison')])
addv('Handheld gaming PC','GPD Win',[('GPD Win Mini','',''),('GPD Win 4','2023',''),('GPD Win 5','','')])
addv('Handheld gaming PC','ONEXPLAYER',[('X1 Mini','','')])
addv('Handheld gaming PC','Ayaneo',[('Ayaneo 3','','')])
# ---- tabletop and hw upgrade g
for kn in ('Tabletop electronic game','Hardware upgrade add-on'):
    kk=kind(kn)
    for e in kk['x']: e['g']=e.get('g') or e.get('mk') or 'Maker not stated'
    kk['xg']='by maker'
    print(kn,[ (e['n'],e['g']) for e in kk['x']])
# ---- flash
k=kind('Flash cartridge')
add(k,{'n':'PVBackup','d':'Nintendo 64 backup device by Valery Pudov, named in the Game backup device article.','mk':'Valery Pudov','y':'','s':W+'Game_backup_device','v':[],'g':'Valery Pudov'})
add(k,{'n':'XG-Flash','d':'Game Boy Advance flash cartridge named in the Game backup device article.','mk':'Maker not stated','y':'','s':W+'Game_backup_device','v':[],'g':'Maker not stated'})
add(k,{'n':'Game Partners Classic','d':'Super Nintendo copier by Bung named in the Game backup device article.','mk':'Bung','y':'','s':W+'Game_backup_device','v':[],'g':'Bung Enterprise'})
r4=ent(k,'R4 cartridge')
if not any(v['n']=='R4DS' for v in r4.get('v',[])): r4.setdefault('v',[]).append({'n':'R4DS','mk':'','y':'','d':'Nintendo DS copier named in the Game backup device article'})
k['sel']=("Product families named in Wikipedia's Game backup device article plus the EverDrive, FXPak Pro, R4 and Mig Flash entries from earlier passes, sectioned by maker. "
 "Complete: all 23 rows of the Game backup device article are entered (as 24 entries with EverDrive 64 under EverDrive and R4DS under R4); the Game Boy Xchanger variants are versions.")
# ---- game card etc. coverage lines
SEL={
 'Home console':"Complete: 92 of 92 in-scope consoles in List of home video game consoles.",
 'Microconsole':"Complete: 12 of 12 in-scope units on Wikipedia's Microconsole page.",
 'FPGA & clone console':"Complete: 10 of 10 families on List of retro style video game consoles, plus MiSTer.",
 'Handheld console':"Complete: 42 of 42 in-scope consoles in List of handheld game consoles.",
 'Hybrid console':"Complete: 2 of 2 in List of home video game consoles and List of handheld game consoles.",
 'Emulation handheld':"No complete list exists; follows Retro Handheld HQ's guide and Wikipedia's List of handheld game consoles.",
 'Plug-and-play & mini console':"Complete: 38 of 38 in-scope rows of List of dedicated consoles and the dedicated section of List of retro style video game consoles.",
 'LCD handheld game':"No complete list exists; follows the Game & Watch page, List of dedicated consoles and List of retro style video game consoles.",
 'Tabletop electronic game':"No complete list exists; follows the Game & Watch page and List of dedicated consoles.",
 'Disk or CD drive add-on':"Complete: 5 of 5 drive add-ons in List of home video game consoles.",
 'Hardware upgrade add-on':"No complete list exists; follows List of home video game consoles.",
 'Game cartridge':"Covers 39 of 52 platform rows in ROM cartridge; the other 13 are not game cartridges or sit under Game card or Consoles & handhelds.",
 'Game card':"No complete list exists; follows the cards' own Wikipedia articles.",
 'Cassette or floppy game':"No complete list exists; follows Wikipedia's Famicom Disk System article.",
 'Budget re-release':"No complete list exists; follows the Nintendo Selects and Player's Choice pages.",
 'Gamepad':"No complete list exists; follows Wikipedia's Gamepad, Game controller and Category:Gamepads (15 pages, all entered as lines). Third-party pads (8BitDo, GameSir, Hori, Razer) have no fetched list.",
 'Joystick':"No complete list exists; follows the Game controller article.",
 'Arcade stick':"Covers 8 stick lines; Wikipedia's Category:Arcade controllers (Arcade controller, Namco Arcade Stick, NES Advantage, Smash Box controller) is held except the Smash Box controller, which is a component. No complete list exists; other brands have no fetched list.",
 'Leverless controller':"No complete list exists; follows the Hit Box and Razer Kitsune pages.",
 'Light gun':"No complete list exists; follows the pages each entry cites.",
 'Racing wheel':"No complete list exists; follows the Game controller article.",
 'Optical drive emulator':"No complete list exists; follows the pages each entry cites.",
 'Modchip':"No complete list exists; follows the Xecuter page.",
 'Cheat device':"No complete list exists; follows the Game Genie, Action Replay and GameShark pages.",
 'Phone VR viewer':"Complete: 3 of 3 viewers in the List of virtual reality headsets.",
 'XR glasses':"No complete list exists; follows the pages each entry cites.",
}
for kn,t in SEL.items():
    kk=kind(kn)
    if kn=='Gamepad': kk['sel']=re.sub(r' Third-party pads.*$','',kk['sel']).rstrip()+' '+t
    elif kn=='Arcade stick': kk['sel']=re.sub(r' Other brands.*$','',kk['sel']).rstrip()+' '+t
    elif kn=='Game cartridge': kk['sel']=re.sub(r' Holds 39.*$','',kk['sel']).rstrip()+' '+t
    elif kn=='Phone VR viewer': kk['sel']=kk['sel'].rstrip()+' '+t
    else: kk['sel']=kk['sel'].rstrip()+' '+t
# generic
G="No complete list exists; follows the pages each entry cites."
for dp in d['depts']:
  for s in dp['s']:
    for k in s['k']:
      if k.get('x'):
        sel=k.get('sel','')
        sel=sel.replace("No whole-space reference exists; entries are those named by the pages each one cites.",G)
        sel=sel.replace("Only the lines named by the cited pages; commodity kind with no whole-space reference.",G)
        k['sel']=sel
# VR tails
k=kind('Standalone VR headset')
k['sel']=re.sub(r'Covers the standalone rows.*$','',k['sel']).rstrip()+" Complete: 14 of 14 in-scope standalone lines in List of virtual reality headsets, read to the end of the page."
k=kind('Tethered VR headset')
k['sel']=re.sub(r'Covers the tethered rows.*$','',k['sel']).rstrip()+" Complete: 14 of 14 in-scope tethered lines in List of virtual reality headsets, read to the end of the page."
# remaining check
for dp in d['depts']:
  for s in dp['s']:
    for k in s['k']:
      if k.get('x') and not any(t in k['sel'] for t in('Complete:','Covers','No complete list')): print('NOCOV',k['n'],k['sel'][-80:])
tmp=P+'.tmp'; json.dump(d,open(tmp,'w'),ensure_ascii=False,indent=1); os.replace(tmp,P)
