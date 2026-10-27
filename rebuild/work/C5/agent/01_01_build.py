import json, os
W = 'https://en.wikipedia.org/wiki/'
PA = 'https://www.penaddict.com/blog/'
UNI = 'Mitsubishi Pencil (Uni)'
PLQ = 'https://www.pilotpen.co.uk/our-products/liquid-ink-pens/'


def X(n, d, mk, y, s, v=(), a='', dt=''):
    o = {'n': n, 'a': a, 'd': d, 'mk': mk, 'y': y, 's': s, 'v': [dict(zip(('n', 'mk', 'y', 'd'), t)) for t in v]}
    if dt: o['dt'] = dt
    return o


fine = {'n': 'Fineliner', 'a': 'felt-tip pen · fibre-tip pen · drawing pen · sign pen',
 'd': 'Fine fibre-tip pen for writing and drawing, often with archival pigment ink.',
 't': ['pigment (archival)', 'dye-based', 'metal-sleeved tip', 'sign pen (broader fibre tip)'],
 's': W + 'Marker_pen',
 'x': [
  X('Pentel Sign Pen', 'The first fibre-tip pen, water-based ink fed through a fibre point; flown on Gemini in 1966.', 'Pentel', '1962',
    'https://collection.sciencemuseumgroup.org.uk/objects/co8057267/sign-pen-the-first-fibre-tip-pen-1962-pen',
    [('Sign Pen', 'Pentel', '1963', 'launched commercially; invented 1962 by Masao Miura and Yukio Horie')]),
  X('Sakura Pigma Micron', 'The first water-based pigment fineliner, an archival standard for drawing and writing.', 'Sakura', '1982',
    'https://sakuracraypas.com/inspiration/history-of-pigma-micron', [('Pigma Micron', 'Sakura', '1982', 'water-based pigment ink')]),
  X('Stabilo Point 88', 'Hexagonal orange-and-white striped fineliner with a metal-sleeved 0.4 mm tip; over 3 billion sold.', 'Stabilo', '',
    'https://www.stabilo.com/uk/fineliner-stabilo-point-88/8850-6', [('Point 88', 'Stabilo', '', '0.4 mm, 65 colours')], dt='65 colours incl. neon'),
  X('Staedtler Pigment Liner', 'Archival pigment fineliner, close rival to the Micron, with a long cap-off time.', 'Staedtler', '',
    PA + '2014/10/31/staedtler-pigment-liner-01-mm-review', [('Pigment Liner 0.1', 'Staedtler', '', ''), ('Pigment Liner 0.3', 'Staedtler', '', '')]),
  X('Uni Pin', 'Waterproof pigment fineliner comparable to the Micron at a lower price.', UNI, '', PA + '2024/5/1/uni-pin-038mm-fineliner-pen-review',
    [('Pin 03 (0.38 mm)', UNI, '', ''), ('Pin 01 (0.28 mm)', UNI, '', '')], dt='0.03–0.8 mm · black, blue, red, grey, brown'),
 ],
 'm': [['KOKUYO WP Finewriter', 'KOKUYO'], ['Uni EMOTT', UNI], ['Pentel Pulaman JM20', 'Pentel'], ['Pilot V-Sign Pen', 'Pilot']]}

hil = {'n': 'Highlighter', 'a': 'highlighter pen · text marker · 蛍光ペン',
 'd': 'Broad-tip pen with translucent fluorescent or pastel ink for marking text.',
 't': ['chisel tip', 'dual tip', 'pastel / mild colours', 'gel stick', 'dry (tape)', 'erasable', 'refillable', 'retractable'],
 's': W + 'Highlighter',
 'x': [
  X('Carter\'s Hi-Liter', 'The first highlighter, invented by Dr Frank Honn; brand now owned by Avery Dennison.', 'Carter\'s', '1963', W + 'Highlighter',
    [('Hi-Liter', 'Carter\'s', '1963', ''), ('Hi-Liter', 'Avery Dennison', '1975', 'after Avery acquired Carter\'s')]),
  X('Stabilo Boss Original', 'Chisel-tip highlighter, Europe\'s best seller since 1971.', 'Stabilo', '1971', 'https://prod.stabilo.com/us/products/highlighting/highlighters/stabilo-boss-original/',
    [('Boss Original', 'Stabilo', '1971', '9 fluorescent colours'), ('Boss Original Pastel', 'Stabilo', '', '6 pastel colours'), ('Boss refill 070', 'Stabilo', '', '')],
    dt='2 and 5 mm lines'),
  X('Faber-Castell Textliner 48', 'Classic chisel-tip highlighter, refillable from a refill station.', 'Faber-Castell', '', 'https://penstore.com/en/prod-s/faber-castell-textliner',
    [('Textliner 48', 'Faber-Castell', '', '1, 2 and 5 mm lines'), ('Textliner 1549 refill station', 'Faber-Castell', '', '')], dt='six super-fluorescent colours'),
  X('Zebra Mildliner', 'Double-ended highlighter in muted "mild" colours.', 'Zebra', '', 'https://www.wellappointeddesk.com/2014/09/review-zebra-mildliner-pen-in-mild-green/',
    [('Mildliner double-sided', 'Zebra', '', 'fine and bold tips, 15 colours')]),
  X('Pilot FriXion Light', 'Erasable highlighter using FriXion thermochromic ink.', 'Pilot', '', 'https://pilot.co.jp/media_english/005/', [('FriXion Light', 'Pilot', '', '')]),
 ],
 'm': [['Pilot Spotliter VW', 'Pilot'], ['edding 24 EcoLine', 'edding'], ['Pilot Kire-Na', 'Pilot'], ['Uni Propus Window', UNI], ['Zebra Kirarich', 'Zebra'],
       ['Kuretake Brush High-Lite Quick C+', 'Kuretake'], ['Marvy PastelLiner', 'Marvy']]}

perm = {'n': 'Permanent marker', 'a': 'marker pen · marker · Sharpie',
 'd': 'Fibre or felt-tip marker with water-resistant ink for marking and labelling paper, plastic, glass, metal and fabric.',
 't': ['bullet tip', 'chisel tip', 'twin tip', 'paint marker', 'laundry / name marker'],
 's': W + 'Marker_pen',
 'x': [
  X('Magic Marker', 'Glass-bottle felt-wick marker that popularised markers.', 'Magic Marker', '1953', W + 'Marker_pen', [('Magic Marker', 'Magic Marker', '1953', 'Sidney Rosenthal')]),
  X('Sharpie Fine Point', 'Pen-style permanent marker from Sanford; the US generic name for a marker.', 'Sharpie', '1964', 'https://www.sharpie.com/about',
    [('Fine Point', 'Sharpie', '1964', 'first Sharpie permanent marker'), ('S-Gel', 'Sharpie', '', 'gel pen spin-off')]),
  X('edding 3000', 'Round-tip German permanent marker, top of a 2007/08 GfK best-seller study in seven European countries.', 'edding', '', 'https://www.edding.com/history/',
    [('edding No. 1', 'edding', '1960', 'first edding marker'), ('edding 3000', 'edding', '', ''), ('edding 750 paint marker', 'edding', '1978', 'first edding paint marker')]),
  X('Zebra Mckee', 'Double-ended oil-based marker with bold and fine tips, unchanged in design since 1976.', 'Zebra', '1976', 'https://www.zebra.co.jp/global/products/mckee/',
    [('Hi-Mckee', 'Zebra', '1976', 'bold and fine'), ('Onamae Mackee', 'Zebra', '', 'name marker for fabric and belongings')], a='Mackee · McKee'),
 ],
 'm': [['KOKUYO Mark+ 2 Way', 'KOKUYO'], ['Kuretake ZIG Clean Color Dot', 'Kuretake'], ['Sun-Star LAMECO', 'Sun-Star']]}

dry = {'n': 'Dry-erase marker', 'a': 'whiteboard marker · board marker',
 'd': 'Marker with erasable ink that wipes dry off whiteboards and other non-porous surfaces.',
 't': ['bullet tip', 'chisel tip', 'low-odour', 'refillable', 'wet-erase (for overhead film)'],
 's': W + 'Marker_pen',
 'x': [
  X('Expo dry-erase marker', 'US whiteboard marker that popularised dry-erase ink from 1976.', 'Expo', '1976', 'https://asop.mnmsa.org/2021/10/14/a-brief-history-and-invention-of-the-expo-marker/',
    [('Expo', 'Expo', '1976', '')]),
  X('Pilot V-Board Master', 'Refillable recycled-plastic whiteboard marker with liquid ink and an ink-feed system.', 'Pilot', '', PLQ, [('V-Board Master', 'Pilot', '', 'refillable')]),
 ]}

brush = {'n': 'Brush pen', 'a': 'fudepen · 筆ペン · sign brush pen',
 'd': 'Pen with a flexible brush or felt brush tip for handwriting, lettering and calligraphy; drawing brush pens are in Craft & Art Supplies.',
 't': ['felt brush tip (firm)', 'bristle brush tip', 'cartridge-fed (refillable)', 'disposable', 'double-sided'],
 's': 'https://www.jetpens.com/Brush-Pens/ct/221',
 'x': [
  X('Pentel Fude Touch Sign Pen', 'Soft brush tip in the classic Sign Pen barrel; marker-like with modest line variation.', 'Pentel', '', PA + '2013/3/29/pentel-fude-touch-sign-pen-review',
    [('Fude Touch Sign Pen', 'Pentel', '', '')]),
  X('Tombow Fudenosuke', 'Small felt brush pen in hard and soft versions, a lettering favourite.', 'Tombow', '', PA + '2010/10/20/review-tombow-fudenosuke-brush-pens.html',
    [('Fudenosuke hard tip', 'Tombow', '', 'steadier line for lettering'), ('Fudenosuke soft tip', 'Tombow', '', 'more line variation')]),
  X('Kuretake Fudegokochi', 'Firm felt-tip brush pen for legible brush handwriting; line 0.4–1.8 mm.', 'Kuretake', '', 'https://penaddict.com/blog/2019/1/17/kuretake-fudegokochi-brush-pen-review',
    [('Fudegokochi', 'Kuretake', '', 'not waterproof')]),
  X('Pentel Pocket Brush', 'Fude-style brush pen with replaceable waterproof ink cartridges.', 'Pentel', '2010s', W + 'Pentel', [('Pocket Brush', 'Pentel', '', 'replaceable cartridges')]),
 ],
 'm': [['Kuretake No. 8 Fountain Brush Pen', 'Kuretake'], ['Pilot Shunpitsu Pocket Brush Pen', 'Pilot'], ['Sailor Shikiori Double-Sided Brush Pen', 'Sailor'], ['Zebra Disposable Brush Pen', 'Zebra']]}


def B(n, c, f, seg, kf, d, s, lines=(), sig=()):
    return {'n': n, 'c': c, 'f': f, 'seg': seg, 'kf': kf, 'd': d, 'lines': list(lines), 'eras': [], 'sig': list(sig), 'sc': [], 'rel': [], 's': s}


brands = [
 B('Pentel', 'Japan', '1946', 'Mainstream', 'Sign Pen, markers', 'Tokyo maker founded by Yukio Horie as Dai Nippon Bungu; inventor of the fibre-tip pen.', W + 'Pentel', ['Sign Pen', 'Pocket Brush', 'EnerGel'], ['Pentel Sign Pen', 'Pentel Fude Touch Sign Pen']),
 B('Sakura', 'Japan', '1921', 'Mainstream', 'archival fineliners', 'Osaka crayon and pen maker behind the Pigma Micron.', 'knowledge', ['Pigma Micron', 'Gelly Roll'], ['Sakura Pigma Micron']),
 B('Stabilo', 'Germany', '1855', 'Mainstream', 'highlighters, fineliners', 'Schwan-Stabilo of Heroldsberg, maker of the Boss and Point 88.', 'knowledge', ['Boss Original', 'Point 88'], ['Stabilo Boss Original', 'Stabilo Point 88']),
 B('Staedtler', 'Germany', '1835', 'Mainstream', 'pencils, drawing pens', 'Nuremberg writing and drawing instrument maker.', 'knowledge', ['Pigment Liner', 'Lumocolor', 'Noris'], ['Staedtler Pigment Liner']),
 B(UNI, 'Japan', '1887', 'Mainstream', 'Jetstream, Uni-ball', 'Tokyo pen and pencil maker selling as Uni and Uni-ball.', 'knowledge', ['Pin', 'Propus', 'Jetstream'], ['Uni Pin']),
 B('Carter\'s', 'United States', '', 'Heritage manufactory', 'ink, Hi-Liter', 'Ink maker that introduced the highlighter; acquired by Avery Dennison in 1975.', W + 'Highlighter', ['Hi-Liter'], ['Carter\'s Hi-Liter']),
 B('Faber-Castell', 'Germany', '1761', 'Mainstream', 'pencils, highlighters', 'Stein pencil maker founded by Kaspar Faber.', 'knowledge', ['Textliner', 'Castell 9000'], ['Faber-Castell Textliner 48']),
 B('Zebra', 'Japan', '1897', 'Mainstream', 'pens and markers', 'Tokyo pen maker of the Mckee and Mildliner.', 'knowledge', ['Mckee', 'Mildliner', 'Sarasa'], ['Zebra Mckee', 'Zebra Mildliner']),
 B('Pilot', 'Japan', '1918', 'Mainstream', 'pens and inks', 'Japan\'s largest pen maker.', 'knowledge', ['FriXion', 'V-Board Master', 'Spotliter'], ['Pilot FriXion Light', 'Pilot V-Board Master']),
 B('Sharpie', 'United States', '1964', 'Mainstream', 'permanent markers', 'Marker brand of Sanford (founded 1857 in Worcester, Massachusetts), now Newell Brands.', 'https://www.sharpie.com/about', ['Fine Point', 'S-Gel'], ['Sharpie Fine Point']),
 B('edding', 'Germany', '1960', 'Mainstream', 'permanent markers', 'Hamburg marker maker founded by Carl-Wilhelm Edding and Volker Detlef Ledermann.', 'https://www.edding.com/history/', ['3000', '750', 'EcoLine'], ['edding 3000']),
 B('Magic Marker', 'United States', '1953', 'Heritage manufactory', 'felt markers', 'Sidney Rosenthal\'s marker brand that popularised felt-tip markers.', W + 'Marker_pen', ['Magic Marker'], ['Magic Marker']),
 B('Expo', 'United States', '', 'Mainstream', 'whiteboard markers', 'Dry-erase marker brand of Sanford, now Newell Brands.', 'https://asop.mnmsa.org/2021/10/14/a-brief-history-and-invention-of-the-expo-marker/', ['Expo'], ['Expo dry-erase marker']),
 B('Tombow', 'Japan', '1913', 'Mainstream', 'pencils, brush pens', 'Tokyo stationery maker of the Mono and Fudenosuke.', 'knowledge', ['Fudenosuke', 'Mono'], ['Tombow Fudenosuke']),
 B('Kuretake', 'Japan', '1902', 'Heritage manufactory', 'sumi ink, brush pens', 'Nara maker of sumi ink and brush pens.', 'knowledge', ['Fudegokochi', 'ZIG'], ['Kuretake Fudegokochi']),
]

notes = ('Felt-tip pen renamed Fineliner; Marker pen renamed Permanent marker; Dry-erase marker added as a new kind (sourced to the Marker pen article). Old JetPens-led model lists trimmed to tier lists with a few icon archetypes. '
 'Moved Zebra Onamae Mackee into the Mckee archetype and FriXion Light into an archetype; Sharpie S-Gel noted as a Sharpie version. Not added: Edding whiteboard markers and Edding 3000 launch year (not on retrieved pages), '
 'Staedtler Lumocolor and Uni Pin launch years, Expo low-odour line (no page). The Expo source is a weak blog and the 1976 date is uncertain. Brand facts for Sakura, Stabilo, Staedtler, Uni, Faber-Castell, Zebra, Pilot, Tombow, Kuretake from knowledge. '
 'sharpie.com blocked WebFetch and was retrieved via firecrawl; Wikipedia Edding page returned 404 to WebFetch, so edding.com history was used.')
out = {'kinds': [fine, hil, perm, dry, brush], 'brands': brands, 'traditions': [], 'notes': notes}
p = 'work/C5/shelves/01_01.json'
json.dump(out, open(p + '.tmp', 'w'), ensure_ascii=False, indent=1); os.replace(p + '.tmp', p)
print('archetypes', sum(len(k.get('x', [])) for k in out['kinds']))
