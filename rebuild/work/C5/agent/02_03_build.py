import json, os
W = 'https://en.wikipedia.org/wiki/'
SEA = W + 'Seal_(East_Asia)'
UN = 'https://ich.unesco.org/en/RL/art-of-chinese-seal-engraving-00217'
JP = 'https://www.jeepe.jp/en/articles/japan-hanko-culture-guide-1799'
SH = 'https://hiraganatimes.com/highlights/shachihata-a-byword-for-seals-that-require-no-ink'
HB = 'https://exaclair.com/brands_herbin.php'
JS = 'https://www.jetpens.com/Herbin-Brass-Wax-Seal-Script-D/pd/15725'


def X(n, d, mk, y, s, v=(), a='', dt=''):
    o = {'n': n, 'a': a, 'd': d, 'mk': mk, 'y': y, 's': s, 'v': [dict(zip(('n', 'mk', 'y', 'd'), t)) for t in v]}
    if dt: o['dt'] = dt
    return o


name = {'n': 'Name seal', 'a': '印鑑 · hanko · inkan · chop · 도장 dojang',
 'd': 'Personal seal carved with the owner\'s name and stamped in red paste as a signature, used in Japan, China and Korea.',
 't': ['jitsu-in (registered seal)', 'ginkō-in (bank seal)', 'mitome-in (everyday seal)', 'gagō-in (artist\'s seal)', 'Korean ingam (registered seal)', 'Chinese name chop', 'pre-inked name stamp'],
 's': 'https://tokyocheapo.com/shopping-2/hanko-japanese-personal-seals/',
 'x': [
  X('Shachihata X Stamper name stamp', 'Pre-inked rubber name stamp needing no ink pad or vermilion paste; so common that similar stamps are called "Shachihata".', 'Shachihata', '1965', SH,
    [('X Stamper', 'Shachihata', '1965', 'ink-saturated porous rubber'), ('Pre-inked name stamp (ネーム印)', 'Shachihata', '1968', ''), ('Name pen', 'Shachihata', '', 'pen with built-in name stamp')],
    dt='everyday use only; often not accepted for registered or bank seals'),
 ],
 'dt': 'materials: boxwood (tsuge), black water-buffalo horn, titanium, acrylic, stone (Chinese) · sizes: jitsu-in 15–18 mm, ginkō-in 13.5–15 mm, mitome-in 10.5–13.5 mm (men\'s guide)'}
name.pop('dt')

paste = {'n': 'Seal paste', 'a': '朱肉 shuniku · 印泥 yinni · vermilion seal ink · seal pad',
 'd': 'Red vermilion paste or pad used to ink East Asian name seals and artists\' seals.',
 't': ['paste-type (練り朱肉)', 'sponge-type pad (スポンジ朱肉)', 'silk-based paste', 'plant (moxa) based paste'],
 's': 'https://www.tkgje.jp/entries/06000/06192_shuniku.html'}

wax_stamp = {'n': 'Wax seal stamp', 'a': 'wax seal · desk seal · seal matrix · signet',
 'd': 'Engraved metal or stone seal pressed into warm sealing wax to close and mark letters; includes signet rings used the same way.',
 't': ['handled desk seal', 'interchangeable head', 'signet ring', 'monogram or initial', 'custom die'],
 's': W + 'Seal_(emblem)',
 'x': [
  X('Herbin brass wax seal', 'Solid-brass initial or motif seal head made to screw onto a separate wooden handle, from the Paris sealing-wax house.', 'J. Herbin', '', JS,
    [('Brass Wax Seal – Script initials', 'J. Herbin', '', 'one seal per letter; handle sold separately')], dt='script letters A–Z · motifs'),
 ],
 'm': [['Wax & Seal gift sets', 'Manuscript']]}

wax = {'n': 'Sealing wax', 'a': 'letter wax · wax sticks · wax beads',
 'd': 'Wax melted onto an envelope or document and pressed with a seal; traditional sticks, flexible mailable wax or glue-gun sticks.',
 't': ['traditional stick (with or without wick)', 'flexible (mailable) wax', 'glue-gun sticks', 'granules or beads', 'faux (self-adhesive) seals'],
 's': W + 'Sealing_wax',
 'x': [
  X('J. Herbin sealing wax', 'Paris sealing wax from the house Jacques Herbin founded in 1670, its first product before inks.', 'J. Herbin', '1670', HB,
    [('Sealing Wax & Accessories', 'J. Herbin', '', 'current line, sold in the US by Exaclair')]),
 ]}

rubber = {'n': 'Rubber stamp', 'a': 'office stamp · self-inking stamp · date stamp · ink pad',
 'd': 'Hand stamp with a rubber or polymer die for dates, addresses, words or marks on office papers; decorative stamps are in Craft & Art Supplies.',
 't': ['traditional stamp with separate ink pad', 'self-inking stamp', 'pre-inked stamp', 'dater', 'address stamp', 'stamp ink pad', 'refill ink'],
 's': 'https://www.officeworks.com.au/shop/officeworks/c/office-supplies',
 'x': [
  X('Trodat Printy', 'Plastic self-inking stamp whose die flips from an internal pad to the paper; Trodat\'s core office stamp.', 'Trodat', '1976', W + 'Trodat',
    [('Printy', 'Trodat', '1976', 'introduced'), ('printy-dater 4810', 'Trodat', '', 'date stamp')]),
 ],
 'm': [['Printer Standard', 'COLOP'], ['Printer Line Dater', 'COLOP'], ['Pocket Stamp', 'COLOP'], ['Classic Line', 'COLOP'], ['X Stamper', 'Shachihata']]}


def B(n, c, f, seg, kf, d, s, lines=(), sig=(), rel=()):
    return {'n': n, 'c': c, 'f': f, 'seg': seg, 'kf': kf, 'd': d, 'lines': list(lines), 'eras': [], 'sig': list(sig), 'sc': [], 'rel': list(rel), 's': s}


brands = [
 B('Shachihata', 'Japan', '1925', 'Mainstream', 'pre-inked stamps', 'Nagoya-rooted maker of ink pads and the pre-inked X Stamper; began as ink-pad maker Funabashi Shokai, renamed 1941.', SH, ['X Stamper', 'name stamps'], ['Shachihata X Stamper name stamp']),
 B('Trodat', 'Austria', '1912', 'Mainstream', 'self-inking stamps', 'Stamp maker founded in Vienna by Franz Just, based in Wels; part of Trodat Trotec.', W + 'Trodat', ['Printy'], ['Trodat Printy'], ['COLOP']),
 B('COLOP', 'Austria', '1981', 'Mainstream', 'self-inking stamps', 'Wels stamp maker founded by Karl Skopek in 1980/81.', 'https://www.colop.com/us/about-us', ['Printer Line', 'Classic Line', 'Pocket Stamp', 'e-mark'], [], ['Trodat']),
 B('J. Herbin', 'France', '1670', 'Heritage manufactory', 'sealing wax, inks', 'Paris house founded by Jacques Herbin in 1670 for sealing wax and later inks.', HB, ['Sealing Wax & Accessories'], ['J. Herbin sealing wax', 'Herbin brass wax seal']),
 B('Manuscript', 'United Kingdom', '1856', 'Specialist', 'calligraphy pens', 'Birmingham calligraphy-pen maker descended from D. Leonardt & Co., also selling wax and seal sets.', 'https://calligraphy.co.uk/pages/about-us', ['Wax & Seal'], []),
]

trads = [
 {'n': 'Chinese seal engraving', 'g': 'Paper & stationery', 'r': 'China', 'p': 'Shang dynasty to present',
  'd': 'Art of designing and cutting name and studio seals in reverse in stone, inscribed by UNESCO in 2009.',
  'tech': 'design sketched on paper, cut in reverse with a knife; printed with vermilion seal paste', 'mat': 'stone (soapstone for cheap seals), jade, metal, wood, bamboo; cinnabar paste',
  'forms': ['Name seal', 'Seal paste'], 'ctr': ['Xiling Seal Engravers\' Society, Zhejiang'],
  'auth': 'hand-cut characters with calligraphic line quality rather than machine-cut lettering', 's': UN},
 {'n': 'Japanese hanko (inkan)', 'g': 'Paper & stationery', 'r': 'Japan', 'p': 'to present (registered seals still used)',
  'd': 'Personal seal culture with a registered jitsu-in, a bank ginkō-in and an everyday mitome-in, printed in vermilion shuniku.',
  'tech': 'name carved in seal script on a round or square face', 'mat': 'boxwood, black water-buffalo horn, titanium, acrylic',
  'forms': ['Name seal', 'Seal paste'], 'ctr': ['seal shops in Asakusa, Kyoto and Osaka'],
  'auth': 'registered seals are hand-finished and unique; pre-inked "Shachihata" stamps are not accepted for registration', 's': JP},
 {'n': 'Korean dojang', 'g': 'Paper & stationery', 'r': 'Korea', 'p': 'Joseon period to present',
  'd': 'Personal seals, with registered ingam certified by a seal-registration certificate since 1914.',
  'tech': 'carved name seal', 'mat': '', 'forms': ['Name seal'], 'ctr': [],
  'auth': 'registered ingam matches its certificate', 's': SEA},
]

notes = ('All five planned kinds kept. Old Rubber stamp and Stamp ink pad merged into Rubber stamp (ink pad as a type). Old Name seal models (jitsu-in, ginkō-in, mitome-in) became types. '
 'Shiny (Taiwan) stamps left out: only retailer search snippets, no retrieved page. Chinese seal stones (Shoushan, Qingtian, Changhua) and Xiling yinni not added: no retrieved page named them. '
 'Herbin brass seal page was blocked to WebFetch and retrieved via firecrawl.')
out = {'kinds': [name, paste, wax_stamp, wax, rubber], 'brands': brands, 'traditions': trads, 'notes': notes}
p = 'work/C5/shelves/02_03.json'
json.dump(out, open(p + '.tmp', 'w'), ensure_ascii=False, indent=1); os.replace(p + '.tmp', p)
