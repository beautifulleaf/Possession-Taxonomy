import json,os,collections
P='/home/user/Possession-Taxonomy/rebuild/out/J8.json'
d=json.load(open(P))
kinds={k['n']:k for dp in d['depts'] for s in dp['s'] for k in s['k']}
tier={}
for k in kinds.values():
  for e in k.get('x',[]):
    if e.get('own') and e.get('tier'): tier.setdefault(e['own'],collections.Counter())[e['tier']]+=1
def W(t): return 'https://en.wikipedia.org/wiki/'+t.replace(' ','_')
LC='https://en.wikipedia.org/wiki/List_of_confectionery_brands'
LI='https://en.wikipedia.org/wiki/List_of_ice_cream_brands'
LB='https://en.wikipedia.org/wiki/List_of_brand_name_breads'
LF='https://en.wikipedia.org/wiki/List_of_brand_name_food_products'
# (kind, name, page, own, cty, y, d)
R=[
('Gummy & jelly sweet',"Allen's","Allen's",'Nestlé','Australia','',"Australian confectionery brand, formerly A. W. Allen Limited, made by Nestlé and the top sugar confectionery brand in Australia."),
('Mint & pastille','Minties','Minties','Nestlé','Australia','',"Hard, chewy, mint-flavoured confection made in Australia and New Zealand; listed under Allen's."),
('Toffee & caramel','Fantales',"Fantales",'Nestlé','Australia','',"Caramel sweet listed under Allen's on the List of confectionery brands."),
('Gummy & jelly sweet','Jelly Babies','Jelly Babies',"Bassett's",'England','',"Soft sugar jelly sweets shaped like plump babies, first made in Lancashire in the 19th century."),
('Hard candy & boiled sweet',"Brach's","Brach's",'Ferrero','United States','',"Candy and sweets brand of the Ferrara Candy Company, which the List of confectionery brands places under Ferrero."),
('Hard candy & boiled sweet','Bobs Candies','Bobs Candies','Ferrero','United States','',"Candy-cane brand made by the Ferrara Candy Company."),
('Sherbet & sour sweets','Fun Dip','Fun Dip','Ferrero','United States','',"Powdered candy with a candy stick, made by the Ferrara Candy Company."),
('Toffee & caramel','Now and Later','Now and Later','Ferrero','United States','',"Fruit-flavoured taffy-like candy made by the Ferrara Candy Company."),
('Chewing gum','Super Bubble','Super Bubble','Ferrero','United States','1946',"Bubble gum from the Ferrara Candy Company, first introduced in Memphis in 1946."),
('Countline','100 Grand Bar','100 Grand Bar','Ferrero','United States','1964',"Candy bar created in 1964 by Nestlé as the $100,000 Candy Bar; now a Ferrero (Ferrara) bar."),
('Liquorice','Darrell Lea','Darrell Lea','Darrell Lea','Australia','',"Australian maker of chocolate, liquorice and other confectionery, headquartered in Ingleburn, Sydney."),
('Chocolate-coated nuts & fruit','FruChocs','FruChocs','Menz Confectionery','Australia','',"Dried apricot and peach paste coated in milk chocolate, made by Menz Confectionery in South Australia."),
('Praline & filled bonbon','Ferrero Rocher','Ferrero Rocher','Ferrero','Italy','1979',"Hazelnut chocolate confection created by Michele Ferrero in 1979, each ball foil-wrapped."),
('Chocolate Easter egg','Kinder Surprise','Kinder Surprise','Ferrero','Italy','1974',"Milk chocolate egg containing a small toy in a plastic capsule, made by Ferrero since 1974."),
('Countline','Heath bar','Heath bar','The Hershey Company','United States','1928',"Toffee, almond and milk chocolate bar first made in 1928 by Heath Brothers Confectionery; made by Hershey since 1996."),
('Milk chocolate bar',"Hershey's Kisses","Hershey's Kisses",'The Hershey Company','United States','1907',"Bite-sized conical chocolates first produced by Hershey in 1907."),
('Toffee & caramel','Hopje','Hopje','','Netherlands','18th century',"Dutch coffee and caramel sweets named after Baron Hendrik Hop."),
('Gummy & jelly sweet','Hot Tamales','Hot Tamales','Just Born','United States','1950',"Cinnamon-flavoured candies made by Just Born, introduced in 1950."),
('Gummy & jelly sweet','Mike and Ike','Mike and Ike','Just Born','United States','1940',"Fruit-flavoured candies introduced in 1940 and made by Just Born."),
('Fruit snack','Joray Fruit Rolls','Joray Fruit Rolls','Joseph Shalhoub & Son','United States','',"Apricot-based fruit snack made in New York City since the 1970s."),
('Mint & pastille',"Grether's Pastilles","Grether's Pastilles",'','Switzerland','',"Glycerin-based soft pastilles made in Altnau since 1974; formerly Allenbury's Pastilles."),
('Hard candy & boiled sweet','Nerds','Nerds (candy)','','United States','1982',"Candy launched in 1982 by the Sunmark Corporation under the Willy Wonka brand."),
('Hard candy & boiled sweet','Bottle Caps','Bottle Caps (candy)','','United States','',"Sweet tablet candies made to look like metal soda bottle caps."),
('Toffee & caramel','Munchies','Munchies (confectionery)','Nestlé','United Kingdom','',"Confectionery introduced by a British firm and produced by Nestlé."),
('Novelty sweets','Nik-L-Nip','Nik-L-Nip','','United States','',"Fruit-flavoured confectionery created in the early 20th century."),
('Sherbet & sour sweets','Pixy Stix','Pixy Stix','','United States','',"Sweet and sour coloured powdered candy in a paper straw."),
('Chewing gum','Rain-Blo','Rain-Blo','','United States','',"American bubble gum in fruit flavours, introduced by Leaf."),
('Lollipop','Ring Pop','Ring Pop','','United States','',"Fruit-flavoured lollipop marketed as a wearable plastic ring."),
('Mint & pastille','Polo','Polo (confectionery)','Nestlé','United Kingdom','',"Breath mint whose defining feature is the hole in the middle."),
('Chocolate-coated nuts & fruit','Poppets','Poppets (sweets)','Valeo','United Kingdom','',"Chocolate-coated confectionery, formerly Paynes Poppets, manufactured by Valeo."),
('Gummy & jelly sweet','Red Ripperz','Red Ripperz','','','',"Red raspberry-flavoured chewy confectionery, formerly Redskins."),
('Gummy & jelly sweet',"Rowntree's Fruit Gums","Rowntree's Fruit Gums",'Nestlé','United Kingdom','',"Circular fruit-gum sweets in five flavours, formerly made by Rowntree's."),
('Gummy & jelly sweet',"Rowntree's Randoms","Rowntree's Randoms",'Nestlé','United Kingdom','2009',"Jelly sweet launched in the UK on 18 May 2009 under the Rowntree's brand."),
('Novelty sweets','Sixlets','Sixlets','Ganong Bros.','Canada','',"Small candy-coated chocolate-flavoured sweets, made at Ganong's St. Stephen factory."),
('Countline','Spira','Spira (confectionery)','Mondelēz International','United Kingdom','1980s',"Hollow twisted milk chocolate spiral by Cadbury, first sold in England in the mid-1980s."),
('Lollipop','Sugar Daddy','Sugar Daddy (candy)','Tootsie Roll Industries','United States','',"Firm caramel sucker made by Tootsie Roll Industries."),
('Lollipop','Caramel Apple Pops','Caramel Apple Pops','Tootsie Roll Industries','United States','',"Green apple hard candy coated in caramel on a stick."),
('Praline & filled bonbon','Andes Chocolate Mints','Andes chocolate mints','Tootsie Roll Industries','United States','',"Small rectangular mints with a mint-green layer between two chocolate layers."),
('Novelty sweets','Sweethearts','Sweethearts (candy)','','United States','',"Small heart-shaped sugar candies sold around Valentine's Day, printed with short messages."),
('Sherbet & sour sweets',"Tart 'n' Tinys","Tart 'n' Tinys",'Leaf Brands','United States','',"Small fruit-flavoured candies, originally made by Wonka."),
('Flavoured & inclusion bar',"Terry's Chocolate Orange","Terry's Chocolate Orange",'','England','1932',"Orange-flavoured chocolate created by Terry's in York in 1932; production moved to Poland in 2005."),
('Milk chocolate bar',"Tony's Chocolonely","Tony's Chocolonely","Tony's Chocolonely",'Netherlands','2005',"Dutch chocolate maker founded in 2005 by Teun van de Keuken to protest child exploitation in the chocolate industry."),
('Single-origin dark chocolate','TCHO','TCHO','TCHO','United States','',"Plant-based chocolate maker in Berkeley, California, working with cacao farmers and cooperatives."),
('Chocolate box assortment','Ganong Bros.','Ganong Bros.','Ganong Bros.','Canada','',"Canadian chocolate and confectionery company based in St. Stephen, New Brunswick."),
]
IC=[
('Ice cream tub','Bassetts Ice Cream','Bassetts Ice Cream','Bassetts','United States','1861',"Founded in 1861 by Lewis Dubois Bassett in Salem, New Jersey; the oldest continuously operating ice cream company in the US."),
('Ice cream tub','Fieldbrook Farms','Fieldbrook Farms','Wells Enterprises','United States','',"Private-label ice cream and frozen dessert maker in Dunkirk, New York; Wells Enterprises acquired it in April 2019."),
('Ice cream tub','Golden North','Golden North','Golden North','Australia','1923',"Ice cream maker headquartered in Laura, South Australia, in business since 1923."),
('Stick bar & choc ice','Good Humor','Good Humor','The Magnum Ice Cream Company','United States','',"Good Humor-Breyers brand started by Harry Burt in Youngstown, Ohio, in the early 1920s, known for its chocolate-coated ice cream bar on a stick."),
('Ice cream tub','HB Ice Cream','HB Ice Cream','The Magnum Ice Cream Company','Ireland','',"Irish ice cream brand, originally Hughes Brothers and Hazelbrook Farm, part of The Magnum Ice Cream Company."),
('Ice cream tub','Hennig-Olsen','Hennig-Olsen Iskremfabrikk','Hennig-Olsen','Norway','',"Family-owned ice cream factory in Kristiansand producing more than 20 types of ice cream."),
('Ice cream tub',"Hershey's Ice Cream",'Hershey Creamery Company','Hershey Creamery Company','United States','1894',"Creamery founded in 1894 by Jacob Hershey and his brothers; makes ice cream, sorbet and frozen yogurt."),
('Ice cream tub','Jack and Jill Ice Cream','Jack and Jill Ice Cream','Jack and Jill','United States','1929',"Founded by Max Schwartz in 1929 in Philadelphia."),
('Ice cream tub','Kawartha Dairy','Kawartha Dairy Company','Kawartha Dairy Company','Canada','1937',"Canadian family-owned dairy in Bobcaygeon, Ontario, founded in 1937."),
('Ice cream tub','Nandini','Karnataka Milk Federation','Karnataka Milk Federation','India','',"Brand under which the government-owned Karnataka dairy cooperative sells ice cream and other dairy products."),
('Ice cream tub','Mauds Ice Creams','Mauds Ice Creams','Mauds','Northern Ireland','',"Northern Ireland ice cream manufacturer with over 350 flavours in 44 years; best known for Poor Bear."),
('Ice cream tub','Mayfield Dairy','Mayfield Dairy','Mayfield Dairy Farms','United States','',"Dairy company in Athens, Tennessee, owned by Dean Foods from 1990 to 2020."),
('Ice cream tub','Milky Mist','Milky Mist Dairy','Milky Mist Dairy','India','1997',"Dairy manufacturer in Perundurai, Tamil Nadu, formed in 1997 by T. Sathish Kumar."),
('Ice cream tub',"Murphy's Ice Cream","Murphys Ice Cream","Murphy's Ice Cream",'Ireland','',"Irish food company in Dingle, County Kerry, using Kerry cattle milk."),
('Ice cream tub','Neilson Dairy','Neilson Dairy','Saputo','Canada','',"Canadian dairy company based in Toronto and owned by Saputo."),
('Ice cream tub',"Perry's Ice Cream","Perry's Ice Cream","Perry's Ice Cream",'United States','',"Ice cream manufacturer in Akron, New York, selling in the north-eastern US."),
('Ice cream tub','Purity Dairies','Purity Dairies','Purity Dairies','United States','',"Nashville dairy company run by the Ezell family, formerly Ezell's Dairy."),
('Ice cream tub','Sealtest','Sealtest Dairy','The Magnum Ice Cream Company','United States','',"Good Humor-Breyers dairy brand, formerly a division of National Dairy Products Corporation."),
('Ice cream tub','Snugburys','Snugburys','Snugburys','England','',"Ice cream maker at Park Farm, Hurleston, near Nantwich, making over 35 flavours."),
('Ice cream tub','Straus Family Creamery','Straus Family Creamery','Straus Family Creamery','United States','',"Organic dairy in Marshall, California, making milk, butter, cheese, ice cream and yogurt."),
('Ice cream tub','Swisslion','Swisslion Group','Swisslion Group','Serbia','',"Serbian food and drink manufacturer in Novi Sad with factories in four Balkan countries."),
('Ice cream tub','Thrifty Ice Cream','Thrifty Ice Cream','Thrifty','United States','1940',"Ice cream, frozen yogurt and sherbet founded in 1940 by Harry and Robert Borun for Thrifty Drug Stores."),
('Ice cream tub','Colonial Ice Cream','Colonial Ice Cream','Colonial Ice Cream','United States','',"Ice cream brand made by Colonial Ice Cream, Inc., of St. Charles, Illinois."),
('Ice cream tub',"Ben & Jerry's","Ben & Jerry's","Ben & Jerry's Homemade Holdings",'United States','',"American company making ice cream, frozen yogurt and sorbet."),
('Ice cream tub','Kibon','Kibon','The Magnum Ice Cream Company','Brazil','',"Brazilian ice cream producer, now owned by The Magnum Ice Cream Company."),
('Ice lolly','Paddle Pop','Paddle Pop','The Magnum Ice Cream Company','Australia','',"Ice confection brand originally created by Streets, sold in Australia, New Zealand and a few other countries."),
]
BR=[
('Sliced & tin loaf','Wonder Bread','Wonder Bread','Flowers Foods','United States','1921',"Sliced bread brand established in Indianapolis in 1921; one of the first to sell sliced bread nationwide."),
('Sliced & tin loaf','Sunbeam Bread','Sunbeam Bread','Quality Bakers of America','United States','',"Franchised white bread and roll brand owned by the Quality Bakers of America cooperative."),
('Sliced & tin loaf','Tip Top','Tip Top Bakeries','Associated British Foods','Australia','',"Australian bread manufacturer owned by George Weston Foods, a subsidiary of Associated British Foods."),
('Enriched bread',"King's Hawaiian","King's Hawaiian","King's Hawaiian",'United States','1950',"Family-owned bakery known for Hawaiian bread, founded by Robert Taira in Hilo in 1950."),
('Bagel & rolls',"Lender's Bagels","Lender's Bagels","Lender's Bagels",'United States','1927',"Brand that pioneered pre-packaged bagels in the US, established by the Lender family in New Haven in 1927."),
('Bagel & rolls','Davidovich Bagels','Davidovich Bagels','Davidovich Bakery','United States','',"Bagel brand of a New York City wholesale bakery, hand-rolled."),
('Rye & wholegrain bread','Polarbröd','Polarbröd','Polarbröd','Sweden','',"Swedish bread company with its head office in Älvsbyn."),
('Sliced & tin loaf','Wibs','Wibs','Western India Baker\'s Association','India','1973',"Bread brand originating in Mumbai in 1973, favoured by local sandwich makers."),
('Sliced & tin loaf',"Nature's Pride","Nature's Pride",'Flowers Foods','United States','',"All-natural bread brand made by Flowers Foods."),
('Rye & wholegrain bread','Alvarado Street Bakery','Alvarado Street Bakery','Alvarado Street Bakery','United States','',"Worker-owned bakery in Petaluma, California, making certified organic whole grain breads and bagels."),
('Sliced & tin loaf','Bond Bread','Bond Bread','General Baking Company','United States','',"Bread product of the General Baking Company."),
('Sliced & tin loaf','Holsum Bread','Holsum Bread','Holsum','United States','',"Packaged sliced white bread brand used by many independent bakeries by the early 1900s."),
('Sliced & tin loaf',"Bost's Bread","Bost's Bread","Bost's Bread",'United States','',"Bread brand distributed in the western Carolinas, Virginia and Tennessee."),
('Loaf & Bundt cake',"Entenmann's","Entenmann's",'Grupo Bimbo','United States','',"US baked goods maker, now owned by Grupo Bimbo."),
]
SN=[
('Popcorn','Act II','Act II (popcorn)','Conagra Brands','United States','',"Microwave popcorn brand modelled on cinema popcorn, made by Conagra Brands."),
('Popcorn','Jiffy Pop','Jiffy Pop','Conagra Brands','United States','',"Popcorn in a disposable foil-covered pan, owned by Conagra Brands."),
('Popcorn',"Crunch 'n Munch","Crunch 'n Munch",'Conagra Brands','United States','',"Caramel-coated popcorn and peanut snack."),
('Popcorn','Fiddle Faddle','Fiddle Faddle','Conagra Brands','United States','1967',"Caramel popcorn introduced in 1967."),
('Popcorn','Poppycock','Poppycock (snack)','','United States','',"Candied popcorn with almonds and pecans in a candy glaze."),
('Extruded corn snack',"Andy Capp's","Andy Capp's",'','United States','1971',"Corn and potato snack shaped like french fries, created by GoodMark Foods in 1971."),
('Extruded corn snack','Cheezies','Cheezies','W. T. Hawkins','Canada','',"Cheese puffs of extruded cornmeal coated in powdered cheddar."),
('Extruded corn snack',"Pirate's Booty","Pirate's Booty",'B&G Foods','United States','1987',"Puffed corn and rice snack developed in 1987 by Robert Ehrlich; B&G Foods bought the company in 2013."),
('Potato crisps','Golden Wonder','Golden Wonder','Golden Wonder','United Kingdom','',"British snack company best known for crisps."),
('Potato crisps','San Nicasio','San Nicasio','San Nicasio','Spain','1999',"Spanish gourmet potato chips, slow-cooked, established in 1999."),
('Wholegrain & woven wheat cracker','Twiglets','Twiglets','','United Kingdom','',"Wheat-based snack with a knobbly twig shape and a yeast-extract coating."),
('Crispbread','Ry-Krisp','Ry-Krisp','','United States','1899',"Rye crisp bread brand introduced in 1899 in Minneapolis."),
('Energy & sports bar','Space Food Sticks','Space Food Sticks','Pillsbury','United States','',"Snack sticks created in the late 1960s for Pillsbury by its food technologist Howard Bauman."),
('Roasted & salted nuts','David Sunflower Seeds','David Sunflower Seeds','Conagra Brands','United States','',"Roasted, salted sunflower seeds produced by ConAgra Foods."),
('Roasted & salted nuts',"Nobby's","Nobby's",'PepsiCo','Australia','',"Australia's largest nuts brand, made by The Smith's Snackfood Company, the Australian snacks division of PepsiCo."),
]
def tr(own):
    c=tier.get(own)
    if c:
        t=c.most_common(1)[0][0]
        return t
    return 'Independent'
def src(page,kind):
    return {'c':LC,'i':LI,'b':LB,'s':LF}[kind]
added=collections.Counter()
for lst,sk in ((R,'c'),(IC,'i'),(BR,'b'),(SN,'s')):
  for kind,n,page,own,cty,y,dd in lst:
    k=kinds[kind]
    if 'x' not in k:
        print('NOX',kind); k['x']=[]; k['nl']='One entry is a brand sold under its own name; flavours, sizes and formats are versions.'; k['xg']='by owner group, then tier'; k['sel']='Brands placed from the fetched Wikipedia brand lists cited on each entry. No complete list exists; follows the Wikipedia brand lists cited on each entry.'
    have={e['n'].lower() for e in k['x']}
    if n.lower() in have: continue
    t=tr(own) if own else 'Independent'
    o=own or n
    e={"n":n,"a":"","d":dd,"mk":o,"y":y,"s":W(page),"v":[],"own":o,"tier":t,"cty":cty}
    e["g"]=o if t=='Global group' else t
    k['x'].append(e); added[kind]+=1
print(sum(added.values()),dict(added))
json.dump(d,open(P+'.tmp','w'),ensure_ascii=False,indent=1); os.replace(P+'.tmp',P)
