import json, copy, os, sys
ROOT = '/home/user/Possession-Taxonomy/rebuild/'
old = json.load(open(ROOT + 'work/STR_C8/bak/C8.json'))
OK = {}
for dp in old['depts']:
    for s in dp['s']:
        for k in s['k']:
            OK[k['n']] = k
DEPTS_OLD = {dp['n']: dp for dp in old['depts']}
W = 'https://en.wikipedia.org/wiki/'
renames = {}
used = set()

def base(name, **kw):
    k = copy.deepcopy(OK[name]); used.add(name)
    k.pop('t', None)
    for a, b in kw.items():
        if b is None: k.pop(a, None)
        else: k[a] = b
    return k

def new(n, a, d, s, tt=None, **kw):
    k = {'n': n, 'a': a, 'd': d, 's': s}
    if tt: k['tt'] = tt
    k.update(kw); return k

def split(old_name, n, a, d, tt=None, keep=False, **kw):
    k = copy.deepcopy(OK[old_name]); used.add(old_name); k.pop('t', None)
    for f in ('x', 'm', 'r', 'tg'):
        if not keep: k.pop(f, None)
    k['n'] = n; k['a'] = a; k['d'] = d
    if tt: k['tt'] = tt
    k.update(kw); return k

def drop_x(k, names):
    k['x'] = [x for x in k.get('x', []) if x['n'] not in names]
    if not k['x']: k.pop('x')
    return k

def S(n, t, ax, kinds):
    s = {'n': n, 't': t, 'k': kinds}
    if ax: s['ax'] = ax
    return s

depts = []

# ---------- 1 Timber
sawn = base('Sawn timber', tt=[["Use", ["Carcassing", "Joinery"]], ["Finish", ["Rough sawn", "Planed all round (PAR)"]], ["Treatment", ["Untreated", "Pressure-treated"]], ["Wood", ["Softwood", "Hardwood"]]])
eng = new('Engineered structural timber', 'LVL · glulam · CLT · laminated timber', 'Beams and panels glued up from veneers, strands or boards, such as laminated veneer lumber, glulam and cross-laminated timber.', W + 'Engineered_wood',
          [["Construction", ["Laminated veneer lumber (LVL)", "Glued laminated timber (glulam)", "Cross-laminated timber (CLT)", "I-joist"]]])
ply = base('Plywood', tt=[["Grade", ["Structural", "Marine", "Exterior", "Interior"]], ["Face", ["Birch", "Hardwood-faced", "Softwood"]]])
eb = OK['Engineered board']; used.add('Engineered board')
mdf = split('Engineered board', 'MDF', 'medium-density fibreboard', 'Smooth sheet of fine wood fibre and resin, for shelving, joinery and mouldings; moisture-resistant grades suit kitchens and bathrooms.',
            [["Grade", ["Standard", "Moisture-resistant"]]], s=eb['s'])
chip = new('Chipboard', 'particle board · flooring chipboard', 'Sheet of wood chips bonded with resin, used for flooring, worktop cores and cheap furniture.', eb['s'],
           [["Grade", ["Standard", "Flooring grade", "Moisture-resistant"]]])
osb = new('OSB', 'oriented strand board', 'Structural sheet of layered wood strands bonded with resin, used for sheathing, floors and hoarding.', W + 'Engineered_wood',
          [["Grade", ["OSB/2 (dry)", "OSB/3 (humid)"]]])
hb = new('Hardboard', 'high-density fibreboard · HDF', 'Thin, hard sheet of compressed wood fibre, used for panel backs, drawer bottoms and floor overlays.', W + 'Engineered_wood',
         [["Type", ["Standard", "Tempered"]]])
pb = base('Plasterboard', tt=[["Performance", ["Standard", "Moisture-resistant", "Fire-resistant", "Acoustic", "Insulated"]], ["Edge", ["Tapered", "Square"]]])
cb = new('Cement board', 'tile backer board', 'Fibre-reinforced cement sheet used as a waterproof base for tiles in wet rooms and as cladding.', W + 'Engineered_wood')
ms = base('Metal section', tt=[["Metal", ["Steel", "Aluminium"]], ["Section", ["Bar", "Angle", "Channel", "Box", "Tube"]]])
sk = base('Skirting and architrave', tt=[["Part", ["Skirting", "Architrave"]], ["Profile", ["Torus", "Ogee", "Pencil round", "Chamfered", "Bullnose"]]])
cov = base('Coving')
deck = base('Decking board', tt=[["Material", ["Softwood", "Hardwood", "Composite"]]])
slp = base('Garden sleeper', tt=[["Material", ["Softwood", "Oak", "Reclaimed railway", "Composite"]]])
depts.append({'n': 'Timber & sheet materials', 'old': 'Timber & sheet materials',
  't': 'Wood, wood-based boards and metal lengths sold loose for building and joinery; finished flooring is in Home Fixtures & Features and fence timber is in Fencing & gates.',
  'ax': 'Is it a solid or structural length, a sheet or section, a shaped trim, or timber made for the garden?',
  's': [S('Sawn and structural timber', 'Lengths of timber cut from the log or glued up into beams and panels, for frames, floors and roofs; a board in sheet form goes to Sheet and section materials.',
          'kinds by how the timber is made: sawn from the log, or glued up as engineered section', [sawn, eng]),
        S('Sheet and section materials', 'Flat boards and metal lengths for lining, flooring, shelving and fabrication, such as plywood, MDF, plasterboard and steel angle; a moulded trim goes to Mouldings and trim.',
          'kinds by what the sheet or section is made of: wood veneer, wood fibre or chips, gypsum and cement, metal', [ply, mdf, chip, osb, hb, pb, cb, ms]),
        S('Mouldings & trim', 'Shaped boards that finish the joins of a room, such as skirting, architrave and coving; a plain board goes to Sheet and section materials.',
          'kinds by where the trim sits: base of wall, round an opening, top of wall', [sk, cov]),
        S('Outdoor timber', 'Heavy timber and boards made for the garden, such as decking and sleepers; fence panels and posts go to Fencing & gates.',
          'kinds by what it builds: surfaces to walk on, then edging and steps', [deck, slp])]})

# ---------- 2 Masonry
brick = base('Brick', tt=[["Use", ["Facing", "Engineering", "Common"]], ["Material", ["Clay", "Concrete"]]])
blk = base('Concrete block', tt=[["Density", ["Dense", "Lightweight aerated"]], ["Form", ["Solid", "Hollow"]]])
cem = base('Cement and mortar', tt=[["Product", ["Portland cement", "Ready-mix concrete", "Ready-mix mortar"]], ["Setting", ["Standard", "Rapid-set"]]])
lint = base('Lintel')
rt = base('Roof tile and slate', tt=[["Material", ["Clay", "Concrete", "Natural slate", "Fibre-cement slate"]], ["Profile", ["Plain", "Interlocking", "Ridge and hip"]], ["Condition", ["New", "Handmade", "Reclaimed"]]])
rsh = base('Roof shingle', tt=[["Material", ["Asphalt", "Wood", "Slate", "Fibre cement", "Metal"]]], s=W + 'Roof_shingle') if False else base('Roof shingle', tt=[["Material", ["Asphalt", "Wood", "Slate", "Fibre cement", "Metal"]]])
rsheet = base('Roofing sheet'); rfelt = base('Roofing felt')
rlead = new('Roofing lead and flashing', 'lead flashing · roof flashing · valley lead', 'Sheet metal dressed over roof joints, ridges and chimneys to keep water out.', W + 'Roof_shingle',
            [["Metal", ["Lead", "Copper"]]])
ins1 = split('Insulation', 'Mineral wool insulation', 'glass wool · rock wool · fibreglass insulation · loft roll',
             'Rolls, batts and slabs of glass or rock wool laid in lofts, walls and floors for warmth or sound.',
             [["Fibre", ["Glass wool", "Rock wool"]], ["Form", ["Roll", "Batt", "Slab"]], ["Use", ["Thermal", "Acoustic"]]], keep=False)
ins2 = new('Rigid foam insulation board', 'PIR board · EPS · XPS · foil-faced board', 'Stiff foam board cut to fit between or over studs, rafters and floors.', OK['Insulation']['s'],
           [["Foam", ["PIR", "EPS", "XPS", "Phenolic"]], ["Facing", ["Foil-faced", "Plain"]]])
ins3 = new('Natural fibre insulation', 'sheep wool insulation · wood fibre board', 'Insulation made from plant or animal fibre, sold as rolls, batts or boards.', W + 'Building_insulation_materials',
           [["Fibre", ["Sheep's wool", "Wood fibre", "Hemp", "Cork", "Flax", "Cotton"]]])
ins4 = new('Loose-fill insulation', 'blown insulation · loft fill', 'Granules or flakes poured or blown into lofts and cavities.', W + 'Building_insulation_materials',
           [["Material", ["Cellulose", "Vermiculite", "Perlite"]]])
ins5 = new('Reflective foil insulation', 'radiant barrier · foil insulation', 'Thin foil-faced layers that reflect heat, used under roofs and behind radiators.', W + 'Building_insulation_materials',
           [["Construction", ["Foil-backed bubble", "Multi-layer foil"]]])
dex = base('Draught excluder')
flue = base('Flue pipe and chimney liner', tt=[["Wall", ["Single-wall", "Twin-wall"]], ["Form", ["Flexible liner", "Rigid liner"]]])
depts.append({'n': 'Masonry, roofing & insulation', 'old': 'Masonry, roofing & insulation',
  't': 'Materials for the walls, roof, insulation and flue of a building shell; period lime and reclaimed materials go to Heritage & reclaimed materials.',
  'ax': 'Which part of the shell is it for: the walls, the roof, the insulation layer or the flue?',
  's': [S('Bricks, blocks & cement', 'Wall units and the binder and support that hold them, such as brick, block, cement and lintel; a reclaimed or lime-based version goes to Heritage & reclaimed materials.',
          'kinds from unit to binder to support: brick, block, cement and mortar, lintel', [brick, blk, cem, lint]),
        S('Roofing', 'Coverings that keep rain out of a roof, such as tiles, slates, shingles, sheets, felt and flashing; gutters go to Plumbing, drainage & electrical.',
          'kinds by how the covering is laid: unit by unit, in sheets or rolls, or at the joints', [rt, rsh, rsheet, rfelt, rlead]),
        S('Insulation & draught-proofing', 'Materials that hold heat in or stop air leaks, such as wool rolls, foam board, loose fill and door strips.',
          'kinds by what it is made of: mineral wool, rigid foam, natural fibre, loose fill, reflective foil, then draught strip', [ins1, ins2, ins3, ins4, ins5, dex]),
        S('Flues & chimneys', 'Pipes and liners that carry smoke from a stove or boiler out of the house; a chimney pot is under Reclaimed and salvage.', None, [flue])]})

# ---------- 3 Heritage
lp = base('Lime putty', tt=[["Form", ["Matured putty", "Hydrated powder"]]])
nhl = base('Natural hydraulic lime', tt=[["Strength", ["NHL 2 (feebly hydraulic)", "NHL 3.5 (moderately hydraulic)", "NHL 5 (eminently hydraulic)"]]])
lm = drop_x(base('Lime mortar and render', tt=[["Use", ["Pointing and bedding mortar", "External render", "Plaster coat"]], ["Mix", ["Plain", "Haired"]], ["Finish", ["Floated", "Polished"]]]), {'Haired lime plaster'})
lw = base('Limewash'); cp = base('Clay plaster')
dis = base('Distemper', tt=[["Binder", ["Soft distemper", "Casein", "Oil-bound"]]])
lop = base('Linseed oil paint')
hc = base('Hempcrete', tt=[["Form", ["Prefabricated block", "Cast or sprayed mix"]]])
enc = base('Encaustic tile', tt=[["Colours", ["Two-colour", "Multi-colour (up to six clays)"]], ["Surface", ["Glazed", "Unglazed"]], ["Use", ["Floor", "Wall"]]])
ct = base('Cement tile', tt=[["Origin", ["Catalan mosaico hidráulico", "Italian cementine", "Vietnamese gạch bông"]], ["Pressing", ["Hand-press", "Electric hydraulic press"]]])
zel = base('Zellige', tt=[["Pattern", ["Star pattern", "Rosette", "Sgraffito"]], ["Form", ["Panel", "Loose pieces"]]])
dt = base('Delft tile', tt=[["Colour", ["Blue-and-white"]], ["Age", ["Antique", "Reproduction"]]])
az = base('Azulejo', tt=[["Design", ["Single pattern tile", "Figurative panel", "Façade tile"]], ["Age", ["Antique", "Reproduction"]]])
tal = base('Talavera tile', tt=[["Certification", ["Certified (DO hologram)", "Uncertified majolica"]], ["Colour", ["Blue-and-white", "Polychrome"]]])
izn = new('İznik tile', 'Iznik tile · Ottoman tile', 'Ottoman fritware tile painted under the glaze in blue, turquoise and red, made at İznik and copied widely.', W + 'Tile')
cuer = new('Cuerda seca tile', 'dry cord tile', 'Tile whose glaze colours are kept apart by a greasy line that burns away in firing, found in Persian and Spanish work.', W + 'Tile')
ter = base('Terracotta floor tile', tt=[["Making", ["Handmade", "Machine-pressed"]]])
rb = base('Reclaimed brick', tt=[["Making", ["Handmade", "Machine-made"]], ["Size", ["Imperial", "Metric"]], ["Colour", ["Red", "Blue", "Yellow stock"]]])
rbm = base('Reclaimed oak beam', tt=[["Species", ["Oak", "Chestnut", "Heart pine", "Baltic pine"]], ["Form", ["Beam", "Barn wood boards", "Reclaimed timber boards"]]])
drop_x(rbm, {'Heart pine', 'Barn wood'})
rf = base('Reclaimed flooring', tt=[["Species", ["Oak", "Pine", "Baltic pine"]], ["Layout", ["Floorboard", "Parquet block", "Chevron"]]])
cpot = base('Chimney pot', tt=[["Top", ["Cannon head", "Roll top", "Beehive", "Crown", "Bishop"]], ["Surface", ["Glazed", "Unglazed"]]])
asv = base('Architectural salvage', tt=[["Part of the building", ["Fireplace surround", "Fire grate", "Period door", "Cast-iron railings", "Cast-iron column", "Corbel", "Garden urn", "Church fittings", "Sanitaryware"]]])
depts.append({'n': 'Heritage & reclaimed materials', 'old': 'Heritage & reclaimed materials',
  't': 'Traditional finishes, period tiles and salvaged building parts that owners of old houses seek out; the modern equivalent sits in its working department, such as Paint & decorating.',
  'ax': 'Is it a traditional lime, earth or paint finish, a tile in a regional tradition, or a salvaged building part?',
  's': [S('Lime & traditional finishes', 'Binders, plasters and paints used on old walls, such as lime putty, limewash, clay plaster and distemper; modern emulsion goes to Paint & decorating.',
          'kinds from binder to coat: lime binders, lime coats, then other traditional paints and walling', [lp, nhl, lm, lw, cp, dis, lop, hc]),
        S('Heritage tiles', 'Tiles from a named regional tradition, such as encaustic, azulejo, zellige and Delft; plain modern wall and floor tiles go to Tiles, wallpaper and plaster.',
          'kinds by tradition of origin: Britain, the Netherlands, Iberia, North Africa and the Islamic world, Mexico, then terracotta floor tiles', [enc, dt, az, ct, zel, cuer, izn, tal, ter]),
        S('Reclaimed & salvage', 'Second-hand building parts taken from old buildings, such as bricks, beams, floors, chimney pots and architectural fittings; new equivalents go to Masonry, roofing & insulation or Timber & sheet materials.',
          'kinds by the building part salvaged: walling, timber, floor, chimney, ornament', [rb, rbm, rf, cpot, asv])]})

# ---------- 4 Aggregates
ag = base('Aggregate', tt=[["Product", ["Building sand", "Sharp sand", "Ballast", "MOT Type 1 sub-base", "Pea shingle"]]])
mac = base('Macadam'); wm = base('Weed membrane')
gg = drop_x(base('Garden gravel', tt=[["Stone", ["Limestone", "Granite", "Flint", "Basalt", "White spar"]], ["Shape", ["Pea gravel", "Rounded river gravel", "Angular chippings"]], ["Colour", ["Golden", "Black", "Panda (black and icy blue)", "Dark grey"]], ["Pack", ["Standard bag", "Bulk bag"]]]), {'Pea gravel', 'Golden gravel'})
slc = drop_x(base('Slate chippings', tt=[["Colour", ["Plum", "Blue", "Green"]], ["Size", ["20 mm", "40 mm"]], ["Origin", ["Welsh", "Imported"]]]), {'Welsh slate chippings'})
dp_ = drop_x(base('Decorative pebbles', tt=[["Size", ["Pebbles", "Cobbles"]], ["Colour", ["Mixed colours", "White"]], ["Origin", ["Scottish", "Beach"]]]), {'Scottish pebbles and cobbles'})
rock = base('Rockery stone and boulders', tt=[["Stone", ["Natural granite", "Limestone", "Artificial stone"]]])
stp = base('Stepping stone')
pslab = base('Paving slab', tt=[["Material", ["Concrete", "Porcelain"]], ["Finish", ["Riven", "Smooth", "Textured"]]])
nsp = drop_x(base('Natural stone paving', tt=[["Stone", ["Indian sandstone", "Granite", "Limestone", "Slate"]], ["Finish", ["Riven", "Sawn", "Honed"]], ["Condition", ["New", "Reclaimed"]]]), {'Indian sandstone colourways'})
bp = base('Block paving', tt=[["Material", ["Concrete", "Clay"]], ["Drainage", ["Standard", "Permeable"]], ["Laying pattern", ["Herringbone", "Stretcher bond", "Basketweave"]], ["Finish", ["Tumbled"]]])
sett = drop_x(base('Sett and cobble', tt=[["Form", ["Sett (rectangular)", "Cobble (rounded)"]], ["Material", ["Granite", "Concrete"]], ["Finish", ["Tumbled"]]]), {'Sett', 'Cobblestone'})
edg = base('Lawn edging', tt=[["Material", ["Metal", "Plastic", "Timber log roll", "Stone", "Concrete kerb"]]])
depts.append({'n': 'Aggregates, paving & landscaping stone', 'old': 'Aggregates, paving & landscaping stone',
  't': 'Loose and cut stone, sand and gravel for ground works and gardens; reclaimed paving belongs here only when sold as a paving stone, and garden structures go to Fencing & gates.',
  'ax': 'Is it laid beneath the surface, scattered on it as decoration, or laid as the walking surface?',
  's': [S('Aggregates & sub-base', 'Sand, gravel and bound stone laid beneath or between other materials, such as ballast, sub-base and macadam.', None, [ag, mac, wm]),
        S('Decorative stone & gravel', 'Loose stone scattered on beds and paths for looks, such as chippings, pebbles, rockery stone and stepping stones; building aggregate goes to Aggregates and sub-base.',
          'kinds by size of stone: gravel and chippings, pebbles and cobbles, boulders, single stepping stones', [gg, slc, dp_, rock, stp]),
        S('Paving & edging', 'Slabs, blocks and kerbs laid as a hard surface or border, such as paving slabs, block paving, setts and lawn edging.',
          'kinds by unit: large slab, natural stone flag, small block, sett, then edging', [pslab, nsp, bp, sett, edg])]})

# ---------- 5 Fencing
fpost = base('Fence post', tt=[["Material", ["Timber", "Concrete slotted", "Steel"]]])
frail = new('Fence rail', 'post-and-rail · arris rail · split rail', 'Horizontal length fixed between posts to carry boards or form an open post-and-rail fence.', W + 'Fence',
            [["Fence style", ["Post and rail", "Split rail"]]])
fpan = base('Fence panel', tt=[["Style", ["Featheredge", "Closeboard", "Lap", "Slatted", "Picket"]], ["Material", ["Timber", "Composite", "Metal"]]])
trel = new('Trellis', 'trellis panel · expanding trellis', 'Lattice panel for climbing plants or screening, fixed to a wall or fence, or sold as an expanding fence.', W + 'Fence',
           [["Form", ["Fixed panel", "Expanding"]]])
gb = base('Gravel board'); gate = base('Gate')
scr = new('Screening roll and hurdle', 'reed screening · willow hurdle · bamboo screening', 'Reed, bamboo or willow screening sold by the roll, and woven hurdle panels for garden privacy.', W + 'Fence',
          [["Material", ["Reed", "Willow", "Brushwood"]], ["Form", ["Roll", "Hurdle panel"]]])
wf = base('Wire fencing', tt=[["Wire", ["Plain", "Barbed", "High-tensile"]], ["Form", ["Stock netting", "Welded mesh", "Woven wire"]]])
cl = new('Chain-link fencing', 'chain link fence · diamond mesh', 'Diamond mesh of woven wire stretched between posts to enclose a boundary cheaply.', W + 'Fence')
ee = base('Electric fence energiser')
ew = base('Electric fence wire and insulators', tt=[["Conductor", ["Polytape", "Polywire", "Rope"]], ["Insulator", ["Ring", "Corner", "Strain"]]])
depts.append({'n': 'Fencing & gates', 'old': 'Fencing & gates',
  't': 'Posts, panels, wire and gates that mark and secure a boundary; ironmongery for the gate itself goes to Ironmongery and ground stone to Aggregates, paving & landscaping stone.',
  'ax': 'What forms the barrier: posts with panels or boards, stretched wire or mesh, or a pulsed charge?',
  's': [S('Panels, posts & gates', 'Upright, rail and infill parts of a timber or composite fence, with its gates and screening.',
          'kinds from structure to infill: post, rail, panel, trellis, base board, gate, screening', [fpost, frail, fpan, trel, gb, gate, scr]),
        S('Wire & mesh fencing', 'Fencing made of stretched wire or mesh, for stock, pets and boundaries; electrified wire goes to Electric fencing.', None, [wf, cl]),
        S('Electric fencing', 'Energisers, wire and insulators that give stock a short shock to keep them in.', None, [ee, ew])]})

# ---------- 6 Paint
wcp = base('Wall and ceiling paint', tt=[["Sheen", ["Dead flat", "Matt", "Soft sheen", "Silk", "Eggshell"]], ["Durability", ["Standard", "Washable or scrubbable", "Contract or trade"]]])
wmp = base('Woodwork and metal paint', tt=[["Sheen", ["Gloss", "Satinwood", "Eggshell"]], ["Carrier", ["Water-based", "Solvent-based"]], ["Surface", ["Wood", "Direct-to-metal"]]])
mas = base('Masonry paint', tt=[["Texture", ["Smooth", "Textured"]], ["Carrier", ["Water-based", "Solvent-based"]]])
fp = base('Furniture paint', tt=[["Paint type", ["Chalk-style", "Mineral", "Milk paint", "Cabinet enamel", "Eggshell"]]])
sp = base('Spray paint', tt=[["Use", ["General-purpose", "Graffiti and artist", "Primer", "Automotive"]], ["Effect", ["Metallic and chrome", "Textured and stone"]], ["Carrier", ["Solvent-based", "Water-based"]], ["Pressure", ["High pressure", "Low pressure"]]])
sp.pop('x'); sp['r'] = [['Montana GOLD', 'Montana Cans'], ['Montana BLACK', 'Montana Cans']]
spec = base('Specialist paint', tt=[["Surface", ["Floor and garage floor", "Radiator (heat-resistant)", "Tile", "Kitchen and bathroom"]], ["Property", ["Anti-mould"]]])
prim = base('Primer and undercoat', tt=[["Coat", ["Primer", "Undercoat", "Primer-undercoat"]], ["Job", ["Stain-blocking sealer", "Bonding primer", "Metal primer"]]])
wst = base('Wood stain', tt=[["Colourant", ["Pigmented", "Dye"]]])
woil = base('Wood oil', tt=[["Oil", ["Danish oil", "Linseed oil", "Teak oil", "Tung oil", "Hardwax oil"]]])
wwax = base('Wood wax', tt=[["Wax", ["Beeswax", "Carnauba"]]])
varn = base('Varnish', tt=[["Resin", ["Alkyd", "Polyurethane (oil-based)", "Polyurethane (water-based)", "Acrylic"]], ["Use", ["Interior", "Spar (yacht)"]]])
shel = new('Shellac', 'French polish · button polish', 'Resin dissolved in alcohol and brushed or rubbed on as a traditional glossy wood finish.', W + 'Wood_finishing')
ext = base('Exterior wood treatment', tt=[["Product", ["Fence and shed paint", "Preservative"]]])
sand = base('Sandpaper', see=[["C1", "Sanding sheet or disc", "cut to fit one power sander"]])
plas = base('Plaster', tt=[["Coat", ["Finish (skim)", "Bonding undercoat", "One-coat"]]], see=[["H2", "Plaster", "a different object: the sticking dressing for a cut"]])
wp = base('Wallpaper', tt=[["Material", ["Paper", "Vinyl", "Non-woven", "Flock", "Grasscloth", "Hand-painted silk"]], ["Hanging", ["Paste the paper", "Paste the wall"]], ["Surface", ["Smooth", "Embossed relief"]]])
lin = new('Lining paper', 'wall lining paper · cross-lining paper', 'Plain paper hung under paint or wallpaper to even out a wall.', W + 'Wallpaper')
bord = new('Wallpaper border', 'border paper', 'Narrow printed strip hung along a wall at dado, picture-rail or ceiling height.', W + 'Wallpaper')
mur = new('Wall mural', 'photo mural · panoramic mural · scenic wallpaper', 'Large printed scene made in panels to cover a whole wall.', W + 'Wallpaper')
wt = base('Wall tile', tt=[["Material", ["Ceramic", "Porcelain", "Glass"]], ["Format", ["Metro", "Mosaic"]]])
ft = base('Floor tile', tt=[["Material", ["Porcelain", "Ceramic", "Natural stone"]], ["Look", ["Wood-effect"]]])
ul = base('Flooring underlay', tt=[["Material", ["Polyethylene foam", "Fibreboard", "Cork", "Rubber"]], ["Damp protection", ["Plain", "With damp-proof membrane"]]])
depts.append({'n': 'Paint & decorating', 'old': 'Paint & decorating',
  't': 'Coats and coverings put on a wall, floor or piece of wood to finish it, from emulsion and varnish to wallpaper, tiles and plaster; period lime paints go to Heritage & reclaimed materials.',
  'ax': 'Is it a paint to brush or spray on, a finish for bare wood, or a covering, tile or plaster for a wall or floor?',
  's': [S('Paint', 'Coloured coatings for walls, trim, masonry and furniture, such as emulsion, gloss, masonry paint and spray paint; a wood oil or varnish goes to Wood finishes and sanding.',
          'kinds by surface painted: walls and ceilings, wood and metal trim, outside masonry, furniture, special surfaces, spray cans, then the base coat under any of them',
          [wcp, wmp, mas, fp, spec, sp, prim]),
        S('Wood finishes & sanding', 'Products that colour, seal or smooth bare wood, such as oil, wax, varnish, stain and sandpaper; an opaque coat goes to Paint.',
          'kinds from soaking-in to film-forming finish: stain, oil, wax, varnish, shellac, outdoor treatment, then sandpaper to prepare', [wst, woil, wwax, varn, shel, ext, sand]),
        S('Tiles, wallpaper & plaster', 'Sheets, tiles and wet coats that finish a wall or floor, such as wallpaper, wall tiles, floor tiles and skim plaster; period tiles go to Heritage tiles.',
          'kinds by surface covered: wet coat on a wall, paper on a wall, tile on a wall, tile on a floor, underlay beneath a floor', [plas, lin, wp, bord, mur, wt, ft, ul])]})

# ---------- 7 Plumbing/electrical
pp = base('Plumbing pipe', tt=[["Material", ["Copper", "PEX", "Polybutylene", "MDPE", "Steel"]]])
pf = base('Pipe fitting', tt=[["Shape", ["Elbow", "Tee", "Coupling", "Reducer", "Union", "Cap", "Plug", "Adaptor"]], ["Joint", ["Push-fit", "Compression", "Solder-ring", "End-feed", "Press-fit"]]])
val = base('Valve', tt=[["Valve type", ["Stopcock", "Isolating", "Ball", "Gate", "Check", "Pressure-reducing", "Thermostatic mixing", "Water hammer arrester"]]])
fh = base('Flexible hose'); pc = base('Pipe clip')
wt_ = base('Waste and trap'); sdp = base('Soil and drain pipe'); dc = base('Drainage channel')
gut = base('Guttering', tt=[["Profile", ["Half round", "Square line", "Ogee", "Deep flow"]], ["Material", ["PVCu", "Cast iron", "Aluminium", "Galvanised steel"]]])
dpipe = new('Downpipe and rainwater fitting', 'downpipe · hopper head · rainwater pipe', 'Vertical pipe, hopper heads, bends and shoes that carry roof water from gutter to drain.', W + 'Rain_gutter',
            [["Fitting", ["Downpipe", "Hopper head", "Bend", "Shoe"]]])
cab = base('Cable', tt=[["Cable", ["Twin and earth (6242Y)", "Three-core and earth", "Armoured (SWA)", "Coaxial", "Flex"]], ["Protection", ["Rigid conduit", "Flexible conduit", "Trunking"]]])
acc = base('Electrical accessory', tt=[["Item", ["Cable clip", "Cable tie", "Mains plug", "Fuse", "Junction box"]]])
ext_ = base('Extension lead and adaptor', tt=[["Feature", ["Surge-protected", "USB", "Smart"]], ["Form", ["Reel", "Trailing socket", "Plug adaptor"]]])
depts.append({'n': 'Plumbing, drainage & electrical', 'old': 'Plumbing & drainage',
  't': 'Pipes, cable and their fittings that carry water, waste or electricity through a house; taps, baths, switches and sockets are in Home Fixtures & Features.',
  'ax': 'What does it carry: clean water, waste and rain water, or electricity?',
  's': [S('Pipe & fittings', 'Supply pipe and the fittings, valves and clips that join and control clean water, such as copper pipe, push-fit joints and stopcocks.',
          'kinds from pipe to joint to control: pipe, fitting, valve, hose, clip', [pp, pf, val, fh, pc]),
        S('Waste & drainage', 'Pipes, gutters and channels that take away used and rain water, such as waste traps, soil pipe, guttering and downpipes.',
          'kinds from the appliance to the drain: waste trap, soil pipe, channel, then roof water: gutter and downpipe', [wt_, sdp, dc, gut, dpipe]),
        S('Cable, plugs & leads', 'Loose wiring and plug-in supplies, such as twin and earth cable, clips, fuses and extension leads; switches, sockets and consumer units go to Home Fixtures & Features.',
          'kinds from fixed wiring to plug-in leads: cable, accessory, extension lead', [cab, acc, ext_])]})

# ---------- 8 Ironmongery
hand = base('Door handle', tt=[["Style", ["Lever on rose", "Lever on backplate", "Knob", "Pull handle"]]])
hing = base('Door hinge', tt=[["Pattern", ["Butt", "H", "HL", "Parliament", "Piano (continuous)", "Tee", "Flush", "Pivot"]], ["Action", ["Plain", "Spring-closing", "Rising butt"]], ["Cranking", ["Straight", "Single cranked", "Double cranked"]]], x=None)
chin = new('Cabinet hinge', 'concealed hinge · cup hinge · Euro hinge', 'Hinge hidden behind a cupboard door, fitted into a drilled hole and adjustable after hanging.', W + 'Hinge',
           [["Closing", ["Standard", "Soft-close"]]])
knob = base('Cabinet knob', tt=[["Form", ["Knob", "Pull handle", "Cup handle"]]])
knock = drop_x(base('Door knocker', tt=[["Style", ["Ring", "Hammer", "Lion-head", "Hamsa hand"]]]), {'Lion-head knocker', 'Hamsa knocker'})
lp_ = base('Letter plate', tt=[["Mounting", ["Horizontal", "Vertical"]], ["Flap", ["Gravity", "Sprung", "Inner flap"]], ["Accessory", ["Letter cage"]]])
lat = drop_x(base('Latch', tt=[["Style", ["Ring", "Thumb", "Gate", "Cottage", "Auto-locking"]]]), {'Cottage latch'})
bolt = base('Door bolt', tt=[["Style", ["Tower", "Surface", "Brenton"]]], see=[["B8", "Door bolt", "the same fitting seen as a security lock"]])
hasp = base('Hasp')
cabin = new('Cabin hook', 'hook and eye · cabin hook and eye', 'Small hook that drops into an eye to hold a door, hatch or gate shut or open.', W + 'Latch')
togg = new('Toggle catch', 'toggle latch · draw catch · over-centre latch', 'Lever catch that pulls two parts together and locks over centre, used on boxes, doors and cases.', W + 'Latch')
brk = base('Bracket')
depts.append({'n': 'Ironmongery', 'old': 'Ironmongery',
  't': 'Loose hardware that hangs, opens, announces or holds shut a door, gate or cabinet; the lock itself goes to Locks & door security and fasteners to Screws, nails & fixings.',
  'ax': 'What does the fitting do: carry and open the door, serve callers and post, or hold something shut or up?',
  's': [S('Hinges & handles', 'Fittings that carry a door on its frame and let a hand open it, such as door hinges, door handles and cabinet knobs.',
          'kinds by part of the door worked: hinge, door handle, cabinet hinge, cabinet knob', [hing, hand, chin, knob]),
        S('Knockers & letter plates', 'Door furniture for callers and post, such as door knockers and letter plates.', None, [knock, lp_]),
        S('Latches, bolts & brackets', 'Fittings that hold a door, gate or shelf shut or up, such as latches, bolts, hasps, hooks and brackets.',
          'kinds by how it holds: swinging latch, sliding bolt, hasp, hook, lever catch, support bracket', [lat, bolt, hasp, cabin, togg, brk])]})

# ---------- 9 Fixings
nsb = OK['Screw']
ws = split('Screw', 'Wood screw', 'fixing screw · timber screw · chipboard screw · decking screw',
           'Screw with a sharp point and coarse thread for fixing into timber and boards.',
           [["Use", ["General wood", "Timber decking", "Composite decking"]], ["Head", ["Countersunk", "Pan", "Round", "Bugle", "Flanged"]], ["Drive", ["Pozidriv", "Phillips", "Torx", "Slotted"]]], keep=True)
ws.pop('t', None)
dws = new('Drywall screw', 'plasterboard screw', 'Bugle-headed screw that fixes plasterboard to timber or metal studs.', nsb['s'], [["Thread", ["Coarse (timber studs)", "Fine (metal studs)"]]])
sts = new('Self-tapping screw', 'self-drilling screw · sheet-metal screw', 'Screw that cuts its own thread in sheet metal or plastic, with or without a drill point.', W + 'Screw',
          [["Point", ["Self-tapping", "Self-drilling"]]])
mcs = new('Machine screw', 'machine screw · bolt screw', 'Parallel-threaded screw that fastens into a nut or tapped hole in metal.', W + 'Screw',
          [["Head", ["Pan", "Countersunk", "Cheese", "Hex socket"]]])
cos = new('Coach screw', 'lag screw · lag bolt', 'Heavy hexagon-headed screw driven by spanner into timber for frames and fences.', W + 'Screw')
wn = split('Nail', 'Wire nail', 'common nail · round wire nail · oval nail · lost-head nail', 'Plain steel nail for general carpentry, in round, oval and lost-head forms.',
           [["Head", ["Round", "Oval", "Lost head"]], ["Length", ["Short", "Medium", "Long"]]], keep=True)
fpn = new('Finishing pin', 'panel pin · veneer pin · brad', 'Slim headless-looking nail for fixing trim, panels and veneer where the head should barely show.', W + 'Nail_(fastener)', [["Pin", ["Panel pin", "Veneer pin", "Brad"]]])
cln = new('Clout nail', 'felt nail · roofing nail', 'Short nail with a wide flat head for roofing felt, shingles and plasterboard.', W + 'Nail_(fastener)')
mn = new('Masonry nail', 'concrete nail', 'Hardened steel nail driven into brick, block or concrete.', W + 'Nail_(fastener)')
rsn = new('Ring-shank nail', 'annular nail · jagged nail · ring nail', 'Nail with ridges along the shank that grip, used for decking, cladding and pallets.', W + 'Nail_(fastener)')
tck = new('Tack', 'carpet tack · upholstery tack', 'Short sharp-pointed nail with a broad head for fixing carpet and upholstery.', W + 'Nail_(fastener)')
stp_ = base('Staple')
bn = split('Bolt, nut, washer and rivet', 'Bolt and nut', 'hex bolt · coach bolt · hexagon nut', 'Threaded bolt and the nut that tightens it, for joining timber and metal.',
           [["Bolt", ["Coach bolt", "Roof bolt", "Hexagon bolt"]], ["Nut", ["Hexagon nut", "Nylon lock nut", "Connector nut"]]], keep=True)
wash = new('Washer', 'penny washer · spring washer', 'Flat or sprung ring that spreads the load under a bolt, nut or screw head.', OK['Bolt, nut, washer and rivet']['s'],
           [["Shape", ["Flat", "Penny", "Repair", "Spring"]]])
riv = new('Rivet', 'pop rivet · blind rivet', 'Metal pin set with a rivet tool to join sheet metal and plastic permanently.', OK['Bolt, nut, washer and rivet']['s'])
wfx = base('Wall fixing', tt=[["Fixing", ["Plastic plug", "Frame fixing", "Spring toggle", "Self-drill plasterboard fixing", "Metal cavity anchor", "Shield anchor", "Through-bolt", "Masonry screw", "Chemical anchor"]]])
tcn = base('Timber connector', tt=[["Connector", ["Joist hanger", "Truss clip", "Nail plate"]]])
psup = base('Post support', tt=[["Fixing", ["Drive-in spike", "Bolt-down base", "Concrete-in shoe"]]])
dow = base('Dowel', tt=[["Dowel", ["Fluted pin", "Spiral pin", "Rod"]]])
bis = base('Jointing biscuit')
pack = base('Packer', tt=[["Shim", ["Glazing shim", "Levelling shim", "U shim", "Kitchen unit space plug"]]])
depts.append({'n': 'Screws, nails & fixings', 'old': 'Screws, nails & fixings',
  't': 'Small parts that hold materials together, from screws and nails to wall plugs and joist hangers; door and cabinet hardware goes to Ironmongery and glues to Adhesives, sealants & packing.',
  'ax': 'How does it hold: driven into the material, clamped through it, anchored in a wall, or joining one member to another?',
  's': [S('Screws', 'Threaded fasteners driven into a material, such as wood, drywall, self-tapping, machine and coach screws.',
          'kinds by what the screw bites into: wood, plasterboard, sheet metal, a nut or tapped hole, then heavy timber', [ws, dws, sts, mcs, cos]),
        S('Nails & staples', 'Driven fasteners hammered or shot in, such as wire nails, pins, clouts, masonry nails and staples.',
          'kinds by job: general carpentry, finishing, roofing, masonry, extra grip, upholstery, then staples', [wn, fpn, cln, mn, rsn, tck, stp_]),
        S('Bolts, nuts & rivets', 'Fasteners that clamp parts through a hole, such as bolts, nuts, washers and rivets.', None, [bn, wash, riv]),
        S('Wall plugs & anchors', 'Fixings that grip inside masonry, plasterboard or a cavity so a screw can hold a load.', None, [wfx]),
        S('Connectors & joints', 'Parts that join or space timber and posts, such as joist hangers, post supports, dowels, biscuits and shims.',
          'kinds by what they join: member to member, post to ground, piece to piece in joinery, then gap spacers', [tcn, psup, dow, bis, pack])]})

# ---------- 10 Adhesives
grab = base('Grab adhesive')
wg = base('Wood glue', tt=[["Resistance", ["Interior", "Weatherproof"]], ["Chemistry", ["PVA", "Resin"]]])
apg = base('All-purpose glue', tt=[["Chemistry", ["PVA", "Polyurethane"]]])
sup = new('Superglue', 'cyanoacrylate adhesive · instant glue', 'Thin fast-setting glue for small repairs on plastic, metal, ceramic and skin-safe gels.', W + 'Adhesive')
epx = new('Epoxy adhesive', 'two-part epoxy · epoxy resin glue', 'Two-part glue that cures hard and fills gaps, for metal, stone, ceramic and wood.', W + 'Adhesive', [["Setting", ["Rapid", "Standard"]]])
hmg = new('Hot-melt glue stick', 'glue gun sticks · hot glue', 'Thermoplastic stick melted in a glue gun to bond craft and light repair work.', W + 'Adhesive')
con = base('Contact and spray adhesive', tt=[["Form", ["Tin or tube", "Aerosol spray"]]])
fl = base('Flooring adhesive', tt=[["Floor", ["Vinyl", "Wood"]]])
wpa = base('Wallpaper adhesive', tt=[["Form", ["Powder paste", "Ready-mixed paste"]]])
seal = base('Sealant', tt=[["Chemistry", ["Silicone", "Polyurethane", "Hybrid", "Acrylic (decorators' caulk)"]], ["Use", ["Sanitary", "Frame"]]])
tad = base('Tile adhesive', tt=[["Form", ["Ready-mixed", "Powder"]]])
tg = base('Tile grout')
ef = base('Expanding foam', tt=[["Application", ["Hand-held can", "Gun-grade"]]])
pbx = base('Packing box', tt=[["Wall", ["Single wall", "Double wall"]], ["Form", ["Wardrobe box"]]])
pt = base('Parcel tape', tt=[["Film", ["Polypropylene", "Vinyl", "Paper"]]])
td = base('Tape dispenser'); dtp = base('Duct tape'); bw = base('Bubble wrap')
pfl = base('Packing fill', tt=[["Material", ["Loose fill", "Paper", "Air pillows", "Foam sheet and corners"]]])
depts.append({'n': 'Adhesives, sealants & packing', 'old': 'Adhesives, sealants & packing',
  't': 'Glues, sealants and packing supplies that bond, seal or protect; mechanical fixings go to Screws, nails & fixings.',
  'ax': 'Does it stick things together, seal a joint or gap, or protect and move goods?',
  's': [S('Adhesives & glue', 'Glues that bond two surfaces, such as wood glue, superglue, epoxy, contact adhesive and grab adhesive; tile adhesive goes to Tiling and sealing.',
          'kinds by what is bonded: wood, general household, small hard parts, hard materials, craft, large sheets, building boards, floors, wallpaper',
          [wg, apg, sup, epx, hmg, con, grab, fl, wpa]),
        S('Tiling & sealing', 'Products that bed tiles and close joints and gaps, such as tile adhesive, grout, sealant and expanding foam.',
          'kinds from setting tiles to finishing their joints, then sealing other gaps', [tad, tg, seal, ef]),
        S('Packing & moving', 'Boxes, tape and padding for storing and shifting goods.',
          'kinds by step in a move: box, close, dispense, reinforce, cushion, fill', [pbx, pt, td, dtp, bw, pfl])]})

# ---------- 11 Energy
hb_ = base('Household battery', tt=[["Size", ["AA (R6/LR6)", "AAA (R03/LR03)", "C (R14/LR14)", "D (R20/LR20)", "9 V (PP3, 6LR61/6F22)"]], ["Chemistry", ["Alkaline", "Lithium (FR6/FR03)", "NiMH rechargeable (HR6/HR03)", "Zinc–carbon"]]])
cc = base('Coin cell', tt=[["Size", ["CR2032", "CR2025", "CR2016", "CR2450", "LR44 / AG13 / A76 / 357", "377"]], ["Chemistry", ["Lithium", "Alkaline", "Silver oxide", "Zinc–air (hearing aid)"]]])
sb = base('Specialty battery', tt=[["Format", ["CR123A (3 V lithium)", "CR2 (3 V lithium)", "A23 (12 V alkaline)", "4LR44 (6 V)", "6 V lantern (4R25)", "4.5 V flat pack (3R12)"]]])
sla = base('Sealed lead-acid battery', tt=[["Voltage", ["6 V", "12 V"]], ["Electrolyte", ["AGM", "Gel"]]])
li = base('Lithium-ion cell', tt=[["Format", ["18650", "21700", "14500", "26650"]]])
bch = base('Battery charger', tt=[["Charging", ["Basic overnight", "Fast", "Smart charger-analyser"]], ["Power", ["Mains", "USB"]]], see=[["C1", "Battery charger", "this one charges loose cells; that one charges a tool battery pack"]])
lpg = base('LPG cylinder', tt=[["Gas", ["Propane", "Butane", "Patio gas"]]])
gc = base('Gas canister', tt=[["Valve", ["Pierceable", "Screw-thread", "Click-on"]]])
reg = base('LPG regulator', tt=[["Gas", ["Propane", "Butane"]]])
fc = base('Fuel can', tt=[["Material", ["Metal jerry can", "Plastic fuel can"]]])
lub = base('Lubricant', tt=[["Product", ["Multi-use oil", "Penetrating oil", "Silicone lubricant", "Grease"]]])
log = base('Firewood logs', tt=[["Dryness", ["Seasoned (air-dried)", "Kiln-dried"]], ["Wood", ["Hardwood", "Softwood"]], ["Pack", ["Net bag", "Bulk bag", "Cord or face cord"]]])
kin = base('Kindling')
lump = drop_x(base('Lump charcoal', tt=[["Wood", ["Mixed hardwood", "Single species", "Marabú", "Quebracho", "Oak and hickory"]], ["Grade", ["Standard", "Restaurant grade (large lumps)"]], ["Certification", ["FSC certified"]]],
              see=[["C2", "Barbecue fuel", "the same lump charcoal as sold for barbecues"]]), {'Marabú charcoal', 'Quebracho lump', 'Oak and hickory lump'})
bri = drop_x(base('Charcoal briquettes', tt=[["Form", ["Pillow", "Sawdust", "Extruded"]], ["Burn", ["Standard", "Instant-light", "Long-burning", "Binder-free", "Coconut shell"]]],
              see=[["C2", "Barbecue fuel", "the same briquettes as sold for barbecues"]]), {'Pillow briquette', 'Sawdust briquette', 'Extruded charcoal'})
bri.setdefault('x', []).append({'n': 'Ogatan', 'a': '', 'd': 'Japanese sawdust charcoal pressed into hollow hexagonal sticks, burning long and clean.', 'mk': '', 'y': '', 's': W + 'Charcoal', 'v': []})
pel = base('Wood pellets', tt=[["Use", ["Heating (DINplus / PFI)", "Cooking"]], ["Wood", ["Single-species", "Blend"]], ["Diameter", ["6 mm", "8 mm"]]])
smk = base('Smoking wood', tt=[["Wood", ["Hickory", "Mesquite", "Oak", "Pecan", "Alder", "Maple", "Beech", "Apple", "Cherry", "Plum", "Mānuka"]], ["Cut", ["Chips", "Chunks"]]])
coal = base('Coal and smokeless fuel', tt=[["Fuel", ["House coal", "Anthracite", "Coke", "Manufactured smokeless briquettes"]]])
fl_ = base('Firelighter', tt=[["Base", ["Paraffin cube", "Odourless", "Natural wood wool"]]])
mat = base('Match', tt=[["Striking", ["Safety match", "Strike-anywhere match"]], ["Length", ["Standard", "Long fireplace match"]]])
ul_ = base('Utility lighter', tt=[["Fuel", ["Butane", "Rechargeable arc"]], ["Reach", ["Long nozzle", "Candle lighter"]]])
lf = base('Lighter fluid', tt=[["Fluid", ["Butane refill", "Naphtha lighter fluid", "Barbecue lighter fluid"]]])
depts.append({'n': 'Batteries, fuel & firelighting', 'old': 'Fuel & firelighting',
  't': 'Cells, chargers and the fuels and flames that supply power and heat for the house and garden; the appliances that burn or use them go to their own categories.',
  'ax': 'What does it store or start: electric charge, gas or liquid fuel, solid fuel, or a flame?',
  's': [S('Batteries & chargers', 'Cells and the chargers for them, from AA batteries to loose lithium-ion cells; a power-tool battery pack goes to the tool categories.',
          'kinds from everyday cells to special formats: household, coin, specialty, lead-acid, loose lithium-ion, then chargers', [hb_, cc, sb, sla, li, bch]),
        S('Gas, liquid fuel & lubricants', 'Bottled gas, fuel carriers and oils bought for heaters, stoves, engines and moving parts.',
          'kinds by form: bottled gas, gas canister, regulator, fuel can, lubricant', [lpg, gc, reg, fc, lub]),
        S('Solid fuel', 'Wood, charcoal, pellets and coal burned for heat, cooking or smoking; barbecue sets and stoves go to their own categories.',
          'kinds by what it is made from: split wood, charcoal, compressed wood, smoking wood, coal', [log, kin, lump, bri, pel, smk, coal]),
        S('Firelighters, matches & lighters', 'Ways to start a flame, such as firelighters, matches, utility lighters and lighter fluid.',
          'kinds from lighting material to the flame source to its fuel', [fl_, mat, ul_, lf])]})

# ---------- assemble
out = copy.deepcopy(old)
out['lead'] = ('Raw building supplies, hardware and household consumables a person buys loose, organised by the part of a build, repair or household job they serve '
               '(timber, walls and roofs, period materials, ground stone, boundaries, decorating, pipes and wiring, ironmongery, fixings, adhesives, batteries and fuel); '
               'built-in fittings live in Home Fixtures & Features.')
out['ax'] = 'Which part of a build, repair or household job is the supply for: structure, shell, period character, ground, boundary, surface finish, services, hardware, fixing, bonding or energy?'
out['key'] = [
 '1. Is it a battery, charger, bottled gas, fuel, firelighter, match or lighter? → Batteries, fuel & firelighting',
 '2. Is it a hinge, handle, latch, door or gate bolt, knocker, letter plate or bracket? → Ironmongery',
 '3. Is it a screw, nail, nut, rivet, wall plug or connector that fixes one thing to another? → Screws, nails & fixings',
 '4. Is it a glue, sealant, tile adhesive, grout, tape or packing material? → Adhesives, sealants & packing',
 '5. Is it a pipe, valve, drain, gutter, cable, plug or lead? → Plumbing, drainage & electrical',
 '6. Is it paint, a wood finish, wallpaper, plaster, a wall or floor tile or underlay? → Paint & decorating',
 '7. Is it a fence post, panel, gate, wire or electric fence part? → Fencing & gates',
 '8. Is it loose stone, sand, gravel, paving or edging for the ground? → Aggregates, paving & landscaping stone',
 '9. Is it a lime, earth or distemper finish, a regional period tile, or a salvaged building part? → Heritage & reclaimed materials',
 '10. Is it brick, block, cement, a roof covering, insulation or a flue? → Masonry, roofing & insulation',
 '11. Is it timber, a board, a metal section or a moulding? → Timber & sheet materials',
 '<i>Precedence: a period or reclaimed item (zellige, reclaimed brick, chimney pot) goes to Heritage before its modern equivalent; charcoal and logs are fuel (step 1), not Home Fixtures; a door bolt is ironmongery (step 2) before fixings.</i>']
newd = []
for d in depts:
    od = DEPTS_OLD[d['old']]
    nd = {'n': d['n'], 'mode': od['mode'], 't': d['t'], 'ax': d['ax']}
    if od.get('note'): nd['note'] = od['note']
    if od.get('b'): nd['b'] = od['b']
    nd['s'] = d['s']
    newd.append(nd)
out['depts'] = newd

# check no old kind lost
placed = set()
for dpt in newd:
    for s in dpt['s']:
        for k in s['k']: placed.add(k['n'])
lost = [n for n in OK if n not in used]
print('old kinds never based:', lost)
json.dump(out, open('/home/user/Possession-Taxonomy/rebuild/work/STR_C8/C8_new.json', 'w'), ensure_ascii=False, indent=1)
print(len(placed))
