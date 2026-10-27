import sys
sys.path.insert(0,'/home/user/Possession-Taxonomy/rebuild/work/E4/agent')
from w0100 import w, X, WP
SP="https://www.sportsmans.com/shooting-gear-gun-supplies/c/cat139644"
WI="Winchester"; RE="Remington"; BR="Browning"; BE="Beretta"; PU="James Purdey & Sons"; HH="Holland & Holland"; MO="Mossberg"
kinds=[
{"n":"Over-under shotgun","a":"Bockdoppelflinte · O/U","d":"Smoothbore long gun with two barrels stacked one above the other.","t":["field","sporting","trap","skeet"],"s":SP,
 "x":[X("Browning Superposed","John Browning's last design, an over-under with a single selective trigger, finished by Val Browning.",WP+'Browning_Superposed',BR,"1931",
        v=[("Superposed (pre-war)",BR,"1931–1940","made by FN"),("Superposed (post-war)",BR,"1948–1960","")]),
      X("Beretta Silver Pigeon","Beretta's boxlock over-under field and sporting family.",WP+'Beretta_Silver_Pigeon',BE,"1950s",
        v=[("683",BE,"",""),("686",BE,"",""),("687",BE,"","higher grade")],dt="12, 20, 28 gauge or .410 · engraving grade · stock"),
      X("Perazzi MX8","Competition over-under with a raised rib, built for Ennio Mattarelli for the 1968 Olympics.",WP+'Perazzi',"Perazzi","1968",
        v=[("MX2000",  "Perazzi","",""),("MX10","Perazzi","",""),("High Tech","Perazzi","","")])]},
{"n":"Side-by-side shotgun","a":"double gun · SxS","d":"Smoothbore long gun with two barrels placed beside each other.","t":["sidelock","boxlock","hammer gun","self-opening"],"s":SP,
 "x":[X("Purdey self-opening sidelock","Hammerless self-opening sidelock designed by Frederick Beesley.",WP+'James_Purdey_%26_Sons',PU,"1880",
        v=[("Wem ejector",PU,"1888","ejector added"),("Hammer Ejector",PU,"2004","reintroduced hammer gun")],dt="12, 16, 20 gauge · engraving · bespoke stock"),
      X("Holland & Holland Royal","Self-opening sidelock side-by-side using the H&H assisted-opening mechanism.",WP+'Holland_%26_Holland',HH,"1922"),
      X("Anson & Deeley boxlock","Compact hammerless boxlock action designed by Anson and Deeley at Westley Richards.",WP+'Boxlock_action',"Westley Richards","1875")]},
{"n":"Pump-action shotgun","a":"slide-action shotgun","d":"Smoothbore long gun cycled by sliding the fore-end back and forth.","s":SP,
 "x":[X("Winchester Model 12","Hammerless pump shotgun by T.C. Johnson, the 'Perfect Repeater'.",WP+'Winchester_Model_1912',WI,"1912",
        v=[("Model 1897",WI,"1897","exposed-hammer predecessor"),("Model 42",WI,"",".410 scaled-down version"),("Special runs","Miroku","to 2006","")]),
      X("Remington 870","American pump shotgun in 12, 16, 20, 28 gauge and .410 bore.",WP+'Remington_Model_870',RE,"1951",
        v=[("Wingmaster",RE,"",""),("Express",RE,"","lower-cost"),("Police Magnum",RE,"",""),("Special Purpose Marine Magnum",RE,"","")]),
      X("Mossberg 500","Pump shotgun designed by Carl Benson for O.F. Mossberg & Sons.",WP+'Mossberg_500',MO,"1961",
        v=[("590",MO,"1987","military"),("590A1",MO,"","heavy barrel, bayonet lug"),("835 Ulti-Mag",MO,"",""),("Maverick 88","Maverick Arms","","budget line"),("Shockwave",MO,"2017","")])]},
{"n":"Semi-automatic shotgun","a":"Selbstladeflinte · autoloader","d":"Smoothbore long gun that reloads itself after each shot.","t":["gas-operated","inertia-operated","recoil-operated"],"s":SP,
 "x":[X("Browning Auto-5","John Browning's long-recoil semi-automatic shotgun, made by FN and under licence.",WP+'Browning_Auto-5',BR,"1902",a="A-5",
        v=[("Auto-5","FN Herstal","1902",""),("Model 11",RE,"1905–1947","licensed"),("Model 720","Savage Arms","1930–1949","licensed"),("Auto-5","Miroku","1975–1998","")]),
      X("Benelli M2","Inertia-operated semi-automatic shotgun.",WP+'Benelli_M2',"Benelli","2004",v=[("M1","Benelli","","predecessor")])]},
{"n":"Single-shot shotgun","a":"","d":"Smoothbore long gun with one barrel loaded by hand with one shell for each shot, usually break-open.","t":["break-open","bolt-action"],"s":SP},
{"n":"Muzzle-loading shotgun","a":"musket · fowler","d":"Smoothbore long gun loaded with powder and shot from the muzzle.","t":["flintlock","percussion"],
 "s":"https://www.muzzle-loaders.com/pedersoli-classic-side-by-side-shotgun-12-ga-percussion-l-241-012.html",
 "x":[X("Brown Bess","British Land Pattern smoothbore flintlock musket, .75 calibre.",WP+'Brown_Bess',"","1722",a="Land Pattern Musket",
        v=[("Long Land Pattern","","1722",""),("Short Land Pattern","","","42-inch barrel"),("India Pattern","","c. 1794","39-inch barrel")])],
 "m":[["Pedersoli Classic Side-by-Side Shotgun","Davide Pedersoli"]]},
{"n":"Combination gun","a":"drilling · rifle-shotgun combination gun · Kombinierte Waffen","d":"Long gun with at least one rifled and one smoothbore barrel in one action.",
 "t":["over-under","drilling (three barrels)","vierling (four barrels)","cape gun (side-by-side)"],
 "s":"https://www.merkel-die-jagd.de/wp-content/uploads/datenblaetter/drilling-96k-en.pdf",
 "x":[X("Drilling","Three-barrelled break-action gun, usually two shot barrels and one rifle barrel.",WP+'Drilling_(firearm)',"","",
        v=[("Merkel Drilling 96K","Merkel Jagd- und Sportwaffen","",""),("M30 Luftwaffe Drilling","","","aircrew survival gun")]),
      X("Savage Model 24","Over-under .22 LR rifle over .410 shotgun, first sold as the Stevens 22-410.",WP+'Savage_Model_24',"Savage Arms","1938",
        v=[("Stevens Model 22-410","Stevens Arms","1938–1950",""),("Model 24B","Savage Arms","",""),("Model 24V","Savage Arms","",""),("Model 242","Savage Arms","",".410 3-inch")]),
      X("Cape gun","Side-by-side combination of one rifled and one smoothbore barrel.",WP+'Drilling_(firearm)',"","")]}]
K=lambda n,c,seg,kf,d,f="",s="knowledge": dict({"n":n,"c":c,"seg":seg,"kf":kf,"d":d,"s":s},**({"f":f} if f else {}))
brands=[K(BR,"United States","Premium","shotguns and rifles","Browning Arms Co., maker of the Superposed and Auto-5 with FN."),
 K(BE,"Italy","Heritage manufactory","shotguns and pistols","Fabbrica d'Armi Pietro Beretta of Gardone Val Trompia.",s=WP+'Beretta_Silver_Pigeon'),
 K("Perazzi","Italy","Professional & flagship","competition shotguns","Brescia maker of competition over-unders founded by Daniele Perazzi.","1957",WP+'Perazzi'),
 K(PU,"United Kingdom","Heritage manufactory","best London guns","London gunmaker founded by James Purdey, owned by Richemont.","1814",WP+'James_Purdey_%26_Sons'),
 K(HH,"United Kingdom","Heritage manufactory","best London guns and rifles","London gunmaker founded by Harris Holland, owned by Beretta Holding.","1835",WP+'Holland_%26_Holland'),
 K("Westley Richards","United Kingdom","Heritage manufactory","boxlock guns and rifles","Birmingham gunmaker where the Anson & Deeley boxlock was designed."),
 K(WI,"United States","Heritage manufactory","lever-action and bolt rifles","Winchester Repeating Arms, maker of the Model 12."),
 K(RE,"United States","Heritage manufactory","rifles and shotguns","Ilion, New York gunmaker of the 870."),
 K(MO,"United States","Mainstream","pump shotguns","O.F. Mossberg & Sons, maker of the 500 pump shotgun.",s=WP+'Mossberg_500'),
 K("Benelli","Italy","Premium","inertia shotguns","Italian maker of inertia-operated shotguns."),
 K("Savage Arms","United States","Mainstream","rifles and combination guns","American gunmaker of the Model 24.")]
notes=("All 7 old kinds kept with old models. Added archetypes from Wikipedia: Superposed, Silver Pigeon, Perazzi MX8; Purdey sidelock, H&H Royal, Anson & Deeley boxlock; Winchester 12, Remington 870, Mossberg 500; Auto-5, Benelli M2; Brown Bess; Drilling, Savage 24, cape gun. "
 "Single-shot shotgun has types only (no source-backed archetype found). Krieghoff drillings left out (not named on retrieved page); Merkel Drilling 96K kept as a drilling version. Beretta 686 year not found.")
if __name__=='__main__': w('02_02',{"kinds":kinds,"brands":brands,"traditions":[],"notes":notes})
