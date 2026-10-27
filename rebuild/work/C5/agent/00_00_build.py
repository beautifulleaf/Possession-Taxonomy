import json, os
W = 'https://en.wikipedia.org/wiki/'
FP = W + 'Fountain_pen'
def X(n, d, mk, y, s, v=(), a='', dt=''):
    o = {'n': n, 'a': a, 'd': d, 'mk': mk, 'y': y, 's': s, 'v': [dict(zip(('n', 'mk', 'y', 'd'), t)) for t in v]}
    if dt: o['dt'] = dt
    return o

cc = {'n': 'Cartridge-converter fountain pen', 'a': '万年筆 · cartridge pen · C/C pen',
 'd': 'Fountain pen filled from a sealed ink cartridge or a removable converter that draws from a bottle.',
 't': ['standard international cartridge', 'proprietary cartridge', 'steel nib', 'gold nib', 'urushi or maki-e finish'],
 's': 'https://www.jetpens.com/Fountain-Pens/ct/214',
 'x': [
  X('Lamy Safari', 'Moulded ABS school and everyday pen with a cut-out grip, wire clip and steel nib; the reference modern cartridge pen.', 'Lamy', '1980', W + 'Lamy',
    [('Safari', 'Lamy', '1980', 'designed by Wolfgang Fabian and Bernt Spiegel'), ('AL-star', 'Lamy', '', 'aluminium body derived from the Safari'), ('Vista', 'Lamy', '', 'clear demonstrator derived from the Safari')],
    dt='body colours and annual special colours · nib widths · Lamy cartridge or converter'),
  X('Kaweco Sport', 'Short octagonal-capped pocket pen that reaches full length when the cap is posted.', 'Kaweco', '1911', W + 'Kaweco',
    [('Sport (first mention)', 'Kaweco', '1911', 'pocket pen for ladies, officers and sportsmen'), ('Sport series reissue', 'Kaweco', '1994', 'based on a 1935 design'), ('Classic Sport', 'Kaweco', '', 'plastic body'), ('Lunar Sport', 'Kaweco', '', '')],
    dt='plastic, aluminium, brass and other bodies · short international cartridges'),
  X('Sailor 1911', 'Rounded cigar-shaped resin pen with gold nib; Sailor\'s core line, called Profit in Japan.', 'Sailor', '1981', W + 'Sailor_(pen_company)',
    [('1911 Standard', 'Sailor', '', 'comparable to the Pro Gear Slim'), ('1911 Large', 'Sailor', '', '21k nib; Naginata Togi nibs offered'), ('King of Pen', 'Sailor', '', 'larger size with #9 21k nib; black ebonite version 2021')],
    a='Profit', dt='21k or 14k gold nib · specialty grinds (Naginata Togi, Concord, Emperor) · resin or ebonite'),
  X('Sailor Pro Gear', 'Flat-topped version of the 1911 with square shoulders and anchor cap medallion.', 'Sailor', '', 'https://www.thejournalshop.com/blogs/guides/sailor-pro-gear-complete-guide',
    [('Pro Gear', 'Sailor', '', 'full size, 21ct gold nib'), ('Pro Gear Slim', 'Sailor', '', 'smaller, 14ct gold nib'), ('Pro Gear Slim Mini', 'Sailor', '', 'pocket size, 14ct nib')],
    a='Professional Gear', dt='colour editions · trim colour · nib width'),
  X('Platinum #3776 Century', 'Platinum\'s flagship gold-nib pen, named for Mount Fuji\'s height in metres.', 'Platinum', '1978', W + 'Platinum_Pen_Company',
    a='3776', dt='resin colours · gold nib widths · Platinum cartridge or converter'),
  X('Pilot Custom', 'Pilot\'s family of torpedo and flat-top gold-nib pens in graded sizes.', 'Pilot', '1992', W + 'Pilot_(pen_company)',
    [('Custom 74', 'Pilot', '1992', ''), ('Custom 742', 'Pilot', '1993', ''), ('Custom 743', 'Pilot', '1993', ''), ('Custom 845 Urushi', 'Pilot', '2002', 'urushi-lacquered'),
     ('Custom Heritage 91', 'Pilot', '2009', 'cartridge or converter'), ('Custom Heritage 912', 'Pilot', '', ''), ('Custom Urushi', 'Pilot', '2016', '')],
    dt='14k gold nib sizes and many grinds · resin colours'),
  X('Pilot Metropolitan', 'Metal-bodied entry pen with steel nib, supplied with a converter.', 'Pilot', '2012', W + 'Pilot_(pen_company)', a='Cocoon (Japan)', dt='body colours · F/M nib'),
  X('Pilot Kakuno', 'Children\'s plastic beginner pen with hexagonal barrel and smiling face on the nib.', 'Pilot', '', 'https://www.penaddict.com/blog/2013/12/19/pilot-kakuno-fountain-pen-review', dt='cap and barrel colours · nib width'),
  X('Platinum Preppy', 'Very low-cost clear plastic pen with steel nib.', 'Platinum', '', 'https://www.penaddict.com/blog/2020/7/5/platinum-prefounte-fine-nib-fountain-pen-review',
    [('Prefounte', 'Platinum', '', 'step-up with Slip & Seal cap')], dt='ink-matched colours · nib width'),
  X('Namiki maki-e pens', 'Pilot\'s hand-lacquered urushi pens decorated with maki-e by lacquer artists.', 'Namiki', '1925', W + 'Namiki',
    [('Dunhill-Namiki', 'Namiki', '1929', 'sold through Alfred Dunhill'), ('Emperor collection', 'Namiki', '', 'largest, most renowned'), ('Yukari', 'Namiki', '', ''), ('Yukari Royale', 'Namiki', '', ''), ('Chinkin', 'Namiki', '', ''), ('Nippon Art', 'Namiki', '', '')],
    a='Pilot maki-e', dt='motif · maki-e technique (hira, togidashi, taka) · size'),
  X('Nakaya urushi pens', 'Hand-turned ebonite pens finished in urushi lacquer by former Platinum craftsmen.', 'Nakaya', '1999', 'https://www.iguanasell.com.au/blogs/news/history-nakaya-fountain-pens',
    [('Portable Cigar', 'Nakaya', '', ''), ('Piccolo', 'Nakaya', '', 'compact'), ('Dorsal Fin', 'Nakaya', '', 'shark-fin profile'), ('Decapod', 'Nakaya', '', 'ten-sided')],
    dt='tame-nuri, maki-e or raden finish · Platinum nib'),
  X('Graf von Faber-Castell Classic', 'Wood-barrelled luxury pen from Faber-Castell\'s premium brand.', 'Graf von Faber-Castell', '1993', W + 'Graf_von_Faber-Castell',
    [('Classic', 'Graf von Faber-Castell', '', 'ebony, pernambuco or grenadilla'), ('Guilloche', 'Graf von Faber-Castell', '', 'carved resin'), ('Intuition', 'Graf von Faber-Castell', '', 'black resin'), ('Pen of the Year', 'Graf von Faber-Castell', '2003', 'annual limited edition, 18k bicolour nib')],
    dt='barrel wood or resin · 18k nib'),
  X('Aurora Duo-Cart', 'Aurora\'s first cartridge pen, holding two linked cartridges.', 'Aurora', '1954', W + 'Aurora_(pen_manufacturer)', dt='designed by Albe Steiner'),
  X('Cross Century', 'Slim tapered metal pen, Cross\'s long-running line.', 'Cross', '', W + 'A._T._Cross_Company',
    [('Century II', 'Cross', '', ''), ('Townsend', 'Cross', '', 'larger sister line')], dt='lacquer or precious-metal finishes'),
 ],
 'm': [['Parker 45', 'Parker'], ['Parker 75', 'Parker'], ['Parker Sonnet', 'Parker'], ['Parker VP', 'Parker'], ['Parker VS', 'Parker'], ['Parker Jotter', 'Parker'],
       ['LAMY scala', 'Lamy'], ['Kaweco Perkeo', 'Kaweco'], ['Waterman Carène', 'Waterman'], ['Waterman Expert', 'Waterman'], ['Waterman Hémisphère', 'Waterman'],
       ['Montegrappa Tarvisium', 'Montegrappa'], ['Platinum Plaisir', 'Platinum'], ['S.T. Dupont Defi Millenium', 'S.T. Dupont'], ['Conklin All American', 'Conklin'], ['Conklin 1898', 'Conklin'],
       ['Monteverde Prima', 'Monteverde'], ['BIGiDESIGN Ti Ultra', 'BIGiDESIGN'], ['Stilform INK', 'Stilform'], ['TRAVELER\'S COMPANY BRASS fountain pen', 'TRAVELER\'S COMPANY'],
       ['Pentel Tradio', 'Pentel'], ['Rhodia scRipt', 'Rhodia'], ['Penlux Masterpiece', 'Penlux'], ['Pent Symphony', 'Pent'], ['Wearingeul Literature', 'Wearingeul'],
       ['Hightide Attache', 'Hightide'], ['IWI Handscript', 'IWI'], ['E+M Contract', 'E+M'], ['Nakabayashi Artnavi', 'Nakabayashi'], ['Kolo Tino', 'Kolo'], ['Meister by Point Slim Liner', 'Meister by Point']],
 'r': [['Kaweco Sport', 'Kaweco'], ['Bungubox Original', 'Bungubox']]}

pis = {'n': 'Piston-filling fountain pen', 'a': 'piston filler', 'd': 'Fountain pen whose barrel is the ink reservoir, filled by turning a knob that draws a built-in piston.',
 't': ['screw piston', 'threaded piston unit', 'demonstrator'], 's': FP,
 'x': [
  X('Pelikan 100', 'Günther Wagner\'s first Pelikan, the first modern screw piston-filling fountain pen.', 'Pelikan', '1929', FP, dt='green-striped and other celluloid barrels'),
  X('Pelikan Souverän', 'Striped-barrel gold-nib piston pens in graded sizes, Pelikan\'s flagship line.', 'Pelikan', '1982', 'https://thepelikansperch.com/2020/11/15/pelikan-m800-history-explored/',
    [('M400', 'Pelikan', '1982', 'first Souverän'), ('M600', 'Pelikan', '1985', 'enlarged to intermediate size 1997'), ('M800', 'Pelikan', '1987', 'first modern oversized Pelikan; threaded piston unit'),
     ('M1000', 'Pelikan', '1997', 'flagship, rival to the Montblanc 149'), ('M850', 'Pelikan', '1997', 'vermeil cap; to 2001'), ('M805', 'Pelikan', '2002', 'palladium trim'), ('M815 Metal Striped', 'Pelikan', '2018', 'brass barrel')],
    dt='green/black, blue, red and tortoiseshell striped barrels · 14C nib to 1990 then 18C · EF–BB and obliques'),
  X('Montblanc Meisterstück 149', 'Largest Meisterstück, black resin with white snowcap emblem and three-tone 18k nib.', 'Montblanc', '1952', 'https://www.fountainpen.de/c-149-en.htm',
    [('149', 'Montblanc', '1952', 'piston filler'), ('146 Le Grand', 'Montblanc', '', 'mid size')], a='Meisterstück', dt='nib EF–OBB · platinum inlay · celluloid then resin'),
  X('Lamy 2000', 'Bauhaus-style Makrolon pen with brushed steel section and semi-hooded nib, designed by Gerd A. Müller.', 'Lamy', '1966', W + 'Lamy_2000',
    [('Stainless steel', 'Lamy', '2013', 'all-metal body'), ('Bauhaus Blue', 'Lamy', '2019', 'special edition'), ('Brown', 'Lamy', '2021', 'special edition'), ('Pine Green', 'Lamy', '2024', 'special edition')],
    dt='14k platinum-coated nib EF–OBB, OM'),
  X('Aurora 88', 'Italian hooded-nib pen designed by Marcello Nizzolli to compete with the Parker 51.', 'Aurora', '1947', W + 'Aurora_(pen_manufacturer)', dt='over five million made'),
  X('Pilot Custom Heritage 92', 'Pilot\'s demonstrator piston-filling pen.', 'Pilot', '2010', W + 'Pilot_(pen_company)'),
  X('TWSBI Eco', 'Inexpensive clear demonstrator piston filler from Taiwan.', 'TWSBI', '', 'https://goldspot.com/collections/twsbi-pens', [('Eco-T', 'TWSBI', '', 'triangular grip')], dt='colours · steel nib widths'),
  X('OMAS Arte Italiana', 'OMAS\'s faceted top line in graded sizes.', 'OMAS', '', W + 'OMAS', [('Paragon', 'OMAS', '', '12-faceted, largest size'), ('Milord', 'OMAS', '', 'second size')], dt='celluloid and resin colours'),
 ],
 'm': [['Pelikan M205', 'Pelikan'], ['TWSBI Diamond 580', 'TWSBI'], ['Aurora Optima', 'Aurora'], ['OMAS 360', 'OMAS']]}

vac = {'n': 'Vacuum and plunger-filling fountain pen', 'a': 'vacuum filler · plunger filler', 'd': 'Fountain pen filled by pushing a plunger that creates a vacuum and draws ink into the barrel.',
 't': ['diaphragm (Vacumatic)', 'plunger with shut-off valve', 'power filler'], 's': FP,
 'x': [
  X('Parker Vacumatic', 'Striped celluloid pen whose whole barrel holds ink, filled by a plunger-operated diaphragm.', 'Parker', '1932', W + 'Parker_Vacumatic',
    [('Golden Arrow', 'Parker', '1932', 'original name'), ('Lock-Down filler', 'Parker', '', 'twist-locked plunger'), ('Duovac', 'Parker', '1940', 'Duofold in the Vacumatic series')],
    dt='pearl and clear striped celluloid · sizes'),
  X('Pilot Custom 823', 'Amber, smoke or clear demonstrator with a plunger filler and shut-off.', 'Pilot', '2000', W + 'Pilot_(pen_company)', dt='14k nib shared with Custom 743'),
  X('TWSBI Vac 700R', 'Clear demonstrator vacuum filler with one valve and large ink capacity.', 'TWSBI', '', 'https://www.purepens.co.uk/products/twsbi-vac-700r-clear',
    [('Vac 700', 'TWSBI', '', 'original version'), ('Vac 700R', 'TWSBI', '', 'one valve, larger feed'), ('Vac Mini', 'TWSBI', '', 'small vacuum filler')]),
  X('Visconti Homo Sapiens', 'Visconti\'s flagship with a body made partly from Etna lava.', 'Visconti', 'c. 2009', W + 'Visconti_(company)',
    [('Lava Bronze', 'Visconti', '', 'Etna lava body with bronze accents')], dt='Visconti power filler system introduced 1993'),
 ]}

sac = {'n': 'Sac-filling fountain pen', 'a': 'self-filler · lever filler · button filler · vintage fountain pen',
 'd': 'Vintage-style pen with a rubber or plastic sac filled by squeezing it with a lever, button, crescent, bar or air pump.',
 't': ['crescent', 'lever', 'button', 'pneumatic (Touchdown)', 'Snorkel', 'aerometric', 'squeeze sac', 'capillary'], 's': FP,
 'x': [
  X('Conklin Crescent Filler', 'Pen filled by pressing a metal crescent on the barrel, locked by a turning ring; endorsed by Mark Twain.', 'Conklin', '1897', 'https://www.artbrown.com/blogs/brand-highlights-and-know-how/the-conklin-crescent-filler-the-invention-that-changed-fountain-pens-forever',
    [('Mark Twain Crescent Filler', 'Conklin', '', 'modern reissue')]),
  X('Sheaffer Lifetime', 'Sheaffer lever filler sold with a lifetime guarantee, marked by the white dot.', 'Sheaffer', '1920', 'https://www.penhero.com/PenGallery/Sheaffer/Sheaffer.htm',
    [('Flat-top lever filler', 'Sheaffer', '1914', ''), ('Lifetime', 'Sheaffer', '1920', 'to c.1928'), ('Jade Senior', 'Sheaffer', '1924', 'jade Radite'), ('Lifetime (revival)', 'Sheaffer', '1963', 'to 1964')],
    dt='white dot from 1924 · Radite colours'),
  X('Parker Duofold', 'Large red hard-rubber button filler that became Parker\'s 1920s flagship.', 'Parker', '1921', W + 'Parker_Duofold',
    [('Duofold', 'Parker', '1921', 'red hard rubber'), ('Duofold Junior', 'Parker', '', 'smaller'), ('Duofold Special', 'Parker', '', 'smaller'), ('Lady Duofold', 'Parker', '', 'ring top'),
     ('Centennial', 'Parker', '1988', 'revived flagship'), ('International', 'Parker', '', 'smaller modern size, cartridge/converter')],
    a='Big Red', dt='hard rubber to 1926, then Permanite in red, jade, lapis, mandarin yellow'),
  X('Sheaffer Balance', 'Streamlined celluloid lever filler of the 1930s.', 'Sheaffer', '1929', 'https://www.penhero.com/PenGallery/Sheaffer/Sheaffer.htm',
    [('Balance', 'Sheaffer', '1929', 'to c.1941'), ('Balance Limited Edition', 'Sheaffer', '1997', ''), ('Balance II', 'Sheaffer', '1998', 'to 2000')]),
  X('Waterman Patrician', 'Waterman\'s celluloid flagship until the Hundred Year Pen of 1939.', 'Waterman', '1929', 'https://vintagepens.com/Waterman_late_Patrician.shtml',
    [('Patrician', 'Waterman', '1929', ''), ('Lady Patricia', 'Waterman', '', 'smaller companion')], dt='Ideal nib · turquoise, emerald and other celluloids'),
  X('Waterman 52', 'Common hard-rubber screw-cap lever filler.', 'Waterman', '', W + 'Waterman_S._A.'),
  X('Parker 51', 'Hooded-nib pen with fin collector, often called the most used fountain pen ever.', 'Parker', '1941', W + 'Parker_51',
    [('51 Vacumatic', 'Parker', '1941', 'diaphragm filler'), ('51 Aerometric', 'Parker', '1948', 'pressure bar on a Pli-Glass sac'), ('51 Special Edition', 'Parker', '2002', 'lookalike'), ('Parker 51 (2021)', 'Parker', '2021', 'reimagined, slightly longer')],
    dt='produced to 1972 · cap and barrel colours'),
  X('Sheaffer Touchdown', 'Pneumatic filler: an outer tube pushed down compresses the sac.', 'Sheaffer', '1949', 'https://www.penhero.com/PenGallery/Sheaffer/Sheaffer.htm',
    [('Touchdown', 'Sheaffer', '1949', ''), ('Thin Model Touchdown', 'Sheaffer', '1950', ''), ('Tip Dip Touchdown', 'Sheaffer', '1953', '')]),
  X('Sheaffer Snorkel', 'Touchdown pen with a tube that extends below the nib so the nib need not be dipped.', 'Sheaffer', '1952', W + 'Sheaffer',
    [('Snorkel', 'Sheaffer', '1952', 'to 1959'), ('PFM (Pen For Men)', 'Sheaffer', '1959', 'fat body, inlaid nib, last Snorkel; to 1968')]),
  X('Esterbrook J', 'Durable lever-filling pen with user-swappable nibs.', 'Esterbrook', '1940s', FP),
  X('Parker 61', 'Pen filled by capillary action from a cell in the barrel.', 'Parker', '1956', FP),
  X('Parker 180', 'Flat pen filled by squeezing a flexible sac.', 'Parker', '1977', W + 'Parker_Pen_Company'),
 ],
 'm': [['Parker 21', 'Parker'], ['Parker Parkette', 'Parker'], ['Esterbrook Dollar Pen', 'Esterbrook'], ['Eversharp Bantam', 'Eversharp'], ['Moore Finger Tip', 'Moore'], ["Morrison's Patriot", 'Morrison'], ['Dunn-Pen', 'Dunn']]}

eye = {'n': 'Eyedropper fountain pen', 'a': 'eyedropper filler · dropper pen', 'd': 'Fountain pen whose barrel is filled directly with ink from a dropper or syringe.',
 't': ['plain eyedropper', 'eyedropper with shut-off valve', 'ebonite', 'urushi finish'], 's': FP,
 'x': [
  X('Parker Jointless', 'Early one-piece-barrel eyedropper with Parker\'s Lucky Curve feed.', 'Parker', '1898', FP),
  X('Waterman 12', 'Slip-cap hard-rubber eyedropper from Waterman\'s early years.', 'Waterman', '', W + 'Waterman_S._A.'),
  X('Swan Safety Screw-Cap', 'Mabie Todd eyedropper with a screw cap to stop leaks.', 'Mabie Todd', '', FP),
  X('Danitrio Genkai', 'Large straight ebonite eyedropper finished in urushi; the name means "the limited".', 'Danitrio', '', 'https://chatterleyluxuries.com/product/danitrio-maki-e-wakasa-nuri-sho-genkai-fountain-pen/',
    dt='#8 18k nib on ebonite feed · urushi and maki-e finishes'),
 ]}

ret = {'n': 'Retractable-nib fountain pen', 'a': 'capless fountain pen · click fountain pen · safety pen', 'd': 'Fountain pen whose nib retracts into the body by click or twist, so it needs no cap.',
 't': ['click', 'twist', 'vintage safety pen'], 's': 'https://iguanasell.com.au/blogs/news/retractable-fountain-pens',
 'x': [
  X('Waterman 42 Safety', 'Early safety pen whose nib retracts into the barrel.', 'Waterman', '1908', W + 'Waterman_S._A.'),
  X('Pilot Capless', 'Click-action pen with a trapdoor tip and 18k nib; sold as Vanishing Point in the West.', 'Pilot', '1963', W + 'Pilot_(pen_company)',
    [('Capless', 'Pilot', '1963', ''), ('Vanishing Point', 'Pilot', '1972', 'reintroduced Capless'), ('Capless Decimo', 'Pilot', '', 'lighter, slimmer'), ('Namiki Capless', 'Namiki', '', '')],
    a='Vanishing Point · VP', dt='18k nib F/M/B · body finishes'),
  X('Lamy Dialog 3', 'Twist-action pen whose ball closure opens and clip sinks as the nib extends.', 'Lamy', '', 'https://iguanasell.com.au/blogs/news/retractable-fountain-pens', dt='14k bicolour nib · designed by Franco Clivio'),
  X('Platinum Curidas', 'Low-cost click retractable with steel nib.', 'Platinum', '2020', 'https://www.gouletpens.com/blogs/fountain-pen-blog/platinum-curidas-retractable-fountain-pens', dt='five colours · EF/F/M'),
 ]}

def B(n, c, f, seg, d, s, lines=(), sig=(), rel=(), eras=()):
    SEG = {'Pelikan':'Premium','Montblanc':'Professional & flagship','Lamy':'Premium','Pilot':'Mainstream','Namiki':'Artisan & independent','Sailor':'Premium','Platinum':'Mainstream',
     'Nakaya':'Artisan & independent','Danitrio':'Artisan & independent','Parker':'Mainstream','Sheaffer':'Heritage manufactory','Waterman':'Mainstream','Esterbrook':'Heritage manufactory',
     'Conklin':'Heritage manufactory','Kaweco':'Value','TWSBI':'Value','Aurora':'Heritage manufactory','Visconti':'Premium','Montegrappa':'Heritage manufactory','OMAS':'Heritage manufactory',
     'Cross':'Mainstream','Graf von Faber-Castell':'Professional & flagship','Mabie Todd':'Heritage manufactory'}
    return {'n': n, 'c': c, 'f': f, 'seg': SEG[n], 'kf': seg, 'd': d, 'lines': list(lines), 'eras': list(eras), 'sig': list(sig), 'sc': [], 'rel': list(rel), 's': s}
brands = [
 B('Pelikan', 'Germany', '1838', 'Premium and mainstream pens and inks', 'Hanover maker that introduced the modern piston filler.', 'knowledge', ['Souverän', 'Classic'], ['Pelikan 100', 'Pelikan Souverän'], ['Montblanc']),
 B('Montblanc', 'Germany', '1906', 'Luxury', 'Hamburg luxury pen maker, owned by Richemont since 1993, known for the snowcap emblem.', W + 'Montblanc_(company)', ['Meisterstück', 'Writers Edition'], ['Montblanc Meisterstück 149'], ['Pelikan']),
 B('Lamy', 'Germany', '1930', 'Design pens', 'Heidelberg design-led pen maker founded by Josef Lamy, owned by Mitsubishi Pencil since 2024.', W + 'Lamy', ['Safari', 'AL-star', '2000', 'Dialog', 'Studio'], ['Lamy 2000', 'Lamy Safari', 'Lamy Dialog 3']),
 B('Pilot', 'Japan', '1918', 'Mass market to premium', 'Japan\'s largest pen maker, founded as Namiki Manufacturing by Ryosuke Namiki and Masao Wada.', W + 'Pilot_(pen_company)', ['Custom', 'Capless', 'Metropolitan', 'Kakuno'], ['Pilot Capless', 'Pilot Custom 823', 'Pilot Custom'], ['Namiki']),
 B('Namiki', 'Japan', '1925', 'Luxury maki-e', 'Pilot\'s hand-lacquered maki-e pen brand.', W + 'Namiki', ['Emperor', 'Yukari', 'Chinkin', 'Nippon Art'], ['Namiki maki-e pens'], ['Pilot']),
 B('Sailor', 'Japan', '1911', 'Premium', 'Kure pen maker known for 21k nibs and specialty nib grinds.', W + 'Sailor_(pen_company)', ['1911', 'Pro Gear', 'King of Pen'], ['Sailor 1911', 'Sailor Pro Gear']),
 B('Platinum', 'Japan', '1919', 'Mass market to premium', 'Tokyo pen maker credited with the first cartridge fountain pen (1956).', W + 'Platinum_Pen_Company', ['3776 Century', 'Preppy', 'Curidas'], ['Platinum #3776 Century', 'Platinum Preppy'], ['Nakaya']),
 B('Nakaya', 'Japan', '1999', 'Artisan urushi', 'Custom urushi pen workshop founded by Toshiya Nakata with former Platinum craftsmen.', 'https://www.iguanasell.com.au/blogs/news/history-nakaya-fountain-pens', ['Portable', 'Piccolo', 'Decapod'], ['Nakaya urushi pens'], ['Platinum']),
 B('Danitrio', '', '', 'Artisan urushi', 'Maker of large hand-lacquered urushi and maki-e pens.', 'https://chatterleyluxuries.com/product/danitrio-maki-e-wakasa-nuri-sho-genkai-fountain-pen/', ['Genkai', 'Mikado'], ['Danitrio Genkai']),
 B('Parker', 'United States', '1888', 'Mainstream to premium', 'Janesville pen maker founded by George S. Parker, now based in France under Newell Brands.', W + 'Parker_Pen_Company', ['Duofold', 'Vacumatic', '51', 'Sonnet', 'Jotter'], ['Parker 51', 'Parker Duofold', 'Parker Vacumatic'], ['Waterman']),
 B('Sheaffer', 'United States', '1913', 'Mainstream', 'Fort Madison maker founded on Walter A. Sheaffer\'s lever filler; owned by William Penn since 2022.', W + 'Sheaffer', ['Lifetime', 'Balance', 'Snorkel', 'PFM', 'Targa', 'Legacy'], ['Sheaffer Lifetime', 'Sheaffer Balance', 'Sheaffer Snorkel'], ['Cross']),
 B('Waterman', 'United States', '1884', 'Mainstream to premium', 'New York maker founded by Lewis Waterman; continues as Paris-based Waterman S.A. under Newell Brands.', W + 'Waterman_S._A.', ['Patrician', 'Carène', 'Expert', 'Hémisphère'], ['Waterman Patrician', 'Waterman 52'], ['Parker']),
 B('Esterbrook', 'United States', '1858', 'Everyday, revived premium', 'Camden steel-pen maker, once America\'s largest, revived in 2014 and owned by Kenro since 2018.', W + 'Esterbrook', ['J', 'Dollar', 'Estie'], ['Esterbrook J']),
 B('Conklin', 'United States', '', 'Vintage and revived', 'Toledo maker of Roy Conklin\'s crescent-filler pen, promoted by Mark Twain.', 'https://www.artbrown.com/blogs/brand-highlights-and-know-how/the-conklin-crescent-filler-the-invention-that-changed-fountain-pens-forever', ['Crescent Filler'], ['Conklin Crescent Filler']),
 B('Kaweco', 'Germany', '1883', 'Everyday pocket pens', 'Heidelberg pen maker, owned by Gutberlet since 1994, known for the Sport.', W + 'Kaweco', ['Sport', 'Perkeo'], ['Kaweco Sport']),
 B('TWSBI', 'Taiwan', '2009', 'Value enthusiast', 'Pen brand of the OEM maker Ta Shin Precision, known for demonstrator piston and vacuum fillers.', 'https://www.purepens.co.uk/products/twsbi-vac-700r-clear', ['Eco', 'Diamond 580', 'Vac 700R'], ['TWSBI Eco', 'TWSBI Vac 700R']),
 B('Aurora', 'Italy', '1919', 'Premium', 'Turin pen and ink maker best known for the 88.', W + 'Aurora_(pen_manufacturer)', ['88', 'Optima'], ['Aurora 88', 'Aurora Duo-Cart']),
 B('Visconti', 'Italy', '1988', 'Luxury', 'Florence maker founded by Luigi Poli and Dante Del Vecchio, known for celluloid and filling innovations.', W + 'Visconti_(company)', ['Homo Sapiens', 'Opera', 'Divina'], ['Visconti Homo Sapiens']),
 B('Montegrappa', 'Italy', '1912', 'Luxury', 'Bassano del Grappa maker of gold nibs and hand-crafted pens.', W + 'Montegrappa', ['Extra 1930', 'Dragon'], []),
 B('OMAS', 'Italy', '1925', 'Luxury', 'Bologna maker founded by Armando Simoni, closed 2016 and revived 2023.', W + 'OMAS', ['Arte Italiana', '360'], ['OMAS Arte Italiana']),
 B('Cross', 'United States', '1846', 'Mainstream gift pens', 'Providence writing-instrument maker known for slim metal pens.', W + 'A._T._Cross_Company', ['Century', 'Townsend'], ['Cross Century'], ['Sheaffer']),
 B('Graf von Faber-Castell', 'Germany', '1993', 'Luxury', 'Premium brand of Faber-Castell launched by Count Anton-Wolfgang von Faber-Castell.', W + 'Graf_von_Faber-Castell', ['Classic', 'Guilloche', 'Intuition', 'Pen of the Year'], ['Graf von Faber-Castell Classic']),
 B('Mabie Todd', 'United Kingdom', '', 'Vintage', 'Maker of Swan fountain pens.', 'knowledge', ['Swan'], ['Swan Safety Screw-Cap']),
]
trads = [
 {'n': 'Maki-e', 'g': 'Lacquer & urushi', 'r': 'Japan', 'p': 'Heian period to present', 'd': 'Japanese lacquer decoration in which metal powder is sprinkled onto designs drawn in wet lacquer.',
  'tech': 'hira maki-e, togidashi maki-e, taka maki-e, shishiai togidashi', 'mat': 'urushi; gold, silver, copper and alloy powders', 'forms': ['Namiki maki-e pens', 'Nakaya urushi pens', 'Danitrio Genkai'],
  'ctr': ['Kōami school', 'Igarashi school', 'Namiki (Pilot) artisans'], 'auth': 'hand-applied raised or polished metal powder, artist signature on lacquer pens', 's': W + 'Maki-e'},
 {'n': 'Wajima-nuri', 'g': 'Lacquer & urushi', 'r': 'Wajima, Ishikawa, Japan', 'p': 'early Edo period (Kanbun era) to present', 'd': 'Wajima lacquerware with a very durable urushi undercoat mixed with powdered diatomaceous earth.',
  'tech': 'multi-layer ji-no-ko undercoat; chinkin and maki-e decoration', 'mat': 'urushi, ji-no-ko (diatomaceous earth), zelkova wood', 'forms': ['Nakaya urushi pens'], 'ctr': ['Wajima'], 'auth': 'layered ji-no-ko base, Wajima origin', 's': W + 'Wajima-nuri'},
 {'n': 'Celluloid pen making', 'g': 'Plastics & pen materials', 'r': 'United States, Europe', 'p': '1920s to present', 'd': 'Pens turned from nitrocellulose plastic blocks in pearl, striped and marbled patterns.',
  'tech': 'turning and machining celluloid rod and block', 'mat': 'celluloid (pyroxylin), sold as Radite, Permanite, Pyralin', 'forms': ['Sheaffer Lifetime', 'Parker Duofold', 'Parker Vacumatic', 'Waterman Patrician'],
  'ctr': ['Sheaffer', 'Parker', 'DuPont'], 'auth': 'warm translucent depth, camphor smell, ageing discolouration', 's': W + 'Radite'},
]
notes = ('Old flat list of 68 models split by filling system into six kinds with 46 archetypes; old models became versions where they belong (Pelikan M815/M1000, Montblanc 149, Pilot Custom 742/Heritage 912, Capless/VP, Sailor King of Pen, Nakaya Portable Cigar, Waterman Patrician/Lady Patricia, Parker 51/Duofold/Vacumatic, Sheaffer Balance/Snorkel/PFM/Touchdown, Lamy Safari, Kaweco Classic/Lunar Sport, TWSBI Eco, Visconti Homo Sapiens, Platinum Preppy, Pilot Kakuno, Cross Century II, Esterbrook J). '
 'Remaining old models kept in m of the kind where they fit best; old ranges Rhodia and TRAVELER\'S COMPANY BRASS folded into models. Dropped novelty/SKU-only: Keyno Stay.tionery Key, Komamono Lab Fonte, Writech Clictek. '
 'Not added for lack of a retrieved page: Montblanc 146 details beyond name, Sheaffer Vac-Fil pen, Conway Stewart, Ranga/Wancher eyedroppers, Pilot Jumbo, Platinum President/Izumo placement. nakaya.org and fountainpen.it blocked. '
 'Danitrio country/founding and Conklin founding year left blank (not confirmed). Filling placement of some m models (Parker 45/75, TWSBI 580, Aurora Optima, OMAS 360) follows the plan, not a retrieved page.')
out = {'kinds': [cc, pis, vac, sac, eye, ret], 'brands': brands, 'traditions': trads, 'notes': notes}
p = 'work/C5/shelves/00_00.json'
json.dump(out, open(p + '.tmp', 'w'), ensure_ascii=False, indent=1); os.replace(p + '.tmp', p)
print('archetypes', sum(len(k.get('x', [])) for k in out['kinds']))
