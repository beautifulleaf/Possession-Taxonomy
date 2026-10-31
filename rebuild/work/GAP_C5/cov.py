import json,os,re
P='/home/user/Possession-Taxonomy/rebuild/out/C5.json'
d=json.load(open(P))
orig=json.load(open('/home/user/Possession-Taxonomy/rebuild/work/GAP_C5/bak/C5.json'))
O={k['n']:k for dp in orig['depts'] for sh in dp['s'] for k in sh['k']}
K={}
for dp in d['depts']:
  for s in dp['s']:
    for k in s['k']: K[k['n']]=k
def strip(s):
  s=re.sub(r"\s*Coverage: \d+ entr(?:y|ies), taken from[^.]*\.","",s)
  s=re.sub(r"\s*Covers \d+ lines?; no complete register exists\.?","",s)
  return s.strip()
NO="No complete list exists; follows "
spec={}
tw="Wikidata class typewriter model (Q96676757, 51 items): 48 are entries across the three typewriter kinds; left out are Granville automatic typewriter and kleidograph, which no page names as a model line, and one item with no English label. Other lines follow the Olivetti typewriters and Typewriter Wikipedia articles, which are not a complete register."
for n in("Manual typewriter","Electric typewriter","Electronic typewriter"):
  spec[n]=lambda c:f"Covers {c} entries here and 48 of 51 items across the three typewriter kinds in the {tw}"
cw="Wikidata class calculator (Q31087, 59 rows): 35 are entries across the scientific, financial and vintage electronic kinds; the other 24 are website calculators, items with no English label, a category page, pocket computers, and regional models no page describes (Tesla, SR1, Uno, ET 55, Summit SM20, Casio HS-4)."
for n in("Scientific calculator","Financial calculator","Vintage electronic calculator"):
  spec[n]=lambda c:f"Covers {c} entries here; "+cw+" HP models also follow the Wikipedia article Hewlett-Packard calculators."
spec["Graphing calculator"]=lambda c:NO+"the Wikipedia articles Graphing calculator, TI-84 Plus CE series and TI-Nspire series, and Hewlett-Packard calculators; Wikipedia has no list of TI or Casio graphing models (the list pages returned 404)."
spec["Mechanical calculator"]=lambda c:f"Covers {c} of about 47 machines named in the Wikipedia article Mechanical calculator (first 100,000 of 127,872 characters read; the rest is references); left out are Babbage's engines and Harvard Mark I (computers, not calculators) and machines with no maker or year (Addiator, Thales, Toshiba, Victor, Sundstrand, Friden)."
spec["Slide rule"]=lambda c:f"Covers {c} of about 33 items named in the Wikipedia article Slide rule (first 100,000 of 129,638 characters read; the rest is references); left out are watches with slide-rule scales, trade-specific rules and general scales with no maker."
spec["Abacus"]=lambda c:f"Covers {c} of 20 types named in the Wikipedia article Abacus (first 100,000 of 112,001 characters read; the rest is references); left out are coulba, choreb, sandboard abacus, binary abacus, nano-abacus, logical abacus and the zhusuan method, which are concepts or have no region or date."
spec["Mechanical pencil"]=lambda c:f"Covers {c} of 21 models and makers named in the Wikipedia article Mechanical pencil (whole article read); left out are items already listed under another name or kind (Fixpencil, Koh-i-Noor colour pencils, Crayola Twistable, Alvin Tech-Matic, Pentel 350 E, Pentel Sharp ratchet) and Tombow."
spec["Fountain pen ink"]=lambda c:NO+"maker and retailer overviews; where a page lists a line's colours they are versions: Diamine standard range 116 of 116 on the Akkerman pages, Pilot Iroshizuku 23 of its 24 colours on the page read, De Atramentis Document 28, Noodler's first page of the Goldspot list only."
for n,k in K.items():
  if not k.get('x'): continue
  c=len(k['x'])
  base=strip((O.get(n,{}).get('sel') or k.get('sel','')))
  base=re.sub(r'[;,]?\s*no (single )?complete (list|register)[^.]*exists\.?','',base).strip().rstrip(';,')
  if base and not base.endswith('.'): base+='.'
  if n in spec:
    k['sel']=(base+" " if n not in("Graphing calculator","Mechanical calculator","Slide rule","Abacus","Mechanical pencil","Fountain pen ink") else "")+spec[n](c)
    if n in("Mechanical calculator","Slide rule","Abacus","Mechanical pencil","Fountain pen ink","Graphing calculator") : pass
    k['sel']=k['sel'].strip()
  else:
    k['sel']=NO+"the sources named here and cited on each entry. "+base
    k['sel']=k['sel'].strip()
json.dump(d,open('/tmp/c5.tmp','w'),ensure_ascii=False,indent=1); os.replace('/tmp/c5.tmp',P)
for n,k in K.items():
  if k.get('x'): print(n,len(k['x']),'|',k['sel'][-170:])
