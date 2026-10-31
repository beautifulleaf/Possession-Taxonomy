import json,os,re
P='out/C4.json'
d=json.load(open(P))
ks={k['n']:k for dp in d['depts'] for sh in dp['s'] for k in sh['k']}
# 1 pigments
pk=ks["Artists' pigment"]
URL='https://mail.artiscreation.com/red.html'
have=set()
for e in pk['x']:
    m=re.match(r'(P[A-Z][a-z]?\d+(?::\d+)?)',e['n'])
    if m: have.add(m.group(1))
    if e.get('a'): have.add(e['a'])
new=[]
for ln in open('work/GAP_C4/pr_rows.txt'):
    c,nm,cl=[x.strip() for x in ln.rstrip('\n').split('|')]
    if c in have: continue
    new.append({'n':f'{c} {nm[0].lower()+nm[1:] if not nm.startswith("Pigment") and not nm[:2].isupper() else nm}','a':c,'d':f'Organic pigment, Colour Index {c}; class: {cl}.','s':URL,'v':[],'g':'Red (organic)'})
idx=max(i for i,e in enumerate(pk['x']) if e.get('g')=='Red (organic)')
pk['x'][idx+1:idx+1]=new
pk['sel']=pk['sel'].rstrip()+f" Pigment Red organics ({len(new)} added) come from The Color of Art Pigment Database's Pigment Red page, read to its end (PR1 to PR288, which omits some codes); the Yellow, Orange, Violet, Blue, Green and Brown pages of that database are not yet read."
# 2 Fabriano
def mk(n,dsc,s,**kw):
    e={'n':n,'d':dsc,'mk':'Fabriano','s':s,'v':[],'cty':'Italy','g':'Italy'};e.update(kw);return e
F='https://www.abovegroundartsupplies.com/learn-all-about-fabriano-historic-handmade-italian-paper/'
add={'Watercolour paper':[mk('Fabriano Studio Watercolour','Fabriano watercolour paper for wet and dry techniques.',F)],
 'Drawing and mixed-media paper':[mk('Fabriano 1264 Sketch and Drawing Paper','Medium-textured white drawing paper for fine detail.',F),
   mk('Fabriano 1264 Bristol Smooth Paper','Extra-smooth white paper for intricate work.',F),
   mk('Fabriano Studio Mixed Media','Bright white paper that takes watercolour, acrylic and drawing media.',F),
   mk('Fabriano Artistico Pittura','Flat-pressed paper for acrylic, also used for oil and tempera.',F),
   mk('Fabriano Tela Oil Pad','Oil painting paper with a surface like linen canvas.',F),
   mk('Fabriano Black Black','Uncoated cardboard in a very deep black for coloured drawing.',F),
   mk('Fabriano Toned Paper','Toned drawing paper for work that stresses shading and highlights.',F)],
 'Sketchbook':[mk('Fabriano Classic Artists\' Journal','Journal for drawing, charcoal, pastel, ink or notes.',F),
   mk('Fabriano Venezia Art Book','Art book bound with Accademia paper for drawing or tempera.',F)]}
for kn,L in add.items():
    names={e['n'].lower() for e in ks[kn]['x']}
    for e in L:
        if e['n'].lower() not in names:
            if 'xg' not in ks[kn]: ks[kn]['xg']='country of the maker'
            ks[kn]['x'].append(e)
    ks[kn]['sel']=ks[kn]['sel'].rstrip()+" Fabriano lines added from the Aboveground Art Supplies Fabriano overview, read in full."
for e in ks['Watercolour paper']['x']:
    if e['n']=='Arches Aquarelle':
        e['d']=e['d'].rstrip('.')+'. Cornelissen lists it in 185, 300, 640 and 850 gsm, in hot-pressed, cold-pressed and rough surfaces (850 gsm has no hot-pressed).'
        e['s2']='https://www.cornelissen.com/arches-aquarelle-paper.html' if False else None; e.pop('s2')
# 3 owners
OW={'Derwent':('ACCO Brands','Global group','1980'),'Sizzix':('Ellison','Independent',''),'Kuretake':('Kuretake','Independent',''),
 'Schmincke':('H. Schmincke & Co. GmbH & Co. KG','Independent',''),'Lion Brand':('Lion Brand Yarn (Blumenthal family)','Independent',''),
 'Olfa':('OLFA Corporation','Independent',''),'Cricut':('Cricut, Inc.','Independent',''),'Sennelier':('Sennelier (privately held)','Independent','')}
cnt=0
for k in ks.values():
    for e in k.get('x',[]):
        for key,(o,t,y) in OW.items():
            if (e.get('mk') or '').startswith(key) and not e.get('own'):
                e['own']=o;e['tier']=t
                if y:e['own_y']=y
                cnt+=1
print('owners',cnt,'new pigments',len(new))
# 4 ms
ms=[{'mkt':'Art, craft and school supplies (group revenue, not a market share)','who':'F.I.L.A. S.p.A.','share':'EUR 612.6 million revenue','yr':2024,'s':'https://emarketstorage.it/sites/default/files/comunicati/2025-03/20250321_162528.pdf','note':'Company revenue for FY2024, down 5.0 % on FY2023 excluding DOMS (EUR 644.9 million).'},
 {'mkt':'Pencils, art and writing supplies (group revenue, not a market share)','who':'Faber-Castell Group','share':'EUR 618.4 million turnover','yr':2024,'s':'https://www.mynewsdesk.com/faber-castell/pressreleases/faber-castell-holds-its-own-in-a-difficult-landscape-3338162','note':'Fiscal year 2023/24, down 4.7 % from EUR 649.2 million.'}]
d['depts'][0]['ms']=ms
for dp in d['depts']:
    if any(k['n']=='Craft cutting machine' for sh in dp['s'] for k in sh['k']):
        dp['ms']=[{'mkt':'Cutting plotters and heat presses (company revenue, not a market share)','who':'Cricut, Inc.','share':'USD 709 million revenue','yr':2025,'s':'https://en.wikipedia.org/wiki/Cricut','note':'Revenue as given on the page for 2025.'}]
json.dump(d,open(P+'.tmp','w'),ensure_ascii=False,indent=1);os.replace(P+'.tmp',P)
# brands
B='out/C4_brands.json';b=json.load(open(B));L=b[list(b)[0]];names={x['n'] for x in L}
C='https://en.wikipedia.org/wiki/Colart'
for n,c,f,dd,s in [('Reeves','','','Art materials brand bought by AB Wilh. Becker in 1991; now part of Colart.',C),
 ('Lefranc & Bourgeois','','','Art materials brand bought by AB Wilh. Becker in 1982; now part of Colart.',C),
 ('Charbonnel','','','Printmaking ink brand bought by Lefranc & Bourgeois in 1988; now part of Colart.',C),
 ('Letraset','','','Brand acquired by Colart in 2012.',C),('Snazaroo','','1989','Face paint brand established in 1989 and owned by Colart.',C),
 ('Elephant Art','','','Colart became its main owner in May 2017.',C),
 ('ACCO Brands','United States','','Owner of Derwent, which it acquired in 1980.','https://en.wikipedia.org/wiki/Derwent_Cumberland_Pencil_Company'),
 ('Ellison','United States','1977','Irvine, California, parent of Sizzix.','https://www.sizzix.com/blogs/news/our-sizzix-story'),
 ('Cricut, Inc.','United States','','South Jordan, Utah; listed on Nasdaq as CRCT.','https://en.wikipedia.org/wiki/Cricut')]:
    if n not in names: L.append({'n':n,'c':c,'f':f,'seg':'Mainstream','kf':'brand group','d':dd,'s':s,'sig':[]})
json.dump(b,open(B+'.tmp','w'),ensure_ascii=False,indent=1);os.replace(B+'.tmp',B)
