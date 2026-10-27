import json, os
W = 'https://en.wikipedia.org/wiki/'
FT = W + 'Four_Treasures_of_the_Study'
INK = W + 'Inkstone'
FUN = 'https://www.fun-japan.jp/en/articles/14080'
NARA = 'https://kogeijapan.com/locale/en_US/narasumi/'
KUM = 'https://kogeijapan.com/locale/en_US/kumanofude/'
TAK = 'https://takase.com/learn-japanese-calligraphy/lesson-1/'
UN = 'https://ich.unesco.org/en/RL/traditional-handicrafts-of-making-xuan-paper-00201'
AME = 'https://www.yamanashi-kankou.jp/english/discover/amehata-suzuri-no-sato-kenshoan.html'
HKW = 'https://www.inkston.com/stories/people/hu-kai-wen'
def X(n, d, mk, y, s, v=(), a='', dt=''):
    o = {'n': n, 'a': a, 'd': d, 'mk': mk, 'y': y, 's': s, 'v': [dict(zip(('n', 'mk', 'y', 'd'), t)) for t in v]}
    if dt: o['dt'] = dt
    return o

brush = {'n': 'Calligraphy brush', 'a': 'shodo brush · fude · maobi', 'd': 'Animal-hair brush on a bamboo handle made for East Asian calligraphy.',
 't': ['soft hair', 'mixed hair', 'hard hair', 'large (ofude)', 'medium (chufude)', 'small (kofude)', 'long, medium or short tuft'], 's': 'https://store.kyotohandicraftcenter.com/en-us/collections/calligraphy-set',
 'x': [
  X('Huzhou brush', 'Chinese brush of mixed weasel, goat and rabbit hair from Shanlian, Huzhou, prized since the Ming dynasty.', '', 'Ming dynasty', FT, a='Hubi · 湖筆', dt='hair blend · tuft size · bamboo handle'),
  X('Kumano fude', 'Japanese brush from Kumano, Hiroshima, made in over 70 mostly hand steps; most Japanese calligraphy brushes come from here.', '', '19th century', KUM,
    [('Neri-maze', '', '', 'slow soaked hair-mixing, top quality'), ('Bon-maze', '', '', 'faster dry mixing, late 19th century')], a='熊野筆', dt='goat, horse, deer, raccoon dog or weasel hair'),
  X('Nara fude', 'Japanese brush from Nara blending more than a dozen hair types, with about 1,200 years of history.', '', '', FUN, a='奈良筆'),
 ]}

stick = {'n': 'Ink stick', 'a': 'inkstick · sumi · mo · meok', 'd': 'Solid stick of soot and animal glue ground with water on an inkstone to make calligraphy ink.',
 't': ['pine soot (shoen)', 'oil soot (yuen)', 'coloured', 'scented'], 's': 'https://www.utrechtart.com/products/kuretake-zig-saiboku-shimbi-colored-sumi-ink-sticks',
 'x': [
  X('Hui ink', 'Chinese ink stick from old Huizhou, still made in She County, Anhui; the most highly regarded Chinese ink.', '', '', FT,
    [('Old Hu Kai Wen', 'Hu Kaiwen', '1765', 'Globe inkstick won gold at the 1915 Panama-Pacific Exhibition')], a='Huimo · 徽墨', dt='musk and borneol · soot type · moulded decoration'),
  X('Nara sumi', 'Japanese oil-soot ink stick from Nara, which makes about 90% of Japan\'s sumi.', '', '806', NARA,
    [('Kobaien', 'Kobaien', '', 'oil-soot sticks from about 200 vessels; made November–April'), ('Kuretake sumi', 'Kuretake', '1902', ''), ('Boku-Undo sumi', 'Boku-Undo', '', '')], a='奈良墨', dt='soot oil (rapeseed, sesame, camellia) · grade · gilded decoration'),
  X('Suzuka sumi', 'Japanese pine-soot ink stick from Suzuka, Mie, said to date from about 780.', '', 'c. 780', FUN, a='鈴鹿墨'),
  X('Coloured ink stick', 'Oil-soot ink blended with pigment, used for accents in painting; cinnabar red is the best known.', '', '', W + 'Inkstick',
    [('Saiboku Shimbi', 'Kuretake', '', 'coloured sumi set'), ('E-Sumi Light', 'Boku-Undo', '', 'six-colour set')]),
 ]}

stone = {'n': 'Inkstone', 'a': 'suzuri · yan · byeoru', 'd': 'Stone or ceramic slab with a flat grinding area and a well, on which an ink stick is ground with water.',
 't': ['stone', 'ceramic (chengni)', 'with lid or box', 'carved', 'antique (over 100 years)'], 's': 'https://www.jetpens.com/Inkstones/ct/8237',
 'x': [
  X('Duan inkstone', 'Purple volcanic tuff inkstone from Zhaoqing, Guangdong, graded by quarry and prized for its "stone eyes".', '', 'Tang dynasty', INK,
    [('Mazukeng', '', '18th century', 'quarry opened in the Qianlong reign'), ('Green Duan', '', 'Song dynasty', '')], a='端硯', dt='quarry (keng) · stone eyes · carving'),
  X('She inkstone', 'Black slate inkstone with gold-like markings from She County, Anhui, and Wuyuan, Jiangxi.', '', 'Tang dynasty', INK, a='歙硯'),
  X('Taohe inkstone', 'Rare green, ripple-banded inkstone from the Tao River in Gansu.', '', 'Song dynasty', INK, a='洮河硯'),
  X('Chengni inkstone', 'Fired-clay inkstone said to originate in Luoyang, Henan.', '', 'Tang dynasty', INK, a='澄泥硯'),
  X('Amehata suzuri', 'Japanese slate inkstone from Amehata village, Yamanashi, cut from riverbed stone.', '', '', AME, a='雨畑硯'),
  X('Akama suzuri', 'Japanese inkstone from Shimonoseki and Ube, Yamaguchi, recorded as early as 1191.', '', '1191', FUN, a='赤間硯'),
  X('Ogatsu suzuri', 'Hard slate inkstone from Ishinomaki, Miyagi.', '', 'c. 1396', FUN, a='雄勝硯'),
 ],
 'm': [['Kuretake Yamato Shinken Traditional Suzuri', 'Kuretake'], ['Yasutomo Natural Suzuri Inkstone', 'Yasutomo']]}

paper = {'n': 'Calligraphy paper', 'a': 'xuan paper · hanshi · hanji · rice paper', 'd': 'Absorbent handmade or machine paper for brush calligraphy, from practice sheets to fine xuan.',
 't': ['raw (unsized)', 'sized', 'practice paper', 'pre-cut sheets', 'rolls'], 's': UN,
 'x': [
  X('Xuan paper', 'Chinese paper from Jing County, Anhui, made by hand from wingceltis bark and rice straw in over a hundred steps.', '', '', UN, a='宣紙', dt='raw or sized · weight · sheet size'),
  X('Hanji', 'Korean paper of paper-mulberry bark, laminated by the we bal method and pounded to reduce bleed.', '', 'Goryeo period', W + 'Korean_paper', a='韓紙 · Korean paper'),
  X('Hanshi', 'Standard Japanese washi practice sheet of 24.2 × 33.3 cm.', '', '', TAK, a='半紙'),
 ]}

acc = {'n': 'Calligraphy desk accessories', 'a': 'bunchin · shitajiki · suiteki · fudeoki', 'd': 'Small tools laid out for brush calligraphy: paperweights, felt underlay, water dropper, brush rest and brush roll.',
 't': ['paperweight (bunchin)', 'felt underlay (shitajiki)', 'water dropper (suiteki)', 'brush rest (fudeoki)', 'ink-stick rest (sumioki)', 'brush roll (fudemaki)', 'brush pot', 'brush washer'], 's': TAK}

cset = {'n': 'Calligraphy set', 'a': 'shodo set · suzuribako', 'd': 'Brush, ink and inkstone sold together in a kit or box.', 't': ['student set', 'boxed or lacquered set', 'travel set'],
 's': 'https://store.kyotohandicraftcenter.com/en-us/collections/calligraphy-set'}

def B(n, c, f, seg, kf, d, s, sig=()):
    return {'n': n, 'c': c, 'f': f, 'seg': seg, 'kf': kf, 'd': d, 'lines': [], 'eras': [], 'sig': list(sig), 'sc': [], 'rel': [], 's': s}
brands = [
 B('Kobaien', 'Japan', '16th century', 'Heritage manufactory', 'Nara sumi ink sticks', 'Nara ink-stick house founded by Dochin Matsui and run by the Matsui family.', 'https://www.kansaiscene.com/2021/02/a-legacy-in-ink/', ['Nara sumi']),
 B('Kuretake', 'Japan', '1902', 'Mainstream', 'sumi, brush pens, art supplies', 'Nara maker founded to make traditional ink sticks.', 'https://www.kuretakezig.us/about', ['Nara sumi', 'Coloured ink stick']),
 B('Boku-Undo', 'Japan', '1805', 'Heritage manufactory', 'sumi ink', 'Japanese sumi and calligraphy supply maker with roots in ink-making from 1805.', 'https://wafuu.com/products/boku-undo-solid-ink-e-sumi-light-6-colors-set-15429', ['Coloured ink stick']),
 B('Hu Kaiwen', 'China', '1765', 'Heritage manufactory', 'Hui ink sticks', 'She County ink workshop founded by Hu Tian Zhu; a China Time-honored Brand.', HKW, ['Hui ink']),
]
def T(n, g, r, p, d, tech, mat, forms, ctr, auth, s):
    return {'n': n, 'g': g, 'r': r, 'p': p, 'd': d, 'tech': tech, 'mat': mat, 'forms': forms, 'ctr': ctr, 'auth': auth, 's': s}
CAL = 'Writing & calligraphy'
trads = [
 T('Huzhou brush making', CAL, 'Huzhou, Zhejiang, China', 'Ming dynasty to present', 'Chinese brush making centred on Shanlian, Huzhou, known for blended-hair brushes.', 'hand sorting and blending of hair into a tuft', 'weasel, goat and rabbit hair; bamboo', ['Huzhou brush'], ['Shanlian, Nanxun District'], 'Shanlian origin, even pointed tuft', FT),
 T('Hui ink making', CAL, 'Huizhou (She County), Anhui, China', 'Qing dynasty to present', 'Making of Huimo ink sticks from soot and glue with musk and borneol.', 'soot collection, kneading with glue, moulding, long drying', 'pine or oil soot, animal glue, musk, borneol', ['Hui ink'], ['Old Hu Kai Wen workshop, She County'], 'workshop mark, hardness and lacquer-black sheen', HKW),
 T('Duan inkstone carving', CAL, 'Zhaoqing, Guangdong, China', 'Tang dynasty to present', 'Carving of purple tuff inkstones graded by quarry.', 'quarrying by keng and relief carving', 'Duan stone (volcanic tuff)', ['Duan inkstone'], ['Zhaoqing', 'Mazukeng quarry'], 'fine even grain, satin feel, clear ring when struck, stone eyes', INK),
 T('She inkstone carving', CAL, 'She County, Anhui and Wuyuan, Jiangxi, China', 'Tang dynasty to present', 'Carving of black slate inkstones with gold-like markings.', 'quarrying and carving', 'She slate', ['She inkstone'], ['She County', 'Wuyuan'], 'black slate with gold-like markings, fine grain', INK),
 T('Xuan paper making', CAL, 'Jing County, Anhui, China', 'to present; UNESCO list 2009', 'Hand-making of xuan paper for calligraphy, painting and printing.', 'over a hundred hand steps over two years', 'wingceltis bark, rice straw', ['Xuan paper'], ['Jing County'], 'soft, strong, ink-absorbent sheet from Jing County', UN),
 T('Nara sumi', CAL, 'Nara, Japan', '806 to present', 'Japanese oil-soot ink-stick making begun at Kofukuji temple and continued by Nara ink houses.', 'oil-soot collection, kneading with nikawa, wooden moulds, ash drying', 'rapeseed, sesame or paulownia oil soot; nikawa glue', ['Nara sumi', 'Ink stick'], ['Kofukuji', 'Kobaien', 'Kuretake'], 'Nara maker stamp; designated traditional craft', NARA),
 T('Kumano fude', CAL, 'Kumano, Hiroshima, Japan', 'early 19th century to present', 'Brush making in Kumano, designated a Traditional Craft in 1975.', 'over 70 mostly hand steps; neri-maze hair mixing', 'goat, horse, deer, raccoon dog, weasel and cat hair', ['Kumano fude', 'Calligraphy brush'], ['Kumano'], 'head made in Kumano by traditional methods', KUM),
 T('Nara fude', CAL, 'Nara and Yamatokoriyama, Japan', 'about 1,200 years', 'Japanese brush making that blends more than a dozen hair types.', 'hair blending', 'sheep, raccoon dog, rabbit and other hair', ['Nara fude'], ['Nara', 'Yamatokoriyama'], 'Nara origin', FUN),
 T('Amehata suzuri', CAL, 'Amehata, Yamanashi, Japan', 'centuries to present', 'Inkstones carved from slate taken from the Amehata River bed.', 'hand carving of river slate', 'Amehata slate', ['Amehata suzuri'], ['Amehata Suzuri no Sato Kenshoan'], 'Amehata slate and village maker', AME),
 T('Hanji', 'Textiles & paper', 'Korea', 'Goryeo period (918–1392) to present', 'Korean handmade paper of paper-mulberry bark.', 'we bal laminated sheet forming; dochim pounding', 'dak (paper mulberry) bark, dakpul mucilage', ['Hanji'], ['26 mills in South Korea (2009)'], 'multi-directional grain, pounded surface', W + 'Korean_paper'),
]
notes = ('Old kinds kept one-to-one (brush, ink stick, inkstone, set); two new kinds added (Calligraphy paper, Calligraphy desk accessories). Archetypes are regional types (Huzhou, Kumano, Nara brushes; Hui, Nara, Suzuka ink; Duan, She, Taohe, Chengni, Amehata, Akama, Ogatsu inkstones; xuan, hanji, hanshi papers). '
 'Old models kept: Kuretake Saiboku Shimbi as a coloured-stick version; Kuretake and Yasutomo suzuri in m. Restraint on sets: types only. Not added: Cao Sugong and other Qing ink masters (only search snippets); named Chinese brush houses beyond Huzhou; Korean inkstones (no page). '
 'Hu Kaiwen founding given as 1765 per Inkston (other sources say 1782). chiculture.org.hk blocked; makkura 404.')
out = {'kinds': [brush, stick, stone, paper, acc, cset], 'brands': brands, 'traditions': trads, 'notes': notes}
p = 'work/C5/shelves/00_02.json'
json.dump(out, open(p + '.tmp', 'w'), ensure_ascii=False, indent=1); os.replace(p + '.tmp', p)
print('archetypes', sum(len(k.get('x', [])) for k in out['kinds']))
