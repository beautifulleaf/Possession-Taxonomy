import json,os
R='/home/user/Possession-Taxonomy/rebuild/'
d=json.load(open(R+'out/F4.json'))
W='https://en.wikipedia.org/wiki/'
K={k['n']:k for dp in d['depts'] for sh in dp['s'] for k in sh['k']}
def add(kind,rows,src,sel):
    k=K[kind]; have={e['n'].lower() for e in k['x']}
    for n,y,desc in rows:
        if n.lower() in have: continue
        k['x'].append({'n':n,'a':'','d':desc,'mk':'','y':y,'s':src,'dt':'','v':[]})
    k['sel']=k['sel'].rstrip()+' '+sel
add('Phurba',[
('Hayagriva phurba','','Variant whose pommel may show the yidam Hayagriva.'),
('Bhairab phurba','','Healing kila of tantric Newari gubajus, used for children\'s diseases.'),
('Jhankri phurba','','Phurba of jhankris with three or more heads on the upper area.'),
('Gubaju phurba','','Phurba of hereditary Newari priests, usually with one head and a double vajra.'),
('Wooden phurba','','Phurba of wood used for shamanic healing, often with two nagas on the blade.'),
],W+'Phurba','Phurba article read in full: Complete: 6 of 6 named types (thokcha and panchaloha are materials).')
add('Nativity set',[
('Weihnachtsberg','','Christmas mountain scene combining a nativity with mining motifs.'),
('Czech paper crèche','','Low-cost paper-cut crèche, called the crèche of the poor.'),
],W+'Nativity_scene','Nativity scene article re-read to 100,000 of 140,460 characters: Covers 10 of 26 rows; the rest are events, competitions, single exhibits and replicas.')
add('Devotional medal',[
('Saint Joseph\'s medal','1971','Sacramental marking the 100th anniversary of Saint Joseph as patron of the Church.'),
('Holy Face medal','1958','Medal approved by Pius XII with the Holy Face devotion.'),
],W+'Catholic_devotions','Catholic devotions article read to 100,000 of 108,514 characters: Covers 4 medals. Saint Christopher medals are described on the Saint Christopher page without dates and are not added. No list of devotional medals was found in two searches.')
json.dump(d,open(R+'work/GAP_F4/t.json','w'),ensure_ascii=False,indent=1); os.replace(R+'work/GAP_F4/t.json',R+'out/F4.json')
