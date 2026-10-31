import json,os
P='/home/user/Possession-Taxonomy/rebuild/out/C5.json'
d=json.load(open(P))
K={}
for dp in d['depts']:
  for s in dp['s']:
    for k in s['k']: K[k['n']]=k
S="https://goldspot.com/collections/kaweco-pens"
N=" Filling system not stated on the page read."
have={e['n'].lower() for k in K.values() for e in k.get('x',[])}
def mk(n,dd):
  return {"n":n,"a":"","d":dd,"mk":"Kaweco","y":"","s":S,"v":[],"g":"Germany","own":"owner not stated","tier":"Independent","cty":"Germany"}
for n,dd in[("Kaweco Classic Sport","Octagonal pocket pen of light ABS; the collection was revived in the 1980s."+N),("Kaweco Frosted Sport","Pocket pen in semi-translucent colours, also made as rollerball, ballpoint and pencil."+N),("Kaweco Skyline Sport","Compact pocket pen of the Sport family."+N),("Kaweco Liliput","Smallest Kaweco pen in metal finishes."+N),("Kaweco Student","Simple fountain pen for students; also made as rollerball and ballpoint."+N),("Kaweco Special","Eight-sided pen, also made as rollerball, ballpoint and pencil."+N),("Kaweco Dia2","Black pen with knurled grip."+N),("Kaweco Supra","Sleek pen with an optional extension."+N),("Kaweco AL Sport","Aluminium pocket pen."+N),("Kaweco Brass Sport","Heavy brass pocket pen."+N),("Kaweco Original","Matte aluminium pen with a faceted octagonal barrel."+N)]:
  if n.lower() not in have: K['Cartridge-converter fountain pen']['x'].append(mk(n,dd))
if 'kaweco piston sport' not in have: K['Piston-filling fountain pen']['x'].append(mk("Kaweco Piston Sport","Sport-size pen that fills from bottled ink."))
json.dump(d,open('/tmp/c5.tmp','w'),ensure_ascii=False,indent=1); os.replace('/tmp/c5.tmp',P)
