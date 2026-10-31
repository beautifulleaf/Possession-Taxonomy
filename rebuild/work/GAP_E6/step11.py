import sys,re; sys.path.insert(0,'/home/user/Possession-Taxonomy/rebuild/work/GAP_E6')
from common import *
d=load()
TT="Wikipedia's List of telescope types"
def designs(k): return sum(1 for e in k['x'] if e.get('g')!='Maker lines')
C={}
for n in ['Refractor telescope','Newtonian reflector','Cassegrain telescope','Gregorian & off-axis reflector','Schmidt-Cassegrain telescope','Maksutov-Cassegrain telescope','Schmidt astrograph','Specialist catadioptric telescope']:
    C[n]=lambda k:f"Complete: {len(k['x'])} of {len(k['x'])} in-scope designs in {TT}; designs used only by observatories and space missions are out of scope."
NC=lambda ref:(lambda k:f"No complete list exists; follows {ref}.")
RET='the retailer and review pages cited on each entry'
C.update({
'Dobsonian telescope':lambda k:"Covers 9 of about 14 named items in the Wikipedia article Dobsonian telescope; left out are custom one-offs (Teeter's 16-inch, the 36-inch hybrid, the 50-inch Fullum folded Newtonian) and the Telekit.",
'Smart telescope':NC("the Wikipedia articles Robotic telescope and Unistellar (the retailer list at skiesandscopes.com returned 403)"),
'Solar telescope':NC("retailer and review pages, since the Wikipedia article Solar telescope names only professional instruments"),
'Solar filter':lambda k:"Complete: 3 of 3 consumer filter types in the Wikipedia article Solar telescope (white-light, hydrogen-alpha, spectrohelioscope), plus its Herschel wedge.",
'Telescope mount':lambda k:"Covers 7 of 13 designs in the Wikipedia article Telescope mount; the rest (fixed, fixed-altitude, alt-alt and altitude-altitude-azimuth mounts) are observatory-only.",
'Star tracker':NC(RET),'Telescope finder':NC(RET),'Telescope focuser':NC(RET),'Binoviewer':NC(RET),'Filter wheel':NC(RET),'Focus motor':NC(RET),'Astrophotography controller':NC(RET),'Cloud sensor':NC(RET),'Sky-quality meter':NC(RET),'Astronomy camera':NC(RET),
'Barlow lens':lambda k:"Complete: 2 of 2 Barlow designs in the Wikipedia article Barlow lens (the microscope Barlow and teleconverter are variants, not owned kinds).",
'Telescope eyepiece':lambda k:"Complete: 11 of 11 eyepiece designs in the Wikipedia article Eyepiece (its Galilean and Keplerian forms are the telescopes under Refractor).",
'Astronomical filter':lambda k:"Covers 8 of about 11 filter types in the Wikipedia article Astronomical filter; left out are solar filters (own kind), the chromatic-aberration filter and the Wratten numbering scheme.",
'Opera glasses':lambda k:"Complete: 2 of 2 types in the Wikipedia article Opera glasses; makers have no complete list.",
'Binoculars':lambda k:"Complete: 6 of 6 prism systems in the Wikipedia article Binoculars (read to its end); maker lines have no complete list.",
'Giant binoculars':NC(RET),
'Monocular':lambda k:"Covers 18 of about 24 named models in the Wikipedia article Monocular; left out are novelty items and models named only in citations.",
'Spotting scope':lambda k:"Complete: 2 of 2 eyepiece layouts in the Wikipedia article Spotting scope; maker lines have no complete list.",
'Night-vision viewer':lambda k:"Complete: 6 of 6 generations in the Wikipedia article Night-vision device (read to its end); named military sets are not sold to the public.",
'Thermal-imaging viewer':NC(RET),
'Simple microscope':NC("the Wikipedia article Optical microscope"),'Pocket microscope':NC(RET),'Microscope camera':NC(RET),'Microscope slide':NC(RET),
'Compound light microscope':lambda k:"Covers 3 of about 19 microscope types in the Wikipedia article Optical microscope; electron, confocal, two-photon and other laboratory types are out of scope.",
'Stereo microscope':lambda k:"Complete: 4 of 4 designs in the Wikipedia article Stereo microscope (Chérubin d'Orléans, Greenough, common main objective, cycloptic); the Wenham and Jentzsch binoviewers show one image to both eyes and are not stereo.",
'Polarising microscope':lambda k:"Complete: 2 of 2 polarising types in the Wikipedia article Optical microscope (polarising, petrographic).",
'Inverted & metallurgical microscope':lambda k:"Complete: 1 of 1 in the Wikipedia article Optical microscope (inverted; metallurgical is a use, not a named type there).",
'Digital microscope':lambda k:"Complete: 2 of 2 types in the Wikipedia article Digital microscope (Hirox system, USB microscope).",
'Weather station':NC("the Wikipedia article Weather station (it names only Davis VantagePro and public networks) and retailer pages"),
'Galileo thermometer':NC("the Wikipedia article Thermometer"),
'Hygrometer':lambda k:"Covers 8 of about 22 types in the Wikipedia article Hygrometer; left out are optical, spectroscopic and laboratory types and historic prototypes with no design given.",
'Anemometer':lambda k:"Covers 7 of 13 types in the Wikipedia article Anemometer; left out are laser Doppler, acoustic resonance, Pitot-static and three-cup variants of the cup type.",
'Rain gauge':lambda k:"Covers 4 of 10 designs in the Wikipedia article Rain gauge; left out are Hooke's manual gauge, Jardi's pluviometer and professional weighing, optical and acoustic gauges.",
'Sunshine recorder':lambda k:"Complete: 3 of 3 recorders with a description in the Wikipedia article Campbell–Stokes recorder; Blake-Larsen, Elektor, Pers and BF3 are only listed there.",
'Stevenson screen':lambda k:"Complete: 3 of 3 shelter designs in the Wikipedia article Stevenson screen.",
'Pyranometer':lambda k:"Complete: 2 of 2 sensor principles in the Wikipedia article Pyranometer (thermopile, photodiode).",
'Barometer':lambda k:"Covers 6 of 9 types in the Wikipedia article Barometer; the Torricelli and Vidi entries repeat mercury and aneroid, and the storm glass and barograph have their own kinds.",
'Barograph':NC("the Wikipedia article Barometer"),'Storm glass':NC("the Wikipedia article Barometer"),
'Geiger counter':lambda k:"Covers 4 of 14 items in the Wikipedia article Geiger counter; left out are laboratory tubes, neutron tubes and hot-spot probes.",
'Home seismometer':lambda k:"Covers 3 of about 34 designs in the Wikipedia article Seismometer; the rest are museum pieces, professional or spacecraft instruments.",
'Orrery':lambda k:"Covers 9 of 16 items in the Wikipedia article Orrery; left out are the Antikythera mechanism (own kind), astronomical clocks, institutional reconstructions and the Armagh human orrery.",
'Armillary sphere':lambda k:"Covers 5 of about 30 examples in the Wikipedia article Armillary sphere; left out are ancient attributions without a surviving object, sculptures and replicas.",
'Celestial globe':lambda k:"Covers 6 of 9 globes in the Wikipedia article Celestial globe; left out are two museum globes and two Roman private pieces with no maker given.",
'Home planetarium projector':lambda k:"Covers 3 of 13 projectors in the Wikipedia article Planetarium; the rest are institutional dome systems.",
'Planisphere':lambda k:"Covers 2 of 12 items in the Wikipedia article Planisphere; the rest are world maps, online tools or printable files without a maker.",
'Astrolabe':lambda k:"Covers 11 of about 17 instruments in the Wikipedia article Astrolabe; left out are treatises, a reconstruction and instruments with no maker or design given.",
'Nocturnal':NC("the Wikipedia article List of astronomical instruments"),
'Quadrant':lambda k:"Complete: 6 of 6 quadrant types in the Wikipedia article Quadrant (instrument); Davis and Cole quadrants are under Backstaff and Hadley's under Sextant.",
'Backstaff':NC("the Wikipedia article List of astronomical instruments"),
'Sextant':lambda k:"Covers 6 of about 9 items in the Wikipedia article Sextant; left out are the aircraft sextant forms, bubble octant and Bris sextant, which the page only lists.",
'Ancient & medieval calculating instrument':NC("the Wikipedia article List of astronomical instruments"),
'Early navigation aid':NC("the Wikipedia article List of astronomical instruments"),
})
miss=[]
for _,_,k in kinds(d):
    if not k.get('x'): continue
    f=C.get(k['n'])
    if f is None:
        if re.search(r'(Complete: \d+ of \d+|Covers \d+ of about|No complete list)',k.get('sel') or ''): continue
        miss.append(k['n']); continue
    s=k.get('sel') or ''
    s=re.sub(r'\s*(Complete:|Covers \d+ of).*$','',s).strip()
    if s and not s.endswith('.'): s+='.'
    k['sel']=(s+' '+f(k)).strip()
print('unmapped',miss)
# xg for kinds with groups>1 but no xg
for _,_,k in kinds(d):
    x=k.get('x') or []
    if not x: continue
    gs=[e.get('g') for e in x]
    if len(set(gs))>1 and not k.get('xg'): k['xg']='design or type, then maker lines'; print('xg set',k['n'])
    if len(x)<=12 and not k.get('nl'): print('no nl',k['n'])
save(d)
