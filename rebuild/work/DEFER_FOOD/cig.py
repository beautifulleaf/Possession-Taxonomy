import json
data={
"José L. Piedra":[("Brevas","1996","Brevas JLP","42 × 133 mm","Corona"),("Cazadores","1996","Cazadores JLP","43 × 152 mm","Long Corona"),("Conservas","1996","Conservas JLP","44 × 140 mm","Long Corona"),("Petit Caballeros","2019","Hermoso Corto","48 × 120 mm","Corona Extra"),("Petit Cazadores","2007","Petit Cazadores","43 × 105 mm","Petit Corona")],
"Quintero":[("Brevas","c2002","Nacionales","40 × 140 mm","Corona"),("Favoritos","2012","Conchas No.2","50 × 115 mm","Petit Robusto"),("Londres Extra","","Standard","40 × 123 mm","Petit Corona"),("Panetelas","c2002","Vegueritos","37 × 127 mm","Short Panetela"),("Petit Quintero","2014","Petit Cazadores","43 × 105 mm","Petit Corona"),("Tubulares","2016","Brevas JLP","42 × 133 mm","Corona")],
"Fonseca":[("Cosacos","","Cosacos","42 × 135 mm","Corona"),("Delicias","","Standard","40 × 123 mm","Petit Corona"),("Fonseca No.1","","Cazadores","43 × 162 mm","Lonsdale"),("KDT Cadetes","","Cadetes","36 × 115 mm","Short Panetela")],
"Vegas Robaina":[("Famosos","1997","Hermosos No.4","48 × 127 mm","Corona Extra"),("Unicos","1997","Piramides","52 × 156 mm","Pyramid")],
"El Rey del Mundo":[("Choix Suprême","","Hermosos No.4","48 × 127 mm","Corona Extra"),("Demi Tasse","","Entreactos","30 × 100 mm","Small Panetela")],
"Juan López":[("Selección No.1","","Coronas Gordas","46 × 143 mm","Grand Corona"),("Selección No.2","","Robustos","50 × 124 mm","Robusto")],
"La Flor de Cano":[("Elegidos","2020","Lirios","50 × 127 mm","Robusto"),("Petit Coronas","c2002","Standard","40 × 123 mm","Petit Corona")],
"Saint Luis Rey":[("Regios","","Hermosos No.4","48 × 127 mm","Corona Extra")],
"Sancho Panza":[("Belicosos","","Campanas","52 × 140 mm","Pyramid")],
}
d=json.load(open('rebuild/out/J10.json'))
k=[k for dp in d['depts'] for s in dp['s'] for k in s['k'] if k['n'].startswith('Habano')][0]
for e in k['x']:
    if e['n'] in data:
        have={v['n'] for v in e.get('v',[])}
        vs=e.setdefault('v',[])
        for n,y,fac,sz,cn in data[e['n']]:
            full=f"{e['n']} {n}"
            if full in have or n in have: continue
            yy=y if y.isdigit() else ""
            note=f"Current production vitola; factory size {fac}, {sz}, {cn}"+("" if y.isdigit() or not y else f"; released {y}")+("; released before 1960" if not y else "")
            vs.append({"n":full,"mk":e['n'],"y":yy,"d":note+"."})
k['sel']=k['sel'].rstrip()+" Current-production vitolas for the marques that had none were added from the Cuban Cigar Website list of Current Production Cigars (236 cigars; fetched 2026-10-31)."
json.dump(d,open('rebuild/work/DEFER_FOOD/J10.tmp','w'),ensure_ascii=False)
