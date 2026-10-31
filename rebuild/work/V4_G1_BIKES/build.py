import json, copy, os
ROOT = '/home/user/Possession-Taxonomy/rebuild/'
src = json.load(open(ROOT + 'out/G1.json'))
W = 'https://en.wikipedia.org/wiki/'
S = dict(
    trek=W + 'Trek_Bicycle_Corporation', spec=W + 'Specialized_Bicycle_Components', giant=W + 'Giant_Manufacturing',
    merida=W + 'Merida_Bikes', cann=W + 'Cannondale_Bicycle_Corporation', ral=W + 'Raleigh_Bicycle_Company',
    brom=W + 'Brompton_Bicycle', pin=W + 'Pinarello', cerv=W + 'Cerv%C3%A9lo', shim=W + 'Shimano', sram=W + 'SRAM_Corporation',
    camp=W + 'Campagnolo', shl=W + 'List_of_Shimano_groupsets', xt=W + 'Shimano_Deore_XT', acc=W + 'Accell_Group',
    pon=W + 'Pon_Holdings', sc=W + 'Santa_Cruz_Bicycles', can=W + 'Canyon_Bicycles', moul=W + 'Moulton_bicycle',
    str=W + 'Strida', dah=W + 'Dahon', tern=W + 'Tern_(company)', schw=W + 'Schwinn_Bicycle_Company', bia=W + 'Bianchi_(company)',
    col=W + 'Colnago', pash=W + 'Pashley_Cycles', surly=W + 'Surly_Bikes', gaz=W + 'Gazelle_(bicycle_company)',
    bt=W + 'Baby_transport', mac=W + 'Owen_Finlay_Maclaren', bug=W + 'Bugaboo_International', upp=W + 'UPPAbaby',
    sx=W + 'Silver_Cross_(company)', stk=W + 'Stokke_AS', ebike=W + 'Electric_bicycle',
    bal='https://strollberry.com/strollers/silver-cross-balmoral', stks='https://strollberry.com/strollers/brand/stokke')

# maker -> (country)
CTY = {}
def c(country, *makers):
    for m in makers: CTY[m] = country
c('Italy', 'Bianchi', 'Colnago', 'Cinelli', 'Pinarello', 'Campagnolo', 'Selle Italia')
c('United States', 'Specialized', 'Trek', 'Surly', 'Rivendell Bicycle Works', 'Breezer', 'Santa Cruz', 'Yeti', 'Wildfire Designs', 'Fatback', 'Haro', 'GT', 'Cruzbike', 'Catrike', 'da Vinci Designs', 'Bilenky Cycle Works', 'Pope Manufacturing Company', 'Huffy', 'Schwinn', 'Adams', 'Burley', 'Weehoo', 'Chris King', 'Cane Creek', 'RockShox', 'Fox Factory', 'Cannondale', 'SRAM', 'Zipp', 'Speedplay', 'Crankbrothers', 'UPPAbaby', 'Baby Jogger', 'BOB Gear', 'WonderFold', 'Dahon')
c('United Kingdom', 'Pashley', 'Brompton', 'Moulton', 'Raleigh', 'Islabikes', 'Reynolds', 'Brooks England', 'Mike Burrows', 'Inspired Cycle Engineering', 'James Starley', 'Leicester Safety Tricycle Company', 'Denis Johnson', 'Singer & Co.', 'Ellis & Co.', 'Hillman, Herbert & Cooper', 'Silver Cross', 'Maclaren', 'Strida', 'Bickerton')
c('Netherlands', 'Gazelle', 'Urban Arrow', 'VanMoof', 'Koga', 'Bugaboo', 'Velomobiel.nl')
c('Germany', 'Canyon', 'Riese & Müller', 'HP Velotechnik', 'Hase Spezialräder', 'Hase', 'Velotaxi GmbH', 'Karl Drais', 'Continental', 'Schwalbe')
c('Canada', 'Cervélo'); c('Japan', 'Shimano'); c('France', 'Look', 'Mavic', 'Babyzen', 'Charles Mochet')
c('Denmark', 'Christiania Bikes', 'Larry vs Harry', 'Leitra'); c('Belgium', 'Cowboy'); c('Czech Republic', 'AZUB')
c('Austria', 'woom'); c('Sweden', 'Thule'); c('Norway', 'Hamax', 'Stokke'); c('Taiwan', 'Giant', 'Merida')
NS = 'Country not stated'
# owner facts: maker -> (own, tier, cty, own_y)
OWN = {
    'Trek': ('Trek Bicycle Corporation', 'Independent', 'United States', ''),
    'Specialized': ('Specialized Bicycle Components', 'Independent', 'United States', ''),
    'Cannondale': ('Pon Holdings', 'Global group', 'United States', '2022'),
    'Cervélo': ('Pon Holdings', 'Global group', 'Canada', ''),
    'Santa Cruz': ('Pon Holdings', 'Global group', 'United States', '2015'),
    'Gazelle': ('Pon Holdings', 'Global group', 'Netherlands', '2011'),
    'Urban Arrow': ('Pon Holdings', 'Global group', 'Netherlands', '2019'),
    'Schwinn': ('Pon Holdings', 'Global group', 'United States', '2021'),
    'Raleigh': ('Accell Group', 'Global group', 'United Kingdom', '2012'),
    'Koga': ('Accell Group', 'Global group', 'Netherlands', ''),
    'Giant': ('Giant Manufacturing', 'Global group', 'Taiwan', ''),
    'Pinarello': ('Ivan Glasenberg', 'Independent', 'Italy', '2023'),
    'Colnago': ('Chimera Investments LLC', 'Independent', 'Italy', '2020'),
    'Bianchi': ('Cycleurope', 'Independent', 'Italy', '1997'),
    'Canyon': ('Canyon Bicycles GmbH', 'Independent', 'Germany', ''),
    'Brompton': ('Brompton Bicycle', 'Independent', 'United Kingdom', ''),
    'Pashley': ('Pashley Cycles', 'Independent', 'United Kingdom', ''),
    'Surly': ('Quality Bicycle Products', 'Independent', 'United States', ''),
    'Dahon': ('DAHON Tech', 'Independent', 'United States', ''),
    'Shimano': ('Shimano Inc.', 'Global group', 'Japan', ''),
    'SRAM': ('SRAM Corporation', 'Global group', 'United States', ''),
    'Campagnolo': ('Campagnolo S.r.l.', 'Independent', 'Italy', ''),
    'Silver Cross': ('Fosun International', 'Independent', 'United Kingdom', '2015'),
    'Bugaboo': ('Bain Capital', 'Independent', 'Netherlands', '2018'),
    'UPPAbaby': ('UPPAbaby', 'Independent', 'United States', ''),
    'Stokke': ('NXMH', 'Independent', 'Norway', ''),
    'Babyzen': ('Stokke AS', 'Independent', 'France', '2021'),
}

def V(n, y='', d='', mk=None):
    o = {'n': n, 'y': y, 'd': d}
    if mk: o['mk'] = mk
    return o
def E(n, mk, y, d, s, v=None, a='', dt='', role=None):
    o = {'n': n, 'a': a, 'd': d, 'mk': mk, 'y': y, 's': s, 'v': v or [], 'dt': dt}
    if role: o['role'] = role
    return o

# ---------------- additions by kind (new entries from fetched pages) ----------------
ADD = {}
ADD['Road bike'] = [
    E('Cannondale CAAD', 'Cannondale', '1996', "Cannondale's aluminium road line; CAAD9 (2007) became a standalone model and CAAD14 (2026) returned to round tubes.", S['cann'],
      [V('2.8 series', '1992', 'lightweight road frame, later renamed CAAD 3'), V('CAAD9', '2007', 'became a standalone model'), V('CAAD13', '2020', 'adopted SuperSix-like shaping'), V('CAAD14', '2026', 'returned to round tubes')], dt='generation · groupset · rim or disc'),
    E('Cannondale SuperSix EVO', 'Cannondale', '2008', "Cannondale's race road bike; the fifth generation arrived in early 2026.", S['cann'], [V('SuperSix (original)', '', 'round-tube carbon frame, ancestor of the EVO'), V('SuperSix EVO', '2008', ''), V('Fifth generation', '2026', 'early 2026; made the SystemSix aero bike redundant')], dt='generation · groupset'),
    E('Cannondale Synapse', 'Cannondale', '2006', "Cannondale's endurance road bike, described as its first full-carbon road bike.", S['cann'], [V('Road Warrior', '2002', 'relaxed predecessor'), V('Synapse', '2006', ''), V('Second generation', '2014', ''), V('Redesign', '2018', ''), V('Sixth generation', '2025', '')], dt='generation · groupset'),
    E('Cervélo Soloist', 'Cervélo', '', "Cervélo's all-round road bike, now no longer made.", S['cerv'], [V('Soloist', '', ''), V('Soloist Carbon', '', ''), V('Soloist Team', '', '')]),
    E('Trek 5500 and 5200', 'Trek', '1992', "Trek's OCLV carbon road frames; the 5500 was described as the world's lightest production road frame.", S['trek']),
    E('Pinarello Paris', 'Pinarello', '', "Aluminium frame on which Ullrich and Riis won the Tour; a carbon FP version followed.", S['pin']),
    E('Pinarello Montello SLX', 'Pinarello', '', "Steel frame of the mid-1980s that brought Pinarello its first major professional wins.", S['pin'], [V('Treviso', '', 'second-tier steel model below the Montello'), V('Gavia', '', 'steel frame with more saddle setback')]),
    E('Pinarello Gan', 'Pinarello', '2016', "Mid-tier Pinarello road series styled after the F8.", S['pin'], [V('Gan', '2016', ''), V('Gan Disk', '2016', ''), V('Gan S', '2016', ''), V('Gan RS', '2016', '')]),
    E('Colnago Super', 'Colnago', '1968', "Colnago's Columbus SL steel racing frame, made in two versions to the late 1980s.", S['col'], [V('Super Version 1', '1968–1978', 'Columbus SL tubing, circular tubing'), V('Super Version 2', '1978', 'to the late 1980s')]),
    E('Colnago Mexico', 'Colnago', '1975–1977', "Columbus Record tubing frame with no crimping on the chainstays; named for the Mexico hour record.", S['col']),
    E('Colnago Tecnos', 'Colnago', '1995–2000', "Colnago's lightest production steel racing frame, made with a custom Tecnos tubeset.", S['col']),
    E('Colnago Extreme Power', 'Colnago', '2007', "Colnago carbon frame built like the C40 and C50 but stiffer, with round carbon tubes.", S['col']),
    E('Bianchi Specialissima', 'Bianchi', '', "Bianchi's racing flagship in the 2017 range.", S['bia']),
    E('Bianchi Oltre', 'Bianchi', '', "Bianchi's aero racing line, shown as XR1 to XR4 in the 2017 range.", S['bia'], [V('Oltre XR1', '', ''), V('Oltre XR2', '', ''), V('Oltre XR3', '', ''), V('Oltre XR4', '', '')]),
    E('Bianchi Infinito', 'Bianchi', '', "Bianchi's endurance racing line in the 2017 range.", S['bia'], [V('Infinito', '', ''), V('Intenso', '', 'endurance range, 2017'), V('Impulso', '', 'endurance range, 2017')]),
    E('Bianchi Aria', 'Bianchi', '', "Bianchi's aero road bike, also listed for time trials, in the 2017 range.", S['bia']),
    E('Canyon Ultimate', 'Canyon', '', "Canyon's lightweight road bike; an Ultimate CF SLX carried Nairo Quintana through the road stages of the 2014 Giro d'Italia.", S['can']),
    E('Canyon Aeroad', 'Canyon', '', "Canyon's aero road bike; Mathieu van der Poel won the 2020 Tour of Flanders on one.", S['can']),
    E('Canyon Endurace', 'Canyon', '', "Canyon's endurance road bike, part of its CFR range.", S['can']),
    E('Specialized Roubaix', 'Specialized', '2003', "Specialized's endurance road bike; Fuji licensed the name to Specialized in 2003.", S['spec']),
    E('Schwinn Varsity', 'Schwinn', '1960', "Schwinn's ten-speed road bike, sold to the early 1970s and still produced into the 1980s.", S['schw'], [V('Varsity', '1960', '8-speed, ten speeds from mid-1961'), V('Continental', '1960', 'differed mainly by its tubular front fork'), V('LeTour', '1973', 'Japanese-made by 1973')]),
    E('Schwinn Paramount', 'Schwinn', '1938', "Schwinn's high-grade racing line, built in Waterford, Wisconsin from 1980.", S['schw'], [V('Paramount tandem', '1969', '')]),
    E('Gazelle Champion Mondial', 'Gazelle', 'c. 1980–1985', "Steel-framed racing bicycle made by Gazelle.", S['gaz']),
]
ADD['Time-trial bike'] = [
    E('Trek TTX', 'Trek', '2005', "Trek's time-trial bike, used by Lance Armstrong.", S['trek']),
    E('Pinarello Sibilo', 'Pinarello', '2013', "Pinarello's second in-house time-trial frame, released in June 2013.", S['pin']),
    E('Canyon Speedmax', 'Canyon', '', "Canyon's time-trial bike; a Speedmax CF was used for the time trials of Quintana's 2014 Giro win.", S['can']),
]
ADD['Gravel bike'] = [
    E('Cannondale Topstone', 'Cannondale', '2019', "Cannondale's gravel bike with the Kingpin rear compliance pivot.", S['cann'], [V('Topstone', '2019', 'Kingpin seat-tube pivot'), V('Topstone CAAD', '2026', 'announced October 2026')]),
    E('Cannondale Slate', 'Cannondale', '2016', "Cannondale's first gravel bike; discontinued in 2019.", S['cann']),
    E('Santa Cruz Stigmata', 'Santa Cruz', '', "Santa Cruz's current 700c cyclocross and gravel bike.", S['sc']),
]
ADD['Cyclocross bike'] = [
    E('Cannondale SuperX', 'Cannondale', '2011', "Cannondale's carbon cyclocross bike; retired in 2021 and revived in February 2025 as a gravel race bike.", S['cann']),
    E('Pinarello Crossista F', 'Pinarello', '2022', "Pinarello's cyclocross bike.", S['pin']),
]
ADD['Cross-country mountain bike'] = [
    E('Cannondale Scalpel', 'Cannondale', '2002', "Cannondale's cross-country race bike; the eighth generation launched in March 2024.", S['cann']),
    E('Canyon Lux', 'Canyon', '', "Canyon's cross-country race bike, part of its CFR range.", S['can']),
    E('Canyon Exceed', 'Canyon', '', "Canyon's cross-country hardtail, part of its CFR range.", S['can']),
]
ADD['Trail mountain bike'] = [
    E('Santa Cruz Tallboy', 'Santa Cruz', '', "Santa Cruz's 29-inch trail bike with 120 mm VPP travel; the Tallboy LT is discontinued.", S['sc']),
    E('Santa Cruz 5010', 'Santa Cruz', '', "Santa Cruz's mixed-wheel trail bike with 130 mm VPP travel.", S['sc']),
    E('Santa Cruz Chameleon', 'Santa Cruz', '', "Santa Cruz's 29-inch hardtail trail bike with 130 mm fork travel.", S['sc']),
    E('Cannondale Habit', 'Cannondale', '2016', "Cannondale's trail bike, begun on 27.5-inch wheels and later moved to 29-inch with 130 mm travel.", S['cann'], [V('Bad Habit', '2016', 'plus-tyre variant; relaunched April 2026')]),
    E('Specialized Rockhopper', 'Specialized', '', "Specialized's mountain bike; the name was the subject of a 1990 lawsuit against RockShox over name similarity.", S['spec']),
]
ADD['Enduro mountain bike'] = [
    E('Cannondale Jekyll', 'Cannondale', '2001', "Cannondale's full-suspension bike; discontinued in 2006, revived in 2011 as an enduro bike and redesigned in 2021.", S['cann']),
]
ADD['Downhill mountain bike'] = [
    E('Canyon Sender', 'Canyon', '', "Canyon's downhill bike, part of its CFR range.", S['can']),
]
ADD['Dirt-jump mountain bike'] = [
    E('Cannondale Chase', 'Cannondale', '2005', "Cannondale dirt-jump bike, discontinued in 2010.", S['cann']),
]
ADD['BMX bike'] = [
    E('Raleigh Burner', 'Raleigh', '', "Very successful UK BMX range from Raleigh.", S['ral'], [V('Bomber', '1981', 'used the original Raleigh 26 TPI threading')]),
    E('Schwinn Scrambler', 'Schwinn', '1975', "Schwinn's first BMX line.", S['schw'], [V('Competition Scrambler', '1976', ''), V('Mag Scrambler', '1977', ''), V('The Sting', '1979', ''), V('Predator', '1982', 'BMX line')]),
]
ADD['City bike'] = [
    E('Pashley Roadster', 'Pashley', '', "Men's traditional roadster, still made to a design that follows the 1920s original.", S['pash'], [V('Princess', '', "women's loop-frame model with a wicker basket and Brooks saddle"), V("Guv'nor", '2007', 'inspired by a 1930s catalogue; Reynolds 531 tubing')]),
    E('Raleigh Superbe', 'Raleigh', '1971', "Green three-speed Raleigh with 26-inch wheels and a hub dynamo.", S['ral']),
]
ADD['Hybrid bike'] = [
    E('Trek MultiTrack', 'Trek', '1990', "Trek's first hybrid line.", S['trek']),
]
ADD['Folding bike'] = [
    E('Dahon Boardwalk', 'Dahon', '2013', "Entry-level steel-frame commuter folder, among Dahon's best sellers.", S['dah']),
    E('Dahon Curl', 'Dahon', '2017', "Folder launched for Dahon's 35th anniversary and funded through Kickstarter.", S['dah'], [V('Curl i8', '2017', 'anniversary edition limited to 500 units')]),
    E('Dahon Mu', 'Dahon', '', "Dahon's long-running folder; special editions were made for the 25th and 30th years.", S['dah'], [V('Mμ XXV', '2008', '250 units for the 25th year of production'), V('Mμ 30th anniversary', '2012', 'carbon parts; 300 units')]),
    E('Dahon EEZZ', 'Dahon', '2012', "Vertical-fold Dahon that won a Eurobike Award.", S['dah']),
    E('Dahon Jifo', 'Dahon', '', "Dahon folder using vertical folding technology.", S['dah']),
    E('Dahon Mariner', 'Dahon', '2023', "Dahon folder; the D8 was named Best Folding Bike by The New York Times and the HD of 2026 takes payloads to 150 kg.", S['dah'], [V('Mariner D8', '2023', ''), V('Mariner HD', '2026', 'reinforced frame'), V('Mariner XL', '2026', '22-inch wheels')]),
    E('Dahon K-Feather', 'Dahon', '2025', "12 kg electric folder with torque-sensing pedal assist.", S['dah']),
    E('Dahon Ciao!', 'Dahon', '2005', "Dahon folder that won a Eurobike Award in 2005 and Fiets RAI Bike of the Year in 2006.", S['dah']),
    E('Tern Verge', 'Tern', '', "One of ten bike lines listed on Tern's page.", S['tern'], [V('Link', '', 'folder; its electric version, the eLink, was announced in August 2014'), V('Eclipse', '', 'listed line'), V('BYB', '', 'listed line')]),
]
ADD['Mini-velo'] = [
    E('Raleigh RSW 16', 'Raleigh', '1965', "Small-wheel Raleigh with balloon tyres and no suspension, made to compete with the Moulton.", S['ral'], [V('Twenty', '', 'sister model, more successful, in production well into the 1980s')]),
]
ADD['Cargo bike'] = [
    E('Surly Big Dummy', 'Surly', '2010', "Surly's longtail cargo frame.", S['surly']),
    E('Tern GSD', 'Tern', '', "Compact utility bike, listed among Tern's ten lines.", S['tern'], [V('HSD', '', 'listed line'), V('NBD', '', 'listed line'), V('Quick Haul', '', 'listed line'), V('Node', '', 'listed line'), V('Cargo Node', '2015', 'Kickstarter with Xtracycle raised US$153,638')]),
    E('Cannondale Cargowagen Neo', 'Cannondale', '2023', "First full-size Cannondale cargo e-bike; the Wonderwagen Neo is sold only in Europe.", S['cann'], [V('Wonderwagen Neo', '2023', 'Europe only')]),
]
ADD['Electric bike'] = [
    E('Gazelle Chamonix', 'Gazelle', '2009', "Gazelle's Innergy electric bike that won Dutch Bike of the Year.", S['gaz']),
    E('Cannondale Tesoro Neo', 'Cannondale', '2019', "Cannondale electric touring and commuter range.", S['cann'], [V('Tesoro Neo Carbon', '2023', '')]),
    E('Cannondale Adventure Neo', 'Cannondale', '2021', "Cannondale electric city and comfort bike with suspension.", S['cann']),
    E('Cannondale Compact Neo', 'Cannondale', '2022', "Folding 20-inch urban e-bike.", S['cann']),
    E('Cannondale Treadwell Neo', 'Cannondale', '', "Electric hybrid with a hidden hub motor.", S['cann']),
    E('Cannondale Mavaro Neo', 'Cannondale', '2023', "Comfort electric city bike; the SL variant uses a Bafang motor.", S['cann']),
    E('Cannondale Moterra', 'Cannondale', '2016', "Cannondale's first full-suspension e-MTB; redesigned in 2025.", S['cann'], [V('Moterra SL', '2024', '')], role='origin'),
    E('Cannondale Flying V', 'Cannondale', '2025', "All-carbon urban e-bike that won a 2026 Design & Innovation Award.", S['cann']),
    E('Santa Cruz Heckler', 'Santa Cruz', '', "Mountain bike of about 1995, discontinued for 2016 and relaunched as an e-bike in 2020.", S['sc']),
    E('Canyon Spectral:ON', 'Canyon', '2018', "Canyon's first e-bike.", S['can']),
    E('Giant Road-E+', 'Giant', '2016', "Giant e-bike announced in late 2016 with a Yamaha mid-drive motor.", S['giant']),
    E('Pinarello Nytro', 'Pinarello', '', "Pinarello's in-house e-bike brand.", S['pin']),
    E('Tern Vektron', 'Tern', '', "Electric bike listed among Tern's ten lines.", S['tern'], [V('eLink', '2014', "Tern's first electric bike, announced August 2014")]),
]
ADD['Children\'s bicycle'] = [
    E('Raleigh Grifter', 'Raleigh', '1976', "Raleigh's wheelie-style bike sharing the 76 mm bottom-bracket shell of the Twenty and Chopper.", S['ral']),
]

# groupset canon (replaces the kind's entries)
def grp(n, mk, y, d, s, v, a=''):
    return E(n, mk, y, d, s, v, a=a, dt='generation · speeds · mechanical or electronic')
SH = lambda code, y, d='': V(code, y, d)
GROUPSETS = [
    grp('Shimano Dura-Ace', 'Shimano', '1973', "Shimano's top road groupset; the 1980–1983 AX range placed it above the 600 group.", S['shl'],
        [V('Dura-Ace (first)', '1973', 'first aluminium pro-level road group'), V('Dura-Ace 10', '1976', 'track group with 10 mm chain pitch'), V('7100', '1977', 'second generation'), V('EX 7200', '1978', '6-speed, new freehubs'), V('AX 7300', '1980', 'aerodynamic design'), V('7400 SIS', '1984', '6-speed Shimano Indexed Shifting'), V('7401', '1987', '7-speed'), V('7402', '1988', '8-speed'), V('7400 STI', '1990', 'shift levers built into brake levers'), V('7700', '1996', '9-speed'), V('7800', '2003', '10-speed'), V('7900', '2008', 'hidden shift cables'), V('Di2 7970', '2009', 'electronic shifting'), V('9000', '2012', '11-speed'), V('R9100', '2016', '11-speed'), V('R9250 Di2', '2021', '12-speed electronic')], a='Dura Ace'),
    grp('Shimano Ultegra', 'Shimano', '', "Shimano's second road group, below Dura-Ace.", S['shl'], [V('6500', '1997', '9-speed'), V('6600', '2005', '10-speed'), V('6770 Di2', '2011', '10-speed electronic'), V('R8000', '2017', '11-speed'), V('R8150 Di2', '2021', '12-speed electronic')]),
    grp('Shimano 105', 'Shimano', '1987', "Shimano's mid-range road group.", S['shl'], [V('1050', '1987', '6-speed'), V('105SC', '1993', '8-speed'), V('5500', '1999', '9-speed'), V('5800', '2014', '11-speed'), V('R7000', '2018', '11-speed'), V('R7100', '2023', '12-speed, hydraulic brakes')]),
    grp('Shimano Tiagra', 'Shimano', '2006', "Shimano road group below 105.", S['shl'], [V('4500', '2006', '9-speed'), V('4700', '2015', '10-speed'), V('4720', '2019', '10-speed, hydraulic brakes'), V('R4000', '2026', '11-speed, hydraulic brakes')]),
    grp('Shimano Sora', 'Shimano', '2008', "Shimano entry-level road group above Claris.", S['shl'], [V('3400', '2008', '9-speed'), V('R3000', '2016', '9-speed'), V('R2000', '2017', '8-speed')]),
    grp('Shimano Claris', 'Shimano', '2009', "Shimano's lowest listed road group.", S['shl'], [V('2300', '2009', '8-speed'), V('2400', '2013', '8-speed')]),
    grp('Shimano Deore XT', 'Shimano', '1983', "Shimano's upper-middle mountain group; with Dura-Ace it received Shimano's innovations first from 1985.", S['xt'],
        [V('M700', '1983', 'friction (Deer Head)'), V('M730', '1987', 'indexed 6-speed'), V('M732', '1989', '7-speed'), V('M735', '1992', '7-speed'), V('M737', '1993', '8-speed'), V('M739', '1995', '8-speed'), V('M750', '1999', '9-speed'), V('M760', '2003', '9-speed'), V('M770', '2008', '9/10-speed'), V('M780', '2011', '10-speed'), V('M8000', '2015', '11-speed'), V('M8100', '2019', '12-speed'), V('M8150 Di2', '2023', 'for eMTB'), V('M8250', '2025', 'wireless Di2'), V('M8200', '2026', '12-speed, 9T cog')]),
    grp('Shimano XTR', 'Shimano', '2018', "Shimano's top mountain group.", S['shl'], [V('M9100', '2018', '12-speed'), V('M9250', '2025', 'wireless Di2')]),
    grp('Shimano SLX', 'Shimano', '2008', "Shimano mountain group between Deore and XT.", S['shl'], [V('M660/T660', '2008', '9-speed'), V('M7000', '2016', '11-speed'), V('M7100', '2019', '12-speed'), V('M7200', '2026', '12-speed')]),
    grp('Shimano Deore', 'Shimano', '2009', "Shimano mountain group below SLX.", S['shl'], [V('M590', '2009', '9-speed'), V('M6000', '2017', '10-speed'), V('M6100', '2020', '12-speed'), V('M6250', '2025', 'wireless Di2'), V('M6200', '2026', '12-speed')]),
    grp('Shimano Saint', 'Shimano', '', "Shimano's gravity-focused mountain group.", S['shl'], []),
    grp('Shimano GRX', 'Shimano', '2018', "Shimano's gravel groupset.", S['shl'], [V('RX800', '2018', '2x11'), V('RX810', '2019', '2x11'), V('RX812', '2019', '1x11'), V('RX820', '2023', '2x12'), V('RX822', '2023', '1x12'), V('RX825', '2024', '2x12 wired and wireless Di2'), V('RX827', '2025', '1x12 wireless Di2'), V('RX717', '2025', '1x12 wireless Di2')]),
    grp('Shimano Alfine', 'Shimano', '2010', "Shimano's internally geared hub, 8- or 11-speed.", S['shim'], [V('Alfine 700', '2010', '')]),
    grp('SRAM Red', 'SRAM', '2007', "SRAM's top road groupset, which brought wireless electronic shifting to road bikes.", S['sram'],
        [V('Red 10-speed', '2007', 'mechanical; the page text gives 2008'), V('Red 22', '2012', '11-speed'), V('Red eTap', '2015', 'wireless electronic'), V('Red eTap AXS', '2019', '12-speed wireless'), V('Red AXS', '2024', ''), V('Red XPLR AXS', '2024', '1x13 gravel')], a='Red eTap · Red AXS'),
    grp('SRAM Force', 'SRAM', '2006', "SRAM's second road group.", S['sram'], [V('Force 10-speed', '2006', ''), V('Force 22', '2013', '11-speed'), V('Force CX1', '2014', '1x11'), V('Force 1', '2015', '1x11'), V('Force eTap AXS D1', '2019', '12-speed'), V('Force eTap AXS D2', '2023', '12-speed'), V('Force AXS XPLR E1', '2025', '13-speed')]),
    grp('SRAM Rival', 'SRAM', '2006', "SRAM's mid-range road group.", S['sram'], [V('Rival 22', '2014', '11-speed'), V('Rival 1', '2015', '1x11'), V('Rival eTap AXS', '2021', '12-speed'), V('Rival AXS XPLR E1', '2025', '13-speed')]),
    grp('SRAM Apex', 'SRAM', '2010', "SRAM's entry road and gravel group.", S['sram'], [V('Apex', '2010', '10-speed'), V('Apex 1', '2016', '1x11'), V('Apex 1x12 and Apex AXS', '2023', ''), V('Apex AXS XPLR', '2025', '12-speed')]),
    grp('SRAM XX1', 'SRAM', '2012', "SRAM's top 1x mountain group, launched as 1x11.", S['sram'], [V('XX1 1x11', '2012', ''), V('XX1 Eagle', '2016', '1x12'), V('XX1 Eagle AXS', '2019', 'wireless')]),
    grp('SRAM X01', 'SRAM', '', "SRAM 1x mountain group below XX1.", S['sram'], [V('X01 1x11', '', ''), V('X01 Eagle', '2016', '1x12'), V('X01 Eagle AXS', '2019', 'wireless'), V('X01 DH', '', '1x7 or 1x10')]),
    grp('SRAM GX', 'SRAM', '2017', "SRAM's mid-priced 1x mountain group; GX Eagle launched in 2017.", S['sram'], [V('GX 1x11', '', ''), V('GX Eagle', '2017', '1x12'), V('GX Eagle AXS', '', ''), V('GX DH', '', '1x7'), V('GX Eagle Transmission', '', '')]),
    grp('SRAM NX', 'SRAM', '', "SRAM's entry 1x mountain group.", S['sram'], [V('NX 1x11', '', ''), V('NX Eagle', '', '1x12')]),
    grp('SRAM SX', 'SRAM', '', "SRAM's lowest-priced 12-speed mountain group.", S['sram'], [V('SX Eagle', '', '1x12')]),
    grp('SRAM Grip Shift', 'SRAM', '1988', "SRAM's twist shifter, on road bikes from 1988 and mountain bikes from 1991.", S['sram'], []),
    grp('Campagnolo Super Record', 'Campagnolo', '1973', "Campagnolo's top road groupset, launched for road and track in 1973.", S['camp'],
        [V('Super Record', '1973', 'road and track groups'), V('Super Record 11-speed', '2008', ''), V('Super Record EPS 11-speed', '2011', 'first electric version, used at the Tour de France'), V('Super Record 12-speed', '2018', 'mechanical'), V('Super Record EPS 12-speed', '2019', 'electronic'), V('Super Record Wireless', '2023', ''), V('Super Record 13-speed', '2025', '')], a='SR'),
    grp('Campagnolo Record', 'Campagnolo', '1963', "Campagnolo's long-running road line, from the 1963 rear derailleur; retired in 2025 and revived as 13-speed in 2026.", S['camp'],
        [V('Record rear derailleur', '1963', 'chromed bronze'), V('Nuovo Record rear derailleur', '1966', ''), V('C-Record', '1986', 'redesigned Record road and track groups'), V('Record 11-speed', '2008', ''), V('Record 12-speed', '2018', ''), V('Record 13-speed', '2026', '')], a='Nuovo Record · C-Record'),
    grp('Campagnolo Chorus', 'Campagnolo', '2008', "Campagnolo road group below Record.", S['camp'], [V('Chorus 11-speed', '2008', ''), V('Chorus EPS', '2015', ''), V('Chorus 12-speed', '2019', 'mechanical')]),
    grp('Campagnolo Athena', 'Campagnolo', '2009', "Campagnolo 11-speed road group, reintroduced in 2009.", S['camp'], [V('Athena EPS', '', 'discontinued 2015')]),
    grp('Campagnolo Centaur', 'Campagnolo', '2002', "Campagnolo group renamed from Daytona in 2002 and reintroduced in 2017 as its cheapest 11-speed group.", S['camp'], [V('Centaur', '2002', 'renamed from Daytona'), V('Centaur 11-speed', '2017', '')]),
    grp('Campagnolo Potenza', 'Campagnolo', '2015', "Campagnolo road group introduced in 2015.", S['camp'], []),
    grp('Campagnolo Veloce', 'Campagnolo', '', "Campagnolo entry-level road group in the flagship ranking.", S['camp'], []),
    grp('Campagnolo Ekar', 'Campagnolo', '2020', "13-speed Campagnolo gravel groupset.", S['camp'], []),
    grp('Campagnolo Gran Sport', 'Campagnolo', '1949', "Campagnolo's parallelogram rear derailleur of 1949.", S['camp'], []),
]

SUSP = [
    E('Cannondale Headshok', 'Cannondale', '1992', "Cannondale's integrated suspension fork system with an oversized head tube; it began as the Delta V fork.", S['cann'], [V('Delta V fork', '1992', ''), V('Lefty', '', 'single-legged fork from the early 2000s'), V('Ocho', '', 'mountain-bike Lefty'), V('Oliver', '', 'gravel Lefty')]),
]

# ---------------- edits of existing entries ----------------
def setfield(e, **kw):
    for k, v in kw.items(): e[k] = v
EDIT = {
    'Specialized Stumpjumper': dict(role='origin', s=S['spec']),
    'Raleigh Chopper': dict(role='landmark', s=S['ral']),
    'Cinelli Supercorsa': dict(role='landmark'),
    'Laufmaschine': dict(role='origin'),
    'Maclaren Buggy': dict(role='landmark', s=S['bt']),
    'Surly Cross-Check': dict(d="Surly's steel cross-check frame; discontinued in 2023 after 24 years.", s=S['surly']),
    'Specialized Epic': dict(s=S['spec']),
}
BIANCHI_DROP = {'Specialissima', 'Infinito', 'Oltre XR1–XR4'}

# per-kind nl / sel
BIKE_REF = "the Wikipedia pages of Trek, Specialized, Cannondale, Pinarello, Cervélo, Colnago, Bianchi, Santa Cruz, Canyon, Giant, Raleigh, Schwinn, Brompton, Dahon, Tern, Pashley, Surly, Gazelle, Strida and Moulton (fetched 2026-10-31)"
def sel_bike(extra=''):
    return "Every model line placed in this kind from " + BIKE_REF + ", plus earlier entries from the kind's own sources; sectioned by maker country, then maker." + extra
NL_LINE = "One entry is a model line or design sold under a maker's name; generations, sizes and builds are versions."
NL = {
    'Recumbent bicycle': NL_LINE, 'Recumbent tricycle': NL_LINE, 'Adult tricycle': "One entry is a named historic tricycle design; later models are versions.",
    'Tandem': NL_LINE, 'Velomobile': NL_LINE, 'Cycle rickshaw': "One entry is a regional type of cycle rickshaw; local makes are versions.",
    'Dandy horse': "One entry is a named early running-machine design.", 'High-wheel bicycle': "One entry is a named high-wheel design; makers' versions are versions.",
    "Children's bicycle": NL_LINE, 'Trailer bike': NL_LINE, 'Child bike seat': NL_LINE, 'Bicycle trailer': NL_LINE,
    'Frameset': "One entry is a named frame design or tubing line; model years are versions.", 'Headset': "One entry is a named headset design.",
    'Suspension fork': NL_LINE, 'Groupset': "One entry is a named groupset line of one maker, such as Shimano Ultegra; each generation is a version.",
    'Wheelset': NL_LINE, 'Bicycle tyre': NL_LINE, 'Bicycle pedals': NL_LINE, 'Bicycle saddle': NL_LINE,
    'Pram': "One entry is a named pram design or line; models and factory periods are versions.", 'Stroller': "One entry is a named stroller line; generations are versions.",
    'Jogging stroller': NL_LINE, 'Stroller wagon': NL_LINE,
}
SELS = {
    'Dandy horse': "Early running machines named on the Wikipedia pages Dandy horse and Tricycle.",
    'High-wheel bicycle': "High-wheel designs named on the Wikipedia page Penny-farthing.",
    'Cycle rickshaw': "Regional types named on the Wikipedia page Cycle rickshaw.",
    'Adult tricycle': "Tricycle designs named on the Wikipedia page Tricycle.",
    'Recumbent bicycle': "Recumbent makers' lines named on the Wikipedia page Recumbent bicycle and the HP Velotechnik and AZUB range pages.",
    'Recumbent tricycle': "Trike lines named on the Wikipedia pages Recumbent bicycle and Inspired Cycle Engineering and the HP Velotechnik, AZUB and Catrike range pages.",
    'Tandem': "Tandem designs named on the Wikipedia page Tandem bicycle.", 'Velomobile': "Velomobiles named on the Wikipedia page Velomobile and the Velomobiel.nl range page.",
    "Children's bicycle": "Children's lines named on the Wikipedia pages Training wheels, Wheelie bike, Schwinn Sting-Ray, Raleigh Chopper, Islabikes and Raleigh Bicycle Company and the woom range page.",
    'Trailer bike': "Trailer bikes named on the Wikipedia pages Trailer bike and Burley Design.", 'Child bike seat': "Child seats named on the Wikipedia page Child bicycle seat and the Thule and Hamax pages.",
    'Bicycle trailer': "Trailers named on the Thule and Hamax pages.",
    'Frameset': "Frame designs named on the Wikipedia pages Bicycle frame and Look (company).", 'Headset': "Headsets named on the Wikipedia page Headset (bicycle part).",
    'Suspension fork': "Forks named on the Wikipedia pages RockShox, Fox Factory, Bicycle fork and Cannondale; sectioned by maker country.",
    'Groupset': "Shimano series and generations from the Wikipedia pages List of Shimano groupsets and Shimano Deore XT; SRAM lines from SRAM Corporation; Campagnolo groups from Campagnolo; sectioned by maker country, then series, with every generation named on those pages as a version.",
    'Wheelset': "Wheelsets named on the Wikipedia page Zipp and the Mavic review page.", 'Bicycle tyre': "Tyres named on the earlier review pages.", 'Bicycle pedals': "Pedals named on the Wikipedia pages Bicycle pedal, Look (company), Shimano Pedaling Dynamics and Speedplay.",
    'Bicycle saddle': "Saddles named on the Brooks England and Bicycle saddle pages.",
    'Pram': "Prams named on the Wikipedia pages Baby transport and Silver Cross (company) and the Silver Cross Balmoral retailer page.",
    'Stroller': "Strollers named on the Wikipedia pages Baby transport, Owen Finlay Maclaren, Bugaboo International, UPPAbaby, Stokke AS and the Stokke stroller retailer page, plus earlier review pages.",
    'Jogging stroller': "Jogging strollers named on the BOB Gear and Thule pages.", 'Stroller wagon': "Wagons named on the WonderFold page.",
}

SORT_LAST = NS
def country_of(mk):
    if not mk: return NS
    return CTY.get(mk, NS)

KIND_DESC_FIX = {}

def process(dept):
    names_added = []
    for sh in dept['s']:
        for k in sh['k']:
            kn = k['n']
            xs = k.get('x') or []
            if kn == 'Groupset':
                xs = copy.deepcopy(GROUPSETS)
            elif kn == 'Suspension fork':
                xs = xs + copy.deepcopy(SUSP)
            else:
                xs = xs + copy.deepcopy(ADD.get(kn, []))
            out = []
            seen = set()
            for e in xs:
                if e['n'].lower() in seen: continue
                seen.add(e['n'].lower())
                if e['n'] in EDIT: e.update(EDIT[e['n']])
                if e['n'] == 'Bianchi celeste racer':
                    e['v'] = [v for v in e['v'] if v['n'] not in BIANCHI_DROP]
                    e['d'] = "Bianchi's racing bicycles in celeste, the brand's turquoise, from Coppi's steel racers to modern carbon."
                if e['n'] == 'Brompton':
                    e['v'] = [v for v in e['v'] if v['n'] != 'P Line'] + [V('P Line', '', '4 or 12 speed'), V('Electric', '', 'rear hub motor, 4 speeds only')]
                    seenv = set(); nv = []
                    for v in e['v']:
                        if v['n'] in seenv: continue
                        seenv.add(v['n']); nv.append(v)
                    e['v'] = nv
                if e['n'] == 'Moulton':
                    e['v'] = [V('Standard (M1) · Deluxe (M2) · Stowaway (M5) · Speedsix (M6)', '1962–1967', 'home-market models'), V('AM series', 'early 1980s', 'Alex Moulton bought back the design rights from Raleigh'), V('APB', '1992–2005', 'cheaper AM variant built under licence by Pashley'), V('New Series', '1998', 'Flexitor front suspension; Double Pylon is its flagship'), V('TSR', '2005', 'called the Moulton TSR from 2008'), V('Bridgestone Moulton', '2000', '')]
                if e['n'] == 'Strida':
                    e['mk'] = 'Strida'; e['y'] = '1987'
                    e['d'] = "Triangular folding bicycle with a belt drive, released in 1987 and in production since 1986."
                    e['s'] = S['str']
                    e['v'] = [V('Strida 1', '1987', 'drum brakes; about 3,000 made in Glasgow'), V('Strida 2', 'c. 1998', 'same mechanism after the 1997 rights purchase'), V('Strida 3', '2002', 'drum brakes'), V('Strida 5', '2007', 'disc brakes; design award 2007, version 5.2 in 2009'), V('Strida SX', '', '355 mm wheels'), V('Strida EVO', '', 'three-speed with Sturmey-Archer kickback bottom bracket'), V('Strida LT', '', 'glass-fibre-reinforced nylon wheels')]
                if e['n'] == 'Bickerton': e['mk'] = 'Bickerton'
                if e['n'] == 'Pashley Pronto / Mailstar':
                    e['s'] = S['pash']
                if e['n'] == 'Santa Cruz Blur':
                    e['s'] = S['sc']
                if e['n'] == 'Bugaboo Frog':
                    e['d'] = "Modular Dutch pushchair taking a carrycot or seat on one chassis; the Frog was popularised by an appearance in Sex and the City."
                    e['role'] = 'landmark'
                if e['n'] == 'YOYO':
                    e['v'] = [V('BABYZEN YOYO', '', 'French stroller from Babyzen'), V('YOYO³', '', 'sold under Stokke after its 2021 acquisition of Babyzen')]
                    e['s'] = S['stk']
                    e['d'] = "Ultra-compact travel stroller from Babyzen; Stokke acquired Babyzen in 2021."
                if e['n'] == 'Maclaren Buggy':
                    e['v'] = [V('B01 prototype', '1965', '6 lb prototype; UK patent applied for 20 July 1965'), V('first production buggy', '1967', 'about 1,000 made in the first year'), V('Buggy Major', 'c. 1970', 'larger folding buggy with square tubes for children with disabilities, commissioned by the Ministry of Health')]
                    e['d'] = "Lightweight aluminium-tube buggy designed by Owen Finlay Maclaren; production rose to a reported 600,000 a year by 1976."
                    e['y'] = '1965'
                if e['n'] == 'Silver Cross coach pram':
                    e['s'] = S['sx']
                if e['n'] == 'UPPAbaby Vista':
                    e['y'] = '2006'
                    e['d'] = "Full-size American modular stroller; UPPAbaby's first product, from the company founded in 2006."
                mk = e.get('mk') or ''
                ctry = country_of(mk)
                if kn == 'Groupset' and mk == 'Shimano': ctry = 'Japan'
                e['g'] = f"{ctry} · {mk}" if mk else NS
                if mk in OWN:
                    own, tier, cty, oy = OWN[mk]
                    e['own'] = own; e['tier'] = tier; e['cty'] = cty
                    if oy: e['own_y'] = oy
                    else: e.pop('own_y', None)
                out.append(e)
            def key(e):
                g = e['g']
                return (1 if g == NS else 0, g, e.get('y') or 'zzzz', e['n'])
            out.sort(key=key)
            if out:
                k['x'] = out
                k['nl'] = NL.get(kn, NL_LINE)
                base = SELS.get(kn)
                if base is None:
                    base = sel_bike()
                k['sel'] = base + f" Covers {len(out)} named entries; no reference lists the whole kind, so no total is known and makers or lines not on the pages read are missing."
                if kn == 'Groupset':
                    k['sel'] = SELS[kn] + f" Complete: {len(out)} of {len(out)} groupset lines named on those pages (the Shimano list was read through a summariser; Tourney, Altus and Acera are not named there)."
                k['xg'] = 'by maker country, then maker'
            for key_ in ('m', 'r'):
                k.pop(key_, None)
    return dept

depts = []
for d in src['depts']:
    if d['n'] in ('Bicycles', 'Prams & strollers'):
        dd = process(copy.deepcopy(d))
        depts.append(dd)

# prams additions
pr = [x for x in depts if x['n'] == 'Prams & strollers'][0]
def kind(dep, n):
    for sh in dep['s']:
        for k in sh['k']:
            if k['n'] == n: return k
def addx(dep, kn, entries):
    k = kind(dep, kn)
    for e in entries:
        mk = e.get('mk') or ''
        e['g'] = f"{country_of(mk)} · {mk}" if mk else NS
        if mk in OWN:
            own, tier, cty, oy = OWN[mk]
            e['own'] = own; e['tier'] = tier; e['cty'] = cty
            if oy: e['own_y'] = oy
    k['x'] = (k.get('x') or []) + entries
    k['x'].sort(key=lambda e: (1 if e['g'] == NS else 0, e['g'], e.get('y') or 'zzzz', e['n']))
    return k

addx(pr, 'Pram', [
    E("Kent's shell carriage", 'William Kent', '1733', "Shell-shaped wheeled basket built for the Duke of Devonshire's children, meant to be pulled by a goat or small pony.", S['bt'], role='origin'),
    E('Silver Cross Balmoral', 'Silver Cross', '', "Silver Cross carrycot pram with a C-shaped steel chassis, made in the United Kingdom.", S['bal'], [V('140th Anniversary Balmoral', '2017', 'limited to 140 made, with a numbered plaque'), V('Vintage Balmoral', '', 'distinctive carrycot colour and coordinated chassis')], dt='fabric · apron · hood'),
])
addx(pr, 'Stroller', [
    E('Richardson reversible stroller', 'William H. Richardson', '1889', "Patented in June 1889 as the first reversible stroller, with independent movement of each wheel.", S['bt']),
    E('Stokke Xplory', 'Stokke', '2003', "Stokke's first stroller, with a high, parent-facing, reversible seat unit.", S['stks'], [V('Xplory V3', '', 'discontinued 2013'), V('Xplory V6', '', 'discontinued 2021'), V('Xplory X', '', 'current model')], dt='seat or carrycot · chassis colour'),
    E('Stokke Trailz', 'Stokke', '2014', "Stokke stroller; the Terrain and Classic versions were both discontinued in 2021.", S['stks']),
    E('Stokke Crusi', 'Stokke', '2012', "Stokke stroller, discontinued in 2016.", S['stks']),
    E('Stokke Scoot', 'Stokke', '2012', "Stokke stroller listed in three versions.", S['stks'], [V('Scoot V1', '', ''), V('Scoot V2', '', ''), V('Scoot V3', '', '')]),
])
CTY['William Kent'] = 'United Kingdom'
for e in kind(pr, 'Pram')['x']:
    if e['mk'] == 'William Kent': e['g'] = 'United Kingdom · William Kent'
    if e['n'] == 'Silver Cross coach pram': pass
for e in kind(pr, 'Stroller')['x']:
    if e['mk'] == 'William H. Richardson': e['g'] = NS
for kn in ('Pram', 'Stroller'):
    k = kind(pr, kn)
    k['x'].sort(key=lambda e: (1 if e['g'] == NS else 0, e['g'], e.get('y') or 'zzzz', e['n']))
    k['sel'] = SELS[kn] + f" Covers {len(k['x'])} named entries; the reference pages give no total for prams or strollers, so makers and lines not on those pages are missing."

# ---------------- department fields ----------------
bk = [x for x in depts if x['n'] == 'Bicycles'][0]
bk['ms'] = [
    {"mkt": "Bicycle components worldwide", "who": "Shimano", "share": "85 %", "yr": 2016, "s": S['shim'], "note": "estimated share by value; the page cites a 2016 Credit Suisse report and gives no other date"},
    {"mkt": "Bicycle components worldwide", "who": "SRAM", "share": "15 %", "yr": 2010, "s": S['sram'], "note": "the company's own estimate of its share of a US$3.5 billion components market, 2010 era"},
    {"mkt": "Shimano revenue", "who": "Shimano", "share": "US$2.872 billion", "yr": 2024, "s": S['shim'], "note": "fiscal-year revenue; bicycle components were 76.6 % of it"},
    {"mkt": "Giant revenue", "who": "Giant Manufacturing", "share": "US$1.9 billion", "yr": 2017, "s": S['giant'], "note": "revenue; 6.6 million bicycles sold in 2017 and more than 12,000 retail stores by 2018"},
    {"mkt": "Giant e-bike share of sales", "who": "Giant Manufacturing", "share": "30 %", "yr": 2021, "s": S['giant'], "note": "share of Giant's sales; first-quarter revenue rose 55 %"},
    {"mkt": "Merida revenue", "who": "Merida", "share": "NT$29.39 billion", "yr": 2021, "s": S['merida'], "note": "over two million bicycles a year, undated; bought 49 % of Specialized in 2001"},
    {"mkt": "Pon Holdings bicycle revenue", "who": "Pon Holdings", "share": "€2.1 billion", "yr": 2024, "s": S['pon'], "note": "described as one of the five largest bicycle manufacturers; brands include Gazelle, Cervélo, Santa Cruz, Cannondale"},
    {"mkt": "Accell Group revenue", "who": "Accell Group", "share": "€1.294 billion", "yr": 2023, "s": S['acc'], "note": "net loss €390 million; KKR bought the group for about €1.56 billion in 2022; insolvency proceedings began in August 2026"},
    {"mkt": "Specialized revenue", "who": "Specialized Bicycle Components", "share": "US$500 million", "yr": 2011, "s": S['spec'], "note": "estimate"},
    {"mkt": "Trek revenue", "who": "Trek Bicycle Corporation", "share": "US$1.0 billion", "yr": 2014, "s": S['trek'], "note": "the page gives no year; 1,800 employees in 2014"},
    {"mkt": "Canyon revenue", "who": "Canyon Bicycles", "share": "€738 million", "yr": 2025, "s": S['can'], "note": "revenue"},
    {"mkt": "Brompton revenue", "who": "Brompton Bicycle", "share": "£42 million", "yr": 2019, "s": S['brom'], "note": "revenue of £42 million or more; about 50,000 bicycles a year, undated"},
    {"mkt": "Gazelle output", "who": "Gazelle", "share": "300,000 a year", "yr": 2025, "s": S['gaz'], "note": "the page gives no year for the current output; total production has passed 13 million"},
    {"mkt": "Folding bicycles worldwide", "who": "Dahon", "share": "two thirds", "yr": 2006, "s": S['dah'], "note": "the page flags this claim as needing a source"},
    {"mkt": "EU e-bike sales", "who": "All makers", "share": "over 5 million", "yr": 2021, "s": S['ebike'], "note": "units sold in the EU; 2 million in 2016"},
    {"mkt": "E-bike share of bicycle sales, Netherlands", "who": "All makers", "share": "57 %", "yr": 2022, "s": S['ebike'], "note": "Austria 49 %, Germany 48 %, Belgium 47 % the same year"},
    {"mkt": "Japan e-bike sales", "who": "All makers", "share": "350,000", "yr": 2023, "s": S['ebike'], "note": "units; 150,000 in 2018"},
    {"mkt": "China e-bike production", "who": "All makers", "share": "22.2 million", "yr": 2009, "s": S['ebike'], "note": "units produced; the page also gives 380 million registered in 2025"},
]
bk['msum'] = "Components are held by two groups: Shimano's estimated 85 % by value and SRAM's own 15 % estimate. Frames are split between Taiwanese makers (Giant, Merida), Pon Holdings and the former Accell Group; the figures below are the last on each fetched page."
pr['ms'] = [
    {"mkt": "Maclaren buggy output", "who": "Maclaren", "share": "600,000 a year", "yr": 1976, "s": S['mac'], "note": "reported production; about 1,000 made in 1967"},
    {"mkt": "Silver Cross ownership", "who": "Fosun International", "share": "87.23 %", "yr": 2017, "s": S['sx'], "note": "Fosun bought the company in 2015"},
    {"mkt": "Bugaboo reach", "who": "Bain Capital", "share": "50 countries", "yr": 2018, "s": S['bug'], "note": "Bain Capital acquired Bugaboo in February 2018; over 1,200 staff"},
    {"mkt": "UPPAbaby reach", "who": "UPPAbaby", "share": "50 countries", "yr": 2022, "s": S['upp'], "note": "more than 175 employees; reported to be exploring a sale in October 2023"},
    {"mkt": "Babyzen purchase", "who": "Stokke", "share": "acquired", "yr": 2021, "s": S['stk'], "note": "Stokke bought Babyzen and its YOYO stroller line"},
]
pr['msum'] = "No fetched page gives a stroller market share. The figures show output and ownership of the best-known makers; the one market-report page tried (Global Market Insights) returned an error."

# ---------------- shelf/kind fixes: shelf order (groupset ordering), kind t ----------------
BR = json.load(open(ROOT + 'out/G1_brands.json'))['b']
have = {b['n'] for b in BR}
def B(n, c_, f, seg, d, s, kf, rel=None, lines=None):
    return {"n": n, "c": c_, "f": f, "seg": seg, "d": d, "lines": lines or [], "eras": [], "sig": [], "sc": [], "rel": rel or [], "s": s, "kf": kf}
newb = [
    B('Pon Holdings', 'Netherlands', '1980', 'Mainstream', "Dutch mobility group founded by Ben Pon Jr., still family-owned; one of the five largest bicycle groups, with Gazelle, Cervélo, Santa Cruz and Cannondale.", S['pon'], 'bicycle group', ['Gazelle', 'Cervélo', 'Santa Cruz', 'Cannondale']),
    B('Accell Group', 'Netherlands', '1998', 'Mainstream', "Dutch bicycle group that owned Raleigh, Batavus, Sparta, Koga, Haibike, Lapierre, Ghost and Babboe; began insolvency proceedings in August 2026.", S['acc'], 'bicycle group', ['Raleigh', 'Koga']),
    B('Giant Manufacturing', 'Taiwan', '', 'Mainstream', "Taichung bicycle maker described as the world's largest bicycle designer and manufacturer; also owns Liv.", S['giant'], 'bicycles'),
    B('Merida', 'Taiwan', '1972', 'Mainstream', "Taiwanese bicycle maker founded by Ike Tseng; bought 49 % of Specialized in 2001.", S['merida'], 'bicycles', ['Specialized']),
    B('Quality Bicycle Products', 'United States', '', 'Specialist', "American bicycle distributor and parent of Surly.", S['surly'], 'bicycle parts', ['Surly']),
    B('Fosun International', 'China', '', 'Mainstream', "Chinese conglomerate that bought Silver Cross in 2015.", S['sx'], 'conglomerate', ['Silver Cross']),
    B('Bain Capital', 'United States', '', 'Mainstream', "Investment firm that acquired Bugaboo in February 2018.", S['bug'], 'private equity', ['Bugaboo']),
    B('Cycleurope', 'Sweden', '', 'Mainstream', "Bicycle group owned by Grimaldi Industri AB; Bianchi joined it in 1997.", S['bia'], 'bicycle group', ['Bianchi']),
]
brands = [b for b in newb if b['n'] not in have]
bu = {}
for mk, (own, tier, cty, oy) in OWN.items():
    if mk in have:
        bu[mk] = {"own": own, "tier": tier, "c": cty}
# Giant,Dahon etc not in register -> add Giant/Dahon covered; keep only existing in bu

part = {"replaces": ["Bicycles", "Prams & strollers"], "depts": depts, "brands": brands, "brand_updates": bu, "renames": {}, "moves": []}
json.dump(part, open(ROOT + 'out/G1_parts/BIKES.json.tmp', 'w'), ensure_ascii=False, indent=1)
os.replace(ROOT + 'out/G1_parts/BIKES.json.tmp', ROOT + 'out/G1_parts/BIKES.json')
n = sum(len(k.get('x', [])) for d in depts for s in d['s'] for k in s['k'])
print('entries', n, 'bytes', os.path.getsize(ROOT + 'out/G1_parts/BIKES.json'))
print('bu', len(bu), 'new brands', len(brands))
