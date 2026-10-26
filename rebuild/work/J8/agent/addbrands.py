import json, os, sys
D = '/home/user/Possession-Taxonomy/rebuild/work/J8/shelves/'
def B(n, c='', f='', seg='', d='', sig=(), rel=(), lines=()):
    b = {"n": n}
    if c: b["c"] = c
    if f: b["f"] = f
    if seg: b["seg"] = seg
    b["d"] = d; b["lines"] = list(lines); b["eras"] = []; b["sig"] = list(sig); b["sc"] = []; b["rel"] = list(rel); b["s"] = "knowledge"
    return b
ADD = {
 "00_00": [
  B("Old El Paso", "United States", "", "Tex-Mex foods", "Tex-Mex brand of tortillas, taco shells and kits, owned by General Mills.", rel=["Mission Foods"]),
  B("Boudin Bakery", "United States", "1849", "Artisan bakery", "San Francisco sourdough bakery founded by the Boudin family during the Gold Rush.", sig=["San Francisco sourdough"]),
  B("Kingsmill", "United Kingdom", "", "Supermarket bread", "British sliced-bread brand of Allied Bakeries, part of Associated British Foods.", rel=["Warburtons", "Hovis"]),
  B("Arnold", "United States", "", "Supermarket bread", "American packaged-bread brand owned by Bimbo Bakeries USA.", rel=["Grupo Bimbo"]),
  B("Udi's", "United States", "", "Gluten-free bread", "Gluten-free bread brand from Denver, owned by Conagra Brands."),
  B("Canyon Bakehouse", "United States", "", "Gluten-free bread", "Colorado gluten-free bakery brand owned by Flowers Foods."),
  B("Genius", "United Kingdom", "", "Gluten-free bread", "British gluten-free bread brand."),
  B("BFree", "Ireland", "", "Gluten-free bread", "Irish gluten-free bread and wrap brand."),
 ],
 "00_01": [
  B("Melegatti", "Italy", "1894", "Industrial festive bakery", "Verona bakery whose founder Domenico Melegatti patented the pandoro in 1894.", sig=["Pandoro"], rel=["Bauli"]),
  B("Motta", "Italy", "1919", "Industrial festive bakery", "Milan panettone maker founded by Angelo Motta; owned by Bauli since 2009.", sig=["Panettone"], rel=["Bauli", "Alemagna"]),
  B("Alemagna", "Italy", "1933", "Industrial festive bakery", "Milan panettone maker founded by Gioacchino Alemagna; owned by Bauli since 2009.", sig=["Panettone"], rel=["Bauli", "Motta"]),
  B("Juchheim", "Japan", "", "Confectionery", "Japanese confectioner founded by German baker Karl Juchheim, who introduced Baumkuchen to Japan.", sig=["Baumkuchen"]),
  B("Fukusaya", "Japan", "1624", "Wagashi & castella", "Nagasaki castella maker, one of the oldest makers of the cake.", sig=["Castella"]),
  B("Fujiya", "Japan", "1910", "Confectionery & patisserie", "Japanese confectionery and cake-shop company founded in Yokohama.", sig=["Japanese Christmas cake"]),
  B("Marks & Spencer", "United Kingdom", "1884", "Retailer (own-label food)", "British retailer whose own-label food range includes Colin the Caterpillar cake.", sig=["Colin the Caterpillar"]),
  B("Tunnock's", "United Kingdom", "1890", "Biscuits & cakes", "Family-owned bakery in Uddingston, Scotland, known for teacakes and caramel wafers."),
 ],
 "01_01": [
  B("Keebler", "United States", "1853", "Biscuit & cracker maker", "American cookie and cracker maker founded in Philadelphia; originated Club crackers.", sig=["Club"], rel=["Kellogg's"]),
  B("Kellogg's", "United States", "1906", "Cereal & snacks", "Battle Creek cereal and snack company; its snack brands passed to Kellanova in 2023.", rel=["Keebler"]),
  B("Mondelēz International", "United States", "2012", "Snack multinational", "Chicago snack company spun off from Kraft Foods; owns Nabisco and LU.", rel=["Nabisco", "LU"]),
  B("LU", "France", "1846", "Biscuit & cracker maker", "Nantes biscuit maker Lefèvre-Utile, now a Mondelēz brand that sells TUC crackers.", sig=["TUC"], rel=["Mondelēz International"]),
 ],
 "02_00": [
  B("Daniel Peter", "Switzerland", "", "Chocolatier", "Vevey chocolatier who made the first commercial milk chocolate with condensed milk.", sig=["Gala Peter"], rel=["Nestlé", "Kohler"]),
  B("Kohler", "Switzerland", "1830", "Chocolate maker", "Lausanne chocolate maker founded by Charles-Amédée Kohler, known for hazelnut chocolate; later merged with Peter.", sig=["Whole-hazelnut bar"], rel=["Daniel Peter", "Nestlé"]),
  B("Bonnat", "France", "1884", "Craft & professional", "Family chocolate maker in Voiron, known for single-origin bars."),
  B("Original Beans", "Netherlands", "2008", "Craft & professional", "Amsterdam bean-to-bar chocolate maker focused on rare-origin cacao."),
  B("Côte d'Or", "Belgium", "1883", "Mass-market chocolate", "Belgian chocolate brand with the elephant logo, owned by Mondelēz International."),
  B("Freia", "Norway", "1889", "Mass-market chocolate", "Oslo chocolate maker known for Melkesjokolade, owned by Mondelēz International.", rel=["Marabou"]),
 ],
 "02_01": [
  B("Tobler", "Switzerland", "1899", "Chocolate maker", "Bern chocolate maker of Jean Tobler, whose son Theodor created Toblerone in 1908.", sig=["Toblerone"]),
  B("Nestlé", "Switzerland", "1866", "Food multinational", "Vevey food company; has made Kit Kat outside the United States since buying Rowntree's in 1988.", rel=["Rowntree's"]),
  B("Mirabell", "Austria", "", "Mozartkugel maker", "Salzburg maker of Real Salzburg Mozartkugeln, owned by Mondelēz International.", rel=["Café Konditorei Fürst"]),
  B("Reber", "Germany", "1865", "Mozartkugel maker", "Bad Reichenhall confectioner making Mozart-Kugeln.", rel=["Café Konditorei Fürst"]),
  B("Manner", "Austria", "1890", "Wafers & confectionery", "Vienna confectioner founded by Josef Manner, known for hazelnut wafers."),
  B("Halloren", "Germany", "1804", "Chocolate maker", "Halle chocolate factory, the oldest in Germany, known for Halloren-Kugeln."),
  B("Alice Medrich", "United States", "", "Chocolatier & author", "Berkeley chocolatier who founded Cocolat and popularised the large American-style truffle.", sig=["Californian truffle"]),
  B("Louis Dufour", "France", "", "Confectioner", "Chambéry confectioner traditionally credited with creating the chocolate truffle in 1895.", sig=["French truffle"]),
  B("Wittamer", "Belgium", "1910", "Belgian praline house", "Brussels pâtissier and chocolatier on the Place du Grand Sablon."),
 ],
 "03_01": [
  B("Hacı Bekir", "Turkey", "1777", "Lokum maker", "Istanbul confectioner founded by Bekir Efendi, credited with popularising lokum.", sig=["Istanbul lokum"]),
  B("Pelino", "Italy", "1783", "Confetti maker", "Sulmona maker of sugared almonds (confetti), with a confetti museum.", sig=["Confetti di Sulmona"]),
  B("Sperlari", "Italy", "1836", "Torrone maker", "Cremona confectioner known for torrone.", sig=["Torrone di Cremona"]),
 ],
 "05_00": [
  B("Kellanova", "United States", "2023", "Snacks", "Snack company formed when Kellogg Company split off its cereal business in 2023.", lines=["Nutri-Grain", "Rice Krispies Treats"]),
  B("Nakd", "United Kingdom", "", "Fruit & nut bars", "British raw fruit-and-nut bar brand owned by Lotus Bakeries."),
  B("Jordans", "United Kingdom", "", "Cereals & cereal bars", "British cereal brand owned by Associated British Foods."),
 ],
}
MK = {"01_01": {"Club": "Keebler", "TUC": "LU"}, "03_01": {}}
for job in sys.argv[1:]:
    p = D + job + '.json'; d = json.load(open(p))
    have = {b['n'] for b in d['brands']}
    added = []
    for b in ADD.get(job, []):
        if b['n'] not in have: d['brands'].append(b); added.append(b['n'])
    for k in d['kinds']:
        for x in k.get('x', []):
            if x['n'] in MK.get(job, {}) and not x.get('mk'): x['mk'] = MK[job][x['n']]
    n = d.get('notes', '')
    n = n.replace(" Club and TUC archetypes have empty mk because their makers have no register entry here.", "")
    if added: n += " Brand entries added later from reliable knowledge (s=knowledge, owner decision): " + ", ".join(added) + "."
    d['notes'] = n
    tmp = p + '.tmp'
    with open(tmp, 'w') as fh: json.dump(d, fh, ensure_ascii=False, indent=1)
    os.replace(tmp, p)
    print(job, 'added', added)
