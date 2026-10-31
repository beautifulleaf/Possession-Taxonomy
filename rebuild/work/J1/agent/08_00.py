import json, os
def X(n, d, s, a="", y="", v=None, mk=""):
    x = {"n": n, "a": a, "d": d, "mk": mk, "y": y, "s": s}
    if v: x["v"] = [{"n": a_, "mk": "", "y": b_, "d": c_} for a_, b_, c_ in v]
    return x
EC = "https://food.ec.europa.eu/safety/novel-food/authorisations/approval-insect-novel-food_en"
kinds = [
 {"n": "Horse meat", "a": "horsemeat · cheval · sakura niku", "d": "Horse meat sold whole or as any cut, including raw slices for eating raw.",
  "s": "https://www.vianderichelieu.com/cheval?lang=en", "t": ["ribeye steak", "sirloin steak", "tenderloin", "flank steak", "mince"],
  "x": [X("Basashi", "Thin-sliced raw horsemeat sashimi eaten with garlic, ginger and soy; Kumamoto, Japan's leading producer, counts it a signature dish.", "https://www.mlit.go.jp/tagengo-db/en/R2-02049.html", "horsemeat sashimi · Kumamoto basashi", "1590s")]},
 {"n": "Bison", "a": "American bison · buffalo", "d": "Meat of North American bison, ranched and sold whole or as steaks, roasts and mince.",
  "s": "https://www.dartagnan.com/buy/meat-game", "t": ["steak", "roast", "mince", "grass-finished", "grain-finished"],
  "x": [X("Plains bison", "Bison of the plains subspecies, ranched for meat and sold as ribeye and other steaks.", "https://heritagefoods.com/products/bison-ribeye-steak", "",
          v=[("Bison Ribeye Steak", "", "16–18 oz, Roaming Acres Farm")])]},
 {"n": "Kangaroo", "a": "kangaroo meat · australus · roo", "d": "Lean meat of wild kangaroos harvested under licence in Australia, sold as fillets, steaks, mince and sausages.",
  "s": "https://en.wikipedia.org/wiki/Kangaroo_meat", "t": ["fillet", "steak", "mince", "sausages", "red kangaroo", "eastern grey", "western grey", "common wallaroo"]},
 {"n": "Ostrich", "a": "ostrich meat", "d": "Dark, lean meat of the farmed ostrich, sold mainly as fillets and steaks.",
  "s": "https://en.wikipedia.org/wiki/Ostrich_meat", "t": ["fillet", "steak", "mince"]},
 {"n": "Crocodile & alligator", "a": "gator meat · crocodile meat", "d": "Pale, mild meat of farmed crocodiles and alligators, the tail being the prized cut.",
  "s": "https://wholey.com/resources/fish-seafood/your-guide-to-gator-meat/", "t": ["tail meat", "body meat", "jaw meat", "ribs"],
  "x": [X("Alligator tail meat", "The most tender alligator cut, from farms in Florida and Louisiana.", "https://wholey.com/resources/fish-seafood/your-guide-to-gator-meat/", "gator tail"),
        X("Crocodile tail meat", "White or pink tail meat of farm-reared crocodiles, the main cut beside leg, torso and jaw.", "https://www.fao.org/4/T0226E/t0226e17.htm")]},
 {"n": "Camel", "a": "camel meat", "d": "Camel meat, like coarse beef; the hump, brisket, ribs and loin are preferred.",
  "s": "http://www.fao.org/4/X6528E/X6528E06.htm", "t": ["hump", "brisket", "ribs", "loin", "mince"]},
 {"n": "Frogs' legs", "a": "cuisses de grenouille", "d": "The hind legs of edible frogs, sold raw or frozen.",
  "s": "https://www.citarella.com/frog-legs.html", "t": ["fresh", "frozen"]},
 {"n": "Turtle meat", "a": "", "d": "The meat of turtles sold to eat.", "s": "https://www.marxfoods.com/Boneless-Turtle-Meat"},
 {"n": "Edible insects", "a": "crickets · mealworms · locusts · insect powder", "d": "Insects sold to eat, frozen, dried, roasted or ground to powder.",
  "s": "https://www.edibleinsects.com/edible-bugs/all-edible-insects/",
  "t": ["house cricket (Acheta domesticus)", "yellow mealworm (Tenebrio molitor)", "migratory locust (Locusta migratoria)", "lesser mealworm (Alphitobius diaperinus)", "frozen", "dried", "powder"],
  "x": [X("EU-authorised insect foods", "Insect species approved as novel foods in the EU, in frozen, dried and powder forms.", EC, "", "2021–2025",
          [("Migratory locust", "2021", "Regulation 2021/1975"), ("Yellow mealworm", "2022", "Regulation 2022/169; UV-treated powder 2025"), ("House cricket", "2022", "Regulation 2022/188; partially defatted powder"), ("Lesser mealworm", "2023", "Regulation 2023/58")])]},
 {"n": "Meat box", "a": "butcher's box · meat subscription box · mixed fresh meats", "d": "A box of raw meats from several animals, bought once or by subscription, no one meat making up half its weight.",
  "s": "https://www.dakotabutcher.com/products", "t": ["one-off box", "subscription", "BBQ box", "family box"]}
]
brands = [{"n": "ButcherBox", "c": "United States", "f": "2015", "seg": "Specialist", "kf": "meat subscription box", "d": "US meat delivery subscription service shipping beef, pork, chicken and seafood.", "s": "knowledge"}]
notes = ("Six old horse kinds (horse meat, ribeye, tenderloin, sirloin, flank, ground) merged into Horse meat with cuts as types; Basashi became an archetype. "
         "Wood bison not attested on a retrieved page, so only plains bison is an archetype. Turtle meat and frogs' legs stay kind-level with old sources. Mixed fresh meats became Meat box (no models).")
out = {"kinds": kinds, "brands": brands, "traditions": [], "notes": notes}
p = "/home/user/Possession-Taxonomy/rebuild/work/J1/shelves/08_00.json"
json.dump(out, open(p + ".tmp", "w"), ensure_ascii=False, indent=1); os.replace(p + ".tmp", p)
