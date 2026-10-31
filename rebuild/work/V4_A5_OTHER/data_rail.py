# Railroad-grade canon from Rails West maker pages. Each entry: (maker, name, years, description, versions)
# version: (name, years, description)
RW = 'http://www.railswest.com/time/'
SRC = {
 'Hamilton': RW + 'hamilton.html', 'Waltham': RW + 'waltham.html', 'Elgin': 'https://mobile.railswest.com/time/elgin.html',
 'Illinois': RW + 'illinois.html', 'Rockford': RW + 'rockford.html', 'South Bend': RW + 'southbend.html',
 'Hampden': RW + 'hampden.html', 'Howard': RW + 'howard.html', 'Columbus': RW + 'columbus.html',
 'Aurora': RW + 'aurora.html', 'Peoria': RW + 'peoria.html', 'United States Watch Company': RW + 'uswatchmarion.html',
 'Ball': 'https://railswest.org/time/ball.html',
}
MK = {'Howard': 'E. Howard', 'United States Watch Company': 'United States Watch Company'}
E = []
def add(mk, n, y, d, v=()):
    E.append((mk, n, y, d, list(v)))

# Hamilton (hamilton.html)
add('Hamilton', '926 / 927', '1895–1923', '18-size, 17-jewel; 926 open face, 927 hunting case.', [('927', '1895–1912', 'hunting case')])
add('Hamilton', '934 / 935', '1894–1909', '18-size, 17-jewel; 934 open face, 935 hunting case.', [('935', '1894–1909', 'hunting case')])
add('Hamilton', '936 / 937', '1893–1915', '18-size, 17-jewel; 936 open face, 937 hunting case.', [('937', '1893–1914', 'hunting case')])
add('Hamilton', '938 / 939', '1894–1907', '18-size, 17-jewel; 938 open face, 939 hunting case.', [('939', '1894–1903', 'hunting case')])
add('Hamilton', '940', '1898–1928', '18-size, 21-jewel open-face grade.', [('941', '1898–1920', 'hunting case'), ('942', '1898–1914', 'open face'), ('943', '1898–1908', 'hunting case')])
add('Hamilton', '944', '1905–1906', '18-size, 19-jewel open-face grade.')
add('Hamilton', '946 / 947', '1904–1921', '18-size, 23-jewel; 946 open face, 947 hunting case.', [('947', '1910–1916', 'hunting case')])
add('Hamilton', '948', '1912–1920', '18-size, 17-jewel open-face grade.')
add('Hamilton', '950 / 950B', '1909–1968', '16-size, 23-jewel open-face top grade.', [('950', '1909–1941', ''), ('950B', '1941–1968', ''), ('950E', '', ''), ('951', '1913–1918', 'hunting case')])
add('Hamilton', '952', '1909–1924', '16-size, 19-jewel open-face grade.')
add('Hamilton', '954', '1910–1913', '16-size, 17-jewel open-face grade.')
add('Hamilton', '960 / 961', '1896–1915', '16-size, 21-jewel; 960 open face, 961 hunting case.', [('961', '', 'hunting case')])
add('Hamilton', '962 / 963', '1896–1897', '16-size, 17-jewel; 962 open face with pendant set, 963 hunting case.', [('963', '', 'hunting case')])
add('Hamilton', '964', '', '16-size, 17-jewel grade.')
add('Hamilton', '968', '', '16-size, 17-jewel grade.')
add('Hamilton', '970 / 971', '1901–1910', '16-size, 21-jewel; 970 open face, 971 hunting case.', [('971', '1901–1907', 'hunting case')])
add('Hamilton', '972 / 973', '1904–1924', '16-size, 17-jewel; 972 open face, 973 hunting case.', [('973', '1905–1914', 'hunting case')])
add('Hamilton', '974', '1897–1927', '16-size, 17-jewel open-face grade.', [('974 Special (Hamilton Traffic Special)', '1927–1939', '')])
add('Hamilton', '978', '1912–1924', '16-size, 17-jewel open-face grade with three positions.')
add('Hamilton', '990 / 991', '1903–1919', '16-size, 21-jewel; 990 open face, 991 hunting case.', [('991', '1905–1908', 'hunting case')])
add('Hamilton', '992 / 992B', '1903–1969', '16-size, 21-jewel open-face railroad grade; the 992B followed in 1940.', [('992', '1903–1940', ''), ('992E', '1936', ''), ('992B', '1940–1969', ''), ('993', '1905–1924', 'hunting case')])
add('Hamilton', '994', '1913–1920', '16-size, 21-jewel open-face grade.')
add('Hamilton', '996', '1915–1928', '16-size, 19-jewel open-face grade.')
add('Hamilton', '999', '', 'Grade made for the Ball Watch Co. and sold under that name.')

# Waltham (waltham.html)
add('Waltham', 'Appleton, Tracy & Co.', '1857–1902', 'Waltham grade name used on the Model 1857, 1877, 1883 and 1892 movements.', [('Model 1857', '1857', '18-size, 15 jewels; Pennsylvania Railroad order 1866'), ('Model 1877', '1877', '18-size, 15 jewels'), ('Model 1883', '', '15 and 17 jewels'), ('Model 1892', '', '18-size, 17 jewels, three positions; replaced 1902'), ('Premier', '1902', '18-size, 17 jewels, five positions')])
add('Waltham', 'Crescent Street', '1870–1929', 'Waltham railroad grade made on five movement models, 18-size then 16-size.', [('Model 1870', '1870–1883', '18-size, 15 jewels'), ('Model 1883', '1885', '15 and 17 jewels'), ('Model 1892', '', '18-size, 19 and 21 jewels; last 18-size made 1914'), ('Model 1899', '', '16-size, 19 and 21 jewels'), ('Model 1908', '–1929', '16-size, 17 to 21 jewels')])
add('Waltham', 'Riverside', '1872–1926', 'Waltham railroad grade made on five movement models.', [('Model 1872', '', '16-size, 15 jewels'), ('Model 1883', '', '15 and 17 jewels'), ('Model 1888', '', '16-size, 15 and 17 jewels'), ('Model 1892', '', '18-size, 17 jewels, three positions'), ('Model 1908', '–1926', '16-size, 17 and 19 jewels')])
add('Waltham', 'Riverside Maximus', '1888–1908', 'Waltham 16-size top grade of 21 and 23 jewels.', [('Model 1888', '', '16-size, 21 jewels'), ('Model 1899 and 1908', '', '16-size, 21 and 23 jewels')])
add('Waltham', 'Vanguard', '1894–1953', 'Waltham railroad grade of 17 to 23 jewels, 18-size then 16-size.', [('Model 1892', '1894', '18-size, 17, 19, 21 or 23 jewels'), ('Model 1899 and 1908', '', '16-size, 19 to 23 jewels'), ('Model 1623', '–1953', '16-size')])
add('Waltham', 'Premier Maximus', '', 'Waltham 16-size, 23-jewel grade named on the Webb Ball list.')
add('Waltham', 'Railroader', '', 'Waltham railroad grade on two models.', [('Model 1892', '', '18-size, 17 jewels, three positions'), ('Model 1888', '', '16-size, 17 jewels')])
add('Waltham', 'Royal', '', 'Waltham 16-size, 17-jewel grade.', [('Model 1888', '', '16-size, 17 jewels'), ('Model 1908', '–1922', '16-size, 17 jewels')])
add('Waltham', 'Special Railroad (Special RR King)', '', 'Waltham 18-size grade of 17 to 23 jewels named on the Webb Ball list.')
add('Waltham', 'Park Road', '', 'Waltham grade on the 1872 Model, 16-size.')
add('Waltham', 'American Watch Co.', '1872–1888', 'Grade named for the maker on the 1872 and 1888 models.', [('Model 1872', '', '16-size, 17 to 21 jewels'), ('Model 1888', '', '16-size, 21 jewels')])
add('Waltham', 'Waltham Watch Co.', '1879–1883', 'Grade named for the company on the 1879 and 1883 models, 15 jewels.')
add('Waltham', 'No. 25', '', 'Model 1883 numbered grade, 15 and 17 jewels.')
add('Waltham', 'No. 35', '', 'Model 1883 numbered grade, 15 and 17 jewels.')
add('Waltham', 'No. 45', '', 'Model 1883 numbered grade, 17 jewels.')
add('Waltham', 'No. 85', '', 'Model 1883 numbered grade, 17 jewels.')
add('Waltham', 'No. 87', '', 'Model 1883 numbered grade, 17 jewels.')
add('Waltham', 'No. 845', '', 'Model 1892 numbered grade, 18-size, 21 jewels.')
add('Waltham', 'No. 636', '1910–1913', 'Model 1908 numbered grade, 16-size, 17 jewels.')
add('Waltham', 'No. 637', '1910–1919', 'Model 1908 numbered grade, 16-size, 17 jewels.')
add('Waltham', 'No. 640', '1923–1926', 'Model 1908 numbered grade, 16-size, 17 jewels.')
add('Waltham', 'No. 642', '1918', 'Model 1908 numbered grade, 16-size, 17 jewels.')
add('Waltham', 'No. 645', '1906–1918', 'Model 1908 numbered grade, 16-size, 19 to 21 jewels.')
add('Waltham', 'No. 650', '', 'Model 1888 numbered grade, 16-size, 17 jewels.')

# Elgin (elgin.html)
add('Elgin', 'B.W. Raymond', '1867–1960', 'Elgin railroad grade from the 1867 18-size to the 1960 wristwatch.', [('Grade 69', '1867', '18-size, 15 jewels'), ('Stem-wind', '1873', '18-size'), ('Grade 240 (Model 8)', '1903–1909', '18-size, 19 jewels'), ('Grade 478', 'c. 1925', '16-size'), ('Grade 730A', '1960', 'first American-made wristwatch qualified for railroad service')])
add('Elgin', 'H.Z. Culver', '1867', 'Grade 62, 18-size, 15 jewels.')
add('Elgin', 'H.H. Taylor', '1867–1892', 'Grade 58, 18-size, 15 jewels; the 1892 catalogue listed it under several numbers.', [('Nos. 33, 76, 123, 124, 125, 126', '1892', '18-size, 15 jewels')])
add('Elgin', 'Veritas', '1903–1938', 'Elgin top railroad grade in 18-size and 16-size, 21 and 23 jewels.', [('No. 214', '1903', '18-size, 23 jewels'), ('No. 239', '1903', '18-size, 21 jewels'), ('Grade 375', 'c. 1911', '')])
add('Elgin', 'Father Time', '1903–1938', 'Elgin railroad grade, 21 jewels, in 18-size and 16-size.', [('Grade 454', 'c. 1920', '16-size')])
add('Elgin', 'Paillard Non-Magnetic', 'c. 1908', 'Elgin 16-size grade of 19 to 23 jewels on the 1908 railroad list.')
add('Elgin', 'No. 91', '1892', '16-size, 21 jewels.')
add('Elgin', 'No. 72', '1892', '16-size, 21 jewels.')
add('Elgin', 'No. 108 / 107', '1892', '16-size, 15 jewels.', [('No. 107', '1892', '')])
add('Elgin', 'No. 4 / 3', '1892', '16-size, 15 jewels.', [('No. 3', '1892', '')])
add('Elgin', 'No. 150 / 149', '1896–1903', '18-size, 21 jewels; 150 open face, 149 hunting.', [('No. 149', '1896–1903', 'hunting case')])
add('Elgin', 'No. 166 / 164', '1896', '18-size, 17 jewels.', [('No. 164', '1896', 'hunting case')])
add('Elgin', 'No. 165 / 163', '1896', '18-size, 17 jewels.', [('No. 163', '1896', 'hunting case')])
add('Elgin', 'No. 148 / 144', '1896', '18-size, 17 jewels.', [('No. 144', '1896', 'hunting case')])
add('Elgin', 'No. 147 / 143', '1896', '18-size, 17 jewels.', [('No. 143', '1896', 'hunting case')])
add('Elgin', 'No. 349', '1908–1914', '18-size, 17 to 21 jewels (seventh model).')
add('Elgin', 'No. 162 / 156', '1896–1908', '16-size, 21 jewels; 162 open face, 156 hunting.', [('No. 156', '1896–1903', 'hunting case')])
add('Elgin', 'No. 161 / 155', '1896–1903', '16-size, 17 jewels.', [('No. 155', '1896–1903', 'hunting case')])
add('Elgin', 'No. 160 / 154', '1896', '16-size, 17 jewels.', [('No. 154', '1896', 'hunting case')])
add('Elgin', 'No. 159 / 153', '1896', '16-size, 17 jewels.', [('No. 153', '1896', 'hunting case')])
add('Elgin', 'No. 246', '1903', '16-size, 17 jewels, open face.')
add('Elgin', 'No. 270', '1904–1938', '16-size, 21 jewels, open face; still on the 1938 Santa Fe list.')
add('Elgin', 'No. 280', '1904', '16-size, 17 jewels, open face.')
add('Elgin', 'No. 342', 'c. 1908', '16-size railroad grade, 17 to 21 jewels.')
add('Elgin', 'No. 571 / 572', 'c. 1908', '16-size; 571 has 21 jewels, 572 has 19.')

# Illinois (illinois.html)
add('Illinois', 'Stuart', '1872–1878', '18-size, 15-jewel adjusted railroad grade.')
add('Illinois', 'Bunn', '1878–1924', 'Illinois railroad grade, 18-size to 1915 then 16-size to 1924.', [('18-size', '–1915', '15, 17 then 19 jewels'), ('Models 8 and 9', '1914–1924', '16-size, 17 and 19 jewels')])
add('Illinois', 'Miller', '1878–1896', '18-size, 15-jewel adjusted railroad grade.')
add('Illinois', 'Bunn Special', '1895–1932', 'Illinois top railroad grade, 21 and 23 jewels, 18-size then 16-size.', [('18-size', '1895–1919', '21 and 24 jewels'), ('Models 8 and 9', '1914–1928', '16-size, 21 and 23 jewels, six positions'), ('Model 11', '1917', '23 jewels, 48-hour mainspring'), ('Model 14', '1924–1925', '21 and 23 jewels, 60-hour mainspring'), ('161-A and 163-A', 'c. 1932', 'renumbered grades')])
add('Illinois', 'A. Lincoln', '1907–1924', 'Illinois 21-jewel railroad grade.', [('18-size, Model 6', '1907–1916', ''), ('16-size, Model 5', '1907–1920', 'five positions'), ('16-size, Model 9', '1915–1924', 'five positions')])
add('Illinois', 'Sangamo', 'c. 1897–1913', 'Illinois 21- and 23-jewel six-position railroad grade.')
add('Illinois', 'Sangamo Special', '1913–1923', 'Illinois 16-size railroad grade of 19 to 23 jewels.', [('Models 8 and 9', '1913', '19, 21 and 23 jewels, six positions'), ('Model 10', '1917', '23 jewels, 48-hour mainspring'), ('Model 13', '1923', '23 jewels, 60-hour mainspring')])
add('Illinois', 'Burlington Special', '', 'Contract grade for the Burlington Watch Co., 19 jewels.')
add('Illinois', 'Burlington', '', 'Contract grade, 19 and 21 jewels.')
add('Illinois', 'Santa Fe Special', 'c. 1923', 'Contract grade for the Santa Fe Watch Co., 21 jewels, sold by mail order.')
add('Illinois', 'Paillard', '', 'Contract grade of 17 and 21 jewels.')
add('Illinois', 'Benjamin Franklin', '', 'Contract grade in 18-size (17 to 24 jewels) and 16-size (17 to 25 jewels).')
add('Illinois', 'Chesapeake & Ohio Special', '', 'Contract grade, 18-size, 21 to 24 jewels.')
add('Illinois', 'Interstate Chronometer', '', 'Contract grade, 18-size and 16-size, 23 jewels.')
add('Illinois', 'Lafayette', '', 'Contract grade, 24 jewels in 18-size and 23 in 16-size.')
add('Illinois', 'Trainsmen', '', 'Contract grade, 18-size, 23 jewels.')
add('Illinois', 'Pennsylvania Special', '', 'Contract grade, 18-size (17 to 26 jewels) and 16-size (17, 21 and 23).')
add('Illinois', 'Railroader / Railroad King', '', 'Contract grades in 18-size.')
add('Illinois', 'Diamond Ruby Sapphire', '', 'Contract grade, 16-size, 21 and 23 jewels.')
add('Illinois', 'Paillard Non-Magnetic', '', 'Contract grade, 16-size, 17 and 21 jewels.')
for n, y, d in [('No. 103, 104, 105', '1883', 'Model 2 (15 jewels) or Model 3 (17 jewels).'), ('No. 106', '1884–1887', 'Model 2 or 3.'), ('No. 107, 108', '1885–1887', 'Model 2 or 3.'), ('No. 5', '1888', 'Model 2 and 3 adjusted grade; later Models 4 and 6, 15 jewels.'),
        ('No. 116', '', '16-size, 15 to 21 jewels, three positions.'), ('No. 114', '', '16-size, 16 and 17 jewels, three positions.'), ('No. 115', '', '16-size, 15 jewels, three positions.'),
        ('No. 179', '1896–1898', '16-size, 21 jewels, six positions.'), ('No. 177', '1896–1897', '16-size, 17 jewels, six positions.'), ('No. 178', '1897–1898', '16-size, 17 jewels, six positions.'),
        ('No. 176', '1896–1913', '16-size, 17 to 21 jewels, four positions.'), ('No. 181', '1896', '16-size, 21 jewels, six positions.'), ('No. 189', '1897–1911', '16-size, 21 jewels, six positions.'),
        ('No. 187', '1898–1913', '16-size, 17 jewels, six positions.'), ('No. 186', '1898–1914', '16-size, 17 jewels, four positions.'), ('No. 185', '1898–1914', '16-size, 17 to 21 jewels.'),
        ('No. 770', '1913', 'Model 9, 16-size, 23 jewels, six positions.'), ('No. 709', '1914', 'Model 9, 16-size, 23 jewels.'), ('No. 710', '1912–1919', 'Model 9, 16-size, 23 jewels.'),
        ('No. 809', '1914–1930', 'Model 9, 16-size, 21 and 23 jewels.'), ('No. 106 (Model 9)', '1915–1917', '16-size, 19 jewels, five positions.'), ('No. 107 (Model 9)', '1917–1930', '16-size, 19 and 21 jewels.'),
        ('No. 108 (Model 9)', '1918–1922', '16-size, 21 jewels, five positions.'), ('No. 706', '1914–1929', 'Model 9, 16-size, 17 to 21 jewels.'), ('No. 707', '1920–1930', 'Model 9, 16-size, 19 jewels, three positions.')]:
    add('Illinois', n, y, d)

# Rockford (rockford.html)
for n, d in [('No. 950', '18-size, 21 jewels.'), ('No. 87', '18-size, 15 jewels.'), ('Grade 900', '18-size, marked RG from about 1898.'), ('Grade 905', '18-size.'), ('Grade 910', '18-size.'), ('Grade 912', '18-size.'), ('Grade 918', '18-size.'), ('Grade 945', '18-size.'), ('Grade 200', '18-size.'), ('Grade 205', '18-size.'),
             ('No. 505', '16-size, 21 jewels, double roller.'), ('No. 515', '16-size, 21 jewels, double roller.'), ('No. 525', '16-size, 21 jewels, double roller.'), ('No. 535', '16-size, 21 jewels, double roller.'), ('No. 545', '16-size, 21 jewels, double roller.'), ('No. 555', '16-size, 21 jewels, double roller.'),
             ('Winnebago', '16-size, 21 jewels, double roller.'), ('No. 655', '21 jewels, lever set.')]:
    add('Rockford', n, '1903' if n == 'No. 545' else ('c. 1891' if n == 'No. 87' else ''), d)

# South Bend (southbend.html)
add('South Bend', 'No. 292 / 293', '1905', '16-size, 19 jewels, Model 1; 292 hunting, 293 open face.', [('No. 292', '1905', 'hunting case'), ('No. 293', '1905', 'open face')])
add('South Bend', 'No. 294 / 295', '1905', '16-size, 21 jewels, Model 1; 294 hunting, 295 open face.', [('No. 294', '1905', 'hunting case'), ('No. 295', '1905', 'open face')])
add('South Bend', 'Studebaker', '1910–1911', 'South Bend named grade.', [('No. 329', '1910', '18-size, 21 jewels, open face'), ('No. 229', '1911', '16-size, 21 jewels, Model 2')])
add('South Bend', 'No. 323', '1910', '18-size, 21 jewels, open face.')
add('South Bend', 'No. 327', '', '18-size, 21 jewels.')
add('South Bend', 'No. 223', '1911', '16-size, 17 jewels, Model 2.')
add('South Bend', 'No. 227', '', '16-size, 21 jewels.')
add('South Bend', 'No. 299', '', '16-size grade.')
add('South Bend', 'Polaris', '', 'Named grade of 21 jewels.')

# Hampden (hampden.html)
add('Hampden', 'Railway', '1883–1891', 'Hampden grade, 15 jewels in 18-size and 19 in 16-size.', [('Model 2', 'c. 1883', '18-size, 15 jewels, hunting case'), ('18-size', '1891', '15 jewels, open face'), ('Model 4', '1902', '16-size, 19 jewels')])
add('Hampden', 'Special Railway', '1891–1920', 'Hampden grade of 17 to 23 jewels.', [('18-size', '1891', '17 jewels'), ('18-size', '1896', '23 jewels'), ('18-size', '1900', '21 jewels'), ('Model 5', 'c. 1920', '16-size, 23 jewels')])
add('Hampden', 'New Railway', '1891', 'Hampden grade, 17 jewels in 18-size, later 23; 21 in 16-size.')
add('Hampden', 'John Hancock', '', 'Hampden 18-size grade, 21 and 23 jewels.')
add('Hampden', 'North American Railway', '', 'Hampden 18-size, 21-jewel grade.')
add('Hampden', 'Wm. McKinley', '', 'Hampden grade, 21 jewels in 18-size and 16-size.')
add('Hampden', 'John C. Dueber', '', 'Hampden 21-jewel grade in 18-size and 16-size.')
add('Hampden', 'J.C. Perry', '', 'Hampden 18-size, 15-jewel grade.')
add('Hampden', 'No. 60', 'c. 1884', 'Model 3, 18-size, 15 jewels, open face.')
add('Hampden', 'No. 104', '', '16-size, 23 jewels (Models 2 and 4).')
add('Hampden', 'No. 105', '', '16-size, 21 to 23 jewels (Models 2, 4 and 5).')

# E. Howard (howard.html)
add('Howard', 'Series VII / VIII (Ball model)', '1893', 'Private-label Ball model, N size, 17 jewels; VII hunting case, VIII open face.', [('Series VII', '1893', 'hunting case'), ('Series VIII', '1893', 'open face')])
add('Howard', 'Series VII / VIII (split plate)', '1894–1895', 'N size, 17 jewels.', [('Series VII', '1894', 'hunting case'), ('Series VIII', '1895', 'open face')])
add('Howard', 'Series XI / XII', '1895', 'Split-plate L (16) size, 17 jewels; XI hunting case, XII open face.', [('Series XI', '1895', 'hunting case'), ('Series XII', '1895', 'open face')])
add('Howard', 'Keystone-Howard 16S', 'after 1903', '16-size in 19, 21 and 23 jewels.')

# Columbus
for n, y, d in [('No. 18 / 99', '', '18-size, 16 jewels; 18 hunting, 99 open face.'), ('No. 28 / 98', '', '18-size, 16 jewels; 28 hunting, 98 open face.'), ('No. 27 / 97', '1887', '18-size; 27 hunting, 97 open face.'), ('No. 35', '', '15 jewels, hunting case.'),
                ('Railway King', 'c. 1889–1899', '18-size; first version 16 jewels, later 17 to 25.'), ('R.W.K. Special', '1892', '18-size, 15 jewels.'), ('No. 47 / 87', '1889', '16-size, 16 jewels; 47 hunting, 87 open face.'),
                ('No. 48', '', '16-size, 16 jewels, hunting case.'), ('No. 46 / 86', '', '16-size, 15 jewels; 46 hunting, 86 open face.'), ('Time King', '1894', '18-size, 21 jewels.'), ('Ruby', '1895', '16-size, 21 jewels.'), ('Columbus King', 'late 1890s', '18-size, 17 to 25 jewels.')]:
    add('Columbus', n, y, d)
# Aurora
add('Aurora', 'No. 10, 11, 12, 8 and 6', '1887', '18-size full-plate quick-train railroad grades, 15 jewels, adjusted.')
add('Aurora', 'Guild grades No. 50 to 53', '1887', 'Marked "Expressly for the Guild", 15 jewels, adjusted; some used in railroad service.')
# Peoria
add('Peoria', 'Peoria railway grades A to J', '1885–1892', 'Nine 18-size, 15-jewel adjusted grades (A, B, H, BB, I, C, G, E, J); the company closed in 1891–92.')
add('Peoria', 'Non-Magnetic Watch Co. of America grades', '1889–1892', 'Peoria-made 18-size, 15-jewel grades Nos. 43, 45, 47 and A.A. Extra, A, B, C.')
# United States Watch Co.
add('United States Watch Company', 'United States Watch Co. railroad grades', '1869–1873', 'Marion, Illinois makers: 18-size Models 1 and 2 and 16-size Model 3 of 15 to 19 jewels.', [('A. H. Wallis', '1869', ''), ('Frederic Atherton & Co.', '1867', 'first watch shipped June 1867'), ('Henry Randel', '1870', ''), ('Fayette Stratton', '', ''), ('Wm Alexander', '', ''), ('Marion Watch Co.', '', ''), ('S. M. Beard', '', ''), ('John W. Lewis', '', '')])
add('United States Watch Company', 'No. 40 / 42 (Waltham)', '1888–1889', '18-size Model 1 hunting-case, lever-set, 15 rubies in gold settings.')
add('United States Watch Company', 'No. 79 / 80 (Waltham)', '1893', 'Open face, 17 rubies.')
add('United States Watch Company', 'The President', '1894', '17 jewels, hunting case and open face, later 21-jewel open face.')
# Ball
add('Ball', 'Official Railroad Standard', '1890s–1990s', 'Ball-branded railroad pocket watches built to Webb C. Ball standards by other makers.', [('Ball\'s Standard Railroad Watch 18-size', '1890', 'Dueber-Hampden'), ('999H', '1904', 'made by Hamilton'), ('Trainmaster', '1959', 'Swiss wristwatch, 21 jewels')])
