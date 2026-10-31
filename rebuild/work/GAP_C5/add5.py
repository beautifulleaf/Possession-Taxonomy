import json,os
P='/home/user/Possession-Taxonomy/rebuild/out/C5.json'
d=json.load(open(P))
K={};E={}
for dp in d['depts']:
  for s in dp['s']:
    for k in s['k']:
      K[k['n']]=k
      for e in k.get('x',[]): E[e['n']]=e
t=E['TI-84 Plus']['v']; names={v['n'] for v in t}
for n,y in[("TI-84 Plus CE-T","2016"),("TI-84 Plus CE Python","2021")]:
  if n not in names: t.append({"n":n,"mk":"Texas Instruments","y":y,"d":"Wikipedia TI-84 Plus CE series"})
for v in t:
  if v['n']=="TI-84 Plus CE": v['y']=v.get('y') or "2015"
tn=E['TI-Nspire']['v']
for v in tn:
  if v['n'].startswith('TI-Nspire CX /') and not v.get('y'): v['y']="2011"
  if v['n'].startswith('TI-Nspire CX II /') and not v.get('y'): v['y']="2019"
  if v['n']=='TI-Nspire / Nspire CAS' and not v.get('y'): v['y']="2007"
S="https://endlesspens.com/blogs/the-sunday-scribble/diving-deep-with-sailor-fountain-pens"
K['Piston-filling fountain pen']['x'].append({"n":"Sailor Professional Gear Realo","a":"","d":"Piston-filling Pro Gear released in 2006.","mk":"Sailor","y":"2006","s":S,"v":[],"g":"Japan","own":"Sailor Pen Co.","tier":"Independent","cty":"Japan"})
K['Cartridge-converter fountain pen']['x'].append({"n":"Sailor 1911 Jr.","a":"","d":"Smaller 1911 with a stainless steel nib and a PMMA resin body. Filling system not stated on the page read.","mk":"Sailor","y":"","s":S,"v":[],"g":"Japan","own":"Sailor Pen Co.","tier":"Independent","cty":"Japan"})
json.dump(d,open('/tmp/c5.tmp','w'),ensure_ascii=False,indent=1); os.replace('/tmp/c5.tmp',P)
