import sys; sys.path.insert(0,'/home/user/Possession-Taxonomy/rebuild/work/CMP_WINE')
from lib import *
d=load()
g=dept(d,'Grape varieties')
for e in findkind(g,'American-species wine varieties')[1]['x']: e['g']='Origin not stated'
it=dept(d,'Wine of Italy')
for s in it['s']:
    for k in s['k']:
        t=k['n'].split(': ')[-1]
        if t.startswith('DOCG'): cover(k,'Complete: the 76 DOCG names that Wikipedia\'s List of Italian DOCG wines actually lists (the page says 77 but names 76).')
        elif t.startswith('DOC'): cover(k,'Covers 330 DOC names of Wikipedia\'s List of Italian DOC wines; Wikidata lists about 980 DOC items for Italian wine, but these are typologies and sub-zones (riserva, grape and colour variants) of the same appellations, so no further appellations were added.')
        elif t.startswith('IGT'): cover(k,'Complete: all 113 distinct IGT names in Wikipedia\'s List of Italian IGT wines (117 rows, because cross-region names such as delle Venezie and Vallagarina repeat).')
for dn in ('Wine of South America','Wine of Australia & New Zealand'):
    dp=dept(d,dn)
    for s in dp['s']:
        for k in s['k']:
            k['sel']=k['sel'].replace(' (first part of the page only)','').replace(', fetched 2026-10-31 (first part of the page only)',', fetched 2026-10-31')
save(d)
