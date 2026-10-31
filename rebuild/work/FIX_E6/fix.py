import json,copy
D=json.load(open('out/E6.json'))
def kinds():
    for dp in D['depts']:
        for s in dp['s']:
            for k in s['k']: yield dp,s,k
def get(n):
    for dp,s,k in kinds():
        if k['n']==n: return dp,s,k
    raise KeyError(n)
def drop(n):
    dp,s,k=get(n); s['k'].remove(k); return k
def uniq(lst):
    out=[]
    for t in lst:
        if t not in out: out.append(t)
    return out
def merge(target,names,newname=None,d=None,a=None,typ=None,s=None):
    tk=get(target)[2]
    ms=list(tk.get('m',[])); ts=list(tk.get('t',[])); rs=list(tk.get('r',[]))
    for n in names:
        k=drop(n); ms+=k.get('m',[]); rs+=k.get('r',[]); ts+=k.get('t',[]) if typ is None else []
        ts.append(n.lower() if typ is None else n.lower())
    if newname: tk['n']=newname
    if d: tk['d']=d
    if a is not None: tk['a']=a
    if typ is not None: tk['t']=typ
    else: tk['t']=uniq(ts)
    if s: tk['s']=s
    tk['m']=uniq(ms)
    if rs: tk['r']=uniq(rs)
    return tk
# E6-1
dob=get('Newtonian & Dobsonian telescope')[2]
X=dob['x']; dobs=X[0]; newt=X[1]
DS='https://en.wikipedia.org/wiki/Dobsonian_telescope'
coul=[v for v in dobs['v'] if v['mk']=='Coulter Optical']
obs=[v for v in dobs['v'] if v['mk']=='Obsession Telescopes']
dobs['v']=[v for v in dobs['v'] if v not in coul+obs]
dobs['v'][1:1]=[]
A_coul={"n":"Coulter Odyssey","a":"","d":"Large-aperture Dobsonians built on Sonotube tubes by Coulter Optical, which helped popularise the type.","mk":"Coulter Optical","y":"1980s","s":DS,"v":[v for v in coul if v['n']=='Odyssey']+[v for v in coul if v['n']!='Odyssey'],"dt":"aperture sizes in several diameters · cardboard-composite tube"}
A_obs={"n":"Obsession truss Dobsonian","a":"","d":"The first commercial truss-tube Dobsonian, a collapsible design for large apertures.","mk":"Obsession Telescopes","y":"1989","s":DS,"v":obs,"dt":"truss tube · large aperture"}
A_astro={"n":"Edmund Astroscan","a":"Astroscan","d":"Compact 4.25-inch f/4.2 Newtonian in a plastic ball-shaped body, sold for wide-field viewing by beginners.","mk":"Edmund Scientific","y":"1976","s":"https://en.wikipedia.org/wiki/Astroscan","v":[],"dt":"ABS body · 15 mm and 28 mm eyepieces · production ended 2013"}
dob['x']=[newt,dobs,A_coul,A_obs,A_astro]
# E6-2 antique makers
ref=get('Refractor telescope')[2]
ref['x'].append({"n":"Dollond achromatic refractor","a":"","d":"Achromatic refracting telescope from the London firm of John and Peter Dollond, built on John Dollond's 1758 patent.","mk":"Dollond","y":"1758","s":"https://en.wikipedia.org/wiki/Achromatic_lens","v":[{"n":"Vine Street business opened","mk":"Dollond","y":"1750","d":"Peter Dollond, near Hatton Garden"},{"n":"John Dollond achromatic patent","mk":"Dollond","y":"1758","d":""}],"dt":"brass tube · achromatic doublet objective"})
cl=get('Compound light microscope')[2]
cl['x'].insert(0,{"n":"Culpeper-type microscope","a":"","d":"Tripod-mounted compound microscope of the kind made by London instrument maker Edmund Culpeper.","mk":"Edmund Culpeper","y":"c.1700","s":"https://en.wikipedia.org/wiki/Edmund_Culpeper","v":[],"dt":"tripod stand · antique brass"})
# Spectroscope kind (lab instruments)
SP={"n":"Spectroscope","a":"hand spectroscope · spectrometer","d":"Instrument that splits light into a spectrum, with a prism or grating, to identify materials or light sources.","t":["prism","diffraction grating","hand-held","gemmological"],"s":"https://en.wikipedia.org/wiki/Spectroscope"}
# E6-3 skipped. E6-4 lab
merge('Beaker',['Laboratory flask','Test tube','Distillation glassware'],newname='Laboratory glassware',a='beaker · flask · test tube',
  d='Beakers, flasks, test tubes and distillation glassware for holding, heating and mixing liquids.',
  typ=['beaker','flask','test tube','round-bottom flask','condenser','still head'],s=get('Distillation glassware')[2]['s'])
merge('Graduated cylinder',['Pipette'],newname='Measuring & dispensing',a='graduated cylinder · pipette',
  d='Graduated cylinders and pipettes that measure and transfer set volumes of liquid.',typ=['graduated cylinder','pipette'])
merge('Laboratory balance',['Laboratory thermometer','Magnetic stirrer','Mini centrifuge'],newname='Lab instruments',a='balance · stirrer · centrifuge',
  d='Small bench instruments for weighing, heating, stirring and separating samples.',typ=['laboratory balance','laboratory thermometer','magnetic stirrer','mini centrifuge'])
merge('Petri dish',['Dissection set','Incubator','Laminar-flow hood'],newname='Culture & sterile kit',a='petri dish · incubator',
  d='Petri dishes, dissection sets, incubators and sterile hoods for growing cultures and preparing specimens.',typ=['petri dish','dissection set','incubator','laminar-flow hood'])
for n in ['Beaker','Laboratory glassware']: pass
_,sh,_=get('Lab instruments'); 
# Move 'Culture & sterile kit' and add Spectroscope to the instruments shelf
ck=drop('Culture & sterile kit'); sh['k'].append(ck); sh['k'].append(SP)
# E6-5
merge('Telescope tripod',['Equatorial wedge','Polar scope','Mount hardware'],newname='Mount accessory',a='tripod · equatorial wedge · polar scope',
  d='Tripods, equatorial wedges, polar scopes, counterweights and rings that support, align and balance a telescope on its mount.',
  typ=['telescope tripod','equatorial wedge','polar scope','counterweight','tube rings','dovetail bar','pier extension'])
ws=get('Weather station')[2]
for n in ['Wind vane','Windsock','Solar radiation sensor']:
    k=drop(n); ws['m']=uniq(ws['m']+k.get('m',[])); ws['t'].append(n.lower())
# E6-6
dp,sh,_=get('Weather station')
sh2=[s for s in dp['s'] if s['n']=='Barometers & weather glasses'][0]
gk=drop('Geiger counter'); sk=drop('Home seismometer')
cur=[drop('Storm glass'),drop('Galileo thermometer')]
i=dp['s'].index(sh2)
dp['s'].insert(i,{"n":"Earth & radiation sensors","k":[gk,sk]})
dp['s'].append({"n":"Weather curios","k":cur})
dp['s']=[s for s in dp['s'] if s['k']]
json.dump(D,open('out/E6.json.tmp','w'),ensure_ascii=False,indent=1)
# brands
B=json.load(open('out/E6_brands.json'))
B['b']+= [
 {"n":"Edmund Scientific","c":"United States","seg":"Specialist","kf":"Astroscan","d":"US science-supply company that sold the Astroscan wide-field telescope from 1976 to 2013.","sig":["Edmund Astroscan"],"s":"https://en.wikipedia.org/wiki/Astroscan"},
 {"n":"Dollond","c":"United Kingdom","f":"1750","seg":"Heritage manufactory","kf":"achromatic telescopes","d":"London optical firm founded by Peter Dollond in Vine Street near Hatton Garden in 1750; John Dollond joined in 1752.","sig":["Dollond achromatic refractor"],"s":"https://en.wikipedia.org/wiki/Dollond_%26_Aitchison"},
 {"n":"Edmund Culpeper","c":"United Kingdom","seg":"Heritage manufactory","kf":"tripod microscopes","d":"London instrument maker (1660-1738) known for tripod-mounted compound microscopes.","sig":["Culpeper-type microscope"],"s":"https://en.wikipedia.org/wiki/Edmund_Culpeper"}]
json.dump(B,open('out/E6_brands.json.tmp','w'),ensure_ascii=False,indent=1)
T=json.load(open('out/E6_traditions.json'))
T['t'].append({"n":"London scientific-instrument trade","g":"Scientific instruments","r":"England (London)","p":"18th century","d":"London workshops around Hatton Garden making optical instruments such as achromatic telescopes and tripod microscopes.","forms":["Achromatic refractor","Culpeper-type microscope"],"ctr":["Vine Street near Hatton Garden","Dollond","Edmund Culpeper"],"s":"https://en.wikipedia.org/wiki/Dollond_%26_Aitchison"})
json.dump(T,open('out/E6_traditions.json.tmp','w'),ensure_ascii=False,indent=1)
