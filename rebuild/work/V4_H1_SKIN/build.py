import json,re,unicodedata,glob,sys,copy,collections
sys.path.insert(0,'/home/user/Possession-Taxonomy/rebuild/work/V4_H1_SKIN')
import data_groups as DG, data_others as DO
R='/home/user/Possession-Taxonomy/rebuild/'
def norm(s):
    s=unicodedata.normalize('NFKD',s or '');s=''.join(c for c in s if not unicodedata.combining(c))
    return re.sub(r'[^a-z0-9]','',s.lower())
SRC=DG.SRC
# register lookup
REG={}
for f in glob.glob(R+'out/*_brands.json'):
    try: bl=json.load(open(f))['b']
    except Exception: continue
    for b in bl: REG.setdefault(norm(b['n']),b)
old=json.load(open(R+'out/H1.json'))
OLD={d['n']:d for d in old['depts']}
WORD={'S':'skin care','M':'make-up'}
DEPTN={'S':'Skincare','M':'Make-up'}
REGION={}
for c in ['Japan','South Korea','China','Taiwan','Hong Kong']: REGION[c]='East Asia'
for c in ['India','Indonesia','Malaysia','Philippines','Thailand','Singapore','Vietnam']: REGION[c]='South & Southeast Asia'
for c in ['United Arab Emirates','Israel','Turkey','Iran','Saudi Arabia','Oman']: REGION[c]='Middle East'
for c in ['Uganda','South Africa','Nigeria','Kenya','Egypt']: REGION[c]='Africa'
for c in ['Brazil','Mexico','Argentina','Colombia','Chile']: REGION[c]='Latin America'
for c in ['United States','Canada']: REGION[c]='North America'
for c in ['Australia','New Zealand']: REGION[c]='Oceania'
for c in ['France','Germany','United Kingdom','Italy','Poland','Spain','Switzerland','Sweden','Russia','Norway','Netherlands','Ireland','Greece','Hungary','Belgium','Denmark','Finland','Austria','Portugal','Latvia','Luxembourg','Ukraine','Czech Republic','Czechia','Romania','Bulgaria','Lithuania','Estonia','Slovenia','Croatia','Serbia','Azerbaijan']: REGION[c]='Europe'
def region(c): return REGION.get(c,'Region not stated')
TIERN={'NC':'National champion','IN':'Independent','CI':'Craft & indie','OL':'Own label','':''}
ENT={}   # key -> dict
ALIAS={}
def key_for(name):
    return ALIAS.get(norm(name))
def reg_c(name):
    r=REG.get(norm(name)); return (r or {}).get('c','') or ''
def reg_f(name):
    r=REG.get(norm(name)); return (r or {}).get('f','') or ''
def add_entry(name,aliases,dept,own,tier,cty,own_y,g,y,s,note,gk=None):
    k=norm(name)
    if k in ENT:
        e=ENT[k]
        if dept not in e['depts']: e['depts'][dept]={'v':[]}
        # fill blanks only
        for f,v in (('own',own),('tier',tier),('cty',cty),('own_y',own_y),('g',g),('y',y),('s',s),('note',note)):
            if v and not e.get(f): e[f]=v
        return e
    e={'n':name,'a':[a.strip() for a in aliases.split('·') if a.strip()] if aliases else [],'depts':{dept:{'v':[]}},'own':own,'tier':tier,'cty':cty,'own_y':own_y,'g':g,'y':y,'s':s,'note':note}
    ENT[k]=e; ALIAS[k]=k
    for a in e['a']: ALIAS.setdefault(norm(a),k)
    return e
ALIAS_EXTRA={'ysl beauty':'Yves Saint Laurent Beauté','mac cosmetics':'MAC Cosmetics','laneige':'Laneige','hera':'HERA','etudehouse':'Etude','maybelline':'Maybelline New York'}
# groups
for gname,(src,ownname,lst) in DG.GROUPS.items():
    for l in lst:
        n,al,dp,oy,g,y,note=l.split('|')
        al=al.replace('|','')
        depts=['S','M'] if dp=='B' else [dp]
        for d in depts:
            add_entry(n,al.replace(' · ','·'),d,ownname,'Global group',reg_c(n),oy,g,y or reg_f(n),SRC[src],note)
# others
for l in DO.OTHERS.strip().split('\n'):
    n,al,dp,own,tier,cty,y,src,note=l.split('|')
    tier=TIERN[tier.replace("''",'')]; own=own.replace("''",'')
    depts=['S','M'] if dp=='B' else [dp]
    for d in depts:
        add_entry(n,al,d,own,tier,cty,'',('' if tier!='Craft & indie' else ''),y or reg_f(n),SRC[src],note)
# fold old
unplaced=[];newfrom=0
def find(name):
    k=ALIAS.get(norm(name))
    if k is None:
        k2=norm({'YSL Beauty':'Yves Saint Laurent Beauté','Etude House':'Etude'}.get(name,name))
        k=ALIAS.get(k2)
    return k
IOPEMAP={'IOPE':'IOPE','HERA':'HERA','Sulwhasoo':'Sulwhasoo','LANEIGE':'Laneige'}
stats=collections.Counter()
def fold(dp,kind,brand,ver,srcurl):
    global newfrom
    if not brand: unplaced.append((dp,kind['n'],ver['n'])); stats['nobrand']+=1; return
    k=find(brand)
    if k is None:
        c=reg_c(brand); 
        e=add_entry(brand,'',dp,'','',c,'','',reg_f(brand),srcurl,'');k=norm(brand);newfrom+=1;stats['newbrand']+=1
    e=ENT[k]
    if dp not in e['depts']:
        e['depts'][dp]={'v':[]}   # brand now also listed in this dept
        stats['cross']+=1
    e['depts'][dp]['v'].append(ver)
for dn,dp in (('Skincare','S'),('Make-up','M')):
    for sh in OLD[dn]['s']:
        for kd in sh['k']:
            for x in kd.get('x',[]):
                vs=[{'n':x['n'],'y':x.get('y',''),'d':x['d'][:200]}]
                brand=x.get('mk','')
                if brand=='Amorepacific':
                    for v in x.get('v',[]):
                        b=next((b for t,b in IOPEMAP.items() if t.lower() in v['n'].lower()),'IOPE')
                        fold(dp,kd,b,{'n':v['n'],'y':v.get('y',''),'d':(v.get('d') or '')+(' ('+x['n']+')' if x['n'] not in v['n'] else '')},x['s'])
                    continue
                for v in x.get('v',[]):
                    if v.get('n') and v['n']!=x['n']:
                        vs.append({'n':(v['n'] if x['n'].lower() in v['n'].lower() else x['n']+': '+v['n']),'y':v.get('y',''),'d':(v.get('d') or '')[:160]})
                if len(vs)>1 and vs[1]['n']==x['n']: vs.pop(1)
                for v in vs: fold(dp,kd,brand,v,x['s'])
            for m in kd.get('m',[]):
                fold(dp,kd,m[1],{'n':m[0],'y':'','d':''},kd.get('s','') or sh.get('s',''))
for dp_,kn,vn in unplaced:
    pass
EXTRA={'Latisse':('Latisse','M'),'Kurlash':('Kurlash','M'),'Patti Nails':('Patti Nails','M')}
for vn,(bn,dp_) in EXTRA.items():
    kdsrc=[k for sh in OLD['Make-up']['s'] for k in sh['k'] if any(m[0]==vn for m in k.get('m',[]))][0]
    add_entry(bn,'',dp_,'','',reg_c(bn),'','',reg_f(bn),kdsrc.get('s',''),'')
    ENT[norm(bn)]['depts'][dp_]['v'].append({'n':vn,'y':'','d':''})
print('stats',dict(stats),'unplaced',unplaced[:20])
# sanity: drop empty-version placeholders for own source
# cty fill from register for all
for e in ENT.values():
    if not e['cty']: e['cty']=reg_c(e['n'])
    if not e['a'] and False: pass
json.dump({'ENT':ENT},open('/home/user/Possession-Taxonomy/rebuild/work/V4_H1_SKIN/ent.json','w'),ensure_ascii=False)
tc=collections.Counter()
for e in ENT.values():
    for d in e['depts']: tc[(d,e['tier'] or '-')]+=1
print(tc, len(ENT))

# ---------------- assemble ----------------
OWNER_ORDER=["L'Oréal","The Estée Lauder Companies","Unilever","Procter & Gamble","Beiersdorf","Shiseido","LVMH","Puig","Coty","Chanel","Amorepacific","LG H&H","Kao","Kosé","e.l.f. Beauty"]
GROUP_TOTAL={"L'Oréal":('LO',62),"The Estée Lauder Companies":('EL',35),"Unilever":('UN',94),"Procter & Gamble":('PG',37),"Beiersdorf":('BE',13),"Shiseido":('SH',35),"LVMH":('LV',16),"Puig":('PU',28),"Coty":('CO',40),"Chanel":('CH',1),"Amorepacific":('AM',31),"LG H&H":('LG',10),"Kao":('KA',15),"Kosé":('KO',7),"e.l.f. Beauty":('EF',6)}
GROUP_PAGE={"L'Oréal":"Wikipedia, L'Oréal (brand sections by division)","The Estée Lauder Companies":"Wikipedia, Estée Lauder Companies (brands section)","Unilever":"Wikipedia, List of Unilever brands (beauty, well-being and personal care section)","Procter & Gamble":"Wikipedia, List of Procter & Gamble brands","Beiersdorf":"Wikipedia, Beiersdorf","Shiseido":"Wikipedia, Shiseido (subsidiary sections)","LVMH":"Wikipedia, LVMH (Perfumes and Cosmetics division)","Puig":"Wikipedia, Puig (company)","Coty":"Wikipedia, Coty, Inc.","Chanel":"Wikipedia, Chanel","Amorepacific":"Wikipedia, Amorepacific Corporation (brand list)","LG H&H":"Wikipedia, LG H&H","Kao":"Wikipedia, Kao Corporation","Kosé":"Wikipedia, Kosé","e.l.f. Beauty":"e.l.f. Beauty press release of 28 May 2025"}
DIV_OK={'Dermatological Beauty',"L'Oréal Luxe",'Consumer Products','Prestige','Premium'}
REG_ORDER=['East Asia','South & Southeast Asia','Europe','North America','Latin America','Middle East','Africa','Oceania','Region not stated']
def cap(s): return s[0].upper()+s[1:] if s else s
def entry_out(e,dp):
    W_=WORD[dp]
    vs=e['depts'][dp]['v']
    # dedupe versions
    seen=set();vv=[]
    for v in vs:
        k=(v['n'].lower())
        if k in seen: continue
        seen.add(k);vv.append({kk:val for kk,val in (('n',v['n']),('mk',e['n']),('y',v.get('y','')),('d',v.get('d',''))) if val or kk in('n','mk')})
    tier=e['tier'];own=e['own']
    g=e['g'] if e['g'] in DIV_OK else ''
    if tier=='Global group':
        where=(f"in {own}'s {g} division" if g else f"in the {own} portfolio")
        d=f"{cap(W_)} brand {where}"+(f"; {e['note']}" if e['note'] else '')+'.'
    elif e['note'] and e['depts']  and e['s'] in set(DG.SRC.values()) :
        d=cap(e['note']).rstrip('.')+'.'
    else:
        names=', '.join(v['n'] for v in vv[:3])
        d=f"{cap(W_)} brand"+(f"; lines listed here include {names}." if names else ' named on the cited page.')
    if tier!='Global group' and e['note'] and not d.startswith(cap(e['note'])[:10]):
        pass
    out={'n':e['n'],'a':' · '.join(e['a']),'d':d,'y':str(e['y'] or ''),'s':e['s'],'v':vv}
    if e['own']: out['own']=e['own']
    if tier: out['tier']=tier
    if e['cty']: out['cty']=e['cty']
    if e['own_y']: out['own_y']=str(e['own_y'])
    return out
ROLES={'proya':('landmark'),'iope':'origin'}
def build_dept(dp):
    W_=WORD[dp]
    ents=[e for e in ENT.values() if dp in e['depts']]
    shelves=[]
    def sortk(o): return (o.get('g',''),o.get('y') or '9999',o['n'].lower())
    # global groups
    kinds=[]
    for ow in OWNER_ORDER:
        es=[e for e in ents if e['tier']=='Global group' and e['own']==ow]
        if not es: continue
        xs=[]
        for e in es:
            o=entry_out(e,dp); g=e['g'] if e['g'] in DIV_OK else ''
            if g: o['g']=g
            xs.append(o)
        xs.sort(key=lambda o:(o.get('g',''),o['n'].lower()))
        src,tot=GROUP_TOTAL[ow]
        hasg=any(o.get('g') for o in xs)
        k={'n':f"{ow} {W_} brands",'a':'','d':f"{cap(W_)} brands owned by {ow}, grouped as the group's own page groups them.",
           's':DG.SRC[src],'nl':f"One entry is a {W_} brand sold under its own name and owned by {ow}; its product lines are versions.",
           'sel':f"Follows {GROUP_PAGE[ow]}, fetched 2026-10-31. Every brand there that sells {W_} is included once in this department; a brand with both skin care and make-up lines is listed in both departments, and hair, fragrance and fashion lines are out of scope. Covers {len(set(e['n'] for e in ENT.values() if e['tier']=='Global group' and e['own']==ow))} of about {tot} brands named on the page; the rest are hair care, fragrance, fashion or health lines, or brands the page names without enough to place them.",
           'x':xs,'tt':[['Sold through',['Department stores and perfumeries','Pharmacies and dermatology clinics','Mass retail and drugstores','Online and direct sales']]]}
        if hasg: k['xg']="sections follow the divisions named on the group's page"
        kinds.append(k)
    shelves.append({'n':'Global groups','t':f"{cap(W_)} brands owned by the multinational groups that dominate beauty worldwide.",'ax':'kinds by owner group: the largest groups in the first half of 2026 first, then the rest','k':kinds})
    for tname,tkey,tdesc,lab in (('National champions','National champion',"Brands that lead or are iconic in their home market, named by a fetched ranking or overview.",'National'),('Independents','Independent',"Established brands owned by a named company that is not one of the global groups.",'Independent'),('Craft & indie','Craft & indie',"Small and new-wave brands named by a fetched indie overview.",'Craft and indie'),('Own label','Own label',"Brands sold under a retailer's own name.",'Own-label')):
        es=[e for e in ents if e['tier']==tkey]
        if not es: continue
        kinds=[]
        regions=REG_ORDER if tkey in('National champion','Independent') else [None]
        for rg in regions:
            ee=[e for e in es if (rg is None or region(e['cty'])==rg)]
            if not ee: continue
            xs=[]
            for e in ee:
                o=entry_out(e,dp)
                o['g']=e['cty'] or 'Country not stated'
                if norm(e['n'])=='proya' and dp=='S': o['role']='landmark'
                xs.append(o)
            xs.sort(key=lambda o:(o['g'],o.get('y') or '9999',o['n'].lower()))
            nm=(f"{lab} {W_} brands: {rg}" if rg else f"{lab} {W_} brands")
            refs=sorted({e['s'] for e in ee})
            k={'n':nm,'a':'','d':f"{cap(W_)} brands in this tier"+(f" from {rg}." if rg else '.'),'s':refs[0],
               'nl':f"One entry is a {W_} brand sold under its own name"+(" that leads or is iconic in its home market" if tkey=='National champion' else (" owned by a company outside the global groups" if tkey=='Independent' else ""))+"; its product lines are versions.",
               'sel':{'National champion':"Brands that a fetched ranking or overview names as leading in their home market: the China Briefing 2025 ASKCI rankings, Yicai (2023), Kotak Neo's India shares, Brazil's Euromonitor 2025 ranking, the Japan overviews of the US Commerce Department and Japanese Taste.",'Independent':"Companies and brands named in Wikipedia's category pages 'Cosmetics companies of' France, Germany, Japan, India, the United Kingdom, the United States and other countries, fetched 2026-10-31, where the company is not one of the global groups.",'Craft & indie':"The brands the Kline and NIQ 'Brands to Watch' report (as reported by Beauty Independent, December 2023) names, in scope for this department; the report names 15 of its 25 indie brands.",'Own label':"Sephora's own-label range; no complete list of retailer own-label beauty ranges was found."}[tkey]+f" Covers {len(ee)} brands here; no whole-market list exists, so this is not complete.",
               'x':xs,'tt':[['Price tier',['Mass','Premium','Prestige']]]}
            if rg: k['xg']='sections by home country'
            kinds.append(k)
        shelves.append({'n':tname,'t':tdesc,'ax':'kinds by world region of the brand' if len(kinds)>3 else None,'k':kinds})
    # no stated owner
    es=[e for e in ents if not e['tier']]
    kinds=[]
    for rg in REG_ORDER:
        ee=[e for e in es if region(e['cty'])==rg]
        if not ee: continue
        xs=[]
        for e in ee:
            o=entry_out(e,dp); o['g']=e['cty'] or 'Country not stated'; xs.append(o)
        xs.sort(key=lambda o:(o['g'],o['n'].lower()))
        refs=collections.Counter(e['s'] for e in ee)
        kinds.append({'n':f"{cap(W_)} brands with no stated owner: {rg}",'a':'','d':f"{cap(W_)} brands whose owner no fetched page states, from {rg}." if rg!='Region not stated' else f"{cap(W_)} brands whose home country and owner no fetched page states.",
          's':refs.most_common(1)[0][0],'nl':f"One entry is a {W_} brand sold under its own name; its product lines are versions.",
          'sel':"Brands named on the retail, reference or category pages cited on each entry, or in the structure pass of this department, where no fetched page names an owner. Owner and tier are left blank rather than guessed; this is a working list, not a complete canon.",
          'x':xs,'xg':'sections by home country','tt':[['Price tier',['Mass','Premium','Prestige']]]})
    shelves.append({'n':'Owner not stated','t':'Brands whose owning company is not stated on a fetched page.','ax':'kinds by world region of the brand','k':kinds})
    for sh in shelves:
        if sh.get('ax') is None: sh.pop('ax',None)
    return shelves
def product_shelves(dn):
    out=[]
    for sh in OLD[dn]['s']:
        s2={kk:v for kk,v in sh.items() if kk!='k'}
        ks=[]
        for k in sh['k']:
            k2={kk:v for kk,v in k.items() if kk not in('x','m','r')}
            ks.append(k2)
        s2['k']=ks;out.append(s2)
    return out
