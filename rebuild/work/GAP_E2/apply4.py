import json,os
P='/home/user/Possession-Taxonomy/rebuild/out/'
d=json.load(open(P+'E2.json')); br=json.load(open(P+'E2_brands.json'))
reg={b['n']:b for b in br['b']}
def find(name):
    for dpt in d['depts']:
        for s in dpt['s']:
            for kk in s['k']:
                if kk['n']==name: return kk
def dept(name):
    return [x for x in d['depts'] if x['n']==name][0]
def addents(kind,mk,names,src,what,extra=None,vers=None):
    k=find(kind); have={e['n'].lower() for e in k['x']}; n=0
    for nm in names:
        full=nm if nm.lower().startswith(mk.lower()) else mk+' '+nm
        if full.lower() in have: continue
        e={'n':full,'a':'','d':what,'mk':mk,'y':'','s':src,'v':[{'n':v,'mk':mk,'y':'','d':''} for v in (vers or {}).get(nm,[])],'g':mk}
        if reg.get(mk,{}).get('c'): e['cty']=reg[mk]['c']
        if extra: e.update(extra)
        k['x'].append(e); have.add(full.lower()); n+=1
    return n
tot={}
# fly rods
T='https://www.tridentflyfishing.com/collections/'
tot['sage']=addents('Fly rod','Sage',"Foundation,Arrow,R8 Core,Maverick,Payload,Salt R8,Power R8,Dart,ESN HD,Classic R8,Spey R8,Sonic Spey & Switch,Trout Spey G5,Trout Spey HD,Signal,Sonic,Igniter,Method,Trout LL,Sense,ESN,X,Salt HD,Accel,Pulse,Little One,Mod,Bolt,Motive,One,Salt".split(','),T+'sage-fly-rods','Sage fly rod series listed on the retailer collection page.')
tot['loomis']=addents('Fly rod','G. Loomis',['Asquith','NRX+','NRX','IMX-Pro V2','IMX-Pro','PRO4x'],T+'g-loomis-fly-rods','G. Loomis fly rod series listed on the retailer collection page.')
tot['scott']=addents('Fly rod','Scott',['Centric','Sector','GT','F Series','Wave','Session','Swing','SC','G Series'],T+'scott-fly-rods','Scott fly rod series listed on the retailer collection page.')
tot['winston']=addents('Fly rod','Winston',['Air 2','Air 2 Max','Pure 2','Pure','Tom Morgan Favorite','Air TH Spey','Air 2 Reach','Air 2 TH Spey','Bamboo','Microspey Air 2','Air Salt','Saltwater Air','Air','Alpha Plus','Nimbus','Kairos','Nexus','Boron III','Boron III Plus','Boron III X','Boron III TH','Boron III LS'],T+'winston-fly-rods','Winston fly rod series listed on the retailer collection page.')
tot['orvis']=addents('Fly rod','Orvis',['Helios D','Helios F','Recon','Clearwater','Superfine','Encounter','Mission','Penns Creek Bamboo','1856 Bamboo','PractiCaster'],T+'orvis-fly-rods','Orvis fly rod series listed on the retailer collection page.',extra={'own':'Perkins family','tier':'Independent','own_y':'1965'})
# Daiwa / Penn
tot['daiwa']=addents('Spinning rod','Daiwa',"Aird X,Tatula XT,Steez Travel,Tatula Elite,Beam X Glass,Ardito Jitte,Ardito Premium,Ardito-TR,Blackline Inshore,DXB,Fuego,ISLA Inshore,Kage B,Power Scope,Presso Air AGS,Procyon,Procyon Inshore,Proteus Inshore,Saltiga Inshore Travel,Saltist Westcoast,Steez,Steez AGS,Steez Real Control,Steez Solid Tip,Tatula Cork,Tatula Elite AGS,TD-SOL Inshore,Zillion".split(','),'https://www.tacklewarehouse.com/Daiwa_Spinning_Rods/catpage-RDSDAIWA.html','Daiwa spinning rod series listed on the retailer category page.',extra={'own':'Globeride, Inc.','tier':'Independent'})
tot['penn']=addents('Sea and surf rod','Penn',['Prevail','Slammer','Regiment','Ocean Assassin','Militia'],'https://compleatanglernedlands.com.au/collections/penn-rods','Penn rod series listed on the retailer collection page.')
# skis
vs='https://www.powder7.com/ski-blog/volkl-skis-preview-2025/'
ve={'own':'Elevate Outdoor Collective (Kohlberg & Company)','tier':'Independent','own_y':'2017','cty':'Germany'}
tot['volkl']=addents('Alpine ski','Völkl',['Secret','Peregrine','Racetiger','Flair','Revolt'],vs,'Völkl ski line named in the 2025 brand preview.',extra=ve)
k=find('Alpine ski')
for e in k['x']:
    if e['n']=='Völkl Mantra' and not e['v']:
        e['v']=[{'n':n,'mk':'Völkl','y':'','d':d_} for n,d_ in (('M7','new model in the 2025 preview'),('88','formerly Kendo 88'),('108','formerly Katana 108'))]
    if e['n']=='Völkl Blaze 94' and not e['v']:
        e['v']=[{'n':'Blaze '+w,'mk':'Völkl','y':'','d':''} for w in ('86','104','114')]
tot['head']=addents('Alpine ski','Head',['Kore','Oblivion','Joy'],'https://www.powder7.com/ski-blog/head-skis-preview-2025/','Head ski line named in the 2025 brand preview.',extra={'cty':'Austria','tier':'Independent'})
tk=find('Touring ski')
if not any(e['n']=='Head Crux' for e in tk['x']):
    tk['x'].append({'n':'Head Crux','a':'','d':'New Head touring line in the 2025 preview, in Pro and standard versions.','mk':'Head','y':'2025','s':'https://www.powder7.com/ski-blog/head-skis-preview-2025/','v':[{'n':'Crux %s%s'%(w,p),'mk':'Head','y':'','d':''} for w in ('105','99','93','87','81') for p in (' Pro','') if not (w=='105' and p=='')],'g':'Head','cty':'Austria','tier':'Independent'})
    tot['crux']=1
jb={'Tweaker':[],'Ultra Mountain Twin':[],'Aviator 2.0':[],'Ultralight Project X':[],'Airheart 2.0':[],'Twin Sister':[],'Dream Weaver':['Split'],'Mind Expander':['Mind Expander Twin','Ultra Mind Expander','Mind Expander Split','Mini Mind Expander',"Women's Mind Expander"],
'Flagship':['Ultra Flagship',"Women's Flagship",'Youth Flagship'],'Stratos':["Women's Stratos",'Stratos Split','Ultra Stratos Split'],'Storm Wolf':[],'Freecarver':['Freecarver 6000s','Freecarver 9000s'],
'Hovercraft 2.0':['Hovercraft 2.0 Split','Ultralight Hovercraft Split'],'Storm Chaser':['Storm Chaser Split'],'Solution':['Ultra Solution',"Women's Solution",'Youth Solution'],'Prodigy':['Ultra Prodigy'],'Ultralight Butterfly Split':[]}
tot['jones']=addents('Snowboard','Jones',list(jb),'https://snowboardingprofiles.com/2024-jones-snowboards-overview','Jones snowboard model listed in the 2024 Jones overview.',extra={'cty':'United States'},vers=jb)
for e in find('Snowboard')['x']:
    if e['n']=='Jones Mountain Twin' and not e['v']: e['v']=[{'n':'Mountain Twin Split','mk':'Jones','y':'','d':''}]
    if e['n']=='Jones Frontier 2.0' and not e['v']: e['v']=[{'n':'Frontier Split','mk':'Jones','y':'','d':''}]
# coverage sentences
def sel(kind,t):
    k=find(kind); k['sel']=k['sel'].rstrip()+' '+t
sel('Fly rod','Series added from retailer collection pages for Orvis, Sage, G. Loomis, Scott and Winston (Trident Fly Fishing); no maker range page was fetched, and discontinued series appear where the retailer lists them. No complete list exists.')
sel('Spinning rod','Daiwa series added from the Tackle Warehouse category page; Daiwa and Penn official range pages were not fetched.')
sel('Sea and surf rod','Penn rod series added from one Australian retailer collection page.')
sel('Alpine ski','Völkl and Head lines added from the Powder7 2025 brand previews; the Head preview names no models for Supershape, Kore or Oblivion. No complete list exists.')
sel('Touring ski','Head Crux line added from the Powder7 2025 Head preview.')
sel('Snowboard','Jones models added from the 2024 Jones overview on Snowboarding Profiles; splitboards are versions of their solid board. No complete list exists.')
# owners from extracts
OW={ # mk:(cty,own,tier,own_y)
'Gin Gliders':('South Korea',None,None,None),'Kookaburra':('Australia',None,None,None),'Srixon':('Japan','SRI Sports Limited (Sumitomo Rubber Industries)','Global group',None),
'Bauer Hockey':('Canada','Peak Achievement Athletics','Global group',None),'Bauer':('Canada','Peak Achievement Athletics','Global group',None),'Fischer':('Austria',None,None,None),'Wills Wing':('United States',None,None,None),'Li-Ning':('China',None,None,None),'Rip Curl':('Australia',None,None,None),
'Yonex':('Japan',None,None,None),'Slazenger':('United Kingdom','Frasers Group plc','Global group','2004'),'Speedo':('United Kingdom','Pentland Group','Independent',None),
'Stiga':('Italy','Castelgarden SpA','Independent','2000'),'Tecnifibre':('France','Lacoste (80% via Major Sports)','Independent','2017'),'Petzl':('France',None,None,None),'Prince':('United States',None,None,None),
'Rottefella':('Norway',None,None,None),'Trangia':('Sweden',None,None,None),'CamelBak':('United States',None,None,None),'BioLite':('United States',None,None,None),'Brunswick':('United States',None,None,None),
'Suunto':('Finland','Liesheng','Independent','2022'),'Aqualung':('France','Head Group','Independent','2025'),'Blizzard':('Austria','Tecnica Group','Independent',None),
'Discraft':('Canada',None,None,None),'Gray-Nicolls':('United Kingdom','Grays International','Independent',None),'Gunn & Moore':('United Kingdom','Unicorn Group','Independent','1968'),
'Independent Truck Company':('United States','NHS, Inc.','Independent',None),'Mikasa':('Japan',None,None,None),'Powell Peralta':('United States',None,None,None),'Riedell':('United States',None,None,None),
'Wahoo Fitness':('United States',None,None,None),'Wham-O':('United States',None,None,None),'Beuchat':('France','Margnat family','Independent','2002'),'Body Glove':('United States',None,None,None),
'Lowe Alpine':('United States','Rab','Independent',None),'Metolius':('United States',None,None,None),'Moyes Delta Gliders':('Australia',None,None,None),'Penny Skateboards':('Australia',None,None,None),
'Marker':('Germany','Kohlberg & Company','Independent','2017'),'Tippmann':('United States','Summit Partners','Independent','2004'),'Winmau':('United Kingdom','Nodor','Independent','2002'),
'Babolat':('France',None,None,None),'O\'Neill':('United States','Sisco Textiles','Independent',None),'Minelab':('Australia','Codan','Independent','2008'),'Edelrid':('Germany','VAUDE','Independent','2006'),
'Schwinn Fitness':('United States',None,None,None),'Hoyt':('United States','Jas. D. Easton, Inc.','Independent',None),'Bear Archery':('United States','Escalade Sports','Independent',None),
'Hilleberg':(None,None,None,None),'Mammut':(None,None,None,None),
}
n=0
for dpt in d['depts']:
  for s in dpt['s']:
    for kk in s['k']:
      for e in kk.get('x',[]):
        f=OW.get(e.get('mk'))
        if f:
          for key,val in zip(('cty','own','tier','own_y'),f):
            if val and not e.get(key): e[key]=val; n+=1
for mk,f in OW.items():
  b=reg.get(mk)
  if b:
    for key,val in zip(('c','own','tier'),f[:3]):
      if val and not b.get(key): b[key]=val
print(tot,n)
# market panel for Target & precision sports
dp=dept('Target & precision sports')
dp['ms']=[
 {"mkt":"Winmau (darts, dartboards)","who":"Nodor","share":"owner since 2002","yr":2002,"s":"https://en.wikipedia.org/w/api.php?action=query&prop=extracts&exintro=1&titles=Winmau","note":"Winmau, founded in Wales in 1945, was acquired by Nodor in 2002, as the Wikipedia extract states."},
 {"mkt":"Bear Archery","who":"Escalade Sports","share":"owner","yr":None,"s":"https://en.wikipedia.org/w/api.php?action=query&prop=extracts&exintro=1&titles=Bear_Archery","note":"The page names Escalade Sports as owner and gives no year."},
 {"mkt":"Hoyt Archery","who":"Jas. D. Easton, Inc.","share":"owner","yr":None,"s":"https://en.wikipedia.org/w/api.php?action=query&prop=extracts&exintro=1&titles=Hoyt_Archery","note":"The page names Jas. D. Easton, Inc. as owner and gives no year."},
 {"mkt":"Brunswick billiards","who":"Escalade Sports","share":"bought billiards business","yr":2022,"s":"https://en.wikipedia.org/w/api.php?action=query&prop=extracts&exintro=1&titles=Brunswick_Bowling_%26_Billiards","note":"Brunswick sold its bowling equipment to BlueArc Capital Management in 2015 and its billiards business to Escalade Sports in 2022."},
 {"mkt":"Tippmann (paintball markers)","who":"Summit Partners","share":"majority stake","yr":2004,"s":"https://en.wikipedia.org/w/api.php?action=query&prop=extracts&exintro=1&titles=Tippmann","note":"Summit Partners, a private equity firm, bought a majority stake in 2004."},
 {"mkt":"Sporting arms and ammunition ownership","who":"Czechoslovak Group","share":"owner of Federal Premium; Vista Outdoor shooting products (2024)","yr":2024,"s":"https://en.wikipedia.org/w/api.php?action=query&prop=extracts&exintro=1&titles=Vista_Outdoor","note":"Firearms are E4; the shooting-products sale is stated on the Vista Outdoor page."}]
dp['msum']='Target and precision sport equipment is held by a few private owners (Nodor, Escalade Sports, Jas. D. Easton, Summit Partners); the facts below are owners stated on Wikipedia extracts, not market shares. No revenue or share figure was found; bows and firearms are listed under E4.'
t=P+'E2.json.tmp'; json.dump(d,open(t,'w'),ensure_ascii=False,indent=1); os.replace(t,P+'E2.json')
t=P+'E2_brands.json.tmp'; json.dump(br,open(t,'w'),ensure_ascii=False,indent=1); os.replace(t,P+'E2_brands.json')
