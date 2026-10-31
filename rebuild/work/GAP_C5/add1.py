import json,os
P='/home/user/Possession-Taxonomy/rebuild/out/C5.json'
d=json.load(open(P))
K={}
for dp in d['depts']:
  for s in dp['s']:
    for k in s['k']: K[k['n']]=k
W=lambda q:'https://www.wikidata.org/wiki/'+q
def add(kind,rows,tpl):
  k=K[kind]; have={e['n'].lower() for e in k['x']}
  for q,n,mk,y,cty,own,tier in rows:
    if n.lower() in have: continue
    k['x'].append({"n":n,"a":"","d":(tpl%mk if "%s" in tpl else tpl),"mk":mk,"y":y,"s":W(q),"g":mk,"own":own,"tier":tier,"cty":cty})
OW="owner not stated"
T="%s typewriter model listed on Wikidata."
add("Manual typewriter",[("Q139796296","Olivetti Lettera 12","Olivetti","","Italy",OW,"Independent"),("Q109831928","Olympia Splendid 66","Olympia","1966","Germany",OW,"Independent"),("Q119142869","Erika 50","Erika","","Germany",OW,"Independent"),("Q130325748","Mignon 4","AEG Mignon","","Germany",OW,"Independent")],T)
add("Electric typewriter",[("Q3881818","Olivetti ET Personal 540","Olivetti","","Italy",OW,"Independent"),("Q16583778","Olivetti ET Personal 55","Olivetti","","Italy",OW,"Independent"),("Q16583843","Olivetti Praxis 35","Olivetti","","Italy",OW,"Independent"),("Q105984380","Olivetti Editor 3","Olivetti","","Italy",OW,"Independent"),("Q107578871","Olivetti Editor S14","Olivetti","","Italy",OW,"Independent"),("Q119159826","Erika 3006","Erika","","Germany",OW,"Independent")],T)
add("Electronic typewriter",[("Q16583781","Olivetti ET 101","Olivetti","","Italy",OW,"Independent"),("Q16583784","Olivetti ET 121","Olivetti","","Italy",OW,"Independent"),("Q16583787","Olivetti ET 201","Olivetti","","Italy",OW,"Independent"),("Q16583791","Olivetti ET 351","Olivetti","","Italy",OW,"Independent"),("Q48806356","Olivetti ET 2400","Olivetti","","Italy",OW,"Independent"),("Q105984436","Olivetti ET 2500","Olivetti","","Italy",OW,"Independent"),("Q48814023","Olivetti Lettera 92","Olivetti","","Italy",OW,"Independent"),("Q24937857","Olivetti CWP1","Olivetti","","Italy",OW,"Independent"),("Q109864433","Silver Reed 2500SL","Silver Seiko","1980","Japan",OW,"Independent"),("Q56298879","Silver Reed Colour PenGraph EB50","Silver Seiko","","Japan",OW,"Independent"),("Q124293673","Robotron S 6011","VEB Robotron","","Germany",OW,"Independent")],T)
C="Calculator model listed on Wikidata (%s)."
hp=lambda q,n,y="":(q,n,"HP",y,"United States","HP Inc.","Global group")
ti=lambda q,n:(q,n,"Texas Instruments","","United States","Texas Instruments","National champion")
add("Scientific calculator",[hp("Q783760","HP-34C"),hp("Q5635553","HP-22S"),hp("Q5635548","HP-20S"),hp("Q9284772","HP-21S"),hp("Q5635541","HP-10s"),hp("Q5635630","HP 33s"),ti("Q7670314","TI-55"),ti("Q1536274","TI-57")],"Calculator model listed on Wikidata.")
add("Financial calculator",[hp("Q5635549","HP-27"),hp("Q5635627","HP 30b"),hp("Q5635547","HP-20b")],"Calculator model listed on Wikidata.")
add("Vintage electronic calculator",[hp("Q17513366","HP-22"),hp("Q5635546","HP-19C/29C"),("Q966756","Sumlock ANITA calculator","Bell Punch","","United Kingdom",OW,"Independent"),("Q131398266","Braun ET 66","Braun","1987","Germany",OW,"Independent"),("Q116046113","Casio HL-820A","Casio","","Japan","Casio Computer Co.","National champion"),("Q105064088","Elektronika MK-41","Svetlana","","Russia",OW,"Independent")],"Calculator model listed on Wikidata.")
json.dump(d,open('/tmp/c5.tmp','w'),ensure_ascii=False,indent=1)
os.replace('/tmp/c5.tmp',P)
