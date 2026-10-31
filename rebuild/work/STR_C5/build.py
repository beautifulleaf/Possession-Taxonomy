import json, os, copy, re, shutil
R = '/home/user/Possession-Taxonomy/rebuild/'
SRC = R + 'work/STR_C5/bak/C5.json'   # always rebuild from the untouched backup
d = json.load(open(SRC))
WP = 'https://en.wikipedia.org/wiki/'
FOUR = WP + 'Four_Treasures_of_the_Study'

old = {}
for dp in d['depts']:
    for s in dp['s']:
        for k in s['k']:
            old[k['n']] = k
used = set()

def get(name):
    used.add(name)
    return copy.deepcopy(old[name])

def arch(k, name):
    for i, x in enumerate(k.get('x', [])):
        if x['n'] == name:
            return k['x'].pop(i)
    raise KeyError(name)

def mod(name, new=None, d_=None, a=None, tt=None, see=None, drop_t=True):
    k = get(name)
    if new: k['n'] = new
    if d_: k['d'] = d_
    if a is not None: k['a'] = a
    if tt: k['tt'] = tt
    if drop_t: k.pop('t', None)
    if see: k['see'] = see
    return k

def new(n, a, dd, s, tt=None, x=None, see=None):
    k = {'n': n, 'a': a, 'd': dd, 's': s}
    if tt: k['tt'] = tt
    if x: k['x'] = x
    if see: k['see'] = see
    return k

def A(n, mk, y, dd, s, dt=None, v=None):
    o = {'n': n, 'a': '', 'd': dd, 'mk': mk, 'y': y, 's': s, 'v': v or []}
    if dt: o['dt'] = dt
    return o

def shelf(n, t, ks, ax=None):
    o = {'n': n, 't': t}
    if ax: o['ax'] = ax
    o['k'] = ks
    return o

# ---------------------------------------------------------------- department 1
fp = []
k = mod('Cartridge-converter fountain pen', tt=[
    ['Cartridge fit', ['Standard international', 'Proprietary']],
    ['Nib', ['Steel', 'Gold']],
    ['Body finish', ['Moulded resin', 'Metal', 'Urushi or maki-e lacquer']]])
k['d'] = 'Fountain pen filled from a sealed ink cartridge, or from a bottle through a removable converter; the usual modern pen.'
fp.append(k)
fp.append(mod('Piston-filling fountain pen', tt=[
    ['Mechanism', ['Screw piston', 'Threaded piston unit']],
    ['Barrel', ['Opaque', 'Clear demonstrator']]]))
fp.append(mod('Vacuum and plunger-filling fountain pen', tt=[
    ['Mechanism', ['Diaphragm (Vacumatic)', 'Plunger with shut-off valve', 'Power filler']]]))
fp.append(mod('Sac-filling fountain pen', tt=[
    ['Sac mechanism', ['Crescent', 'Lever', 'Button', 'Coin or matchstick', 'Pneumatic (Touchdown)', 'Snorkel', 'Aerometric', 'Squeeze sac', 'Capillary']]]))
fp.append(mod('Eyedropper fountain pen', tt=[
    ['Valve', ['Plain', 'With shut-off valve']],
    ['Barrel', ['Ebonite', 'Urushi-finished']]]))
fp.append(mod('Retractable-nib fountain pen', tt=[
    ['Release', ['Click', 'Twist', 'Safety (nib retracts into a sealed barrel)']]]))
k = mod('Calligraphy fountain pen', tt=[
    ['Nib', ['Stub or italic', 'Parallel-plate', 'Fude (bent)', 'Interchangeable set']]])
k['d'] = 'Fountain pen with a broad, italic, parallel-plate or bent nib, filled like any other pen, for edged-pen lettering.'
fp.append(k)
S_FP = shelf('Fountain pens',
    'Pens that carry their own ink in the barrel, grouped by how the ink gets in; a nib dipped in a bottle → Dip pens & glass pens, a ballpoint or gel pen → Everyday pens & pencils.',
    fp, 'kinds by how ink gets into the pen: cartridge, piston, vacuum, sac, eyedropper, retractable nib; pens with a special nib come last')

dp_ = []
dp_.append(new('Quill & reed pen', 'feather pen · reed pen · bamboo pen',
    'Pen cut from a bird\'s flight feather, or from a reed or bamboo stem, and dipped in ink; the writing tool before the steel nib.',
    WP + 'Quill',
    tt=[['Material', ['Goose feather', 'Swan feather', 'Turkey feather', 'Reed', 'Bamboo']]]))
k = mod('Dip pen holder', tt=[
    ['Shape', ['Straight', 'Oblique (flanged)']],
    ['Handle', ['Wood', 'Resin', 'Glass']],
    ['Nib size taken', ['Crow-quill (fine)', 'Standard']]],
    see=[['C4', 'Dip pen and nib', 'dip pens for drawing and lettering']])
arch(k, 'Oblique pen holder')   # generic description, already a type
dp_.append(k)
dp_.append(mod('Dip pen nib', tt=[
    ['Tip', ['Pointed flexible', 'Pointed firm', 'Broad-edge (square cut)', 'Left oblique']],
    ['Size', ['Crow quill (extra fine)']],
    ['Ink holding', ['No reservoir', 'Fitted reservoir', 'Slip-on reservoir']]],
    see=[['C4', 'Dip pen and nib', 'dip pens for drawing and lettering']]))
dp_.append(mod('Glass pen', tt=[
    ['Build', ['Glass tip on wooden or bamboo handle', 'All-glass', 'Twisted handle']]],
    see=[['C4', 'Dip pen and nib', 'dipped pens for drawing']]))
S_DIP = shelf('Dip pens & glass pens',
    'Pens dipped in the bottle for each line, from quills and reeds to steel nibs in holders and glass pens; a pen with its own ink reservoir → Fountain pens.',
    dp_, 'kinds from oldest to newest: feather and reed, steel nib and holder, glass')

br = []
br.append(mod('Calligraphy brush', tt=[
    ['Hair', ['Soft', 'Mixed', 'Hard']],
    ['Size', ['Large (ofude)', 'Medium (chufude)', 'Small (kofude)']],
    ['Tuft length', ['Long', 'Medium', 'Short']]],
    see=[['C4', 'Calligraphy and ink-painting brush', 'the same brush sold for painting']]))
k = mod('Ink stick', tt=[
    ['Soot', ['Pine soot (shoen)', 'Oil soot (yuen)']],
    ['Finish', ['Plain black', 'Coloured', 'Scented']]],
    see=[['C4', 'Inkstick and liquid sumi ink', 'the same ink sold for painting']])
arch(k, 'Coloured ink stick')   # generic; kept as the Finish type
br.append(k)
br.append(mod('Inkstone', tt=[
    ['Material', ['Stone', 'Ceramic (chengni)']],
    ['Form', ['Plain slab', 'Carved', 'With lid or box']],
    ['Age', ['New', 'Antique (over 100 years)']]],
    see=[['C4', 'Inkstone', 'the same object sold as an art supply']]))
br.append(mod('Calligraphy paper', tt=[
    ['Sizing', ['Raw (unsized)', 'Sized']],
    ['Format', ['Pre-cut sheets', 'Rolls']],
    ['Grade', ['Practice paper', 'Fine paper']]],
    see=[['C4', 'Xuan (rice) paper', 'the same paper sold for painting']]))
br.append(mod('Water dropper', tt=[
    ['Material', ['Ceramic', 'Bronze', 'Jade or stone']],
    ['Form', ['Plain', 'Figural (animal, fruit)']],
    ['Age', ['New', 'Antique']]]))
br.append(mod("Scholar's paperweight", tt=[
    ['Set', ['Single bar', 'Pair of bars']],
    ['Material', ['Brass', 'Wood', 'Stone or jade']],
    ['Age', ['New', 'Antique']]],
    see=[['B4', 'Glass paperweight', 'a decorative paperweight']]))
k = mod('Calligraphy desk accessories', tt=[
    ['Fitting', ['Felt underlay (shitajiki)', 'Brush rest (fudeoki)', 'Brush stand', 'Brush pot', 'Brush roll (fudemaki)', 'Ink-stick rest (sumioki)', 'Brush-rinsing pot']]])
k['d'] = 'Small fittings laid out for brush calligraphy: felt underlay, brush rest or stand, brush roll, ink-stick rest and brush-rinsing pot.'
k['s'] = FOUR
br.append(k)
br.append(mod('Calligraphy set', tt=[
    ['Grade', ['Student set', 'Boxed or lacquered set', 'Travel set']]]))
S_BR = shelf('Brush calligraphy tools',
    'East Asian brush-writing tools: brush, ink stick, inkstone and paper (the Four Treasures) with water droppers, weights and rests; a brush for painting → Craft & Art Supplies.',
    br, 'kinds by role at the desk: brush, ink, grinding stone, paper, then water, weights and rests, then boxed sets')

ip = []
ip.append(mod('Fountain pen ink', tt=[
    ['Colourant', ['Dye', 'Pigment (nanoparticle)', 'Iron gall']],
    ['Effect', ['Shimmer', 'High sheen']],
    ['Permanence', ['Washable', 'Permanent or document-proof']]],
    see=[['C4', 'Drawing ink', 'ink for dip pens and drawing']]))
k = ip[0]
# generic archetypes become ranges
for nm in ('Waterman ink', 'J. Herbin Encre'):
    x = arch(k, nm)
    k.setdefault('r', []).append([x['n'], x['mk']])
ip.append(mod('Fountain pen cartridge', tt=[
    ['Fit', ['Standard international (short)', 'Standard international (long)', 'Proprietary']],
    ['Ink', ['Dye', 'Pigment']]]))
ip.append(mod('Fountain pen converter', tt=[
    ['Mechanism', ['Piston', 'Squeeze']],
    ['Fit', ['Standard international', 'Proprietary']]]))
ip.append(mod('Fountain pen nib', tt=[
    ['Unit size', ['#5', '#6']],
    ['Material', ['Steel', 'Gold']],
    ['Fitting', ['Screw-in housing', 'Friction fit', 'Proprietary']],
    ['Grind', ['Factory', 'Custom grind']]]))
S_IP = shelf('Fountain pen ink & parts',
    'What feeds and fits a fountain pen: bottled ink, cartridges, converters and replacement nib units; a pen\'s own pen body → Fountain pens.',
    ip, 'kinds from the ink to the parts that carry it: bottled ink, cartridge, converter, nib unit')

DEPT1 = {
    'n': 'Fountain pens, ink & calligraphy', 'mode': 'variety',
    't': 'Fountain pens, dip and glass pens, East Asian brush-calligraphy tools, and the inks and parts that feed them; ballpoint, gel or felt-tip pens → Everyday pens & pencils; paints and art inks → Craft & Art Supplies.',
    'ax': 'How does the tool take up ink: from a reservoir in the barrel, by dipping, by a brush loaded from a ground stick, or is it the ink and parts themselves?',
    'shelves': [S_FP, S_DIP, S_BR, S_IP]}

# ---------------------------------------------------------------- department 2
bp = []
k = mod('Ballpoint pen', tt=[
    ['Operation', ['Stick (capped)', 'Retractable']],
    ['Ink', ['Oil-based', 'Low-viscosity hybrid', 'Pressurised refill']],
    ['Recording', ['Plain', 'Digital pen that records the writing']]],
    see=[['C1', 'EDC pen', 'tactical and carry pens']])
bp.append(k)
bp.append(mod('Gel pen', tt=[
    ['Operation', ['Capped', 'Retractable']],
    ['Tip', ['Needle tip', 'Ball tip']],
    ['Ink', ['Standard gel', 'Erasable (thermochromic)', 'Pigment / archival', 'Metallic and pastel']]]))
bp.append(mod('Rollerball pen', tt=[
    ['Operation', ['Capped', 'Retractable']],
    ['Supply', ['Disposable', 'Refillable (cartridge or RB refill)']],
    ['Ball', ['Metal', 'Ceramic']]]))
bp.append(mod('Multi pen', tt=[
    ['Tools in the barrel', ['2 pens', '3 pens', '4 pens', 'Pen and pencil']],
    ['Body', ['Fixed body', 'Build-your-own body']],
    ['Refill', ['D1 refills', 'Proprietary refills']]]))
bp.append(mod('Pen refill', tt=[
    ['Standard', ['G2 Parker-style (ISO 12757)', 'D1 mini (multi pens)', 'RB rollerball', 'Pilot G2 size', 'Uni SXR (Jetstream)', 'Cross-type']],
    ['Ink', ['Ballpoint', 'Gel', 'Rollerball']],
    ['Pressure', ['Standard', 'Pressurised']]]))
S_BP = shelf('Ballpoint, gel & rollerball pens',
    'Ball-tip pens by their ink: oil ballpoint, gel and liquid rollerball, with multi pens and refills; a fountain pen → Fountain pens, a felt-tip → Markers & fineliners.',
    bp, 'kinds by ink and tip: oil ballpoint, gel, liquid rollerball, then multi pens and refills')

mk_ = []
mk_.append(mod('Fineliner', tt=[
    ['Ink', ['Pigment (archival)', 'Dye-based']],
    ['Tip', ['Standard fibre tip', 'Metal-sleeved tip', 'Sign pen (broader fibre tip)']]],
    see=[['C4', 'Fineliner and technical drawing pen', 'drawing and technical pens']]))
mk_.append(mod('Highlighter', tt=[
    ['Tip', ['Chisel', 'Dual tip']],
    ['Colour range', ['Fluorescent', 'Pastel / mild']],
    ['Form', ['Marker', 'Gel stick', 'Dry (tape)']],
    ['Extra feature', ['Erasable', 'Refillable', 'Retractable']]],
    see=[['H1', 'Highlighter', 'same name, a make-up product']]))
mk_.append(mod('Permanent marker', tt=[
    ['Tip', ['Bullet', 'Chisel', 'Twin tip']],
    ['Marking job', ['General', 'Paint marker', 'Laundry / name marker']]]))
mk_.append(mod('Dry-erase marker', tt=[
    ['Tip', ['Bullet', 'Chisel']],
    ['Make', ['Standard', 'Low-odour', 'Refillable']],
    ['Surface', ['Dry-erase board', 'Wet-erase (overhead film)']]]))
mk_.append(mod('Brush pen', tt=[
    ['Tip', ['Felt brush (firm)', 'Bristle brush']],
    ['Supply', ['Cartridge-fed (refillable)', 'Disposable']],
    ['Ends', ['Single', 'Double-sided']]],
    see=[['C4', 'Brush pens', 'brush pens for drawing and lettering']]))
S_MK = shelf('Markers, fineliners & highlighters',
    'Felt-tip and fibre-tip pens by the job of the ink: fine writing, marking text, permanent marking, wipe-off boards and brush lettering; a ball-tip pen → Ballpoint, gel & rollerball pens.',
    mk_, 'kinds by the job of the ink: fine writing, highlighting, permanent marking, wipe-off, brush lettering')

pc = []
k = mod('Wooden pencil', tt=[
    ['Section', ['Hexagonal', 'Round', 'Triangular']],
    ['Grade scale', ['H and B scale (10H to 12B)', 'US numbers 1–4']],
    ['Length', ['Full length', 'Short (golf or library)']],
    ['Top', ['Plain', 'With eraser tip']]],
    see=[['C4', 'Graphite pencil', 'drawing grades'], ['C4', 'Coloured pencil', 'colour pencils']])
k['s'] = k.get('s') or WP + 'Pencil'
pc.append(k)
pc.append(mod('Mechanical pencil', tt=[
    ['Advance', ['Click (ratchet)', 'Twist (screw)']],
    ['Build', ['Standard', 'Drafting (long lead sleeve)', 'Retractable tip']],
    ['Special feature', ['Auto-rotating lead', 'Lead-protecting']],
    ['Lead diameter', ['0.2–0.3 mm', '0.5 mm', '0.7 mm', '0.9–1.4 mm']]]))
pc.append(mod('Lead holder', tt=[
    ['Lead diameter', ['2 mm', '3.15 mm', '5.6 mm']],
    ['Body', ['All-metal', 'With cap sharpener']]]))
pc.append(mod('Pencil leads', tt=[
    ['Diameter', ['0.2–0.3 mm', '0.5 mm', '0.7 mm', '0.9 mm and thicker', 'Clutch-pencil (1.18–5.6 mm)']],
    ['Core', ['Polymer-bound graphite', 'Coloured']]]))
pc.append(new('Pencil extender', 'pencil holder · stub holder',
    'Holder into which a short pencil stub is fitted so that it can be used until almost nothing is left.',
    WP + 'Pencil', tt=[['Material', ['Metal', 'Wood', 'Plastic']]]))
pc.append(mod('Pencil sharpener', tt=[
    ['Power', ['Hand-held', 'Rotary (crank)', 'Electric']],
    ['Point', ['Standard', 'Two-step long point', 'Lead pointer (for lead holders)']]]))
S_PC = shelf('Pencils',
    'Graphite pencils and what feeds, extends or sharpens them: wood-cased, mechanical and lead-holder pencils; coloured and art pencils → Craft & Art Supplies.',
    pc, 'kinds by how the lead is held: in wood, pushed by a mechanism, or clutched; then leads, extenders and sharpeners')

er = []
er.append(mod('Eraser', tt=[
    ['Form', ['Block', 'Stick (pen-style)', 'Kneaded']],
    ['Material', ['Rubber', 'Foam', 'Plastic']],
    ['Drive', ['Hand', 'Electric']],
    ['Mark removed', ['Pencil', 'Ink']]],
    see=[['C4', 'Eraser and blending tool', 'erasers for drawing']]))
er.append(mod('Correction tape', tt=[
    ['Supply', ['Disposable', 'Refillable']],
    ['Tape width', ['4 mm', '5 mm', '6 mm']]]))
er.append(mod('Correction fluid', tt=[
    ['Applicator', ['Brush bottle', 'Correction pen']]]))
S_ER = shelf('Erasers & correction',
    'Ways to remove a mark: rubbing it out, covering it with tape or covering it with fluid; a drawing eraser → Craft & Art Supplies.',
    er, 'kinds by how the mark goes: rubbed out, covered by tape, covered by fluid')

DEPT2 = {
    'n': 'Everyday pens & pencils', 'mode': 'mixed',
    't': 'Pens, markers, pencils and erasers for everyday writing and marking; a pen with its own ink reservoir for fine writing → Fountain pens, ink & calligraphy; art pens and pencils → Craft & Art Supplies.',
    'ax': 'What mark does it make or remove: a ball-tip line, a felt-tip or marker line, a graphite line, or the removal of a mark?',
    'shelves': [S_BP, S_MK, S_PC, S_ER]}

# ---------------------------------------------------------------- department 3
nb = []
k = mod('Notebook', tt=[
    ['Binding', ['Sewn hardcover', 'Thread-stitched softcover', 'Perfect-bound', 'Spiral or twin-wire']],
    ['Ruling', ['Plain', 'Lined', 'Grid', 'Dot grid']],
    ['Paper', ['Standard', 'Thin fountain-pen paper', 'Waterproof paper']],
    ['Size', ['Pocket', 'A6', 'A5', 'B5', 'A4']]],
    d_='Bound book of blank, lined, grid or dotted pages for everyday notes; differs by binding, cover, size and paper.',
    a='journal · memo book · writing book',
    see=[['C4', 'Sketchbook', 'a notebook for drawing'], ['D2', 'E-paper writing tablet', 'handwriting on a screen'],
         ['F5', 'Written-in notebook', 'a filled notebook kept as a record']])
fn = arch(k, 'Field Notes')
rr = arch(k, 'Rite in the Rain')
mead = None
for i, m in enumerate(k['m']):
    if m[0] == 'Mead Five Star Composition Notebook':
        mead = k['m'].pop(i); break
nb.append(k)
cb = new('Composition book', 'composition notebook · marble notebook',
    'Notebook of sewn pages in a stiff pasteboard cover, usually ruled, used at school and in the office.',
    WP + 'Notebook',
    tt=[['Ruling', ['Wide-ruled', 'College-ruled', 'Graph']]])
cb['m'] = [mead]
nb.append(cb)
rn = new("Reporter's notebook", 'steno pad · pocket memo book · memo book',
    'Small notebook, usually top-bound, held in one hand for jotting notes on the move; also sold as the steno pad.',
    WP + 'Notebook', tt=[['Binding', ['Top spiral', 'Side spiral', 'Stapled']]], x=[fn])
nb.append(rn)
lf = new('Lab & field notebook', 'lab notebook · field book · surveyor\'s notebook',
    'Hard-wearing notebook for recording experiments or fieldwork, often with numbered pages, graph paper or weatherproof pages.',
    WP + 'Notebook',
    tt=[['Cover', ['Hard-bound', 'Soft']], ['Paper', ['Standard', 'All-weather']], ['Ruling', ['Graph', 'Lined', 'Plain']]], x=[rr])
nb.append(lf)
k = mod('Refillable notebook system', tt=[
    ['Format', ['Travel notebook (elastic-held inserts)', 'Ring organiser', 'Disc-bound']]])
for x in k['x']:
    if x['n'] == 'Disc-bound notebook':
        x['n'] = 'Atoma disc-bound system'
nb.append(k)
nb.append(mod('Planner or notebook cover, refills & inserts', new='Notebook & planner covers, refills & inserts',
    tt=[['Part', ['Cover', 'Refill notebook', 'Index tabs', 'Pocket insert']]]))
S_NB = shelf('Notebooks & journals',
    'Books of blank, lined, grid or dotted pages for notes: everyday, school, reporting and field notebooks and the covers and refills of refillable systems; a book ruled by date → Planners & calendars.',
    nb, 'kinds by what the book is made for: everyday notes, school, reporting, field and lab work, then refillable systems and their parts')

pl = []
pl.append(mod('Diary or planner', tt=[
    ['Page layout', ['Daily (page a day)', 'Weekly', 'Monthly', 'Five-year']],
    ['Dating', ['Dated', 'Undated']]],
    see=[['F5', 'Diary or journal', 'a diary written in and kept'], ['I2', 'Digital planner', 'a planner file for a tablet']]))
pl.append(mod('Calendar', tt=[
    ['Placement', ['Wall', 'Desk', 'Pocket']],
    ['View', ['Monthly', 'Weekly', 'Year planner']],
    ['Form', ['Bound', 'Tear-off', 'Sticky-note']]],
    a='wall calendar · desk calendar · ひめくり · himekuri'))
pl.append(mod('Sticker sheet', tt=[
    ['Purpose', ['Planner stickers', 'Decorative']],
    ['Adhesive', ['Permanent', 'Removable']]],
    see=[['F3', 'Collectible sticker', 'stickers collected as a series']]))
S_PL = shelf('Planners & calendars',
    'Books and sheets ruled by date for planning, and the stickers that mark them up; an undated blank book → Notebooks & journals.',
    pl, 'kinds by how the dates are carried: bound in a planner, printed on a sheet, added as stickers')

ls = []
ls.append(mod('Memo pad', tt=[
    ['Binding', ['Top-stapled', 'Top-spiral', 'Glued block']],
    ['Shape', ['Rectangular', 'Square memo']]]))
lp = new('Legal pad', 'yellow pad · legal notepad',
    'Pad of ruled sheets glued at the head, traditionally yellow, with a margin ruled down the left.',
    WP + 'Notebook',
    tt=[['Paper colour', ['Yellow', 'White']], ['Binding', ['Glued head', 'Wire-bound']]],
    x=[A('Silver City Writing Tablet', '', '1902', 'Australian pad of glued, halved sheets on a cardboard backing, named as a precursor of the legal pad.', WP + 'Notebook')])
ls.append(lp)
ls.append(mod('Sticky notes', tt=[
    ['Shape', ['Square pad', 'Die-cut shape', 'Standing']],
    ['Use', ['Plain', 'Ruled', 'Index flags']]]))
ls.append(mod('Index card', tt=[
    ['Ruling', ['Plain', 'Ruled', 'Grid']],
    ['Binding', ['Loose', 'Ring-bound']]]))
ls.append(mod('Loose-leaf paper', tt=[
    ['Size', ['A4 / letter', 'A5', 'B5 (26-hole)']],
    ['Paper', ['Everyday', 'Fountain-pen paper']]]))
ls.append(mod('Printer paper', tt=[
    ['Size', ['A4', 'US Letter', 'A3']],
    ['Weight', ['70–80 gsm everyday', '90–100 gsm premium']],
    ['Fibre', ['Virgin', 'Recycled']]],
    see=[['D1', 'Printer', 'the machine it feeds']]))
S_LS = shelf('Pads, loose paper & notes',
    'Paper sold as pads, packs and reams for jotting, flagging, filing and printing; a sewn or bound book → Notebooks & journals.',
    ls, 'kinds by how the sheets are held: glued pad, adhesive pad, loose card, punched sheet, ream')

ps = []
ps.append(mod('Letter-writing paper set', tt=[
    ['Format', ['Boxed letter set', 'Writing pad with envelopes', 'Correspondence cards']],
    ['Paper', ['Cotton', 'Laid']]]))
ps.append(mod('Envelope', tt=[
    ['Size', ['DL', 'C5', 'C4']],
    ['Closure', ['Self-seal', 'Gummed']],
    ['Window', ['Windowed', 'Plain']],
    ['Paper', ['Standard', 'Laid', 'Airmail']]],
    see=[['F3', 'Stamped envelope', 'postal stationery collected for its stamps']]))
ps.append(mod('Padded envelope', tt=[['Padding', ['Bubble-lined', 'Paper-padded']]]))
ps.append(mod('Mailing tube', tt=[['Section', ['Round', 'Triangular']]]))
ps.append(mod('Greeting card', tt=[
    ['Inside', ['Blank', 'With message']],
    ['Occasion', ['Birthday', 'Thank-you', 'Seasonal']]]))
ps.append(mod('Gift wrap', tt=[['Form', ['Roll', 'Sheet', 'Tissue paper']]]))
ps.append(new('Adhesive label', 'address label · file-folder label · name tag',
    'Self-adhesive label, blank or printed, for addresses, file folders and name tags.',
    WP + 'Office_supplies',
    tt=[['Use', ['Address label', 'File-folder label', 'Name tag']], ['Format', ['Sheets', 'Rolls']]]))
S_PS = shelf('Letters, post & wrapping',
    'Paper made up for writing a letter, enclosing and posting it, or giving a card or present; plain loose paper → Pads, loose paper & notes.',
    ps, 'kinds by what is sent or given: the letter, its envelope, parcels, cards, wrapping and labels')

DEPT3 = {
    'n': 'Notebooks, planners & paper', 'mode': 'mixed',
    't': 'Paper made up for writing, planning, jotting or posting; blank paper for drawing → Craft & Art Supplies; a printed book to read → Media & Publications.',
    'ax': 'How is the paper made up for use: bound as a book, dated as a planner, cut as loose pads and notes, or made up for posting and giving?',
    'shelves': [S_NB, S_PL, S_LS, S_PS]}

# ---------------------------------------------------------------- department 4
SEAL = WP + 'Seal_(East_Asia)'
RS = WP + 'Rubber_stamp'
es = []
k = mod('Name seal', tt=[
    ['Seal type', ['Jitsu-in (registered)', 'Ginkō-in (bank)', 'Mitome-in (everyday)', 'Korean ingam (registered)', 'Chinese name chop', 'Pre-inked name stamp']],
    ['Material', ['Stone', 'Wood', 'Horn', 'Bamboo or plastic']]],
    see=[['F2', 'Carved seal', 'a carved seal as an art object']])
es.append(k)
es.append(new("Artist's & collector's seal", 'gagō-in · nakkwan · studio seal · collection seal · leisure seal',
    'Carved seal that marks a painting, calligraphy or book as the artist\'s, the studio\'s or the collector\'s, rather than naming a person for legal use.',
    SEAL,
    tt=[['Seal kind', ["Artist's name (gagō-in, nakkwan)", 'Studio seal', 'Alias seal', 'Collection seal', 'Leisure-saying seal', 'Portrait seal']],
        ['Material', ['Stone', 'Jade', 'Wood', 'Horn']]],
    see=[['F2', 'Carved seal', 'a carved seal as an art object']]))
es.append(mod('Seal paste', tt=[
    ['Form', ['Paste in a tin', 'Sponge-type pad']],
    ['Binder', ['Silk', 'Plant (moxa)']]],
    see=[['C4', 'Seal paste and seal stone', 'the same paste sold as an art supply']]))
S_ES = shelf('East Asian seals & paste',
    'Carved personal and artist\'s seals stamped in red paste to sign, register or mark a work; a Western desk or wax seal → Wax seals & embossers.',
    es, 'kinds from the seal to the paste: personal name seal, artist\'s and collector\'s seal, seal paste')

ws = []
k = mod('Wax seal stamp', tt=[
    ['Form', ['Handled desk seal', 'Interchangeable head', 'Signet ring']],
    ['Design', ['Monogram or initial', 'Custom die']]],
    see=[['A3', 'Signet ring', 'the ring form worn as jewellery']])
x = arch(k, 'Herbin brass wax seal')
k.setdefault('r', []).append(['J. Herbin wax seal stamps', x['mk']])
ws.append(k)
k = mod('Sealing wax', tt=[
    ['Form', ['Traditional stick (with or without wick)', 'Flexible (mailable) wax', 'Glue-gun sticks', 'Granules or beads', 'Faux (self-adhesive) seals']]])
x = arch(k, 'J. Herbin sealing wax')
k.setdefault('r', []).append([x['n'], x['mk']])
ws.append(k)
ws.append(new('Embossing seal', 'notary embosser · seal press',
    'Hand or desk press that raises a seal design in the paper without ink; best known as the notary seal.',
    'https://engineersealstamps.com/blogs/info/notary-seal-embosser',
    tt=[['Style', ['Handheld', 'Desk']]]))
S_WS = shelf('Wax seals & embossers',
    'Seals that leave a pressed mark: engraved matrices pressed into sealing wax, and embossers that raise the paper; an inked stamp → Ink stamps.',
    ws, 'kinds by how the mark is made: pressed into wax, or raised in the paper')

st = []
rs = mod('Rubber stamp', tt=[
    ['Message', ['Word stamp', 'Address stamp', 'Dater']],
    ['Die', ['Rubber', 'Polymer']]],
    d_='Hand stamp with a rubber or polymer die, pressed on a separate ink pad, for words, addresses or dates on office papers.',
    a='hand stamp · office stamp')
st.append(rs)
k = new('Self-inking stamp', 'self-inker · automatic stamp',
    'Stamp whose die rests against a built-in ink pad and flips down to print when pressed on the paper.',
    RS,
    tt=[['Message', ['Word stamp', 'Address stamp', 'Dater']], ['Mechanism', ['Flip-down die', 'Pocket stamp']]])
k['x'] = [a_ for a_ in [] ]
# archetype and models carried over from the old Rubber stamp
oldrs = old['Rubber stamp']
k['x'] = [copy.deepcopy(a_) for a_ in oldrs.get('x', [])]
k['m'] = copy.deepcopy(oldrs.get('m', []))
rs.pop('x', None); rs.pop('m', None)
st.append(k)
st.append(new('Pre-inked stamp', 'flash stamp',
    'Stamp whose die is itself impregnated with ink, so it needs no separate pad and gives many impressions.',
    RS, tt=[['Message', ['Word stamp', 'Address stamp', 'Dater']]]))
st.append(new('Stamp ink pad', 'ink pad · stamp pad',
    'Pad of ink-soaked material pressed against a stamp die; refill ink restores it.',
    RS, tt=[['Ink', ['Dye', 'Pigment']], ['Pad', ['Felt', 'Foam']]],
    see=[['C4', 'Ink pad', 'ink pads for craft stamping']]))
S_ST = shelf('Ink stamps',
    'Stamps and pads that leave an inked mark on office papers, whether the die is dipped, self-inking or pre-inked; a wax seal → Wax seals & embossers.',
    st, 'kinds by how the die is inked: separate pad, built-in pad, ink in the die, then the pad itself')

DEPT4 = {
    'n': 'Seals, stamps & sealing wax', 'mode': 'mixed',
    't': 'Tools that press a personal, wax or ink mark on paper to sign, close or authenticate it; stamps for crafts → Craft & Art Supplies; postage stamps → Coins, Stamps, Medals & Trading Cards.',
    'ax': 'What leaves the mark: red paste from a carved seal, melted wax pressed with a seal, a raised impression, or stamp ink?',
    'shelves': [S_ES, S_WS, S_ST]}

# ---------------------------------------------------------------- department 5
dt = []
dt.append(mod('Desk organiser', tt=[['Form', ['Multi-compartment organiser', 'Pen cup', 'Drawer unit', 'Rotating caddy']]]))
dt.append(mod('Letter tray & magazine file', tt=[['Form', ['Letter tray', 'Stacking tray', 'Magazine file']]]))
dt.append(mod('Pen case', tt=[['Form', ['Single-pen sleeve', 'Pen roll', 'Zip case', 'Box', 'Pouch']]]))
dt.append(mod('Desk pad', tt=[['Material', ['Leather (blotter)', 'Felt or PU (mat)', 'Paper (tear-off pad)']]],
    see=[['D1', 'Mouse pad or desk mat', 'a mat for a keyboard and mouse']]))
dt.append(mod('Clipboard', tt=[['Form', ['Board', 'Folding (clip folder)', 'Storage box']]]))
dt.append(mod('Wall board', tt=[
    ['Surface', ['Dry-erase (melamine)', 'Magnetic steel', 'Glass', 'Cork', 'Fabric', 'Chalkboard']],
    ['Mounting', ['Wall-hung', 'Mobile easel']]]))
S_DT = shelf('Desk tidies, pads & boards',
    'Things that hold pens and papers or give a surface to write on: organisers, trays, pen cases, desk pads, clipboards and wall boards; a desk itself → Furniture & Storage.',
    dt, 'kinds by where it sits: on the desk top, as the writing surface, in the hand, on the wall')

da = []
da.append(mod('Inkwell', tt=[
    ['Material', ['Glass', 'Porcelain', 'Silver or pewter', 'Brass']],
    ['Form', ['Desk inkwell', 'Travelling (screw lid)']],
    ['Age', ['New', 'Antique (over 100 years)']]]))
da.append(mod('Letter opener', tt=[
    ['Material', ['Steel', 'Silver or pewter', 'Wood', 'Ivory or bone handle (antique)']],
    ['Age', ['New', 'Antique paper knife']]]))
S_DA = shelf('Desk accessories & collectables',
    'Traditional pieces for a writing desk that are also collected: inkwells and letter openers; a decorative paperweight → Decor.',
    da)

ff = []
ff.append(mod('Ring binder', tt=[
    ['Ring layout', ['2-ring', '4-ring', 'D-ring']],
    ['Format', ['Lever arch', 'Presentation (clear overlay)']]]))
ff.append(mod('Folder', tt=[
    ['Form', ['Folder', 'Document wallet', 'Clear pocket folder', 'Suspension file', 'Box file']],
    ['Build', ['Standard', 'Heavy-duty', 'Expanding']]],
    see=[['B1', 'Filing cabinet', 'where suspension files hang']]))
k = mod('Clips, pins & fasteners', new='Clips', tt=[
    ['Clip', ['Paper clip', 'Bulldog clip', 'Binder clip']],
    ['Finish', ['Bare steel', 'Plastic-coated']]],
    d_='Spring or wire clips that hold sheets together: paper clips, bulldog clips and binder clips.',
    a='paper clip · binder clip · bulldog clip')
ff.append(k)
k2 = new('Pins, bands & tags', 'drawing pin · rubber band · treasury tag · office magnet',
    'Small fasteners that pin papers to a board or bind them: drawing pins, rubber bands, treasury tags, split pins and magnets.',
    old['Clips, pins & fasteners'].get('s') or WP + 'Office_supplies',
    tt=[['Fastener', ['Drawing pin', 'Rubber band', 'Treasury tag', 'Split pin (paper fastener)', 'Office magnet']]])
ff.append(k2)
S_FF = shelf('Files & fasteners',
    'Covers, boxes and small fasteners that keep sheets together: ring binders, folders, clips, pins and bands; a filing cabinet → Furniture & Storage.',
    ff, 'kinds by how the sheets are held: on rings, in a cover, by a clip, by a pin or band')

sc = []
sc.append(mod('Stapler', tt=[
    ['Reach', ['Desktop', 'Plier', 'Long-arm']],
    ['Duty', ['Standard', 'Heavy-duty']],
    ['Drive', ['Manual', 'Electric']]]))
sc.append(mod('Hole punch', tt=[
    ['Holes', ['1-hole', '2-hole', '4-hole']],
    ['Duty', ['Light', 'Heavy-duty']]],
    see=[['C4', 'Craft paper punch', 'shaped punches for crafts']]))
sc.append(mod('Desk tape & dispenser', tt=[
    ['Tape', ['Clear', 'Matte invisible', 'Double-sided']]],
    see=[['C8', 'Tape dispenser', 'larger parcel-tape dispensers']]))
sc.append(mod('Glue stick', tt=[['Glue', ['Standard', 'Disappearing colour', 'Acid-free']]],
    see=[['C4', 'Craft glue', 'glues for crafts']]))
sc.append(mod('Scissors', tt=[['Made for', ['Office', 'Left-handed', "Children's"]]],
    see=[['C4', 'Craft scissors', 'scissors for crafts']]))
sc.append(mod('Paper trimmer', tt=[['Cutter', ['Guillotine', 'Rotary']]],
    see=[['C4', 'Craft paper trimmer', 'trimmers for crafts']]))
S_SC = shelf('Staplers, tape & cutting',
    'Tools that join or cut sheets: staplers, hole punches, tape, glue sticks, scissors and trimmers; a craft knife → Craft & Art Supplies.',
    sc, 'kinds by job: fasten with wire, punch holes, stick with tape or glue, cut')

rl = []
rl.append(mod('Ruler', tt=[['Material', ['Plastic', 'Steel', 'Wooden', 'Flexible']], ['Length', ['15 cm', '30 cm']]]))
rl.append(mod('Geometry set', tt=[['Case', ['Tin', 'Zip case']]]))
rl.append(mod('Drawing compass', tt=[['Type', ['School compass', 'Precision bow compass', 'Beam compass']]],
    see=[['E2', 'Navigation compass', 'a different instrument, for direction']]))
rl.append(mod('Postal scale', tt=[['Display', ['Digital', 'Mechanical']]]))
S_RL = shelf('Rulers, compasses & scales',
    'Instruments for measuring papers and parcels: rulers, geometry sets, drawing compasses and postal scales; a workshop measure → Tools & Workshop Equipment.',
    rl, 'kinds by what is measured: length, angles and circles, weight')

DEPT5 = {
    'n': 'Desk & filing supplies', 'mode': 'tier',
    't': 'Everyday supplies that keep, fasten, cut and measure papers at a desk; pens → Everyday pens & pencils, paper and pads → Notebooks, planners & paper, desks and cabinets → Furniture & Storage.',
    'ax': 'What does it do on the desk: hold and display things, file and fasten papers, join and cut them, measure them, or serve as a traditional desk piece?',
    'shelves': [S_DT, S_DA, S_FF, S_SC, S_RL]}
for x_ in ('note',):
    pass

# ---------------------------------------------------------------- department 6
CAL = WP + 'Calculator'
TW = WP + 'Typewriter'
ca = []
ca.append(mod('Basic calculator', tt=[
    ['Format', ['Pocket', 'Desktop']],
    ['Power', ['Solar', 'Battery']],
    ['Keys', ['Standard', 'Tax and currency keys']]],
    d_='Calculator for the four operations and percentages, from pocket to desktop models.',
    a='desk calculator · pocket calculator'))
ca.append(mod('Scientific calculator', tt=[
    ['Display', ['Natural (textbook)', 'Two-line']],
    ['Power', ['Solar with battery backup', 'Battery']],
    ['Entry', ['Algebraic', 'RPN']],
    ['Programming', ['Fixed functions', 'Programmable']]]))
ca.append(mod('Graphing calculator', tt=[
    ['Screen', ['Monochrome', 'Colour']],
    ['Algebra', ['Numeric', 'CAS (computer algebra)']],
    ['Programmable in', ['Calculator language', 'Python']]]))
ca.append(mod('Financial calculator', tt=[['Entry', ['RPN', 'Algebraic']]]))
ca.append(new('Printing calculator', 'adding machine · tape calculator',
    'Desktop calculator that prints each entry and result on a paper roll, used for adding up accounts.',
    CAL, tt=[['Printing', ['Ink roller', 'Thermal paper']]]))
S_CA = shelf('Calculators',
    'Electronic calculators by the work the keys do: four operations, science, plotting, money and a printed paper trail; a computer or phone app → Computers & Components.',
    ca, 'kinds by the work the keys do: four operations, science, plotting, money, paper trail')

ct = []
ct.append(mod('Abacus', tt=[
    ['Bead layout', ['2:5 (suanpan)', '1:4 (soroban)', '10 beads, horizontal wires (schoty)']],
    ['Use', ['Calculating frame', "Children's counting frame"]]]))
ct.append(mod('Slide rule', tt=[
    ['Sides', ['Simplex', 'Duplex']],
    ['Scale system', ['Rietz', 'Darmstadt', 'Log-log']],
    ['Form', ['Straight', 'Pocket (5 in / 12.5 cm)', 'Circular', 'Cylindrical']],
    ['Specialism', ['General', 'Electrical', 'Flight computer']]]))
ct.append(mod('Mechanical calculator', tt=[
    ['Mechanism', ['Stepped drum (arithmometer)', 'Pinwheel', 'Key-driven adder', 'Slide adder']],
    ['Drive', ['Hand', 'Electric']]],
    d_='Hand- or motor-driven geared machine for arithmetic, from arithmometers and pinwheel calculators to key-driven adders and the Curta.',
    a='arithmometer · pinwheel calculator · comptometer'))
ct.append(mod('Vintage electronic calculator', tt=[
    ['Display', ['LED', 'Vacuum fluorescent']],
    ['Logic', ['Algebraic', 'RPN', 'Programmable']],
    ['Format', ['Desk', 'Pocket']]]))
S_CT = shelf('Calculating antiques & collectables',
    'Calculating devices collected for their age and craft: counting frames, slide rules, geared machines and the first electronic calculators; a current calculator → Calculators.',
    ct, 'kinds by age of the technology: counting frame, slide rule, geared machine, early electronic')

tw = []
k = mod('Typewriter', new='Manual typewriter', tt=[
    ['Print element', ['Typebar (understrike)', 'Typebar (frontstrike)', 'Typewheel', 'Index']],
    ['Size', ['Standard (desktop)', 'Portable', 'Ultra-portable']],
    ['Layout', ['QWERTY', 'QWERTZ', 'AZERTY']],
    ['Typeface', ['Pica', 'Elite', 'Script']]],
    d_='Machine that prints characters on paper as the typist strikes keys, with no motor; collected by maker, model and era.',
    a='manual typewriter · portable typewriter')
ib = k['x']
sel = arch(k, 'IBM Selectric')
ib.insert(0, A('Hansen Writing Ball', 'Rasmus Malling-Hansen', '1870',
    'Machine with 52 keys on a brass hemisphere, invented in 1865 and the first typewriter sold commercially.',
    WP + 'Hansen_Writing_Ball'))
for i_, a_ in enumerate(ib):
    if a_['n'] == 'Sholes and Glidden':
        ib.insert(i_ + 1, A('Hammond Typewriter', 'Hammond Typewriter Company', '1884',
            'Machine with a curved keyboard and interchangeable type sectors, invented in 1880 and released in 1884.', TW))
        break
tw.append(k)
el = new('Electric typewriter', 'electric typewriter · typeball typewriter',
    'Typewriter whose motor powers the typing action, with typebars, a typeball or a daisy wheel as the print element.',
    TW,
    tt=[['Print element', ['Typebar', 'Typeball', 'Daisy wheel']], ['Spacing', ['Monospaced', 'Proportional']]],
    x=[sel,
       A('IBM Electromatic Model 04', 'IBM', '1941', 'IBM electric typewriter that introduced proportional spacing.', TW),
       A('Smith-Corona Coronamatic', 'Smith Corona', '1973', 'Electric typewriter with interchangeable ribbon cartridges.', TW)])
tw.append(el)
tw.append(new('Electronic typewriter', 'word-processing typewriter · daisywheel typewriter',
    'Typewriter run by integrated circuits, often with a daisy wheel or thermal print head and a small display.',
    TW,
    tt=[['Print element', ['Daisy wheel', 'Thermal print head']], ['Display', ['None', 'Small display']]],
    x=[A('Olivetti Tes 501', 'Olivetti', '1976', 'The first electronic daisywheel typewriter marketed.', TW),
       A('Canon Typestar 110', 'Canon', '1989', 'Late electronic typewriter, shown on the Typewriter page as an example of the type.', TW)]))
S_TW = shelf('Typewriters',
    'Machines that type on paper, from the first commercial writing ball to manual portables, electric office machines and electronic models; a keyboard for a computer → Computers & Components.',
    tw, 'kinds by what drives the print: the typist\'s strike, a motor, a chip')

om = []
om.append(mod('Label maker', tt=[['Form', ['Handheld', 'Desktop', 'App-connected']]]))
om.append(mod('Shredder', tt=[
    ['Cut', ['Strip-cut', 'Cross-cut', 'Micro-cut']],
    ['Feed', ['Manual feed', 'Auto-feed']]]))
om.append(mod('Laminator', tt=[['Format', ['A4', 'A3', 'A2']], ['Process', ['Hot', 'Cold']]]))
om.append(mod('Binding machine', tt=[['Binding', ['Comb', 'Wire', 'Thermal']]]))
S_OM = shelf('Office machines',
    'Small machines that label, destroy, seal or bind sheets: label makers, shredders, laminators and binding machines; a printer or scanner → Computers & Components.',
    om, 'kinds by what the machine does to the sheet: labels it, destroys it, seals it, binds it')

DEPT6 = {
    'n': 'Calculators & machines', 'mode': 'mixed',
    't': 'Machines and instruments for working out numbers, typing text or handling paper, current and collectable; a computer or printer → Computers & Components.',
    'ax': 'What does the machine work on: numbers, typed text or sheets of paper?',
    'shelves': [S_CA, S_CT, S_TW, S_OM]}

# ---------------------------------------------------------------- assemble
out = copy.deepcopy(d)
out['ax'] = 'What does the object do for writing and paper work: put ink on a page, hold the page, press a seal or stamp, calculate or type, or keep and handle the papers?'
out['key'] = [
    '1. Is it ink, a pen that carries or dips ink for fine writing, or a tool for East Asian brush calligraphy? → Fountain pens, ink & calligraphy',
    '2. Does it make or remove a mark on paper as a ballpoint, gel, felt-tip, marker, pencil or eraser? → Everyday pens & pencils',
    '3. Is it paper made up to write in, plan with, jot on or post? → Notebooks, planners & paper',
    '4. Does it press a name seal, wax seal, embossed seal or ink stamp? → Seals, stamps & sealing wax',
    '5. Does it keep, fasten, cut or measure papers on a desk? → Desk & filing supplies',
    '6. Is it a machine or instrument that calculates, types or processes paper? → Calculators & machines',
    '<i>Precedence: ink and parts for fountain pens stay in step 1 though bought like stationery; a brush pen is step 2 while brush-calligraphy gear is step 1; a pen case is a desk item (step 5); a stamp ink pad belongs with stamps (step 4); a typewriter or slide rule is a machine (step 6) even when collected.</i>']
olddepts = {dp['n']: dp for dp in d['depts']}
new_depts = []
for D in (DEPT1, DEPT2, DEPT3, DEPT4, DEPT5, DEPT6):
    o = copy.deepcopy(olddepts.get(D['n'], {}))
    o['n'] = D['n']; o['mode'] = D['mode']; o['t'] = D['t']; o['ax'] = D['ax']
    o['s'] = D['shelves']
    # keep b / note
    new_depts.append(o)
# note field: Seals dept had none; drop notes that mention shelf structure removed
out['depts'] = new_depts

# ---------------------------------------------------------------- checks
placed = set()
for dp in out['depts']:
    for s in dp['s']:
        for k in s['k']:
            placed.add(k['n'])
            if 't' in k and 'tt' in k: k.pop('t')
            assert 'tt' in k, k['n']
# every old kind accounted for
renames = {'Typewriter': 'Manual typewriter',
           'Clips, pins & fasteners': 'Clips',
           'Planner or notebook cover, refills & inserts': 'Notebook & planner covers, refills & inserts'}
missing = [n for n in old if n not in used]
assert not missing, missing
# lost archetypes check
oldx = {x['n'] for k in old.values() for x in k.get('x', [])}
newx = {x['n'] for dp in out['depts'] for s in dp['s'] for k in s['k'] for x in k.get('x', [])}
newx |= {'Disc-bound notebook'}  # renamed to Atoma disc-bound system
demoted = {'Oblique pen holder', 'Coloured ink stick', 'Waterman ink', 'J. Herbin Encre', 'Herbin brass wax seal', 'J. Herbin sealing wax'}
print('archetypes lost (excluding demoted):', sorted(oldx - newx - demoted))
print('archetypes', len(oldx), '->', len({x['n'] for dp in out['depts'] for s in dp['s'] for k in s['k'] for x in k.get('x', [])}))

json.dump(out, open(R + 'work/STR_C5/C5.new.json', 'w'), ensure_ascii=False, indent=1)
json.dump(renames, open(R + 'work/STR_C5/renames.new.json', 'w'), ensure_ascii=False, indent=1)
print('kinds', len(old), '->', len(placed))
