import json,re,sys
sys.path.insert(0,'.')
exec(open('b4.py').read().split("groups=collections")[0])  # reuse tables
G=json.load(open('b4_groups.json'))
d=json.load(open('../../out/B4.json'))
def find(n):
    if isinstance(n,dict):
        if n.get('n')=='Design-collection vase': return n
        for k in('depts','s','k'):
            for x in n.get(k,[]) if isinstance(n.get(k),list) else []:
                r=find(x)
                if r: return r
kind=find(d)
existing=kind['x']
skipdes={'Hella Jongerius','Tomáš Gabzdil Libertíny','Ronan Bouroullec, Erwan Bouroullec','Konstantin Grcic','Vincent de Rijk Kom BV','Toots Zynsky','Shiro Kuramata','Jiří Pelcl','Makoto Komatsu','Ursula Morley Price','Sydney Cash','Thomas Patti','Mary Rogers','Paul Chaleff','Sergio Asti','Ettore Sottsass','Enzo Mari','Lino Sabattini'}
new=[]; skipped=[]; merged={}
for (des_,title,y),v in G:
    if des_ in skipdes: skipped.append((des_,title,y)); continue
    if des_=='Otto Natzler': skipped.append((des_,title,y)); continue
    if des_=='Philippe Starck' and 'Contre' in title: skipped.append((des_,title,y)); continue
    if des_=='Tapio Wirkkala' and 'Ovalis' in title: skipped.append((des_,title,y)); continue
    if des_=='Hans Coper' and y=='c. 1963': skipped.append((des_,title,y)); continue
    sh=short.get(des_,des_.split(',')[0] if des_ not in('Elsa Fischer-Treyden, Margret Hildebrand',) else short[des_])
    sh=short.get(des_) or re.sub(r'^.* (?=\S+$)','',des_) 
    plain=title in('Vase','Vases')
    DIST=('Biennale','Bottiglia','Orchid','Jäkälä','Fahrenheitor','Le Parthènon','Cypriote','Petite','Ball')
    if des_=='Alvar Aalto' or des_.startswith('Alvar Aalto') or (title=='Fazzoletto Vase'): skipped.append((des_,title,y)); continue
    if plain: nm=f"Vase{'s' if title=='Vases' else ''} ({sh}, {y})"
    elif any(w in title for w in DIST): nm=title if title.lower().endswith('vase') else title+' vase'
    else: nm=f"{title} ({sh}, {y})"
    if des_=='Unidentified Designer': nm=f"Vase (unidentified designer, {y})"
    if des_=='Vallauris': nm=f"Vallauris vase ({y})"
    n=v['n']
    if nm in merged: merged[nm]['_n']+=n; continue
    dd=f"Vase{'s' if title=='Vases' else ''} by {sh if des_!='Unidentified Designer' else 'an unidentified designer'}, in MoMA's Design classification"+(f" ({n} records of the same design)." if n>1 else ".")
    e={"n":nm,"a":"","d":dd,"mk":("" if des_ in("Unidentified Designer",) else des_ if len(des_)<60 else sh),"y":y,"s":urlbase+(f"&page={v['pg']}" if v['pg']>1 else ""),"v":[],"dt":"","g":ctry.get(des_,"Country not stated")}
    e['_n']=n; merged[nm]=e; new.append(e)
for e in new:
    n=e.pop('_n')
    if n>1 and 'records' not in e['d']: e['d']=e['d'].rstrip('.')+f" ({n} records of the same design)."
    elif n>1: e['d']=re.sub(r'\(\d+ records','('+str(n)+' records',e['d'])
# dedupe names
seen={x['n'] for x in existing}; out=[]
for e in new:
    b=e['n']; k=2
    while e['n'] in seen: e['n']=f"{b} ({k})"; k+=1
    seen.add(e['n']); out.append(e)
def yr(e):
    m=re.search(r'\d{4}',e['y']); return int(m.group()) if m else 0
allx=existing+out
for e in allx: e.setdefault('g','Country not stated')
allx.sort(key=lambda e:(e['g']=="Country not stated",e['g'],yr(e),e['n']))
kind['x']=allx
kind['sel']=("Follows MoMA's Design classification search for 'vase' (178 works online), all five result pages read (pages 1 to 5 through Parallel, 2026-10-31), plus the ADI Design Museum's Compasso d'Oro record for the Marco vase. Complete: all 178 MoMA results are covered; "
 "records of one design are one entry, and two non-vase results (a Tschichold poster and Boontje and Woffenden's Transglass glassware) are left out. Designers whose country the search page does not state and that no fetched page here fixes carry 'Country not stated'.")
json.dump(d,open('B4.new','w'),ensure_ascii=False,indent=1)
print(len(existing),len(out),len(skipped))
for e in out[:200]: print(e['n'],'|',e['g'],'|',e['y'])
