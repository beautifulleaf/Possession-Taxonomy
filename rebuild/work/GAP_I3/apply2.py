import json,os
P='/home/user/Possession-Taxonomy/rebuild/out/I3.json'
d=json.load(open(P)); K={k['n']:k for dp in d['depts'] for s in dp['s'] for k in s['k']}
def setg(kind,m,default):
    for e in K[kind]['x']: e['g']=m.get(e['n'],default)
K['AI assistant subscription']['sel']="Covers 6 of the 7 assistants in the Similarweb share table (Momentic) and the Wikipedia articles for each; DeepSeek is left out because no paid consumer plan was fetched. Plan names carried over from the earlier pass."
K['Mobile phone plan']['sel']="Covers the consumer brands of the 25 largest operators in Wikipedia's List of mobile network operators (45 entries with the national operators and MVNOs kept from the earlier pass); the list names several hundred operators, and the smaller ones are not added. Operator groups (Axiata, VEON, América Móvil) sell under other brands and appear only in the market facts."
us={'Spectrum Internet','Xfinity Internet','AT&T Fiber','Fios Home Internet','Optimum','Frontier Fiber Internet'}
uk={'BT Broadband','Sky Broadband','Virgin Media','Zen Internet','Plusnet','Hyperoptic'}
fr={'Freebox Ultra','Orange','SFR'}
setg('Broadband plan',{**{n:'United States' for n in us},**{n:'United Kingdom' for n in uk},**{n:'France' for n in fr},'MagentaZuhause':'Germany'},'Other')
K['Broadband plan']['xg']='by home country'
K['Broadband plan']['sel']="No complete list exists (broadband sellers number in the thousands); follows the page cited for this kind (https://www.xfinity.com/national/) and the operators of the largest markets."
for e in K['Hotel loyalty status']['x']:
    e['g']='Casino resorts' if e['n'] in('M life Rewards','Total Rewards') else 'Associations and booking sites' if e['n'] in('Preferred Hotels & Resorts','Leading Hotels of the World','Hotels.com reward scheme') else 'Hotel groups'
K['Hotel loyalty status']['xg']='by who runs it'
for e in K['Meal kit and menu plan']['x']:
    e['g']=e.get('cty') or 'Country not given'
K['Meal kit and menu plan']['xg']='by country where the page gives it'
own={'ExpressVPN':'Kape Technologies','Private Internet Access':'Kape Technologies'}
oth={'Avast SecureLine','Hotspot Shield','IPVanish','NordVPN','NymVPN','TunnelBear'}
for e in K['VPN service']['x']:
    e['g']='Owned by Kape Technologies' if e['n'] in own else 'Other owner named by the page' if e['n'] in oth else 'No owner named'
K['VPN service']['xg']='by owner the page names'
for e in K['Antivirus and security suite']['x']:
    e['g']='Gen Digital brands' if e['n'] in('Norton','Avast','AVG','Avira') else 'Other vendors'
K['Antivirus and security suite']['xg']='by owner group'
plat={'WhatsApp','Messenger','FaceTime','Zoom Workplace','Discord','Google Chat','Skype','Snapchat'}
reg={'WeChat','QQ','Line','KakaoTalk','Viber'}
for e in K['Messaging and video calls']['x']:
    e['g']='Run by a platform company' if e['n'] in plat else 'Regional apps' if e['n'] in reg else 'Independent and privacy-focused'
K['Messaging and video calls']['xg']='by who runs it'
tmp=P+'.tmp'; json.dump(d,open(tmp,'w'),ensure_ascii=False,indent=1); os.replace(tmp,P)
