import json,re,os,shutil,copy
R='/home/user/Possession-Taxonomy/rebuild/'
W=R+'work/STR_J7/'
j=json.load(open(W+'bak/J7.json'))
WP='https://en.wikipedia.org/wiki/'
# ---------- index kinds
K={}
for d in j['depts']:
    for s in d['s']:
        for k in s['k']: K[k['n']]=k
before=dict(depts=len(j['depts']),shelves=sum(len(d['s']) for d in j['depts']),kinds=len(K),arch=sum(len(k.get('x',[])) for k in K.values()))
def nk(n,d,s,tt=None,a=''):
    k={'n':n,'a':a,'d':d,'s':s}
    if tt: k['tt']=tt
    return k
NEW=[
 nk('Cinsault','Still red wine from Cinsault (Cinsaut), a light, fruity grape of the south of France and South Africa, often blended or made into rosé.',WP+'List_of_grape_varieties',a='Cinsaut'),
 nk('Zweigelt','Still red wine from Zweigelt, Austria\'s most planted red grape, a cross of Blaufränkisch and St Laurent.',WP+'List_of_grape_varieties'),
 nk('Cap Classique','South African sparkling wine made by the traditional method, with the second fermentation in the bottle.',WP+'Sparkling_wine',a='Méthode Cap Classique · MCC'),
 nk('Brachetto','Sweet, lightly sparkling red wine from the Brachetto grape, made in Piedmont and low in alcohol.',WP+'Sparkling_wine'),
 nk('Sparkling Shiraz','Australian sparkling red wine made from Shiraz, usually off-dry and served chilled.',WP+'Sparkling_wine'),
 nk('Blonde ale','Pale, lightly malty and lightly hopped ale, the easy-drinking entry to craft brewing.',WP+'List_of_beer_styles',a='Golden ale · Summer ale'),
 nk('Amber & red ale','Malty copper to red ale with moderate hops, as American amber ale or Irish red ale.',WP+'List_of_beer_styles',a='American amber ale · Irish red ale',tt=[['Origin',['American amber ale','Irish red ale']]]),
 nk('Brown ale','Nutty, malty brown ale of moderate strength, brewed in English and American versions.',WP+'List_of_beer_styles',tt=[['Origin',['English brown ale','American brown ale']]]),
 nk('Rye beer','Beer in which rye replaces part of the barley malt, giving a dry, spicy, bready character.',WP+'List_of_beer_styles',a='Roggenbier'),
 nk('Blended American whiskey','American whiskey blended from straight whiskeys with neutral spirit or other whiskeys.',WP+'Whisky',a='Blended whiskey'),
 nk('Aguardiente','Clear Latin American spirit, usually distilled from sugar cane; the Colombian version is flavoured with aniseed.',WP+'Distilled_beverage',a='Aguardiente de caña'),
 nk('Flower liqueur','Sweetened spirit flavoured with flowers such as elderflower or violet.',WP+'List_of_liqueurs',tt=[['Flower',['Elderflower','Violet (crème de violette)','Rose (rosolio)']]]),
 nk('Chocolate liqueur','Sweetened spirit flavoured with cocoa, including clear crème de cacao and cream versions.',WP+'List_of_liqueurs',a='Crème de cacao',tt=[['Colour',['Clear (white crème de cacao)','Dark']],['Cream',['Without cream','Chocolate cream liqueur']]]),
 nk('Honey liqueur','Sweetened spirit flavoured with honey, often with herbs or spices, from Poland, Germany and the Caribbean.',WP+'List_of_liqueurs'),
 nk('Whisky liqueur','Sweetened whisky flavoured with honey, herbs or spices, such as Drambuie, Glayva or Irish Mist.',WP+'List_of_liqueurs'),
 nk('Kijōshu','Sweet, rich sake brewed with sake in place of some of the water, often aged to an amber colour.',WP+'Sake'),
 nk('Doburoku','Cloudy, thick, unfiltered rice drink made like sake but pressed little or not at all.',WP+'Sake'),
 nk('Apfelwein & Most','German apfelwein and Austrian or Swiss Most, dry and tart apple wines served in a stoneware jug or glass.',WP+'Cider',a='Ebbelwoi · Viez · Most'),
]
for k in NEW:
    assert k['n'] not in K; K[k['n']]=k
# archetype moves between kinds
def move_arch(frm,name,to):
    f=K[frm]; i=[x['n'] for x in f['x']].index(name); x=f['x'].pop(i); K[to].setdefault('x',[]).append(x)
move_arch('Herb & spice liqueur','St-Germain','Flower liqueur')
move_arch('Herb & spice liqueur','Drambuie','Whisky liqueur')
# ---------- demotions (versions -> m)
DEM={
 'Bordeaux red blend':['Right Bank Merlot-led blend'],'Pinotage':['Coffee Pinotage'],'Plavac Mali':['Island Plavac Mali'],
 'Carmenère':['Chilean Carmenère','Northeast Italian Carmenère'],'Petit Verdot':['Australian Petit Verdot','Ica Petit Verdot'],
 'País':['Southern Chile País'],'Kisi':['Kakhetian Kisi'],'Rkatsiteli':['Kakhetian qvevri Rkatsiteli'],'Kerner':['German Kerner'],
 'Muscat':['Austrian dry Muscat'],'Graciano':['Varietal Rioja Graciano'],'Ice wine':['Cryoextraction dessert wine'],
 'Cava':['Cava de Guarda','Cava Reserva','Cava Gran Reserva','Cava de Paraje Calificado'],'Franciacorta':['Franciacorta (non-vintage)'],
 'Munich Dunkel':['Munich Dunkel (city style)'],'Schwarzbier':['New-world black lager'],'Czech dark lager':['Czech brewery tmavý ležák'],
 'Bock':['Dunkles bock','Maibock (helles bock)'],'Doppelbock':['-ator doppelbock','Pale doppelbock'],'Baltic porter':['Baltic brewery porter'],
 'Berliner Weisse':['Revival Berliner Weisse'],'Gose':['American gose'],'Altbier':['Düsseldorf Altstadt brewpub alts','Sticke alt'],
 'Sweet stout':['Oyster stout'],'Lambic':['Faro'],'Fruit lambic':['Oude kriek','Sweetened kriek','Cantillon fruit lambics'],
 'American wild ale':['Russian River barrel-aged sours','Jester King wild ales'],'Gluten-free beer':['Gluten-free grain beer','Gluten-reduced beer'],
 'Fruit & spice beer':['Pumpkin ale','Christmas spiced beer','Gruit ale','English fruit ale'],'Rauchbier':['Spezial Rauchbier'],
 'Mezcal':['Espadín mezcal','Tobalá mezcal','Wild-agave mezcal','Mezcal de pechuga'],'Armagnac':['Vintage Armagnac','Blanche d’Armagnac'],
 'Pisco':['Pisco puro','Pisco aromático','Pisco acholado','Pisco mosto verde','Gran Pisco'],'Awamori':['Kusu','Hanazake'],
 'Pulque':['Pulque natural','Pulque curado','Canned pulque'],'Gin':['New Western dry gin'],'Orange liqueur':['Curaçao of laraha peel'],
 'Limoncello':['Crema di limoncello'],'Mead':['Traditional mead','Sack mead','Melomel','Metheglin','Braggot','Bochet','Acerglyn','Session mead','Polish mead grades'],
 'Fruit wine':['Elderberry wine','Cherry wine','Pomegranate wine','Dandelion wine','Strawberry wine','Pineapple wine'],
 'Palm wine':['West African palm wine'],
}
RANGES={'Cantillon fruit lambics','Russian River barrel-aged sours','Jester King wild ales'}
demoted=[];moved_to_m=0
for kn,names in DEM.items():
    k=K[kn]
    for nm in names:
        xs=k['x']; i=[x['n'] for x in xs].index(nm); x=xs.pop(i); demoted.append((kn,nm))
        for v in x.get('v',[]) or []:
            e=[v['n'],v.get('mk') or x.get('mk') or '']
            if e not in k.setdefault('m',[]): k['m'].append(e); moved_to_m+=1
        if nm in RANGES and x.get('mk'):
            e=[nm,x['mk']]
            if e not in k.setdefault('r',[]): k['r'].append(e)
    if not k['x']: del k['x']
# ---------- tt
for line in open(W+'tt.txt',encoding='utf8'):
    line=line.rstrip('\n')
    if not line.strip(): continue
    n,rest=line.split(' :: ')
    assert n in K,n
    groups=[]
    for g in rest.split(' ;; '):
        lab,mem=g.split('=',1); groups.append([lab,mem.split('|')])
    K[n]['tt']=groups
for n,k in K.items():
    if 't' in k:
        assert 'tt' in k,('no tt',n)
        del k['t']
# ---------- structure
def sh(n,t,ax,ks): return {'n':n,'t':t,'ax':ax,'k':ks}
D=[]
def dept(n,mode,note,t,ax,shelves):
    d={'n':n,'mode':mode,'t':t,'ax':ax,'s':shelves}
    if note: d['note']=note
    old=[x for x in j['depts'] if x['n']==n][0]
    if old.get('b'): d['b']=old['b']
    D.append(d)
dept('Red wine','variety','Grape view first; classed appellations and icon wines are the archetypes under each grape.',
 'Still red wine named for its grape or its blend, with the great appellations and icon wines under each grape; a sparkling or pink wine → Sparkling, rosé & orange wine; a sweet or fortified red → Sweet & fortified wine.',
 'Which grape names the wine: a classic grown worldwide, a blend, or a grape at home in one region?',[
 sh('Classic red grapes','The red grapes planted on every continent, each sold under its own name: Cabernet Sauvignon, Pinot Noir, Syrah; a blend of several → Red blends.','kinds by the country that made the grape famous, France first, then Italy, Spain, Argentina and California',
   ['Cabernet Sauvignon','Merlot','Cabernet Franc','Petit Verdot','Pinot Noir','Gamay','Syrah','Grenache','Cinsault','Sangiovese','Nebbiolo','Tempranillo','Malbec','Zinfandel']),
 sh('Red blends','Red wines whose name is a blend rather than one grape: Bordeaux, Rhône and Super Tuscan styles; a single grape → its own shelf.','kinds by whether the blend follows the Bordeaux pattern or another',['Bordeaux red blend','Red blend']),
 sh('Italian & Iberian red grapes','Red grapes at home in Italy, Portugal and Spain, from Barbera and Aglianico to Touriga Nacional and Mencía; Sangiovese, Nebbiolo and Tempranillo → Classic red grapes.','kinds from northern Italy through the south and Sicily to Portugal and Spain',
   ['Dolcetto','Barbera','Lagrein','Refosco','Sagrantino','Montepulciano','Aglianico','Nero d\'Avola','Nerello Mascalese','Touriga Nacional','Monastrell','Mencía','Graciano']),
 sh('Central Europe, Balkans, Greece & Caucasus red grapes','Red grapes at home from Austria and Hungary through the Balkans and Greece to Georgia: Blaufränkisch, Xinomavro, Saperavi.','kinds from Austria and Hungary south through the Balkans and Greece to Georgia',
   ['Blaufränkisch','Zweigelt','Kadarka','Plavac Mali','Prokupac','Mavrud','Xinomavro','Agiorgitiko','Saperavi','Aleksandrouli']),
 sh('Americas & southern Africa red grapes','Red grapes whose home or fame is in Chile, Uruguay, California and South Africa: Carmenère, Tannat, Pinotage; Malbec and Zinfandel → Classic red grapes.','kinds by country: Chile, Uruguay, California, South Africa',
   ['Carmenère','País','Tannat','Petite Sirah','Pinotage']),
])
dept('White wine','variety','Grape view first; classed appellations and icon wines are the archetypes.',
 'Still white wine named for its grape or its blend, with the great appellations under each grape; a sparkling wine → Sparkling, rosé & orange wine; a sweet or fortified white → Sweet & fortified wine.',
 'Which grape names the wine: a classic grown worldwide, a blend, or a grape at home in one region?',[
 sh('Classic white grapes','The white grapes planted on every continent and sold under their own name: Chardonnay, Sauvignon Blanc, Riesling.','kinds by the country that made the grape famous: France, then Germany, Austria and Spain',
   ['Chardonnay','Sauvignon Blanc','Chenin Blanc','Sémillon','Viognier','Pinot Blanc','Pinot Grigio','Gewürztraminer','Muscat','Riesling','Grüner Veltliner','Albariño']),
 sh('White blends','White wines whose name is a blend rather than one grape, such as white Bordeaux and Gemischter Satz.','',['White blend']),
 sh('Italian & Iberian white grapes','White grapes at home in Italy, Portugal and Spain, plus the Basque Txakoli; Torrontés is grown in Argentina but has Iberian roots.','kinds from northern Italy through the south to Portugal, Spain and Argentina',
   ['Arneis','Cortese','Garganega','Friulano','Vermentino','Verdicchio','Trebbiano','Pecorino','Greco','Fiano','Falanghina','Carricante','Malvasia','Arinto','Encruzado','Loureiro','Verdejo','Albillo Mayor','Godello','Txakoli','Torrontés']),
 sh('French & Swiss regional white grapes','White grapes tied to one French or Swiss region: Melon de Bourgogne, Savagnin, Altesse, Chasselas.','kinds from the Loire through the Jura and Savoie to Switzerland',
   ['Melon de Bourgogne','Savagnin','Altesse','Petite Arvine','Chasselas']),
 sh('Central Europe, Greece & Caucasus white grapes','White grapes at home from Germany east to Hungary, Greece and Georgia: Furmint, Assyrtiko, Rkatsiteli.','kinds from Germany east to Hungary, then Greece and Georgia',
   ['Müller-Thurgau','Sylvaner','Kerner','Furmint','Assyrtiko','Moschofilero','Rkatsiteli','Kisi']),
])
dept('Sparkling, rosé & orange wine','variety','Champagne by house and cuvée; other sparkling by method and appellation.',
 'Wine whose identity is its bubbles or its colour from the skins: Champagne, other sparkling wine, still rosé and orange wine; a sweet or fortified wine → Sweet & fortified wine.',
 'Is the wine known for its bubbles (and where and how they were made) or for a colour taken from the grape skins?',[
 sh('Champagne','Sparkling wine from the Champagne region, made by the traditional method; sparkling from elsewhere → Other sparkling wine.','kinds by rank of cuvée: everyday non-vintage, single-year vintage, prestige, then pink',
   ['Non-vintage Champagne','Vintage Champagne','Prestige cuvée Champagne','Rosé Champagne']),
 sh('Other sparkling wine','Sparkling wine from outside Champagne: Prosecco, Cava, Crémant, Franciacorta, Lambrusco; a still wine → its grape shelf.','kinds by how the bubbles are made: bottle fermentation, then tank or transfer, then ancestral',
   ['Cava','Crémant','Franciacorta','Cap Classique','Traditional-method sparkling wine','Prosecco','Sekt','Asti & Moscato d\'Asti','Lambrusco','Brachetto','Sparkling Shiraz','Pétillant naturel']),
 sh('Rosé & orange wine','Still wines coloured by the skins: pink rosé and amber skin-contact orange wine; a rosé with bubbles → Champagne or Other sparkling wine.','kinds by how long the juice stays on the skins: short for rosé, long for orange',['Rosé','Orange wine']),
])
dept('Sweet & fortified wine','variety',None,
 'Wine made sweet by concentrated grapes, made strong with added grape spirit, or flavoured with botanicals: Sauternes, Port, Sherry, vermouth; a dry table wine → its grape shelf; a spirit → Spirits.',
 'What gives the wine its sweetness or strength: concentrated grapes, added grape spirit, or added flavourings?',[
 sh('Sweet wine','Wines sweet from grapes concentrated by noble rot, extra hang time, frost or drying: Sauternes, Tokaji, ice wine; a wine with added spirit → Fortified wine.','kinds by how the grapes were concentrated: late harvest, noble rot, frost, drying',
   ['Late-harvest wine','Sauternes & Barsac','Tokaji','Ice wine','Passito & dried-grape wine']),
 sh('Fortified wine','Wines with grape spirit added: Port, Sherry, Madeira, Marsala; a wine flavoured with botanicals → Aromatised wine.','kinds by when the spirit goes in: during fermentation first, then after it',
   ['Port','Vin doux naturel','Regional fortified wine','Sherry','Madeira','Marsala']),
 sh('Aromatised wine','Wines flavoured with herbs, bark, fruit or resin: vermouth, quinquina, retsina, sangria and mulled wine.','kinds by what is infused: wormwood and botanicals, cinchona bark, pine resin, fruit and spices',
   ['Vermouth','Quinquina & americano','Retsina','Sangria & mulled wine']),
])
dept('Beer','variety',"Kinds follow the BJCP style guidelines; breweries go in the brand register; archetypes are reference beers named by BJCP or the style's originator.",
 'Drinks brewed from malted grain and hops, sold by style: lagers, ales, wheat, Belgian, sour and non-barley brews; an alcohol-free beer → No & low alcohol; beer mixed with lemonade → Ready-to-drink & mixed packs.',
 'How is it fermented and what character does it have: cool-fermented lager, ale (pale, brown, dark, wheat, Belgian), wild-soured, or brewed from another grain?',[
 sh('Pale & amber lagers','Cool-fermented lagers from pale gold to amber, from international pale lager and Pils to Märzen and Vienna lager.','kinds from the lightest, most neutral lager to the maltier amber lager',
   ['International pale lager','American light lager','Czech pale lager','German Pils','Munich Helles','Dortmunder Export','Kellerbier','Festbier','Märzen','Vienna lager']),
 sh('Dark lagers & bocks','Cool-fermented dark lagers and strong bocks, including smoked and Baltic types; a dark top-fermented beer → Porter & stout.','kinds from dark lager to smoked, then bock, double bock and ice bock',
   ['Munich Dunkel','Czech dark lager','Schwarzbier','Rauchbier','Bock','Doppelbock','Eisbock','Baltic porter']),
 sh('Pale ales, IPA & bitter','Hop-forward pale ales, IPAs and English bitter, from blonde ale to double IPA; a malty amber or brown ale → Amber, brown & strong ales.','kinds by hop level and strength, American styles before English',
   ['Blonde ale','American pale ale','American IPA','Hazy IPA','Double IPA','English IPA','Bitter']),
 sh('Amber, brown & strong ales','Malt-led ales from amber and brown to the strong, aged Scotch ale, old ale and barleywine; hop-led pale ales → Pale ales, IPA & bitter.','kinds from light-bodied malty ales up to strong, aged ales',
   ['Amber & red ale','Brown ale','Mild','Scottish & Scotch ale','Old ale','Barleywine']),
 sh('Porter & stout','Dark top-fermented beers with roast malt, from porter to imperial stout; a dark lager → Dark lagers & bocks.','kinds by roast and strength, porter first and imperial stout last',
   ['English porter','American porter','Irish stout','Oatmeal stout','Sweet stout','Foreign extra stout','American stout','Imperial stout']),
 sh('Wheat beers & hybrid ales','Wheat beers, and hybrids that use ale yeast with cold conditioning: Weissbier, Witbier, Kölsch, Altbier.','kinds from wheat beers to the lager-like hybrid ales',
   ['Weissbier','Witbier','American wheat beer','Kölsch','Altbier','California common','Cream ale']),
 sh('Belgian & Trappist ales','Belgian-yeast ales from the Trappist, abbey and farmhouse traditions; a wild-soured Belgian beer → Sour & wild beers.','kinds by strength, from single and blond through farmhouse ales to strong ales',
   ['Belgian single','Belgian blond ale','Saison','Bière de garde','Dubbel','Tripel','Belgian golden strong ale','Belgian dark strong ale']),
 sh('Sour & wild beers','Beers soured by wild yeast, bacteria or kettle souring: lambic, gueuze, Flanders red, Berliner Weisse, Gose.','kinds by how the sourness arrives: spontaneous fermentation, blended barrel ageing, wheat sours, wild yeast',
   ['Lambic','Gueuze','Fruit lambic','Flanders red ale','Oud bruin','Berliner Weisse','Gose','American wild ale']),
 sh('Traditional, specialty & gluten-free beers','Beers brewed from grains other than barley, or with fruit and spice: sorghum, millet, maize, rye, sahti; the barley styles above stay on their shelves.','kinds by what replaces or adds to barley malt',
   ['Sorghum beer','Millet beer','Maize beer','Banana beer','Rye beer','Sahti','Gluten-free beer','Fruit & spice beer']),
])
dept('Whisky','variety','Country and style first; Scotch by region → distillery → bottling; distilleries in the brand register.',
 'Spirit distilled from fermented grain mash and aged in wood: Scotch, Irish, American, Japanese, Canadian and world whisky; an unaged grain spirit or a flavoured one → Spirits; a whisky-based sweet drink → Liqueurs.',
 'Which country makes it and in what style: single malt by region, Scotch blends and grain, American whiskey by grain, Irish, or Japanese, Canadian and world whisky?',[
 sh('Single malt Scotch by region','Scotch malt whisky from one distillery, sold by region: Islay, Speyside, Highland, Islands, Campbeltown, Lowland; a blend of distilleries → Blended & grain Scotch whisky.','kinds by region, the peaty west first: Islay, Speyside, Highland, Islands, Campbeltown, Lowland, then independent bottlings',
   ['Islay single malt Scotch','Speyside single malt Scotch','Highland single malt Scotch','Island single malt Scotch','Campbeltown single malt Scotch','Lowland single malt Scotch','Independent bottlings of Scotch single malt']),
 sh('Blended & grain Scotch whisky','Scotch that is a blend or is made from grain, not one distillery\'s malt: Johnnie Walker, Monkey Shoulder, single grain.','kinds from blends of malt and grain to malt-only blends and grain-only whisky',
   ['Blended Scotch whisky','Blended malt Scotch whisky','Single grain Scotch whisky','Blended grain Scotch whisky']),
 sh('American whiskey','Whiskey made in the United States, named for its main grain: bourbon, Tennessee, rye, wheat, corn, malt.','kinds by main grain, corn-led bourbon first, then rye, wheat, corn, malt and blends',
   ['Bourbon','Tennessee whiskey','Rye whiskey','Wheat whiskey','Corn whiskey','American single malt whiskey','Blended American whiskey']),
 sh('Irish whiskey','Whiskey made in Ireland, from the distinctive single pot still to blends, single malt and single grain.','kinds from the Irish pot still original to the wider Irish styles',
   ['Irish single pot still whiskey','Irish whiskey']),
 sh('Japanese, Canadian & world whisky','Whisky from Japan, Canada and every other producing country, from Taiwan and India to Wales and Sweden.','kinds by country, the longest traditions first',
   ['Japanese whisky','Canadian whisky','World whisky']),
])
dept('Spirits','variety','By base material and tradition; grade ladders where the law sets them.',
 'Unsweetened distilled drinks other than whisky, sold by base material and tradition: gin, vodka, rum, agave spirits, brandy, aniseed spirits and Asian spirits; a sweetened one → Liqueurs.',
 'What is the spirit made from and flavoured with: grain and botanicals, sugar cane, agave, grapes and fruit, aniseed, or Asian rice and sorghum?',[
 sh('Gin, vodka & aquavit','Spirits distilled from grain or potato, plain or flavoured with botanicals: vodka, gin, genever, aquavit; a sweetened version → Liqueurs.','kinds by how much flavour is added: plain vodka, flavoured vodka, then botanical gin, genever and aquavit',
   ['Vodka','Flavoured vodka','Gin','Genever','Aquavit']),
 sh('Rum & cane spirits','Spirits distilled from sugar cane juice, syrup or molasses, or from palm sap: rum, rhum agricole, cachaça, arrack.','kinds by what is distilled: molasses, fresh cane juice, cane aguardiente, sap',
   ['Molasses rum','Spiced rum','Rhum agricole','Cachaça','Aguardiente','Arrack']),
 sh('Agave spirits','Spirits distilled from agave and related desert plants in Mexico: tequila, mezcal, raicilla, bacanora, sotol.','kinds from the best-known protected spirit to regional ones',
   ['Tequila','Mezcal','Raicilla','Bacanora','Sotol']),
 sh('Brandy & eau de vie','Spirits distilled from grape wine, grape pomace, apples or other fruit: Cognac, Armagnac, Calvados, grappa, fruit brandy.','kinds by what is distilled: wine, grape pomace, apple cider, other fruit',
   ['Cognac','Armagnac','Grape brandy','Pisco','Grappa & pomace brandy','Calvados','Fruit brandy']),
 sh('Anise spirits & absinthe','Spirits flavoured with aniseed, fennel or wormwood: pastis, ouzo, arak and rakı, absinthe; a sweetened anise drink → Liqueurs.','kinds from sweet aniseed spirits to bitter wormwood absinthe',
   ['Pastis','Ouzo','Arak & rakı','Absinthe']),
 sh('Asian spirits','Spirits distilled from rice, sorghum and other grains in China, Japan and Korea: baijiu, shochu, awamori, soju.','kinds by country: China, Japan, Okinawa, Korea',
   ['Baijiu','Shochu','Awamori','Soju']),
])
dept('Liqueurs','variety',None,
 'Sweetened and flavoured spirits for sipping or mixing: fruit and flower, herb and bitter, and cream, coffee and nut liqueurs; an unsweetened spirit → Spirits; a fortified wine → Sweet & fortified wine.',
 'What flavours the sweetened spirit: fruit and flowers, herbs and bitter roots, or rich dessert flavours such as cream, coffee, nuts and chocolate?',[
 sh('Fruit & flower liqueurs','Liqueurs flavoured with fruit, citrus peel or flowers: curaçao, cassis, cherry, plum, elderflower; a liqueur of herbs → Herb, spice & bitter liqueurs.','kinds from citrus to other fruit, then flowers',
   ['Orange liqueur','Limoncello','Fruit liqueur','Sloe gin','Flower liqueur']),
 sh('Herb, spice & bitter liqueurs','Liqueurs flavoured with herbs, spices, aniseed or bitter roots: Chartreuse, Jägermeister, sambuca, Campari, amaro.','kinds from sweet herbal liqueurs to bitter amari',
   ['Herb & spice liqueur','Anise liqueur','Amaro & bitter liqueur']),
 sh('Cream, coffee & nut liqueurs','Rich, sweet liqueurs based on cream, coffee, nuts, chocolate, honey or whisky: Baileys, Kahlúa, amaretto, Drambuie.','kinds from cream-based to coffee, nut, chocolate, honey and whisky liqueurs',
   ['Cream liqueur','Coffee liqueur','Nut liqueur','Chocolate liqueur','Honey liqueur','Whisky liqueur']),
])
dept('Sake & rice wine','variety','Sake by the legal grade ladder; Korean and Chinese rice wines alongside.',
 'Drinks brewed from rice with a mould starter: Japanese sake, Korean makgeolli and cheongju, Chinese huangjiu; a distilled rice spirit → Spirits.',
 'Which country\'s rice-brewing tradition is it: Japan, Korea or China?',[
 sh('Sake','Japanese rice wine, graded by how far the rice is polished and whether alcohol is added: junmai, ginjo, daiginjo, nigori, kijōshu; distilled shochu → Spirits.','kinds from graded clear sake to ordinary, cloudy, sparkling, infused and sweet or rough specials',
   ['Sake (junmai, honjozo, ginjo & daiginjo)','Futsūshu','Nigori sake','Sparkling sake','Infused sake','Kijōshu','Doburoku']),
 sh('Korean & Chinese rice wine','Rice wines from Korea and China: cloudy makgeolli, clear cheongju, amber Shaoxing huangjiu.','kinds from cloudy Korean makgeolli to clear cheongju and Chinese huangjiu',
   ['Makgeolli','Cheongju','Huangjiu']),
])
dept('Cider, perry & mead','variety',None,
 'Drinks fermented from apples, pears, honey, other fruit or sap rather than grapes or grain: cider, perry, mead, fruit wine, palm wine, pulque; an apple spirit → Spirits.',
 'What is fermented: apples and pears, honey, other fruit, or plant sap?',[
 sh('Cider & perry','Fermented apple and pear drinks, by country of tradition: British, French and Spanish cider, German apfelwein, ice cider, pommeau and perry.','kinds from the cider countries (Britain, France, Spain, Germany) to special treatments, then pear',
   ['British & Irish cider','French cider','Spanish cider','Apfelwein & Most','Ice cider','Fruit & flavoured cider','Pommeau','Perry']),
 sh('Mead, fruit & sap wines','Wines fermented from honey, other fruit or plant sap: mead, fruit wine, palm wine, pulque.','kinds by sugar source: honey, other fruit, palm sap, agave sap',
   ['Mead','Fruit wine','Palm wine','Pulque']),
])
dept('Ready-to-drink & mixed packs','tier',None,
 'Alcoholic drinks sold pre-mixed in a can or bottle: cocktails, hard seltzer, malt coolers, spritzers and radlers; a plain beer or wine → its own department.',
 'What alcoholic base is mixed: spirit, malt or brewed sugar, wine, or beer?',[
 sh('Ready-to-drink','Pre-mixed alcoholic drinks sold chilled and ready to open: canned cocktails, hard seltzer, malt coolers, wine spritzers, radler.','kinds by base alcohol: spirit, malt or sugar, wine, beer',
   ['Ready-to-drink cocktail','Flavoured malt beverage','Hard seltzer','Wine spritzer','Radler & shandy']),
])
dept('No & low alcohol','mixed','Alcohol-free (≤0.5%) and low-alcohol versions of the drinks above.',
 'Alcohol-free (0.5% or less) and low-alcohol stand-ins for beer, wine, sparkling wine, spirits and aperitifs; a soft drink that does not imitate alcohol → J9.',
 'Which alcoholic drink is it standing in for: beer, still wine, sparkling wine, spirit or aperitif?',[
 sh('No & low alcohol','Alcohol-free and low-alcohol drinks made to replace beer, wine, spirits or aperitifs.','kinds by the drink imitated: beer, wine, sparkling wine, spirit, aperitif',
   ['Alcohol-free beer','Alcohol-free wine','Alcohol-free sparkling wine','Non-alcoholic spirit','Alcohol-free aperitif']),
])
# check coverage
used=[n for d in D for s in d['s'] for s_ in [s] for n in s['k']]
assert len(used)==len(set(used)),[n for n in used if used.count(n)>1]
miss=set(K)-set(used); assert not miss,miss
extra=set(used)-set(K); assert not extra,extra
for d in D:
    for s in d['s']: s['k']=[K[n] for n in s['k']]
# ---------- see links
SEE={
 'Pecorino':[['J3','Pecorino','the sheep cheese of the same name']],
 'Radler & shandy':[['J9','Ginger beer','shandygaff uses ginger beer']],
 'Gin':[['J9','Tonic water','the usual mixer']],
 'Sake (junmai, honjozo, ginjo & daiginjo)':[['J5','Mirin','sweet sake-based cooking seasoning']],
 'Huangjiu':[['J5','Shaoxing and Chinese cooking wine','cooking version of the same wine']],
 'British & Irish cider':[['J5','Cider vinegar','vinegar made from cider']],
 'Amaro & bitter liqueur':[['J5','Cooking bitters','bitters for cooking']],
 'Hard seltzer':[['J9','Flavoured sparkling water','non-alcoholic equivalent']],
 'Port':[['B5','Decanter','vintage Port is decanted']],
 'Red blend':[['B5','Wine glass','glass shapes for wine']],
 'Cocktail':[],
 'Ready-to-drink cocktail':[['B5','Cocktail shaker','the home-made alternative']],
 'Alcohol-free aperitif':[['J9','Tonic water','mixers and soft drinks']],
 'Sweet stout':[],
 'Rye beer':[],
}
SEE={k:v for k,v in SEE.items() if v}
for n,v in SEE.items(): K[n]['see']=v
# verify see targets
import glob
tgt={}
for f in glob.glob(R+'reader/[A-J]*.json'):
    if os.path.basename(f).startswith('_'): continue
    dd=json.load(open(f)); tgt[dd['c']]={k['n'] for d in dd['depts'] for s in d['s'] for k in s['k']}
for n,v in SEE.items():
    for c,kn,_ in v:
        if c=='J7': assert kn in K
        else: assert kn in tgt[c],(c,kn)
# ---------- category
j['depts']=D
j['ax']='What is the drink made from and how: fermented grapes, brewed grain, distilled spirit, sweetened liqueur, rice, apples and honey, or a mixed or alcohol-free version?'
j['key']=[
 '1. Is it an alcohol-free (0.5% or less) or low-alcohol stand-in for beer, wine, spirits or an aperitif? → No & low alcohol',
 '2. Is it sold pre-mixed in a can or bottle (canned cocktail, hard seltzer, malt cooler, spritzer, radler)? → Ready-to-drink & mixed packs',
 '3. Is it brewed from rice with a mould starter (sake, makgeolli, huangjiu)? → Sake & rice wine',
 '4. Is it fermented from apples, pears, honey, other fruit or sap (cider, perry, mead, palm wine)? → Cider, perry & mead',
 '5. Is it brewed from malted grain and hops? → Beer',
 '6. Is it a sweetened, flavoured spirit (cream, fruit, herb or bitter liqueur)? → Liqueurs',
 '7. Is it whisky distilled from grain mash and aged in wood? → Whisky',
 '8. Is it any other distilled spirit (gin, vodka, rum, tequila, brandy, aniseed spirit, baijiu)? → Spirits',
 '9. Is it a wine with bubbles, or a rosé or orange wine? → Sparkling, rosé & orange wine',
 '10. Is it a sweet, fortified or flavoured wine (Sauternes, Port, Sherry, vermouth)? → Sweet & fortified wine',
 '11. Is it a still white wine? → White wine',
 '12. Is it a still red wine? → Red wine',
 '<i>Precedence: a whisky liqueur is a liqueur (step 6) before a whisky (step 7); an alcohol-free version of any drink goes to step 1; a pink sparkling wine is sparkling (step 9); a sweet or fortified red or white wine is step 10 before the colour steps.</i>',
]
j['lead']='Alcoholic drinks a person buys, cellars or collects, grouped by what they are made from and how: wine by colour and grape with appellation archetypes, beer by BJCP style family, whisky by country and style, other spirits, liqueurs, sake and rice wines, cider and mead, ready-to-drink, and no- and low-alcohol alternatives, with producers, breweries and distilleries in the brand register.'
after=dict(depts=len(D),shelves=sum(len(d['s']) for d in D),kinds=len(K),arch=sum(len(k.get('x',[])) for d in D for s in d['s'] for k in s['k']))
json.dump(j,open(W+'J7.new.json','w'),ensure_ascii=False,indent=1)
os.replace(W+'J7.new.json',R+'out/J7.json')
json.dump({},open(R+'out/J7_renames.json','w'))
json.dump(dict(before=before,after=after,demoted=demoted,moved_to_m=moved_to_m,new=[k['n'] for k in NEW]),open(W+'stats.json','w'),ensure_ascii=False,indent=1)
print(before,after,len(demoted),moved_to_m,os.path.getsize(R+'out/J7.json'))
