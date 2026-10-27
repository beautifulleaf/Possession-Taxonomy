import json,os
W='https://en.wikipedia.org/wiki/'
def X(n,d,s,mk='',y='',a='',v=None,dt=''):
    x={'n':n,'a':a,'d':d,'mk':mk,'y':y,'s':s}
    if v: x['v']=v
    if dt: x['dt']=dt
    return x
def V(n,d='',mk='',y=''): return {'n':n,'mk':mk,'y':y,'d':d}
CB=W+'Corned_beef'
kinds=[
{'n':'Bacon','a':'rashers','d':'Cured pork belly, back or loin sold in rashers or a piece to be cooked, smoked or unsmoked.','s':'https://farmfetch.co.uk/collections/bacon',
 't':['back','streaky','middle','collar','smoked','unsmoked (green)','dry-cured','wet-cured','rashers','lardons','piece'],
 'x':[X('Wiltshire cure','English bacon and ham cure developed by the Harris family at Calne in the 18th century; brine-cured since the First World War, smoked or green.',W+'Wiltshire_cure',mk='',y='18th century',dt='back, streaky or middle · smoked or green'),
  X('Ayrshire bacon','Scotland\'s distinctive cure: skinned, boned pork brined, then rolled as middle with streaky around the back.',"https://list.co.uk/news/12758/ayrshire-cured-bacon",a='Ayrshire middle',dt='rolled middle, back or streaky'),
  X('American streaky bacon','Side bacon from the belly with layers of fat and lean; what "bacon" means in the US.',W+'Bacon',a='side bacon',dt='thin or thick cut · smoke wood · cured or uncured'),
  X('Peameal bacon','Unsmoked Toronto back bacon of wet-cured boneless loin rolled in cornmeal, credited to William Davies.',W+'Peameal_bacon',a='cornmeal bacon'),
  X('Canadian bacon','US name for back bacon from the loin, usually precooked and thick-sliced.',W+'Bacon',a='Canadian-style back bacon')]},
{'n':'Gammon','a':'','d':'Pork hind leg wet- or dry-cured and sold raw as a joint or steaks to be cooked; once cooked it is ham.','s':'https://farmfetch.co.uk/collections/ham-gammon',
 't':['joint','steak','bone-in','boneless','smoked','unsmoked','dry-cured','wet-cured']},
{'n':'Cooked ham','a':'','d':'Pork leg cured then cooked, sold whole or sliced, bone-in or boneless, glazed or plain.','s':'https://farmfetch.co.uk/collections/ham-gammon',
 't':['on the bone','boneless','formed','glazed','smoked','unsmoked','sliced'],
 'x':[X('York ham','Yorkshire-style dry-cured ham eaten boiled or baked; a generic curing style with no protected status.',W+'York_ham',a='Yorkshire ham',y='18th century'),
  X('Prague ham','Boneless brine-cured ham, stewed then lightly beech-smoked; EU TSG since 2018.',W+'Prague_ham',a='Pražská šunka',mk='',y='1860s',v=[V('Šunka od kosti','cooked on the bone')]),
  X('Jambon de Paris','French steam-cooked ham with a mild flavour and delicate texture.',"https://www.tastefrance.com/essentials/meat-products/label-rouge-superior-cooked-ham",a='jambon blanc',
    v=[V('Jambon de Paris','old data'),V('Label Rouge superior cooked ham','Label Rouge pork, restricted cure list','', '2018')]),
  X('Prosciutto cotto','Italian wet-cured ham, brined, cooked in a mould and surface-pasteurised.',W+'Ham',v=[V('Prosciutto cotto','old data')]),
  X('Wiltshire ham','Ham cured by the Wiltshire brine method; a 2025 TSG bid for Wiltshire Cured Ham failed.',W+'Wiltshire_cure',v=[V('Wiltshire cured ham','old data')]),
  X('Bradenham ham','Black-skinned ham dry-salted then cured in molasses, coriander and juniper, aged six months and smoked; recipe dated 1781.',"https://www.cooksinfo.com/bradenham-ham",y='1781')],
 'm':[['Brunswick ham',''],['Jambon torchon','']]},
{'n':'Corned beef & salt beef','a':'salt beef · silverside','d':'Beef brine-cured and cooked, usually brisket, also silverside (salt beef) or another cut, sold as a piece or sliced.','s':'https://www.zingermans.com/Product/raw-corned-beef-brisket/M-LCB',
 't':['brisket','silverside','round','raw to cook','cooked','sliced'],
 'x':[X('Deli corned beef','Brined brisket sold ready to eat in Jewish delicatessens; the meat of the Reuben sandwich.',CB,a='New York corned beef',v=[V("First Cut Corned Beef",'old data',"Zingerman's")]),
  X('Salt beef','Commonwealth name for salt-cured corned beef.',CB,v=[V('Salt beef','old data')]),
  X('Newfoundland salt beef','Salt beef sold in buckets of brine, used in Jiggs dinner.',CB)]},
{'n':'Pastrami & smoked meat','a':'','d':'Beef cured, seasoned, smoked and cooked, sold as a piece or sliced.','s':'https://www.zingermans.com/Product/pastrami/M-PAS?crf=BASE',
 't':['navel','brisket','turkey','sliced','whole'],
 'x':[X('New York pastrami','Jewish-American beef navel brined, spiced with pepper and coriander, smoked and steamed; served on rye.',W+'Pastrami',v=[V("First Cut Lean Pastrami",'old data',"Zingerman's")]),
  X('Montreal smoked meat','Spiced brisket with more cracked pepper than pastrami, hot-smoked then steamed.',W+'Montreal-style_smoked_meat',a='smoked meat · viande fumée'),
  X('Pastramă','Romanian forerunner of pastrami, often of mutton, lamb or goat.',W+'Pastrami')]},
{'n':'Cooked cured tongue','a':'','d':'Ox or pork tongue brined, cooked and pressed, sold whole or sliced.','s':'https://www.waitrose.com/ecom/shop/browse/groceries/fresh_and_chilled/cooked_meats_deli_and_dips/cooked_meats',
 't':['ox','pork','pressed','sliced']},
]
brands=[{'n':"Zingerman's",'c':'United States','f':'1982','seg':'Artisan & independent','kf':'deli','d':'Ann Arbor, Michigan delicatessen and mail-order food business.','sig':['Deli corned beef','New York pastrami'],'s':'knowledge'}]
out={'kinds':kinds,'brands':brands,'traditions':[],'notes':"All six planned kinds kept with old sources. Zingerman's models became versions of the deli archetypes plus a brand entry. Brunswick ham and Jambon torchon stay as old-data models (no fetched page describing them). Gammon and tongue kept kind-level with types. Benton's not added (not sourced)."}
p='/home/user/Possession-Taxonomy/rebuild/work/J1/shelves/05_02.json'
json.dump(out,open(p+'.tmp','w'),ensure_ascii=False,indent=1); os.replace(p+'.tmp',p)
