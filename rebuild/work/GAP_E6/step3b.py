import sys; sys.path.insert(0,'/home/user/Possession-Taxonomy/rebuild/work/GAP_E6')
from common import *
d=load(); S='https://en.wikipedia.org/wiki/Sundial'
k=find(d,'Sundial & gnomon')
for e in k['x']: e['g']='Fixed dials'
P=[('Ring dial','Ring hung vertically and turned to the sun; light through a small hole falls on hour curves inside.','William Oughtred','c. 1600'),
('Capuchin dial','Altitude dial: a card aligned edge-on to the sun with a bead on a weighted string marking the time.','',''),
('Navicula','Altitude dial shaped like a small ship, with a plumb line on a sliding cursor.','',''),
('Diptych sundial','Two hinged flat faces that fold into a pocket box, with a string gnomon.','','c. 1612'),
("Shepherd's dial",'Portable cylindrical dial hung from a string with a knife-like gnomon twisted to correct for the equation of time.','',''),
('Sundial cannon','Novelty dial where a lens focuses noon sunlight onto a miniature cannon pan, igniting gunpowder.','','late 18th to early 19th century'),
('Multiface dial','Sundials on every face of a polyhedron, usually a cube.','',''),
('Bifilar sundial','Two non-intersecting threads parallel to the dial; the crossing of their shadows gives local solar time.','Hugo Michnik','1922'),
('Benoy dial','Passes sunlight through a thin slit and reflects it into a sheet of light instead of a shadow.','Walter Gordon Benoy',''),
('Globe dial','Sphere aligned with the Earth\'s axis with a spherical vane; time is read from the sun\'s azimuth.','',''),
('Digital sundial','Sunlight strikes numerals to display the current time.','',''),
('Reflection sundial','Small mirror on a south-facing window sill casts a spot of light onto the ceiling.','Isaac Newton','')]
have={e['n'].lower() for e in k['x']}
for n,t,mk,y in P:
    if n.lower() not in have: k['x'].append(ent(n,t,mk=mk,y=y,s=S,g='Portable dials' if n in('Ring dial','Capuchin dial','Navicula','Diptych sundial',"Shepherd's dial") else 'Novelty and modern dials' if n in('Sundial cannon','Digital sundial','Benoy dial','Bifilar sundial','Globe dial','Multiface dial','Reflection sundial') else 'Fixed dials'))
for e in k['x']:
    if e['n'] in('Sunquest sundial','Heliochronometer','Canonical sundial'): e['g']='Fixed dials'
k['xg']='fixed dials, portable dials, novelty and modern dials'
k['sel']='Sundial types in the Wikipedia article Sundial, read to character 200,000 of 214,193; the last window (200,000 onward) holds notes and references. Covers 33 of 33 named types; shadow-clock and scaphe origin items kept.'
save(d)
