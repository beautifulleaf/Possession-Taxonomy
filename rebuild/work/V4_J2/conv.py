import json,re,os,collections
R='/home/user/Possession-Taxonomy/rebuild/'
d=json.load(open(R+'work/V4_J2/bak/J2.json'))
brands=json.load(open(R+'work/V4_J2/bak/J2_brands.json'))
reg={b['n']:b for b in brands['b']}
W='https://en.wikipedia.org/wiki/'
OWN={ # brand:(own,tier,cty,own_y,source)
 'Chicken of the Sea':('Thai Union Group','Global group','United States',2000,W+'Chicken_of_the_Sea'),
 'John West':('Thai Union Group','Global group','United Kingdom',2010,W+'John_West_Foods'),
 'King Oscar':('Thai Union Group','Global group','Norway',2014,W+'Thai_Union_Group'),
 'Rio Mare':('Bolton Group','Global group','Italy',None,W+'Bolton_Group'),
 'StarKist':('Dongwon Industries','Global group','United States',2008,W+'StarKist'),
 'Dongwon':('Dongwon Industries','Global group','South Korea',None,W+'StarKist'),
 'Century Pacific Food, Inc.':('Century Pacific Food, Inc.','Independent','Philippines',None,W+'Century_Pacific_Food'),
 'Ortiz':('Ortiz family','Independent','Spain',None,'https://www.conservasortiz.com/en/?p=5892'),
 'Gomes da Costa':('Grupo Calvo','Independent','',None,W+'Grupo_Calvo'),
 'Aldi':('Aldi Süd','Own label','',None,None),
 'Aldi Süd':('Aldi Süd','Own label','',None,None),
}
DROP={'Traditional fishing of the Strait of Messina','Mullet bottarga and traditional fishing from the Cabras pond','Scandinavian gravad lax','British Isles brown crab','Pacific coast Dungeness crab','Florida stone crab claws','West Coast Kumamoto','New South Wales estuary rock oyster','Creel-caught langoustine','Hybrid sturgeon','Banco Chinchorro and Sian Ka’an Spiny Lobster','Roman Coastline Tellina'}
def drop(n): return n in DROP or n.startswith('Beluga hybrid')
def norm(s): return re.sub(r'\b(pgi|pdo|tsg|gi)\b|\(.*?\)|[^a-z0-9]','',s.lower().replace('ö','o').replace('ø','o').replace('å','a'))
def scheme(n):
    if re.search(r'\bPDO\b',n): return 'EU protected designation of origin'
    if re.search(r'\bPGI\b',n): return 'EU protected geographical indication'
    if re.search(r'\bTSG\b',n): return 'EU traditional speciality guaranteed'
    if re.search(r'[가-힯]',n): return 'Korean geographical indication'
    if re.search(r'[぀-ヿ一-鿿]',n): return 'Japanese geographical indication' if re.search(r'[぀-ヿ]',n) else 'geographical indication'
    if re.search(r'\bGI\b',n): return 'geographical indication'
    return None
PROT='Protected and regional names'
stats=collections.OrderedDict()
for dp in d['depts']:
  for s in dp['s']:
    for k in s['k']:
        ms=k.pop('m',[]) or []
        xs=k.get('x') or []
        before=(len(xs),len(ms))
        have={norm(x['n']) for x in xs}
        for x in xs:
            if not x.get('g'):
                x['g']='Species and grades' if k['n'] in('Sturgeon caviar','American roe') else PROT
        bybrand=collections.OrderedDict(); nprot=0; ndrop=0; nbr=0
        for name,br in ms:
            if drop(name): ndrop+=1; continue
            if not br:
                if norm(name) in have: continue
                sc=scheme(name)
                dsc=(f'{sc[0].upper()+sc[1:]} for this product.' if sc else 'Regional name for this product as listed on the kind page.')
                xs.append({'n':name,'a':'','d':dsc,'mk':'','y':'','s':k['s'],'g':PROT,'v':[]}); have.add(norm(name)); nprot+=1
            else:
                bybrand.setdefault(br,[]).append(name)
        for br,prods in bybrand.items():
            o=OWN.get(br); r=reg.get(br,{})
            ex=[x for x in xs if norm(x['n'])==norm(br)]
            vers=[]
            for p in prods:
                if norm(p)==norm(br): continue
                pn=p[len(br):].strip() if p.lower().startswith(br.lower()) and len(p)>len(br)+1 else p
                vers.append({'n':pn,'mk':br,'y':'','d':'Product listed under this brand on the kind page.'})
            cty=(o[2] if o else '') or r.get('c','')
            e={'n':br,'a':'','d':(f"{r['d']}" if r.get('d') else f'Maker or brand of this kind named on the kind page.'),'mk':br,'y':r.get('f','') or '','s':(o[4] if o and o[4] else k['s']),'v':vers}
            e['own']=o[0] if o else 'owner not stated'
            if o: e['tier']=o[1]
            if cty: e['cty']=cty
            if o and o[3]: e['own_y']=o[3]
            e['g']=(('Global group: '+o[0]) if o and o[1]=='Global group' else (o[1] if o else 'Brands with no published owner'))
            if ex: # merge versions into existing entry
                ex[0]['v']=(ex[0].get('v') or [])+vers; continue
            xs.append(e); nbr+=1
        # sort: sections order then year then name
        order=lambda g:(0 if g.startswith('Global') else 1 if g in('National champion',) else 2 if g=='Independent' else 3 if g=='Own label' else 4 if g.startswith('Brands') else 5)
        if xs:
            k['x']=xs
            has_b=nbr>0 or any(x.get('own') for x in xs)
            has_p=any(x['g']==PROT for x in xs)
            if has_b and has_p:
                k['nl']='One entry is a brand, maker or protected regional name for this kind; a maker\'s product lines are versions.'
                k['xg']='by market tier, then owner group; protected names last'
            elif has_b:
                k['nl']='One entry is a brand or maker of this kind sold under its own name; its product lines and packs are versions.'
                k['xg']='by market tier, then owner group'
            elif k['n'] in('Sturgeon caviar','American roe'):
                k['nl']='One entry is a caviar named by the sturgeon or paddlefish species; a house\'s product lines are versions.'
                k['xg']='by species'
            else:
                k['nl']='One entry is a named regional product, protected name or variety of this kind; a maker\'s version of it is a version.'
                k['xg']='by registration or origin'
            xs.sort(key=lambda x:(order(x['g']),x['g'],x.get('y') or '9999',x['n'].lower()))
            tot=len(xs)
            k['sel']=('No whole-space reference exists for this kind; the list follows the pages cited on its entries and the earlier harvest. '
              +('Owners, tiers and acquisition years come from fetched Wikipedia pages on Thai Union Group, Bolton Group, StarKist, Chicken of the Sea, John West, Century Pacific Food and Ortiz; brands with no fetched owner say so. ' if has_b else '')
              +('Protected names follow the harvest from EU, MAFF and Korean registers; the EU eAmbrosia register could not be read as a list this pass. ' if has_p else '')
              +f'Covers {tot} named entries; the register total could not be counted, so the list is not claimed complete.')
        stats[k['n']]=(before,(len(xs),0),nprot,nbr,ndrop)
json.dump(stats,open(R+'work/V4_J2/stats.json','w'),indent=0)
json.dump(d,open(R+'work/V4_J2/J2.new.json','w'),ensure_ascii=False,indent=1)
print(sum(v[0][1] for v in stats.values()),'models in;',sum(v[2] for v in stats.values()),'protected;',sum(v[3] for v in stats.values()),'brands;',sum(v[4] for v in stats.values()),'dropped')
