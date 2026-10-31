from data import K,R,kd
R['PG']='https://en.wikipedia.org/wiki/Comparison_of_photogrammetry_software'
R['AR']='https://en.wikipedia.org/wiki/List_of_amateur_radio_software'
R['RL']='https://www.rtl-sdr.com/big-list-rtl-sdr-supported-software/'
R['ADBE']='https://www.sec.gov/Archives/edgar/data/796343/000079634325000135/adbeex991q425.htm'
R['ADSK']='https://www.sec.gov/Archives/edgar/data/769397/000076939726000010/q426pressrelease.htm'
R['PE']='https://www.production-expert.com/production-expert-1/2025-daw-survey-the-results'
R['ADOBE']='https://en.wikipedia.org/wiki/Adobe_Inc.'
R['AUTODESK']='https://en.wikipedia.org/wiki/Autodesk'
R['ABL']='https://en.wikipedia.org/wiki/Ableton'
R['AVID']='https://en.wikipedia.org/wiki/Avid_Technology'
R['BMD']='https://en.wikipedia.org/wiki/Blackmagic_Design'
R['STB']='https://en.wikipedia.org/wiki/Steinberg'
R['MAYA']='https://en.wikipedia.org/wiki/Autodesk_Maya'
R['BLN']='https://en.wikipedia.org/wiki/Blender_(software)'
R['MAX']='https://en.wikipedia.org/wiki/Autodesk_3ds_Max'
R['C4D']='https://en.wikipedia.org/wiki/Cinema_4D'
R['STL']='https://en.wikipedia.org/wiki/Stellarium_(software)'
R['LR']='https://en.wikipedia.org/wiki/Adobe_Lightroom'
R['CUB']='https://en.wikipedia.org/wiki/Cubase'
R['FLS']='https://en.wikipedia.org/wiki/FL_Studio'
R['KON']='https://en.wikipedia.org/wiki/Kontakt_(software)'
def add(name,rows,ref=None):
    if name not in K: kd(name,'MUS','')
    K[name]['rows']+= [r.strip() for r in rows.strip().split('\n') if r.strip()]
add('DJ software','''
Final Scratch@MUS|||
''')
kd('Music tracker','MUS','''
SoundMonitor||1986|
NoiseTracker||1989|
OctaMED||1989|
Protracker||1990|
ScreamTracker||1994|
SoundTracker|||
MilkyTracker|||
Buzztrax|||
Jeskola Buzz|||
''')
kd('Audio editor','MUS','''
Ecasound|||
WaveSurfer|||
''')
kd('Music-learning app','MUS','''
Meludia|||
EarMaster|||
EarSketch|||
GNU Solfege|||
Hyperscore|||
Rocksmith|||
Synthesia|||
Chordify|||
GibsonApp|||
''')
add('Digital audio workstation','''
AudioMulch|||
''')
kd('Photogrammetry software','PG','''
3Dsurvey|3Dsurvey d.o.o.|2014
Ames Stereo Pipeline|NASA|
IMAGINE Photogrammetry|Hexagon Geospatial|2009
SOCET SET|BAE Systems|
''')
kd('Ham radio software','AR','''
CW Skimmer|||CW decoding
EchoLink|||VoIP
IRLP|||VoIP
Winlink|||Email and messaging
WSJT-Z|||Digital modes
WSPR|||Digital modes
Pat|||Winlink client
Xlog|||Logging
klog|||Logging
QLog|||Logging
Emacs QSO Logger|||Logging
Amateur Contact Log|N3FJP||Logging
HamLogBook|K6REA||Logging
Winlog32|G0CUZ||Logging
HAMRS|||Logging
Picondo|||Logging
World Radio League|||Logging
QSO Director|||Logging
QSOMate|||Logging
MMSSTV|||SSTV
QSSTV|||SSTV
SPLAT!|||Propagation modelling
RepeaterBook|||Repeater finder
RepeaterSTART|||Repeater finder
RFINDER|||Repeater finder
GridTracker|||WSJT-X data display
HamSphere|||VoIP and simulation
HamTools|||Utilities
QCluster|||DX cluster
LY4A DX Reminder|||DX alerts
CommTrak|Tamatu Systems NZ||Logging and mapping
Pycom Radio Controller|||Rig control
Flarq|||Digital modes
Robust-Chat|||Digital modes
CWGet|||CW decoding
Orbitron|||Satellite tracking
''')
kd('SDR software','RL','''
SDR++|||
SDR--@AR|||
SDR-RADIO.COM|||
Linrad|||
CubicSDR|||
Studio1|||
SDRUno|||
SigDigger|||
ShinySDR|||
WebRadio|||
OpenWebRX|||
SDR Touch|||
PowerSDR|||
QtRadio|||
QIRX SDR|||
Zeus Radio|||
Sodira|||
cuSDR|||
Kukuruku|||
QuestaSDR|||
''')
# facts confirming converted entries: name|ref|year|maker
FACTS='''
PhotoLine|RA|1995|Computerinsel
Corel PaintShop Pro|RA|1992|Corel
G'MIC|RA|2008|David Tschumperlé
Acorn|RA|2007|Flying Meat
IrfanView|RA|1996|Irfan Skiljan
Photopea|RA|2013|Ivan Kutskir
Pinta|RA|2010|Jonathan Pobst
Microsoft Paint|RA|1985|Microsoft
XnView MP|RA|2008|Pierre-emmanuel Gougelet
GraphicConverter|RA|1992|Thorsten Lemke
ImageJ|RA|1997|Wayne Rasband
Xara Photo & Graphic Designer|RA|1995|Xara
Zoner Photo Studio|RA||Zoner
Pixlr|RA|2008|Ola Sevandersson
Photos (Apple)|RA|2014|Apple
ACDSee|RA||ACD Systems
Iridient Developer|RA|2004|Iridient Digital
digiKam|RA|2002|digiKam team
Digital Photo Professional|RA||Canon
RawTherapee|RA|2006|Gabor Horvath
Flux|T2I|2024|Black Forest Labs
Imagen|T2I|2023|Google
HiDream|T2I|2025|HiDream-AI
Ideogram|T2I|2023|Ideogram
Recraft|T2I|2023|Recraft, Inc.
Aurora|T2I|2024|xAI
Google Drawings|VE|2010|Google
Boxy SVG|VE|2013|Jarosław Foksa
Penpot|VE|2021|Kaleidos
VectorStyler|VE|2021|Numeric Path
LibreOffice Draw|VE|2011|The Document Foundation
OmniGraffle|VE|2000|The Omni Group
Xara Designer Pro+|VE|1995|Xara
Autodesk Mudbox|L3D||Autodesk
form-Z|L3D||AutoDesSys, Inc.
LightWave 3D|L3D||Lightwave Digital
iClone|L3D||Reallusion
POV-Ray|L3D||
3D-Coat|L3D||
Bryce|L3D||Daz Productions
Carrara|L3D||Daz Productions
Cheetah3D|L3D||
Daz Studio|L3D||
MeshLab|L3D||
Modo|L3D||The Foundry
Poser|L3D||Bondware
Wings 3D|L3D||
OpenSCAD|CAD||
Gelato|L3D||NVIDIA
mental ray|L3D||NVIDIA
RenderMan|L3D||Pixar
3Delight|L3D||
Aqsis|L3D||
Brazil R/S|L3D||
Kerkythea|L3D||
LuxRender|L3D||
Maxwell Render|L3D||
Octane Render|L3D||
Sunflow|L3D||
V-Ray|L3D||
Alibre Design|CAD||Alibre, LLC
AutoCAD|CAD||Autodesk
Autodesk Fusion|CAD||Autodesk
Autodesk Inventor|CAD||Autodesk
BricsCAD|CAD||Bricsys
Archicad|CAD||Graphisoft
TurboCAD|CAD||IMSI/Design, LLC
SolveSpace|CAD||Jonathan Westhues
QCAD|CAD||Ribbon Soft
Solid Edge|CAD||Siemens Digital Industries Software
ZWCAD|CAD||ZWSOFT
LibreCAD|CAD||
CircuitMaker|EDA||Altium
LTspice|EDA||Analog Devices
OrCAD|EDA||Cadence Design Systems
TINA|EDA||DesignSoft
FreePCB|EDA||
gEDA|EDA||gEDA Project
KTechLab|EDA||KTechLab Developers
Proteus Design Suite|EDA||Labcenter Electronics
NI Multisim|EDA||National Instruments
DipTrace|EDA||Novarm
Qucs|EDA||Qucs Developers
DesignSpark PCB|EDA||RS Components
XCircuit|EDA||Tim Edwards
Pulsonix|EDA||WestDev
CADSTAR|EDA||Zuken
atopile|EDA||
Flux.ai|EDA||
Fritzing|EDA||
Ngspice|EDA||
pcb-rnd|EDA||
TARGET 3001!|EDA||
tscircuit|EDA||
3DF Zephyr|PG|2013|3DFLOW
PhotoModeler|PG|1994|Eos Systems
Qlone|PG|2017|EyeCue Vision Technologies
OpenDroneMap|PG|2013|OpenDroneMap
Pix4Dmapper|PG|2011|Pix4D
Scriptware|SW||Cinovation
Scrite|SW||
Sophocles|SW||
Dramatica|SW||
Cherry Draft|SW||
Adobe Captivate|SCR||Adobe
Snapz Pro X|SCR||Ambrosia Software
QuickTime X|SCR|2009|Apple
Bandicam|SCR||Bandicam Company
Fraps|SCR||Beepa Pty Ltd
BB FlashBack|SCR||Blueberry Software
CamStudio|SCR||CamStudio.org
ShareX|SCR||Jaex and Michael Delpach
SimpleScreenRecorder|SCR||maartenbaert
Xbox Game Bar|SCR||Microsoft
Debut|SCR||NCH Software
Nvidia ShadowPlay|SCR||Nvidia
OBS Studio|SCR||OBS Project
Peek|SCR||Philipp Wolfer
ScreenPal|SCR||ScreenPal
HyperCam|SCR||Solveig Multimedia
recordMyDesktop|SCR||SourceForge
XSplit Broadcaster|SCR||SplitmediaLabs
Camtasia|SCR|2002|TechSmith
ScreenFlow|SCR||Telestream
Snagit|SCR||TechSmith
Corel VideoStudio|VID|1993|Corel
CyberLink PowerDirector|VID|2001|CyberLink
VSDC Free Video Editor|VID|2008|Flash-Intergro LLC
EDIUS|VID|2002|Grass Valley
Lightworks|VID|1989|LWKS
Magix Movie Edit Pro|VID|2001|MAGIX
Shotcut|VID|2011|Meltytech, LLC
Pinnacle Studio|VID|1999|Pinnacle Systems
Flowblade|VID|2012|Open Source Community
Kdenlive|VID|2002|Open Source Community
OpenShot|VID|2008|Open Source Community
Avidemux|VID||
VirtualDub|VID|2000|Avery Lee
Pencil2D|VE|2005|Pascal Naidon, Patrick Corrieri
Mixcraft|DAW||Acoustica
Ardour|DAW||The Ardour Community
Cakewalk Sonar|DAW||BandLab Technologies
ACID Pro|DAW||Boris FX
Mixbus|DAW||Harrison Consoles
Magix Music Maker|DAW||MAGIX
Samplitude|DAW||MAGIX
LMMS|DAW||Tobias Doerffel
Waveform|DAW||Tracktion Software Corporation
BandLab|DAW||BandLab Technologies
Band-in-a-Box|MUS||
Soundtrap|MUS||
Acoustica|MUS||Acon Digital
Total Recorder|MUS||High Criteria
SpectraLayers|MUS||Steinberg
WaveLab|MUS||Steinberg
GoldWave|MUS||
SoX|MUS||
WavePad Audio Editor|MUS||
mp3DirectCut|DAW||Martin Pesch
CrossDJ|MUS||
Deckadance|MUS||
Mixxx|MUS||
MilkyTracker|MUS||
Capella|SC||capella-software AG
Denemo|SC||Benham, Shann
Encore|SC||Passport Music Software
Forte|SC||Lugert Verlag GmbH
Frescobaldi|SC||Wilbert Berendsen
NoteWorthy Composer|SC||NoteWorthy Software
Overture|SC||Sonic Scores
ScoreCloud|SC||Doremir Music Research AB
SmartScore|SC||Musitek Corporation
AIMP|AUD|2006|AIMP DevTeam
iTunes|AUD|2001|Apple
foobar2000|AUD|2002|Peter Pawlowski
MusicBee|AUD|2008|Steven Mayall
PotPlayer|VPL|2006|Kakao
Plex Media Player|VPL|2008|Plex
Kodi|VPL|2002|Team Kodi
VLC media player|VPL|2001|VideoLAN
mpv|VPL|2013|mpv Community
QuickTime|VPL|1991|Apple
Windows Media Player|VPL|1992|Microsoft
Winamp|VPL|1997|Nullsoft
Nexus|VST||reFX
Vanguard|VST||reFX
Gladiator|VST||Tone2
Discovery|VST||Tone2
Komplete|NI||Native Instruments
Audio Units|AP||Apple
Avid Audio eXtension|AP||Avid
Real Time AudioSuite|AP||Avid
TDM|AP||Avid
Audio Random Access|AP||Celemony Software
DirectX plugin|AP||Microsoft
Rack Extension|AP||Reason Studios
CLAP|AP||
DSSI|AP||
LADSPA|AP||
LV2|AP||
VAMP|AP||
Family Historian|GEN||
Family.Show|GEN||
GEDitCOM|GEN||
Genbox Family History|GEN||
Genealogica Grafica|GEN||
GenealogyJ|GEN||
GeneWeb|GEN||
GenoPro|GEN||
Gramps Web|GEN||
Kith and Kin Pro|GEN||
LifeLines|GEN||
My Family Tree|GEN||
Personal Ancestral File|GEN||
PhpGedView|GEN||
The Master Genealogist|GEN||
TNG|GEN||
TreeDraw|GEN||
Ancestral Quest|GEN||
Brother's Keeper|GEN||
Reunion|GEN||
Ancestry.com|GEN||
Familio|GEN||
FamilySearch|GEN||
Findmypast|GEN||
GEDmatch|GEN||
GenealogyBank|GEN||
Geneanet|GEN||
Genes Reunited|GEN||
Geni.com|GEN||
MyHeritage|GEN||
Rodovid|GEN||
WeRelate|GEN||
WikiTree|GEN||
DXLab|AR||AA6YQ
Ham Radio Deluxe|AR||
Log4OM|AR||
MacLoggerDX|AR||
flrig|AR||
SDR#|AR||
SDRangel|AR||
Gqrx|RL||
HDSDR|RL||
Cadcorp SIS|GIS||Cadcorp
GeoMedia|GIS||
gvSIG|GIS||
IDRISI|GIS||
ILWIS|GIS||
Kosmo|GIS||
LandSerf|GIS||
Manifold System|GIS||
MapWindow GIS|GIS||
SAGA GIS|GIS||
SPRING|GIS||
TerraLib/TerraView|GIS||
TNTmips|GIS||
uDig|GIS||
MapInfo Pro|GIS||Pitney Bowes
Maptitude|GIS||
PSPP|STAT||GNU Project
GraphPad Prism|STAT||GraphPad Software, Inc.
EViews|STAT||IHS Markit
JASP|STAT||JASP team, University of Amsterdam
gretl|STAT||The gretl Team
jamovi|STAT||The jamovi project
Orange|STAT||Bioinformatics Laboratory, University of Ljubljana
Maple|STAT||Maplesoft
SageMath|STAT||
Astrarium|PL||
'''
NOTES={'AC3D':'Modeller that began on the Amiga.','Anim8or':'Freeware modelling and animation package.','Animation:Master':'Spline-based modelling and animation, strong in character work.',
'Cheetah3D':'Proprietary Mac program aimed mainly at amateurs.','CityEngine':'Generates large urban 3D environments procedurally.','Clara.io':'Browser-based modelling with real-time collaboration.',
'Daz Studio':'Free tool for posing and rendering; imports Poser models.','Electric Image Animation System':'Known for rendering speed; no built-in modeller.','form•Z':'Solid and surface modeller with rendering and animation.',
'Hexagon':'Subdivision modeller for organic forms.','iClone':'Real-time animation for previsualisation, games and face and body animation.','LightWave 3D':'Began on the Amiga; used in television and film.',
'MakeHuman':'Generates parametric 3D humanoids.','MASSIVE':'Crowd animation system used for large battle scenes.','MeshLab':'Free viewer, processor and converter for 3D meshes.',
'Modo':'Subdivision modelling, texturing and rendering.','Mudbox':'Brush-based high-resolution sculpting; acquired by Autodesk in 2007.','Poser':'Rendering and animation tool for human figures.',
'Realsoft 3D':'Modelling, animation, simulation and rendering on several platforms.','Silo':'Subdivision-surface modeller.','Substance 3D':'Suite of 3D model and texture authoring tools.','Terragen':'Scenery generator.',
'Vue':'Creates and renders natural 3D environments.','Wings 3D':'BSD-licensed subdivision modeller.','3D-Coat':'Digital sculpting with voxels and polygons.','Carrara':'Complete toolset for modelling, texturing, animation and rendering.',
'Bryce':'Known for landscapes; development has stopped.','3Delight':'Path-tracing renderer using the NSI API and OSL.','Aqsis':'Free, open-source renderer compatible with the RenderMan standard.',
'Brazil R/S':'Rendering engine for 3ds Max, Rhino and VIZ.','Kerkythea':'Freeware ray tracer that works with several 3D applications.','LuxRender':'Open-source unbiased renderer using Metropolis light transport.',
'Maxwell Render':'Physics-based multi-platform renderer, claimed as the first unbiased renderer on the market.','mental ray':'Renderer bundled with many high-end packages.','Octane Render':'Unbiased renderer accelerated by NVIDIA GPUs through CUDA.',
'RenderMan':'Renderer used by many studios, often fed by other animation packages.','Sunflow':'Open-source photo-realistic renderer written in Java.','V-Ray':'Renderer used mainly for architectural visualisation.','POV-Ray':'Freeware ray tracer with source code, for several platforms.','Gelato':'Hardware-accelerated, non-real-time renderer.',
'CATIA':'CAD, CAE and CAM software with 3D modelling and rendering.','BRL-CAD':'Open-source solid modelling CAD with ray tracing, developed since 1984.','OpenSCAD':'Script-driven solid modeller.',
'SolveSpace':'Free, open-source constraint-based 2D and 3D CAD.','Solid Edge':'Design, drafting, analysis and simulation for products and machines.','SketchUp':'Sketch-based modelling linked to Google Earth.',
'Poser':'Rendering and animation tool for human figures.','Final Scratch':'Listed among DJ software.',
'Winlink':'Email and messaging over radio.','Neon':'First VST instrument, included with Cubase VST 3.7.','Csound':'Sound-synthesis language from the MIT Media Lab.',
'Alchemy':'Synthesiser in Logic Pro, originally by Camel Audio.','Generator':'Native Instruments synthesis program from 1997; precursor of Reaktor.','Virtual Studio Technology':'Steinberg plug-in standard; the first VST plug-ins shipped with Cubase 3.02.',
'Komplete':'Native Instruments product bundle.','Ames Stereo Pipeline':'NASA open-source stereo photogrammetry tool.'}
for n in ['CityEngine']: pass
VERS={
'Blender':[('Blender 1.00','1995','First release, with Ton Roosendaal as primary author'),('Blender 2.25','2002','Last release before NaN closed; added the Suzanne test model'),('Blender 2.61','2011','Included the Cycles render engine'),('Blender 2.8','2019','Removed the game engine and Blender Internal; added EEVEE'),('Blender 3.0','','Cycles X replaced the old Cycles engine'),('Blender 4.2 LTS','2024','EEVEE Next overhaul')],
'Autodesk Maya':[('Maya 1.0','1998','First release'),('Maya 2.0','1999','Added Windows support'),('Maya 3.0','2000','First Linux version'),('Maya 4.5','2002','Added macOS support'),('Maya 5.0','2003','Added mental ray'),('Maya 8.0','2006','First 64-bit and first Autodesk version'),('Maya 2008','2007','Versioning became year-based'),('Maya 2012','2011','Added Viewport 2.0'),('Maya 2016','2015','Added XGen and Bifrost'),('Maya 2018','2017','Added MASH'),('Maya 2022','2021','Added USD support'),('Maya 2024','2023','Native Apple silicon support'),('Maya 2026','2025','OpenPBR the default material')],
'Autodesk 3ds Max':[('3D Studio Release 1.0','1990','MS-DOS'),('3D Studio Release 4.0','1994','Last DOS release'),('3D Studio MAX 1.0','1996','First Windows NT version'),('3D Studio MAX R2','1997','Added Windows 95 support'),('Discreet 3dsmax 7','2004','Re-released with the Autodesk logo'),('3ds Max 9','2006','First version for x64 hardware'),('3ds Max 2008','2007','Added Scene Explorer'),('3ds Max 2016','2015','Introduced Max Creation Graph'),('3ds Max 2018','2017','Arnold renderer integrated'),('3ds Max 2021','2020','Arnold the default renderer'),('3ds Max 2025','2024','Latest listed on the page')],
'Cinema 4D':[('FastRay','1991','Amiga; first name of Cinema 4D'),('Cinema 4D V1','1993','Amiga'),('Cinema 4D V4','1996','First for Windows and Macintosh'),('Cinema 4D XL V5','1997','First production-worthy version'),('Cinema 4D R8','2002','Introduced a modular system'),('Cinema 4D R10','2006','BodyPaint 3D integrated'),('Cinema 4D R12','2010','Python integration'),('Cinema 4D R13','2011','Physical Render engine'),('Cinema 4D R21','2019','Single unified version, no separate editions'),('Cinema 4D S26','2022','Redshift integration'),('Cinema 4D 2024','2023','Rigid body simulation')],
'Stellarium':[('Stellarium 0.7.1','2006','Gold Education award, Les Trophées du Libre'),('Stellarium 25.1','2025','First version to use Gaia DR3 catalogue data')],
'Lightroom Classic':[('Lightroom 1.0','2007','Shipped 19 February 2007, priced at US$299'),('Lightroom 6','2017','Last perpetual-licence version'),('Lightroom Classic CC','2017','Renamed from Lightroom when Lightroom CC arrived'),('Lightroom Classic','2019','CC dropped from the name')],
'Lightroom':[('Lightroom for iPad','2014','Released 8 April 2014'),('Lightroom Mobile for Android','2015','Released 15 January 2015'),('Lightroom CC','2017','Released 18 October 2017'),('Lightroom','2019','CC dropped from the name')],
'Cubase':[('Cubase 1.0','1989','MIDI-only sequencer for the Atari ST'),('Cubase VST 3.7','1999','Introduced the VSTi interface for software instruments'),('Cubase 4','2006','Control room feature'),('Cubase 6','2011','Five editions with different track limits')],
'FL Studio':[('FruityLoops 1.0.0','1997','Partial release, 18 December 1997, by Didier Dambrin'),('FL Studio for macOS','2018','Added macOS compatibility'),('FL Studio 2024','2024','Added the CLAP plug-in format')],
'Kontakt':[('Kontakt 6','2018','Reviewed September 2018'),('Kontakt 8','2024','Reviewed December 2024')],
}
OWNMAP={'Adobe':('Adobe','Global group','United States'),'Autodesk':('Autodesk','Global group','United States'),'Ableton':('Ableton','Independent','Germany'),'Avid Technology':('Symphony Technology Group','Independent','United States'),
'Blackmagic Design':('Blackmagic Design','Independent','Australia'),'Steinberg':('Yamaha Corporation','Independent','Germany'),'Image-Line':('Image-Line Software','Independent','Belgium')}
OWNY={'Autodesk Mudbox':'2007','Mudbox':'2007','Autodesk EAGLE':'2016','EAGLE':'2016','Aldus PageMaker':'1994','Adobe Audition':'2003','Sibelius':'2006','Substance 3D':'2019','DaVinci Resolve':'2009','Fusion':'2014','Fairlight':'2016','Avid Technology':'2023','Pro Tools':'','Logic Pro':''}
MS={'Photo, design & 3D':[
{'mkt':'Adobe, all segments','who':'Adobe Digital Media segment','share':'US$17.65 billion','yr':2025,'s':R['ADBE'],'note':'segment revenue, fiscal year ended 28 November 2025, of total revenue US$23.77 billion'},
{'mkt':'Adobe Digital Media annual recurring revenue','who':'Adobe','share':'US$19.20 billion','yr':2025,'s':R['ADBE'],'note':'exiting fiscal 2025'},
{'mkt':'Autodesk revenue by product family','who':'AutoCAD and AutoCAD LT','share':'US$1,787 million','yr':2026,'s':R['ADSK'],'note':'fiscal year ended 31 January 2026, of total revenue US$7,206 million'},
{'mkt':'Autodesk revenue by product family','who':'Architecture, engineering, construction and operations','share':'US$3,583 million','yr':2026,'s':R['ADSK'],'note':'fiscal 2026'},
{'mkt':'Autodesk revenue by product family','who':'Manufacturing','share':'US$1,379 million','yr':2026,'s':R['ADSK'],'note':'fiscal 2026'}],
'Video & animation':[
{'mkt':'Autodesk revenue by product family','who':'Media and entertainment (Maya, 3ds Max, Flame)','share':'US$332 million','yr':2026,'s':R['ADSK'],'note':'fiscal year ended 31 January 2026; 4.6 % of total revenue of US$7,206 million'},
{'mkt':'Adobe Digital Media segment (includes Premiere Pro and After Effects)','who':'Adobe','share':'US$17.65 billion','yr':2025,'s':R['ADBE'],'note':'segment revenue, fiscal year ended 28 November 2025'}],
'Music & audio':[
{'mkt':'Professional DAW survey, 2,500+ respondents (multiple answers allowed)','who':'Pro Tools','share':'ranked first, "leads by a wide margin"','yr':2025,'s':R['PE'],'note':'Production Expert survey; the text gives rankings only, with Logic Pro second and Cubase with Nuendo narrowly third'}]}
MSUM={'Photo, design & 3D':'Two vendors publish segment figures: Adobe reports Digital Media revenue, and Autodesk reports revenue by product family. Neither page gives a market share.',
'Video & animation':'Autodesk reports media and entertainment revenue; Adobe reports Digital Media as one segment. No page fetched gives video-editing market shares.',
'Music & audio':'The only fetched survey of DAW use publishes rankings, not percentages.'}

for n in ('Ham radio software',):
    K[n]['notecol']=True
K['Ham radio software']['notecol']=True
