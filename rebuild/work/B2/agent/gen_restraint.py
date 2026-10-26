import json, os, sys
D = '/home/user/Possession-Taxonomy/rebuild/work/B2/shelves'
def K(n, d, s, a='', t=None, m=None, r=None, tg=None):
    k = {'n': n, 'a': a, 'd': d}
    if t: k['t'] = t
    if tg: k['tg'] = tg
    k['s'] = s
    if m: k['m'] = m
    if r: k['r'] = r
    return k
J = {}
J['00_04'] = ([
 K('Door mat', 'A hard-wearing mat laid at a door to wipe shoes and catch dirt.', 'https://www.ikea.com/sg/en/cat/rugs-carpets-textiles-10653',
   t=['coir', 'rubber', 'indoor', 'outdoor']),
 K('Bath mat', 'An absorbent mat laid beside a bath or shower to stand on with wet feet.', 'https://turkishtowelcompany.com/towel-guide',
   t=['cotton pile', 'memory foam', 'non-slip backed']),
 K('Kitchen mat', 'A mat or runner laid in front of a kitchen counter or sink to stand on while working.', 'https://www.wellnessmats.com/collections/all?page=11',
   a='anti-fatigue mat', t=['anti-fatigue mat', 'runner'], m=[['Original', 'Wellness Mats']]),
 K('Chair mat', 'A mat laid under a desk chair to protect the floor and let castors roll.', 'https://www.posturite.co.uk/floor-protector-chair-mat',
   t=['for carpet', 'for hard floor']),
], 'All four old kinds kept with their old sources; materials and anti-fatigue mat recorded as types. Kept the single old Wellness Mats model. Meditation mat moved to Cushions per plan (not on this shelf). No web research.')
J['01_03'] = ([
 K('Bed pillow', 'A stuffed pillow made to support the head in bed.', 'https://www.ikea.com/qa/en/cat/bedding-tl004',
   t=['down', 'feather', 'synthetic fibre', 'memory foam', 'latex', 'buckwheat', 'orthopaedic', 'body pillow', 'soft / medium / firm']),
 K('Travel pillow', 'A pillow, often U-shaped or inflatable, made to support the head and neck while sitting in transit.', 'https://www.coreproducts.com/products/therapeutica-travel-pillow',
   a='neck pillow', t=['U-shaped', 'inflatable', 'memory foam'],
   m=[['Therapeutica Travel Pillow', 'Core Products International'], ['Aeros Premium Travel Pillow', 'Sea to Summit']]),
 K('Positioning cushion', 'A shaped foam or inflatable cushion made to hold the body in a chosen position.', 'https://www.deltachildren.com/products/pregnancy-support-wedge-pillow',
   a='wedge · ramp', t=['wedge', 'ramp', 'pregnancy support']),
], 'Three old kinds kept with old sources; fills, firmness and shapes (orthopaedic, body pillow) recorded as types. Kept the two old travel-pillow models; no new makers added (no research).')
J['01_04'] = ([
 K('Mattress topper', 'A thick removable layer laid on a mattress to change its feel.', 'https://www.dunelm.com/category/home-and-furniture/bedding/all-bedding',
   t=['memory foam', 'latex', 'fibre', 'down']),
 K('Featherbed', 'A thick feather- or down-filled pad laid on top of the mattress to sleep on.', 'https://www.therange.co.uk/home-furnishings/bedding/mattress-toppers/goose-feather-bed-mattress-topper'),
 K('Mattress pad', 'A thin quilted or padded layer fitted over the mattress for light extra comfort.', 'https://shop.americantextile.com/pages/buying-guide-mattress-pad-protector-and-topper'),
 K('Mattress protector', 'A thin, often waterproof cover fitted over or around a mattress to guard it against spills and wear.', 'https://www.dunelm.com/category/home-and-furniture/bedding/100-cotton-bedding?page=14',
   t=['waterproof', 'fitted', 'encasement'], r=[['Mattress protectors', 'Bedgear']]),
 K('Pillow protector', 'A zipped, often waterproof or anti-allergy cover fitted under the pillowcase to guard a bed pillow.', 'https://www.ikea.com/qa/en/cat/bedding-tl004',
   t=['waterproof', 'anti-allergy']),
], 'Five old kinds kept, one per layer, with old sources. Bedgear\'s three protector SKUs (Air-X, Dri-Tec, Ver-Tex) trimmed to one brand-level range entry per the plan. Pillow protector sits with the protectors.')
J['02_00'] = ([
 K('Scatter cushion', 'A loose stuffed decorative cushion for a sofa, chair or bed.', 'https://superbalist.com/browse/apartment/home-decor/cushions-throws', a='throw pillow'),
 K('Cushion pad', 'A plain stuffed inner made to fill a cushion cover.', 'https://www.dunelm.com/category/home-and-furniture/home-furnishings/cushions/large-cushions',
   a='cushion insert', t=['feather', 'synthetic fibre']),
 K('Chair pad', 'A thin cushion, usually with ties or a non-slip back, made to lie on the seat of a chair.', 'https://www.ikea.com/us/en/cat/home-textiles-tl001',
   a='seat pad', t=['with ties', 'non-slip']),
 K('Floor cushion', 'A large frameless cushion made to sit on at floor level.', 'https://www.dunelm.com/category/home-and-furniture/home-furnishings/cushions/large-cushions',
   a='zabuton', t=['zabuton', 'pouffe-style', 'pillow stack']),
 K('Meditation cushion', 'A firm frameless cushion, round or crescent, made to sit on for meditation.', 'https://monasterystore.org/collections/memory-foam-zafu-meditation-cushions',
   a='zafu', t=['round', 'crescent'], m=[['Cloud Zafu', 'Monastery Store'], ['Mountain Seat Zafu', 'Monastery Store']]),
 K('Meditation mat', 'A flat padded mat laid on the floor under a meditation cushion or to sit on.', 'https://monasterystore.org/collections/memory-foam-zafu-meditation-cushions',
   a='zabuton', m=[['Cloud Zabuton', 'Monastery Store'], ['Mountain Seat Zabuton', 'Monastery Store']]),
], 'Six old kinds kept with old sources; meditation cushion and mat placed together. Floor-cushion forms recorded as types. Kept the four old Monastery Store models (paired cushion/mat lines, not a SKU dump).')
J['02_01'] = ([
 K('Cushion cover', 'A removable fabric case for a cushion, sold with or without the insert.', 'https://www.ikea.com/us/en/cat/home-textiles-tl001'),
 K('Sofa cover', 'A removable fabric cover for a sofa.', 'https://www.ikea.com/om/en/cat/extra-covers-10664',
   a='slipcover · throw-over cover · stretch cover', t=['fitted (made for one sofa model)', 'stretch', 'throw-over']),
 K('Chair cover', 'A removable fabric cover for a chair.', 'https://www.ikea.com/om/en/cat/extra-covers-10664',
   t=['fitted (made for one chair model)', 'stretch', 'dining chair', 'event chair']),
], 'Three old kinds kept with old sources; fitted, stretch and throw-over recorded as types. Dropped the IKEA model SKUs (NYHAMN sofa-bed cover, STRANDMON wing chair slipcover) per the plan.')
J['03_00'] = ([
 K('Curtain', 'A panel of fabric hung from a pole or track to cover a window or door.', 'https://www.dunelm.com/category/home-and-furniture/curtains-and-blinds/curtains',
   t=['pencil pleat', 'eyelet', 'tab top', 'pinch pleat', 'lined', 'unlined', 'blackout', 'thermal']),
 K('Sheer curtain', 'A curtain of light translucent fabric that filters light and gives daytime privacy.', 'https://www.dunelm.com/product/boucle-stripe-natural-tape-top-single-voile-panel-1000092973',
   a='voile · net curtain'),
 K('Shower curtain', 'A water-resistant curtain hung from a rail to close a shower or bath opening.', 'https://finnishdesignshop.com/en-us/bathroom/bathroom-textiles/shower-curtains',
   t=['fabric', 'plastic', 'with liner']),
], 'Three old kinds kept with old sources; heading styles (pencil pleat, eyelet, tab top, pinch pleat) and lining recorded as types. No models in old data; none added.')
J['03_01'] = ([
 K('Roller blind', 'A single panel of fabric that rolls up onto a tube at the head of the window.', 'https://en.wikipedia.org/wiki/Window_blind', t=['blackout', 'motorised', 'day and night']),
 K('Roman blind', 'A fabric blind that folds up into horizontal pleats as it is raised by cords.', 'https://en.wikipedia.org/wiki/Window_blind', t=['blackout', 'motorised']),
 K('Venetian blind', 'A blind of horizontal slats that tilt and lift on cords or tapes.', 'https://en.wikipedia.org/wiki/Window_blind', t=['aluminium', 'wood', 'faux wood', 'motorised']),
 K('Vertical blind', 'A blind of vertical vanes hung from a track that rotate and draw to one side.', 'https://en.wikipedia.org/wiki/Window_blind', t=['blackout', 'motorised']),
 K('Pleated blind', 'A blind of crisply pleated fabric that concertinas up or down.', 'https://en.wikipedia.org/wiki/Window_blind', t=['blackout', 'top-down bottom-up']),
 K('Cellular shade', 'A pleated blind of two or more fabric layers forming insulating cells.', 'https://en.wikipedia.org/wiki/Window_blind', a='honeycomb', t=['blackout', 'motorised', 'cordless']),
 K('Panel blind', 'Wide flat fabric panels that slide side to side on a multi-channel track.', 'https://en.wikipedia.org/wiki/Window_blind'),
 K('Tie-up shade', 'A fabric shade gathered up by hand and held by straps or ties, with no roller or cords.', 'https://www.wayfair.com/ideas-and-advice/guide-to-choosing-blinds-shades-S4522.html', a='roll-up shade'),
], 'All eight old kinds kept with old sources; blackout and motorised recorded as types where they apply. No models in old data; none added.')
J['03_02'] = ([
 K('Curtain pole', 'A rod fixed above a window or door from which curtains hang on rings or by their heading.', 'https://www.dunelm.com/category/home-and-furniture/curtains-and-blinds/tracks-poles-and-fixtures/all-tracks-and-poles?page=5',
   a='curtain rod', t=['bracket', 'finial', 'extendable', 'tension rod', 'metal', 'wood']),
 K('Curtain track', 'A fixed track with runners or gliders along which curtains are drawn.', 'https://www.ikea.com/gb/en/cat/curtain-track-18893/',
   a='curtain rail', t=['corded', 'bendable', 'ceiling-fixed', 'wall-fixed'], m=[['FRAMFUSIG', 'IKEA']], r=[['VIDGA', 'IKEA']]),
 K('Curtain fittings', 'Small hardware that attaches a curtain to its pole or track or holds it back when drawn.', 'https://www.dunelm.com/category/home-and-furniture/curtains-and-blinds/tracks-poles-and-fixtures/curtain-rings-and-fixtures?page=2',
   a='curtain rings · curtain hooks · tieback · holdback', t=['rings', 'hooks', 'gliders', 'clips', 'tiebacks', 'holdbacks'], r=[['VIDGA', 'IKEA']]),
], 'Five old kinds merged into three: pole bracket/finial into Curtain pole as types; rings and hooks plus tiebacks into Curtain fittings with rings, hooks, gliders, clips, tiebacks and holdbacks as types. Old sources kept; old IKEA FRAMFUSIG/VIDGA entries kept.')
for job, (kinds, notes) in J.items():
    if sys.argv[1:] and job not in sys.argv[1:]: continue
    p = os.path.join(D, job + '.json'); tmp = p + '.tmp'
    with open(tmp, 'w') as f: json.dump({'kinds': kinds, 'brands': [], 'traditions': [], 'notes': notes}, f, ensure_ascii=False, indent=1)
    os.replace(tmp, p)
