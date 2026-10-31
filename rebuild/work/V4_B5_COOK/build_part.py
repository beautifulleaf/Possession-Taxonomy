import json, copy, re
ROOT='/home/user/Possession-Taxonomy/'
old=json.load(open(ROOT+'rebuild/out/B5.json'))
reg={b['n'] for b in json.load(open(ROOT+'rebuild/out/B5_brands.json'))['b']}
D={dp['n']:dp for dp in old['depts']}
W='https://en.wikipedia.org/wiki/'
def ents(dept):
    out={}
    for sh in D[dept]['s']:
        for k in sh['k']:
            for e in k.get('x',[]): out[e['n']]=(k['n'],e)
    return out
CE=ents('Cookware & bakeware'); KE=ents('Knives & cutting'); TE=ents('Kitchen tools & measuring')

# --- market metadata: (country, owner, tier, own_y) -------------------------------
CTY={'Lodge':'United States','Griswold Manufacturing':'United States','Wagner Manufacturing Company':'United States','Le Creuset':'France','Staub':'France','Chasseur':'France','Vermicular':'Japan','de Buyer':'France','Yamada':'Japan','All-Clad':'United States','Hestan':'United States','Mauviel':'France','Ruffoni':'Italy','Nakamura Douki':'Japan','Matfer Bourgeat':'France','Tefal':'France','Scanpan':'Denmark','Emile Henry':'France','Kamado-san':'Japan','Pyrex':'United States','Nordic Ware':'United States','USA Pan':'United States','Kaiser':'Germany','Gobel':'France','Falcon':'United Kingdom','Lloyd Pans':'United States','Baking Steel':'United States','Silpat':'France','Iwachu':'Japan','Nambu':'Japan','Kuhn Rikon':'Switzerland','Fissler':'Germany','Hawkins':'India','Prestige':'India','Spring':'Switzerland','Garcima':'Spain','Vaello':'Spain','Naniwa':'Japan','Shapton':'Japan','King (Matsunaga)':'Japan','Atoma':'Japan','Masamoto Sohonten':'Japan','Takeda Hamono':'Japan','Konosuke':'Japan','Ashi Hamono':'Japan','Yoshikane Hamono':'Japan','Takamura Hamono':'Japan','Teruyasu Fujiwara':'Japan','Shigefusa':'Japan','Tadafusa':'Japan','Moritaka Hamono':'Japan','Sakai Takayuki':'Japan','Tojiro':'Japan','Misono':'Japan','MAC Knife':'Japan','Chan Chi Kee':'China','Shibazi':'China','Opinel':'France','Victorinox':'Switzerland','Wüsthof':'Germany','Zwilling J. A. Henckels':'Germany','Global':'Japan','Shun':'Japan','K Sabatier':'France'}
def mk_fields(e, mk=None, own=None, tier='Independent', cty=None, own_y=None):
    mk=mk or e.get('mk','')
    e['own']=own or mk
    e['tier']=tier
    e['cty']=cty or CTY.get(mk,'')
    if own_y: e['own_y']=own_y
    return e
OWN={ # maker -> (owner, tier, own_y) from fetched pages
 'Staub':('Zwilling J. A. Henckels','Global group','2008'),
 'Tefal':('Groupe SEB','Global group','1968'),
 'All-Clad':('Groupe SEB','Global group','2004'),
 'Zwilling J. A. Henckels':('Werhahn KG','Global group','1970'),
 'Le Creuset':('Paul van Zuydam','Independent','1988'),
 'Victorinox':('Victorinox-Stiftung','Independent',''),
 'Kai Group':('Kai Group','Independent',''),
 'Global':('Yoshida Metal Industry','Independent',''),
 'Tojiro':('Tojiro Co Ltd','Independent',''),
 'Misono':('Misono','Independent',''),
 'Wüsthof':('Wüsthof','Independent',''),
 'Calphalon':('Newell Brands','Global group','1998'),
}
def clone(name, src, **kw):
    e=copy.deepcopy(src[name][1]); e.update(kw); return e
def fin(e, mk=None):
    mk=mk or e.get('mk','')
    o=OWN.get(mk)
    if o: mk_fields(e,mk,o[0],o[1],None,o[2])
    else: mk_fields(e,mk)
    e.setdefault('a',''); e.setdefault('v',[])
    return e
def ver(n,mk,y,d): return {'n':n,'mk':mk,'y':y,'d':d}

# ===================== COOKWARE =========================
cw=copy.deepcopy(D['Cookware & bakeware'])
for sh in cw['s']:
    for k in sh['k']:
        k.pop('x',None); k.pop('m',None); k.pop('r',None)
def E(name, g, rename=None, **kw):
    e=clone(name,CE); 
    if rename: e['n']=rename
    e['g']=g; e.update(kw)
    return fin(e)
lodge=E('Lodge cast-iron skillet','United States',role='landmark',
  d='Sand-cast pan from a Tennessee foundry opened in 1896; in 2002 Lodge began selling every piece factory-seasoned, which its history page calls an industry first.',
  y='1896 (foundry); factory seasoning 2002', s='https://www.lodgecastiron.com/lodge-celebrates-125-years')
lodge['v']+= [ver('Enamelled cast iron','Lodge','2005','added to the range'),ver('Seasoned carbon steel','Lodge','2013','added to the range')]
lodgeD=E('Lodge Dutch oven','United States')
lodgeG=E('Lodge grill pan and reversible griddle','United States')
gris=E('Griswold skillet','United States'); griD=E('Griswold Dutch oven (vintage)','United States'); wag=E('Wagner Ware skillet','United States')
nam=E('Nambu ironware frying pan','Japan'); nam['mk']=nam.get('mk') or 'Nambu ironware makers'; nam['cty']='Japan'; nam['own']=nam['mk']
iwa=E('Iwachu Nambu iron tamagoyaki pan','Japan')
cast=[lodge,lodgeD,lodgeG,gris,griD,wag,nam,iwa]

lc=E('Le Creuset Cocotte','France',rename='Le Creuset round French oven',role='origin',
  d='Enamelled cast-iron casserole; Le Creuset produced its first cocotte in 1925 in orange flame, now sold in many colours.',
  y='1925', s=W+'Le_Creuset')
staub=E('Staub La Cocotte','France',rename='Staub cocotte',
  d='Cast-iron cocotte with double-glazed enamel; the first piece Francis Staub designed when he founded the firm in Alsace in 1974.',
  y='1974', s=W+'Staub_(cookware)')
chas=E('Chasseur casserole','France'); ver_=E('Vermicular Oven Pot','Japan')
lcs=E('Le Creuset enamelled cast-iron skillet','France'); lcg=E('Le Creuset Grillit','France'); lct=E('Le Creuset tagine','France'); lcf=E('Le Creuset fondue set','France')
for x in (lcs,lcg,lct,lcf): x['own']='Paul van Zuydam'; x['own_y']='1988'
enam=[lc,staub,chas,ver_,lcs,lcg,lct,lcf]

deb=E('de Buyer Mineral B carbon-steel frying pan','France',rename='de Buyer Mineral B',
  d="Carbon-steel pans from the Vosges house of de Buyer, founded 1830, with a beeswax finish; frying pan and crêpe pan are versions.", s=W+'De_Buyer')
crp=E('de Buyer Mineral B crêpe pan','France')
deb['v'].append(ver('Mineral B crêpe pan','de Buyer','current',crp['d']))
yam=E('Yamada hammered iron wok','Japan')
carb=[deb,yam]

ac=E('All-Clad D3 Stainless fry pan','United States',rename='All-Clad D3 Stainless',
  d='Three-ply bonded stainless pans from All-Clad Metalcrafters, founded 1971 by metallurgist John Ulam; owned by Groupe SEB since 2004.',
  y='1971', s=W+'All-Clad')
hes=E('Hestan NanoBond','United States')
clad=[ac,hes]

mh=E("Mauviel M'250 copper frying pan",'France',rename="Mauviel M'Heritage",
  d="Copper line from the Normandy house of Mauviel, whose own history dates the workshop to 1830 at Villedieu-les-Poêles.", y='1830 (house)', s='https://mauviel-usa.com/pages/about-mauviel-1830s-history')
mh['v']=[ver("M'150 B",'Mauviel','current','bronze handle'),ver("M'150 S",'Mauviel','current','stainless handle'),ver("M'150 CI",'Mauviel','current','cast-iron handle'),ver("M'200 CI",'Mauviel','current','thicker copper, cast-iron handle'),ver("M'200 B",'Mauviel','current','thicker copper, bronze handle')]
m250=E("Mauviel M'250 copper frying pan",'France'); m250['n']="Mauviel M'250"
msauce=CE["Mauviel M'Héritage copper saucepan"][1]; m250['v']=[ver(x['n'],'Mauviel',x.get('y',''),x.get('d','')) for x in msauce.get('v',[])]+m250.get('v',[])
ruf=E('Ruffoni Historia hammered copper','Italy'); nak=E('Nakamura Douki copper tamagoyaki pan','Japan'); mat=E('Matfer Bourgeat copper canelé mould','France')
copper=[mh,m250,ruf,nak,mat]

tef=E('Tefal non-stick frying pan','France',rename='Tefal non-stick',role='origin',
  d='Non-stick pans from Tefal, founded 1956 by Marc Grégoire; its page credits the firm with creating the non-stick cookware category.',
  y='1956', s=W+'Tefal')
scan=E('Scanpan Classic','Denmark')
calp=fin({'n':'Calphalon','a':'','d':'US cookware brand owned by Newell Brands, which acquired it in 1998.','mk':'Calphalon','y':'','s':W+'Newell_Brands','v':[],'g':'United States'})
nonst=[tef,scan,calp]

clay=[E('Emile Henry Flame tagine','France'),E('Kamado-san','Japan'),E('Emile Henry ceramic dish','France'),E('Emile Henry pie dish','France'),E('Le Creuset stoneware dish','France'),E('Pyrex glass baking dish','United States'),E('Pyrex glass pie plate','United States')]
clay[4]['own']='Paul van Zuydam'; clay[4]['own_y']='1988'
alu=[E('Nordic Ware Naturals half sheet','United States'),E('Nordic Ware Bundt pan','United States'),E('USA Pan aluminised-steel sheet','United States'),E('USA Pan loaf pan','United States'),E('USA Pan 12-cup muffin tin','United States'),E('Kaiser springform','Germany'),E('Gobel fluted tart mould','France'),E('Falcon enamel pie dish','United Kingdom'),E('Lloyd Pans Detroit-style pan','United States'),E('Baking Steel','United States'),E('Silpat baking mat','France')]
# fix makers lacking CTY lookups
for e in alu+clay+cast+copper+enam+carb+clad+nonst:
    mk=e.get('mk','')
    if not e.get('cty'): e['cty']=CTY.get(mk,'')
    e['g']=e.get('g') or e['cty']
SEL_MAT=lambda n,txt:("%s Entries moved here from the form kinds of the structure pass, with the defining lines named by the fetched maker pages; no whole-space reference exists for cookware lines. %s"%(txt,n))
def kind(n,d,s,x,nl,sel,xg='by country of the maker, then year, then name',tt=None,see=None):
    k={'n':n,'a':'','d':d,'s':s,'x':sorted(x,key=lambda e:(e['g'],str(e.get('y','')),e['n'])),'nl':nl,'sel':sel,'xg':xg}
    if tt: k['tt']=tt
    if see: k['see']=see
    return k
CWP='https://en.wikipedia.org/wiki/Cookware_and_bakeware'
mat_shelf={'n':'Cookware by material','t':'Cookware and bakeware sorted by what it is made of, with the defining named lines of each material; the shape of the vessel is under the other shelves.','ax':'kinds by material: iron, enamelled iron, steel, clad stainless, copper, non-stick coatings, clay, ceramic and glass, then aluminised bakeware','k':[
 kind('Cast-iron cookware','Heavy pans and pots in seasoned cast iron, which heats slowly and evenly and rusts unless oiled.',CWP,cast,'One entry is a named line or maker of seasoned cast-iron cookware; sizes and collections are versions.','Defining lines named by the fetched Lodge history page, plus the vintage American makers and Nambu ironware kept from the structure pass. Covers 8 lines; no whole-space reference lists cast-iron cookware.'),
 kind('Enamelled cast-iron cookware','Cast-iron pots and pans coated in glass enamel, so they need no seasoning and take acidic food.',CWP,enam,'One entry is a named line of enamelled cast-iron cookware; colours and sizes are versions.','Le Creuset and Staub named by their fetched Wikipedia pages as defining makers; other lines kept from the structure pass. Covers 8 lines; no whole-space reference lists enamelled cookware.'),
 kind('Carbon-steel cookware','Thin steel pans that are seasoned like cast iron but are lighter and respond quickly to heat.',CWP,carb,'One entry is a named line of carbon-steel cookware; sizes and finishes are versions.','de Buyer Mineral B named in the brief and the de Buyer Wikipedia page; the hammered wok kept from the structure pass. Covers 2 lines; no whole-space reference lists carbon-steel pans.'),
 kind('Clad stainless-steel cookware','Pans of stainless steel bonded around an aluminium or copper core, so they heat evenly and do not react with food.',CWP,clad,'One entry is a named line of clad stainless cookware; ply count and core are versions.','All-Clad D3 named in the brief and described on its fetched Wikipedia page; one other line kept from the structure pass. Covers 2 lines; no whole-space reference exists.'),
 kind('Copper cookware','Copper pans and pots that conduct heat fastest, lined with tin or steel for food contact.',CWP,copper,'One entry is a named line or maker of copper cookware; handle and thickness variants are versions.',"Mauviel M'Heritage lines read from Mauviel's own fetched history page; other houses kept from the structure pass. Covers 5 lines; no whole-space reference exists."),
 kind('Non-stick cookware','Pans with a coated surface that food releases from; the coating wears and the pan is replaced.',CWP,nonst,'One entry is a named non-stick cookware brand or line.','Tefal and Calphalon from their owners\' fetched Wikipedia pages (Groupe SEB, Newell Brands); Scanpan kept from the structure pass. Covers 3 brands; no whole-space reference exists.'),
 kind('Clay, ceramic & glass cookware','Oven and flame-proof vessels in clay, glazed ceramic, stoneware or borosilicate glass.',CWP,clay,'One entry is a named line of clay, ceramic or glass cookware.','Kept from the structure pass; the fetched Cookware and bakeware page lists the materials but no brands. Covers 7 lines; no whole-space reference exists.'),
 kind('Aluminium & coated-steel bakeware','Baking sheets, tins and moulds in aluminium, aluminised steel, steel or silicone.',CWP,alu,'One entry is a named bakeware line; sizes are versions.','Kept from the structure pass; no brand list was found on a fetched page. Covers 11 lines; no whole-space reference exists.'),
]}
# pressure cooker, fondue, paella: keep remaining entries in form kinds with market fields
rest={'Pressure cooker':['Kuhn Rikon Duromatic','Fissler Vitavit','Hawkins Classic','Prestige pressure cooker'],'Fondue set':['Spring fondue set'],'Paella pan':['Garcima Valencian paella pan','Vaello La Valenciana paella pan'],'Tagine':['Emile Henry Flame tagine'] }
placed=set(e['n'] for kk in mat_shelf['k'] for e in kk['x'])
CTYN={'Pressure cooker':'','Fondue set':'Switzerland','Paella pan':'Spain'}
for sh in cw['s']:
    for k in sh['k']:
        if k['n'] in ('Pressure cooker','Fondue set','Paella pan'):
            xs=[]
            for nm in rest[k['n']]:
                e=clone(nm,CE); fin(e); e['g']=e['cty'] or 'Other'; xs.append(e)
            k['x']=xs
            k['nl']='One entry is a named line or maker of this vessel; models are versions.'
            k['sel']='Kept from the structure pass; no whole-space reference lists them. Covers %d lines.'%len(xs)
            k['xg']='by country of the maker'
# any old entry not placed?
used=set(placed)|{'Lodge cast-iron skillet','Le Creuset Cocotte','Staub La Cocotte','de Buyer Mineral B carbon-steel frying pan','All-Clad D3 Stainless fry pan',"Mauviel M'250 copper frying pan","Mauviel M'Héritage copper saucepan",'Tefal non-stick frying pan','de Buyer Mineral B crêpe pan','Emile Henry pie dish','Pyrex glass pie plate','USA Pan 12-cup muffin tin'}
for k,(kn,e) in CE.items():
    pass
cw['s'].insert(0,mat_shelf)
# see pointers for form kinds
for sh in cw['s']:
    for k in sh['k']:
        if k['n'] in ('Frying pan','Sauté pan','Wok','Dutch oven','Saucepan'):
            k['see']=(k.get('see') or [])+[['B5','Cast-iron cookware','named lines by material']] if False else k.get('see')
cw['t']='Vessels that food is cooked in on the hob or in the oven: pans, pots, pressure and steam cookers and oven tins, sorted by material and by shape; electric cookers → Kitchen appliances, barbecue grills → Garden.'
cw['ax']='What is the vessel made of, and how is the food cooked in it: fried in an open pan, simmered or braised in a pot, pressured or steamed, or baked in an oven tin?'
cw['note']='Material comes first, with the defining named lines as entries; shape (pan, pot, tray, tin) is the second view. Forms that are commodities hold no entries.'
cw['msum']='Cookware market figures from one fetched market report and the makers\' own Wikipedia pages; analyst reports give different totals, so each figure is quoted with its source and year.'
GM='https://www.gminsights.com/pressrelease/cookware-market'
cw['ms']=[
 {'mkt':'Global cookware','who':'All makers','share':'USD 37.5 billion','yr':2025,'s':GM,'note':'market size as the report states it; the same page gives USD 39.2 billion for 2026 and USD 56.5 billion by 2035 as forecasts'},
 {'mkt':'Global cookware','who':'Groupe SEB','share':'over 7 %','yr':2025,'s':GM,'note':'share of the global market; the page names SEB as the leader'},
 {'mkt':'Global cookware','who':'Groupe SEB, Tramontina, Newell Brands, TTK Prestige and Hawkins Cookers','share':'about 13 %','yr':2025,'s':GM,'note':'combined share of the top five players'},
 {'mkt':'Global cookware, non-stick','who':'Non-stick cookware','share':'40.7 %','yr':2023,'s':GM,'note':'share of the narrower cookware market, USD 12.6 billion, a CIC estimate quoted by the report'},
 {'mkt':'Le Creuset revenue','who':'Le Creuset','share':'USD 850 million','yr':2025,'s':W+'Le_Creuset','note':'revenue from the page infobox, citing a 2025 Wall Street Journal article'},
 {'mkt':'Staub sales','who':'Staub','share':'about EUR 44 million','yr':2007,'s':W+'Staub_(cookware)','note':'sales, roughly half from abroad, before Zwilling bought the firm in 2008'},
 {'mkt':'Groupe SEB revenue','who':'Groupe SEB','share':'EUR 8.0 billion','yr':2023,'s':W+'Groupe_SEB','note':'whole group, including small appliances; its cookware brands include Tefal, All-Clad, Lagostina, WMF and Supor'},
 {'mkt':'Tramontina revenue','who':'Tramontina','share':'R$ 10.1 billion','yr':2021,'s':W+'Tramontina','note':'whole Brazilian group (cutlery, cookware, tools, appliances), sold in 120 countries'},
]

# ===================== KNIVES =========================
kn=copy.deepcopy(D['Knives & cutting'])
for sh in kn['s']:
    for k in sh['k']:
        k.pop('x',None); k.pop('m',None); k.pop('r',None)
KN='https://en.wikipedia.org/wiki/Kitchen_knife'; JK=W+'Japanese_kitchen_knife'
def L(n,mk,g,y,d,s,v=None,a='',role=None,own=None):
    e={'n':n,'a':a,'d':d,'mk':mk,'y':y,'s':s,'v':v or [],'g':g}
    if role: e['role']=role
    return fin(e)
def oldv(nm): return [ver(v['n'],KE[nm][1].get('mk',''),v.get('y',''),v.get('d','') or '') for v in KE[nm][1].get('v',[])]
lines=[
 L('Wüsthof Classic','Wüsthof','Germany','1814',"Forged knives from Wüsthof of Solingen, a family firm recorded there since 1814; the Classic series has about 70 items with a triple-riveted black handle.",W+'Wüsthof',
   [ver('Classic Ikon','Wüsthof','','half bolster, second bolster on the butt, curved handle'),ver('Grand Prix II','Wüsthof','','forged with full-length bolster, rivet-free handle'),ver('Gourmet','Wüsthof','','stamped rather than forged, originally named Emerilware'),ver('Epicure','Wüsthof','','forged, two-riveted composite handle')],a='Wusthof Classic · Ikon'),
 L('Zwilling Four Star','Zwilling J. A. Henckels','Germany','1976',"Solingen forged knives from the house founded in 1731; Four Star has a fully forged blade and a moulded polypropylene handle.",W+'Zwilling_J._A._Henckels',[ver('Four Star','Zwilling J. A. Henckels','1976','fully forged blade, moulded polypropylene handle')],a='Henckels Four Star'),
 L('Zwilling Pro','Zwilling J. A. Henckels','Germany','',"Solingen forged chef's knife line with a curved bolster for a pinch grip.",W+'Zwilling_J._A._Henckels',oldv('Zwilling Four Star / Pro')[1:],a='Zwilling Professional S'),
 L('Victorinox Fibrox','Victorinox','Switzerland','',"Stamped Swiss stainless knives with a non-slip Fibrox handle from Victorinox of Ibach, founded 1884; sold under the Forschner name in North America until 2011.",W+'Victorinox',oldv('Victorinox Fibrox'),a='Forschner Fibrox · Fibrox Pro'),
 L('K Sabatier Authentique','K Sabatier','France','1834',"Thiers house descended from Philippe Sabatier of Bellevue; it has sold under the Sabatier-K name since 1834 and says it is the oldest Sabatier maker still operating.",W+'Sabatier',[ver('Authentique','K Sabatier','current','forged in Thiers')],role='origin',a='Sabatier-K'),
 L('Thiers-Issard Sabatier Elephant','Thiers-Issard','France','1958',"Sabatier Elephant knives made in Thiers since 1958.",W+'Sabatier',[ver('4 Star Elephant','Thiers-Issard','since 1958','')]),
 L('Sabatier Trompette','Amefa','France','',"The Trompette and V Sabatier ranges are owned by Amefa; Amefa bought Couzon in 2005 and Richardson Sheffield in 2007.",W+'Sabatier',[]),
 L('Lion Sabatier','Rousselon Frères','France','1991',"Mexeur Lion Sabatier knives, made by Rousselon Frères since 1991; the firm claims the mark was registered in 1812.",W+'Sabatier',[]),
 L('Opinel Parallèle','Opinel','France','',KE['Opinel Parallèle'][1]['d'],KE['Opinel Parallèle'][1]['s'],oldv('Opinel Parallèle')),
 L('Global G series','Global','Japan','1985',"Stainless Japanese knives from Yoshida Metal Industry of Tsubame, designed by Komin Yamada; the G series was listed by the Japanesque Modern Committee in 2006.",W+'Global_(cutlery)',
   [ver("G-2 cook's knife 20 cm",'Global','1985','dimpled hollow handle, CROMOVA 18 steel'),ver('G-46 santoku 18 cm','Global','','santoku'),ver('G-5 nakiri 18 cm','Global','','vegetable knife'),ver('SAI','Global','','later line'),ver('UKON','Global','','later line'),ver('NI','Global','2015','most recent line on the page')],role='landmark',a='Global G-2 · G-46 · G-5'),
 L('Shun Classic','Shun','Japan','2002',"Kai Group knives made in Seki; the Shun brand reached the Western market in 2002 and Classic is the first line of its series.",W+'Shun_Cutlery',
   [ver('Classic Hollow-Ground Santoku 7 in (DM0702)','Shun','',"VG-MAX core, layered Damascus cladding"),ver('Classic 8 in Kiritsuke (DM0771)','Shun','',"kiritsuke-gyuto"),ver('Classic Blonde','Shun','','')],a='Shun Classic DM0702'),
 L('Misono UX10','Misono','Japan','1935',"Family-owned Misono, founded 1935 and called Japan's oldest Western-style knife maker; UX10 in Swedish stainless steel is the top of its range.",'https://korin.com/HMI-UXSU-270',
   [ver('UX10 gyuto 180–300 mm','Misono','current',''),ver('UX10 sujihiki','Misono','current','slicing knife, HRC 60'),ver('UX10 petty','Misono','current','')]),
 L('Misono Swedish Carbon','Misono','Japan','',"Misono's carbon-steel range with riveted Western handles.",KE['Misono Swedish Carbon Honesuki'][1]['s'],oldv('Misono Swedish Carbon Honesuki')),
 L('Tojiro DP','Tojiro','Japan','1953',"Three-layer knives with a VG-10 core clad in softer stainless, from Tojiro (founded as Fujitora Farm Equipment in Tsubame, 1953).",'https://globalkitchenjapan.com/products/tojiro-fujitora-dp-3-layer-gyuto-knife',
   [ver('DP gyuto 180–300 mm','Tojiro','current',''),ver('DP santoku 170 mm','Tojiro','current',''),ver('DP nakiri 165 mm','Tojiro','current',''),ver('DP honesuki 150 mm (F-803)','Tojiro','current','')]),
 L('Tojiro Shirogami','Tojiro','Japan','',"Single-bevel White #2 steel knives with soft-iron cladding from Tojiro.",KE['Tojiro Shirogami Usuba'][1]['s'],oldv('Tojiro Shirogami Usuba')),
 L('MAC Professional','MAC Knife','Japan','1964',KE['MAC Professional'][1]['d'],KE['MAC Professional'][1]['s'],oldv('MAC Professional'),a='MAC MTH-80'),
 L('Masamoto KS','Masamoto Sohonten','Japan','1866',KE['Masamoto KS Wa-Gyuto'][1]['d'],KE['Masamoto KS Wa-Gyuto'][1]['s'],oldv('Masamoto KS Wa-Gyuto')),
 L('Masamoto Hongasumi','Masamoto Sohonten','Japan','1866',"Tokyo White #2 knives with hongasumi finish in the single-bevel patterns: yanagiba and deba.",KE['Masamoto Hongasumi Yanagi'][1]['s'],oldv('Masamoto Hongasumi Yanagi')+oldv('Masamoto Hongasumi Deba')),
 L('Takeda AS','Takeda Hamono','Japan','1920',KE['Takeda AS Gyuto'][1]['d'],KE['Takeda AS Gyuto'][1]['s'],oldv('Takeda AS Gyuto')+oldv('Takeda NAS Bunka')),
 L('Konosuke HD2','Konosuke','Japan','',KE['Konosuke HD2 Wa-Gyuto'][1]['d'],KE['Konosuke HD2 Wa-Gyuto'][1]['s'],oldv('Konosuke HD2 Wa-Gyuto')),
 L('Ashi Hamono Ginga','Ashi Hamono','Japan','',KE['Ashi Hamono Ginga Gyuto'][1]['d'],KE['Ashi Hamono Ginga Gyuto'][1]['s'],oldv('Ashi Hamono Ginga Gyuto')),
 L('Yoshikane SKD Nashiji','Yoshikane Hamono','Japan','1919',"Sanjo hammer-forged knives in semi-stainless SKD with a pear-skin finish, made as gyuto, bunka, nakiri and kiritsuke.",KE['Yoshikane SKD Nashiji Gyuto'][1]['s'],oldv('Yoshikane SKD Nashiji Gyuto')+oldv('Yoshikane SKD Bunka')+oldv('Yoshikane SKD Nashiji Nakiri')+oldv('Yoshikane Nashiji Kiritsuke')),
 L('Takamura Migaki SG2','Takamura Hamono','Japan','',KE['Takamura Migaki SG2 Gyuto'][1]['d'],KE['Takamura Migaki SG2 Gyuto'][1]['s'],oldv('Takamura Migaki SG2 Gyuto')),
 L('Teruyasu Fujiwara Denka','Teruyasu Fujiwara','Japan','',KE['Teruyasu Fujiwara Denka Gyuto'][1]['d'],KE['Teruyasu Fujiwara Denka Gyuto'][1]['s'],oldv('Teruyasu Fujiwara Denka Gyuto')),
 L('Shigefusa','Shigefusa','Japan','1964',"Collector's knives from the Iizuka forge in Sanjo: hand-forged carbon steel in kitaeji and kurouchi finishes.",KE['Shigefusa Kitaeji Wa-Gyuto'][1]['s'],oldv('Shigefusa Kitaeji Wa-Gyuto')+oldv('Shigefusa Kurouchi Nakiri')),
 L('Tadafusa Nashiji','Tadafusa','Japan','1948',KE['Tadafusa Nashiji Nakiri'][1]['d'],KE['Tadafusa Nashiji Nakiri'][1]['s'],oldv('Tadafusa Nashiji Nakiri')),
 L('Moritaka AS','Moritaka Hamono','Japan','',KE['Moritaka AS Kiritsuke'][1]['d'],KE['Moritaka AS Kiritsuke'][1]['s'],oldv('Moritaka AS Kiritsuke')),
 L('Sakai Takayuki Kasumitogi','Sakai Takayuki','Japan','',"Sakai-forged White-steel knives with kasumi finish: usuba and yanagiba.",KE['Sakai Takayuki Kasumitogi Kamagata Usuba'][1]['s'],oldv('Sakai Takayuki Kasumitogi Kamagata Usuba')+oldv('Sakai Takayuki Kasumitogi Yanagiba')),
 L('Sakai Takayuki Ginsan','Sakai Takayuki','Japan','',KE['Sakai Takayuki Ginsan Deba'][1]['d'],KE['Sakai Takayuki Ginsan Deba'][1]['s'],oldv('Sakai Takayuki Ginsan Deba')),
 L('CCK small slicer','Chan Chi Kee','China','',KE['CCK KF1303 small slicer'][1]['d'],KE['CCK KF1303 small slicer'][1]['s'],oldv('CCK KF1303 small slicer'),a='CCK KF1303'),
 L('Shibazi F208','Shibazi','China','',KE['Shibazi F208'][1]['d'],KE['Shibazi F208'][1]['s'],oldv('Shibazi F208')),
]
# owner overrides
for e in lines:
    if e['mk']=='Shun': e['own']='Kai Group'; e['tier']='Independent'
    if e['mk']=='Amefa': e['tier']='Independent'; e['cty']='France'; e['own']='Amefa'
    if e['mk']=='Thiers-Issard': e['cty']='France'
    if e['mk']=='Rousselon Frères': e['cty']='France'
    if e['mk']=='Sabatier Aîné & Perrier': e['cty']='France'
    if e['mk']=='Shun': e['cty']='Japan'
    if e['mk']=='Zwilling J. A. Henckels': e['own_y']='1970'
lines.sort(key=lambda e:(e['g'],str(e['y']) if e['y'] else '9999',e['n']))
for e in lines:
    if e['n']=='K Sabatier Authentique': e['mk']='K Sabatier'
knife_line={'n':'Kitchen knife line','a':'maker line · knife range','d':"A maker's named range of kitchen knives, sectioned by country. Makers sit in knife-making centres: Solingen in Germany, Thiers in France, and Seki, Sakai, Tsubame-Sanjo and Takefu-Echizen in Japan.",'s':KN,'x':lines,
 'nl':"One entry is a maker's named line of kitchen knives; sizes, knife patterns and revisions are versions.",
 'sel':"Lines named in the brief (Wüsthof Classic, Zwilling Pro, Global G series, Shun Classic, Victorinox Fibrox, Misono, Tojiro) and the Sabatier houses on the fetched Sabatier page, plus the smith and brand lines kept from the structure pass. No whole-space reference lists kitchen knife lines. Covers %d lines."%len(lines),
 'xg':'by country of the maker, then year, then name'}
knives_shelf={'n':'Makers & lines','t':'Named kitchen-knife ranges by maker and country; the shape of the knife is under the type shelves.','ax':'one kind: the maker line, sectioned by country','k':[knife_line]}
# type kinds
byk={k['n']:k for sh in kn['s'] for k in sh['k']}
def tk(n,d,s,a=''): return {'n':n,'a':a,'d':d,'s':s}
kn['s'][0]['k'][1]['d']=kn['s'][0]['k'][1]['d']
# update paring etc d with fetched facts
byk["Chef's knife"]['d']="General-purpose kitchen knife with a broad, curved blade for rocking cuts and chopping; 20 cm is the most common length."
byk['Bread knife']['d']="Long serrated knife for crusty bread; Friedrich Dick of Esslingen showed one at the 1893 Chicago World's Columbian Exposition and Joseph E. Burns of Syracuse held a US patent issued in 1921."
byk['Carving knife']['d']="Long thin blade for slicing cooked roasts, poultry and ham; the slicing knife is similar but longer and narrower."
byk['Cleaver']['d']="Heavy thick-spined blade for splitting meat and bone; the Chinese chef's knife (càidāo) is a lighter rectangular all-purpose cousin."
spec=[tk('Fillet knife','Very flexible blade for filleting fish.',KN),tk('Ham slicer','Long flexible blade with a rounded tip for thin slices of ham and smoked fish.',KN),tk('Cheese knife','Short or holed blades shaped for soft, semi-soft, medium-hard and hard cheese; the Parmesan knife is short, stubby and pointed.',KN),tk('Palette knife','Broad flexible rounded blade for spreading and icing.',KN),tk('Oyster knife','Short thick blade for opening oysters, in straight or club-shaped styles.',KN),tk('Tourné knife','Small curved bird\'s-beak blade for peeling and turning vegetables and garnishes.',KN,'peeling knife'),tk('Mezzaluna','Curved mincing blade rocked over the board to chop herbs.',KN,'mincing knife'),tk('Grapefruit knife','Long dull, usually serrated blade for separating grapefruit flesh.',KN),tk('Tomato knife','Small serrated blade for tomato skin and flesh.',KN)]
kn['s'].insert(1,{'n':'Specialist knives','t':'Small knives made for one food: fish, cheese, oysters, citrus and tomatoes; the table knife for steak and butter → Tableware.','ax':'kinds by the food they are made for: fish and ham, cheese, shellfish, vegetables and fruit, then spreading','k':spec})
# Japanese types: split by bevel as the fetched page does
jp_old=[s for s in kn['s'] if s['n']=='Japanese knives'][0]
jk={k['n']:k for k in jp_old['k']}
jk['Gyuto']['d']="Japanese version of the Western chef's knife, double-bevel, for general professional use."; jk['Santoku']['d']='Multipurpose double-bevel knife developed in the 1940s from the deba, nakiri and gyuto.'
jk['Bunka']['d']='Santoku variant with a more angular, straight tip.'; jk['Nakiri']['d']='Double-bevel vegetable knife with a flat edge and square tip.'
jk['Petty knife']['d']='Small paring or utility knife, often used beside the gyuto.'; jk['Sujihiki']['d']='Long double-bevel knife for slicing meat, like a Western carving knife.'
jk['Usuba']['d']='Thinnest single-bevel knife with a flat edge, for push-cutting thin vegetable sheets.'
jk['Kiritsuke']['d']='Large single-bevel hybrid with yanagiba length and usuba-style height, needing great control.'
jk['Yanagiba']['d']='Most popular single-bevel fish knife, for pull cuts and skinning; the tako-hiki and fugu-hiki are its variants.'
jk['Deba']['d']='Thick broad single-bevel knife for filleting fish and cutting bones and heads; variants include ko-deba, aji-kiri, funayuki, mioroshi deba and yo-deba.'
jk['Honesuki']['d']='Small triangular knife for deboning chicken; the thicker gara-suki can cut chicken bone.'
for k in jk.values(): k['s']=JK
new_j=[tk('Hankotsu','Pointed double-bevel boning knife for cutting meat from bone.',JK),tk('Katsuobushi-kiri','Short-bladed double-bevel knife for shaving katsuobushi, dried bonito.',JK),
 tk('Tako-hiki','Lighter, flatter Tokyo variant of the yanagiba with a square tip, for dense flesh such as octopus.',JK),tk('Fugu-hiki','Thin yanagiba variant with a round tip, for preparing pufferfish.',JK),
 tk('Mukimono','Angled-tip single-bevel vegetable knife for decorative cutting, used beside the usuba.',JK),tk('Hamo-kiri','Knife between deba and yanagiba in size, for pike conger.',JK),
 tk('Unagi-saki','Eel-cutting knife with regional styles from Kanto, Kyoto, Nagoya and Kyushu.',JK),tk('Soba-kiri','Large knife for cutting soba noodles; the udon-kiri is its udon variant.',JK),
 tk('Mochi-kiri','Knife for cutting mochi rice cake, in single- or double-handle versions.',JK),tk('Maguro-kiri','Very large knife for bluefin tuna, rarely found in home kitchens.',JK)]
dbl=['Gyuto','Santoku','Bunka','Nakiri','Petty knife','Sujihiki']
sgl=['Yanagiba','Deba','Usuba','Kiritsuke','Honesuki']
sh_d={'n':'Japanese double-bevel knives','t':'Japanese everyday knives ground on both sides, held like a Western knife: the gyuto, santoku, bunka and nakiri and the small and long knives that go with them.','ax':'kinds by the work: all-purpose, vegetable, small, slicing, boning, then bonito','k':[jk[n] for n in dbl]+new_j[:2]}
sh_s={'n':'Japanese single-bevel knives','t':'Japanese knives ground on one side, made for one food: fish, vegetables, eel, noodles, mochi and tuna.','ax':'kinds by the food: sashimi fish, filleting, vegetables, boning, then eel, noodles, rice cake and tuna','k':[jk[n] for n in sgl]+new_j[2:]}
kn['s']=[s for s in kn['s'] if s['n']!='Japanese knives']
idx=[i for i,s in enumerate(kn['s']) if s['n']=='Western kitchen knives'][0]
kn['s'][idx+2:idx+2]=[sh_d,sh_s]
kn['s'].insert(0,knives_shelf)
# boards etc: drop entries; whetstone keeps
for sh in kn['s']:
    for k in sh['k']:
        if k['n']=='Whetstone':
            xs=[]
            for nm in ['Naniwa Chosera / Professional','Naniwa Super Stone','Shapton Kuromaku Pro','Shapton Glass Stone','King 1000/6000 combination stone','Atoma diamond plate']:
                e=clone(nm,KE); fin(e); e['g']='Japan'; xs.append(e)
            k['x']=xs; k['nl']='One entry is a named range of sharpening stones; grits are versions.'
            k['sel']='Kept from the structure pass (Japanese water-stone ranges named on retailer pages); no whole-space reference lists whetstones. Covers 6 ranges.'; k['xg']='by country of the maker'
kn['t']="Kitchen knives by type and by maker line, the boards and slicers used with them, and the tools that keep an edge; pocket and outdoor knives → C1, fighting and hunting knives → E4."
kn['ax']='Is it a knife of the Western pattern, a knife of the Japanese pattern, a maker line, something to cut on or with, or something that sharpens or stores knives?'
kn['note']='Knife types are the kinds; maker lines are entries sectioned by country. Knife-making centres: Solingen, Thiers, Seki, Sakai, Tsubame-Sanjo and Takefu-Echizen.'
kn['msum']='No market-share figures for kitchen knives were found on a fetched page; centres and makers are described in the entries.'
kn['ms']=[]

# ===================== TOOLS =========================
kt=copy.deepcopy(D['Kitchen tools & measuring'])
for sh in kt['s']:
    for k in sh['k']:
        k.pop('x',None); k.pop('m',None); k.pop('r',None)
tb={k['n']:k for sh in kt['s'] for k in sh['k']}
CO='https://en.wikipedia.org/wiki/Can_opener'; PE='https://en.wikipedia.org/wiki/Vegetable_peeler'
yea=fin({'n':'Yeates claw-ended can opener','a':'','d':'Claw-ended can opener devised in 1855 by Robert Yeates, a cutlery and surgical instrument maker in Hackney; the first of its kind on the page.','mk':'Robert Yeates','y':'1855','s':CO,'v':[],'g':'United Kingdom','role':'origin'})
yea['own']='Robert Yeates'; yea['tier']='Independent'; yea['cty']='United Kingdom'
tb['Can opener'].update({'x':[yea],'nl':'One entry is a can opener that the fetched history page names as the first of its kind or held by a design collection.','sel':'Icon rule for commodity kinds: the origin entry only. Covers 1 entry; Ezra Warner\'s 1858 sickle-based opener (adopted by the US Army in the Civil War) is described in the kind text.','xg':'by year'})
tb['Can opener']['d']='Hand tool for opening tin cans; Ezra Warner patented a sickle-based opener in 1858 that the US Army adopted in the Civil War, but its bare blade was thought too dangerous for the home.'
oxo=fin({'n':'OXO Good Grips swivel peeler','a':'Good Grips peeler','d':'Soft-handled peeler designed by Smart Design for OXO in 1990; Cooper Hewitt holds a Good Grips peeler in its packaging (gift of Smart Design, 2011-50-21).','mk':'OXO','y':'1990','s':'https://www.cooperhewitt.org/2013/06/21/remembering-sam-farber/','v':[],'g':'United States','role':'landmark'})
oxo['own']='OXO'; oxo['tier']='Independent'; oxo['cty']='United States'
tb['Peeler']['x']=[oxo]
tb['Peeler']['nl']='One entry is a peeler held by a named design collection.'
tb['Peeler']['sel']='Icon rule for commodity kinds: design-canon landmarks held by a named design collection. Covers 1 entry; the Econome (1928), Jonas (1953) and Zena Rex (1947, called an icon of Swiss design) are named in the kind text only.'
tb['Peeler']['xg']='by year'
tb['Peeler']['d']='Hand tool that strips the skin from fruit and vegetables: the straight Econome (1928), the swivel Jonas (1953) and the Y-shaped Zena Rex (1947).'
tb['Peeler']['s']=PE
tb['Pepper mill']['d']='Hand grinder for peppercorns; Peugeot patented a case-hardened steel grinding mechanism in 1842 and still makes about 2.5 million grinders a year in France.'
tb['Pepper mill']['s']='https://en.wikipedia.org/wiki/Pepper_mill'
for n in ['Mortar and pestle']:
    tb[n]['d']=tb[n]['d']+' Regional forms include the Mexican molcajete and the Japanese suribachi.' if 'molcajete' not in tb[n]['d'] else tb[n]['d']
kt['msum']='No market-share figures for kitchen tools were found on a fetched page; these are commodity kinds with at most one origin or design-collection entry.'
kt['ms']=[]

# ===================== OUTPUT =========================
for dp in (cw,kn,kt):
    dp.setdefault('b',D[dp['n']]['b'])
part={'replaces':['Cookware & bakeware','Knives & cutting','Kitchen tools & measuring'],'depts':[cw,kn,kt],'brands':[],'brand_updates':{},'renames':{},'moves':[]}
# renames
part['renames']={'Japanese knives':'Japanese double-bevel knives'}
# keep Japanese single-bevel too; rename maps old kind-shelf? kinds all reappear, so renames empty
part['renames']={}
# brand updates
BU={'Staub':('Zwilling J. A. Henckels','Global group','France'),'Tefal':('Groupe SEB','Global group','France'),'All-Clad':('Groupe SEB','Global group','United States'),'Zwilling J. A. Henckels':('Werhahn KG','Global group','Germany'),'Calphalon':('Newell Brands','Global group','United States'),'Le Creuset':('Paul van Zuydam','Independent','France'),'Victorinox':('Victorinox-Stiftung','Independent','Switzerland'),'Shun':('Kai Group','Independent','Japan'),'Global':('Yoshida Metal Industry','Independent','Japan'),'Tojiro':('Tojiro Co Ltd','Independent','Japan'),'Misono':('Misono','Independent','Japan'),'Wüsthof':('Wüsthof','Independent','Germany'),'Lodge':('Lodge Cast Iron','Independent','United States'),'Mauviel':('Mauviel 1830','Independent','France'),'de Buyer':('de Buyer','Independent','France'),'K Sabatier':('Sabatier Aîné & Perrier','Independent','France'),'Opinel':('Opinel','Independent','France'),'MAC Knife':('MAC Knife','Independent','Japan')}
for n,(o,t,c) in BU.items():
    if n in reg: part['brand_updates'][n]={'own':o,'tier':t,'c':c}
NEW=[('Groupe SEB','France','1857','Écully, near Lyon; cookware brands include Tefal, All-Clad, Lagostina, WMF, Supor and Mirro; group revenue EUR 8.0 billion in 2023.',W+'Groupe_SEB'),
('Newell Brands','United States','1903','Atlanta group founded in Ogdensburg, New York; owns Calphalon (acquired 1998), Crock-Pot, Mr. Coffee, Oster, Sunbeam, Rubbermaid and Ball.',W+'Newell_Brands'),
('Werhahn KG','Germany','','Neuss family group that has owned Zwilling J. A. Henckels since 1970.',W+'Zwilling_J._A._Henckels'),
('Kai Group','Japan','1908','Tokyo group founded in Seki by Saijiro Endo; makes Shun knives.',W+'Shun_Cutlery'),
('Yoshida Metal Industry','Japan','1954','Tsubame maker of Global knives (the Yoshikin factory), founded as a Western tableware maker in 1954.',W+'Global_(cutlery)'),
('Tramontina','Brazil','1911','Family-run metal-goods group at Carlos Barbosa, Rio Grande do Sul; cutlery, cookware and tools sold in 120 countries.',W+'Tramontina'),
('Victorinox-Stiftung','Switzerland','','Foundation that holds 90 % of Victorinox AG.',W+'Victorinox'),
('Amefa','','','Owner of the Sabatier Trompette and V Sabatier ranges; bought Couzon in 2005 and Richardson Sheffield in 2007.',W+'Sabatier'),
('Thiers-Issard','France','','Thiers maker of Sabatier Elephant knives since 1958.',W+'Sabatier'),
('Rousselon Frères','France','','Thiers maker of Mexeur Lion Sabatier knives since 1991.',W+'Sabatier'),
('Robert Yeates','United Kingdom','','Hackney cutler and surgical instrument maker who devised the first claw-ended can opener in 1855.',CO),
('TTK Prestige','India','','Indian cookware maker named among the top five global cookware players in a 2025 market report.',GM),
('Hawkins Cookers','India','','Indian pressure-cooker maker named among the top five global cookware players in a 2025 market report.',GM),
('Paul van Zuydam','','','Owner of Le Creuset since 1988.',W+'Le_Creuset')]
for n,c,f,d,s in NEW:
    if n in reg: continue
    part['brands'].append({'n':n,'c':c,'f':f,'seg':'Specialist','d':d,'lines':[],'eras':[],'sig':[],'sc':[],'rel':[],'s':s,'kf':'','own':n,'tier':'Global group' if n in('Groupe SEB','Newell Brands','Werhahn KG') else 'Independent'})
json.dump(part,open(ROOT+'rebuild/out/B5_parts/COOK.json','w'),ensure_ascii=False,indent=1)
# stats
for dp in part['depts']:
    n=sum(len(k.get('x',[])) for s in dp['s'] for k in s['k']); print(dp['n'],'entries',n,'kinds',sum(len(s['k']) for s in dp['s']))
# unplaced old
placed_names=set()
print('done')
