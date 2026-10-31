import json, copy, os
R='/home/user/Possession-Taxonomy/rebuild/'
d=json.load(open(R+'work/STR_J9/bak/J9.json'))
K={}
for dp in d['depts']:
    for s in dp['s']:
        for k in s['k']:
            K[k['n']]=k
renames={}
def arch(kn,an):
    k=K[kn]
    for i,a in enumerate(k.get('x',[])):
        if a['n']==an:
            return k['x'].pop(i)
    raise KeyError((kn,an))
def addm(kn,pairs):
    K[kn].setdefault('m',[])
    for p in pairs:
        if p not in K[kn]['m']: K[kn]['m'].append(p)
def addr(kn,pairs):
    K[kn].setdefault('r',[])
    for p in pairs:
        if p not in K[kn]['r']: K[kn]['r'].append(p)
def move_arch(src,an,dst):
    a=arch(src,an); K[dst].setdefault('x',[]).append(a); return a
def newkind(n,d_,s,a='',tt=None):
    K[n]={'n':n,'a':a,'d':d_,'s':s}
demoted=[]
# ---------- demotions: generic archetypes -> models / ranges / types
a=arch('Ginger ale','Golden ginger ale'); demoted.append('Golden ginger ale (to type Style; Vernors kept as archetype)')
a=arch('Fruit soda','Grape soda'); demoted.append('Grape soda')
addm('Fruit soda',[['Fanta Grape','Fanta'],['Crush Grape','Crush'],['Grapette','Grapette'],['NuGrape','NuGrape'],['Grapico','Grapico']])
a=arch('Fruit soda','Crush fruit flavours'); demoted.append('Crush fruit flavours (range)')
addr('Fruit soda',[['Crush fruit sodas','Crush']])
addm('Fruit soda',[['Crush '+v['n'],'Crush'] for v in a['v']])
a=arch('Fruit soda','Fanta flavours'); demoted.append('Fanta flavours (range)')
addr('Fruit soda',[['Fanta flavours','Fanta']])
addm('Fruit soda',[[v['n'],'Fanta'] for v in a['v']])
a=arch('Cream soda','Vanilla cream soda'); demoted.append('Vanilla cream soda')
addm('Cream soda',[['A&W Cream Soda','A&W'],["Barq's French Vanilla Crème","Barq's"]])
a=arch('Cream soda','Red / pink cream soda'); demoted.append('Red / pink cream soda')
addm('Cream soda',[["Barq's Red Crème Soda","Barq's"],['Crush Cream Soda','Crush']])
a=arch('Root beer & birch beer','Birch beer'); demoted.append('Birch beer (to types)')
a=arch('Herbal & sarsaparilla soda','Sarsaparilla'); demoted.append('Sarsaparilla')
addm('Herbal & sarsaparilla soda',[['Badak','Badak'],['Sarsi','Sarsi'],['HeySong Sarsaparilla','HeySong'],['F&N Sarsi','F&N'],['Bundaberg Sarsaparilla','Bundaberg']])
a=arch('Herbal & sarsaparilla soda','Dandelion & Burdock'); demoted.append('Dandelion & Burdock')
addm('Herbal & sarsaparilla soda',[['Fentimans Dandelion & Burdock','Fentimans']])
a=arch('Juice spritzer (Schorle)','Apfelschorle'); demoted.append('Apfelschorle (to type)')
a=arch('Cocktail mix','Sour mix'); demoted.append('Sour mix (to type)')
a=arch('Bottled green & oolong tea','Canned oolong tea'); demoted.append('Canned oolong tea')
addm('Bottled green & oolong tea',[['Suntory Oolong tea','ITO EN'] if False else ['Canned oolong tea','ITO EN']])
a=arch('Fruit syrup (sirop)','Teisseire sirop'); demoted.append('Teisseire sirop (range)')
addr('Fruit syrup (sirop)',[['Teisseire sirop','Teisseire']])
a=arch('Fruit syrup (sirop)','Monin sirop'); demoted.append('Monin sirop (range)')
addr('Fruit syrup (sirop)',[['Monin sirop','Monin']])
a=arch('Café & flavouring syrup','Torani syrup'); demoted.append('Torani syrup (range)')
addr('Café & flavouring syrup',[['Torani syrup','Torani']])
a=arch('Café & flavouring syrup','Monin coffee syrup'); demoted.append('Monin coffee syrup (range)')
addr('Café & flavouring syrup',[['Monin coffee syrups','Monin']])
a=arch('Soda-maker syrup','SodaStream syrups'); demoted.append('SodaStream syrups (range)')
addr('Soda-maker syrup',[['SodaStream syrups','SodaStream']])
addm('Soda-maker syrup',[['SodaStream '+v['n'],'SodaStream'] for v in a['v']])
a=arch('Flavoured sparkling water','Perrier flavoured'); demoted.append('Perrier flavoured (range)')
addr('Flavoured sparkling water',[['Perrier flavoured','Perrier']])
addm('Flavoured sparkling water',[['Perrier '+v['n'],'Perrier'] for v in a['v']])
a=arch('Craft & prebiotic soda','Bundaberg brewed soft drinks'); demoted.append('Bundaberg brewed soft drinks (range, moved to Fruit soda)')
addr('Fruit soda',[['Bundaberg brewed soft drinks','Bundaberg']])
addm('Fruit soda',[['Bundaberg '+v['n'],'Bundaberg'] for v in a['v']])
a=arch('Guaraná soda','Fanta Guaraná'); demoted.append('Fanta Guaraná')
addm('Guaraná soda',[['Fanta Guaraná','Fanta']])
a=arch('Mexican & Latin American soda','Manzana Postobón'); K['Mexican & Latin American soda'].setdefault('_hold',[]).append(a)

# ---------- reassign archetypes between kinds
move_arch('Cordial-based soda','Tango','Orange soda')
move_arch('Cordial-based soda','Sinalco','Orange soda')
move_arch('Cordial-based soda','Ting','Citrus soda')
move_arch('Mexican & Latin American soda','Mirinda','Orange soda')
move_arch('Mexican & Latin American soda','Jarritos','Fruit soda')
sid=arch('Mexican & Latin American soda','Sidral Mundet')
newkind('Cherry soda','Cherry-flavoured fizzy drink, sold as cherryade or as a regional brand.','https://en.wikipedia.org/wiki/Soft_drink')
K['Cherry soda']['x']=[arch('Cordial-based soda','Cheerwine')]
newkind('Apple soda','Fizzy apple-flavoured drink, popular in Mexico and Colombia.',sid['s'])
K['Apple soda']['x']=[sid,K['Mexican & Latin American soda']['_hold'][0]]
K['Apple soda']['x'][0],K['Apple soda']['x'][1]=K['Apple soda']['x'][0],K['Apple soda']['x'][1]
# fold Mexican kind into Fruit soda
fs=K['Fruit soda']; mx=K['Mexican & Latin American soda']
renames['Mexican & Latin American soda']='Fruit soda'
renames['Cordial-based soda']='Mixed-fruit soda'
renames['Craft & prebiotic soda']='Prebiotic & functional soda'
K['Mixed-fruit soda']=K.pop('Cordial-based soda'); K['Mixed-fruit soda']['n']='Mixed-fruit soda'
K['Mixed-fruit soda']['a']='mixed fruit soda · multivitamin soda'
K['Mixed-fruit soda']['d']='Fizzy drink of several fruit flavours blended into one signature taste, such as Vimto.'
K['Prebiotic & functional soda']=K.pop('Craft & prebiotic soda'); K['Prebiotic & functional soda']['n']='Prebiotic & functional soda'
K['Prebiotic & functional soda']['d']='Low-sugar fizzy drinks sold for fibre, vinegar or live cultures, such as Olipop, Poppi and Bionade.'
K['Fruit soda']['d']='Fizzy drink flavoured with a single fruit other than citrus or cherry, such as grape, strawberry, tamarind or guava.'
K['Fruit soda']['a']='fruit-flavoured soda · Mexican fruit soda · Latin American soda'
for n in list(K['Cola'].get('x',[])): pass
# Inca Kola cola model duplicates archetype in bubblegum kind: leave m
# new Grapefruit juice
newkind('Grapefruit & citrus juice','Pressed or reconstituted grapefruit, lemon, lime and mixed citrus juice sold as a single-fruit drink.','https://en.wikipedia.org/wiki/Juice')
newkind('Mageu','Thin sour maize drink fermented with a little wheat, sold in cartons across southern Africa.','https://en.wikipedia.org/wiki/Fermented_drink','mageu · magou · amahewu')
newkind('Kanji & vegetable ferments','Drinks soured from carrots, beetroot or turnips, such as Indian kanji and Turkish şalgam.','https://en.wikipedia.org/wiki/Fermented_drink','kanji · şalgam')
newkind('Orgeat','Almond-and-sugar syrup scented with orange-flower or rose water, used in tiki drinks and as a long-drink syrup.','https://en.wikipedia.org/wiki/Orgeat')
og=arch('Grenadine & cocktail syrup','Orgeat'); K['Orgeat']['s']=og['s']; K['Orgeat']['d']=og['d']; demoted.append('Orgeat (became its own kind)')
fa=arch('Grenadine & cocktail syrup','Falernum'); newkind('Falernum',fa['d'],fa['s'],'non-alcoholic falernum'); demoted.append('Falernum (became its own kind)')
gr=arch('Grenadine & cocktail syrup','Grenadine')
K['Grenadine']=K.pop('Grenadine & cocktail syrup'); K['Grenadine']['n']='Grenadine'
renames['Grenadine & cocktail syrup']='Grenadine'
K['Grenadine']['a']='pomegranate syrup · grenadine syrup'
K['Grenadine']['d']=gr['d']; demoted.append('Grenadine (became the kind itself; Rose\'s grenadine kept as model)')
K['Grenadine']['m']=[["Rose's grenadine","Rose's"]]
newkind('Simple & gomme syrup','Plain sugar syrup, thicker rich syrup or gum-arabic gomme syrup, sold for sweetening cold drinks and cocktails.','https://en.wikipedia.org/wiki/Simple_syrup','simple syrup · sugar syrup · gomme syrup · rich syrup')
K['Orgeat']['m']=[]; 
for n in ('Orgeat','Falernum','Simple & gomme syrup'): K[n]['m']=[]
# remove x emptiness
# ---------- tt by hand
TT={
'Natural mineral water':[['Mineral content',['Very low (under 50 mg/L)','Low','Medium','High','Very high (over 1,500 mg/L)']],['Dominant mineral',['Calcium-rich','Magnesium-rich','Sulphate-rich','Bicarbonate-rich','Low sodium']],['Container',['Glass bottle','PET bottle','Can','Multipack','Sports cap']]],
'Spring water':[['Container',['PET bottle','Glass bottle','Carton','Can']],['Size',['Single-serve','Gallon jug','3- and 5-gallon cooler jug']]],
'Artesian & glacier water':[['Source',['Artesian aquifer','Glacial or snowmelt']],['Container',['Square or cylindrical PET','Glass']]],
'Purified & table water':[['Treatment',['Reverse osmosis','Distilled','Remineralised']],['Container',['PET single-serve','Multipack','Gallon jug','Can','Refill station']]],
'Sparkling mineral water':[['Gas source',['Naturally sparkling','Source gas re-added','Added CO2']],['Bubble strength',['Fine or light','Medium','Intense or extra sparkling']],['Container',['Glass bottle','PET bottle','Can']]],
'Seltzer & carbonated water':[['Minerals',['Plain seltzer','Minerals added']],['Container',['Glass bottle','Can','PET bottle','Multipack']]],
'Flavoured still water':[['Sweetening',['Unsweetened','Sugar-free sweetener','With fruit juice']],['Additions',['Vitamins']]],
'Flavoured sparkling water':[['Flavouring',['Unsweetened essence','With fruit juice']],['Caffeine',['Caffeine-free','Caffeinated']],['Container',['Can','Bottle']]],
'Alkaline & functional water':[['Treatment',['High-pH or ionised','Vapour-distilled with electrolytes','Hydrogen-infused','Oxygenated']],['Additions',['Electrolytes','Fluoride (infant or nursery water)']]],
'Packaged ice':[['Form',['Cubed','Crushed','Block','Clear cocktail ice']]],
'Cola':[['Colour',['Brown','Clear']],['Flavouring',['Original','Cherry','Vanilla','Lime']],['Sweetening',['Sugar','Diet or zero']]],
'Pepper & spiced soda':[['Flavouring',['Original','Cherry','Cherry vanilla']],['Sweetening',['Sugar','Diet or zero']]],
'Cola-orange mix (Spezi)':[['Sweetening',['Sugar','Sugar-free']],['Container',['Glass bottle','PET bottle']]],
'Lemon-lime soda':[['Flavouring',['Original','Cherry','Cranberry']],['Sweetening',['Sugar','Diet or zero']]],
'Citrus soda':[['Fruit',['Grapefruit','Lemon','Tropical lime']],['Caffeine',['Caffeine-free','Caffeinated']]],
'Orange soda':[['Juice',['No juice','With juice','With pulp']],['Fruit',['Orange','Blood orange']]],
'Sparkling lemonade':[['Clarity',['Clear','Cloudy']],['Colour',['Clear','Red','Brown','White (Ireland)']],['Container',['Glass bottle','Can','PET bottle']]],
'Chinotto & bitter soda':[['Bitterness',['Bittersweet','Bitter aperitivo']],['Container',['Glass bottle','Can']]],
'Ramune & marble soda':[['Flavour',['Original lemon-lime','Fruit flavours']],['Bottle',['Glass Codd-neck','Plastic Codd-style']]],
'Fruit soda':[['Fruit',['Grape','Strawberry','Peach','Pineapple','Tropical','Tamarind','Guava']],['Sweetener',['Cane sugar','Corn syrup','Diet or zero']],['Container',['Glass bottle','PET bottle','Can']]],
'Cherry soda':[['Flavour',['Black cherry','Wild cherry','Cherryade']],['Sweetening',['Sugar','Diet or zero']]],
'Apple soda':[['Sweetener',['Cane sugar','Corn syrup']],['Container',['Glass bottle','PET bottle']]],
'Mixed-fruit soda':[['Sweetening',['Sugar','Diet or zero']],['Container',['Glass bottle','Can','PET bottle']]],
'Guaraná soda':[['Sweetening',['Regular','Diet or zero']],['Container',['Glass bottle','Can','PET bottle']]],
'Bubblegum & tutti-frutti soda':[['Colour',['Golden or yellow','Orange','Red']],['Sweetening',['Regular','Diet or zero']],['Container',['Glass bottle','Can','PET bottle']]],
'Root beer & birch beer':[['Base flavour',['Root beer (sassafras or sarsaparilla style)','Birch beer']],['Colour',['Brown','Red','White (clear)']]],
'Cream soda':[['Colour',['Clear or golden','Red or pink']],['Regional style',['US cream soda','Australian and New Zealand creaming soda']]],
'Herbal & sarsaparilla soda':[['Botanical',['Sarsaparilla','Gentian','Alpine herbs','Dandelion and burdock']],['Sweetening',['Regular','Diet or zero']],['Container',['Glass bottle','Can','PET bottle']]],
'Prebiotic & functional soda':[['Functional claim',['Prebiotic fibre','Apple cider vinegar','Botanically brewed','Fermented and organic']],['Sugar',['Low sugar','Standard']]],
'Tonic water':[['Style',['Indian (classic)','Light or slimline','Aromatic','Mediterranean','Floral (elderflower)','High-quinine']],['Container',['Glass bottle (150–200 ml)','Can','PET bottle','Multipack']]],
'Bitter lemon & citrus mixer':[['Fruit',['Bitter lemon','Bitter lime']],['Container',['Glass bottle (150–200 ml)','Can','PET bottle','Multipack']]],
'Ginger beer':[['Production',['Brewed','Carbonated']],['Heat',['Mild','Spiced']],['Sweetening',['Regular','Diet or zero']],['Container',['Glass bottle (150–200 ml)','Can','PET bottle']]],
'Ginger ale':[['Style',['Golden','Dry or pale dry']],['Sweetening',['Regular','Diet or zero']],['Container',['Glass bottle (150–200 ml)','Can','PET bottle']]],
'Soda water & club soda':[['Mineral content',['Soda water (plain)','Club soda (minerals added)']],['Container',['Glass bottle (150–200 ml)','Can','PET bottle']]],
'Cocktail mix':[['Cocktail',['Bloody Mary','Margarita','Sweet and sour','Mojito','Piña colada','Daiquiri']],['Form',['Liquid','Powder']]],
'Orange juice':[['Processing',['Not from concentrate','From concentrate','Freshly squeezed, unpasteurised','Frozen concentrate']],['Pulp',['With pulp','Smooth, no pulp']],['Variety',['Blood orange']],['Additions',['Calcium and vitamin D fortified','Low-acid','Organic']]],
'Apple juice':[['Clarity',['Clear','Cloudy or unfiltered']],['Processing',['From concentrate','Not from concentrate','US fresh apple cider']],['Variety',['Single-variety']],['Standard',['Organic']]],
'Grape juice':[['Grape',['Purple or red (Concord)','White (Niagara)']],['Form',['Still','Sparkling grape juice']],['Processing',['From concentrate','Not from concentrate']]],
'Cranberry & berry juice':[['Juice content',['Juice cocktail (25–27% cranberry)','100% juice blend']],['Berry',['Cranberry','White cranberry','Blackcurrant and other berries']],['Sweetening',['Sweetened','Light']]],
'Grapefruit & citrus juice':[['Fruit',['Grapefruit','Lemon','Lime','Mixed citrus']],['Colour',['White','Pink or ruby']],['Processing',['Not from concentrate','From concentrate']]],
'Tropical & exotic juice':[['Fruit',['Pineapple','Mango','Passion fruit','Guava','Lychee','Pomegranate','Multifruit']]],
'Tomato & vegetable juice':[['Base',['Plain tomato','Mixed vegetable','Carrot and beetroot','Clam-tomato (Clamato)']],['Seasoning',['Plain','Seasoned or spiced']],['Salt',['Standard','Low-sodium']]],
'Plant waters':[['Plant',['Coconut','Birch sap','Maple','Aloe vera','Cactus']],['Production',['Standard','Pressed coconut water']],['Fizz',['Still','Sparkling']]],
'Fruit nectar':[['Fruit',['Peach','Apricot','Pear','Mango','Sour cherry','Banana','Blackcurrant']]],
'Juice drink':[['Container',['Pouch','Carton with straw','Bottle']],['Sugar',['Sweetened','No added sugar']],['Type',['Juice cocktail','Fruit drink']]],
'Juice spritzer (Schorle)':[['Juice',['Apple (Apfelschorle)','Other fruit']],['Form',['Mixed with mineral water','Sparkling fruit juice']]],
'Still lemonade & limeade':[['Fruit',['Lemon','Pink lemonade','Lime']],['Flavour',['Plain','Mint (limonana)','Spiced (nimbu pani, shikanjvi)']],['Sugar',['Regular','Zero sugar']],['Clarity',['Still cloudy']]],
'Cold-pressed juice & shot':[['Protection',['Raw unprocessed (about 3 days)','High-pressure processed (about 30 days)']],['Content',['Green juice','Ginger shot','Turmeric shot']],['Pack',['Single bottle','Cleanse set']]],
'Smoothie':[['Base',['Fruit','Green or vegetable','Yoghurt-based','Protein']],['Pack',['Bottle',"Kids' pouch"]]],
'Squash & fruit cordial':[['Fruit',['Mixed fruit','Blackcurrant','Orange','Barley water']],['Juice content',['High-juice','Standard']],['Sugar',['Sweetened','No added sugar']]],
'Elderflower & botanical cordial':[['Flavour',['Elderflower','Elderflower with fruit','Ginger and lemongrass']],['Form',['Cordial','Sparkling pressé']]],
'Lime cordial':[['Sweetening',['Sweetened lime juice']],['Fruit',['Lime','Lemon','Passion fruit']]],
'Sharbat & rose syrup':[['Flavour',['Rose','Sandalwood','Bael','Khus (vetiver)','Tamarind']]],
'Drinking vinegar & shrub':[['Style',['Fruit shrub','Switchel (vinegar and ginger)','Sekanjabin']]],
'Fruit syrup (sirop)':[['Flavour',['Fruit','Mint','Barley']],['Pack',['Glass bottle','PET bottle']]],
'Café & flavouring syrup':[['Flavour',['Vanilla','Caramel','Hazelnut']],['Sugar',['Sugar-free']],['Form',['Syrup','Sauce']]],
'Soda-maker syrup':[['Flavour',['Cola','Lemon-lime','Fruit']],['Sugar',['Sugar-free']],['Form',['Concentrate','Flavour drops']]],
'Grenadine':[['Base',['Pomegranate juice','Artificially flavoured']],['Colour',['Red']]],
'Orgeat':[['Base',['Almond','Barley']]],
'Falernum':[['Alcohol',['Non-alcoholic','Liqueur']]],
'Simple & gomme syrup':[['Strength',['Simple (1:1)','Rich (2:1)']],['Thickener',['Plain','Gum arabic (gomme)']]],
'Powdered drink mix':[['Sweetening',['Sweetened','Unsweetened','Sugar-free']],['Pack',['Tub','Single-serve sticks']]],
'Water enhancer':[['Form',['Liquid drops','Tablets','Powder']],['Caffeine',['Caffeine-free','Caffeinated']]],
'Kombucha':[['Flavouring',['Original','Fruit, ginger or spice']],['Sugar',['Standard','Zero sugar']],['Alcohol',['Non-alcoholic','Hard kombucha (over 5% ABV)']]],
'Jun':[['Flavouring',['Plain','Fruit or spice']]],
'Water kefir':[['Flavouring',['Plain','Fruit-flavoured']],['Supply',['Bottled drink','Home grains (culture)']]],
'Brewed ginger beer':[['Production',['Traditional brewed','Ginger beer plant (home culture)']],['Heat',['Standard','Spiced']],['Sugar',['Regular','Diet']]],
'Tepache':[['Style',['Traditional','Spiced (chilli, cinnamon)','Tibicos fermented']]],
'Mauby':[['Form',['Fermented (mavi champán)','Syrup or concentrate','Carbonated']]],
'Kanji & vegetable ferments':[['Vegetable',['Carrot','Beetroot','Turnip']],['Origin',['Indian kanji','Turkish şalgam']]],
'Kvass':[['Base',['Bread','White','Beetroot','Fruit (apple, pear)']],['Fermentation',['Fermented','Kvass-flavoured malt drink (unfermented)']]],
'Boza':[['Region',['Turkish (thick, tart)','Albanian (white, sweet)','Bulgarian or Balkan']],['Grain',['Wheat','Millet (Białystok style)']]],
'Malta & malt soft drink':[['Sweetening',['Regular','Light or low sugar']],['Additions',['Vitamin-enriched']]],
'Rice & grain drink':[['Base',['Rice koji','Sake lees','Barley and rice','Pumpkin and rice','Tiger nut or rice (unfermented)']],['Style',['Amazake','Sikhye','Horchata']]],
'Mageu':[['Grain',['Maize','Maize and sorghum']],['Flavouring',['Natural','Fruit-flavoured']]],
'Lactic soft drink':[['Form',['Concentrate','Ready-to-drink','Carbonated']]],
'Energy drink':[['Pack',['Slim 250 ml can','Large can','Tonic bottle (non-carbonated)']],['Sugar',['Regular','Sugar-free or zero']],['Caffeine',['Standard','High-caffeine fitness drink','Coffee hybrid']]],
'Energy shot':[['Strength',['Regular','Extra strength','Decaf']]],
'Mate soda':[['Flavour',['Original','Pomegranate','Cola']],['Sugar',['Regular','Sugar-free']],['Season',['Winter spiced edition']]],
'Sports drink':[['Concentration',['Isotonic','Hypotonic','Hypertonic']],['Sugar',['Regular','Low-sugar or zero']],['Form',['Ready-to-drink','Powder to mix']]],
'Electrolyte drink & tablets':[['Form',['Effervescent tablet','Powder stick','Ready-to-drink']],['Sugar',['Regular','Zero sugar']],['Additions',['With caffeine','With vitamins']]],
'Protein & recovery drink':[['Protein',['Milk protein','Plant protein']],['Style',['High-protein low-sugar','Chocolate milk recovery']]],
'Functional & vitamin drink':[['Purpose',['Vitamin water','Nootropic or smart drink','Adaptogen drink','Relaxation drink']],['Base',['Enhanced water']]],
'Canned coffee':[['Milk',['With milk','Café au lait','Black']],['Sugar',['Sweetened','Low sugar']],['Pack',['Slim can','Bottle-can','Hot-vending can']]],
'Cold brew & iced coffee':[['Brewing',['Cold brew','Slow-drip (Kyoto-style)']],['Texture',['Still','Nitro can']],['Form',['Ready-to-drink','Concentrate']],['Milk',['Black','Sweetened or with milk']]],
'Bottled latte & coffee drink':[['Style',['Blended (Frappuccino-style)','Latte','Mocha']],['Additions',['Protein','Nitro texture']]],
'Iced tea':[['Flavour',['Lemon','Peach','Half-and-half (with lemonade)']],['Sugar',['Sweet tea','Unsweetened']],['Fizz',['Still','Sparkling']]],
'Bottled green & oolong tea':[['Tea',['Sencha','Genmaicha','Matcha blend','Oolong','Black oolong']],['Serving',['Cold','Hot PET bottle']]],
'Barley & grain tea':[['Grain',['Barley','Corn','Mixed grain']],['Serving',['Cold','Hot PET bottle']]],
'Milk tea & bubble tea':[['Pack',['Bottled milk tea','Hong Kong-style canned milk tea','Sealed-cup bubble tea','Bubble tea kit']],['Sugar',['Sweetened','No sugar']]],
'Yerba mate & guayusa drink':[['Plant',['Yerba mate','Guayusa']],['Style',['Still brewed','Sparkling','Sweetened iced mate']]],
}
# check all kinds covered
import sys
# ---------- SEE links
SEE={
'Ginger beer':[['J9','Brewed ginger beer','fermented rather than carbonated']],
'Brewed ginger beer':[['J9','Ginger beer','carbonated mixer style']],
'Sparkling lemonade':[['J9','Still lemonade & limeade','still, juice-based']],
'Still lemonade & limeade':[['J9','Sparkling lemonade','fizzy soda']],
'Mixed-fruit soda':[['J9','Squash & fruit cordial','Vimto also sold as cordial']],
'Squash & fruit cordial':[['J9','Mixed-fruit soda','ready-to-drink fizzy version']],
'Soda-maker syrup':[['B5','Soda maker','the machine it feeds']],
'Kombucha':[['B5','Kombucha and kefir vessel','home brewing vessel'],['C3','Kombucha SCOBY','the culture']],
'Water kefir':[['C3','Water kefir grains','the culture'],['J3','Kefir','milk kefir']],
'Lactic soft drink':[['J3','Drinking yoghurt & ayran','dairy cultured drinks']],
'Plant waters':[['J3','Coconut drink','dairy-free coconut milk drink']],
'Cold brew & iced coffee':[['J6','Cold brew & coffee concentrate','made-at-home coffee products']],
'Iced tea':[['J6','Iced tea mixes & tea concentrates','powders and concentrates']],
'Yerba mate & guayusa drink':[['J6','Yerba mate','the dry leaf'],['J9','Mate soda','carbonated mate']],
'Mate soda':[['J6','Yerba mate','the dry leaf'],['J9','Yerba mate & guayusa drink','still iced mate']],
'Alkaline & functional water':[['J9','Functional & vitamin drink','vitamin-enhanced water']],
'Functional & vitamin drink':[['J9','Alkaline & functional water','mineral-added water']],
'Sports drink':[['J9','Electrolyte drink & tablets','hydration powders']],
'Electrolyte drink & tablets':[['J9','Sports drink','ready-to-drink version']],
'Flavoured sparkling water':[['J9','Seltzer & carbonated water','unflavoured']],
'Seltzer & carbonated water':[['J9','Flavoured sparkling water','flavoured versions']],
'Cocktail mix':[['J9','Grenadine','bar syrups']],
'Simple & gomme syrup':[['J9','Cocktail mix','pre-blended mixes']],
'Kvass':[['J9','Malta & malt soft drink','unfermented malt drinks']],
'Energy drink':[['J9','Energy shot','small-dose version']],
'Canned coffee':[['J9','Bottled latte & coffee drink','chilled milk-coffee bottles']],
'Cola':[['J9','Cola-orange mix (Spezi)','cola blended with orange']],
'Fruit syrup (sirop)':[['J9','Soda-maker syrup','made up with a home carbonator']],
'Ramune & marble soda':[['J9','Lemon-lime soda','same flavour in a Western style']],
'Packaged ice':[['E2','Cooler','keeps it frozen']] if False else [],
}
for n,v in SEE.items():
    if v: K[n]['see']=v
for n,k in K.items():
    if n in ('Mexican & Latin American soda',): continue
    if n not in TT: print('NO TT',n); sys.exit(1)
    k['tt']=TT[n]; k.pop('t',None)
    for key in ('_hold',):
        k.pop(key,None)
    if not k.get('x'): k.pop('x',None)
    if k.get('m')==[]: k.pop('m')
    if k.get('r')==[]: k.pop('r')
# ---------- layout
def S(n,t,ax,kinds):
    return {'n':n,'t':t,'ax':ax,'k':[K[x] for x in kinds]} if ax else {'n':n,'t':t,'k':[K[x] for x in kinds]}
old={dp['n']:dp for dp in d['depts']}
def D(n,t,ax,shelves):
    o=old[n]; r={'n':n,'mode':o['mode']}
    if 'note' in o: r['note']=o['note']
    r['b']=o['b']; r['t']=t; r['ax']=ax; r['s']=shelves; return r
depts=[]
depts.append(D('Water','Drinking water sold in bottles, cans and jugs, plain or with minerals, gas or flavour added; a drink with sugar or juice → Sodas or Juices & smoothies, and tap-water treatment goes with home appliances → B5.',
 'Is it water defined by its source, water given gas, water with something added, or frozen water?',[
 S('Still water by source','Still water named for where it comes from or how it is treated; sparkling versions → Sparkling water, and added flavour → Flavoured & functional water.','kinds by legal source or treatment: protected mineral source, spring, confined aquifer or glacier, purified supply',['Natural mineral water','Spring water','Artesian & glacier water','Purified & table water']),
 S('Sparkling water','Water with carbon dioxide, from the source or added; a sparkling water with flavour → Flavoured & functional water.','kinds by the source of the gas: mineral spring or added to plain water',['Sparkling mineral water','Seltzer & carbonated water']),
 S('Flavoured & functional water','Water sold with a flavour, minerals or other additive; the unflavoured source-named water → Still water by source.','kinds by what is added: flavour, or minerals and treatment',['Flavoured still water','Flavoured sparkling water','Alkaline & functional water']),
 S('Packaged ice','Ice sold bagged for drinks and coolers; dry ice is not a drink ingredient.',None,['Packaged ice'])]))
depts.append(D('Sodas','Sweet flavoured fizzy drinks drunk on their own; plain fizzy water → Water, and fizzy drinks made to mix with spirits → Tonic & mixers.',
 'Which flavour family does the soda belong to: cola and spice, citrus, fruit and sweet, or root, cream and herbal?',[
 S('Cola & spiced sodas','Dark sodas built on cola nut, spice or pepper flavours; a fruit soda → Fruit & sweet sodas.','kinds by flavour: cola, pepper and spice, cola blended with orange',['Cola','Pepper & spiced soda','Cola-orange mix (Spezi)']),
 S('Citrus & lemonade sodas','Sodas flavoured with lemon, lime, orange or bitter orange; a still lemonade → Juices & smoothies.','kinds by citrus fruit: lemon-lime, other citrus, orange, plain lemonade, bitter orange',['Lemon-lime soda','Citrus soda','Orange soda','Sparkling lemonade','Chinotto & bitter soda','Ramune & marble soda']),
 S('Fruit & sweet sodas','Sodas flavoured with a non-citrus fruit or a sweet signature taste; a citrus soda → Citrus & lemonade sodas.','kinds by flavour: single fruit, cherry, apple, mixed fruit, guaraná, bubblegum',['Fruit soda','Cherry soda','Apple soda','Mixed-fruit soda','Guaraná soda','Bubblegum & tutti-frutti soda']),
 S('Root, cream & herbal sodas','Sodas flavoured with roots, vanilla or herbs; a cola → Cola & spiced sodas.','kinds by flavour base: root and bark, vanilla, herbs',['Root beer & birch beer','Cream soda','Herbal & sarsaparilla soda'])]))
depts.append(D('Tonic & mixers','Fizzy drinks made to be mixed with spirits; a soda drunk alone → Sodas, and bar syrups → Syrups & cordials.',
 'Which taste does the mixer add to a spirit: bitter, ginger, or none?',[
 S('Bitter mixers','Mixers whose bitterness balances gin or vodka; ginger mixers → Ginger mixers.','kinds by bitter ingredient: quinine, bitter citrus',['Tonic water','Bitter lemon & citrus mixer']),
 S('Ginger mixers','Mixers flavoured with ginger, from sweet and mild to fiery; a fermented ginger drink sold to drink alone → Fermented soft drinks.','kinds by heat: fiery brewed ginger beer, milder ginger ale',['Ginger beer','Ginger ale']),
 S('Neutral & blended mixers','Mixers that add fizz or a pre-balanced sweet-sour mix; a flavoured soda → Sodas.','kinds by how much flavour is added: none, or a full cocktail base',['Soda water & club soda','Cocktail mix'])]))
depts.append(D('Juices & smoothies','Drinks made from pressed fruit or vegetables, plain, diluted or blended; a fizzy drink → Sodas, and a drink made up from syrup → Syrups & cordials.',
 'What is the drink made from, and how far is it diluted or processed?',[
 S('Single-fruit juice','Juice of one fruit, whole or from concentrate; a blend diluted with water or sugar → Diluted & sparkling fruit drinks.','kinds by fruit: orange, apple, grape, berry, citrus, tropical',['Orange juice','Apple juice','Grape juice','Cranberry & berry juice','Grapefruit & citrus juice','Tropical & exotic juice']),
 S('Vegetable & plant juice','Juice or water drawn from vegetables and plants; a fruit juice → Single-fruit juice.','kinds by plant: tomato and vegetables, coconut and sap',['Tomato & vegetable juice','Plant waters']),
 S('Diluted & sparkling fruit drinks','Fruit juice thinned with water, sugar or fizz; a pure juice → Single-fruit juice.','kinds by dilution: pulp-based nectar, sweetened juice drink, sparkling spritzer, lemonade',['Fruit nectar','Juice drink','Juice spritzer (Schorle)','Still lemonade & limeade']),
 S('Fresh-pressed & blended','Chilled juice pressed raw or blended whole with other ingredients; shelf-stable juice → Single-fruit juice.',None,['Cold-pressed juice & shot','Smoothie'])]))
depts.append(D('Syrups & cordials','Sweet concentrates and powders made up with water, soda or spirits; a ready-to-drink soda → Sodas, and a juice → Juices & smoothies.',
 'How is it used: diluted into a long drink, added to drinks as a flavour, mixed into cocktails or stirred from powder?',[
 S('Cordials & squash','Fruit or flower concentrates diluted with water to drink; a bar syrup → Bar syrups.','kinds by flavour base: fruit, flower, lime, rose and herb, vinegar',['Squash & fruit cordial','Elderflower & botanical cordial','Lime cordial','Sharbat & rose syrup','Drinking vinegar & shrub']),
 S('Flavouring syrups','Syrups for adding flavour to coffee, soda or water; a cordial diluted as a drink → Cordials & squash.','kinds by use: fruit sirop, coffee-bar flavour, home soda maker',['Fruit syrup (sirop)','Café & flavouring syrup','Soda-maker syrup']),
 S('Bar syrups','Syrups made for cocktails and long drinks; a flavouring syrup for coffee → Flavouring syrups.','kinds by flavour: pomegranate, almond, ginger-lime, plain sugar',['Grenadine','Orgeat','Falernum','Simple & gomme syrup']),
 S('Powders & enhancers','Dry or squeezable drink flavourings mixed into water; a syrup → Flavouring syrups.','kinds by form: powder or liquid drops',['Powdered drink mix','Water enhancer'])]))
depts.append(D('Fermented soft drinks','Drinks soured or flavoured by fermentation and sold as non-alcoholic; a brewed soda with no live fermentation → Sodas.',
 'What is fermented: tea or sugar, fruit and plants, grain, or milk?',[
 S('Tea & sugar ferments','Drinks fermented from sweetened tea or sugar water; a ginger mixer sold carbonated → Ginger mixers.','kinds by culture: tea, tea and honey, sugar water, ginger',['Kombucha','Jun','Water kefir','Brewed ginger beer']),
 S('Fruit, vegetable & bark ferments','Drinks fermented from fruit peel, vegetables or bark; a fruit juice → Single-fruit juice.','kinds by raw material: pineapple rind, tree bark, root vegetables',['Tepache','Mauby','Kanji & vegetable ferments']),
 S('Grain ferments','Drinks fermented or malted from grain, rice or bread; a malt flavoured soda with no yeast → Malta & malt soft drink.','kinds by grain: rye bread, millet, malted barley, rice, maize',['Kvass','Boza','Malta & malt soft drink','Rice & grain drink','Mageu']),
 S('Milk ferments','Fizzy or still drinks soured with lactic bacteria from milk; a drinking yoghurt → J3.',None,['Lactic soft drink'])]))
depts.append(D('Energy & sports drinks','Drinks sold to lift energy, replace fluid or add nutrients; a plain flavoured soda → Sodas.',
 'What is the drink meant to do: wake you up, replace what training uses, or add vitamins and plant extracts?',[
 S('Stimulant drinks','Drinks sold for caffeine and similar stimulants; a hydration drink → Hydration & training drinks.','kinds by format: can, small shot, mate soda',['Energy drink','Energy shot','Mate soda']),
 S('Hydration & training drinks','Drinks sold to replace fluid, salts and protein around exercise; a caffeine drink → Stimulant drinks.','kinds by what is replaced: sugar and salts, salts alone, protein',['Sports drink','Electrolyte drink & tablets','Protein & recovery drink']),
 S('Vitamin & functional drinks','Drinks sold for vitamins, fibre or plant extracts rather than energy; a plain flavoured water → Flavoured & functional water.',None,['Functional & vitamin drink','Prebiotic & functional soda'])]))
depts.append(D('Ready-to-drink coffee & tea','Chilled or ambient bottles and cans of brewed coffee, tea or mate; dry tea and coffee → J6.',
 'Is the base coffee, or tea and similar leaf infusions?',[
 S('Coffee drinks','Brewed coffee sold ready to drink; dry coffee and concentrate to make at home → J6.','kinds by style: canned, cold brew, milk coffee',['Canned coffee','Cold brew & iced coffee','Bottled latte & coffee drink']),
 S('Tea & leaf-infusion drinks','Brewed tea, grain tea or mate sold ready to drink; dry leaf → J6.','kinds by leaf: black, green and oolong, grain, milk tea, mate',['Iced tea','Bottled green & oolong tea','Barley & grain tea','Milk tea & bubble tea','Yerba mate & guayusa drink'])]))
# check every kind used once
used=[k['n'] for dp in depts for s in dp['s'] for k in s['k']]
assert len(used)==len(set(used)), 'dup'
orig=set(); 
for dp in d['depts']:
    for s in dp['s']:
        for k in s['k']: orig.add(k['n'])
missing=[n for n in orig if n not in used and n not in renames]
print('orig kinds not placed:',missing)
d['depts']=depts
d['ax']='What is the drink: water, a flavoured soda, a mixer for spirits, a juice, a concentrate to dilute, a fermented drink, a drink for energy or training, or ready-made coffee and tea?'
d['key']=[
'1. Is it water, with or without gas, minerals or flavour added, or ice? → Water',
'2. Is it a sweet flavoured fizzy drink drunk on its own (cola, lemon-lime, root beer, cream soda)? → Sodas',
'3. Is it a fizzy drink sold to mix with spirits (tonic, ginger beer, soda water, cocktail mix)? → Tonic & mixers',
'4. Is it pressed fruit or vegetable juice, a nectar, a smoothie or coconut water? → Juices & smoothies',
'5. Is it a concentrate, syrup or powder made up with water, soda or spirits? → Syrups & cordials',
'6. Is it a drink soured or made by fermentation (kombucha, kvass, boza, water kefir)? → Fermented soft drinks',
'7. Is it sold for caffeine, hydration, protein, vitamins or plant extracts? → Energy & sports drinks',
'8. Is it brewed coffee, tea or mate in a bottle or can? → Ready-to-drink coffee & tea',
'<i>Precedence: fermented drinks (step 6) before sodas, so a brewed ginger beer sold to drink alone is fermented while a carbonated ginger mixer is a mixer (step 3); a drink sold for a body effect (step 7) before a soda; a juice drink is a juice (step 4) even when sold in a pouch.</i>']
json.dump(d,open(R+'work/STR_J9/new.json','w'),ensure_ascii=False,indent=1)
json.dump(renames,open(R+'work/STR_J9/renames.json','w'),ensure_ascii=False,indent=1)
open(R+'work/STR_J9/demoted.txt','w').write('\n'.join(demoted))
print('ok',len(used))
