# kind | name | alias | maker | year | designer/fact | source
LC="https://en.wikipedia.org/wiki/List_of_chairs"
WD="https://www.wikidata.org/wiki/"
KN="https://en.wikipedia.org/wiki/Knoll_(company)"
HM="https://en.wikipedia.org/wiki/Herman_Miller_(manufacturer)"
FH="https://en.wikipedia.org/wiki/Fritz_Hansen_(company)"
CA="https://en.wikipedia.org/wiki/Cassina_S.p.A."
AR="https://en.wikipedia.org/wiki/Artek_(company)"
CP="https://en.wikipedia.org/wiki/Compasso_d%27Oro"
R=[]
def a(k,n,al,mk,y,d,s=LC,role=None,v=None): R.append(dict(k=k,n=n,a=al,mk=mk,y=y,d=d,s=s,role=role,v=v or []))
# Dining chair
D="Dining chair"
a(D,"40/4 chair","","","1964","Stacking chair designed by David Rowland.")
a(D,"A56 chair","","Tolix","1956","Tolix steel chair listed beside the 1927 Chaise A.")
a(D,"620 Chair Programme","620 Chair","Vitsœ","","Dieter Rams design for Vitsœ.")
a(D,"601 Chair","","","","Chair designed by Dieter Rams.")
a(D,"Alta chair","","","","Chair designed by Oscar Niemeyer.")
a(D,"GJ Chair","No. 9-1 · GJ Chair","","","Designed by Grete Jalk and made by Poul Jeppesen.")
a(D,"Ghost chair","","Fiam Italia","1987","Transparent chair designed by Cini Boeri and Tomu Katayanagi.",WD+"Q140429531")
a(D,"Handkerchief Chair","","Knoll","1983","Designed by Lella and Massimo Vignelli.",LC)
a(D,"Iquo chair","","Knoll","","Designed by Ini Archibong for Knoll.")
a(D,"Knotted chair","","","1995","Rope-and-resin chair designed by Marcel Wanders.")
a(D,"Kelp Chair","","","2021","Designed by Alexander Westerlund.")
a(D,"Ladder Chair","","","1920s","Designed by Erich Dieckmann.")
a(D,"Mackintosh chairs","","","1917","Chairs designed by Charles Rennie Mackintosh.")
a(D,"Pop chair","","","2005","Designed by Brad Ascalon.")
a(D,"S chair","\"S\" chair","Cappellini","","Designed by Tom Dixon for Cappellini.")
a(D,"Portuguese chair (5008)","","Adico","1930s","Chair produced by Adico.")
a(D,"Gonçalo chair","","","1940s","Designed by Gonçalo Rodrigues dos Santos.")
a(D,"Polypropylene stacking chair","","","1963","Designed by Robin Day.")
a(D,"Resilient Chair","","","1948","Designed by Eva Zeisel.")
a(D,"Rex chair","","","1952","Designed by Niko Kralj.")
a(D,"Rey Chair","","","1971","Designed by Bruno Rey.")
a(D,"Sawbuck chair (CH29)","CH29","Carl Hansen & Søn","1952","Designed by Hans Wegner.","https://en.wikipedia.org/wiki/Carl_Hansen_%26_S%C3%B8n")
a(D,"Weissenhof chair (MR 10)","MR 10 · Weissenhof chair","Knoll","1927","Cantilever chair designed by Ludwig Mies van der Rohe with Lilly Reich.",WD+"Q1780145")
a(D,"Z chair","\"Z\" Chair","","","Designed by Paul Tuttle.")
a(D,"Stedelijk aluminium chair","","","","Designed by Sabine Marcelis.")
a(D,"Ultraleggera 1660","","","","Designed by Oskar Zieta.")
a(D,"laleggera stacking chair","laleggera","Alias","1998","Stacking chair designed by Riccardo Blumer.",WD+"Q20199417")
a(D,"Margherita chair","","Bonacina","1951","Woven chair designed by Franco Albini and Franca Helg.",WD+"Q60616602")
a(D,"Klismos chair (Robsjohn-Gibbings)","\"Klismos\" Chair","","1937","Designed by T. H. Robsjohn-Gibbings.",WD+"Q20199543")
a(D,"Mido Chair","","","2021","Designed by Jomo Tariku.",WD+"Q110026461")
a(D,"Mollo Oa Leifo","Fire in the hearth","","2021","Chairs Mme and Ngoanana designed by Atang Tshikare.",WD+"Q110026459")
a(D,"Kalahari","","","2005","Designed by Tom Strala.",WD+"Q140893294")
a(D,"Wiggle chair","Wiggle side chair","","1972","Cardboard chair designed by Frank Gehry.")
a(D,"Easy Edges","","","","Cardboard furniture series by Frank Gehry.")
a(D,"High Sticking chair","","Knoll","1989–1991","Designed by Frank Gehry.",KN)
a(D,"Queen Anne chair (Venturi)","Queen Anne chair","Knoll","1984","Designed by Robert Venturi and Denise Scott Brown.",KN)
a(D,"Donald Judd chairs","","","early 1970s","Chairs designed by Donald Judd.")
a(D,"Carimate Chair","","Cassina","1959","Designed by Vico Magistretti.",CA)
a(D,"Bikini chair","","","1949","Designed by Wendell Lovett.")
a(D,"Corner chair (Rohlfs)","Corner chair","","","Designed by Charles Rohlfs.")
a(D,"Ideal A","","","1960s","Designed by Vermund Larsen.")
a(D,"Model 650","","Knoll","1941","Designed by Jens Risom.",KN)
a(D,"Mandarin chair","","Knoll","","Designed by Ettore Sottsass.",KN)
a(D,"Fuld Nesting Chair","","Herman Miller","2024","Designed by Stefan Diez.",HM)
a(D,"Ro Chair","","Fritz Hansen","2013","Designed by Jaime Hayon.",FH)
a(D,"Pirkka stool","Pirkka","Artek","1955","Designed by Ilmari Tapiovaara.",AR)  # moved to Stool below
R.pop()
a(D,"Lilly Reich MR 10 note","","","","")
R.pop()
# Armchair
A="Armchair"
a(A,"4801 armchair","","Kartell","1963","Armchair by Joe Colombo, shown with the 1964 date in the chair list.","https://en.wikipedia.org/wiki/Kartell")
a(A,"Barrel chair (Frank Lloyd Wright)","Barrel chair","Cassina","1937","Designed by Frank Lloyd Wright.",CA)
a(A,"Larkin Administration Building chair","","","","Designed by Frank Lloyd Wright.")
# upholstered lounge
U="Upholstered lounge chair"
a(U,"Karuselli","Karuselli lounge chair","","1965","Designed by Yrjö Kukkapuro.",WD+"Q20918469")
a(U,"Joe","Joe sofa chair","","","Baseball-glove armchair by De Pas, D'Urbino and Lomazzi.",WD+"Q3808629")
a(U,"Gala armchair","","Bonacina","1951","Designed by Franco Albini.",WD+"Q107353721")
a(U,"Proust armchair","","Studio Alchimia","1978","Designed by Alessandro Mendini.",WD+"Q21234427")
a(U,"Rover chair","","","","Designed by Ron Arad.")
a(U,"Miss Blanche","","","","Designed by Shiro Kuramata.")
a(U,"Model 3107 note","","","","")
R.pop()
a(U,"406 Aalto armchair","Armchair 406","Artek","1938","Armchair by Alvar Aalto with webbing seat.")
a(U,"Hanging Egg note","","","","");R.pop()
# tubular
T="Tubular & wire-frame lounge chair"
a(T,"Tugendhat chair","","Knoll","1929–1930","Designed by Ludwig Mies van der Rohe and Lilly Reich.")
a(T,"Gispen 407","","Gispen","1933","Designed by Willem Hendrik Gispen.",WD+"Q26220572")
a(T,"Transat chair","","","","Designed by Eileen Gray.")
a(T,"Bertoia Diamond note","","","","");R.pop()
# moulded
M="Moulded, shell & bentwood lounge chair"
a(M,"Organic Chair","","","1940","Designed by Charles Eames and Eero Saarinen.",WD+"Q2029817")
a(M,"Gyre lounge chair","","","2006","Designed by Zaha Hadid.",WD+"Q96748897")
a(M,"Figure of Eight Chair","","","1993","Designed by Ross Lovegrove.",WD+"Q26134296")
a(M,"I Feltri","","Cassina","1987","Felt chair designed by Gaetano Pesce.",WD+"Q3147089")
a(M,"Ovalia Egg Chair","","","1968","Designed by Henrik Thor-Larsen.")
a(M,"Zocker","","","1970s","Designed by Luigi Colani.")
a(M,"Spun chair","","","","Designed by Thomas Heatherwick.")
a(M,"Eames Fiberglass Armchair note","","","","");R.pop()
a(M,"Marshmallow note","","","","");R.pop()
# chaise
C="Chaise longue"
a(C,"Lockheed Lounge","","","","Designed by Marc Newson.")
# recliner
a("Recliner","Transat note","","","","");R.pop()
# office
O="Office chair"
a(O,"Synthesis 45","","Olivetti","","Designed by Ettore Sottsass.")
a(O,"LessThanFive Chair","","Steelcase","","Designed by Michael Young.")
a(O,"Darwin's writing chair","","","1835","Chair used by Charles Darwin.",WD+"Q137719137")
# stool
S="Stool"
a(S,"Pirkka stool","Pirkka","Artek","1955","Designed by Ilmari Tapiovaara.",AR)
a(S,"Stool 60 note","","","","");R.pop()
# garden
a("Adirondack chair","Muskoka chair","","","","Adirondack-type garden chair named in the chair list.")
a("Garden bench","Strandkorb","Beach chair (Strandkorb)","","","Hooded beach chair named in the chair list.")
# tables
a("Dining table","Super-elliptical table","","Fritz Hansen","1968","Designed by Piet Hein.",FH)
a("Dining table","Essay table","","Fritz Hansen","","Designed by Cecilie Manz.",FH)
a("Dining table","Nomos","Nomos table","Tecno","1987","Table and desk system by Foster + Partners, Compasso d'Oro 1987.",CP,"landmark")
a("Dining table","Plano tables","","Fritz Hansen","","Designed by Pelikan Design.",FH)
a("Coffee table","Saarinen table","","Knoll","1957","Designed by Eero Saarinen.",KN)
a("Coffee table","Noguchi table","","Herman Miller","1948","Designed by Isamu Noguchi.",HM)
# beds
a("Bed frame","Nahalie","Nahalie bed","","1978","Bed by Vico Magistretti; 2020 Compasso d'Oro Products Career Award.",CP,"landmark")
# sofa
a("Sofa","Marshmallow sofa","","Herman Miller","1954","Designed by Irving Harper.",HM)
a("Sofa","Klippan","","IKEA","","IKEA sofa named with Billy and Poäng as sold by the tens of millions.","https://en.wikipedia.org/wiki/IKEA")
# storage
a("Bookcase","Nuage bookcase","","Cassina","","Designed by Charlotte Perriand.",CA)
