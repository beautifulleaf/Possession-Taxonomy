import sys; sys.path.insert(0,'/home/user/Possession-Taxonomy/rebuild/work/GAP_E6')
from common import *
d=load()
W='https://en.wikipedia.org/wiki/'
def add(k,items):
    k.setdefault('x',[])
    have={e['n'].lower() for e in k['x']}
    for e in items:
        if e['n'].lower() not in have: k['x'].append(e)
def prin(name,nl,sel,items,S):
    k=find(d,name); k['nl']=nl; k['sel']=sel; k['xg']='principle, then maker lines'
    add(k,[ent(n,t,mk=mk,y=y,s=S,g='Principles') for n,t,mk,y in items])
    # move principles first
    k['x'].sort(key=lambda e:0 if e.get('g')=='Principles' else 1)
prin('Anemometer','One entry is a wind-measuring principle named in the Wikipedia article Anemometer or a handheld or station anemometer line sold under its own name.',
 'Principles from the Wikipedia article Anemometer (13 types; all that a person can own are listed, the laser Doppler and acoustic-resonance types are laboratory only and omitted), then maker lines from retailer pages.',
 [('Cup anemometer','Hemispherical cups on horizontal arms spin a vertical shaft, and the rotation rate tracks wind speed.','John Thomas Romney Robinson','1845'),
  ('Plate anemometer','Wind deflects a flat plate, and a spring or gauge measures the force.','Leon Battista Alberti','1450'),
  ('Tube anemometer','Pressure openings facing the wind feed a gauge: Lind used a U-tube in 1775 and Dines a float recorder in 1892.','James Lind','1775'),
  ('Vane anemometer','A propeller-like rotor on a horizontal axis, kept into the wind by a vane, counts revolutions to give speed.','',''),
  ('Hot-wire anemometer','An electrically heated wire cools in airflow, and its resistance change indicates speed.','',''),
  ('Ultrasonic anemometer','Sound pulses between transducer pairs give wind velocity from travel-time differences.','','1950s'),
  ('Ping-pong ball anemometer','A ball on a string deflects with the wind, and the angle from vertical estimates speed.','','')],W+'Anemometer')
prin('Hygrometer','One entry is a humidity-measuring principle named in the Wikipedia article Hygrometer or a hygrometer line sold under its own name.',
 'Principles from the Wikipedia article Hygrometer (all home-relevant types; optical and spectroscopic laboratory types omitted), then maker lines from retailer pages.',
 [('Hair tension hygrometer','A tensioned human or animal hair changes length with humidity, and the change is magnified to a dial.','Horace Bénédict de Saussure','1783'),
  ('Psychrometer','Compares a dry thermometer with a moistened one; the temperature difference gives relative humidity.','',''),
  ('Sling psychrometer','Thermometers on a handle are spun in free air until the readings settle.','',''),
  ('Assmann psychrometer','A precise psychrometer with thermometers shielded in double metal tubes and a fan drawing air past them.','Adolph Richard Assmann','late 19th century'),
  ('Metal-paper coil hygrometer','A salt-impregnated paper strip on a metal coil moves a needle as it takes up moisture.','',''),
  ('Capacitive hygrometer','Measures changes in the dielectric constant of a polymer or metal oxide; about 2 % accuracy when calibrated.','',''),
  ('Resistive hygrometer','Measures changes in electrical resistance of salts or conductive polymers.','',''),
  ('Chilled-mirror dew point hygrometer','Cools a mirror until condensation forms and detects it optically; a laboratory reference.','','')],W+'Hygrometer')
prin('Barometer','One entry is a barometer principle or historic pattern, or a named line sold under its own name.',
 'Principles from the Wikipedia article Barometer (mercury, Fortin, aneroid, wheel, MEMS), patterns from the earlier pass, then maker lines.',
 [('Mercury barometer','A vertical glass tube closed at the top stands in a basin of mercury; air pressure supports the column.','Evangelista Torricelli','1643'),
  ('Fortin barometer','A mercury barometer with an adjustable cistern whose zero level is set by a thumbscrew before reading.','Jean Nicolas Fortin',''),
  ('MEMS barometer','Microelectromechanical pressure sensor used in weather stations, altimeters and smartphones.','','')],W+'Barometer')
for e in find(d,'Barometer')['x']:
    if e['n']=='Aneroid barometer': e['mk']='Lucien Vidi'; e['y']='1844'; e['g']='Principles'
    if e['n'] in('Stick barometer','Wheel barometer','Admiral FitzRoy barometer','Kew pattern marine barometer'): e['g']='Principles'
    if e['n']=='Wheel barometer': e['y']='c. 1810'
find(d,'Barometer')['x'].sort(key=lambda e:0 if e.get('g')=='Principles' else 1)
prin('Rain gauge','One entry is a rain gauge design named in the Wikipedia article Rain gauge or a gauge line sold under its own name.',
 'Designs from the Wikipedia article Rain gauge (10 named; the weighing, optical and acoustic types are professional and omitted), then maker lines.',
 [('Standard rain gauge','Funnel feeding a graduated inner cylinder: the UK copper gauge with a five-inch funnel (1863–1890) and the US eight-inch NWS gauge.','George James Symons','1863'),
  ('Tipping bucket rain gauge','A balanced collector tips when full and triggers a switch, so rain can be logged electronically.','Christopher Wren','1662'),
  ('Cheugugi','Korean standardised rain gauge of the Joseon dynasty.','Sejong the Great (reign)','1441'),
  ('Tianchi basin rain and snow gauge','Song-dynasty device for measuring rain and snowfall.','Qin Jiushao','1247')],W+'Rain_gauge')
k=find(d,'Geiger counter'); S=W+'Geiger_counter'
k['nl']='One entry is a Geiger counter tube type named in the Wikipedia article Geiger counter or a handheld counter line sold under its own name.'
k['xg']='tube, then maker lines'
k['sel']='Tube types from the Wikipedia article Geiger counter (Geiger–Müller, end-window, pancake, thick-walled), then maker lines; the article names no consumer models.'
add(k,[ent('Geiger–Müller tube','Sealed gas-filled tube that detects alpha, beta and gamma radiation; the basis of the Geiger counter.',mk='Hans Geiger',y='1928',s=S,g='Tubes',role='origin'),
 ent('End-window tube','Tube with a mica window for alpha and low-energy beta particles.',y='1930s',s=S,g='Tubes'),
 ent('Pancake probe','Large-area tube for quick checks of surface contamination.',s=S,g='Tubes'),
 ent('Thick-walled energy-compensated tube','Steel tube with filter rings for gamma detection.',s=S,g='Tubes')])
k['x'].sort(key=lambda e:0 if e.get('g')=='Tubes' else 1)
# microscopes
S=W+'Optical_microscope'
for name,items in {'Compound light microscope':[('Phase-contrast microscope','Phase-contrast illumination images transparent samples such as live cells without staining.','Frits Zernike','1953'),('Epifluorescence microscope','Illuminates fluorophore-containing samples through the objective and images the emitted light.','',''),('Student microscope','Low-power instrument with simplified controls, for school use.','','')],
 'Polarising microscope':[('Petrographic microscope','Polarising microscope with a rotating stage and gypsum plate for studying minerals and crystals.','','')],
 'Digital microscope':[('USB microscope','Low-power, webcam-like device with a macro lens that connects to a computer.','','')],
 'Inverted & metallurgical microscope':[('Inverted microscope','Views samples from below; used for liquid cell cultures and metallography.','','')]}.items():
    k=find(d,name); add(k,[ent(n,t,mk=mk,y=y,s=S,g='Types') for n,t,mk,y in items])
    k['x'].sort(key=lambda e:0 if e.get('g')=='Types' else 1)
    if name=='Inverted & metallurgical microscope': k['nl']='One entry is a microscope type named in the Wikipedia article Optical microscope.'
# historic
S=W+'Astrolabe'
k=find(d,'Astrolabe'); add(k,[ent('Spherical astrolabe','Variant combining features of the astrolabe and armillary sphere; first described by al-Nayrizi.',mk='Al-Nayrizi',y='fl. 892–902',s=S,g='Medieval (500–1500)'),
 ent('Linear astrolabe','Wooden rod with graduated markings and a plumb line, the staff of al-Tusi.',mk='Sharaf al-Din al-Tusi',y='12th century',s=S,g='Medieval (500–1500)'),
 ent('Geared mechanical astrolabe','Early astrolabe driven by gears.',mk='Abi Bakr of Isfahan',y='1235',s=S,g='Medieval (500–1500)'),
 ent('Balesilha','Simplified astrolabe used by sailors for latitude at sea, promoted by Prince Henry.',s=S,g='Medieval (500–1500)'),
 ent('Jean Fusoris astrolabe','Planispheric astrolabes made in Paris; thirteen survive.',mk='Jean Fusoris',y='1400',s=S,g='Medieval (500–1500)'),
 ent('Hartmann astrolabes','Four identical astrolabes, among the earliest evidence of batch production by division of labour.',mk='Georg Hartmann',y='16th century',s=S,g='Early modern (1500–1800)'),
 ent('Astrolabe watch','Wristwatch with an astrolabe display, designed with Ulysse Nardin.',mk='Ludwig Oechslin',y='1985',s=S,g='Modern (from 1800)')])
k['sel']='Astrolabe types and makers named in the first 100,000 of 147,000 characters of the Wikipedia article Astrolabe; the remaining characters are not read.'
S=W+'Sextant'
k=find(d,'Sextant'); add(k,[ent('Hadley–Godfrey sextant','Reflecting sextant first implemented around 1731 by John Hadley and Thomas Godfrey.',mk='John Hadley',y='c. 1731',s=S,g='Early modern (1500–1800)',role='origin'),
 ent('Quintant','Reflecting instrument spanning about a fifth of a circle (72 degrees) with a scale to 140 degrees.',s=S,g='Early modern (1500–1800)'),
 ent('Aeronautical sextant','Sextant modified for air navigation, with an artificial horizon.',mk='Carlos Viegas Gago Coutinho',y='1922',s=S,g='Modern (from 1800)')])
S=W+'Armillary_sphere'
k=find(d,'Armillary sphere'); add(k,[ent("Zhang Heng's armillary sphere",'Complete Han sphere with horizon and meridian rings, also water powered.',mk='Zhang Heng',y='125',s=S,g='Ancient (to c. 500)'),
 ent("Su Song's clock tower armillary",'Mechanically rotated armillary crowning a water-powered astronomical clock tower.',mk='Su Song',y='1092',s=S,g='Medieval (500–1500)'),
 ent('Honcheonsigye','Korean armillary sphere driven by a clock mechanism; the only surviving Joseon astronomical clock.',mk='Song I-yong',y='1669',s=S,g='Early modern (1500–1800)'),
 ent('Bürgi–Eisenhoit armillary sphere with clock','Armillary sphere with an astronomical clock made in Kassel, now in the Nordiska Museet, Stockholm.',mk='Jost Bürgi',y='1585',s=S,g='Early modern (1500–1800)'),
 ent("Tycho Brahe's armillary spheres",'Three large instruments for precise star and planet positions, described in 1598.',mk='Tycho Brahe',y='1598',s=S,g='Early modern (1500–1800)')])
# fix sundial g
k=find(d,'Sundial & gnomon')
for e in k['x']:
    if e['g'] not in('Ancient (to c. 500)',): pass
save(d)
