import json, os
W = 'https://en.wikipedia.org/wiki/'
FPI = W + 'Fountain_pen_inks'
GSB = 'https://www.gentlemanstationer.com/blog/2019/11/25/back-to-basics-blue-ink-for-everday-writing'
PLAT = 'https://shop.gentlemanstationer.com/products/platinum-classic-inks-60ml'
CC = 'https://www.gouletpens.com/blogs/fountain-pen-blog/cartridge-converter-compatibility-guide'
NIB = 'https://goldspot.com/blogs/magazine/replacement-nibs-and-which-pens-use-them'
def X(n, d, mk, y, s, v=(), a='', dt=''):
    o = {'n': n, 'a': a, 'd': d, 'mk': mk, 'y': y, 's': s, 'v': [dict(zip(('n', 'mk', 'y', 'd'), t)) for t in v]}
    if dt: o['dt'] = dt
    return o

ink = {'n': 'Fountain pen ink', 'a': 'bottled fountain-pen ink', 'd': 'Bottled ink made for fountain pens, chosen by colour, saturation, shading, sheen, flow and water resistance.',
 't': ['dye', 'pigment (nanoparticle)', 'iron gall', 'shimmer', 'high sheen', 'permanent or document-proof'], 's': 'https://www.jetpens.com/Pilot-Ink-Bottles/ct/1789',
 'x': [
  X('J. Herbin 1670', 'Anniversary line from the French ink house founded in 1670, with shimmer and sheen colours in wax-sealed bottles.', 'J. Herbin', '', 'https://www.gouletpens.com/blogs/fountain-pen-blog/jacques-herbin-1670-rouge-hematite-ink-review',
    [('Rouge Hematite', 'J. Herbin', '', 'red with gold shimmer')], a='Jacques Herbin 1670 Anniversary', dt='15 ml and 50 ml bottles · shimmer'),
  X('J. Herbin Encre', 'J. Herbin\'s standard dye inks.', 'J. Herbin', '', FPI, [('Perle Noire', 'J. Herbin', '', 'black')]),
  X('Pelikan 4001', 'Pelikan\'s long-running everyday writing ink, considered safe for nearly all pens.', 'Pelikan', '', GSB,
    [('Royal Blue', 'Pelikan', '', '30 ml, 62.5 ml and historic bottles')], dt='bottles and long standard international cartridges'),
  X('Pelikan Edelstein', 'Pelikan\'s premium gemstone-named ink line with a yearly Ink of the Year.', 'Pelikan', '', 'https://gouletpens.com/blogs/fountain-pen-blog/pelikan-edelstein-ink-of-the-year-pen-history',
    [('Turmaline', 'Pelikan', '2012', 'Ink of the Year, pink'), ('Amber', 'Pelikan', '2013', ''), ('Garnet', 'Pelikan', '2014', ''), ('Amethyst', 'Pelikan', '2015', ''), ('Aquamarine', 'Pelikan', '2016', ''),
     ('Smoky Quartz', 'Pelikan', '2017', ''), ('Olivine', 'Pelikan', '2018', ''), ('Star Ruby', 'Pelikan', '2019', ''), ('Moonstone', 'Pelikan', '2020', 'shimmer'), ('Golden Beryl', 'Pelikan', '2021', 'shimmer'),
     ('Apatite', 'Pelikan', '2022', 'shimmer'), ('Rose Quartz', 'Pelikan', '2023', ''), ('Golden Lapis', 'Pelikan', '2024', 'gold shimmer'), ('Apricot Achat', 'Pelikan', '2025', ''), ('Pyrite', 'Pelikan', '2026', 'gold shimmer')],
    dt='matching M200/M205 pens from 2015'),
  X('Parker Quink', 'Parker\'s quick-drying general-purpose ink with Solv-X additive, safe for all pens.', 'Parker', '1931', W + 'Quink', dt='bottles and Parker cartridges'),
  X('Waterman ink', 'Waterman\'s everyday bottled ink, prized as safe for vintage pens.', 'Waterman', '', GSB, [('Serenity Blue', 'Waterman', '', 'formerly Florida Blue')]),
  X('Pilot Iroshizuku', 'Pilot\'s premium line of seasonal-colour inks; the name means "coloured droplets".', 'Pilot', '', 'https://artbrown.com/blogs/brand-highlights-and-know-how/pilot-iroshizuku',
    [('Take-sumi', 'Pilot', '', 'charcoal black'), ('Shin-kai', 'Pilot', '', 'blue-black'), ('Murasaki-shikibu', 'Pilot', '', 'purple'), ('Yama-budo', 'Pilot', '', 'purple')], a='色彩雫'),
  X('Sailor Shikiori', 'Sailor\'s "Four Seasons" dye inks in small bottles, colours drawn from Japanese seasons.', 'Sailor', '', 'https://pulpaddiction.com.au/products/sailor-shikiori-bottled-ink-yamadori',
    [('Yamadori', 'Sailor', '', 'teal with red sheen; first sold as Jentle Yama-dori')], a='Jentle', dt='20 ml bottles'),
  X('Platinum Classic', 'Platinum\'s iron gall inks that darken towards black as they dry.', 'Platinum', '', PLAT,
    [('Cassis Black', 'Platinum', '', ''), ('Citrus Black', 'Platinum', '', ''), ('Forest Black', 'Platinum', '', ''), ('Khaki Black', 'Platinum', '', ''), ('Lavender Black', 'Platinum', '', ''), ('Sepia Black', 'Platinum', '', '')], dt='60 ml bottle'),
  X('Platinum Carbon', 'Platinum\'s pigmented permanent inks.', 'Platinum', '', PLAT, [('Carbon Black', 'Platinum', '', 'pigment'), ('Pigment Blue', 'Platinum', '', '')], dt='bottles and pigment cartridges'),
  X('Rohrer & Klingner iron gall', 'German iron gall inks whose colour deepens as they oxidise; considered permanent.', 'Rohrer & Klingner', '', 'https://wonderpens.ca/products/rohrer-klingner-fountain-pen-ink-50ml-eisen-gallus-tinte-salix-iron-gall-blue',
    [('Salix', 'Rohrer & Klingner', '', 'blue-black'), ('Scabiosa', 'Rohrer & Klingner', '', 'dusky purple')], a='Eisen-Gallus-Tinte', dt='50 ml bottle'),
  X('Diamine', 'Liverpool-made dye inks in a very wide colour range.', 'Diamine', '1880', W + 'Diamine_Inks_Limited'),
  X('Noodler\'s Bulletproof', 'Permanent inks whose cellulose-reactive dyes bond with paper fibres.', 'Noodler\'s', '', FPI, [('Black', 'Noodler\'s', '', 'bulletproof')]),
  X('De Atramentis Document', 'Waterproof, mixable German document inks.', 'De Atramentis', '', 'https://www.gouletpens.com/collections/de-atramentis-document-inks',
    [('Black', 'De Atramentis', '', ''), ('Cyan', 'De Atramentis', '', ''), ('Urban Grey', 'De Atramentis', '', ''), ('Urban Sienna', 'De Atramentis', '', '')], dt='45 ml bottle · Archive ink sister line'),
 ],
 'm': [['Pilot Blue-Black', 'Pilot'], ['Lamy Blue', 'Lamy'], ['Sheaffer Skrip', 'Sheaffer'], ['Private Reserve', 'Private Reserve'], ['Wancher Silk Road', 'Wancher']],
 'r': [['Pilot Iroshizuku', 'Pilot']]}

cart = {'n': 'Fountain pen cartridge', 'a': 'ink cartridge', 'd': 'Sealed plastic ink reservoir that fits a pen\'s cartridge standard: standard international or a maker\'s own.',
 't': ['standard international short', 'standard international long', 'Pilot', 'Platinum', 'Sailor', 'Lamy', 'Parker', 'Aurora', 'Cross', 'Sheaffer', 'pigment cartridge'], 's': 'https://goldspot.com/collections/fountain-pen-cartridges?page=5',
 'm': [['Pelikan 4001 Long ink cartridge', 'Pelikan'], ['Lamy T 10', 'Lamy'], ['Pilot Parallel ink cartridge', 'Pilot']]}

conv = {'n': 'Fountain pen converter', 'a': 'converter', 'd': 'Refillable piston or squeeze reservoir that fits in place of a cartridge so a pen can take bottled ink.',
 't': ['piston', 'squeeze', 'standard international', 'proprietary'], 's': 'https://www.jetpens.com/Pilot-Fountain-Pen-Converters/ct/3224',
 'm': [['Pilot CON-40', 'Pilot'], ['Pilot CON-70', 'Pilot'], ['Pilot CON-B', 'Pilot'], ['Lamy Z28', 'Lamy'], ['Lamy Z27', 'Lamy'], ['Schmidt K5', 'Schmidt'], ['Platinum converter', 'Platinum'],
       ['Sailor converter', 'Sailor'], ['Kaweco Foldable Mini Piston', 'Kaweco']]}

nib = {'n': 'Fountain pen nib', 'a': 'replacement nib · nib unit', 'd': 'Nib or complete nib unit (nib, feed and housing) sold to fit or upgrade a fountain pen.',
 't': ['#5 unit', '#6 unit', 'steel', 'gold', 'screw-in housing', 'friction fit', 'proprietary', 'custom grind'], 's': 'https://www.gouletpens.com/collections/replacement-nibs/products/goulet-6-steel-flex-nib-silver',
 'x': [
  X('JoWo nib unit', 'German screw-in nib unit, the most common replacement standard; size #6 is usual, #5 for pocket pens.', 'JoWo', '', NIB,
    [('#6', 'JoWo', '', 'common size; Monteverde, Esterbrook, Conklin, Opus 88 and others'), ('#5', 'JoWo', '', 'pocket pens')], dt='steel or gold · coloured finishes · stock and custom grinds'),
  X('Bock nib unit', 'German nib unit fitted by Kaweco, Graf von Faber-Castell, Caran d\'Ache and others.', 'Bock', '', NIB),
  X('Schmidt nib unit', 'German nib unit in #5 and #6 sizes.', 'Schmidt', '', NIB, [('#6', 'Schmidt', '', ''), ('#5', 'Schmidt', '', '')]),
 ],
 'm': [['Goulet #6 steel nib', 'Goulet Pens']]}

def B(n, c, f, seg, kf, d, s, sig=()):
    return {'n': n, 'c': c, 'f': f, 'seg': seg, 'kf': kf, 'd': d, 'lines': [], 'eras': [], 'sig': list(sig), 'sc': [], 'rel': [], 's': s}
brands = [
 B('J. Herbin', 'France', '1670', 'Heritage manufactory', 'inks and sealing wax', 'French ink house often called the oldest fountain-pen ink maker.', FPI, ['J. Herbin 1670', 'J. Herbin Encre']),
 B('Pelikan', 'Germany', '1838', 'Premium', 'pens and inks', 'Hanover maker of 4001 and Edelstein inks.', 'knowledge', ['Pelikan 4001', 'Pelikan Edelstein']),
 B('Parker', 'United States', '1888', 'Mainstream', 'pens and Quink', 'Pen maker that introduced Quink in 1931.', W + 'Parker_Pen_Company', ['Parker Quink']),
 B('Waterman', 'United States', '1884', 'Mainstream', 'pens and inks', 'Pen maker now based in Paris.', W + 'Waterman_S._A.', ['Waterman ink']),
 B('Pilot', 'Japan', '1918', 'Mainstream', 'pens and inks', 'Japan\'s largest pen maker.', W + 'Pilot_(pen_company)', ['Pilot Iroshizuku']),
 B('Sailor', 'Japan', '1911', 'Premium', 'pens and inks', 'Kure pen and ink maker.', W + 'Sailor_(pen_company)', ['Sailor Shikiori']),
 B('Platinum', 'Japan', '1919', 'Mainstream', 'pens and inks', 'Tokyo pen maker, first to sell a cartridge pen (1956).', W + 'Platinum_Pen_Company', ['Platinum Classic', 'Platinum Carbon']),
 B('Rohrer & Klingner', 'Germany', '1892', 'Heritage manufactory', 'inks', 'German ink maker with roots in lithography from 1892, using traditional recipes.', 'https://wonderpens.ca/products/rohrer-klingner-fountain-pen-ink-50ml-eisen-gallus-tinte-salix-iron-gall-blue', ['Rohrer & Klingner iron gall']),
 B('Diamine', 'United Kingdom', '1864', 'Heritage manufactory', 'inks', 'Liverpool ink maker founded as T. Webster and Co.; Diamine line from 1880.', W + 'Diamine_Inks_Limited', ['Diamine']),
 B('Noodler\'s', 'United States', '2004', 'Artisan & independent', 'inks', 'Small American ink maker founded by Nathan Tardif, known for bulletproof inks.', 'knowledge', ['Noodler\'s Bulletproof']),
 B('De Atramentis', 'Germany', '', 'Specialist', 'inks', 'German maker of document, archive and scented inks.', 'knowledge', ['De Atramentis Document']),
 B('JoWo', 'Germany', '', 'Specialist', 'nib units', 'German maker of nib units used by many pen brands.', 'knowledge', ['JoWo nib unit']),
 B('Bock', 'Germany', '', 'Specialist', 'nib units', 'German maker of nibs and nib units for many pen brands.', 'knowledge', ['Bock nib unit']),
 B('Schmidt', 'Germany', '', 'Specialist', 'refills, converters, nib units', 'German maker of refills, converters and nib units.', 'knowledge', ['Schmidt nib unit']),
]
notes = ('Old kinds kept one-to-one. Ink reorganised as maker → line (archetype) → named colours (versions); Pilot Iroshizuku range kept as an archetype. Cartridges and converters kept as types plus a short model list (no SKU dumps); nibs get JoWo, Bock and Schmidt unit archetypes. '
 'Not added for lack of a retrieved page: Montblanc, Kaweco and Sailor Studio ink lines, Diamine Shimmertastic and named Diamine colours, Pelikan 4001 Blue-Black and Brilliant Black, Iroshizuku colours beyond four, Pelikan nib units. '
 'No traditions (inks and nibs are industrial). Brand facts for Pelikan, Noodler\'s, De Atramentis, JoWo, Bock and Schmidt from knowledge; unknown founding years left blank. unsharpen.com blocked; pelikan-collectibles empty; pelikan mam 503; purepens Noodler\'s page 404.')
out = {'kinds': [ink, cart, conv, nib], 'brands': brands, 'traditions': [], 'notes': notes}
p = 'work/C5/shelves/00_03.json'
json.dump(out, open(p + '.tmp', 'w'), ensure_ascii=False, indent=1); os.replace(p + '.tmp', p)
print('archetypes', sum(len(k.get('x', [])) for k in out['kinds']))
