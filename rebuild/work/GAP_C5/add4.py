import json,os
P='/home/user/Possession-Taxonomy/rebuild/out/C5.json'
d=json.load(open(P))
K={}
for dp in d['depts']:
  for s in dp['s']:
    for k in s['k']: K[k['n']]=k
OW="owner not stated"
def add(kind,rows,src,mk,g,cty,own,tier):
  k=K[kind]; have={e['n'].lower() for e in k['x']}
  for n,y,dd in rows:
    if n.lower() in have: continue
    k['x'].append({"n":n,"a":"","d":dd,"mk":mk,"y":y,"s":src,"v":[],"g":g,"own":own,"tier":tier,"cty":cty})
PS="https://goldspot.com/pages/pilot-pens"
N="Filling system not stated on the page read."
add("Cartridge-converter fountain pen",[("Pilot Custom 743","","Pilot Custom line pen. "+N),("Pilot Custom 845","","Pilot Custom line pen with an 18-karat gold nib. "+N),("Pilot Custom 912","","Pilot Custom line pen. "+N),("Pilot Custom Urushi","","Pilot Custom line pen with urushi lacquer. "+N),("Pilot Explorer","","Pilot pen with a stainless steel nib. "+N),("Pilot Grance","","Pilot pen with a 14-karat gold nib. "+N),("Pilot Justus 95","","Pilot pen with an adjustable dual-performance nib. "+N),("Pilot E95S","","Pilot pen named on the page read. "+N)],PS,"Pilot","Japan","Japan","Pilot Corporation","Independent")
add("Retractable-nib fountain pen",[("Pilot Decimo","","Slim retractable-nib pen in the Pilot capless family.")],PS,"Pilot","Japan","Japan","Pilot Corporation","Independent")
C="https://en.wikipedia.org/wiki/Caran_d%27Ache_(company)"
add("Wooden pencil",[("Caran d'Ache Technograph","1920s","Classic pencil introduced in the 1920s."),("Caran d'Ache Prismalo","1931","Described as the first watercolour pencil in the world."),("Caran d'Ache Neocolor","1952","Wax oil pencil, made water-soluble in 1972."),("Caran d'Ache 6901 Luminance","2010","Range of colour pencils.")],C,"Caran d'Ache","Switzerland","Switzerland","Caran d'Ache SA","Independent")
add("Ballpoint pen",[("Caran d'Ache Ecridor","1953","Originally an alternative to the Fixpencil, later a luxury ballpoint line."),("Caran d'Ache 849","1969","Hexagonal ballpoint pen, successor to the Ecridor.")],C,"Caran d'Ache","Switzerland","Switzerland","Caran d'Ache SA","Independent")
add("Cartridge-converter fountain pen",[("Caran d'Ache Madison","","The firm's first fountain pen. "+N)],C,"Caran d'Ache","Switzerland","Switzerland","Caran d'Ache SA","Independent")
json.dump(d,open('/tmp/c5.tmp','w'),ensure_ascii=False,indent=1)
os.replace('/tmp/c5.tmp',P)
