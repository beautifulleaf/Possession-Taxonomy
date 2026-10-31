import sys; sys.path.insert(0,'/home/user/Possession-Taxonomy/rebuild/work/GAP_E6')
from common import *
d=load(); W='https://en.wikipedia.org/wiki/'
def add(k,items):
    have={e['n'].lower() for e in k['x']}
    for e in items:
        if e['n'].lower() not in have: k['x'].append(e)
k=find(d,'Astronomical filter'); S=W+'Astronomical_filter'
for e in k['x']: e['g']='Maker lines'
add(k,[ent('Light pollution reduction filter','Broadband filter that blocks sodium and mercury vapour light and skyglow; helps show nebulae and galaxies from bright skies.',s=S,g='Filter types'),
 ent('UHC filter','Ultra-high contrast narrowband filter passing about 484 to 506 nm, the O-III and H-beta lines; suits planetary and emission nebulae.',s=S,g='Filter types'),
 ent('O-III filter','Passes the 496 and 501 nm oxygen-III lines that are strong in many emission nebulae.',s=S,g='Filter types'),
 ent('H-beta filter','Passes the 486 nm hydrogen-beta line.',s=S,g='Filter types'),
 ent('H-alpha filter','Passes the 656 nm hydrogen-alpha line of HII regions; narrow versions show solar prominences.',s=S,g='Filter types'),
 ent('Lunar filter','Neutral-density filter that cuts glare and improves contrast on the Moon.',s=S,g='Filter types'),
 ent('Planetary colour filter','Absorption filter in red, yellow, green or blue (Wratten numbers) that brings out planetary and lunar detail.',s=S,g='Filter types'),
 ent('Polarising filter (moon filter)','Two rotating polarising layers that adjust brightness from about 3 to 40 per cent; used for the Moon.',s=S,g='Filter types')])
k['x'].sort(key=lambda e:0 if e['g']=='Filter types' else 1)
k['xg']='filter type, then maker lines'
k['nl']='One entry is a filter type named in the Wikipedia article Astronomical filter or a filter line sold under its own name; sizes are versions.'
k['sel']='Filter types from the Wikipedia article Astronomical filter (solar filters are under Solar filter; the chromatic-aberration filter is a minor type left out), then maker lines.'
k=find(d,'Solar filter'); S=W+'Solar_telescope'
add(k,[ent('White-light solar filter','Very dark film or glass filter over the front of the telescope; shows sunspots but hides prominences.',s=S,g='Filter types'),
 ent('Hydrogen-alpha filter system','Narrow-bandwidth filter, often a Fabry–Perot etalon, that shows prominences and chromospheric detail.',s=S,g='Filter types'),
 ent('Spectrohelioscope','Instrument that scans the Sun in one spectral line; amateurs build them at home.',s=S,g='Filter types')])
for e in k['x']: e['g']=e.get('g') or 'Maker lines'
k['x'].sort(key=lambda e:0 if e['g']=='Filter types' else 1)
k['xg']='filter type, then maker lines'
k['sel']='Solar filter types from the Wikipedia article Solar telescope (the Herschel wedge is listed there too), then maker lines of the earlier pass; the article names no consumer models.'
k=find(d,'Solar telescope')
for e in k['x']: e['g']=e.get('g') or 'Maker lines'
k['sel']='Solar telescope lines of the earlier pass; the Wikipedia article Solar telescope names only professional instruments and does not mention Coronado, Lunt or DayStar, so no whole list exists.'
k=find(d,'Home planetarium projector'); S=W+'Planetarium'
add(k,[ent('Zeiss Model I','First Zeiss planetarium projector, shown on a 16 m dome at the Deutsches Museum, Munich.',mk='Carl Zeiss',y='1923',s=S,g='Planetarium classics',role='origin'),
 ent('Spitz A','First Spitz projector, throwing stars from a dodecahedron to cut machining costs; planets moved by hand.',mk='Armand Spitz',s=S,g='Planetarium classics'),
 ent('Learning Technologies portable planetarium','Patented portable system that projected from removable cylinders, designed by Philip Sadler.',mk='Learning Technologies',y='1977',s=S,g='Planetarium classics')])
k['x'].sort(key=lambda e:0 if e['g']=='Planetarium classics' else 1)
k['xg']='planetarium classics, then home projector lines'
k['sel']='Classic projectors from the Wikipedia article Planetarium (institutional dome systems such as Digistar and Universarium are out of scope), then home projector lines of the earlier pass.'
k=find(d,'Opera glasses'); S=W+'Opera_glasses'
add(k,[ent('Folding opera glasses','Metal and glass pocket opera glasses with a leatherette cover; common since the 1890s and most popular in the mid-twentieth century.',y='1890s',s=S,g='Types'),
 ent('Lorgnette-style opera glasses','Ornamental opera glasses on a handle, modelled on nineteenth-century lorgnettes.',y='19th century',s=S,g='Types')])
k['x'].sort(key=lambda e:0 if e['g']=='Types' else 1)
k['xg']='type, then maker lines'
k['sel']='Types named in the Wikipedia article Opera glasses (it lists no makers or models), then maker lines of the earlier pass.'
save(d)
