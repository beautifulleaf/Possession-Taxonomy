import json, os
W = 'https://en.wikipedia.org/wiki/'
PA = 'https://www.penaddict.com/blog/'
GS = 'https://www.gentlemanstationer.com/blog/'
UNI = 'Mitsubishi Pencil (Uni)'
MPG = GS + '2017/1/7/guide-to-multifunction-pens-picking-the-best-multipen-for-your-needs'


def X(n, d, mk, y, s, v=(), a='', dt=''):
    o = {'n': n, 'a': a, 'd': d, 'mk': mk, 'y': y, 's': s, 'v': [dict(zip(('n', 'mk', 'y', 'd'), t)) for t in v]}
    if dt: o['dt'] = dt
    return o


ball = {'n': 'Ballpoint pen', 'a': 'biro · ボールペン · hybrid ink pen',
 'd': 'Pen that rolls thick oil-based ink onto paper through a ball tip; includes low-viscosity hybrid-ink pens.',
 't': ['stick (capped)', 'retractable', 'low-viscosity hybrid ink', 'pressurised refill', 'digital pen that records the writing'],
 's': W + 'Ballpoint_pen',
 'x': [
  X('Bic Cristal', 'Hexagonal clear-barrel stick ballpoint; the world\'s best-selling pen and a MoMA design object.', 'Bic', '1950', W + 'Bic_Cristal',
    [('Cristal (original)', 'Bic', '1950', 'launched December 1950; tungsten-carbide ball from 1961; vented cap from 1991'),
     ('Bic Orange', 'Bic', '1961', 'fine-point sister pen'),
     ('Bic 4 Colours', 'Bic', '1970', 'four-colour retractable'),
     ('Cristal for Her', 'Bic', '2012', 'widely mocked; in the Museum of Failure'),
     ('Cristal Stylus', 'Bic', '2014', 'touchscreen stylus end'),
     ('Cristal UP', 'Bic', '', '')],
    a='Bic Biro', dt='point sizes · 18 ink colours · clear barrel shows ink level'),
  X('Parker Jotter', 'Slim click ballpoint with an arrow clip and stainless cap; Parker\'s first ballpoint, over 750 million sold.', 'Parker', '1954', W + 'Parker_Jotter',
    [('Original Jotter', 'Parker', '1954', 'grooved nylon barrel, V clip'),
     ('Laboratory Jotter', 'Parker', 'c. 1955', 'all stainless steel'),
     ('T-Ball refill', 'Parker', '1957', 'textured tungsten-carbide ball'),
     ('Arrow-clip Jotter', 'Parker', '1958', 'arrow clip used since'),
     ('Jotter core and premium', 'Parker', '2016', 'metal barrels named after London Underground stations'),
     ('Jotter XL', 'Parker', '2017', 'about 7% larger')],
    dt='over 100 barrel colours · plastic, stainless, metal · ballpoint or gel refill'),
  X('Fisher Space Pen', 'Ballpoint with a pressurised, nitrogen-charged refill that writes upside down, in zero gravity and in the cold; flown on Apollo.', 'Fisher Space Pen', '1965', W + 'Fisher_Space_Pen',
    [('AG7 Anti-Gravity Pen', 'Fisher Space Pen', '1965', 'patented by Paul C. Fisher; bought by NASA 1967'),
     ('Bullet Space Pen (400)', 'Fisher Space Pen', '', 'compact brass capped pen; 50th-anniversary 400B'),
     ('Millennium', 'Fisher Space Pen', '', 'lifetime-ink model'),
     ('PR pressurised refill', 'Fisher Space Pen', '', 'also sold to fit Cross and Parker-type pens')],
    a='AG7 · Bullet', dt='brass, chrome, black, gold finishes · clip optional'),
  X('Cross Century', 'Slim tapered metal twist ballpoint, the classic Cross gift pen.', 'Cross', '1953', 'https://penhero.com/PenGallery/Cross/Cross150thLE.htm',
    [('Century pencil', 'Cross', '1946', 'established the Cross look'),
     ('Century ballpoint', 'Cross', '1953', 'still in production as Classic Century')],
    a='Classic Century', dt='chrome, gold-filled, sterling, lacquer finishes · twist mechanism'),
  X('Lamy 2000 ballpoint', 'Ballpoint version of Gerd A. Müller\'s 1966 Bauhaus-style Makrolon and steel design.', 'Lamy', '1966', W + 'Lamy_2000',
    [('2000 ballpoint', 'Lamy', '', 'Makrolon'), ('2000 stainless steel', 'Lamy', '2013', 'all-steel version of the line')],
    dt='brushed Makrolon or steel'),
  X('Uni Jetstream', 'Click ballpoint with low-viscosity hybrid ink that set the modern smooth-ballpoint category.', UNI, '2006', 'https://unsharpen.com/pen/uni-jetstream-ballpoint-pen/',
    [('Jetstream Standard', UNI, '', 'SXR-5 / SXR-7 refills'),
     ('Jetstream Edge', UNI, '', 'ultra-fine 0.28/0.38 mm'),
     ('Jetstream Lite Touch Ink', UNI, '', 'lower-friction ink'),
     ('Jetstream Prime', UNI, '', 'metal premium body'),
     ('Jetstream Sport', UNI, '', '')],
    dt='0.38, 0.5, 0.7, 1.0 mm · black, blue, red'),
  X('Pilot Acroball', 'Pilot\'s low-viscosity oil-ink click ballpoint, the main rival to the Jetstream.', 'Pilot', '', PA + '2009/6/9/review-pilot-acroball-07mm.html',
    [('Acroball', 'Pilot', '', 'Japan first'), ('Easy Touch Pro', 'Pilot', '', 'US-market version')],
    dt='0.5, 0.7 mm · textured grip'),
  X('Zebra F-301', 'Inexpensive stainless-steel-barrel click ballpoint.', 'Zebra', '', PA + '2010/12/15/review-zebra-f-301-07mm-ballpoint.html',
    [('F-301', 'Zebra', '', '0.7 mm'), ('F-301 XL', 'Zebra', '', 'larger barrel')], dt='stainless barrel · plastic grip colours'),
 ],
 'm': [['Uni Power Tank', UNI], ['Uni Boxy 100', UNI], ['Pentel Calme', 'Pentel'], ['Monami 153', 'Monami'], ['OHTO GS01', 'OHTO'],
       ['Kaweco Lunar Sport ballpoint', 'Kaweco'], ['TWSBI Precision', 'TWSBI'], ['Penco Perfection Bullet', 'Penco'],
       ['Leuchtturm1917 Drehgriffel', 'Leuchtturm1917'], ['TRAVELER\'S COMPANY BRASS', 'TRAVELER\'S COMPANY'], ['Schon DSGN Machined Pen V2', 'Schon DSGN']]}

gel = {'n': 'Gel pen', 'a': 'gel ink pen · gel rollerball',
 'd': 'Ball-tip pen with water-based gel ink; erasable thermochromic gel pens included.',
 't': ['capped', 'retractable', 'needle tip', 'erasable (thermochromic)', 'pigment / archival ink', 'metallic and pastel inks'],
 's': W + 'Gel_pen',
 'x': [
  X('Sakura Ball Sign / Gelly Roll', 'The first gel-ink pens, from the inventor of gel ink.', 'Sakura', '1984', W + 'Gel_pen',
    [('Ball Sign 280', 'Sakura', '1984', 'first gel pen, Japan'), ('Gelly Roll', 'Sakura', 'late 1980s', 'US market')]),
  X('Pilot G2', 'Click gel pen with a rubber grip and the widely copied G2-size refill; a US best seller.', 'Pilot', '', 'https://unsharpen.com/refill/pilot-g2-gel-pen-refill/',
    [('G2 0.38', 'Pilot', '', 'ultra fine'), ('G2 0.5', 'Pilot', '', ''), ('G2 0.7', 'Pilot', '', ''), ('G2 1.0', 'Pilot', '', 'bold')],
    a='G-2', dt='0.38–1.0 mm · many ink colours'),
  X('Zebra Sarasa', 'Click gel pen family led by the Sarasa Clip with a spring-hinged clip.', 'Zebra', '2003', 'https://www.zebra.co.jp/main/products/sarasa-clip/',
    [('Sarasa Clip', 'Zebra', '2003', 'launched in 10 colours'), ('Sarasa Nano', 'Zebra', '', '0.3 mm'), ('Sarasa R', 'Zebra', '', 'denser, vivid ink'),
     ('Sarasa Grand', 'Zebra', '', 'metal body'), ('Sarasa Dry', 'Zebra', '', ''), ('Sarasa Mark On', 'Zebra', '', '')],
    dt='0.3–1.0 mm · vintage and milk colour sets'),
  X('Uni-ball Signo', 'Capped gel pen prized for bold, dark lines; the UM-151 is the cult fine-tip model.', UNI, '', PA + '2016/3/9/mnvnys4yz7l8cih1tvxynwx8syncb7',
    [('Signo UM-151 (Signo DX)', UNI, '', '0.28, 0.38, 0.5 mm; UMR-1 refill'), ('Signo RT', UNI, '', 'retractable')],
    dt='capped or retractable · needle tip option'),
  X('Pilot Hi-Tec-C', 'Needle-tip micro gel pen down to 0.25 mm, sold as G-Tec-C outside Japan.', 'Pilot', '', PA + '2016/7/11/pilot-g-tec-c-navy-and-turquoise-review',
    [('Hi-Tec-C', 'Pilot', '', 'Japan'), ('G-Tec-C', 'Pilot', '', 'export name'), ('Hi-Tec-C Coleto', 'Pilot', '', 'multi pen with Hi-Tec-C refills')],
    a='G-Tec-C', dt='0.25, 0.3, 0.4, 0.5 mm'),
  X('Pentel EnerGel', 'Quick-drying low-viscosity "liquid gel" pen favoured by left-handers.', 'Pentel', '', 'https://pentel.co.uk/product/pentel-energel-x-bl107',
    [('EnerGel X (BL107)', 'Pentel', '', 'LR7 refill'), ('EnerGel Permanent (BLP75)', 'Pentel', '', ''), ('EnerGel Plus', 'Pentel', '', 'non-refillable, recycled plastic'), ('EnerGel Euro', 'Pentel', '', 'needle tip, capped')],
    dt='0.5, 0.7 mm · 12 colours'),
  X('Pilot Juice', 'Slim click gel pen in a very wide colour range.', 'Pilot', '', PA + '2013/8/8/pilot-juice-038-mm-grape-review',
    [('Juice 0.38', 'Pilot', '', ''), ('Juice 0.5', 'Pilot', '', '')], dt='0.38–1.0 mm · standard, pastel, metallic colours'),
  X('Pilot FriXion', 'Erasable pen whose thermochromic Metamo-based ink vanishes with friction heat.', 'Pilot', '2006', 'https://pilot.co.jp/media_english/005/',
    [('FriXion Ball', 'Pilot', '2006', 'first launched in Europe'), ('FriXion Waai', 'Pilot', '', '')],
    a='Frixion', dt='erasable · not for signatures; ink returns below freezing'),
 ],
 'm': [['Uni-ball One', UNI], ['Uni-ball ZENTO', UNI], ['Paper Mate InkJoy', 'Paper Mate'], ['Sailor TUZU', 'Sailor'],
       ['Sharpie S-Gel', 'Sharpie'], ['Tombow MONO Graph Lite', 'Tombow']]}

roll = {'n': 'Rollerball pen', 'a': 'roller pen · liquid-ink pen',
 'd': 'Ball-tip pen with liquid water-based ink for a wet, dark line; digital pens of this type included.',
 't': ['capped', 'retractable', 'disposable', 'refillable (cartridge or RB refill)', 'ceramic ball'],
 's': W + 'Rollerball_pen',
 'x': [
  X('Ohto ceramic rollerball', 'Liquid-ink roller from the maker that introduced the rollerball in 1963.', 'OHTO', '1963', W + 'Rollerball_pen',
    [('CB-10F Ceramic Roller Ball Pen', 'OHTO', '', 'used at the 1990 Economic Summit'), ('CR01 Ceramic', 'OHTO', '', ''), ('Fude Ball', 'OHTO', '', '')]),
  X('Uni-ball Vision / Eye', 'Disposable liquid pigment-ink roller with archival Super Ink.', UNI, '', 'https://www.parkablogs.com/content/review-uni-ball-eye-rollerball-pen',
    [('Uni-ball Eye (UB-157)', UNI, '', 'micro 0.3 mm or fine 0.5 mm line'), ('Uni-ball Vision', UNI, '', 'US name of the same design'),
     ('Vision Elite', UNI, '', 'airplane-safe'), ('Uni-ball Air', UNI, '', '')],
    dt='waterproof, fade-proof pigment ink in black, blue, red'),
  X('Pilot V5 / V7 Hi-Tecpoint', 'Disposable needle-tip liquid-ink roller with an ink regulator and see-through barrel; best seller since 1984.', 'Pilot', '1984', 'https://www.pilotpen.co.uk/our-products/liquid-ink-pens/',
    [('V5 / V7 Hi-Tecpoint', 'Pilot', '1984', '0.5 / 0.7 mm'), ('V5 RT / V7 RT', 'Pilot', '', 'retractable cartridge system'),
     ('V7 Grip', 'Pilot', '', ''), ('V10 RT', 'Pilot', '', 'wide line'), ('V-Ball', 'Pilot', '', 'conical tip'), ('Greenball', 'Pilot', '', 'recycled refillable')],
    a='Precise V5 · Hi-Tecpoint'),
  X('Montblanc Meisterstück rollerball', 'Rollerball of Montblanc\'s black-resin flagship line.', 'Montblanc', '', W + 'Meisterst%C3%BCck',
    [('Meisterstück rollerball', 'Montblanc', '', 'resin'), ('Meisterstück Solitaire', 'Montblanc', '', 'metal and precious-metal bodies')],
    dt='Classique and LeGrand sizes · gold or platinum trim'),
 ],
 'm': [['LAMY 2000 rollerball', 'LAMY'], ['LAMY AL-star rollerball', 'LAMY'], ['Kaweco Perkeo rollerball', 'Kaweco'], ['Herbin Refillable Rollerball', 'Jacques Herbin'],
       ['Retro 51 Tornado', 'Retro 51'], ['Kakimori Frost Rollerball', 'Kakimori'], ['Monteverde Engage One Touch', 'Monteverde'], ['Morning Glory Pro Mach', 'Morning Glory'],
       ['Nahvalur Triad', 'Nahvalur'], ['Pentel Rolling Writer', 'Pentel']]}

multi = {'n': 'Multi pen', 'a': 'multi-colour pen · multifunction pen',
 'd': 'One barrel holding several ballpoint or gel refills, sometimes with a pencil, selected in turn.',
 't': ['2-, 3- or 4-colour', 'with mechanical pencil', 'build-your-own body', 'D1 refills', 'proprietary refills'],
 's': MPG,
 'x': [
  X('Bic 4 Colours', 'Four-colour slider ballpoint, the mass-market original.', 'Bic', '1970', W + 'Bic_Cristal', [('4 Colours', 'Bic', '1970', '')]),
  X('Lamy 2000 4-colour', 'Makrolon and steel four-colour ballpoint whose refill is chosen by gravity.', 'Lamy', '', GS + '2016/12/6/pen-review-lamy-2000-4-color-ballpoint-multipen',
    [('2000 4-Color Ballpoint', 'Lamy', '', 'D1 refills')], dt='black, blue, red, green markers'),
  X('Uni Style Fit', 'Build-your-own multi pen: pick a body and fill it with slim gel, ballpoint or pencil units.', UNI, '', PA + '2016/6/15/uni-style-fit-meister-multi-pen-review',
    [('Style Fit', UNI, '', 'plastic, knock-select'), ('Style Fit Meister', UNI, '', 'metal, twist-select, 0.5 mm pencil unit')],
    dt='1-, 3-, 4-, 5-slot bodies · 0.28–0.5 mm gel refills'),
  X('Zebra Sharbo X', 'Premium metal twist multi pen taking D1 refills and a pencil unit.', 'Zebra', '', GS + '2015/12/10/zebra-sharbo-x-the-premium-multi-pen',
    [('Sharbo X LT3', 'Zebra', '', 'slim three-slot'), ('Sharbo X ST3', 'Zebra', '', 'wider three-slot')], dt='rotate-to-select · eraser under cap'),
  X('Uni Jetstream multi pen', 'Jetstream hybrid-ink refills in a multi-colour body, often with a pencil.', UNI, '', MPG,
    [('Jetstream 3 Color', UNI, '', ''), ('Jetstream 4&1', UNI, '', 'four colours plus 0.5 mm pencil')]),
 ],
 'm': [['Pilot FriXion Ball 3 Slim', 'Pilot'], ['Pilot FriXion Ball 4', 'Pilot'], ['Pilot Hi-Tec-C Coleto', 'Pilot'], ['Uni-ball One 3 Color', UNI],
       ['Uni-ball ZENTO 3 Color', UNI], ['Sailor Imperial Black Multifunction Pen', 'Sailor'], ['Zebra Sarasa Multi', 'Zebra'], ['OHTO MS02', 'OHTO'],
       ['Livework 4 Color', 'Livework'], ['Writech Dual Color', 'Writech']]}

refill = {'n': 'Pen refill', 'a': 'ink refill · cartridge',
 'd': 'Ink refill for a ballpoint, gel, rollerball or multi pen, chosen by refill standard rather than brand.',
 't': ['G2 Parker-style (ISO 12757)', 'D1 mini (multi pens)', 'RB rollerball', 'Pilot G2 size', 'Uni SXR (Jetstream)', 'Cross-type', 'pressurised'],
 's': 'https://bleistift.blog/2018/02/refills/',
 'x': [
  X('G2 Parker-style refill', 'Large-capacity metal refill about 6 mm by 98 mm, from the Parker Jotter, fitted by many makers.', 'Parker', '1950s', 'https://bleistift.blog/2018/02/refills/',
    [('T-Ball (Quinkflow)', 'Parker', '1957', 'Jotter refill'), ('PR pressurised G2-fit', 'Fisher Space Pen', '', '')], a='ISO G2'),
  X('D1 mini refill', 'Short 2.35 mm refill used in multi pens and mini pens.', '', '', 'https://bleistift.blog/2018/02/refills/',
    [('Jetstream D1 (SXR-200)', UNI, '', ''), ('Lamy M21', 'Lamy', '', 'for Lamy 2000 4-colour')]),
  X('Pilot G2 gel refill', 'Gel refill for the G2 family, widely copied as a size; not the ISO G2.', 'Pilot', '', 'https://unsharpen.com/refill/pilot-g2-gel-pen-refill/',
    [('G2 refill 0.38–1.0 mm', 'Pilot', '', 'sold as LP2RF/LG2RF in Japan')]),
  X('Uni Jetstream SXR refill', 'Uni\'s hybrid-ink ballpoint refill family.', UNI, '', 'https://unsharpen.com/pen/uni-jetstream-ballpoint-pen/',
    [('SXR-5 / SXR-7', UNI, '', 'standard Jetstream'), ('SXR-38', UNI, '', ''), ('SXR-80', UNI, '', 'multi pen'), ('SXR-600', UNI, '', ''), ('SXR-203', UNI, '', '')]),
 ],
 'm': [['Uni-ball One UMR-05S gel refill', UNI], ['Uni-ball ZENTO gel refill', UNI], ['Pentel EnerGel LR7', 'Pentel'], ['Uni-ball Signo UMR-1', UNI]]}


def B(n, c, f, seg, kf, d, s, lines=(), sig=()):
    return {'n': n, 'c': c, 'f': f, 'seg': seg, 'kf': kf, 'd': d, 'lines': list(lines), 'eras': [], 'sig': list(sig), 'sc': [], 'rel': [], 's': s}


brands = [
 B('Bic', 'France', '1945', 'Value', 'disposable ballpoints', 'Clichy maker of the Cristal ballpoint, lighters and razors.', 'knowledge', ['Cristal', '4 Colours', 'Orange'], ['Bic Cristal', 'Bic 4 Colours']),
 B('Parker', 'United States', '1888', 'Mainstream', 'Jotter ballpoint', 'Pen maker now part of Newell Brands; Jotter made in France.', 'knowledge', ['Jotter', 'Quink'], ['Parker Jotter', 'G2 Parker-style refill']),
 B('Fisher Space Pen', 'United States', '', 'Specialist', 'pressurised space pens', 'Maker of Paul C. Fisher\'s pressurised-refill pens used by NASA.', W + 'Fisher_Space_Pen', ['AG7', 'Bullet', 'Millennium'], ['Fisher Space Pen']),
 B('Cross', 'United States', '1846', 'Mainstream', 'gift pens', 'Rhode Island pen maker known for the Century.', 'knowledge', ['Century', 'Townsend'], ['Cross Century']),
 B('Lamy', 'Germany', '1930', 'Premium', 'design pens', 'Heidelberg design-led pen maker.', W + 'Lamy_2000', ['2000', 'Safari', 'AL-star'], ['Lamy 2000 ballpoint', 'Lamy 2000 4-colour']),
 B(UNI, 'Japan', '1887', 'Mainstream', 'Jetstream, Uni-ball', 'Tokyo pen and pencil maker selling as Uni and Uni-ball.', 'knowledge', ['Jetstream', 'Uni-ball Signo', 'Uni-ball Eye/Vision', 'Style Fit'], ['Uni Jetstream', 'Uni-ball Signo', 'Uni-ball Vision / Eye']),
 B('Zebra', 'Japan', '1897', 'Mainstream', 'pens', 'Tokyo pen maker of the Sarasa and F-301.', 'knowledge', ['Sarasa', 'F-301', 'Sharbo X'], ['Zebra Sarasa', 'Zebra F-301', 'Zebra Sharbo X']),
 B('Pilot', 'Japan', '1918', 'Mainstream', 'pens and inks', 'Japan\'s largest pen maker.', 'knowledge', ['G2', 'FriXion', 'Hi-Tec-C', 'Juice', 'V5/V7', 'Acroball'], ['Pilot G2', 'Pilot FriXion', 'Pilot Hi-Tec-C', 'Pilot V5 / V7 Hi-Tecpoint']),
 B('Pentel', 'Japan', '1946', 'Mainstream', 'pens and markers', 'Tokyo maker of the EnerGel and the Rolling Writer.', 'knowledge', ['EnerGel', 'Rolling Writer', 'Calme'], ['Pentel EnerGel']),
 B('Montblanc', 'Germany', '1906', 'Professional & flagship', 'luxury pens', 'Hamburg luxury pen house of the Meisterstück.', W + 'Meisterst%C3%BCck', ['Meisterstück'], ['Montblanc Meisterstück rollerball']),
 B('Sakura', 'Japan', '1921', 'Mainstream', 'gel pens, art markers', 'Osaka maker that invented gel ink.', 'knowledge', ['Gelly Roll', 'Pigma'], ['Sakura Ball Sign / Gelly Roll']),
 B('OHTO', 'Japan', '', 'Specialist', 'rollerballs, needle-point pens', 'Japanese pen maker that introduced the liquid-ink rollerball in 1963.', W + 'Rollerball_pen', ['CB-10F', 'GS01', 'Fude Ball'], ['Ohto ceramic rollerball']),
]

notes = ('All five planned kinds kept. Old JetPens-led model lists (a retailer-skew finding) were reorganised: Jetstream, Acroball, F-301, G2, Sarasa, Signo, Hi-Tec-C, Juice, EnerGel, FriXion, Vision/Eye, V5/V7 and multi pens became archetypes with versions; '
 'the remaining old models stay in m. Machined-pen boutique makers (Schon DSGN, Retro 51, Kakimori, Nahvalur) kept as flat models without register entries (no page retrieved). Old ranges Kaweco Sport and Leuchtturm Drehgriffel dropped as duplicates of models. '
 'Not added: Uni-ball One, ZENTO, Pentel EnerGel and Signo launch years, Fisher Bullet year (only search snippets), Montblanc 163/164 model numbers (not on retrieved page), Cross Century materials beyond what penhero gives. '
 'Pen refill reorganised by refill standard (G2 Parker-style, D1, Pilot G2 size, SXR). unsharpen.com and spacepen.com blocked WebFetch and were retrieved via firecrawl. Brand facts for Bic, Parker, Cross, Uni, Zebra, Pilot, Pentel, Sakura from knowledge.')
out = {'kinds': [ball, gel, roll, multi, refill], 'brands': brands, 'traditions': [], 'notes': notes}
p = 'work/C5/shelves/01_00.json'
json.dump(out, open(p + '.tmp', 'w'), ensure_ascii=False, indent=1); os.replace(p + '.tmp', p)
print('archetypes', sum(len(k.get('x', [])) for k in out['kinds']))
