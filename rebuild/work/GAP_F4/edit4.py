import json,os
R='/home/user/Possession-Taxonomy/rebuild/'
d=json.load(open(R+'out/F4.json'))
K={k['n']:k for dp in d['depts'] for sh in dp['s'] for k in sh['k']}
def sec(kind,groups,default):
    k=K[kind]; k['xg']=list(groups)+[default]
    for e in k['x']:
        e['g']=default
        for g,names in groups.items():
            if any(e['n'].lower().startswith(n.lower()) for n in names): e['g']=g
sec('Rosary',{'Dominican rosary and its forms':['Dominican','Franciscan','Servite','Irish','Pater','Bridgettine']},'Chaplets')
sec('Scapular',{'Before 1800':['Scapular of the Most Blessed','Scapular of Our Lady of Ransom','Brown','Scapular of the Seven Sorrows','Blue','Black Scapular']},'1800 onwards or undated')
sec('Evil-eye charm',{'Mediterranean and Europe':['Nazar','Hamsa','Cornicello','Cimaruta','Lunula','Fascinus','Muska','Albanian','Dordolec','Red string'],'Africa':['Kitab','Gris-gris','Cowrie'],'Americas and Caribbean':['Azabache','Jumbie'],'Asia':['Drishti',"Ta'awiz",'Assyrian']},'Other')
sec('Ofuda',{'Ise talismans':['Jingu','Oharai','Kenharai','Kakuharai','Daikakuharai'],'Household deity talismans':['Kamadogami','Sanbo','Ujigami']},'Shrine and temple talismans')
sec('Ritual incense',{'Sticks, cones and coils':['Japanese senko','Indian agarbatti','Incense coil','Incense cone','Cored','Dhoop','Dragon','Spiral'],'Paste and resin':['Bakhoor','Neriko','Moskolibano','Athonite','Ketoret']},'Other forms')
sec('Incense burner',{'China':['Hill','Scenting','Shoulu','Xunlu','Tiangong'],'Japan':['Egoro','Koro'],'Islamic world and Africa':['Mabkhara','Dabqaad'],'Americas and South Asia':['Incensario','Dhunachi']},'Europe and ancient Egypt')
sec('Crucifix & devotional cross',{'Worn':['Pectoral','Cross necklace','Wolf']},'Church and devotional use')
json.dump(d,open(R+'work/GAP_F4/t.json','w'),ensure_ascii=False,indent=1); os.replace(R+'work/GAP_F4/t.json',R+'out/F4.json')
for n in ['Rosary','Scapular','Evil-eye charm','Ofuda','Ritual incense','Incense burner','Crucifix & devotional cross']:
    from collections import Counter; print(n,Counter(e['g'] for e in K[n]['x']))
