import json, re, os, collections
R='/home/user/Possession-Taxonomy/rebuild/out/'
d=json.load(open(R+'B3.json'))
kinds={}
for dp in d['depts']:
    for s in dp['s']:
        for k in s['k']: kinds[k['n']]=(dp,k)
mcount=collections.Counter(); became=[]; 
LH='https://www.lightology.com/index.php?module=how_to&sub=italian-lighting-design-history'
CD='https://www.casadiluce.ca/blogs/how-to/compasso-doro-award-winners'
MOMA='https://www.moma.org/collection/artists/1028'
ADI='https://www.adidesignmuseum.org/en/collection/'
WCD='https://en.wikipedia.org/wiki/Compasso_d%27Oro'
def E(n,mk,y,dd,s,a='',dt='',v=None,role=None,**kw):
    e={'n':n,'a':a,'d':dd,'mk':mk,'y':y,'s':s,'v':v or []}
    if dt: e['dt']=dt
    if role: e['role']=role
    e.update(kw); return e
def add(kn,es):
    k=kinds[kn][1]; names={x['n'].lower() for x in k.get('x',[])}
    for e in es:
        if e['n'].lower() not in names: k.setdefault('x',[]).append(e)
def setrole(kn,name,role):
    for x in kinds[kn][1].get('x',[]):
        if x['n']==name: x['role']=role
# --- new entries from fetched canon
add('Table lamp',[
 E('Bilia','FontanaArte','1932','Table lamp by Gio Ponti listed in the Lightology Italian lighting classics.',LH),
 E('Monachella','Azucena','1953','Table lamp by Luigi Caccia Dominioni listed in the Lightology Italian lighting classics.',LH),
 E('1853 glass lamp','FontanaArte','1954','Glass lamp by Max Ingrand listed in the Lightology Italian lighting classics.',LH),
 E('Fato','Arredoluce','1957','Table lamp by Gio Ponti listed in the Lightology Italian lighting classics.',LH),
 E('Acrilica','Oluce','','Table lamp by Joe Colombo listed in the Lightology Italian lighting classics; the page gives no year.',LH),
 E('Coupé','Oluce','1966','Table lamp by Joe Colombo listed in the Lightology Italian lighting classics.',LH),
 E('Biagio','Flos','','Table lamp by Tobia Scarpa listed in the Lightology Italian lighting classics; the page gives no year.',LH),
 E('Gibigiana','Flos','1980','Table lamp by Achille Castiglioni with a tilting mirror reflector; Lightology lists it with Stilnovo.',LH),
 E('Ashoka','Memphis','1981','Table lamp by Ettore Sottsass for Memphis listed in the Lightology Italian lighting classics.',LH),
 E('Super','Memphis','1981','Table lamp by Martine Bedin for Memphis listed in the Lightology Italian lighting classics.',LH),
])
add('Floor lamp',[
 E('Orbital','Foscarini','1992','Floor lamp by Ferruccio Laviani listed in the Lightology Italian lighting classics.',LH),
 E('Mite','Foscarini','2001','Floor light by Marc Sadler that won the Compasso d\'Oro.',CD,role='landmark'),
])
add('Desk lamp',[
 E('Spider','Oluce','1966','Clamp lamp by Joe Colombo; Lightology says it won the Compasso d\'Oro in 1967.',LH,role='landmark'),
 E('Lola','Luceplan','1989','Lamp by Paolo Rizzatto and Alberto Meda that won the Compasso d\'Oro (XV edition).',ADI+'lola-lamp/',role='landmark'),
 E('Ascent','Luceplan','2016','Table lamp with fixed hinge or base that won the Compasso d\'Oro; the page names no designer.',CD,role='landmark'),
])
add('Pendant light',[
 E('Viscontea','','1960','Hanging lamp by Achille Castiglioni held by MoMA; the page names no maker.',MOMA),
 E('Taraxacum','Flos','1960','Hanging lamp by Achille Castiglioni held by MoMA.',MOMA,v=[{'n':'Taraxacum88','mk':'Flos','y':'','d':''}]),
 E('Discovery','Artemide','2018','Suspension lamp that won the Compasso d\'Oro; the page names no designer.',CD,role='landmark'),
])
add('Wall light',[E('Counterbalance','Luceplan','2014','Wall lamp by Daniel Rybakken that won the Compasso d\'Oro.',ADI+'counterbalance-lamp/',role='landmark')])
add('Chandelier',[E('Stilnovo chandelier','Stilnovo','1955','Chandelier by Gaetano Scolari listed in the Lightology Italian lighting classics.',LH)])
for kn,nm in [('Floor lamp','Luminator'),('Floor lamp','Arco'),('Table lamp','Eclisse'),('Table lamp','Atollo'),('Desk lamp','Tolomeo'),('Pendant light','Parentesi'),('Table lamp','Snoopy')]:
    if nm!='Snoopy': setrole(kn,nm,'landmark')
setrole('Lava lamp','Astro','origin')
# Luminator version/Tolomeo year note
for x in kinds['Desk lamp'][1]['x']:
    if x['n']=='Tolomeo' and 'Compasso' not in x['d']: x['d']+=' Won the Compasso d\'Oro in 1989.'
# Arco
for x in kinds['Floor lamp'][1]['x']:
    if x['n']=='Arco' and 'MoMA' not in x['d']: x['d']+=' Held by MoMA; Products Career Award at the 2020 Compasso d\'Oro.'
# --- bulbs
add('Standard bulb',[
 E('Edison carbon-filament lamp','Edison','1879','First practical incandescent bulb according to historians Friedel and Israel; first successful test on 22 October 1879.','https://en.wikipedia.org/wiki/Incandescent_light_bulb',role='origin'),
 E('Swan incandescent lamp','Swan','1881','Incandescent bulb by Joseph Swan, installed and in daily use in London in 1881.','https://en.wikipedia.org/wiki/Incandescent_light_bulb'),
 E('Toshiba white LED lamp','Toshiba','2007','First commercial white LED lamp for homes, released by Toshiba in 2007.','https://en.wikipedia.org/wiki/LED_lamp',role='origin'),
 E('Philips Hue','Signify','2012','Smart bulb and lighting system launched in October 2012; owned by Signify, formerly Philips Lighting.','https://en.wikipedia.org/wiki/Philips_Hue',
   v=[{'n':'Gen 1','mk':'Signify','y':'2012','d':'29 October 2012'},{'n':'Gen 2','mk':'Signify','y':'2015','d':'4 October 2015'},{'n':'Gen 3','mk':'Signify','y':'2016','d':'2 October 2016'},
      {'n':'White','mk':'Signify','y':'','d':'fixed warm 2700 K'},{'n':'White Ambiance','mk':'Signify','y':'','d':'2200 K to 6500 K'},{'n':'White and Color Ambiance','mk':'Signify','y':'','d':'2000 K to 6500 K plus colour'}],
   own='Signify N.V.',tier='Global group',cty='Netherlands'),
 E('Nanoleaf One','Nanoleaf','2013','Smart bulb first launched as NanoLight on Kickstarter in January 2013.','https://en.wikipedia.org/wiki/Nanoleaf',own='Nanoleaf',tier='Independent',cty='Canada'),
 E('Nanoleaf Essentials','Nanoleaf','2020','Smart bulbs and lightstrips from 2020, the first Nanoleaf products to use Thread.','https://en.wikipedia.org/wiki/Nanoleaf',
   v=[{'n':'Matter-compatible Essentials','mk':'Nanoleaf','y':'c. 2022','d':'announced around 2022'}],own='Nanoleaf',tier='Independent',cty='Canada'),
])
add('Tube light',[E('GE Lumiline fluorescent lamp','General Electric','1938','Fluorescent tube lamp; GE built a prototype in 1934 and began sales in 1938 in four tube sizes.','https://en.wikipedia.org/wiki/Fluorescent_lamp',role='origin')])
# Coleman
for x in kinds['Gas & pressure lantern'][1]['x']:
    if x['n']=='Coleman pressure lantern': x.update(own='Newell Brands',own_y='2015',tier='Global group',cty='United States')
# --- cuts: torches
KEEP={'Maglite','SureFire','Kel-Lite','Fulton Industries','Coleman'}
for kn in ['Keychain light','Penlight','EDC flashlight','Tactical flashlight','Duty torch','Thrower','Hand searchlight','Right-angle flashlight','Headlamp','Clip-on light']:
    k=kinds[kn][1]
    k['x']=[x for x in k.get('x',[]) if x.get('mk') in KEEP]
    if not k['x']: del k['x']
# commodity: remove ScreenBar, BenQ
kinds['Monitor light bar'][1].pop('x',None)
# --- remove m everywhere, r in commodity kinds
mtot=0; mlist=[]
for kn,(dp,k) in kinds.items():
    for m in k.pop('m',[]): mtot+=1; mlist.append((kn,m[0],m[1]))
COMM=['Night light','Wake-up light','Monitor light bar','Flush ceiling light','Ceiling spotlight','Mirror light','Wall lantern','Post light','Floodlight','Path light','Spike light','Keychain light','Penlight','EDC flashlight','Tactical flashlight','Duty torch','Thrower','Headlamp','Clip-on light','Electric lantern','Work light','Standard bulb','Candle bulb','Globe bulb','Spot bulb','Capsule bulb','Tube light','Strip light','Lamp shade','Lamp base','Lamp spare parts','Hand searchlight','Right-angle flashlight','Lava lamp','Fibre-optic lamp','Decorative lantern','String light','Linear pendant','Salt lamp','Neon light']
for kn in COMM:
    kinds[kn][1].pop('r',None)
for kn in ['Table lamp','Floor lamp','Pendant light','Wall light']:
    k=kinds[kn][1]; k['r']=[r for r in k.get('r',[]) if r[0] in ('PH lamps',)]
    if not k['r']: del k['r']
# --- g by decade
def gof(y):
    mm=re.findall(r'\d{4}',y or '')
    if mm:
        yr=int(mm[0]); return 'Before 1900' if yr<1900 else f'{yr//10*10}s'
    if re.search(r'1[5-9]th|1[89]th|century|antiquity|Edo|Ottoman|Byzantine|tradition',y or ''): return 'Before 1900'
    return 'Date not stated'
LIGHT=['Table lamp','Floor lamp','Desk lamp','Pendant light','Chandelier','Wall light']
NL={'Table lamp':'One entry is a table-lamp design (such as Eclisse or Akari) with its maker, designer and year; sizes and finishes are versions.',
'Floor lamp':'One entry is a floor-lamp design with its maker, designer and year; sizes and finishes are versions.',
'Desk lamp':'One entry is a desk or task-lamp design with its maker, designer and year; sizes and finishes are versions.',
'Pendant light':'One entry is a hanging-lamp design with its maker, designer and year; sizes and finishes are versions.',
'Chandelier':'One entry is a chandelier type or a named chandelier design with its maker and year; sizes and finishes are versions.',
'Wall light':'One entry is a wall-lamp design with its maker, designer and year; sizes and finishes are versions.'}
CANON=("Follows design collections and awards on fetched pages: MoMA (Achille Castiglioni's works), the ADI Design Museum and the Compasso d'Oro lists (Wikipedia, Casa di Luce), and the Lightology list of Italian lighting classics; earlier-sourced classics stay. No single whole-space reference exists. "
 "Covers the MoMA Castiglioni page (6 of 6 lamps), the lighting winners named on the three Compasso d'Oro pages (not the full ADI list, which could not be fetched), and the Lightology lamps whose type the page states (23 of 41); the Lightology lamps of unstated type and museum holdings of the Design Museum, V&A and Vitra Design Museum are not covered because their collection pages could not be fetched.")
for kn in LIGHT:
    k=kinds[kn][1]; k['nl']=NL[kn]; k['sel']=CANON; k['xg']='Decade of design'
    for x in k['x']: x['g']=gof(x.get('y'))
    k['x'].sort(key=lambda x:(x['g'],x.get('y') or '',x['n']))
# other kinds with entries
SEL2={'Lava lamp':'Two lava-lamp lineages from the Wikipedia lava-lamp page, earlier sourced.','Plasma lamp':'Plasma-lamp lineages from earlier-sourced Wikipedia pages.','Light panel':'Smart light-panel systems (Nanoleaf from the fetched Nanoleaf page; Govee earlier sourced).'}
for kn,t in SEL2.items():
    k=kinds[kn][1]; k['nl']='One entry is a named product line of this kind; revisions are versions.'; k['sel']=t+' No whole-space reference exists; lines not on those pages are not covered.'
    k['xg']='Decade of design'
    for x in k.get('x',[]): x['g']=gof(x.get('y'))
TORCH=("Commodity kind: keeps only the lines the owner named as defining (Maglite, SureFire, Coleman), taken from their Wikipedia pages (Maglite, SureFire, Coleman Company, Flashlight), plus Kel-Lite and the Fulton MX-991/U named on those pages. "
 "Covers the lines on those pages; all other torch makers are out of scope.")
for kn in ['Keychain light','EDC flashlight','Tactical flashlight','Duty torch','Right-angle flashlight']:
    k=kinds[kn][1]; k['nl']='One entry is a torch line by a maker the Wikipedia pages describe as defining; models are versions.'; k['sel']=TORCH; k['xg']='Decade of design'
    for x in k['x']: x['g']=gof(x.get('y'))
for kn in ['Hurricane lantern','Oil & kerosene lamp','Candle lantern','Paper lantern','Gas & pressure lantern',"Safety & miner's lamp"]:
    k=kinds[kn][1]; k['nl']='One entry is a named lantern or lamp type or maker line from the earlier-sourced Wikipedia pages; sizes and models are versions.'
    k['sel']='Historic and heritage lantern types from earlier-sourced Wikipedia pages (Dietz, Coleman, Petromax, Tilley, Vapalux, Davy and related). Covers the types on those pages; no whole-space reference exists.'
    k['xg']='Decade of design'
    for x in k['x']: x['g']=gof(x.get('y'))
BULB=("Commodity kind: keeps only origin products named on the fetched Wikipedia pages (incandescent, fluorescent and LED lamp pages) and the smart lighting systems Philips Hue and Nanoleaf. "
 "Covers the first 100,000 characters of each lamp page; the LIFX page could not be fetched, so LIFX is not listed.")
for kn,(dp,k) in [(n,kinds[n]) for n in ['Standard bulb','Tube light']]:
    k['nl']='One entry is an origin product of its kind or a smart lighting system sold under its own name; generations and colour options are versions.'
    k['sel']=BULB; k['xg']='Decade of design'
    for x in k['x']: x['g']=gof(x.get('y'))
    k['x'].sort(key=lambda x:(x['g'],x.get('y') or '',x['n']))
# market panel
bulbs=[dp for dp in d['depts'] if dp['n']=='Bulbs & strips'][0]
bulbs['ms']=[
 {'mkt':'Global lighting (company revenue)','who':'Signify N.V.','share':'EUR 6.14 billion revenue','yr':2024,'s':'https://en.wikipedia.org/wiki/Signify_N.V.','note':'Revenue, not share; the page gives no market share. Sells mainly under the Philips brand (licensed), Philips Hue, WiZ and Color Kinetics.'},
 {'mkt':'Lighting (company revenue)','who':'GE Lighting','share':'about USD 3 billion revenue','yr':2011,'s':'https://en.wikipedia.org/wiki/GE_Lighting','note':'Revenue, not share. Sold to Savant Systems on 1 July 2020; the Wall Street Journal reported USD 250 million.'},
 {'mkt':'Lighting (corporate history)','who':'ams OSRAM','share':'not stated','yr':2020,'s':'https://en.wikipedia.org/wiki/Osram','note':'ams took over Osram in July 2020. Ledvance was spun off in 2016 and Osram Sylvania sold to Wesco in 2019. The page states a largest North American share without a year.'}]
json.dump(d,open(R+'B3.json.tmp','w'),ensure_ascii=False,indent=1); os.replace(R+'B3.json.tmp',R+'B3.json')
json.dump(mlist,open('m_removed.json','w'),ensure_ascii=False)
print(mtot)
