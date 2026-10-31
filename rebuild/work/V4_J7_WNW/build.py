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
