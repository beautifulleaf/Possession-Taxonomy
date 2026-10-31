import json,copy,os
P='out/J2.json'
d=json.load(open(P))
def pos(name):
  for dp in d['depts']:
    for s in dp['s']:
      for i,k in enumerate(s['k']):
        if k['n']==name: return s,i,k
def take(name):
  s,i,k=pos(name); s['k'].pop(i); return k
# J2-3 sturgeon caviar
names=['Beluga caviar','Osetra caviar','Sevruga caviar','Kaluga caviar','Siberian sturgeon caviar','White sturgeon caviar','Amur sturgeon caviar','Hybrid sturgeon caviar','Sterlet caviar']
shelf,idx,_=pos('Beluga caviar')
ks={n:take(n) for n in names}
pressed=take('Pressed caviar'); hack=take('Hackleback caviar'); pad=take('Paddlefish caviar'); bow=take('Bowfin roe')
lab={'Beluga caviar':'Beluga (Huso huso)','Osetra caviar':'Osetra (Acipenser gueldenstaedtii)','Sevruga caviar':'Sevruga (Acipenser stellatus)','Kaluga caviar':'Kaluga (Huso dauricus)','Siberian sturgeon caviar':'Baerii (Siberian sturgeon)','White sturgeon caviar':'White sturgeon (Acipenser transmontanus)','Amur sturgeon caviar':'Amur sturgeon (Acipenser schrenckii)','Hybrid sturgeon caviar':'Hybrid sturgeon','Sterlet caviar':'Sterlet (Acipenser ruthenus)'}
xs=[];models=[]
for n in names:
  k=ks[n]
  vs=[]
  for h in k.get('x',[]):
    vs.append({"n":h['n'],"mk":h.get('mk',''),"y":h.get('y',''),"d":h['d']})
  a={"n":lab[n],"a":k.get('a',''),"d":k['d'],"mk":"","y":"","s":k['s'],"v":vs,"dt":' · '.join(k.get('t',[]))}
  xs.append(a); models+=k.get('m',[])
models+=pressed.get('m',[])
models=[m for m in models if m[0]!='Siberian osetra']
seen=set();mm=[]
for m in models:
  key=tuple(m)
  if key in seen: continue
  seen.add(key); mm.append(m)
sturgeon={"n":"Sturgeon caviar","a":"black caviar · caviar","d":"Salted roe of sturgeon species, sold as separate grains or pressed, listed by species with caviar houses as versions.","t":["malossol","farmed","pressed (payusnaya, mixed species)"],"s":ks['Beluga caviar']['s'],"x":xs,"m":mm}
shelf['k'].insert(idx,sturgeon)
amer={"n":"American roe","a":"American caviar","d":"Roe of North American fish sold as caviar or black roe: shovelnose, paddlefish and bowfin.","t":["wild","black"],"s":hack['s'],"x":[
 {"n":"Hackleback (shovelnose sturgeon)","a":hack['a'],"d":hack['d'],"mk":"","y":"","s":hack['s'],"v":[],"dt":"American · wild"},
 {"n":"Paddlefish","a":pad['a'],"d":pad['d'],"mk":"","y":"","s":pad['s'],"v":[],"dt":"American · wild"},
 {"n":"Bowfin","a":bow['a'],"d":bow['d'],"mk":"","y":"","s":bow['s'],"v":[],"dt":"black · Louisiana"}]}
shelf['k'].insert(idx+1,amer)
# J2-4 snails
sn=[take(n) for n in ['Periwinkle','Top shell','Mud snail','Apple snail','Conch']]
s,i,w=pos('Whelk')
snail={"n":"Sea & freshwater snails","a":"periwinkle · winkle · conch · top shell · mud snail · apple snail","d":"Sea and freshwater snails other than whelk sold for eating, whole in the shell or as meat.","t":["periwinkle","queen conch (frozen meat)","top shell (turban shell)","mud snail (field snail)","apple snail (freshwater)","in shell","meat"],"s":sn[0]['s']}
s.__setitem__('k',s['k'][:i+1]+[snail]+s['k'][i+1:])
# J2-5 tuna cut grades into criterion
s,i,t=pos('Tuna')
cuts=['loin','saku block','akami','chutoro','otoro','sashimi grade']
t['t']=[x for x in t['t'] if x not in cuts]
d['b'].append({"m":"Tuna cut and sashimi grade","v":"akami (lean) · chutoro (medium fat) · otoro (fattiest) · saku block · loin · sashimi grade","w":"Japanese cut names used on raw tuna labels, applied across bluefin, yellowfin and bigeye."})
t['d']=t['d'].replace(', sold whole, as loins, steaks or sashimi blocks',', sold whole, as loins, steaks or sashimi blocks (cut grades are listed under the department criteria)')
# J2-6
for k in [pos(n)[2] for n in ['Pacific salmon','Vinegar-marinated sea bream']]:
  for a in k['x']:
    if a['n']=='みやぎサーモン': a['a']='みやぎサーモン · Miyagi salmon · Miyagi sāmon'; a['n']='Miyagi Salmon'
    if a['n']=='若狭小浜小鯛ささ漬': a['a']='若狭小浜小鯛ささ漬 · Wakasa Obama kodai sasazuke · Wakasa Obama kodai sasazuke GI'; a['n']='Wakasa Obama small sea bream sasazuke'
# J2-2
pos('Tuna')[2].setdefault('x',[]).append({"n":"Ōma tuna","a":"Oma maguro · 大間マグロ","d":"Bluefin tuna landed at Ōma, Aomori, caught by hand in two-person boats and sold under the registered Ōma brand.","mk":"","y":"","s":"https://en.wikipedia.org/wiki/Oma,_Aomori","v":[],"dt":"bluefin · hand-caught · Aomori"})
mk=pos('Mackerel & horse mackerel')[2]
mk.setdefault('x',[]).extend([
 {"n":"Seki-aji","a":"Sekiaji · 関あじ","d":"Horse mackerel (aji) caught by one-hook fishing in the Hōyo Strait off Saganoseki, Oita; the cooperative tags only fish caught and delivered properly.","mk":"","y":"","s":"https://oitaisan.com/english/heritage/sekiajisekisaba","v":[],"dt":"one-hook caught · live-well transport · brand tag"},
 {"n":"Seki-saba","a":"Sekisaba · 関さば","d":"Mackerel (saba) caught by one-hook fishing in the Hōyo Strait off Saganoseki, Oita; sold with the cooperative's brand tag.","mk":"","y":"","s":"https://oitaisan.com/english/heritage/sekiajisekisaba","v":[],"dt":"one-hook caught · live-well transport · brand tag"}])
# J2-1 Comur eel archetype
pos('Tinned eel')[2].setdefault('x',[]).append({"n":"Comur eel in pickled sauce","a":"enguias em escabeche","d":"Eels in pickled sauce, the regional product that became the calling card of Comur of Murtosa, near Aveiro.","mk":"Comur","y":"1942","s":"https://app.ckbk.com/section/best16392c09s001/comur","v":[],"dt":"pickled sauce · tin"})
json.dump(d,open('work/FIX_J2/J2.tmp','w'),ensure_ascii=False,indent=1)
os.replace('work/FIX_J2/J2.tmp',P)
# brands
B='out/J2_brands.json'
b=json.load(open(B))
def br(n,c,f,seg,kf,dd,s,sig=[]):
  return {"n":n,"c":c,"f":f,"seg":seg,"kf":kf,"d":dd,"lines":[],"eras":[],"sig":sig,"sc":[],"rel":[],"s":s}
nm={x['n'].lower() for x in b['b']}
new=[br("Fishwife","United States","2020","Artisan & independent","Modern tinned seafood","Los Angeles tinned seafood company launched in December 2020, focused on trout and tuna in conservas-style packaging.","https://brownalumnimagazine.com/articles/2021-08-19/the-new-fishwife"),
 br("José Gourmet","Portugal","2008","Premium","Portuguese conservas","Canned-fish brand of 100 Mistérios (Perafita, Porto), established 2008 to revive Portuguese canned fish.","https://www.gourmets.net/salon-gourmets/2024/exhibitors-catalogue/jose-gourmet-by-100-misterios"),
 br("Comur","Portugal","1942","Heritage manufactory","Eels in pickled sauce","Cannery of Murtosa near Aveiro, founded 1942, known for eels in pickled sauce and smoked canned fish.","https://app.ckbk.com/section/best16392c09s001/comur",["Comur eel in pickled sauce"]),
]
for n,kf,dd in [("Herpac","Bluefin and yellowfin tuna","Tinned bluefin and yellowfin tuna cuts, including bluefin loin and belly."),("Olasagasti","White tuna fillets","Cannery named as one where the tradition of singing on shore took hold; sells white tuna fillets in olive oil."),("Carmelo","Tuna fillets in olive oil","Tuna fillets in organic extra virgin olive oil in green and yellow packaging."),("Angelachu","Bonito del Norte","Conservas brand selling white tuna fillets in organic extra virgin olive oil.")]:
  new.append(br(n,"","","Specialist",kf,dd,"https://www.thetinnedfishmarket.com/blogs/guides-to-tinned-fish/bonito-del-norte-tuna"))
for x in new:
  if x['n'].lower() not in nm: b['b'].append(x)
b['b'].sort(key=lambda x:x['n'].lower())
json.dump(b,open('work/FIX_J2/b.tmp','w'),ensure_ascii=False,indent=1); os.replace('work/FIX_J2/b.tmp',B)
