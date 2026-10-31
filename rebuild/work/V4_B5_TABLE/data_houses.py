# Data tables for V4_B5_TABLE. Every row is from a fetched page named in sources.tsv.
PM = "https://en.wikipedia.org/wiki/List_of_porcelain_manufacturers"
EU = "https://en.wikipedia.org/wiki/Porcelain_manufacturing_companies_in_Europe"
W = "https://en.wikipedia.org/wiki/"

# Tableware houses: (country, name, aliases, year, note, source, own, tier, own_y)
# note = what the reference says (plain); own/tier/own_y only where a fetched page states them.
T = []
def t(c, n, y="", note="", s=PM, a="", own="", tier="", oy=""):
    T.append(dict(c=c, n=n, y=y, note=note, s=s, a=a, own=own, tier=tier, oy=oy))

# China
t("China", "Ding ware", "", "Chinese kiln ware listed with porcelain manufacturers.")
t("China", "Jingdezhen porcelain", "", "Chinese porcelain centre listed with porcelain manufacturers.")
# Japan
t("Japan", "Arita ware", "late 16th century", "Hizen porcelain of Arita, Kyushu, whose Imari, Kakiemon and Nabeshima styles supplied early Japanese exports.", W+"Arita_ware", a="Hizen ware")
t("Japan", "Kutani ware", "1655", "Porcelain of Kutani, Kaga, first mentioned in 1655, stopped around 1730 and revived in 1804 or 1807.", W+"Kutani_ware")
t("Japan", "Hirado ware", "", "Japanese porcelain listed with porcelain manufacturers.")
t("Japan", "Kakiemon", "", "Japanese overglaze porcelain style and kiln family listed with porcelain manufacturers.")
t("Japan", "Mikasa & Company", "", "Tableware company listed under Japan.")
t("Japan", "Nabeshima ware", "", "Japanese porcelain listed with porcelain manufacturers.")
t("Japan", "Narumi", "", "Japanese porcelain maker listed under Japan.")
t("Japan", "Noritake", "1904", "Japanese maker whose first Western-style dinner set, Sedan, appeared in 1914.", W+"Noritake", own="Morimura Group", tier="Independent")
# Austria
t("Austria", "Vienna Porcelain Manufactory", "1718", "Imperial porcelain works in Vienna, 1718 to 1864.")
t("Austria", "Augarten", "1923", "Vienna porcelain manufactory founded 1923 and still working.", a="Vienna Porcelain Manufactory Augarten")
t("Austria", "Porzellanmanufaktur Reidling", "", "Austrian porcelain maker at Sitzenberg-Reidling.", EU)
# Croatia
t("Croatia", "Inkerpor", "1953", "Croatian porcelain maker founded 1953.")
# Czech Republic
t("Czech Republic", "Haas & Czjzek", "1792", "Horní Slavkov porcelain works, 1792 to 2011.")
t("Czech Republic", "Thun 1794", "1794", "Porcelain maker at Klášterec nad Ohří, working since 1794.")
t("Czech Republic", "Český porcelán", "1864", "Porcelain maker at Dubí, working since 1864.")
t("Czech Republic", "Rudolf Kämpf", "1907", "Porcelain maker at Nové Sedlo, working since 1907.")
t("Czech Republic", "G. Benedikt", "1882", "Porcelain maker at Karlovy Vary; absorbed Langenthal of Switzerland.", EU)
# Denmark
t("Denmark", "Aluminia", "", "Danish faience works listed under Denmark.")
t("Denmark", "Bing & Grøndahl", "1853", "Danish porcelain maker whose Christmas plates began in 1895.", EU)
t("Denmark", "P. Ipsens Enke", "", "Danish pottery listed under Denmark.")
t("Denmark", "Kastrup Vaerk", "", "Danish works listed under Denmark.")
t("Denmark", "Kronjyden", "", "Danish porcelain listed under Denmark.")
t("Denmark", "Porcelænshaven", "", "Danish porcelain maker listed under Denmark.")
t("Denmark", "Royal Copenhagen", "1775", "Danish porcelain house, working since 1775.", W+"Royal_Copenhagen", own="Fiskars Corporation", tier="Global group", oy="2013")
t("Denmark", "GreenGate", "1991", "Danish tableware maker founded 1991.", EU)
# Finland
t("Finland", "Arabia", "1873", "Helsinki porcelain works founded as a Rörstrand subsidiary in 1873.", W+"Arabia_(company)", own="Fiskars Corporation", tier="Global group", oy="2007")
t("Finland", "Iittala", "1881", "Finnish glass and tableware house founded 1881; its ceramic line Origo dates from 1999.", W+"Iittala", own="Fiskars Corporation", tier="Global group", oy="2007")
t("Finland", "Kupittaan Savi", "", "Finnish pottery listed under Finland.")
t("Finland", "Savitorppa", "", "Finnish pottery listed under Finland.")
t("Finland", "Kultakeramiikka", "", "Finnish ceramics maker listed under Finland.")
t("Finland", "Kermansavi", "", "Finnish pottery listed under Finland.")
t("Finland", "Pentik", "", "Finnish pottery brand listed under Finland, linked to Anu Pentik.")
# France
t("France", "Rouen porcelain", "1673", "Early French soft-paste porcelain of Rouen.", EU)
t("France", "Saint-Cloud porcelain", "1693", "Soft-paste porcelain works, 1693 to 1766.")
t("France", "Chantilly porcelain", "1730", "Soft-paste porcelain works, 1730 to 1800.")
t("France", "Vincennes porcelain", "1740", "Porcelain works, 1740 to 1756, which became Sèvres.")
t("France", "Mennecy-Villeroy porcelain", "1745", "Soft-paste porcelain works, 1745 to 1765.")
t("France", "Sèvres porcelain", "1756", "Royal porcelain manufactory working since 1756.")
t("France", "Niderviller", "1763", "Lorraine factory that made porcelain from 1763 to 1827.", EU)
t("France", "Lunéville", "1766", "Lorraine factory that made porcelain from 1766 to 1777.", EU)
t("France", "Revol porcelain", "1789", "French porcelain maker working since 1789.")
t("France", "Limoges porcelain", "1771", "Porcelain of Limoges, started there in 1771.", EU)
t("France", "Haviland", "", "Limoges porcelain house listed under France.")
t("France", "Bernardaud", "1863", "Limoges porcelain house founded 1863; family firm in its fourth generation.", W+"Bernardaud", own="Bernardaud family", tier="Independent")
t("France", "Marie Daâge", "2000", "Limoges porcelain maker founded 2000.", EU)
# Germany
t("Germany", "Meissen", "1710", "First European hard-paste porcelain works, begun in 1710; owned by the State of Saxony.", W+"Meissen_porcelain", a="Staatliche Porzellan-Manufaktur Meissen", own="Free State of Saxony", tier="Independent")
t("Germany", "Höchst", "1746", "Hesse porcelain works founded 1746.", EU)
t("Germany", "Fürstenberg", "1747", "Lower Saxony porcelain works founded 1747.", EU)
t("Germany", "Nymphenburg", "1747", "Bavarian porcelain works founded 1747.", EU)
t("Germany", "Frankenthal", "1755", "Palatinate porcelain works founded 1755.", EU)
t("Germany", "Gotha", "1757", "Thuringian porcelain works founded 1757.", EU)
t("Germany", "Ludwigsburg", "1758", "Württemberg porcelain works founded 1758.", EU)
t("Germany", "Ansbach", "1758", "Bavarian porcelain works founded 1758.", EU)
t("Germany", "Kloster Veilsdorf", "1760", "Thuringian porcelain works founded 1760.", EU)
t("Germany", "Kelsterbach", "1761", "Hesse porcelain works founded 1761.", EU)
t("Germany", "Volkstedt", "1762", "Thuringian porcelain works founded 1762.", EU)
t("Germany", "KPM Berlin", "1763", "Royal Porcelain Manufacture Berlin, founded 1763.", EU, a="Königliche Porzellan-Manufaktur Berlin")
t("Germany", "Wallendorf", "1764", "Thuringian porcelain works founded 1764.", EU)
t("Germany", "Villeroy & Boch", "1748", "Tableware company at Mettlach; François Boch began making ceramics in Lorraine in 1748 and the firm took its name in 1836.", W+"Villeroy_%26_Boch", own="Villeroy & Boch AG", tier="Independent")
t("Germany", "Ilmenau", "1777", "Thuringian porcelain works founded 1777.", EU)
t("Germany", "Rauenstein", "1783", "Thuringian porcelain works founded 1783.", EU)
t("Germany", "Weimar Porzellan", "1790", "Thuringian porcelain works at Blankenhain, founded 1790.", EU)
t("Germany", "Tettau", "1794", "Bavarian porcelain works founded 1794.", EU)
t("Germany", "Hutschenreuther", "1814", "Selb porcelain maker founded 1814; owned by Rosenthal since 2000.", W+"Rosenthal_(company)", own="Rosenthal GmbH (Sambonet Paderno Industrie)", tier="Independent", oy="2000")
t("Germany", "Lichte", "1822", "Thuringian porcelain works founded 1822.", EU)
t("Germany", "Kahla", "1844", "Thuringian porcelain works founded 1844.", EU)
t("Germany", "Wagner & Apel", "1877", "Porcelain works at Lippelsdorf, founded 1877.", EU)
t("Germany", "Rosenthal", "1879", "Selb porcelain house founded by Philipp Rosenthal; Service 2000 was designed by Raymond Loewy and Richard Latham in 1954.", W+"Rosenthal_(company)", own="Sambonet Paderno Industrie", tier="Independent", oy="2009")
t("Germany", "Bauscher Weiden", "1881", "Weiden porcelain maker founded 1881.", EU)
t("Germany", "Arzberg", "1887", "Bavarian porcelain maker founded 1887; owned by Rosenthal since 2013.", W+"Rosenthal_(company)", own="Sambonet Paderno Industrie", tier="Independent", oy="2013")
t("Germany", "Heinrich & Co.", "1903", "Selb porcelain maker founded 1903.", EU)
t("Germany", "Seltmann Weiden", "1910", "Weiden porcelain maker founded 1910.", EU)
t("Germany", "Linder Porzellanfabrik", "1931", "Porcelain maker at Küps, founded 1931.", EU)
t("Germany", "Barbara Flügel", "1986", "Selb porcelain maker founded 1986.", EU)
# Hungary
t("Hungary", "Hollóháza", "1777", "Hungarian porcelain manufactory working since 1777.")
t("Hungary", "Herend", "1826", "Hungarian porcelain manufactory founded by Vince Stingl in 1826; privatised in 1993.", W+"Herend_Porcelain_Manufactory", own="Herend management and employees", tier="Independent", oy="1993")
t("Hungary", "Zsolnay", "1853", "Pécs porcelain and ceramics manufactory founded 1853.")
t("Hungary", "Alföld Porcelán", "1969", "Hungarian porcelain maker founded 1969.", a="Alföld Porcelán Edénygyár")
# India
t("India", "Arta Broch Ceramics", "", "Indian ceramics maker listed under India.")
t("India", "TCL Ceramics", "", "Indian ceramics maker, formerly Tata Ceramics, listed under India.")
# Ireland
t("Ireland", "Irish Dresden", "", "Irish porcelain figurine and tableware maker listed under Ireland.")
# Italy
t("Italy", "Medici porcelain", "1575", "Florentine porcelain of 1575, the earliest European entry in the list.", EU)
t("Italy", "Vezzi", "1720", "Venetian porcelain works founded 1720.", EU)
t("Italy", "Richard-Ginori", "1735", "Doccia porcelain house near Florence, also styled Ginori 1735; the Ginori family sold it to Giulio Richard in 1896.", W+"Richard-Ginori")
t("Italy", "Capodimonte porcelain", "1743", "Naples porcelain works, 1743 to 1759, later moved to Madrid.")
t("Italy", "Le Nove", "1762", "Italian porcelain works of 1762 to 1835.", EU)
t("Italy", "Cozzi", "1764", "Venetian porcelain works, 1764 to 1812.", EU)
t("Italy", "Naples porcelain", "1771", "Neapolitan porcelain works, 1771 to 1806.")
t("Italy", "Fabris", "1922", "Italian art-porcelain maker, 1922 to 1972.", a="Manifattura Italiana Porcellane Artistiche Fabris")
t("Italy", "Porcellane Principe", "", "Capodimonte-style porcelain maker at Vicenza, listed under Italy.")
t("Italy", "Iconoclastic", "", "Design porcelain maker at Vicenza, listed under Italy.")
t("Italy", "Mangani", "", "Art-porcelain maker at Florence, listed under Italy.")
t("Italy", "Capodimonte's Finest", "2012", "Naples porcelain maker founded 2012.", EU)
t("Italy", "Deruta", "Renaissance", "Umbrian maiolica centre whose Raffaellesco dragon motif is its trademark.", W+"Deruta_ceramics")
# Lithuania
t("Lithuania", "Jiesia", "1938", "Porcelain maker at Kaunas, founded 1938.")
# Monaco
t("Monaco", "Manufacture de Porcelaine de Monaco", "1975", "Porcelain maker founded 1975.", EU)
# Netherlands
t("Netherlands", "Weesp", "1759", "Dutch porcelain works founded 1759.", EU, a="Weesp Porselein")
t("Netherlands", "Loosdrecht", "1774", "Dutch porcelain works founded 1774.", EU, a="Loosdrechts Porselein")
t("Netherlands", "Haagsche Plateelbakkerij Rozenburg", "", "Dutch pottery listed under the Netherlands.")
t("Netherlands", "Jema", "1955", "Porcelain maker at Maastricht, founded 1955.", EU)
# Norway
t("Norway", "Porsgrund", "1885", "Norwegian porcelain maker founded 1885.", EU)
t("Norway", "Figgjo", "1941", "Norwegian porcelain maker at Sandnes, founded 1941.")
t("Norway", "Egersund", "", "Norwegian porcelain listed under Norway.")
t("Norway", "Herrebøe", "", "Norwegian porcelain listed under Norway.")
t("Norway", "Stavangerflint", "", "Norwegian pottery listed under Norway.")
# Poland
t("Poland", "Ćmielów", "1809", "Polish porcelain maker founded 1809.", EU)
t("Poland", "Bolesławiec", "", "Polish ceramics town with a tradition from the Middle Ages.", EU)
t("Poland", "Kristoff", "1820", "Polish porcelain maker at Wałbrzych, founded 1820.", EU)
t("Poland", "Wałbrzych", "1831", "Polish porcelain works founded 1831.", EU)
t("Poland", "Tułowice", "1852", "Polish porcelain works founded 1852.", EU)
t("Poland", "Karolina", "1860", "Polish porcelain works at Jaworzyna Śląska, founded 1860.", EU)
t("Poland", "Pruszków", "1872", "Polish porcelain works founded 1872.", EU)
t("Poland", "Włocławek", "1873", "Polish porcelain works founded 1873.", EU)
t("Poland", "Chodzież", "1897", "Polish porcelain works founded 1897.", EU)
t("Poland", "Huta Franciszka", "1920", "Polish porcelain works at Bykowina, founded 1920.", EU)
t("Poland", "Bogucice", "1922", "Polish porcelain works at Katowice, founded 1922.", EU)
t("Poland", "Lubiana", "1969", "Polish porcelain maker founded 1969.", EU, a="ZPS Lubiana")
# Portugal
t("Portugal", "Vista Alegre", "1824", "Portuguese porcelain maker licensed by King João VI in 1824; bought by Visabeira in 2009.", W+"Vista_Alegre_Atlantis", own="Visabeira", tier="Independent", oy="2009")
t("Portugal", "Alcobaça", "", "Portuguese porcelain maker listed under Portugal.", a="Sociedade Porcelanas de Alcobaça")
t("Portugal", "Costa Verde", "", "Portuguese porcelain maker in Aveiro district.")
t("Portugal", "Porcel", "1987", "Portuguese porcelain maker at Aveiro, founded 1987.", EU)
# Romania
t("Romania", "Apulum", "1970", "Romanian porcelain maker at Alba Iulia, founded 1970.", EU)
t("Romania", "AXA Porcelaine", "1991", "Romanian porcelain maker at Alba Iulia, founded 1991.", EU)
# Russia
t("Russia", "Imperial Porcelain Factory", "1744", "Saint Petersburg porcelain works founded 1744.")
t("Russia", "Verbilki", "1766", "Russian porcelain works founded 1766.", a="Gardner")
t("Russia", "Gzhel", "1802", "Russian ceramics centre working since 1802.")
t("Russia", "Dulevo", "1832", "Russian porcelain works at Likino-Dulyovo, founded 1832.", a="Dulevo Farfor")
t("Russia", "Lomonosov", "", "Russian porcelain maker listed under Russia.")
# Spain
t("Spain", "Alcora", "1750", "Spanish ceramics and porcelain works founded 1750.", EU)
t("Spain", "Buen Retiro", "1760", "Madrid royal porcelain factory, 1760 to 1812.")
t("Spain", "La Moncloa", "1817", "Madrid porcelain works founded 1817.", EU)
t("Spain", "Sargadelos", "1808", "Galician porcelain works, from 1808 and intermittently since.")
t("Spain", "Porvasal", "", "Spanish porcelain maker listed under Spain.")
# Sweden
t("Sweden", "Marieberg", "1758", "Stockholm porcelain works founded 1758.", EU)
t("Sweden", "Rörstrand", "1770", "Swedish porcelain maker founded 1770.", EU)
t("Sweden", "Gustavsberg", "", "Swedish porcelain maker listed under Sweden.", a="Gustavsberg porcelain")
# Switzerland
t("Switzerland", "Langenthal", "1906", "Swiss porcelain maker founded 1906, now part of G. Benedikt.", EU, a="Suisse Langenthal")
# Belgium
t("Belgium", "Tournai", "1751", "Belgian porcelain works founded 1751.", EU)
# United Kingdom
t("United Kingdom", "Bow", "1747", "London porcelain factory, 1747 to 1776.", a="Bow porcelain factory")
t("United Kingdom", "Chelsea", "1743", "London porcelain factory begun about 1743-45 and merged with Derby in 1770.", a="Chelsea porcelain factory")
t("United Kingdom", "Royal Crown Derby", "1750", "Derby porcelain house dating from 1750 or 1757; bought by Kevin Oakes in 2016.", W+"Royal_Crown_Derby", own="Oakes family", tier="Independent", oy="2016")
t("United Kingdom", "Royal Worcester", "1751", "Worcester porcelain house, 1751 to 2008, acquired by Portmeirion in 2009.", W+"Portmeirion_Pottery", own="Portmeirion Group", tier="Independent", oy="2009")
t("United Kingdom", "Liverpool porcelain", "1754", "Liverpool porcelain factories from 1754.", EU)
t("United Kingdom", "Lowestoft", "1757", "Suffolk porcelain factory founded 1757.", EU, a="Lowestoft Porcelain Factory")
t("United Kingdom", "Wedgwood", "1759", "Staffordshire pottery founded by Josiah Wedgwood on 1 May 1759; porcelain from 1812.", W+"Wedgwood", own="Fiskars Corporation", tier="Global group", oy="2015")
t("United Kingdom", "Spode", "1767", "Stoke-on-Trent maker, 1767 to 2008, acquired by Portmeirion in 2009.", W+"Portmeirion_Pottery", own="Portmeirion Group", tier="Independent", oy="2009")
t("United Kingdom", "Plymouth porcelain", "1768", "Plymouth porcelain works founded 1768.", EU, a="Plymouth Porcelain")
t("United Kingdom", "Aynsley China", "1775", "Longton bone china maker founded 1775.")
t("United Kingdom", "Mintons", "1793", "Stoke-on-Trent maker, 1793 to 1968, merged with Royal Doulton.", a="Mintons Ltd")
t("United Kingdom", "Coalport", "1795", "English porcelain works founded 1795.", EU, a="Coalport porcelain")
t("United Kingdom", "Nantgarw", "1813", "Welsh porcelain works; porcelain made 1813 to 1820.", EU, a="Nantgarw Pottery")
t("United Kingdom", "Cambrian Pottery", "1814", "Swansea pottery, 1814 to 1870.", EU, a="Swansea porcelain")
t("United Kingdom", "Royal Doulton", "1815", "English maker, 1815 to 2009, acquired by Fiskars.", own="Fiskars Corporation", tier="Global group", oy="2015", s=W+"Fiskars")
t("United Kingdom", "Belleek", "1884", "Northern Irish porcelain maker founded 1884.", EU)
t("United Kingdom", "Portmeirion", "1960", "Stoke-on-Trent pottery founded 1960 by Susan Williams-Ellis and Euan Cooper-Willis; Botanic Garden dates from 1972.", W+"Portmeirion_Pottery", own="Portmeirion Group", tier="Independent", a="Portmeirion Pottery")
t("United Kingdom", "Caughley", "", "Shropshire porcelain factory listed under the United Kingdom.", a="Caughley porcelain")
t("United Kingdom", "Churchill China", "", "Staffordshire tableware maker listed under the United Kingdom.")
t("United Kingdom", "Davenport", "", "Staffordshire pottery listed under the United Kingdom.")
t("United Kingdom", "Denby", "1809", "Derbyshire stoneware pottery founded 1809; reported bought by TJ Morris, trading as Home Bargains, in August 2026.", W+"Denby_Pottery_Company", a="Denby Pottery Company", own="TJ Morris (Home Bargains)", tier="Independent", oy="2026")
t("United Kingdom", "Goss crested china", "", "Souvenir china listed under the United Kingdom.")
t("United Kingdom", "Longton Hall", "", "Staffordshire porcelain factory listed under the United Kingdom.", a="Longton Hall porcelain")
t("United Kingdom", "New Hall", "", "Staffordshire porcelain factory listed under the United Kingdom.", a="New Hall porcelain")
t("United Kingdom", "Rockingham", "", "Yorkshire pottery listed under the United Kingdom.", a="Rockingham Pottery")
t("United Kingdom", "Saint James's Factory", "1750s", "London porcelain factory of the 1750s, known for Girl-in-a-Swing wares.")
t("United Kingdom", "Vauxhall", "", "London porcelain factory listed under the United Kingdom.", a="Vauxhall porcelain")
# Brazil, Colombia, Iran, Taiwan, Malaysia, South Africa, South Korea, Sri Lanka, Turkey, UAE, Vietnam
t("Brazil", "Germer", "", "Brazilian porcelain maker listed under Brazil.", a="Germer Porcelanas Finas")
t("Brazil", "Porcelana Schmidt", "", "Brazilian porcelain maker listed under Brazil.")
t("Colombia", "Corona", "", "Colombian ceramics company listed under Colombia.")
t("Iran", "Maghsoud", "1993", "Iranian porcelain group working since 1993.", a="Maghsoud Factories Group")
t("Iran", "Zarin Iran Porcelain Industries", "1881", "Iranian porcelain maker, a Maghsoud subsidiary, working since 1881.")
t("Taiwan", "Franz Collection", "", "Taiwanese porcelain maker listed under Taiwan.")
t("Malaysia", "Royal Selangor", "", "Malaysian maker listed under Malaysia.")
t("South Africa", "Continental China", "", "South African china maker listed under South Africa.")
t("South Korea", "Haengnam Chinaware", "", "Korean chinaware maker listed under South Korea.")
t("South Korea", "Hankook Chinaware", "", "Korean chinaware maker listed under South Korea.")
t("South Korea", "Prouna", "", "Korean chinaware maker listed under South Korea.")
t("Sri Lanka", "Dankotuwa Porcelain", "", "Sri Lankan porcelain maker listed under Sri Lanka.")
t("Sri Lanka", "Noritake Lanka Porcelain", "", "Sri Lankan porcelain maker listed under Sri Lanka.")
t("Sri Lanka", "Royal Fernwood Porcelain", "", "Sri Lankan porcelain maker linked to Dankotuwa in the list.")
t("Turkey", "Yildiz Porselen", "1890", "Turkish porcelain maker, 1890 to 1936 and again from 1994.")
t("Turkey", "Sümerbank Porselen", "1957", "Turkish porcelain maker, 1957 to 1994.")
t("Turkey", "Istanbul Porselen", "1963", "Turkish porcelain maker, 1963 to the early 1990s.")
t("Turkey", "Kütahya Porselen", "1970", "Turkish porcelain maker working since 1970.")
t("Turkey", "Porland Porselen", "1976", "Turkish porcelain maker working since 1976.")
t("Turkey", "Bonna Porselen", "1983", "Turkish porcelain maker working since 1983.")
t("Turkey", "Güral Porselen", "1989", "Turkish porcelain maker working since 1989.")
t("United Arab Emirates", "RAK Porcelain", "", "Porcelain maker in Ras Al Khaimah, listed under the United Arab Emirates.")
t("Vietnam", "Minh Long I", "1970", "Vietnamese porcelain maker working since 1970.", a="Minh Long I porcelain")
# United States
t("United States", "Wonder Porcelain", "", "American porcelain maker listed under the United States.")
t("United States", "Blue Ridge", "", "American hand-painted dinnerware listed under the United States.")
t("United States", "Franciscan", "", "American dinnerware listed under the United States.")
t("United States", "Lenox", "", "American porcelain maker listed under the United States.")
t("United States", "Lotus Ware", "", "American porcelain listed under the United States.")
t("United States", "Pickard China", "", "American china maker listed under the United States.")
t("United States", "Fiesta", "1936", "Colourful dinnerware line of the Homer Laughlin China Company, introduced 1936; the company was renamed Fiesta Tableware Company in 2020.", W+"Fiesta_(dinnerware)", a="Homer Laughlin China Company", own="Fiesta Tableware Company", tier="Independent")
t("United States", "Steubenville Pottery", "", "American pottery maker of the American Modern line.", W+"Fiesta_(dinnerware)")
t("United States", "Heath Ceramics", "", "American pottery maker of the Coupe line.")
t("United States", "Corelle", "", "American glass-ceramic dinnerware brand.")
t("United States", "Anchor Hocking", "", "American glassware maker of the Fire-King Jadeite line.")
t("United States", "Pyrex", "", "American oven-glass tableware brand.")
# Other pattern makers (UK)
t("United Kingdom", "Royal Albert", "", "English bone china brand of the Old Country Roses pattern; a Fiskars subsidiary.", W+"Fiskars", own="Fiskars Corporation", tier="Global group")
t("United Kingdom", "Emma Bridgewater", "", "English earthenware maker of the Polka Dot pattern.")
t("United Kingdom", "Hornsea", "", "English pottery maker of the Heirloom and Saffron patterns.")
t("United Kingdom", "Midwinter", "", "English pottery maker of the Galaxy and Spanish Garden patterns.")
t("United Kingdom", "T. G. Green", "", "English maker of Cornishware.")

# Glass houses: (country, name, aliases, year, note, source, own, tier, own_y)
G = []
def g(c, n, y="", note="", s="", a="", own="", tier="", oy=""):
    G.append(dict(c=c, n=n, y=y, note=note, s=s, a=a, own=own, tier=tier, oy=oy))
CAT = "https://en.wikipedia.org/wiki/Category:Glassmaking_companies_of_"
g("Austria", "J. & L. Lobmeyr", "", "Viennese glass house listed under Austria.", CAT+"Austria")
g("Austria", "Riedel", "1756", "Family glassworks founded in Bohemia in 1756; the present company dates from 1956 at Kufstein.", W+"Riedel_(glass_manufacturer)", own="Riedel family (Tiroler Glashütte GmbH)", tier="Independent")
g("Austria", "Stölzle Glass", "", "Glass maker listed under Austria.", CAT+"Austria")
g("Austria", "Swarovski", "", "Crystal maker listed under Austria.", CAT+"Austria")
g("Austria", "Zalto", "", "Austrian maker of thin hand-blown glasses.", "https://www.zaltoglas.at/en/products/denkart/")
g("Czech Republic", "Moser", "1857", "Karlovy Vary glass house founded by Ludwig Moser in 1857.", W+"Moser_(glass_company)")
g("Czech Republic", "Crystalex", "", "Czech glass maker listed under the Czech Republic.", CAT+"the_Czech_Republic")
g("Czech Republic", "Nižbor glassworks", "", "Czech glassworks listed under the Czech Republic.", CAT+"the_Czech_Republic")
g("Czech Republic", "Preciosa", "", "Czech crystal maker listed under the Czech Republic.", CAT+"the_Czech_Republic")
g("Czech Republic", "SIN", "", "Czech glass brand listed under the Czech Republic.", CAT+"the_Czech_Republic")
g("Czech Republic", "Joh. Loetz Witwe", "", "Bohemian art-glass house listed in the general glassmaking category.", "https://en.wikipedia.org/wiki/Category:Glassmaking_companies")
g("Denmark", "Bodum", "", "Danish houseware maker listed under Denmark.", CAT+"Denmark")
g("Denmark", "Holmegaard", "", "Danish glassworks listed under Denmark.", CAT+"Denmark", a="Holmegaard Glass Factory")
g("Denmark", "Kastrup Glasværk", "", "Danish glassworks listed under Denmark and among defunct glassmakers.", CAT+"Denmark")
g("Finland", "Iittala", "1881", "Finnish glassworks founded 1881; Fiskars bought it in 2007.", W+"Iittala", own="Fiskars Corporation", tier="Global group", oy="2007")
g("Finland", "Riihimäki glass", "", "Finnish glassworks listed under Finland.", CAT+"Finland")
g("France", "Saint-Louis", "1586", "Glassworks founded in 1586; parent company Hermès International.", W+"Saint-Louis_(glass_manufacturer)", own="Hermès International", tier="Global group")
g("France", "Baccarat", "1764", "Glassworks licensed by Louis XV in 1764; a Hong Kong fund group took control in December 2020.", W+"Baccarat_(company)", own="Fortune Fountain Limited (Hong Kong funds)", tier="Independent", oy="2020")
g("France", "Lalique", "1888", "Glass house founded in Paris by René Lalique in 1888; owned by Art & Fragrance, now Lalique Group SA, since 2010.", W+"Lalique", own="Lalique Group SA (Silvio Denz)", tier="Independent", oy="2010")
g("France", "Arc", "", "French tableware glass group listed under France.", CAT+"France", a="Arc Holdings")
g("France", "Daum", "", "French crystal studio listed under France.", CAT+"France", a="Daum (studio)")
g("France", "Duralex", "1945", "French tempered-glass tableware maker founded 1945; International Cookware bought it in January 2021.", W+"Duralex", own="La Maison française du verre (formerly International Cookware Group)", tier="Independent", oy="2021")
g("France", "Edmond Etling", "", "French glass maker listed under France.", CAT+"France")
g("France", "La Rochère", "", "French glassworks listed under France.", CAT+"France")
g("France", "Vallérysthal", "", "Lorraine glassworks listed under France.", CAT+"France")
g("Germany", "Nachtmann", "", "German crystal maker listed under Germany.", CAT+"Germany", a="Nachtmann (glass manufacturer)")
g("Germany", "Zwiesel Kristallglas", "1872", "Bavarian Forest glassworks, sheet glass from 1872; sold under the Schott Zwiesel name from 1972 and bought out by management in 2001.", W+"Zwiesel_Kristallglas", a="Schott Zwiesel", own="Zwiesel Kristallglas AG", tier="Independent", oy="2001")
g("Germany", "Spiegelau", "", "", "")  # placeholder removed below
G.pop()
g("Hungary", "Ajka Crystal", "", "Hungarian crystal maker listed in the general glassmaking category.", "https://en.wikipedia.org/wiki/Category:Glassmaking_companies")
g("Ireland", "Waterford", "1947", "Irish crystal house; the Waterford Glassworks dated from 1783, and Fiskars completed its purchase on 2 July 2015.", W+"Waterford_Crystal", a="Waterford Crystal", own="Fiskars Corporation", tier="Global group", oy="2015")
g("Ireland", "Tipperary Crystal", "", "Irish crystal maker listed under Ireland.", CAT+"Ireland")
g("Italy", "Barovier & Toso", "", "Murano glassworks, one of the island's oldest.", W+"Murano_glass")
g("Italy", "Seguso", "1933", "Murano glassworks, Seguso Vetri d'Arte, founded 1933.", W+"Seguso")
g("Italy", "Venini", "", "Murano glassworks named in the Murano glass article.", W+"Murano_glass")
g("Italy", "Salviati", "", "Murano glassworks named in the Murano glass article.", W+"Murano_glass")
g("Italy", "Berengo Studio", "", "Murano glass studio named in the Murano glass article.", W+"Murano_glass")
g("Italy", "Pauly & C.", "", "Venetian glassmaker, Compagnia Venezia Murano.", W+"Murano_glass")
g("Italy", "De Biasi", "", "Murano glassworks named in the Murano glass article.", W+"Murano_glass")
g("Italy", "Gabbiani", "", "Murano glassworks named in the Murano glass article.", W+"Murano_glass")
g("Italy", "Formia International", "", "Murano glassworks named in the Murano glass article.", W+"Murano_glass")
g("Italy", "Simone Cenedese", "", "Murano glassworks named in the Murano glass article.", W+"Murano_glass")
g("Italy", "Mandruzzato", "", "Murano glassworks of the Mandruzzato family, named in the Murano glass article.", W+"Murano_glass", a="Alessandro Mandruzzato")
g("Italy", "Vetreria Ducale", "", "Murano glassworks named in the Murano glass article.", W+"Murano_glass")
g("Italy", "Estevan Rossetto 1950", "", "Murano glassworks named in the Murano glass article.", W+"Murano_glass")
g("Italy", "Antica Vetreria Fratelli Toso", "1854", "Murano glassworks dating from 1854.", W+"Murano_glass")
g("Italy", "Altare", "", "Ligurian glass tradition listed under Italy.", CAT+"Italy")
g("Italy", "Bormioli Rocco", "", "Italian glassmaker listed under Italy.", CAT+"Italy")
g("Italy", "Laguna B", "", "Italian glass studio listed under Italy.", CAT+"Italy", a="Laguna~B")
g("Netherlands", "Royal Leerdam", "", "Dutch crystal maker listed in the general glassmaking category.", "https://en.wikipedia.org/wiki/Category:Glassmaking_companies", a="Royal Leerdam Crystal")
g("Norway", "Hadeland Glassverk", "", "Norwegian glassworks listed under Norway.", CAT+"Norway")
g("Norway", "Magnor Glassverk", "", "Norwegian glassworks listed under Norway.", CAT+"Norway")
g("Norway", "Drammens Glassverk", "", "Norwegian glassworks listed under Norway.", CAT+"Norway")
g("Poland", "Krosno Glass", "", "Polish glassworks listed under Poland.", CAT+"Poland")
g("Russia", "Gus Crystal", "", "Russian crystal maker listed in the general glassmaking category.", "https://en.wikipedia.org/wiki/Category:Glassmaking_companies")
g("Spain", "Real Fábrica de Cristales de La Granja", "", "Spanish royal glass factory listed in the general glassmaking category.", "https://en.wikipedia.org/wiki/Category:Glassmaking_companies")
g("Sweden", "Orrefors", "1898", "Swedish glassworks founded 1898; it bought Kosta Boda in 1990 and the Orrefors works closed in 2012.", W+"Orrefors_Glassworks", a="Orrefors Glassworks")
g("Sweden", "Kosta Boda", "1742", "Swedish glassworks; Kosta Glasbruk was founded in 1742 and Orrefors bought it in 1990.", W+"Kosta_Boda", own="New Wave Group (Orrefors Kosta Boda)", tier="Independent", oy="2005")
g("Sweden", "Boda glasbruk", "", "Swedish glassworks listed under Sweden.", CAT+"Sweden")
g("Sweden", "Åseda Glasbruk", "", "Swedish glassworks listed under Sweden.", CAT+"Sweden")
g("Sweden", "Henrikstorps glasbruk", "", "Swedish glassworks listed under Sweden.", CAT+"Sweden")
g("Sweden", "Johansfors Glasbruk", "", "Swedish glassworks listed under Sweden.", CAT+"Sweden")
g("Sweden", "Kingdom of Crystal", "", "Swedish glass attraction group listed under Sweden.", CAT+"Sweden")
g("Sweden", "Limmareds glasbruk", "", "Swedish glassworks listed under Sweden.", CAT+"Sweden")
UKG = CAT+"the_United_Kingdom"
g("United Kingdom", "Caithness Glass", "", "Scottish glassworks listed under the United Kingdom.", UKG)
g("United Kingdom", "Dartington Crystal", "", "Devon crystal maker listed under the United Kingdom.", UKG)
g("United Kingdom", "Edinburgh Crystal", "", "Scottish crystal maker listed under the United Kingdom.", UKG)
g("United Kingdom", "Tyrone Crystal", "", "Northern Irish crystal maker listed under the United Kingdom and Ireland.", UKG)
g("United Kingdom", "Whitefriars Glass", "", "London glassworks listed among defunct glassmakers.", "https://en.wikipedia.org/wiki/List_of_defunct_glassmaking_companies")
g("United Kingdom", "Stevens & Williams", "", "Stourbridge glassworks listed among defunct glassmakers.", "https://en.wikipedia.org/wiki/List_of_defunct_glassmaking_companies")
g("United Kingdom", "Nailsea Glassworks", "", "Somerset glassworks listed among defunct glassmakers.", "https://en.wikipedia.org/wiki/List_of_defunct_glassmaking_companies")
g("United Kingdom", "Ravenhead Glass", "", "St Helens glassworks listed among defunct glassmakers.", "https://en.wikipedia.org/wiki/List_of_defunct_glassmaking_companies")
USG = CAT+"the_United_States"
DEF = "https://en.wikipedia.org/wiki/List_of_defunct_glassmaking_companies"
g("United States", "Steuben", "1903", "Corning glassworks founded 1903 by Frederick Carder and Thomas Hawkes; Corning bought it in 1918 and took the brand back in 2011.", W+"Steuben_Glass_Works", a="Steuben Glass Works", own="Corning Incorporated", tier="Independent", oy="2011")
g("United States", "Libbey", "1818", "Glassmaker descended from the New England Glass Company of 1818, independent since a 1993 spin-off from Owens-Illinois.", W+"Libbey_Incorporated", a="Libbey Incorporated", own="Libbey Incorporated", tier="Independent")
for n, note in [
    ("Anchor Hocking", "American glassware maker listed under the United States."),
    ("Bakewell Glass", "Pittsburgh glass maker listed under the United States."),
    ("Blenko Glass Company", "West Virginia art-glass maker listed under the United States."),
    ("Boston and Sandwich Glass Company", "Massachusetts glassworks listed under the United States."),
    ("Bryce Brothers", "Pennsylvania glass maker listed under the United States."),
    ("Cambridge Glass", "Ohio glassworks listed among defunct glassmakers."),
    ("Corelle Brands", "American tableware group listed under the United States."),
    ("Corning Glass Works", "American glassworks listed under the United States."),
    ("Dugan Glass Company", "Indiana pressed-glass maker listed under the United States."),
    ("Duncan & Miller Glass Company", "Pennsylvania glass maker listed under the United States."),
    ("Fenton Art Glass Company", "West Virginia art-glass maker listed under the United States."),
    ("Fostoria Glass Company", "American glass maker listed under the United States."),
    ("Hazel-Atlas Glass Company", "American glassworks listed under the United States."),
    ("Heisey Glass Company", "Ohio glassworks listed among defunct glassmakers."),
    ("Hobbs, Brockunier and Company", "West Virginia glassworks listed under the United States."),
    ("Indiana Glass Company", "Indiana glassworks listed under the United States."),
    ("Lancaster Glass Company", "Ohio glassworks listed under the United States."),
    ("Mosser Glass", "Ohio glassworks listed under the United States."),
    ("New England Glass Company", "Massachusetts glassworks listed among defunct glassmakers."),
    ("New Martinsville Glass Company", "West Virginia glassworks listed under the United States."),
    ("Northwood Glass Company", "American glassworks listed among defunct glassmakers."),
    ("Millersburg Glass Company", "Ohio glassworks listed among defunct glassmakers."),
    ("Pairpoint Glass", "Massachusetts glassworks listed under the United States."),
    ("Seneca Glass Company", "West Virginia glassworks listed under the United States."),
    ("Union Glass Company", "Massachusetts glassworks listed among defunct glassmakers."),
    ("United States Glass Company", "American glass combine listed under the United States."),
    ("Warsaw Cut Glass Company", "Indiana cut-glass maker listed under the United States."),
    ("Westmoreland Glass Company", "Pennsylvania glassworks listed under the United States."),
]:
    g("United States", n, "", note, USG)
