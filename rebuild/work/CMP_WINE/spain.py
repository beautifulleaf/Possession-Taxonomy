import sys; sys.path.insert(0,'/home/user/Possession-Taxonomy/rebuild/work/CMP_WINE')
from lib import *
import re,copy
d=load(); dp=dept(d,'Wine of Spain & Portugal')
SRC='https://www.mapa.gob.es/es/dam/jcr:2a49b727-24c9-4d11-aec6-3a6f44dc3b9e/Informe%20DOPs%202023_2024.pdf'
rows=[]
for l in open('/tmp/claude-0/-home-user-Possession-Taxonomy/0fa341d7-9ce7-5e1d-8d76-d0d6deeae94e/scratchpad/mapa.txt',encoding='utf8'):
    m=re.match(r'\| ([^|]+?) \| (DOCa|DO|VP|VC) \| ([^|]+?) \|',l)
    if m: rows.append(m.groups())
print(len(rows))
nm=allnames(dp)
vp=lambda reg:f'Vino de Pago, a single-estate designation, in {reg}.'
adds=[('Castilla-La Mancha: single-estate wines','Rosalejo',vp('Castilla-La Mancha')),
('Valencia: single-estate wines','Chozas Carrascal',vp('the Valencian Community')),
('Navarre: single-estate wines','Bolandín',vp('Navarre')),
('Castile and León: quality wine','Cebreros','Vino de Calidad con indicación geográfica in Castile and León.')]
for kn,n,dd in adds: print(add(dp,kn,{'n':n,'d':dd,'s':SRC},nm))
# new kind CyL pagos
s,qk=findkind(dp,'Castile and León: quality wine')
if not findkind(dp,'Castile and León: single-estate wines'):
    nk=copy.deepcopy(qk); nk['n']='Castile and León: single-estate wines'; nk['d']='Single-estate Vinos de Pago of Castile and León.'; nk['x']=[]
    s['k'].append(nk)
for n in ['Abadía Retuerta','Dehesa Peñalba','Urueña']:
    print(add(dp,'Castile and León: single-estate wines',{'n':n,'d':vp('Castile and León'),'s':SRC},nm))
# check
missing=[r for r in rows if norm(r[2]) not in nm and norm(re.sub(r'^Pago (de |Los )?','',r[2])) not in nm]
print('missing',missing)
sent='Complete for Spain: all 103 wine DOPs (2 DOCa, 69 DO, 7 VC, 25 VP) in the Ministry of Agriculture report for the 2023/24 campaign, together with the other Spanish kinds; the IGP (vino de la tierra) kinds follow Wikipedia and are not checked against the register.'
for sh in dp['s']:
    for k in sh['k']:
        if k['n'].startswith(('Rioja, Navarre','Navarre','Catalonia','Andalusia','Galicia','Castile','Aragon','Castilla','Valencia','Madrid','Extremadura','Balearic','Canary','Asturias')) and 'regional' not in k['n']:
            cover(k,sent)
save(d)
