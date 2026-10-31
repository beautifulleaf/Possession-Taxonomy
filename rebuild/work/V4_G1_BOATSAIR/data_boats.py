# Fetched Wikipedia builder pages (2026-10-31). Each line: name|year|designer-or-fact
BEN="https://en.wikipedia.org/wiki/Beneteau"
JEA="https://en.wikipedia.org/wiki/Jeanneau"
HR="https://en.wikipedia.org/wiki/Hallberg-Rassy"
def rows(t):
    out=[]
    for l in t.strip().splitlines():
        p=[x.strip() for x in l.split('|')]
        out.append(p+['']*(3-len(p)))
    return out
OCEANIS=rows("""
Oceanis 320|1987|Philippe Briand; generation 1
Oceanis 350|1985|Philippe Briand; generation 1
Oceanis 370|1989|Philippe Briand; generation 1
Oceanis 390|1987|generation 1
Oceanis 430|1985|Philippe Briand; generation 1
Oceanis 500|1987|Philippe Briand; generation 1
Oceanis 281|1994|Jean-Marie Finot; generation 2
Oceanis 300|1991|Jean-Marie Finot; generation 2
Oceanis 321|1994|Jean-Marie Finot; generation 2
Oceanis 351 / 352|1993|Jean Berret, Olivier Racoupeau, Armel Briand; generation 2
Oceanis 400|1992|Jean-Marie Finot; generation 2
Oceanis 440|1991|Bruce Farr; generation 2
Oceanis 461|1995|Bruce Farr, Armel Briand; generation 2
Oceanis 50|1995|Bruce Farr, Armel Briand; generation 2
Oceanis 510|1992|Philippe Briand; generation 2
Oceanis 36CC|1996|Jean Berret, Olivier Racoupeau, Armel Briand; generation 3
Oceanis 40CC|1994|Jean-Marie Finot, Armel Briand; generation 3
Oceanis 42CC|2001|Jean-Marie Finot; generation 3
Oceanis 44CC|1994|Bruce Farr, Armel Briand; generation 3
Oceanis 57|2002|Bruce Farr, Franck Darnet Design; generation 3
Oceanis Clipper 311 to 523|2004|Jean-Marie Finot; generation 4 (311, 323, 331, 343, 361, 373, 381, 393, 411, 423, 473, 523)
Oceanis 34|2008|Jean-Marie Finot, Nauta Design; generation 5
Oceanis 37|2007|Finot, Pascal Conq, Nauta Design; generation 5
Oceanis 40|2006|Berret, Racoupeau, Nauta Design; generation 5
Oceanis 41|2011|Finot-Conq, Nauta Design; generation 5
Oceanis 43|2006|Berret, Racoupeau, Nauta Design; generation 5
Oceanis 46|2007|Berret, Racoupeau, Nauta Design; generation 5
Oceanis 50 (generation 5)|2005|Berret, Racoupeau, Nauta Design
Oceanis 50 mk2|2009|Berret, Racoupeau, Nauta Design; generation 5
Oceanis 54|2008|Berret, Racoupeau, Nauta Design; generation 5
Oceanis 58|2009|Berret, Racoupeau, Nauta Design; generation 5
Oceanis 31|| Finot-Conq, Nauta Design; generation 6
Oceanis 35|2014|Finot-Conq, Nauta Design; generation 6
Oceanis 38|2014|Finot-Conq, Nauta Design; generation 6
Oceanis 45||Finot-Conq, Nauta Design; generation 6
Oceanis 48||Berret Racoupeau, Nauta Design; generation 6
Oceanis 55||Berret Racoupeau, Nauta Design; generation 6
Oceanis 60||Berret Racoupeau, Nauta Design; generation 6
Oceanis 30.1||Finot-Conq, Nauta Design; generation 7
Oceanis 35.1|2017|Finot-Conq, Nauta Design; generation 7
Oceanis 38.1|2017|Finot-Conq, Nauta Design; generation 7
Oceanis 41.1||Finot-Conq, Nauta Design; generation 7
Oceanis 46.1||Finot-Conq, Nauta Design; generation 7
Oceanis 51.1||Berret Racoupeau, Nauta Design; generation 7
Oceanis 55.1||Berret Racoupeau, Nauta Design; generation 7
Oceanis Yacht 62||Berret Racoupeau, Andreani Design; generation 7
""")
FIRST=rows("""
First 22|1978|Groupe Finot; generation 1
First 27|1978|André Mauric; generation 1
First 30 / 30E|1977|André Mauric; generation 1
First 18|1979|Groupe Finot; generation 1
First 25|1980|Jean-Marie Finot; generation 1
First 28|1981|Jean-Marie Finot; generation 1
First 32|1981|Jean Berret; generation 1
First 38|1982|Jean Berret; generation 1
First 42|1981|Germán Frers; generation 1
First 24|1983|Jean-Marie Finot; generation 1
First 26|1984|Jean-Marie Finot; generation 1
First 29|1984|Groupe Finot; generation 1
First 235|1986|Jean-Marie Finot; generation 2
First 265|1991|Jean-Marie Finot; generation 2
First 285|1987|Jean-Marie Finot; generation 2
First 305|1985|Jean Berret; generation 2
First 310|1990|Groupe Finot; generation 2
First 325|1984|Jean Berret; generation 2
First 345|1984|Jean Berret; generation 2
First 375|1985|Jean Berret; generation 2
First 405|1986|Jean Berret; generation 2
First 435|1985|Germán Frers; generation 2
First 456|1983|Germán Frers; generation 2
First 51|1987|Germán Frers; generation 2
First 32S5|1988|Jean Berret, Philippe Starck; generation 3
First 35S5|1988|Jean Berret, Philippe Starck; generation 3
First 35.7|1992|Jean Berret, Philippe Starck; generation 3
First 36S7|1995|Jean Berret, Philippe Starck; generation 3
First 38S5|1989|Jean Berret, Philippe Starck; generation 3
First 41S5|1989|Jean Berret, Philippe Starck; generation 3
First 42S7|1994|Bruce Farr, Philippe Starck; generation 3
First 45F5|1990|Bruce Farr, Sergio Pininfarina; generation 3
First 53F5|1990|Bruce Farr, Sergio Pininfarina; generation 3
First 210 Spirit|1992|Jean-Marie Finot; generation 4
First 211|1998|Groupe Finot; generation 4
First 260 Spirit|1995|Groupe Finot; generation 4
First 300 Spirit|1994|Groupe Finot; generation 4
First 31.7|1998|Finot Conq et Associés; generation 4
First 33.7|1996|Berret Racoupeau Yacht Design; generation 4
First 36.7|2001|Farr Yacht Design; generation 4
First 40.7|1997|Farr Yacht Design; generation 4
First 44.7|2003|Farr Yacht Design; generation 4
First 47.7|1999|Farr Yacht Design; generation 4
First 21.7|2004|Groupe Finot; generation 5
First 21.7S|2007|Finot Conq et Associés; generation 5
First 25.7|2004|Jean-Marie Finot; generation 5
First 27.7S|2002|Groupe Finot; generation 5
First 34.7 (10R)|2005|Farr Yacht Design; generation 5
First 20||Finot-Conq; generation 6
First 25 (generation 6)||Finot-Conq
First 30|2010|Juan Yacht Design, Nauta Design; generation 6
First 35|2008|Farr Yacht Design, Nauta Design; generation 6
First 40|2007|Farr Yacht Design, Nauta Design; generation 6
First 45|2007|P. Briand Yacht Design; generation 6
First 50|2006|P. Briand Yacht Design, Veerle Battiau; generation 6
First 53|2019|Biscontini Yacht Design; generation 7
""")
BEN_ONE=rows("""
Mumm 36|1992|Bruce Farr
Platu 25 (Beneteau 25)|1996|Bruce Farr
First Class 7|1984|Jean-Marie Finot, Jacques Fauroux
First Class 7.5|2003|Jean-Marie Finot
First Class 8|1982|Jean-Marie Finot, Jacques Fauroux
First Class 10|1983|Jean-Marie Finot, Jacques Fauroux
First Class 12|1986|Jean-Marie Finot
First Class Europe|1989|Jean-Marie Finot
First Class Challenge|1992|Jean-Marie Finot, Jean Berret
""")
FIGARO=rows("""
Figaro|1994|Jean-Marie Finot, Jean Berret
Figaro 2|2002|Marc Lombard
Figaro 3|2017|Van Peteghem Lauriot Prévost (VPLP)
""")
SENSE=rows("""
Sense 50|2010|first built 2010
Sense 43|2011|first built 2011
Sense 55|2012|first built 2012
Sense 46|2013|first built 2013
Sense 57|2016|first built 2016
""")
IDYLLE=rows("""
Idylle 880|1982|André Bénéteau
Idylle 1050|1985|André Bénéteau
Idylle 1150|1983|Jean Berret
Idylle 1350|1984|Germán Frers
Idylle 1550|1985|Germán Frers; also Mooring 51
""")
BEN_EARLY=rows("""
Guppy|1964|dinghy
Fletan|1966|
Galion|1967|
Baroudeur|1970|André Bénéteau
Piranha|1972|
Kerlouan|1972|André Bénéteau
Capelan|1972|André Bénéteau
Baroudeur MkII|1973|André Bénéteau
Cabochard|1973|André Bénéteau
Escapade|1976|André Bénéteau
Chenapan|1976|André Bénéteau
Canot 3.90|1977|junk rig
Wizz|1981|Jean-Marie Finot; two-person dinghy
California 5.20|1982|André Bénéteau
California 4.70|1983|André Bénéteau
California 6.60|1983|André Bénéteau
California 5.50|1986|André Bénéteau
""")
# Jeanneau (page's designs list) name|year
JEA_ALL=rows("""
Jeanneau Sea-bird|1960
Alize 20|1963
Jeanneau Storm|1966
Jeanneau Captain|1968
Jeanneau Arcachonnais|1969
Sangria 25|1969
Jeanneau Beniguet|1970
Jeanneau Cape Breton|1970
Jeanneau Folie Douce|1970
Jeanneau Love Love|1971
Jeanneau Metaf|1972
Jeanneau Poker|1972
Gin Fizz 37|1974
Melody 34|1974
Aquila 27|1975
Jeanneau Brin de Folie|1975
Jeanneau Flirt|1976
Jeanneau Brio|1979
Rush 31|1979
Rush Royale 31|1979
Symphonie 32|1979
Espace 1000|1980
Microsail|1980
Sun Fizz 40|1980
Espace 800|1981
Espace 1300|1981
Fantasia 27|1981
Trinidad 48|1981
Attalia 32|1982
Fun 23|1982
Regatta 39|1982
Sun Shine 36|1982
Arcadia 30|1983
Bahia 22|1983
Eolia 25|1983
Espace 620|1983
Sun Kiss 45|1983
Sun Kiss 47|1983
Sun Shine 38|1983
Fantasia 37|1984
Legende 1 Ton|1984
Selection 37|1984
Sun Fast 1/2 Ton|1984
Sun Legende 41|1984
Sun Rise 34|1984
Espace 990|1985
Espace 1100|1985
Sun Fast 20|1985
Tonic 23|1985
Tonic 23 CB|1985
CAP 450|1986
CAP 540|1986
Sun Light 30|1986
Sun Odyssey 43|1986
Lagoon 55|1987
Sun Dream 28|1987
Sun Magic 44|1987
Sun Odyssey 44|1987
Sun Way 27|1987
Sun Way 28|1987
Sun Way 28 CB|1987
Voyage 12.5|1987
Sun Charm 39|1988
Sun Dance 36|1988
Voyage 11.2|1988
Sun Fast 39|1989
Sun Liberty 34|1989
Sun Odyssey 51|1989
Sun Way 21|1989
Lagoon 42|1990
Sun Fast 41|1990
Sun Odyssey 36|1990
Sun Odyssey 39|1990
Sun Odyssey 42|1990
Jeanneau One Design 35|1991
Lagoon 37|1991
Sun Fast 31|1991
Sun Odyssey 31|1991
Sun Odyssey 34|1991
Sun Odyssey 47|1991
Sun Odyssey 47 CC|1991
Sun Fast 52|1992
Sun Odyssey 33|1992
Sun Odyssey 42.1|1992
Sun Fast 32|1993
International 50|1994
Mini JOD|1994
Sun Fast 17|1994
Sun Fast 36|1994
Sun Odyssey 28.1|1994
Sun Odyssey 32.1|1994
Sun Odyssey 37.1|1994
Sun Odyssey 43 DS|1994
Jeanneau One Design 24|1994
Sun Odyssey 42.2|1995
Sun Odyssey 45.1|1995
Sun Odyssey 52.2|1995
Lagoon 35|1995
Sun Fast 42|1996
Sun Odyssey 37.2|1996
Sun Odyssey 42 CC|1996
Lagoon 410|1997
Sun Odyssey 29.2|1997
Sun Odyssey 32.2|1997
Sun Odyssey 45.2|1997
Lagoon 470|1998
Stardust 342|1998
Stardust 343|1998
Sun Fast 26 (1998)|1998
Sun Odyssey 24.2|1998
Sun Odyssey 34.2|1998
Sun Odyssey 36.2|1998
Sun Odyssey 37|1998
Sun Odyssey 40|1998
Jeanneau 34.2|1999
Sun 2000|1999
Lagoon 380|2000
Sun Fast 37|2000
Sun Odyssey 40 DS|2000
Sun Fast 32i|2001
Moorings 32|2002
Sun Odyssey 32|2002
Sun Fast 26 (2003)|2003
Sun Fast 40|2003
Sun Fast 43|2003
Sun Odyssey 26|2003
Sun Odyssey 35|2003
Sun Odyssey 49|2003
Sun 2500|2004
Sun Fast 35|2004
Sun Fast 40.3|2004
Sun Odyssey 40.3|2004
Sun Odyssey 45|2004
Sun Odyssey 49 DS|2004
Sun Odyssey 54 DS|2004
Sun Odyssey 32i|2005
Sun Odyssey 39i|2005
Sun Odyssey 42i|2005
Sun Odyssey 42 DS|2007
Sun Odyssey 45 DS|2007
Jeanneau Yachts 53|2008
Sun Fast 3200|2008
Sun Odyssey 30i|2008
Sun Odyssey 33i|2008
Sun Odyssey 39 DS|2008
Sun Odyssey 50 DS|2008
Jeanneau Yachts 57|2009
Sun Odyssey 36i|2009
Sun Odyssey 44i|2009
Sun Odyssey 49i|2009
Sun Odyssey 409|2010
Sun Odyssey 379|2011
Sun Odyssey 439|2011
Sun Odyssey 44 DS|2011
Sun Odyssey 509|2011
Sun Fast 3600|2012
Sun Odyssey 41 DS|2013
Sun Odyssey 469|2013
Sun Odyssey 349|2014
Jeanneau Yachts 51|2015
Jeanneau Yachts 54|2015
Jeanneau Yachts 64|2015
Sun Odyssey 389|2015
Sun Odyssey 419|2015
Sun Odyssey 449|2015
Sun Odyssey 519|2015
Jeanneau Yachts 58|2016
Sun Odyssey 440|2017
Sun Odyssey 319|2018
Sun Odyssey 410|2018
Sun Odyssey 490|2018
Sun Fast 3300|2019
Jeanneau Yachts 60|2021
Jeanneau Yachts 65|2022
Sun Odyssey 380|2022
Jeanneau Yachts 55|2023
Sun Fast 30 One Design|2023
""")
HR_ROWS=rows("""
Misil I|1964–1972|
Hallberg-Rassy 24 (Misil II)|1972–1977|
Hallberg-Rassy 26|1978–1985|
P 28|1955–1973|
Hallberg-Rassy 29|1982–1994|Germán Frers
Monsun 31|1974–1982|
Hallberg-Rassy 312|1979–1993|Germán Frers
Hallberg-Rassy 31 Mk I|1992–2005|Germán Frers
Hallberg-Rassy 31 Mk II|2005–2009|Germán Frers
Hallberg-Rassy 310|2010–|Germán Frers
Hallberg-Rassy 94 Kutter|1981–1994|Germán Frers
Mistress 32|1969–1974|
Mistral 33|1966–1975|
Hallberg-Rassy 34|1990–2005|Germán Frers
Hallberg-Rassy 340|2017–|Germán Frers
Hallberg-Rassy 342|2005–2017|Germán Frers
Rasmus 35|1967–1978|
Hallberg-Rassy 352|1978–1991|Germán Frers
Hallberg-Rassy 36 Mk I|1989–1994|Germán Frers
Hallberg-Rassy 36 Mk II|1994–2003|Germán Frers
Hallberg-Rassy 37|2003–2012|Germán Frers
Hallberg-Rassy 372|2008–|Germán Frers
Hallberg-Rassy 38|1977–1986|
Hallberg-Rassy 382|1984–1992|Germán Frers
Hallberg-Rassy 39 Mk I|1991–1994|Germán Frers
Hallberg-Rassy 39 Mk II|1994–2003|Germán Frers
Hallberg-Rassy 40C|2019–|Germán Frers
Hallberg-Rassy 40 Mk I|2002–2015|Germán Frers
Hallberg-Rassy 40 Mk II|2016–2018|Germán Frers
Hallberg-Rassy 41|1975–1981|
Hallberg-Rassy 412|2012–|Germán Frers
Hallberg-Rassy 42 (E)|1980–1991|Germán Frers
Hallberg-Rassy 42F Mk I|1991–1994|Germán Frers
Hallberg-Rassy 42F Mk II|1994–2001|Germán Frers
Hallberg-Rassy 43 Mk I|2001–2007|Germán Frers
Hallberg-Rassy 43 Mk II|2007–2013|Germán Frers
Hallberg-Rassy 43 Mk III|2013–2016|Germán Frers
Hallberg-Rassy 44|2016–|Germán Frers
Hallberg-Rassy 45|1988–1996|Germán Frers
Hallberg-Rassy 46|1995–2005|Germán Frers
Hallberg-Rassy 48 Mk I|2004–2013|Germán Frers
Hallberg-Rassy 48 Mk II|2014–|Germán Frers
Hallberg-Rassy 49|1982–1997|Germán Frers
Hallberg-Rassy 50|2020–|Germán Frers
Hallberg-Rassy 53|1992–2006|Germán Frers
Hallberg-Rassy 54|2006–2012|Germán Frers
Hallberg-Rassy 55|2012–2017|Germán Frers
Hallberg-Rassy 57|2018–|Germán Frers
Hallberg-Rassy 62|1997–2011|Germán Frers
Hallberg-Rassy 64|2011–|Germán Frers
Hallberg-Rassy 69|2024–|Germán Frers
""")
