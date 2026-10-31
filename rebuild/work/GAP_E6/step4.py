import sys; sys.path.insert(0,'/home/user/Possession-Taxonomy/rebuild/work/GAP_E6')
from common import *
d=load(); W='https://en.wikipedia.org/wiki/'
def add(k,items):
    have={e['n'].lower() for e in k['x']}
    for e in items:
        if e['n'].lower() not in have: k['x'].append(e)
k=find(d,'Night-vision viewer'); S=W+'Night-vision_device'
for e in k['x']: e['g']='Maker lines'
add(k,[ent('Generation 1 image intensifier','Passive intensifier tube needing some moonlight; the AN/PVS-1 Starlight scope of the 1960s was the first.',s=S,g='Intensifier generations',y='1960s'),
 ent('Generation 2 microchannel plate intensifier','Adds a microchannel plate for about 20,000 times gain, as in the AN/PVS-5 goggles of the 1970s.',s=S,g='Intensifier generations',y='1970s'),
 ent('Generation 3 gallium arsenide intensifier','Gallium arsenide photocathode with 30,000 to 50,000 times gain; the AN/PVS-14 monocular is the common form.',s=S,g='Intensifier generations',y='late 1980s'),
 ent('Generation 3 autogated intensifier','Autogating power supply that adapts quickly to changing light; sometimes sold as Gen 4 though the US NVESD does not recognise a Gen 4.',s=S,g='Intensifier generations'),
 ent('Fusion night vision','Intensifier image overlaid with a thermal image, as in the AN/PSQ-42 ENVG-B.',s=S,g='Intensifier generations'),
 ent('Active infrared viewer (Generation 0)','Viewer that needs an infrared searchlight; the German Vampir and the US Sniperscope of the Second World War.',s=S,g='Intensifier generations',y='before 1945')])
k['x'].sort(key=lambda e:0 if e['g']=='Intensifier generations' else 1)
k['xg']='intensifier generation, then maker lines'
k['nl']='One entry is a night-vision technology generation named in the Wikipedia article Night-vision device or a viewer line sold under its own name.'
k['sel']='Generations from the first 100,000 of 126,000 characters of the Wikipedia article Night-vision device (military procurement series such as OMNI are out of scope), then maker lines from the earlier pass.'
k=find(d,'Planisphere'); S=W+'Planisphere'
add(k,[ent('Usus Astronomicus Planisphaerii Stellati','First star chart to carry the name planisphere.',mk='Jacob Bartsch',y='1624',s=S,g='Early modern (1500–1800)',role='origin'),
 ent("Philips' Planisphere",'Rotating star chart sold by Philips, shown in the Wikipedia article.',mk='Philips',y='c. 1900',s=S,g='Modern (from 1800)')])
k['sel']="Named planispheres in the Wikipedia article Planisphere (12 listed; Ptolemy's and Mercator's planisphaerium are maps, not star charts, and the online and printable tools are software, so out of scope)."
k=find(d,'Celestial globe'); S=W+'Celestial_globe'
add(k,[ent('Al-Sahli celestial globe','Earliest surviving celestial globe, made in Valencia, showing the 48 classical constellations.',mk='Ibrahim ibn Said al-Sahli',y='1080–1085',s=S,g='Medieval (500–1500)',role='origin'),
 ent('Maragha globe','Inlaid brass globe from the Maragha observatory showing the 48 Ptolemaic constellations.',mk='Muhammad b. Mu\'ayyad al-\'Urdi',y='1288',s=S,g='Medieval (500–1500)'),
 ent('Farnese Atlas globe','Roman marble statue of Atlas holding a celestial globe of about 65 cm.',y='2nd century',s=S,g='Ancient (to c. 500)'),
 ent('Mughal celestial globe','Globe with Arabic and Sanskrit inscriptions.',mk='Muhammad Saleh Thattvi',y='1663–4',s=S,g='Early modern (1500–1800)'),
 ent('Lahore celestial globe','One-piece seamless globe with meridian and horizon rings.',mk='Diya\' ad-din Muhammad',y='1668',s=S,g='Early modern (1500–1800)')])
k['sel']='Named globes in the Wikipedia article Celestial globe (museum pieces are listed as the canon of historic globes; the two Metropolitan Museum globes and two Roman private pieces are not added because the page gives no maker).'
k=find(d,'Home seismometer'); S=W+'Seismometer'
for e in k['x']: e['g']='Home sensors'
add(k,[ent('Houfeng Didong Yi','Bronze seismoscope with dragon heads that dropped balls into toads to show the direction of a quake.',mk='Zhang Heng',y='132',s=S,g='Historic designs',role='origin'),
 ent('Palmieri seismometer','Metal pendulums that closed a circuit to stop a clock, widely distributed in the nineteenth century.',mk='Luigi Palmieri',y='1856',s=S,g='Historic designs'),
 ent('Milne horizontal pendulum seismograph','Early modern horizontal-pendulum design, the basis of later seismometers.',mk='John Milne',y='1880',s=S,g='Historic designs'),
 ent('Quake-Catcher Network detector','Residential quake detector built into a computer.',mk='Quake-Catcher Network',s=S,g='Home sensors')])
k['x'].sort(key=lambda e:0 if e['g']=='Historic designs' else 1)
k['xg']='historic designs, then home sensors'
k['nl']='One entry is a seismometer design named in the Wikipedia article Seismometer that a person could own or collect, or a home sensor line.'
k['sel']='Designs from the Wikipedia article Seismometer (34 listed; professional broadband, geophone and spacecraft instruments are out of scope, and the other nineteenth-century pendulum devices exist only in museums).'
save(d)
