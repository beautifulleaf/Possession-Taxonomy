import json,copy,os,sys,shutil,datetime
R='/home/user/Possession-Taxonomy/rebuild'
src=json.load(open(R+'/work/STR_D3/bak/D3.json'))
old={}
for dp in src['depts']:
    for s in dp['s']:
        for k in s['k']: old[k['n']]=copy.deepcopy(k)
used=set()
WIKI='https://en.wikipedia.org/wiki/'
renames={}
def K(o,new=None,d=None,tt=None,see=None,demote=(),m=None,r=None,xadd=(),s=None,a=None,xdrop=()):
    if o in old:
        k=copy.deepcopy(old[o]); used.add(o)
    else:
        k={'n':o,'a':'','d':'','s':s or '','x':[]}
    if new and new!=o:
        renames[o]=new; k['n']=new
    if d: k['d']=d
    if a is not None: k['a']=a
    if s: k['s']=s
    k.pop('t',None)
    k['tt']=tt
    for nm in demote:
        xs=k.get('x',[])
        hit=[x for x in xs if x['n']==nm]
        assert hit,(o,nm)
        x=hit[0]; k['x']=[y for y in xs if y is not x]
        k.setdefault('r',[])
        if [nm,x.get('mk','')] not in k['r']: k['r'].append([nm,x.get('mk','')])
        k.setdefault('m',[])
        for v in x.get('v',[]):
            e=[v['n'],v.get('mk') or x.get('mk','')]
            if e not in k['m']: k['m'].append(e)
    for nm in xdrop:
        k['x']=[y for y in k['x'] if y['n']!=nm]
    for x in xadd: k.setdefault('x',[]).append(x)
    if m is not None: k['m']=m
    if r is not None: k['r']=r
    if see: k['see']=see
    if not k.get('x'): k.pop('x',None)
    if not k.get('m'): k.pop('m',None)
    if not k.get('r'): k.pop('r',None)
    return k
def ARCH(n,d,mk,y,s,dt=None,v=None):
    x={'n':n,'a':'','d':d,'mk':mk,'y':y,'s':s,'v':v or []}
    if dt: x['dt']=dt
    return x
def S(n,t,k,ax=None):
    s={'n':n,'t':t,'k':k}
    if ax: s['ax']=ax
    return s
def DEPT(o,t,ax,shelves,mode=None,note=None):
    od=[d for d in src['depts'] if d['n']==o][0] if o else None
    dp={'n':o}
    return dp
def D(name,mode,note,t,ax,shelves,b=None):
    dp={'n':name,'mode':mode}
    if note: dp['note']=note
    if b: dp['b']=b
    dp['t']=t; dp['ax']=ax; dp['s']=shelves
    return dp
def mv(k,names):
    """take models from k whose model name in names"""
    return [e for e in k['m'] if e[0] in names]
# ---------- helper for splits ----------
hc=old['Home cinema speakers']; rd=old['Radio']
HC_PKG=['Klipsch Reference Theater Pack','Klipsch R-600F Home Theater System','Klipsch R-800F Home Theater System','Polk Audio Signature Elite 5.2 Home Theater System','Polk Audio Signature Elite 2.1 System','Monitor Audio Bronze AMS 7G']
HC_CEN=['Polk Audio Reserve R350','Polk Audio Signature Elite ES35','Polk Audio Monitor XT30','Polk Audio T30','JBL Stage 240H']
HC_SUR=['Klipsch RP-502S II','Paradigm Surround 3','Polk Audio SR2 Wireless Surrounds','Polk Audio Signature Elite ES10']
HC_HGT=['Klipsch RP-500SA II','Mission LX-3D','Polk Audio Reserve R900']
HC_INW=['Polk Audio 265-LS','Polk Audio 80 F/X-LS']
assert sorted(HC_PKG+HC_CEN+HC_SUR+HC_HGT+HC_INW)==sorted(e[0] for e in hc['m'])
HCS=hc['s']
HOME=WIKI+'Home_cinema'
RD_TAB=['TAV2000DB','Blutune 300L','Revere 100','Revere 500']
RD_POR=['Rambler Max','SolarDAB 99','SportsDAB 65']
assert sorted(RD_TAB+RD_POR)==sorted(e[0] for e in rd['m'])

# ================= departments =================
depts=[]
# ---- 1 Headphones
over=K('Over-ear headphones',d='Headphone whose cups enclose the ear, open or sealed at the back, with a dynamic, planar-magnetic or electrostatic driver; electrostatic models need a separate energiser.',
 tt=[['Back',['Open-back','Semi-open','Closed-back']],['Driver',['Dynamic','Planar magnetic','Electrostatic']],['Connection',['Wired','Bluetooth','Wired and wireless']],['Noise control',['Passive isolation','Active noise cancelling']]],
 a='circumaural headphones · full-size headphones · electrostatic headphones · Stax earspeakers',
 see=[['E3','Studio headphones','same headphones sold for studio monitoring']])
es=old['Electrostatic headphones']; renames['Electrostatic headphones']='Over-ear headphones'; used.add('Electrostatic headphones')
over['x']=over.get('x',[])+es.get('x',[])
over['m']=over.get('m',[])+es.get('m',[])
onear=K('On-ear headphones',d='Headphone whose pads rest on the ear rather than around it, open or closed, such as the Grado SR and Sennheiser HD 25.',
 tt=[['Back',['Open','Closed']],['Connection',['Wired','Bluetooth']],['Use',['Hi-fi listening','DJ monitoring','Travel']]],a='supra-aural headphones')
headset=K('Headset',d='Headphones with a microphone attached, over or on the ear, for gaming, calls or streaming.',
 tt=[['Use',['Gaming','Office and calls']],['Connection',['Wired','Wireless']],['Microphone',['Boom','Built into the cup']]],
 see=[['G1','Headset','a different object: the bearing set of a bicycle'],['D1','Microphone','a stand-alone desktop microphone']])
ear=K('Earbuds',d='Earphone that rests in the outer ear without sealing the canal, wired.',tt=[['Connector',['3.5 mm','USB-C','Lightning']]],a='EarPods · outer-ear earphones')
iem=K('In-ear monitors',d='Earphone that seals the ear canal with standard tips, sold for listening.',
 tt=[['Driver',['Dynamic','Balanced armature','Hybrid','Planar magnetic','Electrostatic']],['Cable connector',['MMCX','Two-pin','Fixed']]],
 see=[['E3','In-ear monitors','the same earphones used on stage and in the studio']])
ciem=K('Custom in-ear monitors',d='In-ear earphones with shells moulded to one listener\'s ear canal.',
 tt=[['Shell',['Acrylic','Silicone']],['Driver count',['Single','Two to four','Five to ten','More than ten']]],
 demote=['Ultimate Ears custom monitors'],see=[['E3','In-ear monitors','stage and studio use of custom moulds']])
tws=K('True wireless earbuds',d='Two separate wireless buds sold with a charging case.',tt=[['Noise control',['With active noise cancelling','Without']],['Fit',['Sealed in the canal','Open, no seal','Ear-hook']]])
oe=K('Open-ear earphones',d='Earphones that leave the ear canal open, by bone conduction or an open-ear driver.',tt=[['Conduction',['Bone conduction','Air conduction (open-ear driver)']],['Wear',['Behind-the-neck band','Ear-clip','Ear-hook']]],a='bone-conduction headphones')
depts.append(D('Headphones & earphones','mixed','Tier for everyday wireless models; variety for the enthusiast (head-fi) end.',
 'Audio worn on or in the ears, wired or wireless, from hi-fi headphones to earbuds; spare parts and cables → Stands, cables & accessories; stage and studio monitoring gear → E3.',
 'Does the sound unit sit around or on the ear, or go in or beside it?',[
 S('Over-ear & on-ear headphones','Headphones with a band and two cups, from open hi-fi models to noise-cancelling travel sets and headsets; an earphone that goes in the ear → Earphones shelf.',[over,onear,headset],
   ),
 S('Earphones & in-ear monitors','Units that sit in or beside the ear, from wired earbuds and moulded monitors to true wireless buds and bone-conduction sets; a band-and-cup headphone → Headphones shelf.',[ear,iem,ciem,tws,oe],
   'kinds by how the unit sits: outer ear, sealed canal, moulded canal, cordless in the canal, outside the canal')]))
# ---- 2 Loudspeakers
bs=K('Bookshelf speakers',d='Compact speaker cabinet made to stand on a stand, shelf or desk, passive or active.',
 tt=[['Power',['Passive','Active (powered)','Wireless streaming']],['Cabinet loading',['Sealed','Ported','Passive radiator']],['Driver arrangement',['Two-way','Three-way','Coaxial']]],
 demote=['Genelec active monitors'])
fs=K('Floor-standing speakers',d='Tall speaker cabinet that stands on the floor.',tt=[['Power',['Passive','Active or wireless']],['Driver arrangement',['Two-way','Three-way','Dual-concentric']],['Cabinet loading',['Ported','Sealed','Transmission line']]])
sub=K('Subwoofer',d='Speaker that reproduces only bass, for stereo or surround systems.',tt=[['Power',['Active','Passive','Wireless']],['Cabinet loading',['Sealed','Ported','Passive radiator']]],see=[['D3','Home cinema speaker package','a subwoofer is the .1 of a surround layout']])
esl=K('Electrostatic and planar loudspeakers',d='Loudspeaker driven by a large thin film panel, electrostatic or planar-magnetic, usually radiating front and back.',tt=[['Panel type',['Full-range electrostatic','Hybrid electrostatic with cone woofer','Planar magnetic','Ribbon']]])
horn=K('Horn loudspeakers',d='Home loudspeaker whose drivers fire through horns for high efficiency, often suited to low-power valve amplifiers.',tt=[['Horn loading',['Fully horn-loaded','Horn with direct-radiating woofer']],['Horn form',['Corner horn','Folded horn','Spherical horn']]])
fr=K('Full-range speaker',d='Loudspeaker built around one wide-range driver with no crossover, often in a horn, baffle or transmission-line cabinet.',s=WIKI+'Loudspeaker',
 tt=[['Cabinet',['Open baffle','Back-loaded horn','Transmission line','Bass reflex']],['Cone',['Paper cone','Whizzer cone']]],a='single-driver speaker · wide-range speaker')
pkg=K('Home cinema speakers',new='Home cinema speaker package',d='Matched set of speakers sold together for a surround layout, with or without a subwoofer.',m=[e for e in hc['m'] if e[0] in HC_PKG],r=hc.get('r'),
 tt=[['Channel layout',['2.1','5.1','7.1','5.1.2 Atmos','7.1.4 Atmos']],['Front speakers',['Satellite','Bookshelf','Floor-standing']],['Rear speakers',['Wired','Wireless']]],see=[['D3','Soundbar','a soundbar is the one-box alternative']])
cen=K('Centre channel speaker',d='Speaker placed under or behind the screen to carry dialogue in a surround layout.',s=HOME,m=[e for e in hc['m'] if e[0] in HC_CEN],tt=[['Placement',['Under the screen','On a shelf','Behind an acoustically transparent screen']],['Driver arrangement',['Two-way','Three-way']]],a='centre speaker · centre channel')
sur=K('Surround speaker',d='Speaker placed at the sides or rear of the room for the surround channels, on a stand, shelf or wall.',s=HOME,m=[e for e in hc['m'] if e[0] in HC_SUR],tt=[['Placement',['Bookshelf','On-wall','Bipole or dipole']],['Connection',['Wired','Wireless']]],a='rear speaker · side speaker')
hgt=K('Height speaker',d='Speaker for the overhead channels of an object-based surround layout, upward-firing or ceiling-mounted.',s=HOME,m=[e for e in hc['m'] if e[0] in HC_HGT],tt=[['Method',['Upward-firing module','On-wall high','Ceiling-mounted']],['Format',['Dolby Atmos','DTS:X']]],a='Atmos speaker · Atmos-enabled speaker')
inw=K('In-wall and in-ceiling speaker',d='Speaker made to be built into a wall or ceiling, with a grille flush to the surface; the installed fitting belongs with the home.',s=HOME,m=[e for e in hc['m'] if e[0] in HC_INW],tt=[['Mounting',['In-wall','In-ceiling','On-wall']],['Channel role',['Front','Surround','Height']]],see=[['G3','In-wall and in-ceiling speaker','the same speaker as a fitted part of the home']])
sb=K('Soundbar',d='Speaker made as a bar for a TV, with or without a separate subwoofer.',tt=[['Channels',['2.0','3.1','5.1.2','7.1.4']],['Form',['Soundbar','Sound base','Bar with separate subwoofer']],['TV connection',['HDMI eARC','Optical','Bluetooth']]],s=old['Soundbar']['s'])
wf=K('Wi-Fi and multi-room speakers',d='Mains-powered speaker that streams over Wi-Fi or Bluetooth, often grouping with others across rooms.',tt=[['Connection',['Wi-Fi multi-room','Mains-powered Bluetooth']],['Size',['Compact','Mid-size','Large']]],see=[['D3','Smart speaker','a speaker run by a voice assistant']])
pb=K('Portable Bluetooth speakers',d='Battery-powered speaker made to carry around, usually Bluetooth and often waterproof; party speakers are the largest.',tt=[['Size',['Pocket','Mid-size','Party speaker']],['Protection',['Splash-resistant','Waterproof']]],see=[['D3','Boombox','a portable system with its own player']])
depts.append(D('Loudspeakers','mixed','Variety for hi-fi loudspeakers; tier for home-cinema, soundbars and wireless speakers.',
 'Speakers that turn an amplifier or wireless signal into room sound, from hi-fi to surround to soundbars; a speaker run by an assistant → Smart speakers & displays; a stage PA speaker → E3.',
 'What system is the speaker made for: stereo listening, a surround layout, or self-contained TV and wireless use?',[
 S('Hi-fi loudspeakers','Speakers for two-channel listening, from stand-mounted monitors and floor-standers to panel, horn and single-driver designs; a surround channel speaker → Home cinema speakers.',[bs,fs,sub,esl,horn,fr],
   'kinds by cabinet role first (stand-mount, floor-standing, bass-only), then by driver principle (panel, horn, single driver)'),
 S('Home cinema speakers','Speakers sold for a surround layout, as a package or by position in the room; a stereo pair for music → Hi-fi loudspeakers.',[pkg,cen,sur,hgt,inw],
   'kinds by place in the layout: the whole package, centre, sides and rear, overhead, built into the wall'),
 S('Soundbars & wireless speakers','Self-contained speakers that need no separate amplifier: a bar under the TV, a mains-powered Wi-Fi speaker, a battery speaker to carry; a speaker with a voice assistant → Smart speakers & displays.',[sb,wf,pb],
   )]))
# ---- 3 Turntables
gram=K('Gramophone and phonograph',s=WIKI+'Phonograph',d='Acoustic or early electric record player that plays wax cylinders or shellac discs through a horn, from Edison\'s phonograph to the wind-up gramophone.',
 tt=[['Medium',['Wax cylinder','Shellac disc']],['Sound path',['External horn','Internal horn in a cabinet']],['Power',['Hand-wound spring motor','Electric']]],a='phonograph · gramophone · wind-up gramophone · Victrola',
 xadd=[ARCH('Victor Victrola','Victor\'s cabinet gramophone with the horn hidden inside, sold as a piece of furniture; electrical Orthophonic models followed in 1925.','Victor Talking Machine Company','',WIKI+'Victrola',
   v=[{'n':'Orthophonic Victrola','mk':'Victor Talking Machine Company','y':'1925','d':'played the new electrically recorded discs'}])],
 see=[['F1','78 rpm record','the discs it plays'],['F1','Cylinder record','the cylinders it plays']])
aio=K('All-in-one record player',s=WIKI+'Phonograph',d='Complete electric record player with built-in speakers, in a suitcase, console or compact case, needing no separate amplifier.',
 tt=[['Form',['Suitcase','Console cabinet','Compact radio-style']],['Features',['Built-in speakers','Bluetooth','USB recording']]],a='record player · portable record player · suitcase turntable',
 xadd=[ARCH('Philco TPA-1','Early all-transistor portable record player for 45 rpm discs.','Philco','1955',WIKI+'Phonograph')],
 see=[['D3','Radiogram','a record player in a furniture cabinet with a radio']])
tt_=K('Turntable',d='Record-playing deck with platter and tonearm, sold without amplifier or speakers.',
 tt=[['Drive',['Belt drive','Direct drive','Idler drive']],['Arm',['Pivoted','Tangential','Detachable']],['Operation',['Manual','Semi-automatic','Fully automatic','Record changer']],['Built-in extras',['Phono stage','USB output','Bluetooth']]],
 demote=[],see=[['E3','DJ turntable','a direct-drive deck built for mixing']])
arm=K('Tonearm',d='Arm that carries the cartridge across the record, sold separately for a turntable.',tt=[['Geometry',['Pivoted','Unipivot','Linear tracking']],['Length',['9-inch','10-inch','12-inch']]])
hs=K('Headshell',s=WIKI+'Phonograph',d='Removable carrier at the end of the tonearm that holds the cartridge.',tt=[['Fitting',['Standard four-pin','SME bayonet','Cartridge-integrated']],['Material',['Aluminium','Magnesium','Wood','Carbon']]])
pl=K('Turntable plinth',d='Base or chassis made to hold one turntable mechanism and its tonearm, sold separately.',tt=[['Material',['Solid wood','Slate','Layered or composite']],['Made for',['Idler decks (Garrard, Lenco)','Belt-drive decks']]])
cart=K('Phono cartridge',d='Pickup cartridge made to fit a turntable tonearm.',tt=[['Generator',['Moving magnet','Moving coil','Moving iron']],['Mount',['Half-inch standard','P-mount','Headshell-integrated']],['Use',['Hi-fi','DJ']]],
 demote=['Koetsu','Lyra moving coil'],see=[['E3','DJ cartridge','a cartridge built for scratching and cueing']])
sty=K('Turntable stylus',d='Replacement stylus made for a phono cartridge.',tt=[['Shape',['Spherical','Elliptical','Shibata','Microline','Van den Hul']],['Groove',['Stereo microgroove','78 rpm']]])
ph=K('Phono preamplifier',d='Stage that raises and equalises a phono cartridge signal to line level.',tt=[['Cartridge',['Moving magnet','Moving coil','Both']],['Circuit',['Valve','Solid-state']],['Power',['Built into amplifier','Mains box','Battery']]],a='phono stage')
rcm=K('Record cleaning machine',d='Machine that washes vinyl records and removes the fluid, by vacuum or ultrasonic bath.',tt=[['Method',['Vacuum','Ultrasonic','Manual bath']]])
depts.append(D('Turntables & vinyl playback','variety','Turntable, tonearm, cartridge and phono stage kept together as the vinyl chain.',
 'Gear for playing vinyl and shellac records, from the player to the pickup and the stage after it; the records themselves → F1; a DJ deck → E3.',
 'Which link in the record-playing chain is it: the player, the arm, the pickup or the stage after it?',[
 S('Record players & turntables','Machines that spin a record and track the groove, from acoustic gramophones and all-in-one players to hi-fi turntable decks; the radio-and-record cabinet → Radios & music systems.',[gram,aio,tt_],
   'kinds from the earliest to the hi-fi separate: acoustic machine, all-in-one electric player, turntable deck'),
 S('Arms, headshells & plinths','Parts that carry the cartridge or hold the deck, sold for upgrades: tonearms, headshells and plinths; the cartridge itself → Cartridges & styli.',[pl,arm,hs],
   'kinds from the base up to the pickup: plinth, arm, headshell'),
 S('Cartridges & styli','The pickup that reads the groove and the tip that wears out: moving-magnet and moving-coil cartridges, and replacement styli.',[cart,sty]),
 S('Phono stages & record care','What happens to the signal and the record around the deck: phono preamplifiers and record-cleaning machines.',[ph,rcm])]))
# ---- 4 Amplifiers
rec=K('Stereo receiver',d='Stereo amplifier with a built-in radio tuner.',tt=[['Era',['Vintage analogue','Current']],['Features',['Network streaming','Bluetooth','Phono input']]],demote=[])
ia=K('Integrated amplifier',d='Stereo amplifier with preamplifier and power stage in one box.',tt=[['Output stage',['Valve','Solid-state','Hybrid valve and solid-state']],['Class',['Class A','Class AB','Class D']],['Built-in inputs',['Analogue only','DAC or streaming','Phono']]],
 see=[['D3','Stereo receiver','the same amplifier with a radio tuner added']])
pre=K('Preamplifier',d='Control and switching stage that feeds a separate power amplifier.',tt=[['Circuit',['Valve','Solid-state']],['Inputs',['Line-level only','With phono stage','With DAC']]],demote=['Quad control units','Naim NAC preamplifiers'])
pa=K('Power amplifier',d='Amplifier stage that drives speakers from a preamplifier signal, stereo or one channel per box.',tt=[['Layout',['Stereo','Monoblock']],['Circuit',['Valve','Solid-state']],['Class',['Class A','Class AB','Class D']]],demote=['Quad current-dumping amplifiers'])
eq=K('Equaliser',d='Stereo component for shaping the tone or sound field of a signal.',tt=[['Control',['Graphic','Parametric']],['Form',['Hardware component','Digital sound processor']]])
dh=K('DAC and headphone amplifier',d='External device that converts digital audio and drives headphones in one unit.',tt=[['Form',['Desktop','Portable with battery','USB dongle','Bluetooth receiver']]])
dac=K('DAC',d='External device whose designed function is converting digital audio to analogue.',tt=[['Conversion',['R-2R multibit','Delta-sigma','FPGA']],['Output stage',['Solid-state','Valve']],['Extras',['With preamplifier','External master clock input']]])
ha=K('Headphone amplifier',d='External device whose designed function is amplifying a headphone signal.',tt=[['Circuit',['Solid-state','Valve','Hybrid','OTL valve']],['Output',['Single-ended','Balanced']],['Form',['Desktop','Portable']]])
bt=K('Bluetooth audio adapter',d='External unit that sends audio from a TV or player to wireless headphones or speakers, or receives Bluetooth audio into a hi-fi.',tt=[['Direction',['Transmitter','Receiver','Both']]],s=old['Bluetooth audio adapter']['s'])
avr=K('AV receiver',d='Multichannel amplifier with surround decoding, video switching and a tuner in one box.',tt=[['Channels',['5.1','7.2','9.2','11.2']],['Surround formats',['Dolby Atmos','DTS:X']],['HDMI',['4K passthrough','8K passthrough']]])
avp=K('AV processor',d='Multichannel surround preamplifier and decoder that feeds separate power amplifiers.',tt=[['Type',['Surround processor','Video processor']],['Channels',['Up to 11','16','32']]],see=[['D3','AV receiver','the same decoding with amplifiers built in']])
depts.append(D('Amplifiers & electronics','mixed','Variety for stereo hi-fi including vintage; tier for AV gear.',
 'Boxes that amplify, convert or decode sound for speakers and headphones; an instrument amplifier → E3; a set with speakers built in → Radios & music systems.',
 'What does the box do to the signal: amplify it for speakers, convert digital audio for headphones, or decode it for surround?',[
 S('Stereo amplifiers & receivers','Two-channel amplifiers from all-in-one receivers to separate preamplifier and power stages, such as the Marantz 2270, Quad II and McIntosh MC275; a surround amplifier → Home cinema electronics.',[rec,ia,pre,pa,eq],
   'kinds by how many stages share a box: tuner, preamplifier and power together; preamplifier and power; each alone; tone shaping'),
 S('DACs & headphone amplifiers','Boxes that turn digital audio into analogue and drive headphones, such as the Chord Mojo and Schiit Bifrost; a headphone or earphone → Headphones & earphones.',[dac,dh,ha,bt],
   'kinds by what the box does: convert only, convert and drive headphones, drive headphones only, bridge to wireless'),
 S('Home cinema electronics','Boxes that decode and amplify surround sound and switch video, such as the Denon AVR-X range and Trinnov Altitude; a stereo amplifier → Stereo amplifiers & receivers.',[avr,avp])]))
# ---- 5 Hi-fi sources
reel=K('Reel-to-reel tape deck',d='Hi-fi component that plays and records open-reel magnetic tape.',tt=[['Track format',['Quarter-track','Half-track']],['Reel size',['7-inch','10.5-inch']],['Speed',['3¾ ips','7½ ips','15 ips']],['Circuit',['Valve','Solid-state']]],demote=['Tandberg tape recorders'])
e8=K('8-track player',d='Home component that plays (and may record) 8-track tape cartridges; an 8-track player fitted in a car is in Vehicles.',tt=[['Function',['Player','Recorder']],['Sound',['Stereo','Quadraphonic']]],see=[['F1','Tape cartridge (4- and 8-track)','the cartridges it plays']])
cas=K('Cassette deck',d='Hi-fi component that plays and records compact cassettes.',tt=[['Heads',['Two-head','Three-head']],['Direction',['Single direction','Auto-reverse']],['Transport',['Single cassette','Dual cassette']],['Noise reduction',['Dolby B, C or S','dbx']]],see=[['F1','Compact cassette','the cassettes it plays']])
dat=K('DAT deck',d='Hi-fi component that plays and records digital audio tape (DAT) cassettes.',tt=[['Use',['Home hi-fi','Studio']]])
cd=K('CD player',d='Player for compact discs.',tt=[['Discs',['CD only','SACD and CD']],['Form',['Complete player','Transport only','Multi-disc changer']],['Inputs',['With DAC inputs','Without']]],demote=['Quad CD players'])
md=K('MiniDisc deck',d='Hi-fi component that plays and records MiniDiscs.',tt=[['Recording format',['ATRAC','MDLP','Hi-MD']]])
cdr=K('CD recorder',s=WIKI+'Hi-fi',d='Hi-fi component that records audio onto recordable compact discs from other sources.',tt=[['Disc',['CD-R','CD-RW']]],a='CD burner deck')
ns=K('Network streamer',d='Hi-fi source that plays music from the network or streaming services into an audio system.',tt=[['Built-in functions',['Streamer only','DAC','Preamplifier','Storage (music server)']]],see=[['I3','Music streaming','the service it plays']])
tun=K('FM/DAB tuner',d='Hi-fi separate that receives radio broadcasts for an amplifier, with no speaker of its own.',tt=[['Band',['FM','AM and FM','DAB and DAB+','Internet radio']]])
depts.append(D('Hi-fi sources: tape, disc & streaming','mixed','Variety for tape and vintage decks (period view); tier for modern disc and streaming sources.',
 'Hi-fi components that read tape, discs or a network stream and send the signal to an amplifier; the media themselves → F1; a record deck → Turntables & vinyl playback.',
 'What carries the music into the system: tape, a disc, or a network or radio signal?',[
 S('Tape decks','Components that play and record magnetic tape, from open reel to cassette to digital tape, such as the Revox A77, Nakamichi Dragon and Sony DTC-60ES.',[reel,e8,cas,dat],
   'kinds by tape format, from open reel to cartridge to cassette to digital tape'),
 S('Disc players','Components that play or record optical and magneto-optical discs, such as the Sony CDP-101 and Sony MDS-JE780.',[cd,md,cdr]),
 S('Network & broadcast sources','Components that take the music from the internet, the home network or the air, such as the Linn DS and Quad FM3.',[ns,tun])]))
# ---- 6 Portable audio
pc=K('Portable cassette player',d='Battery-powered personal player for compact cassettes, listened to through headphones; hi-fi tape decks are a separate kind.',tt=[['Function',['Playback only','Recorder']],['Extras',['Radio','Auto-reverse']]])
pcd=K('Portable CD player',d='Battery-powered personal player for compact discs, listened to through headphones; hi-fi CD players are a separate kind.',tt=[['Features',['Anti-skip','MP3 or ATRAC playback']],['Disc',['Audio CD','Video CD']]])
pmd=K('Portable MiniDisc player',d='Battery-powered personal player or recorder for MiniDisc, a rewritable magneto-optical disc format sold 1992–2013.',tt=[['Function',['Player','Recorder']],['Format',['Standard MiniDisc','NetMD','Hi-MD']]])
mp3=K('MP3 player',d='Portable device sold mainly to play stored or streamed music, with no calling.',tt=[['Storage',['Flash memory','Hard drive']],['Class',['Pocket MP3 player','Hi-res player','Android player']]],
 demote=['Astell&Kern players','FiiO X and M series','Shanling M series'],
 xadd=[ARCH('MPMan F10','First flash-memory MP3 player, sold in South Korea from 1998 and in North America as the EigerMan.','SaeHan Information Systems','1997',WIKI+'Digital_audio_player'),
       ARCH('Compaq Personal Jukebox','First hard-drive MP3 player, developed by Hango Electronics and sold by Compaq.','Compaq','1999',WIKI+'Digital_audio_player'),
       ARCH('Archos Jukebox 6000','Hard-drive MP3 player that rivalled the Creative Nomad Jukebox.','Archos','2000',WIKI+'Digital_audio_player')])
pmp=K('Portable media player',s=WIKI+'Digital_audio_player',d='Pocket device that plays video and photos as well as music from its own storage, without calling.',tt=[['Storage',['Hard drive','Flash memory']],['Media',['Music and video','Music, video and photos']]],a='PMP · MP4 player',
 xadd=[ARCH('Archos Jukebox Multimedia','The first portable media player, with a colour screen for video.','Archos','2002',WIKI+'Digital_audio_player')])
bb=K('Boombox',d='Portable radio-cassette or CD system with built-in speakers and a carry handle.',tt=[['Media',['Radio-cassette','Double cassette','CD']],['Wireless',['Bluetooth','DAB']]],demote=['Sony CD boombox'])
depts.append(D('Portable audio','variety','Personal players with a strong collector following, plus portable radio-cassettes.',
 'Battery-powered players you carry: headphone players from the Walkman to the iPod, and boomboxes with speakers; a speaker without a player → Loudspeakers; a phone → D2.',
 'Is the music heard through headphones or through speakers built into the unit?',[
 S('Headphone players','Pocket players made for headphones, such as the Sony Walkman, Discman, MiniDisc Walkman and Apple iPod; a boombox with speakers → Boombox shelf.',[pc,pcd,pmd,mp3,pmp],
   'kinds by what holds the music: cassette, compact disc, MiniDisc, memory, memory with a video screen'),
 S('Boomboxes','Carry-handle systems with their own speakers, such as the Philips Radiorecorder and JVC RC-M90; a Bluetooth speaker with no player → Soundbars & wireless speakers.',[bb])]))
# ---- 7 Radios
tabr=K('Radio',new='Table radio',d='Mains or battery radio with a built-in speaker, made to stand on a shelf or table.',m=[e for e in rd['m'] if e[0] in RD_TAB],r=rd.get('r'),
 tt=[['Band',['FM','AM','AM and FM','DAB and DAB+','Internet radio']],['Power',['Mains','Battery']],['Technology',['Valve','Transistor','Digital']]],
 xdrop=['Regency TR-1','Sony TR-55','Braun T 3'],a='tabletop radio · valve radio · DAB radio')
porr=K('Portable radio',s=rd['s'],d='Radio small enough to carry, battery or solar powered, from pocket transistor sets to rugged outdoor and emergency radios.',m=[e for e in rd['m'] if e[0] in RD_POR],
 tt=[['Band',['AM','FM','DAB']],['Power',['Battery','Solar or wind-up','Rechargeable']],['Size',['Pocket','Mid-size']]],a='transistor radio · pocket radio',
 xadd=[x for x in rd['x'] if x['n'] in ('Regency TR-1','Sony TR-55','Braun T 3')])
tabr['x']=[x for x in tabr['x'] if x['n'] in ('Ekco AD-65','Philips Bi-Ampli','Roberts R200 / Revival','Tivoli Audio Model One')]
if not tabr.get('r'): tabr.pop('r',None)
assert len(tabr['x'])==4
renames['Radio']='Table radio'
clk=K('Clock radio',d='Radio combined with a clock and alarm, for the bedside.',tt=[['Band',['FM','DAB']],['Clock display',['Standard','Projection']],['Extras',['Bluetooth','USB charging']]])
sw=K('Shortwave and world-band receiver',d='Receiver covering the shortwave bands to hear international and distant broadcasts, often with SSB and synchronous detection.',tt=[['Form',['Portable','Tabletop']],['Reception',['SSB','Synchronous detection','Airband']]],see=[['D2','Radio scanner','a receiver for listening to services rather than broadcasts']])
xtal=K('Crystal radio',s=WIKI+'Crystal_radio',d='Unpowered radio that runs on the energy of the signal it receives through a crystal detector, sold ready-made or as a kit.',tt=[['Build',['Ready-made set','Kit']],['Detector',['Cat\'s whisker','Germanium diode']]],a='crystal set · cat\'s whisker radio')
rg=K('Radiogram',d='Furniture-style cabinet combining a radio and a record player with speakers.',tt=[['Form',['Console','Table-top','Portable']],['Circuit',['Valve','Transistor']]],demote=['Braun radio-phonographs'],see=[['D3','All-in-one record player','a record player with no radio or cabinet']])
jb=K('Jukebox',d='Machine that plays a record or track chosen from a menu, coin-operated or for home use.',tt=[['Media',['78 rpm','45 rpm','CD','Digital']],['Form',['Floor-standing','Countertop','Wallbox']]],demote=['Rock-Ola jukeboxes'])
chs=K('Compact hi-fi system',d='Music system with source, amplifier and speakers sold together as one unit.',tt=[['Size',['Micro','Mini','Midi','Music centre']],['Sources',['CD','Network','Cassette','Turntable']]])
kar=K('Karaoke machine',d='Machine that plays music for singing along, with microphone inputs.',tt=[['Form',['Portable','Party speaker','TV-connected']]],see=[['E3','Dynamic microphone','the microphone it is sung into']])
depts.append(D('Radios & music systems','mixed','Variety for vintage radios, radiograms and jukeboxes; tier for everyday radios and compact systems.',
 'Sets that receive broadcasts, and cabinet, coin or shelf machines that play recorded music; a hi-fi tuner → Hi-fi sources; two-way and amateur radio → D2.',
 'Does it only receive broadcasts, or does it also play recorded music?',[
 S('Radios','Broadcast receivers with a built-in speaker, from valve table sets and transistor portables to shortwave and crystal radios.',[tabr,porr,clk,sw,xtal],
   'kinds from everyday to specialist listening: table, carried, bedside, long-distance, unpowered'),
 S('Music systems, radiograms & jukeboxes','Machines that play recorded music with their own speakers, from furniture radiograms to coin jukeboxes and shelf systems; a hi-fi separate → Amplifiers & electronics.',[rg,jb,chs,kar],
   'kinds from furniture to coin machine to shelf unit to party use')]))
# ---- 8 TVs
tv=K('Television',d='Screen sold with television reception or as a television, of any display technology.',tt=[['Panel',['OLED','QD-OLED','Mini-LED LCD','QLED','LED-LCD','RGB Mini-LED']],['Size',['32–43 in','50–65 in','75 in and up']],['Resolution',['Full HD','4K','8K']]],see=[['D1','TV tuner card','a tuner for a computer']])
rpt=K('Rear-projection television',d='Television whose picture is projected onto the screen from inside its cabinet.',tt=[['Imaging',['CRT','DLP','LCD or LCoS']]])
crt=K('CRT television and video monitor',d='Television or video monitor with a cathode-ray tube, now collected for design and for retro gaming.',tt=[['Colour',['Colour','Black-and-white']],['Form',['Portable','Console','Flat-screen CRT']],['Role',['Domestic television','Professional monitor']]])
pj=K('Projector',d='Projector that throws a picture from a video or computer signal onto a screen or wall from a distance.',tt=[['Light source',['Lamp','LED','Laser']],['Imaging',['DLP','LCD','LCoS']],['Use',['Home cinema','Portable','Gaming']]],see=[['D3','Projector screen','the surface it throws onto']])
ust=K('Ultra-short-throw projector',d='Projector made to sit at the wall just below the image it throws.',tt=[['Light source',['Laser','LED']],['Resolution',['1080p','4K']]])
sl=K('Slide projector',d='Projector that shows 35 mm photographic slides from a tray or magazine.',tt=[['Magazine',['Rotary tray','Straight tray']],['Lenses',['Single lens','Twin lens dissolve']]])
cine=K('Cine film projector',d='Projector that shows motion-picture film at home.',tt=[['Film gauge',['Super 8','8 mm','Single 8','9.5 mm','16 mm']],['Sound',['Silent','Magnetic sound']]],demote=['Elmo projectors','Eumig Super 8 projectors'])
stick=K('Streaming stick or box',d='Stick or box that plays streamed video and audio on a television.',tt=[['Form',['Stick','Box']],['Maximum picture',['HD','4K HDR','4K Dolby Vision']]],see=[['I3','Video streaming service','the service it plays']])
stb=K('Set-top box',d='Box that receives broadcast television for a screen, often with a recorder.',tt=[['Reception',['Terrestrial (Freeview, ATSC)','Satellite','Cable']],['Recording',['Without','With recorder (PVR)']]])
bd=K('Blu-ray and DVD player',d='Player or recorder for DVD, Blu-ray and 4K Ultra HD Blu-ray discs.',tt=[['Disc',['DVD','Blu-ray','4K Ultra HD Blu-ray','Universal (SACD, DVD-Audio)','Video CD']],['Function',['Player','Recorder']]])
ms=K('Movie server',d='Box that stores a library of films and plays them on a television or projector.',tt=[['Build',['Player with storage','Player with separate server']]])
ld=K('LaserDisc player',d='Player for LaserDisc, the 30 cm analogue video disc sold from 1978, often combined with CD or DVD.',tt=[['Combination',['LaserDisc only','LaserDisc and CD','LaserDisc and DVD']],['Disc system',['LaserDisc','MUSE Hi-Vision','CED videodisc']]],demote=['Pioneer LaserDisc players'])
vcr=K('Video cassette recorder',d='Machine that records and plays television on videotape cassettes.',tt=[['Format',['VHS','S-VHS','VHS-C','Betamax','Video 2000','Philips VCR','U-matic']],['Audio',['Mono','Hi-fi stereo']]],
 xadd=[ARCH('Sony U-matic','The first commercial videocassette format, introduced in Tokyo.','Sony','1971',WIKI+'Videocassette_recorder')],
 see=[['F1','VHS cassette','the tapes it plays'],['F1','Betamax cassette','the rival format']])
scr=K('Projector screen',s=HOME,d='Surface made to receive a projected picture, on a fixed frame, a pull-down roller or a motorised drop.',tt=[['Mounting',['Fixed frame','Pull-down','Motorised','Floor-rising']],['Surface',['Matte white','Grey','Ambient-light-rejecting']]],see=[['G3','Motorised TV lift and projection screen','the built-in motorised version']])
depts.append(D('TVs, projectors & video players','mixed','Tier for current TVs, projectors and streamers; variety for CRT, vintage projection and obsolete video formats.',
 'Screens, projectors and the boxes that feed them; a computer monitor → D1; a camera → D4; the discs and tapes themselves → F1.',
 'Does it show the picture, throw it onto a surface, or supply the picture to a screen?',[
 S('Televisions','Screens with a tuner or smart platform, from current OLED and LED sets back through rear-projection to cathode-ray tubes such as the Sony Trinitron and Braun HF 1; a computer monitor → D1.',[tv,rpt,crt],
   'kinds from current flat panels back through projection sets to cathode-ray tubes'),
 S('Projectors','Machines that throw a picture onto a wall or screen, from home video projectors to slide and cine projectors such as the Kodak Carousel; the screen → Stands, cables & accessories.',[pj,ust,sl,cine],
   'kinds by what is projected: a video signal from a distance, a video signal from the wall, slides, film'),
 S('Video players & streaming boxes','Sources that feed a screen: streaming boxes, set-top boxes, disc players, film servers and obsolete tape and disc formats such as VHS, Betamax and LaserDisc.',[stick,stb,bd,ms,ld,vcr],
   'kinds by where the picture comes from: the internet, an aerial or dish, a disc, a stored library, then obsolete disc and tape')]))
# ---- 9 Smart
sp=K('Smart speaker',d='Speaker whose designed function is a voice assistant.',tt=[['Voice assistant',['Alexa','Google Assistant','Siri']],['Size',['Compact','Full-size']]],see=[['D3','Wi-Fi and multi-room speakers','a streaming speaker without an assistant']])
sd=K('Smart display',d='Voice-assistant device with a screen.',tt=[['Voice assistant',['Alexa','Google Assistant']],['Screen size',['5–8 in','10 in','15 in and over']]])
hub=K('Smart-home hub',d='Device that links and controls smart-home devices.',tt=[['Protocol',['Zigbee','Z-Wave','Thread and Matter','Wi-Fi']]])
depts.append(D('Smart speakers & displays','tier',None,
 'Speakers, screens and hubs run by a voice assistant; a Wi-Fi or Bluetooth speaker without one → Loudspeakers; a smartphone → D2.',
 'Does the device listen and speak, show a screen, or link other devices?',[
 S('Smart speakers & displays','Assistant devices for the home, such as the Amazon Echo, Apple HomePod and Google Nest Hub; a plain streaming speaker → Soundbars & wireless speakers.',[sp,sd,hub])]))
# ---- 10 Accessories
tvm=K('TV and speaker stands and mounts',new='TV stand and wall mount',d='Stand, bracket or arm made to hold a TV on a wall, table or floor.',tt=[['Wall mount',['Fixed','Tilting','Full-motion']],['Stand',['Table stand','Floor stand']]],a='TV bracket · TV mount',s=old['TV and speaker stands and mounts'].get('s') or '')
sst=K('Speaker stand and bracket',s=old['TV and speaker stands and mounts'].get('s') or '',d='Stand or bracket made to hold a speaker at ear height, on the floor, desk or wall.',tt=[['Form',['Floor stand','Desk stand','Wall bracket']],['Fill',['Sand-fillable','Hollow']]])
renames['TV and speaker stands and mounts']='TV stand and wall mount'
ant=K('TV antenna',d='Aerial made to receive broadcast television for a TV or receiver.',tt=[['Placement',['Indoor','Outdoor','Attic']],['Signal',['Passive','Amplified']]])
rem=K('Remote control',d='Remote made for one TV or audio system; a universal remote is listed here too.',tt=[['Scope',['Made for one model','Universal','Learning']]])
psc=scr
psc=None
cab=K('Audio cable',d='Audio cable with standard connectors for hi-fi, speakers and TV sound.',tt=[['Cable type',['Speaker cable','RCA interconnect','Balanced XLR','Optical (Toslink)','Digital coaxial','Subwoofer cable']]],s=WIKI+'Hi-fi')
spare=K('Headphone & earbud spare parts',d='Replacement part made for one headphone or earbud model, such as ear pads or tips.',tt=[['Part',['Ear pads','Ear tips','Replacement charging case','Headband pad','Stand or hanger']]])
hcab=K('Headphone cable',d='Cable made for one headphone model; standard-connector cables are in Computers.',tt=[['Plug',['3.5 mm','2.5 mm balanced','4.4 mm balanced','4-pin XLR']],['Headphone end',['Mini-XLR','Two-pin','MMCX','Proprietary']]],s=old['Headphone cable'].get('s') or '')
for k in (hcab,sst,tvm):
    if not k['s']: k['s']=WIKI+'Hi-fi'
depts.append(D('Stands, cables & accessories','tier',None,
 'Things made to go with other audio and video gear: stands, mounts, antennas, remotes, cables and headphone parts; a built-in motorised screen or speaker → G3.',
 'What is the accessory made for: a screen, a speaker or hi-fi system, or headphones?',[
 S('For screens','Things that hold, feed or control a TV: stands and wall mounts, aerials and remote controls; the projector screen is on the Projectors shelf.',[tvm,ant,rem]),
 S('For speakers & hi-fi','Things that carry or connect speakers and hi-fi components: stands, brackets and audio cables.',[sst,cab]),
 S('For headphones','Spare parts and cables made for headphones and earbuds, such as ear pads, tips and detachable cables.',[spare,hcab])]))
# move Projector screen into Projectors shelf? keep as kind in TV dept shelf Projectors
for dp in depts:
    for s in dp['s']:
        if s['n']=='Projectors': s['k'].append(scr)
        if s['n']=='Projectors': s['t']='Machines that throw a picture onto a wall or screen, and the screens they throw onto, such as the Kodak Carousel slide projector; a built-in motorised screen → G3.'
# fix accessories shelf text mention
for dp in depts:
    for s in dp['s']:
        if s['n']=='For screens': s['t']='Things that hold, feed or control a TV: stands and wall mounts, aerials and remote controls; a projector screen → Projectors shelf.'
# projectors ax now includes screen
for dp in depts:
    for s in dp['s']:
        if s['n']=='Projectors': s['ax']='kinds by what is projected: a video signal from a distance, a video signal from the wall, slides, film; then the screen'
missing=set(old)-used
print('unused old kinds:',missing)
assert not missing
out=copy.deepcopy(src)
out['depts']=depts
out['ax']='What does the equipment do for sound or picture: go on the ear, fill a room, play records, amplify, feed a hi-fi, travel with you, receive broadcasts, show a picture, answer a voice, or support the rest?'
out['key']=[
 '1. Is it a stand, mount, cable, aerial, remote or spare part made for other audio or video gear? → Stands, cables & accessories',
 '2. Is it worn on or in the ears? → Headphones & earphones',
 '3. Is it a speaker, screen or hub run by a voice assistant? → Smart speakers & displays',
 '4. Does it show a picture, throw one onto a surface, or feed one to a screen? → TVs, projectors & video players',
 '5. Does it play records or belong to the record-playing chain (deck, arm, pickup, phono stage, record cleaner)? → Turntables & vinyl playback',
 '6. Is it a battery player you carry, or a boombox with its own speakers? → Portable audio',
 '7. Does it receive broadcasts with its own speaker, or play records, discs or coins from a cabinet or shelf system? → Radios & music systems',
 '8. Is it a box that amplifies, converts or decodes sound for speakers or headphones? → Amplifiers & electronics',
 '9. Is it a component that reads tape, a disc or a network stream and sends it to an amplifier? → Hi-fi sources: tape, disc & streaming',
 '10. Is it a speaker, soundbar or subwoofer? → Loudspeakers',
 '<i>Precedence: a smart speaker is step 3 before a loudspeaker (step 10); a boombox or radio-cassette is step 6 before a loudspeaker; a receiver with a tuner is step 8, a stand-alone tuner step 9; a radiogram is step 7 before a turntable (step 5).</i>']
out['lead']='Home and personal audio and video equipment, organised by what it does for sound or picture (headphones, speakers, record playing, amplifying, sources, portable players, radios, screens, smart speakers, accessories); enthusiast areas are broken into archetypes and versions, everyday screens and smart devices by what makes a good one.'
json.dump(out,open(R+'/work/STR_D3/D3.new.json','w'),ensure_ascii=False,indent=1)
json.dump(renames,open(R+'/work/STR_D3/renames.json','w'),ensure_ascii=False,indent=1)
print(len(renames),renames)
