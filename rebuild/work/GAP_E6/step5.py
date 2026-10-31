import sys; sys.path.insert(0,'/home/user/Possession-Taxonomy/rebuild/work/GAP_E6')
from common import *
d=load(); W='https://en.wikipedia.org/wiki/'
def add(k,items):
    k.setdefault('x',[])
    have={e['n'].lower() for e in k['x']}
    for e in items:
        if e['n'].lower() not in have: k['x'].append(e)
k=find(d,'Air thermometer'); S=W+'Thermometer'
for e in k['x']: e['g']='Maker lines'
add(k,[ent('Thermoscope','Air-filled bulb joined to a partly water-filled tube; shows relative heat changes but has no scale.',mk='Galileo Galilei',y='late 16th century',s=S,g='Principles',role='origin'),
 ent('Air thermometer','Vertical tube closed by an air bulb and opening into water, with a scale; the water level tracks air expansion.',mk='Santorio Santorio',y='1625',s=S,g='Principles'),
 ent('Sealed liquid-in-glass thermometer','Sealed tube with a bulb and a numbered scale, independent of air pressure; the modern form dates from about 1654.',mk='Ferdinando II de\' Medici',y='c. 1654',s=S,g='Principles'),
 ent('Mercury-in-glass thermometer','Reliable mercury thermometer that replaced alcohol and water mixtures; accurate but toxic.',mk='Daniel Gabriel Fahrenheit',y='1714',s=S,g='Principles'),
 ent('Alcohol thermometer','Liquid-expansion thermometer using alcohol, less reliable than mercury in its first form.',mk='René Antoine Ferchault de Réaumur',y='1730',s=S,g='Principles'),
 ent("Six's maximum-minimum thermometer",'Records the highest and lowest temperatures; used in meteorology and climatology.',s=S,g='Principles'),
 ent('Bimetallic thermometer','Two metals with different expansion coefficients; used in ovens and meat thermometers.',s=S,g='Principles'),
 ent('Liquid crystal thermometer','Thermochromic compounds show the temperature; used in forehead thermometers and mood rings.',s=S,g='Principles')])
k['x'].sort(key=lambda e:0 if e['g']=='Principles' else 1)
k['xg']='principle, then maker lines'
k['nl']='One entry is a home or outdoor thermometer principle named in the Wikipedia article Thermometer, or a thermometer line sold under its own name.'
k['sel']='Principles from the first 100,000 of 138,000 characters of the Wikipedia article Thermometer (clinical, electronic-sensor, laboratory and industrial types are out of scope here; the last 38,000 characters are not read), then maker lines.'
k=find(d,'Quadrant'); S=W+'Quadrant_(instrument)'
add(k,[ent('Sinecal quadrant','Gridded quadrant with a 90 degree arc, cord, bead and plumb bob, used for trigonometry and observations.',mk='Muhammad ibn Musa al-Khwarizmi',y='9th century',s=S,g='Medieval (500–1500)',role='origin'),
 ent('Horary quadrant','Tells the time of day from the sun\'s position, using equal or unequal hours; the oldest found dates to about 1300.',y='c. 1300',s=S,g='Medieval (500–1500)'),
 ent('Islamic astrolabe quadrant','Half of an astrolabe plate with a cord and bead to mark the positions of the sun or stars.',s=S,g='Medieval (500–1500)'),
 ent('Geometric quadrant','Quarter-circle wood or brass panel with sights and a plumb bob, used by surveyors and navigators; marine examples from about 1460.',y='c. 1460',s=S,g='Medieval (500–1500)')])
k['sel']='Quadrant types named in the Wikipedia article Quadrant (instrument): 8 of 8 types described there (Cole and Hadley quadrants are under Backstaff and Sextant).'
# new kinds: guide scope & off-axis guider
sh=None
for dp in d['depts']:
    for s in dp['s']:
        if s['n']=='Astrophotography': sh=s
G='https://astrobackyard.com/guide-scope-for-astrophotography/'
names={k['n'] for k in sh['k']}
if 'Guide scope' not in names:
    sh['k'].append({'n':'Guide scope','a':'autoguiding scope · guider','d':'Small second telescope on the main rig; a camera on it watches a star so software can correct the mount\'s tracking.','s':G,
      'x':[ent('Orion 50mm Mini Guide Scope','Compact guide scope sold by Orion for autoguiding.',mk='Orion',s=G,g='Maker lines'),
           ent('William Optics UniGuide 50mm','50 mm slide-base guide scope.',mk='William Optics',s=G,g='Maker lines'),
           ent('William Optics 32mm Guide Scope','32 mm guide scope.',mk='William Optics',s=G,g='Maker lines'),
           ent('ZWO ASI120MM Mini','Small monochrome camera used for autoguiding.',mk='ZWO',s=G,g='Guide cameras'),
           ent('Starlight Xpress Lodestar X2','Guide camera used with an off-axis guider.',mk='Starlight Xpress',s=G,g='Guide cameras')],
      'nl':'One entry is a guide scope or guide camera line sold under its own name.','xg':'guide scopes, then guide cameras',
      'sel':'No complete list exists; follows the AstroBackyard guide-scope article, one retailer-neutral overview.',
      'tt':[['Guiding method',['Separate guide scope','Off-axis guider']]]})
    sh['k'].append({'n':'Off-axis guider','a':'OAG','d':'Pick-off prism that diverts a star from the main telescope\'s own field to a guide camera, so guiding runs at the main focal length.','s':G})
save(d)
