import json,os
P='/home/user/Possession-Taxonomy/rebuild/out/C5.json'
d=json.load(open(P))
E={}
for dp in d['depts']:
  for s in dp['s']:
    for k in s['k']:
      for e in k.get('x',[]): E[e['n']]=e
iro="Ajisai|Ama-iro|Asa-gao|Chiku-rin|Fuyu-gaki|Fuyu-syogun|Hana-ikada|Hotaru-bi|Kon-peki|Ku-jaku|Momiji|Murasaki-shikibu|Shin-kai|Shin-ryoku|Sui-gyoku|Take-sumi|Syo-ro|Yama-budo|Yama-guri|Yu-yake|Syun-gyo|To-ro|Rikka".split("|")
e=E['Pilot Iroshizuku']; have={v['n'].lower() for v in e['v']}
for n in iro:
  if n.lower() not in have: e['v'].append({"n":n,"y":"","d":""})
e['s']="https://pulpaddiction.com.au/products/pilot-iroshizuku-ink-sample-package-complete-line-24"
nd="Revolution Blue|Southwest Sunset|54th Massachusetts|Black Swan in Australian Roses|Heart of Darkness|Baystate Blue|Lexington Gray|Black Eel|X-Feather Blue|Red-Black|Rome Burning|Habanero|Navajo Turquoise|Azure|English Roses|Kiowa Pecan Brown|V-mail North African Violet|Brevity Blue|Dark Matter|Hellfire|Fox Red|Air-Corp Blue-Black|Zhivago|American Aristocracy|Blue Ghost|Baltimore Canyon|La Reine Mauve|Eel Blue|Blue Nosed Bear".split("|")
e=E["Noodler's Bulletproof"]; have={v['n'].lower() for v in e['v']}
for n in nd:
  if n.lower() not in have: e['v'].append({"n":n,"y":"","d":""})
e['s']="https://goldspot.com/collections/noodlers-inks-1"
json.dump(d,open('/tmp/c5.tmp','w'),ensure_ascii=False,indent=1); os.replace('/tmp/c5.tmp',P)
