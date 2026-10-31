import sys, json, copy, re, os
sys.path.insert(0,'/home/user/Possession-Taxonomy/rebuild/work/V4_J8_SAVOURY')
from lib import *
import bread as B, crisps as C, nuts as N
TT_OWN=["Global group","National champion","Independent","Craft & indie","Own label"]
def BK(n,d,s,x,nl,sel,xg,form=None,page_total=None,cov=None,a=''):
    cnt=len(x)
    if cov is None: cov=f'Complete: {cnt} of {cnt} in the cited page.' if page_total is None else f'Covers {cnt} of {page_total}.'
    return {'n':n,'a':a,'d':d,'s':s,'x':x,'nl':nl,'sel':sel+' '+cov,'xg':xg,
            'tt':[['Owner tier',TT_OWN],['Form',form or ['packaged','fresh','multipack']]]}
def sortx(x):
    return sorted(x,key=lambda e:(e.get('g',''),str(e.get('y','')),e['n'].lower()))
NLB='One entry is a brand sold under its own name; its flavours, sizes and formats are versions.'
# ---------------- BREAD ----------------
def nlb(what): return f'One entry is a {what} sold under its own name; its loaves, flavours and sizes are versions.'
bread_global=[
 BK('Grupo Bimbo bakery brands',"Bread, bun, pastry and snack-cake brands of the Mexican group, the world's largest bakery group by the page's account.",B.S_BIMBO,sortx(B.bimbo),
    nlb('bakery brand in the Grupo Bimbo portfolio'),'Follows the brand and acquisition list on the Grupo Bimbo page (Wikipedia, fetched 2026-10-31). Left to other departments: Barcel and Popcornopolis (savoury snacks); Ricolino sold to Mondelez 2022, Duvalín, Lunetas, La Corona, Vero and Cajeta Coronado (confectionery); East Balt Bakeries and Grupo Adghal (trade suppliers, not branded retail).','country of the brand',
    page_total='about 45 bakery-related names on the page; the rest are listed in other departments or are trade suppliers.',form=['sliced bread','buns','snack cake','tortilla']),
 BK('Associated British Foods bread brands','Bread brands of the British group, including the Hovis takeover completed in July 2026.',B.S_ABF,sortx(B.abfk),
    nlb('bread brand owned by Associated British Foods'),'Follows the Associated British Foods page (fetched 2026-10-31). Ryvita crispbread, Jordans and Dorset Cereals are left to Biscuits & crackers and Snack nuts & bars; Bakers Oven (sold 1994) and Burton\'s (sold 2000) are no longer owned.','country of the brand',
    cov='Covers 6 of the 7 bread brands the page lists as owned; Allied Bakeries itself is the company that holds them.'),
 BK('Lantmännen bakery brands','Bakery brands of the Swedish farmer-owned group.',B.S_LAN,B.lan,
    nlb('bakery brand in the Lantmännen portfolio'),'Follows the brand list on the Lantmännen page (fetched 2026-10-31). Cereal, flour and pasta brands (AXA, Kungsörnen, START!, Amo, Myllyn Paras) belong to the pantry categories; Finn Crisp crispbread to Biscuits & crackers. Unibake, Schulstad and Doggy are not named on the page.','region',
    cov='Covers 4 of 10 food brands on the page; the other 6 are pantry or cracker brands.'),
 BK('Barilla bakery brands','Bread and bakery brands of the Italian family group.',WP+'Barilla_Group',B.bar,
    nlb('bakery brand in the Barilla portfolio'),'Follows the Barilla Group page (fetched 2026-10-31). Biscuit brands (Pavesi, Pan di Stelle, GranCereale, Gocciole, Ringo), Wasa crispbread and Back to Nature belong to Biscuits & crackers; pasta and sauce brands are outside J8.','country of the brand',
    cov='Covers 2 of the bakery brands on the page; the biscuit and cracker brands sit in Biscuits & crackers.'),
 BK("Campbell's bakery brands","Bakery brand of the American soup and snack group.",WP+'Campbell_Soup_Company',B.camp,
    nlb("bakery brand owned by Campbell's"),"Follows the Campbell's Company page (fetched 2026-10-31). Goldfish crackers belong to Biscuits & crackers; Snyder's-Lance snacks to Crisps & savoury snacks.",'country of the brand',cov='Complete: 1 of 1 bakery brand on the page.'),
 BK('Mars bakery brands','Toaster pastry from the Kellanova portfolio, which Mars completed buying on 11 December 2025.',WP+'Kellanova',B.mars,
    nlb('bakery brand owned by Mars'),'Follows the Kellanova page (fetched 2026-10-31). Crackers go to Biscuits & crackers, Pringles to Crisps & savoury snacks, bars to Snack nuts & bars; Eggo, Morningstar Farms, Gardenburger, Incogmeato and the cereals are outside J8.','country of the brand',cov='Covers 1 of 26 Kellanova brands on the page; the others sit in other departments.'),
]
bread_nat=[
 BK('Bread champions: Europe','Leading and long-established bread makers of Europe, beside the group brands.',WP+'Warburtons',sortx(B.eur),
    nlb('bread or bakery brand that leads or is iconic in its European home market'),'Warburtons, Mestemacher, Pågen and Fazer pages (Wikipedia, fetched 2026-10-31); UK shares from The Grocer (26 June 2026, NIQ). Hovis, Kingsmill, Sunblest and Allinson sit under Associated British Foods; Harry-Brot, Mother\'s Pride, Schär and the French and Spanish champions could not be sourced.','country',
    cov='Covers 6 brands from 4 fetched pages; no complete European champion list was found.'),
 BK('Bread champions: North America','American bread and cake makers beside the Bimbo brands.',WP+'Flowers_Foods',sortx(B.fl+B.cake),
    nlb('bread or snack-cake brand that leads or is iconic in its home market'),'Flowers Foods, Twinkie and Colin the Caterpillar pages (Wikipedia, fetched earlier and 2026-10-31). Flowers was the second-largest US baking company as of February 2013.','owner',
    cov='Covers the 5 Flowers Foods brands on its page plus 2 branded cakes; Wonder is the only bread brand shown by a page as sold nationally.'),
 BK('Bread champions: Asia-Pacific','Japanese bread maker and its American subsidiaries; Tip Top sits under Associated British Foods.',WP+'Yamazaki_Baking',B.asia,
    nlb('bread brand that leads or is iconic in its home market'),'Yamazaki Baking page (Wikipedia, fetched 2026-10-31). The Pasco, Shikishima and Indian champions pages could not be fetched.','country',
    cov='Covers 3 brands from one fetched page; incomplete for Asia.'),
 BK('Bread champions: Africa','South African bread and cake brands.',WP+'Tiger_Brands',B.afr,
    nlb('bread or cake brand that leads or is iconic in its home market'),'Tiger Brands and Pioneer Foods pages (Wikipedia, fetched 2026-10-31). No Middle East or North Africa bakery champion could be sourced (Almarai names no bakery brand).','country',
    cov='Covers 3 brands from 2 fetched pages; incomplete for Africa.'),
]
craft_k=BK('Craft and artisan bakeries','Independent bakeries on the Real Bread Campaign Loaf Mark list, plus the Paris sourdough house Poilâne.',B.LM,sortx(B.craft+B.loaf),
    'One entry is an independent bakery that sells bread under its own name; its loaves are versions.','Follows the Loaf Mark licensee list in the Sustain article compiled 1 September 2026 (fetched 2026-10-31), and the Poilâne page (Wikipedia). The Loaf Mark is a licence to use the mark on additive-free loaves, not a certification.','country, then region',
    cov=f'Covers {B.LOAF_D} distinct bakeries from {B.LOAF_N} listed lines in the page text returned; the page says roughly 250 and the summariser may have dropped some, so the list is likely a little short.')
craft_k['tt']=[['Owner tier',TT_OWN],['Loaf Mark',['Real Bread Loaf Mark','Sourdough Loaf Mark']]]
prot=[
 BK('Protected breads','Breads whose name is protected by an EU PDO or PGI, with the district where they are made.',S_WD:='https://www.wikidata.org/wiki/',sortx(B.prot_bread),
    'One entry is a bread whose name is protected as a PDO or PGI; its ordinary and wholemeal forms are versions.','Follows a Wikidata SPARQL query for items with an EU protected-designation identifier (P11794) and a bakery label (fetched 2026-10-31), plus the earlier pages kept on each entry. The EU register (eAmbrosia) needs JavaScript and was not read.','country',
    cov='Covers 8 names; the Wikidata coverage is thin outside Italy, so the French, Spanish, German and other bread names (for example Bayerische Brezel, Brioche vendéenne, Pan de Alfacar, Lesachtaler Brot) are not yet entries.'),
 BK('Protected pastries & festive bakes','Pastries, gingerbreads and festive cakes with protected names.',S_WD,sortx(B.prot_bake),
    'One entry is a pastry or festive bake whose name is protected or listed as a protected geographical indication.','Follows the same Wikidata query and the Pastel de Tentúgal page (Wikipedia, fetched 2026-10-31); Nürnberger Lebkuchen, Dresdner Stollen and Toruń gingerbread keep their earlier pages.','country',
    cov='Covers 7 names; the full register was not readable, so this list is short of the EU bakery class.'),
]
for k in prot: k['tt']=[['Protection',['PDO','PGI','TSG']],['Form',['bread','pastry','festive cake']]]
# forms
def fk(dept,name,**kw): return form_kind(dept,name,**kw)
BR='Bread & bakery'
shelf_forms=[]
for sh in OLDDEPT[BR]['s']:
    kinds=[fk(BR,k['n']) for k in sh['k']]
    shelf_forms.append({'n':sh['n'],'t':sh['t'],'ax':sh['ax'],'k':kinds})
bread_dept=copy.deepcopy(OLDDEPT[BR])
bread_dept['t']="Bread, pastry and cake bought from a baker or shop, fresh or packaged, listed by brand and market, then by the forms they come in; a dry biscuit or cracker → Biscuits & crackers; a chocolate bar → Chocolate; a dish made from bread belongs in the Culinary Taxonomy."
bread_dept['ax']='Who makes the loaf: a global bakery group, a national champion, an independent or a craft bakery; and what form does it take?'
bread_dept['note']='Brands lead; protected names (Pane di Altamura, Aachener Printen, Pastel de Tentúgal) are entries; generic bread and pastry forms stay kinds and link to the Culinary Taxonomy.'
bread_dept['s']=[
 {'n':'Global groups','t':'Bread and bakery brands owned by the multinational groups that dominate packaged baking, one kind per group.','ax':'kinds from the largest group by revenue down','k':bread_global},
 {'n':'National champions','t':'Bread and cake brands that lead or are iconic in their home market, by world region.','ax':'kinds by world region','k':bread_nat},
 {'n':'Craft & indie','t':'Independent bakeries selling real bread under their own name.','ax':'one kind: independent bakeries by country and region','k':[craft_k]},
 {'n':'Protected names','t':'Breads and bakes whose names are protected by EU PDO or PGI status.','ax':'kinds by whether the name is a bread or a pastry and festive bake','k':prot},
]+shelf_forms
bread_dept['msum']="UK bread is led by Warburtons; Grupo Bimbo is the largest group worldwide and the figures below are the last ones the cited pages give."
bread_dept['ms']=[
 {"mkt":"UK branded plant bread","who":"Warburtons","share":"47.2 %","yr":2026,"s":"https://www.thegrocer.co.uk/analysis-and-features/allied-hovis-what-are-the-priorities-now-bakerys-big-merger-is-on/720613.article","note":"share of branded plant bread, 52 weeks to 21 February 2026 (NIQ)"},
 {"mkt":"UK branded plant bread","who":"Hovis and Kingsmill (Allied Bakeries, ABF)","share":"30.6 %","yr":2026,"s":"https://www.thegrocer.co.uk/analysis-and-features/allied-hovis-what-are-the-priorities-now-bakerys-big-merger-is-on/720613.article","note":"combined share of branded plant bread, 52 weeks to 21 February 2026 (NIQ); volumes each fell over 12 %"},
 {"mkt":"UK bread","who":"Warburtons","share":"24 %","yr":2010,"s":WP+"Warburtons","note":"share of the UK bread market as the page states"},
 {"mkt":"UK bread","who":"Hovis takeover by Allied Bakeries (ABF)","share":"£75m","yr":2025,"s":WP+"Associated_British_Foods","note":"purchase price agreed August 2025; completed July 2026"},
 {"mkt":"Global bakery","who":"Grupo Bimbo","share":"MXN 348.8 billion (US$17.1 billion)","yr":2021,"s":WP+"Grupo_Bimbo","note":"revenue; over 100 brands in over 33 countries"},
 {"mkt":"US bread and cake","who":"Flowers Foods","share":"US$5.256 billion","yr":2025,"s":WP+"Flowers_Foods","note":"revenue; second-largest US baking company as of February 2013"},
 {"mkt":"Japan bread","who":"Yamazaki Baking","share":"JPY 995.01 billion","yr":2013,"s":WP+"Yamazaki_Baking","note":"revenue for fiscal 2013"},
 {"mkt":"Italy and Europe bakery","who":"Barilla Group","share":"EUR 4.837 billion","yr":2025,"s":WP+"Barilla_Group","note":"group revenue, all categories"},
 {"mkt":"Nordic food and bakery","who":"Lantmännen","share":"about SEK 18 billion","yr":2024,"s":WP+"Lantm%C3%A4nnen","note":"group turnover, all categories"},
 {"mkt":"US soup, snacks and bakery","who":"Campbell's Company","share":"US$10.3 billion","yr":2025,"s":WP+"Campbell_Soup_Company","note":"revenue, all categories"},
]
# ---------------- CRISPS ----------------
CR='Crisps & savoury snacks'
def gk(name,d,s,x,sel,xg,nl,cov): return BK(name,d,s,sortx(x),nl,sel,xg,cov=cov,form=['potato crisps','corn snacks','pretzels','popcorn','nuts'])
cr_global=[
 gk('PepsiCo (Frito-Lay) brands',"The world's largest savoury snack group: Frito-Lay's American brands and its local brands in Latin America, Europe, Australia and India.",WP+'Frito-Lay',C.pepsico,
    "Follows the brand list on the Frito-Lay page (Wikipedia, fetched 2026-10-31), with Walkers (Leicester, 1948) and Smith's pages for the UK and Australia. Cookie brands (GrandMa's, Gamesa and its lines) go to Biscuits & crackers, Quaker bars to Snack nuts & bars, Japan Frito-Lay to the Calbee kind, and the Indofood-made Indonesian brands to Asia champions.",'region',
    nlb('savoury snack brand owned by PepsiCo'),'Complete: all snack brands named on the Frito-Lay page except those moved to other kinds (cookies, bars, Japan, Indonesia).'),
 gk('Mars (Kellanova) brands','Pringles, in the Kellanova portfolio that Mars completed buying on 11 December 2025.',WP+'Kellanova',C.mars,
    'Follows the Kellanova page (fetched 2026-10-31); Pringles is its only crisp. Crackers, bars and toaster pastry sit in their own departments.','country',
    nlb('crisp or chip brand owned by Mars'),'Complete: 1 of 1 crisp brand on the page.'),
 gk('Intersnack brands','Crisp, snack and nut brands of the German private group, second in European savoury snacks after PepsiCo by the page.',WP+'Intersnack',C.intersnack,
    "Follows the brand list on the Intersnack page (fetched 2026-10-31) and the KP Snacks page. Nut brands (ültje, KP Nuts) go to Snack nuts & bars; Whole Earth (spreads) and Goldfischli (crackers) go elsewhere; Utz is an agreed purchase (July 2026), not yet owned.",'region',
    nlb('crisp or snack brand owned by Intersnack'),'Complete: every crisp and snack brand on the page.'),
 gk('Calbee brands','Snacks of the Japanese group that leads Japanese potato chips.',WP+'Calbee',C.calbee,
    'Follows the product and subsidiary list on the Calbee page (fetched 2026-10-31); Frugra (cereal) goes to the pantry departments.','region',
    nlb('snack brand owned by Calbee'),'Complete: every snack brand on the page.'),
 gk("Campbell's snack brands","Snacks from Snyder's-Lance, which Campbell's bought in early 2018.",CP:=WP+'Campbell_Soup_Company',C.campbell,
    "Follows the Campbell's Company page (fetched 2026-10-31). Pop Secret was sold in August 2024 (see US independents); Goldfish and Pepperidge Farm sit in other departments.",'country',
    nlb("snack brand owned by Campbell's"),'Covers the 6 Snyder\'s-Lance snack brands the page names; Emerald nuts are not named.'),
 gk('General Mills snack brands','Corn snacks and mixes of General Mills.',WP+'General_Mills',C.gmc,
    'Follows the General Mills page (fetched 2026-10-31, first 100,000 characters). Fruit snacks go to Sweets & confectionery; bars go to Snack nuts & bars.','country',
    nlb('savoury snack brand owned by General Mills'),'Complete: 3 of 3 savoury snack brands on the page read.'),
 gk('Grupo Bimbo snack brands','Savoury snacks of the Mexican group.',WP+'Grupo_Bimbo',C.bimbo_snk,
    'Follows the Grupo Bimbo page (fetched 2026-10-31).','country',nlb('savoury snack brand owned by Grupo Bimbo'),'Complete: 3 of 3 snack brands on the page.'),
 gk('Hershey snack brands','Popcorn and pretzel brands the 2026 snack ranking names for The Hershey Company.',C.FN,C.hersh,
    'Follows the FoodNavigator ranking of 29 January 2026 (fetched 2026-10-31).','country',nlb('savoury snack brand owned by Hershey'),'Covers 2 brands the article names.'),
]
cr_nat=[
 gk('Champions: Europe, Russia and Israel','Crisp and snack brands that lead or are iconic outside the group portfolios.',C.PC,C.europe,
    'Follows the List of potato chip brands page (Wikipedia, fetched 2026-10-31) and the Lorenz and Bamba pages. Owners are given only where a page states them.','country',
    nlb('crisp or snack brand that leads or is iconic in its home market'),'Covers 6 brands; no complete European list was found. Spain, Poland and France are covered under PepsiCo and Intersnack; Germany under Intersnack and Lorenz.'),
 gk('Champions: Asia','Snack makers of East, South and Southeast Asia.',C.PC,C.asia,
    'Follows the Euromonitor China savoury snack ranking (bakeryandsnacks.com, 2017), Haldiram\'s, Balaji, Want Want, Koikeya and Nongshim pages and the potato chip brands page (all fetched 2026-10-31).','country',
    nlb('snack brand that leads or is iconic in its home market'),'Covers the 8 companies in the China ranking and 11 other brands; no complete Asian list was found.'),
]
cr_ind=[gk('Independents: United States and Canada','Regional chip brands and independent makers of North America.',C.UZ,C.usind,
    'Follows the Utz Brands page (acquisitions 2011–2022), the Herr\'s page and the regional brands on the potato chip brands page (fetched 2026-10-31). Owners are stated only where a page gives them.','region',
    nlb('chip, popcorn or snack brand sold by a company outside the global groups'),'Covers 22 brands; Utz is to be bought by Intersnack (agreed July 2026).')]
cr_craft=[gk('Craft & indie crisp brands','Small British makers that cook crisps in batches.',C.LF,C.crafts,
    'Follows the Lovefood overview of British craft crisp producers (fetched 2026-10-31); Tyrrells (Intersnack) and Kettle Brand (Campbell\'s) are in their group kinds. Pipers, Just Crisps and Kent Crisps appear only in search excerpts and are not entries.','country',
    nlb('crisp maker working in small batches'),'Covers 4 of the 5 producers the overview names; Burts, Fairfields, Corkers and Yorkshire Crisps are entries and Tyrrells sits under Intersnack.')]
crisp_dept=copy.deepcopy(OLDDEPT[CR])
crisp_dept['t']="Savoury snacks eaten from the packet, from crisps and puffs to pretzels and pork scratchings, listed by brand and market and then by type; nuts and bars → Snack nuts & bars; a cracker or biscuit → Biscuits & crackers."
crisp_dept['ax']='Who sells it: a global snack group, a national champion, an independent or a craft maker; and what is it made from?'
crisp_dept['note']='Brands lead; flavours and formats are versions. Types of snack remain as kinds below.'
crisp_dept['mode']='mixed'
types=[]
for sh in OLDDEPT[CR]['s']:
    types.append({'n':sh['n'],'t':sh['t'],'ax':sh['ax'],'k':[fk(CR,k['n']) for k in sh['k']]})
crisp_dept['s']=[
 {'n':'Global groups','t':'Savoury snack brands of the multinational groups that dominate the category, one kind per group.','ax':'kinds from the largest group by revenue down','k':cr_global},
 {'n':'National champions','t':'Snack brands that lead or are iconic outside the group portfolios, by world region.','ax':'kinds by world region','k':cr_nat},
 {'n':'Independents','t':'Established snack makers outside the global groups.','ax':'one kind per home market','k':cr_ind},
 {'n':'Craft & indie','t':'Small makers named in published craft overviews.','ax':'one kind','k':cr_craft},
]+types
crisp_dept['msum']="PepsiCo's Frito-Lay leads savoury snacks worldwide; in Japan Calbee leads, in India Haldiram's, in China Want Want. The figures below are the last the cited pages give, with their years."
G='https://www.foodnavigator.com/Article/2026/01/29/worlds-biggest-snack-companies-in-2026-ranked/'
crisp_dept['ms']=[
 {"mkt":"Global savoury snacks","who":"PepsiCo","share":"about 25 % or more","yr":2024,"s":G,"note":"estimated share of global savoury snacks; PepsiCo revenue US$91.9 billion (FY2024), all categories"},
 {"mkt":"World snack companies","who":"Mondelēz International","share":"US$36.4 billion","yr":2024,"s":G,"note":"company revenue, all categories; rank 3"},
 {"mkt":"World snack companies","who":"Mars (with Kellanova)","share":"about US$36 billion","yr":2024,"s":G,"note":"combined estimate for snacks; rank 4"},
 {"mkt":"World snack companies","who":"General Mills","share":"US$19.9 billion","yr":2024,"s":G,"note":"company revenue, all categories; rank 5"},
 {"mkt":"World snack companies","who":"The Hershey Company","share":"US$11.2 billion","yr":2024,"s":G,"note":"company revenue; SkinnyPop and Dot's Pretzels named; rank 6"},
 {"mkt":"World snack companies","who":"Intersnack","share":"EUR 4.5 billion or more","yr":2024,"s":G,"note":"revenue; about 3 to 4 % of the European snack market (estimate); the Intersnack page gives EUR 4.51 billion"},
 {"mkt":"World snack companies","who":"Calbee","share":"JPY 303 billion","yr":2024,"s":G,"note":"revenue, financial year ended March 2024"},
 {"mkt":"US savoury snacks","who":"Frito-Lay","share":"40 %","yr":2009,"s":WP+"Frito-Lay","note":"share of US savoury snack sales as the page states"},
 {"mkt":"Savoury snacks outside the US","who":"Frito-Lay","share":"30 %","yr":2009,"s":WP+"Frito-Lay","note":"share of the non-US savoury snack market"},
 {"mkt":"UK savoury snacks","who":"Walkers (PepsiCo)","share":"17.3 %","yr":2024,"s":WP+"Walkers_(snack_foods)","note":"share of Britain's savoury snack market"},
 {"mkt":"UK crisps","who":"Walkers (PepsiCo)","share":"56 %","yr":2013,"s":WP+"List_of_potato_chip_brands","note":"share of the British crisp market"},
 {"mkt":"Japan potato chips","who":"Calbee","share":"about 70 %","yr":"not stated","s":WP+"Calbee","note":"share of Japan's potato chip market; the page cites a 2026 source without dating the figure"},
 {"mkt":"Japan potato chips","who":"Koikeya","share":"second-largest maker","yr":2019,"s":WP+"Koikeya","note":"ranking only, no percentage"},
 {"mkt":"China savoury snacks","who":"Want Want","share":"9.9 %","yr":2016,"s":C.BS,"note":"value share (Euromonitor)"},
 {"mkt":"China savoury snacks","who":"PepsiCo","share":"5.1 %","yr":2016,"s":C.BS,"note":"value share (Euromonitor)"},
 {"mkt":"China savoury snacks","who":"Orion","share":"4.2 %","yr":2016,"s":C.BS,"note":"value share (Euromonitor)"},
 {"mkt":"China savoury snacks","who":"Hefei Huatai Food","share":"3.4 %","yr":2016,"s":C.BS,"note":"value share (Euromonitor)"},
 {"mkt":"China savoury snacks","who":"Shanghai Liwayway Food","share":"2.8 %","yr":2016,"s":C.BS,"note":"value share (Euromonitor)"},
 {"mkt":"China savoury snacks","who":"Fujian Dali Food","share":"2.4 %","yr":2016,"s":C.BS,"note":"value share (Euromonitor)"},
 {"mkt":"China savoury snacks","who":"Three Squirrels","share":"2.3 %","yr":2016,"s":C.BS,"note":"value share (Euromonitor)"},
 {"mkt":"Indian snacks","who":"Haldiram's","share":"Rs 4,224.8 crore","yr":2017,"s":"https://www.restaurantindia.in/news/Haldiram-s-regains-its-Position-as-Largest-Snack-Company.n15113","note":"sales in the year ended September 2017; ahead of PepsiCo at Rs 3,990.7 crore and Balaji at Rs 2,121 crore"},
 {"mkt":"Indian chips","who":"Balaji Wafers","share":"13.7 %","yr":2012,"s":WP+"Balaji_Wafers","note":"share of the local potato and vegetable chip market (Euromonitor); 9.5 % in 2008"},
 {"mkt":"Indian snacks","who":"Haldiram's","share":"Rs 12,800 crore","yr":2024,"s":WP+"Haldiram%27s","note":"company revenue, fiscal 2024, all products"},
 {"mkt":"US regional snacks","who":"Utz Brands","share":"US$1.181 billion","yr":2021,"s":WP+"Utz_Brands","note":"revenue"},
 {"mkt":"Brazil, Germany and France","who":"no figure","share":"n/a","yr":"n/a","s":WP+"Frito-Lay","note":"No fetched page gave a share for these markets; Elma Chips (Brazil), funny-frisch (Germany) and Vico (France) are the group-owned leaders the pages name."},
]
# ---------------- NUTS ----------------
NB='Snack nuts & bars'
nb_global=[
 BK('General Mills bar brands','Cereal, fibre and fruit bars of General Mills.',WP+'General_Mills',sortx(N.gmb),nlb('bar brand owned by General Mills'),'Follows the General Mills page and the Nature Valley page (fetched 2026-10-31).','country',cov='Covers 4 bar brands read on the page.'),
 BK('Mars bar brands','Kind and the Kellanova bars that Mars completed buying in December 2025.',WP+'Kind_(company)',sortx(N.marsb),nlb('bar brand owned by Mars'),'Follows the Kind and Kellanova pages (fetched 2026-10-31).','country',cov='Complete: 7 of 7 bar brands on the Kellanova page plus Kind.'),
 BK('Mondelēz bar brands','Energy bars of the American Clif company, bought by Mondelēz in 2022.',WP+'Clif_Bar_%26_Company',N.mond,nlb('bar brand owned by Mondelēz'),'Follows the Clif Bar page (fetched 2026-10-31).','country',cov='Complete: 1 of 1 (Luna Bar is a version).'),
 BK('PepsiCo bar brands','Quaker bars and rice cakes within Frito-Lay North America.',WP+'Frito-Lay',N.pepb,nlb('bar or cake brand owned by PepsiCo'),'Follows the Frito-Lay page (fetched 2026-10-31); TrueNorth nut crisps sit with PepsiCo snacks.','country',cov='Complete: 2 of 2 on the page.'),
 BK('Intersnack nut brands','Nut brands of the German group.',WP+'Intersnack',N.inter,nlb('nut brand owned by Intersnack'),'Follows the Intersnack and KP Snacks pages (fetched 2026-10-31).','country',cov='Complete: 2 of 2.'),
 BK('Associated British Foods bar brands','British cereal-bar brand of ABF.',WP+'Associated_British_Foods',N.abfn,nlb('cereal and bar brand owned by ABF'),'Follows the ABF page (fetched 2026-10-31); Dorset Cereals and Ryvita sit in the pantry and cracker departments.','country',cov='Covers 1 of 3 ABF cereal brands.'),
]
nb_ind=[BK('Nut and bar brands outside the groups','Nut brands, cooperatives and energy-bar brands outside the global groups.',WP+'Planters',sortx(N.ind),nlb('nut or bar brand sold by a company outside the global groups'),
 'Follows the Planters, Blue Diamond, Graze and Energy bar pages (fetched 2026-10-31) and the Quest page kept from the earlier pass.','country, then energy bars',cov='Covers 11 brands; the Energy bar page is read in full (10 of 10 brands, three of them in group kinds).')]
nuts_dept=copy.deepcopy(OLDDEPT[NB])
nuts_dept['t']="Nuts, seeds, mixes and bars bought as snacks, listed by brand and market and then by type; a chocolate countline → Chocolate; a savoury crisp → Crisps & savoury snacks."
nuts_dept['ax']='Who sells it: a global group, a national champion or independent; and is it a bar, a plain nut or a seasoned mix?'
nuts_dept['note']='Brands lead; plain nuts are commodity kinds with no brand entries; protected nut names are entries.'
nuts_dept['mode']='mixed'
types=[]
for sh in OLDDEPT[NB]['s']:
    ks=[]
    for k in sh['k']:
        kk=fk(NB,k['n'])
        if k['n']=='Hazelnuts':
            kk['x']=[N.nocc]
            kk['nl']='One entry is a hazelnut with a protected name.'
            kk['sel']='Follows the Wikidata record with an EU protected-designation identifier (fetched 2026-10-31). Complete: 1 of 1 hazelnut name found; Wikidata coverage of the EU register is thin.'
            kk['xg']='country'
        if k['n']=='Almonds': kk['a']=(kk.get('a','')+' · Marcona almond').strip(' ·')
        ks.append(kk)
    types.append({'n':sh['n'],'t':sh['t'],'ax':sh['ax'],'k':ks})
nuts_dept['s']=[
 {'n':'Global groups','t':'Bar and nut brands of the multinational groups, one kind per group.','ax':'kinds by group','k':nb_global},
 {'n':'Independents & national champions','t':'Nut and bar brands outside the global groups.','ax':'one kind','k':nb_ind},
]+types
nuts_dept['msum']='Snack bars and nuts are split between a few groups (General Mills, Mars, Mondelēz) and independents; the figures below are deal values and revenues from the cited pages.'
nuts_dept['ms']=[
 {"mkt":"Snack bars","who":"Mars (KIND)","share":"about US$5 billion","yr":2020,"s":WP+"Kind_(company)","note":"reported price of the full takeover"},
 {"mkt":"Energy bars","who":"Mondelēz International (Clif Bar)","share":"US$2.9 billion","yr":2022,"s":WP+"Clif_Bar_%26_Company","note":"agreed price in June 2022"},
 {"mkt":"US peanuts and mixed nuts","who":"Hormel Foods (Planters)","share":"US$3.35 billion","yr":2021,"s":WP+"Planters","note":"price paid to Kraft Heinz, completed 7 June 2021"},
 {"mkt":"World snack companies","who":"General Mills","share":"US$19.9 billion","yr":2024,"s":G,"note":"company revenue, all categories"},
 {"mkt":"World snack companies","who":"Mars (with Kellanova)","share":"about US$36 billion","yr":2024,"s":G,"note":"combined estimate for snacks"},
 {"mkt":"Almonds","who":"Blue Diamond Growers","share":"about 3,500 growers","yr":"not stated","s":WP+"Blue_Diamond_Growers","note":"cooperative membership; the page gives no market share"},
]
# ---------------- ASSEMBLE ----------------
depts=[bread_dept,crisp_dept,nuts_dept]
# cleanup roles
for dp in depts:
    for sh in dp['s']:
        for k in sh['k']:
            for e in k.get('x',[]):
                if e['n'] in ("Lay's",'Hovis','Kettle Brand','Poilâne','Bimbo','Pringles'): e.pop('role',None)
# renames and moves
renames={}
out={'replaces':['Bread & bakery','Crisps & savoury snacks','Snack nuts & bars'],'depts':depts,'brands':[],'brand_updates':{},'renames':renames,'moves':[]}
# brand register
reg=json.load(open(ROOT+'out/J8_brands.json'))['b']
low={b['n'].lower():b for b in reg}
seen=set()
def addb(n,seg,d,kf,c='',f='',s=''):
    if not n or n.lower() in seen or n=='owner not stated': return
    seen.add(n.lower())
    b={'n':n,'seg':seg,'d':d,'kf':kf}
    if c: b['c']=c
    if f and re.fullmatch(r'\d{4}',str(f)): b['f']=str(f)
    if s: b['s']=s
    out['brands'].append(b)
for dp,kf in zip(depts,['bread and bakery','crisps and savoury snacks','nuts and bars']):
    for sh in dp['s']:
        for k in sh['k']:
            for e in k.get('x',[]):
                if 'own' not in e: continue
                for name in {e['n'],e['own']}:
                    if name.lower() in low:
                        if name==e['n']:
                            out['brand_updates'][low[name.lower()]['n']]={'own':e['own'],'tier':e['tier'],'c':e.get('cty','')}
                    else:
                        seg='Artisan & independent' if e['tier']=='Craft & indie' else ('Own-label & retailer' if e['tier']=='Own label' else 'Mainstream')
                        isown=(name==e['own'] and name!=e['n'])
                        addb(name,seg,('Owner of brands in the '+dp['n']+' department.') if isown else e['d'],kf,'' if isown else e.get('cty',''),'' if isown else e.get('y',''),'' if isown else e['s'])
json.dump(out,open(ROOT+'out/J8_parts/SAVOURY.json','w'),ensure_ascii=False)
print('written',os.path.getsize(ROOT+'out/J8_parts/SAVOURY.json'),'brands',len(out['brands']),'updates',len(out['brand_updates']))
