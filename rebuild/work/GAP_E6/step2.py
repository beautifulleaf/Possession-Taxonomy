import sys; sys.path.insert(0,'/home/user/Possession-Taxonomy/rebuild/work/GAP_E6')
from common import *
d=load()
W='https://en.wikipedia.org/wiki/'
def add(k,items):
    have={e['n'].lower() for e in k['x']}
    for e in items:
        if e['n'].lower() not in have: k['x'].append(e)
# eyepiece
k=find(d,'Telescope eyepiece'); S=W+'Eyepiece'
for e in k['x']:
    if e['n'] in('Plössl','Orthoscopic','Kellner'): e['g']='Designs'
    if e['n'] in('Tele Vue Nagler','Tele Vue Ethos'): e['g']='Designs'
add(k,[ent('Huygens','Two air-spaced plano-convex lenses; the first compound eyepiece, now obsolete for short-focus telescopes.',mk='Christiaan Huygens',y='late 1660s',s=S,g='Designs'),
 ent('Ramsden','Two plano-convex lenses spaced closer than one focal length; its external focal plane suits reticles and micrometers.',mk='Jesse Ramsden',y='1782',s=S,g='Designs'),
 ent('Monocentric','Thick cemented triplet free of ghost reflections, giving a contrasty image with a narrow field near 25 degrees.',mk='H. A. Steinheil',y='c. 1883',s=S,g='Designs'),
 ent('Erfle','Five-element wide-field design that shows astigmatism and ghosting at high power.',mk='Heinrich Erfle',y='World War I era',s=S,g='Designs'),
 ent('König','Cemented doublet plus plano-convex singlet, with high eye relief and a field of about 55 degrees.',mk='Albert König',y='1915',s=S,g='Designs'),
 ent('RKE','Kellner-derived layout resembling a widely spaced König, with a slightly wider field than the Kellner.',mk='David Rank',y='late 1960s',s=S,g='Designs')])
for e in k['x']:
    if e['n']=='Kellner': e['mk']='Carl Kellner'
k['nl']='One entry is an eyepiece optical design named in the Wikipedia article Eyepiece or an eyepiece line sold under its own name; models and focal lengths are versions.'
k['xg']='design, then maker lines'
k['sel']='Eyepiece designs from the Wikipedia article Eyepiece (Huygens to Ethos; the negative-lens and convex-lens forms are the Galilean and Keplerian telescopes), then maker lines from retailer pages.'
# mounts
k=find(d,'Telescope mount'); S=W+'Telescope_mount'
for e in k['x']:
    e['g']='Designs' if e['n']=='German equatorial mount' else 'Maker lines'
add(k,[ent('Altazimuth mount','Mount that moves in altitude and azimuth as separate motions; digital tracking has made it common in large and amateur telescopes.',s=S,g='Designs'),
 ent('Equatorial fork mount','Equatorial mount that supports one or both ends of the polar axis.',s=S,g='Designs'),
 ent('Yoke mount','Equatorial mount, also called English mount, that supports the polar axis at both ends.',s=S,g='Designs'),
 ent('Cross-axis mount','Equatorial design that, like the German mount, needs large counterweights.',s=S,g='Designs'),
 ent('Equatorial platform','Platform that tilts on a polar axis under a fixed telescope so it tracks the sky; the Poncet platform is the common form.',s=S,g='Designs'),
 ent('Transit mount','Single-axis mount fixed in azimuth that rotates in altitude, used in transit telescopes.',s=S,g='Designs'),
 ent('Hexapod mount','Supports the mirror or tube on six extendable struts, allowing motion in all six degrees of freedom.',s=S,g='Designs')])
k['nl']='One entry is a mount design named in the Wikipedia article Telescope mount or a mount line sold under its own name; models are versions.'
k['xg']='design, then maker lines'
k['sel']='Mount designs from the Wikipedia article Telescope mount (fixed mounts are professional and left out), then maker lines from retailer and review pages. Complete: 7 of 13 designs in scope (the rest are fixed, fixed-altitude, alt-alt and altitude-altitude-azimuth mounts used only in observatories).'
# orrery
k=find(d,'Orrery'); S=W+'Orrery'
add(k,[ent("Dondi's astrarium",'Seven-faced astronomical clock showing the sun, moon and five planets, built by Giovanni Dondi dell\'Orologio.',mk='Giovanni Dondi dell\'Orologio',y='1348–1364',s=S,g='Medieval (500–1500)'),
 ent('Huygens planetary machine','Mechanical model of the solar system by Christiaan Huygens, built 1665–1681 and described in 1703.',mk='Christiaan Huygens',y='1703',s=S,g='Early modern (1500–1800)'),
 ent('Eisinga Planetarium','Room-sized moving model of the solar system built into a house ceiling in Franeker, Netherlands.',mk='Eise Eisinga',y='1774–1781',s=S,g='Early modern (1500–1800)'),
 ent('Bate orrery','Orrery in the Thinktank museum, Birmingham, made by Robert Brettell Bate.',mk='Robert Brettell Bate',y='c. 1812',s=S,g='Modern (from 1800)'),
 ent('Fulton orreries','Three orreries by John Fulton, including the one in Kelvingrove museum.',mk='John Fulton',y='1823–1833',s=S,g='Modern (from 1800)'),
 ent('Meccano orrery (Model 391)','Orrery built from Meccano parts, described in the Meccano Manual.',mk='Meccano',y='1918',s=S,g='Modern (from 1800)'),
 ent('LEGO Planet Earth and Moon in Orbit (42179)','LEGO Technic set that models the Earth and Moon in orbit.',mk='LEGO Group',y='2024',s=S,g='Modern (from 1800)')])
k['sel']="Orreries and planetary machines named in the Wikipedia article Orrery that a person can own or build, plus the earlier-pass lines. Complete: all 16 items of the article's list were considered; the Antikythera mechanism sits under Ancient & medieval calculating instrument and the Hesse-Kassel clocks, Armagh human orrery and Derby grand orrery are institutional or reconstructions, so out of scope."
# sundial
k=find(d,'Sundial & gnomon'); S=W+'Sundial'
sd=[('Equatorial sundial','Shadow falls on a plane perpendicular to the style, so hour lines are evenly spaced 15 degrees apart.',''),
('Horizontal sundial','Garden dial whose shadow falls on a level plane; hour lines are unevenly spaced and the style angle equals the latitude.',''),
('Vertical sundial','Dial on an upright plane with the style still parallel to the Earth\'s axis.',''),
('Polar sundial','Receiving plane parallel to the style, so the shadow slides sideways.',''),
('Analemmatic sundial','Dial with a movable style and figure-eight hour layout that corrects for the equation of time.',''),
('Heliochronometer','Precision dial that converts apparent solar time to mean or standard time.','1763'),
('Sunquest sundial','Dial designed by Richard L. Schmoyer that casts light onto an equatorial time scale and corrects for the equation of time.','1950s'),
('Nodus (spider-web) dial','Dial that uses a point rather than a style, with concentric hour lines.',''),
('Canonical sundial','Dial that marks the canonical hours of church services.','7th–14th century'),
('Shadow clock','Earliest known sundial type, in use around 1500 BC.','c. 1500 BC')]
add(k,[ent(n,t,y=y,s=S,g=('Ancient (to c. 500)' if n=='Shadow clock' else 'Medieval (500–1500)' if n.startswith('Canon') else 'Early modern (1500–1800)' if n=='Heliochronometer' else 'Modern (from 1800)' if n.startswith('Sunq') else 'Dial layouts')) for n,t,y in sd])
k['xg']='period or dial layout'
k['nl']='One entry is a sundial type named in the Wikipedia article Sundial.'
k['sel']='Sundial types described in the first 100,000 of 214,000 characters of the Wikipedia article Sundial; the remaining portable types (ring, capuchin, navicula, diptych) are read in a later window.'
save(d)
