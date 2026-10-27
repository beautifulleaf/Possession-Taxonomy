import json, os
W = 'https://en.wikipedia.org/wiki/'
PA = 'https://www.penaddict.com/blog/'
MN = 'https://www.gouletpens.com/blogs/fountain-pen-blog/maruman-mnemosyne-notebook-overview'
TN = 'https://groundingpage.com/facts/travelers-notebook/'
TR = 'https://www.gentlemanstationer.com/blog/2022/5/7/paper-review-first-impressions-of-the-new-sanzen-tomoe-river-paper'
CF = W + 'Clairefontaine_paper_mills'


def X(n, d, mk, y, s, v=(), a='', dt=''):
    o = {'n': n, 'a': a, 'd': d, 'mk': mk, 'y': y, 's': s, 'v': [dict(zip(('n', 'mk', 'y', 'd'), t)) for t in v]}
    if dt: o['dt'] = dt
    return o


nb = {'n': 'Notebook', 'a': 'journal · notebook · memo book · composition book',
 'd': 'Bound book of blank, lined, grid or dot pages; differs by binding, cover, size and paper.',
 't': ['sewn hardcover', 'thread-stitched softcover', 'perfect-bound', 'spiral or twin-wire', 'composition book', 'pocket memo book', 'dot grid', 'waterproof paper', 'thin fountain-pen paper'],
 's': W + 'Moleskine',
 'x': [
  X('Moleskine notebook', 'Black hardcover notebook with rounded corners, elastic closure, ribbon and back pocket, revived from the Paris notebooks Chatwin described.', 'Moleskine', '1997', W + 'Moleskine',
    [('Notebook', 'Moleskine', '1997', 'first run of 5,000'), ('Smart Writing Set', 'Moleskine', '2016', 'digitising notebook and pen')],
    dt='pocket and large sizes · ruled, squared, plain, dotted · hard or soft cover'),
  X('Leuchtturm1917 Medium A5', 'A5 hardcover notebook with numbered pages, contents index, back pocket and spine labels; the bullet-journal favourite.', 'Leuchtturm1917', '', 'https://www.gouletpens.com/blogs/fountain-pen-blog/leuchtturm1917-notebooks',
    [('Medium A5', 'Leuchtturm1917', '', '80 gsm'), ('Pocket', 'Leuchtturm1917', '', ''), ('Master', 'Leuchtturm1917', '', '100 gsm'),
     ('Bullet Journal edition', 'Leuchtturm1917', '', 'official edition, 120 gsm')],
    dt='dot grid, lined, graph, blank · many cover colours'),
  X('Clairefontaine notebook', 'French staple notebook with varnished cover and purple ruling, on the mill\'s smooth paper.', 'Clairefontaine', '1951', CF,
    [('Clairefontaine notebook', 'Clairefontaine', '1951', 'launched by Charles Nusse')]),
  X('Midori MD Notebook', 'Thread-stitched notebook of cream MD paper that opens flat, with a paper wrap instead of a cover.', 'Midori', '', PA + '2017/8/18/the-midori-md-notebook-a5-gridded-a-review',
    [('MD Notebook A5', 'Midori', '', '176 pages'), ('MD Notebook Light', 'Midori', '', ''), ('MD Notebook 1 Day 1 Page Codex', 'Midori', '', '')], dt='grid, blank, lined'),
  X('Kokuyo Campus', 'Perfect-bound Japanese school and office notebook, one of Japan\'s most popular.', 'KOKUYO', '1975', 'https://www.kokuyostore.com/en/blog/blog32-history-of-campus-notebook.html',
    [('Campus', 'KOKUYO', '1975', 'perfect binding'), ('Campus (tear-resistant spine)', 'KOKUYO', '2000', ''), ('Campus fifth generation', 'KOKUYO', '2011', 'smoother spine tape, updated ruling')],
    dt='6 mm and 7 mm ruling · dot ruling'),
  X('Maruman Mnemosyne', 'Black twin-wire business notebook with perforated 80 gsm paper.', 'Maruman', '', MN,
    [('N194 B5', 'Maruman', '', 'lined'), ('N195 A5', 'Maruman', '', 'lined'), ('N199 A4', 'Maruman', '', ''), ('N105 A5', 'Maruman', '', 'dot grid'), ('N180 A4 Imagination', 'Maruman', '', 'graph')]),
  X('Tomoe River paper notebook', 'Notebook of ultra-thin 52 gsm Tomoe River paper, loved for fountain-pen sheen; now made by Sanzen.', 'Tomoegawa', '', TR,
    [('Tomoegawa Tomoe River', 'Tomoegawa', '', 'original, discontinued about 2021'), ('Sanzen Tomoe River', 'Sanzen', '', 'reworked formula, stiffer'), ('68 gsm Tomoe River', 'Tomoegawa', '', 'heavier weight')]),
  X('Stalogy 365 Days', 'Thin-paper day-per-page notebook with date headers, a Tomoe River alternative.', 'STALOGY', '', PA + '2025/3/6/stalogy-editors-series-365days-a5-notebook-review',
    [('365Days A5', 'STALOGY', '', '368 pages, 52 gsm'), ('365Days A6', 'STALOGY', '', ''), ('365Days B6', 'STALOGY', '', '')]),
  X('Apica CD Premium', 'Thread-and-glue notebook with very smooth 86.5 gsm paper.', 'Apica', '', PA + '2020/4/2/apica-cd-premium-notebook-review', [('Premium CD A5', 'Apica', '', '')]),
  X('Field Notes', 'Pocket memo book modelled on American farm promotional memo books, with quarterly limited editions.', 'Field Notes', '2007', W + 'Field_Notes',
    [('Original memo book', 'Field Notes', '2007', 'ruled, graph, blank'), ('Quarterly limited editions', 'Field Notes', '2009', 'subscription')]),
  X('Rite in the Rain', 'All-weather notebook of coated paper that can be written on wet.', 'Rite in the Rain', '1916', 'https://www.southsoundmag.com/travel-outdoor/rite-in-the-rain-celebrates-100th-birthday/article_c9bd19b7-23d1-5aa5-8c85-0821f32a3e76.html',
    [('Mini-Stapled Notebook', 'Rite in the Rain', '', ''), ('Centennial Bound Book', 'Rite in the Rain', '2016', '')]),
  X('Baron Fig Confidant', 'Cloth-covered lay-flat notebook with 100 gsm paper, born on Kickstarter.', 'Baron Fig', '', PA + '2014/6/18/baron-fig-confidant-review', [('Confidant', 'Baron Fig', '', '5.4 × 7.7 in, 192 pages')]),
 ],
 'm': [['Hobonichi Graph Notebook', 'Hobonichi'], ['Delfonics Rollbahn', 'Delfonics'], ['Mead Five Star Composition Notebook', 'Mead'], ['Pilot Black Note', 'Pilot'],
       ['Takeo Dressco Onion Skin', 'Takeo'], ['Midori Yuru Log', 'Midori'], ['Nouto Nombre', 'Nouto'], ['Beverly Marumi', 'Beverly'], ['Daigo Easy Journal', 'Daigo']]}

ref = {'n': 'Refillable notebook system', 'a': 'traveler\'s notebook · ring organiser · personal organiser · discbound notebook',
 'd': 'Cover plus refillable inserts or pages sold as one system: band-held notebooks, ring binders or disc-bound books.',
 't': ['travel notebook (elastic-held inserts)', 'ring organiser', 'discbound'],
 's': 'https://www.jetpens.com/Notebooks/ct/762',
 'x': [
  X('Traveler\'s Notebook', 'Leather cover holding several elastic-bound refill booklets.', 'TRAVELER\'S COMPANY', '2006', TN,
    [('Regular size', 'TRAVELER\'S COMPANY', '2006', 'about 230 × 145 mm; first sold under the Midori name'), ('Passport size', 'TRAVELER\'S COMPANY', '', 'about 134 × 98 mm')],
    dt='vegetable-tanned leather from Chiang Mai · black, brown, camel, blue · refills 001–026'),
  X('Filofax organiser', 'Six-ring leather personal organiser of loose-leaf diary and note inserts, a 1980s status object.', 'Filofax', '1921', W + 'Filofax',
    [('Lefax', '', '', 'Philadelphia original'), ('Filofax organiser', 'Filofax', '1921', 'sold by Norman & Hill')]),
  X('Disc-bound notebook', 'Notebook whose mushroom-punched pages snap on and off plastic or metal discs, so pages can be moved.', 'Atoma', '1948', W + 'Disc-binding',
    [('Atoma', 'Atoma', '1948', 'Belgian original'), ('Levenger Circa', 'Levenger', '', 'US, supplied by Rollabind')]),
 ]}

dia = {'n': 'Diary or planner', 'a': '手帳 · techo · agenda · journal',
 'd': 'Book ruled by date (daily, weekly, monthly or multi-year), dated or undated.',
 't': ['daily (page a day)', 'weekly', 'monthly', 'five-year', 'undated'],
 's': 'https://www.jetpens.com/Planners/ct/2815',
 'x': [
  X('Hobonichi Techo', 'Japanese page-a-day planner printed mostly on Tomoe River paper, with a cult cover culture.', 'Hobonichi', '', W + 'Hobonichi_Techo',
    [('Original', 'Hobonichi', '', 'A6, daily'), ('Cousin', 'Hobonichi', '', 'A5, daily, weekly and monthly'), ('Weeks', 'Hobonichi', '', 'slim weekly'),
     ('Weeks Mega', 'Hobonichi', '', 'more note pages'), ('Day-Free', 'Hobonichi', '', 'undated'), ('5-Year Techo', 'Hobonichi', '', 'five-year journal'),
     ('English edition', 'Hobonichi', '2013', ''), ('HON', 'Hobonichi', '2023', 'hard cardboard cover')]),
 ],
 'm': [['KOKUYO Jibun Techo', 'KOKUYO'], ['LIFE Free Days', 'LIFE'], ['Rhodia Goalbook', 'Rhodia'], ['Roterfaden Calendar', 'Roterfaden'], ['Moleskine planner', 'Moleskine']]}

cov = {'n': 'Planner or notebook cover, refills & inserts', 'a': 'notebook cover · planner refill · insert · index tabs',
 'd': 'Covers, refill books, index tabs and inserts made for one planner or notebook system, sold separately.',
 't': ['cover', 'refill notebook', 'index tabs', 'pocket insert'],
 's': 'https://www.jetpens.com/Notebook-Covers/ct/5758',
 'm': [['Hobonichi Cover on Cover (A6)', 'Hobonichi'], ['Hobonichi Techo Weeks cover', 'Hobonichi'], ['MD Notebook Cover (clear)', 'Midori'],
       ['TRAVELER\'S notebook refill (Regular size)', 'TRAVELER\'S COMPANY'], ['TRAVELER\'S notebook Lightweight Paper refill 013', 'TRAVELER\'S COMPANY'],
       ['Hobonichi TSUKI no IRO 12 Month Index Pockets', 'Hobonichi'], ['Sunny Light refills', 'Sunny Light']]}

memo = {'n': 'Memo pad', 'a': 'notepad · writing pad · memo block',
 'd': 'Glued or bound pad of tear-off sheets for short notes.',
 't': ['top-stapled', 'top-spiral', 'glued block', 'square memo'],
 's': 'https://www.jetpens.com/Memo-Notepads/ct/1654',
 'x': [
  X('Rhodia orange pad', 'Top-stapled pad with an orange cover and pre-scored sheets of smooth 80 gsm vellum, unchanged since 1934.', 'Rhodia', '1934', 'https://www.bloc-rhodia.com/gb/page/rhodia-universe/the-iconic-orange-pad',
    [('Orange pad', 'Rhodia', '1934', ''), ('DotPad', 'Rhodia', '', 'dot grid')], dt='orange or black cover · many sizes'),
  X('Maruman Mnemosyne pad', 'Black twin-wire memo pads and notepads of perforated 80 gsm paper.', 'Maruman', '', MN,
    [('N196 B6', 'Maruman', '', 'lined'), ('N193 A7', 'Maruman', '', ''), ('N192 B7', 'Maruman', '', ''), ('N183 A5 Inspiration', 'Maruman', '', 'blank')]),
  X('Midori MD Paper Pad', 'Pads and memo blocks of Midori\'s cream MD paper.', 'Midori', '', PA + '2017/8/18/the-midori-md-notebook-a5-gridded-a-review',
    [('MD Paper Pad', 'Midori', '', ''), ('MD Memo Block', 'Midori', '', '')]),
 ],
 'm': [['Clairefontaine Triomphe Notepad', 'Clairefontaine'], ['YAMAMOTO PAPER Tomoe River Writing Pad', 'YAMAMOTO PAPER'], ['STALOGY Editor\'s Memo Pad', 'STALOGY'],
       ['Midori Patto Quick Open Memo Pad', 'Midori'], ['Sun-Star Square Memo Pad', 'Sun-Star'], ['Wemo Wearable Memo Pad', 'Wemo'], ['Paperian Flat Notepad', 'Paperian']]}

loose = {'n': 'Loose-leaf paper', 'a': 'filler paper · binder paper',
 'd': 'Punched loose sheets made for a ring binder or disc system.',
 't': ['A4 / letter', 'A5', 'B5 (26-hole)', 'fountain-pen paper'],
 's': 'https://www.jetpens.com/Loose-Leaf-Paper/ct/2696',
 'm': [['KOKUYO Campus Loose Leaf Sarasara', 'KOKUYO'], ['KOKUYO Campus Biz Loose Leaf', 'KOKUYO'], ['Maruman Loose Leaf Easy to Write', 'Maruman'],
       ['Tomoe River S Loose Leaf', 'Tomoegawa'], ['Kobeha Graphilo Fountain Pen Paper', 'Kobeha'], ['Sakae TP Iroful', 'Sakae TP']]}

let = {'n': 'Letter-writing paper set', 'a': 'letter set · writing paper · correspondence set · stationery',
 'd': 'Writing sheets or pads with matching envelopes for personal letters, from cute mini sets to fine cotton and laid papers.',
 't': ['letter set', 'writing pad with envelopes', 'cotton paper', 'laid paper', 'correspondence cards'],
 's': 'https://www.jetpens.com/Stationery-Paper/ct/2714',
 'x': [
  X('G. Lalo Vergé de France', 'French laid-finish 100 gsm writing paper in pads with matching envelopes.', 'G. Lalo', '', 'https://www.wellappointeddesk.com/2014/03/review-g-lalos-verge-de-france-writing-pad/',
    [('Vergé de France A5 pad', 'G. Lalo', '', '50 sheets, white or pistachio')]),
  X('Crane cotton stationery', 'American cotton-paper writing stationery from the currency-paper mill.', 'Crane', '1801', W + 'Crane_Currency',
    [('Crane Stationery', 'Crane', '', 'spun off 2015; Mohawk from 2018')]),
 ],
 'm': [['Original Crown Mill Pure Cotton Stationery Gift Set', 'Original Crown Mill'], ['Hobonichi Mini Letter Set', 'Hobonichi'], ['Midori Mogu Mogu Mini Letter Set', 'Midori'],
       ['Midori Letter Set with Animal Stickers', 'Midori'], ['Pepin Letter Writing Set', 'Pepin'], ['Seed OKU LETTER Mini Letter Set', 'Seed']]}


def B(n, c, f, seg, kf, d, s, lines=(), sig=()):
    return {'n': n, 'c': c, 'f': f, 'seg': seg, 'kf': kf, 'd': d, 'lines': list(lines), 'eras': [], 'sig': list(sig), 'sc': [], 'rel': [], 's': s}


brands = [
 B('Moleskine', 'Italy', '1997', 'Premium', 'notebooks', 'Milan notebook brand founded by Maria Sebregondi at Modo & Modo.', W + 'Moleskine', ['Notebook', 'Planners', 'Smart Writing'], ['Moleskine notebook']),
 B('Leuchtturm1917', 'Germany', '1917', 'Premium', 'notebooks, albums', 'Family firm re-established in Hamburg in 1948, maker of stamp and coin albums and notebooks.', 'https://www.gouletpens.com/blogs/fountain-pen-blog/leuchtturm1917-notebooks', ['Medium A5', 'Bullet Journal'], ['Leuchtturm1917 Medium A5']),
 B('Clairefontaine', 'France', '1858', 'Heritage manufactory', 'paper, notebooks', 'Paper mill at Étival-Clairefontaine in the Vosges; part of Exacompta Clairefontaine; owns Rhodia since 1997.', CF, ['1951', 'Triomphe'], ['Clairefontaine notebook']),
 B('Rhodia', 'France', '1932', 'Premium', 'orange pads', 'Notepad brand of the Vérilhac brothers, owned by Clairefontaine since 1997.', 'https://www.bloc-rhodia.com/gb/page/rhodia-universe/the-iconic-orange-pad', ['orange pad', 'DotPad', 'Webnotebook', 'Goalbook'], ['Rhodia orange pad']),
 B('Midori', 'Japan', '', 'Mainstream', 'MD paper', 'Japanese stationery brand of Designphil, maker of MD paper notebooks.', PA + '2017/8/18/the-midori-md-notebook-a5-gridded-a-review', ['MD Notebook', 'MD Paper Pad'], ['Midori MD Notebook']),
 B('TRAVELER\'S COMPANY', 'Japan', '2015', 'Premium', 'traveler\'s notebook', 'Brand separated from Midori in 2015 for the Traveler\'s Notebook.', TN, ['Traveler\'s Notebook'], ['Traveler\'s Notebook']),
 B('KOKUYO', 'Japan', '1905', 'Mainstream', 'Campus notebooks', 'Osaka stationery and office-furniture maker.', 'knowledge', ['Campus', 'Jibun Techo'], ['Kokuyo Campus']),
 B('Maruman', 'Japan', '', 'Mainstream', 'Mnemosyne notebooks', 'Japanese paper company named for its Mnemosyne line.', MN, ['Mnemosyne'], ['Maruman Mnemosyne']),
 B('Tomoegawa', 'Japan', '', 'Specialist', 'Tomoe River paper', 'Japanese paper maker that created Tomoe River paper and sold the formula to Sanzen.', TR, ['Tomoe River'], ['Tomoe River paper notebook']),
 B('Sanzen', 'Japan', '', 'Specialist', 'thin paper', 'Japanese paper maker producing Tomoe River paper since the 2020s.', TR, ['Tomoe River'], []),
 B('STALOGY', 'Japan', '', 'Mainstream', 'thin-paper notebooks', 'Japanese notebook brand of the Editor\'s Series.', PA + '2025/3/6/stalogy-editors-series-365days-a5-notebook-review', ['365 Days', 'Editor\'s Series'], ['Stalogy 365 Days']),
 B('Apica', 'Japan', '', 'Mainstream', 'smooth-paper notebooks', 'Japanese notebook maker of the CD notebook.', PA + '2020/4/2/apica-cd-premium-notebook-review', ['CD Premium'], ['Apica CD Premium']),
 B('Field Notes', 'United States', '2007', 'Artisan & independent', 'memo books', 'Chicago memo-book brand of Aaron Draplin and Jim Coudal.', W + 'Field_Notes', ['Original', 'Quarterly editions'], ['Field Notes']),
 B('Rite in the Rain', 'United States', '1916', 'Specialist', 'all-weather paper', 'Tacoma maker of waterproof field notebooks founded by Jerry Darling.', 'https://www.southsoundmag.com/travel-outdoor/rite-in-the-rain-celebrates-100th-birthday/article_c9bd19b7-23d1-5aa5-8c85-0821f32a3e76.html', ['field books'], ['Rite in the Rain']),
 B('Baron Fig', 'United States', '', 'Artisan & independent', 'notebooks', 'Notebook brand that began on Kickstarter.', PA + '2014/6/18/baron-fig-confidant-review', ['Confidant'], ['Baron Fig Confidant']),
 B('Filofax', 'United Kingdom', '1921', 'Heritage manufactory', 'ring organisers', 'Dalkeith-based organiser maker, formerly Norman & Hill.', W + 'Filofax', ['Personal', 'A5'], ['Filofax organiser']),
 B('Atoma', 'Belgium', '1948', 'Heritage manufactory', 'disc-bound notebooks', 'Original disc-binding system of André Thomas and André Martin, made by Mottart.', W + 'Disc-binding', ['Atoma'], ['Disc-bound notebook']),
 B('Levenger', 'United States', '', 'Premium', 'Circa notebooks', 'US retailer of the Circa disc-bound system.', W + 'Disc-binding', ['Circa'], []),
 B('Hobonichi', 'Japan', '', 'Premium', 'Techo planners', 'Publisher of the Hobonichi Techo, Hobo Nikkan Itoi Shinbun.', W + 'Hobonichi_Techo', ['Techo Original', 'Cousin', 'Weeks', '5-Year'], ['Hobonichi Techo']),
 B('G. Lalo', 'France', '', 'Heritage manufactory', 'writing paper', 'French maker of fine writing paper.', 'https://www.wellappointeddesk.com/2014/03/review-g-lalos-verge-de-france-writing-pad/', ['Vergé de France'], ['G. Lalo Vergé de France']),
 B('Crane', 'United States', '1801', 'Heritage manufactory', 'cotton paper', 'Dalton, Massachusetts cotton-paper maker; stationery arm owned by Mohawk since 2018.', W + 'Crane_Currency', ['Crane Stationery'], ['Crane cotton stationery']),
]

trads = [
 {'n': 'Étival papermaking (Clairefontaine)', 'g': 'Paper & stationery', 'r': 'Étival-Clairefontaine, Vosges, France', 'p': '1512 to present',
  'd': 'Papermaking on the Valdange and Meurthe at Étival, authorised by the abbey in 1512 and continued by the Clairefontaine mill.',
  'tech': 'machine-made smooth vellum writing paper from local forests', 'mat': 'wood pulp from Vosges fir and spruce',
  'forms': ['Clairefontaine notebook', 'Rhodia orange pad'], 'ctr': ['Papeteries de Clairefontaine', 'Exacompta Clairefontaine group'],
  'auth': 'Clairefontaine or Rhodia branding; very smooth paper that resists fountain-pen feathering', 's': CF},
]

notes = ('All seven planned kinds kept; old Planner cover, Refill notebook and Planner index tabs merged into one covers-refills-inserts kind. Old Notebook "Other notebooks" type dropped; composition, spiral and pocket kept as types. '
 'Old ranges (Rhodia, STALOGY, Tomoe River, Sunny Light, MD, Mnemosyne, Campus) turned into archetypes or models. Moleskine Classic sizes, Rhodia No. 16 and Webnotebook names, Letts, Quo Vadis and Midori diaries, Life Noble Note and Levenger Circa details not added (only search snippets, no retrieved page). '
 'Tomoe River treated as a maker and archetype rather than a craft tradition; one tradition added for Étival papermaking. kokuyo.com corporate history was blocked (403 and firecrawl proxy error) so kokuyostore.com history was used. Kokuyo facts from knowledge.')
out = {'kinds': [nb, ref, dia, cov, memo, loose, let], 'brands': brands, 'traditions': trads, 'notes': notes}
p = 'work/C5/shelves/02_00.json'
json.dump(out, open(p + '.tmp', 'w'), ensure_ascii=False, indent=1); os.replace(p + '.tmp', p)
print('archetypes', sum(len(k.get('x', [])) for k in out['kinds']))
