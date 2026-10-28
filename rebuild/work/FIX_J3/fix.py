import json,os,copy
P='out/'
d=json.load(open(P+'J3.json')); B=json.load(open(P+'J3_brands.json')); mv=json.load(open(P+'J3_moves.json'))
dept=lambda n:[x for x in d['depts'] if x['n']==n][0]
def shelf(dp,n):return [s for s in dp['s'] if s['n']==n][0]
def kind(sh,n):return [k for k in sh['k'] if k['n']==n][0]
def arch(n,d_,mk,y,s,dt='',v=None,a=''):
    return {"n":n,"a":a,"d":d_,"mk":mk,"y":y,"s":s,"v":v or [],"dt":dt}
ch=dept('Cheese')
W='https://en.wikipedia.org/wiki/'
# --- new archetypes
kind(shelf(ch,'Soft white-rind cheese'),'Double- & triple-cream cheese')['x'].append(
 arch("Mt Tam","Californian triple-cream cheese resembling Explorateur, named after Mount Tamalpais.","Cowgirl Creamery","",W+'Cowgirl_Creamery'))
kind(shelf(ch,'Washed-rind cheese'),"Vacherin Mont-d'Or")['x'].append(
 arch("Harbison","Soft-ripened cow's-milk cheese from Jasper Hill Farm, Vermont; Best of Show at the 2018 American Cheese Society competition.","Jasper Hill Farm","",W+'Jasper_Hill_Farm'))
kind(shelf(ch,'Spanish, Portuguese & Latin American cheese'),'Spanish goat cheese')['x'].append(
 arch("Garrotxa","Catalan goat's-milk cheese with a powdery grey rind, near extinct by the early 1980s and revived from 1981.","","1981 revival",W+'Garrotxa_cheese'))
kind(shelf(ch,'Italian grana, pecorino & pressed cheese'),'Pecorino')['x'].append(
 arch("Casu marzu","Sardinian sheep's-milk pecorino deliberately infested with cheese-fly larvae; sale banned in Italy and the EU.","","",W+'Casu_martzu'))
kind(shelf(ch,'Dutch & Nordic cheese'),'Edam')['x'].append(
 arch("Mini Babybel","Small round Edam-style cheese from pasteurised milk in a coloured wax coating, made by the Bel Group.","Bel Group","1952",W+'Babybel'))
kind(shelf(ch,'Regional pressed cheese'),'Roomi') # existence check
shelf(ch,'Regional pressed cheese')['k'].append({"n":"Mimolette","a":"","d":"French hard cheese traditionally made around Lille, orange from annatto, aged two months to two years.","s":W+'Mimolette',
 "x":[arch("Mimolette","French hard orange cheese traditionally made around Lille, coloured with annatto.","","",W+'Mimolette',"aged two months to two years",[{"n":"Mimolette extra-vieille","d":"Longest-aged grade."}])]})
# --- new pressed sheep shelf
sp=shelf(ch,'Spanish, Portuguese & Latin American cheese'); it=shelf(ch,'Italian grana, pecorino & pressed cheese'); rg=shelf(ch,'Regional pressed cheese')
def pop(sh,n):
    k=kind(sh,n); sh['k'].remove(k); return k
new={"n":"Pressed uncooked sheep cheese","k":[pop(sp,'Manchego'),pop(rg,'Pyrenean sheep cheese'),pop(it,'Pecorino'),pop(sp,'Idiazábal & Roncal'),
 {"n":"Zamorano","a":"","d":"Hard Spanish sheep's-milk cheese from Zamora province, with protected designation of origin.","s":W+'Zamorano_cheese',
  "x":[arch("Zamorano PDO","Hard sheep's-milk cheese of Zamora province, Spain.","","",W+'Zamorano_cheese')]},
 {"n":"Oscypek","a":"","d":"Smoked salted sheep's-milk cheese of Poland's Tatra region, PDO since 2008.","s":W+'Oscypek',
  "x":[arch("Oscypek PDO","Smoked salted cheese made with at least 60% sheep's milk in the Tatra region of Poland.","","PDO 2008",W+'Oscypek')]},
 {"n":"Pag cheese","a":"Paški sir","d":"Firm sheep's-milk cheese from the Adriatic island of Pag, Croatia, PDO since 2019.","s":W+'Pag_cheese',
  "x":[arch("Paški sir PDO","Firm sheep's-milk cheese of Pag island, Croatia.","","PDO 2019",W+'Pag_cheese')]}]}
i=d['depts'].index(ch); ch['s'].insert(ch['s'].index(it)+1,new)
# --- eggs
eg=shelf(dept('Eggs'),'Eggs'); duck=pop(eg,'Duck egg'); pop(eg,'Quail egg')
eg['k'].insert(1,{"n":"Eggs from other birds","a":"duck egg · quail egg · goose egg","d":"Eggs of ducks, quail and geese sold raw in the shell, distinguished by type rather than kind.","t":["duck","quail","goose"],"s":duck['s']})
# --- meat alternatives out
td=dept('Tofu, tempeh & meat alternatives'); ts=td['s'][0]
for n in('Plant-based meat','Mycoprotein','Seitan'):
    mv['out'].append({"to":"J1","dept":"Meat alternatives","kind":pop(ts,n)})
td['n']='Tofu, tempeh & yuba'; ts['n']='Tofu, tempeh & yuba'
# --- brands
b=B['b']; bn={x['n']:x for x in b}
cg=bn['Cypress Grove']; cc=bn.pop('Cypress Grove Chevre'); b.remove(cc)
cg['lines']=["Midnight Moon","Humboldt Fog"]; cg['sig']=["Humboldt Fog","Goat's-milk Gouda"]
cg['d']="Goat-cheese maker in Arcata, California, known for Humboldt Fog; Midnight Moon is made for it in Holland."
def walk():
    for dp in d['depts']:
        for s in dp['s']:
            for k in s['k']:
                for x in k.get('x',[]):
                    yield x
                    for v in x.get('v',[]): yield v
for x in walk():
    if x.get('mk')=='Cypress Grove Chevre': x['mk']='Cypress Grove'
for x in mv['out']:pass
add=[("Fromagerie Lincet","France","","Artisan & independent","triple-cream","Fifth-generation Burgundian dairy at Saligny, maker of Délice de Bourgogne, created by Jean Lincet in 1975.",W+'D%C3%A9lice_de_Bourgogne'),
("Žemaitijos Pienas","Lithuania","1924","Mainstream","hard cheese","Dairy in Telšiai, Lithuania, maker of Džiugas.","https://www.dairyreporter.com/Article/2019/08/12/Lithuanian-cheese-Dziugas-gets-PGI-status/"),
("Cowgirl Creamery","United States","1994","Artisan & independent","triple-cream","Petaluma, California, cheesemaker; maker of Mt Tam.",W+'Cowgirl_Creamery'),
("Bel Group","France","1865","Mainstream","snack cheese","French food company behind The Laughing Cow, Babybel, Kiri and Boursin.",W+'Bel_Group'),
("Sargento","United States","1953","Mainstream","packaged cheese","Wisconsin food company known mainly for packaged cheese products.",W+'Sargento')]
for n,c,f,seg,kf,dd,s in add:
    if n in bn: continue
    b.append({"n":n,"c":c,"f":f,"seg":seg,"d":dd,"lines":[],"eras":[],"sig":[],"sc":[],"rel":[],"s":s,"kf":kf})
json.dump(d,open(P+'J3.json.tmp','w'),ensure_ascii=False,indent=1);os.replace(P+'J3.json.tmp',P+'J3.json')
json.dump(B,open(P+'J3_brands.json.tmp','w'),ensure_ascii=False,indent=1);os.replace(P+'J3_brands.json.tmp',P+'J3_brands.json')
json.dump(mv,open(P+'J3_moves.json.tmp','w'),ensure_ascii=False,indent=1);os.replace(P+'J3_moves.json.tmp',P+'J3_moves.json')
