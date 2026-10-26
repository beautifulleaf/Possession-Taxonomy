import json, os
W='https://en.wikipedia.org/wiki/'
SC=W+'Scythe'; BH=W+'Billhook'; SK=W+'Sickle'; MA=W+'Machete'; KA=W+'Kama_(tool)'
OK='https://www.knivesandtools.co.uk/en/ct/okatsune-shears.htm'
GI='https://www.gardensillustrated.com/garden-equipment/tools/topiary-shears'
BB=W+'Burgon_%26_Ball'
PSU='https://extension.psu.edu/mowing-with-a-scythe'
SA='https://scytheassociation.org/equipment/'
FAL='https://www.scythecymru.co.uk/falci-scythe-blades'
WS='https://wildscythe.co.uk/choosing-scythe-blades-for-rough-mowing/'
PP='https://poorprolesalmanac.substack.com/p/anatomy-of-a-scythe'
SX='https://www.schroeckenfux.at/schroeckenfux-en-us/'
SXH='https://scythesupply.com/schr%C3%B6ckenfux-history.html'
UN='https://www.unesco.at/fileadmin/Redaktion/Kultur/IKE/IKE-DB/files/952.pdf'
TN='https://www.toolnut.co.uk/products/morris-dunsford-devon-and-sussex-billhooks'
BHE='https://www.billhooks.co.uk/catalogues/english/'
BHI='https://www.billhooks.co.uk/photos-and-other-images/italian-billhooks'
EL=W+'Edward_Elwell_Ltd'
HW='https://hardwickandsons.com/products/japanese-nokogama-sickle-saw-1'
CO='https://condortk.com/about/'
def A(n,d,s,mk='',y='',a='',v=None,dt=''):
    x={'n':n,'a':a,'d':d,'mk':mk,'y':y,'s':s}
    if v: x['v']=[dict(zip(('n','mk','y','d'),t)) for t in v]
    if dt: x['dt']=dt
    return x
kinds=[
 {'n':'Hedge shears','a':'garden shears · topiary shears','d':'Two-handed long-bladed shears for clipping hedges, shrubs and topiary.',
  't':['straight blade','wavy-edge blade','topiary (short or narrow blade)','telescopic handles'],
  's':'https://www.hornbach.de/c/garten/gartenwerkzeug-gartengeraete/S1943/',
  'x':[
   A('Japanese hand-forged hedge shears','Two-handed shears forged from Japanese carbon (non-stainless) steel, favoured for hedges and detailed clipping.',OK,
     v=[('No.217','Okatsune','','best-seller'),('No.231','Okatsune','','best-seller'),('No.216','Okatsune','',''),('No.205K','Okatsune','','with bumper'),('No.214','Okatsune','','broad shoulders'),('No.230','Okatsune','','')],
     dt='Japanese carbon steel, not stainless · blade and handle length by model'),
   A('Sheffield garden shears','Forged British garden shears from the Sheffield cutlery trade; Burgon & Ball made more garden shears than sheep shears by 1920.',BB,mk='Burgon & Ball',y='by 1920'),
   A('Topiary shears','Light shears with short or slender blades for shaping box, yew and other topiary.',GI,
     v=[('Topiary shear, 22 cm blades','Niwaki','','for larger shrubs and hedges'),('Sophie Conran Topiary Shears','Burgon & Ball','','polished stainless steel, 28 cm overall'),('Expert Topiary Shears','Darlac','','35 cm overall'),('Topiary Shears','Wilkinson Sword','','hardened steel, non-stick coating'),('Razorsharp Advantage Topiary Shears','Spear & Jackson','','16.4 cm high-carbon steel blades'),('Topiary Shears with Brown Leather Handles','Bradleys','','made in Shropshire')],
     dt='blade length · carbon or stainless steel · handle material'),
  ]},
 {'n':'Scythe','a':'snath and blade','d':'Two-handed mowing tool: a long curved blade fixed to a shaft (snath) with one or two grips.',
  't':['grass blade','ditch blade','bush blade','garden blade','field/hay blade','left-handed blade','two-grip snath','one-grip snath','straight snath','bent snath','adjustable snath','replacement blade','snath sold alone'],
  's':'https://www.hornbach.de/c/garten/gartenwerkzeug-gartengeraete/S1943/',
  'x':[
   A('Austrian scythe','European scythe with a thin, curved, hand-forged blade that is peened and whetted in the field, on a straight or nearly straight snath.',PSU,
     a='European scythe · continental scythe',y='16th century (water-hammered "blue" scythes)',
     v=[('Schröckenfux blades','Schröckenfux','since 1540','Roßleithen, Upper Austria; water-hammered "blue" scythes'),
        ('FUX 2010 scythe set','Schröckenfux','','complete set'),('J4000','Schröckenfux','',''),
        ('Styria ditch blade, 55 and 65 cm','Schröckenfux','','0.8 mm'),('Fux bush blade, 40 cm','Schröckenfux','',''),
        ('Fux adjustable snath','Schröckenfux','','two-grip')],
     dt='blade 30–125 cm · grass, ditch, bush or garden blade · snath straight or bent, one or two grips · ash or aluminium'),
   A('Italian scythe blades (Falci)','Italian-made continental blades, generally finer than equivalent Fux blades and needing less frequent peening.',FAL,mk='Falci',
     v=[('100 Meadow and Lawn Blade','Falci','','60 cm'),('128 Grass / Trimming Blade','Falci','',''),('187 Short Ditch Blade','Falci','','55 cm, 0.7 mm'),('177 "The Dragon" Long Ditch Blade','Falci','',''),('"The Bear" Heavy Ditch / Bush Blade','Falci','','55 cm, 1.3 mm')],
     dt='blade type and length · tang angle differs from Fux'),
   A('American scythe','Scythe with a thick, narrow, straight blade without a beard, ground rather than peened, on an intricately curved snath with adjustable grips.',PSU,
     dt='heavier (about 2.7 kg) · curved snath · grinder-sharpened blade'),
   A('English scythe','Traditional heavier English-pattern scythe, made in Sheffield, North Derbyshire and Belbroughton; now kept mainly for interest or tradition.',SA,
     v=[("'Best Crown' Briar bush blade, 26 in",'Isaac Nash','','vintage, 66 cm, 1.8 mm')],
     dt='vintage and restored blades · English snath'),
  ]},
 {'n':'Billhook','a':'bill hook · hedging bill · serpe · roncola','d':'Hooked chopping blade on a short handle for cutting brush, hedge laying and coppice work.',
  't':['single-edged','double-edged','one-handed','two-handed (long handle)'],
  's':'https://www.machetespecialists.com/products/machetes/billhook',
  'x':[
   A('Devon billhook','Devon/Dorchester "half turn" pattern with a heavy nose, 6-inch handle and 10-inch blade.',BH,a='Devon half turn',
     v=[('Devon pattern','W. Gilpin','1918',''),('Devon pattern','Morris of Dunsford','','no longer made')]),
   A('Yorkshire billhook','Generally two-handed pattern with a 14-inch (up to 36-inch) handle and 10-inch blade.',BH),
   A('Llandeilo billhook','Carmarthenshire pattern with a 9-inch handle, 10-inch blade, no back edge and a "hedge grip" notch.',BH),
   A('Spar hook','Very light bill with a 6–7-inch blade, used for splitting hazel spars for thatching.',BH),
   A('Pontypool billhook','Monmouthshire pattern with a 6-inch handle, 10-inch blade, no back edge or hedge grip.',BH),
   A('Leicester billhook','One-handed Leicester/Warwickshire pattern with a curved front edge and straight back edge.',BH,a='Warwickshire billhook'),
   A('Kent billhook','Kent pattern, also called brishing hook; made single-bevel in right- and left-handed versions.',BH,a='brishing hook'),
   A('Sussex billhook','Southern English regional pattern made by Morris of Dunsford alongside the Devon pattern.',TN,
     v=[('Sussex pattern','Morris of Dunsford','','no longer made')]),
   A('Roncola','Italian single-edged billhook, made in many regional shapes (Rome maraccio, Calabria, Venice/Istria).',BHI,a='roncole',
     v=[('Valcamonica billhook','Rinaldi','',''),('Varese billhook','Rinaldi','',''),('Maraccio roma','Rinaldi','','Rome-region shape')],
     dt='regional shape · hand guard · handle'),
   A('Pennato','Italian double-edged billhook, typical of Umbria, Terni, Teano, Ripi and Rieti.',BHI,a='pennati'),
   A('Serpe','French billhook, used notably for pruning vines; miniature forms serve for grape harvesting.',BH,a='serpette'),
  ],
  'm':[['Billhook No. 1807','Martindale']]},
 {'n':'Sickle','a':'reaping hook · grass hook · kama','d':'One-handed curved blade for cutting grass and crops.',
  't':['smooth edge','serrated edge','cranked (offset) handle'],
  's':'https://www.hornbach.de/c/garten/gartenwerkzeug-gartengeraete/S1943/',
  'x':[
   A('Serrated sickle','Toothed sickle of prehistoric lineage, still used for reaping grain and tough fibrous growth.',SK,a='toothed sickle',
     v=[('Serrated sickle','Redtenbacher','1897','Scharnstein, Austria'),('Serrated sickle','Krenhof','1942','Austria'),('Industrial serrated sickle','Falci','1965','Italy')]),
   A('Grass hook','Sickle variant for cutting grass, sometimes cranked (offset downward).',SK,a='grasshook · swap hook'),
   A('Bagging hook','Heavier, larger, non-serrated sickle with an offset handle.',SK,a='badging hook · fagging hook · rip hook'),
   A('Kama','Traditional Japanese sickle used mostly for cutting rice; the blade runs straight into the handle.',KA),
   A('Nokogama','Japanese sickle-saw with a finely serrated high-carbon blade for grasses, weeds, turf, roots and light stems.',HW,a='nokogiri-gama · noko gama',dt='blade about 7 in · carbon or stainless steel'),
   A('Hasiya','Nepali sickle; the khurpa is a larger, heavier form.',SK,a='aasi'),
  ]},
 {'n':'Machete','a':'cutlass · panga · bush knife','d':'Long heavy-bladed knife swung to cut vegetation.',
  't':['blade length','straight or curved','saw back'],
  's':'https://www.homedepot.com/b/Tools-Hand-Tools-Cutting-Tools-Machetes/Machete/N-5yc1vZ1z18gf9Z1z0pgp1',
  'x':[
   A('Panga','East and Southern African machete with a blade that broadens on the back, about 41–46 cm long.',MA,a='tapanga'),
   A('Parang','Malaysian and Indonesian short, thick-bladed chopper suited to woody vegetation.',MA),
   A('Golok','Malaysian and Indonesian short, thick-bladed chopper, close to the parang.',MA),
   A('Bolo','Philippine hand-forged, usually curved-edged blade of about 25–45 cm.',MA),
   A('Cutlass','Caribbean agricultural machete; Robert Mole & Sons of Birmingham was long the leading maker.',MA,
     v=[('Agricultural cutlass','Robert Mole & Sons','','Birmingham, England')]),
  ],
  'm':[['Clearing Machete','Fiskars'],['Gator Machete Jr','Gerber']]},
]
brands=[
 {'n':'Schröckenfux','c':'Austria','f':'1540','seg':'Scythe and sickle forge','d':'Scythe works founded on the river Pießling at Roßleithen, Upper Austria; also makes mower blades.','lines':['scythes','sickles','scythe snaths','Fux'],'sig':['Austrian scythe'],'rel':['Falci'],'s':SX},
 {'n':'Falci','c':'Italy','f':'1921','seg':'Scythe and sickle maker','d':'Italian maker of scythe blades and sickles, based in Dronero.','lines':['scythe blades','sickles'],'sig':['Italian scythe blades (Falci)','Serrated sickle'],'rel':['Schröckenfux'],'s':FAL},
 {'n':'Okatsune','c':'Japan','f':'','seg':'Japanese forged shears','d':'Japanese brand of carbon-steel hedge shears and secateurs.','lines':['hedge shears','pruning shears'],'sig':['Japanese hand-forged hedge shears'],'s':OK},
 {'n':'Burgon & Ball','c':'United Kingdom','f':'1730','seg':'Sheffield shears and garden tools','d':'Sheffield maker of sheep shears and garden tools, at La Plata Works, Malin Bridge, since 1873.','lines':['sheep shears','garden shears','Sophie Conran'],'sig':['Sheffield garden shears'],'s':BB},
 {'n':'Morris of Dunsford','c':'United Kingdom','f':'','seg':'Regional edge-tool maker','d':'Devon edge-tool maker of regional-pattern billhooks; the name is continued by Richard Morris.','lines':['billhooks'],'sig':['Devon billhook','Sussex billhook'],'rel':['Edward Elwell'],'s':BHE},
 {'n':'Edward Elwell','c':'United Kingdom','f':'1817','seg':'Edge-tool maker (closed 2005)','d':'Wednesbury Forge edge-tool maker; joined Spearwell Tools in 1967, later Spear & Jackson.','lines':['axes','billhooks','hoes','spades'],'rel':['Spear & Jackson','Morris of Dunsford'],'s':EL},
 {'n':'Rinaldi','c':'Italy','f':'','seg':'Billhook maker','d':'Italian edge-tool maker with a wide catalogue of regional roncole and pennati.','lines':['roncole','pennati'],'sig':['Roncola'],'s':BHI},
 {'n':'Imacasa','c':'El Salvador','f':'1964','seg':'Machete maker','d':'Machete maker founded in Santa Ana by the Solingen firm Gebr. Weyersberg (1787).','lines':['machetes','Condor'],'rel':['Condor Tool & Knife'],'s':CO},
 {'n':'Condor Tool & Knife','c':'El Salvador','f':'2004','seg':'Premium machetes and outdoor knives','d':'Premium tool and knife brand introduced by Imacasa for North American and European outdoor markets.','lines':['machetes','knives'],'rel':['Imacasa'],'s':CO},
 {'n':'Fiskars','c':'Finland','f':'1649','seg':'Consumer tools and homeware','d':'Finnish consumer-goods group making garden tools, scissors and knives; owns Gerber.','lines':['garden tools','scissors','Gerber'],'rel':['Gerber'],'s':W+'Fiskars'},
 {'n':'Tramontina','c':'Brazil','f':'1911','seg':'Cutlery, cookware and tools','d':'Brazilian maker of cutlery, cookware and agricultural and garden tools, based in Carlos Barbosa.','lines':['agricultural tools','garden tools','cutlery'],'s':W+'Tramontina'},
]
trads=[
 {'n':'Austrian scythe-smithing','g':'Metal & blades','r':'Austria (Upper Austria, Styria, Carinthia)','p':'16th century–present','d':'Free-forged "blue" Austrian scythe blades, exported worldwide in many market-specific forms; Austrian intangible cultural heritage since 2014.','tech':'free-form forging and spreading of the blade under water-driven hammers','mat':'steel; charcoal and later mineral coal','forms':['Scythe','Sickle'],'ctr':['Roßleithen (Schröckenfux; former Kirchdorf-Micheldorf guild)','Wolfsberg (former Himmelberg guild)','Sensenschmiedemuseum Micheldorf','Geyerhammer Scharnstein','Sensenwerk Deutschfeistritz'],'auth':'guild and master marks that became trade marks; about 215 works in 11 guilds c. 1800, two makers left','s':UN},
 {'n':'British regional billhook patterns','g':'Metal & blades','r':'England and Wales','p':'19th–20th century','d':'Up to about 200 regional billhook shapes made by local and Midlands edge-tool works for hedging and coppice work.','tech':'forged edge tools','mat':'steel blade, wooden handle','forms':['Billhook'],'ctr':['Morris of Dunsford (Devon)','Edward Elwell (Wednesbury)','Brades (William Hunt & Sons)','Nash (Stourbridge)','Fussell (Mells)'],'auth':'maker stamp and regional pattern name','s':BHE},
]
notes=("Merged old k23 Scythe, k27 Scythe blade and k28 Scythe snath into one Scythe kind (blade and snath types in t; old FUX 2010 and J4000 models became Schröckenfux versions). "
 "Left out: Niwaki brand entry and Niwaki/Okatsune No.217 product pages (niwaki.com returned 403 to WebFetch, so not used); Jakoti and Darlac brand entries (no brand page retrieved); "
 "Gerber brand entry (Wikipedia page not found); Collins Company and Robert Mole & Sons brand entries (no page retrieved); Latin pattern machete archetype and Condor/Imacasa named models (search snippets only); "
 "Elwell billhook pattern numbers (not on retrieved pages). Fighting machetes (e.g. Brazilian Army jungle machete) belong in Weapons per the knife rule and are not listed. "
 "Martindale No. 1807 and the Fiskars/Gerber machetes stay as plain models from the old data.")
out={'kinds':kinds,'brands':brands,'traditions':trads,'notes':notes}
p='/home/user/Possession-Taxonomy/rebuild/work/C2/shelves/01_02.json'
open(p+'.tmp','w').write(json.dumps(out,ensure_ascii=False,indent=1)); os.replace(p+'.tmp',p)
print('ok')
