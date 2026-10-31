import json,os
p='out/B10.json'
d=json.load(open(p))
W='https://en.wikipedia.org/wiki/Beehive'
def e(n,d_,mk='',y='',g='',a=''):
    return {"n":n,"a":a,"d":d_,"mk":mk,"y":y,"s":W,"v":[],"g":g}
ks={k['n']:k for s in d['depts'][9]['s'] for k in s['k']}
fv=ks['Framed vertical hive']
fv['x']+= [
 e('German Normal hive','Standard vertical frame hive of Germany, listed as DNM.','','', 'Framed vertical','DNM'),
 e('Zander hive','Vertical frame hive of southern Germany named for its designer.','Enoch Zander','','Framed vertical'),
 e('D.E. hive','Vertical frame hive named for its designer David Eyre.','David Eyre','','Framed vertical'),
 e('B-BOX','Vertical frame hive made by the Italian company Beeing.','Beeing','','Framed vertical'),
 e('Hyper Hyve','Vertical frame hive designed by Mike James.','Mike James','','Framed vertical'),
 e('CDB hive','Vertical frame hive from Ireland, attributed to Charles Nash Abbott.','Charles Nash Abbott','1890','Framed vertical'),
 e('AZ hive','Vertical frame hive of Slovenia named for Anton Žnideršič.','Anton Žnideršič','','Framed vertical'),
]
lg=ks['Long hive']
lg['x']+=[
 e('Long box hive','Traditional horizontal box hive of the south-eastern United States.','','','Long'),
 e('Long Langstroth hive','Horizontal hive built to take Langstroth frames.','','','Long'),
 e('Dartington long deep hive','Horizontal deep-frame hive from the United Kingdom designed by Robin Dartington.','Robin Dartington','','Long','DLD'),
 e('ZEST hive','Horizontal hive designed by Bill Summers.','Bill Summers','','Long'),
 e('Lazutin hive','Horizontal hive designed by Fedor Lazutin.','Fedor Lazutin','','Long'),
 e('Golden hive','Horizontal hive known in Ukraine as the Ukrainian hive.','','','Long','Ukrainian hive'),
]
tb=ks['Top-bar hive']
tb['x']+=[
 e('Cathedral hive','Top-bar hive type listed in Wikipedia Beehive.','','','Top-bar'),
 e('Beehaus hive','Hybrid of top-bar and Langstroth hives.','','2009','Top-bar'),
]
sh=d['depts'][9]['s'][0]['k']
base={"nl":"One entry is a named hive design with its inventor and year; box sizes and frame sizes are versions.","xg":"by hive family"}
for n,desc,items,tt in [
 ('Log hive','A hollow log or tree section kept as a hive without frames.',[e('Bee gum','Hollow-log hive of the south-eastern United States.','','','Traditional'),e('Barć','Hollow-log tree hive of Poland.','','','Traditional')],[["Material",["hollow log","tree cavity"]]]),
 ('Stingless bee hive','A box hive made for stingless (meliponine) bees rather than honey bees.',[e('Nogueira-Neto hive','Meliponine hive named in Wikipedia Beehive.','','','Stingless bee'),e('UTOB hive','Meliponine hive named in Wikipedia Beehive.','','','Stingless bee')],[["Species",["stingless bee"]]])]:
    k={"n":n,"a":"","d":desc,"s":W,"x":items,"tt":tt}; k.update(base); sh.append(k)
# insert new kinds after Warre, before Skep
sh[:]=[k for k in sh if k['n'] not in('Log hive','Stingless bee hive')][:4]+[k for k in sh if k['n'] in('Log hive','Stingless bee hive')]+[k for k in sh if k['n'] not in('Log hive','Stingless bee hive')][4:]
cov="Complete: all designs Wikipedia's Beehive article names with a description are listed (Langstroth to UTOB, 33 entries including the Flow Hive and Rose hive from earlier pages). Left out: Stewarton hive, which that page links but does not describe, and the Skep, which is its own kind."
for n in ['Framed vertical hive','Long hive','Top-bar hive','Warré hive','Log hive','Stingless bee hive']:
    k=ks.get(n) or next(k for k in sh if k['n']==n)
    k['sel']=k['sel'].split(' Covers 15')[0]+' '+cov if 'sel' in k and 'Covers 15' in k['sel'] else (k['sel']+' '+cov)
json.dump(d,open(p+'.tmp','w'),ensure_ascii=False,indent=1); os.rename(p+'.tmp',p)
