import json, os
W = 'https://en.wikipedia.org/wiki/'
DP = W + 'Glass_dip_pen'
TOMS = 'https://tomsstudio.com/pages/calligraphy-nib-guide'
SCR = 'https://scribblers.co.uk/collections/copperplate-nibs?page=1'
TOP5 = 'https://scribblers.co.uk/blogs/news/top-5-best-selling-nibs-for-traditional-calligraphy-and-why-we-like-them'
MES = 'https://mes.net.au/products/speedball-nib-holders'
def X(n, d, mk, y, s, v=(), a='', dt=''):
    o = {'n': n, 'a': a, 'd': d, 'mk': mk, 'y': y, 's': s, 'v': [dict(zip(('n', 'mk', 'y', 'd'), t)) for t in v]}
    if dt: o['dt'] = dt
    return o

holder = {'n': 'Dip pen holder', 'a': 'nib holder · penholder · dip pen',
 'd': 'Handle that grips a loose dip-pen nib; straight for most work, oblique for slanted pointed-pen scripts.',
 't': ['straight', 'oblique (flanged)', 'crow-quill', 'wood, resin or glass handle'], 's': 'https://www.jetpens.com/Dip-Pens/ct/6932',
 'x': [
  X('Oblique pen holder', 'Holder with an offset flange that sets the nib at about 55° for Copperplate and Spencerian.', '', '19th century', DP,
    [('Speedball Oblique Pen Holder', 'Speedball', '', 'fits pointed nibs 22B, 56, 99, 100, 101, 103')], dt='flange metal or 3D-printed · handle wood or plastic · left-hand versions'),
  X('Speedball Standard Nib Holder', 'Plain straight holder that takes Speedball broad lettering nibs and most pointed nibs.', 'Speedball', '', MES,
    [('Standard Nib Holder', 'Speedball', '', 'A, B, C and LC nibs plus pointed nibs'), ('#102 Crow Quill Holder', 'Speedball', '', 'for crow-quill nibs 102, 107, 108'), ('#104 Crow Quill Holder', 'Speedball', '', 'for nibs 100, 103, 104')],
    dt='black, mahogany or black and gold'),
  X('Tachikawa comic nib holder', 'Japanese wooden holder with rubber rings that grip G, school and maru nibs, favoured for manga inking.', 'Tachikawa', '', 'https://yosekastationery.com/products/tachikawa-clear-nib-holder',
    [('T-40', 'Tachikawa', '', '14.8 cm wood holder with cap'), ('T-25', 'Tachikawa', '', 'shorter holder')], dt='wood or resin · fits G, Maru, School, Spoon nibs'),
 ],
 'm': [['Brause Ergonomic Nib Holder', 'Brause'], ['Kakimori Nib Holder', 'Kakimori'], ['Pilot Iro-Utsushi', 'Pilot'], ['Sailor Hocoro', 'Sailor']]}

nib = {'n': 'Dip pen nib', 'a': 'calligraphy nib · pen nib · crow quill',
 'd': 'Loose steel nib for a dip-pen holder: pointed and flexible for Copperplate, or broad-edged for italic and lettering.',
 't': ['pointed flexible', 'pointed firm', 'broad-edge (square cut)', 'left oblique', 'crow quill', 'fitted reservoir', 'slip-on reservoir'], 's': SCR,
 'x': [
  X('Gillott 303', 'Sharp, flexible Birmingham pointed nib giving fine hairlines; a Copperplate standard.', 'Gillott', '', TOMS,
    [('303', 'Gillott', '', 'flexible'), ('404', 'Gillott', '', 'moderate flex, beginner-friendly')]),
  X('William Mitchell Round Hand', 'Square-cut English broad-edge nib in ten sizes with a slip-on reservoir.', 'William Mitchell', '', TOP5,
    [('Round Hand', 'William Mitchell', '', 'square cut or left oblique'), ('Italic', 'William Mitchell', '', 'gold-coloured, 1R–5R and 1L–5L'), ('Copperplate', 'William Mitchell', '', 'pointed'), ('Post Office', 'William Mitchell', '', 'pointed')],
    dt='size number = stroke width'),
  X('Speedball lettering nibs', 'American lettering nib series by tip shape, first released by Hunt in 1915.', 'Speedball', '1915', W + 'Speedball_(art_products)',
    [('A-style', 'Speedball', '1915', 'square tip'), ('B-style', 'Speedball', '', 'round tip'), ('C-style', 'Speedball', '', 'chisel; C0 largest to C6'), ('D-style', 'Speedball', '', 'oval; discontinued'), ('LC', 'Speedball', '', 'left-handed C')],
    dt='fitted reservoir'),
  X('Brause EF66', 'Very small, highly flexible pointed nib for advanced pointed-pen work.', 'Brause', '', TOMS, [('66EF', 'Brause', '', 'arrow-stamped')]),
  X('Brause 361 Steno', 'Brause pointed steno nib, sold as the Blue Pumpkin.', 'Brause', '', SCR, a='Blue Pumpkin'),
  X('Brause Bandzug', 'German broad-edge nib with fitted reservoir, in ten sizes.', 'Brause', '', TOP5, dt='size number = width in mm · left oblique sizes'),
  X('G-pen nib', 'Japanese manga nib with medium flex and moderately sharp point; a common first pointed nib.', '', '', TOMS,
    [('Nikko G', 'Nikko', '', 'medium flex all-rounder'), ('Zebra G', 'Zebra', '', 'firmer, fine point'), ('Tachikawa G', 'Tachikawa', '', 'easy flex')]),
  X('Hunt 101', 'Flexible American pointed nib stamped Imperial.', 'Speedball', '', SCR,
    [('101', 'Speedball', '', 'Imperial'), ('22B', 'Speedball', '', 'extra fine'), ('56', 'Speedball', '', ''), ('99', 'Speedball', '', ''), ('513EF Globe', 'Speedball', '', '')], a='Hunt Imperial'),
  X('Leonardt EF Principal', 'Extra-fine, highly flexible pointed nib for expressive downstrokes.', 'Leonardt', '', TOMS,
    [('EF Principal', 'Leonardt', '', ''), ('Steno 40', 'Leonardt', '', 'highly flexible, large lettering'), ('Index', 'Leonardt', '', 'moderate flex'), ('Crown', 'Leonardt', '', ''), ('TAPE', 'Leonardt', '', 'broad-edge, integrated reservoir')]),
 ],
 'm': [['Esterbrook 442 Jackson Stub', 'Esterbrook']]}

glass = {'n': 'Glass pen', 'a': 'glass dip pen · ガラスペン', 'd': 'Dip pen with a spiral-grooved glass tip that holds ink by capillary action.',
 't': ['glass tip on wooden or bamboo handle', 'all-glass', 'twisted handle'], 's': 'https://shop.japanhouselondon.uk/producers/sase-kogyosho/',
 'x': [
  X('Sasaki glass pen', 'Japanese grooved glass-tipped dip pen devised by wind-chime maker Sadajirō Sasaki.', 'Sase Kogyosho', '1902', 'https://shop.japanhouselondon.uk/producers/sase-kogyosho/',
    [('Glass tip, bamboo handle', 'Sase Kogyosho', '1912', 'early workshop form'), ('All-glass pen', 'Sase Kogyosho', '1989', 'devised by Sase Isamu')], dt='eight-groove tip · twisted handle · colour'),
 ],
 'm': [['Jacques Herbin Twisted Glass Pen', 'Jacques Herbin'], ['Wearingeul Glass Dip Pen', 'Wearingeul']]}

cfp = {'n': 'Calligraphy fountain pen', 'a': 'italic pen · broad-nib fountain pen', 'd': 'Fountain pen with a broad, italic or parallel-plate nib for edged-pen lettering.',
 't': ['stub or italic nib', 'parallel-plate nib', 'fude (bent) nib', 'interchangeable nib set'], 's': 'https://goldspot.com/collections/calligraphy-pens?page=1',
 'x': [
  X('Pilot Parallel', 'Calligraphy pen whose nib is two parallel steel plates, giving crisp edges; colours can be blended.', 'Pilot', '', 'https://www.jennibick.com/products/pilot-parallel-calligraphy-pen',
    [('1.5 mm', 'Pilot', '', ''), ('2.4 mm', 'Pilot', '', ''), ('3.0 mm', 'Pilot', '', ''), ('3.8 mm', 'Pilot', '', ''), ('4.5 mm', 'Pilot', '', ''), ('6.0 mm', 'Pilot', '', '')], dt='mixable colour cartridges'),
  X('Lamy Joy', 'Long tapered calligraphy pen with a Safari-style grip and steel italic nibs, designed by Wolfgang Fabian.', 'Lamy', '', 'https://www.lamy.com/en-ca/p/lamy-joy-al-fountain-pen',
    [('Joy', 'Lamy', '', 'plastic, 1.5 mm stub'), ('Joy AL', 'Lamy', '', 'aluminium cap'), ('Joy calligraphy set', 'Lamy', '', '1.1, 1.5 and 1.9 mm nibs')], dt='left-handed nibs · T10 cartridge or Z 28 converter'),
  X('Kaweco calligraphy set', 'Kaweco pen sold with interchangeable italic nibs.', 'Kaweco', '', 'https://goldspot.com/collections/calligraphy-pens?page=1',
    [('Perkeo Calligraphy Set', 'Kaweco', '', '1.1, 1.5, 1.9 mm'), ('Calligraphy set', 'Kaweco', '', '1.5 and 2.3 mm'), ('Twin-nib calligraphy pen', 'Kaweco', '', '')]),
 ],
 'm': [['Sailor Compass HighAce Neo Calligraphy', 'Sailor'], ['Sailor Fude De Mannen', 'Sailor'], ['Monteverde Monza ID calligraphy set', 'Monteverde']]}

SEGS = {}
def B(n, c, f, seg, kf, d, s, lines=(), sig=()):
    return {'n': n, 'c': c, 'f': f, 'seg': seg, 'kf': kf, 'd': d, 'lines': list(lines), 'eras': [], 'sig': list(sig), 'sc': [], 'rel': [], 's': s}
brands = [
 B('Gillott', 'United Kingdom', '1827', 'Heritage manufactory', 'steel dip-pen nibs', 'Birmingham steel-nib maker founded by Joseph Gillott.', W + 'Joseph_Gillott', ['303', '404'], ['Gillott 303']),
 B('William Mitchell', 'United Kingdom', '', 'Heritage manufactory', 'broad-edge calligraphy nibs', 'Birmingham steel-pen firm of the Mitchell family, pioneers of machine-cut nibs.', DP, ['Round Hand', 'Italic'], ['William Mitchell Round Hand']),
 B('Speedball', 'United States', '1899', 'Mainstream', 'lettering nibs, holders, printmaking', 'Successor to C. Howard Hunt\'s Camden pen company; independent since 1997.', W + 'Speedball_(art_products)', ['Speedball A–D', 'Hunt'], ['Speedball lettering nibs', 'Hunt 101']),
 B('Brause', 'Germany', '1850', 'Heritage manufactory', 'calligraphy nibs', 'German maker of pointed and broad-edge calligraphy nibs.', 'knowledge', ['EF66', '361 Steno', 'Bandzug'], ['Brause EF66', 'Brause Bandzug']),
 B('Leonardt', 'United Kingdom', '1856', 'Heritage manufactory', 'calligraphy nibs', 'Birmingham nib maker D. Leonardt & Co.', DP, ['Principal', 'Steno', 'TAPE'], ['Leonardt EF Principal']),
 B('Nikko', 'Japan', '', 'Specialist', 'manga nibs', 'Japanese maker of comic and calligraphy nibs.', 'knowledge', ['G'], ['G-pen nib']),
 B('Zebra', 'Japan', '1897', 'Mainstream', 'pens and comic nibs', 'Japanese pen maker that also makes comic nibs.', 'knowledge', ['G'], []),
 B('Tachikawa', 'Japan', '', 'Specialist', 'manga nibs and holders', 'Japanese maker of comic nibs and nib holders.', 'knowledge', ['T-40', 'T-25', 'G'], ['Tachikawa comic nib holder']),
 B('Sase Kogyosho', 'Japan', '1912', 'Artisan & independent', 'glass pens', 'Tokyo workshop continuing Sadajirō Sasaki\'s glass pen technique.', 'https://shop.japanhouselondon.uk/producers/sase-kogyosho/', ['glass pens'], ['Sasaki glass pen']),
 B('Pilot', 'Japan', '1918', 'Mainstream', 'pens and inks', 'Japan\'s largest pen maker.', W + 'Pilot_(pen_company)', ['Parallel'], ['Pilot Parallel']),
 B('Lamy', 'Germany', '1930', 'Premium', 'design pens', 'Heidelberg design-led pen maker.', W + 'Lamy', ['Joy', 'Safari'], ['Lamy Joy']),
 B('Kaweco', 'Germany', '1883', 'Value', 'pocket pens', 'Heidelberg-rooted pen maker known for the Sport.', W + 'Kaweco', ['Sport', 'Perkeo'], ['Kaweco calligraphy set']),
]
trads = [
 {'n': 'Copperplate', 'g': 'Writing & calligraphy', 'r': 'England, spreading to Europe and North America', 'p': '17th–19th century, revived today',
  'd': 'English roundhand script engraved in copybooks and written with a pointed flexible pen.', 'tech': 'pointed-pen shaded strokes at a steep slant', 'mat': 'flexible steel nib, oblique holder, iron gall or sumi ink',
  'forms': ['Oblique pen holder', 'Gillott 303', 'Dip pen nib'], 'ctr': ['London writing masters', 'George Bickham, The Universal Penman (1733–41)'], 'auth': 'consistent slant around 55°, shaded downstrokes, hairline upstrokes', 's': W + 'Copperplate_script'},
 {'n': 'Spencerian script', 'g': 'Writing & calligraphy', 'r': 'United States', 'p': '1840 to about 1925',
  'd': 'American business and ornamental script developed by Platt Rogers Spencer, lighter and less shaded than Copperplate.', 'tech': 'pointed-pen script with sparing shading', 'mat': 'steel pointed nib, oblique holder',
  'forms': ['Oblique pen holder', 'Hunt 101'], 'ctr': ['Platt Rogers Spencer\'s school', 'Louis Madarasz'], 'auth': 'about 52° slant, delicate unshaded lowercase', 's': W + 'Spencerian_script'},
 {'n': 'Japanese glass pen', 'g': 'Ceramics & glass', 'r': 'Tokyo, Japan', 'p': '1902 to present',
  'd': 'Hand-made glass dip pens with a grooved tip, from the technique of Sadajirō Sasaki.', 'tech': 'lampworked glass tip with eight even twists', 'mat': 'glass; bamboo or glass handle',
  'forms': ['Sasaki glass pen', 'Glass pen'], 'ctr': ['Sase Kogyosho, Tokyo'], 'auth': 'even eight-groove twist, workshop provenance; designated an Intangible Cultural Property', 's': 'https://shop.japanhouselondon.uk/producers/sase-kogyosho/'},
]
notes = ('Old Dip pen kind became Dip pen holder; its nib, glass-pen and dip-pen models were split out: Brause 361/66 EF into Dip pen nib archetypes, J. Herbin and Wearingeul glass pens into Glass pen, Tachikawa T-25/T-40 and Speedball Standard holder into holder archetypes. '
 'New kinds Dip pen nib, Glass pen and Calligraphy fountain pen sourced from retrieved pages. Not added: Hario and Fuji glass pens (no page found); Sheaffer calligraphy sets (not on any retrieved page); Hunt 22B and Speedball nib dates beyond the A-series. '
 'Brause founding year and Japanese nib makers from knowledge; Nikko and Tachikawa founding years left blank. thepostmansknock and jetpens blocked; monk.ca and stlartsupply returned 404.')
out = {'kinds': [holder, nib, glass, cfp], 'brands': brands, 'traditions': trads, 'notes': notes}
p = 'work/C5/shelves/00_01.json'
json.dump(out, open(p + '.tmp', 'w'), ensure_ascii=False, indent=1); os.replace(p + '.tmp', p)
print('archetypes', sum(len(k.get('x', [])) for k in out['kinds']))
