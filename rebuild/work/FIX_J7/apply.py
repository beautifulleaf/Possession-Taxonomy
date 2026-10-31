import json,copy
d=json.load(open('out/J7.json'))
B=json.load(open('out/J7_brands.json'))
bl=B['b']
W='https://en.wikipedia.org/wiki/'
def kind(dept,name):
    for dp in d['depts']:
        if dp['n']==dept:
            for s in dp['s']:
                for k in s['k']:
                    if k['n']==name: return s,k
    raise KeyError(name)
def shelf(dept,name):
    for dp in d['depts']:
        if dp['n']==dept:
            for s in dp['s']:
                if s['n']==name: return s
    raise KeyError(name)
def arch(n,mk,y,s,dsc,vs=(),dt=''):
    return {"n":n,"a":"","d":dsc,"mk":mk,"y":y,"s":s,"v":[{"n":v,"mk":mk,"y":"","d":""} for v in vs],"dt":dt}
def addb(n,c,f,seg,kf,dsc,s,sig=()):
    if n.lower() in {x['n'].lower() for x in bl}: return
    e={'n':n,'c':c,'f':f,'seg':seg,'d':dsc,'sig':list(sig),'rel':[],'s':s,'kf':kf}
    bl.append(e)
# ---- J7-1 Scotch
s,sm=kind('Whisky','Single malt Scotch whisky')
old=sm['x']; models=sm['m']
reg={'Glenfiddich 12':'Speyside','The Macallan Sherry Oak':'Speyside','The Glenlivet 12':'Speyside','Lagavulin 16':'Islay','Laphroaig 10':'Islay','Ardbeg Ten':'Islay','Talisker 10':'Islands','Highland Park 12':'Islands','Springbank 10':'Campbeltown','The Balvenie DoubleWood':'Speyside','Glenmorangie Original':'Highland','Oban 14':'Highland','Bowmore 12':'Islay',"The GlenDronach 12 Original":'Highland',"Aberlour A'bunadh":'Speyside'}
mreg={'Deanston':'Highland','Glen Moray':'Speyside','Glenallachie':'Speyside','Ian Macleod Distillers':'Highland','Loch Lomond':'Highland','Rosebank':'Lowland','Royal Brackla':'Highland','Scapa':'Islands','Tormore':'Speyside','Torabhaig':'Islands',"Nc'nean":'Highland',"Macleod's":'Highland','East Asia Whisky Company':'Islay','Spiritfilled':'Speyside','':'Speyside'}
new={r:[] for r in ['Islay','Speyside','Highland','Islands','Campbeltown','Lowland']}
for x in old: new[reg[x['n']]].append(x)
S=lambda t:W+t
new['Islay']+= [
 arch("Bruichladdich","Bruichladdich","1881 (distillery)",S('Bruichladdich_distillery'),"Rhinns of Islay distillery whose unpeated Bruichladdich, peated Port Charlotte and heavily peated Octomore are separate lines.",["Classic Laddie","Port Charlotte","Octomore"],"peat level · cask type · age"),
 arch("Caol Ila","Caol Ila","1846",S('Caol_Ila_distillery'),"Islay distillery near Port Askaig; most output goes to blends, with 12-year-old and older single malts.",["Caol Ila 12 Year Old","Caol Ila Cask Strength","Caol Ila 18 Year Old","Caol Ila 25 Year Old"],"age · cask strength"),
 arch("Kilchoman","Kilchoman","2005",S('Kilchoman_distillery'),"Farm distillery on north-west Islay, begun in 2005; core expressions bottled at 46% ABV.",["Machir Bay","Sanaig","Loch Gorm"],"cask type · ABV")]
new['Speyside']+= [
 arch("Glenfarclas","Glenfarclas","1836 (licensed)",S('Glenfarclas_distillery'),"Ballindalloch distillery in Strathspey known for a 60% ABV cask-strength 105 and a vintage Family Casks series.",["Glenfarclas 105 Cask Strength","Family Casks"],"age · cask strength · vintage"),
 arch("Mortlach","Mortlach","1823",S('Mortlach_distillery'),"Dufftown distillery founded by James Findlater; Diageo markets a small range of Mortlach single malts.",["Mortlach Rare Old","Mortlach Special Strength","Mortlach 18 Year Old","Mortlach 25 Year Old"],"age")]
new['Highland']+= [
 arch("The Dalmore","Dalmore","1839",S('Dalmore_distillery'),"Alness distillery on the Cromarty Firth, founded by Alexander Matheson; 12- to 25-year-old core range.",["Dalmore 12 Year Old","Dalmore 15 Year Old","Dalmore 18 Year Old","Dalmore 25 Year Old"],"age · cask finish"),
 arch("Clynelish","Clynelish","1967 (current distillery)",S('Clynelish_distillery'),"Brora-area Highland distillery; the current building dates from 1967 beside the original 1819 site.",["Clynelish 14 Year Old","Clynelish Distillery Only Bottling"],"age · cask type")]
for dm in models:
    r=mreg[dm[1]]
    new[r].append(None) if False else None
mod={r:[m for m in models if mreg[m[1]]==r] for r in new}
defs={'Islay':'Single malt whisky from Islay distilleries, Scotland.','Speyside':'Single malt whisky from Speyside distilleries around the River Spey, Scotland.','Highland':'Single malt whisky from the Highland region of Scotland, excluding Speyside and the islands.','Islands':'Single malt whisky from the Scottish island distilleries other than Islay (Orkney, Skye and others).','Campbeltown':'Single malt whisky from the Campbeltown region of the Kintyre peninsula, Scotland.','Lowland':'Single malt whisky from the Lowland region of Scotland.'}
nm={'Islay':'Islay single malt Scotch','Speyside':'Speyside single malt Scotch','Highland':'Highland single malt Scotch','Islands':'Island single malt Scotch','Campbeltown':'Campbeltown single malt Scotch','Lowland':'Lowland single malt Scotch'}
shk=[]
common=['Peated','Unpeated','Sherry cask','Bourbon cask','Cask strength']
for r in new:
    k={"n":nm[r],"a":"%s single malt"%r+(" · Single malt Scotch whisky" if r=='Speyside' else ''),"d":defs[r],"t":common,"s":sm['s'],"x":new[r],"m":mod[r]}
    shk.append(k)
ib=[ arch("Gordon & MacPhail","Gordon & MacPhail","1895",S('Gordon_%26_MacPhail'),"Elgin independent bottler owned by the Urquhart family, with ranges such as Generations and Connoisseurs Choice.",["Generations","Connoisseurs Choice"],"distillery · vintage · cask type"),
    arch("William Cadenhead","William Cadenhead","1842","https://scotchwhisky.com/whiskypedia/2296/william-cadenhead/","Independent bottler owned by the Springbank owner since 1972; single-cask malts, not chill-filtered or coloured.",[],"distillery · vintage · cask type"),
    arch("Signatory Vintage","Signatory Vintage","1988","https://scotchwhisky.com/whiskypedia/2272/signatory-vintage-scotch-whisky-company/","Independent bottler founded by Andrew Symington; owns Edradour distillery and releases about 50 single malts at a time.",[],"distillery · vintage · cask type")]
shk.append({"n":"Independent bottlings of Scotch single malt","a":"Independent bottlers · Single malt Scotch whisky (independent bottling)","d":"Single malts bottled by firms that buy or mature casks from distilleries, sold under the bottler's name.","t":["Single cask","Cask strength","Non-chill-filtered"],"s":"https://scotchwhisky.com/whiskypedia/2296/william-cadenhead/","x":ib,"m":[]})
# replace in shelf: put region shelf
for dp in d['depts']:
    if dp['n']=='Whisky':
        sh=[x for x in dp['s'] if x['n']=='Scotch whisky'][0]
        sh['k']=[k for k in sh['k'] if k is not sm]
        i=dp['s'].index(sh)
        dp['s'].insert(i,{"n":"Single malt Scotch by region","k":shk})
# brands
addb('Bruichladdich','United Kingdom','1881','Premium','Islay malt','Islay distillery making unpeated, peated and heavily peated single malts.',S('Bruichladdich_distillery'),['Octomore','Port Charlotte'])
addb('Caol Ila','United Kingdom','1846','Mainstream','Islay malt','Islay distillery near Port Askaig, mostly supplying blends.',S('Caol_Ila_distillery'))
addb('Kilchoman','United Kingdom','2005','Artisan & independent','Farm distillery','Islay farm distillery producing single malts since 2005.',S('Kilchoman_distillery'),['Machir Bay'])
addb('Glenfarclas','United Kingdom','1836','Heritage manufactory','Family distillery','Speyside distillery in Ballindalloch, known for the 105 cask strength.',S('Glenfarclas_distillery'),['105','Family Casks'])
addb('Mortlach','United Kingdom','1823','Premium','Speyside malt','Dufftown distillery founded by James Findlater.',S('Mortlach_distillery'))
addb('Dalmore','United Kingdom','1839','Premium','Highland malt','Alness distillery on the Cromarty Firth.',S('Dalmore_distillery'))
addb('Clynelish','United Kingdom','1967','Specialist','Highland malt','Highland distillery near Brora.',S('Clynelish_distillery'))
addb('Gordon & MacPhail','United Kingdom','1895','Heritage manufactory','Independent bottler','Elgin independent bottler and owner of Benromach distillery.',S('Gordon_%26_MacPhail'),['Generations','Connoisseurs Choice'])
addb('William Cadenhead','United Kingdom','1842','Heritage manufactory','Independent bottler','Aberdeen-founded independent bottler based in Campbeltown, owned by the Springbank owner.','https://scotchwhisky.com/whiskypedia/2296/william-cadenhead/')
addb('Signatory Vintage','United Kingdom','1988','Artisan & independent','Independent bottler','Independent bottler founded by Andrew Symington; owns Edradour distillery.','https://scotchwhisky.com/whiskypedia/2272/signatory-vintage-scotch-whisky-company/')
# ---- J7-2
lk=W+'List_of_rum_brands'
addb('Foursquare','Barbados','1995','Artisan & independent','Barbados rum','Barbados rum distillery in Four Roads, Saint Philip, founded by David Seale.',W+'Foursquare_Rum_Distillery',['Exceptional Cask Selection'])
addb('Zacapa','Guatemala','1976','Premium','Guatemalan rum','Guatemalan aged rum introduced in 1976 for the 100th anniversary of the town of Zacapa.',W+'Ron_Zacapa_Centenario',['Centenario 23'])
addb('Worthy Park','Jamaica','','Artisan & independent','Jamaican rum','Jamaican rum brand listed in the Wikipedia list of rum brands.',lk)
addb('Smith & Cross','Jamaica','','Specialist','Jamaican rum','Jamaican rum brand listed in the Wikipedia list of rum brands.',lk)
addb('Cynar','Italy','1952','Mainstream','Artichoke amaro','Bittersweet amaro made from 13 herbs, mostly artichoke; owned by Campari Group.',W+'Cynar')
addb('Ramazzotti','Italy','1815','Mainstream','Amaro','Amaro first made in Milan by Ausano Ramazzotti; owned by Pernod Ricard.',W+'Ramazzotti_(liqueur)')
addb('Braulio','Italy','1875','Heritage manufactory','Alpine amaro','Herbal amaro from Bormio in the Valtellina, recipe dating from 1826.',W+'Braulio_(liqueur)')
addb('Amaro Lucano','Italy','1894','Heritage manufactory','Amaro','Family-owned herbal amaro made in Pisticci, Basilicata.',W+'Amaro_Lucano')
addb('Suze','France','1889','Mainstream','Gentian bitters','Gentian-flavoured French bitters apéritif, renamed Suze in 1898; owned by Pernod Ricard.',W+'Suze_(drink)')
s,k=kind('Spirits','Molasses rum')
k['x'].append(arch("Foursquare Exceptional Cask Selection","Foursquare","1995 (distillery)",W+'Foursquare_Rum_Distillery',"Signature series from the Barbados Foursquare distillery, run by David Seale since 1996.",[],"blend · age · cask finish"))
s,k=kind('Liqueurs','Amaro & bitter liqueur')
for n,mk,y,u,dd in [("Cynar","Cynar","1952",'Cynar',"Dark bittersweet amaro of 13 herbs, chiefly artichoke, at 16.5% ABV."),
 ("Ramazzotti","Ramazzotti","1815",'Ramazzotti_(liqueur)',"Bitter digestif from Milan macerating at least 33 roots and herbs, at 30% ABV."),
 ("Braulio","Braulio","1826 (recipe)",'Braulio_(liqueur)',"Alpine herbal amaro from Bormio in the Valtellina."),
 ("Amaro Lucano","Amaro Lucano","1894",'Amaro_Lucano',"Herbal amaro from Pisticci, Basilicata, created by Pasquale Vena."),
 ("Suze","Suze","1889",'Suze_(drink)',"Yellow gentian-root bitters drunk as an apéritif, 15% ABV in most of Europe.")]:
    if n not in [x['n'] for x in k['x']]: k.setdefault('x',[]).append(arch(n,mk,y,W+u,dd))
# ---- J7-3
def newkind(dept,shn,n,u,dd,a=''):
    sh=shelf(dept,shn)
    if any(n.lower()==kk['n'].lower() for dp in d['depts'] for ss in dp['s'] for kk in ss['k']): return
    sh['k'].append({"n":n,"a":a,"d":dd,"s":W+u})
for dp,shn,n,u,dd,a in [
 ('White wine','White blends & more white grapes','Sylvaner','Sylvaner','White grape grown mainly in Alsace and Germany, strongest in Franconia.','Silvaner'),
 ('White wine','White blends & more white grapes','Müller-Thurgau','M%C3%BCller-Thurgau','White grape bred in 1882 at Geisenheim; grown across Germany, Austria and central Europe.','Rivaner'),
 ('White wine','White blends & more white grapes','Chasselas','Chasselas','White grape whose main home is Switzerland, sold widely as Fendant.','Fendant'),
 ('White wine','White blends & more white grapes','Moschofilero','Moschofilero','Fragrant pink-skinned Greek grape with its main base in the Peloponnese.',''),
 ('White wine','Italian & Iberian white grapes','Arneis','Arneis','White Piedmont grape grown mainly in Roero and the Langhe.',''),
 ('White wine','Italian & Iberian white grapes','Cortese','Cortese','White grape of south-east Piedmont, best known for Gavi (Cortese di Gavi DOCG).','Gavi'),
 ('White wine','Italian & Iberian white grapes','Greco','Greco_(grape)','Italian grape in white and black forms; Greco di Tufo in Campania, Greco nero in Calabria.','Greco di Tufo'),
 ('White wine','Italian & Iberian white grapes','Carricante','Carricante','Sicilian white grape grown on the slopes of Mount Etna; main variety of Etna DOC.',''),
 ('White wine','Italian & Iberian white grapes','Arinto','Arinto','Portuguese white grape grown mainly in Bucelas, Tejo and Vinho Verde.','Arinto de Bucelas'),
 ('White wine','Italian & Iberian white grapes','Encruzado','Encruzado','Portuguese white grape grown chiefly in the Dão region, mostly used in blends.',''),
 ('White wine','Italian & Iberian white grapes','Txakoli','Txakoli','Crisp, dry, lightly fizzy white wine from the Basque Country, Cantabria and northern Burgos.','Txakolina · Chacolí'),
 ('Red wine','More red grapes','Agiorgitiko','Agiorgitiko','Red Greek grape, the most planted in Greece in 2012, grown mainly in Nemea.','Saint George'),
 ('Red wine','More red grapes','Mavrud','Mavrud','Red Balkan grape grown mainly in Bulgaria\'s Thrace region.',''),
 ('Red wine','More red grapes','Kadarka','Kadarka','Dark-skinned red grape grown chiefly in Hungary, Romania, Bulgaria and Slovakia.',''),
 ('Red wine','More red grapes','Petite Sirah','Petite_Sirah','Name used in the US and Israel for Durif, a red grape grown in Australia, California, France and Israel.','Durif'),
 ('Red wine','Italian & Iberian red grapes','Sagrantino','Sagrantino','Dark-skinned red grape native to Umbria, grown mainly around Montefalco.',''),
 ('Red wine','Italian & Iberian red grapes','Lagrein','Lagrein','Red grape from the valleys of South Tyrol, in Trentino-Alto Adige.','')]:
    newkind(dp,shn,n,u,dd,a)
addb('Egon Müller','Germany','','Premium','Saar Riesling','Scharzhof estate at Wiltingen in the Saar, Mosel, run by the sixth generation of the family.',W+'Egon_M%C3%BCller_Scharzhof',['Scharzhofberger'])
addb('Giacomo Conterno','Italy','','Premium','Barolo','Monforte d\'Alba producer of traditional Barolo, including Monfortino riserva.',W+'Giacomo_Conterno',['Monfortino'])
addb('Domaine Coche-Dury','France','1920s','Premium','Meursault','Meursault estate best known for white Burgundy from Chardonnay.',W+'Domaine_Coche-Dury')
addb('Domaine Leflaive','France','1717','Premium','Puligny white','Puligny-Montrachet estate with about 5.1 hectares of Grand Cru vineyards.',W+'Domaine_Leflaive')
_,k=kind('Red wine','Nebbiolo'); k.setdefault('x',[]).append(arch("Giacomo Conterno Monfortino","Giacomo Conterno","1920s",W+'Giacomo_Conterno',"Barolo riserva from Monforte d'Alba, made only in exceptional vintages and aged seven years in large casks.",[],"vintage"))
_,k=kind('White wine','Chardonnay'); k.setdefault('x',[]).extend([arch("Domaine Coche-Dury","Domaine Coche-Dury","1920s",W+'Domaine_Coche-Dury',"Meursault estate best known for white Burgundy made from Chardonnay.",[],"appellation · vineyard · vintage"),arch("Domaine Leflaive","Domaine Leflaive","1717",W+'Domaine_Leflaive',"Puligny-Montrachet estate highly regarded for white wines; about 5.1 ha of Grand Cru vineyards.",[],"appellation · vineyard · vintage")])
_,k=kind('White wine','Riesling'); k.setdefault('x',[]).append(arch("Egon Müller Scharzhofberger","Egon Müller","",W+'Egon_M%C3%BCller_Scharzhof',"Riesling from the Wiltinger Scharzhofberg vineyard in the Saar, made by the Egon Müller estate.",[],"Prädikat level · vintage"))
# ---- J7-4
for dp in d['depts']:
    if dp['n']=='Ready-to-drink & mixed packs':
        for sh in dp['s']: sh['k']=[k for k in sh['k'] if k['n']!='Mixed case & gift set']
    dp.setdefault('b',[]).append({"m":"Pack format","v":"Single bottle or can · mixed case or multipack · gift set · miniatures tasting set · advent calendar","w":"Format of the pack, applied to every kind in this department rather than a kind of its own."})
# ---- J7-6
for dp in d['depts']:
    if dp['n']=='Sake & rice wine':
        sh=dp['s'][0]; a=[k for k in sh['k'] if k['n']=='Junmai sake'][0]; b2=[k for k in sh['k'] if k['n'].startswith('Honjozo')][0]
        a['n']='Sake (junmai, honjozo, ginjo & daiginjo)'; a['a']=(a.get('a','')+' · Junmai sake · Honjozo, ginjo & daiginjo sake · Seishu').strip(' ·')
        a['d']='Rice sake graded by polishing ratio and added alcohol: junmai, honjozo, ginjo and daiginjo grades, with brewery archetypes.'
        a['t']=['Polishing ratio (seimaibuai, % of grain remaining)']+[t for t in a['t'][2:]]
        a['x']=a['x']+b2['x']; seen=set(tuple(m) for m in a['m'])
        a['m']=a['m']+[m for m in b2['m'] if tuple(m) not in seen]
        sh['k']=[k for k in sh['k'] if k is not b2]
        dp['b'].insert(0,{"m":"JAS grade ladder","v":"Junmai · Tokubetsu junmai · Junmai ginjo (≤60% polish) · Junmai daiginjo (≤50%) · Honjōzō (≤70%) · Tokubetsu honjōzō (≤60%) · Ginjō (≤60%) · Daiginjō (≤50%)","w":"Grades apply to the one Sake kind; a reader looking for daiginjo finds it here."})
# ---- J7-7
_,k=kind('Cider, perry & mead','English cider'); k['n']='British & Irish cider'; k['a']=(k.get('a','')+' · English cider · Irish cider').strip(' ·')
k['d']=k['d'] if 'Irish' in k['d'] else k['d'].rstrip('.')+', including Irish cider.'
json.dump(d,open('work/FIX_J7/J7.tmp','w'),ensure_ascii=False,indent=1)
json.dump(B,open('work/FIX_J7/B.tmp','w'),ensure_ascii=False,indent=1)
