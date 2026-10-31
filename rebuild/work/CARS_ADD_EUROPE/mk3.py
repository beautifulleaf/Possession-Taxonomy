def blk(g,url,names):
    out=['#%s|%s'%(g,url)]
    for t in names:
        p=t.split('|'); n=p[0]; y=p[1] if len(p)>1 else ''; c=p[2] if len(p)>2 else ''
        out.append('%s|%s|%s|%s'%(g,n,y,c))
    return '\n'.join(out)+'\n'
S=''
alfa="""Alfa Romeo 4C|2013|sports car
Alfa Romeo 6C|1927
Alfa Romeo 8C
Alfa Romeo 8C Competizione|2007|sports car
Alfa Romeo 12C
ALFA 15/20 HP
ALFA 12 HP
ALFA 15 HP|1911
ALFA 20/30 HP|1914
ALFA 24 HP
Alfa Romeo 33|1983
Alfa Romeo 33 Stradale||sports car
Alfa Romeo 33 Stradale (2023)||sports car
ALFA 40/60 HP
Alfa Romeo 75|1985
Alfa Romeo 90|1984
Alfa Romeo 105/115 Series Coupés|1963|coupé
Alfa Romeo 145
Alfa Romeo 146
Alfa Romeo 147|2000
Alfa Romeo 155
Alfa Romeo 156
Alfa Romeo 159
Alfa Romeo 164
Alfa Romeo 166
Alfa Romeo 1750 Berlina
Alfa Romeo 1900
Alfa Romeo 2000
Alfa Romeo 2000 Berlina
Alfa Romeo 2000 GTV
Alfa Romeo 2000 Spider Veloce
Alfa Romeo 2000 Sportiva
Alfa Romeo 2300
Alfa Romeo 2600
Alfa Romeo Alfa 6
Alfa Romeo Alfasud
Alfa Romeo Alfasud Sprint
Alfa Romeo Alfetta
Alfa Romeo Arna
Alfa Romeo Brera and Spider
Alfa Romeo Dauphine
Alfa Romeo G1
Alfa Romeo Giulia
Alfa Romeo Giulia (2015)
Alfa Romeo Giulietta
Alfa Romeo Giulietta (1954)
Alfa Romeo Giulietta (2010)
Alfa Romeo Giulietta (1977)
Alfa Romeo Giulietta Sprint Speciale
Alfa Romeo Gran Sport Quattroruote
Alfa Romeo GT
Alfa Romeo GT 1300 Junior
Alfa Romeo GTA
Alfa Romeo GTV 2.0
Alfa Romeo GTV and Spider
Alfa Romeo Junior (2024)
Alfa Romeo MiTo
Alfa Romeo Montreal
Alfa Romeo RL
Alfa Romeo RM
Alfa Romeo RZ
Alfa Romeo Spider
Alfa Romeo Sports Sedan
Alfa Romeo Sprint
Alfa Romeo Sprint Veloce
Alfa Romeo Stelvio
Alfa Romeo SZ
Alfa Romeo Tonale""".split('\n')
lancia="""Lancia Delta (1911)|1911
Lancia 2000|1971
Lancia A112
Lancia Appia|1953
Lancia Aprilia|1937
Lancia Ardennes
Lancia Ardea|1939
Lancia Artena|1931
Lancia Astura|1931
Lancia Augusta|1933
Lancia Aurelia|1950
Lancia Belna
Lancia Beta|1972
Lancia Beta Montecarlo
Lancia Beta Trevi
Lancia Beta (1909)|1909
Lancia Dedra|1989
Lancia Delta
Lancia Dialfa
Lancia Dikappa
Lancia Dilambda
Lancia Epsilon
Lancia Eta
Lancia Flaminia
Lancia Flavia
Lancia Fulvia
Lancia Gamma
Lancia Gamma (2026)
Lancia Gamma (1910)
Lancia HPE
Lancia Jolly
Lancia Kappa
Lancia Kappa (1919)
Lancia Lambda
Lancia Y
Lancia Lybra
Lancia Montecarlo
Lancia Musa
Lancia Phedra
Lancia Prisma
Lancia Scorpion
Lancia Thema
Lancia Thesis
Lancia Theta
Lancia Trevi
Lancia Trikappa
Lancia Voyager
Lancia Y10
Lancia Ypsilon
Lancia Z
Lancia Zeta
Lancia Zeta (1912)""".split('\n')
jag="""SS 1
Jaguar 240
Jaguar 340
Jaguar 420 and Daimler Sovereign (1966–1969)
Jaguar 420G
Jaguar E-Pace
Jaguar E-Type
Jaguar F-Pace
Jaguar F-Type
Jaguar I-Pace
SS 90
SS Jaguar 100
Jaguar Mark 1
Jaguar Mark 2
Jaguar Mark IV
Jaguar Mark V
Jaguar Mark VII
Jaguar Mark VIII
Jaguar Mark IX
Jaguar Mark X
Jaguar S-Type (1999)
Jaguar S-Type (1963)
Jaguar Sovereign
Jaguar X-Type
Jaguar XE
Jaguar XF
Jaguar XJ
Jaguar XJ6
Jaguar XJ12
Jaguar XJ220
Jaguar XJR
Jaguar XJS
Jaguar XK
Jaguar XK-E
Jaguar XK100
Jaguar XK120
Jaguar XK140
Jaguar XK150
Jaguar XKSS""".split('\n')
lr="""Land Rover 101 Forward Control
Land Rover Defender
Land Rover Discovery
Land Rover Freelander
Land Rover Discovery Sport
Land Rover Series II
Land Rover Series IIa
Land Rover Series III
Land Rover Llama
Land Rover LR3
Land Rover LR4
Range Rover
Range Rover Classic
Range Rover Evoque
Range Rover GT
Range Rover Sport
Range Rover Velar""".split('\n')
bent="""Bentley Arnage
Bentley Azure
Bentley Mulliner Bacalar
Bentley Mulliner Batur
Bentley Bentayga
Bentley Brooklands
Bentley Brooklands Coupé
Bentley Continental
Bentley Continental GT
Bentley Continental GTC
Bentley Continental R
Bentley Continental S
Bentley Continental T
Bentley Corniche
Bentley Eight
Bentley Flying Spur (2005)
Bentley Mark V
Bentley Mark VI
Bentley Mulsanne (1980–1992)
Bentley Mulsanne (2010)
Bentley R Type
Bentley S1
Bentley S2
Bentley S3
Bentley State Limousine
Bentley T-series
Bentley Torcal
Bentley Turbo R
Bentley Turbo RT
Bentley Turbo S""".split('\n')
mor="""Morris 8/40
Morris 11/55
Morris 18-22
Morris 575
Morris 850
Morris 1100
Morris 1300
Morris 1500
Morris 1700
Morris 1800
Morris 2200
Morris Cooper
Morris Freeway
Morris Mascot
Morris Metro
Morris Mini
Morris Monaco
Morris Mini Minor
Morris-Martel
Morris Oxford
Morris Oxford MO
Morris Series Z
Morris Major (1931 to 1933)""".split('\n')
tri="""Triumph 2.5 PI
Triumph 10
Triumph 12/50
Triumph 1200
Triumph 1800
Triumph 2500
Triumph Atlas
Triumph Chicane
Triumph Courier
Triumph Dolomite
Triumph Dolomite Sprint
Triumph TR-X
Triumph 20TS""".split('\n')
lada="""Lada 1200
Lada 1300
Lada 1500
Lada 1600
Lada 2101
Lada 2104
Lada 2105
Lada 2107
Lada Azimut
Lada Bushman
Lada Cevaro
Lada Iskra
Lada Aura
Lada Niva Vision
Lada Nova
Lada Oda
Lada Sable
Lada VFTS
Lada Volante
VAZ-2104
VAZ-2107
VAZ-2108
VAZ-2110
VAZ-2111
VAZ-2112
VAZ-2117
VAZ-2118
VAZ-2119
VAZ-2120
VAZ-2121
VAZ-2123
VAZ-2170
VAZ-2171
VAZ-2172""".split('\n')
rov="""Rover 2000
Rover Commerce
Rover P1
Rover P2
Rover P6BS
Rover Two-litre
Rover V8-S
Rover Vitesse""".split('\n')
tra="""Trabant P 50|1957
Trabant 600|1962""".split('\n')
S+=blk('Alfa Romeo','https://en.wikipedia.org/wiki/Category:Alfa_Romeo_vehicles',alfa)
S+=blk('Lancia','https://en.wikipedia.org/wiki/Category:Lancia_vehicles',lancia)
S+=blk('Jaguar','https://en.wikipedia.org/wiki/Category:Jaguar_vehicles',jag)
S+=blk('Land Rover','https://en.wikipedia.org/wiki/Category:Land_Rover_vehicles',lr)
S+=blk('Bentley','https://en.wikipedia.org/wiki/Category:Bentley_vehicles',bent)
S+=blk('Morris','https://en.wikipedia.org/wiki/Category:Morris_vehicles',mor)
S+=blk('Triumph','https://en.wikipedia.org/wiki/Category:Triumph_Motor_Company_vehicles',tri)
S+=blk('Lada','https://en.wikipedia.org/wiki/Category:Lada_vehicles',lada)
S+=blk('Rover','https://en.wikipedia.org/wiki/Category:Rover_vehicles',rov)
S+=blk('Trabant','https://en.wikipedia.org/wiki/Trabant_P_50',tra)
# VW past models from list page
vw="""Volkswagen Beetle (Type 1)|1938
Volkswagen Type 18A|1949
Volkswagen Hebmüller Cabriolet|1949|convertible
Volkswagen Karmann Ghia|1955
Volkswagen 1500/1600 (Type 3)|1961
Volkswagen 411/412 (Type 4)|1967
Volkswagen Country Buggy|1967
Volkswagen 181|1968
Volkswagen K70|1968
Volkswagen Scirocco|1974
Volkswagen Dasher|1974
Volkswagen Rabbit|1975
Volkswagen Derby|1977
Volkswagen Caribe|1977
Volkswagen Iltis|1978
Volkswagen Cabriolet|1979
Volkswagen Gol|1980
Volkswagen Atlantic|1981
Volkswagen Santana|1981
Volkswagen Quantum|1982
Volkswagen Parati|1982
Volkswagen Voyage|1983
Volkswagen Gacel|1983
Volkswagen Corsar|1984
Volkswagen Citi Golf|1984
Volkswagen Carat|1987
Volkswagen Corrado|1988
Volkswagen Apollo|1990
Volkswagen Senda|1991
Volkswagen Logus|1993
Volkswagen Pointer|1994
Volkswagen Sharan|1995
Volkswagen Polo Playa|1996
Volkswagen New Beetle|1997
Volkswagen Jetta King|1997
Volkswagen Lupo|1998
Volkswagen Phaeton|2002
Volkswagen Touareg|2002
Volkswagen Fox|2003
Volkswagen Golf Plus|2004
Volkswagen Passat Lingyu|2005
Volkswagen Eos|2006
Volkswagen Suran|2006
Volkswagen Routan|2008
Volkswagen Clásico|2010
Volkswagen Jetta Pioneer|2010
Volkswagen Vento|2010
Volkswagen Beetle (A5)|2011
Volkswagen Up|2011
Volkswagen Passat NMS|2011
Volkswagen New Jetta|2013
Volkswagen Golf Sportsvan|2014
Volkswagen SpaceCross|2014
Volkswagen XL1|2015
Volkswagen Ameo|2016
Volkswagen Phideon|2016
Volkswagen Tiguan Allspace|2018
Volkswagen Tiguan X|2020""".split('\n')
S+=blk('Volkswagen','https://en.wikipedia.org/wiki/List_of_Volkswagen_vehicles',vw)
peu="""Peugeot Type 160|1913
Peugeot Quadrilette|1921
Peugeot Type 163|1921
Peugeot Type 172|1923
Peugeot Type 173|1923
Peugeot Type 174|1923
Peugeot Type 175|1923
Peugeot Type 176|1924
Peugeot Type 177|1924
Peugeot Type 181|1925
Peugeot 12 CV Six|1928
Peugeot Type 184|1928
Peugeot Type 190|1928
Peugeot Type 159|1920
Lion-Peugeot Type VA|1907
Lion-Peugeot Type VC2|1909
Lion-Peugeot Type VD2|1915""".split('\n')
S+=blk('Peugeot','https://en.wikipedia.org/wiki/List_of_Peugeot_vehicles',peu)
open('lists_r3.txt','w',encoding='utf-8').write(S)
# versions: marque|base model|code|year
V="""BMW|1 Series|E81/E82/E87/E88|2004
BMW|1 Series|F20/F21|2011
BMW|1 Series|F52|2017
BMW|1 Series|F40|2019
BMW|2 Series|F22/F23|2013
BMW|2 Series|F44|2020
BMW|3 Series|E21|1975
BMW|3 Series|E30|1982
BMW|3 Series|E36|1990
BMW|3 Series|E46|1998
BMW|3 Series|E90/E91/E92/E93|2005
BMW|3 Series|F30/F31/F34|2011
BMW|4 Series|F32/F33/F36|2013
BMW|5 Series|E12|1972
BMW|5 Series|E28|1981
BMW|5 Series|E34|1987
BMW|5 Series|E39|1995
BMW|5 Series|E60/E61|2003
BMW|5 Series|F07/F10/F11|2010
BMW|5 Series|G30/G31|2016
BMW|6 Series|E24|1976
BMW|6 Series|E63/E64|2003
BMW|6 Series|F06/F12/F13|2011
BMW|6 Series|G32|2017
BMW|7 Series|E23|1977
BMW|7 Series|E32|1986
BMW|7 Series|E38|1994
BMW|7 Series|E65/E66|2001
BMW|7 Series|F01/F02|2008
BMW|7 Series|G11/G12|2015
BMW|8 Series|E31|1989
BMW|8 Series|G14/G15|2018
BMW|X1|E84|2009
BMW|X1|F48|2015
BMW|X3|E83|2003
BMW|X3|F25|2011
BMW|X3|G01|2017
BMW|X4|F26|2014
BMW|X4|G02|2018
BMW|X5|E53|1999
BMW|X5|E70|2006
BMW|X5|F15|2013
BMW|X6|E71|2008
BMW|X6|F16|2014
BMW|Z4|E85/E86|2002
BMW|Z4|E89|2009
BMW|Z4|G29|2018
Audi|A3|8L|1996
Audi|A3|8P|2003
Audi|A3|8V|2012
Audi|A3|8Y|2020
Audi|A4|B5|1994
Audi|A4|B6|2001
Audi|A4|B7|2004
Audi|A4|B8|2007
Audi|A4|B9|2015
Audi|A6|C4|1994
Audi|A6|C5|1997
Audi|A6|C6|2004
Audi|A6|C7|2011
Audi|A6|C8|2018
Audi|A8|D2|1994
Audi|A8|D3|2003
Audi|A8|D4|2010
Audi|A8|D5|2017
Audi|TT|Mk1|1998
Audi|TT|Mk2|2006
Audi|TT|Mk3|2014
Audi|R8|Type 42|2006
Audi|R8|Type 4S|2015
Audi|A5|8T/8F|2007
Audi|A5|F5|2016
Audi|A5|B10|2024
Audi|Q5|8R|2008
Audi|Q5|FY|2016
Audi|Q5|GU|2024
Audi|Q3|8U|2011
Audi|Q3|F3|2018
Audi|Q3|FJ|2025
Audi|A1|8X|2010
Audi|A1|GB|2019
Audi|A7|4G8|2010
Audi|A7|4K8|2018
Mercedes-Benz|C-Class|W202|1993
Mercedes-Benz|C-Class|W203|2001
Mercedes-Benz|C-Class|W204|2008
Mercedes-Benz|C-Class|W205|2014
Mercedes-Benz|C-Class|W206|2021
Mercedes-Benz|E-Class|W124|1985
Mercedes-Benz|E-Class|W210|1996
Mercedes-Benz|E-Class|W211|2003
Mercedes-Benz|E-Class|W212|2009
Mercedes-Benz|E-Class|W213|2016
Mercedes-Benz|E-Class|W214|2023
Mercedes-Benz|S-Class|W116|1972
Mercedes-Benz|S-Class|W126|1979
Mercedes-Benz|S-Class|W140|1991
Mercedes-Benz|S-Class|W220|1998
Mercedes-Benz|S-Class|W221|2006
Mercedes-Benz|S-Class|W222|2013
Mercedes-Benz|S-Class|W223|2020
Mercedes-Benz|A-Class|W168|1997
Mercedes-Benz|A-Class|W169|2005
Mercedes-Benz|A-Class|W176|2013
Mercedes-Benz|A-Class|W177|2018
Mercedes-Benz|G-Class|W460|1979
Mercedes-Benz|G-Class|W463|1990
Mercedes-Benz|G-Class|W465|2024
Mercedes-Benz|SL|R107|1971
Mercedes-Benz|SL|R129|1989
Mercedes-Benz|SL|R230|2001
Mercedes-Benz|SL|R231|2013
Mercedes-Benz|SL|R232|2022
Mercedes-Benz|SLK-Class|R170|1996
Mercedes-Benz|SLK-Class|R171|2004
Mercedes-Benz|SLK-Class|R172|2011
Mercedes-Benz|M-Class|W163|1997
Mercedes-Benz|M-Class|W164|2005
Mercedes-Benz|B-Class|W245|2006
Mercedes-Benz|B-Class|W246|2012
Mercedes-Benz|B-Class|W247|2019
Mercedes-Benz|CLS-Class|C219|2004
Mercedes-Benz|CLS-Class|W218|2011
Mercedes-Benz|CLS-Class|C257|2018
Mercedes-Benz|CLA|C117|2013
Mercedes-Benz|CLA|C118|2019
Mercedes-Benz|CLA|C178|2025
Mercedes-Benz|GLC|X253|2015
Mercedes-Benz|GLC|X254|2022
Mercedes-Benz|GLS|X166|2012
Mercedes-Benz|GLS|X167|2019
Mercedes-Benz|GLA|X156|2013
Mercedes-Benz|GLA|H247|2020
Volkswagen|Beetle|Type 1|1938
Volkswagen|Beetle|A5|2011"""
open('versions_r3.txt','w',encoding='utf-8').write(V)
