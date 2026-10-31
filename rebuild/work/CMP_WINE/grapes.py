import sys,copy; sys.path.insert(0,'/home/user/Possession-Taxonomy/rebuild/work/CMP_WINE')
from lib import *
d=load(); g=dept(d,'Grape varieties')
SRC='https://en.wikipedia.org/wiki/List_of_grape_varieties'
hs,hk=findkind(g,'Interspecific hybrid varieties')
if not any(s['n']=='American species varieties' for s in g['s']):
    nk=copy.deepcopy(hk); nk['n']='American-species wine varieties'; nk['x']=[]
    nk['d']='Wine grape varieties of Vitis labrusca, V. rotundifolia and other American species.'
    nk['tt']=[['Species',['Vitis labrusca','Vitis rotundifolia','Vitis aestivalis','Vitis mustangensis']]]
    sh=copy.deepcopy({k:v for k,v in hs.items() if k!='k'}); sh['n']='American species varieties'; sh['t']='Wine grapes of American vine species listed in the same Wikipedia list.'; sh['k']=[nk]
    g['s'].append(sh)
else: nk=findkind(g,'American-species wine varieties')[1]
nm=allnames(g)
sp={'Catawba':'Vitis labrusca','Concord':'Vitis labrusca','Delaware':'Vitis labrusca','Diamond':'Vitis labrusca','Fredonia':'Vitis labrusca','Isabella':'Vitis labrusca','Ives':'Vitis labrusca','Niagara':'Vitis labrusca','Noah':'Vitis labrusca','Black Spanish':'Vitis aestivalis','Muscadine':'Vitis rotundifolia','Scuppernong':'Vitis rotundifolia','Noble':'Vitis rotundifolia','Carlos':'Vitis rotundifolia','Black Beauty':'Vitis rotundifolia','Magnolia':'Vitis rotundifolia','Mustang Grape':'Vitis mustangensis'}
for n,s in sp.items():
    print(n,add(g,nk['n'],{'n':n,'d':f'Wine grape variety listed under {s}; berry colour not stated here.','s':SRC,'g':'United States'},nm))
sent="Read to the end of the page text; the part after character 280,000 holds only the rosé rows, table-only grapes and species sections, of which the wine grapes of American species are in their own kind. The page was read through a summariser, so completeness is not proven; table-only grapes and rootstocks are out of scope."
for s in g['s']:
    for k in s['k']: cover(k,sent)
save(d)
