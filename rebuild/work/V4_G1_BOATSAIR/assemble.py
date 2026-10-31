import json,copy,re
ROOT='/home/user/Possession-Taxonomy/'
G=json.load(open(ROOT+'rebuild/out/G1.json'))
bo=json.load(open('boats_out.json'))
ai=json.load(open('air_out.json'))
vc=copy.deepcopy(next(x for x in G['depts'] if x['n']=='Vehicle care & detailing'))
droppedvc=[]
removed_x=[]
for s in vc['s']:
    for k in s['k']:
        for m in k.pop('m',[]) or []: droppedvc.append((k['n'],m))
        for r in k.pop('r',[]) or []: droppedvc.append((k['n'],r))
        for e in k.pop('x',[]) or []: removed_x.append((k['n'],e['n']))
DB='https://www.databridgemarketresearch.com/reports/global-car-care-products-market'
TW='https://en.wikipedia.org/wiki/Turtle_Wax'
MG='https://www.meguiars.co.uk/showroom/meguiars-history-lesson-since-1901/'
vc['note']='Commodity products named by job and chemistry; no product models are listed because tests and rankings change yearly. Brand origins and owners are in the brand register.'
vc['ms']=[
 {'mkt':'Global car care products','who':'All makers','share':'USD 9.16 billion','yr':2024,'s':DB,'note':'market size; Data Bridge forecasts USD 12.01 billion by 2032, a 3.45 % annual growth rate for 2025 to 2032'},
 {'mkt':'Global car care products by product','who':'Car cleaning products','share':'38.5 %','yr':2024,'s':DB,'note':'largest product segment'},
 {'mkt':'Global car care products by end user','who':'Retail (B2C)','share':'62 %','yr':2024,'s':DB,'note':'against professional users'},
 {'mkt':'Global car care products by channel','who':'Retail stores','share':'45 %','yr':2024,'s':DB,'note':'largest distribution channel'},
 {'mkt':'Global car care products by pack size','who':'251 to 500 ml','share':'41 %','yr':2024,'s':DB,'note':'largest packaging volume band'},
 {'mkt':'Global car care products by region','who':'North America','share':'32.01 %','yr':2024,'s':DB,'note':'largest regional share'},
 {'mkt':'Global car care products, named players','who':'3M, Sonax, Tetrosyl, Chemical Guys, Armor All, Würth, MA-FRA, Cartec, Turtle Wax, Liqui Moly, Autoglym, Mothers, Adam\'s Polishes, Griot\'s Garage, Simoniz','share':'no shares given','yr':2024,'s':DB,'note':'major players as listed by Data Bridge; the page gives no company shares'},
 {'mkt':'Turtle Wax ownership','who':'Turtle Wax','share':'privately held; founded 1941 in Chicago as Plastone by Benjamin Hirsch','yr':2026,'s':TW,'note':'Professional Products arm sold to Transchem in 2013; Transchem acquired by OPW (Dover) in 2024'},
 {'mkt':'Meguiar\'s origin','who':'Meguiar\'s','share':'founded 1901 as a furniture polish plant in the garage of Frank Meguiar Jr.','yr':1901,'s':MG,'note':'consumer automotive line introduced 1973'}]
vc['msum']='Only one market report page could be read; it gives the global size and segment shares but no company shares. Kinds stay commodity: no product models are listed, since they would date within a year.'
brands=[
 {"n":"Jeanneau","c":"France","f":"1957","seg":"Mainstream","d":"Les Herbiers builder founded by Henri Jeanneau; bought by Groupe Beneteau in 1995.","lines":["Sun Odyssey","Sun Fast","Jeanneau Yachts"],"eras":[],"sig":["Sun Odyssey"],"sc":[],"rel":["Beneteau"],"s":"https://en.wikipedia.org/wiki/Jeanneau","kf":"cruising yachts"},
 {"n":"Groupe Beneteau","c":"France","f":"","seg":"Professional & flagship","d":"Parent of Beneteau and Jeanneau; owns Rec Boat Holdings and bought Seascape in 2018.","lines":[],"eras":[],"sig":[],"sc":[],"rel":["Beneteau","Jeanneau"],"s":"https://en.wikipedia.org/wiki/Beneteau","kf":"owner group"},
 {"n":"Brunswick Corporation","c":"United States","f":"","seg":"Professional & flagship","d":"Owns Boston Whaler (bought 1996) and Sea Ray (bought 1986) through its Brunswick Boat Group.","lines":[],"eras":[],"sig":[],"sc":[],"rel":["Boston Whaler","Sea Ray"],"s":"https://en.wikipedia.org/wiki/Boston_Whaler","kf":"owner group"},
 {"n":"DJI","c":"China","f":"","seg":"Professional & flagship","d":"Chinese technology company that makes the Mavic folding camera drones.","lines":["Mavic"],"eras":[],"sig":["Mavic Pro"],"sc":[],"rel":[],"s":"https://en.wikipedia.org/wiki/DJI_Mavic","kf":"camera drones"},
 {"n":"Johnson Outdoors","c":"United States","f":"","seg":"Professional & flagship","d":"Owner of Old Town since 2004; S.C. Johnson bought Old Town in 1974.","lines":[],"eras":[],"sig":[],"sc":[],"rel":["Old Town"],"s":"https://en.wikipedia.org/wiki/Old_Town_Canoe","kf":"owner group"},
 {"n":"Azimut Benetti S.p.A.","c":"Italy","f":"","seg":"Professional & flagship","d":"Parent of Azimut Yachts; Azimut bought Benetti in 1985.","lines":[],"eras":[],"sig":[],"sc":[],"rel":["Azimut Yachts"],"s":"https://en.wikipedia.org/wiki/Azimut_Yachts","kf":"owner group"},
 {"n":"China Aviation Industry General Aircraft","c":"China","f":"","seg":"Professional & flagship","d":"Subsidiary of AVIC; bought Cirrus Aircraft in 2011.","lines":[],"eras":[],"sig":[],"sc":[],"rel":["Cirrus"],"s":"https://en.wikipedia.org/wiki/Cirrus_Aircraft","kf":"owner group"},
 {"n":"US Financial, LLC","c":"United States","f":"","seg":"Specialist","d":"Wyoming company, behind a group of Mooney owners, that took over Mooney on 1 September 2020.","lines":[],"eras":[],"sig":[],"sc":[],"rel":["Mooney"],"s":"https://en.wikipedia.org/wiki/Mooney_International_Corporation","kf":"owner"}]
upd={
 "Beneteau":{"own":"Groupe Beneteau","tier":"Global group","c":"France"},
 "Jeanneau":{"own":"Groupe Beneteau","tier":"Global group","c":"France","own_y":"1995"},
 "Hallberg-Rassy":{"own":"The Rassy family","tier":"Independent","c":"Sweden"},
 "Sunseeker":{"own":"Lionheart Capital and Orienta Capital Partners","tier":"Independent","c":"United Kingdom","own_y":"2024"},
 "Azimut Yachts":{"own":"Azimut Benetti S.p.A.","tier":"Independent","c":"Italy"},
 "Boston Whaler":{"own":"Brunswick Corporation","tier":"Global group","c":"United States","own_y":"1996"},
 "Sea Ray":{"own":"Brunswick Corporation","tier":"Global group","c":"United States","own_y":"1986"},
 "Old Town":{"own":"Johnson Outdoors","tier":"Independent","c":"United States","own_y":"2004"},
 "Cirrus":{"own":"China Aviation Industry General Aircraft (AVIC)","tier":"National champion","c":"United States","own_y":"2011"},
 "Mooney":{"own":"US Financial, LLC","tier":"Independent","c":"United States","own_y":"2020"},
 "Robinson Helicopter":{"own":"Private company","tier":"Independent","c":"United States"},
 "Alexander Schleicher":{"own":"Kremer family management","tier":"Independent","c":"Germany"},
 "Schempp-Hirth":{"own":"Holighaus family management","tier":"Independent","c":"Germany"},
 "Turtle Wax":{"own":"Turtle Wax (privately held)","tier":"Independent","c":"United States"},
 "Meguiar's":{"own":"3M","tier":"Global group","c":"United States"}}
# only keep updates for names present in register
reg={b['n'] for b in json.load(open(ROOT+'rebuild/out/G1_brands.json'))['b']}
upd={k:v for k,v in upd.items() if k in reg}
part={"replaces":["Boats","Aircraft","Vehicle care & detailing"],"depts":[bo['dept'],ai['dept'],vc],"brands":brands,"brand_updates":upd,"renames":{},"moves":[ai['move']]}
json.dump(part,open(ROOT+'rebuild/out/G1_parts/BOATSAIR.json','w'),ensure_ascii=False)
json.dump({'vc_dropped':droppedvc,'vc_removed_x':removed_x,'upd_missing':[k for k in ["Robinson Helicopter"]]},open('vc_out.json','w'))
print(len(droppedvc),len(removed_x),sorted(upd))
