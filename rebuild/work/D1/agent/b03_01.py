import json, os
W = 'https://en.wikipedia.org/wiki/'
WD = 'https://www.wikidata.org/wiki/'
def X(n, mk, y, s, d, v=(), a='', dt=''):
    x = {'n': n, 'a': a, 'd': d, 'mk': mk, 'y': y, 's': s if s.startswith('http') else W + s,
         'v': [dict(zip(('n', 'mk', 'y', 'd'), t)) for t in v]}
    if dt: x['dt'] = dt
    return x
LG, AP, MS, WA, HU, XP = 'Logitech', 'Apple', 'Microsoft', 'Wacom', 'Huion', 'XP-Pen'
mouse_x = [
 X('Apple mouse', AP, '1983', 'Apple_Mouse', 'Apple\'s line of mice, from the one-button Lisa and Macintosh mice to the touch-surface Magic Mouse.',
   [('Lisa Mouse', AP, '1983', 'shipped with the Lisa'), ('ADB Mouse', AP, '1986', 'Apple Desktop Bus'), ('Apple Pro Mouse', AP, '2000', 'first Apple optical mouse'),
    ('Mighty Mouse', AP, '2005', 'first multi-button Apple mouse, scroll ball'), ('Magic Mouse', AP, '2009', 'multi-touch top surface'), ('Magic Mouse 2', AP, '2015', '')],
   a='Macintosh mouse · Magic Mouse', dt='one button or touch surface · wired or wireless · white, black'),
 X('Microsoft IntelliMouse', MS, '1996', 'Microsoft_IntelliMouse', 'Microsoft mouse that popularised the scroll wheel; the Explorer shape remains a gaming favourite.',
   [('IntelliMouse', MS, '1996', 'ball mouse with scroll wheel'), ('IntelliMouse Explorer', MS, '1999', 'first optical Explorer shape'), ('IntelliMouse Optical', MS, '2000', 'ambidextrous'),
    ('IntelliMouse Explorer 3.0', MS, '2006', 're-release of the Explorer shape for gaming'), ('Classic IntelliMouse', MS, '2017', 'BlueTrack sensor'), ('Pro IntelliMouse', MS, '2019', '16,000 DPI gaming sensor')],
   a='IME 3.0', dt='right-handed Explorer shape or ambidextrous · ball, optical'),
 X('Logitech MX518', LG, '2005', 'https://meyerweb.com/eric/thoughts/2019/03/18/legend-of-the-stalwart-mouse/', 'Long-lived wired gaming mouse descended from the MX500 shape, reissued in 2019.',
   [('MX500', LG, '', 'original shape'), ('MX510', LG, '2004', 'predecessor'), ('MX518', LG, '2005', 'gaming-branded'), ('MX518 Legendary', LG, '2019', 'reissue, all black')]),
 X('Logitech G502', LG, '2014', 'https://pcworld.com/article/402764/logitech-g502-hero-mouse-review.html', 'Many-button wired gaming mouse, refreshed through several sensors.',
   [('G502 Proteus Core', LG, '2014', 'original'), ('G502 Proteus Spectrum', LG, '', 'RGB lighting'), ('G502 Hero', LG, '2018', 'Hero sensor, 50-million-click switches')]),
 X('Logitech MX Master', LG, '2015', WD + 'Q135917054', 'Large wireless productivity mouse with thumb scroll wheel, speed-adaptive main wheel and gesture button.',
   [('MX Master', LG, '2015', 'first model, Darkfield sensor'), ('MX Master 2S', LG, '2017', 'refinement'), ('MX Master 3S', LG, '2022', ''), ('MX Master 4', LG, '2025', '')],
   dt='graphite, pale grey, black · Bluetooth or receiver'),
 X('Razer DeathAdder', 'Razer', '2006', WD + 'Q64504097', 'Right-handed ergonomic gaming mouse, Razer\'s best-selling line.',
   [('DeathAdder 2013 Edition', 'Razer', '2013', ''), ('DeathAdder Elite', 'Razer', '', ''), ('DeathAdder V3 HyperSpeed', 'Razer', '2024', 'wireless')]),
 X('Zowie EC', 'Zowie', '', 'https://zowie.benq.com/en/news/2019/ec-series-with-large-mouse-feet.html', 'Right-handed ergonomic esports mouse, one of Zowie\'s oldest shapes, sold in several sizes.',
   [('EC-A', 'Zowie', '', 'classic feet'), ('EC-B', 'Zowie', '', '3360 sensor'), ('EC1 / EC2', 'Zowie', '2019', 'merged line, large feet, black')], dt='size 1 (large), 2 (medium)'),
 X('Logitech G Pro X Superlight', LG, '2021', 'https://www.red-dot.org/zh/project/logitech-g-pro-x-superlight-53210', 'Very light wireless esports mouse made with professional players, a reference light mouse.',
   [('G Pro X Superlight', LG, '', '63 g, HERO sensor, LIGHTSPEED wireless')]),
]
tb_x = [
 X('Logitech TrackMan', LG, '', 'Trackball', 'Logitech\'s trackball family, both thumb-operated and finger-operated.',
   [('Cordless TrackMan Wheel', LG, '', 'thumb ball'), ('TrackMan Marble Wheel', LG, '', ''), ('M570', LG, '', 'wireless thumb trackball'), ('MX Ergo', LG, '', 'tilting base'), ('MX Ergo S Plus', LG, '', 'current version')]),
 X('Kensington Expert Mouse', 'Kensington', '', 'https://www.kensington.com/news/ergonomic-workspace-blog/evolution-of-kensington-trackballs/', 'Large-ball finger trackball with a scroll ring, descended from the 1989 TurboMouse.',
   [('TurboMouse', 'Kensington', '1989', 'forerunner'), ('Expert Mouse', 'Kensington', '', 'large ball, scroll ring'), ('SlimBlade', 'Kensington', '', '')]),
 X('Elecom HUGE', 'Elecom', '', 'https://www.custompc.com/elecom-huge-trackball-m-ht1drbk-review', 'Very large finger-operated trackball with a 52 mm ball and padded palm rest.',
   [('M-HT1DRBK', 'Elecom', '', 'wireless')]),
]
pen_x = [
 X('Wacom Intuos', WA, '1998', 'https://community.wacom.com/en-us/?p=811242', 'Wacom\'s screenless pen tablet line, the standard for digital drawing.',
   [('Intuos', WA, '1998', 'first generation'), ('Intuos Pro', WA, '', 'professional line'), ('Bamboo', WA, '2007', 'beginners\' tablet')], dt='small, medium, large · wired or Bluetooth'),
 X('Wacom Cintiq', WA, '2001', 'https://community.wacom.com/en-us/?p=811242', 'Wacom\'s pen display line, for drawing directly on the screen.',
   [('Cintiq', WA, '2001', 'first Cintiq'), ('Cintiq Pro 13 / 16', WA, '2016', 'Pro Pen 2'), ('Cintiq 16', WA, '', ''), ('Cintiq 24', WA, '', ''), ('Cintiq Pro 17', WA, '', ''), ('Cintiq Pro 22', WA, '', ''), ('Cintiq Pro 27', WA, '', '')],
   dt='13–32 in · HD to 4K'),
 X('Wacom One', WA, '2020', 'Wacom', 'Entry-level Wacom pen display and pen tablet range.',
   [('Wacom One', WA, '2020', 'pen display'), ('Wacom One 14', WA, '', ''), ('Wacom One pen tablet', WA, '', '')]),
 X('Wacom Movink', WA, '2024', 'Wacom', 'Thin portable OLED pen display.', [('Movink 13', WA, '2024', '')]),
 X('Huion Kamvas', HU, '', 'HUION', 'Huion\'s pen display line, a cheaper rival to Cintiq.',
   [('Kamvas Pro 22', HU, '2019', ''), ('Kamvas 16', HU, '2021', ''), ('Kamvas Pro 24', HU, '2021', ''), ('Kamvas Pro 19 / Pro 27', HU, '2023', ''), ('Kamvas Pro 24 (Gen 3)', HU, '2025', ''), ('Kamvas 22 (Gen 3)', HU, '2026', '')]),
 X('XP-Pen Artist', XP, '2015', 'XP-PEN', 'XP-Pen\'s pen display line, alongside the screenless Deco tablets.',
   [('Artist 22HD', XP, '2015', ''), ('Artist 16', XP, '2016', ''), ('Artist 24', XP, '2021', ''), ('Artist 16 (2nd Gen)', XP, '2022', ''), ('Artist 22 Plus', XP, '2023', '')]),
]
pad_x = [
 X('SteelSeries QcK', 'SteelSeries', '', 'https://steelseries.com/blog/history-steelseries-mousepads-457', 'Micro-woven cloth pad on natural rubber, a long-standing reference gaming pad.',
   [('Icemat', 'SteelSeries', '', 'SteelSeries\' first pad, forerunner'), ('QcK', 'SteelSeries', '', 'cloth and rubber')], dt='sizes small to XXL desk mat · thickness'),
]
kinds = [
 {'n': 'Mouse', 'a': 'computer mouse · gaming mouse · vertical mouse', 'd': 'Hand-held pointing device moved over a surface.',
  't': ['wired', 'wireless', 'gaming', 'ergonomic / vertical', 'travel / compact', 'silent'], 's': 'https://pcpartpicker.com/products/mouse/', 'x': mouse_x,
  'm': [['Logitech MX Anywhere 3S', LG], ['Logitech MX Vertical', LG], ['Logitech Lift', LG], ['Logitech M720 Triathlon', LG], ['Logitech M705 Marathon', LG], ['Logitech Signature M650', LG],
        ['Logitech Pebble Mouse 2 M350s', LG], ['Microsoft Surface Arc Mouse', MS], ['Kensington Pro Fit', 'Kensington'], ['Dell MS3320W', 'Dell'], ['HP Desktop 320M', 'HP'], ['Logitech M100', LG]]},
 {'n': 'Trackball', 'a': 'trackball mouse', 'd': 'Pointing device operated by turning a ball held in a fixed base.',
  't': ['thumb-operated', 'finger-operated', 'wired', 'wireless'], 's': 'https://pcpartpicker.com/products/mouse/', 'x': tb_x},
 {'n': 'Pen tablet', 'a': 'graphics tablet · drawing tablet · pen display', 'd': 'Drawing tablet used with a pen, with or without a built-in screen (a pen display is a pen tablet with a screen).',
  't': ['pen tablet (no screen)', 'pen display'], 's': 'https://wacom.com/en-my/products/pen-tablets', 'x': pen_x,
  'm': [['Huion Inspiroy 2', HU], ['Huion Inspiroy Keydial', HU], ['Huion Kamvas 13 (Gen 3)', HU]]},
 {'n': 'Mouse pad or desk mat', 'a': 'mousepad · desk mat', 'd': 'Pad or mat made for moving a mouse on, from a mouse-sized pad to a desk mat under keyboard and mouse.',
  't': ['cloth', 'hybrid', 'hard / glass', 'desk mat (XL)'], 's': 'https://www.lambda-tek.com/Steelseries-63004-shUS/B253182?viewSpec=y', 'x': pad_x,
  'm': [['MM350 PRO', 'Corsair']]},
]
K = 'knowledge'
def B(n, c, f, seg, kf, d, s=K, **kw):
    b = {'n': n, 'c': c, 'f': f, 'seg': seg, 'kf': kf, 'd': d, 's': s}; b.update(kw); return b
brands = [
 B(LG, 'Switzerland', '1981', 'Mainstream', 'mice, keyboards', 'Swiss-American maker of mice, keyboards and other peripherals.', W + 'Logitech', lines=['MX', 'G', 'Pebble', 'Signature'], sig=['Logitech MX Master', 'Logitech G502', 'Logitech MX518', 'Logitech TrackMan']),
 B(AP, 'United States', '1976', 'Premium', 'Mac, iPhone', 'American maker of the Macintosh and its mice and keyboards.', sig=['Apple mouse']),
 B(MS, 'United States', '1975', 'Premium', 'software, Surface', 'American software company that also made influential mice and keyboards.', sig=['Microsoft IntelliMouse']),
 B('Razer', 'United States', '', 'Premium', 'gaming peripherals', 'Singapore-American gaming peripheral and laptop brand.', sig=['Razer DeathAdder']),
 B('Zowie', 'Taiwan', '', 'Specialist', 'esports mice', 'Esports mouse and monitor brand of BenQ.', 'https://zowie.benq.com/en/news/2019/ec-series-with-large-mouse-feet.html', sig=['Zowie EC'], rel=['BenQ']),
 B('Kensington', 'United States', '', 'Mainstream', 'trackballs, locks', 'American maker of computer accessories and trackballs.', 'https://www.kensington.com/news/ergonomic-workspace-blog/evolution-of-kensington-trackballs/', sig=['Kensington Expert Mouse']),
 B('Elecom', 'Japan', '', 'Mainstream', 'PC accessories', 'Japanese maker of computer accessories, including large trackballs.', sig=['Elecom HUGE']),
 B(WA, 'Japan', '1983', 'Professional & flagship', 'pen tablets', 'Japanese maker of pen tablets and pen displays.', W + 'Wacom', lines=['Intuos', 'Cintiq', 'Wacom One', 'Movink'], sig=['Wacom Intuos', 'Wacom Cintiq']),
 B(HU, 'China', '2011', 'Value', 'pen displays', 'Shenzhen maker of pen tablets and pen displays, founded by Henry Xu.', W + 'HUION', lines=['Kamvas', 'Inspiroy'], sig=['Huion Kamvas']),
 B(XP, 'China', '2005', 'Value', 'pen displays', 'Pen tablet and pen display brand of the Shenzhen Hanvon Ugee group.', W + 'XP-PEN', lines=['Artist', 'Deco'], sig=['XP-Pen Artist']),
 B('SteelSeries', 'Denmark', '', 'Premium', 'gaming peripherals', 'Danish gaming peripheral maker that began with a mouse pad.', 'https://steelseries.com/blog/history-steelseries-mousepads-457', sig=['SteelSeries QcK']),
]
out = {'kinds': kinds, 'brands': brands, 'traditions': [],
 'notes': 'Mouse: 25 old SKUs cut to 12 models plus 8 archetypes (Apple mouse, IntelliMouse, MX518, G502, MX Master, DeathAdder, Zowie EC, G Pro X Superlight); dropped low-end duplicates (M196, M220, M240, M310, M325s, Mobi Fold, Lenovo Essential, Dell Pro 7, G305 X Superlight). Zowie FK, G Pro Wireless (2018) and Superlight 2 not added (no fetched page with versions). Trackball: Elecom HUGE, Kensington Expert Mouse, Logitech TrackMan added; Kensington SlimBlade year unconfirmed. Pen tablet: old Wacom/Huion SKUs folded into Intuos, Cintiq, Wacom One, Movink, Kamvas, XP-Pen Artist archetypes; minor Huion Inspiroy SKUs (Dial 2, Frego, Giano, Kamvas 12, 22 Plus, 24 Plus, Pro 16 V2) dropped. Mouse pads: Artisan and Logitech G640 not added (no page fetched); QcK archetype added.'}
p = '/home/user/Possession-Taxonomy/rebuild/work/D1/shelves/03_01.json'
json.dump(out, open(p + '.tmp', 'w'), ensure_ascii=False, indent=1); os.replace(p + '.tmp', p)
print('written')
