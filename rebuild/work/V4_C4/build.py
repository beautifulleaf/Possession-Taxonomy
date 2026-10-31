import json,re,os,copy
R='/home/user/Possession-Taxonomy/rebuild/'
OUT='/home/user/Possession-Taxonomy/rebuild/work/V4_C4/'
d=json.load(open(R+'out/C4.json')); bj=json.load(open(R+'out/C4_brands.json')); B={x['n']:x for x in bj['b']}
BL={n.lower():n for n in B}
ren=json.load(open(R+'out/C4_renames.json'))
log={'conv_ver':0,'conv_ent':0,'dropped':[],'removed_x':[]}
# --- owners (fetched) ---
W='https://en.wikipedia.org/wiki/'
OWN={ # maker: (own,tier,own_y,src)
 'Winsor & Newton':('Colart','Global group',None,W+'ColArt'),
 'Liquitex':('Colart','Global group','2000',W+'ColArt'),
 'Conté':('Colart','Global group','2004',W+'ColArt'),
 'Conté à Paris':('Colart','Global group','2004',W+'ColArt'),
 'Canson':('F.I.L.A. S.p.A.','Global group','2016',W+'Canson'),
 'Sharpie':('Newell Brands','Global group','1992',W+'Newell_Brands'),
 "Elmer's":('Newell Brands','Global group','2015',W+'Newell_Brands'),
 'Singer':('SVP Worldwide','Global group',None,W+'SVP_Worldwide'),
 'Husqvarna Viking':('SVP Worldwide','Global group',None,W+'SVP_Worldwide'),
 'Pfaff':('SVP Worldwide','Global group',None,W+'SVP_Worldwide'),
 'Fiskars':('Fiskars Group','Global group',None,W+'Fiskars'),
}
newbrands=[('Colart','Sweden','1992','Art materials group owned by Lindéngruppen; owns Winsor & Newton, Liquitex and Conté à Paris.',W+'ColArt'),
 ('F.I.L.A. S.p.A.','Italy','','Milan-based group that bought Canson in 2016.',W+'Canson'),
 ('Newell Brands','','','Owner of Sharpie (bought 1992) and Elmer\'s (bought 2015).',W+'Newell_Brands'),
 ('SVP Worldwide','United States','','Nashville sewing-machine group that owns Singer, Husqvarna Viking and Pfaff.',W+'SVP_Worldwide'),
 ('Fiskars Group','Finland','1649','Finnish maker of scissors and garden tools, founded in Fiskars, Raseborg.',W+'Fiskars')]
for n,c,f,dd,s in newbrands:
    if n not in B:
        x={'n':n,'c':c,'f':f,'seg':'Mainstream','kf':'brand group','d':dd,'s':s,'sig':[]}; bj['b'].append(x); B[n]=x
def brandify(x):
    mk=x.get('mk'); 
    if not mk: return
    b=B.get(BL.get(mk.lower(),mk))
    if b and b.get('c'): x['cty']=b['c']; x['g']=b['c']
    elif b: x['g']='Country not stated'
    else: x['g']='Country not stated'
    if mk in OWN:
        o,t,y,s=OWN[mk]; x['own']=o; x['tier']=t
        if y: x['own_y']=y
        x['own_s']=s
def yr(x):
    m=re.search(r'\d{4}',str(x.get('y','')));return int(m.group()) if m else 9999
def finish_kind(k,nl,sel,xg="by the maker's home country"):
    k['nl']=nl;k['sel']=sel
    if any(x.get('g') for x in k['x']):
        k['xg']=xg
        order=sorted({x.get('g','Country not stated') for x in k['x']},key=lambda g:(g=='Country not stated',g))
        for x in k['x']: x.setdefault('g','Country not stated')
        k['x'].sort(key=lambda x:(order.index(x['g']),yr(x),x['n']))
def mname(m,mk):
    return m if mk.split()[0].lower() in m.lower() else f"{mk} {m}"
SEL_GEN=("No complete reference lists this space. The entries are the lines named by the fetched overview or maker page cited on each entry, "
 "with the loose models the earlier pass gathered placed as versions of their maker's line or as entries sourced to the maker's own page.")
for dp in d['depts']:
  for s in dp['s']:
    for k in s['k']:
      kn=k['n']; low=kn[0].lower()+kn[1:] if kn[1:2].islower() else kn
      x=k.setdefault('x',[]) if (k.get('x') or k.get('m')) else None
      # fabric houses are makers, not entries
      if kn in('Quilting and printed cotton','Denim','Wax-print fabric'):
        for e in k.get('x',[]):
          log['removed_x'].append((kn,e['n'],e['mk']))
          b=B.get(e['mk'])
          if b is not None and e['n'] not in b.setdefault('sig',[]): b['sig'].append(e['n'])
        k['x']=[]; k.pop('nl',None); continue
      if x is None: continue
      for e in x: brandify(e)
      byk={}
      for e in x: byk.setdefault(e.get('mk'),e)
      for m,mk in k.get('m',[]) or []:
        mk=BL.get(mk.lower(),mk) if mk else mk
        if mk in byk:
          e=byk[mk]; vs=e.setdefault('v',[])
          if not any(v['n']==m for v in vs) and e['n']!=m:
            vs.append({'n':m,'mk':mk,'y':'','d':f"model in {mk}'s range"}); log['conv_ver']+=1
        elif mk in B and B[mk].get('s'):
          nn=mname(m,mk)
          if any(e['n']==nn for e in x): continue
          e={'n':nn,'d':f"A {low.lower()} in the {mk} range.",'mk':mk,'s':B[mk]['s'],'v':[]}; brandify(e); x.append(e); byk.setdefault(mk,e); log['conv_ent']+=1
        else: log['dropped'].append((kn,m,mk))
      k.pop('m',None)
      if x:
        finish_kind(k,f"One entry is a maker's named {low.lower()} line sold under its own name; sizes, colours and student or artist grades are versions.",SEL_GEN)
      else: k.pop('nl',None)
# --- pigments ---
IN='https://en.wikipedia.org/wiki/List_of_inorganic_pigments'
inorg={'Purple':[('Ultramarine violet','PV15'),('London purple',''),('Han purple',''),('Cobalt violet','PV14'),('Purple of Cassius',''),('Caput mortuum (Mars violet)',''),('Manganese violet','PV16'),('Strontium violet','PV62')],
'Blue':[('Ultramarine','PB29'),('Smalt',''),('Cobalt blue','PB28'),('Cerulean blue','PB35'),('Cerium uranium blue',''),('Cobalt chromite blue-green spinel','PG50'),('Cobalt zinc aluminate spinel','PB36'),('Azurite',''),('Blue verditer',''),('Prussian blue','PB27'),('Vivianite',''),('YInMn blue',''),('Manganese blue',''),('Zirconium-vanadium blue zircon','PB74')],
'Green':[("Scheele's green",''),('Paris green',''),('Cadmium green',''),('Chrome green','PG17'),('Viridian','PG18'),('Cobalt green',''),('Cobalt titanate green',''),('Malachite',''),('Brunswick green',''),('Verdigris',''),('Atacamite',''),('Brochantite',''),('Green verditer',''),('Egyptian green',''),('Green earth','')],
'Yellow':[('Orpiment',''),('Pararealgar',''),('Primrose yellow','PY184'),('Bismuth molybdate','PY227'),('Cadmium yellow','PY37'),('Cadmium lemon','PY37'),('Chrome yellow','PY34'),('Strontium yellow','PY32'),('Barium yellow','PY31'),('Zinc yellow','PY36'),('Aureolin','PY40'),('Yellow ochre','PY43'),('Mars yellow','PY42'),('Naples yellow','PY41'),('Lead-tin yellow',''),('Massicot',''),('Titanium yellow','PY53'),('Mosaic gold','')],
'Orange':[('Realgar',''),('Bismuth vanadate orange','PO86'),('Bismuth oxyhalide orange','PO85'),('Cadmium orange','PO20')],
'Red':[('Cadmium red','PR108'),('Cerium sulfide red','PR265'),('Oxide red (sanguine, Indian red, Venetian red)','PR102'),('Red ochre','PR102'),('Burnt sienna','PBr7'),('Minium',''),('Vermilion','PR106')],
'Brown':[('Raw umber','PBr7'),('Raw sienna','PBr7')],
'Black and grey':[('Aniline black','PBk1'),('Lamp black','PBk6'),('Carbon black','PBk7'),('Vine black','PBk8'),('Ivory black','PBk9'),('Graphite','PBk10'),('Mineral black','PBk18'),('Mars black (iron black)','PBk11'),('Manganese dioxide','PBk14'),('Iron manganese oxide','PBk33'),('Molybdenum disulfide','PBk34'),('Titanium black',''),('Titanium dioxide black','PBk35'),('Iron titanium brown spinel','PBk12'),('Cobalt black','PBk13'),('Zinc sulfide','PBk17'),('Slate black','PBk19'),('Copper chromite black','PBk22, PBk28'),('Tin antimony grey','PBk23'),('Titanium vanadium antimony grey','PBk24'),('Cobalt nickel grey','PBk25'),('Manganese ferrite black','PBk26'),('Iron cobalt chromite black','PBk27'),('Iron cobalt black','PBk29'),('Chrome iron nickel black','PBk30')],
'White':[('Antimony white',''),('Barium sulfate (baryte)','PW5'),('Lithopone',''),('Cremnitz white','PW1'),('Titanium white','PW6'),('Zinc white','PW4'),('Sachtolith','')],
'Fluorescent':[('Uranium salts (uranates)','')]}
PG='https://en.wikipedia.org/wiki/Pigment'; CP='https://en.wikipedia.org/wiki/Copper_phthalocyanine'; QU='https://en.wikipedia.org/wiki/Quinacridone'; CAT='https://en.wikipedia.org/wiki/Category:Organic_pigments'
org={'Blue':[('PB15','Phthalo blue (copper phthalocyanine)',CP),('PB16','Metal-free phthalocyanine blue',CP)],
'Green':[('PG7','Phthalocyanine green (chlorinated copper phthalocyanine)',CP),('PG36','Phthalocyanine green (brominated)',CP)],
'Purple':[('PV19','Quinacridone violet',QU),('PV23','Dioxazine violet',CAT)],
'Yellow':[('PY1','Arylide yellow (PY1)',PG),('PY3','Arylide yellow (PY3)',PG),('PY74','Arylide yellow (PY74)',PG),('PY83','Diarylide yellow (PY83)',PG),('PY128','Disazo condensation yellow',PG),('PY154','Benzimidazolone yellow',PG),('PY155','Disazo yellow (acetoacetic anilide)',PG),
 ('PY10','Pigment Yellow 10',CAT),('PY12','Pigment Yellow 12',CAT),('PY13','Pigment Yellow 13',CAT),('PY14','Pigment Yellow 14',CAT),('PY16','Pigment Yellow 16',CAT),('PY81','Pigment Yellow 81',CAT),('PY139','Pigment Yellow 139',CAT),('PY185','Pigment Yellow 185',CAT)],
'Orange':[('PO5','Monoazo orange (PO5)',PG),('PO36','Benzimidazolone orange',PG),('PO13','Pigment Orange 13',CAT),('PO34','Pigment Orange 34',CAT)],
'Red':[('PR112','Naphthol red (PR112)',PG),('PR22','Monoazo red (PR22)',PG)]}
order=['Purple','Blue','Green','Yellow','Orange','Red','Brown','Black and grey','White','Fluorescent']
ents=[]
def seen(cat):
    return None
for fam in order:
    for n,c in inorg.get(fam,[]):
        nn=(f"{c} {n[0].lower()+n[1:]}" if c else n)
        ents.append({'n':nn,'a':c,'d':f"Inorganic pigment in the {fam.lower()} family"+(f", Colour Index {c}." if c else ", with no Colour Index name on the reference."),'s':IN,'v':[],'g':fam+' (inorganic)'})
    for c,n,src in org.get(fam,[]):
        ents.append({'n':f"{c} {n[0].lower()+n[1:]}" if not n.startswith('Pigment ') else n.replace('Pigment ','').replace('Yellow ','PY').replace('Orange ','PO') ,'a':c,'d':f"Organic pigment in the {fam.lower()} family, Colour Index {c}.",'s':src,'v':[],'g':fam+' (organic)'})
# fix names of category-only ones
for e in ents:
    if re.fullmatch(r'P[YO]\d+',e['n']): e['n']=f"{e['n']} (named only as a Colour Index number)"
for dp in d['depts']:
  for s in dp['s']:
    for k in s['k']:
      if k['n']=='Dry pigment':
        old=k['x']
        for e in old: e['g']="Makers' pigment ranges"; brandify(e); e['g']="Makers' pigment ranges"
        k['n']="Artists' pigment"; ren['Dry pigment']="Artists' pigment"
        k['a']=k.get('a','')
        k['d']="Colour as a pigment identified by its Colour Index name, sold as dry powder or used as the colour in paint."
        k['x']=ents+old
        k['nl']="One entry is a pigment identified by its Colour Index generic name (a letter code and number, such as PB29 for ultramarine), or a maker's range of loose pigments."
        k['sel']=("Every row of Wikipedia's List of inorganic pigments, by colour family (the page is flagged as possibly machine-written, and repeats realgar, caput mortuum and Scheele's green, which are listed once here). "
          "Wikipedia has no list of organic pigments, so organic entries are those whose Colour Index names the fetched Pigment, Copper phthalocyanine, Quinacridone and Category:Organic pigments pages give; this part is not complete. No artists' colour maker's names for a pigment were fetched.")
        k['xg']="by colour family, then makers' ranges"
# --- yarn weight kind ---
YW=W+'Yarn'
yw=[('0','Lace','fingering, crochet 10-count thread'),('1','Super fine','sock, fingering, baby'),('2','Fine','sport, baby'),('3','Light','DK, light worsted'),('4','Medium','worsted, Afghan, Aran'),('5','Bulky','chunky, craft, rug'),('6','Super bulky','bulky, roving'),('7','Jumbo','jumbo, roving')]
for dp in d['depts']:
  for s in dp['s']:
    if s['n']=='Yarn':
      s['k'].insert(0,{'n':'Yarn weight class','a':'standard yarn weight · yarn thickness','d':'The thickness class of a yarn, from lace to jumbo, whatever its fibre.',
        'x':[{'n':f"Weight {n}: {nm}",'a':ty,'d':f"Craft Yarn Council standard weight {n}; also sold as {ty}.",'s':YW,'v':[],'g':'Craft Yarn Council standard weights'} for n,nm,ty in yw],
        'tt':[['Fibre',['Wool','Cotton and plant fibre','Acrylic','Silk','Alpaca, mohair and cashmere','Blend']]],
        'nl':'One entry is one of the eight Craft Yarn Council standard yarn weights, numbered 0 to 7; the fibre is an attribute, not a separate entry.',
        'sel':"All eight weights in the table of Wikipedia's Yarn article, which gives the Craft Yarn Council classes (the article notes the type names are not regulated). Fibre-based kinds below keep the makers' lines.",
        'xg':'Craft Yarn Council standard weights'})
# --- Canson families ---
CS=W+'Canson'
for dp in d['depts']:
  for s in dp['s']:
    for k in s['k']:
      if k['n']=='Drawing and mixed-media paper':
        for n,dd in [('Canson Ingres Vidalon','Coloured laid paper from Canson.'),('Canson "C" à Grain','Canson drawing paper.'),('Canson 1557','Canson drawing paper.'),('Canson Figueras','Canson paper for oil and acrylic.')]:
          e={'n':n,'d':dd,'mk':'Canson','s':CS,'v':[]}; brandify(e); k['x'].append(e)
        finish_kind(k,k['nl'],k['sel'])
      if k['n']=='Watercolour paper':
        for e in k['x']:
          if e['n']=='Canson Montval': e['d']=e.get('d') or 'Canson watercolour paper.'
        k['nl']="One entry is a named watercolour paper family from a paper maker (Arches, Fabriano, Canson); weights and surfaces are versions."
# --- finish: dup check, write ---
for dp in d['depts']:
  for s in dp['s']:
    for k in s['k']:
      seen_n=set()
      for e in k.get('x',[]):
        if e['n'] in seen_n: e['n']+=' ('+e.get('mk','')+')'
        seen_n.add(e['n'])
        e.setdefault('v',[])
json.dump(d,open(R+'out/C4.json.tmp','w'),ensure_ascii=False,indent=1); os.replace(R+'out/C4.json.tmp',R+'out/C4.json')
json.dump(bj,open(R+'out/C4_brands.json.tmp','w'),ensure_ascii=False,indent=1); os.replace(R+'out/C4_brands.json.tmp',R+'out/C4_brands.json')
json.dump(ren,open(R+'out/C4_renames.json.tmp','w'),ensure_ascii=False,indent=1); os.replace(R+'out/C4_renames.json.tmp',R+'out/C4_renames.json')
json.dump(log,open(OUT+'log.json','w'),ensure_ascii=False,indent=1)
print({k:(v if isinstance(v,int) else len(v)) for k,v in log.items()})
