# ---------- generic conversion of remaining models ----------
def conv(kname,nl,sel,xg=None,keepx=True,gold='Maker lines',gnew='Maker lines',extra=None,keep_r=True,skip=()):
    k=K[kname]; old=k.get('x',[]) or []
    xs=[]
    for x in old:
        x=copy.deepcopy(x); x['g']=gold; xs.append(x)
    have={x['n'].lower() for x in xs}
    for m,mk in k.get('m',[]) or []:
        if m in skip: continue
        n=m if (mk and mk.split()[0].lower() in m.lower()) or not mk else f"{mk.split(' (')[0]} {m}"
        if n.lower() in have: continue
        have.add(n.lower())
        xs.append(E(n,f"{k['n'].lower()} model from {mk.split(' (')[0]}." if mk else f"{k['n'].lower()} design.",k['s'],mk,'',g=gnew))
    k['nl']=nl; k['sel']=sel
    if xg: k['xg']=xg
    k['x']=(extra or [])+xs
    k.pop('m',None)
    if not keep_r: k.pop('r',None)
BS=BIN
# ---------- BINOCULARS ----------
B='Binoculars'
bx=[x for x in K[B]['x'] if x['n'] not in('Zeiss Porro binoculars','Hensoldt pentaprism roof binoculars','Zeiss Victory FL')]
prism=[
 E('Porro prism binoculars','Two Porro prisms per side give the offset body; patented by Ignazio Porro in 1854 and made commercial by Carl Zeiss in 1894.',BS,'Ignazio Porro','1854',[V('Zeiss Porro binoculars','Carl Zeiss','1894','first modern Porro binoculars'),V('Derby Compact 8×40','Eschenbach Optik','','Porro-type, central focus')],g='Prism type'),
 E('Pentaprism roof binoculars','Roof binoculars with pentaprisms, first marketed by Moritz Hensoldt.',BS,'Moritz Hensoldt','1897',[V('Hensoldt pentaprism roof binoculars','Moritz Hensoldt','1897','')],g='Prism type'),
 E('Schmidt–Pechan roof binoculars','Straight-barrel roof binoculars using Schmidt–Pechan prisms, invented in 1899.',BS,'','1899',[V('Zeiss Victory FL','Carl Zeiss','2004','dielectric-coated Schmidt–Pechan prisms')],g='Prism type'),
 E('Abbe–König roof binoculars','Roof binoculars with Abbe–König prisms, patented by Abbe and König.',BS,'Carl Zeiss','1905',g='Prism type'),
 E('Uppendahl prism binoculars','Three cemented prisms per side, offered on a small scale.',BS,g='Prism type'),
 E('Perger prism binoculars','Porro variant with reduced axial offset.',BS,g='Prism type'),
]
K[B]['x']=bx
conv(B,"One entry is a prism system of binoculars or a maker line sold under its own name; models of the line are versions.","Prism types named in the Wikipedia article Binoculars, then maker lines from the earlier pass; Wikipedia gives no whole list of binocular lines.",'prism type, then maker lines',extra=prism)
for x in K[B]['x']:
    if x['n']=='Zeiss 7×50 B/GA T*': x['g']='Maker lines'
conv('Opera glasses',"One entry is an opera-glass line sold under its own name.","Opera-glass lines of the earlier pass; no whole-space reference exists.")
conv('Giant binoculars',"One entry is a giant-binocular line sold under its own name.","Giant-binocular lines of the earlier pass; no whole-space reference exists.")
conv('Monocular',"One entry is a monocular line sold under its own name.","Monocular lines of the earlier pass; Wikipedia's List of telescope types names the monocular only as a type.")
conv('Spotting scope',"One entry is a spotting-scope line sold under its own name.","Spotting-scope lines of the earlier pass; no whole-space reference exists.")
conv('Night-vision viewer',"One entry is a night-vision viewer line sold under its own name.","Night-vision lines of the earlier pass; no whole-space reference exists.")
conv('Thermal-imaging viewer',"One entry is a thermal-imaging viewer line sold under its own name.","Thermal viewer lines of the earlier pass; no whole-space reference exists.")
# ---------- MICROSCOPES ----------
MN="One entry is a microscope line sold under its own name or a named historic model; models of the line are versions."
MS="Microscope lines of the earlier pass; the Wikipedia article Microscope names only the types (optical, electron, scanning probe), so no whole list of lines exists."
for kn in ['Compound light microscope','Stereo microscope','Polarising microscope','Digital microscope']:
    conv(kn,MN,MS,keep_r=True)
# ---------- WEATHER ----------
WN="One entry is a weather instrument line or historic form sold or collected under its own name; models are versions."
WS="Instrument types follow Wikipedia's List of weather instruments (thermometer, barometer, hygrometer, anemometer, pyranometer, rain gauge, wind vane, wind sock); lines are from the earlier pass."
wk=K['Weather station']
for kn in ['Weather station','Air thermometer','Hygrometer','Anemometer','Rain gauge','Barometer','Barograph','Geiger counter']:
    if kn=='Weather station':
        skip=('GW1202 gateway','SP-110')
    else: skip=()
    conv(kn,WN,WS,skip=skip)
# pyranometer + wind vane kinds
shw=[s for dp in d['depts'] if dp['n']=='Weather & Earth instruments' for s in dp['s'] if s['n']=='Weather stations & sensors'][0]
shw['k'].append({'n':'Pyranometer','d':'Sensor that measures incoming sunlight, sold for home stations and solar-power checks.','s':WL,'nl':WN,'sel':"Named in Wikipedia's List of weather instruments; line from the earlier pass.",'x':[E('Apogee SP-110','Pyranometer from Apogee Instruments.',WL,'Apogee Instruments')]})
shw['k'].append({'n':'Wind vane & windsock','d':'Simple devices that show wind direction and, for the windsock, rough speed.','s':WL,'nl':WN,'sel':"Wind vane and wind sock, both named in Wikipedia's List of weather instruments; they are commodity forms with no named lines.",'x':[]})
shw['k'].append({'n':'Disdrometer & ceilometer','d':'Professional sensors for raindrop size and cloud height, seldom owned at home.','s':WL,'nl':WN,'sel':"Disdrometer, ceilometer, transmissometer and present-weather sensor are named in Wikipedia's List of weather instruments; they are professional instruments with no home lines.",'x':[]})
# ---------- HISTORIC ----------
HN="One entry is a named instrument from Wikipedia's List of astronomical instruments; makers' pieces and replicas are versions."
HS="Every historic instrument in Wikipedia's List of astronomical instruments, grouped by the period of first use; modern detectors, space and electronic items in that list (CCD, CMOS, bolometer, photometer, spectrometer, interferometer, space telescope, computers) are out of scope here. Wikipedia's historical-instruments list could not be fetched (404)."
P1,P2,P3,P4='Ancient (to c. 500)','Medieval (500–1500)','Early modern (1500–1800)','Modern (from 1800)'
def addperiod(kn,period):
    for x in K[kn].get('x',[]):
        x['g']=period
for kn,p in [('Orrery',P3),('Celestial globe',P3),('Planisphere',P4),('Astrolabe',P2),('Quadrant',P2),('Backstaff',P3),('Sextant',P3)]:
    addperiod(kn,p)
for kn in ['Orrery','Celestial globe','Planisphere','Astrolabe','Quadrant','Backstaff','Sextant','Armillary sphere','Nocturnal']:
    K[kn]['nl']=HN; K[kn]['sel']=HS; K[kn]['xg']='by period'
K['Home planetarium projector']['nl']="One entry is a home planetarium projector line; models are versions."
K['Home planetarium projector']['sel']="Projector lines of the earlier pass; no whole-space reference exists."
conv('Home planetarium projector',K['Home planetarium projector']['nl'],K['Home planetarium projector']['sel'])
conv('Orrery',HN,HS,'by period',gold=P3,gnew=P4)
for x in K['Orrery']['x']:
    if x['n'] in('Grand Orrery',): x['g']=P3
K['Armillary sphere']['x']=[E('Armillary sphere','Model of sky objects built from a framework of rings.',AL,g=P1)]
K['Nocturnal']['x']=[E('Nocturnal','Tool for finding local time at night from the position of a star.',AL,g=P2)]
K['Astrolabe']['x'].append(E('Canterbury Astrolabe Quadrant','Medieval astrolabe quadrant found in England.',AL,g=P2))
K['Quadrant']['x'].append(E('Mural instrument','Angle-measuring quadrant fixed to a wall.',AL,g=P3))
K['Sextant']['x'].append(E('Octant','Reflecting instrument used mainly in navigation.',AL,g=P3,v=[vers('Sextant','Hadley octant')]))
K['Sextant']['x']=[x for x in K['Sextant']['x'] if x['n']!='Hadley octant']
sh=[s for dp in d['depts'] if dp['n']=='Sky models & historic instruments' for s in dp['s'] if s['n']=='Star finders & navigation instruments'][0]
sh['k'].append({'n':'Ancient & medieval calculating instrument','d':'Instruments and mechanisms for computing the sky: Antikythera mechanism, torquetum, equatorium, volvelle, triquetrum, astrarium, cosmolabe and others.','s':AL,'nl':HN,'sel':HS,'xg':'by period','x':[
 E('Nebra sky disk','Bronze disc from about 1600 BC, found in Germany, with sky symbols.',AL,g=P1),
 E('Antikythera mechanism','Ancient Greek analog astronomical computer.',AL,g=P1),
 E('Triquetrum','Ancient astronomical instrument.',AL,g=P1),
 E('Cosmolabe','Ancient astronomical instrument.',AL,g=P1),
 E('Torquetum','Medieval astronomical instrument.',AL,g=P2),
 E('Equatorium','Astronomical calculating instrument.',AL,g=P2),
 E('Volvelle','Paper construct with rotating parts.',AL,g=P2),
 E('Astrarium','Timepiece and astronomical prediction device.',AL,g=P2),
 E('Astronomical clock','Clock that displays astronomical information.',AL,g=P2,v=[V('Prague astronomical clock','','','medieval clock in the Czech Republic')]),
 E('Equatorial ring','Instrument for determining the moment of the equinoxes.',AL,g=P2)],
 'tt':[['Material',['Brass','Paper','Wood']],['Origin',['Antique','Reproduction']]]})
sh['k'].append({'n':'Sundial & gnomon','d':'Time-telling devices that use a shadow, from the scaphe to the garden dial.','s':AL,'nl':HN,'sel':HS,'x':[E('Sundial','Time-telling device.',AL,g=P1),E('Gnomon','Part of a sundial that casts a shadow.',AL,g=P1),E('Scaphe','Sundial said to have been invented by Aristarchus.',AL,g=P1)],'tt':[['Type',['Horizontal','Vertical','Armillary','Pocket']],['Origin',['Antique','Reproduction']]]})
sh['k'].append({'n':'Early navigation aid','d':'Simple sighting and latitude instruments from before the sextant.','s':AL,'nl':HN,'sel':HS,'x':[E('Kamal','Navigation device that determines latitude.',AL,g=P2),E('Celatone','Navigation aid that relies on tracking Jupiter\'s moons.',AL,g=P3),E('Dioptra','Classical surveying instrument from the 3rd century BCE.',AL,g=P1),E('Alidade','Device for sighting a distant object.',AL,g=P1)],'tt':[['Origin',['Antique','Reproduction']]]})
# ---------- write ----------
out=R+'out/E6.json'
json.dump(d,open(out+'.tmp','w'),ensure_ascii=False,indent=1); os.replace(out+'.tmp',out)
b=json.load(open(R+'out/E6_brands.json')); have={x['n'] for x in b['b']}
for n in sorted(newbrands):
    if n not in have: b['b'].append({'n':n})
json.dump(b,open(R+'out/E6_brands.json.tmp','w'),ensure_ascii=False,indent=1); os.replace(R+'out/E6_brands.json.tmp',R+'out/E6_brands.json')
print('written; new brands',len([n for n in newbrands if n not in have]))
