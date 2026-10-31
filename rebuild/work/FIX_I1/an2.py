import json,re
d=json.load(open('out/I1.json'))
for dp in d['depts']:
  for s in dp['s']:
    for k in s['k']:
      for a in k.get('x',[]):
        if re.search(r'^(other|independent|mastering chains|modular and|vocal effects|tape plug|character|dynamic eq|single-game|multi-network)|emulators$',a['n'],re.I) or a['n'] in('Arch lineage','Mandriva lineage'):
          print(k['n'],'|',json.dumps(a,ensure_ascii=False)[:900])
for k in [k for dp in d['depts'] for s in dp['s'] for k in s['k'] if k['n'] in('File manager','Terminal emulator','AI coding assistant','Code editor plug-in','Media player','Backup software','Music player','Screenshot tool','Screen recorder and streaming software','Online whiteboard','Diagramming software')]:
  print(k['n'],k['m'])
