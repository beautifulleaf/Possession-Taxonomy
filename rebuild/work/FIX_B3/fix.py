import json,os,collections
P='out/B3.json'
d=json.load(open(P))
moves=json.load(open('out/B3_moves.json'))
K={}
loc={}
for dp in d['depts']:
  for s in dp['s']:
    for k in s['k']:
      K[k['n']]=k; loc[k['n']]=(dp,s)
def remove(n):
  dp,s=loc[n]; s['k']=[k for k in s['k'] if k['n']!=n]
cnt=lambda:sum(len(s['k']) for dp in d['depts'] for s in dp['s'])
arch=lambda:sum(len(k.get('x',[])) for k in K.values())
before=(cnt(),arch())
# moves
for n,to,dept in [('Recessed downlight','G3','Built-in lighting'),('Track lighting','G3','Built-in lighting'),('Under-cabinet light','G3','Built-in lighting'),('Step & plinth light','G3','Built-in lighting'),('Party & DJ light','B4','Party & celebration effects')]:
  moves['out'].append({"to":to,"dept":dept,"kind":K[n]}); remove(n)
# CFL, panel
K['Tube light']['t']+=['Compact fluorescent (pin-base CFL)']
K['Tube light']['a']+=' · CFL · compact fluorescent lamp'
remove('Compact fluorescent bulb')
K['Flush ceiling light']['t'].append('Panel (troffer)')
K['Flush ceiling light']['a']+=' · LED panel · troffer'
remove('Panel light')
# cuts
def keep(n,names):
  k=K[n]; k['m']=[m for m in k['m'] if m[0] in names]
keep('Flush ceiling light',{'Doris CL257','Fiobbo','NÖSUND','Caboche Plus','Paris Lamp','Match'})
keep('Ceiling spotlight',{'Limbali','NYMÅNE','Corato','Nova','Alec','Imageo'})
keep('Path light',{'Kyna','GL 80 SC','Flindt','Apex','Alara','Tetragono'})
# torch leftovers
k=K['Keychain light']
drop={'TIKI','Tiki GITD','TINI 2','TUP2','iMini 2','I1R 2 Pro EOS'}
k['m']=[m for m in k['m'] if m[0] not in drop]
k['x'].insert(0,{"n":"Nitecore TIKI","a":"TIKI keychain light","d":"Nitecore's rechargeable key-ring light with a white and UV auxiliary emitter in a 12 g body.","mk":"Nitecore","y":"","s":"https://www.nitecore.com/product/tiki","v":[{"n":"TIKI","mk":"Nitecore","d":"high-CRI neutral white plus UV"},{"n":"TIKI LE","mk":"Nitecore","d":"red and blue flashing signal lights"},{"n":"TIKI UV","mk":"Nitecore","d":"1000 mW UV light"},{"n":"TIKI GITD","mk":"Nitecore","d":"glow-in-the-dark body"},{"n":"TIKI GITD BLUE","mk":"Nitecore","d":"glow-in-the-dark variant"}],"dt":"130 mAh built-in Li-ion · USB-C"})
k['x'].append  # noop
K['EDC flashlight']['x'].append({"n":"Ledlenser P-series","a":"P7 · Ledlenser P7","d":"Ledlenser's long-running focusing hand torch range, anchored by the P7, with a rechargeable R line and Pro variants.","mk":"Ledlenser","y":"","s":"https://ledlenser.co.uk/blogs/news/ledlensers-new-p-series-raises-the-bar-for-torches","v":[{"n":"P7","mk":"Ledlenser","d":"the original classic, non-rechargeable"},{"n":"P7R","mk":"Ledlenser","d":"rechargeable evolution"},{"n":"P7R Pro","mk":"Ledlenser","d":"Pro version"},{"n":"P5","mk":"Ledlenser","d":"non-rechargeable"},{"n":"P5R","mk":"Ledlenser","d":"rechargeable"},{"n":"P18R","mk":"Ledlenser","d":"larger rechargeable"},{"n":"P21R","mk":"Ledlenser","d":"largest rechargeable, one-touch focus"}],"dt":"Advanced Focus System · fourth generation 2025 (16 models) · IP54–IP68"})
# cap per maker in dominant torch kinds
for n in ['EDC flashlight','Tactical flashlight','Thrower','Headlamp','Keychain light']:
  c=collections.Counter(); out=[]
  for m in K[n].get('m',[]):
    c[m[1]]+=1
    if c[m[1]]<=3: out.append(m)
  K[n]['m']=out
# table lamp icons
t=K['Table lamp']
t['m']=[m for m in t['m'] if m[0] not in ('Snoopy','Glo-Ball T1','Boalum')]
t['x']+= [
 {"n":"Snoopy","a":"Snoopy lamp","d":"Table lamp with a half-dome enamelled metal shade on a marble base, designed by the Castiglioni brothers.","mk":"Flos","y":"1967","s":"https://en.wikipedia.org/wiki/Achille_Castiglioni","v":[],"dt":"marble base · shade colours"},
 {"n":"Glo-Ball","a":"Glo-Ball lamp","d":"Jasper Morrison's opal glass globe light, made as table, floor, wall and pendant versions.","mk":"Flos","y":"1998","s":"https://en.wikipedia.org/wiki/Jasper_Morrison","v":[{"n":"Glo-Ball T1","mk":"Flos","d":"table version"}],"dt":"diameter · glass finish"},
 {"n":"Boalum","a":"Boalum lamp","d":"Flexible ribbed-tube lamp, designed by Gianfranco Frattini and Livio Castiglioni.","mk":"Artemide","y":"1969–70","s":"https://en.wikipedia.org/wiki/Gianfranco_Frattini","v":[],"dt":"white or other diffuser colours"}]
# safety lamp kind
sh=loc['Hurricane lantern'][1]
def A(n,a,dd,mk,y,s):return {"n":n,"a":a,"d":dd,"mk":mk,"y":y,"s":s,"v":[],"dt":""}
W="https://en.wikipedia.org/wiki/Safety_lamp"
sh['k'].append({"n":"Safety & miner's lamp","a":"miner's lamp · mine lamp · carbide lamp","d":"Flame or carbide lamp built for mines, with a gauze or glass guard against firedamp, now collected.","t":["flame safety lamp","carbide lamp","candle-clip miner's lamp"],"s":W,"x":[
 A("Davy lamp","Davy safety lamp","Oil lamp whose flame is enclosed in wire gauze so it cannot ignite firedamp.","","1815",W),
 A("Clanny lamp","","William Reid Clanny's safety lamp, the first of its kind, later refined with glass and gauze.","","1813",W),
 A("Geordie lamp","Stephenson lamp","George Stephenson's safety lamp with the flame in glass and air admitted through small tubes.","","1815",W),
 A("Mueseler lamp","","Clanny-type lamp with an internal chimney and a locking base.","","1840",W),
 A("Carbide lamp","acetylene lamp","Lamp burning acetylene made by dripping water onto calcium carbide; used in mining, on bicycles and by cavers.","","c. 1900","https://en.wikipedia.org/wiki/Carbide_lamp")]})
json.dump(d,open('work/FIX_B3/B3.new.json','w'),ensure_ascii=False,indent=1)
json.dump(moves,open('work/FIX_B3/moves.new.json','w'),ensure_ascii=False,indent=1)
print(before,cnt(),sum(len(k.get('x',[])) for dp in d['depts'] for s in dp['s'] for k in s['k']))
