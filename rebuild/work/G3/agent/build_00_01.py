import json, os
W = 'https://en.wikipedia.org/wiki/'
AGA = W + 'AGA_cooker'; LC = W + 'La_Cornue'; GW = W + 'Gaggenau_Hausgeräte'; SZ = W + 'Sub-Zero_(company)'
CHAT = 'https://www.lacornueusa.com/chateau-series/chateau'
SULLY = 'https://www.lacanche.com/Kitchen-ranges/Piano_info.php?fourneaux=sully'
LACL = 'https://www.frenchranges.com/lacanche-ranges/'
WOLF = 'https://ca.subzero-wolf.com/en/products/wolf/ranges/dual-fuel'
OG = 'https://www.officinegullo.com/'
FAL = 'https://nz.agafalcon.com/about-us/falcon-history'
ESSE = 'https://www.esse.com/about/'
EVH = 'https://everhot.co.uk/about/history-and-innovation/'
ER7 = 'https://www.agarangeusa.com/classic/ranges/product/aga-er7-100'
VARIO = 'https://www.gaggenau.com/us/products/cooktops/400-series'
BORA = 'https://www.bora.com/en-int/press/willi-bruckbauer-full-steam-ahead-in-the-battle-against-cooking-vapours'
SZD = 'https://www.subzero-wolf.com/refrigeration/designer-series'
GVC = 'https://www.gaggenau.com/us/products/refrigerators/400-series'
EC = 'https://www.eurocave.com/en/cabinets-and-wine/flush-fitting-wine-cabinet'
MCOF = 'https://www.mieleusa.com/category/1014554/built-in-coffee-machines'
MWD = 'https://www.mieleusa.com/category/1013132/gourmet-warming-drawers'


def v(n, mk='', y='', d=''):
    return {'n': n, 'mk': mk, 'y': y, 'd': d}


kinds = [
 {'n': 'Range cooker', 'a': 'range · kitchen range · range stove',
  'd': 'Wide freestanding-look cooker combining one or more ovens with a hob on top, often fitted between kitchen units.',
  't': ['gas', 'electric', 'dual fuel', 'induction top', 'single cavity', 'twin cavity'],
  's': W + 'Kitchen_stove',
  'x': [
   {'n': 'La Cornue Château', 'a': 'Château series', 'd': 'Hand-built French range with vaulted ovens, one gas and one electric on the larger sizes.',
    'mk': 'La Cornue', 'y': '1908 (vaulted oven)', 's': CHAT,
    'v': [v('Grand Palais 180', 'La Cornue', '', '1800 mm; grand vaulted gas and electric ovens'),
          v('Le Château 165', 'La Cornue', '', '1650 mm'), v('Le Château 150', 'La Cornue', '', '1500 mm; two standard vaulted ovens'),
          v('Le Château 120', 'La Cornue', '', '1200 mm; gas and electric vaulted ovens'), v('Le Château 90', 'La Cornue', '', '900 mm; one grand vaulted oven'),
          v('Le Château 75', 'La Cornue', '', '750 mm'), v('Le Château 60', 'La Cornue', '', '600 mm; induction rangetop'),
          v('Le Châtelet 135', 'La Cornue', '', 'vaulted oven plus warming oven')],
    'dt': 'width 600–1800 mm · gas or electric vaulted ovens · rangetop configuration · enamel colour and trim'},
   {'n': 'La Cornue CornuFé', 'a': 'CornuFé', 'd': 'La Cornue’s more compact range line, made alongside the Château.',
    'mk': 'La Cornue', 'y': '', 's': LC, 'v': [], 'dt': 'oven type · colour and trim'},
   {'n': 'Lacanche Sully', 'a': 'Sully Classique', 'd': 'Burgundy-built range of 1405 mm with two large ovens under a large hob.',
    'mk': 'Lacanche', 'y': '', 's': SULLY,
    'v': [v('Sully', 'Lacanche', '', '1405 mm; gas, electric or multifunction ovens'), v('Sully 1800', 'Lacanche', '', '71 in wide'),
          v('Sully 2200', 'Lacanche', '', '86 in wide'), v('Sully Moderne', 'Lacanche', '', 'Moderne line styling')],
    'dt': 'width · oven fuel · hob layout (burners, plancha, simmer plate) · Classique or Moderne trim · colour'},
   {'n': 'Lacanche Cluny', 'a': 'Cluny', 'd': 'Lacanche range about 1000 mm wide with two ovens; also made in 1400 and 1800 widths.',
    'mk': 'Lacanche', 'y': '', 's': LACL,
    'v': [v('Cluny', 'Lacanche', '', '39⅜ in wide'), v('Cluny 1400', 'Lacanche', '', '55 in wide'), v('Cluny 1800', 'Lacanche', '', '71 in wide'),
          v('Cluny Moderne', 'Lacanche', '', 'Moderne line styling')],
    'dt': 'width · oven fuel · hob layout · Classique or Moderne trim · colour'},
   {'n': 'Wolf dual-fuel range', 'a': 'Wolf range', 'd': 'American professional-style range pairing sealed gas burners with an electric convection oven.',
    'mk': 'Wolf', 'y': '', 's': WOLF, 'v': [],
    'dt': '4, 6 or 8 burners · rangetop: all burner, infrared griddle, infrared charbroiler, French top · finish'},
   {'n': 'Officine Gullo OG Professional', 'a': 'OG Professional', 'd': 'Florentine made-to-order cooking unit in professional style.',
    'mk': 'Officine Gullo', 'y': '', 's': OG, 'v': [v('Fiorentina', 'Officine Gullo', '', 'companion cooking-unit line')],
    'dt': 'configuration · finish and metal trim'},
   {'n': 'Falcon range cooker', 'a': '', 'd': 'British range cooker made by AGA Rangemaster in Leamington Spa.',
    'mk': 'Falcon', 'y': '', 's': FAL,
    'v': [v('Elan Deluxe', 'Falcon'), v('Classic Deluxe 110 Induction', 'Falcon'), v('Nexus Steam', 'Falcon'), v('Nexus SE Induction', 'Falcon')],
    'dt': 'width · fuel · hob type · colour'},
  ]},
 {'n': 'Heat-storage range cooker', 'a': 'AGA-type cooker · storage cooker',
  'd': 'Heavy cast-iron range that stores heat from a continuous low-intensity source and keeps ovens always ready.',
  't': ['gas', 'oil', 'electric', 'wood-fired', 'with hot water or central heating'],
  's': AGA,
  'x': [
   {'n': 'AGA cooker', 'a': 'Aga', 'd': 'Swedish-invented cast-iron heat-storage range with fixed-temperature ovens and two hotplates.',
    'mk': 'AGA', 'y': '1922', 's': AGA,
    'v': [v('AGA 60', 'AGA', '', 'smallest model, 60 cm wide'), v('Dual Control', 'AGA'), v('Total Control', 'AGA', '2011'),
          v('3 Series', 'AGA'), v('eR7 100', 'AGA', '', 'electric; three cast-iron ovens, two hotplates, touch-screen'),
          v('eR7 150', 'AGA', '', 'adds slow-cook and warming ovens'), v('eR7 160', 'AGA', '', 'adds conventional and convection ovens and gas hob'),
          v('eR7 210', 'AGA', '', 'adds slow-cook and warming ovens and dual-fuel module')],
    'dt': '2–5 ovens · fuel · width · enamel colour (17 on eR7)'},
   {'n': 'Rayburn', 'a': '', 'd': 'Range cooker sold under the Rayburn name by AGA Rangemaster, sister to AGA.',
    'mk': 'Rayburn', 'y': '', 's': FAL, 'v': [], 'dt': 'fuel · heating and hot-water options · colour'},
   {'n': 'ESSE wood-burning range cooker', 'a': 'ESSE Woodfired', 'd': 'British cast-iron wood-burning range cooker built at the ESSE foundry.',
    'mk': 'ESSE', 'y': '1854 (first ESSE stove)', 's': ESSE,
    'v': [v('Ironheart', 'ESSE', '2004', 'wood-fired cooking stove'), v('Woodfired', 'ESSE', '2006', 'continuous-use cooker; hot water and heating options'),
          v('990', 'ESSE', '2011'), v('1000 W', 'ESSE', '2023', 'Ecodesign wood-burning range cooker')],
    'dt': 'cooking only, hot water or central heating · colour'},
   {'n': 'Electric ESSE', 'a': '', 'd': 'ESSE’s electric range cooker.', 'mk': 'ESSE', 'y': '2000', 's': ESSE, 'v': [], 'dt': 'width · colour'},
   {'n': 'Everhot', 'a': '', 'd': 'Electric heat-storage range on a trickle-feed design that runs from a standard 13 A supply.',
    'mk': 'Everhot', 'y': '1979 (first brochure)', 's': EVH,
    'v': [v('60', 'Everhot'), v('90', 'Everhot'), v('100', 'Everhot'), v('110', 'Everhot'), v('120', 'Everhot'), v('150', 'Everhot')],
    'dt': 'width (series number in cm) · colour'},
  ]},
 {'n': 'Built-in oven', 'a': 'oven · wall oven · integrated oven',
  'd': 'Enclosed oven fitted into kitchen units at eye or under-counter level, heating food in a closed chamber.',
  't': ['single', 'double', 'compact', 'wall oven', 'fan (convection)'],
  's': 'https://www.diy-kitchens.com/appliances/cooking/single-ovens/bosch-series-8-single-oven-hbg7341b1b',
  'r': [['Series 8', 'Bosch Home Appliances']],
  'x': [
   {'n': 'Gaggenau EB 900', 'a': 'EB900', 'd': 'Gaggenau’s wide built-in oven designed under chief designer Timothy Jacob Jensen.',
    'mk': 'Gaggenau', 'y': '1991–1998', 's': GW, 'v': [], 'dt': 'width · finish'}]},
 {'n': 'Steam and combination oven', 'a': 'steam oven · combi-steam oven · combination microwave · speed oven',
  'd': 'Built-in oven that cooks with steam, or combines steam or microwave with conventional heat.',
  't': ['steam only', 'combi-steam', 'microwave combination', 'speed oven', 'plumbed or tank-fed'],
  's': W + 'Steam_oven'},
 {'n': 'Hob', 'a': 'cooktop',
  'd': 'Built-in cooking surface of burners or heating zones on which pans are set.',
  't': ['gas', 'induction', 'ceramic', 'modular (domino)', 'venting hob'],
  's': 'https://www.siemens-home.bsh-group.com/za/en/mkt-category/cooking-and-baking/hobs/induction-hobs',
  'r': [['iQ700', 'Siemens']],
  'x': [
   {'n': 'Gaggenau Vario 400 series', 'a': 'Vario hobs', 'd': 'Modular cooktop system combining single-function modules side by side.',
    'mk': 'Gaggenau', 'y': '', 's': VARIO, 'v': [],
    'dt': 'modules: full-surface induction, flex induction, induction wok, gas wok, gas, Teppan Yaki, electric grill, downdraft · width 15–36 in'},
   {'n': 'BORA cooktop extractor', 'a': 'venting hob · BORA', 'd': 'Hob with an extractor drawing cooking vapours down at the hob surface.',
    'mk': 'BORA', 'y': '2008', 's': BORA, 'v': [v('BORA Professional', 'BORA', '2008', 'first market launch')],
    'dt': 'induction or gas zones · ducted or recirculating · width'}]},
 {'n': 'Cooker hood', 'a': 'kitchen hood · extractor hood · range hood',
  'd': 'Fan unit above or beside the hob that removes grease, smoke, heat and steam by extraction or filtering.',
  't': ['wall-mounted', 'ceiling', 'downdraft', 'ducted', 'recirculating (charcoal filter)'],
  's': W + 'Kitchen_hood'},
 {'n': 'Built-in refrigerator', 'a': 'integrated fridge · fridge column · built-in fridge freezer',
  'd': 'Refrigerator or freezer fitted into cabinetry, often behind furniture panels, singly or as columns.',
  't': ['integrated (panel-ready)', 'fridge column', 'freezer column', 'fridge-freezer', 'undercounter'],
  's': SZ,
  'x': [
   {'n': 'Sub-Zero Designer Series', 'a': 'Sub-Zero integrated column', 'd': 'Panel-ready built-in refrigeration with hidden hinges for flush fitting.',
    'mk': 'Sub-Zero', 'y': '', 's': SZD,
    'v': [v('Column', 'Sub-Zero', '', 'all-refrigerator or all-freezer'), v('Over-and-Under', 'Sub-Zero', '', 'fridge above, freezer below'),
          v('Undercounter', 'Sub-Zero')],
    'dt': 'width · panel or stainless finish · single or side-by-side'},
   {'n': 'Gaggenau Vario cooling 400 series', 'a': 'Vario refrigerators', 'd': 'Fully integrated fridge, freezer and wine units combined into a cooling wall.',
    'mk': 'Gaggenau', 'y': '', 's': GVC, 'v': [],
    'dt': 'combination · anthracite aluminium or stainless steel cladding · with or without handles'}]},
 {'n': 'Built-in wine cabinet', 'a': 'integrated wine cooler · wine fridge',
  'd': 'Temperature-controlled wine storage fitted under a worktop or in a tall unit.',
  't': ['undercounter', 'tall column', 'single temperature', 'multi-temperature', 'glass door', 'furniture front'],
  's': EC,
  'x': [
   {'n': 'Sub-Zero 424', 'a': '', 'd': 'Sub-Zero wine storage unit kept to nearly the same design since the early 1990s.',
    'mk': 'Sub-Zero', 'y': 'early 1990s', 's': SZ, 'v': [], 'dt': ''},
   {'n': 'EuroCave Inspiration', 'a': '', 'd': 'Built-in wine cabinet with concealed technical parts, made to match surrounding furniture.',
    'mk': 'EuroCave', 'y': '', 's': EC, 'v': [], 'dt': '1, 2 or multi-temperature · 3 sizes'},
   {'n': 'EuroCave Compact', 'a': '', 'd': 'Compact built-in wine cabinet for kitchen integration.',
    'mk': 'EuroCave', 'y': '', 's': EC, 'v': [], 'dt': 'glass or matching front · single or multi-temperature · 2 sizes'},
   {'n': 'Gaggenau Vario wine climate cabinet', 'a': '', 'd': 'Wine unit of the Vario 400 cooling system, combinable with fridge and freezer columns.',
    'mk': 'Gaggenau', 'y': '', 's': GVC, 'v': [], 'dt': 'cladding · handles'}]},
 {'n': 'Built-in coffee machine', 'a': 'built-in bean-to-cup · integrated coffee machine',
  'd': 'Bean-to-cup coffee machine fitted into a tall unit, either tank-fed or plumbed in.',
  't': ['tank-fed', 'plumbed-in'], 's': MCOF,
  'm': [['CVA 7845', 'Miele'], ['CVA 7875', 'Miele'], ['CVA 7775', 'Miele'], ['CVA 7445', 'Miele']]},
 {'n': 'Warming drawer', 'a': 'gourmet warming drawer',
  'd': 'Built-in heated drawer under an oven for warming plates and keeping food warm.',
  't': ['plate warming', 'low-temperature cooking', 'shallow', 'deep'], 's': MWD,
  'm': [['ESW 7680', 'Miele'], ['ESW 7580', 'Miele'], ['ESW 7670', 'Miele'], ['ESW 7570', 'Miele']]},
]


def b(n, c, f, seg, d, s, lines=(), eras=(), sig=(), rel=(), sc=()):
    return {'n': n, 'c': c, 'f': f, 'seg': seg, 'd': d, 'lines': list(lines), 'eras': list(eras), 'sig': list(sig), 'sc': list(sc), 'rel': list(rel), 's': s}


brands = [
 b('AGA', 'United Kingdom', '1922', 'Heat-storage range cookers', 'Cast-iron range invented in Sweden by Gustaf Dalén, made mainly in the UK since 1957; owned by Middleby since 2015.',
   AGA, ['Total Control', 'Dual Control', '3 Series', 'eR7'], ['Svenska AB Gasaccumulator, from 1922', 'AGA Rangemaster, Middleby from 2015'], ['AGA cooker'], ['Rayburn', 'Falcon', 'La Cornue']),
 b('Rayburn', 'United Kingdom', '', 'Range cookers', 'Range cooker name traded by AGA Rangemaster alongside AGA and Falcon.', FAL, [], [], ['Rayburn'], ['AGA', 'Falcon']),
 b('Falcon', 'United Kingdom', '1803', 'Range cookers', 'Range-cooker brand of AGA Rangemaster, Leamington Spa, with a history traced to 1803 and John Flavel.', FAL,
   ['Elan Deluxe', 'Classic Deluxe', 'Nexus'], [], ['Falcon range cooker'], ['AGA', 'Rayburn']),
 b('La Cornue', 'France', '1908', 'Luxury range cookers', 'French maker of vaulted-oven ranges founded by Albert Dupuy; part of Middleby since 2015.', LC,
   ['Château', 'CornuFé', 'CornuChef'], ['Albert Dupuy, 1908', 'André Dupuy, 1950s', 'Xavier Dupuy, from 1985'], ['La Cornue Château', 'La Cornue CornuFé'], ['AGA']),
 b('Lacanche', 'France', '', 'Luxury range cookers', 'Range cookers made in Lacanche, Côte-d’Or, in Classique and Moderne lines from 27 to 86 inches wide.', LACL,
   ['Classique', 'Moderne'], [], ['Lacanche Sully', 'Lacanche Cluny']),
 b('Officine Gullo', 'Italy', '', 'Luxury cooking units', 'Florentine maker of made-to-order kitchens and cooking units founded by Carmelo Gullo.', OG,
   ['OG Professional', 'Fiorentina'], [], ['Officine Gullo OG Professional']),
 b('Wolf', 'United States', '', 'Premium cooking', 'Cooking-appliance brand of the Sub-Zero group since it bought Wolf Range Corporation’s domestic line in 2000.', SZ,
   ['Dual Fuel'], [], ['Wolf dual-fuel range'], ['Sub-Zero']),
 b('Sub-Zero', 'United States', '1945', 'Premium refrigeration', 'Madison, Wisconsin refrigeration maker founded by Westye F. Bakke; claims the first built-in refrigerators.', SZ,
   ['Designer Series'], [], ['Sub-Zero Designer Series', 'Sub-Zero 424'], ['Wolf']),
 b('Gaggenau', 'Germany', '1683', 'Premium built-in appliances', 'Black Forest ironworks turned high-end appliance maker; part of BSH since 1995.', GW,
   ['400 series', 'Vario'], ['Timothy Jacob Jensen, chief designer 1991–1998'], ['Gaggenau Vario 400 series', 'Gaggenau Vario cooling 400 series', 'Gaggenau EB 900'], ['Neff']),
 b('ESSE', 'United Kingdom', '1854', 'Range cookers and stoves', 'British cooker and stove maker founded by James Smith; hand-built at the Ouzledale foundry, Barnoldswick.', ESSE,
   ['Woodfired', 'Ironheart', 'Electric ESSE'], ['Ashby family, from 1985'], ['ESSE wood-burning range cooker', 'Electric ESSE']),
 b('Everhot', 'United Kingdom', '1979', 'Electric heat-storage range cookers', 'Range maker at Coaley Mill, Gloucestershire, founded on Ossie Goring’s trickle-feed electric cooker.', EVH,
   [], ['Ossie Goring, founder'], ['Everhot']),
 b('BORA', 'Germany', '2007', 'Cooktop extractors', 'Rosenheim company founded by Willi Bruckbauer, pioneer of the hob-mounted downdraft extractor.', BORA,
   ['Professional'], ['Willi Bruckbauer, founder'], ['BORA cooktop extractor']),
 b('Miele', 'Germany', '1899', 'Premium appliances', 'Gütersloh family firm making built-in ovens, steam ovens, hobs, cooling and coffee systems.', W + 'Miele',
   ['Gourmet warming drawers', 'CVA coffee machines'], ['Carl Miele and Reinhard Zinkann, founders'], [], ['Gaggenau']),
 b('Neff', 'Germany', '1877', 'Built-in kitchen appliances', 'Kitchen-appliance maker founded by Carl Andreas Neff in Bretten; owned by BSH since 1982.', W + 'Constructa-Neff',
   [], [], [], ['Bosch', 'Siemens', 'Gaggenau']),
 b('Liebherr', 'Germany', '1949', 'Refrigeration', 'German-Swiss group founded by Hans Liebherr that also makes domestic refrigerators.', W + 'Liebherr'),
 b('EuroCave', 'France', '1976', 'Wine cabinets', 'French maker of wine cabinets, including built-in ranges.', EC, ['Inspiration', 'Compact', 'Tête à Tête'], [], ['EuroCave Inspiration', 'EuroCave Compact']),
]
notes = ("Both old kinds kept (Oven -> Built-in oven, Hob) with their old sources and ranges. Eight new kinds added per plan. "
         "Tier brands for ovens/hobs: Which? reliability survey covers AEG, Beko, Bosch, Hotpoint, Miele, Neff, Samsung, Siemens, Zanussi among others, "
         "but winners are behind a paywall, so no test-winner models were named; no further oven/hob SKUs added. "
         "Left out (no retrieved confirmation): AGA eR3, Gaggenau 200 series and 400-series ovens, Miele MasterCool, Westin and Falmec hoods, "
         "Wolf hobs/ovens, Lacanche founding year, Officine Gullo founding year, Bosch/Siemens brand entries. "
         "Freestanding fridges and dishwashers stay in B5. No craft traditions apply to this shelf.")
out = {'kinds': kinds, 'brands': brands, 'traditions': [], 'notes': notes}
p = '/home/user/Possession-Taxonomy/rebuild/work/G3/shelves/00_01.json'
json.dump(out, open(p + '.tmp', 'w'), ensure_ascii=False, indent=1); os.replace(p + '.tmp', p)
print('kinds', len(kinds), 'archetypes', sum(len(k.get('x', [])) for k in kinds), 'brands', len(brands))
