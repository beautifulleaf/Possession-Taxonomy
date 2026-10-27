import sys; sys.path.insert(0, 'work/E1/agent')
from lib import *
MK = WP + 'M%C3%A4rklin'; HR = WP + 'Hornby_Railways'; SC = WP + 'Rail_transport_modelling_scales'; DCC = WP + 'Digital_Command_Control'
DMS = WP + 'Digital_model_railway_control_systems'; KA = WP + 'Kato_Precision_Railroad_Models'; LI = WP + 'Lionel_Corporation'; LG = WP + 'LGB_(trains)'
PE = WP + 'Peco'; BB = WP + 'Bachmann_Branchline'; FL = WP + 'Fleischmann_(model_railroads)'; RO = WP + 'Roco_(model_railroads)'; PI = WP + 'Piko_(model_trains)'
GF = WP + 'Graham_Farish'; FA = WP + 'Faller'; WS = WP + 'Woodland_Scenics'; PM = 'https://www.keymodelworld.com/article/point-motors-solenoid-and-stall-motor'
GAUGES = ['Z (1:220, 6.5 mm)', 'N (1:160; British N 1:148, 9 mm)', 'TT / TT:120 (1:120, 12 mm)', 'HO / H0 (1:87, 16.5 mm)', 'OO (1:76.2, 16.5 mm)', 'EM and P4 finescale (4 mm scale)', 'S (1:64)', 'O (1:43.5–1:48, 32 mm)', 'Gauge 1 (1:32, 45 mm)', 'G / garden (about 1:22.5, 45 mm)']
OLDR = [['Hornby RailRoad', 'Hornby'], ['Hornby TT:120', 'Hornby']]
ts = K('Model railway train set', 'A starter set of locomotive, rolling stock, track and controller sold together.', 'https://uk.hornby.com/catalogue/train-sets-rolling-stock',
  a='starter set · train set', t=GAUGES + ['Analogue DC', 'Digital (DCC, mfx)', 'Three-rail AC', 'Clockwork or live steam'],
  x=[X('Märklin H0 three-rail AC system', 'H0 trains running on alternating current with a stud contact rail hidden between the running rails.', 'Märklin', '1935', MK,
       [('Märklin gauges 1–5', 'Märklin', '1891', 'toy-train gauge standards shown at Leipzig'), ('Märklin Digital', 'Märklin', '1984', 'digital control on Motorola chips'), ('Mini-Club Z', 'Märklin', '1972', '1:220 range'), ('Trix', 'Märklin', '1997', 'acquired; two-rail DC H0 and N')], dt='gauge · analogue or digital · era'),
     X('Hornby Dublo and Hornby OO', 'British-outline OO trains, the main UK ready-to-run system.', 'Hornby', '1938', HR,
       [('Hornby O gauge clockwork', 'Hornby', '1920', 'first Hornby train'), ('Hornby Dublo three-rail', 'Hornby', '1938', 'first OO trains'), ('Two-rail track and Super Detail stock', 'Hornby', '1959', ''),
        ('Tri-ang Hornby', 'Hornby', '1964', 'after Lines Bros bought Meccano'), ('Hornby Railways', 'Hornby', '1972', 'renamed'), ('Hornby RailRoad', 'Hornby', '', 'entry range (old data)'), ('Hornby TT:120', 'Hornby', '2022', 'launched October 2022')]),
     X('Lionel three-rail O', 'American toy trains on three-rail track, the postwar Christmas-tree train.', 'Lionel', '1906', LI,
       [('Standard Gauge "Standard of the World"', 'Lionel', '1906', 'three-rail track'), ('Lionel O gauge', 'Lionel', '', 'smaller budget line'), ('Postwar era', 'Lionel', '1946–1956', 'outsold American Flyer')]),
     X('LGB garden railway', 'Large 45 mm gauge trains built to run outdoors in all weather.', 'LGB', '1968', LG, [('Stainz 0-4-0', 'LGB', '1968', 'first model, still made in 2021')]),
     X('Kato Unitrack starter set', 'N or HO train with track that has roadbed moulded in, snapped together on any floor.', 'Kato', '', KA),
     X('Bachmann Branchline', 'British-outline OO ready-to-run range from Bachmann Europe.', 'Bachmann', '1990', BB, [('Graham Farish N', 'Graham Farish', '2000', 'N gauge sister range')])],
  m=[["Valley Drifter 'Crimson King' Train Set", 'Hornby']], r=OLDR)
loco = K('Model locomotive', 'A powered model railway engine or multiple unit.', 'https://uk.hornby.com/catalogue/train-sets-rolling-stock',
  a='model engine · model loco', t=GAUGES + ['Steam outline', 'Diesel outline', 'Electric outline', 'Multiple unit', 'DCC ready', 'DCC fitted', 'DCC sound', 'Live steam'],
  x=[X('Märklin Crocodile', 'Articulated Swiss electric locomotive model, a Märklin O gauge classic.', 'Märklin', '1920s–1930s', MK),
     X('Märklin Schienenzeppelin', 'O gauge model of the propeller-driven rail car.', 'Märklin', '1932', MK),
     X('Lionel Santa Fe F3', 'Red-and-silver warbonnet diesel that became the icon of the postwar Lionel era.', 'Lionel', '1946–1956', LI),
     X('LGB Stainz', 'Small Austrian 0-4-0 tank engine, the first LGB model.', 'LGB', '1968', LG, [('Stainz with sound', 'LGB', '2021', 'still in production')]),
     X('Hornby live steam', 'Real steam-powered OO and gauge models from Hornby.', 'Hornby', '1980', HR, [('Stephenson\'s Rocket', 'Hornby', '1980', 'Rocket 150'), ('Mallard', 'Hornby', '2003', 'first steam-powered 00 locomotive')]),
     X('Kato C62', 'N scale JNR 4-6-4 steam locomotive.', 'Kato', '', KA),
     X('Kato EMD E5A "Silver Speed"', 'N scale American streamlined diesel.', 'Kato', '', KA),
     X('Bachmann Peppercorn A1 Tornado', 'OO model of LNER Peppercorn A1 60163 Tornado.', 'Bachmann', '', BB, [('Class 66', 'Bachmann', '', 'diesel'), ('Class 47', 'Bachmann', '', 'diesel'), ('Blue Pullman', 'Bachmann', '', 'Classes 251/261')]),
     X('Graham Farish N', 'British-outline N gauge locomotives, first sold under the Grafar label.', 'Graham Farish', '1970', GF),
     X('Fleischmann piccolo', 'Fleischmann\'s N scale range.', 'Fleischmann', '1969', FL)],
  r=OLDR)
rs = K('Model rolling stock', 'An unpowered model railway wagon, coach or carriage.', 'https://www.hearnshobbies.com/collections/rolling-stock', a='wagon · coach · carriage',
  t=GAUGES + ['Coach or carriage', 'Goods wagon', 'Van', 'Brake van or caboose', 'Tank wagon', 'Dummy multiple-unit car'], r=OLDR)
tr = K('Model railway track', 'Rails, points and crossings for a model railway, as sectional or flexible track.', 'https://uk.hornby.com/catalogue/train-sets-rolling-stock',
  t=['Sectional (set) track', 'Flexible track', 'Track with moulded roadbed', 'Point or turnout', 'Crossing', 'Buffer stop', 'Code 100', 'Code 83', 'Code 75', 'Code 55', 'Bullhead rail', 'Three-rail stud contact'],
  x=[X('Peco Streamline', 'Flexible track and points at many radii for experienced modellers, from Z to G.', 'Peco', '', PE,
       [('Code 100', 'Peco', '', '00/H0'), ('Code 75', 'Peco', '', '00/H0'), ('Code 55', 'Peco', '', 'N and TT:120'), ('Bullhead 00', 'Peco', '2019', ''), ('Unifrog points', 'Peco', '', 'replacing Electrofrog and Insulfrog')]),
     X('Peco Setrack', 'Rigid sectional track pieces for less experienced modellers.', 'Peco', '', PE),
     X('Kato Unitrack', 'Track with integrated roadbed in N and HO.', 'Kato', '', KA),
     X('Märklin three-rail track', 'Track with a centre row of studs for AC current pick-up.', 'Märklin', '', MK, [('M-track', 'Märklin', '', '')]),
     X('Hornby two-rail track', 'Two-rail OO track that replaced Hornby Dublo\'s tinplate three-rail.', 'Hornby', '1959', HR)],
  r=[['Hornby TT:120', 'Hornby']])
sc = K('Model railway scenery & buildings', 'Buildings, scenery or lineside accessories sold for a model railway, with the gauge or railway scale stated.', 'https://www.scalemodelscenery.co.uk/collections/oo-scale-9',
  a='model railway scenery', t=['Building kit', 'Ready-built building', 'Bridge or tunnel', 'Trees and foliage', 'Grass and static grass', 'Ballast', 'Figures', 'Road vehicles', 'Signals', 'Backscene'],
  x=[X('Faller building kits', 'Polystyrene kits of stations, houses, bridges and fairground rides in H0, N, TT and Z.', 'Faller', '1946', FA,
       [('Pola', 'Faller', '1997', 'G scale structures'), ('Faller Car System', 'Faller', '', 'self-steering road vehicles'), ('Digital Car System', 'Faller', '2013', 'computer control')]),
     X('Woodland Scenics scenery', 'Turf, foliage and tree kits for realistic landscape.', 'Woodland Scenics', '1975', WS, [('First catalogue', 'Woodland Scenics', '1975', '28 products')]),
     X('Ratio and Wills kits', 'British plastic lineside and building kits now owned by Peco.', 'Peco', '', PE)],
  r=[['Hornby TT:120', 'Hornby']])
ct = K('Model railway controller', 'A hand or digital controller for a model railway.', 'https://uk.hornby.com/products/elite-digital-controller-r8214',
  a='throttle · command station · power controller', t=['Analogue DC controller', 'AC transformer', 'DCC command station', 'Handheld throttle', 'Wireless or app control', 'Booster'],
  x=[X('Analogue DC controller', 'Variable-voltage controller that runs one train per electrical section.', '', '', 'https://www.hampshiremodels.co.uk/products/gaugemaster-combi-single-track-controller-with-plug-in-transformer-analog',
       [('Gaugemaster COMBI', 'Gaugemaster', '', '12 V DC and 16 V AC outputs')]),
     X('DCC command station', 'NMRA-standard digital system that addresses each locomotive by decoder.', '', '1993', DCC,
       [('Hornby Elite', 'Hornby', '', 'with RailMaster software from 2010'), ('Roco Z21', 'Roco', '', 'phone and tablet control')]),
     X('Märklin Central Station', 'Märklin multi-protocol digital centre for Motorola, mfx and DCC.', 'Märklin', '', 'https://www.marklin.com/products/details/article/60657',
       [('Central Station 3 (60226)', 'Märklin', '', ''), ('Central Station 3 plus (60216)', 'Märklin', '', ''), ('Mobile Station (60657)', 'Märklin', '', 'handheld')]),
     X('Hornby Zero 1', 'Early digital system for up to 16 locomotives and 99 accessories.', 'Hornby', '1979', HR),
     X('Lionel TMCC and Legacy', 'Lionel command control for three-rail O.', 'Lionel', '1995', DMS, [('TMCC', 'Lionel', '1995', ''), ('Legacy', 'Lionel', '2007', 'successor')]),
     X('Selectrix', 'Digital system from Döhler & Haas for Trix, later open and standardised by MOROP.', '', 'early 1980s', DMS)],
  m=[['Hornby Elite DCC Controller', 'Hornby']])
dc = K('Model railway decoder', 'A digital decoder chip fitted in a model locomotive or accessory to receive DCC commands.', 'https://www.hattons.co.uk/stocklist/1000389/0/hornby/mfrnest',
  a='DCC decoder · chip', t=['Locomotive (mobile) decoder', 'Sound decoder', 'Function decoder', 'Accessory decoder', '21-pin', 'Hardwired'],
  x=[X('DCC locomotive decoder', 'Decoder set by configuration variables (CVs), giving each engine its own address.', '', '1993', DCC,
       [('ESU LokSound 5 (58429)', 'ESU', '', 'HO 21-pin DCC sound decoder with RailComPlus')]),
     X('DCC accessory decoder', 'Stationary decoder that switches points, signals and lights.', '', '', DCC)])
pt = K('Point motor', 'A motor or solenoid that throws a model railway point by switch or digital command.', 'https://www.hattons.co.uk/stocklist/1000389/0/hornby/mfrnest',
  a='turnout motor · switch machine', t=['Below-baseboard', 'Surface-mounted', 'DCC-fitted', 'Servo'],
  x=[X('Solenoid point motor', 'Two coils fire a pin across with a pulse, usually with a capacitor discharge unit.', '', '', PM,
       [('Peco PL-10', 'Peco', '', 'long-running below-baseboard solenoid'), ('Peco PL-11', 'Peco', '', 'side-mounted'), ('Hornby R8014', 'Hornby', '', ''), ('Hornby R8243', 'Hornby', '', 'surface-mounted'),
        ('Gaugemaster SEEP PM10', 'Gaugemaster', '2015', ''), ("Hattons HAT-PM-01", "Hattons", '', 'best solenoid in Hornby Magazine test')]),
     X('Slow-action stall motor', 'A geared motor eases the blades across and holds them, with switches for frog polarity.', '', '', PM,
       [('Circuitron Tortoise 800-6000', 'Circuitron', 'mid-1980s', ''), ('DCC Concepts Cobalt', 'DCC Concepts', '2010', 'Cobalt iP 2014; Hornby Magazine choice'), ('Traintronics TT300', 'Traintronics', '', 'DCC fitted')])])
KN = 'knowledge'
brands = [
 B('Märklin', 'Germany', '1859', 'Heritage manufactory', 'H0 three-rail, Z', 'Göppingen maker that set early toy-train gauges and makes three-rail AC H0, Z Mini-Club and LGB.', MK,
   lines=['H0', 'Mini-Club (Z)', 'Trix', 'LGB'], sig=['Märklin H0 three-rail AC system', 'Märklin Crocodile', 'Märklin Central Station'], rel=['LGB']),
 B('Hornby', 'United Kingdom', '1901', 'Mainstream', 'OO trains', 'British model railway firm, from Hornby Dublo to today\'s OO and TT:120 ranges.', HR,
   lines=['Hornby Dublo', 'Hornby RailRoad', 'Hornby TT:120'], sig=['Hornby Dublo and Hornby OO', 'Hornby live steam', 'Hornby Zero 1'], rel=['Airfix', 'Corgi']),
 B('Bachmann', 'United States', '1835', 'Mainstream', 'OO and HO trains', 'Kader-owned model railway maker; Bachmann Europe makes Branchline OO.', BB, lines=['Branchline', 'Graham Farish'], sig=['Bachmann Branchline'], rel=['Graham Farish']),
 B('Graham Farish', 'United Kingdom', '1928', 'Mainstream', 'British N gauge', 'Poole firm that became the main British N gauge maker; owned by Bachmann since 2000.', GF, sig=['Graham Farish N'], rel=['Bachmann']),
 B('Kato', 'Japan', '1957', 'Premium', 'N scale, Unitrack', 'Tokyo maker of N and HO models and Unitrack.', KA, sig=['Kato Unitrack', 'Kato C62']),
 B('Lionel', 'United States', '1900', 'Heritage manufactory', 'three-rail O', 'New York toy-train maker, now Lionel, LLC.', LI, sig=['Lionel three-rail O', 'Lionel Santa Fe F3']),
 B('LGB', 'Germany', '1968', 'Specialist', 'garden railways', 'Lehmann Gross Bahn, 45 mm garden trains; owned by Märklin since 2007.', LG, sig=['LGB Stainz'], rel=['Märklin']),
 B('Fleischmann', 'Germany', '1887', 'Mainstream', 'N scale', 'Nuremberg maker, N-only since 2019 under the Roco parent.', FL, lines=['piccolo'], rel=['Roco']),
 B('Roco', 'Austria', '1960', 'Mainstream', 'H0 trains', 'Salzburg maker of H0 trains and the Z21 digital system.', RO, rel=['Fleischmann']),
 B('Piko', 'Germany', '1949', 'Value', 'H0, G trains', 'Sonneberg maker of G, H0, TT and N trains.', PI, lines=['Expert', 'Hobby', 'SmartControl']),
 B('Peco', 'United Kingdom', '1946', 'Specialist', 'track', 'Beer, Devon maker of Streamline and Setrack track, point motors and kits.', PE, lines=['Streamline', 'Setrack', 'PECOlectrics', 'Ratio', 'Wills'], sig=['Peco Streamline']),
 B('Tomix', 'Japan', '', 'Mainstream', 'N scale, Fine Track', 'Japanese N gauge train and track brand of the Takara Tomy group.', KN),
 B('Faller', 'Germany', '1946', 'Specialist', 'building kits', 'Black Forest maker of model railway buildings and scenery.', FA, lines=['Pola', 'Faller Car System'], sig=['Faller building kits']),
 B('Woodland Scenics', 'United States', '1975', 'Specialist', 'scenery', 'US maker of model railway scenery materials.', WS, sig=['Woodland Scenics scenery']),
 B('Gaugemaster', 'United Kingdom', '', 'Specialist', 'controllers', 'British maker of model railway controllers and point motors.', PM),
 B('Circuitron', 'United States', '', 'Specialist', 'Tortoise point motor', 'US maker of the Tortoise slow-action point motor.', PM),
 B('DCC Concepts', '', '', 'Specialist', 'Cobalt point motors', 'Maker of Cobalt slow-action point motors and DCC accessories.', PM),
 B('ESU', 'Germany', '', 'Specialist', 'LokSound decoders', 'Maker of LokSound DCC sound decoders.', 'https://trainsupply.com/products/esu58429'),
]
notes = ("Gauge register (Z, N, TT/TT:120, HO, OO, EM/P4, S, O, Gauge 1, G) as types on set, locomotive and rolling stock (ratios from the scales article). Train-set archetypes are the maker systems (Märklin H0 AC, Hornby, Lionel, LGB, Kato, Bachmann); locomotive archetypes are sourced icons. "
 "Rolling stock left without archetypes (no sourced icons). Not added: Tomix Fine Track, Bachmann E-Z Track, Märklin C-track/K-track and mfx decoders (no fetched page naming them); Tomix brand from knowledge. Circuitron country from the point-motor test (US); Gaugemaster (UK) and ESU (Germany) countries from knowledge; DCC Concepts country and founding years of these four left blank. No traditions (industrial products). All 8 planned kinds kept.")
write('03_01', [ts, loco, rs, tr, sc, ct, dc, pt], brands, [], notes)
