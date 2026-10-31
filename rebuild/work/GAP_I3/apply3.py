import json,os
B='/home/user/Possession-Taxonomy/rebuild/out/'
d=json.load(open(B+'I3.json')); K={k['n']:k for dp in d['depts'] for s in dp['s'] for k in s['k']}
W='https://en.wikipedia.org/wiki/'
upd={('Video streaming service','MGM+'):('Amazon MGM Studios',2022,W+'MGM%2B'),
('Video streaming service','Discovery+'):('Skydance',2026,W+'Discovery%2B'),
('Video streaming service','SkyShowtime'):('Sky Group and Skydance (50/50 joint venture)',None,W+'SkyShowtime'),
('Video streaming service','Binge'):('DAZN (Foxtel Group)',None,W+'Binge_(streaming_service)'),
('Music streaming','Tidal'):('Block, Inc.',2021,W+'Tidal_(service)'),
('Music streaming','SoundCloud'):('SoundCloud Global Limited & Co. KG',None,W+'SoundCloud'),
('Music streaming','Bandcamp'):('Songtradr',2023,W+'Bandcamp'),
('Music streaming','Deezer'):('Access Industries (largest shareholder, 41 %)',2016,W+'Deezer')}
for (k,n),(o,y,s) in upd.items():
    for e in K[k]['x']:
        if e['n']==n:
            e['own']=o
            if y: e['own_y']=str(y)
brands=json.load(open(B+'I3_brands.json')); have={b['n'].lower() for b in brands['b']}
add=set()
for k in K.values():
    for e in k.get('x') or []:
        for f in ('mk','own'):
            v=e.get(f)
            if v and v.lower() not in have: add.add((v,k['n']))
seen=set()
for v,kn in sorted(add):
    if v.lower() in seen: continue
    seen.add(v.lower())
    brands['b'].append({'n':v,'c':'','f':'','seg':'Mainstream','kf':'','d':f'Owner or maker of {kn}.','s':K[kn].get('s') or ''})
print('brands added',len(seen))
for fn,obj in (('I3.json',d),('I3_brands.json',brands)):
    t=B+fn+'.tmp'; json.dump(obj,open(t,'w'),ensure_ascii=False,indent=1); os.replace(t,B+fn)
