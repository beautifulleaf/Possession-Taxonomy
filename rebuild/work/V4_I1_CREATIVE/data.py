W='https://en.wikipedia.org/wiki/'
R={'RA':W+'Comparison_of_raster_graphics_editors','VE':W+'Comparison_of_vector_graphics_editors','L3D':W+'List_of_3D_computer_graphics_software',
'VID':W+'Comparison_of_video_editing_software','DAW':W+'Comparison_of_digital_audio_editors','PL':W+'Planetarium_software','SS':W+'Software_synthesizer',
'VST':W+'Virtual_Studio_Technology','AP':W+'Audio_plug-in','NI':W+'Native_Instruments','WA':W+'Waves_Audio','FF':W+'FabFilter','UA':W+'Universal_Audio_(company)',
'SP':W+'Spectrasonics','XF':W+'Xfer_Records','SC':W+'Comparison_of_scorewriters','GIS':W+'Comparison_of_geographic_information_systems_software',
'GEN':W+'Genealogy_software','SW':W+'List_of_screenwriting_software','CAD':W+'Comparison_of_computer-aided_design_editors','EDA':W+'Comparison_of_EDA_software',
'SCR':W+'Comparison_of_screencasting_software','AUD':W+'Comparison_of_audio_player_software','VPL':W+'Comparison_of_video_player_software',
'T2I':W+'Text-to-image_model','STAT':W+'Comparison_of_statistical_packages','MUS':W+'List_of_music_software'}
# rows: Name|Maker|Year|Alias|Note  (ref key given per block)
K={}
def kd(name,ref,rows,**kw):
    K[name]=dict(ref=ref,rows=[r.strip() for r in rows.strip().split('\n') if r.strip()],**kw)

kd('Image editor','RA','''
Ability Photopaint|Ability Software|2001
Acorn|Flying Meat|2007|Acorn Image Editor
Artipic|Artipic AB|2014
Brush Strokes Image Editor|Paul Bird|2004
Chasys Draw IES|John Paul Chacha|2001
CinePaint|Robin Rowe|2002
CodedColor PhotoStudio Pro|1STEIN Corp.|2001
Corel PaintShop Pro|Corel|1992|Jasc Paint Shop Pro
Corel PHOTO-PAINT|Corel|1992
Fotografix|Madhavan Lakshminarayanan|2009
G'MIC|David Tschumperlé|2008
GrafX2|Sunset Design|1996
GraphicConverter|Thorsten Lemke|1992
GraphicsMagick|GraphicsMagick Group|2002
HDR PhotoStudio|Unified Color|2009
Helicon Filter|Helicon Soft|2004
ImageJ|Wayne Rasband|1997
ImageMagick|ImageMagick Studio|1990
IrfanView|Irfan Skiljan|1996
KolourPaint|KDE|2004
LazPaint|circular|2011
LiveQuartz|Romain Piveteau|2005
Microsoft Paint|Microsoft|1985|Paint
mtPaint|Mark Tyler|2004
Photopea|Ivan Kutskir|2013
PhotoLine|Computerinsel|1995
PhotoPerfect|Arcadia Software|2002
Pinta|Jonathan Pobst|2010
Pixlr|Ola Sevandersson|2008
Seashore|Mark Pazolli|2003
Xara Photo & Graphic Designer|Xara|1995
''',gone=['Photopea ','Pixlr '])
kd('Photo manager & RAW developer','RA','''
ACDSee|ACD Systems||ACDSee Home · ACDSee Pro · ACDSee Ultimate
Bibble|Bibble Labs|2000
digiKam|digiKam team|2002|DigiKam
Digital Photo Professional|Canon|
gThumb|Paolo Bacchilega|2001
Iridient Developer|Iridient Digital|2004
RawTherapee|Gabor Horvath|2006
Shotwell|Yorba Foundation|2009
Photos|Apple|2014|Photos (Apple)
XnView MP|Pierre-emmanuel Gougelet|2008|XnView Classic
Zoner Photo Studio|Zoner|
''')
kd('AI image generator','T2I','''
Imagen|Google|2023
Ideogram|Ideogram|2023
Recraft|Recraft, Inc.|2023
Flux|Black Forest Labs|2024
Aurora|xAI|2024
AuraFlow|FAL|2024
HiDream|HiDream-AI|2025
Halfmoon|Reve AI, Inc.|2025|Reve
''')
kd('3D modelling software','L3D','''
AC3D|Inivis||
Anim8or|||
Animation:Master|HASH, Inc||
Cheetah3D|||
CityEngine|Procedural Inc||
Clara.io|Exocortex||
Daz Studio|||
Electric Image Animation System|||
form•Z|AutoDesSys, Inc.||
Hexagon|Daz Productions||
iClone|Reallusion||
LightWave 3D|Lightwave Digital||
MakeHuman|||
MASSIVE|||
MeshLab|||
Modo|The Foundry||
Mudbox|Autodesk||
Poser|Bondware||
Realsoft 3D|||
Silo|Nevercenter||
Substance 3D|Adobe||
Terragen|||
Vue|E-on Software||
Wings 3D|||
3D-Coat|||
Carrara|Daz Productions||
Bryce|Daz Productions||
''')
kd('3D renderer','L3D','''
3Delight|||
Aqsis|||
Brazil R/S|||
Kerkythea|||
LuxRender|||
Maxwell Render|||
mental ray|NVIDIA||
Octane Render|||
RenderMan|Pixar||
Sunflow|||
V-Ray|||
POV-Ray|||
Gelato|NVIDIA||
''',new=True)
kd('CAD software','CAD','''
ABViewer|CADSoftTools||
Alibre Design|Alibre, LLC||
Allplan|Allplan GmbH||
Archicad|Graphisoft||
Autodesk Inventor|Autodesk||
Autodesk Revit|Autodesk||
BricsCAD|Bricsys||
BRL-CAD|United States Army Research Laboratory||
CATIA|Dassault Systèmes||
Creo|Parametric Technology Corporation||
DataCAD|DATACAD LLC||
DesignSpark Mechanical|RS Components||
IntelliCAD|IntelliCAD Technology Consortium||
IRONCAD|IronCAD LLC||
KeyCreator|Kubotek||
LibreCAD|||
MicroStation|Bentley Systems||
NX|Siemens Digital Industries Software||
OpenSCAD|||
QCAD|Ribbon Soft||
Salome|||
Solid Edge|Siemens Digital Industries Software||
SolveSpace|Jonathan Westhues||
SpaceClaim Engineer|Ansys, Inc.||
Tekla Structures|Trimble||
T-FLEX CAD|Top Systems Ltd||
TurboCAD|IMSI/Design, LLC||
VariCAD|VariCAD||
VisualARQ|Asuni CAD S.A.||
ZWCAD|ZWSOFT||
DraftSight|Dassault Systèmes||
Vectorworks|Vectorworks, Inc.||
''')
kd('Circuit design software','EDA','''
CircuitMaker|Altium||
CADSTAR|Zuken||
DesignSpark PCB|RS Components||
DipTrace|Novarm||
Flux.ai|||
Fritzing|||
gEDA|gEDA Project||
LibrePCB|LibrePCB Team||
LTspice|Analog Devices||
NI Multisim|National Instruments||
Ngspice|||
OrCAD|Cadence Design Systems||
pcb-rnd|||
Proteus Design Suite|Labcenter Electronics||
Pulsonix|WestDev||
Qucs|Qucs Developers||
TARGET 3001!|||
TINA|DesignSoft||
atopile|||
tscircuit|||
XCircuit|Tim Edwards||
KTechLab|KTechLab Developers||
''')
kd('Embroidery digitising software','VE','''
Embroidermodder|Embroidermodder Team|2004
Wilcom|Wilcom||
Embird|Embird||
''')
kd('Vector graphics editor','VE','''
Apache OpenOffice Draw|Apache Software Foundation|2000
Boxy SVG|Jarosław Foksa|2013
Collabora Online Draw|Collabora Productivity|2016
ConceptDraw PRO|CS Odessa|1999
Dia|GNOME Project|1998
Edraw Max|EdrawSoft|2004
EazyDraw|Dekorra Optics|2003
GodSVG|MewPurPur|2023
Google Drawings|Google|2010
Karbon|KDE Calligra Suite|2012
LibreOffice Draw|The Document Foundation|2011
Microsoft Visio|Microsoft|1992|Visio
OmniGraffle|The Omni Group|2000
Penpot|Kaleidos|2021
SaviDraw|Silicon Beach Software|2019
sK1|sK1 Project Team|2009
SVG-edit|SVG-edit community|2009
Synfig Studio|Synfig Team|2005|Synfig
VectorStyler|Numeric Path|2021
WinFIG|winfig Team|2003
Xara Designer Pro+|Xara|1995
Xfig|Xfig Team|1985
''')
kd('Digital painting app','RA','''
Autodesk SketchBook|Autodesk|2004|SketchBook Pro
MyPaint|Martin Renold|2005
OpenCanvas|Portalgraphics|2000
Project Dogwaffle|Dan Ritchie|1997
Tux Paint|Bill Kendrick|2002
Artweaver|Boris Eyrich|2002
Corel Painter Essentials|Corel|2003
''')
kd('Screenwriting software','SW','''
Scriptware|Cinovation||Cinovation Scriptware
Sophocles|||
Dramatica|||
Cherry Draft|||
Scrite|||
Index Card|||
''')
kd('Screen recorder and streaming software','SCR','''
Adobe Captivate|Adobe|
BB FlashBack|Blueberry Software|
CamStudio|CamStudio.org|
Debut|NCH Software|
Fraps|Beepa Pty Ltd|
HyperCam|Solveig Multimedia|
Peek|Philipp Wolfer|
recordMyDesktop|SourceForge|
ScreenPal|ScreenPal|
ScreenFlow|Telestream|
SimpleScreenRecorder|maartenbaert|
Snapz Pro X|Ambrosia Software|
''',gone=['ShareX','Snagit'])
kd('Video editor','VID','''
Adobe Premiere Elements|Adobe Inc.|2004
Avid Media Composer First|Avid|2017
AVS Video Editor|Online Media Technologies Ltd.|2003
Blackbird|Blackbird PLC|2004
Cinelerra|Heroine Virtual|2002
Cinelerra-GG Infinity|Open Source Community|2016
ivsEdits|Interactive Video Systems|2008
LiVES|Gabriel Finch and others|2002
LosslessCut|Mikael Finstad|2016
Nero Video|Nero AG|2002
Pitivi|Open Source Community|2004
VideoPad|NCH Software|2008
Camtasia|TechSmith Corporation|2002
Microsoft Photos Video Editor|Microsoft Corporation|2017
''',gone=['Camtasia'])
kd('Visual effects software','VID','''
Autodesk Flame|Autodesk|1993
Natron|Alexandre Gauthier, Frédéric Devernay|2014
''')
kd('Digital audio workstation','DAW','''
AudioDesk|Mark of the Unicorn||
Fairlight|Blackmagic Design||
Kristal|Kreatives||
MuLab|MuTools||
MultitrackStudio|Bremmers Audio Design||
MusE|MuseE||
n-Track|n-Track Software||
Nuendo|Steinberg||
Podium|Zynewave||
Qtractor|Qtractor||
Rosegarden|Rosegarden||
LUNA|Universal Audio|2020|
''')
kd('Music notation software','SC','''
Canorus|Katzmann, Jekovec, Rudolph||
Early Notation Typesetter|Gossner, West, Theuns||
Flat|Tutteo||
Harmony Assistant|Myriad Software||
Impro-Visor|Bob Keller||
MagicScore|Maestro Music Software||
Mozart|Mozart Music Software||
Mus2|Utku Uzmen||
MusiCAD|Musys Software||
MusicEase|MusicEase Software||
Musink|Lee Reid||
MusiXTeX|Taupin, Mitchell, Egler||
Notation Composer|Notation Software||
Philip's Music Writer|Philip Hazel||
SCORE|Leland Smith||
The Note Processor|ThoughtProcessors|1991
''')
kd('Media player','AUD','''
Amarok|Mark Kretschmann|2003
aTunes|Alex Aranda et al.|2006
Audacious|Audacious Development Team|2005
Clementine|Clementine Team|2010
cmus|Timo Hirvonen|2005
Cog|Vincent Spader|2006
DeaDBeeF|Oleksiy Yakovenko|2009
Exaile|Adam Olsen|2006
Groove Music|Microsoft|2012
Guayadeque Music Player|Juan Rios, Tiago T Barrionuevo|2009
JRiver Media Center|JRiver, Inc.|1999
JuK|Scott Wheeler|2003
MediaMonkey|Ventis Media Inc.|2003
Music on Console|Damian Pietras|2002
Music Player Daemon|Warren Dukes|2003
musikCube|Casey Langen|2005
Napster|William Christopher Gorog|2003
Quod Libet|Quod Libet Team|2004
Rhythmbox|Colin Walters|2004
Sayonara Player|Michael Lugmair|2011
Sonic Visualiser|Centre for Digital Music, Queen Mary University of London|2007
Spotify|Spotify LTD|2008
XMMS|XMMS Team|1997
XMPlay|Un4seen Developments|1998
BZR Player|aargirakis|2008
ALLPlayer|ALLPlayer Group|1998
Elmedia Player|Electronic Team, Inc.|2005
DivX|DivX, LLC|2001
FFplay|FFmpeg project|2000
GOM Player|GOM & Company|2003
jetAudio|Cowon Systems|1997
K-Multimedia Player|YoungHuee Kang|2002
Mac Blu-ray Player|Macgo Inc.|2011
MediaPortal|Team MediaPortal|2004
Media Player Classic Home Cinema|Gabest|2006
Microsoft Movies & TV|Microsoft|2012
Microsoft Photos|Microsoft|2012
MPlayer|Árpád Gereöffy|2000
RealPlayer|RealNetworks|1995
SMPlayer|Ricardo Villalba|2006
GNOME Videos|The GNOME Project|2003|Totem
Videostream|Videostream Team|2014
WinDVD Pro|Corel|1998
xine|xine Team|2000
sView|Kirill Gavrilov|2009
PowerDVD|CyberLink|1998
Apprentice Video|Pavel Koshevoy|2010
IPTVX|IPTVX LLC|2019
''')
kd('Software synthesiser','SS','''
Alchemy|Apple|2015|Camel Audio Alchemy
Zebra|u-he||
Circle|Future Audio Workshop||
Csound|Barry Vercoe, MIT Media Lab|1985
Neon|Steinberg|1999
Generator|Native Instruments|1997
ReBirth RB-338|Propellerhead Software|1997
FM8|Native Instruments||
Absynth|Native Instruments||
Razor|Native Instruments||
Monark|Native Instruments||
Moog Model D|Moog|2018
Arturia Wurlitzer V|Arturia|2012
Rhodes V8|Arturia|2023
GForce Oberheim OB-X|GForce|2023
Lounge Lizard EP-4|Applied Acoustics Systems|2006
Bristol|||
''')
kd('Sampler & sample player','SS','''
GigaSampler|NemeSys|1997
GigaStudio|Tascam|2008
Groove Agent ONE|Steinberg||
Battery|Native Instruments|2002
Maschine|Native Instruments||
''')
kd('Virtual piano & keys','SS','''
Mrs Mills Piano|Spitfire Audio|2021
Hans Zimmer Piano|Spitfire Audio|2016
Château Piano|Spitfire Audio|2025
Lounge Lizard EP-4|Applied Acoustics Systems|2006
Trilian|Spectrasonics||
''')
kd('Compressor & dynamics plug-in','WA','''
Waves L1 Ultramaximizer|Waves Audio|1994
Waves C6 Multiband Compressor|Waves Audio|2013
FabFilter Pro-L|FabFilter|2010
FabFilter Pro-MB|FabFilter|2013
FabFilter Pro-DS|FabFilter|2012
FabFilter Pro-G|FabFilter|2011
Waves Vocal Rider|Waves Audio|2010
Waves NS1 Noise Suppressor|Waves Audio|2012
''')
kd('EQ & filter plug-in','WA','''
Waves Q10|Waves Audio|1992
Waves RS56 Passive EQ|Waves Audio|2013
FabFilter Volcano|FabFilter|2005
FabFilter Simplon|FabFilter|2007
FabFilter Micro|FabFilter|2010
''')
kd('Console & channel-strip emulation','WA','''
Waves API Collection|Waves Audio|2007
Waves REDD Console|Waves Audio|2012
Waves Scheps Omni Channel|Waves Audio|2018
Waves Chris Lord-Alge Signature Series|Waves Audio|2010
Waves Eddie Kramer Signature Series|Waves Audio|2009
''')
kd('Pitch correction & vocal plug-in','WA','''
Waves Tune|Waves Audio|2005
Waves Butch Vig Vocals|Waves Audio|2015
''')
kd('Metering & analysis plug-in','WA','''
Waves WLM Meter|Waves Audio|2014
''')
kd('Reverb plug-in','WA','''
Waves Abbey Road Studio 3|Waves Audio|2019
''')
kd('Genealogy software','GEN','''
Family.Show|||
GenealogyJ|||
LifeLines|||
GeneWeb|||
Gramps Web|||
PhpGedView|||
webtrees|||
My Family Tree|||
Genealogica Grafica|||
Personal Ancestral File|||
Family Historian|||
Genbox Family History|||
GenoPro|||
Kith and Kin Pro|||
GEDitCOM|||
The Master Genealogist|||
TreeDraw|||
TNG|||The Next Generation of Genealogy Sitebuilding
Ancestral Quest|||
Reunion|||
Brother's Keeper|||
''')
kd('Online family-tree service','GEN','''
FamilySearch|||
GEDmatch|||
Rodovid|||
WeRelate|||
WikiTree|||
Ancestry.com|||
Familio|||
Findmypast|||
GenealogyBank|||
Geneanet|||
Genes Reunited|||
Geni.com|||
MyHeritage|||
''',new=True)
kd('Planetarium software','PL','''
Astrarium|||
C2A|||
Digital Universe Atlas|||
HNSKY|||
OpenSpace|||
Nightshade|||
SkyExplorer|||
Sky Map|||
SpaceEngine|||
Redshift|||
Sky Guide|||
WinStars|||
Digistar|||
Shira Player|||
Shira Universe|||
PlanetariumVR|||
Starry Night|||
TheSky|||
WorldWide Telescope|||
XEphem|||
Google Sky|||
''')
kd('GIS and mapping software','GIS','''
Cadcorp SIS|Cadcorp||
Erdas Imagine|ERDAS, Inc.|1980
GeoMedia|||
IDRISI|||
Kosmo|||
LandSerf|||
SPRING|||
TerraLib/TerraView|||
TNTmips|||
''')
kd('Scientific and statistics software','STAT','''
Analyse-it|Analyse-it||
GAUSS|Aptech Systems||
GenStat|VSN International||
JMP|JMP Statistical Discovery LLC||
MedCalc|MedCalc Software Ltd||
Minitab|Minitab, LLC||
NCSS|NCSS, LLC||
OriginPro|OriginLab||
SAS|SAS Institute||
SPSS|IBM||
Stata|StataCorp LLC||
Statgraphics|Statgraphics Technologies Incorporated||
Statistica|Tibco Software||
StatPlus|AnalystSoft||
SYSTAT|Systat Software Inc.||
WPS Analytics|World Programming||
StatCrunch|Pearson Education||
Dataplot|Alan Heckert||
Epi Info|Centers for Disease Control and Prevention||
OpenEpi|A. Dean, K. Sullivan, M. Soe||
Salstat|Alan J. Salmoni, Mark Livingstone||
RKWard|RKWard community||
SOFA Statistics|Grant Paton-Simpson||
ROOT|ROOT Analysis Framework||
LIMDEP|Econometric Software, Inc.||
''')
kd('Plug-in format','AP','''
Virtual Studio Technology|Steinberg|1996|VST · VST3
Audio Units|Apple||AU
Avid Audio eXtension|Avid||AAX
Real Time AudioSuite|Avid||RTAS
TDM|Avid||
Rack Extension|Reason Studios||
CLAP|||
LV2|||
LADSPA|||
DSSI|||
DirectX plugin|Microsoft||
VAMP|||
Audio Random Access|Celemony Software||ARA
''',new=True)
kd('Instrument & effect bundle','NI','''
Komplete|Native Instruments||
Arturia V Collection|Arturia|2024|V Collection
Pigments|Arturia||
''',new=True)
