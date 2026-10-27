from common import *
CMP3=WP+'Comparison_of_3D_computer_graphics_software'
L3=WP+'List_of_3D_modeling_software'
m3={'n':'3D modelling software','a':'','d':'Program for modelling, sculpting and rendering three-dimensional objects.',
 't':['general-purpose suite','digital sculpting','character and figure posing','procedural and node-based','architectural and interior','rendering'],
 's':L3,'x':[
 A('Blender','Free and open-source 3D suite covering modelling, sculpting, animation and rendering, begun by Ton Roosendaal in 1994.',WP+'Blend_(file_format)',[V('Blender','Blender Foundation','1994','First released 2 January 1994; open-sourced in 2002'),V('Blender 4.2 LTS','Blender Foundation','2024','Long-term support release, July 2024')],mk='Blender Foundation',y='1994',dt='version · add-ons · render engine'),
 A('Autodesk Maya','Industry 3D animation and effects package, first released by Alias in 1998.',WP+'Autodesk_Maya',[V('Maya 1.0','Alias','1998','February 1998'),V('Autodesk Maya','Autodesk','2005','Autodesk bought Maya in October 2005')],mk='Autodesk',y='1998'),
 A('Autodesk 3ds Max','Windows-only modelling and animation program descended from DOS-era 3D Studio.',WP+'Autodesk_3ds_Max',[V('3D Studio','Yost Group','','DOS original, published by Autodesk'),V('3D Studio MAX','Kinetix','1996','Windows NT rewrite'),V('Autodesk 3ds Max','Autodesk','','Subscription; free one-year student version')],mk='Autodesk',y='1996'),
 A('Cinema 4D','Maxon\'s 3D program, strong in motion graphics; began on the Amiga.',WP+'Cinema_4D',[V('FastRay','Maxon','1991','Amiga original'),V('Cinema 4D Lite','Maxon','2014','Bundled with After Effects CC 2014'),V('Cinema 4D R12-R20','Maxon','','Four variants: Prime, Visualize, Broadcast, Studio'),V('Cinema 4D R21','Maxon','','Single version; licensing differs for commercial, educational and demo use')],mk='Maxon',y='1990'),
 A('ZBrush','Digital sculpting program presented at SIGGRAPH in 1999; Maxon bought it in 2022.',WP+'ZBrush',[V('ZBrush','Pixologic','1999','Founded by Ofer Alon and Jack Rimokh'),V('ZBrush under Maxon','Maxon','2022','Bought January 2022')],mk='Maxon',y='1999'),
 A('Houdini','Node-based procedural 3D package for effects and animation from Side Effects Software.',CMP3,[V('Houdini','Side Effects Software')],mk='Side Effects Software'),
 A('Rhinoceros 3D','Free-form NURBS surface modeller from Robert McNeel & Associates, for Windows and Mac.',WP+'Rhinoceros_3D',[V('Rhino 8','McNeel','','Latest listed release 8.33, July 2026')],mk='McNeel')],
 'm':M(('LightWave 3D','LightWave Digital'),('Modo',''),('Wings 3D',''),('3D-Coat',''),('Shapr3D',''),('Plasticity',''),('OpenSCAD','Marius Kintel'),('Sweet Home 3D',''),('Daz Studio',''),('Poser',''),('iClone','Reallusion'),('Bryce',''),('Carrara',''),('Cheetah3D',''),('form-Z','AutoDesSys'),('POV-Ray','The POV-Team'),('MeshLab',''),('BrickLink Studio',''),('LeoCAD',''),('Autodesk Mudbox','Autodesk'))}
cad_s=WP+'Comparison_of_computer-aided_design_software'
cad={'n':'CAD software','a':'','d':'Program for computer-aided design and drafting of parts, buildings and drawings.',
 't':['2D drafting','parametric solid modelling','browser-based','free and open source','architectural'],
 's':cad_s,'x':[
 A('AutoCAD','Autodesk\'s drafting and 3D design program, the 2D drafting standard.',cad_s,[V('AutoCAD','Autodesk','','Proprietary; macOS, Windows, Android, iOS')],mk='Autodesk'),
 A('Autodesk Fusion','Cloud-connected parametric CAD and CAM from Autodesk; formerly Fusion 360.',cad_s,[V('Autodesk Fusion','Autodesk','','Proprietary; Windows, macOS, web')],mk='Autodesk'),
 A('SolidWorks','Dassault Systèmes\' parametric mechanical CAD; Windows only.',L3,[V('SolidWorks','Dassault Systèmes','','Commercial')],mk='Dassault Systèmes'),
 A('FreeCAD','Free, open-source parametric 3D modeller started in 2002 by Jürgen Riegel, Werner Mayer and Yorik van Havre.',WP+'FreeCAD',[V('FreeCAD 0.0.1','','2002','29 October 2002'),V('FreeCAD 1.1','','2026','24 March 2026')],y='2002'),
 A('SketchUp','Trimble\'s easy 3D modeller used for architecture, woodworking and interiors; freemium.',L3,[V('SketchUp','Trimble','','Freemium')],mk='Trimble'),
 A('Onshape','Browser-based mechanical CAD from former SolidWorks leaders, bought by PTC in 2019.',WP+'Onshape',[V('Onshape','PTC','2012','Founded 2012; PTC deal closed November 2019'),V('Onshape Education Plan','PTC','2016','Free Professional version for students and educators')],mk='PTC',y='2012'),
 A('Tinkercad','Free browser-based 3D design tool for beginners, launched in 2011 and owned by Autodesk.',WP+'Tinkercad',[V('Tinkercad','Autodesk','2011','Autodesk announced the acquisition in May 2013')],mk='Autodesk',y='2011')],
 'm':M(('Autodesk Inventor','Autodesk'),('BricsCAD','Bricsys'),('LibreCAD',''),('QCAD','Ribbon Soft'),('DraftSight',''),('SolveSpace','Jonathan Westhues'),('TurboCAD','IMSI/Design'),('Vectorworks Fundamentals',''),('Archicad','Graphisoft'),('Solid Edge','Siemens Digital Industries Software'),('Alibre Design','Alibre, LLC'),('ZWCAD','ZWSOFT (ZWCAD Software)'))}
SL=WP+'Slicer_(3D_printing)'
sl={'n':'3D printing slicer','a':'','d':'Program that prepares a 3D model for printing by slicing it into printer instructions.',
 't':['filament (FDM)','resin','printer-maker slicer','open source'],
 's':SL,'x':[
 A('Cura','Slicer created by David Braam and maintained by Ultimaker; LGPL since 2017.',WP+'Cura_(software)',[V('Cura 2.0','Ultimaker','2015','Summer 2015'),V('UltiMaker Cura','Ultimaker')],mk='Ultimaker'),
 A('Slic3r lineage','Open-source slicers descended from Slic3r, started in 2011 in the RepRap community.',WP+'Slic3r',[V('Slic3r','Alessandro Ranellucci','2011','Latest release 1.3.0, May 2018'),V('Slic3r Prusa Edition','Prusa Research','2016','Fork by Prusa Research'),V('PrusaSlicer','Prusa Research','2019','Renamed with version 2.0, May 2019'),V('SuperSlicer','','','Fork of PrusaSlicer'),V('Bambu Studio','Bambu Lab','','Fork of PrusaSlicer'),V('OrcaSlicer','','','Fork of Bambu Studio'),V('Creality Print','Creality','','Based on Cura; fork of OrcaSlicer')],y='2011')],
 'm':M(('CHITUBOX','ChiTu Systems'),('Lychee Slicer','Mango3D'),('Simplify3D',''),('KISSlicer',''),('Elegoo Print','Elegoo'),('Anycubic Slicer Next','Anycubic'),('Formlabs PreForm','Formlabs'),('ideaMaker','Raise3D'),('Voxeldance Tango','Voxeldance'))}
TH=WP+'x'
laser={'n':'Laser & CNC control software','a':'laser software · CNC CAM','d':'Program that lays out designs and sends them to a hobby laser cutter, engraver or CNC router.',
 't':['G-code laser (GRBL)','DSP controller laser','desktop CAM','cloud CAM'],
 's':'https://www.thunderlaser.com/laser-blogs/lasergrbl-vs-lightburn.html','x':[
 A('LightBurn','Paid layout and control program for laser cutters; perpetual licence with a year of updates.','https://www.thunderlaser.com/laser-blogs/lasergrbl-vs-lightburn.html',[V('LightBurn Core','LightBurn','','G-code controllers such as GRBL, Smoothieware, Marlin, Grbl-LPC; listed at $99 in July 2026'),V('LightBurn Pro','LightBurn','','Adds DSP (Ruida, Trocen, TopWisdom) and galvo (BSL, EZCad2) controllers; $199 in July 2026')],mk='LightBurn',dt='controller type · licence tier (Core, Pro) · Windows, macOS, Linux'),
 A('LaserGRBL','Free open-source program for GRBL-based hobby lasers; Windows only.','https://www.thunderlaser.com/laser-blogs/lasergrbl-vs-lightburn.html',[V('LaserGRBL','','','Supports GRBL v0.9 and v1.1; not DSP or galvo controllers')]),
 A('Easel','Inventables\' cloud-based CNC design and toolpath program; exports G-code for other machines.','https://forum.easel.com/t/carbide-vs-easel/95708',[V('Easel','Inventables','','Needs internet; uses web fonts')],mk='Inventables'),
 A('Carbide Create','Carbide 3D\'s offline desktop CAD/CAM program for CNC routers.','https://forum.easel.com/t/carbide-vs-easel/95708',[V('Carbide Create','Carbide 3D','','Works offline with locally installed fonts')],mk='Carbide 3D')]}
circ={'n':'Circuit design software','a':'EDA software · PCB design software','d':'Program for drawing electronic schematics, laying out printed circuit boards and checking them for manufacture.',
 't':['schematic and PCB layout','circuit simulator','browser-based','free and open source','beginner breadboard view'],
 's':WP+'Comparison_of_EDA_software','x':[
 A('KiCad','Free open-source schematic and PCB suite begun by Jean-Pierre Charras in 1992; CERN contributed developers.',WP+'KiCad',[V('KiCad','KiCad Developers','1992','GPL-3.0; Linux, macOS, Windows')],y='1992'),
 A('EAGLE','Scriptable schematic and PCB tool from CadSoft (1988), bought by Autodesk in 2016; support ends 7 June 2026.',WP+'EAGLE_(EDA_tool)',[V('EAGLE','CadSoft','1988','Founded by Rudolf Hofer and Klaus-Peter Schmidinger'),V('EAGLE Free edition','Autodesk','','From version 8.0.0; 2 schematic sheets, 2 layers, 80 cm2 board, non-commercial'),V('EAGLE end of support','Autodesk','2026','Support ends 7 June 2026')],mk='Autodesk',y='1988'),
 A('Altium Designer','Professional PCB suite from Altium (founded as Protel Systems, 1985); free CircuitMaker was its maker tool.',WP+'ACCEL_Technologies,_Inc.',[V('Altium Designer','Altium','','Windows; Altium became a Renesas subsidiary in August 2024'),V('CircuitMaker','Altium','','Free maker tool, no longer actively developed')],mk='Altium',y='1985'),
 A('EasyEDA','Browser-based schematic, simulation and PCB tool from JLCPCB\'s parent group, first released August 2013.',WP+'EasyEDA',[V('EasyEDA','JiaLiChuang (HongKong) Co., Limited','2013')],y='2013')],
 'm':M(('DipTrace','Novarm'),('LibrePCB','LibrePCB Team'),('Fritzing',''),('Proteus Design Suite','Labcenter Electronics'),('OrCAD','Cadence Design Systems'),('LTspice','Analog Devices'),('Qucs','Qucs Developers'),('gEDA','gEDA Project'),('DesignSpark PCB','RS Components'),('NI Multisim','National Instruments'),('FreePCB','FreePCB community'),('TINA','DesignSoft'))}
pg={'n':'Photogrammetry software','a':'','d':'Program that builds 3D models or measured maps from sets of overlapping photographs.',
 't':['desktop reconstruction','phone scanning app','drone mapping','free and open source'],
 's':WP+'Comparison_of_photogrammetry_software','x':[
 A('Agisoft Metashape','Photogrammetry program from Agisoft (St Petersburg), formerly PhotoScan, sold as a perpetual licence.',WP+'Metashape',[V('Metashape Standard','Agisoft','2010','For interactive media work'),V('Metashape Pro','Agisoft','','For authoring GIS content')],mk='Agisoft',y='2010'),
 A('RealityCapture','Photogrammetry program from Capturing Reality, bought by Epic Games in 2021 and renamed RealityScan 2.0 in 2025.',WP+'RealityCapture',[V('RealityCapture public beta','Capturing Reality','2016','2 February 2016'),V('RealityCapture free tier','Epic Games','2024','Free for individuals, students, educators and firms under US$1 million revenue'),V('RealityScan 2.0','Epic Games','2025','Merged with the RealityScan mobile app, June 2025')],mk='Capturing Reality',y='2016'),
 A('Meshroom','Free, open-source node-based photogrammetry program built on the AliceVision framework (MPL 2.0).','https://alicevision.readthedocs.io/en/latest/',[V('Meshroom','AliceVision')]),
 A('Polycam','Phone and tablet scanning app with LiDAR and photo modes; free, Pro and Business tiers.','https://www.skyebrowse.com/news/posts/polycam-review',[V('Polycam LiDAR mode','Polycam','','Needs iPhone 12 Pro or later, iPad Pro 2020 or later'),V('Polycam Photo mode','Polycam','','Works on more devices; slower')],mk='Polycam')],
 'm':M(('3DF Zephyr','3DFLOW'),('Pix4Dmapper','Pix4D'),('OpenDroneMap','OpenDroneMap'),('PhotoModeler','Eos Systems'),('Qlone','EyeCue Vision Technologies'))}
emb={'n':'Embroidery digitising software','a':'embroidery software','d':'Program that turns artwork or lettering into stitch files for an embroidery machine.',
 't':['digitising','editing and lettering only','free and open source','machine-maker software'],
 's':'https://www.embpunch.com/blog/best-embroidery-digitizing-software','x':[
 A('Hatch Embroidery','Wilcom\'s hobbyist embroidery program, sold in several levels with a free trial.','https://www.embpunch.com/blog/best-embroidery-digitizing-software',[V('Hatch 3','Wilcom','','Multiple levels for different skill levels')],mk='Wilcom'),
 A('Embrilliance','Embrilliance\'s embroidery software.','https://www.embpunch.com/blog/best-embroidery-digitizing-software',[V('Embrilliance','Embrilliance')],mk='Embrilliance'),
 A('Ink/Stitch','Embroidery software named in the review list.','https://www.embpunch.com/blog/best-embroidery-digitizing-software',[V('Ink/Stitch','')])],
 'm':M(('Wilcom','Wilcom'),('Embird','Embird'),('Bernina Embroidery Software','Bernina'),('PE-Design','Brother'),('Janome Digitizer','Janome'))}
brands=[B('Autodesk','United States','1982','Professional & flagship','CAD, 3D, media','American maker of AutoCAD, Maya, 3ds Max and Fusion.'),
 B('Dassault Systèmes','France','1981','Professional & flagship','SolidWorks, CATIA','French maker of SolidWorks and CATIA.'),
 B('Trimble','United States','1978','Professional & flagship','SketchUp, surveying','American company that owns SketchUp.'),
 B('PTC','United States','1985','Professional & flagship','Creo, Onshape','American maker of Creo and Onshape.'),
 B('Maxon','Germany','','Professional & flagship','Cinema 4D, ZBrush','German maker of Cinema 4D; owns ZBrush.',s=WP+'Cinema_4D'),
 B('Blender Foundation','Netherlands','2002','Artisan & independent','Blender','Non-profit founded in May 2002 to develop Blender.',s='https://en.wikipedia.org/wiki/Blend_(file_format)'),
 B('Altium','Australia','1985','Professional & flagship','PCB design','Founded as Protel Systems in Australia; now a Renesas subsidiary.',s=WP+'ACCEL_Technologies,_Inc.'),
 B('Agisoft','Russia','','Specialist','photogrammetry','St Petersburg maker of Metashape.',s=WP+'Metashape'),
 B('Capturing Reality','Slovakia','2013','Specialist','RealityCapture','Bratislava company bought by Epic Games in 2021.',s=WP+'RealityCapture'),
 B('Prusa Research','Czech Republic','2012','Premium','3D printers','Czech 3D printer maker and PrusaSlicer developer.'),
 B('Bambu Lab','China','2020','Mainstream','3D printers','Chinese 3D printer maker behind Bambu Studio.'),
 B('Ultimaker','Netherlands','2011','Premium','3D printers, Cura','Dutch 3D printer maker that maintains Cura.')]
notes=('3D modelling software cut from 72 to 7 archetypes (Blender, Maya, 3ds Max, Cinema 4D, ZBrush, Houdini, Rhino) plus 20 flat; dropped dead or niche (Softimage, trueSpace, Silo, Amapi, Aladdin4D, Animation:Master, VistaPro, E-on Vue, Electric Image, Hexagon, Realsoft, Art of Illusion, Anim8or and similar), trade/research (CityEngine, MASSIVE, Quake Army Knife) and non-3D-modelling tools (Oculus Medium, 3D Slash). '
 'CAD software cut from 59 to 7 archetypes plus 12; dropped trade, building-services and industrial CAD (FINE MEP, CATIA, NX, Creo, MicroStation, Tekla, Allplan, Cadwork, HiCAD, Caddie, Digital Project, BRL-CAD, KeyCreator, T-FLEX, SpaceClaim, Revit). Blender and Rhino stay on the 3D modelling kind. '
 '3D printing slicer 18 to 2 archetypes plus 9 (dropped Skeinforge). New kinds Laser & CNC control software and Embroidery digitising software are sourced from reviews and a forum thread because no Wikipedia pages were found; LaserWeb, K40 Whisperer, Embrilliance editions and Ink/Stitch details were not on any retrieved page and are omitted. '
 'Circuit design 31 to 4 archetypes plus 12 (added EasyEDA and Fritzing from the retrieved comparison page; dropped industrial EDA: PSpice, SaberRD, ADS, Zuken CR/CADSTAR, PSIM, PowerEsim, Pulsonix, Micro-Cap, AutoCAD Electrical and similar). Photogrammetry 12 to 4 archetypes plus 5; dropped SOCET SET, IMAGINE Photogrammetry, Ames Stereo Pipeline (survey/defence/research), 3Dsurvey and dead Photosynth.')
put('04_02',{'kinds':[m3,cad,sl,laser,circ,pg,emb],'brands':brands,'traditions':[],'notes':notes})
