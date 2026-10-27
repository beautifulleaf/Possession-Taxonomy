import sys; sys.path.insert(0, 'work/E1/agent')
from lib import *
BG = WP + '1:10_radio-controlled_off-road_buggy'; TC = WP + 'Tamiya_Corporation'; KY = WP + 'Kyosho'; TX = WP + 'Traxxas'; AE = WP + 'Associated_Electrics'
SX = WP + 'Scalextric'; CA = WP + 'Carrera_(slot_car_brand)'; AU = WP + 'Aurora_AFX'; PC = WP + 'Pancake_(slot_car)'; NI = WP + 'Ninco'; M4 = WP + 'Mini_4WD'
rc = K('Radio-controlled vehicle', 'A car, truck, boat, aircraft or hobby drone controlled by radio, sold as a toy or a hobby-grade model.', 'https://canyonhobbies.com/collections/cars-trucks',
  a='RC vehicle · RC car', t=['Toy-grade', 'Hobby-grade kit', 'Ready-to-run (RTR)', 'Electric (brushed or brushless)', 'Nitro (glow engine)', 'Off-road buggy', 'Monster truck', 'Short-course truck', 'Stadium truck',
   'Touring car', 'Rock crawler or trail truck', 'Drift car', 'RC boat', 'RC aircraft', 'RC helicopter', 'Hobby drone (no camera)', '1:8', '1:10', '1:12', '1:24 and smaller'],
  x=[X('Tamiya Porsche 934 Turbo RSR', '1:12 on-road car that started Tamiya radio control and the RC car boom.', 'Tamiya', '1976', TC),
     X('Tamiya Rough Rider', 'Early off-road buggy with three-speed gearbox and independent suspension.', 'Tamiya', '1979', BG),
     X('Tamiya Grasshopper', '2WD 1:10 buggy on a plastic bathtub chassis, reportedly the best-selling RC car.', 'Tamiya', '1984', BG,
       [('58346 re-release', 'Tamiya', '2005', '')], dt='motor · body colour · original or re-release'),
     X('Tamiya Hornet', 'Faster sister of the Grasshopper on the same chassis; launched the 2WD buggy boom.', 'Tamiya', '1984', 'https://www.tamiyaclub.com/car.asp?cid=558',
       [('58336 re-release', 'Tamiya', '2004', 'no hump battery, changed stickers')]),
     X('Team Associated RC10', 'Aluminium-chassis 1:10 electric racing buggy that swept the first off-road world championship.', 'Team Associated', '1984', AE,
       [('RC10 at first IFMAR 1:10 off-road worlds', 'Team Associated', '1985', 'first, second and third'), ('B44', 'Team Associated', '2007', '4WD')]),
     X('Kyosho Optima', '4WD buggy with double wishbones on all four corners.', 'Kyosho', '1985', KY,
       [('Optima Mid', 'Kyosho', '1988', ''), ('Turbo Optima Mid', 'Kyosho', '1989', '')]),
     X('Tamiya Wild One', 'Tube-frame dune buggy on the Fast Attack Vehicle chassis.', 'Tamiya', '1985', 'https://technicopedia.com/RC/Wild%20One/index.html',
       [('58050', 'Tamiya', '1985', 'original'), ('58525 Wild One Off-Roader', 'Tamiya', '2012', 're-release with stronger axles')]),
     X('Tamiya Lunch Box', '1/12 wheelie van on monster-truck wheels, on what became the CW-01 chassis.', 'Tamiya', '1987', 'https://www.tamiyaclub.com/car.asp?cid=1827',
       [('Lunch Box Red Edition (47402)', 'Tamiya', '2019', 'CW-01, 540 motor')]),
     X('Kyosho Inferno', '1:8 nitro competition buggy, IFMAR 1:8 IC off-road world champion.', 'Kyosho', '', KY, [('IFMAR win', 'Kyosho', '1992', '')]),
     X('Kyosho Mini-Z', '1:28 scale small electric racers.', 'Kyosho', '', KY),
     X('Traxxas Maxx', 'Large monster trucks, nitro then electric.', 'Traxxas', '1999', TX, [('T-Maxx', 'Traxxas', '1999', 'first full-sized monster truck'), ('X-Maxx', 'Traxxas', '2015', 'larger electric truck')]),
     X('Traxxas Slash', 'Short-course truck in 2WD and 4WD.', 'Traxxas', '', TX),
     X('Traxxas TRX-4', 'Scale trail truck and crawler.', 'Traxxas', '', TX, [('TRX-4M', 'Traxxas', '', 'small-scale version (old data)')]),
     X('Axial AX10 and SCX10 crawlers', 'Purpose-built rock crawlers; the SCX10 set the scale-crawler pattern.', 'Axial', '2007', 'https://www.axialadventure.com/axi-blog-flashback-ax10.html',
       [('AX10 Scorpion', 'Axial', '2007', 'first purpose-built crawler'), ('SCX10', 'Axial', '', 'followed the AX10')])],
  m=[['Axial AX24', 'Axial'], ['BlackZon Slyder', 'BlackZon']])
sl = K('Slot-car racing set', 'A toy car racing set with grooved track and hand controllers.', 'https://uk.scalextric.com/products/scalextric-1980s-grand-prix-race-set-c1432m',
  a='slot cars · Scalextric', t=['1:32', '1:24', '1:43', 'HO (about 1:64)', 'Analogue', 'Digital (lane-changing)', 'Slot car (single)', 'Track and borders', 'Hand controller'],
  x=[X('Scalextric', 'British 1:32 slot-car system, the name many use for the hobby.', 'Scalextric', '1957', SX,
       [('First sets', 'Scalextric', '1956', 'made in Havant; shown at Harrogate January 1957'), ('Classic plastic track (Mk 2)', 'Scalextric', '1962', ''), ('Super 124', 'Scalextric', '1968–1970', '1:24'),
        ('Micro Scalextric', 'Scalextric', '1994', '1:64'), ('Sport track', 'Scalextric', '2001', ''), ('Scalextric Digital', 'Scalextric', '2004', ''), ('Start', 'Scalextric', '2010', '')], dt='scale · analogue or digital · licence'),
     X('Aurora Thunderjet 500', 'HO "pancake" motor slot car, probably the best-selling slot car ever.', 'Aurora', '1963', PC),
     X('Aurora AFX', 'Faster HO chassis line that succeeded the Thunderjet.', 'Aurora', '1971', AU,
       [('A/FX chassis', 'Aurora', '1971', ''), ('Magna-Traction', 'Aurora', '1974', 'exposed magnets for downforce'), ('G-Plus', 'Aurora', '1976', 'in-line motor')]),
     X('Carrera', 'German slot-car system with 1:24, 1:32 and 1:43 lines and Digital 132.', 'Carrera', 'early 1960s', CA,
       [('Servo', 'Carrera', '1970', 'lane changes by guard rails'), ('Carrera Exclusiv', 'Carrera', '1999', '1:24'), ('Carrera Go!!!', 'Carrera', '2001', 'entry level'), ('Evolution / Digital 132', 'Carrera', '', 'up to six cars overtake')]),
     X('Ninco', 'Spanish 1:32 slot cars and track, with a digital system for up to eight cars.', 'Ninco', '1993', NI)],
  m=[['Scalextric 1980s Grand Prix Race Set', 'Scalextric']],
  r=[['Scalextric Hot Laps Sets', 'Scalextric'], ['Micro Scalextric', 'Scalextric'], ['My First Scalextric', 'Scalextric'], ['Scalextric Pro Sets', 'Scalextric'], ['Scalextric Retro Sets', 'Scalextric'], ['Scalextric Standard Race Sets', 'Scalextric']])
m4 = K('Mini 4WD', 'A 1:32 snap-together battery car with four-wheel drive, raced on walled U-section tracks.', M4, a='Mini Yonku · mini 4WD racer',
  t=['Kit', 'Chassis', 'Upgrade parts (motors, gears, rollers)', 'Track'],
  x=[X('Tamiya Mini 4WD', 'Tamiya\'s original 1:32 four-wheel-drive mini car kits.', 'Tamiya', '1982', M4,
       [('Ford Ranger 4x4', 'Tamiya', '1982', 'early model')], dt='chassis · motor · body'),
     X('Racer Mini 4WD', 'Racing-bodied Mini 4WD series.', 'Tamiya', '1986', TC, [('Hotshot Jr.', 'Tamiya', '1986', 'first of the series')])])
KN = 'knowledge'
brands = [
 B('Tamiya', 'Japan', '1946', 'Premium', 'kits, RC cars', 'Shizuoka maker of plastic kits, RC cars and Mini 4WD.', TC, sig=['Tamiya Grasshopper', 'Tamiya Hornet', 'Tamiya Wild One', 'Tamiya Lunch Box', 'Tamiya Mini 4WD']),
 B('Kyosho', 'Japan', '1963', 'Premium', 'RC buggies, Mini-Z', 'Tokyo maker of RC cars, aircraft and boats.', KY, sig=['Kyosho Optima', 'Kyosho Inferno', 'Kyosho Mini-Z']),
 B('Traxxas', 'United States', '1986', 'Mainstream', 'RTR monster trucks', 'McKinney, Texas maker of ready-to-run electric and nitro RC.', TX, sig=['Traxxas Maxx', 'Traxxas Slash', 'Traxxas TRX-4']),
 B('Team Associated', 'United States', '1964', 'Specialist', 'racing buggies', 'Associated Electrics, Californian RC racing maker; owned by Thunder Tiger since 2005.', AE, sig=['Team Associated RC10']),
 B('Axial', 'United States', '', 'Mainstream', 'rock crawlers', 'RC brand known for scale rock crawlers.', 'https://www.axialadventure.com/axi-blog-flashback-ax10.html', sig=['Axial AX10 and SCX10 crawlers']),
 B('Scalextric', 'United Kingdom', '1957', 'Mainstream', '1:32 slot cars', 'British slot-car brand founded by Fred Francis; owned by Hornby from 1968, sold to Purbeck Capital Partners in 2026.', SX, sig=['Scalextric'], rel=['Hornby']),
 B('Carrera', 'Germany', '', 'Mainstream', 'slot cars', 'Fürth-born slot-car brand, owned by the Stadlbauer Group since 1999.', CA, sig=['Carrera']),
 B('Aurora', 'United States', '', 'Heritage manufactory', 'HO slot cars', 'Aurora Plastics, maker of Thunderjet and AFX HO slot cars until 1983.', AU, sig=['Aurora Thunderjet 500', 'Aurora AFX']),
 B('Ninco', 'Spain', '1993', 'Specialist', '1:32 slot cars', 'Spanish maker of 1:32 slot cars and track.', NI, sig=['Ninco']),
]
notes = ("RC: archetypes ordered by significance (Porsche 934 first, then 1980s buggy icons, Traxxas and Axial); nitro/electric, toy/hobby, boats, aircraft and drones as types. Old TRX-4M became a TRX-4 version; Axial AX24 and BlackZon Slyder kept in m. "
 "Not added: Arrma, SCX (Spanish) and Tyco slot cars (no page retrieved naming them); Grasshopper/Hornet first-release item numbers not found. Mini 4WD added as a new kind (Wikipedia). No traditions.")
write('03_02', [rc, sl, m4], brands, [], notes)
