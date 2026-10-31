import json,re,sys
sys.path.insert(0,'/home/user/Possession-Taxonomy/rebuild/work/V4_B5_APPL')
from brands_table import B
R='/home/user/Possession-Taxonomy/rebuild/'
st=json.load(open(R+'work/V4_B5_APPL/stage1.json')); D=st['D']; rep=st['report']
W='https://en.wikipedia.org/wiki/'
NAMES=["Kitchen appliances","Coffee","Tea & kettles","Brewing, fermenting & preserving","Food storage & on-the-go","Spare parts"]
ALIAS={'Whirlpool Corporation':'Whirlpool','Samsung Electronics':'Samsung','LG Electronics':'LG','Breville Group':'Breville','Zojirushi Corporation':'Zojirushi','Tiger Corporation':'Tiger','Cuckoo Electronics':'Cuckoo',
'Mazzer (family company)':'Mazzer','Smeg Group S.p.A.':'Smeg','Jura Elektroapparate AG':'Jura','Bamix of Switzerland':'Bamix',"JDE Peet's (Kraft Heinz in North America)":"JDE Peet's",
"Procter & Gamble (brand); small appliances made by De'Longhi under licence":'Procter & Gamble','Midea Group':'Midea Group'}
for d in D.values():
    for s in d['s']:
        for k in s['k']:
            for e in k.get('x',[]):
                if e.get('own') in ALIAS: e['own']=ALIAS[e['own']]
                if e.get('mk')=='Braun': e['d']=e['d']+' Small appliances are made by De\'Longhi under a licence from Procter & Gamble, which owns the brand.' if 'licence' not in e['d'] else e['d']
IC_KINDS={('Brewing, fermenting & preserving'),('Food storage & on-the-go')}
ICON_TE={'Teapot','Tea caddy','Kettle','Soda maker','Water filter jug','Hot water dispenser'}
FORMS={'Yixing teapot','Kyusu','Chawan','Matcha whisk and scoop','Japanese tea caddy','Tetsubin','Samovar','Gaiwan'}
NLX={
'Yixing teapot':'One entry is a classic Yixing teapot shape named in teaware guides; clay and maker are attributes.',
'Kyusu':'One entry is a kyusu tradition named by its kiln town, such as Tokoname or Banko.',
'Chawan':'One entry is a matcha-bowl kiln tradition named by a fetched page, such as Raku, Hagi, Karatsu or Shino.',
'Matcha whisk and scoop':'One entry is a named whisk tradition, such as the Takayama chasen.',
'Japanese tea caddy':'One entry is a named caddy form or maker, such as the natsume, the chaire shapes or Kaikado.',
'Tetsubin':'One entry is a regional tradition of cast-iron kettle, such as Nambu.',
'Samovar':'One entry is a regional samovar tradition.',
}
SELX={
'Yixing teapot':'Ten shapes named by two teaware guides (Tealao and Moychay); neither is a complete canon and the Wikipedia article on Yixing teapots names none, so the list stays at the shapes both guides print.',
'Kyusu':'Two kiln traditions named by teaware pages (Wikipedia Tokoname ware; a Banko ware retailer page); no complete list of kyusu kilns was fetched.',
'Chawan':'Kiln traditions named on the Wikipedia pages for Raku, Hagi, Karatsu and Shino ware; Japanese tea utensils page lists chawan only as a form.',
'Matcha whisk and scoop':'Takayama chasen from the Kougeihin craft page; no complete list of whisk traditions was fetched.',
'Japanese tea caddy':'Natsume, chaire and chazutsu forms from the Wikipedia pages Chaki and Kaikado; the Japanese tea utensils page lists chaki, natsume and chaire as forms.',
'Tetsubin':'Nambu tradition from the JapanObjects feature on Nambu ironware; no complete list of tetsubin regions was fetched.',
'Samovar':'Tula, Borujerd and Kashmiri traditions named in the Wikipedia article on the samovar.',
}
def cov_lines(n,ref): return f"Covers {n} {'line' if n==1 else 'lines'} named by the cited pages; no complete reference list of this kind exists, so this is not a total."
def cov_icon(n): return f"Covers {n} {'entry' if n==1 else 'entries'}: the origin products and design-collection landmarks that the cited pages name; commodity kinds hold no further brands."
for dn in NAMES:
    d=D[dn]
    for s in d['s']:
        for k in s['k']:
            xs=k.get('x') or []
            if not xs:
                k.pop('x',None); continue
            n=len(xs)
            if k['n'] in NLX:
                k['nl']=NLX[k['n']]; k['sel']=SELX[k['n']]+' '+f"Covers {n} of the forms those pages name; the rest of the tradition is not listed on the fetched pages."; k['xg']='by country of origin'
            elif dn in IC_KINDS or (dn=='Tea & kettles' and k['n'] in ICON_TE):
                k['nl']='One entry is the first product of its kind or a landmark of the kind, under the icon rule for commodity kinds.'
                k['sel']='Icon rule in BRIEF.md: one origin entry as a fetched page states it, plus design-canon landmarks confirmed on a fetched page; popularity is never a reason. Source: '+k['s']+'. '+cov_icon(n)
                k['xg']='by country of origin'
            else:
                k['nl']='One entry is a named product line or model family sold under one maker\'s name; generations and size variants are versions.'
                k['sel']='Follows '+k['s']+' and the entry pages cited on each line; every line those pages name for this kind is included, plus loose models folded in from the earlier pass. '+cov_lines(n,'')
                k['xg']='by home country of the maker'
# ---- department fields
KA=D['Kitchen appliances']; CO=D['Coffee']
H=W+'Haier'
KA['msum']=("Large appliances sit with a few groups: Euromonitor ranked Haier first by sales volume in 2024, and the Electrolux page calls Electrolux the second-largest maker by units after Whirlpool. "
 "Portfolios on the cited pages: Whirlpool (KitchenAid 1986, Maytag, Jenn-Air and Amana 2006, Indesit 2014); Haier (Fisher & Paykel 2012, GE Appliances 2016, Candy 2018, Aqua, Hoover Europe, Casarte, Leader); "
 "BSH (Bosch, Siemens, Gaggenau, Neff, Thermador, Balay, Constructa, Pitsos, Profilo); Electrolux (AEG, Frigidaire, Zanussi 1984); Midea (Toshiba appliances and Eureka 2016, Little Swan 2008). "
 "Small appliances split between Groupe SEB (Tefal, Moulinex, Rowenta, Krups, WMF, All-Clad 2004), De'Longhi (Kenwood 2001, Braun licence 2012), SharkNinja (Shark, Ninja), Versuni (Philips, Saeco, Gaggia, Senseo) and Breville (Sage, Baratza, Lelit). "
 "Only figures that fetched pages state are listed; no current share by brand for small appliances could be sourced.")
def ms(mkt,who,share,yr,s,note): return {'mkt':mkt,'who':who,'share':share,'yr':yr,'s':s,'note':note}
KA['ms']=[
 ms('Global large household appliances, retail volume','Haier','10.3 %',2017,'https://www.kbbreview.com/?p=7868','Euromonitor figure in an article dated 9 February 2017, Haier\'s eighth year at No. 1'),
 ms('Global major appliances, sales volume','Haier','No. 1',2024,'https://retailtimes.co.uk/haier-named-no-1-global-major-appliances-brand-for-the-16th-year/','sixteenth consecutive year per Euromonitor; the article gives no percentage'),
 ms('Global refrigerators','Haier','6.3 %',2009,H,'share of sales; Haier passed Whirlpool as fourth-largest refrigerator producer'),
 ms('US dishwashers','General Electric','40 %',1991,W+'Home_appliance','market split cited from the Encyclopedia of American Industries (1994)'),
 ms('US dishwashers','Whirlpool','31 %',1991,W+'Home_appliance','same split'),
 ms('US dishwashers','Electrolux','20 %',1991,W+'Home_appliance','same split'),
 ms('US dishwashers','Maytag','7 %',1991,W+'Home_appliance','same split'),
 ms('US dishwashers','Thermador','2 %',1991,W+'Home_appliance','same split'),
 ms("China's ten largest appliance makers, sales",'Midea, Haier and Gree together','80 %',2020,W+'Midea_Group','share of sales among the top ten'),
 ms('Group revenue','Haier','about US$35 billion',2022,W+'Midea_Group','estimate on the Midea page that Haier was the largest home-appliance company by revenue'),
 ms('Group revenue','Midea Group','CN¥458.5 billion',2025,W+'Midea_Group','group revenue, not category share'),
 ms('Group revenue','Whirlpool Corporation','about US$15.52 billion',2025,W+'Whirlpool_Corporation','net sales'),
 ms('Group revenue','BSH Hausgeräte','€15 billion',2025,W+'BSH_Hausger%C3%A4te','group revenue'),
 ms('Group revenue','Electrolux','134.88 billion kr',2022,W+'Electrolux','revenue'),
 ms('Group revenue','Groupe SEB','€8.0 billion',2023,W+'Groupe_SEB','group revenue, including cookware'),
 ms('Group revenue',"De'Longhi",'€3.16 billion',2022,W+'De%27Longhi','group revenue'),
 ms('Group revenue','SharkNinja','about US$6.4 billion',2025,W+'SharkNinja','group revenue, including Shark floorcare'),
 ms('Group revenue','Versuni','€2.2 billion',2021,W+'Versuni','group revenue'),
 ms('Group revenue','Breville Group','A$1.48 billion',2023,W+'Breville','group revenue'),
 ms('Group revenue','Smeg','€906 million',2021,W+'Smeg_(appliances)','group revenue'),
]
CO['msum']=("Coffee machines are a capsule market led by Nestlé (Nespresso, Dolce Gusto), Keurig Dr Pepper (Keurig) and JDE Peet's (Tassimo outside North America), "
 "with espresso machines and grinders split among Italian, Swiss and specialty makers. Group portfolios: De'Longhi (Kenwood, Braun licence), Versuni (Saeco, Gaggia, Philips), Breville (Sage, Baratza, Lelit). Only fetched figures are listed.")
CO['ms']=[
 ms('US single-serve coffee machines','Nespresso','about 3 %',2013,W+'Nespresso','the year before Vertuo launched in the US'),
 ms('Canadian single-serve coffee machines','Nespresso','4–5 %',2013,W+'Nespresso','market share'),
 ms('European single-serve coffee machines','Nestlé','about 70 %',2013,W+'Nespresso','Nestlé across its capsule systems'),
 ms('Nespresso revenue','Nestlé Nespresso','about CHF 3 billion',2011,W+'Nespresso','revenue, up 20 % that year'),
 ms('Group revenue','Keurig Dr Pepper','US$16.603 billion',2025,W+'Keurig_Dr_Pepper','group revenue including soft drinks'),
 ms('Group revenue','Jura','CHF 579.9 million',2020,W+'Jura_Elektroapparate','company revenue'),
]
# ---- brands and brand_updates
reg={b['n'] for b in json.load(open(R+'out/B5_brands.json'))['b']}
reg_l={n.lower() for n in reg}
used={}
for dn in NAMES:
    for s in D[dn]['s']:
        for k in s['k']:
            for e in k.get('x',[]):
                if e.get('mk'): used.setdefault(e['mk'],[]).append(e)
                if e.get('own') and e['own']!='owner not stated': used.setdefault('OWN:'+e['own'],[]).append(e)
SEG={'Global group':'Mainstream','National champion':'Traditional & regional','Independent':'Specialist','Craft & indie':'Artisan & independent'}
COUNTRY_OWN={'BSH Hausgeräte':('Germany','1967',W+'BSH_Hausger%C3%A4te'),'Groupe SEB':('France','1857',W+'Groupe_SEB'),'Versuni':('Netherlands','',W+'Versuni'),'Nestlé':('Switzerland','',W+'Nespresso'),
 'Keurig Dr Pepper':('United States','',W+'Keurig_Dr_Pepper'),"JDE Peet's":('Netherlands','',W+'Tassimo'),'Newell Brands':('United States','',W+'Tupperware'),'Midea Group':('China','1968',W+'Midea_Group'),
 'Procter & Gamble':('United States','',W+'De%27Longhi'),'Party Products LLC':('United States','',W+'Tupperware'),'Lavazza':('Italy','',W+'Espresso_machine')}
newb=[]; upd={}
LINES={'Whirlpool':['KitchenAid (1986)','Maytag, Jenn-Air, Amana (2006)','Indesit (2014)','Bauknecht (1989)','InSinkErator (2022)'],
'Haier':['GE Appliances (2016)','Fisher & Paykel (2012)','Candy (2018)','Aqua','Hoover (Europe)','Casarte','Leader'],
'Electrolux':['AEG','Frigidaire','Zanussi (1984)'],'Midea Group':['Toshiba home appliances (2016)','Eureka (2016)','Little Swan (2008)','Hualing','MDV'],
'BSH Hausgeräte':['Bosch','Siemens','Gaggenau','Neff','Thermador','Balay','Constructa','Pitsos','Profilo'],
'Groupe SEB':['All-Clad (2004)','Emsa','Krampouz','Krups','Lagostina','Mirro','Moulinex','OBH Nordica','Rowenta','Schaerer','Supor','Tefal / T-fal','WearEver','WMF'],
'Versuni':['Philips (licensed)','Saeco (licensed from Evoca)','Gaggia','Senseo','L\'Or','Preethi','Baristina'],'Nestlé':['Nespresso','Nescafé Dolce Gusto'],
'Keurig Dr Pepper':['Keurig'],"JDE Peet's":['Tassimo'],'Newell Brands':['Mr. Coffee','Crock-Pot'],'Procter & Gamble':['Braun']}
for key,es in used.items():
    if key.startswith('OWN:'):
        n=key[4:]
        if n.lower() in reg_l or n in ('Haier',): 
            continue
        c,f,s=COUNTRY_OWN.get(n,('','',es[0]['s']))
        newb.append({'n':n,'c':c,'f':f,'seg':'Mainstream' if B.get(es[0].get('mk',''),('','',''))[1]=='Global group' else 'Specialist','d':f'Company that owns brands named in the Kitchen appliances, Coffee and storage departments.','lines':LINES.get(n,[]),'eras':[],'sig':[],'sc':[],'rel':[],'s':s})
    else:
        mk=key
        if mk in B:
            own,tier,cty,oy=B[mk]; own=ALIAS.get(own,own)
        else: continue
        if mk in reg: upd[mk]={'own':own,'tier':tier,'c':cty}
        elif mk.lower() not in reg_l:
            newb.append({'n':mk,'c':cty,'f':'','seg':SEG[tier],'d':f'Brand named on the Kitchen appliances, Coffee, Tea or storage pages; owner: {own}.','lines':[e['n'] for e in es][:5],'eras':[],'sig':[mk+' lines'],'sc':[],'rel':[],'s':es[0]['s']})
# add owner-lines to existing register owners
for n,ln in LINES.items():
    if n in reg: upd.setdefault(n,{})['lines']=ln
for n in ('Whirlpool','Haier','Electrolux','Samsung','LG','Bosch','Siemens','Frigidaire','GE Appliances','Fisher & Paykel','Tefal','Kenwood','Braun',"De'Longhi",'SharkNinja','Breville','Smeg','Keurig','Nespresso','Saeco','Gaggia','Baratza','Lelit','Tupperware','Miele','Liebherr','Hotpoint','Indesit','Beko','Panasonic','Mr. Coffee','Zojirushi'):
    pass
EXTRA={'Whirlpool':('Whirlpool Corporation','Global group','United States'),'Haier':('Haier','Global group','China'),'Electrolux':('Electrolux','Global group','Sweden'),'Samsung':('Samsung Electronics','Global group','South Korea'),'LG':('LG Electronics','Global group','South Korea'),
'Siemens':('BSH Hausgeräte','Global group','Germany'),'Frigidaire':('Electrolux','Global group','United States'),'GE Appliances':('Haier','Global group','United States'),'Fisher & Paykel':('Haier','Global group','New Zealand'),
'Tefal':('Groupe SEB','Global group','France'),'Kenwood':("De'Longhi",'Global group','United Kingdom'),"De'Longhi":("De'Longhi",'Global group','Italy'),'SharkNinja':('SharkNinja','Global group','United States'),
'Breville':('Breville','Independent','Australia'),'Smeg':('Smeg','Independent','Italy'),'Indesit':('Whirlpool Corporation','Global group','Italy')}
for n,(own,tier,c) in EXTRA.items():
    if n in reg and n not in upd or (n in reg and 'own' not in upd.get(n,{})): upd.setdefault(n,{}).update({'own':own,'tier':tier,'c':c})
for n in ('Hotpoint','Beko'): pass
json.dump({'D':D,'rep':rep,'newb':newb,'upd':upd},open(R+'work/V4_B5_APPL/stage2.json','w'),ensure_ascii=False)
print(len(newb),len(upd))
