import sys; sys.path.insert(0,'/home/user/Possession-Taxonomy/rebuild/work/GAP_E6')
from common import *
d=load(); W='https://en.wikipedia.org/wiki/'
def add(k,items):
    k.setdefault('x',[])
    have={e['n'].lower() for e in k['x']}
    for e in items:
        if e['n'].lower() not in have: k['x'].append(e)
k=find(d,'Stereo microscope'); S=W+'Stereo_microscope'
for e in k['x']:
    if e['n']=='Greenough stereo microscope': e['mk']='Horatio Saltonstall Greenough'; e['y']='1892'; e['d']='Two independent objectives focused on one object; designed 1892 and sold by Zeiss from 1896, the first practical stereo microscope.'; e['s']=S; e['g']='Designs'
add(k,[ent('Common main objective stereo microscope','Modern binocular layout with one shared main objective and parallel light paths for each eye.',s=S,g='Designs'),
 ent('Cycloptic stereo microscope','Galilean optics in a revolving drum give discrete magnification steps; made by AO Spencer.',mk='AO Spencer',s=S,g='Designs'),
 ent("Chérubin d'Orléans binocular microscope",'Early microscope with two separate optical paths.',mk="Chérubin d'Orléans",y='1671',s=S,g='Designs',role='origin')])
k=find(d,'Digital microscope'); S=W+'Digital_microscope'
add(k,[ent('Hirox digital microscope','First digital microscope, a control box and lens linked to a computer; all-in-one units followed around 2005.',mk='Hirox',y='1986',s=S,g='Designs',role='origin')])
k=find(d,'Sunshine recorder'); S=W+'Campbell%E2%80%93Stokes_recorder'
for e in k['x']: e['g']='Designs'; e['y']=e['y'] or '1853'; e['s']=S
add(k,[ent('Marvin sunshine recorder','Sunshine recorder generally used by the US National Weather Service.',s=S,g='Designs'),ent('Jordan sunshine recorder','Sunshine recorder named in the article\'s navigation list.',s=S,g='Designs')])
k['nl']='One entry is a sunshine-recorder design named in the Wikipedia article Campbell–Stokes recorder.'
k=find(d,'Pyranometer'); S=W+'Pyranometer'
add(k,[ent('Thermopile pyranometer','Measures solar irradiance with a thermopile under a dome; the classes of ISO 9060 apply.',s=S,g='Designs'),ent('Photodiode pyranometer','Photovoltaic sensor for solar irradiance, cheaper than a thermopile.',s=S,g='Designs')])
for e in k['x']: e['g']=e.get('g') or 'Maker lines'
# sundial claims
k=find(d,'Sundial & gnomon'); S=W+'Sundial'
k['sel']=f"Sundial types in the Wikipedia article Sundial, read to the end of its 214,193 characters. Covers {len(k['x'])} of about 35 named types or sections; left out are formula variants of fixed dials (declining, reclining, Lambert, London, bowstring, Foster-Lambert), curved-surface and prismatic dials, ring and noon marks and human shadows, which the page names without describing an owned object."
k=find(d,'Astrolabe')
k['sel']="Astrolabe types and makers named in the Wikipedia article Astrolabe, read to the end of its 147,170 characters; treatises and astronomers are not instruments and are left out."
k=find(d,'Thermometer') if False else None
k=find(d,'Air thermometer')
k['sel']="Principles from the Wikipedia article Thermometer, read to the end of its 137,990 characters (clinical, electronic-sensor, laboratory and industrial types are out of scope here), then maker lines. Covers 8 of about 30 named thermometer types in that article."
k=find(d,'Night-vision viewer')
k['sel']='Generations from the Wikipedia article Night-vision device, read to the end of its 126,167 characters (military procurement series such as OMNI are out of scope), then maker lines from the earlier pass. Covers all 6 generations; named military sets are not listed as they are not sold to the public.'
k=find(d,'Compound light microscope')
k['sel']=k['sel'].split(';')[0]+'; types from the Wikipedia article Optical microscope, read to its end (110,695 characters).'
# g by maker in large kinds
def bymaker(k):
    for e in k['x']:
        if e.get('g') in ('Maker lines',None,''):
            e['g']=(e.get('mk') or 'Maker lines')
    firsts=[e for e in k['x'] if e.get('g') not in {m for m in [e2.get('mk') for e2 in k['x']] if m}]
    k['x'].sort(key=lambda e:(0 if e['g'] not in {x.get('mk') for x in k['x'] if x.get('mk')} else 1))
for n in ['Spotting scope','Weather station','Stereo microscope','Compound light microscope','Digital microscope','Thermal-imaging viewer','Giant binoculars','Anemometer','Telescope mount','Astronomy camera','Telescope eyepiece']:
    k=find(d,n)
    for e in k['x']:
        if e.get('g') in ('Maker lines',None,''): e['g']=e.get('mk') or 'Maker lines'
    xg=k.get('xg')
    k['xg']=(xg.split(', then')[0]+', then maker' if xg else 'maker')
    # stable: non-maker (design) groups first
    designs={e['g'] for e in k['x'] if not e.get('mk') or e['g'] in('Designs','Types','Principles','Filter types')}
    k['x'].sort(key=lambda e:0 if e['g'] in ('Designs','Types','Principles','Filter types','Tubes') else 1)
# Binoculars: maker lines g -> maker
k=find(d,'Binoculars')
for e in k['x']:
    if e['g']=='Maker lines': e['g']=e.get('mk') or 'Maker lines'
# fill missing g where kind has xg or any entries
for _,_,k in kinds(d):
    xs=k.get('x') or []
    for e in xs:
        if not e.get('g'): e['g']=(e.get('mk') or 'Entries') if k.get('xg') or len(xs)>12 else e.get('g','') 
save(d)
