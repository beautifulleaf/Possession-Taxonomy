import json,os,sys,copy
sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
from tt import TT
R='/home/user/Possession-Taxonomy/rebuild/'
d=json.load(open(R+'work/STR_I1/bak/I1.json'))
TT['3D modelling software']=TT['3D modelling software'][:2]
TT['Stop-motion software']=[["Form",["Professional frame capture","Phone app"]],["Subject",["Brickfilm","Puppets and clay"]]]
TT['Home publishing software']=TT['Home publishing software'][:1]
K={}
for dp in d['depts']:
    for s in dp['s']:
        for k in s['k']: K[k['n']]=k
before=(len(d['depts']),sum(len(s['k']) for dp in d['depts'] for s in dp['s']),sum(len(k.get('x',[])) for k in K.values()))
before_sh=sum(len(dp['s']) for dp in d['depts'])
W='https://en.wikipedia.org/wiki/'
def nk(n,dfn,s,a='',m=None):
    k={'n':n,'a':a,'d':dfn,'s':s}
    if m: k['m']=m
    K[n]=k
def take(frm,names):
    out=[]
    m=K[frm].get('m',[])
    for n in names:
        for x in list(m):
            if x[0]==n: out.append(x); m.remove(x)
    return out
nk('Word processor','Program for writing, formatting and printing text documents, sold alone or inside an office suite; a bundle of several programs → Office suite.',W+'Word_processor',m=take('Office suite',['Microsoft Word','Pages','Google Docs']))
nk('Spreadsheet program','Program for calculating and analysing data laid out in rows and columns; the same product may also come inside an office suite → Office suite.',W+'Spreadsheet',m=take('Office suite',['Microsoft Excel','Numbers','Google Sheets']))
nk('Presentation program','Program for building and showing slides; the same product may also come inside an office suite → Office suite.',W+'Presentation_program',m=take('Office suite',['Microsoft PowerPoint','Apple Keynote','Google Slides']))
nk('Screenshot tool','Program that captures still images of the screen, often with markup; a tool that records moving video → Screen recorder and streaming software.',W+'Screenshot',m=take('Screen recorder and streaming software',['Snipping Tool','Snagit','Greenshot'])+[['ShareX','']])
nk('Feed reader','Program or web service that gathers new posts from chosen sites and podcasts into one list.',W+'News_aggregator','news reader · RSS reader')
nk('Authenticator app','App that makes the one-time codes used as a second step when logging in; a stored-password app → Password manager.',W+'Google_Authenticator','two-factor app · 2FA app')
nk('CD ripper','Program that copies audio from compact discs into digital files, with optional error checking and tagging.',W+'List_of_music_software','')
nk('Clipboard manager','Program that keeps a history of copied text, images and files and pastes them again.',W+'Utility_software')
nk('Disk space analyser','Program that shows what is using a drive\'s space, as lists or treemaps.',W+'Utility_software','disk usage analyser')
nk('File comparison tool','Program that shows the differences between two files or folders and merges them.',W+'Utility_software','diff tool')
K['Office suite']['a']='office bundle'
# demotions / renames of archetypes
def arch(kn,name): 
    for a in K[kn]['x']:
        if a['n']==name: return a
def demote(kn,name,rng=None):
    k=K[kn]; a=arch(kn,name); k['x'].remove(a)
    m=k.setdefault('m',[])
    have={x[0] for x in m}
    for v in a.get('v',[]):
        if v['n'] not in have: m.append([v['n'],v.get('mk') or a.get('mk') or '']); have.add(v['n'])
    if rng: k.setdefault('r',[]).append(rng)
    return a
def ren(kn,old,new,dsc=None,mk=None,y=None):
    a=arch(kn,old); a['n']=new
    if dsc: a['d']=dsc
    if mk is not None: a['mk']=mk
    if y: a['y']=y
LD='Linux distribution'
ren(LD,'Debian lineage','Debian','The Debian Project\'s volunteer-built distribution, the base of Ubuntu, Mint and many others.')
ren(LD,'Red Hat and Fedora lineage','Fedora','Fedora, the community distribution sponsored by Red Hat, and the RPM-based systems built from it or from Red Hat Enterprise Linux.')
ren(LD,'Arch lineage','Arch Linux','Rolling-release distribution using the pacman package manager, and the systems built on it.')
ren(LD,'openSUSE lineage','openSUSE','The community distribution from the openSUSE Project and systems built on it.')
ren(LD,'Mandriva lineage','Mandrake Linux','The Mandrake and Mandriva line, now kept going by community projects.')
ren(LD,'Slackware lineage','Slackware','One of the oldest distributions, kept deliberately simple, and its derivatives.')
ren(LD,'Gentoo lineage','Gentoo Linux','Distribution that builds its software from source, and its derivatives.')
AH='Alternative & hobby operating system'
ren(AH,'FreeBSD and desktop BSDs','FreeBSD','Unix descended from Berkeley BSD, first released in 1993, with desktop-oriented derivatives.')
ren(AH,'OS/2 continuations','OS/2','IBM\'s operating system, first released in December 1987 with Microsoft, continued by ArcaOS and, earlier, eComStation.',mk='IBM',y='1987')
arch(AH,'OS/2')['s']=W+'OS/2'
ren(AH,'AmigaOS and descendants','AmigaOS','The Amiga computer\'s operating system, first released in 1985, continued by AmigaOS 4 and MorphOS.',mk='Commodore International',y='1985')
arch(AH,'AmigaOS')['s']=W+'AmigaOS'
a=arch('3D printing slicer','Slic3r lineage'); a['n']='Slic3r'; a['d']='Open-source slicer started in 2011 in the RepRap community; PrusaSlicer, Bambu Studio and OrcaSlicer descend from it.'; a['mk']='Alessandro Ranellucci'
ren('Peer-to-peer file sharing client','eDonkey and eMule','eDonkey2000','Network and client launched in September 2000; eMule, released in 2002, became its most popular client.',mk='MetaMachine')
demote('Game mod manager','Minecraft mod platforms')
demote('Screen saver','Windows built-in savers')
demote('Peer-to-peer file sharing client','Gnutella clients')
demote('Peer-to-peer file sharing client','Direct Connect clients')
demote('Home & garden design software','Vegetable garden planners')
demote('Code editor plug-in','Visual Studio Code extensions')
demote('Code editor plug-in','JetBrains Marketplace plug-ins')
demote('Amp & cabinet simulator','Neural DSP plug-ins',['Neural DSP amp plug-ins','Neural DSP'])
demote('Reverb plug-in','Valhalla reverbs',['ValhallaDSP reverbs','ValhallaDSP'])
demote('Reverb plug-in','Eventide reverbs',['Eventide reverbs','Eventide'])
demote('Delay & modulation plug-in','Valhalla delays',['ValhallaDSP delays','ValhallaDSP'])
demote('Compressor & dynamics plug-in','Tokyo Dawn Labs free dynamics',['Tokyo Dawn free dynamics','Tokyo Dawn Labs'])
demote('Pitch correction & vocal plug-in','Synchro Arts alignment tools',['Synchro Arts alignment tools','Synchro Arts'])
demote('Metering & analysis plug-in','Mastering The Mix metering',['Mastering The Mix meters','Mastering The Mix'])
# ARP 2600 split
ar=arch('Software synthesiser','ARP 2600 and Oberheim classics'); K['Software synthesiser']['x'].remove(ar)
K['Software synthesiser']['x'].append({'n':'ARP 2600','a':'','d':'Semi-modular analogue synthesiser introduced by ARP Instruments in 1971; Arturia models it as a plug-in.','mk':'ARP Instruments','y':'1971','s':W+'ARP_2600','v':[v for v in ar['v'] if v['n']=='ARP2600 V']})
K['Software synthesiser'].setdefault('m',[]).extend([[v['n'],v['mk']] for v in ar['v'] if v['n']!='ARP2600 V'])
# Lexicon split
lx=arch('Reverb plug-in','Lexicon 224 and 480L'); xs=K['Reverb plug-in']['x']; i=xs.index(lx); xs.remove(lx)
v480=[v for v in lx['v'] if v['n'] in('Relab LX480','Valhalla VintageVerb')]
xs[i:i]=[{**lx,'n':'Lexicon 224','d':'Lexicon\'s first digital reverb unit, from 1978.','y':'1978','v':[]},{**lx,'n':'Lexicon 480L','d':'The 224\'s successor of 1986, the studio standard digital reverb.','y':'1986','v':v480}]
# ---------- layout ----------
OSD='Operating systems & system tools'
LAY=[
(OSD,'Programs that run the computer, run other systems on it, look after it and its data, handle its files, or change how it works; a program for a task such as writing or editing images → its own department.','What does the program do for the machine: be its system, run other systems, keep it healthy, protect its data, handle files, or reshape how it works?',[
 ('Operating systems','A complete system that starts the computer and runs programs: Windows, macOS, a Linux distribution or a hobby system; a program run on top of one → the other shelves.','What is the system built from: a mainstream vendor, the Linux kernel, or something else?',['Desktop operating system','Linux distribution','Alternative & hobby operating system']),
 ('Running other systems\' software','Programs that run software made for another system, console or computer: virtual machines, compatibility layers and game emulators; a hosted game service → B9.','How much of the other system is imitated: a whole machine, only its programs, or a game console?',['Virtual machine software','App compatibility layer','Game emulator']),
 ('Cleaning, tuning & repair','Programs that remove clutter, repair or tidy the system and its disks; a copy of the data → Backup & recovery.','What does it fix or tidy: junk files, installed programs, drivers, disk layout, or a mix of small tools?',['PC cleaner','Uninstaller','Driver updater','Disk space analyser','Partition manager','System utility suite']),
 ('Backup & recovery','Programs that copy data to safety, bring lost data back or move a whole setup to a new machine; storing it at a provider → Subscriptions, Memberships & Online Services.','At what point does it act: before data is lost, after it is lost, or when changing machine?',['Backup software','Data recovery software','PC migration software']),
 ('Files, search & access','Programs for working with files and reaching them: managers, archivers, search, disc burning, remote control and home servers.','What is done with the files: browse, pack, find, write to disc, reach from afar or serve to others?',['File manager','File archiver','File comparison tool','Desktop search tool','Disc burning software','Remote desktop software','Home server software']),
 ('Customising & automating','Programs that change how the desktop looks, launches or behaves, or how a game is modded; a theme for a phone → its own device.','What is customised: the launcher, the desktop look, copied text, or a game?',['App launcher','Clipboard manager','Desktop customisation tool','Game mod manager']),
]),
('Security & privacy','Programs that protect the device, family, accounts, connections and stored data; a hardware key or router → Computers & Components.','What is being protected: the device and family, or the accounts, connections and data?',[
 ('Device & family protection','Programs that keep malware out, filter network traffic and limit what children see; sold on their own or inside a security suite.','What is guarded against: malware, unwanted connections or content seen by children?',['Antivirus software','Firewall','Parental controls']),
 ('Accounts, connections & data','Programs that protect logins, network traffic and stored files, or deliberately erase them.','Which part is protected: the login, the connection, or the stored data?',['Password manager','Authenticator app','VPN','Encryption software','Data eraser','Password recovery software']),
]),
('Office & productivity','Suites and single programs for documents, planning, language and household money; a hosted service people pay for monthly → Subscriptions, Memberships & Online Services.','What is the work: writing and reading documents, organising notes and time, language, or money?',[
 ('Documents & forms','Programs that make, read and capture documents: office suites and their single programs, PDF tools, scanned-text recognition, long writing and forms.','What is the document: a text, a sheet, slides, a fixed PDF, a scan, a book or a form?',['Office suite','Word processor','Spreadsheet program','Presentation program','PDF editor','OCR software','Long-form writing app','Survey and form software']),
 ('Notes, plans & time','Programs for jotting, planning, scheduling and drawing ideas.','What is organised: ideas, tasks, dates, time spent or diagrams?',['Note-taking app','Task manager','Calendar app','Time-tracking software','Mind mapping software','Diagramming software']),
 ('Language, typing & voice','Programs for learning, translating, typing and speaking languages.','What does it do with language: teach it, translate it, type it, or turn it into or from speech?',['Language-learning software','Machine translation software','Computer-assisted translation tool','Input method editor','Typing tutor','Dictation software','Text-to-speech software']),
 ('Money, tax & freelance work','Programs for household money, tax returns and a freelancer\'s books.','Whose money is handled: the household\'s, the taxpayer\'s or a business\'s?',['Personal finance manager','Tax software','Accounting software']),
]),
('Internet & AI','Programs to go online, talk to an AI, or extend other software or a device; a hosted service people pay for → Subscriptions, Memberships & Online Services.','How does the program connect you: to sites, mail and files, to an AI, or as an add-on to something else?',[
 ('Browsers, mail & downloads','Programs for viewing websites, reading mail and feeds, and fetching files.','What comes in: web pages, mail and posts, or downloaded files?',['Web browser','Email client','Feed reader','Download manager','BitTorrent client']),
 ('AI assistants & agents','AI programs the owner talks to, asks or sends off to do tasks.','What does the AI do: converse, answer with sources, or act on its own?',['AI assistant','AI answer engine','AI agent platform']),
 ('Add-ons & device apps','Add-ons to a browser or office suite, and apps tied to one device.','What does it attach to: a browser, an office suite or a device?',['Browser extension','Office suite add-in','Device companion app','Device feature unlock']),
]),
('Photo, design & 3D','Programs for editing photographs, drawing and laying out designs, and modelling or preparing objects in 3D; video → Video & animation.','What is made: a photograph or bitmap image, a drawn or laid-out design, or a 3D or physical object?',[
 ('Photo editing & imaging','Programs for editing, developing, generating and bundling photographs and bitmap images.','What is done to the picture: edit pixels, manage and develop a photo library, generate it or buy a bundle?',['Image editor','Photo manager & RAW developer','AI image generator','Creative suite']),
 ('Drawing, design & type','Programs for painting, vector drawing, page layout, template design and fonts.','What is made: a painting, a scalable drawing, a multi-page layout, a quick template design or a type collection?',['Digital painting app','Vector graphics editor','Desktop publishing software','Graphic design app','Font manager']),
 ('3D, CAD & making','Programs for 3D models, engineering drawings and the machines that make them: printers, lasers, circuits and embroidery.','What is the 3D or made object: a model, a part drawing, a print job, a cut file, a circuit or a stitch file?',['3D modelling software','CAD software','3D printing slicer','Laser & CNC control software','Circuit design software','Photogrammetry software','Embroidery digitising software']),
]),
('Video & animation','Programs for writing, capturing, editing, animating and converting moving pictures; music → Music & audio.','Which stage of the film does the program serve: writing and capture, editing and animating, or converting?',[
 ('Writing & capture','Programs for scripting a film and recording what is on screen.','What is made before editing: a script, a screen recording or a screenshot?',['Screenwriting software','Screen recorder and streaming software','Screenshot tool']),
 ('Editing, effects & animation','Programs for cutting video, adding effects and making animation.','How are the moving pictures made: cut from footage, composited, drawn or photographed frame by frame?',['Video editor','Visual effects software','2D animation software','Stop-motion software']),
 ('Converting','Programs that change video and audio files between formats.','Is the file only reformatted?',['Video converter']),
]),
('Music & audio','Programs for making, writing down, performing and playing music and for reading e-books; plug-ins have their own department.','What is the job: record and produce, write music down, perform or learn, or play finished media?',[
 ('Recording & producing','Programs for recording, arranging, editing and patching sound.','How is the sound made: recorded on tracks, edited as a waveform, entered in patterns or patched from modules?',['Digital audio workstation','Audio editor','Music tracker','Modular and visual audio environment','CD ripper']),
 ('Writing music down','Programs for notation, tablature and sung melodies.','What is entered: a score, tablature or a sung line?',['Music notation software','Guitar tablature software','Singing voice synthesiser']),
 ('Performing & learning','Programs for DJs, live shows and music lessons.','Who uses it live: a DJ, a stage operator or a learner?',['DJ software','Show-control software','Music-learning app']),
 ('Players & readers','Programs that play finished video, music and e-books.','What is played or read: video and music, or books?',['Media player','E-book reader']),
]),
('Audio plug-ins & virtual instruments','Plug-ins that run inside a DAW, organised kind → archetype (plug-in or emulated hardware) → version; makers are in the brand register. A standalone program → Music & audio.','What does the plug-in do with sound: make it, shape its level and tone, place it in space and time, process a voice or guitar, or repair and measure it?',[
 ('Virtual instruments','Plug-ins that make sound when played: synths, samplers, orchestras, pianos and drums.','What is the sound source: oscillators, recordings played by a sampler, an orchestra, keys or a drum kit?',['Software synthesiser','Sampler & sample player','Orchestral sample library','Virtual piano & keys','Virtual drum instrument']),
 ('Level & tone','Plug-ins that change loudness and tone: compressors, EQs, saturation, channel strips and mastering.','What is changed: loudness, frequency balance, harmonic colour, a whole channel or the final mix?',['Compressor & dynamics plug-in','EQ & filter plug-in','Saturation & distortion plug-in','Console & channel-strip emulation','Mastering suite']),
 ('Space & time','Plug-ins that add room or repetition: reverbs, delays and modulation.','Is the effect a space or a repeat?',['Reverb plug-in','Delay & modulation plug-in']),
 ('Voice & guitar','Plug-ins built for vocals and guitar: tuning, alignment and amp models.','Which source is processed: a voice or a guitar?',['Pitch correction & vocal plug-in','Amp & cabinet simulator']),
 ('Repair & measurement','Plug-ins that remove defects or show what the sound is doing without changing it.','Does it change the sound or only show it?',['Audio restoration software','Metering & analysis plug-in']),
]),
('Hobbies, science & sky','Software for collections, family history, home planning, health, radio, the night sky, maps and data.','What is the interest: home and family life, radio, or the sky, the earth and data?',[
 ('Home, family & health','Programs for the owner\'s own records and plans: collections, ancestors, house and garden, health.','What is recorded or planned: a collection, a family, a house and garden, or the body?',['Collection cataloguing software','Genealogy software','Home & garden design software','Medical app']),
 ('Radio','Programs for amateur radio and software-defined receivers.','Is it for licensed operators or for tuning any signal?',['Ham radio software','SDR software']),
 ('Science, maps & sky','Programs for the night sky, geographic data and scientific calculation.','What is studied: the sky, the ground or numbers?',['Planetarium software','Astrophotography software','GIS and mapping software','Scientific and statistics software']),
]),
('Developer tools','Tools a person installs to write code, make games and sites and work with machines; servers and enterprise tooling are out of scope.','What stage of making software is it: writing and building code, making a game or site, or working with data and machines?',[
 ('Writing & building code','Programs for writing, extending, compiling, tracking and getting AI help with code.','What is done to the code: write it, extend the editor, build it, track changes or have an AI help?',['Code editor','Code editor plug-in','AI coding assistant','Compiler and runtime','Version control software']),
 ('Making games & sites','Programs for building a game or a website.','What is built: a game or a website?',['Game engine','Web design software']),
 ('Databases, terminals & networks','Programs for holding data and working with other machines from the keyboard.','What is reached: local data, a shell, remote servers or network traffic?',['Desktop database software','Terminal emulator','SSH and FTP client','Network analyser']),
]),
('Classic software','Kinds whose heyday has passed, kept for collectors of boxed software and people running it on vintage machines or emulators.','What did the program do for its owner: decorate the screen, look things up, print at home or share files?',[
 ('Classic & discontinued software','Programs of the 1980s to 2000s sold or shared as products in their own right.','What did the program do: decorate the idle screen, look things up, print at home or share files?',['Screen saver','Reference CD-ROM','Home publishing software','Peer-to-peer file sharing client']),
]),
]
AX_SH={
'Operating systems':None,
}
def sh_ax(name,ks):
    return None
SHAX={
'Cleaning, tuning & repair':'kinds by what is tidied, from files and programs to drivers, disks and small tools',
'Files, search & access':'kinds from working with files to reaching them from afar',
'Customising & automating':'kinds from launching to looking to game-specific changes',
'Documents & forms':'kinds from the bundle to its single programs, then fixed, scanned, long and form documents',
'Notes, plans & time':'kinds from words to tasks, dates, time and drawings',
'Language, typing & voice':'kinds from learning a language to translating, typing and speech',
'Browsers, mail & downloads':'kinds from the web to mail and posts, then downloads',
'Photo editing & imaging':'kinds from editing pixels to managing, generating and bundling',
'Drawing, design & type':'kinds from freehand painting to scalable drawing, layout, templates and type',
'3D, CAD & making':'kinds from the 3D model to the machine that makes it',
'Recording & producing':'kinds from the all-round workstation to waveform editing, patterns and modular patching',
'Virtual instruments':'kinds from synthesised sound to sampled instruments',
'Level & tone':'kinds from dynamics to tone, colour, the whole channel and the final master',
'Science, maps & sky':'kinds from the sky to the ground to numbers',
'Writing & building code':'kinds from writing to extending, helping, building and tracking',
'Classic & discontinued software':'kinds by what the program did for its owner',
'Operating systems':'kinds by the system\'s lineage',
'Running other systems\' software':'kinds from a whole machine to single programs to game consoles',
'Accounts, connections & data':'kinds from the login to the connection and the stored data',
'Home, family & health':'kinds from collections to family, house and body',
'Writing & capture':'kinds from script to capture',
'Editing, effects & animation':'kinds from live footage to drawn and photographed frames',
'Databases, terminals & networks':'kinds from local data to shells, remote servers and traffic',
}
newd=[]
used=set()
for dn,t,ax,shelves in LAY:
    odp=next(x for x in d['depts'] if x['n']==dn) if dn!=OSD else next(x for x in d['depts'] if x['n']=='Operating systems & system tools')
    dp={k:v for k,v in odp.items() if k!='s'}
    dp['t']=t; dp['ax']=ax
    dp['s']=[]
    for sn,st,sax,ks in shelves:
        sh={'n':sn,'t':st}
        if len(ks)>3: sh['ax']=SHAX.get(sn,'kinds ordered from the commonest to the most specialised')
        sh['k']=[]
        for kn in ks:
            k=K[kn]; used.add(kn)
            if kn not in TT: print('NO TT',kn)
            k['tt']=TT[kn]; k.pop('t',None)
            sh['k'].append(k)
        dp['s'].append(sh)
    newd.append(dp)
for kn in K:
    if kn not in used: print('UNPLACED',kn)
d['depts']=newd
d['ax']='What job does the software do for its owner: run and maintain the machine, protect it, handle documents and money, go online, make images, film, music or plug-in sound, serve a hobby, build software, or belong to a past era?'
d['key']=['1. Is it a system, or a program that runs, cleans, backs up, searches, customises or reaches the machine or its files? → Operating systems & system tools',
'2. Does it protect the device, children, accounts, connections or stored data? → Security & privacy',
'3. Is it for documents, notes, planning, language or household money? → Office & productivity',
'4. Does it browse, mail, download, answer as an AI, or extend a browser or device? → Internet & AI',
'5. Does it edit photographs, draw or lay out designs, or model objects in 3D? → Photo, design & 3D',
'6. Does it write, capture, cut, animate or convert moving pictures? → Video & animation',
'7. Does it record, notate, perform, teach or play music, or read e-books? → Music & audio',
'8. Is it a plug-in that runs inside a music program? → Audio plug-ins & virtual instruments',
'9. Is it for a collection, family tree, home plan, radio, the sky, maps or scientific data? → Hobbies, science & sky',
'10. Is it used to write code, make a game or site, or inspect data and networks? → Developer tools',
'11. Is it a program of a past era kept by collectors, such as a screen saver, reference disc or file-sharing client? → Classic software',
'<i>Precedence: a plug-in is step 8 before the standalone kind (step 7); an AI coding tool is step 10 before an AI assistant (step 4); a classic program that is still sold is placed by its job.</i>']
d.pop('lead') if False else None
# see links
SEE={
'Digital painting app':[['I1','Image editor','photo-style pixel editing']],
'Image editor':[['I1','Digital painting app','brush-based painting']],
'Vector graphics editor':[['I1','Diagramming software','connected shapes rather than artwork'],['I1','Graphic design app','template-based layouts']],
'Diagramming software':[['I1','Vector graphics editor','freer vector drawing']],
'Video editor':[['I1','Visual effects software','compositing shots']],
'Visual effects software':[['I1','Video editor','cutting footage']],
'Screen recorder and streaming software':[['I1','Screenshot tool','still captures']],
'Screenshot tool':[['I1','Screen recorder and streaming software','moving captures']],
'Audio editor':[['I1','Audio restoration software','repairing defects'],['I1','Digital audio workstation','multitrack production']],
'Audio restoration software':[['I1','Audio editor','general sound editing']],
'Digital audio workstation':[['I1','Audio editor','single-file editing']],
'Software synthesiser':[['I1','Sampler & sample player','recorded sounds']],
'Sampler & sample player':[['I1','Software synthesiser','generated sounds'],['I1','Orchestral sample library','sampled orchestras']],
'Orchestral sample library':[['I1','Sampler & sample player','host instrument']],
'Password manager':[['I1','Authenticator app','one-time codes']],
'Authenticator app':[['I1','Password manager','stored logins']],
'Browser extension':[['I1','Password manager','full password apps']],
'Game emulator':[['I1','Virtual machine software','whole-computer emulation'],['I1','Game mod manager','game modding']],
'Virtual machine software':[['I1','App compatibility layer','no emulated hardware']],
'App compatibility layer':[['I1','Virtual machine software','full guest system']],
'Backup software':[['I1','PC migration software','moving to a new machine']],
'PC migration software':[['I1','Backup software','safe copies']],
'Word processor':[['I1','Office suite','sold as a bundle']],
'Spreadsheet program':[['I1','Office suite','sold as a bundle']],
'Presentation program':[['I1','Office suite','sold as a bundle']],
'Office suite':[['I1','Word processor','single program']],
'Feed reader':[['I1','Email client','mail rather than feeds']],
'Ham radio software':[['I1','SDR software','general receiver software']],
'SDR software':[['I1','Ham radio software','operator logging and digital modes']],
'AI coding assistant':[['I1','Code editor','plain editors'],['I1','AI assistant','general assistants']],
'Code editor plug-in':[['I1','AI coding assistant','AI-led coding tools']],
'Scientific and statistics software':[['I1','Desktop database software','data storage']],
'Peer-to-peer file sharing client':[['I1','BitTorrent client','BitTorrent network']],
'BitTorrent client':[['I1','Peer-to-peer file sharing client','older networks']],
'Game engine':[['I1','Web design software','building websites']],
'Media player':[['I1','E-book reader','books']],
'Disk space analyser':[['I1','PC cleaner','clearing space']],
'Clipboard manager':[['I1','App launcher','quick access']],
'Music tracker':[['I1','Digital audio workstation','modern production']],
'CD ripper':[['I1','Media player','playing the files']],
'Screen saver':[['I1','Desktop customisation tool','live wallpaper']],
}
allk={k['n']:k for dp in d['depts'] for s in dp['s'] for k in s['k']}
for kn,v in SEE.items():
    for t in v: assert t[1] in allk,t
    allk[kn]['see']=v
# lead keep; brands
b=json.load(open(R+'work/STR_I1/bak/I1_brands.json'))
have={x['n'].lower() for x in b['b']}
tmpl=next(x for x in b['b'] if x['n']=='Microsoft')
for n,c,f in [('IBM','United States','1911'),('Commodore International','United States','1954'),('ARP Instruments','United States','1969'),('MetaMachine','United States','2000'),('Alessandro Ranellucci','Italy','')]:
    if n.lower() not in have: b['b'].append({'n':n,'c':c,'f':f,'seg':tmpl['seg'],'kf':'','d':'','s':''})
after=(len(d['depts']),sum(len(s['k']) for dp in d['depts'] for s in dp['s']),sum(len(k.get('x',[])) for k in allk.values()))
print(before,before_sh,after,sum(len(dp['s']) for dp in d['depts']))
def wr(p,o):
    json.dump(o,open(p+'.tmp','w'),ensure_ascii=False,indent=1); os.replace(p+'.tmp',p)
wr(R+'out/I1.json',d); wr(R+'out/I1_brands.json',b)
wr(R+'out/I1_renames.json',{})
