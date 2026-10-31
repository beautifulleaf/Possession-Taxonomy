import json, copy, os, sys
ROOT='/home/user/Possession-Taxonomy/rebuild/'
old=json.load(open(ROOT+'work/STR_F4/bak/F4.json'))
K={}
for dp in old['depts']:
    for s in dp['s']:
        for k in s['k']: K[k['n']]=k
def xs(kind,arch):
    for a in K[kind].get('x',[]):
        if a['n']==arch: return a
    raise KeyError((kind,arch))
WP='https://en.wikipedia.org/wiki/'

# ---------- kind edits ----------
# TT: types by named axes (hand-written)
TT={
'Crucifix & devotional cross':[["Placement",["Wall crucifix","Standing crucifix","Hand or pocket cross"]],["Material",["Carved wood","Cast metal"]]],
'Icon':[["Making",["Hand-painted in egg tempera","Printed on wood"]],["Cover",["Uncovered","Metal-covered (riza or oklad)"]],["Form",["Single panel","Travelling icon"]]],
'Devotional statue':[["Subject",["Madonna","Sacred Heart","Saint","Infant Jesus"]],["Material",["Carved wood","Resin or plaster"]],["Dress",["Painted","Dressed (vested) figure"]]],
'Murti':[["Deity",["Ganesha","Lakshmi","Durga","Saraswati","Kali"]],["Material",["Panchaloha","Brass","Marble","Black granite","Wood","Clay"]],["Use",["Home worship","Festival (utsava) murti"]]],
'Buddha image':[["Subject",["Shakyamuni","Amida","Kannon","Medicine Buddha (Yakushi)"]],["Style",["Thai","Tibetan"]],["Material",["Bronze","Wood","Stone"]]],
'Tsa-tsa':[["Form",["Plaque","Miniature chorten"]],["Material",["Clay","Metal"]]],
'Nativity set':[["Contents",["Figures only","Figures with stable","Stable only"]],["Size",["Table-top","Life-size"]]],
'Icon_':None,
'Thangka & scroll painting':[["Making",["Hand-painted","Printed","Silk appliqué"]],["Mount",["Hanging scroll with silk brocade","Kakejiku honzon scroll (Japan)"]]],
'Calligraphy wall panel':[["Script",["Thuluth","Naskh","Kufic","Diwani","Nasta'liq"]]],
'Mizrach & shiviti':[["Plaque",["Mizrach (marks the east wall)","Shiviti (the divine name)"]],["Making",["Papercut","Printed","Embroidered"]]],
'Yantra':[["Material",["Brass plate","Silver or copper plate"]],["Form",["Flat plate","Meru (three-dimensional)"]]],
'Pysanka':[["Egg",["Hen","Goose","Wooden"]],["Technique",["Wax-resist (drop-pull)","Etched"]]],
'Khanda emblem':[["Form",["Wall plaque","Pendant","Flag finial (Nishan Sahib)"]]],
'Palm cross':[["Material",["Woven palm","Wooden"]]],
'Home altarpiece & triptych':[["Form",["Folding triptych","Diptych","Carved retablo","Icon triptych","Travelling altar"]]],
'Butsudan':[["Mounting",["Floor-standing","Wall-hung","Mini"]],["Finish",["Karaki","Gold-leaf (kinbutsudan)"]],["Style",["Traditional","Modern furniture-style"]]],
'Home mandir':[["Mounting",["Wall-mounted","Freestanding"]],["Material",["Wooden","Marble"]],["Top",["Flat","Gopuram"]]],
'Kamidana':[["Doors",["One-door (ichisha)","Three-door (sansha)"]],["Mounting",["Wall shelf"]]],
'Household deity altar':[["Mounting",["Wall-mounted","Floor cabinet"]],["Deity marker",["Red paper tablet","Carved tablet"]]],
'Miniature stupa':[["Form",["Eight chorten shapes","Kalachakra stupa","Votive stupa"]]],
'Palki sahib':[["Material",["Wooden"]],["Furnishing",["With quilted mat and cushions"]],["Use",["Fixed","Processional palanquin"]]],
'Prie-dieu':[["Design",["Shelf version","Padded armrest version","Double"]]],
'Reliquary':[["Form",["Casket or chasse","Arm or bust reliquary","Cross-shaped","Monstrance-type","Pendant theca"]]],
'Relic':[["Class",["First class (body part or object of Christ's life)","Second class (item the saint used)","Third class (touched a first or second class relic; abolished 2017)"]],["Significance",["Significant (insigni)","Non-significant (non insigni)"]]],
# prayer aids
'Rosary':[["Length",["Five-decade","One-decade","Finger rosary","Wrist rosary","Pocket rosary"]],["Related chaplet",["Divine Mercy (five decades)","St Michael (36 beads)"]]],
'Anglican prayer beads':[["Count",["33 beads and a cross"]],["Form",["Looped string"]]],
'Prayer rope':[["Knots",["33","50","100"]],["Make",["Knotted cord","Bead version"]]],
'Tasbih':[["Count",["33 beads","99 beads","100 beads"]],["Material",["Wood","Amber","Faturan","Karbala clay","Olive seed"]],["Form",["Strand","Bracelet"]]],
'Mala':[["Count",["108 beads","54 beads","27 beads"]],["Bead",["Rudraksha","Tulsi","Sandalwood","Crystal"]],["Form",["Full mala","Wrist mala"]]],
'Juzu':[["School",["Shingon (red string, counter strands)","Tendai (flat soroban beads)","Nichiren (five counters)","Zen (no counters)","Jodo Shinshu (short)","Jodo-shu (double ring)"]],["Count",["108 beads","54 beads"]]],
'Prayer rug':[["Material",["Wool","Silk","Cotton"]],["Origin",["Turkish","Persian","Indian dari"]],["Form",["Woven rug","Travel mat","Padded mat","Smart mat"]]],
'Tallit':[["Colour",["Ashkenazi white with black stripes","Sephardi all white"]],["Material",["Wool","Silk"]],["Accessory",["Tallit bag"]]],
'Rumala':[["Material",["Silk","Cotton"]],["Decoration",["Embroidered","Plain"]]],
'Khata':[["Material",["White silk","Cotton or polyester"]],["Colour",["White","Yellow-gold"]]],
'Prayer flag':[["Hanging",["Horizontal (lung ta)","Vertical (darchog)"]],["Set",["Five-colour set"]]],
'Shrine rope':[["Material",["Hemp","Rice straw"]],["Fittings",["With shide"]],["Size",["Household kamidana size"]]],
'Altar handbell':[["Tradition",["Christian sanctus bell","Hindu puja ghanta","Tibetan drilbu"]]],
'Rin':[["Size",["Table rin","Large temple rin"]],["Support",["With cushion","Without cushion"]]],
'Tingsha':[["Make",["Matched pair joined by strap","Antique bronze"]]],
'Prayer wheel':[["Size",["Handheld","Large temple","Row installation"]],["Power",["Hand","Water","Wind","Fire","Electric"]]],
'Mokugyo':[["Material",["Wood","Composite"]],["Set",["With mallet and cushion"]]],
'Damaru':[["Material",["Wood","Metal"]],["Variant",["Skull damaru (export banned)"]]],
'Shankha':[["Turn",["Right-turning (dakshinavarta)","Common left-opening"]],["Finish",["Carved","With metal mount"]]],
'Shofar':[["Horn",["Ram's horn (Ashkenazi, Sephardi)","Kudu horn (Yemenite)","Moroccan flat shofar"]],["Mouthpiece",["Plain","Carved"]]],
'Devotional medal':[["Metal",["Aluminium","Silver","Gold-filled"]],["Finish",["Plain","Enamelled"]]],
'Scapular':[["Colour",["Brown","Green","White","Black","Blue"]],["Form",["Cloth","Scapular medal"]]],
'Holy card':[["Printing",["Chromolithograph","Laminated"]],["Purpose",["Funeral card","Relic-bearing card"]]],
'Omamori':[["Purpose",["Traffic safety","Avoiding evil","Open luck","Education","Business prosperity","Love and marriage","Pregnancy","Family safety"]]],
'Evil-eye charm':[["Shape",["Eye bead","Hand-shaped"]],["Placement",["Worn as a bead","Hung on a wall or door"]]],
'Ofuda':[["Material",["Paper (kamifuda)","Wood (kifuda)"]],["Placement",["Purpose-specific (doorway, kitchen)"]],["Form",["Shinsatsu"]]],
'Ema':[["Size",["Standard plaque (about 15 x 9 cm)","Large votive ema"]],["Design",["Plain","Zodiac-year ema"]]],
'Daoist talisman':[["Make",["Paper","Burnable"]],["Placement",["Door-lintel","Carried"]]],
'Bagua mirror':[["Surface",["Flat","Convex","Concave"]]],
'Gau box':[["Material",["Copper","Gold-plated","Wood"]],["Contents",["Empty","With deity statue"]]],
'Dreamcatcher':[["Material",["Willow and sinew"]],["Decoration",["Feathers and beads","Plain"]]],
'Tefillin':[["Make",["Peshutim (simple)","Dakkot (thin, single hide)","Gassot (thick, single hide)"]],["Script",["Beis Yosef","Arizal","Velish"]]],
'Tallit katan':[["Material",["Wool","Cotton","Silk"]],["Fringes",["Tzitzit tied"]]],
'Kirpan':[["Blade",["Iron","Steel"]],["Size",["Small"]],["Carrier",["Gatra strap"]]],
'Kara':[["Metal",["Plain steel","Iron"]],["Design",["Engraved khanda","Plain"]]],
'Kangha':[["Material",["Wood"]],["Size",["Small"]]],
# scriptures
'Bible':[["Format",["Family Bible","Pocket Bible"]]],
'Mushaf':[["Format",["Single volume","Thirty-part (juz') set"]]],
'Gutka & pothi':[["Form",["Gutka (small bound book)","Pothi (loose-leaf)"]]],
'Sutra book':[["Format",["Folding book (orihon)","Scroll","Bound book"]]],
'Torah scroll':[["Layout",["42 lines per column","Yemenite 51 lines"]],["Dress",["Mantle","Sephardi tik case"]]],
'Megillah':[["Form",["Parchment scroll","Illustrated scroll"]]],
'Mezuzah scroll':[["Script",["Beit Yosef","Ari"]],["Size",["Cut to fit the case"]]],
'Ketubah':[["Making",["Illuminated","Papercut","Printed"]],["Mount",["Unframed","Framed"]]],
"Qur'an box & cover":[["Material",["Wood","Mother-of-pearl","Silver"]],["Form",["Box","Fabric cover"]]],
'Mezuzah case':[["Material",["Silver","Wood","Ceramic","Pewter","Stone"]]],
'Rehal':[["Build",["Folding wood","Carved","Inlaid"]],["Fitting",["With box","Without box"]]],
'Torah finials':[["Material",["Silver","Wood"]],["Fitting",["With bells","Without bells"]]],
'Torah pointer':[["Material",["Silver","Wood"]],["Shape",["Straight","Twisted (Mountain Jews form)"]]],
# vessels
'Chalice':[["Bowl",["Gilded","Enamelled"]],["Set",["Single cup","Travelling set"]]],
'Altar cruets':[["Set",["Pair of cruets","Pair with tray"]]],
'Kiddush cup':[["Material",["Silver","Pewter","Porcelain"]],["Form",["Stemmed","With saucer"]]],
'Kapala':[["Material",["Skull","Metal"]]],
'Holy-water vessel':[["Form",["Wall-hung stoup","Home font","Glass or plastic bottle","Souvenir shrine bottle"]]],
'Aspergillum':[["Form",["Metal sprinkler","Brush","Pocket sprinkler"]]],
'Kalash':[["Metal",["Brass","Copper","Silver"]]],
'Ritual washing cup':[["Handles",["Two-handled","One-handled"]],["Material",["Silver","Stainless steel"]]],
'Ciborium':[["Form",["Covered cup"]],["Material",["Gilt metal","Silver"]]],
'Pyx':[["Use",["For the sick","Pocket pyx"]]],
'Paten':[["Tradition",["Western saucer-like paten","Byzantine diskos on a stand","Alexandrian flat paten"]]],
'Monstrance':[["Form",["Sunburst","Tower","Relic monstrance"]]],
'Seder plate':[["Wells",["Six-well","Tiered"]],["Material",["Ceramic","Silver"]],["Set",["With matching matzah plate"]]],
'Challah board & cover':[["Board",["Wooden","Glass"]],["Cover",["Embroidered cover"]]],
'Puja thali':[["Material",["Steel","Brass","Silver"]],["Set",["Daily plate","Festival set"]]],
'Offering vessel':[["Holds",["Water bowl","Rice bowl","Tea cup","Flower vase (hanatate)"]]],
'Offering stand':[["Form",["Brass plate with stand","Tiered","Fruit stand"]]],
'Mandala offering set':[["Form",["Metal plate with rings"]]],
'Etrog box':[["Material",["Silver","Wood","Cardboard"]]],
'Spice box':[["Form",["Tower","Fruit-shaped","Box"]],["Material",["Silver","Wood"]],["Set",["Havdalah set"]]],
'Alms box':[["Tradition",["Church alms box","Tzedakah box","Saisen-bako (wooden coin box with grate)","Mite box"]]],
'Ritual spoon or ladle':[["Form",["Achamani","Sruk (fire ladle)"]],["Material",["Brass"]]],
'Havan kund':[["Material",["Copper","Brass","Brick"]],["Shape",["Square","Pyramid"]]],
'Dorje (vajra)':[["Prongs",["One-prong","Three-prong","Five-prong"]],["Set",["Single","With bell (drilbu)"]]],
'Phurba':[["Material",["Wood","Metal","Stone"]]],
'Kartika':[["Blade",["Blue iron blade"]],["Set",["With kapala"]]],
'Peach-wood sword':[["Material",["Peach wood","Steel and brass"]]],
'Paper-streamer wand':[["Streamers",["Two shide (gohei)","Many shide (onusa)","Kinpei"]]],
'Chaur sahib':[["Hair",["Horsehair","Synthetic"]],["Handle",["Metal","Wooden"]]],
'Qibla compass':[["Type",["Magnetic","Digital"]],["Fitting",["Plain","With tally counter"]]],
# light
'Oil lamp for worship':[["Material",["Clay diya","Brass diya","Stone kalvilakku"]],["Rite",["Aarti lamp","Akhand diya (continuous)","Floating leaf lamp"]],["Mounting",["Standing","Hanging"]]],
'Sanctuary lamp & lampada':[["Mounting",["Hanging","Wall-mounted","Standing"]],["Light source",["Oil","LED"]]],
'Hanukkah lamp':[["Fuel",["Candle","Oil","Electric"]],["Mounting",["Table","Wall-mounted"]]],
'Seven-branch menorah':[["Setting",["Table","Wall","Large public"]]],
'Shabbat candlesticks':[["Material",["Silver","Brass"]],["Form",["Pair","Travel","Candelabrum"]]],
'Altar candlestick':[["Mounting",["Floor-standing","Table altar"]],["Material",["Brass"]],["Fitting",["With candle follower"]]],
'Ramadan lantern':[["Material",["Metal and glass","Plastic"]],["Extras",["Musical","String lights"]]],
'Ritual lantern':[["Setting",["Standing stone toro","Standing bronze toro","Hanging tsuri-doro","Floating Obon lantern"]]],
'Altar & votive candle':[["Use",["Altar","Votive","Vigil","Procession","Grave"]],["Burn",["7-day glass"]],["Wax",["Beeswax"]]],
'Paschal candle':[["Marking",["Cross, alpha and omega, year numerals","Five grains of incense"]],["Wax",["Beeswax"]]],
'Memorial candle':[["Occasion",["Yahrzeit","Seven-day memorial","Grave light"]],["Burn",["24-hour","7-day glass"]]],
'Havdalah candle':[["Form",["Braided multi-wick"]]],
'Advent wreath':[["Hanging",["Table wreath","Hanging wreath"]],["Candles",["Three violet one rose","Four red"]]],
'Ritual incense':[["Form",["Cored stick (agarbatti)","Solid stick (dhoop, senko)","Cone","Coil","Rope","Paper","Powder","Resin or granulated","Smudge bundle"]],["Blend",["Bakhoor","Church incense"]]],
'Incense burner':[["Form",["Stick holder","Cone holder","Dhupdaan","Koro"]]],
'Thurible & hand censer':[["Form",["Chained thurible","Hand censer"]],["Fitting",["Plain","Orthodox kadilo with bells"]]],
'Joss paper':[["Offered to",["Deities (gold paper)","Ancestors (silver paper)"]],["Form",["Cash paper","Hell bank notes","Zhizha paper goods"]]],
# divination
'Tarot deck':[["Size",["Standard 78 cards","Pocket size"]],["Edition",["Reproduction of a historic deck","Independent artist deck"]]],
'Lenormand deck':[["Cards",["36 cards"]],["Face",["Plain","With playing-card inset"]]],
'Oracle deck':[["Theme",["Angel","Faerie","Goddess","Animal","Affirmation"]]],
'Rune set':[["Alphabet",["Elder Futhark (24 runes)","Younger Futhark"]],["Material",["Stone","Wood","Bone"]],["Set",["With pouch"]]],
'I Ching set':[["Method",["Three coins","Fifty yarrow stalks","Wood or lacquered rods"]],["Case",["With pouch or box","Loose"]]],
'Kau cim':[["Count",["100 sticks"]],["Holder",["Bamboo cup (qiantong)"]]],
'Jiaobei':[["Material",["Wood","Bamboo","Clam shell"]]],
'Omikuji':[["Fortune",["Graded from dai-kichi to kyo"]],["Extras",["Paper slip only","With charm"]]],
'Spirit board':[["Make",["Wooden","Printed"]],["Finish",["Glow-in-the-dark","Plain"]],["Sold as",["Board with planchette","Planchette only"]]],
'Crystal ball':[["Material",["Quartz","Glass"]],["Stand",["With stand","Without stand"]]],
'Scrying mirror':[["Material",["Obsidian","Black glass"]],["Shape",["Flat","Convex"]]],
'Pendulum':[["Material",["Crystal","Brass","Wooden"]]],
'Dowsing rods':[["Form",["Forked stick","L-rods"]]],
'Luopan':[["School",["San He","San Yuan","Zong He"]]],
'Athame':[["Handle",["Black handle (British Traditional)","Plain"]],["Blade",["Double-edged"]],["Material",["Copper or bronze","Obsidian"]]],
'Altar pentacle':[["Material",["Metal","Wood","Cloth","Parchment"]]],
'Wand':[["Material",["Wood (oak, hazel)","Metal","Bone or stone"]],["Tip",["Plain","Crystal-tipped"]]],
'Cauldron':[["Material",["Cast iron","Bronze"]],["Fitting",["With lid","Tripod"]]],
'Book of Shadows':[["Use",["Coven copy","Personal journal"]],["Form",["Bound blank book"]]],
# funeral
'Coffin':[["Shape",["Coffin (tapered)","Casket (rectangular)"]],["Material",["Steel","Wood","Cardboard or X-Board","Bamboo, willow or banana leaf","Mycelium"]],["Supply",["Bought","Rental casket"]]],
'Burial shroud':[["Fibre",["White cotton","Linen","Wool","Hemp"]],["Tradition",["Tachrichim","Kaffan"]]],
'Cremation urn':[["Size",["Keepsake (1-50 cubic inches)","Companion (about 400+ cubic inches)"]],["Use",["Pet","Scattering","Military"]],["Material",["Biodegradable"]],["Fitting",["Urn plaque or medallion"]]],
'Cremation jewellery':[["Form",["Necklace","Bracelet","Charm or pendant"]]],
'Urn vault':[["Form",["Urn vault","Grave liner"]],["Material",["Concrete"]]],
'Grave marker':[["Form",["Headstone","Footstone","Ledger slab","Plaque"]],["Material",["Granite","Bronze","Wood"]]],
'Memorial tablet':[["Finish",["Black lacquer","Gilt"]],["Form",["Kuridashi ihai"]]],
'Ancestral tablet':[["Material",["Red paper","Wood","Tile","Metal"]]],
'Memorial register':[["Form",["Bound book","Folding album"]]],
# regalia
'Mace':[["Body",["Parliament","Council","University"]],["Material",["Silver-gilt","Wood"]]],
'Sceptre':[["Office",["Sovereign","Civic"]],["Material",["Gilt metal","Wood","Resin replica"]]],
'Orb':[["Office",["Sovereign","Civic"]],["Material",["Gilt metal","Resin replica"]]],
'Gavel':[["Material",["Wood"]],["Set",["Gavel only","With sound block"]]],
'Chain of office':[["Office",["Mayoral","Judicial","Academic"]],["Material",["Gold","Silver-gilt","Gilt metal"]]],
'Crown of office':[["Office",["Civic","Academic","Ceremonial"]],["Material",["Gilt metal","Fabric"]]],
}
TT.pop('Icon_')

def kind(name, **kw):
    """existing kind with optional overrides"""
    k=copy.deepcopy(K[kw.pop('base',name)])
    k['n']=name
    drop=kw.pop('drop_x',[])
    k['x']=[a for a in k.get('x',[]) if a['n'] not in drop]
    for a in kw.pop('add_x',[]): k['x'].append(a)
    if 'a_add' in kw:
        al=[x for x in (k.get('a') or '').split(' · ') if x]+kw.pop('a_add')
        k['a']=' · '.join(al)
    for key,v in kw.items():
        if v is None: k.pop(key,None)
        else: k[key]=v
    k.pop('t',None)
    if name not in TT: sys.exit('no tt: '+name)
    k['tt']=TT[name]
    return k
def new(name,d,s,tg=None,a='',x=None,see=None):
    k={'n':name,'a':a,'d':d,'s':s,'tt':TT[name]}
    if tg: k['tg']=tg
    if x: k['x']=x
    if see: k['see']=see
    return k

# ---------- shelves ----------
D=[]
def dept(n,mode,t,ax,shelves,note=None,b=None):
    dd={'n':n,'mode':mode,'t':t,'ax':ax,'s':shelves}
    if note: dd['note']=note
    if b: dd['b']=b
    D.append(dd)
def shelf(n,t,ax,ks):
    s={'n':n,'t':t,'k':ks}
    if ax: s['ax']=ax
    return s
def tell(k,*see):
    k['see']=[list(x) for x in see]; return k

ET=WP+'Evil_eye'
# ---- 1 Images
dept('Images, altars & shrines','variety',
 "Sacred images and signs, and the shrines and cases that house them, across traditions; a picture bought as art → Art; a lamp or candle set before one → Light, incense & offerings.",
 "Is it the sacred image or sign itself, the structure that houses it, or a relic?",
 [shelf('Sculpted figures & scenes',"Three-dimensional images of Christ, saints, deities and buddhas, and the scenes built from them; a flat painted image → Painted & written images.",
   "kinds by the subject sculpted: saint, deity, buddha, votive clay, whole scene",
   [kind('Devotional statue'),kind('Murti',drop_x=['Ganesha murti','Lakshmi murti','Durga murti','Saraswati murti','Kali murti']),
    kind('Buddha image',drop_x=['Amida Buddha'],add_x=[{"n":"Budai","a":"Laughing Buddha · Hotei","d":"Smiling, pot-bellied monk figure, venerated as an incarnation of Maitreya and sold as a luck figure across East Asia.","mk":"","y":"d. 917","s":WP+'Budai',"v":[],"dt":"seated or standing · bronze, wood, resin, ceramic"}]),
    kind('Tsa-tsa'),kind('Nativity set')]),
  shelf('Painted & written images',"Flat sacred images made by painting, printing or lettering and framed, mounted or scrolled; a figure in the round → Sculpted figures & scenes.",
   "kinds by how the image is made: painted panel, painted scroll, calligraphy, plaque, diagram, decorated egg",
   [kind('Icon'),kind('Thangka & scroll painting'),kind('Calligraphy wall panel'),
    new('Mizrach & shiviti',"Decorated wall plaque marking the east wall of a Jewish home (mizrach) or displaying the divine name (shiviti).",WP+'Jewish_ceremonial_art',tg=['Jewish']),
    kind('Yantra'),kind('Pysanka',see=[["B4","Decorated Easter egg","Easter egg as seasonal decor"]])]),
  shelf('Crosses & emblems',"Signs of faith hung, held or carried, with no figure beyond the crucified Christ; a figure of a saint or deity → Sculpted figures & scenes.",None,
   [kind('Crucifix & devotional cross'),kind('Palm cross'),kind('Khanda emblem')]),
  shelf('Home altars & shrines',"Furniture and structures that house sacred images or scripture at home; a church fitting or a temple building is not a personal possession.",
   "kinds by form: folding panel, cabinet shrine, wall shelf, miniature monument, seat or kneeler",
   [kind('Home altarpiece & triptych'),kind('Butsudan'),kind('Home mandir'),kind('Kamidana',drop_x=['Wall-mounted kamidana']),kind('Household deity altar'),kind('Miniature stupa'),kind('Palki sahib'),kind('Prie-dieu')]),
  shelf('Relics & reliquaries',"Remains and objects kept as holy, and the cases made to hold them; a medal or charm → Prayer & devotion aids.",None,
   [kind('Reliquary',drop_x=['Chasse reliquary','Monstrance-type reliquary','Pendant theca']),kind('Relic')])],
 note=None)
# ---- 2 Prayer aids
dept('Prayer & devotion aids','variety',
 "Objects a person holds, wears, spreads, rings or hangs while praying; the image prayed to → Images, altars & shrines; a text → Scriptures, scrolls & holders.",
 "How is it used in prayer: counted, spread or draped, sounded, carried as a token, or worn?",
 [shelf('Prayer beads',"Strings of beads or knots that count prayers; a bead bracelet sold as fashion → jewellery (A3).",
   "kinds by the form of the string and its count: decades with a cross, knotted cord, loop of 33 or 99, loop of 108",
   [kind('Rosary'),
    new('Anglican prayer beads',"Looped string of 33 beads and a cross, used mainly by Anglicans as a counting aid to prayer.",WP+'Anglican_prayer_beads',tg=['Christian'],a='Anglican rosary'),
    kind('Prayer rope'),kind('Tasbih',drop_x=['Misbaha','Faturan tasbih'],a_add=['misbaha']),kind('Mala',drop_x=['Rudraksha mala','Tulsi mala']),kind('Juzu',drop_x=['Jodo-shu nikka juzu','Shingon juzu'])]),
  shelf('Mats, shawls & hangings',"Cloths and cords used in prayer: knelt on, worn as a shawl, wrapped round scripture, offered as a scarf or hung out of doors.",
   "kinds by how the cloth or cord is used: knelt on, worn as a shawl, covering scripture, offered as a scarf, hung outdoors, tied across a shrine",
   [kind('Prayer rug',drop_x=['Turkish prayer rug','Persian prayer rug','Indian dari prayer rug']),kind('Tallit',drop_x=['Tallit gadol','Tallit katan'],a_add=['tallit gadol']),kind('Rumala'),kind('Khata'),kind('Prayer flag',drop_x=['Lung ta','Darchog']),kind('Shrine rope')]),
  shelf('Bells, wheels & horns',"Objects that make the sound of prayer or are turned to send it; a musical instrument played for its own sake → instruments (E3).",
   "what the hand does: ring, strike, turn, shake, blow",
   [kind('Altar handbell',base='Altar bell & chime',d="Handbell rung at an altar or shrine: the Christian sanctus bell, the Hindu puja ghanta and the Tibetan drilbu.",a_add=['altar bell']),
    new('Rin',"Bowl-shaped bell set rim upwards on a cushion and struck, used at Buddhist altars, especially in Japan; the Himalayan singing bowl is its cousin.",WP+'Standing_bell',tg=['Buddhist'],a='standing bell · singing bowl (temple)',see=[["E3","Singing bowl","same bowl-bell as a musical instrument"]]),
    new('Tingsha',"Pair of small, thick cymbals joined by a strap or chain and struck together in Tibetan Buddhist prayer and ritual.",WP+'Tingsha',tg=['Buddhist']),
    kind('Prayer wheel',drop_x=['Handheld prayer wheel']),kind('Mokugyo'),kind('Damaru'),kind('Shankha',drop_x=['Dakshinavarta shankha']),kind('Shofar',drop_x=["Ram's horn shofar",'Yemenite shofar'])]),
  shelf('Medals & cards',"Small struck or printed tokens carried or kept in a book; a charm from a Japanese shrine or a talisman → Charms & talismans.",None,
   [kind('Devotional medal'),kind('Scapular'),kind('Holy card',drop_x=['Chromolithographed holy card'])]),
  shelf('Charms & talismans',"Objects believed to protect or bring luck, carried, hung or fixed by a door; a medal of a saint → Medals & cards.",
   "kinds by where the charm is kept: carried or worn, kept on a shelf or hung at a shrine, fixed over a door or bed",
   [kind('Omamori',base='Protective charm',d="Small cloth pouch charm sold by a Japanese shrine or temple for one purpose and carried or hung on a bag.",a='omamori · Japanese shrine charm',drop_x=['Omamori','Nazar','Hamsa']),
    kind('Gau box'),
    new('Evil-eye charm',"Amulet against the evil eye: a blue eye bead (nazar) or a hand-shaped plaque (hamsa), worn, or hung on a wall or door.",ET,a='nazar · hamsa · hand of Fatima',
        x=[xs('Protective charm','Nazar'),xs('Protective charm','Hamsa')],see=[["A3","Evil-eye amulet","the same charm as jewellery"]]),
    kind('Ofuda'),kind('Ema'),kind('Daoist talisman'),kind('Bagua mirror'),kind('Dreamcatcher')]),
  shelf('Articles of faith worn',"Objects worn daily by the observant as a sign of faith; ordinary clothing or a bangle sold as fashion → A-series.",
   "kinds by where on the body: head and arm, under the shirt, waist, wrist, hair",
   [kind('Tefillin'),
    new('Tallit katan',"Small four-cornered fringed garment worn under the shirt every day by observant Jewish men.",xs('Tallit','Tallit katan')['s'],tg=['Jewish']),
    new('Kirpan',"Small sword or knife carried by initiated Sikhs as one of the Five Ks, worn on a strap (gatra).",K['Worn article of faith']['s'],tg=['Sikh']),
    kind('Kara',base='Worn article of faith',d="Steel or iron bangle worn on the wrist by initiated Sikhs as one of the Five Ks.",a='steel bangle'),
    new('Kangha',"Small wooden comb worn in the hair by initiated Sikhs as one of the Five Ks.",K['Worn article of faith']['s'],tg=['Sikh'])])])
# fix Tallit tallit katan tg etc after

# ---- 3 Scriptures
bible=kind('Bible',base='Sacred text copy',d="A Bible as a physical book to keep at home, from the large family Bible with record pages to a pocket copy; editions for reading belong to the Literature taxonomy.",a='family Bible',drop_x=['Mushaf','Gutka','Orihon sutra book','Megillat Esther'],tg=['Christian'])
mush=new('Mushaf',"Bound copy of the Qur'an as an object, kept wrapped or on a stand; editions for reading belong to the Literature taxonomy.",xs('Sacred text copy','Mushaf')['s'],tg=['Islamic'],a="Qur'an copy")
gut=new('Gutka & pothi',"Small bound prayer book (gutka) or loose-leaf volume (pothi) holding Sikh scripture, kept in a cloth wrapper.",xs('Sacred text copy','Gutka')['s'],tg=['Sikh'])
sut=new('Sutra book',"Hand-copied or printed Buddhist scripture, often a folding concertina book (orihon).",xs('Sacred text copy','Orihon sutra book')['s'],tg=['Buddhist'],x=[xs('Sacred text copy','Orihon sutra book')])
meg=new('Megillah',"Parchment scroll of the Book of Esther, read at Purim; collectors prize illustrated Italian and Dutch scrolls.",xs('Sacred text copy','Megillat Esther')['s'],tg=['Jewish'],a='Megillat Esther · Esther scroll')
dept('Scriptures, scrolls & holders','variety',
 "Sacred texts as objects, the scrolls and documents written for rites, and the cases, stands and ornaments made for them; a text edition to read → Literature taxonomy.",
 "Is it the bound text, a scroll or document written for a rite, or what shelters, supports or adorns a text?",
 [shelf('Sacred text copies',"Books of scripture kept as objects of reverence in the home; a rolled scroll → Scrolls & documents.",
   "kinds by book form: bound codex, bound mushaf, small prayer book, folding book",[bible,mush,gut,sut]),
  shelf('Scrolls & documents',"Parchment and paper written by hand for a rite or a vow, from the full Torah scroll to the marriage contract.",
   "kinds from the full scroll to the small parchment and the decorated contract",
   [kind('Torah scroll'),meg,kind('Mezuzah scroll'),kind('Ketubah',drop_x=[])]),
  shelf('Cases, stands & ornaments',"Objects that shelter, support, cover, crown or point along a text; the text itself → Sacred text copies.",
   "kinds by what the object does for the text: shelter, support, cover, crown, point",
   [kind("Qur'an box & cover"),kind('Mezuzah case'),kind('Rehal'),kind('Torah finials'),kind('Torah pointer')])])
# ---- 4 Vessels
dept('Ritual vessels & implements','variety',
 "Cups, dishes, boxes and hand tools used in a rite at home or in worship; ordinary tableware → Kitchen; a fighting blade → Weapons.",
 "What is the object for: holding drink, water, bread, food or offerings, or being handled in the rite?",
 [shelf('Cups, cruets & bowls',"Vessels for the wine or other libation of a rite; a water vessel → Water vessels.",
   "kinds by what is held: Communion wine, Sabbath wine, wine and water, offering bowl",
   [kind('Chalice',drop_x=['Western chalice','Eastern chalice']),kind('Kiddush cup'),
    new('Altar cruets',"Pair of small jugs holding the wine and water brought to the altar at Mass.",WP+'Vasa_Sacra',tg=['Christian']),
    new('Kapala',"Cup made from a human skull, or a metal copy, held by Tibetan Buddhist deities and used for offerings.","https://www.exoticindia.com/article/ritual",tg=['Buddhist'],a='skull cup')]),
  shelf('Water vessels',"Vessels for holy water, ritual washing and blessed water on the altar.",None,
   [kind('Holy-water vessel',d="Stoup, home font or bottle holding blessed water, hung by the door or kept on a shelf.",tg=['Christian']),kind('Kalash'),kind('Ritual washing cup')]),
  shelf('Eucharistic bread vessels',"Vessels that hold, carry or show the bread of Communion.",
   "kinds from the vessel that holds many hosts to the one that shows one: covered cup, small box, plate, display",
   [kind('Ciborium',base='Host vessel',d="Covered cup holding the hosts for Communion.",a='covered cup',drop_x=['Pyx','Ciborium']),
    new('Pyx',"Small round box carrying a few hosts to the sick.",xs('Host vessel','Pyx')['s'],tg=['Christian']),
    new('Paten',"Small plate holding the host at the Eucharist; the Byzantine diskos stands on a foot.",WP+'Paten',tg=['Christian'],a='diskos'),
    kind('Monstrance',drop_x=['Sunburst monstrance','Tower monstrance'])]),
  shelf('Dishes & stands for food and offerings',"Plates, boards and stands that carry the food or offerings of a rite.",
   "kinds by the meal or offering: Seder, Sabbath bread, daily puja, shrine offering, tantric offering",
   [kind('Seder plate',drop_x=['Six-item seder plate']),kind('Challah board & cover'),kind('Puja thali'),kind('Offering vessel'),kind('Offering stand'),kind('Mandala offering set')]),
  shelf('Boxes & containers',"Boxes that keep a ritual fruit, spice or coin.",None,
   [kind('Etrog box'),kind('Spice box',drop_x=['Havdalah spice container']),kind('Alms box')]),
  shelf('Fire & ladle tools',"Tools for pouring into and tending the sacred fire.",None,
   [kind('Ritual spoon or ladle'),kind('Havan kund')]),
  shelf('Hand-held implements',"Objects held in the hand and used in the rite; a drinking vessel → Cups, cruets & bowls.",
   "kinds by what the hand does: hold up, drive, cut, strike, wave, fan, sprinkle, point",
   [kind('Dorje (vajra)',drop_x=['Dorje and drilbu set']),kind('Phurba'),kind('Kartika',drop_x=['Tibetan kartika']),kind('Peach-wood sword',drop_x=['Qing Taoist ritual sword']),kind('Paper-streamer wand'),kind('Chaur sahib'),
    new('Aspergillum',"Brush or perforated rod used to sprinkle holy water; also a pocket sprinkler.",WP+'Vasa_Sacra',tg=['Christian'],a='holy-water sprinkler'),
    kind('Qibla compass',drop_x=['Traditional qibla compass'],see=[["E2","Navigation compass","ordinary compass"]])])])
# ---- 5 Light
dept('Light, incense & offerings','mixed',
 "Things lit or burnt before a sacred image or for the dead: lamps, candles, incense and paper offerings; a lamp or candle for home mood → B3 or B4.",
 "What is lit or burnt: oil or wax in a holder, a candle, incense, or paper?",
 [shelf('Lamps & candleholders',"Holders and lamps that carry a flame for worship or a festival; the candle itself → Candles & wreaths.",
   "kinds by the flame: oil lamp, hanging oil lamp, multi-flame lamp, candlestick, lantern",
   [kind('Oil lamp for worship'),kind('Sanctuary lamp & lampada'),kind('Hanukkah lamp',drop_x=['Hanukkiah'],a_add=['hanukkiah']),kind('Seven-branch menorah'),kind('Shabbat candlesticks'),
    kind('Altar candlestick',drop_x=['Altar candlestick set'],see=[["B4","Candle holder","the same holder for the home"]]),
    kind('Ramadan lantern',drop_x=['Fanous Ramadan'],a_add=['fanous']),kind('Ritual lantern',see=[["B3","Decorative lantern","lantern as home lighting"]])]),
  shelf('Candles & wreaths',"Candles made for a rite and the wreath that holds them; a scented or decor candle → B4.",
   "kinds by when it is lit: every service, Easter, remembrance of the dead, end of the Sabbath, Advent",
   [kind('Altar & votive candle',base='Ritual candle',d="Plain candle lit at an altar, before an icon or as a votive offering, from beeswax altar candles to vigil lights.",drop_x=['Orthodox offering candle','Seven-day memorial candle','Paschal candle','Havdalah candle','Yahrzeit candle'],tg=['Christian']),
    kind('Paschal candle',base='Ritual candle',d="Large candle blessed and lit at Easter, marked with a cross, alpha and omega and the year.",s=xs('Ritual candle','Paschal candle')['s'],drop_x=['Orthodox offering candle','Seven-day memorial candle','Paschal candle','Havdalah candle','Yahrzeit candle'],tg=['Christian'],a=''),
    kind('Memorial candle',base='Ritual candle',d="Candle burnt for a dead person: the Jewish yahrzeit candle, the seven-day memorial candle and the grave light.",s=xs('Ritual candle','Seven-day memorial candle')['s'],drop_x=['Orthodox offering candle','Seven-day memorial candle','Paschal candle','Havdalah candle','Yahrzeit candle'],tg=['Christian','Jewish'],a='yahrzeit candle · grave light'),
    kind('Havdalah candle',base='Ritual candle',d="Braided multi-wick candle lit at the end of the Sabbath.",s=xs('Ritual candle','Havdalah candle')['s'],drop_x=['Orthodox offering candle','Seven-day memorial candle','Paschal candle','Havdalah candle','Yahrzeit candle'],tg=['Jewish'],a='',),
    kind('Advent wreath',see=[["B4","Wreath","wreath as seasonal decor"]])]),
  shelf('Incense & burners',"Incense burnt in worship and the vessels that burn it; incense for the home → B4.",
   "kinds from the incense burnt to the vessel that burns it, fixed then swung",
   [kind('Ritual incense',see=[["B4","Stick incense","incense for the home"]]),
    kind('Incense burner',see=[["B4","Incense burner","the same burner for home fragrance"]]),
    kind('Thurible & hand censer',drop_x=['Hand censer'])]),
  shelf('Paper offerings',"Paper money and goods burnt for deities and ancestors.",None,[kind('Joss paper')])])
# ---- 6 Divination
dept('Tarot & divination','variety',
 "Objects used to foretell, answer a question or work ritual magic; a card game → Board, card & table games (E1).",
 "How is it used: read from cards, cast or drawn by chance, watched or pointed, or wielded in ritual?",
 [shelf('Tarot & oracle decks',"Card decks read to foretell; organised by pattern archetype and publisher, never as flat title lists.",None,
   [kind('Tarot deck',drop_x=['Independent artist tarot'],add_x=[{"n":"Etteilla tarot","a":"Grand Etteilla","d":"First tarot deck designed for divination, with new card names and order, published in Paris.","mk":"","y":"1789","s":WP+'Etteilla',"v":[],"dt":"reproduction · 78 cards"}],see=[["E1","Playing cards","the same cards used for games"]]),
    kind('Lenormand deck'),
    kind('Oracle deck',drop_x=['Cartomancy oracle deck','Hay House oracle line','Independent artist oracle'],r=[["Hay House oracle line","Hay House"]])]),
  shelf('Casting & drawing tools',"Objects cast, drawn or tossed to get an answer by chance.",
   "kinds by what is cast or drawn: carved stones, coins or stalks, numbered sticks, moon blocks, paper slips",
   [kind('Rune set',drop_x=['Elder Futhark rune set']),kind('I Ching set',drop_x=['Three-coin set','Yarrow stalk set']),kind('Kau cim'),kind('Jiaobei'),kind('Omikuji')]),
  shelf('Watching & pointing tools',"Objects the reader watches or follows rather than casts.",
   "kinds by what the reader watches: letters spelled, an image in glass, a swinging weight, a twitching rod, a ring of directions",
   [kind('Spirit board'),kind('Crystal ball'),kind('Scrying mirror'),
    new('Pendulum',"Weight on a string or chain held over a chart or a map and read by its swing.",K['Dowsing tool']['s'],a='dowsing pendulum'),
    kind('Dowsing rods',base='Dowsing tool',d="Forked stick or pair of L-shaped rods held in the hands and read by how they move.",a='divining rod'),
    new('Luopan',"Chinese magnetic compass with up to 40 rings of feng shui formulas, used to fix the direction of a building.",WP+'Luopan',tg=['Daoist & Chinese folk'],a='feng shui compass',see=[["E2","Navigation compass","ordinary compass"]])]),
  shelf('Ritual-magic tools',"Tools laid on or used at a witch's altar.",
   "kinds by role at the altar: blade, disc, wand, vessel, book",
   [kind('Athame'),kind('Altar pentacle'),kind('Wand'),kind('Cauldron'),kind('Book of Shadows')])])
# ---- 7 Funeral
dept('Funeral & memorial','tier',
 "Goods bought for a death: to hold the body or ashes, mark the grave or keep the memory at home; flowers and one-off services are not possessions.",
 "Does it hold the body or ashes, mark the grave, or keep the memory at home?",
 [shelf('Containers for body & ashes',"What the dead are laid in or what the ashes are kept in, from coffin to wearable keepsake.",
   "kinds from burial containers to cremation containers, large to wearable",
   [kind('Coffin'),kind('Burial shroud'),kind('Cremation urn',see=[["B4","Decorative urn","decor urn is not made for ashes"],["G2","Cremation plot & niche","where the urn is placed"]]),
    new('Cremation jewellery',"Pendant, bracelet or charm made to hold a small amount of ashes.","https://funeral.com/collections/all-cremation-urns-and-cremation-jewelry")]),
  shelf('Grave goods',"What goes in or on the grave.",None,[kind('Urn vault'),kind('Grave marker')]),
  shelf('Home memorials & ancestor tablets',"Objects kept at home to remember the dead, chiefly in East Asian traditions.",None,
   [kind('Memorial tablet'),kind('Ancestral tablet',drop_x=['Household spirit tablet']),kind('Memorial register')])])
# ---- 8 Regalia
reg_s=lambda n:K[n]['s']
dept('Ceremonial regalia & office insignia','mixed',
 "Staffs, chains, crowns and hammers that mark civic, judicial, academic or royal office rather than a faith; a real weapon → Weapons; a tiara worn as jewellery → A3.",
 "What does it signal: authority carried, judgement, rank worn, or sovereignty?",
 [shelf('Carried insignia',"Objects held or carried to show authority, from the parliamentary mace to the gavel.",
   "kinds by what is held: staff of authority, sovereign's rod, globe, striking hammer",
   [kind('Mace',see=[["E4","Mace","the weapon form"]]),
    new('Sceptre',"Rod held by a ruler or civic head as a sign of authority.",WP+'Regalia_of_the_Netherlands'),
    new('Orb',"Globe topped with a cross held by a sovereign as a sign of rule.",WP+'Regalia_of_the_Netherlands'),
    kind('Gavel')]),
  shelf('Worn insignia',"Chains and crowns worn to mark an office.",None,
   [kind('Chain of office'),kind('Crown of office',see=[["A3","Crown","crown as hair jewellery"]])])])

# ---------- tags, fixes ----------
for dp in D:
    for s in dp['s']:
        for k in s['k']:
            if k['n'] in ('Mushaf','Gutka & pothi','Sutra book','Megillah'): pass
out=copy.deepcopy(old)
out['depts']=D
out['ax']="What does the object do for its owner: show something sacred, aid a person's prayer, hold or carry a text, serve a rite, give light and smoke, foretell, remember the dead, or mark an office?"
out['key']=[
"1. Is it a sacred image or sign, or the shrine, altar or case that houses one? → Images, altars & shrines",
"2. Is it held, worn, hung or sounded by a person while praying (beads, mat, bell, medal, charm)? → Prayer & devotion aids",
"3. Is it a sacred text, a scroll or document written for a rite, or what shelters, supports or adorns one? → Scriptures, scrolls & holders",
"4. Is it a cup, dish, box or hand tool used in a rite (chalice, seder plate, dorje)? → Ritual vessels & implements",
"5. Is it lit or burnt as an offering (lamp, candle, incense, joss paper)? → Light, incense & offerings",
"6. Is it used to foretell, answer a question or work ritual magic (cards, runes, spirit board)? → Tarot & divination",
"7. Does it hold the body or ashes, mark the grave or keep a dead person's memory at home? → Funeral & memorial",
"8. Is it carried or worn to mark a civic, legal, academic or royal office rather than a faith? → Ceremonial regalia & office insignia",
"<i>Precedence: a lamp used only in worship is light (step 5) before a vessel (step 4); a candle holder or lamp for home decor belongs to B3 or B4; a text edition sold to read belongs to the Literature taxonomy; a ritual blade made for fighting belongs to Weapons.</i>"]
tmp=ROOT+'work/STR_F4/F4.new.json'
json.dump(out,open(tmp,'w'),ensure_ascii=False,indent=1)
os.replace(tmp,ROOT+'out/F4.json')
# renames
ren={"Sacred text copy":"Bible","Host vessel":"Ciborium","Altar bell & chime":"Altar handbell","Protective charm":"Omamori","Worn article of faith":"Kara","Ritual candle":"Altar & votive candle","Dowsing tool":"Dowsing rods"}
json.dump(ren,open(ROOT+'out/F4_renames.json','w'),indent=1,ensure_ascii=False)
# accounting
names=lambda d:{k['n'] for dp in d['depts'] for s in dp['s'] for k in s['k']}
o,n=names(old),names(out)
print('removed',sorted(o-n)); print('added',sorted(n-o))
cnt=lambda d:(len(d['depts']),sum(len(dp['s']) for dp in d['depts']),len(names(d)),sum(len(k.get('x',[])) for dp in d['depts'] for s in dp['s'] for k in s['k']))
print(cnt(old),cnt(out))
