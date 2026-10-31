import json
W='https://en.wikipedia.org/wiki/'
T=W+'T-shirt'
rows=[
('Katharine Hamnett','Designer','Designer who pioneered outsize T-shirts with large-print slogans in the early 1980s.',W+'T-shirt'),
('Global Hypercolour','Streetwear','Colour-change T-shirt brand that was one of the most popular youth brands in the US and UK in the 1980s.',W+'T-shirt'),
('Kamehameha','Heritage & workwear','Aloha shirt manufacturer founded in 1936.',W+'Aloha_shirt'),
('King-Smith Clothiers and Dry Goods','Heritage & workwear','Honolulu clothier whose Ellery Chun registered "aloha sportswear" as a trademark in 1936.',W+'Aloha_shirt'),
('Musa-Shiya the Shirtmaker','Heritage & workwear','Honolulu shirtmaker under Kōichirō Miyamoto, said to have made shirts from Japanese prints.',W+'Aloha_shirt'),
('Shaheen','Heritage & workwear','Aloha shirt manufacturer that began business in 1948.',W+'Aloha_shirt'),
('Annichen Sibbern','Specialist','Norwegian designer who published the yoke-sweater design in the magazine URD in 1930.',W+'Lopapeysa'),
("Hudson's Bay Company",'High street','Retailer that revealed a clothing line for the 2010 Vancouver Winter Olympics in 2009.',W+'Cowichan_sweater'),
('Adrian Nyman','Designer','Label for which Damien Hirst designed the Butterfly Hoodie in 2008.',W+'Hoodie'),
('Sonja de Lennart','Designer','Designer who introduced capri pants in 1948.',W+'Capri_pants'),
('H.A. & E. Smiths','Heritage & workwear','Bermudian firm that improved the design of Bermuda shorts after the war.',W+'Bermuda_shorts'),
('Nathaniel Coxon','Specialist','Bermudian tea shop owner credited with hemming uniform pants into Bermuda shorts in 1914.',W+'Bermuda_shorts'),
('Trimingham Bros.','Heritage & workwear','Bermudian firm that improved the design of Bermuda shorts after the war.',W+'Bermuda_shorts'),
('Dorothée Bis','Designer','French ready-to-wear company whose fashions gave hot pants their name, per Women\'s Wear Daily.',W+'Hot_pants'),
('Sanko Group','Specialist','Owner of the registered brand name Jeggings.',W+'Leggings'),
('Juli Lynne Charlot','Designer','Designer of the poodle skirt in 1947.',W+'Poodle_skirt'),
('Emanuel Ungaro','Designer','Designer whose late-1980s minis were likened to 1950s bathing suits.',W+'Miniskirt'),
('John Bates','Designer','British designer called the first to offer fashionable miniskirts, in 1965.',W+'Miniskirt'),
('Jacques Tiffeau','Designer','Designer who showed above-the-knee lengths in the US in the mid-1960s.',W+'Miniskirt'),
('Rudi Gernreich','Designer','American designer among the first to offer miniskirts, in 1967.',W+'Miniskirt'),
('Eugene Lami','Specialist','Designer of the tutu worn by Marie Taglioni in La Sylphide in 1832.',W+'Tutu_(clothing)'),
('Hippolyte Lecomte','Specialist','Designer of the basic silhouette of the Romantic tutu in 1827.',W+'Tutu_(clothing)'),
('Cecil Beaton','Specialist','Designer named among those who have designed tutus.',W+'Tutu_(clothing)'),
('Barbara Karinska','Specialist','Costumier who designed and made tutus.',W+'Tutu_(clothing)'),
('Isaac Mizrahi','Designer','American designer named among those who have designed tutus.',W+'Tutu_(clothing)'),
('Nicolas Ghesquière','Designer','Designer who tried to bring the jumpsuit back in 2002.',W+'Jumpsuit'),
('Bonnie Cashin','Designer','American designer who made evening jumpsuits from the 1950s.',W+'Jumpsuit'),
('Vera Maxwell','Designer','American designer of sporty jumpsuits in the mid-1940s.',W+'Jumpsuit'),
]
out=[]
for n,seg,d,s in rows:
    out.append({'n':n,'seg':seg,'d':d,'s':s,'kf':'','c':'','f':'','lines':[],'sig':[],'rel':[],'eras':[],'sc':[]})
json.dump(out,open('brands_new.json','w'),ensure_ascii=False)
nb=json.load(open('newbrands.json'))['new']


# ---- brands added when restoring pieces and empty-kind originators
import sys
sys.path.insert(0, '.')
import build_part as B
EXTRA = {
 'Cia. Hering': ('Value & basics', 'Blumenau basics maker whose Camiseta Brasil tee was relaunched in 2026.', None),
 'Sex': ('Subculture & alternative', 'London shop of Malcolm McLaren and Vivienne Westwood, source of the Anarchy in the UK T-shirt.', None),
 'Susana Duniau': ('Specialist', 'French-born Chilean seamstress who designed the pilucho, forerunner of the infant bodysuit.', W + 'Infant_bodysuit'),
 'Hejco': ('Specialist', 'Swedish workwear and uniform shirt maker.', None),
 'Moné Monte Carlo': ('Designer', 'Monaco label whose first hero shirt is La Chemise Monégasque.', None),
 'Éric Bompard': ('Designer', 'French cashmere house whose Origines cardigan is a signature item.', None),
 'Aubin': ('Contemporary & premium', 'London menswear label.', None),
 'Nazzal Studio': ('Designer', 'Palestinian label whose Keffiyah Hoodie is a signature piece.', None),
 'Ursa Minor': ('Contemporary & premium', 'Montreal label named on a sustainable Canadian clothing list.', None),
 'Naked & Famous Denim': ('Japanese & denim', 'Montreal denim brand of Japanese selvedge jeans; Elephant X is the 10th iteration of its Elephant series.', None),
 'Indigofera': ('Japanese & denim', 'Swedish denim brand, founded 2009.', None),
 'R.M. Williams': ('Heritage & workwear', 'Australian outback outfitter, founded 1932.', None),
 'Fashion Box': ('Contemporary & premium', 'Italian owner of the Replay jeans label.', None),
 'KSENIASCHNAIDER': ('Designer', 'Ukrainian label known for hybrid denim pieces.', None),
 'AMIRI': ('Luxury house', 'Los Angeles label founded 2014 whose MX1 jean is a signature style.', None),
 'Beaufille': ('Contemporary & premium', 'Canadian label named on a workwear-brand list.', None),
 'Cimalp': ('Outdoor & technical', 'French maker of stretch windproof ski trousers.', None),
 'Gardeur': ('Contemporary & premium', 'Mönchengladbach trouser maker, founded 1920.', None),
 'JohnBull': ('Japanese & denim', 'Kojima denim and workwear brand, founded 1952.', None),
 'Bourniche': ('Designer', 'Couturier credited with designing harem-style trousers in the 1910s.', W + 'Harem_pants'),
 'Jeanne Margaine-Lacroix': ('Designer', 'Couturier who presented wide-legged trousers in 1910.', W + 'Harem_pants'),
 'M. C. Hammer': ('Streetwear', 'Musician who popularised harem pants, known as Hammer pants, in the late 1980s.', W + 'Harem_pants'),
 'Paul Poiret': ('Designer', 'Paris couturier who introduced harem pants and jupe-culottes in 1911.', W + 'Harem_pants'),
 'Benjamin Bixby': ('Designer', 'Clothing line of André Benjamin that featured plus fours in 2008.', W + 'Plus_fours'),
 "Jimmy'z": ('Streetwear', 'Pacific Palisades surfwear brand, founded 1984, known for E-Z-In shorts.', None),
 'Roots Canada': ('Heritage & workwear', 'Toronto brand whose Salt and Pepper sweatpants are made in Canada.', None),
 'Lux Industries': ('Value & basics', 'Kolkata innerwear maker, founded 1957, whose Lyra leggings launched in 2012.', None),
 'Sweaty Betty': ('Athletic & sportswear', 'London activewear brand, founded 1998, whose Power legging is a bestseller.', None),
 'Bettie Page Clothing': ('Subculture & alternative', 'Las Vegas retro-style label.', None),
 'Hanasport & Golf Couture': ('Specialist', 'Labels under which Hana Havelova-Vanek sold the inverted box pleat she invented in 1984.', W + 'Pleat'),
 'Mariano Fortuny': ('Designer', 'Designer of the Fortuny pleats set in silk.', W + 'Pleat'),
 'Montgomery Ward': ('High street', 'Catalogue retailer that claimed to have invented the skort in 1959.', W + 'Skort'),
 'MiiK': ('Contemporary & premium', 'Etobicoke label named on a made-in-Canada clothing list.', None),
}
nb = json.load(open('newbrands.json'))['new']
have = {r['n'] for r in out}
for n in nb:
    if n in have:
        continue
    seg, d, s = EXTRA[n]
    m = B.MAKERS.get(n.lower().strip())
    c = B.ISO.get(m['country'], '') if m else ''
    f = (m['founded'] if m else '') or ''
    if not s:
        s = (m['sources'].split(' | ')[0] if m else '')
    assert s, n
    out.append({'n': n, 'seg': seg, 'd': d, 's': s, 'kf': '', 'c': c, 'f': f, 'lines': [], 'sig': [], 'rel': [], 'eras': [], 'sc': []})
json.dump(out, open('brands_new.json', 'w'), ensure_ascii=False)
print(len(out), 'new brand rows')
