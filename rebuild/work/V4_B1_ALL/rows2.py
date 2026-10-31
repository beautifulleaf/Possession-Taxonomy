from rows import R,a,LC
W="https://en.wikipedia.org/wiki/"
WDQ="https://query.wikidata.org/sparql?format=json&query=SELECT%20DISTINCT%20%3FiLabel%20%3FcLabel%20%3FdLabel%20%3Fy%20WHERE%20%7BVALUES%20%3Fc%20%7Bwd%3AQ188740%20wd%3AQ213322%20wd%3AQ689651%20wd%3AQ1236619%7D%20%3Fi%20wdt%3AP195%20%3Fc.%20%3Fi%20wdt%3AP31%2Fwdt%3AP279*%20wd%3AQ14745%7D"
J=W+"Finn_Juhl";WG=W+"Hans_Wegner";AJ=W+"Arne_Jacobsen";PK=W+"Poul_Kj%C3%A6rholm";EA=W+"Charles_and_Ray_Eames"
CAS=W+"Achille_Castiglioni";PO=W+"Gio_Ponti";NE=W+"George_Nelson_(designer)"
M="Moulded, shell & bentwood lounge chair";U="Upholstered lounge chair";D="Dining chair";S="Sofa"
# Finn Juhl
for n,al,y,k,d in [("Pelican chair","","1940",U,""),("NV45 chair","","1945",U,""),("Chieftain chair","FJ49A","1949",U,""),("Egyptian chair","","1949",U,""),("Japan chair","FD137","1953",D,""),("Bwana chair","FD152","1962",U,""),("Diplomat chair","209","1965",U,"")]:
    a(k,n,al,"",y,"Designed by Finn Juhl.",J)
a(S,"Poet sofa","FJ41","","1941","Designed by Finn Juhl.",J)
a(S,"Baker sofa","","","1951","Designed by Finn Juhl.",J)
a("Dining table","Judas table","","","1946","Designed by Finn Juhl.",J)
a(U,"Model 48 armchair","Armchair (model 48)","","1946","Finn Juhl armchair held by MoMA.",WDQ)
# Wegner
for k,n,al,y,d in [(U,"Flag Halyard Chair","GE225","1950",""),(U,"Sawhorse Easy Chair","CH28","1952",""),(D,"Chinese Chair","FH4283 · PP66","1944",""),(D,"Peter's Chair","CH410","1944",""),(D,"Valet chair","","1953",""),(D,"Circle Chair","PP130","1985",""),("Office chair","Swivel Chair","JH502 · PP502","1955",""),("Rocking chair","Rocking Chair (J16)","J16","1944",""),("Folding chair","Folding Chair (JH512)","JH512","1949",""),(D,"Ferry Chair","PP52 · PP62","1978",""),(D,"Stangerup Chair","","1938","")]:
    a(k,n,al,"",y,"Designed by Hans Wegner.",WG)
a("Storage cabinet","Fish Cabinet","","","1944","Cabinet designed by Hans Wegner.",WG)
a("Sideboard","CH825","","Carl Hansen & Søn","2014","Credenza by Hans Wegner.",WG)
# Jacobsen
a(U,"Paris Lounge Chair","","","1929","Designed by Arne Jacobsen.",AJ)
a(U,"Charlottenborg Lounge Chair","A.J 237","","1936","Designed by Arne Jacobsen.",AJ)
a(S,"Charlottenborg Sofa","","","1937","Designed by Arne Jacobsen.",AJ)
a("Coffee table","Charlottenborg Coffee Table","","","1937","Designed by Arne Jacobsen.",AJ)
a("Stool","Dot Stool","Model 3170","Fritz Hansen","1954","Designed by Arne Jacobsen.",AJ)
a(U,"Pot chair","","Fritz Hansen","1959","Designed by Arne Jacobsen.",AJ)
a(U,"Giraffe chair","","Fritz Hansen","1959","Designed by Arne Jacobsen.",AJ)
# Panton
a(D,"Cone Chair","","Plus-Linje","1958","Designed by Verner Panton.",W+"Verner_Panton")
a(U,"Tivoli Chair","","Fritz Hansen","1955","Commissioned from Verner Panton.",W+"Verner_Panton")
a(U,"Bachelor Chair","","Fritz Hansen","1955","Commissioned from Verner Panton.",W+"Verner_Panton")
a("Sectional sofa","System 1-2-3","","Fritz Hansen","1977","Designed by Verner Panton.",W+"Verner_Panton")
a(D,"Vilbert Chair","","IKEA","1994","Commissioned from Verner Panton by IKEA.",W+"Verner_Panton")
# Kjaerholm
for k,n,al,y,d in [(U,"PK25","PK25 lounge chair","1951","Lounge chair; production started 1956."),(U,"PK22","PK22 lounge chair","1956","Lounge chair by Poul Kjærholm."),("Coffee table","PK61","PK61 coffee table","1955","Coffee table by Poul Kjærholm."),("Chaise longue","PK24","PK24 hammock chair","1965","Chaise longue by Poul Kjærholm."),("Rocking chair","PK20","PK20 rocking chair","1967","Rocking chair by Poul Kjærholm."),("Stool","PK33","PK33 tripod stool","1959","Stool by Poul Kjærholm."),("Stool","PK91","PK91 X stool","1961","Folding stool by Poul Kjærholm."),(D,"PKO","PKO plywood series","1952","Plywood chair by Poul Kjærholm."),("Daybed","PK80","PK80 day bed","1957","Day bed by Poul Kjærholm.")]:
    a(k,n,al,"",y,d,PK)
# Eames
a(D,"Kleinhans Music Hall Chair","","","1939–1940","Eames and Saarinen design for Kleinhans Music Hall.",EA)
a(U,"Conversation Armchair","","","1940","Eames and Saarinen design.",EA)
a(D,"Dining Chair Wood","DCW","Herman Miller","1945–1946","Moulded plywood dining chair by Charles and Ray Eames.",EA)
a("Coffee table","Molded Plywood Coffee Table","","Herman Miller","1945–1946","Coffee table by Charles and Ray Eames.",EA)
a(D,"Wire Mesh Side Chair","DKR","Herman Miller","1951","Wire chair by Charles and Ray Eames.",EA)
a("Chaise longue","LaChaise","","","1948","Prototype chaise longue held by MoMA.",EA)
a("Chaise longue","Eames Chaise","","Herman Miller","1968","Chaise by Charles and Ray Eames.",EA)
a(S,"Eames Sofa","","Herman Miller","1984","Production began 1984.",EA)
a("Coat rack","Hang-It-All","","Herman Miller","1953","Wall rack by Charles and Ray Eames.",EA)
# Aalto
a(U,"Armchair 404","Zebra Tank Chair","Artek","1935–1936","Armchair by Alvar Aalto.",W+"Alvar_Aalto")
a("Stool","Four-legged Stool E60","","Artek","1933","Four-legged stool by Alvar Aalto.",W+"Alvar_Aalto")
# Prouve, Perriand, Breuer
a(D,"Chaise inclinable","","","1924","Designed by Jean Prouvé.",W+"Jean_Prouv%C3%A9")
a("Bench","Maison de la Tunisie bench-bookshelf","","","1952","Bench with shelf by Jean Prouvé.",W+"Jean_Prouv%C3%A9")
a("Office chair","Siège pivotant","","","1927","Swivel seat by Charlotte Perriand.",W+"Charlotte_Perriand")
a("Recliner","B301 reclining chair","","","1928","Charlotte Perriand with Le Corbusier and Pierre Jeanneret.",W+"Charlotte_Perriand")
a("Chaise longue","Tokyo Chaise longue","","","","Charlotte Perriand chaise longue.",W+"Charlotte_Perriand")
a("Chaise longue","Long Chair","Isokon Long Chair","Isokon","1935–1936","Plywood chaise longue by Marcel Breuer.",W+"Marcel_Breuer")
# Mogensen, Nelson
a(U,"Spanish Chair","","Fredericia","1959","Designed by Børge Mogensen.",W+"B%C3%B8rge_Mogensen")
a("Modular shelving system","Øresund shelving","","","1955–1967","Shelving series by Børge Mogensen.",W+"B%C3%B8rge_Mogensen")
a("Bench","Slat Bench","Platform Bench","Herman Miller","1946","Designed by George Nelson.",NE)
a("Storage cabinet","Basic Cabinet Series","","Herman Miller","1946","Designed by George Nelson.",NE)
a("Side table","Nelson End Table","","Herman Miller","1954","Designed by George Nelson.",NE)
a(D,"Kangaroo Chair","","Herman Miller","1956","Designed by George Nelson.",NE)
a("Modular shelving system","Comprehensive Storage System","CSS","Herman Miller","1959","Designed by George Nelson.",NE)
a("Chest of drawers","Thin Edge Cases","","Herman Miller","1956","Designed by George Nelson.",NE)
a("Desk","Action Office I","","Herman Miller","1964","Principally designed by Robert Propst.",NE)
# Italian
a(D,"Selene Chair","","","1968","Chair by Vico Magistretti held by the V&A.",WDQ)
a(S,"Cubo","Cubo couch and armchair","Arflex","1957","Designed by Achille and Pier Giacomo Castiglioni.",CAS)
a("Stool","Rochetto","","Kartell","1959","Tables and stools by the Castiglioni brothers.",CAS)
a(D,"Lierna chair","","Cassina","1959","Designed by the Castiglioni brothers; Cassina e Gavina.",CAS)
a(U,"Sanluca","Sanluca lounge chair","Gavina","1960","Designed by the Castiglioni brothers.",CAS)
a("Folding chair","Tric","","BBB","1965","Designed by the Castiglioni brothers.",CAS)
a("Folding chair","Ginevra","","BBB","1979","Folding chair by Achille Castiglioni.",CAS)
a("Floor chair","Primate","","Zanotta","1970","Designed by Achille Castiglioni.",CAS)
a("Dining table","Cumano","Cumano tripod table","Zanotta","1977","Folding table by Achille Castiglioni.",CAS)
a("Dining table","Tavolo 95","","De Padova","1995","Table by Achille Castiglioni.",CAS)
a("Desk","Scrittarello","","De Padova","1996","Writing desk by Achille Castiglioni.",CAS)
a(D,"Leggera 646","Leggera chair","Cassina","1951","Chair by Gio Ponti.",PO)
a(U,"Distex","Distex armchair 807","Cassina","1953","Armchair by Gio Ponti.",PO)
a(U,"Dezza armchair","","Poltrona Frau","1966","Armchair by Gio Ponti.",PO)
a(U,"Continuum armchair","","Bonacina","1963","Armchair by Gio Ponti.",PO)
a("Stool","Triposto","","Tecno","1968","Stool by Gio Ponti.",PO)
a(U,"Dragons armchair","","","1917–1919","Designed by Eileen Gray.",W+"Eileen_Gray")
a(D,"S Bend chair","","","1938","Eileen Gray chair held by the V&A.",W+"Eileen_Gray")
a(U,"Grasshopper lounge chair","","Knoll","1946","Designed by Eero Saarinen.",W+"Eero_Saarinen")
a(S,"Womb settee","","Knoll","1950","Designed by Eero Saarinen.",W+"Eero_Saarinen")
a("Storage cabinet","Superbox","","Poltronova","1966","Cabinet by Ettore Sottsass.",W+"Ettore_Sottsass")
a("Bookcase","Carlton bookcase","","Memphis","1981","Designed by Ettore Sottsass.",W+"Ettore_Sottsass")
a("Bookcase","Malabar bookcase","","Memphis","1981","Designed by Ettore Sottsass.",W+"Ettore_Sottsass")
a("Sideboard","Casablanca cabinet","","Memphis","1981","Designed by Ettore Sottsass.",W+"Ettore_Sottsass")
a(D,"Nine-0 chair","","Emeco","2008","Designed by Ettore Sottsass.",W+"Ettore_Sottsass")
# Museum Wikidata
a(D,"Pratt Chair","","","1984","Gaetano Pesce chair held by MoMA and the V&A.",WDQ)
a(U,"Up 1 Chair","","B&B Italia","","Gaetano Pesce chair held by MoMA.",WDQ)
a(U,"Fiocco armchair","","","","Armchair held by MoMA.",WDQ)
a("Side table","Candy Cube","","","2014","Designed by Sabine Marcelis; held by MoMA.",WDQ)
a(M,"Chain armchair","","","1967","Designed by Fabio Lenci; held by MoMA.",WDQ)
a("Chest of drawers","You Can't Lay Down Your Memory","","Droog","1991","Designed by Tejo Remy; held by MoMA.",WDQ)
a("Four-poster bed","Great Bed of Ware","","","1590","Held by the V&A.",WDQ)
a("Four-poster bed","Golden Bed","","","1879","Designed by William Burges; held by the V&A.",WDQ)
a("Storage cabinet","King René's Honeymoon Cabinet","","Morris, Marshall, Faulkner & Co.","1861","Painted cabinet held by the V&A.",WDQ)
a("Storage cabinet","John Evelyn's cabinet","","","1645","Held by the V&A.",WDQ)
a(S,"Mae West Lips Sofa","","","1938","Designed by Salvador Dalí; held by the V&A.",WDQ)
a("Bookcase","Leistler Bookcase","","","","Held by the V&A.",WDQ)
a("Rocking chair","Endless Flow Rocking Chair","","","2011","Designed by Dirk Vander Kooij; held by MoMA.",W+"Special:Search?search=Endless+Flow+Rocking+Chair")
R[-1]['s']="https://www.moma.org/collection/works/160528"
# V&A page
VA="https://www.vam.ac.uk/search?q=chair&type=object&category=furniture"
a(D,"BA3 chair","","","1946–1948","London chair held by the V&A.",VA)
a(D,"Ply Chair","","","1990","Great Britain; held by the V&A.",VA)
a(D,"21400 mm chair","","","2010","Tokyo; held by the V&A.",VA)
a(D,"Joan's chair","","","1901","England; held by the V&A.",VA)
# Makers
BB=W+"B%26B_Italia"
a(U,"UP chair","UP series · UP 5 and UP 6","B&B Italia","1969","Designed by Gaetano Pesce.",BB)
a(S,"Le Bambole","","B&B Italia","1979","Designed by Mario Bellini; Compasso d'Oro 1979.",BB)
a(S,"Sisamo","","B&B Italia","1984","Designed by Studio Kairos; Compasso d'Oro 1984.",BB)
a("Sectional sofa","Sity","","B&B Italia","1987","Designed by Antonio Citterio; Compasso d'Oro 1987.",BB)
a(S,"Charles sofa","","B&B Italia","","Designed by Antonio Citterio.",BB)
a("Sectional sofa","Tufty-Time","","B&B Italia","","Designed by Patricia Urquiola.",BB)
a("Sectional sofa","Moon System","","B&B Italia","","Sofa system by Zaha Hadid.",BB)
a(S,"Moël","Moël sofa","Ligne Roset","2007","Designed by Inga Sempé.",W+"Ligne_Roset")
PF=W+"Poltrona_Frau"
a(S,"John-John sofa","","Poltrona Frau","2011","Designed by Jean-Marie Massaud.",PF)
a("Bed frame","John-John bed","","Poltrona Frau","2012","Designed by Jean-Marie Massaud.",PF)
a(D,"Juliet chair","","Poltrona Frau","2012","Designed by Benjamin Hubert; won the centenary competition.",PF)
FX=W+"Flexform"
a(U,"Boomerang lounge chair","","","","Designed by Rodolfo Bonetto; held by MoMA per the Flexform page.",FX)
a(U,"A.B.C.D. armchair","","Flexform","2016","Designed by Antonio Citterio; Compasso d'Oro honourable mention.",FX)
a("Dining table","621 Table","","Vitsœ","","Dieter Rams design.",W+"606_Universal_Shelving_System")
a(U,"Acapulco chair","","","","Named in Wikipedia's Category:Chairs.",W+"Category:Chairs")
a("Sectional sofa","Chadwick modular seating","","Herman Miller","","Named in Wikipedia's Category:Chairs.",W+"Category:Chairs")
# IKEA
HK="https://www.hunker.com/13727450/most-iconic-ikea-designs/"
a(S,"Ektorp","","IKEA","","IKEA sofa named in Hunker's list of iconic IKEA designs.",HK)
a("Bed frame","Malm","","IKEA","","IKEA bed named in Hunker's list of iconic IKEA designs.",HK)
a("Dining table","Docksta","","IKEA","","IKEA table named in Hunker's list of iconic IKEA designs.",HK)
a("Stool","Frosta","","IKEA","","IKEA stool named in Hunker's list of iconic IKEA designs.",HK)
a("Rolling cart","Råskog","","IKEA","","IKEA cart named in Hunker's list of iconic IKEA designs.",HK)
