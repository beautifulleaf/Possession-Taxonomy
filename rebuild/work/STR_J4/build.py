import json,copy,os
SRC='work/STR_J4/bak/J4.json'
d=json.load(open(SRC))
K={}   # name -> kind
for D in d['depts']:
    for S in D['s']:
        for k in S['k']: K[k['n']]=k
FR='https://en.wikipedia.org/wiki/List_of_culinary_fruits'
VG='https://en.wikipedia.org/wiki/List_of_vegetables'
SW='https://en.wikipedia.org/wiki/Edible_seaweed'
MU='https://www.nutritionadvance.com/?p=6621'
HB='https://en.wikipedia.org/wiki/List_of_culinary_herbs_and_spices'

def demote(name, xs, newtt=None):
    k=K[name]; keep=[]; m=k.setdefault('m',[])
    have={tuple(e) for e in m}
    for x in k.get('x',[]):
        if x['n'] in xs:
            e=(x['n'],x.get('mk','') or '')
            if e not in have: m.append(list(e)); have.add(e)
            for v in x.get('v',[]):
                e=(v['n'],v.get('mk','') or '')
                if e not in have: m.append(list(e)); have.add(e)
        else: keep.append(x)
    k['x']=keep
    assert len(k['x'])+len(xs)>=0
def new(n,dd,s,a='',tt=None,x=None):
    k={'n':n,'a':a,'d':dd,'s':s}
    if tt: k['tt']=tt
    if x: k['x']=x
    K[n]=k; return k
def tt(name,groups):
    k=K[name]; k['tt']=groups; k.pop('t',None)

# ---- demotions of generic archetypes
D_={
'Peach':['Flat peach'],'Strawberry':['Alpine strawberry'],'Blueberry':['Lowbush wild blueberry'],
'Melon':['Cantaloupe','Honeydew'],'Banana':['Red banana','Apple banana'],
'Dragon fruit':['White-fleshed dragon fruit','Red-fleshed dragon fruit','Yellow dragon fruit'],
'Passion fruit':['Purple passion fruit','Yellow passion fruit'],'Tamarillo':['Red tamarillo','Yellow tamarillo'],
'Lime':['Makrut lime'],'Carrot':['Purple carrot'],'Beetroot':['Golden beetroot','Albino beetroot'],
'Radish':['Daikon','Korean mu'],'Potato':['Andean native potatoes'],'Sweet pepper':['Bell pepper'],
'Cucumber':['Slicing cucumber','Pickling cucumber','Seedless cucumber'],'Courgette':['Pattypan squash'],
'Cabbage':['White cabbage','Red cabbage','Savoy cabbage','Spring greens'],
'Broccoli':['Calabrese','Sprouting broccoli'],
'Cauliflower':['White cauliflower','Orange cauliflower','Green cauliflower','Purple cauliflower'],
'Kale':['Curly kale','Ornamental kale'],'Pak choi':['White-stemmed pak choi','Green-stemmed pak choi'],
'Chard':['Green chard','Red-ribbed chard','Rainbow chard'],
'Pea':['Garden pea','Mangetout','Sugar snap pea'],
'Green bean':['French bean','Runner bean','Yardlong bean','Romano bean'],
'Asparagus':['Green asparagus','White asparagus'],
'Lettuce':['Iceberg','Romaine','Butterhead','Batavia','Loose-leaf'],
'Chicory':['Radicchio','Witloof','Puntarelle'],
'Basil':['Lemon basil','Purple basil','Greek bush basil'],
'Perilla':['Shiso','Kkaennip'],
'Button mushroom':['White button','Cremini','Portobello'],
'Shiitake':['Donko','Koshin'],
'Oyster mushroom':['Pearl oyster','King oyster','Pink oyster','Golden oyster'],
'Matsutake':['Japanese matsutake','Jilin matsutake'],
'Banana ':[],
}
for n,xs in D_.items():
    if n in K and xs: demote(n,set(xs))

# ---- new kinds from splits / coverage
lx=K['Lettuce']['x']; celtuce=[x for x in lx if x['n']=='Celtuce']
K['Lettuce']['x']=[x for x in lx if x['n']!='Celtuce']
ca=K['Custard apple']; cax={x['n']:x for x in ca['x']}
cher=K['Custard apple']; cher['n']='Cherimoya'; cher['a']='custard apple · chirimoya'
cher['d']='Fresh Annona cherimola, the custard apple of the Andes, sold by cultivar and protected origin.'
cher['x']=[cax['Fino de Jete']]; cher.pop('t',None); K['Cherimoya']=cher
new('Atemoya',cax['Atemoya']['d'],'https://en.wikipedia.org/wiki/Atemoya',m=None) if False else None
atm=new('Atemoya','Fresh hybrid of cherimoya and sugar apple, first crossed at the USDA lab in Miami in 1908.','https://en.wikipedia.org/wiki/Atemoya')
atm['m']=[['Gefner',''],['Thompson','']]
new('Sugar apple','Fresh Annona squamosa, also called sweetsop, with segmented, sweet, custard-like flesh.','https://en.wikipedia.org/wiki/Custard_Apple',a='sweetsop')
new('Soursop','Fresh Annona muricata, a large spiny green fruit with tart, aromatic white flesh; a different species from sugar apple.','https://en.wikipedia.org/wiki/Custard_Apple',a='guanábana')
new('Pawpaw','Fresh Asimina triloba, the North American custard-flavoured fruit, sold in season.',FR)
# mushrooms
sp=K['Speciality cultivated mushrooms']; shim=sp; shim['n']='Shimeji'; shim['a']='beech mushroom · buna-shimeji'
shim['d']='Fresh clustered, firm-stemmed Hypsizygus mushroom sold in brown and white forms.'; shim.pop('t',None); K['Shimeji']=shim
demote('Shimeji',{'Buna-shimeji','Bunapi-shimeji'})
new('King oyster mushroom','Fresh Pleurotus eryngii, a thick, meaty white stem with a small tan cap.',MU,a='king trumpet · eryngii')
new('Enoki','Fresh Flammulina velutipes sold as a bundle of long, thin white stems with tiny caps.',MU,a='enokitake')
new('Maitake','Fresh Grifola frondosa grown as a frilled, feathery cluster of grey-brown fronds.',MU,a='hen-of-the-woods')
new('Lion\'s mane','Fresh Hericium erinaceus, a white shaggy pom-pom with a seafood-like texture when cooked.',MU)
new('Wood ear','Fresh or soaked Auricularia, a dark, crisp-gelatinous ear-shaped mushroom.',MU,a='pepeao · Jew\'s ear')
new('Straw mushroom','Fresh Volvariella volvacea, a small egg-shaped mushroom grown on rice straw.',MU)
new('Giant puffball','Fresh Calvatia gigantea, a wild white ball sliced and fried while the flesh is still firm.',MU)
# sea vegetables
new('Nori','Red seaweed (Porphyra) pressed into sheets, sold fresh, toasted or dried.',SW,a='laver')
new('Kombu','Broad brown kelp (Saccharina) sold fresh or dried for stock and eating.',SW,a='kelp')
new('Arame','Brown seaweed (Eisenia bicyclis) sold shredded as thin dark strands.',SW)
new('Hijiki','Brown seaweed (Sargassum fusiforme) sold as short dark twigs.',SW)
new('Mozuku','Brown seaweed (Cladosiphon okamuranus) sold as fine slimy strands in vinegar.',SW)
new('Irish moss','Red seaweed (Chondrus crispus) sold fresh or dried, used for setting jellies.',SW,a='carrageen')
# fruit
new('Calamansi','Small, sour, round green-orange citrus (Citrus × microcarpa) eaten as juice and zest.',FR,a='calamondin')
new('Bilberry','Wild Vaccinium myrtillus with dark blue flesh throughout, sold fresh in northern Europe.',FR,a='whortleberry')
new('Cempedak','Fresh jackfruit relative (Artocarpus integer) with sweet, strong-smelling flesh.',FR)
new('Breadfruit','Starchy Artocarpus altilis, mostly cooked, sometimes sold fresh in tropical markets.',FR)
new('Langsat','Small Southeast Asian fruit (Lansium) with translucent, sweet-sour segments.',FR,a='lanzones')
new('Wax apple','Bell-shaped crisp, watery fruit (Syzygium samarangense) of Southeast Asia.',FR,a='rose apple')
new('Tamarind','Pods of Tamarindus indica with sweet-sour pulp, sold fresh in tropical markets.',FR)
new('Bael','Hard-shelled fruit (Aegle marmelos) of the Indian subcontinent with soft, aromatic pulp.',FR)
new('Mamey sapote','Large brown-skinned fruit (Pouteria sapota) with soft orange flesh.',FR)
new('Acerola','Small red, vitamin-rich cherry-like fruit (Malpighia emarginata).',FR,a='Barbados cherry')
new('Jaboticaba','Purple fruit (Plinia cauliflora) that grows directly on the trunk.',FR)
new('Naranjilla','Orange Andean fruit (Solanum quitoense) with green, tart flesh, eaten as juice.',FR,a='lulo')
new('Babaco','Seedless, five-sided Andean papaya relative (Vasconcellea × heilbornii).',FR)
# vegetables
new('Oca','Andean tuber (Oxalis tuberosa) with waxy, tangy flesh in several colours.',VG)
new('Yacón','Andean root (Smallanthus sonchifolius) with crisp, sweet, pear-like flesh.',VG)
new('Water chestnut','Crisp, sweet corm of Eleocharis dulcis, sold fresh in Asian shops.',VG)
new('Chinese artichoke','Small segmented tuber (Stachys affinis) with a nutty taste.',VG,a='crosne')
new('Cucamelon','Grape-sized cucumber-like fruit (Melothria scabra) with a sour tang.',VG,a='mouse melon')
new('Snake gourd','Long, twisting Trichosanthes cucumerina gourd cooked young in South Asian dishes.',VG)
new('Drumstick','Long, ridged pods of Moringa oleifera used in South Asian curries.',VG,a='moringa pod')
new('Winged bean','Four-winged green pod (Psophocarpus tetragonolobus) of Southeast Asia.',VG)
new('Mustard greens','Peppery leaves of Brassica juncea, from mild to very hot.',VG)
new('Tatsoi','Rosette of dark, spoon-shaped Asian brassica leaves with mild mustard taste.',VG)
new('Garland chrysanthemum','Herb-scented leaves of Glebionis coronaria used in East Asian cooking.',VG,a='shungiku · tong ho')
new('Purslane','Succulent, slightly sour leaves of Portulaca oleracea.',VG)
new('Malabar spinach','Thick, mucilaginous vine leaves (Basella) cooked like spinach in warm climates.',VG)
new('Dandelion greens','Bitter leaves of cultivated or wild dandelion, eaten raw or cooked.',VG)
new('Celtuce','Stem lettuce grown for its thick, crunchy peeled stem.',VG,a='stem lettuce')
K['Celtuce']['x']=celtuce
new('Banana blossom','Purple banana flower bud peeled and cooked as a vegetable in Asia.',VG)
new('Heart of palm','Tender inner stem of certain palms, sold fresh in the tropics and tinned elsewhere.',VG)
# herbs
for n,dd,a in [('Chervil','Delicate, anise-scented leaves, one of the French fines herbes.',''),
 ('Lovage','Tall celery-flavoured leaves used in soups and stocks.',''),
 ('Lemon balm','Lemon-scented soft leaves used in teas and desserts.',''),
 ('Sorrel','Sharp, lemony leaves used in soups, sauces and salads.',''),
 ('Curry leaf','Glossy aromatic leaves of Murraya koenigii, fried at the start of South Indian cooking.',''),
 ('Makrut lime leaf','Double-lobed fragrant citrus leaves for Thai and Southeast Asian cooking.','kaffir lime leaf'),
 ('Pandan','Long, sweet-scented screwpine leaves used to flavour rice and desserts.','screwpine'),
 ('Vietnamese coriander','Peppery, coriander-like leaves (Persicaria odorata) used in Southeast Asian dishes.','laksa leaf'),
 ('Epazote','Pungent Mexican herb used with beans.',''),
 ('Culantro','Long serrated leaves with a strong coriander taste, used in Caribbean and Latin American cooking.','')]:
    new(n,dd,HB,a=a)

# ---- types (tt) by hand
T=tt
T('Apple',[['Use',['Dessert','Cooking','Dual-purpose']],['Skin',['Smooth','Russet']]])
T('Pear',[['Use',['Dessert','Perry and cooking']],['Origin',['European','Asian-hybrid']]])
T('Peach',[['Flesh colour',['Yellow','White']],['Stone',['Clingstone','Freestone']],['Shape',['Round','Flat']]])
T('Nectarine',[['Flesh colour',['Yellow','White']],['Stone',['Clingstone','Freestone']]])
T('Cherry',[['Taste',['Sweet']],['Skin colour',['Dark red','Yellow-blush']]])
T('Plum',[['Group',['European','Japanese','Greengage','Damson','Mirabelle','Interspecific hybrid']]])
T('Orange',[['Group',['Navel','Valencia','Common']],['Use',['Eating','Juicing']]])
T('Mandarin',[['Group',['True mandarin','Tangor','Tangelo']]])
T('Lime',[['Group',['Persian','Key','Makrut']]])
T('Japanese aromatic citrus',[['Fruit',['Yuzu','Sudachi','Kabosu']]])
T('Strawberry',[['Fruiting habit',['June-bearing','Everbearing','Day-neutral']],['Fruit',['Garden','Alpine or wild','White']]])
T('Blueberry',[['Plant',['Highbush','Rabbiteye','Lowbush']],['Pack',['Single berry','Mixed berry pack']]])
T('Raspberry',[['Fruit colour',['Red','Golden','Black']],['Fruiting season',['Summer-bearing','Autumn-fruiting']]])
T('Blackberry',[['Canes',['Thorned','Thornless','Trailing hybrid']]])
T('Table grape',[['Seeds',['Seedless','Seeded']],['Skin colour',['White','Red','Black']]])
T('Kiwifruit',[['Flesh colour',['Green','Gold','Red']]])
T('Melon',[['Rind',['Netted','Smooth']],['Flesh colour',['Orange','Green','White']]])
T('Watermelon',[['Seeds',['Seeded','Seedless']],['Size',['Standard','Mini']],['Flesh colour',['Red','Yellow']]])
T('Mango',[['Ripeness',['Ripe for eating','Green for pickling']]])
T('Banana',[['Group',['Cavendish','Dessert','Red','Apple']]])
T('Papaya',[['Ripeness',['Ripe','Green']],['Flesh colour',['Red','Yellow']]])
T('Coconut',[['Maturity',['Young','Mature']]])
T('Jackfruit',[['Maturity',['Young green','Ripe']],['Flesh',['Soft-bulb','Firm-bulb']]])
T('Dragon fruit',[['Flesh colour',['White','Red','Yellow']]])
T('Passion fruit',[['Skin colour',['Purple','Yellow']],['Species',['Passion fruit','Granadilla']]])
T('Carambola',[['Taste',['Sweet','Sour']]])
T('Star apple',[['Skin colour',['Purple','Greenish-brown','Yellow']]])
T('Date',[['Ripeness',['Khalal','Rutab','Tamar']],['Texture',['Fresh soft','Dried']]])
T('Persimmon',[['Astringency',['Astringent','Non-astringent']]])
T('Pomegranate',[['Form',['Whole','Arils']]])
T('Tamarillo',[['Skin colour',['Red','Yellow']]])
T('Fruit gift box',[['Presentation',['Japanese gift fruit','Western fruit basket','Mixed fruit pack']]])
T('Potato',[['Texture',['Waxy','Floury','All-rounder']],['Harvest',['New or early','Maincrop']],['Size',['Standard','Salad or fingerling']]])
T('Sweet potato',[['Flesh colour',['Orange','White','Purple']]])
T('Cassava',[['Cyanide content',['Sweet','Bitter']]])
T('Taro',[['Corm',['Large central corm','Small side corm (eddoe)']]])
T('Radish',[['Size',['Small salad','Large winter']]])
T('Salsify',[['Skin colour',['Pale (salsify)','Black (scorzonera)']]])
T('Maca',[['Root colour',['Cream-yellow','Purple','Black']]])
T('Ginger',[['Maturity',['Young','Mature']]])
T('Galangal',[['Species',['Greater','Lesser']]])
T('Bulb onion',[['Skin colour',['Yellow','Red','White']],['Taste',['Standard','Sweet']]])
T('Garlic',[['Stem',['Hardneck','Softneck']],['Stage',['Cured dry bulb','Green (wet) garlic']]])
T('Leek',[['Season',['Summer','Overwintering']]])
T('Tomato',[['Size and shape',['Cherry','Grape','Plum','Round or salad','Beefsteak']],['Presentation',['Loose','On the vine']],['Breeding',['Hybrid','Heirloom']]])
T('Sweet pepper',[['Shape',['Blocky bell','Pointed','Frying','Mini']]])
T('Chilli',[['Species',['Capsicum annuum','Capsicum chinense','Capsicum baccatum','Capsicum frutescens','Capsicum pubescens']]])
T('Avocado',[['Skin',['Dark pebbled (Hass-type)','Green smooth']],['Origin race',['Mexican and Guatemalan','West Indian']],['Seed',['Stoned','Stoneless cocktail']]])
T('Okra',[['Pod colour',['Green','Red']]])
T('Fresh olive',[['Ripeness',['Green','Semi-ripe','Black']]])
T('Cucumber',[['Use',['Slicing','Pickling']],['Size',['Standard','Mini']],['Origin',['European','Asian']]])
T('Courgette',[['Colour',['Green','Yellow']],['Shape',['Long','Round']],['Stage',['Fruit','Flowers']]])
T('Pumpkin & winter squash',[['Species',['Cucurbita maxima','Cucurbita moschata','Cucurbita pepo']]])
T('Bitter melon',[['Type',['Chinese','Indian','Miniature']]])
T('Cabbage',[['Head shape',['Round','Pointed','Flat']],['Colour',['White or green','Red']],['Leaf',['Smooth','Savoyed']],['Season',['Spring greens','Summer','Winter']]])
T('Broccoli',[['Form',['Calabrese head','Sprouting','Long-stemmed (tenderstem)']]])
T('Cauliflower',[['Curd colour',['White','Orange','Green','Purple']]])
T('Pak choi',[['Size',['Baby','Full-size']],['Stem colour',['White','Green']]])
T('Gai lan',[['Size',['Baby','Full-size']]])
T('Spinach',[['Leaf',['Flat','Savoyed']],['Sold as',['Baby leaf','Bunched']]])
T('Pea',[['Pod eaten',['Shelled (garden pea)','Whole flat (mangetout)','Whole round (sugar snap)']]])
T('Green bean',[['Pod',['Round (French)','Flat (runner, Romano)','Very long (yardlong)']]])
T('Sweetcorn',[['Sugar gene',['su','se','sh2 supersweet']],['Kernel colour',['Yellow','White','Bicolour']],['Stage',['Full cob','Baby corn']]])
T('Asparagus',[['Colour',['Green','White','Purple']],['Source',['Cultivated','Wild']]])
T('Celery',[['Blanching',['Self-blanching','Trenched']]])
T('Rhubarb',[['Growing',['Forced','Field-grown']]])
T('Wild shoots & fiddleheads',[['Shoot',['Warabi','Kogomi','Taranome','Ostrich fern']]])
T('Lettuce',[['Head type',['Crisphead','Cos or romaine','Butterhead','Batavia','Loose-leaf']],['Sold as',['Cut head','Living lettuce']]])
T('Chicory',[['Form',['Radicchio','Witloof','Endive or frisée','Escarole','Puntarelle']]])
T('Rocket',[['Species',['Salad rocket','Wild rocket']]])
T('Mixed salad leaves',[['Pack',['Mixed leaves','Mixed vegetable pack','Crudité tray']]])
T('Sprouts & microgreens',[['Crop',['Bean sprouts','Alfalfa','Cress','Microgreens']]])
T('Parsley',[['Leaf',['Flat-leaf','Curly']]])
T('Mint',[['Species',['Spearmint','Peppermint','Other mints']]])
T('Oregano & marjoram',[['Species',['Greek oregano','Sweet marjoram','Turkish marjoram']]])
T('Tarragon',[['Type',['French','Russian','Mexican (Tagetes lucida)']]])
T('Lemongrass',[['Species',['West Indian (C. citratus)','East Indian (C. flexuosus)']]])
T('Perilla',[['Leaf',['Green shiso','Red shiso','Kkaennip']]])
T('Basil',[['Leaf colour',['Green','Purple']],['Scent',['Sweet','Lemon','Clove','Anise']]])
T('Button mushroom',[['Maturity',['White button','Chestnut or cremini','Portobello']]])
T('Shiitake',[['Harvest',['Donko (early, thick cap)','Koshin (later, flat cap)']]])
T('Oyster mushroom',[['Colour',['Grey','Pink','Golden']]])
T('Shimeji',[['Colour',['Brown (buna)','White (bunapi)']]])
T('Truffle',[['Grade',['By size','By aroma']]])
T('Matsutake',[['Origin',['Japan','Jilin, China']]])
T('Chanterelle',[['Species',['Golden','Trumpet or yellowfoot']]])
T('Morel',[['Colour',['Black','Yellow']]])
T('Wakame',[['Preservation',['Fresh','Salted','Dried']]])
T('Nori',[['Form',['Fresh','Toasted sheet','Seasoned snack sheet']]])
T('Kombu',[['Use',['Stock','Eating']]])
T('Cherimoya',[['Skin',['Smooth','Scaly']]])
T('Soursop',[['Shape',['Round','Heart-shaped']]])
T('Prickly pear',[['Skin colour',['Green','Red','Yellow']]])
T('Jackfruit',K['Jackfruit']['tt'])

# ---- layout
def shelf(n,t,ax,names):
    s={'n':n,'t':t,'k':[K[x] for x in names]}
    if len(names)>3 and ax: s['ax']=ax
    return s
FRB=d['depts'][0]['b']; VGB=d['depts'][1]['b']
depts=[]
def dept(n,mode,t,ax,b,shelves,note=None):
    D={'n':n,'mode':mode,'t':t,'ax':ax,'b':copy.deepcopy(b),'s':shelves}
    if note: D['note']=note
    depts.append(D)
fnote=d['depts'][0].get('note')
dept('Temperate fruit','variety','Fruit of orchard, bush, cane and vine in cool and warm-temperate climates, sold by cultivar; sweet citrus → Citrus, warm-climate fruit → Tropical & subtropical fruit.',
 'Is it a pome or stone fruit on a tree, a berry on a bush or cane, or a vine fruit?',FRB,[
 shelf('Pome fruit','Tree fruit with a core of small seeds: apples, pears and their rarer relatives; stone-hard fruit such as cherries → Stone fruit.','kinds from everyday apple and pear to rarer pomes',['Apple','Pear','Asian pear','Quince','Loquat','Medlar','Hawthorn fruit']),
 shelf('Stone fruit','Tree fruit with one hard stone: peaches, plums, cherries and apricots; a fruit with a core → Pome fruit.','kinds by fruit type: peach family, apricot, plum, cherry, ume',['Peach','Nectarine','Apricot','Plum','Cherry','Sour cherry','Ume']),
 shelf('Soft fruit','Small juicy fruit on canes, bushes or low plants, such as strawberries, raspberries and currants; grapes → Grapes, kiwifruit & melons.','kinds by plant family: strawberry, cane berries, heath berries, currants, wild and northern berries',['Strawberry','Raspberry','Blackberry','Mulberry','Blueberry','Bilberry','Cranberry','Lingonberry','Blackcurrant','Redcurrant & white currant','Gooseberry','Elderberry','Cloudberry','Sea buckthorn']),
 shelf('Grapes, kiwifruit & melons','Sweet fruit of vines and trailing plants: table grapes, kiwifruit and the melon family; wine grapes → wine categories.','kinds by plant: grape and kiwi vines, then melon-family fruit',['Table grape','Kiwifruit','Kiwiberry','Melon','Watermelon','Kiwano']),
],note=fnote)
dept('Citrus','variety','Fruit of the genus Citrus sold fresh; the sweet segmented kinds to eat and the sour or aromatic kinds for juice, zest and scent.',
 'Is it eaten as sweet segments, or used sour and aromatic for juice, zest and flavour?',FRB,[
 shelf('Oranges, mandarins & grapefruit','Sweet citrus eaten in segments or juiced: oranges, mandarins and grapefruit; sour lemons and limes → Lemons, limes & aromatic citrus.','kinds from orange through the mandarin group to grapefruit and pomelo',['Orange','Blood orange','Mandarin','Clementine','Satsuma','Grapefruit','Pomelo']),
 shelf('Lemons, limes & aromatic citrus','Sour or fragrant citrus used for juice, zest and flavour: lemons, limes, yuzu, bergamot; sweet citrus → Oranges, mandarins & grapefruit.','kinds by use: juice and zest, flavouring fruit, ornamental curiosities',['Lemon','Lime','Calamansi','Bitter orange','Japanese aromatic citrus','Kumquat','Citron','Finger lime']),
])
dept('Tropical & subtropical fruit','variety','Fruit of warm climates sold fresh, grouped by where the plant comes from; temperate fruit → Temperate fruit, citrus → Citrus.',
 'Which region is the fruit from: world-traded staples, South-East Asia, India, the Americas, the Andes, or the warm-temperate belt?',FRB,[
 shelf('World-traded tropical fruit','The tropical fruits shipped worldwide in volume: bananas, pineapples, mangoes, papayas and coconuts.','kinds by plant: banana family, pineapple, then tree fruit',['Banana','Plantain','Pineapple','Mango','Papaya','Coconut']),
 shelf('South-East Asian fruit','Fruit of South-East Asia and southern China: lychee family, durian, jackfruit relatives and their neighbours; Indian fruits → Indian subcontinent fruit.','kinds by plant family: lychee family, durian and mangosteen, jackfruit family, then others',['Litchi','Longan','Rambutan','Durian','Mangosteen','Jackfruit','Cempedak','Breadfruit','Salak','Carambola','Langsat','Wax apple','Marian plum']),
 shelf('Indian subcontinent fruit','Fruit of India and its neighbours sold fresh: jamun, amla, bael and tamarind; mango → World-traded tropical fruit.','kinds from table fruit to sour fruit used in cooking',['Jamun','Amla','Karonda','Bael','Tamarind']),
 shelf('Annonas','Fruit of the custard-apple family with sweet, creamy flesh: cherimoya, sugar apple, atemoya, soursop and pawpaw.','kinds from cool-growing to hot-climate annonas',['Cherimoya','Atemoya','Sugar apple','Soursop','Pawpaw']),
 shelf('Andean & highland fruit','Fruit of the Andes and South American highlands, often sharp-flavoured: feijoa, tamarillo, physalis and relatives.','kinds by plant family: myrtle, nightshade, papaya relatives',['Feijoa','Tamarillo','Physalis','Pepino','Naranjilla','Babaco']),
 shelf('Tropical American fruit','Fruit of lowland tropical America: dragon fruit, passion fruit, guava, sapote and their relatives.','kinds by plant family: cactus, passion flower, myrtle, sapote',['Dragon fruit','Passion fruit','Guava','Acerola','Jaboticaba','Sapodilla','Star apple','Mamey sapote']),
 shelf('Warm-temperate & desert fruit','Fruit of dry, warm regions from the Mediterranean to East Asia: figs, dates, persimmons, pomegranates, prickly pears and jujubes.','kinds from Mediterranean staples to East Asian and desert fruit',['Fig','Date','Pomegranate','Persimmon','Prickly pear','Jujube']),
])
dept('Fruit gifts','variety','Fruit sold boxed or arranged as a gift; the fruit itself → the crop on its own shelf.',
 'How is the fruit presented: a single premium fruit, a box or a basket?',FRB,[
 shelf('Gift boxes & baskets','Fruit presented as a gift: Japanese premium fruit boxes and Western baskets; a single fruit sold loose → its crop shelf.','',['Fruit gift box']),
])
dept('Roots, tubers & bulbs','variety','Vegetables that grow underground: starchy tubers, root vegetables, pungent rhizomes and bulbs; salad radish counts here, leaf crops → Brassicas, leaves & stems.',
 'Is it a starchy tuber, a root eaten as a vegetable, a pungent rhizome or a bulb?',VGB,[
 shelf('Potatoes, sweet potatoes & starchy roots','Starchy tubers and roots eaten as a staple: potatoes, sweet potatoes, cassava, yams and taro; a salad root → Root vegetables.','kinds by plant family: potatoes, sweet potatoes, tropical starch roots, Andean tubers, water plants',['Potato','Sweet potato','Cassava','Yam','Taro','Jicama','Jerusalem artichoke','Oca','Yacón','Lotus root','Water chestnut','Arrowhead','Chinese artichoke']),
 shelf('Root vegetables','Roots grown for boiling, roasting and salads: carrots, beetroot, radishes, parsnips and swedes; starchy staples → Potatoes, sweet potatoes & starchy roots.','kinds from everyday orange and red roots to white, celery-family and medicinal roots',['Carrot','Beetroot','Radish','Parsnip','Turnip','Swede','Celeriac','Parsley root','Salsify','Burdock','Maca']),
 shelf('Ginger, wasabi & pungent roots','Hot or aromatic rhizomes and roots grated or sliced fresh: ginger, wasabi, horseradish, turmeric, galangal; dried spices → J5.','kinds by flavour family: ginger relatives, mustard-family roots',['Ginger','Fresh turmeric','Galangal','Fresh wasabi','Horseradish']),
 shelf('Onions, leeks & garlic','Bulb and stem alliums: onions, shallots, garlic, leeks and spring onions; chives and wild garlic leaves are here too.','kinds from dry bulbs to green and wild alliums',['Bulb onion','Shallot','Garlic','Leek','Spring onion','Welsh onion','Garlic chive','Wild garlic','Rakkyo']),
])
dept('Fruiting vegetables & pods','variety','Vegetables that are the fruit, pod or seed of the plant: tomatoes, peppers, squashes, beans and sweetcorn; sweet dessert fruit → fruit departments.',
 'Which plant family is it: nightshade, gourd, legume or grass, or another?',VGB,[
 shelf('Nightshade vegetables','Fruit of the nightshade family eaten as vegetables: tomatoes, peppers, chillies and aubergines; potatoes → Roots, tubers & bulbs.','kinds from tomato and tomatillo to peppers, chillies and aubergine',['Tomato','Tomatillo','Sweet pepper','Chilli','Aubergine']),
 shelf('Cucumbers, squash & gourds','Fruit of the gourd family eaten as vegetables: cucumbers, courgettes, pumpkins and Asian gourds; sweet melons → Grapes, kiwifruit & melons.','kinds by eating stage: raw cucumbers, summer squash, winter squash, Asian gourds',['Cucumber','Cucamelon','Courgette','Pumpkin & winter squash','Bitter melon','Bottle gourd','Snake gourd','Wax gourd','Luffa','Chayote']),
 shelf('Peas, beans & sweetcorn','Seeds and pods eaten fresh and green: peas, beans, edamame and sweetcorn; dried pulses → J5.','kinds by what is eaten: whole pod, shelled seed, cob',['Pea','Green bean','Winged bean','Drumstick','Broad bean','Shelling bean','Edamame','Sweetcorn']),
 shelf('Avocado, okra & olive','Other savoury fruit sold with vegetables: avocados, okra and fresh olives.','',['Avocado','Okra','Fresh olive']),
])
dept('Brassicas, leaves & stems','variety','Cabbage-family crops, cooked leafy greens and stem vegetables; raw salad leaves → Salad & herbs.',
 'Is it a brassica, another cooked leaf, or a stem or shoot?',VGB,[
 shelf('Cabbages & brassicas','The cabbage family: headed cabbages, flower heads, sprouts, leafy brassicas and kohlrabi; spinach and chard → Spinach & leafy greens.','kinds by the part eaten: head, flower, bud, leaf, swollen stem',['Cabbage','Chinese cabbage','Broccoli','Cauliflower','Brussels sprout','Kale','Collard greens','Cime di rapa','Pak choi','Gai lan','Komatsuna','Mustard greens','Tatsoi','Kohlrabi']),
 shelf('Spinach & leafy greens','Cooked and sometimes raw leaves outside the cabbage family: spinach, chard, amaranth and water spinach; brassica leaves → Cabbages & brassicas.','kinds from temperate to tropical and wild leaves',['Spinach','Chard','Amaranth greens','Water spinach','Malabar spinach','Purslane','Dandelion greens','Garland chrysanthemum','Water dropwort']),
 shelf('Asparagus, artichokes & stems','Shoots, stalks and buds eaten as vegetables: asparagus, artichokes, celery, rhubarb and bamboo shoots.','kinds by part eaten: spears, buds, stalks, shoots and flowers',['Asparagus','Globe artichoke','Cardoon','Celery','Celtuce','Florence fennel','Rhubarb','Bamboo shoot','Wild shoots & fiddleheads','Nopal','Banana blossom','Heart of palm']),
])
dept('Salad & herbs','mixed','Leaves eaten raw in salads and fresh herbs used to flavour; cooked greens → Brassicas, leaves & stems, dried herbs → J5.',
 'Is it eaten as a salad leaf, or used in small amounts to flavour food?',d['depts'][2]['b'],[
 shelf('Salad leaves & sprouts','Leaves, sprouts and mixes eaten raw: lettuces, chicories, rocket and cress; herbs → Fresh herbs.','kinds by taste: mild heads, bitter chicories, peppery leaves, mild small leaves, mixes, sprouts',['Lettuce','Chicory','Rocket','Watercress','Mizuna','Lamb\'s lettuce','Mixed salad leaves','Sprouts & microgreens']),
 shelf('Soft-leaved herbs','Tender herbs added fresh at the end of cooking or served raw: basil, coriander, parsley, mint, dill and chives; potted plants → C3.','kinds from the everyday to the delicate and sour-leaved',['Basil','Coriander','Parsley','Mint','Dill','Chives','Chervil','Tarragon','Lovage','Lemon balm','Sorrel','Mixed herbs']),
 shelf('Woody herbs','Sturdy, resinous herbs that stand up to long cooking: thyme, rosemary, sage and oregano; potted plants → C3.','kinds from thyme and rosemary to sage and oregano',['Thyme','Rosemary','Sage','Oregano & marjoram']),
 shelf('Asian & Latin American herbs','Herbs of Asian and Latin American cooking: lemongrass, shiso, curry leaf, pandan, culantro and epazote.','kinds by cuisine: South and Southeast Asian, East Asian, Latin American',['Lemongrass','Curry leaf','Makrut lime leaf','Pandan','Vietnamese coriander','Perilla','Culantro','Epazote']),
])
dept('Mushrooms & sea vegetables','variety','Fungi and seaweeds sold to eat: farmed mushrooms, foraged mushrooms and truffles, and sea vegetables; dried and preserved forms → J5.',
 'Is it farmed, foraged in the wild, or taken from the sea or shore?',d['depts'][3]['b'],[
 shelf('Cultivated mushrooms','Mushrooms grown on farms and sold fresh: button, shiitake, oyster, enoki, maitake and other speciality kinds.','kinds by form: classic caps, clustered mushrooms, jelly and straw mushrooms',['Button mushroom','Shiitake','Oyster mushroom','King oyster mushroom','Enoki','Shimeji','Maitake','Lion\'s mane','Wood ear','Straw mushroom']),
 shelf('Wild mushrooms & truffles','Mushrooms and truffles gathered, not farmed: truffles, matsutake, porcini, chanterelles, morels; farmed mushrooms → Cultivated mushrooms.','kinds by where they are found: underground, under pines, in woods, in meadows',['Truffle','Matsutake','Porcini','Chanterelle','Morel','Giant puffball']),
 shelf('Sea vegetables','Seaweeds and shore plants eaten fresh, salted or dried; grouped by colour of the weed.','kinds by group: brown, red and green seaweeds, then shore plants',['Wakame','Kombu','Arame','Hijiki','Mozuku','Nori','Dulse','Irish moss','Sea lettuce','Sea grapes','Samphire']),
])
d['depts']=depts
d['ax']='What part of which plant or fungus is it: a tree or vine fruit, citrus, a tropical fruit, an underground vegetable, a fruiting or pod vegetable, a leaf or stem, a salad leaf or herb, or a mushroom or seaweed?'
d['key']=['1. Is it a boxed or arranged gift of fruit? → Fruit gifts',
 '2. Is it a mushroom, truffle or seaweed? → Mushrooms & sea vegetables',
 '3. Is it a salad leaf, sprout or a herb used to flavour? → Salad & herbs',
 '4. Is it a citrus fruit? → Citrus',
 '5. Is it a sweet fruit from a warm climate (banana, mango, lychee, fig, date)? → Tropical & subtropical fruit',
 '6. Is it a sweet fruit of orchard, bush, cane or vine, including melon? → Temperate fruit',
 '7. Does it grow underground, or is it an onion, garlic or leek? → Roots, tubers & bulbs',
 '8. Is it a tomato, pepper, gourd, bean, pea, sweetcorn, avocado or okra? → Fruiting vegetables & pods',
 '9. Is it a cabbage-family crop, a cooked leaf, or a stem or shoot? → Brassicas, leaves & stems',
 '<i>Precedence: a salad radish is a root (step 7); an avocado, tomato and olive are eaten as vegetables (step 8) though botanically fruit; rhubarb is a stem (step 9) though cooked as fruit.</i>']
d['lead']='Fresh fruit, vegetables, salad, herbs, mushrooms and sea vegetables as sold to eat, organised by crop group and species, then named cultivar, then origin (PDO/PGI/GI), club brand or breeder code, with marketing grades attached.'

# ---- see links
def see(n,*items):
    K[n].setdefault('see',[]).extend([list(i) for i in items])
see('Prickly pear',('C3','Prickly pear','the plant sold for growing'))
see('Rosemary',('C3','Rosemary','the plant sold for growing'))
see('Thyme',('C3','Thyme','the plant sold for growing'))
see('Arrowhead',('E4','Arrowhead','the arrow tip, a different object'))
see('Horseradish',('J5','Horseradish','prepared sauce'))
see('Plantain',('J4','Banana','the sweet dessert relative'))
see('Banana',('J4','Plantain','the cooking relative'))
see('Sweet pepper',('J4','Chilli','the hot relative'))
see('Chilli',('J4','Sweet pepper','the mild relative'))
see('Cherry',('J4','Sour cherry','the tart cherry'))
see('Sour cherry',('J4','Cherry','the sweet cherry'))
see('Fresh wasabi',('J4','Horseradish','the common substitute'))
see('Horseradish',('J4','Fresh wasabi','the Japanese root'))
see('Spring onion',('J4','Welsh onion','the bunching onion'))
see('Welsh onion',('J4','Spring onion','the young green onion'))
see('Kale',('J4','Collard greens','the closest leafy cabbage'))
see('Collard greens',('J4','Kale','the closest leafy cabbage'))
see('Pak choi',('J4','Gai lan','another Chinese brassica'))
see('Edamame',('J4','Shelling bean','seed eaten fresh from the pod'))
see('Taro',('J4','Yam','confused starchy root'))
see('Yam',('J4','Taro','confused starchy root'))
see('Apricot',('J4','Ume','closest relative'))
see('Ume',('J4','Apricot','closest relative'))
see('Pomelo',('J4','Grapefruit','pomelo is its parent'))
see('Bitter orange',('J4','Orange','sweet relative'))
see('Cauliflower',('J4','Broccoli','closest brassica'))
see('Broccoli',('J4','Cauliflower','closest brassica'))
see('Wild garlic',('J4','Garlic chive','other leafy allium'))
see('Perilla',('J4','Mint','same plant family'))
see('Kiwano',('J4','Cucumber','related gourd family'))
see('Cucamelon',('J4','Cucumber','larger relative'))
see('Water chestnut',('J4','Lotus root','another water plant'))
see('Tamarind',('J4','Jujube','another sour-sweet fruit eaten fresh') ) if False else None
see('Sea grapes',('J4','Wakame','another sea vegetable'))
see('Samphire',('J4','Sea grapes','shore or sea plant eaten raw'))
see('Matsutake',('J4','Porcini','other prized wild mushroom'))
see('Porcini',('J4','Matsutake','other prized wild mushroom'))
see('Truffle',('J4','Porcini','other prized wild fungus'))

see('Shiitake',('J5','Dried mushrooms','the dried form'))
see('Wakame',('J5','Dried seaweed','the dried form'))
see('Kombu',('J5','Dried seaweed','the dried form'))
see('Nori',('J5','Dried seaweed','the dried form'))
# ---- verify no kind lost
allk=[k['n'] for D in depts for S in D['s'] for k in S['k']]
assert len(allk)==len(set(allk)),[n for n in allk if allk.count(n)>1]
old={k['n'] for D in json.load(open(SRC))['depts'] for S in D['s'] for k in S['k']}
ren={'Custard apple':'Cherimoya','Speciality cultivated mushrooms':'Shimeji'}
miss=[n for n in old if n not in allk and n not in ren]
print('missing',miss,'count',len(allk),'old',len(old))
for k in K.values():
    if 'tt' in k: k.pop('t',None)
json.dump(d,open('work/STR_J4/J4.new.json','w'),ensure_ascii=False,indent=1)
json.dump(ren,open('work/STR_J4/renames.json','w'),ensure_ascii=False,indent=1)
