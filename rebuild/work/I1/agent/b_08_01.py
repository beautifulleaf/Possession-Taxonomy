from common import *
PS=WP+'Planetarium_software'
CS=WP+'Comparison_of_statistical_packages'
pl={'n':'Planetarium software','a':'','d':'Program that shows the sky for a chosen place and time and simulates the motion of sky objects.',
 't':['desktop planetarium','phone sky map','3D universe explorer','telescope control'],
 's':PS,'x':[
 A('Stellarium','Free open-source planetarium begun by Fabien Chereau in 2001; the beginner default on Linux, Mac and Windows.',WP+'Stellarium_(software)',[V('Stellarium','Stellarium team','2001','GPL v2 or later'),V('Stellarium Mobile','Stellarium team','','Port with limited functions for Android and iOS')],y='2001'),
 A('Celestia','3D space simulator by Chris Laurel that lets you fly through the universe; first released 26 February 2001.',WP+'Celestia',[V('Celestia 1.6.4','Celestia Development Team','2023','5 November 2023'),V('Celestia 1.7 beta','Celestia Development Team','2026','Beta builds; released on Steam in 2026')],y='2001'),
 A('KStars','KDE planetarium with the Ekos astrophotography suite (INDI telescope, camera and focuser control).',WP+'KStars',[V('KStars 3.8.0','KDE','2025','3 December 2025'),V('Ekos','KDE','','Capture, autofocus, autoguiding and sequence manager inside KStars')],mk='KDE'),
 A('Cartes du Ciel','Free planetarium and star chart by Patrick Chevalley, with telescope control; GPLv2 since version 3.',WP+'Cartes_du_Ciel',[V('Cartes du Ciel 4.2.1','Patrick Chevalley','2019','24 November 2019'),V('Cartes du Ciel 4.3 preview','Patrick Chevalley','2024','December 2024')]),
 A('SkySafari','Proprietary sky-chart app for iOS, Android and macOS.',PS,[V('SkySafari','')])],
 'm':M(('Starry Night',''),('TheSky',''),('WorldWide Telescope',''),('Google Sky','Google'),('XEphem',''))}
astro={'n':'Astrophotography software','a':'astro imaging software','d':'Program that captures, stacks and processes images of the night sky, or controls the camera, mount and guiding that make them.',
 't':['capture and sequencing','stacking','processing','autoguiding','planetary'],
 's':'https://astrobackyard.com/astrophotography-image-stacking-software/','x':[
 A('PixInsight','Paid processing platform with a steep learning curve and strong gradient and noise tools.','https://www.highpointscientific.com/astronomy-hub/post/best-software-for-astrophotography-in-2023',[V('PixInsight','PixInsight','','Paid, one-time purchase; Windows, macOS, Linux')],mk='PixInsight'),
 A('DeepSkyStacker','Free beginner-friendly stacking program for calibration, alignment and stacking.','https://astrobackyard.com/astrophotography-image-stacking-software/',[V('DeepSkyStacker','','','Free, open source')]),
 A('Siril','Free cross-platform program for calibration, stacking and processing.','https://astrobackyard.com/astrophotography-image-stacking-software/',[V('Siril','','','Free, open source; Windows, macOS, Linux')]),
 A('N.I.N.A.','Free open-source capture and sequencing program with a framing assistant and autofocus; Windows-focused.','https://www.saashub.com/compare-n-i-n-a-vs-apt-astro-photography-tool',[V('N.I.N.A.','N.I.N.A. project')]),
 A('SharpCap','Capture tool for astronomy cameras, webcams and USB frame grabbers with live stacking and polar alignment.','https://www.saashub.com/compare-n-i-n-a-vs-apt-astro-photography-tool',[V('SharpCap','')]),
 A('Astro Photography Tool','Capture and sequencing program for DSLR and CCD cameras (APT); Windows.','https://www.saashub.com/compare-n-i-n-a-vs-apt-astro-photography-tool',[V('APT','')])],
 'm':M(('Astro Pixel Processor','Mabula Haverkamp'),('Sequator',''),('AutoStakkert!',''),('StarTools',''),('PHD2',''),('TheSkyX Professional','Bisque'),('ASI Air app','ZWO'),('CPWI','Celestron'))}
gis={'n':'GIS and mapping software','a':'earth-mapping software','d':'Program on the owner\'s machine that edits, analyses or views geographic data. A hosted map or navigation service is in Subscriptions, Memberships & Online Services.',
 't':['desktop GIS','free and open source','globe viewer','Windows-only commercial'],
 's':'https://en.wikipedia.org/wiki/Comparison_of_geographic_information_systems_software','x':[
 A('QGIS','Free open-source desktop GIS started by Gary Sherman in 2002 as Quantum GIS; long-term-release every year or two.',WP+'QGIS',[V('Quantum GIS','Gary Sherman','2002','July 2002; OSGeo incubator project 2007'),V('QGIS 3.40 LTR','QGIS project','2024','Bratislava'),V('QGIS 3.44 LTR','QGIS project','2025','Solothurn')],y='2002'),
 A('ArcGIS Pro','Esri\'s commercial desktop GIS, Windows only.',WP+'Comparison_of_GIS_software',[V('ArcGIS Pro','Esri')],mk='Esri'),
 A('Google Earth Pro','Free desktop version of Google Earth for Windows, Mac and Linux; downloads end after 25 June 2027 per the page.',WP+'Earth.google.com',[V('Keyhole EarthViewer','Keyhole','2001','June 2001'),V('Google Earth 3.0','Google','2005','June 2005; Google bought Keyhole in 2004'),V('Google Earth Pro','Google','2015','Free from 2015 (paid $399 a year before); 7.3 in 2017')],mk='Google',y='2001'),
 A('GRASS GIS','Open-source GIS begun in 1982 at the US Army Construction Engineering Research Laboratory; GPL since version 5.0 in 1999.',WP+'GRASS_GIS',[V('GRASS','USA-CERL','1982'),V('GRASS 5.0','GRASS Development Team','1999','Moved to GPL'),V('GRASS GIS 8.5.0','GRASS Development Team','2026','8 May 2026')],y='1982')],
 'm':M(('MapInfo Pro','Pitney Bowes'),('Maptitude','Caliper Corporation'),('Manifold System',''),('SAGA GIS',''),('gvSIG',''),('uDig',''),('ILWIS',''),('MapWindow GIS',''))}
sci={'n':'Scientific and statistics software','a':'scientific and analytical software','d':'Program for scientific computation, statistics and data analysis.',
 't':['statistics package','numerical computing','computer algebra','notebook environment','graphing','free and open source'],
 's':'https://en.wikipedia.org/wiki/List_of_numerical-analysis_software','x':[
 A('R','Free open-source language and environment for statistics, an implementation of S; GNU GPL.',CS,[V('R 4.5.3','R Foundation','2026','11 March 2026')],mk='R Foundation'),
 A('MATLAB','MathWorks\' proprietary numerical computing environment with its own language.',CS,[V('MATLAB','MathWorks'),V('Simulink','MathWorks')],mk='MathWorks'),
 A('Mathematica','Wolfram Research\' computer-algebra and technical computing system, first released in 1988 with the Wolfram Language.',WP+'Wolfram_Language',[V('Mathematica 1.0','Wolfram Research','1988'),V('Wolfram Language','Wolfram Research','2013','Name adopted 2013'),V('Wolfram Engine','Wolfram Research','2019','Freeware for developers'),V('Mathematica 15.0.1','Wolfram Research','2026','July 2026')],mk='Wolfram Research',y='1988'),
 A('SPSS','IBM\'s menu-driven statistics package; JASP and PSPP are free alternatives.',CS,[V('SPSS Statistics 28','IBM','2021','24 May 2021')],mk='IBM'),
 A('Stata','StataCorp\'s statistics package for economics, epidemiology and the social sciences.',CS,[V('Stata 19','StataCorp','2025','8 April 2025')],mk='StataCorp'),
 A('Jupyter','Notebook environment spun out of IPython (2001) by Fernando Perez in 2014; supports Python, Julia and R.',WP+'Ipython',[V('IPython','Fernando Perez','2001'),V('Project Jupyter','Project Jupyter','2014','Language-agnostic notebook spin-off')],y='2001'),
 A('Origin','OriginLab\'s Windows software for scientific graphs and data analysis.',CS,[V('Origin 10.3','OriginLab','2025','21 November 2025')],mk='OriginLab')],
 'm':M(('GNU Octave',''),('Julia',''),('JASP','JASP team'),('jamovi','The jamovi project'),('PSPP','GNU Project'),('gretl','The gretl Team'),('SAS',''),('JMP','JMP Statistical Discovery'),('Minitab','Minitab'),('GraphPad Prism','GraphPad Software'),('Maple',''),('SageMath',''),('Scilab',''),('Igor Pro',''),('Orange','University of Ljubljana'),('Weka','University Of Waikato'),('EViews','IHS Markit'))}
brands=[B('Esri','United States','1969','Professional & flagship','ArcGIS','American maker of ArcGIS.'),
 B('MathWorks','United States','1984','Professional & flagship','MATLAB','American maker of MATLAB and Simulink.'),
 B('Wolfram Research','United States','1987','Professional & flagship','Mathematica','Maker of Mathematica and the Wolfram Language.',s=WP+'Wolfram_Language'),
 B('StataCorp','United States','1985','Professional & flagship','Stata','Texas maker of Stata.')]
notes=('Planetarium 11 old names to 5 archetypes plus 5; Digistar dropped as a dome-projector system. Astrophotography is new, sourced from AstroBackyard, High Point Scientific and SaaSHub (via firecrawl once). GIS 52 old names trimmed to 4 archetypes plus 8: dropped enterprise servers and libraries (ArcGIS Server, GeoServer, MapServer, PostGIS, OpenLayers, Leaflet, GeoTools, GeoTrellis, GeoNetwork, MapDotNet, Oracle Spatial, GeoMedia and WebMap, SuperMap, Smallworld, TNTmips, TerraLib, TerraView), transport modelling (TransModeler), fleet (GeoBase) and ETL (FME). '
 'Scientific software cut from 142 to 7 archetypes plus 17; dropped trade/niche/dead: Alteryx, BMDP, S-PLUS, Statistica, RATS, LIMDEP, NLOGIT, Shazam, TSP, Ox, XploRe, ELKI, PRIMER, ADMB, AMPL, COMSOL, LabVIEW, OpenFOAM, Trilinos, libraries (LAPACK, ScaLAPACK, Armadillo, NumPy, pandas, SciPy, scikit-learn, Torch, mlpack) and others. GeoGebra is named in the brief but no retrieved page covered it, so it is omitted.')
put('08_01',{'kinds':[pl,astro,gis,sci],'brands':brands,'traditions':[],'notes':notes})
