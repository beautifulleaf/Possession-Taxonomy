import json,os
P='/home/user/Possession-Taxonomy/rebuild/out/'
d=json.load(open(P+'E2.json'))
def find(name):
    for dpt in d['depts']:
        for s in dpt['s']:
            for kk in s['k']:
                if kk['n']==name: return kk
fly=find('Artificial fly'); have={e['n'].lower() for e in fly['x']}
DRY='https://www.orvis.com/fly-fishing/flies/dry-flies'; STR='https://www.orvis.com/fly-fishing/flies/streamer-flies'
new=[("Adam's Purple Parachute",DRY,'Dry fly'),("Fluttering Blue Damsel",DRY,'Dry fly'),("Lexi's Tactical Get 'Er Dun May",DRY,'Dry fly'),
("Finesse Game Changer",STR,'Streamer'),("Mini Articulated Trout Slider",STR,'Streamer'),("TH Rubber-Legged Bugger",STR,'Streamer'),("Daniel's UV Polar Jig",STR,'Streamer'),("Tungsten Jig Bugger",STR,'Streamer')]
add=0
for n,s,g in new:
    if n.lower() in have: continue
    fly['x'].append({'n':n,'a':'','mk':'','y':'','s':s,'v':[],'g':g}); add+=1
fly['sel']=fly['sel'].replace(' The Orvis dry-flies and streamer-flies pages were cut off by the fetch (about 105 and 80 results listed); the nymph page is page 1 of 2.',' The Orvis dry-flies page (84,274 characters) and streamer page were re-read in windows and are now covered as far as the fetch returned them; the nymph page is page 1 of 2. Covers %d patterns from those pages; no complete list of fly patterns exists (Wikipedia has no list page).'%len(fly['x']))
# Cleto Reyes
bg=find('Boxing glove')
for e in bg['x']:
    if e['n']=='Cleto Reyes glove':
        e['s']='https://cletoreyes.com/en/pages/acerca-de-nosotros'
        e['d']='Mexican glove maker; Cleto Reyes Castro began repairing gloves in 1938, his gloves were first used in a world title fight in 1945, the trademark followed in 1975 and Industria Reyes in 1979.'
        e['own']='Industria Reyes, S.A. de C.V.'; e['own_y']='1979'
# Hilleberg Anaris
t=find('Tent')
if 'hilleberg anaris' not in {e['n'].lower() for e in t['x']}:
    t['x'].append({'n':'Hilleberg Anaris','a':'','d':'Two-person ridge tent shown in the Hilleberg article.','mk':'Hilleberg','y':'','s':'https://en.wikipedia.org/wiki/Hilleberg','v':[],'g':'Hilleberg','cty':'Sweden','tier':'Independent'})
# paraglider / athletics notes
pg=find('Paraglider')
if 'EN 926' not in pg['sel'][-400:]:
    pg['sel']+=' Searched: "EN 926-1 paraglider certification classes LTF DHV"; the DHV article on wing choice (404) and the EN 926 PDF could not be fetched, so the EN equivalence is not stated here.'
for nm in ('Shot put','Discus','Hammer','Javelin'):
    k=find(nm)
    if k and 'sel' in k and 'Rule 187' not in k['sel']:
        k['sel']+=' World Athletics Rule 187 was searched for but its PDF was not fetched; the javelin table was re-read on athleticsdirect.co.uk (secondary guide, 800 g / 2.6-2.7 m for senior men, 600 g / 2.2-2.3 m for senior women).'
t_=P+'E2.json.tmp'; json.dump(d,open(t_,'w'),ensure_ascii=False,indent=1); os.replace(t_,P+'E2.json')
print(add)
