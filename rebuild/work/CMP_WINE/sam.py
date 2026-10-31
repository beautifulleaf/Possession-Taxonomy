import sys; sys.path.insert(0,'/home/user/Possession-Taxonomy/rebuild/work/CMP_WINE')
from lib import *
d=load(); sa=dept(d,'Wine of South America'); au=dept(d,'Wine of Australia & New Zealand')
C='https://en.wikipedia.org/wiki/Chilean_wine'; N='https://en.wikipedia.org/wiki/New_Zealand_wine'
nm=allnames(sa)
for kn,n in [('Chile: northern and coastal valleys','Atacama'),('Chile: northern and coastal valleys','Coquimbo'),('Chile: southern valleys','Austral'),('Chile: Central Valley','Central Valley (region)')]:
    print(add(sa,kn,{'n':n,'d':'Wine region of Chile named in the page'+"'s region list.",'s':C},nm))
for k in ('Chile: northern and coastal valleys','Chile: Central Valley','Chile: southern valleys'):
    cover(findkind(sa,k)[1],'Complete: the whole page was read (characters 0 to the end); the later part added only Atacama, Coquimbo, Austral and Central Valley from its region list. The page gives no appellation (DO) list.')
for k in ('Argentina: Cuyo','Argentina: Northwest','Argentina: Patagonia','Argentina: Buenos Aires, Córdoba and the east'):
    cover(findkind(sa,k)[1],'Complete: the whole page was read; the part after character 100,000 holds no further regions or geographical indications.')
nz=allnames(au)
for kn,n in [('North Island wine regions',"Central Hawke's Bay")]:
    print(add(au,kn,{'n':n,'d':'Wine region of New Zealand.','s':N},nz))
for k in ('North Island wine regions','South Island wine regions'):
    cover(findkind(au,k)[1],'Complete: the whole page was read; the part after character 100,000 added only Central Hawke\'s Bay.')
save(d)
