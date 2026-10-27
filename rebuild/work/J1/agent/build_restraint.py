import json, os, sys
OUT = '/home/user/Possession-Taxonomy/rebuild/work/J1/shelves'
def K(n, d, s, a='', t=None, m=None):
    k = {'n': n, 'a': a, 'd': d, 's': s}
    if t: k['t'] = t
    if m: k['m'] = m
    return k
DA='https://www.dartagnan.com/buy/meat-game'; BW='https://www.blackwing.com/beef.html'
OT='https://www.oldetownebutcher.com/beef'; MP='https://meatpeoplebutcher.com/price-list'; TM='https://www.themeatman.co.uk/collections/pork'
J = {}
J['00_01'] = ([
 K('Ribeye steak','Beef steak cut from the rib section, boneless or on the bone.',DA,'rib-eye · entrecôte · Scotch fillet (AU) · Delmonico',['boneless','bone-in','cowboy cut','tomahawk','ribeye cap (spinalis)']),
 K('Sirloin steak (striploin)','Beef steak cut from the strip loin of the short loin.','https://www.blackwing.com/beef.html','sirloin (UK) · New York strip · Kansas City strip · contre-filet · porterhouse (AU)',['New York strip','Kansas City strip']),
 K('Fillet steak (tenderloin)','The beef tenderloin, the leanest and most tender loin muscle, whole or cut into steaks.',DA,'filet mignon · tournedos · chateaubriand (centre cut) · eye fillet (AU)',['whole fillet','centre cut','steaks']),
 K('T-bone & porterhouse','Bone-in short-loin steak holding striploin and fillet either side of a T-shaped bone.',BW,'T-bone steak · porterhouse steak',['T-bone','porterhouse (larger fillet portion)','Florentine (bistecca alla fiorentina cut)']),
 K('Rump steak (top sirloin)','Beef steak cut from the rump, at the hip end of the loin.','https://www.crowdcow.com/shop/beef/pasture-raised','rump (UK/AU) · top sirloin (US) · rumsteck'),
 K('Rump cap (picanha)','The rump cap muscle with its fat cap, whole or sliced into steaks.','https://thefarmersbutcher.co.uk/product/rump-cap-500g','picanha · coulotte · top sirloin cap'),
 K('Tri-tip','Triangular roast or steak from the bottom sirloin.','https://www.44steaks.com/collections/butchers-cuts','Santa Maria steak · aiguillette baronne · bottom sirloin'),
 K('Flat iron steak','Beef steak cut from the top blade muscle of the chuck.',OT,"feather blade · top blade · butler's steak"),
 K('Flank steak','Long, lean steak from the abdominal muscle behind the plate.','https://www.44steaks.com/collections/butchers-cuts','bavette (UK) · London broil (US)'),
 K('Skirt steak','Thin, coarse-grained steak from the diaphragm muscles.',OT,'arrachera · entraña',['outside skirt','inside skirt']),
 K('Hanger steak','Steak from the hanging tender attached to the diaphragm.','https://farmfetch.co.uk/products/ex-dairy-onglet',"onglet · butcher's steak"),
], 'Restraint only. Old models (cowboy cut ribeye, tomahawk; New York and Kansas City strip; filet mignon) moved into types or aliases. Regional names added as aliases from the shelf plan. Nothing dropped; no new kinds.')
J['00_02'] = ([
 K('Rib roast','Beef roasting joint from the rib section, on or off the bone.',DA,'fore rib (UK) · standing rib · prime rib · côte de boeuf (single-rib)',['bone-in','boneless','côte de boeuf (single rib)']),
 K('Topside & top round','Lean joint or steak from the inside of the hind leg (round).',BW,'topside (UK) · top round (US) · inside round'),
 K('Silverside & eye of round','Lean joints from the outside of the round, including the cylindrical eye of round.',BW,'',['silverside','eye of round']),
 K('Chuck & blade','Roasting or braising joints and steaks from the shoulder.',OT,'chuck roast · braising steak',['chuck eye roast','English chuck roast','blade','braising steak']),
 K('Beef brisket','Beef joint from the breast, sold whole or as point or flat.','https://www.crowdcow.com/shop/beef/pasture-raised','',['whole packer','point','flat']),
 K('Beef short rib','Rib bones with meat, cut short across or along the bones.',DA,'',["English cut",'flanken/galbi cut','plate short rib',"Jacob's ladder"]),
 K('Beef shin','Cut from the lower leg of cattle, sold to braise.',MP,'shank · gravy beef',['on the bone','off the bone']),
 K('Oxtail','The tail of cattle, sold raw in sections to braise.',BW),
 K('Beef mince & burgers','Raw minced beef, loose or packed, or shaped into burgers and meatballs, plain or only seasoned.','https://www.dakotabutcher.com/products','ground beef · hamburger meat',['mince 5% fat','mince 10% fat','mince 15% fat','mince 20% fat','steak mince','burgers','meatballs']),
 K('Veal','Meat of young cattle, sold as chops, escalopes and other cuts.',DA,'',['chop','escalope','flank','osso buco','loin','white veal','rose veal']),
 K('Beef by the quarter or side','Beef bought in bulk for the freezer as a primal, quarter, half or whole carcass.','https://usameats.com/','beef primal · side of beef',['primal','quarter','half','whole carcass']),
], 'Restraint only. Merged ground beef with shaped burgers/meatballs (k23+k24) and veal chop with veal flank (k12+k17). Chuck models moved into types. No models kept; nothing dropped; no new kinds.')
J['00_03'] = ([
 K('Beef liver','The liver of cattle, sold raw.',BW,"ox liver",["calf's liver"]),
 K('Beef tongue','The tongue of cattle, sold raw.',OT,'ox tongue'),
 K('Beef heart','The heart of cattle, sold raw.',BW),
 K('Beef kidney','The kidney of cattle, sold raw.',BW,'ox kidney'),
 K('Sweetbreads','The thymus or pancreas glands of a calf or lamb, sold raw.',DA),
], 'Restraint only; kind-level, no models. Nothing dropped.')
J['01_01'] = ([
 K('Pork loin','The loin of a pig, sold as chops, steaks or a roasting joint, on or off the bone.',TM,'',['loin chop','loin joint','rack (French-trimmed)','boneless loin steak']),
 K('Pork tenderloin','The pork tenderloin, whole or in medallions.',DA,'pork fillet',['whole','medallions']),
 K('Pork shoulder','The front leg and lower shoulder of a pig, or the whole shoulder as one joint.','https://usameats.com/','picnic · arm · hand',['whole shoulder','blade','picnic']),
 K('Pork collar','Pork from the neck and upper shoulder, sold as a joint or steaks.','https://www.smokeymountainfoods.com/product/pork-collar-steaks','Boston butt · neck end · capocollo (fresh) · cabecero',['joint','steaks']),
 K('Pork leg','The raw, uncured hind leg of a pig, whole, as a joint or as steaks.',TM,'fresh ham',['whole leg','joint','steaks']),
 K('Pork by the half or side','Pork bought in bulk for the freezer as a primal, half or whole carcass.','https://www.farmersgatemarket.com/product-page/side-of-pork','pork primal · side of pork',['primal','half','whole carcass']),
], 'Restraint only. Merged loin chop and loin joint (k30+k33). Pork collar models Cabecero and Coppa turned into aliases (coppa as capocollo, fresh). Nothing dropped; no new kinds.')
J['01_02'] = ([
 K('Pork belly','Raw, uncured pork belly, skin-on or skinless.',TM,'',['skin-on','skinless']),
 K('Pork ribs','Pork rib sections sold raw.',DA,'',['spare ribs','baby back ribs','St. Louis cut','country-style ribs','rib tips']),
 K('Pork mince & burgers','Raw minced pork, loose or packed, or shaped into burgers and meatballs, plain or only seasoned.',MP,'ground pork',['mince','burgers','meatballs']),
 K('Pork hock','The lower leg joint of a pig above the trotter, sold raw.','https://tussocksedgefarm.com/store/product/pork-hock-fresh','knuckle · Eisbein · ham hock (fresh)'),
 K('Pork jowl & cheek','The cheek and jowl of a pig, sold raw.','https://www.marbleridgefarms.com/products/pork-jowl','pork jowl · pig cheek'),
 K('Pork trotter','The foot of a pig, sold raw.','https://omnifrozenfood.com.sg/products/pork-hock-knuckle-cut-1kg-pkt',"pig's foot"),
 K('Pork stomach & offal','Pig stomach and other offal, sold raw.','https://omnifrozenfood.com.sg/products/pork-hock-knuckle-cut-1kg-pkt','maw',['stomach (maw)','liver','kidney','caul fat','blood']),
], 'Restraint only. Merged ground pork with shaped burgers/meatballs (k44+k45). Rib models (baby back, country-style, St. Louis) moved into types. Nothing dropped; no new kinds.')
J['02_00'] = ([
 K('Lamb leg','The hind leg of a lamb, whole or part, on or off the bone.',DA,'gigot',['whole','half (shank end)','half (fillet end)','butterflied','boneless']),
 K('Lamb rack','The rib section of a lamb with its chops joined, sold raw.',DA,"best end · carré d'agneau",['French-trimmed','crown roast']),
 K('Lamb chops','Lamb chops cut from the loin or rib, bone-in.',MP,'',['loin chop','cutlet','Barnsley chop','chump chop']),
 K('Lamb shoulder','The shoulder of a lamb, whole or part, on or off the bone.',MP,'',['bone-in','boneless']),
 K('Lamb shank','The lower leg of a lamb, sold raw to braise.',MP),
], 'Restraint only; kind-level, no models. Nothing dropped; no new kinds.')
J['02_02'] = ([
 K('Goat & kid','Goat or kid meat sold whole or as cuts such as leg, chops, shank and shoulder.','https://onestophalal.com/collections/halal-goat-meat','cabrito (kid) · mutton (South Asian usage)',['whole or half','leg','chops','shank','shoulder','diced','kid (cabrito)','adult goat']),
 K('Goat mince & burgers','Raw minced goat meat, loose or packed, or shaped into burgers, plain or only seasoned.','https://newbarnfarmdorset.co.uk/shop-online/goat-mince','ground goat',['mince','burgers']),
], 'Restraint only. Merged goat, goat leg, goat chops and goat shank (k53-k56) into Goat & kid with cut types; merged ground goat and goat burgers (k57+k58). Nothing dropped; no new kinds.')
J['07_01'] = ([
 K('Rotisserie chicken','A whole chicken roasted plain or only seasoned, sold ready to eat.','https://www.waitrose.com/ecom/products/waitrose-cooked-whole-roast-chicken/025811-12584-12585','roast chicken · plain-cooked whole bird'),
 K('Cooked sliced roast meat','A roasted cut, plain or only seasoned, sold whole or sliced to eat cold.','https://www.sezamo.ro/en-RO/16148-sliced-porchetta-montagna','roast beef · roast turkey',['roast beef','roast turkey','roast pork'],[['Porchetta','']]),
 K('Cooked meatballs & patties','Minced meat shaped and cooked, plain or only seasoned, not coated, filled or sauced.','https://www.hannaford.com/groceries/meat/cooked-perfect-dinner-size-italian-style-meatballs-apx-26-ct-frozen-26-oz-bag.html','cooked meatball · patty · meat loaf',None,[['Cooked Perfect Italian Style Meatballs','Home Market Foods']]),
 K('Luncheon meat','Cured, seasoned minced meat formed into a block and cooked in a sealed tin.','https://www.hannaford.com/groceries/browse-aisles/4502-canned-luncheon-potted-meat','',None,[['SPAM Classic','Hormel Foods']]),
 K('Tinned corned beef','Cured beef cooked and sealed in its tin.','https://www.hannaford.com/groceries/browse-aisles/2730-canned-meat','bully beef'),
 K('Charcuterie & deli selection','A mixed pack of cured meats, sausages or cooked meats, no single kind making up half its weight.','https://farmfetch.co.uk/products/cobble-lane-cured-charcuterie-platter-1','mixed cured meats · mixed sausages · deli platter',['cured selection','sausage selection','cooked deli platter']),
], 'Restraint only. Merged mixed cured meats, mixed sausages and mixed cooked meats (k118, k126, k142) into Charcuterie & deli selection. Kept old models only (Porchetta; Cooked Perfect meatballs/Home Market Foods; SPAM Classic/Hormel Foods). NEEDS WEB PASS: the shelf brief names market-covering tinned brands (Tulip, Libby\'s, Exeter, Hereford) and supermarket own-label cooked meats; these are not in the old data and were left out unsourced. No brand entries added.')
jobs = sys.argv[1:] or list(J)
for j in jobs:
    kinds, notes = J[j]
    p = os.path.join(OUT, j + '.json'); tmp = p + '.tmp'
    with open(tmp, 'w') as f: json.dump({'kinds': kinds, 'brands': [], 'traditions': [], 'notes': notes}, f, ensure_ascii=False, indent=1)
    os.replace(tmp, p)
