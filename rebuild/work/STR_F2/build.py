import json, os, sys, shutil, importlib.util
W = '/home/user/Possession-Taxonomy/rebuild/work/STR_F2/'
OUT = '/home/user/Possession-Taxonomy/rebuild/out/'

def load(fn):
    sp = importlib.util.spec_from_file_location(fn, W + fn)
    m = importlib.util.module_from_spec(sp); sp.loader.exec_module(m); return m
TT = {}
TT.update(load('tt_data1.py').TT); TT.update(load('tt_data2.py').TT)

d = json.load(open(W + 'bak/F2.json'))
old = {}
for dp in d['depts']:
    for s in dp['s']:
        for k in s['k']:
            old[k['n']] = k

WIKI = 'https://en.wikipedia.org/wiki/'
PHOTO = WIKI + 'List_of_photographic_processes'
FREW = 'https://robertfrew.com/print-terms-and-techniques'
FIBER = WIKI + 'Fiber_art'
GLOSS = WIKI + 'Glossary_of_sculpting'
LUMEN = 'https://courses.lumenlearning.com/pierce-art/chapter/oer-1-21/'

NEW = {
 "Gongbi painting": dict(d="Meticulous fine-brush painting in precise outline and layered colour on sized silk or cooked paper, the counterpart of loose xieyi ink painting.", s=WIKI + 'Gongbi', a="fine-line painting"),
 "Marker and felt-tip drawing": dict(d="An image drawn with felt-tip pens or markers, whose ink dries fast and leaves a permanent mark.", s=LUMEN, a="marker drawing"),
 "Architectural drawing": dict(d="A plan, elevation, section or perspective of a building, kept as art when finely drawn or by a noted architect.", s=WIKI + 'Architectural_drawing', a="architectural rendering · presentation drawing"),
 "Soft-ground etching": dict(d="A print from a plate whose wax ground is softened with grease, so a drawing made through paper lifts the ground in a grainy, pencil-like line.", s=FREW, a=""),
 "Stipple engraving": dict(d="A print from a plate worked in punched or etched dots that build tone, used for portraits and to imitate chalk drawings.", s=FREW, a="stipple"),
 "Chromolithograph": dict(d="A colour lithograph made with a separate stone for each colour, used for 19th-century posters, trade cards and picture reproductions.", s=FREW, a="chromo"),
 "Crystoleum": dict(d="A photograph stuck to the back of a sheet of glass and painted in oils, framed behind convex glass; popular in the late 19th century.", s=PHOTO, a=""),
 "Collotype": dict(d="A photomechanical print from a hardened gelatin plate that gives continuous tone without a screen, in use from 1855 for fine books and postcards.", s=PHOTO, a="photocollography"),
 "Kallitype and Van Dyke print": dict(d="Warm brown contact prints made with iron and silver salts, an alternative to platinum printing.", s=PHOTO, a="kallitype · Van Dyke brown · argyrotype"),
 "Cliché verre": dict(d="A print made by drawing on glass or a coated plate and exposing it on light-sensitive paper, halfway between drawing and photography.", s=PHOTO, a="glass-plate print"),
 "Maquette": dict(d="A small model in clay, wax or plaster made to test the form of a full-size sculpture; a bozzetto is a first sketch model.", s=GLOSS, a="bozzetto · modello"),
 "Woven wall hanging": dict(d="A hand-woven textile made to hang on a wall, freer in form than a picture tapestry.", s=FIBER, a="weaving"),
 "Fibre sculpture": dict(d="A three-dimensional work made of fibre or cloth, whether woven, wrapped, knotted, felted or stuffed.", s=FIBER, a="soft fibre form"),
}

# archetypes to demote (kind -> list of archetype names); folded into tt by hand
DEMOTE = {
 "Oil painting": ["Old Master painting", "Plein-air oil sketch", "Colour-field canvas"],
 "Acrylic painting": ["Flat-colour acrylic canvas"],
 "Encaustic painting": ["Encaustic and collage painting"],
 "Watercolour": ["English landscape watercolour"],
 "Gouache": ["Gouache poster and cover design", "Gouache landscape view"],
 "Tempera painting": ["Renaissance tempera panel", "Modern egg tempera panel"],
 "Fresco": ["Detached fresco fragment"],
 "Ink wash painting": ["Late Qing and modern Chinese ink painting"],
 "Nihonga": ["Modern Nihonga"],
 "Portrait miniature": ["Watercolour-on-ivory miniature"],
 "Pencil drawing": ["Graphite portrait drawing", "Artist's sketchbook"],
 "Charcoal drawing": ["Charcoal sketch", "Contemporary large-scale charcoal drawing"],
 "Chalk drawing": ["Old Master red chalk drawing", "Academic figure study"],
 "Pastel drawing": ["18th-century pastel portrait", "Impressionist pastel"],
 "Coloured-pencil drawing": ["Fine-art coloured-pencil drawing"],
 "Pen-and-ink drawing": ["Old Master pen-and-wash drawing", "Renaissance pen study", "Modern pen drawing", "Architectural drawing"],
 "Metalpoint drawing": ["Renaissance silverpoint", "Modern metalpoint"],
 "Original comic art": ["Splash page", "Interior story page", "Cover art"],
 "Illustration original": ["Magazine cover painting"],
 "Vintage poster": ["Vintage film poster"],
 "Gelatin silver print": ["Magnum distribution press print"],
 "Dye-transfer print": ["Dye-transfer colour photograph"],
 "Tintype": ["Pocket portrait tintype", "Gem tintype", "Contemporary tintype"],
 "Platinum or palladium print": ["Pictorialist platinum print", "Modern platinum print"],
 "Photogram": ["Contemporary cameraless photograph"],
 "Gum bichromate print": ["Pictorialist gum print"],
 "Bromoil print": ["Pictorialist bromoil"],
 "Woodburytype": ["Woodburytype cabinet card"],
 "Wax sculpture": ["Wax portrait relief", "Sculptor's wax model"],
 "Stone carving": ["Grand Tour marble after the antique"],
 "Jade carving": ["Qing jade boulder carving"],
 "Netsuke": ["Katabori netsuke"],
 "Found-object sculpture": ["Cubist construction and assemblage origins"],
 "Asian art ceramics": ["Chinese imperial porcelain"],
 "Needlework sampler": ["Band sampler", "Schoolgirl sampler"],
 "Art quilt": ["American art quilt"],
}

# new archetypes (all sourced from fetched pages)
NEWX = {
 "Found-object sculpture": [dict(n="Fountain", a="Duchamp urinal", d="A porcelain urinal signed 'R. Mutt' and submitted to a 1917 New York exhibition; the original is lost and later authorised versions exist.", mk="Marcel Duchamp", y="1917", s=WIKI + 'Fountain_(Duchamp)', v=[dict(n="1964 Galleria Schwarz edition of eight", mk="Marcel Duchamp", y="1964", d="authorised replicas")], dt="original lost · authorised replicas · signed R. Mutt")],
 "Lithograph": [dict(n="Currier and Ives hand-coloured lithograph", a="Currier & Ives print", d="A New York firm's hand-coloured stone lithographs of American scenes, published in standard folio sizes from the trade card to the large folio.", mk="Currier and Ives", y="1835-1907", s=WIKI + 'Currier_and_Ives', v=[], dt="size: trade card · small · medium · large folio · hand colouring")],
 "Aquatint": [dict(n="Audubon Birds of America (Havell edition)", a="double elephant folio", d="Audubon's life-size bird plates, engraved and aquatinted by Robert Havell Jr. in London and hand-coloured, issued as 435 plates.", mk="Robert Havell Jr.", y="1827-1838", s='https://www.lindahall.org/robert-havell-jr/', v=[], dt="plate number · hand colouring · double-elephant folio sheet")],
}

SEE = {
 "Gouache": [["C4", "Gouache", "the paint itself, not the picture"]],
 "Tempera painting": [["F4", "Icon", "devotional panels in egg tempera"]],
 "Ink wash painting": [["F4", "Thangka & scroll painting", "Buddhist hanging scrolls on cloth"]],
 "Art glass": [["B4", "Glass vase", "factory-made Murano and decorative vases"]],
 "Studio glass": [["B4", "Glass paperweight", "paperweights are decorative glass"]],
 "Art pottery": [["B4", "Earthenware & stoneware vase", "factory vases for the home"]],
 "Studio pottery": [["B4", "Earthenware & stoneware vase", "decorative vases for the home"]],
 "Miniature cottage and village building": [["B4", "Christmas village", "lighted seasonal villages"]],
 "Resin figurine": [["E1", "Static figure", "pop-culture statues and toy figures"]],
 "Carved seal": [["C5", "Artist's & collector's seal", "seals as writing tools"]],
 "East Asian calligraphy": [["F4", "Calligraphy wall panel", "blessing and scripture panels"]],
 "Western calligraphy": [["F1", "Illuminated manuscript", "medieval hand-lettered books"]],
 "Albumen print": [["F5", "Cabinet card", "mounted albumen studio portraits"]],
 "Woodburytype": [["F5", "Carte de visite", "portrait cards in this process"]],
 "Gelatin silver print": [["F5", "Photographic print", "snapshots and family prints"]],
 "Instant print": [["D4", "Integral instant film", "the film that makes the print"]],
 "Jade carving": [["F6", "Jade", "the mineral itself"]],
 "Paper cut": [["B4", "Paper-cut window decoration", "festival window paper-cuts"]],
 "Art quilt": [["B2", "Quilt", "a quilt made for a bed"]],
 "Netsuke": [["A3", "Netsuke", "wearable toggle"]] if False else [],
 "Vintage poster": [["F5", "Paper ephemera", "other printed paper"]] if False else [],
 "Canvas and framed art print": [["B4", "Picture frame", "frames for hanging prints"]],
 "Photogravure": [["F1", "Illustrated book", "gravure plates in books"]] if False else [],
}

# ---------------------------------------------------------------- structure
CAT_AX = "What is the work made in: paint, drawing, printing, photography, a three-dimensional form, clay or glass, fibre, or script and paper, or is it a mass-made figure?"
CAT_KEY = [
 "1. Is it a figure, jug or miniature building made in numbers by a porcelain, crystal or gift house and collected by series? → Collectible figurines",
 "2. Is it a pot or glass piece made by a potter or glassmaker as a one-off, a short run or art pottery, not for table or shelf use? → Studio ceramics & glass",
 "3. Is it a three-dimensional form that is cast, carved, built from parts or light, or collected by the culture that made it? → Sculpture",
 "4. Is the image made by light on a sensitised surface, from a daguerreotype to an instant print? → Photographs",
 "5. Is it an impression pulled from a plate, block, stone or screen, or a poster or reproduction? → Prints",
 "6. Is it made with paint on a panel, canvas, paper, silk, glass or plaster? → Paintings",
 "7. Is it drawn in dry media or ink, or is it original art made for a book, comic, film or building? → Drawings & illustration art",
 "8. Is the picture made of woven, stitched or sewn fibre? → Textile & fibre art",
 "9. Is it brush writing made as the picture, a carved seal, or a picture of pasted, cut or set pieces? → Calligraphy, collage & paper art",
 "<i>Precedence: a mass-made figure is a figurine (step 1) before sculpture (step 3); a studio glass sculpture is studio glass (step 2) before sculpture; a photogravure or collotype is a photograph (step 4) before a print; ink wash on silk is a painting (step 6) before a drawing.</i>",
]

DEPTS = {
"Paintings": dict(
 t="Original pictures made with paint on a movable support, from studio oils to regional traditions with their own materials; ink or pencil on paper → Drawings & illustration art; an inked impression → Prints.",
 ax="What is the picture painted with, or which tradition's materials and format define it?",
 shelves=[
  ("Oil, acrylic & wax", "Pictures in oil, acrylic or wax on canvas, panel or board, plus mixed-media and sprayed work; a water-based picture → Water-based paints, tempera & fresco.", "kinds by binder (oil, acrylic, wax), then paintings that mix media or are sprayed",
   ["Oil painting", "Acrylic painting", "Encaustic painting", "Mixed-media painting", "Spray-paint and street-art painting"]),
  ("Water-based paints, tempera & fresco", "Pictures in watercolour, gouache, egg tempera or lime-plaster fresco, such as a landscape watercolour or a panel in gold ground; an oil picture → Oil, acrylic & wax.", "kinds by what binds the pigment: gum arabic, gum with white body, egg, lime plaster",
   ["Watercolour", "Gouache", "Tempera painting", "Fresco"]),
  ("East Asian painting", "Paintings in brush, ink, mineral pigment or lacquer from China, Japan, Korea and Vietnam, such as a hanging scroll or a six-panel screen; an East Asian print → Relief prints.", "kinds by medium and tradition: ink, fine-line colour, mineral pigment, screen, lacquer, folk",
   ["Ink wash painting", "Gongbi painting", "Nihonga", "Painted folding screen", "Lacquer painting", "Korean folk painting"]),
  ("Miniatures & painting on glass", "Small court and portrait paintings and pictures painted behind glass, such as a locket portrait or a Mughal album page; a large folk painting → Folk, indigenous & outsider painting.", "kinds by tradition: Western portrait, Persian and Indian courts, painting under glass",
   ["Portrait miniature", "Persian and Indian miniature painting", "Reverse glass painting"]),
  ("Folk, indigenous & outsider painting", "Paintings by self-taught or community-trained artists outside the academy, such as Aboriginal dot paintings, Madhubani or Haitian work; East Asian folk painting → East Asian painting.", "kinds by region or by the maker's training",
   ["Aboriginal Australian painting", "Indian folk painting", "Tingatinga painting", "Naive painting", "Outsider art", "Retablo and ex-voto painting"]),
 ]),
"Drawings & illustration art": dict(
 t="Original drawings made as works in themselves, and production art made for a book, comic, film or building; a coloured wash painting → Paintings; a printed copy → Prints.",
 ax="Is it drawn in a dry material, drawn in ink, or made as production art for print, film or building?",
 shelves=[
  ("Dry-media drawings", "Drawings in graphite, charcoal, chalk, pastel, coloured pencil or metalpoint, such as a red-chalk figure study; a drawing in liquid ink → Ink drawings.", "kinds by material, from hard and fine to soft and powdery",
   ["Metalpoint drawing", "Pencil drawing", "Coloured-pencil drawing", "Chalk drawing", "Charcoal drawing", "Pastel drawing"]),
  ("Ink drawings", "Drawings made with a pen, nib or marker in liquid ink, such as a pen-and-wash study; a brush ink landscape of East Asia → East Asian painting.", "",
   ["Pen-and-ink drawing", "Marker and felt-tip drawing"]),
  ("Production art", "Originals made to be reproduced or built, such as a comic page, an animation cel or a book illustration; a finished print of one → Prints.", "kinds by what the original was made for: book or magazine, comic, film, building",
   ["Illustration original", "Original comic art", "Animation cel", "Architectural drawing"]),
 ]),
"Prints": dict(
 t="Impressions pulled in an edition from a plate, block, stone or screen, and posters and reproductions; a unique painted copy → Paintings; a light-made image → Photographs.",
 ax="How does the ink reach the paper: from grooves, a raised surface, a flat surface or stencil, a plate used once, or by reproduction?",
 shelves=[
  ("Intaglio prints", "Prints from lines cut or bitten into a metal plate, such as a Rembrandt etching or an aquatint; a raised-block print → Relief prints.", "kinds by how the grooves are made: acid, burin, needle, dots, rocker",
   ["Etching", "Line engraving", "Drypoint", "Soft-ground etching", "Aquatint", "Mezzotint", "Stipple engraving"]),
  ("Relief prints", "Prints from the raised surface of a cut block, from European woodcuts to Japanese woodblock prints; a print from a flat stone → Planographic & stencil prints.", "kinds by block and tradition: European wood, linoleum, then Chinese and Japanese woodblock from the Edo period on",
   ["Woodcut", "Wood engraving", "Linocut", "Chinese New Year print", "Ukiyo-e print", "Shin-hanga print", "Sōsaku-hanga print", "Surimono"]),
  ("Planographic & stencil prints", "Prints from a flat stone or plate, or through a stencil, such as a Mourlot lithograph or a Warhol screenprint; a block print → Relief prints.", "kinds by how the image is held: greasy stone or plate, then stencil and mesh",
   ["Lithograph", "Chromolithograph", "Screenprint", "Pochoir"]),
  ("Monotypes & built-plate prints", "Prints from a plate used once or built up by hand, such as a Degas monotype; an etched or engraved plate → Intaglio prints.", "",
   ["Monotype", "Collagraph", "Embossed print"]),
  ("Posters & reproductions", "Posters and copies printed from images that exist elsewhere, such as a Belle Epoque poster or a giclée; an artist's own edition → the other print shelves.", "kinds from the period original to the modern copy",
   ["Vintage poster", "Exhibition and art poster", "Giclée and fine-art reproduction", "Canvas and framed art print"]),
 ]),
"Photographs": dict(
 t="Pictures made by light on a sensitised plate or paper and sold as art or collectors' objects; snapshots and cabinet cards → F5; a pictorial print from a block → Prints.",
 ax="How was the image made and carried: a unique early plate, a 19th-century paper print, a hand-made alternative process, or a 20th-century commercial print?",
 shelves=[
  ("Early unique photographs", "One-off images on metal or glass from 1839, such as a cased daguerreotype or a tintype; a paper print → 19th-century paper prints.", "kinds by support: silvered copper, glass, iron, dyed-starch glass",
   ["Daguerreotype", "Ambrotype", "Tintype", "Autochrome", "Crystoleum"]),
  ("19th-century paper prints", "Early prints on paper, such as a salt print from Talbot's negative or an albumen view; a one-off plate image → Early unique photographs.", "kinds by where the image sits: paper fibres, egg white, gelatin relief, printing ink",
   ["Salted paper print", "Albumen print", "Woodburytype", "Collotype", "Photogravure"]),
  ("Hand-made alternative processes", "Prints made by hand-coating paper with light-sensitive chemistry, such as a cyanotype or a platinum print; a commercial darkroom print → 20th-century commercial prints.", "kinds by sensitiser: iron, platinum metals, chromate, then cameraless methods",
   ["Cyanotype", "Kallitype and Van Dyke print", "Platinum or palladium print", "Carbon print", "Gum bichromate print", "Bromoil print", "Photogram", "Cliché verre"]),
  ("20th-century commercial prints", "Prints on factory-made paper, from black-and-white darkroom prints to inkjet and instant film; a hand-coated print → Hand-made alternative processes.", "kinds by chemistry, from black-and-white to colour, instant and digital",
   ["Gelatin silver print", "Chromogenic print", "Dye-transfer print", "Silver dye bleach print", "Instant print", "Archival pigment print"]),
 ]),
"Sculpture": dict(
 t="Fine-art three-dimensional works by an artist, cast, carved, built or collected by origin; a mass-made figure → Collectible figurines; a studio glass or clay piece → Studio ceramics & glass.",
 ax="Is the form built up by casting or modelling, cut away by carving, joined from parts, collected by the culture that made it, or a stand for it?",
 shelves=[
  ("Cast & modelled sculpture", "Works built up in metal, clay, plaster or wax, such as a lifetime bronze or a terracotta bozzetto; a carved work → Carved sculpture.", "kinds by material poured or modelled: metal, clay, plaster, wax, then models and editions",
   ["Bronze sculpture", "Terracotta sculpture", "Plaster sculpture", "Wax sculpture", "Maquette", "Multiple"]),
  ("Carved sculpture", "Works cut from stone, wood, jade, ivory or bone, such as a marble bust or a netsuke; a cast work → Cast & modelled sculpture.", "kinds by material cut away: stone, wood, jade, ivory and bone, then the Japanese netsuke",
   ["Stone carving", "Wood carving", "Jade carving", "Ivory and bone carving", "Netsuke"]),
  ("Constructed, kinetic & light sculpture", "Works joined or built from steel, found objects, fabric or light, such as a Calder mobile or a neon text; a cast or carved work → the shelves above.", "kinds by what it is built from: metal, moving parts, found objects, fabric, light",
   ["Steel and iron sculpture", "Mobile and kinetic sculpture", "Found-object sculpture", "Soft sculpture", "Neon sculpture"]),
  ("African, Oceanic & ancient American sculpture", "Ritual and ceremonial carvings collected by their region, such as a Dan mask or a Moche portrait vessel; modern African art by a named artist → the shelves above.", "kinds by region and object: African masks and figures, Oceanic carving, ancient American figures",
   ["African mask", "African carved figure", "Oceanic carving", "Pre-Columbian figure"]),
  ("Stands & plinths", "Bases and cases made for one sculpture, such as a turntable stand or a stone plinth; a decorative plinth for a room → B4.", "",
   ["Sculpture stand"]),
 ]),
"Collectible figurines": dict(
 t="Figures, jugs and miniature buildings made in numbers by porcelain, crystal and gift houses and collected by series; a one-off artist sculpture → Sculpture; a toy or designer figure → E1.",
 ax="What is the figure made of?",
 shelves=[
  ("Porcelain & bone china", "Figures from named porcelain and bone-china houses and gift makers, such as a Meissen group, a Royal Doulton lady or a Lladro piece; an earthenware figure → Earthenware figures & jugs.", "kinds by maker's home: Continental houses, English houses, then gift-trade makers",
   ["Continental porcelain figure", "English bone-china figure", "Collectible giftware figurine"]),
  ("Earthenware figures & jugs", "Pottery figures and jugs made in the Staffordshire tradition, such as a flatback or a Toby jug; a porcelain figure → Porcelain & bone china.", "",
   ["Staffordshire figure", "Character and Toby jug"]),
  ("Crystal, metal & resin", "Figures and buildings in crystal, pewter, cast metal or resin, such as a Swarovski animal or a Lilliput Lane cottage; a ceramic figure → the shelves above.", "kinds by material: glass and crystal, metal, resin, then resin buildings",
   ["Crystal and glass figurine", "Pewter and cast-metal figurine", "Resin figurine", "Miniature cottage and village building"]),
 ]),
"Studio ceramics & glass": dict(
 t="Pottery and glass made as art by an individual maker or small studio, or as art pottery and art glass; table and shelf ware → B4, B5; a clay or glass figure → Collectible figurines.",
 ax="Is the piece made of clay or of glass?",
 shelves=[
  ("Studio & art pottery", "Clay pieces by individual potters, sculptors, art-pottery works and Asian kilns, such as a Hamada bowl or a moon jar; a factory vase for the home → B4.", "kinds by maker: individual potter, ceramic sculptor, small art-pottery works, Asian kilns",
   ["Studio pottery", "Ceramic sculpture", "Art pottery", "Asian art ceramics"]),
  ("Studio & art glass", "Glass made as art by studios and art-glass houses, and leaded panels, such as a Tiffany lamp shade or a Chihuly piece; a drinking glass → B5.", "",
   ["Studio glass", "Art glass", "Stained-glass panel"]),
 ]),
"Textile & fibre art": dict(
 t="Pictures and forms made of woven, stitched or sewn fibre, hung or displayed as art; a rug for the floor → B2; a bedding quilt → B2.",
 ax="How is the work made: woven, stitched, pieced or sewn on, or built in three dimensions?",
 shelves=[
  ("Textile art", "Fibre works made to be hung or displayed, such as a tapestry, a sampler or a mola; a rug or bedding → B2.", "kinds by technique: weave, stitch, piece, sew on, build in fibre",
   ["Tapestry", "Woven wall hanging", "Embroidered picture", "Needlework sampler", "Art quilt", "Appliqué textile picture", "Fibre sculpture"]),
 ]),
"Calligraphy, collage & paper art": dict(
 t="Works where script, or pasted, cut or set pieces, make the picture; a printed page → Prints; a book hand-lettered by a scribe → F1.",
 ax="Is the image made of written characters, or of pasted, cut or set pieces?",
 shelves=[
  ("Calligraphy & seals", "Brush and pen writing made as the picture, and carved seals, such as a hanging scroll in running script or a Shoushan stone seal; a printed text → F1.", "kinds by script tradition: East Asian, Islamic, Western, then carved seals",
   ["East Asian calligraphy", "Islamic calligraphy", "Western calligraphy", "Carved seal"]),
  ("Collage, mosaic & paper art", "Pictures built or cut from pieces, such as a Cubist collage, a Roman mosaic fragment or a papel picado; a painting on paper → Paintings.", "kinds by how the pieces are joined: pasted, set, cut",
   ["Collage", "Mosaic picture", "Paper cut", "Silhouette portrait"]),
 ]),
}
# kind order across depts is as in DEPTS dict (python preserves insertion order)

def parse_tt(s):
    out = []
    for g in s.split(' | '):
        lab, rest = g.split(': ', 1)
        out.append([lab.strip(), [x.strip() for x in rest.split(';') if x.strip()]])
    return out

def build():
    new = dict(c=d['c'], rev=d.get('rev', True), lead=d['lead'], ax=CAT_AX, key=CAT_KEY, b=d['b'], depts=[])
    olddept = {dp['n']: dp for dp in d['depts']}
    used = set(); missing = []
    for dn, spec in DEPTS.items():
        od = olddept[dn]
        nd = {k: v for k, v in od.items() if k not in ('s',)}
        nd['t'] = spec['t']; nd['ax'] = spec['ax']; nd['s'] = []
        for sn, st, sax, kinds in spec['shelves']:
            sh = dict(n=sn, t=st)
            if sax: sh['ax'] = sax
            elif len(kinds) > 3: print('NEEDS AX', sn)
            sh['k'] = []
            for kn in kinds:
                if kn in old:
                    k = json.loads(json.dumps(old[kn]))
                    k.pop('t', None)
                else:
                    nk = NEW[kn]
                    k = dict(n=kn, a=nk['a'], d=nk['d'], s=nk['s'], x=[])
                dem = DEMOTE.get(kn, [])
                if dem and k.get('x'):
                    k['x'] = [a for a in k['x'] if a['n'] not in dem]
                for a in NEWX.get(kn, []):
                    k.setdefault('x', []).append(a)
                if kn not in TT: missing.append(kn)
                else: k['tt'] = parse_tt(TT[kn])
                if SEE.get(kn): k['see'] = SEE[kn]
                if kn == 'Resin figurine': pass
                used.add(kn); sh['k'].append(k)
            nd['s'].append(sh)
        new['depts'].append(nd)
    unused = [n for n in old if n not in used]
    return new, missing, unused

if __name__ == '__main__':
    new, missing, unused = build()
    print('missing tt:', missing); print('unused old kinds:', unused)
    tmp = OUT + 'F2.json.tmp'
    json.dump(new, open(tmp, 'w'), ensure_ascii=False, indent=1)
    os.replace(tmp, OUT + 'F2.json')
