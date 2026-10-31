# kind codes: CN colour negative, BW black-and-white, CR slide, BR bw reversal, IR infrared, CINE cine colour negative, INT integral instant, PEEL peel-apart instant
CUR='https://en.wikipedia.org/wiki/List_of_photographic_films'
DIS='https://en.wikipedia.org/wiki/List_of_discontinued_photographic_films'
# (src, kind, maker, name, years, versions "n@yrs@note;...")
R=[]
def add(src,kind,block):
    for line in block.strip().splitlines():
        p=[x.strip() for x in line.split('|')]
        while len(p)<4: p.append('')
        R.append((src,kind,p[0],p[1],p[2],p[3]))
# ---- current list
add(CUR,'CN','''
ADOX|Color Mission 200|2022–
ADOX|Color Mission Helios|TBC
AgfaPhoto|AgfaPhoto Color 400|2024–
CatLABS|X FILM 100 Color|2025–
dubblefilm|Apollo|2017–
dubblefilm|Bubblegum|2018–
dubblefilm|Jelly|2018–
dubblefilm|Pacific|2018–
dubblefilm|Solar|2017–
dubblefilm|Stereo|2019–
dubblefilm|Daily Color|2020–
Fujifilm|Fujifilm 200|2021–
Fujifilm|Fujifilm 400|2023–
Fujifilm|Fujicolor 100|avail|
Harman Technology|Harman RED 125|2025–
Harman Technology|Harman Switch Azure 125|2026–
Ilford Imaging (Europe)|Ilfocolor 400 (2020s)|2023–|Vintage tone@2023–;Plus Vintage tone@2024–;Cine tone@2024–
Kodak|Kodacolor|1942–|Kodacolor@1942–1963@first Kodacolor;Kodacolor-X@1963–1975;Kodacolor II@1972–1983;Kodacolor 400@1977–1983;Kodacolor HR@1982–1983;Kodacolor VR@1982–1989@100, 200, 400, 1000;Kodacolor VR-G@1987–1988;Kodacolor Gold@1988–@100, 200, 400, 1600;Kodacolor 100 and 200@2025–@current consumer films
Kodak|ProImage 100|1997–
Kono!|Donau 6|avail
Kono!|Kolorit 125 Tungsten|avail
Kono!|Kolorit 400 Tungsten|avail
Kono!|Rotwild 400|avail
Kono!|Alien 200|avail
Kono!|UFO 200|avail
Kono!|Katz 200|avail
Kono!|Luft 200|avail
Kono!|Liebe 200|avail
Kono!|Wintermärchen 200|?–2018
Lomography|Lomography Color Negative|avail|100@avail;400@avail;800@avail
Lomography|LomoChrome Turquoise XR|2015–
Lomography|LomoChrome Purple XR|2017–
Lomography|Redscale XR|2018–
Lomography|LomoChrome Metropolis XR|2019–
Lomography|Color Tiger 200|2022–
Lomography|Lobster Redscale|2022–
Lomography|LomoChrome Color '92|2023–|LomoChrome Color '92 Sun-kissed@2024–
Lomography|LomoChrome Classicolor 200|2025–
Luckyfilm|Luckyfilm C200|2025–
Luckyfilm|Luckyfilm C400|2026–
Optik Oldschool|OptiColour 200|2025–
Optik Oldschool|SantaColor|2025–|SantaColor 800@2025–;SantaColor 100@2026–
Original Wolfen|Original Wolfen NC|2022–|NC 500@2022–;NC 400@2023–
Rera|Rera Cool 100|2018–
Revolog|Revolog Echo|avail
Revolog|Revolog Kolor|avail
Revolog|Revolog Kosmos|avail
Revolog|Revolog Laser|avail
Revolog|Revolog Plexus|avail
Revolog|Revolog Rasp|avail
Revolog|Revolog Streak|avail
Revolog|Revolog Tesla|avail|Tesla I@avail;Tesla II@avail
Revolog|Revolog Texture|avail
Revolog|Revolog Volvox|avail
Revolog|Revolog 460 nm|avail
Revolog|Revolog 600 nm|avail
Revolog|Revolog Nebula|2020–
Rollei|Rollei Redbird|2018–
SFL|SFL A-Color 125|avail
Shanghai|Shenguang 400|2024–
Silberra|Silberra Color|2020–|Color 50@2020–;Color 100@2020–;Color 160@2020–
Svema|Svema Color|avail
Vibe|Vibe Photo|avail|Photo 400@avail;Photo 800@avail
Yodica|Yodica Antares|2018–
Yodica|Yodica Andromeda|2018–
Yodica|Yodica Atlas|2018–
Yodica|Yodica Pegasus|2018–
Yodica|Yodica Polaris|2018–
Yodica|Yodica Sirio|2018–
Yodica|Yodica Vega|2018–
Flic Film|Flic Elektra 100|2023–
Flic Film|Flic Aurora|2024–|Aurora 800@2024–2026@discontinued early 2026;Aurora 400@2025–
''')
add(DIS,'CN','''
Kodak|Kodak Ektar (1989 series)|1989–1997|Ektar 25@1989–1997;Ektar 125@1989–1997;Ektar 1000@1989–1997
Kodak|Kodak Royal Gold|1996–c2004|Royal Gold 25@1996–c2004;Royal Gold 100@1996–c2004;Royal Gold 200@1996–c2004;Royal Gold 400@1996–c2004;Royal Gold 1000@1996–c2004
Kodak|Kodak Gold (1997 series) and Gold Max|c1997–c2002
Kodak|Kodak Max|c2002–2007|Max 400@c2002–2007;Max Zoom 800@c2002–2007
Kodak|Kodak Supra|?–c2003|Supra 100@?–c2003;Supra 400@?–c2003;Supra 800@?–c2003
Kodak|Kodak High Definition|2003–?|High Definition 200@2003–?;High Definition 400@2003–?
Kodak|Kodak Ultra Color|2004–?|Ultra Color 100UC@2004–?;Ultra Color 400UC@2004–?
Fujifilm|Fujicolor F-II|1974–?|F-II@1974–?;F-II 400@1976–2017
Fujifilm|Fujicolor HR and Super HG|1983–?|HR series@1983–?;Super HR and Super HG series@1986–?
Fujifilm|Fujifilm Superia Reala|1989–2013
Fujifilm|Fujicolor C200|c1990–2021
Fujifilm|Fujicolor Venus 800|?–2019
Fujifilm|Fujicolor Press|?–c2008|Press 400/800/1600@?–c2008
Agfa|Agfacolor negative (CN series)|1949–c1984|Negativfilm T and K@1949–1956;CN17@1956–1971;CN14@1958–1966;CN17M@1963–c1966;CN17S@1966–1968;CNS@1968–1975;CNS 2@1971–c1982;CNS 400@1978–c1984;Agfacolor 100@1981–c1984
Agfa|Agfacolor XR and XRG|1984–1989|XR 100/200/400@1984–1989;XRG 100/200/400@1989–?
Agfa|Agfacolor XRS|1984–c1996|XRS 100/200/400/1000@1984–c1996
Agfa|Agfacolor HDC|?–2001|HDC 100/200/400@?–c1997;HDC plus 100/200/400@c1997–2001
Agfa|Agfacolor Optima|c1990–2005|Optima 125@c1990–c1996;Optima II 100/200/400@c1996–2005
Agfa|Agfacolor Vista|2001–2018|Vista 100/200/400/800@2001–2005;AgfaPhoto Vista@2005–2009;AgfaPhoto Vista plus@2009–2018
Agfa|Agfacolor Ultra and Portrait 160|c1990–2005|Ultra 50@c1990–c2001;Ultra 100@c2001–2005;Portrait 160@c1990–2005
Konica|Sakuracolor|1967–c1984|Sakuracolor N100@1967–1975;Sakuracolor II N100@1974–c1984;Sakuracolor 400@c1976–1984
Konica|Konica SR|c1984–c1997|SR@c1984–1986;SR-V 3200@1987;SR-G@1989–c1994;Super SR@1991–c1997
Konica|Konica Impresa|1991–
Konica|Konica Centuria|1999–
Konica|Konica Super XG and VX|1993–1999|Super XG@1993–c1996;VX@c1994–1999
Ilford|Ilfocolor (1960s–1980s)|1960–1988|Ilfocolor@1960–1965;Colorprint@1965–?;Super Colorprint@1967–?;Ilfocolor 100 and 400@c1983–1985;Ilfocolor HR@1984–1988;Ilfocolor Super HR@1985–1988
ORWO|ORWO NC series|?–1991|NC 16 to NC 21@?–1991;NF 100@1989–1990;PR 100@1990–1991;QRS 100/200@1991–1994
Ferrania|Ferrania Solaris FG|2000–2009|Solaris FG@2000–2003;Solaris FG Plus@2003–2009
Ferrania|Ferrania Color Print|1970s–c1986|Color Print 100@1970s–c1983;Color Print II@c1983–?;Color Print HR@?–c1986
Gevaert|Gevacolor N5|1950–?
Valca|Valcolor|1974–1991|Valcolor@1974–1975;Valcolor II@1975–1980;Valcolor HR100@?–1991
Negra|Negracolor|1970–1984|NC80@1970–1973;NC100@1973–1976;II and 400@1976–1984
Svema|Svema colour negative|1960s–1990s|DS-2, DS-5M, LN-5M, CND/CNL@1960s–1990s;Svemacolor DS 100@c1990–?
Luckyfilm|Luckyfilm GBR|2003–2012|GBR 100/200/400@2003–2012
ADOX|ADOX Color Implosion|2012–2017
efke|efkecolor|1968–1999|Color NM19@1968–1977;Color NM20@1972–1977;Color NM21@1979–c1986;efkecolor 100 and 400@1986–1999
Fuda|Fuda Color 100|c1984–c1990
''')
add(CUR,'BW','''
ADOX|ADOX CMS 20 II PRO|avail
ADOX|ADOX HR-50|2018–
ADOX|ADOX CHS 100 II|2013–|CHS 100 II@2013–2016;CHS 100 II reissue@2018–
Agfa-Gevaert|Agfa Copex Rapid|avail
AgfaPhoto|AgfaPhoto APX|2013–|APX 100@2013–;APX 400@2013–;APX 200@2026–
Argenti|Argenti Nanotomic X|avail
Argenti|Argenti Scale-X|avail
Argenti|Argenti Pan-X|avail
Argenti|Argenti ARF+ Reporter Film Plus|avail
Arista EDU|Arista EDU Ultra|avail|100@avail;200@avail;400@avail
Bergger|Bergger Pancro 400|2015–
CatLABS|CatLABS X FILM 80|2019–
CatLABS|CatLABS X FILM 320|2019–|X FILM 320@2019–;X FILM 320 Pro@2022–
CineStill|CineStill bwXX|2015–
dubblefilm|dubblefilm Daily black&white|2020–
Ferrania|FILM Ferrania P30|2019–
Ferrania|FILM Ferrania Orto|2023–
Ferrania|FILM Ferrania P33|2024–
Film Washi|Film Washi|2017–|'E'@2024–;'F'@2018–;'I'@avail;'K'@2024–;'P'@special order;'V'@2017–2025@discontinued;'W'@avail;'Y'@avail;'Z'@avail
Flic Film|Flic Wolfen 100|2022–
Flic Film|Flic XX-250|2022–
Flic Film|Flic UltraPan|2024–|UltraPan 100@2024–;UltraPan 200@2024–;UltraPan 400@2024–
Foma|Fomapan Retropan 320 Soft|2015–2021
Foma|Foma Ortho 400|2023–
Holga|Holga 400|2010–
Ilford|Ilford PAN|avail|PAN 100@avail;PAN 400@avail
Ilford|Ilford ORTHO Plus|2019–
Ilford|Ilford SFX 200|2007–
Ilford|Ilford XP2 Super|avail
Japan Camera Hunter|Streetpan 400|2016–
Kono!|Kono! Monolit 64|2018–
Kono!|Kono! Rekorder 100-200|2018–
Kosmo Foto|Kosmo Foto Mono|2017–
Kosmo Foto|Kosmo Foto Agent Shadow|2021–
Lomography|Lomography Orca|2012–
Lomography|Lomography Earl Grey and Lady Grey|2017–|Earl Grey@2017–;Lady Grey@2017–
Lomography|Lomography Berlin 400|2018–
Lomography|Lomography Potsdam 100|2019–
Lomography|Lomography Fantôme Kino|2020–
Lomography|Lomography Babylon Kino|2020–
Luckyfilm|Luckyfilm SHD|2024–|SHD 100@2024–;SHD 400@2024–
Optik Oldschool|Motion DBL-X|avail
Optik Oldschool|OptiMono 100|2026–
Oriental|Oriental Seagull|2016–|Seagull 100@2016–;Seagull 400@2016–
Original Wolfen|Original Wolfen UN 54|2022–
Original Wolfen|Original Wolfen NP 100|2022–
Original Wolfen|Original Wolfen P 400|2022–
Rera|Rera Pan|2018–|Pan 100S@2019–;Pan 400@2018–
Revolog|Revolog Snovlox|2019–
Rollei|Rollei Ortho 25 Plus|2017–
Rollei|Rollei Retro 80S|2009–
Rollei|Rollei SuperPan 200|2007–
Rollei|Rollei Retro 400S|avail
Rollei|Rollei Blackbird|2019–
Rollei|Rollei Paul & Reinhold|2020–
SFL|SFL black-and-white films|avail|T-25@avail;T-42@avail;UN54@avail;UN75@avail;Double-X 5222@avail;Double-X Aerographic 400@avail
Shanghai|Shanghai GP3 PAN|1958–|GP3 100 PAN@1958–;GP3 100 PAN relaunch@2019–;GP3 400 PAN@2019–
Silberra|Silberra Pan and Ultima|2017–|S25@2020–;Orta 50@2018–;Pan 50 / Ultima 50@2017–;Ultima 100@2017–;Pan 160 / Ultima 160@2017–;Pan 200 / Ultima 200@2017–;U200@2018–;U400@2018–
Silberra|Silberra Cinema|2018–|Cinema UN54@2018–;Cinema 75N+@2019–;Cinema 52XX@2018–
SPUR|SPUR DSX|avail
SPUR|SPUR Ultra R 800|2019–
Svema|Svema black-and-white films|avail|MZ-3@avail;FN 64@avail;Foto 100@avail;Foto 200@avail;Foto 400@avail;A-2SH@avail;NK-2SH@avail
UltraFine|UltraFine Finesse and Xtreme|avail|Finesse 100@avail;Finesse 400@avail;Xtreme 100@avail;Xtreme 400@avail;Ortho Litho Film@avail
Vibe|Vibe Photo B&W|avail|Photo B&W 100@avail;Photo B&W 400@avail
Kentmere|Kentmere Pan 200|2025–
''')
add(DIS,'BW','''
Kodak|Kodak Verichrome Safety Film|1931–1956
Kodak|Kodak Panatomic-X|1933–1987|Panatomic-X@1933–1940s;Panatomic-X reissue@1956–1987
Kodak|Kodak Super-XX|1940–1992
Kodak|Kodak Royal Pan|1954–?
Kodak|Kodak Plus-X Pan|1954–2011
Kodak|Kodak Verichrome Pan|1956–2002
Kodak|Kodak Royal-X Pan|1956–c1987
Kodak|Kodak Ektapan|?–2002
Kodak|Kodak Technical Pan|c1984–2004
Kodak|Kodak Academy 200|?–2000
Kodak|Kodak BW400CN|2004–2014|T400CN@?–2004;BW400CN@2004–2014;Portra 400BW@c2001–?
Ilford|Ilford FP series|1934–1990|FP@1934–1939;FP2@1939–1942;FP3@1942–1968;FP4@1968–1990
Ilford|Ilford HP series|1935–1989|HP@1935–1939;HP2@1939–1941;HP3@1941–1969;HP4@1965–1976;HP5@1976–1989
Ilford|Ilford HPS|1954–1998
Ilford|Ilford Pan F (1948)|1948–1992
Ilford|Ilford Selochrome|?–c1970
Ilford|Ilford XP1 and XP2|1981–1998|XP1@1981–1993;XP2@1991–1996;XP2 Plus@1996–1998
Fujifilm|Fujifilm Neopan SS|1953–2012
Fujifilm|Fujifilm Neopan F, S and SSS|c1954–2000s|Neopan F@c1954–2000s;Neopan S@c1954–?;Neopan SSS@c1954–1980s
Fujifilm|Fujifilm Neopan 400 Professional|1978–2014
Fujifilm|Fujifilm Neopan 1600 Professional|?–2010
Fujifilm|Fujifilm Neopan 400CN|2003–2020
Agfa|Agfa Isopan|c1935–c1985|Isopan FF / IFF@c1935–c1968;Isopan F / IF@c1935–c1979;Isopan Super Special@1935–c1980;Isopan Ultra@c1935–c1979;Isopan Record@mid-1950s–c1968;Isopan@c1966–c1985;Isopan 21@c1975–c1981
Agfa|Agfapan Professional|1968–c1989|Agfapan 25@1968–c1989;Agfapan 100@1968–c1989;Agfapan 200@1968–c1989;Agfapan 400@1968–c1989;Agfapan 1000@1968–c1982
Agfa|Agfapan APX|1989–2005|APX 25@1989–2000;APX 100@1989–2005;APX 400@c1990s–2005
Agfa|Agfa Isochrom F|c1933–1960s
Agfa|Agfacontour Professional|1970–c2002
Konica|Konica Sakura Panchro|c1946–?
Konica|Konica Konipan|?–?|Konipan SS;Konipan SSS
ORWO|ORWO NP series|1964–1994|NP 10, 15, 18, 20, 22, 27, 30@1964–1994
ORWO|ORWO PAN|1991–2005|PAN 25/100/400/125@1991–2005
efke|efke KB series|?–2012|KB 14 / 17 / 21@1974–c1991;KB 25 / 50 / 100@1990s–2012;KB 400@?–2012
Forte|Fortepan|1960s–2007|Fortepan 27@1960s–c1980;Fortepan 100@1980s–2007;Fortepan 200@1980s–2007
ADOX|ADOX KB / R series|1952–1973|KB 14 / R 14@1952–1973;KB 17 / R 17 / PL 17@1952–1973;KB 21 / R 21 / PL 21@1952–1973
Rollei|Rollei R3|2004–?
Svema|Svema Foto (1965 series)|c1965–1990s|Foto 32, 65, 130, 250@c1965–1987;FN 32, 64, 125, 250@?–1990s
Luckyfilm|Luckyfilm SHD (1990s series)|?–2012|SHD 100@?–2012;SHD 400@?–2012;SHD 400 CN@?–2012
''')
add(CUR,'CR','''
Fujifilm|Fujichrome Velvia 50|2007–
Kodak|Kodak Ektachrome E100|2018–
Lomography|Lomography Color Slide|avail
Rera|Rera Chrome 100|2018–
Rollei|Rollei CrossBird|2018–
Flic Film|Flic Chrome|2024–
Ilford Imaging (Europe)|Ilfochrome 100 (2020s)|2025–
Film Photography Project|FPP Retrochrome 400|avail
''')
add(DIS,'CR','''
Kodak|Kodachrome II and Kodachrome-X|1961–1974|Kodachrome II@1961–1974;Kodachrome-X@1962–1974;Kodachrome II Professional@1962–1978
Kodak|Kodachrome 200|1986–2007
Kodak|Kodak Ektachrome E200|?–2011
Kodak|Kodak Professional Elite Chrome|1989–2012|Elite Chrome 100@1989–2012;Elite Chrome Extra Color 100@1991–2012
Kodak|Kodak Ektachrome E100G, E100GX and E100VS|2000–2012|E100G@2000–2012;E100GX@2001–2009;E100VS@2002–2012
Kodak|Kodak Ektachrome 64T|?–2012
Kodak|Kodak Ektachrome 100 Plus|2001–2009
Fujifilm|Fujichrome Sensia|1994–2011|Sensia 100 / II / III@1994–2011;Sensia 200 and 400@1994–2010
Fujifilm|Fujichrome Provia 400F, 400X and 1600|1994–2013|Provia 400@1994–2000;Provia 1600@1994–2000;Provia 400F@2000–2006;Provia 400X@2006–2013
Fujifilm|Fujichrome Velvia 100F|2002–2021
Fujifilm|Fujichrome Astia 100F|2003–2012
Fujifilm|Fujichrome Fortia|2004–2007
Fujifilm|Fujichrome Professional D and T|1972–1999|Professional D and T@1972–c1979;100 Professional D@1978–1994;64 Professional T@1979–1999;400 Professional D@1980–1994;1600 Professional D@1984–1994
Fujifilm|Fujichrome R100|1961–?|Fujicolor R100@1961–c1966;New Fujicolor R100 / Fujichrome R100@1966–?
Agfa|Agfachrome CT|1958–1999|CT18@1958–1984;CT21@1974–1984;CT 200@1982–1992;CT 100@1984–1992;CT 100i@1992–1995;CT 100x@1995–1999
Agfa|Agfachrome RS and RSX|1984–2005|RS 50/100/200/1000@1984–1995;RSX 50/100/200@1995–1998;RSX II 50/100/200@1999–2005
Agfa|Agfa CTprecisa|1999–2018|CTprecisa 100/200@1999–2005;AgfaPhoto CTprecisa 100@2005–2009;CTprecisa 100 (new)@2009–2018
Agfa|Agfacolor Neu|1931–c1945|Agfacolor@1931–c1936;Agfacolor Neu@1936–c1945
Konica|Konica Chrome and Sakurachrome|?–1990|Sakuracolor R-100@?–1972;Sakurachrome R-100@c1983–c1986;Konica Chrome 100@c1986–1990
Ilford|Ilford Colour Film and Ilfochrome slide films|1948–1988|Colour Film D@1948–1960;Ilfochrome@1960–1965;Colorslide@1965–?;Ilfochrome 50/100/200/1000@1985–1988
ORWO|ORWO UT and UK slide films|1948–1994|Umkehrfilm T/K@1948–1964;UT and UK series@1964–1991;DIA 18, DIA 21, RC 100@1991–1994
Ferrania|Ferrania Scotch Chrome|1947–2005|Ferraniacolor@1947–c1962;Scotch Chrome@1980s–1990s;Solaris Chrome 100@2000–2005
efke|efkechrome|1964–1999|Color RD15@1964–1968;efkechrome 100@1984–1999
Svema|Svema CO slide films|1960s–c1994|CO-2, CO-22D, CO-32D, CO-50D, CO-65D, CO-90L, CO-180L@1960s–c1994
Rollei|Rollei Vario Chrome|2017–
''')
add(CUR,'BR','''
ADOX|ADOX Scala 50|2019–
Foma|Fomapan R 100|1998–
''')
add(DIS,'BR','''
Agfa|Agfa Scala 200x|c1990s–2005
Agfa|Agfa Dia Direct|1970s–1995|Dia Direct@1970s–1980s;Dia Direct DD 12 Professional@1980s–1995
ADOX|ADOX Scala 160|2016–2020
''')
add(CUR,'IR','''
Rollei|Rollei Infrared 400|avail
Film Photography Project|FPP BW IR|?–
''')
add(DIS,'IR','''
Kodak|Kodak High Speed Infrared|?–2007
Kodak|Kodak Ektachrome Professional Infrared EIR|1997–2012
Kodak|Kodak Aerochrome III IR (1443)|c1980s–2009
Konica|Konica Infrared 750 nm|?–?
efke|efke IR 820|1974–2012
ADOX|ADOX IR-HR PRO 50|2018–2021
''')
add(CUR,'CINE','''
CineStill|CineStill 400D|2022–
CineStill|CineStill Red Rum|2021–
Flic Film|Flic Cine color|2022–|Cine color 50D@2022–;Cine color 250D@2022–;Cine color 200T@2022–;Cine color 500T@2022–
Optik Oldschool|Optik Oldschool Motion|avail|Motion 200T@avail;Motion 250D@avail;Motion 500T@avail
SFL|SFL cine colour negative|avail|50D@avail;250D@avail;200T@avail;500T@avail
''')
add(DIS,'INT','''
Polaroid|Polaroid Spectra film|2013–2019
''')
add(CUR,'INT','''
Polaroid|Polaroid 8x10 film|avail
''')
add(DIS,'PEEL','''
Polaroid|Polaroid instant roll film|?–?|Types 20, 20C, 31, 32, 37, 38, 40, 41, 42, 43, 44, 46, 46L, 47 and 48
Polaroid|Polaroid Type 55 sheet film|?–2008
Fujifilm|Fujifilm FP-100B and FP-3000B|2003–2016|FP-100B Super@2003–2016;FP-3000B Super Speedy@2003–2013
''')
