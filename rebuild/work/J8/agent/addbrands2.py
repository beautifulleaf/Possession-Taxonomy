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
 "01_00": [
  B("Sunshine Biscuits", "United States", "1902", "Biscuit & cookie maker", "American biscuit maker, founded as the Loose-Wiles Biscuit Company of Kansas City; bought by Keebler in 1996.", sig=["Hydrox"], rel=["Nabisco"]),
  B("Burton's Biscuit Company", "United Kingdom", "", "Biscuit maker", "British biscuit maker whose brands include Jammie Dodgers and Wagon Wheels.", sig=["Jammie Dodger"]),
  B("Meiji Seika", "Japan", "1916", "Confectionery", "Tokyo confectionery company, now part of Meiji Holdings.", sig=["Hello Panda"], rel=["Lotte", "Glico"]),
  B("Lotte", "Japan", "1948", "Confectionery", "Tokyo confectionery company founded by Shin Kyuk-ho, known for chewing gum and Koala's March.", sig=["Koala's March"], rel=["Lotte Wellfood"]),
  B("Lotte Wellfood", "South Korea", "1967", "Confectionery", "Seoul confectionery company of the Lotte group, formerly Lotte Confectionery (renamed 2023).", sig=["Pepero"], rel=["Lotte"]),
  B("Jacob's", "Ireland", "1851", "Biscuit maker", "Biscuit brand of W. & R. Jacob, founded in Waterford and later based in Dublin, known for cream crackers and Fig Rolls.", sig=["Lincoln"]),
  B("Mr Kipling", "United Kingdom", "1967", "Packaged cakes", "British packaged-cake brand owned by Premier Foods.", sig=["Viennese whirl"]),
  B("Macdonald Biscuits", "United Kingdom", "", "Biscuit maker", "Glasgow biscuit maker that created the Penguin biscuit in 1932; later part of United Biscuits.", sig=["Penguin"], rel=["McVitie's"]),
  B("Leaf Brands", "United States", "", "Confectionery", "American confectionery company that revived Hydrox cookies in 2015.", sig=["Hydrox"]),
  B("Viau", "Canada", "", "Biscuit maker", "Montreal biscuit maker known for Whippet chocolate-marshmallow cookies.", sig=["Chocolate teacake"]),
  B("Maison Dandoy", "Belgium", "1829", "Artisan biscuit bakery", "Brussels biscuit bakery known for speculoos.", sig=["Speculoos"]),
  B("Maison Méert", "France", "1761", "Pâtisserie & confectioner", "Lille pâtisserie known for its vanilla-filled waffles.", sig=["Stroopwafel"]),
  B("Papadopoulou", "Greece", "", "Biscuit maker", "Greek biscuit maker known for Caprice rolled wafers.", sig=["Rolled wafer"]),
  B("DeBeukelaer", "United States", "", "Biscuit maker", "American maker of Pirouline rolled wafers in cylindrical tins.", sig=["Rolled wafer"]),
  B("Antonio Mattei", "Italy", "1858", "Artisan biscuit bakery", "Prato biscuit bakery known for its traditional biscotti di Prato.", sig=["Cantucci"]),
 ],
 "04_00": [
  B("Frito-Lay", "United States", "1961", "Snack multinational", "Snack company formed by the merger of the Frito Company and H.W. Lay & Company; a PepsiCo division since 1965.", sig=["Doritos", "Cheetos", "Fritos", "Tostitos"], rel=["Lay's", "Walkers"]),
  B("Frito Company", "United States", "1932", "Corn snacks", "San Antonio company founded by Charles Elmer Doolin to make Fritos; merged with H.W. Lay & Company in 1961 to form Frito-Lay.", sig=["Fritos"], rel=["Frito-Lay"]),
  B("Barcel", "Mexico", "", "Snacks", "Mexican snack maker owned by Grupo Bimbo, known for Takis.", sig=["Takis"]),
  B("Osem", "Israel", "1942", "Food company", "Israeli food company, controlled by Nestlé, known for Bamba.", sig=["Bamba"]),
  B("Nongshim", "South Korea", "1965", "Instant noodles & snacks", "Seoul food company known for Shin Ramyun and Saeukkang prawn crackers.", sig=["Saeukkang"]),
  B("Glico", "Japan", "1922", "Confectionery", "Ezaki Glico, Osaka confectionery company, maker of Pocky and Pretz.", sig=["Pretz"]),
  B("General Mills", "United States", "1928", "Food multinational", "Minneapolis-area food company known for breakfast cereals; maker of Bugles.", sig=["Bugles"]),
  B("Wise Foods", "United States", "1921", "Snacks", "Berwick, Pennsylvania snack maker, owned by Arca Continental since 2012.", sig=["Cheez Doodles"]),
  B("Snyder's of Hanover", "United States", "1909", "Pretzels", "Hanover, Pennsylvania pretzel maker, owned by Campbell's since 2018.", sig=["Snyder's of Hanover"]),
  B("American Pop Corn Company", "United States", "1914", "Popcorn", "Sioux City, Iowa popcorn company, maker of Jolly Time.", sig=["Jolly Time"]),
  B("Procter & Gamble", "United States", "1837", "Consumer goods multinational", "Cincinnati consumer-goods company that created Pringles in 1968.", sig=["Pringles"], rel=["Pringles"]),
  B("Hain Celestial Group", "United States", "1993", "Natural foods", "American natural and organic food company, owner of Terra chips.", sig=["Terra Chips"]),
  B("Conagra Brands", "United States", "1919", "Packaged foods", "Chicago packaged-food company, owner of Orville Redenbacher's.", sig=["Orville Redenbacher's"]),
  B("General Foods", "United States", "1929", "Packaged foods", "American food company formed from the Postum Company; merged into Kraft in 1989.", sig=["Twisties"]),
  B("Tom's Snacks", "United States", "", "Snacks", "Snack maker from Columbus, Georgia.", sig=["Bugles"]),
 ],
}
MK = {"01_00": {"Hydrox": "Sunshine Biscuits", "Jammie Dodger": "Burton's Biscuit Company", "Hello Panda": "Meiji Seika",
                "Koala's March": "Lotte", "Pepero": "Lotte Wellfood"}}
NOTE_RM = {
 "01_00": " Makers without a retrieved brand page (Sunshine Biscuits, Burton's, Meiji, Lotte, Jacob's, Mr Kipling) appear only in version mk, archetype mk left empty.",
 "04_00": " Frito-Lay, Barcel, Osem, Nongshim, Glico, General Mills, Wise Foods and Frito-Lay-owned brands are archetype makers without register pages (no page fetched for the company).",
}
for job in sys.argv[1:]:
    p = D + job + '.json'; d = json.load(open(p))
    have = {b['n'] for b in d['brands']}
    added = []
    for b in ADD.get(job, []):
        if b['n'] not in have: d['brands'].append(b); added.append(b['n'])
    names = {b['n'] for b in d['brands']}
    for k in d['kinds']:
        for x in k.get('x', []):
            m = MK.get(job, {}).get(x['n'])
            if m and not x.get('mk') and m in names: x['mk'] = m
    n = d.get('notes', '').replace(NOTE_RM.get(job, '@@'), '')
    if added: n += " Brand entries added from reliable knowledge (s=knowledge, owner decision): " + ", ".join(added) + "."
    d['notes'] = n
    tmp = p + '.tmp'
    with open(tmp, 'w') as fh: json.dump(d, fh, ensure_ascii=False, indent=1)
    os.replace(tmp, p)
    print(job, 'added', added)
