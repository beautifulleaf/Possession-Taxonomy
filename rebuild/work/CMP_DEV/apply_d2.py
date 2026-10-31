import json,os,re
d=json.load(open('out/D2.json'))
fam=[];cur=None
for l in open('work/CMP_DEV/nokia_raw.txt'):
    l=l.rstrip('\n')
    if l.startswith('#'):
        n,dd=l[1:].split('|'); cur={'n':n,'d':dd,'m':[]}; fam.append(cur)
    elif l: m,y=l.split('|'); cur['m'].append((m,y))
# existing names
names=set()
for de in d['depts']:
  for s in de['s']:
    for k in s['k']:
      for x in k.get('x',[]):
        names.add(x['n'].lower())
        for v in x.get('v',[]): names.add(v['n'].lower())
def full(m):
    return m if m.lower().startswith(('nokia','mobira','n-gage','cardphone','d211','d311')) else 'Nokia '+m
dest={'Nokia 9000 series':'Keyboard smartphone','Nokia C, E, N and X series':'Keyboard smartphone','Nokia Symbian three-digit series':'Keyboard smartphone','Nokia Asha series':'Touchscreen smartphone','Nokia Lumia series':'Touchscreen smartphone'}
src='https://en.wikipedia.org/wiki/List_of_Nokia_products'
added=0;newfam={}
for f in fam:
    vs=[]
    for m,y in sorted(f['m'],key=lambda t:(t[1] or '9999',t[0])) if False else f['m']:
        fn=full(m)
        if f['n'] in('Nokia Lumia series',) and not fn.lower().startswith('nokia lumia') and m in('X','X+','XL','X2','XL 4G'): fn='Nokia '+m
        if fn.lower() in names: continue
        names.add(fn.lower()); vs.append({'n':fn,'mk':'Nokia','y':y,'d':''}); added+=1
    ys=[v['y'] for v in vs if v['y']]
    if not vs: continue
    newfam[f['n']]={'n':f['n'],'a':'','d':f['d'],'mk':'Nokia','y':min(ys) if ys else '','s':src,'v':vs,'g':'Nokia'}
    if f['n']=='Nokia Lumia series': newfam[f['n']]['n']='Nokia Lumia series (and Nokia X)'
for de in d['depts']:
  for s in de['s']:
    for k in s['k']:
      kn=k['n']
      if kn in('Keypad phone','Keyboard smartphone','Touchscreen smartphone'):
        mine=[v for fn,v in newfam.items() if dest.get(fn,'Keypad phone')==kn]
        if not mine: continue
        xs=k['x']; idx=max([i for i,x in enumerate(xs) if x.get('g')=='Nokia'],default=len(xs)-1)+1
        mine.sort(key=lambda e:(e['y'] or '9999',e['n']))
        k['x']=xs[:idx]+mine+xs[idx:]
        k['sel']+=" Nokia handsets follow Wikipedia's List of Nokia products (numbered 1000 to 9000 series, C/E/N/X, Symbian, Asha, Lumia, X and three-digit feature phones, read in windows to character 250,000 of 351,000), one family entry per series with each model as a version; the Mobira, Series 30+ rows and the products page after character 300,000 and some rows without a listed year are not complete."
      if kn=='Tablet':
        # Pixel Tablet
        k['x'].append({'n':'Pixel Tablet','a':'','d':'Google tablet sold with a charging speaker dock, released in June 2023.','mk':'Google','y':'2023','s':'https://en.wikipedia.org/wiki/Google_Pixel','v':[],'g':'Google'})
        k['x'].sort(key=lambda x:0) 
        for x in k['x']:
          pass
        k['sel']+=' Pixel Tablet added from Wikipedia\'s Google Pixel article.'
      if kn=='E-reader':
        for x in k['x']:
          if x['n']=='Kindle DX' and not any('2 International' in v['n'] for v in x['v']): pass
          if x['n']=='Kindle':
            if not any('2 International' in v['n'] for v in x['v']):
              x['v'].insert(2,{'n':'Kindle 2 International','mk':'Amazon','y':'2009','d':'Released 19 October 2009.'})
        k['sel']+=' Complete for the e-reader rows of the Kindle table in Wikipedia\'s Amazon Kindle article (29 devices, 1 to 11, DX, Paperwhite, Voyage, Oasis, Scribe and Colorsoft) with its four unlisted newer models added from earlier fetches.'
      for x in k.get('x',[]):
        if x['n']=='Apple Watch':
          have={v['n'] for v in x['v']}
          new=[('Apple Watch Series 1','2016','Released 12 September 2016.'),('Apple Watch Series 2','2016','Released 16 September 2016.'),('Apple Watch Series 3','2017','Released 22 September 2017.')]
          pos=[i for i,v in enumerate(x['v']) if v['n']=='Series 4'][0]
          for n,y,dd in reversed(new):
            if n not in have: x['v'].insert(pos,{'n':n,'mk':'Apple','y':y,'d':dd})
          k['sel']+=' Series 1 to 3 added from the life-cycle table of Wikipedia\'s Apple Watch article.'
        if x['n']=='Pixel Watch':
          for v in x['v']:
            if v['n']=='Pixel Watch 3' and not v['y']: v['y']='2024'; v['d']='Released August 2024.'
            if v['n']=='Pixel Watch 4' and not v['y']: v['y']='2025'; v['d']='Released August 2025.'
        if x['n']=='Pixel':
          pd={'Pixel / Pixel XL':'Released 20 October 2016.','Pixel 2':'Released 19 October 2017, with the 2 XL.','Pixel 3':'Released 18 October 2018, with the 3 XL.','Pixel 3a':'Released 15 May 2019, with the 3a XL.','Pixel 4':'Released 23 October 2019, with the 4 XL.','Pixel 4a':'Released 20 August 2020; the 4a (5G) followed.','Pixel 5':'Released 15 October 2020.','Pixel 5a':'Released 26 August 2021.','Pixel 6 / 6 Pro':'Released 28 October 2021.','Pixel 6a':'Released 21 July 2022.','Pixel 7':'Released 13 October 2022, with the 7 Pro.','Pixel 7a':'Released 10 May 2023.','Pixel Fold':'Released 20 June 2023.','Pixel 8 / 8 Pro':'Released 12 October 2023.','Pixel 8a':'Released 14 May 2024.','Pixel 9 / 9 Pro / 9 Pro XL':'Released 22 August 2024.','Pixel 9 Pro Fold':'Released 4 September 2024.','Pixel 9a':'Released 10 April 2025.','Pixel 10 / 10 Pro / 10 Pro XL':'Pixel 10 released 28 August 2025; Pro models 9 October 2025.','Pixel 10 Pro Fold':'Released 9 October 2025.','Pixel 10a':'Released 5 March 2026.','Pixel 11 / 11 Pro / 11 Pro XL':'Pixel 11 released 20 August 2026.'}
          for v in x['v']:
            if not v.get('d') and v['n'] in pd: v['d']=pd[v['n']]
          k['sel']+=" Pixel release dates from Wikipedia's Google Pixel article, which is complete for the phones (XL and Pro variants are grouped with their base model)."
json.dump(d,open('work/CMP_DEV/D2.tmp','w'),ensure_ascii=False,indent=1)
os.replace('work/CMP_DEV/D2.tmp','out/D2.json'); print(added,{k:len(v['v']) for k,v in newfam.items()})
