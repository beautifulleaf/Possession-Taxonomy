# -*- coding: utf-8 -*-
# Data fetched 2026-10-31 (see sources.tsv). Format: name|maker|year|section
def P(s):
    out=[]
    for l in s.strip().split('\n'):
        l=l.strip()
        if not l: continue
        p=[x.strip() for x in l.split('|')]
        p+=['']*(4-len(p))
        out.append(tuple(p[:4]))
    return out

WIKI='https://en.wikipedia.org/wiki/'
SRC={
 'browsers':WIKI+'Comparison_of_web_browsers',
 'office':WIKI+'Comparison_of_office_suites',
 'pw':WIKI+'List_of_password_managers',
 'vpn':WIKI+'Comparison_of_virtual_private_network_services',
 'linux':WIKI+'List_of_Linux_distributions',
 'dw':'https://distrowatch.com/dwres.php?resource=popularity',
 'os':WIKI+'List_of_operating_systems',
 'av':WIKI+'Category:Antivirus_software',
 'ide':WIKI+'Comparison_of_integrated_development_environments',
 'te':WIKI+'Comparison_of_text_editors',
 'bt':WIKI+'Comparison_of_BitTorrent_clients',
 'mail':WIKI+'Comparison_of_email_clients',
 'virt':WIKI+'Comparison_of_platform_virtualization_software',
 'chat':WIKI+'List_of_chatbots',
 'hos':WIKI+'History_of_software',
 'disc':WIKI+'Category:Discontinued_software',
 'arch':WIKI+'Comparison_of_file_archivers',
 'notes':WIKI+'Comparison_of_note-taking_software',
 'ubuntu':WIKI+'Ubuntu_version_history',
 'libreoffice':WIKI+'LibreOffice',
 'msoffice':WIKI+'Microsoft_Office',
}

BROWSERS=P('''
Amaya|W3C, INRIA||Retired
AOL Explorer|America Online||Retired
Arora|Benjamin C. Meyer||Retired
Avast Secure Browser|Avast Software||Current
Basilisk|Basilisk-Dev||Current
Brave|Brave Software||Current
Camino|The Camino Project||Retired
Chromium|The Chromium Project||Current
Cliqz|Cliqz GmbH||Retired
Comodo Dragon|Comodo Group||Current
Comodo IceDragon|Comodo Group||Retired
Dillo|The Dillo team||Current
Dooble|Dooble Team||Current
ELinks|Baudis, Fonseca, et al.||Current
Falkon|David Rosca||Current
Flock|Flock Inc||Retired
Galeon|Marco Pesenti Gritti||Retired
GNOME Web|Marco Pesenti Gritti||Current
GNU IceCat|GNU||Current
iCab|Alexander Clauss||Current
Internet Explorer for Mac|Microsoft||Retired
K-Meleon|Dorian, KKO, et al.||Current
Konqueror|KDE||Current
Ladybird|Ladybird Browser Initiative||Current
Links|Patocka, et al.||Current
Lunascape|Lunascape Corporation||Current
Lynx|Montulli, Grobe, Rezac, et al.||Current
Maxthon|Maxthon International Limited||Current
Midori|Christian Dywan, et al.||Current
Mosaic|NCSA||Retired
Mozilla Application Suite|Mozilla Foundation||Retired
Netscape (v6–7)|Netscape Communications Corporation, AOL||Retired
Netscape Browser (v8)|Mercurial Communications for AOL||Retired
Netscape Communicator (v4)|Netscape Communications||Retired
Netscape Navigator 9|Netscape Communications||Retired
NetSurf|The NetSurf Developers||Current
OmniWeb|The Omni Group||Retired
Opera Mobile|Opera Software||Current
Origyn Web Browser|Sand-labs||Retired
Pale Moon|Moonchild Productions||Current
Puffin Browser|CloudMosa||Current
qutebrowser|Freya Bruhin||Current
SalamWeb|Salam WebTechnologies||Current
SeaMonkey|SeaMonkey Council||Current
Shiira|Happy Macintosh Developing Team||Retired
Sleipnir|Fenrir Inc.||Current
SRWare Iron|SRWare||Current
surf|suckless.org||Current
Torch Browser|Torch Media||Retired
Uzbl|Dieter Plaetinck||Current
Waterfox|Alex Kontos||Current
WebPositive|Haiku||Current
WorldWideWeb (Nexus)|Tim Berners-Lee||Retired
w3m|Akinori Ito||Current
Yandex Browser|Yandex||Current
''')
BROWSER_ALIAS={'Chrome':'Google Chrome','Edge':'Microsoft Edge','Firefox':'Mozilla Firefox','Netscape Navigator (v1–4)':'Netscape Navigator'}

OFFICE=P('''
Ability Office|Ability Plus Software|1995
Apache OpenOffice|Apache Software Foundation|2012
Calligra Suite|KDE|2011
Collabora Online|Collabora|2019
Feng Office Community Edition|Feng Office|2007
GNU TeXmacs|Joris van der Hoeven|1996
NeoOffice|Planamesa Software|2005
OfficeSuite|MobiSystems|2004
Polaris Office|Infraware|2011
Tiki Wiki CMS Groupware|Tiki Association|2002
Zimbra|Synacor|2005
''')
OFFICE_VERS=P('''
Microsoft Office for Windows (first release)|Microsoft
''')

PW=P('''
Enpass||
Firefox Lockwise||
GNOME Keyring||
Intuitive Password||
KeePass||
KeePassX||
KeePassDX||
KeeWeb||
Keychain|Apple|
KWallet|KDE|
Meldium||
Microsoft Autofill|Microsoft|
Mitro||
Myki||
oneID||
pass||
Password Safe||
Pleasant Password Server||
SafeInCloud||
SecureSafe||
Yojimbo|Bare Bones Software|
Norton Password Manager|Gen Digital|
''')
VPN=P('''
Avast SecureLine|Avast
Amnezia VPN|
HMA|Avast
Hotspot Shield|
IVPN|
NordLayer|Nord Security
NymVPN|
Premier VPN|
PrivadoVPN|
PureVPN|
SaferVPN|
StrongVPN|
Tailscale|Tailscale
Hola|
Mozilla VPN|Mozilla
Windscribe|Windscribe
''')

# AV category pages (Wikipedia Category:Antivirus software); (name, maker, year, section)
AV=P('''
360 Total Security|Qihoo 360||Current
AOL Active Virus Shield|AOL||Discontinued
Avira|Avira||Current
ClamAV|Cisco Talos||Current
ClamTk||| Current
ClamWin Free Antivirus|||Current
Clario|Clario Tech||Current
Comodo Internet Security|Comodo Group||Current
Cylance|BlackBerry||Current
Disinfectant|John Norstad||Discontinued
Dr Solomon's Antivirus|Dr Solomon's||Discontinued
Dr.Web|Doctor Web||Current
DriveSentry|DriveSentry||Discontinued
ESafe|eSafe||Current
ESET NOD32 Antivirus|ESET||Current
Immunet|Cisco||Current
INCA Internet|INCA Internet||Current
IObit Malware Fighter|IObit||Current
Kaspersky Anti-Virus|Kaspersky||Current
Kaspersky Internet Security|Kaspersky||Current
Lavasoft Ad-Aware|Lavasoft||Current
MacKeeper|Clario Tech||Current
Microsoft Security Essentials|Microsoft||Discontinued
MSAV|Microsoft||Discontinued
NANO Antivirus|NANO Security||Current
Norton AntiVirus|Norton||Discontinued
Norton Internet Security|Norton||Discontinued
Norton Security|Norton||Discontinued
Online Armor Personal Firewall|Tall Emu||Discontinued
Panda Cloud Antivirus|Panda Security||Discontinued
PC Tools|PC Tools||Discontinued
PCKeeper|Kromtech||Discontinued
Prevx|Prevx||Discontinued
Surfshark Antivirus|Surfshark||Current
Symantec Endpoint Protection|Symantec||Current
ThunderByte Antivirus|ESaSS||Discontinued
Vba32 AntiVirus|VirusBlokAda||Current
VirusBuster|VirusBuster||Discontinued
Webroot|Webroot||Current
Windows Live OneCare|Microsoft||Discontinued
WiperSoft|WiperSoft||Current
ZoneAlarm|Check Point||Current
''')

CHAT_LLM=P('''
ChatGPT|OpenAI|2022
Character.AI|Character Technologies|2022
ChatGLM|Z.ai|2023
Ernie Bot|Baidu|2023
GigaChat|Sberbank|2023
HKChat|HKChat OmniServe Limited|2025
Kimi|Moonshot AI|2023
Leo|Brave Software|2023
Mistral Vibe|Mistral AI|2024
Amazon Q|Amazon|2023
Llama|Meta AI|2023
YouChat|You.com|2021
Lumo|Proton AG|2025
''')
CHAT_GEN=P('''
Amazon Alexa|Amazon|2014
Alice|Yandex|2017
AliGenie|Alibaba Group|2017
Bixby|Samsung Electronics|2017
Braina|Brainasoft|2014
Celia|Huawei|2020
Chai|Chai|2021
ChatBot|Text|2019
Cleverbot|Rollo Carpenter|2008
Clova|Naver Corporation|2017
Jabberwacky|Rollo Carpenter|1997
Kuki|Steve Worswick|2005
SILVIA|Cognitive Code|2008
SimSimi|ISMaker|2002
Ultra Hal|Robert Medeksza|2000
Xiaowei|Tencent|2017
''')
LOCAL_RUNNERS=P('''
Ollama
LM Studio
llama.cpp
vLLM
SGLang
TensorRT-LLM|NVIDIA
''')

IDE=P('''
Adobe Animate|Adobe
Flash Builder|
Powerflasher FDT|
SlickEdit|SlickEdit
Understand|SciTools
Fresh|
SASM|
Basic4android|Anywhere Software
Gambas|Benoît Minisini
Microsoft Small Basic|Microsoft
MonoDevelop|Xamarin and Mono community
PBASIC Stamp Editor|Parallax
PureBasic|Fantaisie Software
SharpDevelop|ICSharpCode Team
Xojo|Xojo
Anjuta|Anjuta Team
C++Builder|Embarcadero Technologies
CodeLite|CodeLite
LabWindows/CVI|National Instruments
OpenWatcom|Open Watcom community
Oracle Solaris Studio|Oracle
Pelles C IDE|
Rational Software Architect|IBM
U++ TheIDE|Ultimate++
Allegro Common Lisp|
LispWorks|LispWorks Ltd
SLIME|Community
BlackBox Component Builder|Oberon microsystems
EiffelStudio|Eiffel Software
Simply Fortran|Approximatrix
Android Studio|Google
DrJava|
Greenfoot|
JBuilder|
JDeveloper|Oracle
jGRASP|
MyEclipse|
Rational Application Developer|IBM
Brackets|Adobe
Aptana Studio|Aptana
Codeanywhere|Codeanywhere
Komodo IDE|ActiveState
ZeroBrane Studio|ZeroBrane
Decoda|Unknown Worlds Entertainment
Free Pascal IDE|Volunteers
Padre|Padre Team
Codelobster|Codelobster
HyperEdit|Jonathan Deutsch
PHPEclipse|PHPEclipse project team
PHPEdit|WaterProof SARL
Zend Studio|Zend
eric|Detlev Offenbach
PyDev / LiClipse|Appcelerator
Wing|Wingware
IDLE|Guido van Rossum et al.
Ninja-IDE|
RStudio|RStudio
DrRacket|PLT Design
Zed|
Dolphin Smalltalk|Object Arts
Pharo|INRIA
Squeak|squeak.org
VisualAge|IBM
VisualWorks|Cincom
IBM Rational Business Developer|IBM
Mule|
''')
JB_VERS=['IntelliJ IDEA Community Edition','IntelliJ IDEA Ultimate','WebStorm','PyCharm','PhpStorm','RubyMine','CLion','Rider','AppCode','RustRover']
ECL_VERS=['Eclipse CDT','Eclipse JDT','Eclipse PDT','Eclipse Web Tools','Eclipse DLTK','Eclipse EPIC','Eclipse StatET','Eclipse GDT','EclipseFP']

TEXTED=P('''
Acme|Rob Pike|1993
Alphatk|Vince Darley|1999
BBEdit|Rich Siegel|1992
Bluefish|Bluefish Development Team|1999
Coda|Panic|2007
ConTEXT|ConTEXT Project Ltd|1999
Crimson Editor|Ingyu Kang|1999
ed|Ken Thompson|1970
Editra|Cody Precord|2007
EmEditor|Emurasoft|1997
epsilon|Lugaru Software|1984
FeatherPad|Pedram Pourang|2016
FocusWriter|Graeme Gott|2008
gedit|GNU Project|2000
GNU nano|Chris Allegretta|1999
iA Writer|Information Architects|2010
JED|John E. Davis|1992
jEdit|Slava Pestov|1998
JOE|Joseph Allen|1988
JOVE|Johnathon Payne|1983
Kate|KDE Project|2000
KEDIT|Mansfield Software Group|1983
Komodo Edit|ActiveState|2007
KWrite|KDE Project|2000
LE|Alexander V. Lukyanov|1997
Leo|Edward K. Ream|1996
Light Table|Chris Granger|2012
mcedit|Miguel de Icaza|1994
Metapad|Alexander Davidson|1999
mg|Dave Conroy|1986
MinEd|Thomas Wolff|1992
MS-DOS Editor|Microsoft|1991
ne|Sebastiano Vigna, Todd Lewis, Daniele Filaretti|1993
NEdit|Mark Edel|1991
Notepad|Microsoft|1985
nvi|Keith Bostic|1994
Pico|University of Washington|1992
PolyEdit|PolySoft Solutions|1998
PSPad|Jan Fiala|2002
RJ TextEd|Rickard Johansson|2004
Sam|Rob Pike|
SciTE|Neil Hodgson|1999
Smultron|Peter Borg|2004
SubEthaEdit|TheCodingMonkeys|2003
TED Notepad|Juraj Simlovic|2001
Textadept|Mitchell|2007
TextEdit|Apple|2001
TextMate|MacroMates|2004
TextPad|Helios Software Solutions|1992
TextWrangler|Bare Bones Software|2003
The SemWare Editor|Sammy Mitchell|1985
UltraEdit|IDM Computer Solutions|1994
Ulysses|The Soulmen|
VEDIT|Ted Green, Greenview Data|1980
vi|Bill Joy|1976
XEmacs|Lucid Inc.|1991
XNEdit|Olaf Wintermann|2018
''')

BT=P('''
BitLord|||
Lftp|||
Miro|||
MLDonkey|||
Robert|||
Tonido|||
''')
MAIL=P('''
BlitzMail|Dartmouth College
Elm|Internet Promotion Agency
Evolution|The GNOME Project
FirstClass|Open Text
Forté Agent|Mark Sidell
Geary|The GNOME Project
GNUMail|Ludovic Marcotte and others
Gnus|Gnus team
GroupWise|Micro Focus
Hiri|Hiri
i.Scribe|Memecode
HCL Notes|HCL Technologies
IMP|Horde LLC
KMail|KDE
Mail (Windows)|Microsoft
Mailpile|Mailpile
mailx|
Microsoft Entourage|Microsoft
Mozilla Mail & Newsgroups|Mozilla Foundation
Mulberry|Cyrus Daboo
Netscape Messenger|Netscape Communications
Nylas Mail|Nylas
nmh / MH|RAND Corporation
Opera Mail|Opera Software
Outlook Express|Microsoft
Pegasus Mail|David Harris
Pine|University of Washington
Pocomail|Poco Systems
RoundCube|The RoundCube Team
SeaMonkey Mail & Newsgroups|SeaMonkey Council
SquirrelMail|The SquirrelMail Project Team
Sylpheed|Hiroyuki Yamamoto
The Bat!|RitLabs
Trojitá|KDE
Turnpike|Thus PLC
Windows Live Mail|Microsoft
Windows Mail (Vista)|Microsoft
YAM|YAM Open Source Team
Zimbra Desktop|Zimbra
''')
VIRT=P('''
Cooperative Linux|Dan Aloni, other developers
DOSEMU|Community project
Hercules|Roger Bowler
GXemul|Anders Gavare
LXC|Community project, Canonical
PearPC|Sebastian Biallas
SIMH|Bob Supnik, The Computer History Simulation Project
User Mode Linux|Jeff Dike, other developers
Xen|Xensource, now Citrix Systems
XCP-ng|Vates
''')
ARCH=P('''
ALZip|ESTsoft
B1 Free Archiver|Adam Buyer
Commander One|Eltima Software
Disk ARchiver|Denis Corbin
Expander|Haiku
Filzip|Philipp Engel
FreeArc|Bulat Ziganshin
iArchiver|Dare to be Creative
KGB Archiver|Tomasz Pawlak
Terse|IBM
TUGZip|Christian Kindahl
WinAce|e-merge GmbH
XAD|Dirk Stoecker
Xarchiver|Giuseppe Torelli
ZipGenius|M.Dev Software
ZPAQ|Matt Mahoney
''')
NOTES=P('''
AllMyNotes Organizer|Vladonai Software
CintaNotes|Cinta Software
ConnectedText|Eduardo Mauro
Dropbox Paper|Dropbox
Gnote|Aurimas Černius
KeyNote|Marek Jedliński
Logseq|Logseq Inc
Memonic|Nektoon
MyInfo|Milenix Software
MyNotex|Massimo Nardello
Notational Velocity|Zachary Schneirov
Open-Sankoré|Sankoré
Org-mode|Carsten Dominik, et al.
PDF Studio|Qoppa Software
Personal Knowbase|Bitsmith Software
QOwnNotes|Patrizio Bekerle
Qiqqa|Quantisle
Roam Research|Roam Research
TagSpaces|TagSpaces UG
TiddlyWiki|Jeremy Ruston
Tomboy|Alex Graveley
Ulysses|The Soulmen
Whizfolders|AvniTech Solutions
Microsoft Windows Journal|Microsoft
Zettlr|Hendrik Erz
Zim|Jaap Karssenberg
Zoho Notebook|Zoho
''')
