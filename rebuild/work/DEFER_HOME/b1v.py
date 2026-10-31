import json,re
d=json.load(open('../../out/B1.json'))
def find(n,name):
    if isinstance(n,dict):
        if n.get('n')==name and n.get('x'): return n
        for k in('depts','s','k'):
            for x in n.get(k,[]) if isinstance(n.get(k),list) else []:
                r=find(x,name)
                if r: return r
dc=find(d,'Dining chair')
have={e['n'].lower() for e in dc['x']}
skipnames={'la fonda side chair','upholstered stacking chair 0716-1','plexiglas chair vb 101 w','a son of panton chair','between two stools, the thick air'}
DES=["Eero Saarinen; Charles Eames","Charles Eames & Eero Saarinen","Eero Saarinen","Charles & Ray Eames","George Nelson & Associates; George Nelson","George Nelson & Associates","George Nelson","Gaetano Pesce","Vico Magistretti","Hans J. Wegner","Finn Juhl","Ettore Sottsass","Ron Arad","Jasper Morrison","Eero Aarnio","Hans Theodor Baumann","Giandomenico Belotti","Trix & Robert Haussmann","Gerrit T. Rietveld"]
seen=set(); new=[]
base='https://collection.design-museum.de/en/collection/?q=chair+'
for line in open('vitra_raw.txt'):
    q,t=line.rstrip('\n').split('|',1)
    des=None
    for dd in sorted(DES,key=len,reverse=True):
        if t.endswith(' '+dd): des=dd; t=t[:-len(dd)-1]; break
    if not des: print('NODES',t); continue
    m=re.search(r',? ?((?:c\. )?\d{4}(?:[/–]\d{2,4})?)$',t)
    y=m.group(1) if m else ''
    if m: t=t[:m.start()]
    t=t.strip().rstrip(',')
    parts=[p.strip() for p in t.split(' / ')]
    if len(parts)>1:
        code,rest=parts[0],parts[1]
        first=rest.split(', ')[0]
        nm=f"{first} ({code})" if re.search(r'\d',code) or code.isupper() else first
        if first.lower().startswith(('plastic','plywood','wire','swaged','tilting')) or len(first)<4: nm=f"{first} ({code})"
        if code.startswith('No. ') and first: nm=f"{first} ({code})"
    else: nm=parts[0]
    if nm.lower() in skipnames or nm.lower() in have: continue
    key=(nm.lower(),y)
    if key in seen: continue
    seen.add(key)
    dn=des.replace('Charles & Ray Eames','Charles and Ray Eames').replace('George Nelson & Associates; George Nelson','George Nelson & Associates')
    yr=re.search(r'\d{4}',y); dec=(yr.group()[:3]+'0s') if yr else 'Date not stated'
    if dec=='1990s' and False: pass
    new.append({"n":nm,"a":"","d":f"Held by the Vitra Design Museum; by {dn}.","mk":"","y":y,"s":base+q,"v":[],"dt":"","g":dec})
print(len(new))
for e in new: print(e['n'],'|',e['y'],'|',e['g'],'|',e['d'][-30:])
json.dump(new,open('vitra_new.json','w'),ensure_ascii=False)
