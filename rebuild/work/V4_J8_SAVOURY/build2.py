import sys, json, copy, re, os, io, contextlib
sys.path.insert(0,'/home/user/Possession-Taxonomy/rebuild/work/V4_J8_SAVOURY')
with contextlib.redirect_stdout(io.StringIO()):
    import build as OB
from lib import *
import bread as B, crisps as C, nuts as N
TT_OWN=["Global group","National champion","Independent","Craft & indie","Own label"]
TIER_ORDER={t:i for i,t in enumerate(["National champion","Independent","Craft & indie","Own label","Protected name"])}
EUR='https://www.lexaris.de/library/tableofcontents/'
def prot(n,d,s,y,g_cty,**kw):
    e=E(n,d,s,y=y,**kw); e['cty']=g_cty; e['g']='Protected name'; return e
# --- extra entries
bimbo_x=[
 E('Wickbold','Brazilian bread brand; Grupo Bimbo agreed to buy Wickbold and Seven Boys on 2 September 2024.','https://www.just-food.com/news/grupo-bimbo-boosts-brazil-presence-with-wickbold-buy',own='Grupo Bimbo',tier='Global group',cty='Brazil',own_y='2024'),
 E('Seven Boys','Brazilian bread brand that Wickbold bought in 2015, in the 2024 Bimbo deal.','https://www.just-food.com/news/grupo-bimbo-boosts-brazil-presence-with-wickbold-buy',own='Grupo Bimbo',tier='Global group',cty='Brazil',own_y='2024'),
]
FLs=WP+'Elma_Chips'
pep_x=[E(n,d,FLs,own='PepsiCo',tier='Global group',cty='Brazil',y=y,own_y='') for n,d,y in [
 ('Cebolitos','Brazilian onion-flavoured corn snack, the Funyuns equivalent, from Elma Chips.','1978'),
 ('Zambinos','Brazilian Elma Chips snack.','1982'),
 ('Ovinhos','Brazilian Elma Chips snack.','1986'),
 ('Fofura','Brazilian snack from the Lucky acquisition of 2010.','2010')]]
SIMBA=WP+'Simba_Chips'
pep_x+=[E('Simba','South African snack company founded 1957; PepsiCo bought it in 1995.',SIMBA,own='PepsiCo',tier='Global group',cty='South Africa',y='1957',own_y='1995'),
 E('NikNaks','South African snack named on the Simba page.',SIMBA,own='PepsiCo',tier='Global group',cty='South Africa'),
 E('Ghost Pops','South African snack named on the Simba page.',SIMBA,own='PepsiCo',tier='Global group',cty='South Africa')]
P=[ # protected additions
 prot('Bayerische Brezel','Bavarian soft pretzel (Bayerische Breze, Brezn, Brez\'n); PGI entered 18 February 2014.','https://www.legislation.gov.uk/eur/2014/161/data.html','PGI 2014','Germany'),
 prot('Štramberské uši','Czech spiced honey-cake "ears" from Štramberk; PGI entered 6 March 2007.',EUR+'2119030','PGI 2007','Czech Republic'),
 prot('Alfajor de Medina Sidonia','Spanish honey and almond sweet from Medina Sidonia; PGI entered 6 March 2007.',EUR+'2119030','PGI 2007','Spain'),
 prot('Skalický trdelník','Slovak spit cake from Skalica; PGI entered 14 December 2007.',EUR+'2118871','PGI 2007','Slovakia'),
 prot('Gâche vendéenne','Enriched Easter bread of the Vendée; PGI entered 4 November 2013.',EUR+'2116994','PGI 2013','France'),
 prot('Salzwedeler Baumkuchen','Layered spit cake of Salzwedel; PGI entered 9 December 2010.','https://lexaris.de/library/tableofcontents/2025715','PGI 2010','Germany'),
 prot('Daujėnų naminė duona','Lithuanian home-style bread of Daujėnai; PGI entered 13 February 2014.','https://lexaris.de/library/tableofcontents/2116685','PGI 2014','Lithuania'),
 prot('Liers vlaaike','Belgian small flan of Lier; PGI entered 9 December 2013.','https://lexaris.de/library/tableofcontents/2116772','PGI 2013','Belgium'),
 prot('Valašský frgál','Czech large round pie of Wallachia; PGI entered 28 November 2013.','https://lexaris.de/library/tableofcontents/2116798','PGI 2013','Czech Republic'),
 prot('Zagorski mlinci','Croatian baked dough sheets of Zagorje; PGI entered 2019.','https://www.legislation.gov.uk/eur/2019/1036/article/1/data.html','PGI 2019','Croatia'),
 prot('Poljički soparnik','Croatian chard-filled pie of Poljica (also Poljički zeljanik, uljenjak); PGI entered 30 March 2016.','https://www.legislation.gov.uk/eur/2016/526/data.html','PGI 2016','Croatia'),
]
IT='https://en.wikipedia.org/wiki/List_of_Italian_food_and_drink_products_with_protected_status'
# date upgrades from the Italian list
DATES={'Coppia ferrarese':'PGI, registered 17 October 2001','Pagnotta del Dittaino':'PDO, registered 17 June 2009','Pane casareccio di Genzano':'PGI, registered 24 November 1997','Pane di Altamura':'PDO, registered 18 July 2003','Pane di Matera':'PGI, registered 21 February 2008','Ricciarelli di Siena':'PGI, registered 18 March 2010'}
# --- mapping
MB={
'Sliced & tin loaf':"Bimbo,Tía Rosa,Sunbeam,Mrs Baird's,Oroweat,Arnold,Stroehmann,Freihofer's,Sara Lee (North American fresh bakery),Canada Bread,Stonemill Bakehouse,Pullman,Plus Vita,Nutrella,Fargo,Ideal,Nutra Bien,Supán,Panettiere,El Paisa,Bimbo Iberia,Panrico,Vel Pitar,Modern,Kitty Bread,Mankattan,Wickbold,Seven Boys,Kingsmill,Sunblest,Allinson,Burgen,Hovis,Tip Top,Mulino Bianco,Harrys,Pepperidge Farm,Wonder,Dave's Killer Bread,Nature's Own,Canyon Bakehouse,Warburtons,Pågen,Yamazaki Baking,Albany,SASKO",
'Rye & wholegrain bread':"Mestemacher,Vaasan,Oululainen,Skogaholm,Druva,Daujėnų naminė duona",
'Baguette & French bread':"Hatting,Bonjour,Tom Cat Bakery",
'Bagel & rolls':"Korvbrödsbagarn,Fleischer's Bagels,St Pierre,Bayerische Brezel",
'English muffin & crumpet':"Thomas',Bays English Muffins",
'Flatbread':"Ready Roti,Boboli,Piadina romagnola,Focaccia di Recco col formaggio,Zagorski mlinci",
'Castella & sponge cake':"Marinela,Gansito,Vachon,Tastykake,Tinkies,Twinkie",
'Croissant & viennoiserie':"El Globo",
'Tart & shortcrust pastry':"Pop-Tarts,Liers vlaaike,Valašský frgál",
'Celebration cake':"Colin the Caterpillar",
'Sourdough bread':"Poilâne",
'Enriched bread':"Gâche vendéenne",
'Italian bread':"Pane di Altamura,Pane toscano,Pane casareccio di Genzano,Pagnotta del Dittaino,Pane di Matera,Coppia ferrarese",
'Gingerbread & Lebkuchen':"Aachener Printen,Nürnberger Lebkuchen,Toruń gingerbread,Štramberské uši,Alfajor de Medina Sidonia",
'Stollen & Christmas breads':"Dresdner Stollen",
'Fruitcake':"Panforte di Siena,Ricciarelli di Siena",
'Baumkuchen & layer cake':"Salzwedeler Baumkuchen,Skalický trdelník",
'Turnover & strudel':"Pastel de Tentúgal,Poljički soparnik",
}
MC={
'Potato crisps':"Lay's,Ruffles,Munchos,Miss Vickie's,Elma Chips,Sabritas,Matutano,Star Chips,Pepito,Savoy Brands,Hostess (Canada),Walkers,Smiths,Smith's (Australia),Uncle Chipps,Solinki,Paw Ridge,Twistos,funny-frisch,Chio,Pom-Bär,Kelly,Vico,Tayto,KP Snacks,McCoy's,Discos,Frisps,Bohemia,Popchips,Estrella,Maarud,Griffin's Foods,Snack Brands Australia,Calbee Potato Chips,Jagariko,Jagabee,Jaga Pokkuru,Seabrook,Warnock Food Products,Frito-Lay Japan,Potabee,Lance,Hunky Dorys,King,Russkaya Kartoshka,Just Brutal,Crunchips,Koikeya,Orion,Hefei Huatai Food,Shanghai Liwayway Food,Fujian Dali Food,Jack 'n Jill,Chitato,Qtela,Balaji Wafers,Utz,Herr's,Wachusett Potato Chip Company,Golden Flake,Snyder of Berlin,Vitner's,Old Dutch,Jays,Better Made,Mikesells,Martin's Potato Chips,Charles Chips,President's Choice,Simba",
'Kettle crisps':"Kettle Brand,Cape Cod,Tyrrells,Zapp's,Boulder Canyon,Burts,Fairfields Farm Crisps,Corkers,Yorkshire Crisps",
'Stackable crisps':"Pringles",
'Tortilla chips':"Doritos,Tostitos,Takis,Barcel,Sun Chips,Stacy's Pita Chips,On the Border,R.W. Garcia,Late July",
'Extruded corn snack':"Fritos,Cheetos,Funyuns,Rancheritos,Poffets,Crujitos,Sabritones,Fandangos,Lucky,Stiksy,Pingo d'Ouro,Baconzitos,Torcida,Cebolitos,Zambinos,Ovinhos,Fofura,Monster Munch,Quavers,Wotsits,Squares,Frazzles,Chipsticks,Bacon Fries,Scampi Fries,Snaps,Twisties,Kurkure,Chiki,Maxicorn,JetZ,Hula Hoops,Nik Naks,Space Raiders,Wheat Crunchies,Wise Foods,Bamba,Bugles,Chex Mix,Sapporo Potato,Ghost Pops,NikNaks",
'Popcorn':"Smartfood,Cracker Jack,Butterkist,Orville Redenbacher's,Jolly Time,Pop Secret,Popcornopolis,SkinnyPop,Calbee Caramel",
'Pretzel':"Rold Gold,Snyder's of Hanover,Snack Factory,Dot's Pretzels,Pretz,Penn State,Bachman,Gardetto's",
'Rice cracker & senbei':"Happy Turn,Want Want,Snack-a-Jacks",
'Prawn cracker':"Kappa Ebisen,Saeukkang,Nongshim,Skips",
'Namkeen & Bombay mix':"Haldiram's",
}
MN={
'Granola & cereal bar':"Nature Valley,Fiber One,Cascadian Farms,Rice Krispies Treats,Nutri-Grain,Special K,Bear Naked,Quaker Chewy,Quaker rice cakes,Jordans",
'Fruit & nut bar':"KIND,Lärabar,Pure Organic",
'Protein bar':"RXBAR,Quest Nutrition",
'Energy & sports bar':"Clif Bar,PowerBar,Balance Bar,CalorieMate,Odwalla Bar,Soldier Fuel,Tiger's Milk,ZonePerfect",
'Roasted & salted nuts':"Planters,ültje,KP Nuts,Three Squirrels,Duyvis,TrueNorth,ManiMoto",
'Almonds':"Blue Diamond",
'Trail mix':"Graze",
'Hazelnuts':"Nocciola Piemonte IGP",
}
def split(s):
    out=[];cur=''
    for part in s.split(','):
        out.append(part)
    # names with commas none; handle apostrophes ok
    return [x.strip() for x in out]
# collect entries
def allx(*lists):
    d={}
    for L in lists:
        for e in L: d[e['n']]=e
    return d
bread_all=allx(B.bimbo,bimbo_x,B.abfk,B.lan,B.bar,B.camp,B.mars,B.fl,B.eur,B.asia,B.afr,B.cake,B.craft,B.prot_bread,B.prot_bake,P)
crisp_all=allx(C.pepsico,pep_x,C.mars,C.intersnack,C.calbee,C.campbell,C.gmc,C.bimbo_snk,C.hersh,C.europe,C.asia,C.usind,C.crafts)
nuts_all=allx(N.gmb,N.marsb,N.mond,N.pepb,N.inter,N.abfn,N.ind,[N.nocc])
def urlname(u):
    m=re.search(r'wikipedia\.org/wiki/(.+)$',u)
    if m: return 'Wikipedia '+m.group(1).replace('_',' ').replace('%27',"'").replace('%26','&').replace('%C3%A5','å').replace('%C3%A4','ä').replace('%C3%A2','â').replace('%C3%BA','ú').replace('%C5%84','ń')
    h=re.search(r'https?://(?:www\.)?([^/]+)',u).group(1); return h
def gset(e):
    if e.get('g')=='Protected name': return
    if 'own' not in e: e['g']='Protected name'; e.setdefault('cty',e.get('cty',''))
    elif e.get('tier')=='Global group': e['g']=e['own']
    elif e.get('tier'): e['g']=e['tier']
def sortx(x):
    def key(e):
        g=e['g']; isg= g not in TIER_ORDER
        return (0 if isg else 1, g if isg else TIER_ORDER[g], str(e.get('y','')), e['n'].lower())
    return sorted(x,key=key)
def fill(dept,mapping,pool,intro):
    placed=set(); kinds={}
    for kn,names in mapping.items():
        xs=[]
        for nm in split(names):
            e=copy.deepcopy(pool[nm]) if nm in pool else None
            if e is None: print('MISSING',dept,nm); continue
            if nm in DATES and dept=='Bread & bakery':
                e['y']=DATES[nm]; e['s']=IT if 'wikipedia' not in e['s'] else e['s']
            gset(e); xs.append(e); placed.add(nm)
        kinds[kn]=xs
    return kinds,placed
def apply(dept_old,newdept,mapping,pool,extra_covers=None):
    kinds,placed=fill(dept_old,mapping,pool,'')
    left=set(pool)-placed
    if left: print('UNPLACED',dept_old,sorted(left))
    shelves=[]
    for sh in OLDDEPT[dept_old]['s']:
        ks=[]
        for k in sh['k']:
            kk=form_kind(dept_old,k['n'],keep=())
            xs=kinds.get(k['n'])
            if xs:
                srcs=[]
                for e in xs:
                    n=urlname(e['s'])
                    if n not in srcs: srcs.append(n)
                hasprot=any(e.get('g')=='Protected name' for e in xs)
                hasbrand=any('own' in e for e in xs)
                nl='One entry is '+('a brand sold under its own name' if hasbrand else '')+(' or ' if hasbrand and hasprot else '')+('a bakery or food whose name is protected' if hasprot else '')+'; its flavours, sizes and formats are versions.'
                if not hasbrand: nl='One entry is a bread or bake whose name is protected; its ordinary and special forms are versions.'
                sel=('Brands whose flagship product is '+k['n'].lower()+', placed from the fetched owner-group, champion and market pages ('+'; '.join(srcs[:10])+('; and others' if len(srcs)>10 else '')+', fetched 2026-10-31).') if hasbrand else ('Protected names from the fetched pages ('+'; '.join(srcs[:8])+', fetched 2026-10-31).')
                if hasbrand and hasprot: sel+=' Protected names follow the Italian protected-status list, the Wikidata P11794 query and EU registration regulations.'
                sel+=f' Covers {len(xs)} entries; no whole-market reference exists, so the count is of the fetched owner and champion pages.'
                if hasprot and not hasbrand: sel+=' The EU register (eAmbrosia) is JavaScript-only and was not read.'
                kk['x']=sortx(xs); kk['nl']=nl; kk['sel']=sel; kk['xg']='by owner group, then tier'
                kk['tt']=[['Owner tier',TT_OWN]]+list(kk.get('tt',[]))[:3]
            ks.append(kk)
        shelves.append({'n':sh['n'],'t':sh['t'],'ax':sh['ax'],'k':ks})
    return shelves
# ---- BREAD
bd=copy.deepcopy(OB.bread_dept)
bd['s']=apply('Bread & bakery',bd,MB,bread_all)
art=BK=None
loafx=copy.deepcopy(B.loaf)
for e in loafx: pass
art={'n':'Artisan bakery','a':'Real Bread Loaf Mark bakery · craft bakery','d':'Independent bakery selling real bread under its own name, as listed by the Real Bread Campaign Loaf Mark licensee list.','s':B.LM,
 'x':sorted(loafx,key=lambda e:(e['g'],e['n'].lower())),'nl':'One entry is an independent bakery; its loaves and bakes are versions.',
 'sel':f'Follows the Loaf Mark licensee list in the Sustain article compiled 1 September 2026 (fetched 2026-10-31); the page states a total of 219 bakeries (205 UK, 14 outside the UK). Complete: 219 of 219 lines; one exact duplicate (The Heritage Bakery, Oxfordshire) is merged, so {B.LOAF_D} entries. The Loaf Mark is a licence to use the mark on additive-free loaves, not a certification.',
 'xg':'by country, then tier','tt':[['Loaf Mark',['Real Bread Loaf Mark','Sourdough Loaf Mark']],['Owner tier',["Craft & indie"]]]}
bd['s'].insert(0,{'n':'Bakeries','t':'Independent bakeries that sell bread under their own name.','ax':'one kind: independent bakeries by country','k':[art]})
bd['note']='Brands sit under the product they are best known for (Warburtons in Sliced & tin loaf); protected names (Pane di Altamura, Aachener Printen, Pastel de Tentúgal) sit in their product kinds; generic forms stay kinds and link to the Culinary Taxonomy. The tier breakdown is on the market view.'
bd['msum']="UK bread is led by Warburtons and German pre-packed bread by Harry-Brot; Grupo Bimbo is the largest group worldwide. The figures are the last the cited pages give."
bd['ms']=[m for m in OB.bread_dept['ms']]+[
 {"mkt":"German pre-packaged bread","who":"Harry-Brot","share":"more than 40 %","yr":2025,"s":"https://www.bundeskartellamt.de/SharedDocs/Meldung/EN/Pressemitteilungen/2025/04_15_2025_Harry_Rewe.html","note":"Bundeskartellamt press release of 15 April 2025 on Harry-Brot's takeover of Glockenbrot"},
 {"mkt":"Brazilian packaged bread","who":"Grupo Bimbo with Wickbold","share":"no share stated","yr":2024,"s":"https://www.just-food.com/news/grupo-bimbo-boosts-brazil-presence-with-wickbold-buy","note":"Bimbo agreed on 2 September 2024 to buy Wickbold and Seven Boys; Wickbold revenue reported as R$1.6 billion for 2022; the page gives no share"},
 {"mkt":"French bread","who":"no figure","share":"n/a","yr":"n/a","s":WP+"Barilla_Group","note":"No fetched page gave a share for France; Harrys (Barilla) is the sliced-bread brand the page names"},
]
# ---- CRISPS
cd=copy.deepcopy(OB.crisp_dept)
cd['s']=apply('Crisps & savoury snacks',cd,MC,{**crisp_all})
cd['note']='Brands sit under the snack they are best known for (Lay\'s in Potato crisps, Pringles in Stackable crisps, Doritos in Tortilla chips); the tier breakdown is on the market view. Cookie and cracker brands of the groups sit in Biscuits & crackers; bars in Snack nuts & bars.'
cd['ms']=[m for m in OB.crisp_dept['ms'] if m['who']!='no figure']+[
 {"mkt":"US savoury snacks","who":"Frito-Lay","share":"59 %","yr":2012,"s":WP+"Lay's","note":"Frito-Lay products' share of the US savoury snack-food market, as the Lay's page states (the Frito-Lay page gives 40 % for 2009)"},
 {"mkt":"Mexican potato chips","who":"Sabritas (PepsiCo)","share":"about 80 %","yr":"not stated","s":WP+"Chipsy","note":"reported share, undated, on the Lay's page"},
 {"mkt":"German sweets and salty snacks","who":"Intersnack","share":"22 %","yr":2024,"s":"https://lebensmittelpraxis.de/suesswaren/44468-suesswarenmarkt-salzige-snacks-auf-dem-vormarsch.html","note":"share by packs sold in grocery and drugstores (NielsenIQ via Lebensmittel Praxis, June 2025); 16 % in 2013; salty snacks' share of sweets and snacks rose from 19 % to 26 %"},
 {"mkt":"French sweet and savoury snacks","who":"Lorenz Bahlsen Snacks","share":"17.63 %","yr":2005,"s":"https://www.bakeryandsnacks.com/Article/2007/02/06/Room-for-growth-in-French-snack-sector/","note":"article of 2007 whose sales figures are for 2005; brands Bahlsen, Curly, Monster Munch, Crunchips"},
 {"mkt":"French sweet and savoury snacks","who":"Pepsi (Lay's, Doritos, Cheetos)","share":"14.95 %","yr":2005,"s":"https://www.bakeryandsnacks.com/Article/2007/02/06/Room-for-growth-in-French-snack-sector/","note":"same article"},
 {"mkt":"Brazilian salty snacks","who":"no figure","share":"n/a","yr":"n/a","s":FLs,"note":"No fetched page gave a share; the Elma Chips page names PepsiCo's Brazilian brands"},
 {"mkt":"South African and African snacks","who":"Simba (PepsiCo)","share":"owned since 1995","yr":1995,"s":SIMBA,"note":"the page gives no share; no Middle East or other African champion could be sourced"},
]
# ---- NUTS
nd=copy.deepcopy(OB.nuts_dept)
pool=dict(nuts_all)
for nm in ['Three Squirrels','Duyvis','TrueNorth','ManiMoto']:
    pool[nm]=crisp_all[nm]
    cd_pool=crisp_all
nd['s']=apply('Snack nuts & bars',nd,MN,pool)
# the nuts that came from crisps pool must not stay in crisps: crisps mapping excludes them already
nd['note']='Brands sit under the product they are best known for (KIND in Fruit & nut bar, Planters in Roasted & salted nuts); plain nuts are commodity kinds; the tier breakdown is on the market view.'
nd['ms']=OB.nuts_dept['ms']
# --- roles cleanup & 1-in-5
for dp in (bd,cd,nd):
    for sh in dp['s']:
        for k in sh['k']:
            xs=k.get('x',[])
            r=[e for e in xs if e.get('role')]
            if r and len(r)*5>len(xs)+4:
                for e in r[1:] if len(xs)>=5 else r: e.pop('role',None)
            for e in xs:
                if e['n'] in ("Lay's",'Hovis','Kettle Brand','Poilâne','Bimbo','Pringles'): e.pop('role',None)
for dp in (bd,cd,nd):
    for sh in dp['s']:
        for k in sh['k']:
            if 0<len(k.get('x',[]))<5:
                for e in k['x']: e.pop('role',None)
depts=[bd,cd,nd]
out={'replaces':['Bread & bakery','Crisps & savoury snacks','Snack nuts & bars'],'depts':depts,'brands':[],'brand_updates':{},'renames':{},'moves':[]}
reg=json.load(open(ROOT+'out/J8_brands.json'))['b']; low={b['n'].lower():b for b in reg}; seen=set()
def addb(n,seg,d,kf,c='',f='',s=''):
    if not n or n.lower() in seen or n=='owner not stated': return
    seen.add(n.lower()); b={'n':n,'seg':seg,'d':d,'kf':kf}
    if c: b['c']=c
    if f and re.fullmatch(r'\d{4}',str(f)): b['f']=str(f)
    if s: b['s']=s
    out['brands'].append(b)
for dp,kf in zip(depts,['bread and bakery','crisps and savoury snacks','nuts and bars']):
    for sh in dp['s']:
        for k in sh['k']:
            for e in k.get('x',[]):
                if 'own' not in e: continue
                for name in {e['n'],e['own']}:
                    if name.lower() in low:
                        if name==e['n']: out['brand_updates'][low[name.lower()]['n']]={'own':e['own'],'tier':e['tier'],'c':e.get('cty','')}
                    else:
                        seg='Artisan & independent' if e['tier']=='Craft & indie' else ('Own-label & retailer' if e['tier']=='Own label' else 'Mainstream')
                        isown=(name==e['own'] and name!=e['n'])
                        addb(name,seg,('Owner of brands in the '+dp['n']+' department.') if isown else e['d'],kf,'' if isown else e.get('cty',''),'' if isown else str(e.get('y','')),'' if isown else e['s'])
json.dump(out,open(ROOT+'out/J8_parts/SAVOURY.json','w'),ensure_ascii=False)
print('written',os.path.getsize(ROOT+'out/J8_parts/SAVOURY.json'),'brands',len(out['brands']),'updates',len(out['brand_updates']))
