import sys; sys.path.insert(0,'/home/user/Possession-Taxonomy/rebuild/work/GAP_E6')
from common import *
d=load(); W='https://en.wikipedia.org/wiki/'
k=find(d,'Dobsonian telescope'); S=W+'Dobsonian_telescope'
have={e['n'].lower() for e in k['x']}
for n,t,mk,y in [('Webster D18','18-inch truss Dobsonian reviewed in the article.','Webster Telescopes',''),
 ('Hubble Optics UL','Ultra-light truss Dobsonians; the UL16 is a 16-inch model.','Hubble Optics',''),
 ('Waite Research Renegade','Large Dobsonian reviewed in Astronomy magazine; the Renegade 20 is the model cited.','Waite Research',''),
 ('New Moon Telescopes collapsible truss','Collapsible-truss Dobsonians from 16 to 36 inch, including a 36-inch hybrid shown in 2018.','New Moon Telescopes','2013'),
 ('Meade and Orion upgraded Dobsonians','Imported 1990s Dobsonians with metal tubes and more refined hardware from Meade and Orion.','Meade Instruments','1990s')]:
    if n.lower() not in have: k['x'].append(ent(n,t,mk=mk,y=y,s=S,g='Maker lines'))
for e in k['x']:
    if e['n']=='Coulter Odyssey': e['y']='1980s'
    if e['n']=='Obsession truss Dobsonian': e['y']='1989'; e['role']='origin' if False else e.get('role')
k['sel']='Dobsonian design and named lines from the Wikipedia article Dobsonian telescope (all named lines in the article; the 50-inch Fullum folded Newtonian is a one-off, out of scope), with maker lines from the earlier pass.'
k=find(d,'Smart telescope'); S=W+'Unistellar'
for e in k['x']:
    if e['n']=='Unistellar eVscope':
        e['v'].extend([{'n':'eVscope 2','mk':'Unistellar','y':'','d':'wider field of view and improved monitor'},{'n':'eQuinox','mk':'Unistellar','y':'','d':'longer battery life and no monitor'}])
        e['d']='114 mm reflector with a CMOS sensor and live stacking, viewed on a connected phone, tablet or laptop; prototype shown in 2017.'
        e['s']=S
k['sel']="Smart telescopes named in Wikipedia's Robotic telescope article (Seestar, Dwarf, Unistellar, Vaonis) and Unistellar article, with lines from the earlier pass; the retailer list (skiesandscopes.com) returned 403 and is deferred."
k=find(d,'Guide scope')
for e in k['x']:
    if e['g']=='Maker lines': e['g']='Guide scopes'
save(d)
