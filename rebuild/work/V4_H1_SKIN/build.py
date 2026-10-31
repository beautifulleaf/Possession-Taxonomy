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
