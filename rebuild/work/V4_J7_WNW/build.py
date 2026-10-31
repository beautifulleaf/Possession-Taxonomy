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
# multi-state AVAs and their states as listed on the page
multi={"Ozark Mountain":"Arkansas, Missouri and Oklahoma","Upper Mississippi River Valley":"Illinois, Iowa, Minnesota and Wisconsin","Ohio River Valley":"Indiana, Kentucky, Ohio and West Virginia","Southeastern New England":"Connecticut, Massachusetts and Rhode Island","Loess Hills District":"Iowa and Missouri","Mississippi Delta":"Louisiana, Mississippi and Tennessee","Cumberland Valley":"Maryland and Pennsylvania","Central Delaware Valley":"New Jersey and Pennsylvania","Mesilla Valley":"New Mexico and Texas","Lake Erie":"New York, Ohio and Pennsylvania","Appalachian High Country":"North Carolina, Tennessee and Virginia","Upper Hiwassee Highlands":"Georgia and North Carolina","Snake River Valley":"Idaho and Oregon","Lewis-Clark Valley":"Idaho and Washington","Columbia Gorge":"Oregon and Washington","Columbia Valley":"Oregon and Washington","Walla Walla Valley":"Oregon and Washington","Shenandoah Valley":"Virginia and West Virginia","Augusta":"Missouri"}
# place each multi-state AVA once, in the first kind that lists its state
extra={"Arkansas":["Ozark Mountain"],"Illinois":[],"Indiana":["Ohio River Valley"],"Iowa":["Upper Mississippi River Valley"] ,"Louisiana":[],"Maryland":[],"Massachusetts":[],"Missouri":["Loess Hills District","Ozark Mountain"],"Connecticut":[],"Oklahoma":[]}
# simpler: explicit placement of AVAs that appear in more than one state on the page
extra={"Arkansas":["Ozark Mountain"],"Illinois":["Upper Mississippi River Valley"],"Indiana":["Ohio River Valley"],"Iowa":["Loess Hills District"],"Louisiana":["Mississippi Delta"],"Maryland":["Cumberland Valley"],"Connecticut":["Southeastern New England"],"New Jersey":[],"New Mexico":[],"New York":[],"North Carolina":[],"Idaho":["Snake River Valley","Lewis-Clark Valley"] ,"Washington":["Columbia Gorge","Columbia Valley","Walla Walla Valley"],"Virginia":[],"Pennsylvania":["Lake Erie"]}
def usents(names,g,state):
    out=[]
    for n in names:
        sp=multi.get(n)
        d="Viticultural area in "+(sp if sp else state)+"."
        out.append(E(n,d,US,g))
    return out
def with_extra(key,state,gl=None):
    names=[x for x in raw[key].split(';')]
    for e in extra.get(key,[]):
        if e not in names: names.append(e)
    return names
# remove from raw the names that are placed through 'extra' in a different kind
placed={}
def add(key,state):
    names=raw.get(key,"").split(';') if key in raw else []
    for e in extra.get(key,[]):
        if e not in names: names.append(e)
    names=[n for n in names if n]
    return names
# explicit multi-state placement: the AVA sits in the kind of the state that comes first on the page
extra={"Arkansas":["Ozark Mountain"],"Illinois":["Upper Mississippi River Valley"],"Indiana":["Ohio River Valley"],"Iowa":["Loess Hills District"],"Louisiana":["Mississippi Delta"],"Maryland":["Cumberland Valley"],"Connecticut":["Southeastern New England"],"New Jersey":["Central Delaware Valley"],"New Mexico":["Mesilla Valley"],"New York":["Lake Erie"],"North Carolina":["Appalachian High Country","Upper Hiwassee Highlands"] if False else ["Appalachian High Country"],"Idaho":["Snake River Valley","Lewis-Clark Valley"],"Oregon":["Columbia Gorge","Columbia Valley","Walla Walla Valley"],"Georgia":["Upper Hiwassee Highlands"],"Virginia":["Shenandoah Valley"]}
# Idaho/Oregon: Snake River Valley and the Columbia names are filed once; drop duplicates from the later state
for k in ("Oregon",):
    raw[k]=";".join(n for n in raw[k].split(';') if n not in ("Columbia Gorge","Columbia Valley","Walla Walla Valley","Snake River Valley"))
raw["Washington"]=raw["Washington"]
for n in ("Columbia Gorge","Columbia Valley","Walla Walla Valley"):
    extra.setdefault("Washington",[])
extra["Oregon"]=["Columbia Gorge","Columbia Valley","Walla Walla Valley"]
extra["Washington"]=[]
raw["Oregon"]+=";Snake River Valley" if False else ""
extra["Idaho"]=["Snake River Valley","Lewis-Clark Valley"]
def usk(name,key,state,g,d,note=""):
    names=add(key,state)
    return K(name,d,"One entry is an American Viticultural Area, a delimited grape-growing area approved by the Alcohol and Tobacco Tax and Trade Bureau (TTB).","Every AVA listed on Wikipedia's List of American Viticultural Areas for this state or region, fetched 2026-10-31; an AVA that spans several states is filed once, under the first state that lists it. The page gives no approval years.","state",usents(names,g,state))
def uskinds(keys):
    return keys
US_SHELVES=[
 S("California","California AVAs grouped by the region the Wikipedia list gives.",[
  usk("California: North Coast AVAs","CA-north-coast","California","North Coast","Napa, Sonoma, Mendocino and Lake County AVAs, including Napa Valley, Russian River Valley and Alexander Valley."),
  usk("California: Central Coast AVAs","CA-central","California","Central Coast","AVAs from Santa Cruz south to Santa Barbara and Paso Robles."),
  usk("California: Central Valley AVAs","CA-valley","California","Central Valley","AVAs of the Sacramento and San Joaquin valleys, including Lodi and Clarksburg."),
  usk("California: Sierra Foothills AVAs","CA-sierra","California","Sierra Foothills","AVAs in the Sierra Nevada foothills such as El Dorado and Fiddletown."),
  usk("California: South Coast AVAs","CA-south","California","South Coast","AVAs from Malibu to Temecula and the high desert."),
  usk("California: northern interior AVAs","CA-north","California","Northern interior","Small AVAs in the far north of California (Inwood Valley, Manton Valley, Seiad Valley, Trinity Lakes, Willow Creek)."),
 ],"California regions as the Wikipedia list groups them"),
 S("Pacific Northwest","Oregon, Washington and Idaho AVAs.",[
  usk("Oregon AVAs","Oregon","Oregon","Oregon","AVAs of Oregon, led by the Willamette Valley and its nested AVAs; the Columbia names are filed here."),
  usk("Washington AVAs","Washington","Washington","Washington","AVAs of Washington State inside and beside the Columbia Valley."),
  usk("Idaho AVAs","Idaho","Idaho","Idaho","AVAs of Idaho, including the Snake River Valley."),
 ]),
 S("Southwest, Mountain West & Hawaii","AVAs of the dry interior and the islands.",[
  usk("Texas AVAs","Texas","Texas","Texas","AVAs of Texas, from the Hill Country to the High Plains."),
  usk("Arizona, New Mexico and Colorado AVAs","Arizona","Arizona","Arizona","AVAs of the Southwest and Rockies."),
  usk("Hawaii AVAs","Hawaii","Hawaii","Hawaii","The single AVA in Hawaii."),
 ]),
 S("Midwest & South","AVAs of the central states, the Ozarks and the South.",[
  usk("Great Lakes and Midwest AVAs","Michigan","Michigan","Michigan","AVAs around the Great Lakes and the upper Mississippi."),
  usk("Missouri, Arkansas and Ozark AVAs","Missouri","Missouri","Missouri","AVAs of Missouri, Arkansas and the Ozarks."),
  usk("Southern AVAs","Georgia","Georgia","Georgia","AVAs of Georgia, Tennessee, Louisiana and the Carolinas."),
 ]),
 S("Northeast & Mid-Atlantic","AVAs from New England to Virginia.",[
  usk("New York AVAs","New York","New York","New York","AVAs of New York including the Finger Lakes and Long Island."),
  usk("New England AVAs","Connecticut","Connecticut","Connecticut","AVAs of Connecticut and Massachusetts."),
  usk("Mid-Atlantic AVAs","Virginia","Virginia","Virginia","AVAs from New Jersey and Pennsylvania to Virginia and West Virginia."),
 ]),
]
