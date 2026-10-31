import sys; sys.path.insert(0,'/home/user/Possession-Taxonomy/rebuild/work/GAP_E6')
from common import *
d=load()
removed={}
REMOVE=['Telescope tripod & pier','Mount fitting','Star diagonal','Telescope camera adapter','Dew shield & heater','Microscope optics & parts','Microscope slide','Handheld magnifier','Stand magnifier','Loupe','Head-worn magnifier','Laboratory glassware','Measuring & dispensing','Laboratory balance','Hot plate & stirrer','Centrifuge','Laboratory thermometer','Petri dish','Incubator','Laminar-flow hood','Dissection set']
for n in REMOVE:
    k=find(d,n); removed[n]=len(k.get('m',[])); k.pop('m',None)
    k.pop('r',None) if n in('Microscope optics & parts','Head-worn magnifier') else None
NOUN={'Telescope mount':'telescope mount','Telescope finder':'telescope finder','Telescope focuser':'telescope focuser','Barlow lens':'Barlow lens','Binoviewer':'binocular viewer for telescopes','Astronomical filter':'astronomical filter','Microscope camera':'microscope camera','Cloud sensor':'cloud sensor for observatories','Focus motor':'motorised telescope focuser','Astrophotography controller':'astrophotography controller','Telescope eyepiece':'eyepiece line'}
def lines(k,noun):
    s=k['s']; have={e['n'].lower() for e in k['x']}
    for m,mk in k.pop('m'):
        n=m if (not mk or mk.lower() in m.lower()) else f'{mk} {m}'
        if n.lower() in have: continue
        txt=f'{noun[0].upper()+noun[1:]} sold by {mk}.' if mk else f'{noun[0].upper()+noun[1:]}.'
        k['x'].append(ent(n,txt,mk=mk,s=s,g='Maker lines',v=[{'n':m,'mk':mk,'y':'','d':''}]))
for n in ['Telescope mount','Telescope finder','Telescope focuser','Barlow lens','Binoviewer','Astronomical filter','Microscope camera','Cloud sensor','Focus motor','Astrophotography controller']:
    k=find(d,n); k.setdefault('x',[]); lines(k,NOUN[n])
# eyepiece: group Explore Scientific, Kellner as design
k=find(d,'Telescope eyepiece'); s=k['s']
es=[];rest=[]
for m,mk in k.pop('m'):
    (es if mk=='Explore Scientific' else rest).append((m,mk))
for m,mk in rest:
    if m=='Kellner':
        k['x'].append(ent('Kellner','Three-element eyepiece with an achromatic eye lens, a low-cost wide-field design from the nineteenth century.',y='1849',s='https://en.wikipedia.org/wiki/Eyepiece',g='Designs'))
        k['x'][-1]['y']='1849'
    else:
        n=m if m.lower().startswith(mk.lower()) or mk.lower() in m.lower() else f'{mk} {m}'
        k['x'].append(ent(n,f'Eyepiece line sold by {mk}.',mk=mk,s=s,g='Maker lines',v=[{'n':m,'mk':mk,'y':'','d':''}]))
k['x'].append(ent('Explore Scientific eyepiece series','Explore Scientific sells eyepieces in series named by apparent field: 52, 62, 68, 82, 100 and 120 degrees.',mk='Explore Scientific',s=s,g='Maker lines',
   v=[{'n':m,'mk':mk,'y':'','d':''} for m,mk in es if m!='Explore Scientific wide-field series']))
k.pop('r',None)
# astronomy camera grouped
k=find(d,'Astronomy camera'); s=k['s']; ms=k.pop('m'); k.pop('r',None)
grp={}
def key(m,mk):
    if mk=='ZWO':
        return 'ZWO ASI Pro cooled cameras' if (m in('ASI2600MC Pro','ASI2600','ASI6200','ASI294','ASI533','ZWO ASI Pro cooled camera')) else 'ZWO ASI planetary cameras'
    if mk=='QHY': return 'QHY5III cameras'
    return f'{mk} cameras'
for m,mk in ms: grp.setdefault((key(m,mk),mk),[]).append(m)
for (n,mk),vs in grp.items():
    k['x'].append(ent(n,f'Astronomy camera range sold by {mk}.',mk=mk,s=s,g='Maker lines',v=[{'n':v,'mk':mk,'y':'','d':''} for v in vs]))
save(d)
print(removed)
