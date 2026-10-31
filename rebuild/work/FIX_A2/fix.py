import json,os
p='out/A2.json'
d=json.load(open(p))
def find(n):
    for dp in d['depts']:
        for s in dp['s']:
            for i,k in enumerate(s['k']):
                if k['n']==n: return dp,s,i,k
def dept(n): return [x for x in d['depts'] if x['n']==n][0]
AJ='https://en.wikipedia.org/wiki/Air_Jordan'
# A2-1
dp,s,i,bk=find('Basketball sneaker')
aj1=[x for x in bk['x'] if x['n']=='Air Jordan 1'][0]
bk['x']=[x for x in bk['x'] if x['n']!='Air Jordan 1']
aj1['v']=[v for v in aj1['v'] if v['n'] not in('Air Jordan III','Air Jordan IV','Air Jordan XI')]
models=[('2','1986','Peter Moore and Bruce Kilgore'),('3','1988',''),('4','1989','Tinker Hatfield'),('5','1990','Tinker Hatfield'),('6','1991',''),('7','1992',''),('8','1993',''),('9','1993',''),('10','1994',''),('11','1995','Tinker Hatfield'),('12','1996',''),('13','1997','Tinker Hatfield'),('14','1998','Tinker Hatfield and Mark Smith')]
xs=[aj1]
for n,y,des in models:
    xs.append({"n":"Air Jordan "+n,"a":"AJ"+n+" · Jordan "+n,"d":"Numbered Michael Jordan signature basketball shoe"+(f", designed by {des}" if des else "")+".","mk":"Nike","y":y,"s":AJ,"v":[],"dt":"OG and retro releases · colourway by style code"})
aj1['d']="Michael Jordan's first Nike signature basketball shoe, designed by Peter B. Moore; first of the numbered Air Jordan line."
s['k'].insert(i+1,{"n":"Air Jordan","a":"Jordan Brand numbered line · AJ","d":"Michael Jordan's numbered signature basketball shoe line, one archetype per model (I to XIV listed).","t":["High","Mid","Low"],"s":AJ,"x":xs,"m":[]})
# A2-2 / A2-3
dp,s,i,hk=find('Heritage running sneaker')
hx=hk['x']
oth=[x for x in hx if x['n']=='Air Max family (other models)'][0]
AM='https://en.wikipedia.org/wiki/Nike_Air_Max'
new=[("Air Max BW","Air Classic BW","1991","Air Max BW","Nike Air Max line model first released as the Air Classic BW."),
("Air Max 180","","1991","Air Max 180","Nike Air Max model with a larger visible air unit."),
("Air Max 93","","1993","Air Max 93","Nike Air Max model of 1993."),
("Air VaporMax","VaporMax","2017","Air VaporMax","Nike Air Max line model with the air unit forming the sole.")]
vers={v['n']:v for v in oth['v']}
newx=[]
for n,a,y,vk,dd in new:
    newx.append({"n":n,"a":a,"d":dd,"mk":"Nike","y":y,"s":AM,"v":[],"dt":"colourway by style code"})
oth['v']=[v for v in oth['v'] if v['n'] not in('Air Max BW','Air Max 180','Air Max 93','Air VaporMax')]
idx=hx.index(oth)
# Air Max 95 year fix not needed; insert after Air Max Plus
hx[idx:idx]=newx
oth['n']="Later Air Max models"
oth['d']="Air Max generations from the Light to the 270 and DN; each is listed as a version."
# new lifestyle icons
hx.append({"n":"Yeezy Boost 350","a":"350","d":"Primeknit adidas and Kanye West sneaker, worldwide launch 27 June 2015.","mk":"adidas","y":"2015","s":"https://en.wikipedia.org/wiki/Adidas_Yeezy","v":[{"n":"Yeezy Boost 350 V2","mk":"adidas","y":"2016","d":"debuted 24 September 2016 in the Beluga colourway"}],"dt":"colourways"})
hx.append({"n":"Air Huarache","a":"Huarache","d":"Nike running shoe introduced in 1992.","mk":"Nike","y":"1992","s":"https://en.wikipedia.org/wiki/Nike_Air_Huarache","v":[],"dt":"colourway by style code"})
hx.append({"n":"Gel-Kayano","a":"Kayano","d":"ASICS running line named after its designer Toshikazu Kayano; first released 1993.","mk":"ASICS","y":"1993","s":"https://en.wikipedia.org/wiki/Asics","v":[{"n":"Gel-Kayano 14","mk":"ASICS","y":"","d":"older model revived in fashion circles"}],"dt":"colourway"})
dp,s,i,ck=find('Chunky sneaker')
ck['x']=[x for x in ck['x'] if x['n']!='Triple S']
ck['x'].append({"n":"XT-6","a":"Salomon XT-6","d":"Trail-ready Salomon sneaker adopted by the fashion industry in 2023.","mk":"Salomon","y":"","s":"https://en.wikipedia.org/wiki/Salomon_Group","v":[],"dt":"colourway"})
# A2-2 Subculture shoes shelf
dd=dept('Dress & casual shoes')
dd['s'].append({"n":"Subculture shoes","k":[
{"n":"Brothel creeper","a":"creeper","d":"Shoe with a thick crepe-rubber sole, usually in suede, worn by Teddy Boys and later punk and goth scenes.","t":["Suede","Leather","Platform"],"s":"https://en.wikipedia.org/wiki/Brothel_creeper","x":[
 {"n":"Hamilton creeper","a":"","d":"Thick crepe-soled shoe first developed commercially by George Cox of Wellingborough in 1949 and sold under the Hamilton name.","mk":"George Cox","y":"1949","s":"https://en.wikipedia.org/wiki/Brothel_creeper","v":[],"dt":"suede upper · crepe sole thickness"}]},
{"n":"Dr. Martens lace-up","a":"DMs · Docs","d":"Air-cushioned-sole lace-up boot or shoe in the Dr. Martens numbering system, named for its year of introduction.","s":"https://en.wikipedia.org/wiki/Dr._Martens","x":[
 {"n":"1460","a":"8-eye boot","d":"Eight-eyelet boot, the brand's first, introduced 1 April 1960 in cherry-red smooth leather.","mk":"Dr. Martens","y":"1960","s":"https://en.wikipedia.org/wiki/Dr._Martens","v":[],"dt":"smooth leather · colours"},
 {"n":"1461","a":"3-eye shoe","d":"Three-eyelet shoe introduced in 1961, sister to the 1460.","mk":"Dr. Martens","y":"1961","s":"https://en.wikipedia.org/wiki/Dr._Martens","v":[],"dt":"smooth leather · colours"}]}]})
# A2-4
dp,s,i,pk=find('Peep-toe shoe')
cs=find('Court shoe')[3]
cs['t'].append('peep-toe (also on slingbacks and platforms)')
s['k'].pop(i)
fs=find('Insole'); sh=fs[1]
ins=fs[3]; hg=find('Heel grip')[3]
sh['k']=[k for k in sh['k'] if k['n'] not in('Insole','Heel grip')]
sh['k'].insert(fs[2],{"n":"Fit aids","a":"insole · heel grip","d":"Removable insoles and heel pads that change a shoe's comfort or fit, not medical orthotics.","t":["Insole","Heel grip"],"s":ins['s'],"m":ins['m']+hg['m'],"r":[]})
# A2-6
dp,s,i,jk=find('Jika-tabi')
sp=find('Split-toe work boot')
sp[1]['k'].pop(sp[2])
jk['m']=jk.get('m',[])+sp[3]['m']
jk['a']=jk['a'].replace('split-toe work boot · ','split-toe work boot · jika-tabi boot · ') if False else jk['a']
mt=[x for x in jk['x'] if x['n']=='Tabi (Margiela)'][0]
jk['x']=[x for x in jk['x'] if x is not mt]
mt['n']='Tabi'; mt['a']='Margiela Tabi'
find('Designer sneaker')[3]['x'].append(mt)
vs=find('Skate shoe'); so=find('Slip-on sneaker')
vs[3]['x'].append(so[3]['x'][0]); vs[3]['a']=(vs[3].get('a','')+' · slip-on').strip(' ·')
so[1]['k'].pop(so[2])
json.dump(d,open('out/A2.tmp','w'),ensure_ascii=False,indent=1)
os.replace('out/A2.tmp',p)
# A2-7 traditions
t=json.load(open('out/A2_traditions.json'))
for x in t['t']:
    if x['g']=='Leather & footwear': x['g']='Footwear & leather'
json.dump(t,open('out/A2_traditions.tmp','w'),ensure_ascii=False,indent=1)
os.replace('out/A2_traditions.tmp','out/A2_traditions.json')
