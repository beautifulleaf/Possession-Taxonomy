import json,os
R='/home/user/Possession-Taxonomy/rebuild/'
d=json.load(open(R+'out/F4.json'))
W='https://en.wikipedia.org/wiki/'
K={k['n']:k for dp in d['depts'] for sh in dp['s'] for k in sh['k']}
def add(kind,rows,src,sel,repl=None):
    k=K[kind]; have={e['n'].lower() for e in k['x']}
    for n,y,desc in rows:
        if n.lower() in have: continue
        k['x'].append({'n':n,'a':'','d':desc,'mk':'','y':y,'s':src,'dt':'','v':[]})
    if repl: k['sel']=k['sel'].replace(*repl)
    k['sel']=k['sel'].rstrip()+' '+sel
add('Advent wreath',[
('Modern Advent wreath','','Smaller four- or five-candle wreath that German Protestant churches developed from Wichern\'s; it may have a white Christ candle.'),
('Advent crown','1964','Home-made wreath of coathangers and tinsel shown on Blue Peter; baubles later replaced candles.'),
('Eastern Orthodox six-candle wreath','','Six coloured candles for the six weeks of the Orthodox Advent and Christmas period.'),
],W+'Advent_wreath','Advent wreath read to 100,000 of 113,506 characters: Covers 4 forms; colour and candle-count variants are versions of the modern wreath.')
add('Ketubah',[
('Venetian illuminated ketubah','1750','Illuminated marriage contract from Venice.'),
('Livorno decorated ketubah','1698','Decorated marriage contract from Livorno.'),
('Sephardic ketubah','','Records the family\'s actual contributions to the new household and the divorce settlement.'),
('Ashkenazi ketubah','','Uses set amounts for all weddings rather than negotiated sums.'),
('Conservative ketubah','modern','Adds the Lieberman clause sending divorce to a beth din.'),
('Ketubah de\'irkesa','','Replacement ketubah written when the original is lost.'),
],W+'Ketubah','Ketubah article read: Covers 8 styles; Iraqi and Ukrainian examples carry no detail, and ancient contracts (Maresha, Babatha) and Geniza finds are documents, not styles.')
add('Hanukkah lamp',[('North Macedonian silver hanukkiah','','Silver Hanukkah lamp from North Macedonia.')],W+'Hanukkah_menorah','Hanukkah menorah article re-read: Covers 6 of 17 rows; the rest are single museum pieces, public monuments, a digital menorah and novelty items.')
K['Calligraphy wall panel']['sel']+=' Islamic calligraphy re-read to 100,000 of 184,335 characters: hilye is the only wall object; the tughra is a monogram on documents.'
# fix wording
s=K['Devotional statue']['sel']; K['Devotional statue']['sel']=s.replace('Complete: 8 of 8 regional traditions it names (Santo, Val Gardena and Oberammergau from earlier passes are named in other articles).','Complete: 5 of 5 regional traditions it names; Santo, Val Gardena and Oberammergau come from earlier passes.')
s=K['Oil lamp for worship']['sel']; K['Oil lamp for worship']['sel']=s.replace('Covers 11 of the 23 lamps named','Covers 11 of the 22 lamps named')
json.dump(d,open(R+'work/GAP_F4/t.json','w'),ensure_ascii=False,indent=1); os.replace(R+'work/GAP_F4/t.json',R+'out/F4.json')
