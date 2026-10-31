import json
W='https://en.wikipedia.org/wiki/'
T=W+'T-shirt'
rows=[
('Katharine Hamnett','Designer','Designer who pioneered outsize T-shirts with large-print slogans in the early 1980s.',W+'T-shirt'),
('Global Hypercolour','Streetwear','Colour-change T-shirt brand that was one of the most popular youth brands in the US and UK in the 1980s.',W+'T-shirt'),
('Kamehameha','Heritage & workwear','Aloha shirt manufacturer founded in 1936.',W+'Aloha_shirt'),
('King-Smith Clothiers and Dry Goods','Heritage & workwear','Honolulu clothier whose Ellery Chun registered "aloha sportswear" as a trademark in 1936.',W+'Aloha_shirt'),
('Musa-Shiya the Shirtmaker','Heritage & workwear','Honolulu shirtmaker under Kōichirō Miyamoto, said to have made shirts from Japanese prints.',W+'Aloha_shirt'),
('Shaheen','Heritage & workwear','Aloha shirt manufacturer that began business in 1948.',W+'Aloha_shirt'),
('Annichen Sibbern','Specialist','Norwegian designer who published the yoke-sweater design in the magazine URD in 1930.',W+'Lopapeysa'),
("Hudson's Bay Company",'High street','Retailer that revealed a clothing line for the 2010 Vancouver Winter Olympics in 2009.',W+'Cowichan_sweater'),
('Adrian Nyman','Designer','Label for which Damien Hirst designed the Butterfly Hoodie in 2008.',W+'Hoodie'),
('Sonja de Lennart','Designer','Designer who introduced capri pants in 1948.',W+'Capri_pants'),
('H.A. & E. Smiths','Heritage & workwear','Bermudian firm that improved the design of Bermuda shorts after the war.',W+'Bermuda_shorts'),
('Nathaniel Coxon','Specialist','Bermudian tea shop owner credited with hemming uniform pants into Bermuda shorts in 1914.',W+'Bermuda_shorts'),
('Trimingham Bros.','Heritage & workwear','Bermudian firm that improved the design of Bermuda shorts after the war.',W+'Bermuda_shorts'),
('Dorothée Bis','Designer','French ready-to-wear company whose fashions gave hot pants their name, per Women\'s Wear Daily.',W+'Hot_pants'),
('Sanko Group','Specialist','Owner of the registered brand name Jeggings.',W+'Leggings'),
('Juli Lynne Charlot','Designer','Designer of the poodle skirt in 1947.',W+'Poodle_skirt'),
('Emanuel Ungaro','Designer','Designer whose late-1980s minis were likened to 1950s bathing suits.',W+'Miniskirt'),
('John Bates','Designer','British designer called the first to offer fashionable miniskirts, in 1965.',W+'Miniskirt'),
('Jacques Tiffeau','Designer','Designer who showed above-the-knee lengths in the US in the mid-1960s.',W+'Miniskirt'),
('Rudi Gernreich','Designer','American designer among the first to offer miniskirts, in 1967.',W+'Miniskirt'),
('Eugene Lami','Specialist','Designer of the tutu worn by Marie Taglioni in La Sylphide in 1832.',W+'Tutu_(clothing)'),
('Hippolyte Lecomte','Specialist','Designer of the basic silhouette of the Romantic tutu in 1827.',W+'Tutu_(clothing)'),
('Cecil Beaton','Specialist','Designer named among those who have designed tutus.',W+'Tutu_(clothing)'),
('Barbara Karinska','Specialist','Costumier who designed and made tutus.',W+'Tutu_(clothing)'),
('Isaac Mizrahi','Designer','American designer named among those who have designed tutus.',W+'Tutu_(clothing)'),
('Nicolas Ghesquière','Designer','Designer who tried to bring the jumpsuit back in 2002.',W+'Jumpsuit'),
('Bonnie Cashin','Designer','American designer who made evening jumpsuits from the 1950s.',W+'Jumpsuit'),
('Vera Maxwell','Designer','American designer of sporty jumpsuits in the mid-1940s.',W+'Jumpsuit'),
]
out=[]
for n,seg,d,s in rows:
    out.append({'n':n,'seg':seg,'d':d,'s':s,'kf':'','c':'','f':'','lines':[],'sig':[],'rel':[],'eras':[],'sc':[]})
json.dump(out,open('brands_new.json','w'),ensure_ascii=False)
nb=json.load(open('newbrands.json'))['new']

