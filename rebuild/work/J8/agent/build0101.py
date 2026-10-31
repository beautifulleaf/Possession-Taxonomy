import json, os
W = 'https://en.wikipedia.org/wiki/'
CARR = W + 'Carr%27s'; JAC = W + 'Jacob%27s'; WASA = W + 'Wasabr%C3%B6d'; ARN = W + 'Arnott%27s_Biscuits'
RAK = W + 'Rakusen%27s'; STR = W + 'Streit%27s'; FINN = 'https://www.business-sweden.com/try-swedish/food-from-sweden/finn-crisp'
PY = 'https://www.greatbritishchefs.com/features/peters-yard-crispbreads'; GT = 'https://www.guidatorino.com/?p=9744'

def X(n, d, mk, y, s, v=None, a='', dt=''):
    return {"n": n, "a": a, "d": d, "mk": mk, "y": y, "s": s, "v": v or [], "dt": dt}
def V(n, mk='', y='', d=''):
    return {"n": n, "mk": mk, "y": y, "d": d}

kinds = [
 {"n": "Water biscuit & cream cracker", "a": "water cracker · table water biscuit · cream cracker · ship's biscuit · pilot bread",
  "d": "Thin, plain, crisp savoury biscuit of flour and water (or fermented, fat-layered dough for cream crackers), eaten with cheese.",
  "t": ["plain", "high-bake", "with sesame or black pepper", "square", "round"], "s": W + "Water_biscuit",
  "x": [
   X("Table water biscuit", "Thin, brittle, blistered round of flour and water; the classic cheese-board biscuit.", "Carr's", "", CARR,
     [V("Carr's Table Water", "Carr's", "", "made in Carlisle; now owned by Pladis"), V("Jacob's water biscuits", "Jacob's", "", "named with Carr's as a leading brand")],
     dt="round · plain, sesame, black pepper · high-bake"),
   X("Water cracker (Bent's)", "Hard, keeping water cracker sold for long sea voyages from Boston.", "", "1801", W + "Water_biscuit",
     [V("Bent's water crackers", "G. H. Bent Company", "1801", "Josiah Bent, Milton, Massachusetts")]),
   X("Cream cracker", "Flat, square, flaky cracker of fermented wheat dough, oil and yeast; named for the creaming step.", "Jacob's", "c. 1885", W + "Cream_cracker",
     [V("Jacob's Cream Crackers", "Jacob's", "c. 1885", "invented by Joseph Haughton in Dublin; made by William Jacob"),
      V("Khong Guan cream crackers", "Khong Guan"), V("Hup Seng cream crackers", "Hup Seng"),
      V("Britannia cream crackers", "Britannia Industries"), V("Bakers cream crackers", "Bakers"),
      V("Purity cream crackers", "Purity Factories", "", "lard-based, Newfoundland")],
     dt="square · fermented dough · plain, wholemeal"),
   X("Bath Oliver", "Firm, dry yeast-and-milk cracker biscuit devised by Dr William Oliver of Bath, served with cheese.", "", "c. 1750", W + "Bath_Oliver",
     [V("Fortt's Bath Oliver", "Fortt", "19th century", "recipe passed via Atkins, Norris and Carter to James Fortt"),
      V("Jacob's Bath Oliver", "Jacob's", "", "discontinued 2025")]),
   X("Ship's biscuit & pilot bread", "Dense keeping cracker of flour, water and sometimes salt, descended from naval hardtack.", "", "", W + "Hardtack",
     [V("Sailor Boy Pilot Bread", "Interbake Foods", "", "most US commercial hardtack, mostly sold in Alaska"),
      V("Purity Hard Bread", "Purity Factories", "", "Newfoundland hardtack"),
      V("Crown Pilot Crackers", "Purity Factories", "", "made by Nabisco until 2008"),
      V("Saloon Pilot", "The Diamond Bakery", "", "sold in Hawaii")],
     a="hardtack · sea biscuit · cabin bread")]},
 {"n": "Butter cracker", "a": "snack cracker · round cracker",
  "d": "Light, flaky, lightly salted cracker enriched with fat for a buttery taste, eaten alone or with toppings.",
  "t": ["original", "reduced fat", "wholewheat", "cheese", "sandwich (filled)", "mini"], "s": W + "Ritz_Crackers",
  "x": [
   X("Ritz", "Lightly salted round cracker about 46 mm wide with seven holes and a scalloped edge.", "Nabisco", "1934", W + "Ritz_Crackers",
     [V("Ritz Original", "Nabisco", "1934"), V("Ritz Fresh Stacks", "Nabisco"), V("Ritz Cheese Sandwich", "Mondelēz International", "", "UK and Ireland")],
     dt="round 46 mm · seven holes · flavours (cheese, whole wheat, hint of salt, garlic butter)"),
   X("Club", "Rectangular buttery cracker with 18 holes in a 3×6 grid, flaky and light.", "", "", W + "Club_Crackers",
     [V("Club Crackers", "Keebler", "", "Kellogg's from 2001"), V("Club & Cheddar", "Kellogg's", "", "square sandwich cracker")]),
   X("TUC", "Salted, octagonal golden-yellow cracker from Belgium.", "", "1958", W + "TUC_(cracker)",
     [V("TUC Original", "LU", "1958", "now Mondelēz; Jacob Fruitfield makes it for some markets")]),
   X("Jatz", "Round malted cracker about 5 cm across, lightly salted on one side, with a scalloped edge.", "Arnott's", "1952", W + "Jatz")]},
 {"n": "Saltine & soda cracker", "a": "saltine · soda cracker · soda biscuit",
  "d": "Thin square cracker of white flour, fat and baking soda, docked with holes and usually topped with coarse salt.",
  "t": ["salted top", "unsalted top", "wholewheat", "multigrain"], "s": W + "Saltine_cracker",
  "x": [
   X("Premium saltine", "The original soda-leavened saltine, first sold as the Premium Soda Cracker.", "Nabisco", "1876", W + "Saltine_cracker",
     [V("Premium Soda Cracker", "F. L. Sommer & Company", "1876", "St. Joseph, Missouri; joined Nabisco 1898"),
      V("Nabisco Premium (US)", "Nabisco"), V("Christie's Premium Plus", "Christie's", "", "Canada"),
      V("Nabisco Premium (Australia & NZ)", "Nabisco")],
     dt="square · 13 holes · salted or unsalted tops")],
  "m": [["Zesta", "Keebler"], ["Krispy", "Sunshine Biscuits"], ["Salada", "Arnott's"], ["Saladitas", "Gamesa"],
        ["Criollitas", "Gamesa"], ["Saltín", "Noel"], ["Hatuey", "Molinos Modernos"]]},
 {"n": "Wholegrain & woven wheat cracker", "a": "whole-wheat cracker · woven wheat",
  "d": "Crisp cracker made wholly from whole grains, typically baked wafers of shredded or woven wheat.",
  "t": ["original", "reduced fat", "thin", "flavoured"], "s": W + "Triscuit",
  "x": [X("Triscuit", "Square wafer of baked shredded whole wheat.", "Nabisco", "1903", W + "Triscuit",
          [V("Triscuit", "Shredded Wheat Company", "1903", "invented by Henry Perky 1900; Nabisco 1928–2012, now Mondelēz")])],
  "m": [["Wholegrain Crackers", "Nairn's"]]},
 {"n": "Oatcake", "a": "oat biscuit · oatcakes · bannock",
  "d": "Flat cracker-like bread made mainly from oatmeal, griddled or oven-baked; pancake-like in some regional forms.",
  "t": ["rough", "fine", "cheese", "rounds", "farls", "gluten-free"], "s": W + "Oatcake",
  "x": [
   X("Scottish oatcake", "Crisp round or farl of oats, salt and water; the classic cheese and breakfast oatcake.", "", "", W + "Oatcake",
     [V("Nairn's Oatcakes", "Nairn's", "1896", "UK's largest oatcake producer"), V("Walker's oatcakes", "Walker's", "", "holds a Royal Warrant"),
      V("Paterson's oatcakes", "Paterson's"), V("Stockan's oatcakes", "Stockan's"), V("Ditty's oatcakes", "Ditty's", "", "Northern Ireland")],
     dt="rough or fine oatmeal · rounds or farls · plain, cheese"),
   X("Staffordshire oatcake", "Large soft pancake-like oat cake from North Staffordshire, made with a good share of wheat flour.", "", "", W + "Oatcake")]},
 {"n": "Crispbread", "a": "knäckebröd · knækbrød · knekkebrød · näkkileipä · Knäckebrot · hard bread",
  "d": "Flat, dry, long-keeping bread, mostly of rye, baked crisp in rounds or rectangles.",
  "t": ["rye", "wholegrain", "sesame", "seeded", "sourdough", "thin", "gluten-free"], "s": W + "Crispbread",
  "x": [
   X("Swedish knäckebröd", "Thin rye crispbread baked in large rounds with a central hole for storing on poles.", "", "6th century", W + "Crispbread",
     [V("AU Bergmans enka", "AU Bergmans enka", "1850", "Sweden's first industrial crispbread bakery, Stockholm")],
     dt="round with hole or rectangle · rye · thin or thick"),
   X("Wasa", "Swedish rye crispbread brand, named after its first product Vasaknäcke.", "Wasa", "1919", WASA,
     [V("Vasaknäcke", "Wasa", "", "original product, bore an image of King Gustavus Vasa")], dt="rye, sesame, wheat, other grains"),
   X("Ryvita", "British rye crispbread first made in Birmingham.", "Ryvita", "1925", W + "Ryvita",
     [V("Ryvita crackerbread and thins", "Ryvita", "", "wheat-based lines")], dt="rye · fruit, seeds · crackerbread, thins"),
   X("Finn Crisp Original", "Thin wholegrain sourdough rye crispbread from Finland.", "Finn Crisp", "1952", FINN,
     [V("Finn Crisp Original", "Finn Crisp", "1952", "launched with the Helsinki Olympics; baked in Kotka")]),
   X("Peter's Yard sourdough crispbread", "Sourdough knäckebröd with milk, rye and honey, from a revived Swedish recipe.", "Peter's Yard", "", PY,
     [V("Original knäckebröd", "Peter's Yard")], dt="original, seeded wholegrain, rye, caraway, pink peppercorn, spelt and fig")],
  "m": [["Vita-Weat", "Arnott's"]]},
 {"n": "Rice cake", "a": "puffed rice cake · rice thin",
  "d": "Flat, hard, light disc of puffed rice, eaten as a low-calorie snack or base for toppings.",
  "t": ["plain", "salted", "wholegrain", "multigrain", "chocolate-coated", "yogurt-coated", "mini"], "s": W + "Puffed_rice_cakes",
  "x": [X("Puffed rice cake", "Disc of steam-puffed rice pressed together; made in American, Chinese and Korean styles.", "", "", W + "Puffed_rice_cakes",
          [V("Quaker Rice Cakes", "Quaker", "1980s", "popular low-fat diet snack in the 1980s–90s")])]},
 {"n": "Grissini & breadsticks", "a": "grissino · breadsticks",
  "d": "Pencil-thin sticks of crisp, dry baked bread, originally from Turin.",
  "t": ["plain", "olive oil", "sesame", "rosemary", "wholemeal", "thin", "soft (restaurant style)"], "s": W + "Grissini",
  "x": [
   X("Grissino rubatà", "Oldest Turin form, hand-rolled to 40–80 cm with a knobby surface.", "", "1679", GT,
     [V("Antonio Brunero's grissino", "", "1679", "court baker's crumbless bread for the young Vittorio Amedeo II")]),
   X("Grissino stirato", "Later Turin form stretched rather than rolled, giving a more crumbly stick.", "", "", GT)]},
 {"n": "Matzo", "a": "matzah · matza · matzos · unleavened bread",
  "d": "Thin unleavened Jewish flatbread, crisp and cracker-like when machine-made, central to Passover.",
  "t": ["plain", "whole wheat", "bran", "organic", "flavoured (onion, poppy seed)", "chocolate-covered", "matzo crackers"], "s": W + "Matzah",
  "x": [
   X("Machine matzo", "Square, mass-produced crisp matzo; the common form in Europe and North America.", "", "1839", W + "Matzah",
     [V("Manischewitz matzo", "Manischewitz", "1888"), V("Streit's matzo", "Streit's", "1916"),
      V("Rakusen's matzos", "Rakusen's", "1900"), V("Yehuda Matzos", "Yehuda Matzos"), V("Osem matzo", "Osem")],
     dt="square · plain, whole wheat · Passover or year-round"),
   X("Shmurah matzo", "Matzo from grain guarded from harvest against fermentation; often hand-made and round.", "", "", W + "Matzah"),
   X("Egg matzo", "Matzo kneaded with fruit juice (sometimes egg) instead of water; not used for the Seder.", "", "", W + "Matzah")]},
]

def B(n, c, f, seg, d, lines, sig, s, eras=None, rel=None):
    return {"n": n, "c": c, "f": f, "seg": seg, "d": d, "lines": lines, "eras": eras or [], "sig": sig, "sc": [], "rel": rel or [], "s": s}
brands = [
 B("Carr's", "United Kingdom", "1831", "Biscuit & cracker maker", "Carlisle biscuit maker founded by Jonathan Dodgson Carr; now owned by Pladis.", ["Table Water"], ["Table water biscuit"], CARR, rel=["Jacob's"]),
 B("Jacob's", "Ireland", "1850s", "Biscuit & cracker maker", "Biscuit maker founded by William Beale Jacob in Waterford, later Dublin; Cream Crackers made at Aintree since 1914.", ["Cream Crackers", "Cracker Crisps", "Mini Cheddars"], ["Cream cracker"], JAC, rel=["Carr's"]),
 B("Nabisco", "United States", "1898", "Biscuit & cracker maker", "National Biscuit Company of Chicago; Mondelēz subsidiary since 2012.", ["Ritz", "Premium", "Triscuit", "Wheat Thins"], ["Ritz", "Premium saltine", "Triscuit"], W + "Nabisco"),
 B("Arnott's", "Australia", "1865", "Biscuit & cracker maker", "Australian biscuit maker founded by William Arnott in Newcastle, NSW; owned by KKR.", ["Jatz", "SAO", "Salada", "Vita-Weat", "Cruskits"], ["Jatz"], ARN),
 B("Wasa", "Sweden", "1919", "Crispbread maker", "Swedish knäckebröd maker founded by Karl Edvard Lundström in Skellefteå; Barilla-owned since 1999.", ["Wasa crispbread"], ["Wasa"], WASA, rel=["Finn Crisp", "Ryvita"]),
 B("Ryvita", "United Kingdom", "1925", "Crispbread maker", "British rye crispbread brand started by John Edwin Garratt; Associated British Foods since 1949.", ["Crispbread", "Crackerbread", "Thins"], ["Ryvita"], W + "Ryvita", rel=["Wasa"]),
 B("Finn Crisp", "Finland", "1849", "Crispbread maker", "Finnish rye crispbread maker from Vaasa, baking in Kotka; part of Lantmännen.", ["Finn Crisp Original"], ["Finn Crisp Original"], FINN, rel=["Wasa"]),
 B("Peter's Yard", "United Kingdom", "", "Artisan crispbread maker", "Sourdough crispbread bakery started by Ian Tencor and Wendy Wilson-Bett from a Swedish recipe.", ["Sourdough crispbread"], ["Peter's Yard sourdough crispbread"], PY),
 B("Nairn's", "United Kingdom", "1896", "Oatcake maker", "Scottish oatcake baker founded by John and Sarah Nairn in Strathaven; two Edinburgh bakeries.", ["Oatcakes", "Oat Biscuits", "Wholegrain Crackers"], ["Scottish oatcake"], "https://nairns.com/about-us"),
 B("Manischewitz", "United States", "1888", "Kosher food maker", "Kosher food company founded by Rabbi Dov Behr Manischewitz in Cincinnati; the world's largest matzo maker.", ["Matzo", "Kosher wine"], ["Machine matzo"], W + "Manischewitz", rel=["Streit's", "Rakusen's"]),
 B("Streit's", "United States", "1916", "Matzo maker", "Family-owned matzo company founded by Aron Streit on the Lower East Side of Manhattan.", ["Matzo"], ["Machine matzo"], STR, rel=["Manischewitz"]),
 B("Rakusen's", "United Kingdom", "1900", "Matzo maker", "Leeds matzo maker founded by watchmaker Lloyd Rakusen.", ["Matzos", "Matzo crackers", "Matzo meal"], ["Machine matzo"], RAK, rel=["Manischewitz"]),
]
trads = [
 {"n": "Scandinavian crispbread (knäckebröd)", "g": "Food & drink", "r": "Sweden, Finland, Norway", "p": "6th century–present",
  "d": "Rye hard bread baked in thin rounds with a central hole and dried on poles.", "tech": "thin-rolled rye dough baked dry, often sourdough",
  "mat": "rye flour, water, salt", "forms": ["Swedish knäckebröd", "Crispbread"], "ctr": ["eastern Värmland", "Stockholm (AU Bergmans enka, 1850)"],
  "auth": "Rye-based, very low moisture, traditional round form with hole.", "s": W + "Crispbread"},
 {"n": "Grissini torinesi", "g": "Food & drink", "r": "Turin, Piedmont, Italy", "p": "1679–present",
  "d": "Turin breadsticks in the hand-rolled rubatà and stretched stirato forms.", "tech": "hand-rolling (rubatà) or stretching (stirato)",
  "mat": "wheat flour, water, yeast, olive oil", "forms": ["Grissino rubatà", "Grissino stirato"], "ctr": ["Turin", "Antonio Brunero"],
  "auth": "Rubatà show an irregular knobby hand-rolled surface and run 40–80 cm.", "s": GT},
]
notes = ("No old data for this shelf; all kinds new. Added 'Wholegrain & woven wheat cracker' (Triscuit) as it fits no planned kind. "
         "Hardtack/pilot bread sits under Water biscuit as the parent form. Rice crackers/senbei left to the savoury-snacks shelf. "
         "Left out (no retrieved page): Leksands, Kallo, Krisprolls, Grissin Bon and other grissini brands, Hi Ho, Wheat Thins details, Kellogg's/Keebler/Mondelēz/LU register entries. "
         "Club and TUC archetypes have empty mk because their makers have no register entry here.")
out = {"kinds": kinds, "brands": brands, "traditions": trads, "notes": notes}
p = 'work/J8/shelves/01_01.json'; tmp = p + '.tmp'
json.dump(out, open(tmp, 'w'), ensure_ascii=False, indent=1); os.replace(tmp, p)
print('kinds', len(kinds), 'archetypes', sum(len(k.get('x', [])) for k in kinds), 'brands', len(brands))
