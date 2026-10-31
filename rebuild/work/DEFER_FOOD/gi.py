import json,re,collections
API="https://webgate.ec.europa.eu/eambrosia-api/api/v1/geographical-indications"
CN={'IT':'Italy','FR':'France','ES':'Spain','PT':'Portugal','GR':'Greece','CN':'China','DE':'Germany','GB':'United Kingdom','HR':'Croatia','TR':'Türkiye','PL':'Poland','HU':'Hungary','CZ':'Czechia','SE':'Sweden','SI':'Slovenia','SK':'Slovakia','BE':'Belgium','AT':'Austria','RO':'Romania','FI':'Finland','CY':'Cyprus','NL':'Netherlands','IE':'Ireland','DK':'Denmark','LT':'Lithuania','BG':'Bulgaria','ID':'Indonesia','TH':'Thailand','LV':'Latvia','LU':'Luxembourg','NO':'Norway','IN':'India','KH':'Cambodia','CO':'Colombia','VN':'Vietnam','AD':'Andorra','DO':'Dominican Republic','LK':'Sri Lanka','MN':'Mongolia','ZA':'South Africa','EE':'Estonia','CM':'Cameroon','IS':'Iceland','UK(NI)':'United Kingdom (Northern Ireland)','MT':'Malta','BA':'Bosnia and Herzegovina','NE':'Niger','GT':'Guatemala'}
arr=json.load(open('rebuild/work/DEFER_FOOD/gi_register.json'))
R=[a for a in arr if a['productType']=='FOOD' and a['status']=='registered']
def cat(c): return [a for a in R if a['productCategories'] and c in a['productCategories']]
butter=lambda a: any(x['cnText'].startswith('0405') for x in (a.get('cnClassification') or [])) or re.search(r'beurre|butter|burro|manteiga|mantequilla',a['protectedNames'][0],re.I)
SETS={
 'J1a':cat(142),'J1b':cat(143),'J2':cat(148),'J4':cat(147),
 'J5':[a for a in cat(146) if not butter(a)],'J8':cat(153)}
def entries(lst):
    out=[]
    for a in lst:
        names=a['protectedNames']; c=', '.join(CN.get(x,x) for x in a['countries'])
        y=(a.get('euProtectionDate') or '')[:4]
        out.append({"n":names[0],"a":" · ".join(names[1:]),"d":f"{a['giType']} name from {c}; EU register file {a['fileNumber']}.","mk":"","y":y if y.isdigit() else "","s":API,"g":c,"cty":c,"v":[]})
    out.sort(key=lambda e:(e['g'],e['y'] or '9999',e['n']))
    return out
def sel(n,what):
    c=collections.Counter(e['cty'] for e in n)
    return (f"Every registered name in the EU eAmbrosia register's {what} (public API, fetched 2026-10-31 through Parallel; 4,022 records in all, registered food names only, applications and published names left out). "
            f"Complete: {len(n)} of {len(n)} registered names in that class; sections are countries ({len(c)} countries, largest {c.most_common(1)[0][0]} with {c.most_common(1)[0][1]}). Names not under an EU or bilateral GI scheme are not in it.")
def kind(name,desc,what,lst):
    n=entries(lst)
    return {"n":name,"a":"PDO · PGI · GI names","d":desc,"s":API,"nl":"One entry is one protected name registered in the EU register; the pack or product sold under it is not an entry.","sel":sel(n,what),"xg":"country","tt":[["Designation",["PDO (protected designation of origin)","PGI (protected geographical indication)"]]],"x":n}
def add(code,dept,shelf_name,shelf_t,k,ax):
    d=json.load(open(f'rebuild/out/{code}.json'))
    dp=[x for x in d['depts'] if x['n']==dept][0]
    if any(s.get('n')==shelf_name for s in dp['s']): return
    dp['s'].append({"n":shelf_name,"t":shelf_t,"k":[k]})
    json.dump(d,open(f'rebuild/work/DEFER_FOOD/{code}.tmp','w'),ensure_ascii=False)
    import os; os.replace(f'rebuild/work/DEFER_FOOD/{code}.tmp',f'rebuild/out/{code}.json')
    print(code,k['n'],len(k['x']))
add('J1','Beef & veal','Protected fresh meat names','Fresh meat and poultry sold under an EU protected name, from beef and lamb to Bresse poultry; the plain cut → the cut shelves.',
    kind('EU protected fresh meat names','Fresh meat, poultry and offal sold under an EU protected designation of origin or geographical indication.',"class 'fresh meat (and offal)'",SETS['J1a']),0)
add('J1','Ham, bacon & cured meats','Protected meat-product names','Cured and cooked meat products sold under an EU protected name, such as Prosciutto di Parma or Jamón de Teruel; the unprotected style → the style shelves.',
    kind('EU protected meat-product names','Hams, sausages, cured meats and other meat products sold under an EU protected designation of origin or geographical indication.',"class 'meat products (cooked, salted, smoked)'",SETS['J1b']),0)
add('J2','Fresh & frozen fish','Protected fish names','Fish, shellfish and fish products sold under an EU protected name, such as Mejillón de Galicia; the plain species → the species shelves.',
    kind('EU protected fish and seafood names','Fresh, smoked, cured and processed fish, molluscs and crustaceans sold under an EU protected designation or geographical indication.',"class 'fresh fish, molluscs, crustaceans and products derived therefrom'",SETS['J2']),0)
add('J4','Temperate fruit','Protected produce names','Fruit, vegetables, nuts, pulses and cereals sold under an EU protected name, such as Pomodoro di Pachino; the plain crop → the crop shelves.',
    kind('EU protected fruit, vegetable and cereal names','Fresh or processed fruit, vegetables, nuts, pulses and cereals sold under an EU protected designation or geographical indication.',"class 'fruit, vegetables and cereals, fresh or processed'",SETS['J4']),0)
add('J5','Oils, vinegars & fats','Protected oil names','Olive and other oils sold under an EU protected name, such as Kalamata or Toscano; the plain oil → the oil shelves.',
    kind('EU protected oil names','Olive and other oils (butter excluded) sold under an EU protected designation of origin or geographical indication.',"class 'oils and fats' (butter excluded)",SETS['J5']),0)
add('J8','Bread & bakery','Protected bakery names','Bread, pastry, cakes, biscuits and confectionery sold under an EU protected name, such as Lebkuchen or Pane di Altamura; the plain style → the style shelves.',
    kind('EU protected bakery and confectionery names','Bread, pastry, cakes, confectionery and biscuits sold under an EU protected designation of origin or geographical indication.',"class 'bread, pastry, cakes, confectionery, biscuits and other baker's wares'",SETS['J8']),0)
