import json,os,copy
R='/home/user/Possession-Taxonomy/rebuild/'
d=json.load(open(R+'work/V4_E6/bak/E6.json'))
TL='https://en.wikipedia.org/wiki/List_of_telescope_types'
AL='https://en.wikipedia.org/wiki/List_of_astronomical_instruments'
WL='https://en.wikipedia.org/wiki/List_of_weather_instruments'
BIN='https://en.wikipedia.org/wiki/Binoculars'
MIC='https://en.wikipedia.org/wiki/Microscope'
newbrands={}
def V(n,mk='',y='',dd=''): return {'n':n,'mk':mk,'y':y,'d':dd}
def E(n,dd,s,mk='',y='',v=None,g='',a='',role=None,dt=''):
    e={'n':n,'a':a,'d':dd,'mk':mk,'y':y,'s':s,'v':v or [],'dt':dt,'g':g}
    if role: e['role']=role
    if mk: newbrands[mk]=1
    return e
K={}
for dp in d['depts']:
    for s in dp['s']:
        for k in s['k']: K[k['n']]=k
def setk(name,nl,sel,xg,x,drop_mr=True):
    k=K[name]; k['nl']=nl; k['sel']=sel
    if xg: k['xg']=xg
    k['x']=x
    if drop_mr:
        k.pop('m',None); k.pop('r',None)
def oldx(kname,n):
    return [x for x in K[kname].get('x',[]) if x['n']==n][0]
def vers(kname,n,**kw):
    x=oldx(kname,n); return V(x['n'],x.get('mk',''),x.get('y',''),x['d'])
def mv(ms,mk,names=None):
    return [V(m,mk) for m,k in ms if k==mk and (names is None or m in names)]
# ---------- TELESCOPES ----------
NLT='One entry is an optical design of telescope as named in Wikipedia\'s list of telescope types; maker lines and models of that design are versions.'
RF='Refractor telescope'
setk(RF,NLT,"Every refracting design in Wikipedia's List of telescope types (Refracting section) that a person can own, with maker lines from the earlier pass as versions; binoculars and monoculars are under their own kinds.",'by colour correction',[
 E('Galilean telescope','Convex objective with a concave eyepiece, giving an upright image and a narrow field; the first astronomical telescope.',TL,'Galileo Galilei','c. 1609',g='Non-achromatic',role='origin'),
 E('Keplerian telescope','Convex objective and convex eyepiece, giving a wider field and an inverted image; the basis of modern refractors.',TL,'Johannes Kepler','1611',[vers(RF,'Galileoscope')],g='Non-achromatic'),
 E('Aerial telescope','Very long non-achromatic refractor with no tube, listed under Keplerian telescopes.',TL,g='Non-achromatic'),
 E('Achromatic refractor','Refractor whose doublet objective brings two colours to a common focus; the beginner and classic long-focus design.',TL,v=[vers(RF,'Dollond achromatic refractor'),vers(RF,'Unitron achromat'),V('StarTravel','Sky-Watcher'),V('Inspire 100AZ','Celestron'),V('StarSense Explorer DX 102AZ','Celestron')],g='Achromatic',a='dialytic refractor'),
 E('Apochromatic refractor','Refractor with ED, fluorite or triplet objective that corrects three colours; sold by aperture and focal ratio.',TL,v=[vers(RF,'Takahashi FC fluorite doublet'),vers(RF,'Sky-Watcher Evostar / Equinox ED'),vers(RF,'Takahashi FSQ-106'),vers(RF,'Astro-Physics StarFire'),vers(RF,'Sky-Watcher Esprit'),V('TOA-130','Takahashi Seisakusho'),V('130PHQ','Askar'),V('SQA106','Askar'),V('Askar V','Askar'),V('Z4','Sharpstar'),V('FLT','William Optics'),V('Fluorostar 132','William Optics'),V('ZenithStar','William Optics'),vers(RF,'William Optics RedCat 51')],g='Apochromatic',a='apo'),
 E('Petzval telescope','Apochromatic refractor with a Petzval objective, giving a short, flat-field tube for imaging.',TL,v=[vers(RF,'Tele Vue Genesis / NP101'),V('Petzval 75','Radian')],g='Apochromatic'),
 E('Superachromat','Refractor whose objective corrects colour more tightly than an apochromat.',TL,g='Apochromatic'),
 E('Copyscope','Refracting design named in the reference list; sold as a small optical instrument.',TL,g='Other refracting designs'),
 E("Baden-Powell's unilens",'Refracting design named in the reference list.',TL,g='Other refracting designs'),
])
NLN="One entry is an optical design of reflecting telescope as named in Wikipedia's list of telescope types; maker lines and models are versions."
NW='Newtonian reflector'
setk(NW,NLN,"Newtonian telescope from Wikipedia's List of telescope types (Reflecting section); the Dobsonian mounting has its own kind.",'',[
 E('Newtonian telescope','Concave primary mirror with a flat secondary at the side of the tube.',TL,v=[vers(NW,'Edmund Astroscan'),V('Explorer P','Sky-Watcher'),V('SpaceProbe 130ST EQ','Orion Telescopes & Binoculars'),V('AstroMaster 114 EQ','Celestron'),V('StarSense Explorer DX 130AZ','Celestron'),V('VX Newtonian','Orion Optics UK')],g='Reflecting',a='Newtonian reflector'),
])
DB='Dobsonian telescope'
setk(DB,"One entry is a named Dobsonian line: a Newtonian on a rocker-box mount; models of the line are versions.","Dobsonian telescope from Wikipedia's List of telescope types, with the dobsonian makers of the earlier pass as lines.",'',[
 E('Dobsonian telescope','Newtonian on a simple rocker-box alt-azimuth mount, designed by John Dobson.',TL,'John Dobson','',[V('Heritage 130P','Sky-Watcher'),V('Library Telescope','Apertura'),V('Stargate','Sky-Watcher'),V('Flextube','Sky-Watcher')],g='Design',role='origin'),
 E('Coulter Odyssey','Large-aperture commercial Dobsonians from Coulter Optical.',oldx(DB,'Coulter Odyssey')['s'],'Coulter Optical','1980s',g='Maker lines'),
 E('Obsession truss Dobsonian','Truss-tube Dobsonians from Obsession Telescopes.',oldx(DB,'Obsession truss Dobsonian')['s'],'Obsession Telescopes','1989',g='Maker lines'),
 E('Sky-Watcher Skyliner','Solid-tube and collapsible Dobsonian lines.',K[DB]['s'],'Sky-Watcher','',[V('Skyliner Classic','Sky-Watcher'),V('Heritage FlexTube Virtuoso GTi','Sky-Watcher')],g='Maker lines'),
 E('Orion SkyQuest','Dobsonian range from Orion Telescopes & Binoculars.',K[DB]['s'],'Orion Telescopes & Binoculars','',[V('SkyQuest XT8 Plus','Orion Telescopes & Binoculars'),V('SkyQuest XT6 Plus / XT10i IntelliScope','Orion Telescopes & Binoculars')],g='Maker lines'),
 E('Apertura AD','Dobsonian line from Apertura.',K[DB]['s'],'Apertura','',[V('AD6','Apertura')],g='Maker lines'),
 E('Omegon Dobsonian','Dobsonian lines from Omegon.',K[DB]['s'],'Omegon','',[V('ProDob','Omegon'),V('Pro Truss','Omegon')],g='Maker lines'),
 E('Zhumell Z','Dobsonian line from Zhumell.',K[DB]['s'],'Zhumell','',[V('Z10 Deluxe','Zhumell')],g='Maker lines'),
])
CA='Cassegrain telescope'
setk(CA,NLN,"Every Cassegrain-family and other multi-mirror design in the Reflecting section of Wikipedia's List of telescope types, except the Gregorian, Herschelian and off-axis designs, which are under their own kind.",'by design family',[
 E('Cassegrain telescope','Concave primary with a convex secondary that folds the light back through a hole in the primary.',TL,v=[V('Pro CC 154/1848','Omegon')],g='Cassegrain family'),
 E('Dall–Kirkham telescope','Cassegrain with an elliptical primary and spherical secondary.',TL,'Horace Dall','1928',[vers(CA,'Takahashi Mewlon')],g='Cassegrain family'),
 E('Ritchey–Chrétien telescope','Cassegrain with hyperbolic primary and secondary, free of coma; the design of most large observatory telescopes.',TL,'','1910s',g='Cassegrain family'),
 E('Nasmyth telescope','Cassegrain-type arrangement with a tertiary mirror sending light to the side of the altitude axis.',TL,g='Cassegrain family'),
 E('Three-mirror anastigmat','Reflector with three powered mirrors that corrects aberrations over a wide field.',TL,g='Other multi-mirror designs'),
 E('Wolter telescope','Grazing-incidence mirror design used for X-ray telescopes.',TL,g='Other multi-mirror designs'),
 E('Crossed Dragone telescope','Two-mirror off-axis reflector used mainly in radio and microwave work.',TL,g='Other multi-mirror designs'),
 E('Liquid mirror telescope','Telescope whose primary mirror is a spinning pool of liquid.',TL,g='Other multi-mirror designs'),
])
GR='Gregorian & off-axis reflector'
setk(GR,NLN,"Gregorian, Herschelian and off-axis designs from the Reflecting section of Wikipedia's List of telescope types.",'',[
 E('Gregorian telescope','Concave primary with a concave secondary beyond the focus, giving an upright image.',TL,'James Gregory','1663',g='Gregorian'),
 E('Herschelian telescope','Tilted primary mirror that sends light to an eyepiece at the front of the tube.',TL,'William Herschel','1789',g='Off-axis'),
 E('Schiefspiegler telescope','Tilted-mirror reflector with no central obstruction.',TL,'Anton Kutter','',g='Off-axis'),
 E('Yolo telescope','Obstruction-free reflector using tilted toroidal mirrors.',TL,'Arthur S. Leonard','mid-1960s',g='Off-axis'),
 E('Stevick–Paul telescope','Off-axis three-mirror reflector named in the reference list.',TL,g='Off-axis'),
 E('Pfund telescope','Reflector design named in the reference list.',TL,g='Off-axis'),
 E('Schwarzschild telescope','Two-mirror aplanatic reflector; the Couder telescope is a variant.',TL,g='Off-axis'),
])
NLC="One entry is an optical design of catadioptric telescope as named in Wikipedia's list of telescope types; maker lines and models are versions."
SC='Schmidt-Cassegrain telescope'
setk(SC,NLC,"Schmidt–Cassegrain and Schmidt–Newtonian designs from the Catadioptric section of Wikipedia's List of telescope types; Schmidt cameras are under Schmidt astrograph.",'',[
 E('Schmidt–Cassegrain telescope','Cassegrain with a thin Schmidt corrector plate at the front; the common compact amateur design.',TL,v=[vers(SC,'Celestron C8'),vers(SC,'Celestron EdgeHD'),vers(SC,'Meade LX200 / ACF'),V('NexStar SLT','Celestron'),V('StarSense Explorer DX 6 AZ','Celestron'),V('Advanced VX','Celestron'),V('CGX','Celestron')],g='Schmidt family'),
 E('Schmidt–Newtonian telescope','Newtonian with a Schmidt corrector plate at the front.',TL,g='Schmidt family'),
])
MK='Maksutov-Cassegrain telescope'
setk(MK,NLC,"Maksutov designs from the Catadioptric section of Wikipedia's List of telescope types, with the Gregory, Rutten and sub-aperture variants it names; maker lines of the earlier pass are versions.",'',[
 E('Maksutov–Cassegrain telescope','Cassegrain with a thick meniscus corrector, giving a long focal length in a short sealed tube.',TL,v=[vers(MK,'Questar 3.5'),vers(MK,'Meade ETX'),vers(MK,'Sky-Watcher Skymax'),V('C90 Mak','Celestron'),V('NexStar 127 SLT','Celestron'),V('NexStar SE','Celestron'),V('OMC Maksutov-Cassegrain','Orion Optics UK'),V('MAKSYGO-60','Acuter'),V('MightyMak','Omegon'),V('Rumak','iOptron'),V('VMC200L','Vixen')],g='Maksutov family'),
 E('Maksutov–Newtonian telescope','Newtonian with a meniscus corrector at the front.',TL,g='Maksutov family'),
 E('Maksutov camera','Wide-field camera design using a meniscus corrector.',TL,g='Maksutov family'),
])
SA='Schmidt astrograph'
setk(SA,NLC,"Schmidt camera family from Wikipedia's List of telescope types (Baker–Nunn, Baker–Schmidt, lensless Schmidt, Mersenne–Schmidt, Schmidt–Väisälä) plus the Celestron RASA of the earlier pass.",'',[
 E('Schmidt camera','Wide-field photographic camera with a spherical mirror and a Schmidt corrector plate.',TL,'','1930',[V('Celestron RASA','Celestron','2014','Rowe-Ackermann Schmidt Astrograph, f/2')],g='Schmidt family'),
 E('Baker–Nunn camera','Schmidt-camera variant built for tracking satellites.',TL,g='Schmidt family'),
 E('Baker–Schmidt camera','Schmidt-camera variant named in the reference list.',TL,g='Schmidt family'),
 E('Lensless Schmidt telescope','Schmidt-type design without a refractive corrector.',TL,g='Schmidt family'),
 E('Mersenne–Schmidt camera','Schmidt-camera variant named in the reference list.',TL,g='Schmidt family'),
 E('Schmidt–Väisälä camera','Schmidt-camera variant named in the reference list.',TL,g='Schmidt family'),
])
# new catadioptric kind
sh=[s for dp in d['depts'] if dp['n']=='Telescopes' for s in dp['s'] if s['n']=='Catadioptric telescopes'][0]
sh['k'].append({'n':'Specialist catadioptric telescope','d':'Catadioptric designs beyond the Schmidt and Maksutov families, named in the reference list.','s':TL,'nl':NLC,'sel':"Remaining designs of the Catadioptric section of Wikipedia's List of telescope types.",'x':[
 E('Argunov–Cassegrain telescope','Catadioptric Cassegrain with a corrector in the converging beam.',TL,g='Catadioptric'),
 E('Klevtsov–Cassegrain telescope','Catadioptric Cassegrain with a sub-aperture corrector.',TL,g='Catadioptric'),
 E('Lurie–Houghton telescope','Catadioptric design with a Houghton lens corrector.',TL,g='Catadioptric'),
 E('Jones–Bird telescope','Catadioptric Newtonian-type design.',TL,g='Catadioptric'),
 E('Modified Dall–Kirkham telescope','Dall–Kirkham variant with a corrector.',TL,g='Catadioptric'),
 E('Catadioptric dialyte','Catadioptric design using separated corrector elements.',TL,g='Catadioptric'),
]})
# smart, solar
SM='Smart telescope'
setk(SM,"One entry is a smart telescope line sold under its own name; models are versions.","Smart-telescope lines of the earlier pass (Wikipedia's List of telescope types names no smart telescopes).",'',
 [E(x['n'],x['d'],x['s'],x.get('mk',''),x.get('y',''),x.get('v',[]),dt=x.get('dt','')) for x in K[SM]['x']]+[E('Vaonis Hestia','Smartphone-based smart telescope from Vaonis.',K[SM]['s'],'Vaonis','')])
SO='Solar telescope'
setk(SO,"One entry is a solar telescope line sold under its own name; models are versions.","Solar telescope lines of the earlier pass; a Solar telescope is also a task class in Wikipedia's List of telescope types.",'',
 [E(x['n'],x['d'],x['s'],x.get('mk',''),x.get('y',''),x.get('v',[]),dt=x.get('dt','')) for x in K[SO]['x']]+[
  E('Coronado SolarMax','Hydrogen-alpha solar telescope range.',K[SO]['s'],'Meade Instruments','',[V('SolarMax III','Meade Instruments'),V('Solar Ranger','Meade Instruments')]),
  E('DayStar solar telescopes','Hydrogen-alpha solar telescopes.',K[SO]['s'],'DayStar Filters','',[V('Sol 60','DayStar Filters'),V('SolarScout','DayStar Filters')]),
  E('Sky-Watcher Heliostar','Solar telescope from Sky-Watcher.',K[SO]['s'],'Sky-Watcher')])
SF='Solar filter'
setk(SF,"One entry is a solar filter line sold under its own name; sizes and models are versions.","Solar filter lines of the earlier pass.",'',
 [E(x['n'],x['d'],x['s'],x.get('mk',''),x.get('y',''),x.get('v',[]),dt=x.get('dt','')) for x in K[SF]['x']]+[
  E('Seymour Solar Helios','Glass solar filter.',K[SF]['s'],'Seymour Solar','',[V('Helios Solar Glass','Seymour Solar')]),
  E('Astrozap AstroSolar','Solar filter film from Astrozap.',K[SF]['s'],'Astrozap','',[V('AstroSolar solar filter','Astrozap')])])
for x in K[SF]['x']:
    if x['n']=='Baader AstroSolar': pass
next(x for x in K[SF]['x'] if x['n']=='Baader AstroSolar')['v'].append(V('BDSF digital solar filter','Baader Planetarium'))
exec(open(R+'work/V4_E6/build2.py').read())
