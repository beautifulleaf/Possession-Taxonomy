import json,sys,os,re
sys.path.insert(0,'.')
from data_varieties import *
O='/home/user/Possession-Taxonomy/rebuild/out/'
d=json.load(open(O+'J6.json')); B=json.load(open(O+'J6_brands.json'))
reg={b['n']:b for b in B['b']}
W="https://en.wikipedia.org/wiki/"
S_JDE=W+"JDE_Peet%27s"; S_COF=W+"List_of_coffee_companies"; S_TEA=W+"List_of_tea_companies"
K={}
for dp in d['depts']:
    for s in dp['s']:
        for k in s['k']: K[k['n']]=k
def dept(n): return [x for x in d['depts'] if x['n']==n][0]
def low(s): return s.lower()
def have(k,n): return any(low(x['n'])==low(n) for x in k.get('x',[]))
def ent(k,n,dd,s,own=None,tier=None,cty=None,own_y=None,y="",mk="",g=None,v=None,a="",role=None,dt=None):
    if have(k,n): 
        return
    e={"n":n,"a":a,"d":dd,"mk":mk or (own or ""),"y":y,"s":s,"v":v or []}
    if own: e["own"]=own
    if tier: e["tier"]=tier
    if cty: e["cty"]=cty
    if own_y: e["own_y"]=own_y
    if g: e["g"]=g
    if role: e["role"]=role
    if dt: e["dt"]=dt
    k.setdefault('x',[]).append(e)
def setf(k,n,**f):
    for x in k.get('x',[]):
        if low(x['n'])==low(n): x.update({a:b for a,b in f.items() if b}); return
    raise SystemExit("missing "+n)
def V(n,mk="",y="",dd=""): return {"n":n,"mk":mk,"y":y,"d":dd}
def rs(n): return reg[n]
G="Global group";NC="National champion";IND="Independent";CR="Craft & indie";OL="Own label"
def nl_sel(k,nl,sel):
    k['nl']=nl; k['sel']=sel

# ---------- Coffee varieties (WCR) ----------
kv=K['Geisha & rare-variety coffee']
old={x['n']:x for x in kv['x']}
alias={'Geisha (Panama)':'Geisha / Gesha','Bourbon Mayaguez 139':None}
keep=[]
by={low(x['n']):x for x in kv['x']}
def find(n):
    m={'geisha (panama)':'geisha / gesha','harar rwanda':None}
    return by.get(m.get(low(n),low(n))) if low(n) in m or low(n) in by else None
new=[]
for n,al,g,dd in ARABICA:
    x=find(n)
    if x is None:
        x={"n":n,"a":al,"d":dd,"mk":"","y":"","s":U,"v":[],"dt":"WCR arabica catalogue"}
    x['g']="Origin: "+g if g!=NS else "Origin: not stated in the WCR listing"
    if g in(CAT,SAR): x['g']="Genetic group: "+g.replace(' group','')
    if n=="Nemaya (Coffea canephora)": x['g']="Robusta rootstock"
    new.append(x)
names={low(x['n']) for x in new}|{'geisha / gesha'}
for x in kv['x']:
    if low(x['n']) not in {low(y['n']) for y in new}:
        x['g']="Not in the WCR catalogue (Wikipedia list of coffee varieties)"; new.append(x)
for x in new:
    if x['n'] in('Typica','Bourbon','Geisha / Gesha'): x['role']='landmark'
kv['x']=new
nl_sel(kv,"One entry is a named arabica variety (cultivar or selection) that the World Coffee Research catalogue describes.",
 f"Follows the World Coffee Research arabica varieties catalogue ({U}), every variety it lists, plus four varieties kept from the Wikipedia list of coffee varieties that the catalogue omits; sections give the origin or genetic group the listing names. Complete: {len(ARABICA)} of {len(ARABICA)} in the catalogue listing (an older text on the site gives 55).")
kv['n']='Coffee varieties'
rn={"Geisha & rare-variety coffee":"Coffee varieties"}
# robusta
kr=K['Speciality Robusta, Liberica & Excelsa']
for n,al,g,dd in ROBUSTA:
    kr.setdefault('x',[]).append({"n":n,"a":al,"d":dd,"mk":"","y":"","s":R,"v":[],"g":("Origin: "+g) if g!=NS else "Origin: not stated in the WCR listing","dt":"WCR robusta catalogue"})
for x in kr['x']:
    x.setdefault('g',"Liberica and others (Wikipedia)")
nl_sel(kr,"One entry is a named robusta clone or variety from the World Coffee Research catalogue, or a named liberica coffee.",
 f"Follows the World Coffee Research robusta catalogue ({R}), every variety it lists, with sections by the country the listing names. Complete: {len(ROBUSTA)} of {len(ROBUSTA)} robusta varieties in the catalogue; liberica and excelsa coffees are covered only by the one entry kept from the earlier edition.")

# ---------- Coffee brands: market layer ----------
k=K['Everyday ground & filter coffee']
for x in k['x']:
    if x['n']=="Café Bustelo": x.update(own="The J.M. Smucker Company",tier=NC,cty="United States",own_y="2011")
ent(k,"Douwe Egberts","Dutch brand of ground and instant coffee, part of JDE Peet's.",rs("Douwe Egberts")['s'],"JDE Peet's",G,"Netherlands",y="1753",g="Global group: JDE Peet's")
ent(k,"Jacobs","German filter-coffee brand of JDE Peet's.",S_JDE,"JDE Peet's",G,"Germany",g="Global group: JDE Peet's")
ent(k,"Kenco","British coffee brand of JDE Peet's.",S_JDE,"JDE Peet's",G,"United Kingdom",g="Global group: JDE Peet's")
ent(k,"Maxwell House","American brand founded in 1892; Kraft Heinz owns it in North America and JDE Peet's elsewhere.",rs("Maxwell House")['s'],"Kraft Heinz (North America); JDE Peet's (elsewhere)",NC,"United States",y="1892",g="National champion: United States",v=[V("Maxwell House (outside North America)","JDE Peet's")])
ent(k,"Folgers","San Francisco brand of ground coffee, owned by J.M. Smucker since 2008.",rs("Folgers")['s'],"The J.M. Smucker Company",NC,"United States",own_y="2008",y="1850",g="National champion: United States")
ent(k,"Lavazza","Turin family firm with over 36 % of sales in Italy; its Qualità Rossa is a filter-coffee blend.",W+"Lavazza","Lavazza family (Luigi Lavazza S.p.A.)",NC,"Italy",y="1895",g="National champion: Italy",v=[V("Qualità Rossa","Lavazza")])
ent(k,"Tchibo","Hamburg roaster and retailer that became German market leader after buying Eduscho in 1997.",W+"Tchibo","Maxingvest AG",NC,"Germany",y="1949",g="National champion: Germany",v=[V("Eduscho Filterkaffee Nr. 1 Klassisch","Tchibo")])
ent(k,"Melitta","German company founded in 1908 around Melitta Bentz's paper filter.",W+"Melitta","Melitta Group",IND,"Germany",y="1908",g="Independent: Germany",v=[V("Melitta Auslese Klassisch","Melitta")])
ent(k,"Paulig","Helsinki family roaster founded in 1876 whose coffee brands the page says continued to dominate the Finnish market.",W+"Paulig","Paulig family",NC,"Finland",y="1876",g="National champion: Finland")
ent(k,"Cafédirect","Fairtrade coffee brand founded in the United Kingdom in 1991.",S_COF,"Cafédirect",IND,"United Kingdom",y="1991",g="Independent: United Kingdom",v=[V("Fairtrade Colombia Reserva","Cafédirect")])
ent(k,"Eight O'Clock Coffee","American brand founded in 1859, part of Tata Consumer Products since 2006.",S_COF,"Tata Consumer Products",G,"United States",own_y="2006",y="1859",g="Global group: Tata Consumer Products",v=[V("100% Colombian","Eight O'Clock Coffee")])
ent(k,"Dunkin' Donuts","American chain founded in 1950 whose coffee is also sold packaged.",S_COF,"",IND,"United States",y="1950",g="Independent: United States")
for x in k['x']:
    if x['n']=="Dunkin' Donuts": x.pop('own',None)
nl_sel(k,"One entry is a packaged-coffee brand sold ground or whole-bean for filter and moka brewing; blends and packs are versions.",
 f"Brand list from the fetched JDE Peet's, Lavazza, Tchibo, Paulig, Melitta and Tata Consumer pages and the Wikipedia list of coffee companies ({S_COF}); owners and years as those pages state them. Covers {len(k['x'])} brands of about 80 on that list; no complete ranked list of packaged coffee brands exists.")
k.pop('m',None)

k=K['Espresso blends']
ent(k,"Lavazza","Turin family firm; Qualità Oro, Super Crema and Qualità Rossa are its best-known espresso blends.",W+"Lavazza","Lavazza family (Luigi Lavazza S.p.A.)",NC,"Italy",y="1895",g="National champion: Italy",v=[V("Qualità Oro","Lavazza"),V("Super Crema","Lavazza"),V("Qualità Rossa","Lavazza")])
ent(k,"illy","Trieste family firm founded in 1933 that sells one house blend.",W+"Illy","Illy family (illycaffè S.p.A.)",IND,"Italy",y="1933",g="Independent: Italy",v=[V("illy classico blend","illy")])
setf(k,"Mocha-Java",g="Historic blend")
nl_sel(k,"One entry is a blend or roaster line sold for espresso; its blends are versions.","Brands from the fetched Lavazza and Illy pages. No complete reference for espresso blends exists, so this is not exhaustive.")
k.pop('m',None);k.pop('r',None)

k=K['Decaffeinated coffee']
ent(k,"New England Coffee","American roaster founded in 1916.",S_COF,"",IND,"United States",y="1916",g="Independent: United States",v=[V("Decaffeinated Colombian","New England Coffee")])
ent(k,"Nescafé Azera","Nestlé ground-and-instant coffee line with an Americano decaf.",W+"Nescaf%C3%A9","Nestlé",G,"Switzerland",g="Global group: Nestlé",v=[V("Azera Americano Decaff","Nestlé")])
ent(k,"Lavazza","Italian roaster with a ground decaf.",W+"Lavazza","Lavazza family (Luigi Lavazza S.p.A.)",NC,"Italy",y="1895",g="National champion: Italy",v=[V("Ground Decaf","Lavazza")])
ent(k,"illy","Italian roaster with a decaffeinated ground coffee.",W+"Illy","Illy family (illycaffè S.p.A.)",IND,"Italy",y="1933",g="Independent: Italy",v=[V("Decaffeinated Ground Coffee","illy")])
ent(k,"Dunkin' Donuts","American chain; sells a decaf.",S_COF,"",IND,"United States",y="1950",g="Independent: United States",v=[V("Dunkin' Decaf","Dunkin'")])
for x in k['x']:
    x.pop('own',None) if x['n']=="Dunkin' Donuts" else None
setf(k,"Café HAG",own="JDE Peet's",tier=G,cty="Germany",g="Global group: JDE Peet's")
nl_sel(k,"One entry is a decaffeination process or a brand's decaffeinated line; blends are versions.","Brands from the fetched JDE Peet's, Lavazza and Illy pages and the list of coffee companies. No complete reference exists.")
k.pop('m',None)

k=K['Coffee capsules & pods']
for n,o,t,c,oy in (("Nespresso Original","Nestlé",G,"Switzerland",None),("Nespresso Vertuo","Nestlé",G,"Switzerland",None),("Keurig K-Cup","Keurig Dr Pepper",G,"United States",None),("Nescafé Dolce Gusto","Nestlé",G,"Switzerland",None),("Lavazza A Modo Mio","Lavazza family (Luigi Lavazza S.p.A.)",NC,"Italy",None),("illy iperEspresso","Illy family (illycaffè S.p.A.)",IND,"Italy",None),("Senseo pad","JDE Peet's",G,"Netherlands",None),("Tassimo T-Disc","JDE Peet's",G,"Germany",None)):
    try: setf(k,n,own=o,tier=t,cty=c)
    except SystemExit: pass
ent(k,"L'OR","Capsule and pod brand of JDE Peet's.",S_JDE,"JDE Peet's",G,"France",g="Global group: JDE Peet's",v=[V("Lungo Profondo","L'OR"),V("Espresso Supremo","L'OR")])
for x in k['x']:
    if x['n']=="Nespresso Original": x['v'].append(V("Ispirazione Firenze Arpeggio","Nespresso"))
    if x['n']=="illy iperEspresso":
        x['v']+= [V("Classico Pods Mild and Balanced","illy"),V("Iperespresso Brazil Single Origin","illy")]
    if x['n']=="Lavazza A Modo Mio": x['v'].append(V("Espresso Passionale","Lavazza"))
nl_sel(k,"One entry is a capsule, pod or pad system that fits one machine family; roasts are versions.","Systems from the fetched Nestlé, Keurig Dr Pepper, JDE Peet's and Lavazza pages. No complete list of capsule systems exists; this is a selection of the established systems.")
k.pop('m',None)

k=K['Instant coffee']
for n,o,t,c in (("Nescafé spray-dried instant","Nestlé",G,"Switzerland"),("Camp Coffee","Reckitt (not stated on fetched page)",None,"United Kingdom"),("Starbucks VIA Ready Brew","Nestlé (licence from Starbucks, 2018)",None,"United States"),("Nescafé Taster's Choice","Nestlé",G,"Switzerland")):
    try:
        setf(k,n,own=o,cty=c,tier=t)
    except SystemExit: pass
for x in k['x']:
    if x['n']=="Camp Coffee": x.pop('own',None); x.pop('tier',None)
    if x['n']=="Starbucks VIA Ready Brew": x['own']="Starbucks Corporation"; x['tier']=G
    if x['n']=="Nescafé spray-dried instant": x['v'].append(V("Nescafé Gold Blend","Nestlé"))
ent(k,"Douwe Egberts Pure Gold","Instant coffee of the Dutch Douwe Egberts brand, part of JDE Peet's.",rs("Douwe Egberts")['s'],"JDE Peet's",G,"Netherlands",g="Global group: JDE Peet's",y="")
nl_sel(k,"One entry is an instant-coffee brand or process; its lines are versions.","Brands from the fetched Nescafé, Nestlé and JDE Peet's pages. No complete list of instant coffee exists; this is a selection.")
k.pop('m',None)

# single origin / green: remove origin rows (no canon)
for n in('Single-origin coffee','Green coffee','Cold brew & coffee concentrate'): K[n].pop('m',None); K[n].pop('r',None)
K['Single-origin coffee']['nl']="One entry is a protected or auction-sold coffee origin; estates and cooperatives are versions."
K['Single-origin coffee']['sel']="Origins kept from the earlier edition, each backed by a fetched page. No whole-space reference exists; origin names as sold (Yirgacheffe, Sumatra, Gayo and others) are descriptions in the text, not separate entries."
K['Traditional regional coffee']['nl']="One entry is a regional coffee preparation sold as ground or prepared coffee."
K['Traditional regional coffee']['sel']="Kept from the earlier edition, each backed by a fetched page. No whole-space reference exists."
K['Special-process coffee']['nl']="One entry is a coffee defined by an unusual process or animal passage."
K['Special-process coffee']['sel']="Kept from the earlier edition; no whole-space reference exists."

# ---------- Tea ----------
T=W+"List_of_Chinese_teas"
k=K['Chinese green tea']
for n,a,dd in (("Baimao Hou","","Green tea named on the Chinese tea list."),("Chun Mee","","Green tea named on the Chinese tea list."),("Da Fang","","Green tea named on the Chinese tea list."),("Mengding Ganlu","","Green tea named on the Chinese tea list."),("Zhuyeqing","","Green tea named on the Chinese tea list.")):
    ent(k,n,dd,T,g="Green (Chinese tea list)",a=a)
nl_sel(k,"One entry is a named Chinese green tea.","Follows the Wikipedia list of Chinese teas (45 teas, fetched), the green teas on it; entries kept from the earlier edition cover further teas. Complete: all 11 green teas on that list (Lu'an Melon Seed is Lu'an Guapian, Pouchong is under Taiwanese oolong).")
k=K['Chinese & Taiwanese black tea']
ent(k,"Congou","Black tea named on the Chinese tea list.",T,g="Black (Chinese tea list)")
ent(k,"Golden Monkey tea","Black tea named on the Chinese tea list.",T,g="Black (Chinese tea list)")
nl_sel(k,"One entry is a named Chinese or Taiwanese black tea.","Follows the black teas on the Wikipedia list of Chinese teas (fetched); Taiwanese teas are kept from the earlier edition. Complete: all 7 black teas on that list (Keemun, Dianhong, Lapsang souchong, Jin Jun Mei, Yingdehong, Congou, Golden Monkey; Fu Cha is dark tea).")
k=K['Wuyi rock oolong']
for n in("Ban Tian Yao","Bu Zhi Chun","Qilan","Shui Jin Gui"): ent(k,n,"Oolong named on the Chinese tea list.",T,g="Oolong (Chinese tea list)")
nl_sel(k,"One entry is a named Wuyi rock oolong.","Follows the oolongs on the Wikipedia list of Chinese teas (fetched); the list does not state provinces, so oolongs of unstated origin are in the next kind.")
k=K['Tieguanyin & Anxi oolong']
for n in("Fo Shou","Huang Guanyin","Huang Meigui","Jin Fo","Jin Suo Chi","Ruan Zhi"): ent(k,n,"Oolong named on the Chinese tea list; the list does not state its origin.",T,g="Oolong, origin not stated (Chinese tea list)")
nl_sel(k,"One entry is a named oolong from Anxi or one the source does not place.","Follows the oolongs on the Wikipedia list of Chinese teas (fetched). Complete: all 16 oolongs on that list are entries across this kind and Wuyi rock oolong (Pouchong is under Taiwanese oolong).")
for n,t in(("Taiwanese oolong","One entry is a named Taiwanese oolong."),("White tea","One entry is a named white tea."),("Yellow tea","One entry is a named yellow tea."),("Korean green tea","One entry is a named Korean green tea.")):
    K[n]['nl']=t
K['Taiwanese oolong']['sel']="Kept from the earlier edition; Pouchong (Baozhong) also appears on the Wikipedia list of Chinese teas. No whole-space reference was fetched."
K['White tea']['sel']="Follows the white teas on the Wikipedia list of Chinese teas (fetched). Complete: Baihao Yinzhen, Bai Mudan and Shou Mei are all entries; Gong Mei is kept from the earlier edition."
K['Yellow tea']['sel']="Follows the yellow teas on the Wikipedia list of Chinese teas (fetched). Complete: Huoshan Huangya and Junshan Yinzhen are entries; Meng Ding Huangya and Korean hwangcha are kept from the earlier edition."
K['Korean green tea']['sel']="Kept from the earlier edition; no whole-space reference exists."
for n in('Raw pu-erh (sheng)','Dark tea (hei cha)','Ripe pu-erh (shou)'):
    pass
K['Raw pu-erh (sheng)']['nl']="One entry is a pu-erh recipe number, mountain or factory line."
K['Raw pu-erh (sheng)']['sel']="Kept from the earlier edition; recipes and factories rest on the fetched Pu'er tea page. The Wikipedia list of Chinese teas has only the single entry Pu'er, so no complete list exists."
K['Dark tea (hei cha)']['nl']="One entry is a named dark tea."
K['Dark tea (hei cha)']['sel']="Kept from the earlier edition; the Chinese tea list adds only Fu Cha, which is Fu brick tea."
for n,t in(("Darjeeling tea","One entry is a Darjeeling estate or the Darjeeling indication."),("Assam & Indian black tea","One entry is a named Indian black tea or estate."),("Ceylon tea","One entry is a Sri Lankan tea-growing region."),("Kenyan, African & Black Sea tea","One entry is a named tea from Africa, Nepal or the Black Sea."),("Sencha & steamed green tea","One entry is a Japanese sencha type or cultivar."),("Gyokuro & kabusecha","One entry is a Japanese shaded tea or cultivar."),("Matcha","One entry is a matcha origin."),("Earl Grey & bergamot tea","One entry is a bergamot tea style."),("Jasmine & scented tea","One entry is a scented tea."),("Flavoured tea","One entry is a named flavoured blend."),("Breakfast & everyday black tea","One entry is a tea blend style or a packaged tea brand; packs and blends are versions.")):
    K[n]['nl']=t
    K[n]['sel']="Kept from the earlier edition with fetched sources; the Wikipedia pages on Japanese tea and the tea company list name the categories but no complete list of named Japanese, Indian or Sri Lankan teas was found." if n!="Breakfast & everyday black tea" else ""
k=K['Breakfast & everyday black tea']
ent(k,"PG Tips","British brand of pyramid bags, made by Lipton Teas and Infusions.",rs("PG Tips")['s'],"Lipton Teas and Infusions",G,"United Kingdom",own_y="2022",g="Global group: Lipton Teas and Infusions")
ent(k,"Lipton","Brand founded in Glasgow in 1871 (tea from 1890); Unilever kept it in India, Nepal and Indonesia and sold the rest to CVC in 2022.",W+"Lipton","Lipton Teas and Infusions (Unilever in India, Nepal, Indonesia)",G,"United Kingdom",own_y="2022",y="1871",g="Global group: Lipton Teas and Infusions")
ent(k,"Lyons","Irish and British brand of Lipton Teas and Infusions.",S_TEA,"Lipton Teas and Infusions",G,"United Kingdom",own_y="2022",g="Global group: Lipton Teas and Infusions")
ent(k,"Brooke Bond","Manchester brand founded in 1869; Lipton Teas and Infusions outside India.",rs("Brooke Bond")['s'],"Lipton Teas and Infusions (Hindustan Unilever in India)",G,"United Kingdom",y="1869",g="Global group: Lipton Teas and Infusions")
ent(k,"Red Rose Tea","Canadian brand founded in 1890; Lipton Teas and Infusions in Canada.",rs("Red Rose Tea")['s'],"Lipton Teas and Infusions (Teekanne in the United States)",G,"Canada",y="1890",g="Global group: Lipton Teas and Infusions")
ent(k,"Tetley","Tea brand bought by Tata for £271 million in 2000; second-biggest seller in the United Kingdom and United States, biggest in Canada.",W+"Tata_Consumer_Products","Tata Consumer Products",G,"United Kingdom",own_y="2000",g="Global group: Tata Consumer Products")
ent(k,"Twinings","London brand founded in 1706, owned by Associated British Foods since 1964.",W+"Twinings","Associated British Foods",G,"United Kingdom",own_y="1964",y="1706",g="Global group: Associated British Foods")
ent(k,"Yorkshire Tea","Taylors of Harrogate brand introduced in 1977; best-selling tea brand in Britain since 2019.",W+"Yorkshire_Tea","Bettys & Taylors Group",NC,"United Kingdom",y="1977",g="National champion: United Kingdom")
ent(k,"Typhoo","Birmingham brand launched in 1903; the tea company list names Apeejay Surrendra Group, while the earlier register says Supreme Imports bought it in December 2024.",rs("Typhoo")['s'],"Supreme Imports",IND,"United Kingdom",y="1903",g="Independent: United Kingdom")
ent(k,"Barry's Tea","Cork company founded in 1901.",rs("Barry's Tea")['s'],"Barry's Tea",NC,"Ireland",y="1901",g="National champion: Ireland")
ent(k,"Tapal","Karachi family firm founded in 1947 and described as one of the largest tea brands in Pakistan.",W+"Tapal_Tea","Tapal family",NC,"Pakistan",y="1947",g="National champion: Pakistan")
ent(k,"Çaykur","Turkish state tea company founded in 1983, held by the Turkey Wealth Fund.",W+"%C3%87aykur","Turkey Wealth Fund",IND,"Turkey",y="1983",g="Independent: Turkey",own_y="2017")
ent(k,"Ito En","Tokyo company founded in 1966; the page calls it Japan's largest green tea distributor.",W+"Ito_En","",NC,"Japan",y="1966",g="National champion: Japan")
for x in k['x']:
    if x['n']=="Ito En": x.pop('own',None)
k['sel']=f"Brands from the fetched Lipton, Twinings, Tata Consumer, Yorkshire Tea, Tapal, Çaykur and Ito En pages and the Wikipedia list of tea companies ({S_TEA}); owners as those pages state them. Covers {len(k['x'])} of about 120 companies on that list; English Breakfast and the other blend styles are kept from the earlier edition."
k['nl']="One entry is a blend style or a packaged tea brand sold for everyday brewing; blends and packs are versions."
for n in K:
    K[n].pop('m',None); K[n].pop('r',None)
K['Matcha']['see']=K['Matcha'].get('see')

# herbal brands
k=K['Herbal blend']
ent(k,"Celestial Seasonings","Boulder herbal tea company founded in 1969; Sleepytime dates to 1972; part of Hain Celestial.",rs("Celestial Seasonings")['s'],"The Hain Celestial Group",G,"United States",y="1969",g="Global group: Hain Celestial",v=[V("Sleepytime","Celestial Seasonings","1972")])
ent(k,"Yogi Tea","Organic herbal, green and black blends owned by East West Tea Company.",rs("Yogi Tea")['s'],"East West Tea Company",IND,"United States",g="Independent: United States")
ent(k,"Teekanne","German tea company; owns Red Rose in the United States.",S_TEA,"Teekanne",IND,"Germany",g="Independent: Germany")
ent(k,"TeaGschwendner","German tea retailer.",S_TEA,"TeaGschwendner",IND,"Germany",g="Independent: Germany")
nl_sel(k,"One entry is a herbal-blend brand; blends are versions.","Brands from the fetched Celestial Seasonings and Yogi Tea pages and the Wikipedia list of tea companies. No complete reference exists; this is a selection.")
k=K['Yerba mate']
ent(k,"Taragüí","Argentine yerba mate brand owned by Establecimiento Las Marías.",rs("Taragüí")['s'],"Establecimiento Las Marías",NC,"Argentina",g="National champion: Argentina",v=[V("Taragui Sin Palo","Taragüí")])
k.setdefault('nl',"One entry is a mate style or brand.");k['sel']="Kept from the earlier edition with fetched sources; no complete reference exists."
for n in('Rooibos','Kava'):
    K[n].setdefault('nl',"One entry is a named variety or origin."); K[n].setdefault('sel',"Kept from the earlier edition with fetched sources; no complete reference exists.")

# ---------- Cocoa ----------
C=W+"Theobroma_cacao"
k=K['Cacao beans']
for n,dd in (("Contamana","Cacao genetic group named in Motamayor's 2008 classification."),("Curaray","Cacao genetic group named in Motamayor's 2008 classification."),("Cacao guiana","Cacao genetic group named in Motamayor's 2008 classification."),("Iquitos","Cacao genetic group named in Motamayor's 2008 classification."),("Marañon","Cacao genetic group named in Motamayor's 2008 classification."),("Nanay","Cacao genetic group named in Motamayor's 2008 classification."),("Purús","Cacao genetic group named in Motamayor's 2008 classification.")):
    ent(k,n,dd,C,y="2008 genetic grouping",g="Motamayor genetic groups (2008)")
for x in k['x']:
    if x['n'] in('Criollo','Forastero (Amelonado)','Nacional (Arriba)'): x['g']="Motamayor genetic groups (2008)"
    elif x['n']=='Trinitario': x['g']="Historical group (hybrid)"
    else: x['g']="Cultivar or appellation"
setf(k,"Criollo",role="origin")
for x in k['x']: x.pop('role',None) if x['n']=="Criollo" else None
nl_sel(k,"One entry is a cacao genetic group, a historical cacao group, a clone or a protected origin.",f"Follows the ten genetic groups the Wikipedia article on Theobroma cacao names from the 2008 classification ({C}): Amelonado, Criollo, Nacional, Contamana, Curaray, Cacao guiana, Iquitos, Marañon, Nanay, Purús. Complete: 10 of 10; Trinitario, Chuao and CCN-51 are kept from the earlier edition.")
K['Drinking chocolate']['x']  # exists
k=K['Drinking chocolate']
ent(k,"Cadbury Drinking Chocolate","British drinking chocolate from the Cadbury chocolate maker.",W+"Cadbury","",IND,"United Kingdom",g="Independent: United Kingdom")
for x in k['x']:
    if x['n']=="Cadbury Drinking Chocolate": x.pop('own',None); x['tier']=IND
ent(k,"Ghirardelli","San Francisco chocolate maker; sells a Double Chocolate premium hot cocoa.",rs("Ghirardelli")['s'] or W+"Ghirardelli_Chocolate_Company","",IND,"United States",g="Independent: United States")
nl_sel(k,"One entry is a drinking-chocolate tradition or brand; products are versions.","Traditions kept from the earlier edition; brands only where a fetched page exists. No complete reference exists.")
for x in k['x']:
    if x['n']=="Ghirardelli": x.pop('own',None)
for n in('Instant hot chocolate mix','Cocoa powder','Malted chocolate drink powder'):
    K[n]['nl']="One entry is a cocoa or malted-drink brand or process."; K[n]['sel']="Kept from the earlier edition with fetched sources; no complete reference exists."
for n,o,t,c in(("Nesquik","Nestlé",G,"United States"),):
    setf(K['Instant hot chocolate mix'],n,own=o,tier=t,cty=c)
for n,o,t,c in(("Ovaltine","Wander (Swiss company), now Associated British Foods outside the United States",None,"Switzerland"),("Milo","Nestlé",G,"Australia"),("Horlicks","Hindustan Unilever (India)",None,"United Kingdom")):
    pass
setf(K['Malted chocolate drink powder'],"Milo",own="Nestlé",tier=G,cty="Australia")

# ---------- market summaries ----------
cof=dept('Coffee'); tea=dept('Tea')
cof['ms']=[
 {"mkt":"Global at-home coffee","who":"Nestlé","share":"just under 25 %","yr":2020,"s":"https://www.foodbusinessnews.net/articles/16135-jde-peet-s-raises-25-billion-in-ipo".replace("peet-s","peets"),"note":"Euromonitor figure quoted in an article of 29 May 2020; share of the at-home market"},
 {"mkt":"Global at-home coffee","who":"JDE Peet's","share":"10 %","yr":2020,"s":"https://www.foodbusinessnews.net/articles/16135-jde-peets-raises-25-billion-in-ipo","note":"Euromonitor figure quoted in the same article; second to Nestlé"},
 {"mkt":"Italian coffee","who":"Lavazza","share":"over 36 % of sales","yr":None,"s":W+"Lavazza","note":"year not stated on the page; revenue €3.35 billion in 2024"},
 {"mkt":"German roasted coffee","who":"Tchibo","share":"20 %","yr":None,"s":W+"Tchibo","note":"share after buying Eduscho in 1997, as the page states; year of the figure not given"},
 {"mkt":"Starbucks packaged coffee outside its shops","who":"Nestlé","share":"","yr":2018,"s":"https://www.foxbusiness.com/markets/nestle-to-pay-7-15-billion-to-starbucks-in-coffee-tie-up","note":"Nestlé paid Starbucks US$7.15 billion for worldwide marketing rights; no sales figure on the page"},
 {"mkt":"Keurig Dr Pepper coffee","who":"Keurig Dr Pepper","share":"","yr":2025,"s":W+"Keurig_Dr_Pepper","note":"announced the acquisition of JDE Peet's in August 2025 with a takeover offer in January 2026; outcome not on the fetched page"},
 {"mkt":"JDE Peet's brands","who":"JDE Peet's","share":"","yr":2021,"s":S_JDE,"note":"revenue €7.0 billion in 2021; JAB Holding agreed in October 2024 to raise its stake to about 68 %"},
 {"mkt":"Specialist roasters ranked by Coffee Review (top 10 coffees of 2025)","who":"JBC Coffee Roasters; Red Rooster Coffee Roaster; KakaLove Café; Hula Daddy Kona Coffee; Heady Cup Coffee Roasters; Big Island Coffee Roasters; Utopian Coffee; Coffee Cycle Roasting; Magnolia Coffee","share":"","yr":2025,"s":"https://www.coffeereview.com/the-list-coffee-reviews-top-50-coffees-of-2025/","note":"ranks 1 to 10 in that order, KakaLove Café at ranks 3 and 7; list of coffees, not of firms; published 4 December 2025"},
]
tea['ms']=[
 {"mkt":"British black tea","who":"Yorkshire Tea","share":"28 %","yr":2019,"s":W+"Yorkshire_Tea","note":"share of the traditional black tea market reported in November 2019"},
 {"mkt":"Indian tea","who":"Tata Tea brands","share":"about 25 %","yr":1999,"s":W+"Tata_Consumer_Products","note":"the page marks this figure as unsourced; branded tea is about 86 % of Tata Consumer turnover (year not stated)"},
 {"mkt":"Lipton Teas and Infusions","who":"CVC Capital Partners","share":"","yr":2022,"s":W+"Lipton","note":"bought most of Unilever's tea business for €4.5 billion; completed July 2022"},
 {"mkt":"Twinings","who":"Associated British Foods","share":"","yr":1964,"s":W+"Twinings","note":"owner since 1964"},
 {"mkt":"Japanese green tea","who":"Ito En","share":"","yr":None,"s":W+"Ito_En","note":"largest green tea distributor in Japan per the page; no figure or year"},
 {"mkt":"Pakistani tea","who":"Tapal","share":"","yr":None,"s":W+"Tapal_Tea","note":"one of the largest brands per the page; no figure"},
]
# note on missing markets
tea['note']=(tea.get('note') or "")
# ---------- brand register ----------
def addb(n,c,f,d,s,seg="Mainstream",kf=""):
    if n in reg: return
    B['b'].append({"n":n,"c":c,"f":f,"seg":seg,"kf":kf,"d":d,"s":s}); reg[n]=B['b'][-1]
addb("JDE Peet's","Netherlands","","Coffee and tea group; JAB Holding agreed in October 2024 to raise its stake to about 68 %.",S_JDE,kf="coffee group")
addb("Keurig Dr Pepper","United States","1996","Beverage group that owns Keurig and has bought into La Colombe.",W+"Keurig_Dr_Pepper",kf="beverage group")
addb("Tata Consumer Products","India","","Indian group that owns Tata Tea, Tetley and Eight O'Clock Coffee.",W+"Tata_Consumer_Products",kf="tea group")
addb("Associated British Foods","United Kingdom","","Owner of Twinings since 1964.",W+"Twinings",kf="food group")
addb("Maxingvest","Germany","","Owner of Tchibo.",W+"Tchibo",kf="holding")
addb("Bettys & Taylors Group","United Kingdom","","Owner of Yorkshire Tea.",W+"Yorkshire_Tea",kf="tea company")
addb("Çaykur","Turkey","1983","Turkish state tea company.",W+"%C3%87aykur",kf="state tea")
addb("Ito En","Japan","1966","Japan's largest green tea distributor.",W+"Ito_En",kf="green tea")
addb("Tapal","Pakistan","1947","Karachi tea family firm.",W+"Tapal_Tea",kf="tea")
addb("Paulig","Finland","1876","Helsinki family coffee firm.",W+"Paulig")
if "Lyons" not in reg: addb("Lyons","United Kingdom","","Tea brand of Lipton Teas and Infusions.",S_TEA)
addb("Eduscho","Germany","","Brand bought by Tchibo in 1997.",W+"Tchibo")
for dn in ('Coffee','Tea','Herbal & fruit infusions','Cocoa & drinking chocolate'): pass
json.dump(d,open('J6.new.json','w'),ensure_ascii=False,indent=1)
json.dump(B,open('J6_brands.new.json','w'),ensure_ascii=False,indent=1)
json.dump(rn,open('J6_renames.new.json','w'),ensure_ascii=False,indent=1)
