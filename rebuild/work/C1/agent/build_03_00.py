import json, os
W='https://en.wikipedia.org/wiki/'
def A(n,a,d,mk,y,s,v=(),dt=""): return {"n":n,"a":a,"d":d,"mk":mk,"y":y,"s":s,"v":[dict(n=x[0],mk=x[1],y=x[2],d=x[3]) for x in v],"dt":dt}
kinds=[
{"n":"Folding knife","a":"pocket knife · EDC folder · locking folder","d":"Modern locking pocket knife opened one-handed, carried for everyday cutting.",
 "t":["frame lock","liner lock","lockback","AXIS lock","compression lock","assisted opening","flipper"],
 "s":"https://www.knivesandtools.com/en/ct/pocket-knives-and-fixed-blade-knives.htm",
 "x":[A("Chris Reeve Sebenza","Sebenza","Titanium-handled folder that introduced the Integral Lock, the original frame lock.","Chris Reeve Knives","1991",W+"Chris_Reeve_Knives",[("Sebenza 25","Chris Reeve Knives","2012","")],"small or large · titanium handle · inlays"),
  A("Buck 110 Folding Hunter","Buck 110","Brass-bolstered lockback folder strong enough to do a fixed blade's work; set the pattern for the lockback hunter.","Buck","1964",W+"Buck_Knives",[("Ranger 112","Buck","","smaller version")],"wood or synthetic handle · brass bolsters"),
  A("Spyderco Worker","C01 Worker","First knife with Spyderco's round opening hole for one-handed, ambidextrous opening.","Spyderco","1981",W+"Spyderco",[],""),
  A("Spyderco Delica","Delica 4","Light FRN-handled lockback with the round thumb hole; the Endura is its larger sibling.","Spyderco","","https://knifeinformer.com/?p=7204",[("Delica 4","Spyderco","","VG-10 full-flat blade, made in Japan")],"blade plain or serrated · FRN colour"),
  A("Spyderco Paramilitary 2","PM2 · Para 2","Spyderco folder with the strong Compression Lock and a full-flat S30V blade.","Spyderco","","https://morethanjustsurviving.com/spyderco-paramilitary-2-edc-folding-knife-review",[("Paramilitary 2","Spyderco","","replaced the original Paramilitary")],"G10 colour · blade steel"),
  A("Benchmade Griptilian","551 Griptilian","Benchmade's AXIS-lock everyday folder.","Benchmade","",W+"Benchmade",[("551 Griptilian","Benchmade","2014","Gear of the Year award")],"full or mini size · blade shape · handle colour"),
  A("Kershaw Leek","1660","Slim Ken Onion-designed flipper with SpeedSafe torsion-bar assisted opening.","Kershaw","","https://agrussell.com/ecommerce/products/view/2844",[("1660","Kershaw","","3 in plain blade"),("1660ST","Kershaw","","part-serrated")],"blade finish · plain or serrated")],
 "m":[["Bugout 535","Benchmade"],["940 Osborne","Benchmade"],["Elementum II","Civivi"],["Mini Praxis","Civivi"],["Solis","Real Steel"],["Folsom","The James Brand"],["Quickslide Pocket Knife","Stanley"]]},
{"n":"Traditional folding knife","a":"slip-joint knife · regional folding knife · penknife","d":"Traditional or regional pocket knife, usually a slip-joint or friction folder without a modern lock.",
 "t":["slip-joint","friction folder","locking collar","trapper","stockman","peanut"],"s":W+"Barlow_knife",
 "x":[A("Laguiole","Laguiole knife","Slim French slip-joint with a tapered semi-yataghan blade and a 'bee' at the end of the backspring.","","1829",W+"Laguiole_knife",[("Calmels design","","1829","first laguiole, Jean-Pierre Calmels"),("classic form","","c. 1860","navaja-like shape")],"handle horn, wood or bone · shepherd's cross · Thiers or Laguiole made"),
  A("Opinel","Opinel knife","Beech-handled French folding knife with a turning collar lock, made in numbered sizes.","Opinel","1890",W+"Opinel_knife",[("numbered sizes 1–12","Opinel","1897",""),("Virobloc collar","Opinel","1955","locking ring, patented by Marcel Opinel"),("No. 08","Opinel","","most common size")],"size No. 2–13 · carbon XC90 or stainless 12C27M"),
  A("Higonokami","higo no kami","Japanese friction folder with a folded sheet-metal handle and a chikiri lever, no lock.","Nagao Kanekoma","1896",W+"Higonokami",[],"blade steel · handle finish"),
  A("Douk-Douk","","Thiers slip-joint with a folded sheet-metal handle engraved with a Melanesian spirit figure.","Cognet","1929",W+"Douk-Douk",[("Sorcier, El-Baraka, Tiki, l'Écureuil","Cognet","","handle engravings")],"size · handle engraving"),
  A("Barlow","Barlow knife","Sheffield pattern with a long bolster, oval handle and one or two blades.","","early 19th century",W+"Barlow_knife",[("Barlow","Case","","Case Damascus Barlow")],"one or two blades · bolster"),
  A("Case Trapper","54 pattern","Two-blade slip-joint with clip and spey blades, Case's best-known collectable pattern.","Case","",W+"W._R._Case_%26_Sons_Cutlery_Co.",[("Tiny Trapper","Case","","")],"handle material · tang stamp"),
  A("Sod Buster","Sodbuster","Case's plain single-blade work knife.","Case","",W+"W._R._Case_%26_Sons_Cutlery_Co.",[],"")]},
{"n":"Swiss Army knife","a":"Swiss Army knife · officer's knife · penknife · multi-blade knife","d":"Red-handled multi-blade pocket knife with tools such as screwdriver, can opener and corkscrew, made by Victorinox and Wenger.",
 "s":W+"Swiss_Army_knife",
 "x":[A("Swiss soldier's knife","Modell 1890 · Soldatenmesser","Issue knife of the Swiss Army with blade, reamer, can opener and screwdriver.","","1891",W+"Swiss_Army_knife",[("Modell 1890","","1891","first 15,000 from Wester & Co., Solingen"),("Modell 1908","Victorinox","1908–1951","clip-point; made by Victorinox and Wenger"),("Modell 1951","","1951–1961","first stainless tools"),("Modell 1961","","1961–2008","alox scales"),("Soldatenmesser 08","Victorinox","2008","one-hand blade")],""),
  A("Officer's knife","Schweizer Offiziers- und Sportmesser · Original Swiss Army Knife","Karl Elsener's two-blade knife with corkscrew, the base of the civilian Swiss Army knife.","Victorinox","1897",W+"Victorinox",[("Huntsman","Victorinox","",""),("Climber","Victorinox","","")],"91 mm or other lengths · layers · scale colour"),
  A("SwissChamp","","Victorinox's large multi-layer flagship with 33 functions.","Victorinox","1986",W+"Victorinox",[("SwissChamp XXLT","Victorinox","2002–2005","with butane lighter"),("SwissChamp XAVT","Victorinox","2006","80 functions"),("SwissChamp XXL","Victorinox","","")],"layers · functions"),
  A("Wenger Giant","","Wenger's 87-implement knife, recorded by Guinness as the most multifunctional penknife.","Wenger","2006",W+"Swiss_Army_knife",[],"")],
 "m":[["Companion","Victorinox"]]},
{"n":"Multi-tool","a":"pocket multi-tool · multitool","d":"Pocket-size tool with pliers and folding implements (knife, scissors, drivers, file, saw) in its handles.",
 "t":["butterfly-opening pliers","sliding pliers","keychain","no-plier"],"s":"https://leatherman.com/collections/leatherman-multi-tools",
 "x":[A("Leatherman PST","Pocket Survival Tool","Tim Leatherman's folding-plier tool, the originator of the plier multi-tool.","Leatherman","1983",W+"Leatherman",[],""),
  A("Leatherman Super Tool","","Full-size Leatherman with locking implements.","Leatherman","1994",W+"Leatherman",[("Super Tool 200","Leatherman","2001–2005",""),("Super Tool 300","Leatherman","2009","")],""),
  A("Leatherman Wave","","Leatherman with outside-opening blades usable while closed.","Leatherman","1998",W+"Leatherman",[("Wave (new)","Leatherman","2004–2018",""),("Wave Plus","Leatherman","2018",""),("Wave Alpha","Leatherman","","")],""),
  A("Leatherman Charge","","Premium version of the Wave layout with better materials.","Leatherman","2004",W+"Leatherman",[("Charge Ti/XTi","Leatherman","2004–2008",""),("Charge AL/ALX/TTi","Leatherman","2007–2018",""),("Charge+","Leatherman","2018","")],""),
  A("Leatherman Surge","","Large heavy-duty Leatherman.","Leatherman","2005",W+"Leatherman",[("Surge (new)","Leatherman","2013","")],""),
  A("Leatherman Skeletool","","Light skeletonised Leatherman with few tools.","Leatherman","2007",W+"Leatherman",[("Skeletool CX","Leatherman","2007",""),("Skeletool RX","Leatherman","","rescue"),("Skeletool SX","Leatherman","2013","")],""),
  A("Leatherman Micra","","Keychain scissor-based Leatherman.","Leatherman","1996",W+"Leatherman",[],""),
  A("Gerber Multi-Plier","MP600","Gerber multi-tool whose plier head slides out of the handles on rails, openable one-handed.","Gerber","1998","https://wiki.multitool.org/Multi-Plier+600",[("Multi-Plier 600","Gerber","1998","")],"needlenose or bluntnose"),
  A("Victorinox SwissTool","","Victorinox's plier multi-tool.","Victorinox","",W+"Victorinox",[],"")],
 "m":[["Curl","Leatherman"],["Raptor Rescue","Leatherman"],["Rebar","Leatherman"],["Sidekick","Leatherman"],["Signal","Leatherman"],["Wingman","Leatherman"]]},
{"n":"Fixed-blade bushcraft knife","a":"bushcraft knife · sheath knife · outdoor knife","d":"Fixed-blade sheath knife for camp, woodcraft and general outdoor work.",
 "t":["carbon steel","stainless","laminated","Scandi grind","full tang"],"s":W+"Mora_knife",
 "x":[A("Mora knife","Morakniv · Mora of Sweden","Small Swedish sheath knife from the cutleries of Mora, Dalarna, made in carbon or stainless steel.","Morakniv","",W+"Mora_knife",[("Clipper 840/860","Morakniv","","discontinued"),("Companion MG","Morakniv","","carbon or stainless, replaced the Clipper"),("Basic 511 / 546","Morakniv","","carbon / stainless"),("Bushcraft series","Morakniv","",""),("Kansbol","Morakniv","",""),("Garberg","Morakniv","","full tang")],"steel 12C27 or carbon · handle colour"),
  A("Fällkniven F1","","Swedish survival knife, official for Swedish Air Force pilots since 1995.","Fällkniven","1995","https://en.wikipedia.org/wiki/Fällkniven",[("S1","Fällkniven","","longer sibling"),("A1","Fällkniven","","larger sibling")],"laminated VG-10 or 3G steel · sheath")],
 "m":[["162 Bushcrafter","Benchmade"]]},
{"n":"Utility knife","a":"Stanley knife · box cutter · snap-off knife · trimming knife","d":"Knife with a replaceable or snap-off blade for cutting materials in a trade or workshop.",
 "t":["retractable","fixed blade","folding","snap-off 9/18/25 mm"],"s":"https://www.toolstation.com/hand-tools/knives-blades/c28",
 "x":[A("Stanley 99","Classic 99 · 99E","All-metal retractable knife with reversible trapezoid blades stored in the handle.","Stanley","","https://silodrome.com/stanley-classic-99-retractable-utility-knife",[],"metal handle · blade storage"),
  A("OLFA snap-off cutter","snap-off knife","Cutter with a segmented blade whose dull tip is snapped off for a fresh edge.","OLFA","1956",W+"Olfa",[],"9, 18 or 25 mm blade")],
 "m":[["FatMax Pro Knife","Stanley"],["Interlock Snap Off Knife","Stanley"],["Milwaukee FASTBACK Flip Utility Knife","Milwaukee"],["Snap Safe Retractable Knife","Tajima"]],"r":[["FatMax","Stanley"]]}]
K='knowledge'
SEG={'Chris Reeve Knives': 'Premium', 'Buck': 'Mainstream', 'Spyderco': 'Premium', 'Benchmade': 'Premium', 'Kershaw': 'Mainstream', 'Opinel': 'Heritage manufactory', 'Case': 'Heritage manufactory', 'Cognet': 'Heritage manufactory', 'Nagao Kanekoma': 'Artisan & independent', 'Victorinox': 'Heritage manufactory', 'Wenger': 'Heritage manufactory', 'Leatherman': 'Mainstream', 'Gerber': 'Mainstream', 'Morakniv': 'Value', 'Fällkniven': 'Premium', 'Stanley': 'Mainstream', 'OLFA': 'Specialist'}
def B(n,c,f,seg,d,sig,s,lines=(),eras=(),rel=()): return dict(n=n,c=c,f=f,seg=SEG[n],kf=seg,d=d,lines=list(lines),eras=list(eras),sig=sig,sc=[],rel=list(rel),s=s)
brands=[
B("Chris Reeve Knives","South Africa","1984","premium folding knives","Knife maker founded in Durban, later based in the United States; originator of the Integral Lock.",["Chris Reeve Sebenza"],W+"Chris_Reeve_Knives",["Sebenza","Umnumzaan","Inkosi"]),
B("Buck","United States","1947","hunting and pocket knives","American knife maker begun by Hoyt Buck in San Diego, now in Post Falls, Idaho.",["Buck 110 Folding Hunter"],W+"Buck_Knives"),
B("Spyderco","United States","1978","EDC folding knives","Golden, Colorado knife maker founded by Sal Glesser, known for the round opening hole.",["Spyderco Worker","Spyderco Delica","Spyderco Paramilitary 2"],W+"Spyderco"),
B("Benchmade","United States","1979","EDC folding knives","Oregon City knife maker begun as Bali-Song in California; holds the AXIS lock licence.",["Benchmade Griptilian"],W+"Benchmade"),
B("Kershaw","United States","1974","EDC folding knives","Portland knife brand founded by Pete Kershaw, owned by Kai since 1977; SpeedSafe with Ken Onion.",["Kershaw Leek"],W+"Kershaw_Knives",rel=["Zero Tolerance"]),
B("Opinel","France","1890","traditional folding knives","Savoie maker of beech-handled numbered folding knives with the Virobloc collar.",["Opinel"],W+"Opinel_knife"),
B("Case","United States","1889","traditional pocket knives","W. R. Case & Sons of Bradford, Pennsylvania, owned by Zippo; collected by pattern and tang stamp.",["Case Trapper","Sod Buster","Barlow"],"https://en.wikipedia.org/wiki/W._R._Case_%26_Sons_Cutlery_Co."),
B("Cognet","France","","traditional folding knives","Thiers cutler making the Douk-Douk since 1929.",["Douk-Douk"],W+"Douk-Douk"),
B("Nagao Kanekoma","Japan","","traditional folding knives","Miki factory making higonokami knives under the KaneKoma brand.",["Higonokami"],W+"Higonokami"),
B("Victorinox","Switzerland","1884","Swiss Army knives and multi-tools","Ibach knife maker founded by Karl Elsener; absorbed Wenger in 2005.",["Officer's knife","SwissChamp","Victorinox SwissTool"],W+"Victorinox",rel=["Wenger"]),
B("Wenger","Switzerland","1893","Swiss Army knives","Delémont-area supplier of Swiss Army knives, bought by Victorinox in 2005; knife brand merged into Victorinox in 2013.",["Wenger Giant"],W+"Swiss_Army_knife",rel=["Victorinox"]),
B("Leatherman","United States","1983","multi-tools","Portland, Oregon maker founded by Tim Leatherman; originator of the plier multi-tool.",["Leatherman PST","Leatherman Wave","Leatherman Charge","Leatherman Skeletool"],W+"Leatherman"),
B("Gerber","United States","1939","knives and multi-tools","Portland, Oregon knife and multi-tool brand owned by Fiskars.",["Gerber Multi-Plier"],K,rel=["Fiskars"]),
B("Morakniv","Sweden","","outdoor knives","Mora, Dalarna maker formed from KJ Eriksson and Frosts.",["Mora knife"],W+"Mora_knife"),
B("Fällkniven","Sweden","1984","outdoor knives","Boden knife firm founded by Peter Hjortberger, making laminated-steel knives in Japan.",["Fällkniven F1"],"https://en.wikipedia.org/wiki/Fällkniven"),
B("Stanley","United States","1843","hand tools","New Britain, Connecticut hand-tool brand, now Stanley Black & Decker.",["Stanley 99"],"https://silodrome.com/stanley-classic-99-retractable-utility-knife",["FatMax"]),
B("OLFA","Japan","1956","cutters","Osaka maker founded by Yoshio Okada, originator of the snap-off blade.",["OLFA snap-off cutter"],W+"Olfa")]
trads=[
{"n":"Thiers cutlery","g":"Metal & blades","r":"Thiers, Auvergne, France","p":"19th century–present","d":"France's main cutlery centre, making about 70% of the country's cutting tools, including laguiole and Douk-Douk knives.","tech":"forged or stamped blades, slip-joint assembly","mat":"carbon and stainless steel, horn, wood","forms":["Laguiole","Douk-Douk"],"ctr":["Thiers","Laguiole (Forge de Laguiole, Honoré Durand)"],"auth":"'Laguiole' is not a protected name; French makers stamp their mark, steel or 'Made in France' on the blade.","s":W+"Laguiole_knife"},
{"n":"Miki blades","g":"Metal & blades","r":"Miki, Hyōgo, Japan","p":"1896–present (higonokami)","d":"Japanese tool-making town where the higonokami friction folder is still made.","tech":"folded sheet-metal handle, flat-ground laminated blade","mat":"steel, brass","forms":["Higonokami"],"ctr":["Nagao Kanekoma Factory"],"auth":"handle stamped with maker's name and blade steel","s":W+"Higonokami"}]
notes=("Old 'Pocket knife' split: modern locking folders vs traditional/regional; Victorinox Companion/Huntsman moved into Swiss Army knife; SwissChamp XXL moved from Multi-tool. "
 "Left out for lack of a retrieved source: Svord Peasant, Okapi, Spyderco Endura history (1990 date search-only), ESEE, Ka-Bar Becker (KA-BAR is a fighting knife -> Weapons by knife rule), Stockman/Peanut archetypes (kept as types), Stanley 99 launch year (sources conflict 1936/1952/1960s), Victorinox Spartan/Classic SD, SOG PowerAccess. "
 "Stanley AutoLock and Quick Point utility knives dropped as SKU noise. Gerber brand from knowledge.")
out={"kinds":kinds,"brands":brands,"traditions":trads,"notes":notes}
p='work/C1/shelves/03_00.json'; json.dump(out,open(p+'.tmp','w'),ensure_ascii=False,indent=1); os.replace(p+'.tmp',p)
