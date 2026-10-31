import csv, json, re, sys
sys.path.insert(0, '/home/user/Possession-Taxonomy/rebuild/work/V4_A1_TOPS')
import build_part as B
csv.field_size_limit(10**9)
W = B.W
NF = {}
for r in csv.DictReader(open(B.ROOT + 'data/named_forms.tsv'), delimiter='\t'):
    if r['kind_id'].startswith('A1'):
        NF.setdefault(r['name'].lower(), []).append(r)


def ent(kind):
    return B.KINDS[kind]['entries']


def R(kind, piece, brand, name=None, y=None, d=None, s=None, role=None, v=None):
    rows = NF.get(piece.lower(), [])
    r = rows[0] if rows else {}
    src = s or (r.get('sources', '').split(' | ')[0] if r else '')
    assert src, piece
    nm = name or (piece if brand.lower().split()[0].strip("'.") in piece.lower() else f'{brand} {piece}')
    dd = d if d is not None else (r.get('notes', '') or '')
    dd = dd.strip()
    if dd and not dd.endswith('.'):
        dd += '.'
    yy = y if y is not None else (r.get('first_year', '') or '')
    e = B.N(nm, brand, yy, dd, s=src, role=role, v=v)
    ent(kind).append(e)
    return e


def edit(kind, name, **kw):
    for e in ent(kind):
        if e['n'] == name:
            e.update(kw)
            return e
    raise KeyError(name)


# ---- recorded in data/named_forms.tsv: restore with that page
R('T-shirt', 'Pima Curved Hem Tee', 'Buck Mason')
R('T-shirt', 'Camiseta Brasil', 'Cia. Hering')
R('T-shirt', 'Georgia Tee', 'Elizabeth Suzann')
R('T-shirt', 'Anarchy in the UK T-shirt', 'Sex', name='Anarchy in the UK T-shirt')
R('T-shirt', 'Plant and Algae T Shirt', 'Vollebak')
R('T-shirt', 'Arrival', 'Gymshark', name='Gymshark Arrival T-shirt', y='', d='Arrival is the Gymshark essentials range; the T-shirt is designed for lifting, running and HIIT and is made from recycled polyester.', s='https://www.gymshark.com/products/gymshark-arrival-t-shirt-black-ss22') if False else None
ent('T-shirt').append(B.N('Gymshark Arrival T-shirt', 'Gymshark', '', 'Arrival T-shirt is designed for lifting, running and HIIT and is made from recycled polyester, per the brand page.', s='https://www.gymshark.com/products/gymshark-arrival-t-shirt-black-ss22'))
R('Polo shirt', 'Pensacola Polo', 'Billy Reid')
R('Polo shirt', 'g.Deacon', 'Glenmuir')
ent('Polo shirt').append(B.N('Fila Borg polo', 'Fila', '1975', 'Fila modified a polo with pinstripes in 1975 and it became the Borg polo, named after Björn Borg.', s='https://fashionheritage.eu/object-voices-introducing-fila-lines/'))
R('Tank top', 'Cotton Dobby Camisole', 'Uniqlo')
R('Tank top', 'Toffee', 'Cake Maternity', name='Cake Maternity Toffee')
ent('Tank top').append(B.N('Gymshark Arrival Tank', 'Gymshark', '', 'Arrival Tank is part of the Gymshark essentials range, per the brand page.', s='https://www.gymshark.com/products/gymshark-arrival-t-shirt-black-ss22'))
ent('Baby bodysuit').append(B.N('Pilucho (Duniau)', 'Susana Duniau', '1950s', 'French-born Chilean seamstress Susana Duniau designed the pilucho in Chile in the early 1950s, the forerunner of the infant bodysuit.', s=W + 'Infant_bodysuit', role='origin', v=[{'n': 'Opaline export', 'mk': 'Opaline', 'y': '', 'd': 'later exported to the United States and Europe through the clothing brand Opaline'}]))
ent('Rugby shirt').append(B.N('J.Crew Editions x Canterbury rugby shirt', 'J.Crew', '1984', 'J.Crew\'s rugby shirt, sold in a Canterbury collaboration.', s='https://www.jcrew.com/p/mens/categories/clothing/t-shirts/jcrew-editions-x-canterbury-rugby-shirt/M1056'))
R('Dress shirt', 'Non-Iron Twill Shirt', 'Charles Tyrwhitt')
ent('Dress shirt').append(B.N('Uniqlo Super Non-Iron Shirt', 'Uniqlo', '', 'Made entirely of cotton and marketed as needing no ironing, though light ironing may be needed.', s='https://www.uniqlo.com/us/en/contents/feature/masterpiece/product/super-non-iron-shirt/'))
R('Dress shirt', 'Luxor', 'Olymp', name='Olymp Luxor')
R('Dress shirt', 'Henrik', 'Hejco', name='Hejco Henrik')
R('Button-up shirt', 'Alaskan Guide Shirt', 'Filson')
R('Button-up shirt', 'Savoy Suede Workshirt', 'Billy Reid')
R('Button-up shirt', 'Shoals Denim Shirt', 'Billy Reid')
R('Button-up shirt', 'Twisted shirt', 'Lemaire')
R('Button-up shirt', 'La Chemise Monégasque', 'Moné Monte Carlo', name='Moné Monte Carlo La Chemise Monégasque')
ent('Overshirt').append(B.N('Barbour International Steve McQueen Radial Overshirt', 'Barbour', '', 'Steve McQueen collection overshirt in 100% rinse-washed cotton denim.', s='https://www.barbour.com/gb/steve-mcqueen-radial-overshirt-MOS0509IN71.html'))
R('Blouse', 'Rayon Blouse', 'Uniqlo')
R('Blouse', 'Denim Blouse', 'Uniqlo')
R('Sweater', 'Sailor', 'Andersen-Andersen', name='Andersen-Andersen Sailor')
R('Sweater', 'Seaman', 'Andersen-Andersen', name='Andersen-Andersen Seaman')
R('Sweater', 'Rollneck sweater', 'J.Crew')
R('Sweater', 'Burlington V Neck', 'N.Peal', name='N.Peal Burlington V Neck')
R('Sweater', 'Oxford Round Neck', 'N.Peal', name='N.Peal Oxford Round Neck')
R('Sweater', 'Trafalgar Polo Neck', 'N.Peal', name='N.Peal Trafalgar Polo Neck')
R('Sweater', 'g.Lomond', 'Glenmuir', name='Glenmuir g.Lomond')
R('Sweater', 'g.Morar', 'Glenmuir', name='Glenmuir g.Morar')
R('Sweater', 'Vón sweater', 'Guðrun & Guðrun')
R('Cardigan', 'Barbour Hartland Knitted Shawl Neck Cardigan', 'Barbour')
R('Cardigan', 'Barbour Croscombe Knitted Zip Through Cardigan', 'Barbour')
R('Cardigan', 'Aubin Studham Shawl Collar Cardigan', 'Aubin')
R('Cardigan', 'Joules Hillside Cardigan', 'Joules')
R('Cardigan', 'Origines', 'Éric Bompard', name='Éric Bompard Origines')
R('Sweater vest', "Men's Performance Sweater Vest", "Lands' End")
R('Sweater vest', 'Unisex Cotton Modal Pullover Sweater Vest', "Lands' End")
R('Hoodie', 'Keffiyah Hoodie', 'Nazzal Studio')
ent('Hoodie').append(B.N('Reigning Champ Midweight Terry Standard Hoodie', 'Reigning Champ', '', '100% cotton French terry, 390 GSM, with slim and relaxed fits also sold.', s='https://ca.reigningchamp.com/products/midweight-terry-standard-hoodie-navy'))
R('Sweatshirt', 'Marquette Crewneck Sweatshirt', 'Carhartt')
R('Sweatshirt', 'Dover Sweatshirt', 'Billy Reid')
R('Sweatshirt', 'Atubay', 'American Vintage')
R('Sweatshirt', 'Leona crop sweatshirt', 'Ursa Minor')
R('Heritage American jeans', 'Relaxed Straight Rugged Flex Jeans', 'Carhartt')
R('Heritage American jeans', 'Relaxed Fit Carpenter Jeans', 'Dickies')
R('Fashion & designer jeans', 'Ramco', 'R.M. Williams', name='R.M. Williams Ramco')
R('Fashion & designer jeans', 'Anbass', 'Fashion Box', name='Replay Anbass')
R('Fashion & designer jeans', 'MX1', 'AMIRI', name='AMIRI MX1')
R('Fashion & designer jeans', 'Demi-Denim', 'KSENIASCHNAIDER', name='KSENIASCHNAIDER Demi-Denim')
# selvedge
ent('Selvedge reproduction jeans').append(B.N("The Real McCoy's Lot. 001XX", "The Real McCoy's", '', 'Modelled after a 1955 denim silhouette, per the brand page.', s='https://therealmccoys.com/products/the-real-mccoy-s-lot-001_141-indigo'))
R('Selvedge reproduction jeans', 'Lot 64 Outlaw', 'Mister Freedom', name='Mister Freedom Lot 64 Outlaw')
R('Selvedge reproduction jeans', '288 Regular Straight', 'ONI Denim', name='ONI 288 Regular Straight')
R('Selvedge reproduction jeans', 'Lot. 771', 'Burgus Plus', name='Burgus Plus Lot. 771')
R('Selvedge reproduction jeans', 'Weird Guy', 'Naked & Famous Denim', name='Naked & Famous Weird Guy')
ent('Selvedge reproduction jeans').append(B.N('Naked & Famous Elephant series', 'Naked & Famous Denim', '', 'Heavyweight selvedge line; Elephant X is the 10th iteration, at 19 oz.', s='https://nakedandfamousdenim.com/blogs/naked-and-famous-denim/elephant-x', v=[{'n': 'Elephant X', 'mk': 'Naked & Famous Denim', 'y': '', 'd': '19 oz, dark indigo warp with space grey weft'}]))
R('Selvedge reproduction jeans', 'SL-100x', '3sixteen', name='3sixteen SL-100x')
R('Selvedge reproduction jeans', 'Ladbroke Grove', 'Tellason', name='Tellason Ladbroke Grove')
R('Selvedge reproduction jeans', 'BDD-006', 'Benzak', name='Benzak BDD-006')
R('Selvedge reproduction jeans', 'Clint', 'Indigofera', name='Indigofera Clint')
ent('Selvedge reproduction jeans').append(B.N('orSlow 105 Standard Fit', 'orSlow', '', 'Mid-rise straight leg based on vintage 501s, in selvedge or non-selvedge denim.', s='https://www.meadowweb.com/blogs/journal/a-guide-to-orslow-s-denim-fits-at-meadow'))
ent('Selvedge reproduction jeans').append(B.N('orSlow 107 Ivy Fit', 'orSlow', '', 'Slim straight cut with a slight taper, inspired by Ivy League style.', s='https://www.meadowweb.com/blogs/journal/a-guide-to-orslow-s-denim-fits-at-meadow'))
edit('Selvedge reproduction jeans', 'Edwin 503', y='1997', d='Edwin\'s most popular line, first sold in 1997.', s=W + 'Edwin_(company)')
edit('Selvedge reproduction jeans', 'Big John RARE', s='https://denimhunters.com/big-john-rare/', y='1980', d='Slubby shuttle-loom selvedge jeans; the RARE line continues today.')
# trousers etc
R('Trousers', 'Super Secco', 'Aspesi', name='Aspesi Super Secco')
R('Trousers', 'Pleated Wide Pants', 'Uniqlo')
R('Trousers', 'Smart Ankle Pants', 'Uniqlo')
R('Trousers', 'Florence Pant', 'Elizabeth Suzann', name='Elizabeth Suzann Florence Pant')
R('Trousers', 'Antonio Trousers', 'Kardo', name='Kardo Antonio Trousers')
R('Trousers', 'Erwin Trouser', 'Beaufille', name='Beaufille Erwin Trouser')
R('Trousers', 'g.Ross', 'Glenmuir', name='Glenmuir g.Ross')
R('Trousers', 'Bergen', 'Cimalp', name='Cimalp Bergen')
ent('Trousers').append(B.N('Freddy WR.UP shaping pants', 'Freddy', '', 'WR.UP is Freddy\'s patented line of shaping pants, designed in Italy.', s='https://freddywear.de/pages/cms-wrup-technology'))
R('Culottes & skort', 'Cotton Culottes', 'Uniqlo')
R('Chinos', 'Gold School Chino', 'Duck Head', name='Duck Head Gold School Chino')
R('Chinos', 'Benny', 'Gardeur', name='Gardeur Benny')
R('Chinos', "Levi's XX Chino", "Levi's")
R('Cargo trousers', 'One-side pocket cargo jeans (11101)', 'JohnBull', name='JohnBull one-side pocket cargo jeans (11101)')
R('Bondage trousers', 'Bumflap Pant', 'Tripp NYC', name='Tripp NYC Bumflap Pant')
R('Bondage trousers', 'Classic Slim Leg Bondage Pant', 'Tripp NYC', name='Tripp NYC Classic Slim Leg Bondage Pant')
R('Shorts', 'Rigby Cargo Shorts', 'Carhartt')
R('Shorts', 'Loose Fit Flat Front Work Shorts 13 in', 'Dickies')
R('Shorts', 'Arrival 5" Shorts', 'Gymshark')
R('Shorts', 'E-Z-In shorts', "Jimmy'z", name="Jimmy'z E-Z-In shorts")
R('Shorts', 'Alghero Shorts', 'Kardo', name='Kardo Alghero Shorts')
R('Joggers', 'Relaxed Force Joggers', 'Carhartt')
R('Joggers', 'Rastoria Slim trousers', 'Kappa', name='Kappa Rastoria Slim trousers', v=None)
R('Joggers', 'Salt and Pepper sweatpants', 'Roots Canada', name='Roots Salt and Pepper sweatpants')
ent('Joggers').append(B.N('Sergio Tacchini Damarindo', 'Sergio Tacchini', '', 'Damarindo is a Sergio Tacchini range named on a vintage-sportswear listing.', s='https://atomretro.com/sergio_tacchini'))
R('Leggings', 'Elite MCS', '2XU', name='2XU Elite MCS')
R('Leggings', 'Power leggings', 'Sweaty Betty')
R('Leggings', 'Lyra', 'Lux Industries', name='Lux Lyra')
R('Leggings', 'Dagger legging', 'Lip Service')
R('Fit-and-flare & swing dress', 'Shop Till You Drop dress', 'Bettie Page Clothing')
R('Fit-and-flare & swing dress', 'Belinda dress', 'Bettie Page Clothing')
R('Sundress & tea dress', 'Atlanta dress', 'Sleeper')
R('Sundress & tea dress', 'Bettie on Holiday dress', 'Bettie Page Clothing')
R('A-line skirt', 'Bel Skirt', 'Elizabeth Suzann')
R('Jumpsuit', 'Activist Jumpsuit', 'Carla Fernández')
R('Jumpsuit', 'Blakely Jumpsuit', 'MiiK')
# pieces already entries: attach recorded pages to versions
ent('Hoodie')
# ---- empty-kind checks, fetched Wikipedia pages
ent('Pleated skirt').append(B.N('Fortuny pleats', 'Mariano Fortuny', 'early 20th century', 'Crisp pleats set in silk fabrics by designer Mariano Fortuny.', s=W + 'Pleat', role='origin'))
ent('Pleated skirt').append(B.N('Havelova-Vanek inverted box pleat', 'Hanasport & Golf Couture', '1984', 'The inverted box pleat was invented in 1984 by Hana Havelova-Vanek and sold under the labels Hanasport and Golf Couture.', s=W + 'Pleat'))
ent('Harem pants').append(B.N('Poiret harem pants', 'Paul Poiret', '1911', 'The Paris couturier introduced harem pants in 1911 as part of his effort to reinvent Western women\'s fashion.', s=W + 'Harem_pants', role='origin'))
ent('Harem pants').append(B.N('Margaine-Lacroix wide-legged trousers', 'Jeanne Margaine-Lacroix', '1910', 'The couturier presented wide-legged trousers in 1910, a precursor to harem pants.', s=W + 'Harem_pants'))
ent('Harem pants').append(B.N('Bourniche harem pants', 'Bourniche', '1910s', 'A fellow couturier credited with designing such styles at the time.', s=W + 'Harem_pants'))
ent('Harem pants').append(B.N('Hammer pants', 'M. C. Hammer', '1980s', 'A version of harem pants popularised in the late 1980s by M. C. Hammer.', s=W + 'Harem_pants'))
ent('A-line skirt').append(B.N('Dior A-line (1955)', 'Christian Dior', '1955', 'The term A-line was first used by Dior as the label for his spring 1955 collection.', s=W + 'A-line_(clothing)', role='origin'))
ent('Culottes & skort').append(B.N('Montgomery Ward skort', 'Montgomery Ward', '1959', 'Montgomery Ward claimed in its 1959 spring-summer catalogue to have invented the garment it called a skort.', s=W + 'Skort'))
ent('Culottes & skort').append(B.N('Poiret jupe-culotte', 'Paul Poiret', '1911', 'In 1911 Paul Poiret produced designs combining skirts and trousers, known as jupe-culottes.', s=W + 'Skort'))
ent('Plus fours & breeks').append(B.N('Benjamin Bixby plus fours', 'Benjamin Bixby', '2008', 'André Benjamin\'s Benjamin Bixby clothing line featured plus fours in 2008.', s=W + 'Plus_fours'))
