import json,os,re
p='out/B10.json'
d=json.load(open(p))
cats=("Dog food","Dog treats","Dry cat food","Wet cat food","Fresh, frozen and raw cat food","Veterinary cat food","Cat treats","Cat litter")
origin="No complete list exists; only the origin entry is kept under the icon rule (no design-collection or major-award landmark confirmed on a fetched page)."
other={"Western saddle":"No complete list exists; follows the Western types named in Wikipedia's Saddle article and one earlier sourced page.",
"Australian stock saddle":"No complete list exists; follows earlier sourced maker and museum pages (Wikipedia's Saddle article names the type only).",
"Side saddle":"No complete list exists; follows earlier sourced pages (Wikipedia's Saddle article names the type only).",
"Stirrup":"No complete list exists; follows earlier sourced pages.",
"Snaffle bit":"Covers the snaffle patterns named in Wikipedia's Bit (horse) article (snaffle and bradoon) plus the Fulmer and Baucher from earlier pages; the article names no further snaffle patterns.",
"Bitless bridle":"No complete list exists; follows earlier sourced Wikipedia and maker pages.",
"Reins":"No complete list exists; follows earlier sourced Wikipedia and maker pages.",
"Falconry hood":"No complete list exists; follows earlier fetched falconry pages. Not a complete list of hood patterns.",
"Jesses and anklets":"No complete list exists; follows earlier fetched falconry pages.",
"Falconry bells":"No complete list exists; follows earlier fetched falconry pages.",
"Falconry glove":"No complete list exists; follows earlier fetched falconry pages.",
"Falconry perch":"No complete list exists; follows earlier fetched falconry pages."}
for dp in d['depts']:
  for s in dp.get('s',[]):
    for k in s.get('k',[]):
      if not k.get('x'): continue
      sel=k.get('sel','')
      if k['n'] in cats:
        k['sel']=re.sub(r"Covers (\d+) of about 100 brands","No complete list exists; follows the brand pages of the five dominant groups and a US sales list. Lists \\1 brands",sel)
        continue
      if any(t in sel for t in('Complete:','Covers','No complete list')): continue
      add=other.get(k['n'],origin if 'origin entry' in sel else "No complete list exists; follows earlier sourced pages.")
      k['sel']=(sel.rstrip()+' '+add).strip()
json.dump(d,open(p+'.tmp','w'),ensure_ascii=False,indent=1); os.rename(p+'.tmp',p)
for dp in d['depts']:
  for s in dp.get('s',[]):
    for k in s.get('k',[]):
      if k.get('x') and not any(t in k.get('sel','') for t in('Complete:','Covers','No complete list')): print('MISSING',k['n'])
      if k['n']=='Dog toy': print(k['sel'][-250:])
