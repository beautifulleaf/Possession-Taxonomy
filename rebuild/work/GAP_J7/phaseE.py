import json,re,unicodedata
d=json.load(open('stageD.json'))
def norm(s):
    s=unicodedata.normalize('NFKD',s.lower());s=''.join(c for c in s if not unicodedata.combining(c));return re.sub(r'[^a-z0-9]+','',s)
bar='''Albesani;Asili;Ausario;Balluri;Basarin;Bernadot;Bordini;Bric Micca;Bricco di Neive;Bricco di Treiso;Ca’ Grossa;Canova;Cars;Casot;Castellizzano;Cavanna;Cole;Cottà;Currà;Faset;Fausoni;Ferrere;Gaia-Principe;Gallina;Garassino;Giacone;Giacosa;Manzola;Marcarini;Marcorino;Martinenga;Meruzzano;Montaribaldi;Montefico;Montersino;Montestefano;Muncagota;Nervo;Ovello;Pajè;Pajorè;Pora;Rabajà;Rabajà-Bas;Rio Sordo;Rivetti;Rizzi;Roccalini;Rocche Massalupo;Rombone;Roncaglie;Roncagliette;Ronchi;San Cristoforo;San Giuliano;San Stunet;Secondine;Serraboella;Serracapelli;Serragrilli;Starderi;Tre Stelle;Trifolera;Valeirano;Vallegrande;Vicenziana'''.split(';')
bl=[l.split('. ',1)[1] for l in open('barolo_mga.txt').read().strip().split('\n')]
for dp in d['depts']:
  for s in dp['s']:
    for k in s['k']:
      if k['n']=='Piedmont: DOCG appellations':
        for e in k['x']:
          if e['n'] in('Barolo','Barbaresco'):
            lst=bl if e['n']=='Barolo' else bar
            have={norm(v['n']) for v in e['v']}
            for m in lst:
                if norm(m) in have: continue
                have.add(norm(m))
                e['v'].append({'n':m,'mk':'','y':'','d':f"{e['n']} MGA (additional geographical mention), vineyard area."})
        k['sel']+=" Versions of Barolo are the 174 MGA names the Barolo World list prints (the disciplinare approves 181); versions of Barbaresco are the 66 MGAs on Italian Wine Central; Barolo Riserva and Chinato are earlier versions."
json.dump(d,open('stageE.json','w'),ensure_ascii=False)
