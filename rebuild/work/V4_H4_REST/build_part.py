import json,re,copy,os
R='/home/user/Possession-Taxonomy/rebuild/'
d=json.load(open(R+'out/H4.json'))
D={x['n']:x for x in d['depts']}
names=["Oils, attars & body fragrance","Samples, decants & sets","Bottles & atomisers","Perfumery materials","Perfumer's tools & kits"]
dep={n:copy.deepcopy(D[n]) for n in names}
def kind(dp,n):
    for s in dp['s']:
        for k in s['k']:
            if k['n']==n: return k
WP='https://en.wikipedia.org/wiki/'
# ---------- Oils
o=dep[names[0]]
for s in o['s']:
    for k in s['k']:
        k.pop('m',None)
        for e in k.get('x',[]): e.setdefault('v',[])
k=kind(o,'Attar (deg-bhapka distillate)')
ATT=WP+'Attar'; KAN=WP+'Kannauj'; LHI='https://livehistoryindia.com/story/living-culture/kannauj-attar'; SCE='https://www.scento.com/blog/guide-indian-attars-history-modern-use'
for e in k['x']:
    e['g']='Kannauj and India'
byn={e['n']:e for e in k['x']}
byn['Rooh gulab (rose attar)']['s']=ATT
byn['Rooh gulab (rose attar)']['v']=[]
byn['Mitti attar']['v']=[]
byn['Mitti attar']['s']=LHI
byn['Mitti attar']['d']="Attar distilled from broken shards of earthen vessels to give the smell of first rain; a Kannauj speciality."
byn['Shamama']['s']=LHI
byn['Shamama']['d']="Kannauj attar named by master distillers as one of their products; the Attar article lists it as samamme, credited to Shah Jahan."
byn['Ruh khus (vetiver attar)']['s']=ATT
byn['Ruh khus (vetiver attar)']['d']="Vetiver (khus) attar, one of the cool summer attars; also named by Kannauj distillers."
byn['Kewra attar']['s']=ATT
byn['Kewra attar']['d']="Kewra (pandanus) attar, one of the cool summer attars made in Kannauj."
k['x']+= [
 {"n":"Jasmine attar (mogra, motia)","a":"mogra attar · motia attar","d":"Jasmine attar, listed among the popular Kannauj attars and as a cool summer attar.","mk":"","y":"","s":KAN,"v":[],"g":"Kannauj and India","dt":"cool attar"},
 {"n":"Marigold attar","a":"","d":"Marigold attar, named by Kannauj master distillers among their products.","mk":"","y":"","s":LHI,"v":[],"g":"Kannauj and India"},
 {"n":"Blue lotus attar","a":"","d":"Blue lotus attar, named by Kannauj master distillers among their products.","mk":"","y":"","s":LHI,"v":[],"g":"Kannauj and India"},
 {"n":"Kesar attar (saffron)","a":"saffron attar","d":"Saffron attar, listed as a warm winter attar.","mk":"","y":"","s":ATT,"v":[],"g":"Kannauj and India","dt":"warm attar"},
 {"n":"Yemeni mountain-flower attar","a":"","d":"Mountain-flower attar of Yemen, introduced by Arwa al-Sulayhi according to the Attar article.","mk":"","y":"","s":ATT,"v":[],"g":"Yemen"},
]
k['x'][0]['role']='origin' if False else k['x'][0].get('role')
k['nl']="One entry is a named attar, a flower, herb or earth distillate captured in a sandalwood or paraffin base; brand bottlings are not entries."
k['sel']="Named attars from the fetched Attar and Kannauj articles, a Kannauj feature and an Indian attars guide (Kannauj attars; Yemen). Covers 10 of 10 attars these pages name; henna (hina) attar appears only in search excerpts and is left out. No whole-space reference exists."
k['xg']="Grouped by tradition: Kannauj and India, then Yemen."
k['d']="Natural distillate of flowers, herbs, earth or spices captured in a sandalwood or paraffin base by deg-bhapka distillation, then aged; Kannauj holds a protected geographical indication (2014)."
k['s']=KAN
k=kind(o,'Rose oil & Taif rose')
k['x'][0]['g']='Saudi Arabia'
k['x'][0]['s']=WP+'Rose_oil'
k['x'][1]['g']='Bulgaria'
k['x'][1]['s']=WP+'Rose_oil'
k['x'][0]['d']="Rose oil from the Taif rose (Rosa damascena) of the Saudi Arabian mountains, distilled in copper pots each spring."
k['x'][0]['v']=[]
k['x'].append({"n":"Turkish rose oil","a":"Turkish Rose","d":"Rose oil from the Turkish Rosa damascena, named beside Bulgarian and Taif rose on the Rose oil article.","mk":"","y":"","s":WP+'Rose_oil',"v":[],"g":"Turkey"})
k['nl']="One entry is a rose oil named by its place of origin; brand bottlings are not entries."
k['sel']="Origins named in the fetched Rose oil article (Bulgarian, Turkish and Taif rose from Rosa damascena); Moroccan, Iranian and Indian roses are named without a product and are not entries. Complete: 3 of 3 named origins in Wikipedia Rose oil."
k['xg']="Grouped by country."
k=kind(o,'Oud oil (dehn al oud)')
AG=WP+'Agarwood'
oud=[("Cambodian agarwood (khloem chann)","Cambodia","Agarwood of Aquilaria crassna named khloem chann on the Agarwood article, the Cambodian source of oud oil."),
("Assam agarwood (xasi)","India","Assam agarwood, named xasi on the Agarwood article."),
("Vietnamese agarwood (kỳ nam, trầm hương)","Vietnam","Vietnamese agarwood grades, kỳ nam (calambac) and trầm hương, named on the Agarwood article."),
("Thai agarwood (mai kritsana)","Thailand","Thai agarwood, mai kritsana on the Agarwood article."),
("Lao agarwood (mai ketsana)","Laos","Lao agarwood, mai ketsana on the Agarwood article."),
("Myanmar agarwood (Thit Mhwae)","Myanmar","Burmese agarwood, Thit Mhwae on the Agarwood article."),
("Sri Lankan agarwood (Walla Patta)","Sri Lanka","Agarwood of Gyrinops walla named Walla Patta on the Agarwood article."),
("Tibetan agarwood","Tibet","Tibetan agarwood in four named kinds: unique, yellow, white and black eaglewood.")]
k['x']=[{"n":n,"a":"","d":dd,"mk":"","y":"","s":AG,"v":[],"g":g} for n,g,dd in oud]
k['nl']="One entry is an agarwood named by its place of origin; the oil distilled from it carries that origin."
k['sel']="Origins named on the fetched Agarwood article (also Japan: kyara, a wood grade of jinko, not an oil). Complete: 8 of 8 oil-producing origins named there; the page gives no oil grade lists, so these are agarwood names."
k['xg']="Grouped by country."
k['d']="Oil distilled from resin-infected agarwood (Aquilaria), worn neat; scent varies with species, origin, wood part and distillation."
k=kind(o,'Musk oil')
k['x'][0]['v']=[]; k['x'][0]['g']='Middle East'; k['x'][0]['s']=ATT
k['nl']="One entry is a named musk oil of a tradition; brand bottlings are not entries."
k['sel']="Musk Tahara from the fetched Attar article; no whole-space reference exists. Covers 1 of 1 named on that page."
k=kind(o,'Mukhallat (blended oil)')
k['x']=[]
k['s']='https://fragplace.com/blog/the-art-of-arabic-perfumery-discovering-middle-eastern-fragrance-traditions'
k['d']="Arabian blended perfume oil built entirely in oil, layering oud, rose and other notes into one dense accord; a house blend, so the kind has no named entries."
k=kind(o,'Perfume oil')
k['x']=[]
k=kind(o,'Body mist')
k['x'][0]['own']="Bath & Body Works, Inc.";k['x'][0]['tier']="Independent";k['x'][0]['cty']="United States"
k['x'][1]['own']="Victoria's Secret & Co.";k['x'][1]['tier']="Independent";k['x'][1]['cty']="United States";k['x'][1]['own_y']="2021"
k['x'][2]['own']="Groupe L'Occitane";k['x'][2]['tier']="Independent";k['x'][2]['cty']="United States";k['x'][2]['own_y']="2021"
for e in k['x']: e['g']='United States'
k['nl']="One entry is a body mist sold under its own name; flankers and sizes are versions."
k['sel']="No whole-space reference exists; three mists named by fetched pages and the brand pages Bath & Body Works, Victoria's Secret and Sol de Janeiro. Covers 3 of an unmeasured market."
k['xg']="Grouped by brand home country."
k=kind(o,'Solid perfume'); k['x']=[]
o['msum']="No market share figure for attars, oil perfumes or body mists was found on a fetched page."
# ---------- Samples
sm=dep[names[1]]
for s in sm['s']:
    for k in s['k']:
        k.pop('m',None); k['x']=[]; k.pop('r',None) if k['n'] in('Decant',) else None
kk=kind(sm,'Discovery set'); kk['d']="House-made boxed set of small vials or sprays covering part of a line, bought to explore before a full bottle; commodity, so the kind has no named entries."
kk['s']=kk['s']
sm['note']=sm.get('note','')+" Commodity departments hold no named entries."
# ---------- Bottles
b=dep[names[2]]
for s in b['s']:
    for k in s['k']:
        k.pop('m',None); k.pop('r',None)
VA='https://collections.vam.ac.uk/item/O2687'; CM='https://glasscollection.cmog.org/objects/45140/perfume-bottle'
k=kind(b,'Collectible perfume bottle')
k['x']=[
 {"n":"Cyclamen (Lalique for Coty)","a":"Coty Cyclamen","d":"First Lalique bottle for Coty, designed 1909 and made at the Combs-la-Ville glassworks; the V&A holds it.","mk":"Lalique","y":"1909","s":VA,"v":[],"role":"origin","g":"Lalique for Coty","dt":"press-moulded and mould-blown glass, patinated","own":"Lalique","tier":"Independent","cty":"France"},
 {"n":"Ambre antique (Lalique for Coty)","a":"Coty - 3, Ambre antique","d":"Cylindrical bottle with four moulded female figures and a sepia patina, designed 1910; held by the Corning Museum of Glass.","mk":"Lalique","y":"1910","s":CM,"v":[],"g":"Lalique for Coty","dt":"colourless glass with sepia patina","own":"Lalique","tier":"Independent","cty":"France"},
 {"n":"Chanel No. 5 flacon","a":"Chanel No. 5 bottle","d":"Plain rectangular bottle; the 1922 first version had rounded shoulders and the square faceted form with an octagonal stopper dates from 1924.","mk":"Chanel","y":"1922","s":WP+'Chanel_No._5',"v":[{"n":"First bottle","y":"1922","d":"rounded shoulders, sold in Chanel boutiques only"},{"n":"Faceted bottle","y":"1924","d":"square corners, octagonal stopper, essentially unchanged since"}],"g":"Chanel","dt":"clear glass · stopper · extrait size","own":"Chanel","tier":"Independent","cty":"France"},
]
k['nl']="One entry is a named bottle design that is the first of its kind or is held by a museum, as a fetched page states; other house flacons are not entries."
k['sel']="Bottle designs held by named museums (V&A, Corning Museum of Glass) and origin bottles (Lalique for Coty, first commissioned 1908). The Chanel No. 5 flacon is the icon named by the brief; MoMA's Chanel page shows only the 1959 exhibition The Package, so no museum holding is confirmed. Not a complete list: no whole-space reference exists; flacons such as Shalimar and Quelques Fleurs were dropped for lack of a fetched museum page."
k['xg']="Grouped by the house the bottle was made for."
k=kind(b,'Bulb atomiser')
k['x']=[{"n":"DeVilbiss perfumizer","a":"perfumizer","d":"DeVilbiss's perfume atomiser, introduced 1907; the earliest were salt cellars fitted with atomiser mounts.","mk":"DeVilbiss","y":"1907","s":"https://perfumeprojects.com/museum/marketers/DeVilbiss.shtml","v":[],"g":"United States","dt":"bulb · glass base · metal collar","own":"DeVilbiss","tier":"Independent","cty":"United States"}]
k['nl']="One entry is the first bulb atomiser made for perfume; later makers are not entries."
k['sel']="DeVilbiss perfumizer from the fetched DeVilbiss history page, which dates it to 1907 and says medical atomisers came earlier. No page confirms an earlier perfume atomiser."
k=kind(b,'Refillable travel atomiser'); k['x']=[]
kind(b,'Attar bottle')['x']=[]
kind(b,'Czech crystal perfume bottle')['x']=[]
# ---------- Tools
t=dep[names[4]]
for s in t['s']:
    for k in s['k']:
        k.pop('m',None); k['x']=[]
# ---------- Materials
m=dep[names[3]]
CAT=WP+'Category:Perfume_ingredients'; LEO=WP+'List_of_essential_oils'; LFC=WP+'List_of_fragrance_compounds'; ACP=WP+'Aroma_compound'; PER=WP+'Perfume'; CEO=WP+'Category:Essential_oils'
low=lambda s:re.sub(r'[^a-z0-9]','',s.lower())
EO_RAW="""Agar oil|Ajwain oil|Amyris oil|Angelica root oil|Anise oil|Armoise/Mugwort oil|Asafoetida oil|Basil oil|Bay leaf oil|Beeswax absolute|Bergamot oil|Birch oil|Bitter almond oil|Black pepper oil|Buchu oil|Calamodin oil|Calamus oil|Camphor oil|Cannabis flower essential oil|Caraway seed oil|Cardamom seed oil|Carrot seed oil|Cedar oil|Chamomile oil|Cinnamon oil|Cistus ladanifer oil|Citron oil|Citronella oil|Clary sage oil|Clove oil|Coconut oil|Coffee oil|Coriander oil|Costmary oil|Costus root oil|Cranberry seed oil|Cubeb oil|Cumin seed/black seed oil|Curry leaf oil|Cypress oil|Cypriol oil|Davana oil|Dill oil|Douglas-fir oil|Elecampane oil|Elemi oil|Eucalyptus oil|Fennel seed oil|Fenugreek oil|Fir oil|Frankincense oil|Galangal oil|Galbanum oil|Garlic oil|Geranium oil|Ginger oil|Goldenrod oil|Grapefruit oil|Henna oil|Helichrysum oil|Hickory nut oil|Horseradish oil|Hyssop oil|Jasmine oil|Juniper berry oil|Lavender oil|Ledum oil|Lemon oil|Lemongrass oil|Lime oil|Litsea cubeba oil|Mandarin oil|Marjoram oil|Manuka oil|Melissa oil|Mentha arvensis oil|Moringa oil|Mountain savory oil|Mugwort oil|Mustard oil|Myrrh oil|Myrtle oil|Neem oil|Neroli oil|Nutmeg oil|Orange oil|Oregano oil|Orris oil|Palo santo oil|Parsley oil|Patchouli oil|Perilla oil|Pennyroyal oil|Peppermint oil|Petitgrain oil|Pine oil|Ravensara oil|Red cedar oil|Roman chamomile oil|Rose oil|Rosehip oil|Rosemary oil|Rosewood oil|Sage oil|Sandalwood oil|Sassafras oil|Savory oil|Schisandra oil|Spearmint oil|Spikenard oil|Spruce oil|Star anise oil|Tangerine oil|Tarragon oil|Tea tree oil|Thyme oil|Tsuga oil|Turmeric oil|Valerian oil|Warionia oil|Vetiver oil|Western red cedar oil|Wintergreen oil|Yarrow oil|Ylang-ylang oil"""
EO=EO_RAW.split('|')
extra_cat=[("Cajeput oil",),("Cananga odorata oil",),("Chinese cinnamon oil",),("Lemon myrtle oil (Backhousia citriodora)",),("Palmarosa oil (Cymbopogon martinii)",),("Oil of guaiac",),("Ravintsara oil",),("Sugandha kokila oil",),("Shemen Afarsimon",),("Monoï oil",)]
fam=[("Citrus",r"bergamot|calamodin|citron\b|grapefruit|lemon\b|lime|mandarin|orange|tangerine|neroli|petitgrain|litsea|lemon myrtle|lemongrass|citronella|palmarosa"),
("Wood, conifer & resin",r"cedar|cypress|cypriol|fir|pine|spruce|tsuga|sandalwood|rosewood|agar|palo santo|amyris|birch|guaiac|elemi|frankincense|myrrh|galbanum|ledum|cistus|juniper"),
("Spice & seed",r"anise|ajwain|black pepper|caraway|cardamom|carrot|cinnamon|clove|coriander|cubeb|cumin|curry|dill|fennel|fenugreek|ginger|galangal|nutmeg|turmeric|asafoetida|mustard|horseradish|garlic|schisandra|celery|parsley|costus|angelica|calamus|elecampane|valerian|spikenard|star anise"),
("Herb & mint",r"basil|bay leaf|marjoram|melissa|oregano|peppermint|spearmint|pennyroyal|thyme|tarragon|rosemary|sage|savory|hyssop|mugwort|armoise|perilla|mentha|yarrow|tea tree|eucalyptus|cajeput|manuka|myrtle|ravensara|ravintsara|buchu|goldenrod|helichrysum|davana|wintergreen|camphor|costmary|chamomile|lavender|clary|patchouli|vetiver|geranium"),
("Flower",r"jasmine|rose oil|ylang|cananga|orris|henna|cannabis|sugandha|chamomile|neroli|monoï|afarsimon")]
def eofam(n):
    for f,rx in fam:
        if re.search(rx,n.lower()): return f
    return "Seed, nut & fruit oils and other plants"
k=kind(m,'Essential oil')
old={e['n']:e for e in k['x']}
keep=list(k['x'])
skipmatch={"sandalwood oil":"Mysore sandalwood oil","vetiver oil":"Haitian vetiver","bergamot oil":"Bergamot oil","lavender oil":"Lavender oil","neroli oil":"Neroli","patchouli oil":"Patchouli oil","cedar oil":"Cedarwood oil"}
fmap={"Mysore sandalwood oil":"Wood, conifer & resin","Haitian vetiver":"Herb & mint","Bergamot oil":"Citrus","Lavender oil":"Herb & mint","Neroli":"Citrus","Patchouli oil":"Herb & mint","Cedarwood oil":"Wood, conifer & resin"}
for e in keep:
    e['g']=fmap[e['n']]
new=[]
for n in EO:
    if n.lower() in skipmatch: continue
    new.append({"n":n[0].upper()+n[1:],"a":"","d":"Essential oil listed on Wikipedia's List of essential oils.","mk":"","y":"","s":LEO,"v":[],"g":eofam(n)})
for (n,) in extra_cat:
    new.append({"n":n,"a":"","d":"Essential oil named in Wikipedia's Essential oils category.","mk":"","y":"","s":CEO,"v":[],"g":eofam(n)})
k['x']=keep+new
k['nl']="One entry is an essential oil or plant oil named on the reference list; origin, species and grade are versions or attributes."
k['sel']="Wikipedia List of essential oils (every row except Attar, which has its own kind, and Linalool, which is an aroma chemical) plus the oils named in Wikipedia's Essential oils category; seven earlier entries are kept. Plant-family sections are the compiler's grouping of the names, as the page has none."
k['xg']="Grouped by plant use: citrus, wood and conifer, spice and seed, herb and mint, flower, then other."
k['x'].sort(key=lambda e:(e['g'],e['n']))
EOc=len(k['x'])
k['sel']+=f" Complete: {len(EO)+2} of {len(EO)+2} rows in Wikipedia List of essential oils (Attar and Linalool moved to their own kinds; {len(EO)-0} rows give {EOc-len(extra_cat)} entries after merging the seven earlier ones); {len(extra_cat)} oils added from the category."
# natural plant extracts
ABS=[("Orris butter","Orris oil and butter from iris rhizome; kept from the earlier list."),("Oakmoss absolute","Absolute from the oakmoss lichen; kept from the earlier list.")]
k=kind(m,'Absolute & CO2 extract')
k['x'][0]['g']='Root, moss & lichen';k['x'][1]['g']='Root, moss & lichen'
PL=["Cascarilla","Sassafras","Jasmine","Osmanthus","Plumeria","Mimosa","Tuberose","Narcissus","Cassie","Ambrette","Vanilla","Blackcurrant leaf","Violet","Hay","Tomato leaf","Iris rhizome","Tonka bean","Cocoa","Mace","Treemoss","Bladderwrack (Fucus vesiculosus)","Almond"]
for n in PL:
    g="Flower" if n in("Jasmine","Osmanthus","Plumeria","Mimosa","Tuberose","Narcissus","Cassie","Violet") else ("Seed, bean & leaf" if n in("Ambrette","Vanilla","Blackcurrant leaf","Tomato leaf","Tonka bean","Cocoa","Mace","Almond","Cascarilla","Sassafras","Hay") else "Root, moss & lichen")
    k['x'].append({"n":n,"a":"","d":"Plant material the Perfume article names as used in perfumery.","mk":"","y":"","s":PER,"v":[],"g":g})
for n,u in [("Valeriana celtica",CAT),("Cyperus articulatus",CAT),("Nardostachys (spikenard)",CAT),("Polianthes tuberosa",CAT),("Pelargonium graveolens",CAT),("Artemisia pallens (davana)",CAT)]:
    pass
k['x']=[e for e in k['x'] if e['n']!='Tuberose']+[{"n":"Tuberose (Polianthes tuberosa)","a":"","d":"Plant material the Perfume article names as used in perfumery; also in the Perfume ingredients category.","mk":"","y":"","s":PER,"v":[],"g":"Flower"}]
for n in ["Valeriana celtica","Cyperus articulatus (adrue)","Artemisia pallens (davana)","Pelargonium graveolens (geranium)"]:
    k['x'].append({"n":n,"a":"","d":"Plant material in Wikipedia's Perfume ingredients category.","mk":"","y":"","s":CAT,"v":[],"g":"Root, moss & lichen" if 'Valeriana' in n or 'Cyperus' in n else "Seed, bean & leaf"})
k['nl']="One entry is a plant material used in perfumery as an absolute, concrete, butter or extract; the extraction is a version."
k['sel']="Plant materials named in the first 100,000 characters of Wikipedia Perfume and in the Perfume ingredients category; the page does not state which are absolutes, so the kind lists the materials. The rest of the Perfume article (91,793 characters) was not read. Essential-oil plants are in the Essential oil kind."
k['xg']="Grouped by plant part: flower, seed, bean and leaf, then root, moss and lichen."
# animal & resin
k=kind(m,'Animalic & resin material')
for e in k['x']:
    e['g']='Animal' if e['n'] in('Ambergris','Deer musk','Civet','Castoreum','Hyraceum') else 'Resin & balsam'
    e['v']=e.get('v',[])
have={low(e['n']) for e in k['x']}
for n,u in [("Amber (fossil resin)",PER),("Copal (fossil resin)",PER),("Honeycomb (beeswax and honey)",PER),("Bdellium",CAT),("Balm of Gilead",CAT),("Copaiba",CAT),("Opopanax",CAT),("Storax balsam",CAT),("Tolu balsam",CAT),("Tincture of benzoin",CAT)]:
    g='Animal' if 'Honeycomb' in n else 'Resin & balsam'
    k['x'].append({"n":n,"a":"","d":("Animal-derived material" if g=='Animal' else "Resin or balsam")+" named on the cited reference page.","mk":"","y":"","s":u,"v":[],"g":g})
k['nl']="One entry is an animal-derived or resin material used in perfumery; synthetic replacements are aroma chemicals."
k['sel']="Animal and resin materials named in Wikipedia Perfume (first 100,000 characters) and its Perfume ingredients category, plus ten earlier entries. Agarwood, labdanum and spikenard sit in the category list but are treated as oils or plant materials."
k['xg']="Grouped by source: animal, then resin and balsam."
# aroma chemicals
k=kind(m,'Aroma chemical')
CATX="""Acetoin|Ambrein|Ambroxide|Ambrinol 95|Amber Xtreme|Ambermor Ketal IPM|Benzyl acetate|Benzyl alcohol|Benzyl benzoate|Benzyl cinnamate|Benzylacetone|Bisabolol|Bornafix|Bourgeonal|Calone|Camphene|Camphor|Cashmeran|Cetalor|Chavicol|Cinnamyl alcohol|Citral|Citronellol|Citronellyl acetate|Citronellyl formate|Citronellyl propionate|Civetone|Cuminaldehyde|Cyclamen aldehyde|Cyclododecanone|Cyclohexadecanone|5-Cyclohexadecenone|Cyclopentadecanolide|Cyclopentanone|Damascenone|Damascone|Diethyl malonate|Dihydromyrcenol|3,7-Dimethyl-1-octanol|Dodecanenitrile|Estragole|Ethyl benzoate|Ethyl maltol|Ethyl methylphenylglycidate|Ethyl salicylate|Ethylvanillin|Eugenol|Farnesene|Farnesol|Filbertone|Fructone|Galaxolide|Gastrodigenin|Geraniol|Geranyl acetate|Geranyl formate|Geranyl propionate|Geranyl-linalool|Grapefruit mercaptan|Grisalva|Helional|Heptyl acetate|2-Heptylcyclopentanone|Hexyl benzoate|α-Hexylcinnamaldehyde|Hydroxycitronellal|Hydroxymethylpentylcyclohexenecarboxaldehyde|Indole|Ionone|Irone|Isoamyl butyrate|Isobornyl cyclohexanol|α-Isomethyl ionone|Isopropyl salicylate|Isovanillin|Jasminaldehyde|Juniperol|γ-Lactone|Lilial|Linalool|p-Menthane-3,8-diol|p-Menthane|Menthone|Methyl benzoate|Methyl butyrate|Methyl dihydrojasmonate (Hedione)|Methyl heptanoate|Methyl isobutyrate|Methyl pivalate|2-(2-(4-Methyl-3-cyclohexen-1-yl)propyl)cyclopentanone|Muscone|Musk xylene|Myrcene|Nerol|Nerolidol|2-Octanone|3-Octanone|2-Ethylhexyl salicylate|Patchoulol|Perillaldehyde|Phellandrene|Phenethyl alcohol|Phenethyl benzoate|Phenylacetic acid|Phenylisohexanol|β-Pinene|Pomarose|Pulegone|Raspberry ketone|Rhodinol|Safrole|Sandalore|α-Santalol|β-Santalol|Skatole|Synthetic musk|Tetramethyl acetyloctahydronaphthalenes (Iso E Super)|Thujone|Vanillin|o-Vanillin|α-Vetivone|Floralozone"""
ACPX="""Methyl formate|Methyl acetate|Methyl propionate|Ethyl acetate|Ethyl butyrate|Pentyl butyrate|Pentyl pentanoate|Octyl acetate|Methyl anthranilate|Hexyl acetate|Limonene|Menthol|Carvone|Terpineol|Eucalyptol|Jasmone|Anisole|Anethole|Thymol|Furaneol|1-Hexanol|cis-3-Hexen-1-ol|Acetaldehyde|Hexanal|cis-3-Hexenal|Furfural|Hexyl cinnamaldehyde|Isovaleraldehyde|Anisic aldehyde|Dihydrojasmone|Oct-1-en-3-one|2-Acetyl-1-pyrroline|6-Acetyl-2,3,4,5-tetrahydropyridine|Diacetyl|gamma-Decalactone|gamma-Nonalactone|delta-Octalactone|Jasmine lactone|Massoia lactone|Wine lactone|Sotolon|Cinnamaldehyde|Benzaldehyde|Methyl salicylate|Citronellal|Ocimene|Coumarin"""
famrx=[("Musks",r"musk|muscone|civetone|cyclopentadecanolide|cyclohexadecanone|cyclohexadecenone|cyclododecanone|galaxolide|ambrettolide|hexadecanolide|zenolide|celestolide|luminide|muscemor|edenolide"),
("Woody & amber",r"ambr|amber|cashmeran|bornafix|cetalor|grisalva|iso e super|tetramethyl|santalol|sandalore|patchoulol|vetivone|juniperol|isobornyl|bisabolol|farnes|operanide|trisamber|cedr"),
("Floral",r"hedione|dihydrojasmonate|bourgeonal|lilial|cyclamen|helional|hydroxy|hexylcinnam|jasmin|phenethyl|phenylisohexanol|rhodinol|geraniol|nerol\b|citronellol|linalool|indole|skatole|ionone|irone|damasc|pomarose|floralozone|geranyl-linalool|benzyl alcohol|cinnamyl alcohol|nerolidol|phenylacetic"),
("Citrus, green & marine",r"citral|dihydromyrcenol|mercaptan|calone|hexen|hexanol|hexanal|limonene|ocimene|myrcene|phellandrene|pinene|citronellal|terpineol|dimethyl-1-octanol|perillaldehyde|menthane|menthol|menthone|carvone|pulegone|eucalyptol|camphene|camphor|thujone|dodecanenitrile"),
("Sweet, fruity & gourmand",r"vanill|maltol|raspberry|filbertone|fructone|glycidate|lactone|furaneol|sotolon|diacetyl|acetoin|pyrrol|pyridine|butyrate|acetate|formate|propionate|benzoate|salicylate|heptanoate|isobutyrate|pivalate|anthranilate|malonate|methyl propionate|pentanoate|benzylacetone|octanone|cyclopentanone|heptylcyclopentanone|methyl-3-cyclohexen|jasmone|coumarin|acetaldehyde|furfural|isovaleraldehyde"),
("Spice & aromatic",r"eugenol|safrole|estragole|chavicol|anethole|anisole|thymol|cinnamaldehyde|benzaldehyde|anisic|cuminaldehyde|gastrodigenin|benzyl cinnamate|oct-1-en")]
def cfam(n):
    for f,rx in famrx:
        if re.search(rx,n.lower()): return f
    return "Other aroma chemicals"
YEARS={"Methyl dihydrojasmonate (Hedione)":("1966","Characterised and synthesised by Edouard Demole of Firmenich between 1957 and 1962; first used in Eau Sauvage (Dior, 1966).",WP+'Methyl_dihydrojasmonate',"Firmenich"),
"Tetramethyl acetyloctahydronaphthalenes (Iso E Super)":("1973","Created at IFF in 1973 by John Hall and James Milton Sanders; patent 1975; first used in Halston (1975). Called the most successful synthetic fragrance.",WP+'Tetramethyl_acetyloctahydronaphthalenes',"IFF"),
"Galaxolide":("1965","Polycyclic musk first synthesised at IFF in 1965 by Heeringa and Beets, per the History section.",WP+'Galaxolide',"IFF"),
"Calone":("1966","Marine-note molecule discovered by Pfizer in 1966; used in perfumery from the 1980s.",WP+'Calone',"Pfizer"),
"Musk xylene":("1888","Nitro musk found by accident by Albert Baur in 1888.",WP+'Synthetic_musk',""),
"Muscone":("1926","Macrocyclic musk first synthesised in small amounts by Leopold Ruzicka in 1926.",WP+'Synthetic_musk',""),
"Ethylvanillin":("1889","Added in large amount by Jacques Guerlain to Jicky (1889), one of the earliest uses of synthetic molecules.",WP+'Ethylvanillin',""),
"Vanillin":("19th century","Purified in the 19th century.",ACP,""),
"Cinnamaldehyde":("19th century","Purified in the 19th century; the first single-component fragrance.",ACP,""),
"Benzaldehyde":("19th century","Purified in the 19th century.",ACP,""),
"Methyl salicylate":("19th century","Purified in the 19th century.",ACP,""),
"Ambroxide":("","Synthetic ambergris-note molecule made from sclareol; sold as Ambrox (Firmenich), Ambrofix (Givaudan) and Ambroxan (Kao). The page gives no year.",WP+'Ambroxide',"")}
ents={}
def add(n,src,fam_=None):
    if low(n) in ents: return
    y,dd,s,mkr=YEARS.get(n,("",None,None,""))
    e={"n":n,"a":"","d":dd or "Aroma compound listed on the cited reference page.","mk":mkr,"y":y,"s":s or src,"v":[],"g":fam_ or cfam(n)}
    ents[low(n)]=e
for n in CATX.split('|'): add(n,CAT)
for n in ACPX.split('|'): add(n,ACP)
ents[low("Tetramethyl acetyloctahydronaphthalenes (Iso E Super)")]['role']='landmark'
ents[low("Cinnamaldehyde")]['role']='origin'
ents[low("Tetramethyl acetyloctahydronaphthalenes (Iso E Super)")]['a']='Iso E Super · IFF'
ents[low("Methyl dihydrojasmonate (Hedione)")]['a']='Hedione'
ents[low("Ethylvanillin")]['a']='ethyl vanillin'
ents[low("Ambroxide")]['a']='Ambrox · Ambrofix · Ambroxan'
# keep earlier chemistry entries not in lists (Coumarin, Cashmeran etc covered); add earlier names if missing
TRADE=[l for l in """Bergamal|Citral Dimethyl Acetal|Citrolate|Clonal|Dimyrcetol|Herbalime|Limoxal|Myrcenol Super|Nootkatone|Octacetal|Orange Flower Ether|Pamplefleur|Valencene|Verbenal|Anisimea|Aquaflora|Auralva|Cyclemax|Damascol|Fleuramone|Gelsone|Hyacinth Body|Hydroxyol|Jasmal|Jessemal|Kharismal|Lavonax|Lilianth|Lindenol|Lyral|Melafleur|Muguesia|Peomosa|Phenafleur|Phenoxanol|Rosalva|Rosethyl|Starfleur|Violiff|Ylanganate|Intreleven Aldehyde|Maritima|Myrac aldehyde|Oceanol|Ozofleur|Pino Acetaldehyde|Precyclemone B|Cassiffix|Cyclabute|Cyclemone A|Dulcinyl|Fraistone|Hexalon|Nectarate|Tropicalia|Vanoris|Galbascone|Cortex Aldehyde|Liffarome|Melozone|Montaverdi|Syvertal|Vertoliff|Vivaldie|Canthoxal|Fleuranil|Herbac|Oxaspirane-819|Salicynalva|Verdol|Verdone|Isobutyl quinoline|Celestolide|Edenolide|Hexadecanolide|Luminide|Muscemor|Zenolide|Musk Z 4|Bicyclononalactone|Cinnamalva|Prismantol|Veraspice|Andrane|Bacdanol|Cedrafix|Cedramber|Cedryl acetate|Coniferan|Karmawood|Koavone|Kohinool|Mysantol|Orivone|Piconia|Sanjinol|Santaliff|Timbersilk|Tobacarol|Trimofix|Veramoss|Vertofix|Ambermor|Operanide|Trisamber|Ambrettolide|Methyl ionone|Damascone alpha|Damascone beta|Damascone delta|Citronellyl acetate""".split('|')]
for n in TRADE:
    if low(n) not in ents and not any(low(n)==low(x.split(' (')[0]) for x in CATX.split('|')):
        f=cfam(n)
        add(n,LFC,f)
        ents[low(n)]['d']="Trade-name aroma chemical listed on Wikipedia's List of fragrance compounds."
chem=list(ents.values())
# earlier entries: coumarin etc. already; old ones with fields
oldchem={e['n']:e for e in k['x']}
for e in chem:
    pass
k['x']=sorted(chem,key=lambda e:(e['g'],e['n']))
k['nl']="One entry is a single aroma compound or a trade-named specialty chemical; grades and dilutions of one compound are versions."
k['sel']=("Wikipedia's Perfume ingredients category (155 pages, compounds only), the aroma compounds named in Wikipedia Aroma compound, and the trade names on Wikipedia's List of fragrance compounds with grade and dilution variants merged. "
 "Family sections are the compiler's chemical and olfactive grouping, as the pages give none. Years are given only where a fetched page states them (Hedione, Iso E Super, Galaxolide, Calone, musk xylene, muscone, ethyl vanillin).")
k['xg']="Grouped by family: musks, woody and amber, floral, citrus green and marine, sweet fruity and gourmand, spice and aromatic, other."
kind(m,'Perfumer\'s alcohol & carrier oil')['x']=[]
# counts
cnt=len(k['x'])
k['sel']+=f" Covers {cnt} entries; the category's non-compound pages (concepts such as fixative, fragrance oil, gourmand, herbal distillate, nag champa) and its natural materials are in the other kinds or left out, and the List of fragrance compounds repeats compounds in many grades, so a page count is not comparable."
# cleaning m
for dp in dep.values():
    for s in dp['s']:
        for kd in s['k']:
            kd.pop('m',None)
            if kd.get('x') is not None and not kd['x'] and 'sel' not in kd:
                kd['nl']=kd.get('nl') or ""
                kd.pop('nl') if not kd['nl'] else None
out={"replaces":names,"depts":[dep[n] for n in names],"brands":[],"brand_updates":{
 "Bath & Body Works":{"own":"Bath & Body Works, Inc.","tier":"Independent","c":"United States"},
 "Victoria's Secret":{"own":"Victoria's Secret & Co.","tier":"Independent","c":"United States"},
 "Sol de Janeiro":{"own":"Groupe L'Occitane","tier":"Independent","c":"United States"}},
 "renames":{},"moves":[]}
os.makedirs(R+'out/H4_parts',exist_ok=True)
json.dump(out,open(R+'out/H4_parts/REST.tmp','w'),ensure_ascii=False)
os.rename(R+'out/H4_parts/REST.tmp',R+'out/H4_parts/REST.json')
print(cnt,EOc,os.path.getsize(R+'out/H4_parts/REST.json'))
