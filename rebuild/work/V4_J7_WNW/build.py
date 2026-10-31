import json, os
W='https://en.wikipedia.org/wiki/'
TTW=[["Colour and style",["Red","White","Rosé","Sparkling","Sweet or fortified"]],["Labelling",["Appellation only","Appellation and grape","Appellation and vineyard"]]]
def E(n,d,s,g=None,y="",a="",v=None):
    e={"n":n,"a":a,"d":d,"mk":"","y":y,"s":s,"v":v or []}
    if g: e["g"]=g
    return e
def K(n,d,nl,sel,xg,x,a=""):
    return {"n":n,"a":a,"d":d,"nl":nl,"sel":sel,"xg":xg,"x":x,"tt":TTW}
def S(n,t,ks,ax=None):
    s={"n":n,"t":t,"k":ks}
    if ax or len(ks)>3: s["ax"]=ax or "kinds by sub-region"
    return s
def D(n,t,ax,ss):
    return {"n":n,"mode":"tier","t":t,"ax":ax,"s":ss}

# ---------- United States
US=W+'List_of_American_Viticultural_Areas'
raw={
"Hawaii":"Ulupalakua","Arizona":"Sonoita;Verde Valley;Willcox","Arkansas":"Altus;Arkansas Mountain;Ozark Mountain",
"CA-north":"Inwood Valley;Manton Valley;Seiad Valley;Trinity Lakes;Willow Creek",
"CA-central":"Adelaida District;Alisos Canyon;Arroyo Grande Valley;Arroyo Seco;Ballard Canyon;Ben Lomond Mountain;Carmel Valley;Central Coast;Chalone;Cienega Valley;Contra Costa;Creston District;Edna Valley;El Pomar District;Gabilan Mountains;Hames Valley;Happy Canyon of Santa Barbara;Lamorinda;Lime Kiln Valley;Livermore Valley;Los Olivos District;Monterey;Mt. Harlan;Pacheco Pass;Paicines;Paso Robles;Paso Robles Estrella District;Paso Robles Geneseo District;Paso Robles Highlands District;Paso Robles Willow Creek District;San Antonio Valley;San Benito;San Bernabe;San Francisco Bay;San Juan Creek;San Lucas;San Luis Obispo Coast;San Miguel District;San Ysidro District;Santa Clara Valley;Santa Cruz Mountains;Santa Lucia Highlands;Santa Margarita Ranch;Santa Maria Valley;Santa Ynez Valley;Sta. Rita Hills;Templeton Gap District;York Mountain",
"CA-valley":"Alta Mesa;Borden Ranch;Capay Valley;Clarksburg;Clements Hills;Cosumnes River;Diablo Grande;Dunnigan Hills;Jahant;Lodi;Madera;Merritt Island;Mokelumne River;Paulsell Valley;River Junction;Salado Creek;Sloughhouse;Squaw Valley-Miramonte;Tracy Hills;Winters Highlands",
"CA-north-coast":"Alexander Valley;Anderson Valley;Atlas Peak;Benmore Valley;Bennett Valley;Big Valley District-Lake County;Calistoga;Chalk Hill;Chiles Valley;Clear Lake;Cole Ranch;Comptche;Coombsville;Covelo;Crystal Springs of Napa Valley;Diamond Mountain District;Dos Rios;Dry Creek Valley;Eagle Peak Mendocino County;Fort Ross-Seaview;Fountaingrove District;Green Valley of Russian River Valley;Guenoc Valley;High Valley;Howell Mountain;Kelsey Bench-Lake County;Knights Valley;Long Valley-Lake County;Los Carneros;McDowell Valley;Mendocino;Mendocino Ridge;Moon Mountain District Sonoma County;Mt. Veeder;Napa Valley;North Coast;Northern Sonoma;Oak Knoll District of Napa Valley;Oakville;Petaluma Gap;Pine Mountain-Cloverdale Peak;Potter Valley;Red Hills Lake County;Redwood Valley;Rockpile;Russian River Valley;Rutherford;Solano County Green Valley;Sonoma Coast;Sonoma Mountain;Sonoma Valley;Spring Mountain District;St. Helena;Stags Leap District;Suisun Valley;Upper Lake Valley;West Sonoma Coast;Wild Horse Valley;Yorkville Highlands;Yountville",
"CA-sierra":"California Shenandoah Valley;El Dorado;Fair Play;Fiddletown;North Yuba;Sierra Foothills",
"CA-south":"Antelope Valley of the California High Desert;Cucamonga Valley;Leona Valley;Malibu Coast;Malibu-Newton Canyon;Palos Verdes Peninsula;Ramona Valley;Saddle Rock-Malibu;San Luis Rey;San Pasqual Valley;Sierra Pelona Valley;South Coast;Tehachapi Mountains;Temecula Valley;Yucaipa Valley",
"Colorado":"Grand Valley;West Elks","Connecticut":"Eastern Connecticut Highlands;Southeastern New England;Western Connecticut Highlands",
"Georgia":"Dahlonega Plateau;Upper Hiwassee Highlands","Idaho":"Eagle Foothills;Lewis-Clark Valley;Snake River Valley",
"Illinois":"Shawnee Hills;Upper Mississippi River Valley","Indiana":"Indiana Uplands;Ohio River Valley","Iowa":"Loess Hills District",
"Louisiana":"Mississippi Delta","Maryland":"Catoctin;Cumberland Valley;Linganore","Massachusetts":"Martha's Vineyard;Nashoba Valley",
"Michigan":"Fennville;Lake Michigan Shore;Leelanau Peninsula;Old Mission Peninsula;Tip of the Mitt","Minnesota":"Alexandria Lakes",
"Missouri":"Augusta;Hermann;Ozark Highlands","New Jersey":"Cape May Peninsula;Central Delaware Valley;Outer Coastal Plain;Warren Hills",
"New Mexico":"Mesilla Valley;Middle Rio Grande Valley;Mimbres Valley",
"New York":"Cayuga Lake;Champlain Valley of New York;Finger Lakes;Hudson River Region;Lake Erie;Long Island;Niagara Escarpment;North Fork of Long Island;Seneca Lake;The Hamptons, Long Island;Upper Hudson",
"North Carolina":"Appalachian High Country;Crest of the Blue Ridge Henderson County;Haw River Valley;Swan Creek;Tryon Foothills;Yadkin Valley",
"Ohio":"Grand River Valley;Isle St. George;Loramie Creek",
"Oregon":"Applegate Valley;Chehalem Mountains;Columbia Gorge;Columbia Valley;Dundee Hills;Elkton Oregon;Eola-Amity Hills;Laurelwood District;Lower Long Tom;McMinnville;Mount Pisgah, Polk County;Red Hill Douglas County;Ribbon Ridge;The Rocks District of Milton-Freewater;Rogue Valley;Snake River Valley;Southern Oregon;Tualatin Hills;Umpqua Valley;Van Duzer Corridor;Walla Walla Valley;Willamette Valley;Yamhill-Carlton",
"Pennsylvania":"Lancaster Valley;Lehigh Valley","Tennessee":"Nine Lakes of East Tennessee;Upper Cumberland",
"Texas":"Bell Mountain;Escondido Valley;Fredericksburg in the Texas Hill Country;Texas Davis Mountains;Texas High Plains;Texas Hill Country;Texoma",
"Virginia":"Middleburg Virginia;Monticello;North Fork of Roanoke;Northern Neck George Washington Birthplace;Rocky Knob;Shenandoah Valley;Virginia's Eastern Shore;Virginia Peninsula",
"Washington":"Ancient Lakes of the Columbia Valley;Beverly, Washington;Candy Mountain;Columbia Hills;Goose Gap;Horse Heaven Hills;Lake Chelan;Naches Heights;Puget Sound;Rattlesnake Hills;Red Mountain;Rocky Reach;Royal Slope;Snipes Mountain;The Burn of Columbia Valley;Wahluke Slope;White Bluffs;Yakima Valley",
"West Virginia":"Kanawha River Valley","Wisconsin":"Lake Wisconsin;Wisconsin Ledge",
}

add_first={"Arkansas":["Ozark Mountain"],"Illinois":["Upper Mississippi River Valley"],"Indiana":["Ohio River Valley"],"Iowa":["Loess Hills District"],"Louisiana":["Mississippi Delta"],"Maryland":["Cumberland Valley"],"Connecticut":[],"New Jersey":[],"New Mexico":[],"New York":["Lake Erie"],"North Carolina":["Appalachian High Country"],"Georgia":["Upper Hiwassee Highlands"],"Idaho":[],"Oregon":["Columbia Gorge","Columbia Valley","Walla Walla Valley"],"Virginia":["Shenandoah Valley"]}
multi={"Ozark Mountain":"Arkansas, Missouri and Oklahoma","Upper Mississippi River Valley":"Illinois, Iowa, Minnesota and Wisconsin","Ohio River Valley":"Indiana, Kentucky, Ohio and West Virginia","Southeastern New England":"Connecticut, Massachusetts and Rhode Island","Loess Hills District":"Iowa and Missouri","Mississippi Delta":"Louisiana, Mississippi and Tennessee","Cumberland Valley":"Maryland and Pennsylvania","Central Delaware Valley":"New Jersey and Pennsylvania","Mesilla Valley":"New Mexico and Texas","Lake Erie":"New York, Ohio and Pennsylvania","Appalachian High Country":"North Carolina, Tennessee and Virginia","Upper Hiwassee Highlands":"Georgia and North Carolina","Snake River Valley":"Idaho and Oregon","Lewis-Clark Valley":"Idaho and Washington","Columbia Gorge":"Oregon and Washington","Columbia Valley":"Oregon and Washington","Walla Walla Valley":"Oregon and Washington","Shenandoah Valley":"Virginia and West Virginia"}
# state AVAs with their multi-state ones filed once at the first state that lists them
raw["Oregon"]="Applegate Valley;Chehalem Mountains;Columbia Gorge;Columbia Valley;Dundee Hills;Elkton Oregon;Eola-Amity Hills;Laurelwood District;Lower Long Tom;McMinnville;Mount Pisgah, Polk County;Red Hill Douglas County;Ribbon Ridge;The Rocks District of Milton-Freewater;Rogue Valley;Southern Oregon;Tualatin Hills;Umpqua Valley;Van Duzer Corridor;Walla Walla Valley;Willamette Valley;Yamhill-Carlton"
raw["Idaho"]="Eagle Foothills;Lewis-Clark Valley;Snake River Valley"
raw["Arkansas"]="Altus;Arkansas Mountain;Ozark Mountain"
raw["Illinois"]="Shawnee Hills;Upper Mississippi River Valley"
raw["Indiana"]="Indiana Uplands;Ohio River Valley"
raw["Iowa"]="Loess Hills District"
raw["Louisiana"]="Mississippi Delta"
raw["Maryland"]="Catoctin;Cumberland Valley;Linganore"
raw["Pennsylvania"]="Lancaster Valley;Lehigh Valley"
raw["Missouri"]="Augusta;Hermann;Ozark Highlands"
raw["Kentucky"]="";raw["Mississippi"]="";raw["Oklahoma"]="";raw["Rhode Island"]="";raw["Minnesota"]="Alexandria Lakes";raw["Ohio"]="Grand River Valley;Isle St. George;Loramie Creek"
raw["Georgia"]="Dahlonega Plateau;Upper Hiwassee Highlands"
raw["Virginia"]="Middleburg Virginia;Monticello;North Fork of Roanoke;Northern Neck George Washington Birthplace;Rocky Knob;Shenandoah Valley;Virginia's Eastern Shore;Virginia Peninsula"
raw["New Jersey"]="Cape May Peninsula;Central Delaware Valley;Outer Coastal Plain;Warren Hills"
raw["New Mexico"]="Mesilla Valley;Middle Rio Grande Valley;Mimbres Valley"
raw["North Carolina"]="Appalachian High Country;Crest of the Blue Ridge Henderson County;Haw River Valley;Swan Creek;Tryon Foothills;Yadkin Valley"
raw["New York"]="Cayuga Lake;Champlain Valley of New York;Finger Lakes;Hudson River Region;Lake Erie;Long Island;Niagara Escarpment;North Fork of Long Island;Seneca Lake;The Hamptons, Long Island;Upper Hudson"
raw["Connecticut"]="Eastern Connecticut Highlands;Southeastern New England;Western Connecticut Highlands"
raw["Washington"]="Ancient Lakes of the Columbia Valley;Beverly, Washington;Candy Mountain;Columbia Hills;Goose Gap;Horse Heaven Hills;Lake Chelan;Naches Heights;Puget Sound;Rattlesnake Hills;Red Mountain;Rocky Reach;Royal Slope;Snipes Mountain;The Burn of Columbia Valley;Wahluke Slope;White Bluffs;Yakima Valley"
raw["Tennessee"]="Nine Lakes of East Tennessee;Upper Cumberland"
raw["West Virginia"]="Kanawha River Valley"
raw["Massachusetts"]="Martha's Vineyard;Nashoba Valley"
raw["Wisconsin"]="Lake Wisconsin;Wisconsin Ledge"
seen=set()
def usents(keys,labels):
    out=[]
    for key in keys:
        g=labels.get(key,key)
        for n in raw[key].split(';'):
            if not n or n in seen: continue
            seen.add(n)
            where=multi.get(n) or ("California" if key.startswith("CA") else key)
            out.append(E(n,"Viticultural area in "+where+".",US,g))
    return out
NL="One entry is an American Viticultural Area, a grape-growing area delimited and approved by the Alcohol and Tobacco Tax and Trade Bureau (TTB)."
SEL="Every AVA listed on Wikipedia's List of American Viticultural Areas, fetched 2026-10-31. An AVA that spans several states is filed once, under the first state that lists it. The page gives no approval years."
def usk(name,d,keys,labels=None,xg="state or region"):
    return K(name,d,NL,SEL,xg,usents(keys,labels or {}))
CAL={"CA-north-coast":"North Coast","CA-central":"Central Coast","CA-valley":"Central Valley","CA-sierra":"Sierra Foothills","CA-south":"South Coast","CA-north":"Northern interior"}
US_SHELVES=[
 S("California","California AVAs, grouped by the region the Wikipedia list uses.",[
  usk("California: North Coast AVAs","Napa, Sonoma, Mendocino and Lake County AVAs, including Napa Valley, Russian River Valley and Alexander Valley.",["CA-north-coast"],CAL),
  usk("California: Central Coast AVAs","AVAs from Santa Cruz south to Santa Barbara, with Paso Robles and Monterey.",["CA-central"],CAL),
  usk("California: Central Valley AVAs","AVAs of the Sacramento and San Joaquin valleys, including Lodi and Clarksburg.",["CA-valley"],CAL),
  usk("California: Sierra Foothills AVAs","AVAs in the Sierra Nevada foothills, such as El Dorado and Fiddletown.",["CA-sierra"],CAL),
  usk("California: South Coast AVAs","AVAs from Malibu to Temecula and the high desert.",["CA-south"],CAL),
  usk("California: northern interior AVAs","Five small AVAs in the far north of California.",["CA-north"],CAL),
 ],"California regions, north to south"),
 S("Pacific Northwest","Oregon, Washington and Idaho AVAs.",[
  usk("Oregon AVAs","AVAs of Oregon, led by the Willamette Valley; the Columbia names shared with Washington are filed here.",["Oregon"]),
  usk("Washington AVAs","AVAs of Washington State.",["Washington"]),
  usk("Idaho AVAs","AVAs of Idaho, including the shared Snake River Valley.",["Idaho"]),
 ]),
 S("Southwest, Mountain West & Hawaii","AVAs of the dry interior and the islands.",[
  usk("Texas AVAs","AVAs of Texas, from the Hill Country to the High Plains.",["Texas"]),
  usk("Arizona, New Mexico and Colorado AVAs","AVAs of the Southwest and Rockies.",["Arizona","New Mexico","Colorado"]),
  usk("Hawaii AVAs","The single AVA in Hawaii.",["Hawaii"]),
 ]),
 S("Midwest & Ozarks","AVAs of the Great Lakes, the upper Mississippi and the Ozarks.",[
  usk("Great Lakes AVAs","AVAs around the Great Lakes.",["Michigan","Ohio","Minnesota","Wisconsin"]),
  usk("Upper Mississippi and Ohio valley AVAs","AVAs along the upper Mississippi and Ohio rivers.",["Illinois","Indiana","Iowa"]),
  usk("Missouri and Ozark AVAs","AVAs of Missouri and Arkansas.",["Missouri","Arkansas"]),
 ]),
 S("South & Mid-Atlantic","AVAs from the Mississippi Delta to the Carolinas and Virginia.",[
  usk("Southern AVAs","AVAs of Louisiana, Georgia, Tennessee and North Carolina.",["Louisiana","Georgia","Tennessee","North Carolina"]),
  usk("Virginia and Maryland AVAs","AVAs of Virginia, West Virginia and Maryland.",["Virginia","West Virginia","Maryland"]),
  usk("New Jersey and Pennsylvania AVAs","AVAs of New Jersey and Pennsylvania.",["New Jersey","Pennsylvania"]),
 ]),
 S("New York & New England","AVAs of New York and southern New England.",[
  usk("New York AVAs","AVAs of New York, including the Finger Lakes and Long Island.",["New York"]),
  usk("New England AVAs","AVAs of Connecticut and Massachusetts.",["Connecticut","Massachusetts"]),
 ]),
]

# ---------- generic helpers for national lists
def NLx(what): return "One entry is "+what+"."
def kind(name,d,what,sel,xg,rows,src):
    # rows: (name, description, group[, year])
    x=[E(r[0],r[1],r[4] if len(r)>4 and r[4] else src,r[2],r[3] if len(r)>3 else "") for r in rows]
    return K(name,d,NLx(what),sel,xg,x)
# ---------- Canada & Mexico
VQA=W+'Vintners_Quality_Alliance'; CAN=W+'Canadian_wine'; MEX=W+'Mexican_wine'
canON=[("Niagara Peninsula","Ontario VQA viticultural area containing most of the province's vineyards, with nine sub-appellations.","Ontario"),
("Niagara Escarpment","Sub-area of the Niagara Peninsula VQA, holding three bench sub-appellations.","Niagara Peninsula"),
("Short Hills Bench","Sub-appellation within Niagara Escarpment.","Niagara Escarpment"),
("Twenty Mile Bench","Sub-appellation within Niagara Escarpment.","Niagara Escarpment"),
("Beamsville Bench","Sub-appellation within Niagara Escarpment.","Niagara Escarpment"),
("Niagara-on-the-Lake","Sub-area of the Niagara Peninsula VQA, holding four sub-appellations.","Niagara Peninsula"),
("Niagara River","Sub-appellation within Niagara-on-the-Lake.","Niagara-on-the-Lake"),
("Niagara Lakeshore","Sub-appellation within Niagara-on-the-Lake.","Niagara-on-the-Lake"),
("Four Mile Creek","Sub-appellation within Niagara-on-the-Lake.","Niagara-on-the-Lake"),
("St. David's Bench","Sub-appellation within Niagara-on-the-Lake.","Niagara-on-the-Lake"),
("Vinemount Ridge","Sub-appellation of the Niagara Peninsula VQA.","Niagara Peninsula"),
("Creek Shores","Sub-appellation of the Niagara Peninsula VQA.","Niagara Peninsula"),
("Lincoln Lakeshore","Sub-appellation of the Niagara Peninsula VQA.","Niagara Peninsula"),
("Lake Erie North Shore","Ontario VQA viticultural area on the north shore of Lake Erie.","Ontario"),
("South Islands","Sub-appellation of Lake Erie North Shore.","Lake Erie North Shore"),
("Prince Edward County","Ontario VQA viticultural area on Lake Ontario.","Ontario")]
canBC=[("Fraser Valley","British Columbia geographical indication.","British Columbia"),("Gulf Islands","British Columbia geographical indication.","British Columbia"),("Kootenays","British Columbia geographical indication.","British Columbia"),("Lillooet","British Columbia geographical indication.","British Columbia"),
("Okanagan Valley","British Columbia geographical indication holding eleven sub-geographical indications.","British Columbia"),
("East Kelowna Slopes","Sub-geographical indication of the Okanagan Valley.","Okanagan Valley"),("Golden Mile Bench","Sub-geographical indication of the Okanagan Valley.","Okanagan Valley"),("Golden Mile Slopes","Sub-geographical indication of the Okanagan Valley.","Okanagan Valley"),("Lake Country","Sub-geographical indication of the Okanagan Valley.","Okanagan Valley"),("Okanagan Falls","Sub-geographical indication of the Okanagan Valley.","Okanagan Valley"),("Naramata Bench","Sub-geographical indication of the Okanagan Valley.","Okanagan Valley"),("Skaha Bench","Sub-geographical indication of the Okanagan Valley.","Okanagan Valley"),("South Kelowna Slopes","Sub-geographical indication of the Okanagan Valley.","Okanagan Valley"),("Summerland Bench","Sub-geographical indication of the Okanagan Valley.","Okanagan Valley"),("Summerland Lakefront","Sub-geographical indication of the Okanagan Valley.","Okanagan Valley"),("Summerland Valleys","Sub-geographical indication of the Okanagan Valley.","Okanagan Valley"),
("Shuswap","British Columbia geographical indication.","British Columbia"),("Similkameen Valley","British Columbia geographical indication.","British Columbia"),("Thompson Valley","British Columbia geographical indication.","British Columbia"),
("Vancouver Island","British Columbia geographical indication holding the Cowichan Valley.","British Columbia"),("Cowichan Valley","Sub-geographical indication of Vancouver Island.","Vancouver Island")]
SELV="Every designated area on Wikipedia's Vintners Quality Alliance page for this province, fetched 2026-10-31, with sub-appellations as their own entries sectioned by parent. The page gives no years; areas it calls emerging are left out."
cm_ks=[
 kind("Ontario VQA areas","The VQA viticultural areas of Ontario and the sub-appellations within them.","a VQA viticultural area or sub-appellation of Ontario",SELV,"parent area",canON,VQA),
 kind("British Columbia VQA geographical indications","The geographical indications of British Columbia and the Okanagan sub-geographical indications.","a VQA geographical indication or sub-geographical indication of British Columbia",SELV,"parent area",canBC,VQA)]
mexB=[("Valle de Guadalupe","Baja California valley around San Antonio de las Minas; the page gives a Baja-wide grape list of Cabernet Sauvignon, Ruby Cabernet, Zinfandel, Grenache and Mission, with Chenin Blanc, Palomino, Riesling, Sauvignon Blanc and Sémillon.","Baja California"),("Valle de San Vicente","Baja California valley.","Baja California"),("Llano Colorado","Baja California valley.","Baja California"),("Santo Tomás Valley","Baja California valley.","Baja California"),("Calafia Valley","Baja California valley.","Baja California"),("Ensenada","Baja California area of boutique producers.","Baja California")]
mexC=[("Parras Valley","La Laguna wine area in Coahuila; Cabernet Sauvignon, Shiraz, Merlot and Tempranillo, with some whites.","Coahuila and Durango"),("Cuatro Ciénegas","Wine area in Coahuila.","Coahuila and Durango"),
("Ezequiel Montes","Wine area in Querétaro; the Central region is mostly sparkling wine.","Querétaro"),("San Juan del Río","Wine area in Querétaro.","Querétaro"),("Bernal","Wine area in Querétaro.","Querétaro"),("Tequisquiapan","Wine town in Querétaro.","Querétaro"),
("Ojocaliente","Wine area in Zacatecas; Cabernet Sauvignon, Merlot, Zinfandel, Black Spanish and Lenoir.","Zacatecas"),("Valle de la Macarena","Wine area in Zacatecas.","Zacatecas"),("Valle de las Arcinas","Wine area in Zacatecas.","Zacatecas")]
mexD=[("Cuatro Sierras","Sonora wine area between Agua Prieta and Cananea; Cabernet Sauvignon, Touriga Nacional, Carmenère, Grenache, Chardonnay and Verdejo.","Sonora"),("Cerocahui Valley","Small vineyard area in Chihuahua.","Chihuahua"),("San Miguel de Allende","Wine area in Guanajuato.","Guanajuato"),("Dolores Hidalgo","Wine town in Guanajuato.","Guanajuato")]
SELM="Every wine area named on Wikipedia's Mexican wine page, fetched 2026-10-31. Mexico has no appellation system on that page, so national wine areas stand in; areas with only a historical planting are left out."
cm_mx=[kind("Baja California wine valleys","The wine valleys of Baja California, Mexico's main wine state.","a wine valley or area of Baja California",SELM,"state",mexB,MEX),
 kind("Central and northern Mexican wine areas","Wine areas of Coahuila, Querétaro, Zacatecas, Sonora and other states.","a national wine area outside Baja California",SELM,"state",mexC+mexD,MEX)]
DEPT_CM=D("Wine of Canada & Mexico","Wine from Canada by VQA area and from Mexico by wine valley; a wine from the United States → Wine of the United States.","Which country, which province or state, and which designated area?",
 [S("Canada","Canadian VQA areas by province.",cm_ks),S("Mexico","Mexican wine valleys and areas by state.",cm_mx)])

# ---------- South America
CHI=W+'Chilean_wine'; ARG=W+'Argentine_wine'; URU=W+'Uruguayan_wine'; BRA=W+'Brazilian_wine'
SELC="Every wine region and sub-region on Wikipedia's Chilean wine page, fetched 2026-10-31 (first part of the page only), sectioned by macro-region. Sub-regions are separate entries beside their valley."
chi=lambda rows,d,n: kind(n,d,"a Chilean wine region or sub-region",SELC,"parent valley",rows,CHI)
chiN=[("Copiapó Valley","Atacama valley; mostly pisco and table grapes, with small-scale wine since the 1950s.","Atacama"),("Huasco Valley","Atacama valley; pisco, table grapes and Pajarete.","Atacama"),("Elqui Valley","Coquimbo valley; Syrah, with pisco and table grapes.","Coquimbo"),("Limarí Valley","Coquimbo valley; Sauvignon Blanc, Chardonnay, Syrah and Pinot Noir.","Coquimbo"),("Choapa Valley","Coquimbo valley; Syrah and Cabernet Sauvignon around Illapel and Salamanca.","Coquimbo"),
("Aconcagua Valley","Aconcagua region valley; red varieties, with white grapes in new coastal plantings.","Aconcagua"),("Casablanca Valley","Aconcagua region valley; Sauvignon Blanc, Chardonnay and Pinot Noir.","Aconcagua"),("San Antonio Valley","Aconcagua region valley; Pinot Noir, Sauvignon Blanc and Chardonnay.","Aconcagua")]
chiC=[("Maipo Valley","Central Valley valley with three sub-regions.","Maipo"),("Alto Maipo","Upper Maipo; Cabernet Sauvignon.","Maipo"),("Central Maipo","Central Maipo; Cabernet Sauvignon and Carmenère.","Maipo"),("Pacific Maipo","Coastal Maipo; Sauvignon Blanc.","Maipo"),
("Rapel Valley","Central Valley valley holding Cachapoal and Colchagua.","Rapel"),("Cachapoal Valley","Rapel sub-region; Cabernet Sauvignon inland, Carmenère toward the coast.","Rapel"),("Colchagua Valley","Rapel sub-region; Malbec, Cabernet Sauvignon, Carmenère and Syrah.","Rapel"),
("Curicó Valley","Central Valley valley with Teno and Lontué sub-regions; Cabernet Sauvignon and Sauvignon Blanc.","Curicó"),("Maule Valley","Central Valley valley; Cabernet Sauvignon, Carmenère, old-vine Carignan, Merlot, Cabernet Franc and Malbec.","Maule")]
chiS=[("Itata Valley","Southern valley; País, Muscat of Alexandria and Carignan, with newer Cabernet Sauvignon.","Southern Chile"),("Bío-Bío Valley","Southern valley; Pinot Noir, Chardonnay and Sauvignon Blanc.","Southern Chile"),("Malleco Valley","Southern valley; Chardonnay and Pinot Noir.","Southern Chile")]
SA_CHI=[S("Chile","Chilean wine regions from the dry north to the cool south.",[chi(chiN,"Valleys of the Atacama, Coquimbo and Aconcagua regions.","Chile: northern and coastal valleys"),chi(chiC,"Valleys and sub-regions of the Central Valley: Maipo, Rapel, Curicó and Maule.","Chile: Central Valley"),chi(chiS,"Valleys of southern Chile.","Chile: southern valleys")])]
SELA="Every wine province and sub-region on Wikipedia's Argentine wine page, fetched 2026-10-31 (first part of the page only). Argentina's provinces are used as national wine regions; sub-regions sit beside them."
arg=lambda rows,d,n: kind(n,d,"an Argentine wine province or sub-region",SELA,"province",rows,ARG)
argCuyo=[("Mendoza","Province with over 60 % of output; Malbec leads.","Mendoza"),("Luján de Cuyo","Mendoza area; Malbec; first controlled appellation in Mendoza, 1993.","Mendoza"),("Uco Valley","Mendoza valley; Malbec, old-vine Tempranillo and Chardonnay.","Mendoza"),("Tupungato","Mendoza area; Chardonnay and Malbec.","Mendoza"),("Gualtallary","Sub-district of Tupungato; Malbec.","Mendoza"),("Maipú","Mendoza area; Cabernet Sauvignon.","Mendoza"),
("San Juan","Province; Torrontés Sanjuanino and Pedro Giménez, with sherry-style wine, brandy and vermouth.","San Juan"),("Tulum Valley","San Juan valley; Syrah, Bonarda and Cereza.","San Juan"),("Pedernal Valley","High-altitude valley in western San Juan.","San Juan"),("Calingasta","San Juan department.","San Juan"),("Ullum","San Juan department.","San Juan"),("Zonda","San Juan department.","San Juan"),
("La Rioja","Province; Torrontés Riojano and Moscatel de Alexandria.","La Rioja")]
argNW=[("Salta","Province of high-altitude vineyards.","Salta"),("Cafayate","Calchaquí Valleys area in Salta; Torrontés Riojano, Cabernet Sauvignon and Tannat.","Salta"),("Cachi","Calchaquí Valleys area in Salta.","Salta"),("Catamarca","Northwest province.","Catamarca"),("Jujuy","Northwest province.","Jujuy")]
argP=[("Río Negro","Patagonian province; Pinot Noir, Merlot, Chardonnay and Sauvignon Blanc.","Río Negro"),("Neuquén","Patagonian province; Upper Neuquén Valley (San Patricio del Chañar) grows Pinot Noir, Chardonnay, Malbec, Semillon and Torrontés Riojano.","Neuquén"),("La Pampa","Province; Cabernet Franc in the Colorado River area (25 de Mayo).","La Pampa"),("Chubut","Patagonian province; Pinot Noir, Chardonnay, Sauvignon Blanc, Gewürztraminer, Merlot, Riesling and Pinot Gris.","Chubut"),("Trevelin Valley","Chubut cool-climate valley.","Chubut")]
argO=[("Buenos Aires Province","Province with coastal and southern-hill vineyards (Mar del Plata, Médanos).","Buenos Aires"),("Córdoba","Province; Sierras de Córdoba vineyards.","Córdoba"),("Entre Ríos","Province with wine named on the page.","Entre Ríos"),("Santiago del Estero","Province with the first recorded commercial vineyard, 1557.","Santiago del Estero")]
SA_ARG=[S("Argentina","Argentine wine provinces by region.",[arg(argCuyo,"Mendoza, San Juan and La Rioja.","Argentina: Cuyo"),arg(argNW,"Salta, Catamarca and Jujuy.","Argentina: Northwest"),arg(argP,"Río Negro, Neuquén, La Pampa and Chubut.","Argentina: Patagonia"),arg(argO,"Provinces of the east and centre.","Argentina: Buenos Aires, Córdoba and the east")])]
uru=[("Artigas",115),("Canelones",5046),("Colonia",563),("Durazno",89),("Florida",49),("Lavalleja",10),("Maldonado",252),("Montevideo",1073),("Paysandú",172),("Rivera",47),("Rocha",8),("Salto",58),("San José",502),("Soriano",11),("Tacuarembó",28)]
uruK=kind("Uruguay wine departments","The vineyard departments of Uruguay, led by Canelones; Tannat is the main grape.","a Uruguayan department with vineyards","Every department with vineyards on Wikipedia's Uruguayan wine page, fetched 2026-10-31, with its 2013 vineyard area. Uruguay has no appellation list on that page, so departments stand in.","area under vine",[(n,"Vineyard department; %s ha under vine in 2013."%format(h,','),"Uruguay","2013") for n,h in uru],URU)
bra=[("Serra Gaúcha","Rio Grande do Sul; the oldest and most important wine region, known for sparkling wine.","Rio Grande do Sul"),("Campanha","Rio Grande do Sul pampas region bordering Uruguay and Argentina.","Rio Grande do Sul"),("Serra do Sudeste","Rio Grande do Sul wine region.","Rio Grande do Sul"),("Campos de Cima da Serra","Rio Grande do Sul wine region.","Rio Grande do Sul"),("São Francisco Valley","Pernambuco semi-arid region with two grape crops a year.","Pernambuco"),("Santa Catarina","State with smaller-scale viticulture.","Santa Catarina")]
braK=kind("Brazil wine regions","The wine regions of Brazil, with Serra Gaúcha first.","a Brazilian wine region","Every wine region named on Wikipedia's Brazilian wine page, fetched 2026-10-31. The page names no Indicação de Procedência or Denominação de Origem, so regions stand in.","state",bra,BRA)
DEPT_SA=D("Wine of South America","Wine from Chile, Argentina, Uruguay and Brazil by region; a wine from Mexico → Wine of Canada & Mexico.","Which country, and which valley, province or region inside it?",SA_CHI+SA_ARG+[S("Uruguay & Brazil","Uruguayan departments and Brazilian regions.",[uruK,braK])])

# ---------- South Africa
WRSA=W+'Wine_regions_of_South_Africa'
SELSA="Every district and ward on Wikipedia's Wine regions of South Africa page, fetched 2026-10-31, sectioned by district. Boberg, a repealed fortified-wine designation, is left out; districts the page lists without wards are entries."
sa_data={
"Breede River Valley":[("Breedekloof",None,"district"),("Goudini","Breedekloof","ward"),("Slanghoek","Breedekloof","ward"),("Robertson",None,"district"),("Agterkliphoogte","Robertson","ward"),("Bonnievale","Robertson","ward"),("Boesmansrivier","Robertson","ward"),("Eilandia","Robertson","ward"),("Hoopsrivier","Robertson","ward"),("Klaasvoogds","Robertson","ward"),("Le Chasseur","Robertson","ward"),("McGregor","Robertson","ward"),("Vinkrivier","Robertson","ward"),("Worcester",None,"district"),("Aan-de-Doorns","Worcester","ward"),("Hex River Valley","Worcester","ward"),("Nuy","Worcester","ward"),("Scherpenheuvel","Worcester","ward")],
"Cape South Coast":[("Cape Agulhas",None,"district"),("Elim","Cape Agulhas","ward"),("Overberg",None,"district"),("Elgin","Overberg","ward"),("Greyton","Overberg","ward"),("Klein River","Overberg","ward"),("Theewater","Overberg","ward"),("Swellendam",None,"district"),("Buffeljags","Swellendam","ward"),("Malgas","Swellendam","ward"),("Stormsvlei","Swellendam","ward"),("Walker Bay",None,"district"),("Bot River","Walker Bay","ward"),("Hemel-en-Aarde Ridge","Walker Bay","ward"),("Hemel-en-Aarde Valley","Walker Bay","ward"),("Sunday's Glen","Walker Bay","ward"),("Upper Hemel-en-Aarde Valley","Walker Bay","ward"),("Plettenberg Bay",None,"district"),("Herbertsdale",None,"ward"),("Stilbaai East",None,"ward")],
"Coastal Region":[("Darling",None,"district"),("Groenekloof","Darling","ward"),("Paarl",None,"district"),("Simonsberg-Paarl","Paarl","ward"),("Voor Paardeberg","Paarl","ward"),("Wellington","Paarl","ward"),("Stellenbosch",None,"district"),("Banghoek","Stellenbosch","ward"),("Bottelary","Stellenbosch","ward"),("Devon Valley","Stellenbosch","ward"),("Jonkershoek Valley","Stellenbosch","ward"),("Papegaaiberg","Stellenbosch","ward"),("Polkadraai Hills","Stellenbosch","ward"),("Simonsberg-Stellenbosch","Stellenbosch","ward"),("Swartland",None,"district"),("Malmesbury","Swartland","ward"),("Riebeekberg","Swartland","ward"),("Tygerberg",None,"district"),("Durbanville","Tygerberg","ward"),("Philadelphia","Tygerberg","ward"),("Constantia",None,"ward"),("Hout Bay",None,"ward"),("Cape Peninsula",None,"district"),("Franschhoek Valley",None,"ward"),("Tulbagh",None,"district")],
"Klein Karoo":[("Calitzdorp",None,"district"),("Langeberg-Garcia",None,"district"),("Montagu",None,"ward"),("Tradouw",None,"ward"),("Tradouw Highlands",None,"ward"),("Outeniqua",None,"ward"),("Upper Langkloof",None,"ward")],
"Olifants River":[("Citrusdal Mountain",None,"district"),("Piekenierskloof","Citrusdal Mountain","ward"),("Citrusdal Valley",None,"district"),("Lutzville Valley",None,"district"),("Koekenaap","Lutzville Valley","ward"),("Bamboes Bay",None,"ward"),("Spruitdrift",None,"ward"),("Vredendal",None,"ward"),("Cederberg",None,"ward"),("Ceres",None,"ward"),("Lamberts Bay",None,"ward"),("Prince Albert Valley",None,"ward"),("Swartberg",None,"ward")],
"Northern Cape & Eastern Cape":[("Douglas",None,"district"),("Sutherland-Karoo",None,"district"),("Hartswater",None,"ward"),("Central Orange River",None,"ward"),("Rietrivier FS",None,"ward"),("St Francis Bay",None,"ward")],
}
def sak(region,d):
    rows=[]
    for n,par,lvl in sa_data[region]:
        g=par or ("Region level" if False else region)
        rows.append((n,"Wine of Origin %s%s."%(lvl," in "+par if par else " in the "+region+" area"),g))
    return kind("%s districts and wards"%region,d,"a Wine of Origin district or ward",SELSA,"district",rows,WRSA)
SA_S=[S("Coastal Region & Cape South Coast","The Western Cape's two coastal regions, from Stellenbosch to Walker Bay.",[sak("Coastal Region","Paarl, Stellenbosch, Swartland, Tygerberg, Darling and the Cape Peninsula wards."),sak("Cape South Coast","Walker Bay, Overberg, Cape Agulhas, Swellendam and Plettenberg Bay.")]),
 S("Inland & northern regions","Breede River Valley, Klein Karoo, Olifants River and the northern and eastern Cape.",[sak("Breede River Valley","Breedekloof, Robertson and Worcester."),sak("Klein Karoo","Calitzdorp, Langeberg-Garcia and the Little Karoo wards."),sak("Olifants River","Citrusdal, Lutzville and the west-coast wards."),sak("Northern Cape & Eastern Cape","The wards and districts of the Northern and Eastern Cape.")],"kinds by region, coast to interior")]
DEPT_ZA=D("Wine of South Africa","South African wine by Wine of Origin district and ward; Boberg fortified wine is not covered.","Which region, then which district or ward?",SA_S)

# ---------- Australia & NZ
AUR='https://wineaustralia.com/labelling/register-of-protected-gis-and-other-terms/geographical-indications'
SELAU="Every Geographical Indication on Wine Australia's register page, fetched 2026-10-31, as zones and super zones in one kind and regions and subregions in the kinds of their state. The page gives no registration dates."
au={
"South Australia":[("Mount Lofty Ranges","Adelaide",["Adelaide Hills","Lenswood","Piccadilly Valley"]),("Barossa","Adelaide",["Barossa Valley","Eden Valley","High Eden"]),("Fleurieu","Adelaide",["Currency Creek","Kangaroo Island","Langhorne Creek","McLaren Vale","Southern Fleurieu"]),("Limestone Coast","South Australia",["Coonawarra","Mount Benson","Mount Gambier","Padthaway","Robe","Wrattonbully"]),("Lower Murray","South Australia",["Riverland"]),("Far North","South Australia",[]),("Southern Flinders Ranges","South Australia",[]),("The Peninsulas","South Australia",[]),("Adelaide Plains","South Australia",[]),("Clare Valley","South Australia",[])],
"New South Wales":[("Big Rivers","New South Wales",["Murray Darling","Perricoota","Riverina","Swan Hill"]),("Central Ranges","New South Wales",["Cowra","Mudgee","Orange"]),("Hunter Valley","New South Wales",["Hunter","Broke Fordwich","Pokolbin","Upper Hunter Valley"]),("Northern Rivers","New South Wales",["Hastings River"]),("Northern Slopes","New South Wales",["New England Australia"]),("South Coast","New South Wales",["Shoalhaven Coast","Southern Highlands"]),("Southern New South Wales","New South Wales",["Canberra District","Gundagai","Hilltops","Tumbarumba"]),("Western Plains","New South Wales",[])],
"Victoria":[("Central Victoria","Victoria",["Bendigo","Goulburn Valley","Nagambie Lakes","Heathcote","Strathbogie Ranges","Upper Goulburn"]),("Gippsland","Victoria",[]),("North East Victoria","Victoria",["Alpine Valleys","Beechworth","Glenrowan","King Valley","Rutherglen"]),("North West Victoria","Victoria",["Murray Darling","Swan Hill"]),("Port Phillip","Victoria",["Geelong","Macedon Ranges","Mornington Peninsula","Sunbury","Yarra Valley"]),("Western Victoria","Victoria",["Grampians","Great Western","Henty","Pyrenees"])],
"Western Australia":[("Central Western Australia","Western Australia",[]),("Eastern Plains, Inland and North of Western Australia","Western Australia",[]),("Greater Perth","Western Australia",["Peel","Perth Hills","Swan District","Swan Valley"]),("South West Australia","Western Australia",["Blackwood Valley","Geographe","Great Southern","Manjimup","Margaret River","Pemberton"]),("West Australian South East Coastal","Western Australia",[])],
"Tasmania, Queensland & territories":[("Tasmania","Tasmania",[]),("Queensland regions","Queensland",["Granite Belt","South Burnett"]),("Northern Territory","Northern Territory",[]),("Australian Capital Territory","Australian Capital Territory",[]),("Australia","Australia",[]),("South Eastern Australia","Multi-state",[])]}
gs=["Albany","Denmark","Frankland River","Mount Barker","Porongurup"]
zones=[];regions={}
for st,zl in au.items():
    for z,par,rs in zl:
        if z=="Queensland regions":
            for r in rs: regions.setdefault(st,[]).append((r,"Queensland","Queensland region"))
            continue
        zones.append((z,par,st))
        for r in rs: regions.setdefault(st,[]).append((r,z,"region or subregion"))
for st in regions:
    pass
regions["Western Australia"]+= [(r,"Great Southern","subregion") for r in gs]
zone_rows=[(z,"Zone, super zone or state-level Geographical Indication in %s."%par if par!="Multi-state" else "Multi-state Geographical Indication covering New South Wales, Victoria, Tasmania and parts of Queensland and South Australia.",par) for z,par,st in zones if not (z=="Queensland regions")]
def aus_regions(st,d,name):
    rows=[(r,"%s of %s, in the %s zone."%("Subregion" if t=="subregion" else "Region or subregion",st if st in ("South Australia","New South Wales","Victoria","Western Australia") else "Queensland",par),par) for r,par,t in regions[st]]
    if st=="Western Australia": rows=[(r,("Subregion of Great Southern." if p=="Great Southern" and r in gs else "Region in the %s zone."%p),p) for r,p,t in regions[st]]
    return kind(name,d,"an Australian Geographical Indication at region or subregion level",SELAU,"zone",rows,AUR)
au_zonekind=kind("Australian zones & super zones","Zone, super-zone and state-level Geographical Indications that contain the regions, plus the multi-state South Eastern Australia GI.","an Australian zone or super zone Geographical Indication",SELAU,"state or zone",zone_rows,AUR)
au_q=[(r,"Region of Queensland.", "Queensland") for r in ["Granite Belt","South Burnett"]]
AUS=[S("Zones","Zones and super zones above the regions.",[au_zonekind]),
 S("South Australia","South Australian regions and subregions.",[aus_regions("South Australia","Regions of the Adelaide, Limestone Coast and Lower Murray zones, with Clare Valley.","South Australian regions")]),
 S("New South Wales & Southern States","Regions of New South Wales, Victoria and Queensland.",[aus_regions("New South Wales","Regions of the Hunter, Central Ranges, Big Rivers and Southern New South Wales zones.","New South Wales regions"),aus_regions("Victoria","Regions of Central, North East, Port Phillip and Western Victoria.","Victorian regions"),kind("Queensland regions","The two Queensland regions.","a Queensland Geographical Indication region",SELAU,"state",au_q,AUR)]),
 S("Western Australia","Western Australian regions and subregions.",[aus_regions("Western Australia","Regions of Greater Perth and South West Australia, with the Great Southern subregions.","Western Australian regions")])]
NZW=W+'New_Zealand_wine'
SELNZ="Every region and named sub-region on Wikipedia's New Zealand wine page, fetched 2026-10-31 (first part of the page only), with GI years where the page gives them."
nzN=[("Northland","Geographical indication since 2017; Chardonnay, Syrah and Pinot Gris.","Northland","2017"),("Auckland","Region; Chardonnay, Bordeaux-style reds and Syrah.","Auckland"),("Waiheke Island","Auckland sub-region.","Auckland"),("Kumeu","Auckland sub-region.","Auckland"),("Matakana","Auckland sub-region.","Auckland"),("Gisborne","Geographical indication since 2017; Chardonnay, Gewürztraminer and Viognier.","Gisborne","2017"),
("Hawke's Bay","Region; Merlot and Syrah, with Chardonnay, Sauvignon Blanc and Viognier.","Hawke's Bay"),("Gimblett Gravels","Hawke's Bay sub-region.","Hawke's Bay"),("Bridge Pa Triangle","Hawke's Bay sub-region.","Hawke's Bay"),("Te Mata Special Character Zone","Hawke's Bay sub-region.","Hawke's Bay"),
("Wairarapa","Geographical indication since 2017; Pinot Noir, Sauvignon Blanc and Pinot Gris.","Wairarapa","2017"),("Gladstone","Wairarapa sub-region.","Wairarapa"),("Martinborough","Wairarapa sub-region.","Wairarapa"),("Masterton","Wairarapa sub-region.","Wairarapa"),("Opaki","Wairarapa sub-region.","Wairarapa")]
nzS=[("Marlborough","Region; Sauvignon Blanc and Pinot Noir; the Wairau and Awatere valleys are named areas.","Marlborough"),("Nelson","Region.","Nelson"),("Waimea","Nelson sub-region.","Nelson"),("Moutere Valley","Nelson sub-region.","Nelson"),
("Canterbury","Region whose geographical indication covers the whole region; Pinot Noir.","Canterbury"),("North Canterbury","Geographical indication since 2020.","Canterbury","2020"),("Waipara","Canterbury sub-region.","Canterbury"),("Waitaki Valley","North Otago geographical indication since 2018; Pinot Noir, Pinot Gris, Chardonnay and Riesling.","Waitaki Valley","2018"),
("Central Otago","Geographical indication; Pinot Noir, with Riesling and Pinot Gris.","Central Otago"),("Bannockburn","Central Otago sub-region with its own geographical indication.","Central Otago"),("Bendigo","Central Otago sub-region.","Central Otago"),("Gibbston","Central Otago sub-region.","Central Otago"),("Queenstown","Central Otago sub-region.","Central Otago"),("Wānaka","Central Otago sub-region.","Central Otago"),("Kawarau Gorge","Central Otago sub-region.","Central Otago"),("Alexandra Basin","Central Otago sub-region.","Central Otago"),("Cromwell Basin","Central Otago sub-region.","Central Otago")]
NZ=[S("New Zealand","New Zealand wine regions by island.",[kind("North Island wine regions","Northland, Auckland, Gisborne, Hawke's Bay and Wairarapa, with their sub-regions.","a New Zealand wine region or sub-region",SELNZ,"region",nzN,NZW),kind("South Island wine regions","Marlborough, Nelson, Canterbury, Waitaki Valley and Central Otago, with their sub-regions.","a New Zealand wine region or sub-region",SELNZ,"region",nzS,NZW)])]
DEPT_AN=D("Wine of Australia & New Zealand","Wine from Australian Geographical Indications and New Zealand regions; wine from elsewhere in the Pacific is not covered.","Which country, then which zone, state or island, then which region?",AUS+NZ)

# ---------- England & Wales, China, Japan, India
EW=W+'English_wine'
ew=[("English wine","Protected designation of origin for England only, with vines up to 220 m; sparkling styles from Chardonnay, Pinot Noir, Pinot Noir Précoce, Pinot Meunier, Pinot Blanc, Pinot Gris, Seyval Blanc and Reichensteiner.","England"),("English regional wine","Protected geographical indication for England with no defined area.","England"),("Sussex wine","Protected designation of origin for Sussex only; mainly Chardonnay, Pinot Noir and Pinot Meunier, still and sparkling.","England")]
wl=[("Welsh wine","Protected designation of origin for Wales, with vines under 220 m.","Wales"),("Welsh regional wine","Protected geographical indication for Wales or a bordering derogated area; at least 85 % Welsh-harvested grapes.","Wales")]
SELEW="Every protected designation of origin and geographical indication for wine named on Wikipedia's English wine page, fetched 2026-10-31. Darnibole, Westerhill and English Quality Sparkling Wine are not on that page and are left out."
DEPT_EW=D("Wine of England & Wales","Wine from the protected designations of England and Wales; wine from Scotland or Ireland is not covered.","Which country, then which designation?",[S("England & Wales","Protected names for English and Welsh wine.",[kind("English protected wine names","The PDO and PGI names for English wine.","an English protected wine name",SELEW,"country",ew,EW),kind("Welsh protected wine names","The PDO and PGI names for Welsh wine.","a Welsh protected wine name",SELEW,"country",wl,EW)])])
CH=W+'Chinese_wine'
SELCH="Every wine region named on Wikipedia's Chinese wine page, fetched 2026-10-31. The page names no appellation system, so provinces and areas stand in."
ch=[("Ningxia","Autonomous region with almost 40,000 hectares of vines and about a quarter of national output in 2017; Cabernet Sauvignon blends.","North",""),("Xinjiang","Autonomous region; Cabernet varieties; Turfan is a historic grape area.","North"),("Shanxi","Province; Cabernet Sauvignon; historically Taiyuan wine from the mare-teat grape.","North"),("Shandong","Province whose Yantai-Penglai area has over 140 wineries and about 40 % of China's wine.","East"),("Beijing","Municipality with wine named on the page.","North"),("Hebei","Province; Zhangjiakou.","North"),("Sichuan","Province; Yibin.","South-west"),("Jilin","Province; Tonghua.","North-east"),("Inner Mongolia","Autonomous region with organic wine production.","North"),("Gansu","Province with historic vines at Dunhuang and Liangzhou.","North-west")]
ch=[(r[0],r[1],r[2]) for r in ch]
JP=W+'Japanese_wine'; NTA='https://www.nta.go.jp/english/taxes/liquor_administration/geographical/02.htm'
jp=[("Yamanashi","Wine geographical indication designated 16 July 2013 by the National Tax Agency; home of the Koshu grape.","Prefectures with a wine GI","2013",NTA),("Hokkaido","Wine geographical indication designated 28 June 2018.","Prefectures with a wine GI","2018",NTA),("Yamagata","Wine geographical indication designated 30 June 2021.","Prefectures with a wine GI","2021",NTA),("Osaka","Wine geographical indication designated 30 June 2021.","Prefectures with a wine GI","2021",NTA),("Nagano","Wine geographical indication designated 30 June 2021.","Prefectures with a wine GI","2021",NTA)]
IN=W+'Indian_wine'; NV=W+'Nashik_valley_wine'
ind=[("Nashik Valley","Geographical indication for red and white wine from Nashik district, Maharashtra, application no. 123; about 8,000 acres of wine grapes.","Maharashtra","",NV),("Pune, Baramati, Sangli and Solapur","Other Maharashtra vineyard areas on the Deccan Plateau.","Maharashtra"),("Karnataka","Vineyards near Bangalore at about 200 m.","South"),("Telangana","Vineyards near Hyderabad.","South"),("Andhra Pradesh","Warm wine region.","South"),("Tamil Nadu","Southern warm wine region.","South"),("Goa","Site of early imported-variety winemaking.","West"),("Punjab","Cooler north-western wine area.","North"),("Kashmir","Northern vineyards at about 1,000 m.","North")]
ind=[tuple(r) for r in ind]
SELJ="The five wine geographical indications on the National Tax Agency page, fetched 2026-10-31, with designation dates."
SELI="Nashik Valley, India's one wine GI found, from Wikipedia's Nashik valley wine page, and the other wine areas on Wikipedia's Indian wine page, fetched 2026-10-31. The page names no other GI."
DEPT_ASIA=D("Wine of China, Japan & India","Wine from China by province, Japan by geographical indication and India by wine area; wine from Korea or Southeast Asia is not covered.","Which country, then which province, prefecture or state?",[S("China","Chinese wine provinces and areas.",[kind("China wine regions","Provinces and areas where the page places Chinese wine.","a Chinese wine province or area",SELCH,"part of China",ch,CH)]),S("Japan","Japanese wine geographical indications.",[kind("Japan wine geographical indications","The wine GIs designated by Japan's National Tax Agency, oldest first.","a Japanese wine geographical indication",SELJ,"designation group",jp,NTA)]),S("India","Indian wine areas.",[kind("India wine areas","Nashik Valley and the other Indian wine areas, by state or part of India.","an Indian wine area",SELI,"state",ind,IN)])])

DEPTS=[DEPT_US:=D("Wine of the United States","American wine by American Viticultural Area, grouped by state and region; wine from Canada or Mexico → Wine of Canada & Mexico.","Which state or region, then which AVA?",US_SHELVES),DEPT_CM,DEPT_SA,DEPT_ZA,DEPT_AN,DEPT_EW,DEPT_ASIA]
renames={"Zinfandel":"California: Central Valley AVAs","Malbec":"Argentina: Cuyo","Carmenère":"Chile: Central Valley","Tannat":"Uruguay wine departments","Pinotage":"Coastal Region districts and wards","País":"Chile: Central Valley"}
out={"depts":DEPTS,"brands":[],"renames":renames,"moves":[]}
tmp='/home/user/Possession-Taxonomy/rebuild/out/J7_parts/WNW.json.tmp'
json.dump(out,open(tmp,'w'),ensure_ascii=False,indent=1)
os.replace(tmp,'/home/user/Possession-Taxonomy/rebuild/out/J7_parts/WNW.json')
print({d['n']:sum(len(k['x']) for s in d['s'] for k in s['k']) for d in DEPTS})
