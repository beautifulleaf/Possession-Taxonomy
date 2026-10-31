import json,re
P='/home/user/Possession-Taxonomy/rebuild/out/H1.json'
d=json.load(open(P))
W='https://en.wikipedia.org/wiki/'
# n -> (own, tier, own_y, srcpage)
O={
 'Pechoin':('Shanghai Pehchaolin Daily Chemical Co Ltd','National champion','','Pechoin'),
 'Cellina':('Shen Hsiang Tang','Independent','','Cellina'),
 'Missha':('ABLE C&C Co., Ltd.','Independent','','Missha'),
 'Creme 21':('Emami','Independent','','Creme_21'),
 'Roger & Gallet':('Impala SAS','Independent','2020','Roger_%26_Gallet'),
 'Sebamed':('Sebapharma GmbH & Co. KG','Independent','','Sebamed'),
 'Tropic Skincare':('Susie Ma','Independent','','Tropic_Skincare'),
 'Ahava':('Fosun International','Independent','2015','Ahava'),
 'Premier Dead Sea':('Hadan Group','Independent','','Premier_Dead_Sea'),
 'Sol de Janeiro':("Groupe L'Occitane",'Independent','','Sol_de_Janeiro'),
 'Carmex':('Carma Laboratories, Inc.','Independent','','Carmex'),
 'ChapStick':('Evermark','Independent','','ChapStick'),
 'Morphe':('Forma Brands','Independent','','Morphe_Cosmetics'),
 "Carol's Daughter":("L'Oréal",'Global group','2014',"Carol%27s_Daughter"),
 'Meril':('Square Toiletries','Independent','','Meril'),
 'Pert Plus':('Sodalis USA','Independent','','Pert_Plus'),
 'Prell':("Scott's Liquid Gold-Inc.",'Independent','','Prell'),
 'Psssssst':('Woodridge Labs','Independent','','Psssssst'),
 'Selsun Blue':('Opella','Independent','','Selsun_Blue'),
 'Timotei':('Unilever','Global group','','Timotei'),
 'White Rain':('International Wholesale','Independent','','White_Rain'),
 'Barbasol':('Perio, Inc.','Independent','','Barbasol'),
 'Mäurer & Wirtz':('Dalli Group','Independent','1990','M%C3%A4urer_%26_Wirtz'),
 'Proraso':('Ludovico Martelli srl','Independent','','Proraso'),
 'Stomatol':('Cederroth AB','Independent','1985','Stomatol'),
 'Fels-Naptha':('Summit Brands','Independent','','Fels-Naptha'),
 'Fenjal':('Fit GmbH','Independent','2016','Fenjal'),
 'Mr. Bubble':('The Village Company','Independent','','Mr._Bubble'),
 'Right Guard':('Thriving Brands LLC','Independent','2021','Right_Guard'),
 'Swarfega':('Deb Limited','Independent','','Swarfega'),
 "Dr. Bronner's":('the Bronner family','Independent','',"Dr._Bronner%27s"),
}
EM='https://www.euromonitor.com/'
def gname(dept,own,tier):
    skin=dept in('Skincare','Make-up')
    if tier=='Global group': return own if skin else 'Global group: '+own
    if tier=='Independent': return 'Independents' if skin else 'Independents and national champions'
    return 'National champions' if skin else 'Independents and national champions'
ch=[];ad=[]
NEW={'Skincare':[('Mistine','Better Way (Thailand)','Thailand','Highlighted in the Euromonitor 2025 Thailand skin-care summary.',EM+'beauty-and-personal-care-in-thailand/report')],
 'Make-up':[('Karmarts','Karmarts','Thailand','Named in the Euromonitor 2025 Thailand colour-cosmetics summary as expanding its influence.',EM+'beauty-and-personal-care-in-thailand/report'),
            ('Srichand','Srichand','Thailand','Highlighted in the Euromonitor 2025 Thailand colour-cosmetics summary.',EM+'beauty-and-personal-care-in-thailand/report'),
            ('La Glace','La Glace','Thailand','Highlighted in the Euromonitor 2025 Thailand colour-cosmetics summary.',EM+'beauty-and-personal-care-in-thailand/report'),
            ('Misr Cosmetics','Misr Cosmetics','Egypt','Joint leader with L\'Oréal in Egyptian colour cosmetics in 2025 (Euromonitor summary).',EM+'beauty-and-personal-care-in-egypt/report')],
 'Hair':[('Norshek','Norshek','Egypt','Named as a leader in Egyptian hair care in 2025 (Euromonitor summary).',EM+'beauty-and-personal-care-in-egypt/report'),
         ('Nouvique Egypt','Nouvique Egypt','Egypt','Named as a leader in Egyptian hair care in 2025 (Euromonitor summary).',EM+'beauty-and-personal-care-in-egypt/report')]}
for dp in d['depts']:
  for s in dp['s']:
    for k in s['k']:
      x=k.get('x') or []
      if len(x)<=20: continue
      for e in x:
        o=O.get(e['n'])
        if o and not e.get('own'):
          own,tier,oy,pg=o
          e['own']=own;e['tier']=tier
          if oy:e['own_y']=oy
          e['g']=gname(dp['n'],own,tier)
          src=W+pg
          e['d']=e.get('d','').rstrip('.')+'. Owner stated on the Wikipedia page for '+e['n']+'.'
          if not str(e.get('s','')).startswith('http'): e['s']=src
          ch.append((dp['n'],e['n']))
      for nm,own,cty,dd,src in NEW.get(dp['n'],[]):
        if not any(z['n'].lower()==nm.lower() for z in x):
          x.append({'n':nm,'a':'','d':dd,'y':'','s':src,'v':[],'own':own,'tier':'National champion','cty':cty,'g':'National champions' if dp['n'] in('Skincare','Make-up') else 'Independents and national champions'}); ad.append((dp['n'],nm))
      k['sel']=k['sel'].rstrip()+' Round 2 (2026-10-31): owners read from Wikipedia introductions where stated; markets added from Euromonitor country summaries (Thailand, Egypt).' if 'Round 2' not in k['sel'] else k['sel']
def R(m,who,share,yr,url,note): return {'mkt':m,'who':who,'share':share,'yr':yr,'s':EM+url+'/report','note':note}
sk=[R('US skin care','L\'Oréal USA Inc','18 %',2025,'skin-care-in-the-us','value share; up from 12 % in 2020; market described as highly fragmented'),
 R('UK skin care',"L'Oréal (UK) Ltd",'15 %',2025,'skin-care-in-the-united-kingdom','value share'),
 R('UK skin care','Boots UK Ltd','9 %',2025,'skin-care-in-the-united-kingdom','value share'),
 R('UK skin care','Estée Lauder Cosmetics Ltd','8 %',2025,'skin-care-in-the-united-kingdom','value share'),
 R('German skin care','L\'Oréal Deutschland GmbH','16 %',2025,'skin-care-in-germany','share as the page states'),
 R('German skin care','Beiersdorf AG','15 %',2025,'skin-care-in-germany','share as the page states'),
 R('French skin care','Cosmétique Active International','15 %',2025,'skin-care-in-france','up from 9 % in 2020'),
 R('French skin care','L\'Oréal SA','8 %',2025,'skin-care-in-france','share as the page states'),
 R('French skin care','Beiersdorf (France) SA','8 %',2025,'skin-care-in-france','share as the page states'),
 R('Japan skin care','Shiseido Co Ltd','13 %',2025,'skin-care-in-japan','top three; share as the page states'),
 R('Japan skin care','Kosé Corp','12 %',2025,'skin-care-in-japan','top three'),
 R('Japan skin care','Kao Corp','7 %',2025,'skin-care-in-japan','top three'),
 R('French mass beauty and personal care','Gemey Maybelline Garnier SNC','12 %',2025,'mass-beauty-and-personal-care-in-france','retail value share; all mass beauty, not skin care alone'),
 R('Thai mass beauty and personal care','Unilever Thai Holdings','10 %',2025,'mass-beauty-and-personal-care-in-thailand','14 % in 2020; all mass beauty'),
 R('Thai mass beauty and personal care','L\'Oréal Thailand','9 %',2025,'mass-beauty-and-personal-care-in-thailand','8 % in 2020'),
 R('Thai mass beauty and personal care','Beiersdorf Thailand','7 %',2025,'mass-beauty-and-personal-care-in-thailand','stable since 2020'),
 R('Thai beauty and personal care','Thailand market','THB 270 billion',2025,'beauty-and-personal-care-in-thailand','retail sales, growth 6 %; L\'Oréal Thailand leads skin care'),
 R('Turkish mass beauty and personal care','L\'Oréal Turkiye Kozmetik San ve Tic AS','11 %',2025,'mass-beauty-and-personal-care-in-turkiye','10 % in 2020; value or volume not specified'),
 R('Mexican mass beauty and personal care','Unilever de México S de RL de CV','14 %',2025,'mass-beauty-and-personal-care-in-mexico','value share'),
 R('Mexican premium beauty and personal care','Frabel SA de CV','25 %',2025,'premium-beauty-and-personal-care-in-mexico','value share; 19 % in 2020; Frabel is L\'Oréal\'s Mexican company'),
 R('Saudi skin care','L\'Oréal; Al Naghi Co','leaders; no share stated',2025,'beauty-and-personal-care-in-saudi-arabia','Euromonitor headline for skin care'),
 R('Egyptian beauty and personal care','Unilever; Procter & Gamble','lead; no share stated',2025,'beauty-and-personal-care-in-egypt','L\'Oréal and Misr Cosmetics lead colour cosmetics'),
 R('South African beauty and personal care','Unilever; Beiersdorf','lead; no share stated',2025,'beauty-and-personal-care-in-south-africa','Euromonitor headline'),
 R('Argentine beauty and personal care','Natura Argentina; Unilever','lead; no share stated',2025,'beauty-and-personal-care-in-argentina','Euromonitor headline; Cdimex growing')]
for dp in d['depts']:
  if dp['n']=='Skincare':
    for r in sk:
      if r not in dp['ms']: dp['ms'].append(r)
    dp['msum']=dp['msum'].replace('No fetched page gives a current skin care share for the United States, the United Kingdom, Germany or France.','L\'Oréal leads skin care in the United States (18 %), United Kingdom (15 %) and Germany (16 %, with Beiersdorf at 15 %); in France Cosmétique Active International leads (15 %); in Japan Shiseido leads (13 %) (all 2025).')
json.dump(d,open('H1.r2.json','w'),ensure_ascii=False)
print(len(ch),ad)
