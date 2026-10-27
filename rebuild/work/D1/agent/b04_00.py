import json, os
W = 'https://en.wikipedia.org/wiki/'
DT = 'https://deskthority.net/wiki/'
def X(n, mk, y, s, d, v=(), a='', dt=''):
    x = {'n': n, 'a': a, 'd': d, 'mk': mk, 'y': y, 's': s if s.startswith('http') else W + s,
         'v': [dict(zip(('n', 'mk', 'y', 'd'), t)) for t in v]}
    if dt: x['dt'] = dt
    return x
LG, MS = 'Logitech', 'Microsoft'
kb_x = [
 X('IBM Model F', 'IBM', '1981', 'Model_F_keyboard', 'IBM\'s original buckling-spring capacitive keyboard, shipped with the first IBM PC.',
   [('Model F XT', 'IBM', '1981', 'IBM PC keyboard'), ('Model F AT', 'IBM', '1984', 'IBM PC AT keyboard'), ('Model F 122-key', 'IBM', '', 'terminal keyboard'),
    ('Model F Labs reproduction', 'Model F Labs', '2019', 'new-made keyboards with the original mechanism, shipping from 2019')], dt='XT, AT, terminal layouts'),
 X('IBM Model M', 'IBM', '1985', 'Model_M_keyboard', 'Buckling-spring keyboard that set the 101-key layout; still made by Unicomp.',
   [('Model M Enhanced 101 (1391401)', 'IBM', '1986', 'most common variant'), ('Space Saving Keyboard (SSK)', 'IBM', '', '84 keys, no number pad'),
    ('M13', 'Lexmark', '', 'with TrackPoint II'), ('New Model M', 'Unicomp', '2020', 'new tooling'), ('Mini-M', 'Unicomp', '2020', '87 keys'), ('Ultra Classic', 'Unicomp', '', 'compact case')],
   a='buckling spring', dt='makers IBM, Lexmark, Maxi Switch, Unicomp · 101/104 keys or SSK'),
 X('Apple Extended Keyboard', 'Apple', '1987', 'Apple_Extended_Keyboard', 'Full-size Apple Desktop Bus keyboard with Alps mechanical switches, prized by collectors.',
   [('Apple Extended Keyboard (M0115)', 'Apple', '1987', ''), ('Apple Extended Keyboard II (M3501)', 'Apple', '1990', '')]),
 X('Cherry G80-3000', 'Cherry', '1988', DT + 'Cherry_G80-3000', 'Full-size Cherry MX keyboard made in many revisions since 1988.',
   [('G80-3000', 'Cherry', '1988', ''), ('G80-3494', 'Cherry', '', 'black, MX-Board branding'), ('G80-3600', 'Cherry', '', '6KRO'), ('G80-3060', 'Cherry', '', '60th-anniversary edition')]),
 X('Happy Hacking Keyboard', 'PFU', '1996', 'Happy_Hacking_Keyboard', 'Compact keyboard built with Topre switches from the Professional onward.',
   [('Happy Hacking Keyboard', 'PFU', '1996', 'original'), ('HHKB Lite', 'PFU', '1999', 'membrane'), ('HHKB Professional', 'PFU', '2003', 'Topre'),
    ('HHKB Professional 2', 'PFU', '2006', ''), ('HHKB Professional 2 Type-S', 'PFU', '2011', 'silenced'), ('HHKB Professional Hybrid / Hybrid Type-S', 'PFU', '2019', '')],
   a='HHKB', dt='black or white · blank or printed keycaps'),
 X('Topre Realforce', 'Topre', '2001', DT + 'Topre_Realforce', 'Japanese Topre electrostatic-capacitive keyboard line.',
   [('Realforce 106', 'Topre', '2001', 'first Realforce, JIS'), ('Realforce 87U', 'Topre', '2009', ''), ('Realforce 104U', 'Topre', '2010', ''), ('Realforce 88UB', 'Topre', '2011', 'ISO'), ('Realforce R2', 'Topre', '2017', '')],
   dt='uniform or variable weighting · full size or tenkeyless'),
 X('Das Keyboard', 'Metadot', '2005', DT + 'Das_Keyboard', 'Keyboard first sold with blank keycaps, later mechanical with Cherry MX switches.',
   [('Das Keyboard', 'Metadot', '2005', 'blank keycaps'), ('Das Keyboard Professional', 'Metadot', '2008', 'first with printed legends'), ('Das Keyboard Model S', 'Metadot', '', ''), ('Das Keyboard 4 Professional', 'Metadot', '2014', '')]),
 X('Filco Majestouch', 'Diatec', '', DT + 'Filco_Majestouch', 'Plain, sturdy Japanese Cherry MX keyboard made by Costar for Diatec.',
   [('Majestouch (MJ1)', 'Diatec', '', ''), ('Majestouch 2 (MJ2)', 'Diatec', '', ''), ('Majestouch 2 Convertible', 'Diatec', '', 'USB, PS/2 and Bluetooth'), ('Majestouch Minila', 'Diatec', '', '67–68 keys')]),
 X('Razer BlackWidow', 'Razer', '2010', DT + 'Razer_BlackWidow', 'Razer\'s mechanical gaming keyboard line.',
   [('BlackWidow', 'Razer', '2010', 'Cherry MX'), ('BlackWidow Ultimate', 'Razer', '2010', 'backlit'), ('BlackWidow Chroma', 'Razer', '2014', 'Razer switches, RGB'), ('BlackWidow Chroma V2', 'Razer', '2017', '')]),
 X('Corsair K70', 'Corsair', '2013', 'https://www.vortez.net/articles_pages/corsair_vengeance_k70_review,1.html', 'Aluminium-framed mechanical gaming keyboard with per-key backlighting.',
   [('Vengeance K70', 'Corsair', '2013', 'Cherry MX Red, brushed aluminium')]),
 X('Apple Magic Keyboard', 'Apple', '2015', 'Magic_Keyboard', 'Apple\'s slim wireless keyboard for Mac.', [('Magic Keyboard', 'Apple', '2015', '')]),
 X('Keychron K series', 'Keychron', '2018', DT + 'Keychron', 'Affordable mechanical keyboards, the first Keychron line.',
   [('K1 (Keytron)', 'Keychron', '2018', ''), ('K2', 'Keychron', '2019', ''), ('K6', 'Keychron', '2020', '')]),
 X('Wooting analog keyboard', 'Wooting', '2017', DT + 'Wooting_One', 'Keyboard with analog (depth-sensing) switches, later Hall-effect.',
   [('Wooting One', 'Wooting', '2017', 'Flaretech optical switches'), ('Wooting Two', 'Wooting', '2018', 'full size')]),
]
split_x = [
 X('Microsoft Natural keyboard', MS, '1994', 'Microsoft_Natural_keyboard', 'Fixed-split, tented keyboard that brought ergonomic layouts to the mass market.',
   [('Natural Keyboard', MS, '1994', ''), ('Natural Keyboard Elite', MS, '1998', ''), ('Natural Keyboard Pro', MS, '1999', ''), ('Natural Ergonomic Keyboard 4000', MS, '2005', ''),
    ('Sculpt Ergonomic Keyboard', MS, '2013', 'scissor switches, split space bar'), ('Surface Ergonomic Keyboard', MS, '2016', 'Bluetooth')]),
 X('Kinesis Advantage', 'Kinesis', '1992', 'Kinesis_(keyboard)', 'Contoured keyboard with key wells and thumb clusters.',
   [('Model 100', 'Kinesis', '1992', 'original'), ('Advantage (USB)', 'Kinesis', '2002', ''), ('Advantage2', 'Kinesis', '2016', ''), ('Advantage360', 'Kinesis', '2021', 'split halves')]),
 X('Kinesis Freestyle', 'Kinesis', '2007', 'Kinesis_(keyboard)', 'Flat split keyboard whose halves are joined by a cable.',
   [('Freestyle', 'Kinesis', '2007', ''), ('Freestyle2', 'Kinesis', '2012', ''), ('Freestyle Edge', 'Kinesis', '2017', 'gaming'), ('Freestyle Pro', 'Kinesis', '2018', '')]),
 X('ErgoDox', '', '2012', DT + 'ErgoDox', 'Open-source split columnar keyboard with thumb clusters.',
   [('ErgoDox', '', '2012', 'open design'), ('ErgoDox EZ', 'ZSA', '', 'assembled'), ('Infinity ErgoDox', '', '', 'backlit, LCD')]),
 X('ZSA Moonlander', 'ZSA', '', 'https://www.pcgamer.com/zsa-moonlander-review/', 'Split columnar keyboard from the makers of the ErgoDox EZ.', [('Moonlander', 'ZSA', '', '')]),
 X('Corne', '', '2018', DT + 'Corne', 'Open-source 42-key split columnar kit with three thumb keys per half.',
   [('Corne Classic', '', '', ''), ('Corne Cherry', '', '', 'MX hot-swap'), ('Corne Chocolate', '', '', 'Kailh Choc'), ('Corne Light', '', '', '')], a='crkbd'),
]
kit_x = [
 X('Glorious GMMK Pro', 'Glorious', '', 'https://switchandclick.com/gmmk-pro/', 'Gasket-mounted 75% aluminium kit that brought custom-style boards to the mainstream.', [('GMMK Pro', 'Glorious', '', '75% barebone')]),
 X('Keychron Q series', 'Keychron', '2021', 'https://www.inverse.com/input/reviews/keychron-q1-review-customizable-mechanical-keyboard-everyone-can-love', 'Aluminium gasket-mount QMK boards, sold barebones or assembled.',
   [('Q1', 'Keychron', '2021', '75%, first QMK board'), ('Q1 V2', 'Keychron', '', ''), ('Q3 HE', 'Keychron', '', ''), ('Q4', 'Keychron', '', ''), ('Q5 HE', 'Keychron', '', ''), ('Q8', 'Keychron', '', '')]),
 X('Keycult No. 1', 'Keycult', '', 'https://milktooth.com/catalog/item/keycult-no-1-rev-1-0439', 'High-end group-buy custom keyboard.', [('No. 1 Rev. 1', 'Keycult', '', '80% / TKL')]),
 X('TGR Jane', 'TGR Keyboards', '', 'https://milktooth.com/catalog/item/tgr-keyboards-designer-yuktsi-jane-v1-5-0784', 'Sought-after group-buy custom keyboard.', [('Jane v1.5', 'TGR Keyboards', '', '65%')]),
]
macro_x = [
 X('Elgato Stream Deck', 'Elgato', '2017', 'Elgato', 'Pad of LCD keys for shortcuts and streaming control.',
   [('Stream Deck', 'Elgato', '2017', '15 keys'), ('Stream Deck Mini', 'Elgato', '2018', '6 keys'), ('Stream Deck XL', 'Elgato', '2019', '32 keys'), ('Stream Deck Mk.2', 'Elgato', '2021', ''), ('Stream Deck Neo', 'Elgato', '2024', '8 keys')]),
]
kinds = [
 {'n': 'Keyboard', 'a': 'mechanical keyboard · computer keyboard', 'd': 'Key-based input device sold ready to type.',
  't': ['full size', 'tenkeyless (80%)', '75%', '65%', '60%', 'mechanical', 'Topre (electrostatic capacitive)', 'buckling spring', 'Hall-effect / analog', 'membrane / scissor', 'wired', 'wireless'],
  's': 'https://pcpartpicker.com/products/keyboard/', 'x': kb_x,
  'm': [['Logitech MX Keys S', LG], ['Logitech MX Keys Mini', LG], ['Logitech MX Mechanical', LG], ['Logitech K780', LG], ['Logitech Pebble Keys 2 K380s', LG], ['Logitech POP Keys', LG], ['Logitech Signature K650', LG], ['Logitech K250', LG]]},
 {'n': 'Split & ergonomic keyboard', 'a': 'ergonomic keyboard · split keyboard · ortholinear', 'd': 'Keyboard shaped to keep wrists straight: split, tented, contoured, columnar or ortholinear.',
  't': ['fixed split', 'fully split', 'contoured / key-well', 'columnar', 'ortholinear'], 's': 'https://en.wikipedia.org/wiki/Microsoft_Natural_keyboard', 'x': split_x,
  'm': [['Logitech ERGO K860', LG], ['Logitech Wave Keys', LG]]},
 {'n': 'Keyboard kit', 'a': 'barebones keyboard · custom keyboard kit', 'd': 'Case, plate and circuit board sold to be built into a keyboard with chosen switches and keycaps.',
  't': ['gasket mount', 'tray mount', 'top mount', 'hot-swap', 'solder', 'aluminium', 'plastic'], 's': 'https://www.ozokeyboards.com/nl/collections/60-diy-kits', 'x': kit_x,
  'm': [['Meletrix Zoom65 V3', 'Meletrix'], ['Meletrix Zoom75', 'Meletrix'], ['Qwertykeys Neo65', 'Qwertykeys'], ['Chilkey ND75', 'Chilkey'], ['Monsgeek M1', 'Monsgeek'],
        ['Wuque Studio x Whatever Studio Paper80', 'Wuque Studio'], ['Glorious GMMK 2', 'Glorious'], ['Zuoya GMK87', 'Zuoya']]},
 {'n': 'Numeric keypad', 'a': 'numpad', 'd': 'Separate input device with number keys.', 's': 'https://www.bhphotovideo.com/c/product/649580-REG/Targus_AKP11US_Wireless_Numeric_Keypad.html',
  't': ['wired', 'wireless'], 'm': [['Logitech MX Keypad', LG], ['Targus AKP10 Numeric Keypad', 'Targus'], ['Targus AKP11 Wireless Numeric Keypad', 'Targus']]},
 {'n': 'Macro pad', 'a': 'stream deck · shortcut pad', 'd': 'Separate input device of a few programmable keys, dials or sliders used for shortcuts, not for typing.',
  's': 'https://secure.logitech.com/en-ca/shop/c/logi-keyboards', 'x': macro_x, 'm': [['MX Creative Console', LG]]},
]
K = 'knowledge'
def B(n, c, f, seg, kf, d, s=K, **kw):
    b = {'n': n, 'c': c, 'f': f, 'seg': seg, 'kf': kf, 'd': d, 's': s}; b.update(kw); return b
brands = [
 B('IBM', 'United States', '1911', 'Professional & flagship', 'Model F, Model M', 'American computer company whose Model F and Model M keyboards defined the PC keyboard.', sig=['IBM Model F', 'IBM Model M']),
 B('Model F Labs', 'United States', '', 'Artisan & independent', 'Model F reproductions', 'Small maker of new keyboards using the Model F mechanism.', W + 'Model_F_keyboard'),
 B('Lexmark', 'United States', '1991', 'Mainstream', 'printers', 'IBM spin-off that made Model M keyboards from 1991 to 1996.', W + 'Model_M_keyboard'),
 B('Unicomp', 'United States', '1996', 'Heritage manufactory', 'buckling spring', 'Maker that has continued the Model M buckling-spring keyboard since 1996.', W + 'Model_M_keyboard', lines=['New Model M', 'Mini-M', 'Ultra Classic']),
 B('Apple', 'United States', '1976', 'Premium', 'Mac, iPhone', 'American maker of the Macintosh and its keyboards.', sig=['Apple Extended Keyboard', 'Apple Magic Keyboard']),
 B('Cherry', 'Germany', '1953', 'Heritage manufactory', 'MX switches', 'German maker of MX key switches and keyboards.', W + 'Cherry_(company)', sig=['Cherry G80-3000']),
 B('PFU', 'Japan', '', 'Specialist', 'HHKB', 'Japanese Fujitsu-group company that makes the Happy Hacking Keyboard.', W + 'Happy_Hacking_Keyboard', sig=['Happy Hacking Keyboard']),
 B('Topre', 'Japan', '', 'Premium', 'capacitive switches', 'Japanese industrial firm that makes Topre switches and Realforce keyboards.', W + 'Topre_Corporation', sig=['Topre Realforce']),
 B('Metadot', 'United States', '', 'Specialist', 'Das Keyboard', 'Texas company behind Das Keyboard.', DT + 'Das_Keyboard', sig=['Das Keyboard']),
 B('Diatec', 'Japan', '', 'Specialist', 'Filco keyboards', 'Japanese company that sells Filco Majestouch keyboards.', DT + 'Filco_Majestouch', sig=['Filco Majestouch']),
 B('Razer', 'United States', '', 'Premium', 'gaming peripherals', 'Singapore-American gaming peripheral and laptop brand.', sig=['Razer BlackWidow']),
 B('Corsair', 'United States', '1994', 'Premium', 'gaming PC parts', 'American maker of gaming peripherals and PC components.', sig=['Corsair K70']),
 B('Keychron', '', '2018', 'Value', 'wireless mechanical', 'Keyboard brand that began with a 2018 Kickstarter.', DT + 'Keychron', lines=['K', 'Q'], sig=['Keychron K series', 'Keychron Q series']),
 B('Wooting', 'Netherlands', '', 'Specialist', 'analog keyboards', 'Dutch maker of analog and Hall-effect keyboards.', DT + 'Wooting_One', sig=['Wooting analog keyboard']),
 B(LG, 'Switzerland', '1981', 'Mainstream', 'mice, keyboards', 'Swiss-American maker of mice, keyboards and other peripherals.', W + 'Logitech', lines=['MX', 'Pebble', 'POP', 'Signature']),
 B(MS, 'United States', '1975', 'Premium', 'software, Surface', 'American software company that made influential ergonomic keyboards.', sig=['Microsoft Natural keyboard']),
 B('Kinesis', 'United States', '1991', 'Specialist', 'ergonomic keyboards', 'Washington State maker of contoured and split ergonomic keyboards.', W + 'Kinesis_(keyboard)', sig=['Kinesis Advantage', 'Kinesis Freestyle']),
 B('ZSA', 'Canada', '', 'Specialist', 'split keyboards', 'Maker of the ErgoDox EZ and Moonlander split keyboards.', 'https://www.pcgamer.com/zsa-moonlander-review/', sig=['ZSA Moonlander']),
 B('Glorious', 'United States', '', 'Value', 'gaming peripherals', 'Gaming peripheral brand whose GMMK Pro popularised keyboard kits.', 'https://switchandclick.com/gmmk-pro/', sig=['Glorious GMMK Pro']),
 B('Keycult', '', '', 'Artisan & independent', 'custom keyboards', 'Small maker of high-end custom keyboards.', 'https://milktooth.com/catalog/item/keycult-no-1-rev-1-0439', sig=['Keycult No. 1']),
 B('TGR Keyboards', '', '', 'Artisan & independent', 'custom keyboards', 'Maker of the Jane custom keyboard.', 'https://milktooth.com/catalog/item/tgr-keyboards-designer-yuktsi-jane-v1-5-0784', sig=['TGR Jane']),
 B('Elgato', 'Germany', '', 'Specialist', 'streaming gear', 'Streaming and capture brand known for the Stream Deck.', W + 'Elgato', sig=['Elgato Stream Deck']),
]
out = {'kinds': kinds, 'brands': brands, 'traditions': [],
 'notes': 'Keyboard: 15 old Logitech-only models cut to 8 (Logitech ERGO K860 and Wave Keys moved to the new Split & ergonomic kind; Alto Keys, POP Icon Keys, Keys-To-Go 2, Signature Slim Solar+ dropped as duplicates); 13 archetypes added from Model F to Wooting. Not added (no page fetched): Ducky One, Leopold, Logitech MX Keys as archetype, Mode Sonnet, Wuque as archetype, Keychron Q kits beyond Q1 dates. Keyboard kit: 23 old models cut to 8 plus 4 archetypes (GMMK Pro, Keychron Q series absorbing the Q models, Keycult No. 1, TGR Jane); dropped Fantech, Leobog, Modokey, Niuniu, Yunzii, Zuoya GMK67S, Meletrix Zoom98, Qwertykeys QK75N. Moonlander year not on the fetched page, left blank. Numeric keypad and Macro pad kept; Stream Deck archetype added.'}
p = '/home/user/Possession-Taxonomy/rebuild/work/D1/shelves/04_00.json'
json.dump(out, open(p + '.tmp', 'w'), ensure_ascii=False, indent=1); os.replace(p + '.tmp', p)
print('written')
