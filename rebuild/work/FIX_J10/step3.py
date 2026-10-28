import json,os
P='out/J10.json';d=json.load(open(P))
B=json.load(open('out/J10_brands.json'));reg={x['n']:x for x in B['b']}
def K(n):
    for D in d['depts']:
        for S in D['s']:
            for k in S['k']:
                if k['n']==n: return k
def Dp(n): return [D for D in d['depts'] if D['n']==n][0]
# mk renames
ren={'Tangiers Tobacco':'Tangiers','Nakhla Tobacco':'Nakhla','Philip Morris':'Philip Morris International'}
def walk(o):
    if isinstance(o,dict):
        if o.get('mk') in ren: o['mk']=ren[o['mk']]
        for v in o.values(): walk(v)
    elif isinstance(o,list):
        for v in o: walk(v)
walk(d)
# blends
T='https://www.tobaccoreviews.com/blend/'
def A(kind,n,dd,mk,s,v=None,y=''):
    K(kind).setdefault('x',[]).append({"n":n,"a":"","d":dd,"mk":mk,"y":y,"s":s,"v":v or []})
A('Virginia blend','Best Brown Flake','Unflavoured straight-Virginia flake from hand-stripped flue-cured leaf; medium strength.','Samuel Gawith',T+'1005/samuel-gawith-best-brown-flake/')
A('Virginia blend','Erinmore Flake','Virginia and Burley flake pressed into cakes, with floral and fruit-citrus flavouring.','Scandinavian Tobacco Group',T+'1126/scandinavian-tobacco-group-stg-erinmore-flake/',[{"n":"Murray & Sons, UK","mk":"","y":"to 2005","d":"Original blender"},{"n":"Scandinavian Tobacco Group, Orlik factory","mk":"Scandinavian Tobacco Group","y":"2005","d":"Current maker, Assens, Denmark"}])
A('Virginia/Perique blend','Dunhill Elizabethan Mixture','Ribbon-cut blend of pressed, darkened Virginia with perique; now sold under the Peterson name.','Dunhill',T+'454/dunhill-elizabethan-mixture/',[{"n":"Dunhill, London","mk":"Dunhill","y":"","d":"Original, until 1981"},{"n":"Murray and Sons, Belfast","mk":"","y":"1981","d":"Made there until 2005"},{"n":"Scandinavian Tobacco Group reintroduction","mk":"Scandinavian Tobacco Group","y":"2013","d":"Sold as a Peterson product"}])
E=K('English & Balkan blend')
A('English & Balkan blend','Squadron Leader','Medium-bodied English ribbon of Virginia, Oriental and Latakia.','Samuel Gawith',T+'1040/samuel-gawith-squadron-leader/')
A('English & Balkan blend','Nightcap','English ribbon of Virginia, Oriental and Latakia with a little perique; first sold as Dunhill Nightcap.','Dunhill',T+'459/peterson-nightcap/',[{"n":"Dunhill Nightcap","mk":"Dunhill","y":"","d":"Original name"},{"n":"Peterson Nightcap","mk":"Peterson","y":"","d":"Renamed when the brand moved to Peterson"}])
A('English & Balkan blend','Commonwealth Mixture','Strong, full-bodied ribbon of Virginia and Latakia.','Samuel Gawith',T+'1018/samuel-gawith-commonwealth-mixture/')
A('English & Balkan blend','Charing Cross','Full-bodied Balkan ribbon of Virginia, Cyprian Latakia and Oriental leaf, made by Cornell & Diehl.','G. L. Pease','http://www.tobaccoreviews.com/blend/1975/g-l-pease-charing-cross/')
A('English & Balkan blend','Balkan Sobranie','Re-released Balkan ribbon of Virginia, Oriental and Latakia, blended by J. F. Germain & Son.','J. F. Germain & Son',T+'5204/j-f-germain-son-balkan-sobranie/')
A('English & Balkan blend','Penzance','Balkan flake of Latakia, Oriental and Virginia, listed under Esoterica Tobacciana.','Esoterica Tobacciana',T+'498/esoterica-tobacciana-penzance/')
A('English & Balkan blend','Plum Pudding','Small-batch pressed English Balkan cake of six tobaccos incl. Latakia and Perique.','Seattle Pipe Club',T+'3059/seattle-pipe-club-plum-pudding/')
A('English & Balkan blend','Frog Morton','Ribbon of Latakia and Virginia, English style with strong Latakia character.','McClelland Tobacco Company',T+'768/mcclelland-frog-morton/')
A('Burley blend','Irish Flake','Full-bodied flake of equal parts air-cured, flue-cured and dark-fired tobacco.','Peterson',T+'2698/peterson-irish-flake/')
A('Burley blend','Burley Flake No. 1','Flake of dark burley, Kentucky, Virginia and a splash of perique.','Cornell & Diehl',T+'3530/cornell-diehl-burley-flake-1/')
A('Aromatic blend','Frog Morton\'s Cellar','Ribbon of Latakia and Virginia aged with oak stave cubes from whiskey barrels, whisky-flavoured.','McClelland Tobacco Company',T+'5273/mcclelland-frog-mortons-cellar/')
A('Aromatic blend','1-Q','Mild vanilla-flavoured ribbon built on golden Cavendish and Virginia.','Lane Limited',T+'630/lane-limited-1-q/')
A('Aromatic blend','1792 Flake','Strong dark Kentucky and Virginia flake flavoured with tonquin bean.','Samuel Gawith',T+'1004/samuel-gawith-1792-flake/')
# strains
W='https://en.wikipedia.org/wiki/List_of_cannabis_strains'
cf=K('Cannabis flower');cf['n']='Cannabis flower'
cf['d']='Dried cannabis flower sold loose, usually under a strain name; strain, grower and batch label vary by market.'
cf['x']=[
 {"n":"OG Kush","a":"","d":"Widely sold strain trade name.","mk":"","y":"","s":W,"v":[{"n":"BC OG Kush","mk":"","y":"","d":"Hybrid of BC Grapefruit Kush and Afghani"}]},
 {"n":"Blue Dream","a":"","d":"Sativa-dominant hybrid strain.","mk":"","y":"","s":W,"v":[]},
 {"n":"Sour Diesel","a":"","d":"Strain listed as Cannabis sativa.","mk":"","y":"","s":W,"v":[]},
 {"n":"Northern Lights","a":"","d":"Widely sold strain trade name.","mk":"","y":"","s":W,"v":[]},
 {"n":"Girl Scout Cookies","a":"","d":"Widely sold strain trade name.","mk":"","y":"","s":W,"v":[]},
 {"n":"White Widow","a":"","d":"Hybrid strain.","mk":"","y":"","s":W,"v":[]},
 {"n":"Gorilla Glue","a":"","d":"Widely sold strain trade name.","mk":"","y":"","s":W,"v":[]},
 {"n":"Jack Herer","a":"","d":"Widely sold strain trade name.","mk":"","y":"","s":W,"v":[]},
 {"n":"Pineapple Express","a":"","d":"Strain trade name.","mk":"","y":"","s":W,"v":[]},
 {"n":"AK-47","a":"","d":"Sativa-dominant hybrid strain.","mk":"","y":"","s":W,"v":[]},
 {"n":"Skunk","a":"","d":"Widely sold strain trade name.","mk":"","y":"","s":W,"v":[]}]
Dp('Cannabis & hemp')['mode']='mixed'
Dp('Cannabis & hemp')['note']='Tier for products; variety for flower, where buyers shop by strain name.'
# brands
def Br(n,c,f,seg,kf,dd,s,**kw):
    if n in reg: return
    e={'n':n,'c':c,'f':f,'seg':seg,'kf':kf,'d':dd,'s':s};e.update(kw);B['b'].append(e);reg[n]=e
Wk='https://en.wikipedia.org/wiki/'
Br('R.J. Reynolds','United States','1875','Mainstream','Camel, Newport','American cigarette maker, owned by British American Tobacco since 2017.',Wk+'R._J._Reynolds_Tobacco_Company')
Br('Nat Sherman','United States','1930','Premium','luxury cigarettes','New York tobacconist turned maker of handmade cigars and luxury cigarettes.',Wk+'Nat_Sherman')
Br('Benson & Hedges','United Kingdom','1873','Premium','100s cigarettes','Cigarette brand founded in London, now owned by Altria and made regionally.',Wk+'Benson_%26_Hedges')
Br('Imperial Tobacco','United Kingdom','1901','Mainstream','Golden Virginia, Drum','Name still used for Imperial Brands, maker of fine-cut tobacco and papers.',Wk+'Imperial_Tobacco',rel=['Imperial Brands'])
Br('Gallaher','United Kingdom','1857','Mainstream','Silk Cut, Sobranie','Former UK tobacco group bought by Japan Tobacco in 2007.',Wk+'Gallaher_Group',rel=['Japan Tobacco'])
Br('American Tobacco','United States','1890','Mainstream','Lucky Strike','Trust formed by James B. Duke, broken up in 1911.',Wk+'American_Tobacco_Company')
Br('SEITA','France','','Mainstream','Gauloises, Gitanes','Former French state tobacco monopoly, merged into Altadis in 1999.',Wk+'SEITA')
Br('Douwe Egberts','Netherlands','1753','Mainstream','Drum (historic)','Dutch coffee company that sold its tobacco brands, including Drum, to Imperial Tobacco in 1998.',Wk+'Douwe_Egberts')
Br('Sobranie','United Kingdom','1879','Premium','Cocktail, Black Russian','London brand begun as Balkan Sobranie tobacco, now Japan Tobacco.',Wk+'Sobranie',rel=['Gallaher'])
Br('Cartier','France','1847','Premium','luxury goods','French luxury house, maker of cigarette cases among much else.',Wk+'Cartier_(jeweler)')
Br('Fabergé','Russia','1842','Premium','imperial eggs','Russian jewellery house, maker of boxes and cigarette cases.',Wk+'Faberg%C3%A9')
Br('Santa Fe Natural Tobacco','United States','1982','Mainstream','Natural American Spirit','Oxford, North Carolina cigarette maker, sold to R.J. Reynolds in 2002.',Wk+'Santa_Fe_Natural_Tobacco_Company')
Br('U.S. Smokeless Tobacco Company','United States','1822','Mainstream','Copenhagen, Skoal','Smokeless tobacco maker, subsidiary of Altria.',Wk+'U.S._Smokeless_Tobacco_Company')
Br('Scandinavian Tobacco Group','Denmark','1961','Specialist','cigars, pipe tobacco','Copenhagen cigar and pipe-tobacco company behind Captain Black and Peterson tobaccos.',Wk+'Scandinavian_Tobacco_Group')
Br('Butz-Choquin','France','1858','Heritage manufactory','Saint-Claude briar pipes','French pipe maker founded by Jean-Baptiste Choquin and Gustave Butz.',Wk+'Butz-Choquin')
Br('Vegas Robaina','Cuba','1997','Heritage manufactory','Robaina farm tobacco','Cuban cigar line launched by Habanos SA, named after Alejandro Robaina\'s farm.',Wk+'Vegas_Robaina')
Br('Diplomáticos','Cuba','1966','Heritage manufactory','mild Montecristo-derived','Cuban cigar brand created in 1966, first new brand after the Revolution.',Wk+'Diplom%C3%A1ticos')
tr='https://www.tobaccoreviews.com/blend/'
for n,dd,s in [('Samuel Gawith','Pipe-tobacco blender listed on TobaccoReviews as both blender and manufacturer.',tr+'1040/samuel-gawith-squadron-leader/'),
 ('Gawith, Hoggarth & Co.','Pipe-tobacco blender of Ennerdale Flake.',tr+'564/gawith-hoggarth-co-ennerdale-flake/'),
 ('Lane Limited','Pipe-tobacco blender of Captain Black and 1-Q, made by Scandinavian Tobacco Group.',tr+'630/lane-limited-1-q/'),
 ('Orlik','Danish pipe-tobacco maker; Orlik factory in Assens belongs to Scandinavian Tobacco Group.',tr+'828/orlik-golden-sliced'),
 ('Murrays','Belfast tobacco maker of Murray & Sons blends until 2005.',tr+'1126/scandinavian-tobacco-group-stg-erinmore-flake/'),
 ('Cornell & Diehl','Pipe-tobacco blender; also manufactures G. L. Pease blends.',tr+'3530/cornell-diehl-burley-flake-1/'),
 ('McClelland Tobacco Company','Pipe-tobacco blender of the Frog Morton line.',tr+'768/mcclelland-frog-morton/'),
 ('G. L. Pease','Pipe-tobacco line of Gregory Pease, manufactured by Cornell & Diehl.','http://www.tobaccoreviews.com/blend/1975/g-l-pease-charing-cross/'),
 ('J. F. Germain & Son','Blender of the re-released Balkan Sobranie.',tr+'5204/j-f-germain-son-balkan-sobranie/'),
 ('Esoterica Tobacciana','Pipe-tobacco line under which Penzance is listed.',tr+'498/esoterica-tobacciana-penzance/'),
 ('Seattle Pipe Club','Small-batch pipe-tobacco label of Joe Lankford, maker of Plum Pudding.',tr+'3059/seattle-pipe-club-plum-pudding/')]:
    Br(n,'','','Specialist','pipe tobacco',dd,s)
for D in d['depts']: pass
# tidy: Peterson, Dunhill exist in register
for p,o in((P,d),('out/J10_brands.json',B)):
    json.dump(o,open(p+'.tmp','w'),ensure_ascii=False,indent=1);os.replace(p+'.tmp',p)
