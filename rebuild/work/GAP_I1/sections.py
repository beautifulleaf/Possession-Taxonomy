import json,os,re
P='/home/user/Possession-Taxonomy/rebuild/out/I1.json'
d=json.load(open(P))
def norm(s): return re.sub(r'[^a-z0-9]','',s.lower())
def lst(g,names): return {n:g for n in names.split('|')}
S={}
vcs={}
vcs.update(lst("Distributed","GNU Bazaar|BitKeeper|Code Co-op|darcs|Dat|Fossil|Git|GNU arch|Mercurial|Monotone|Vesta"))
vcs.update(lst("Client-server","AccuRev SCM|IBM DevOps Code ClearCase|Concurrent Versions System|CVSNT|Dimensions CM|IC Manage|PTC Integrity|PVCS|IBM Rational Team Concert|StarTeam|Subversion|Surround SCM|Vault"))
vcs.update(lst("Both distributed and client-server","Azure DevOps|Perforce P4|Rational Synergy|Unity Version Control"))
vcs.update(lst("Local or shared folder","Revision Control System|Source Code Control System|Microsoft Visual SourceSafe"))
S["Version control software"]=("by model",vcs,"Not on the reference list")
os_=lst("Open source","Aleph One|Babylon.js|Blend4Web|Cocos2d|Codea|Crystal Space|Defold|GDevelop|Godot|Irrlicht Engine|jMonkeyEngine|Kivy|LibGDX|LÖVE|MonoGame|O3DE|OGRE|OpenMW|OpenSimulator|ORX|Panda3D|Phaser|PlayCanvas|Pygame|Ren'Py|Scratch|Solar2D|Stride|Three.js|TIC-80|Torque3D|Twine|Flixel|Cube 2 Engine|A-Frame|Adventure Game Studio|Doom engine|Quake engine|Wintermute Engine|StepMania")
pr=lst("Proprietary","AppGameKit|Amazon Lumberyard|Buildbox|Clickteam Fusion|Construct|CryEngine|GameMaker|GameSalad|Gamestudio|Leadwerks|Marmalade|Pico-8|Pixel Game Maker MV|Roblox|RPG Maker|Stencyl|Unigine|Unity|Unreal Engine|Virtools|Zillions of Games|S&box|M.U.G.E.N|Starling Framework|Visual Pinball")
os_.update(pr)
S["Game engine"]=("by licence",os_,"Not on the reference list")
t={}
t.update(lst("Unix-like","Alacritty|GNOME Terminal|guake|kitty|konsole|Linux console|rxvt|Terminator|Tilda|Tilix|xfce4-terminal|xterm"))
t.update(lst("Windows","AbsoluteTelnet|AlphaCom|ConEmu|HyperACCESS|HyperTerminal|mintty|PComm|Qmodem Pro|Tera Term|Windows Console|Windows Terminal"))
t.update(lst("macOS","iTerm2|Terminal|ZTerm"))
t.update(lst("Classic Mac OS","MacTerminal|MacWise|Red Ryder"))
t.update(lst("MS-DOS","Telix|Terminate"))
t.update(lst("Cross-platform","Kermit 95|PuTTY|SecureCRT|SyncTERM|Warp|x3270|ZOC"))
t.update(lst("Other systems","CBterm/C64|fshell|NComm|Termux"))
S["Terminal emulator"]=("by platform",t,"Not on the reference list")
b={}
b.update(lst("Free and open source","Amanda|Attic|BackupPC|Back In Time|Bacula|BorgBackup|Bup|DAR|DirSync Pro|Duplicati|duplicity|FlyBack|FreeFileSync|git-annex|luckyBackup|Restic|rdiff-backup|rsnapshot"))
b.update(lst("Proprietary","Acronis True Image|Argentum Backup|BackupAssist|Bvckup 2|MSP360 Backup|Cobian Backup|Comodo Backup|Crashplan|Genie Backup Manager|Image for Windows|Macrium Reflect|Norton Ghost|Novabackup|NTBackup|Retrospect|SpiderOak|Syncovery|Time Machine|Windows Backup and Restore"))
b.update(lst("Defunct","Areca Backup|Mozy|SyncToy|Mac Backup"))
S["Backup software"]=("by licence",b,"Not on the reference list")
c={}
c.update(lst("C and C++","GCC|Clang|Microsoft Visual C++|Intel oneAPI DPC++/C++ Compiler"))
c.update(lst("C#","Mono|Roslyn"))
c.update(lst("Lisp","Steel Bank Common Lisp|CLISP|Clozure CL|Allegro Common Lisp|LispWorks"))
c.update(lst("D","D (DMD)|LDC"))
c.update(lst("Fortran and COBOL","GNU Fortran|GnuCOBOL"))
c.update(lst("Go","Go (gc)"))
c.update(lst("Java","javac"))
c.update(lst("Haskell","GHC"))
c.update(lst("Pascal","Free Pascal|Delphi"))
c.update(lst("Python","PyPy|Jython|IronPython|Nuitka|Cython"))
c.update(lst("Ruby","YARV|JRuby"))
c.update(lst("Rust","rustc"))
c.update(lst("Scheme","Racket|Chez Scheme|GNU Guile|Chicken|Gambit"))
c.update(lst("Swift","swiftc"))
S["Compiler and runtime"]=("by language",c,"Not on the reference list")
r={}
r.update(lst("Open source","Krdc|MeshCentral|Remmina|RustDesk|TigerVNC|TightVNC|UltraVNC|Veyon|Vinagre|xpra|X11vnc|X2Go|rdesktop"))
r.update(lst("Proprietary","Ammyy Admin|AnyDesk|Anyplace Control|Apple Remote Desktop|Apple Screen Sharing|Chrome Remote Desktop|GoToMyPC|LogMeIn Resolve|Mikogo|NetSupport Manager|NoMachine|Parsec|RealVNC|Remote Desktop Services|Remote Utilities|ScreenConnect|Splashtop|Symantec pcAnywhere|TeamViewer|Timbuktu"))
S["Remote desktop software"]=("by licence",r,"Not on the reference list")
for dp in d['depts']:
  for sh in dp['s']:
    for k in sh['k']:
      if k['n'] in S:
        xg,m,dflt=S[k['n']]; nm={norm(a):v for a,v in m.items()}
        k['xg']=xg
        for e in k['x']:
            g=nm.get(norm(e['n'])) or nm.get(norm(e.get('a','') or '~'))
            if g: e['g']=g
            elif not e.get('g'): e['g']=dflt
tmp=P+'.tmp'; json.dump(d,open(tmp,'w'),ensure_ascii=False); os.replace(tmp,P)
