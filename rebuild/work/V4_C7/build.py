import json, os, copy, sys
R='/home/user/Possession-Taxonomy/rebuild/'
d=json.load(open(R+'out/C7.json'))
bj=json.load(open(R+'out/C7_brands.json'))
brands={x['n']:x for x in bj['b']}
W="https://en.wikipedia.org/wiki/"
S=dict(IH=W+'Farmall',JD=W+'List_of_John_Deere_tractors',FO=W+'Fordson',AC=W+'Allis-Chalmers',MH=W+'Massey-Harris',
 LZ=W+'Lanz_Bulldog',OL=W+'Oliver_Farm_Equipment_Company',MM=W+'Minneapolis-Moline',DB=W+'David_Brown_Ltd.',
 FE=W+'Ferguson_TE20',CA=W+'Case_Corporation',DE=W+'Deutz-Fahr',ZE=W+'Zetor')
# ---- 1. commodity kinds: strip m and r, record makers
removed={}
vint=[dp for dp in d['depts'] if dp['n'].startswith('Vintage')][0]
for dp in d['depts']:
    for sec in dp['s']:
        for k in sec['k']:
            for f in ('m','r'):
                if f in k and (dp is not vint):
                    for row in k[f]:
                        mk=row[1] if len(row)>1 else ''
                        removed.setdefault(mk,[]).append((k['n'],row[0],k.get('s','')))
                    del k[f]
# vintage non-tractor kinds: drop m, r and x (commodity)
for sec in vint['s']:
    for k in sec['k']:
        if sec['n']=='Vintage tractors': continue
        for f in ('m','r','x'):
            if f in k:
                for row in k[f]:
                    if isinstance(row,dict): removed.setdefault(row.get('mk',''),[]).append((k['n'],row['n'],row.get('s','')))
                    else: removed.setdefault(row[1],[]).append((k['n'],row[0],k.get('s','')))
                del k[f]
# ---- 2. vintage tractor canon
def E(name,mk,y,s,desc,v=None,role=None,a='',dt='model · years · originality'):
    e=dict(n=name,a=a,d=desc,mk=mk,y=y,s=s,dt=dt)
    if v: e['v']=[dict(n=n,mk=mk,y=yy,d=dd) for n,yy,dd in v]
    if role: e['role']=role
    return e
new={
'Early tractor (pre-1930)':[
 E('Hart-Parr No. 1','Hart-Parr','1902',S['OL'],'Single experimental tractor of 1902, scrapped in 1916.'),
 E('Hart-Parr Model 3','Hart-Parr','1903',S['OL'],'Recognised by the American Society of Mechanical Engineers as the first successful farm tractor with an internal combustion engine; 15 built.',role='origin'),
 E('Hart-Parr 22-45','Hart-Parr','1903–1911',S['OL'],'Early Hart-Parr model shown in the page gallery.'),
 E('Hart-Parr 30-60 Old Reliable','Hart-Parr','1907–1918',S['OL'],'Rated 30 drawbar and 60 pulley horsepower; 3,798 built, four more in 1924.'),
 E('Hart-Parr 20-40 Steel King','Hart-Parr','1911–1914',S['OL'],'About 197 built.'),
 E('Hart-Parr Little Red Devil','Hart-Parr','1915',S['OL'],'Two-cylinder two-stroke model that failed and was recalled.'),
 E('Hart-Parr 12-25','Hart-Parr','1918',S['OL'],'Basis for later Hart-Parr tractors; re-rated 15-30 after Nebraska testing.',v=[('16-30','1924','upgrade of the 15-30')]),
 E('Hart-Parr 18-36','Hart-Parr','1926–1930',S['OL'],"The firm's most popular tractor of that period."),
 E('Allis-Chalmers 10-18','Allis-Chalmers','1912–1918',S['AC'],'One of the first Allis-Chalmers farm tractors.'),
 E('Allis-Chalmers 6-12','Allis-Chalmers','1914–1919',S['AC'],'Small early farm tractor developed 1914–1919.'),
 E('Allis-Chalmers 15-30','Allis-Chalmers','1914–1919',S['AC'],'Early farm tractor developed 1914–1919.'),
 E('Allis-Chalmers 20-30','Allis-Chalmers','1918–1930',S['AC'],'Long-running early model.'),
 E('Case 10-20','Case','1915–1918',S['CA'],'Early Case tractor shown in the page gallery.'),
 E('Case 9-18','Case','1916–1918',S['CA'],'Early Case tractor shown in the page gallery.'),
 E('Case 15-27','Case','1919–1924',S['CA'],'Case tractor of the early 1920s.'),
 E('Case 12-20','Case','1921–1927',S['CA'],'Case tractor of the 1920s.'),
 E('Moline Universal','Moline Plow Company','1917',S['MM'],'Single-axle tractor with interchangeable implements; Model D introduced 1917.'),
],
'Hot-bulb and semi-diesel tractor':[
 E('Lanz Bulldog','Lanz','1921',S['LZ'],'Hot-bulb tractor made from 1921 to 1960 in many versions; production began with the HL.',v=[('HL','1921','first model'),('8506','1939',''),('D 7506/3','1939',''),('D 9506','',''),('Model N','','35 hp; basis of the Australian KL Bulldog')],role='origin'),
 E('Lanz Alldog','Lanz','1951–1957',S['LZ'],'Rear-engined Bulldog derivative.'),
 E('Lanz Iberica Bulldog','Lanz Iberica','1956–1963',S['LZ'],'Spanish-built Bulldog made at Getafe; 17,100 tractors in all.'),
],
'Vintage row-crop tractor':[
 E('Farmall Regular and F-20','International Harvester','1924–1932',S['IH'],'The original Farmall, renamed F-20 in 1932; large-scale production from 1926.',v=[('Regular','1924–1932','original name'),('F-20','1932','more powerful engine')]),
 E('Farmall F-30','International Harvester','1931',S['IH'],'Bigger, heavier and more powerful than the Regular.'),
 E('Farmall F-12 and F-14','International Harvester','1932–1939',S['IH'],'Smaller, lighter Farmall without the rear portal axle.',v=[('F-12','1932–1938',''),('F-14','1938–1939','updated steering column, higher rev limit')]),
 E('Farmall H','International Harvester','1939–1954',S['IH'],"Described by the page as the number two selling tractor model of all time in North America.",v=[('Super H','1953–1954','last two years')],role='landmark'),
 E('Farmall A','International Harvester','1939',S['IH'],'Small letter-series tractor with the Culti-Vision offset design.',v=[('Super A','1947','')]),
 E('Farmall B','International Harvester','1939',S['IH'],'Narrow tricycle front end; replaced by the C in 1948.',v=[('BN','','')]),
 E('Farmall M','International Harvester','1939',S['IH'],'Largest of the letter series.',v=[('Super M','1952',''),('Super M-TA','','with Torque Amplifier'),('MD','1941','first Farmall diesel')]),
 E('Farmall C','International Harvester','1948',S['IH'],'Replaced the B in 1948.',v=[('Super C','1951','')]),
 E('Farmall Cub','International Harvester','1947–1979',S['IH'],'Smallest Farmall, with a 60 cu. in. four-cylinder engine.',v=[('Cub Lo-Boy','1955','low version')]),
 E('Farmall Hundred series','International Harvester','1954',S['IH'],'Numbered models that replaced the letters.',v=[('100','1954','Fast Hitch'),('130','',''),('140','',''),('200','',''),('230','',''),('240','',''),('300','1955',''),('350','1956–1958','first direct-start diesel Farmall'),('400','1955',''),('450','1956–1958','')]),
 E('John Deere Model B','John Deere','1935',S['JD'],'Smaller two-cylinder row-crop tractor.',v=[('B (unstyled)','1935–1939',''),('B (styled)','1939–1952',''),('50, 520, 530','','later variants')]),
 E('John Deere Model GP','John Deere','1928–1935',S['JD'],'General-purpose two-cylinder tractor.',v=[('GP','1928–1935','standard front'),('GP tricycle','1928–1929',''),('GP wide-tread','1929–1933',''),('GPO orchard','1931–1935','')]),
 E('John Deere Model G','John Deere','1937',S['JD'],'Three-plow two-cylinder row-crop tractor.',v=[('G (unstyled)','1937–1941',''),('G (styled)','1942',''),('70, 720, 730','','later variants')]),
 E('John Deere Model H','John Deere','1938–1947',S['JD'],'Small two-cylinder row-crop tractor.'),
 E('John Deere Model L','John Deere','1940–1947',S['JD'],'Light two-cylinder tractor.',v=[('LA','1940–1947','')]),
 E('John Deere Model M','John Deere','1947–1953',S['JD'],'Compact utility two-cylinder tractor.',v=[('40, 320, 330, 420, 430, 435, 440','','later variants')]),
 E('Allis-Chalmers Model B','Allis-Chalmers','1937',S['AC'],'Second-generation, lighter row-crop tractor; a top seller.'),
 E('Allis-Chalmers WD-45','Allis-Chalmers','1953–1957',S['AC'],'Replaced the WD; Buda diesel from 1955.'),
 E('Oliver Fleetline','Oliver Farm Equipment','1948–1954',S['OL'],'Fleetline series of the Oliver 66, 77 and 88.',v=[('66','1948–1954',''),('77','1948–1954','petrol or diesel'),('88','1948–1954','petrol or diesel')]),
],
'Vintage standard tractor':[
 E('Allis-Chalmers Model U','Allis-Chalmers','c. 1930',S['AC'],'Built under a deal with the United conglomerate, which collapsed around 1930.'),
 E('Allis-Chalmers D-series','Allis-Chalmers','1957',S['AC'],'Series that followed the WD-45.',v=[('D15','1957',''),('D17','',''),('D19','','first factory turbocharger on a farm tractor, per the page'),('D21 Series II','','')]),
 E('Case Model C and CC','Case','1929–1940',S['CA'],'Case Model C 1929–1940 and CC 1929–1939.',v=[('C','1929–1940',''),('CC','1929–1939','')]),
 E('Case Model L','Case','1929–1940',S['CA'],'Case row-crop and standard tractor of the 1930s.'),
 E('Fordson Model N','Fordson','1927',S['FO'],'27 hp tractor made in Cork from 1927 and Dagenham from 1933; over 136,000 built there in the war.'),
 E('Fordson All-Around','Fordson','1936',S['FO'],'Row-crop Fordson prototyped 1930–31 and built by Ford Ltd in Britain.'),
 E('Massey-Harris GP 15/22','Massey-Harris','1930–1936',S['MH'],'20 hp general-purpose tractor.'),
 E('Minneapolis-Moline GT','Minneapolis-Moline','1941',S['MM'],'Four-cylinder 40 hp tractor.'),
 E('Minneapolis-Moline ZB series','Minneapolis-Moline','1953–1955',S['MM'],'34.8 hp improvement of the ZA.',v=[('ZBU','',''),('ZBN','',''),('ZBE','','')]),
 E('Minneapolis-Moline M series','Minneapolis-Moline','1960–1970',S['MM'],'M-5, M-504, M-602, M-604 and M-670; the M-604 was four-wheel drive.'),
 E('Oliver Super 55','Oliver Farm Equipment','1954',S['OL'],"The company's first compact utility tractor."),
 E('Oliver 660, 770, 880 and 990','Oliver Farm Equipment','1958',S['OL'],'Models marketed from 1958.'),
 E('Oliver 1600, 1800 and 1900','Oliver Farm Equipment','1960',S['OL'],'Four-digit models introduced in 1960.'),
 E('David Brown Ferguson-Brown','David Brown','1936–1940',S['DB'],'Joint design with Harry Ferguson; 1,350 built.'),
 E('David Brown VAK1','David Brown','1939–1945',S['DB'],'Launched at the 1939 Royal Show.',v=[('VAK1A','1945–1947',''),('VAK1C Cropmaster','1947–1954','')]),
 E('David Brown 900 series','David Brown','1955–1957',S['DB'],'Successor to the Cropmaster.'),
 E('David Brown Implematic series','David Brown','1958–1965',S['DB'],'Implematic hydraulics; the 950 and 850 were also rebadged as Oliver 500 to 600.',v=[('950','1958–1961',''),('850','1961–1965',''),('880','1961–1965',''),('990','1961–1965','')]),
 E('David Brown Selectamatic series','David Brown','1965–1971',S['DB'],'Selectamatic hydraulics; the 780 petrol was sold as the 3800 in the US.',v=[('770','1965–1970',''),('880','1965–1971',''),('990','1965–1971',''),('780','1965–1971',''),('1200','1967–1971','')]),
 E('David Brown Synchromesh series','David Brown','1971–1979',S['DB'],'Synchromesh range; the 1410 and 1412 were the first turbocharged David Browns.',v=[('885','1971–1979',''),('990, 995, 996','1971–1979',''),('1210','1971–1979',''),('1212 Hydra-Shift','1971–1979',''),('1410','1974–1979',''),('1412 Hydra-Shift','1974–1979','')]),
],
'Vintage European diesel tractor':[
 E('Deutz MTH 222','Deutz','1926',S['DE'],'First series-production diesel tractor, according to the page.',role='origin'),
 E('Deutz MTZ','Deutz','1929',S['DE'],'Up to 36 hp; about 2,000 built.'),
 E('Deutz F2M 315 and F3M 317','Deutz','1934–1935',S['DE'],'Steel-wheeled F-series tractors.',v=[('F2M 315','1934','28 hp'),('F3M 317','1935','45 to 50 hp')]),
 E('Deutz F1M 414 Elfer','Deutz','1936',S['DE'],'Small tractor; nearly 19,000 built by 1953.'),
 E('Deutz F1L 514','Deutz','1950',S['DE'],'Air-cooled tractor; about 37,000 built.',v=[('F2L 514','1950s',''),('F3L 514','1950s','about 17,000 built')]),
 E('Deutz 612','Deutz','1953',S['DE'],'Compact models for smaller farms (F1L and F2L 612).'),
 E('Deutz 712','Deutz','1957',S['DE'],'F2L 712 with improved engine characteristics.'),
 E('Deutz D series','Deutz','1957',S['DE'],'D 15 to D 80 range; the D 30 was the best seller and the D 80 of 1964 was the first six-cylinder.',v=[('D 15','1964–1965','last single-cylinder'),('D 50','1960','46 hp'),('D 80','1964','75 hp six-cylinder')]),
 E('Deutz D-05 series','Deutz','1965',S['DE'],'D 2505 to D 9005; the D 60 05 of 1966 was the first direct-injection model.'),
 E('Deutz D-06 series','Deutz','1968',S['DE'],'D 2506 to D 16006 with the 912 engine.'),
 E('Fahr F22','Fahr','1938',S['DE'],"Fahr's first tractor, 22 hp.",v=[('T22','1940','development of the F22'),('HG25','1942','wood-gas powered'),('D30 W and D15','1949',''),('D12N and D17N','1953',''),('D90 and D180H','1954','')]),
 E('Zetor 25','Zetor','1946–1949',S['ZE'],'First Zetor tractor, built by Zbrojovka Brno.',v=[('25A and 25K','1954–1961','')]),
 E('Zetor 15','Zetor','1948–1949',S['ZE'],'Approved for production in 1948.'),
 E('Zetor 35','Zetor','1955–1960',S['ZE'],'42 hp four-cylinder tractor.',v=[('50 Super','to 1968','upgrade of the 35')]),
 E('Zetor Unified Series','Zetor','late 1950s',S['ZE'],'Two-, three- and four-cylinder tractors with shared parts.',v=[('Series I: 2011, 3011, 4011','late 1950s',''),('Series II','1968','rollover-protected cab'),('Crystal 12011','1969','first six-cylinder Zetor')]),
],
'Vintage crawler tractor':[
 E('David Brown crawlers','David Brown','1942–1965',S['DB'],'Tracklayers built by David Brown.',v=[('DB4','1942–1949','110 built'),('Taskmaster','1948–1965',''),('50TD Trackmaster','1950–1963',''),('30TD Trackmaster','1953','')]),
],
}
# merge into vintage tractor kinds
mapping={}
sec=[s for s in vint['s'] if s['n']=='Vintage tractors'][0]
drop={'Vintage row-crop tractor':{'Farmall','John Deere Model A'},
      'Vintage standard tractor':{'David Brown Cropmaster'},
      'Vintage European diesel tractor':{'Deutz F-series','Zetor 25'},
      'Hot-bulb and semi-diesel tractor':{'Lanz Bulldog'},
      'Early tractor (pre-1930)':{'Hart-Parr'}}
# keep John Deere Model A existing entry (do not drop)
drop['Vintage row-crop tractor']={'Farmall'}
for k in sec['k']:
    if k['n']=='Steam traction and ploughing engine': continue
    ex=[e for e in k.get('x',[]) if e['n'] not in drop.get(k['n'],set())]
    ex=ex+new.get(k['n'],[])
    for e in ex:
        e['g']=e['mk']
        if e['mk']=='Ferguson' or e['mk']=='Massey Ferguson': e['g']=e['mk']
    # sort by maker, year, name
    def yr(e):
        import re
        m=re.search(r'\d{4}',e.get('y','') or ''); return int(m.group()) if m else 9999
    ex.sort(key=lambda e:(e['g'],yr(e),e['n']))
    k['x']=ex
    k['xg']='by maker'
    k['nl']='One entry is a tractor model line sold under one maker\'s name; revisions, engine and fuel variants and styled versions are versions.'
    k['sel']=("Model lines named on the fetched Wikipedia pages of the classic makers (Allis-Chalmers, Case, David Brown, Deutz-Fahr, Farmall/International Harvester, Ferguson, Fordson, John Deere, Lanz, Massey-Harris, Minneapolis-Moline, Oliver/Hart-Parr, Zetor) up to about 1979, placed by tractor type; "
              "no single whole-space reference exists, and makers not fetched keep the entries of the earlier pass.")
# 'John Deere Model D' etc. exist; add JD tractor mk-based g done.
# ---- 3. market panel on the tractor department
t0=d['depts'][0]
FW="https://www.fwi.co.uk/machinery/ranked-europes-biggest-farm-equipment-manufacturers"
FE_="https://www.farm-equipment.com/articles/22667-ag-companies-make-the-industry-week-us-500-report"
ms=[]
for who,sh,note in [('Deere & Company','$61.222 billion','rank 20 on the IndustryWeek U.S. 500; company revenue, not farm-machinery share'),
                    ('AGCO','$14.4 billion','rank 100 on the IndustryWeek U.S. 500; revenue up 13.9 %'),
                    ('Alamo Group','$1.690 billion','rank 464 on the IndustryWeek U.S. 500')]:
    ms.append(dict(mkt='US 500 ranking, agricultural machinery makers',who=who,share=sh,yr=2023,s=FE_,note=note))
for r,(who,sh,yy,note) in enumerate([('Kuhn Group','€1,177 million',2019,'group turnover'),('DeLaval','€1,082 million',2019,'dairy equipment division turnover'),
  ('Krone','€698 million',2019,'turnover'),('GEA Farm Technologies','€656 million',2019,'division turnover'),('Lely Group','€606 million',2019,'group turnover'),
  ('Grimme','€492 million',2019,'group turnover'),('Exel Industries','€469 million',2019,'agricultural equipment operations only'),('Amazone','€467 million',2019,'group turnover'),
  ('Horsch','€424 million',2019,'group turnover'),('Pöttinger','€382 million',2019,'2018–19 financial year'),('Lemken','€380 million',2019,'group turnover'),
  ('Väderstad','€321 million',2019,'group turnover'),('Maschio Gaspardo','€316 million',2019,'ranked 13th')],1):
    ms.append(dict(mkt='European farm equipment, rank %d by turnover'%r,who=who,share=sh,yr=yy,s=FW,note=note))
t0['ms']=ms
t0['msum']="Deere leads the farm-machinery companies on the 2023 IndustryWeek U.S. 500 (rank 20, $61.2 billion), ahead of AGCO (rank 100). In Europe, Kuhn headed the 2019 turnover ranking of independent equipment makers. CNH, Kubota, CLAAS and Mahindra could not be sourced."
# ---- 4. brand register
SEGM={'default':'Specialist'}
def addb(n,src,kf,sc):
    if n and n not in brands:
        brands[n]=dict(n=n,c='',seg='Specialist',d='Maker named on a source page for this category.',sig=[],rel=[],s=src,sc=sc,kf=kf)
for mk,rows in removed.items():
    if mk:
        k,_,src=rows[0]; addb(mk,src,k.lower(),['Smallholding','Acreage and estate'])
for sec2 in vint['s']:
    for k in sec2['k']:
        for e in k.get('x',[]):
            if e.get('mk'): addb(e['mk'],e['s'],'tractors',['Vintage tractor rallies and restoration'])
        # versions makers
        for e in k.get('x',[]):
            for v in e.get('v',[]):
                if v.get('mk'): addb(v['mk'],e['s'],'tractors',['Vintage tractor rallies and restoration'])
for n in ['Deere & Company','AGCO','Alamo Group','Kuhn Group','Krone','Grimme','Amazone','Horsch','Lemken','Väderstad','Maschio Gaspardo','Pöttinger','Lely Group','DeLaval','GEA Farm Technologies','Exel Industries']:
    addb(n,FW,'farm machinery makers',['Smallholding','Acreage and estate'])
bj['b']=list(brands.values())
tmp=R+'work/V4_C7/C7.json.tmp'
json.dump(d,open(tmp,'w'),indent=1,ensure_ascii=False); os.replace(tmp,R+'out/C7.json')
json.dump(bj,open(tmp,'w'),indent=1,ensure_ascii=False); os.replace(tmp,R+'out/C7_brands.json')
print(len(removed),'makers removed from m/r')
