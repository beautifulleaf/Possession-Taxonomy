import json,os
P='rebuild/out/J10.json'
d=json.load(open(P))
U='https://en.wikipedia.org/wiki/List_of_cigar_brands'
kinds={K['n']:K for D in d['depts'] for S in D['s'] for K in S['k']}
G=['Altadis','Imperial','Swedish Match','Gallaher']
def tier(o):
    return 'Global group' if any(g in o for g in G) else 'Independent'
def add(kind,n,cty,own,desc=None):
    K=kinds[kind]
    if any(e['n'].lower()==n.lower() for e in K['x']): return
    K['x'].append({'n':n,'a':'','d':desc or f"Cigar marque; the list names {own} as maker or owner." if own!='owner not stated' else f"Cigar marque in the list of cigar brands; no owner stated.",'mk':n,'y':'','s':U,'g':own,'own':own,'tier':tier(own),'cty':cty})
allnames={e['n'].lower() for K in kinds.values() for e in K.get('x',[])}
# country-placed
add('Dominican premium cigar','Aristoff','Dominican Republic','Corporacion Cigar Export')
add('Dominican premium cigar','Star Cigar','Dominican Republic','owner not stated')
add('Honduran premium cigar','777','Honduras','Tabacos S.A.','Cigar marque made in Honduras and Nicaragua; the list names Tabacos S.A.')
for n in ['1881','1881 Perique','La Flor de la Isabela']:
    add('Cigar from other countries',n,'Philippines','Tabacalera Incorporada')
add('Cigar from other countries','Sancti Spiritus','United States','José "Pepin" Garcia','Cigar marque made in Miami, Florida; the list names José "Pepin" Garcia.')
add('Cigar from other countries','Lars Tetens','United States','Lars Tetens','Cigar marque made in the United States, Dominican Republic and Mexico.')
add('Cigar from other countries','Propio','Ecuador','Achievement Cigar Company Inc.','Cigar marque made in Ecuador from Cuban-seed tobacco; the list names Achievement Cigar Company Inc.')
add('Cigar from other countries','Zino Platinum','','x') if False else None
# country not stated
src=base=kinds['Cigar from other countries']
new={'n':'Cigar marque, country not stated','a':'','d':'Cigar marque that the list of cigar brands names without a country of manufacture.','s':U,'tt':[['Format',['Premium handmade','Machine-made']]],'x':[],'m':[],'xg':'by owner','nl':'One entry is a cigar marque sold under its own name; the list gives no country, so none is placed.'}
rows="""57|ITC
5 Vegas|Cigars International
898 Collection|Mike's Cigars
Adan y Eva|Cuban Desire Corporation
American Rebel|Stogiebird
Bahman|ITC
Cabaiguan|Tatuaje Cigars, Inc.
Cuesta-Rey|J.C. Newman
Davidoff|Davidoff / Imperial Tobacco
Diesel|A. J. Fernandez Cigars
Djarum Black|Djarum
Don Alfredo|owner not stated
Don Cándido|owner not stated
Dunhill|owner not stated
DUX|Altadis
East Coast Rollers|Famous Smoke Shop
El Crédito|Altadis
Flor de las Antillas|Don Pepin Garcia
Flor del Punto|owner not stated
Fumadores|José "Pepin" García
Guantanamera|owner not stated
Havana Soul|General Cigar Company
Hestia Tobacco|ITC
Indian Tabac|Rocky Patel
Loeser & Wolff|owner not stated
Maker's Mark|owner not stated
Marsh Wheeling|National Cigar Corp.
Maximus|J.C. Newman
Maxum|owner not stated
Morro Castle|A. J. Fernandez Cigars
Nat Sherman|Nat Sherman
Old Henry|J. Cortès Cigars N.V.
Padilla|Padilla
La Palina Goldie|La Palina
Paul Garmirian|Davidoff
La Paz|Swedish Match
Playboy|Altadis
Royal Dutch Cigars|Ritmeester
Royal Jamaican|Altadis
San Bosco|owner not stated
San Lotano|A. J. Fernandez Cigars
Siglo|Altadis
Tierra del Sol|Tabacalera Perdomo
TIR|ITC
Toraño|General Cigar Co.
T4|ITC
Zar|ITC
Zica|ITC""".split('\n')
rows=[r for r in rows if not r.startswith('La Palina Goldie')]
for r in rows:
    n,o=r.split('|')
    if n.lower() in allnames: continue
    new['x'].append({'n':n,'a':'','d':(f"Cigar marque; the list names {o} as owner or maker." if o!='owner not stated' else "Cigar marque in the list; neither country nor owner is stated."),'mk':n,'y':'','s':U,'g':o,'own':o,'tier':tier(o),'cty':''})
new['x'].sort(key=lambda e:(e['g'],e['n']))
new['sel']=f"Every marque in Wikipedia's List of cigar brands whose country the list leaves blank and that is not already a Cuban, machine-made or cigarillo entry here; owner as the list gives it. Complete: all {len(new['x'])} such rows of the list's about 170; the country-bearing rows sit in the kinds by country."
sh=[S for D in d['depts'] if D['n']=='Cigars' for S in D['s'] if any(K['n']=='Cigar from other countries' for K in S['k'])][0]
if 'Cigar marque, country not stated' not in kinds:
    sh['k'].append(new)
# coverage lines
def cov(kind,txt):
    K=kinds[kind]; s=K['sel']; i=s.find('Covers ')
    K['sel']=(s[:i] if i>=0 else s).rstrip()+' '+txt
total=lambda k:len(kinds[k]['x'])
for k in ['Dominican premium cigar','Nicaraguan premium cigar','Honduran premium cigar','Mexican & Brazilian cigar','Cigar from other countries']:
    cov(k,f"Complete: all {total(k)} country-bearing rows of Wikipedia's List of cigar brands (about 170 rows) for this country; marques made in both Cuba and the Dominican Republic sit with the Habanos kind; rows with no country sit in 'Cigar marque, country not stated'; machine-made brands stay in their own kinds.")
json.dump(d,open(P+'.tmp','w'),ensure_ascii=False,indent=1); os.replace(P+'.tmp',P)
print(len(new['x']))
