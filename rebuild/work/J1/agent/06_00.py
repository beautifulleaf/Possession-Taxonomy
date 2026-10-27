import json, os
W = "https://en.wikipedia.org/wiki/"
L = W + "List_of_sausages"
DT = "meat content · natural or collagen casing · links, coil or loose sausagemeat · seasoning"
kinds = [
 {"n": "British sausage", "a": "banger · English sausage", "d": "Fresh pork sausage seasoned with pepper, herbs and rusk, sold in links or coils to fry or grill.",
  "s": "https://farmfetch.co.uk/collections/sausages", "t": ["pork", "pork and herb", "beef", "skinless"],
  "x": [
   {"n": "Cumberland sausage", "a": "Traditional Cumberland sausage", "d": "Long, coarsely chopped, pepper-heavy pork sausage sold in a flat coil; PGI requires Cumbrian production and at least 80% meat.", "mk": "", "y": "PGI 2011", "s": W + "Cumberland_sausage",
    "v": [{"n": "Traditional Cumberland sausage PGI", "mk": "", "y": "2011", "d": "made in Cumbria, ≥80% meat, sold in a long coil"}], "dt": "coil or links · meat content 80–98%"},
   {"n": "Lincolnshire sausage", "a": "", "d": "Chunky pork sausage dominated by sage; earliest recorded recipe 1886.", "mk": "", "y": "1886", "s": W + "Lincolnshire_sausage", "dt": "sage, parsley or thyme · coarse grind"},
   {"n": "Oxford sausage", "a": "", "d": "Pork and veal sausage, heavily spiced, often with lemon and herbs; originally skinless and floured.", "mk": "", "y": "1723", "s": W + "Oxford_sausage", "dt": "skinless or natural casing"},
   {"n": "Chipolata", "a": "chipo", "d": "Small, finger-width pork sausage, the one wrapped in streaky bacon as pigs in blankets.", "mk": "", "y": "by 1830s", "s": W + "Chipolata", "dt": "pork or chicken · plain or bacon-wrapped"},
   {"n": "Lorne sausage", "a": "square sausage · slice", "d": "Scottish sausage, listed among British regional sausages (Scotland).", "mk": "", "y": "", "s": L}
  ]},
 {"n": "Bratwurst", "a": "Bratwürste · brat", "d": "Fresh German pork or veal sausage made to fry or grill, in many regional styles.",
  "s": "https://hermannwursthaus.com/our-bratwurst/", "t": ["fresh", "pre-cooked"],
  "x": [
   {"n": "Fränkische Bratwurst", "a": "Franconian bratwurst", "d": "Long, thick, coarse marjoram-flavoured sausage of Franconia, the oldest documented bratwurst tradition (Nuremberg 1313).", "mk": "", "y": "1313", "s": W + "Bratwurst"},
   {"n": "Nürnberger Rostbratwurst", "a": "Nürnberger Bratwürste", "d": "Small, thin pork sausage seasoned with marjoram and grilled over beechwood; PGI, made only in Nuremberg.", "mk": "", "y": "1567", "s": W + "Bratwurst",
    "v": [{"n": "Nürnberger Rostbratwurst PGI", "mk": "", "y": "2003", "d": "may be made only in Nuremberg"}]},
   {"n": "Thüringer Rostbratwurst", "a": "Thuringian sausage", "d": "Thin, low-fat spiced sausage with caraway, marjoram and garlic; PGI.", "mk": "", "y": "1404", "s": W + "Bratwurst"},
   {"n": "Coburger Bratwurst", "a": "", "d": "Pork sausage with at least 15% beef, bound with raw egg; first documented in Coburg in 1498.", "mk": "", "y": "1498", "s": W + "Bratwurst"},
   {"n": "Kulmbacher Bratwurst", "a": "", "d": "Finely ground, mostly veal fresh sausage from Kulmbach.", "mk": "", "y": "", "s": W + "Bratwurst"},
   {"n": "Würzburger Bratwurst", "a": "Winzerbratwurst", "d": "Würzburg sausage the size of a Thüringer with regional white wine in the recipe.", "mk": "", "y": "", "s": W + "Bratwurst"},
   {"n": "Nordhessische Bratwurst", "a": "North Hessian bratwurst", "d": "20 cm coarse, heavily seasoned pork sausage grilled over wood.", "mk": "", "y": "", "s": W + "Bratwurst"},
   {"n": "Rote Wurst", "a": "Swabian red sausage", "d": "Finely ground pork and bacon sausage with X-shaped cuts at the ends.", "mk": "", "y": "", "s": W + "Bratwurst"},
   {"n": "St. Galler Bratwurst", "a": "", "d": "Swiss veal bratwurst popular in eastern Switzerland since 1438.", "mk": "", "y": "1438", "s": W + "Bratwurst"},
   {"n": "Banater Bratwurst", "a": "", "d": "Paprika-seasoned bratwurst brought by Banat Swabians, sold fresh or smoked.", "mk": "", "y": "", "s": W + "Bratwurst"}
  ]},
 {"n": "Italian sausage", "a": "salsiccia · sweet or hot Italian sausage", "d": "Fresh pork sausage seasoned with garlic and pepper, often fennel, to cook.",
  "s": "https://www.truebites.co.uk/products/italian-pork-sausage", "t": ["links", "coil", "loose sausagemeat"],
  "x": [
   {"n": "Luganega", "a": "luganiga · lucanica", "d": "Long fresh pork sausage coiled like a snail, from Lombardy and Veneto, descended from Lucanian sausage.", "mk": "", "y": "pre-Roman origin", "s": W + "Luganega", "dt": "plain or with Grana Padano and Marsala"},
   {"n": "North American Italian sausage", "a": "sweet · mild · hot Italian", "d": "Fennel- or anise-seasoned pork sausage sold as mild, sweet (with basil) or hot (with chilli flakes).", "mk": "", "y": "", "s": W + "Italian_sausage",
    "v": [{"n": "Mild", "mk": "", "y": "", "d": "base spice mix"}, {"n": "Sweet", "mk": "", "y": "", "d": "with sweet basil"}, {"n": "Hot", "mk": "", "y": "", "d": "with red pepper flakes"}]}
  ]},
 {"n": "Breakfast sausage", "a": "breakfast links · sausage patties", "d": "Fresh, highly seasoned ground pork sausage eaten at breakfast, as links, patties or loose sausagemeat.",
  "s": "https://sclydeweaver.com/product/maple-apple-breakfast-links-for-sale-s-clyde-weaver/", "t": ["links", "patties", "loose", "maple", "sage", "hot"],
  "x": [
   {"n": "American breakfast sausage", "a": "country sausage", "d": "Fresh ground pork sausage made in the US since colonial days, sold as links, patties or rolls; maple or cayenne versions.", "mk": "", "y": "colonial era", "s": W + "Breakfast_sausage", "dt": "links, patties or chub · original, maple, hot"},
   {"n": "Canadian breakfast sausage", "a": "", "d": "Breakfast sausage seasoned with sage and black pepper, close to a Lincolnshire sausage.", "mk": "", "y": "", "s": W + "Breakfast_sausage"}
  ]},
 {"n": "Toulouse sausage", "a": "saucisse de Toulouse", "d": "Coarse fresh pork sausage of south-west France, seasoned only with salt and pepper, sold in coils.",
  "s": W + "Saucisse_de_Toulouse",
  "x": [{"n": "Saucisse de Toulouse", "a": "", "d": "About 75% lean pork and 25% belly in a 3 cm natural casing; the sausage of cassoulet; a Label Rouge standard has been proposed.", "mk": "", "y": "", "s": W + "Saucisse_de_Toulouse", "dt": "coil or links · plain or confit"}]},
 {"n": "Merguez", "a": "mergez", "d": "Red, spicy fresh lamb or beef sausage of the Maghreb, seasoned with cumin, chilli or harissa.",
  "s": W + "Merguez", "t": ["lamb", "beef", "lamb and beef"],
  "x": [{"n": "Merguez", "a": "", "d": "Lamb or beef in a thin lamb casing, spiced with cumin, harissa, sumac, fennel and garlic; Algerian origin, popular in France since the 1960s.", "mk": "", "y": "", "s": W + "Merguez"}]},
 {"n": "Boerewors", "a": "wors · farmer's sausage", "d": "South African coiled fresh sausage of beef with pork or lamb, spiced with toasted coriander, cooked on the braai.",
  "s": W + "Boerewors",
  "x": [{"n": "Boerewors", "a": "", "d": "By South African law at least 90% meat, no more than 30% fat, no offal; coriander, pepper, nutmeg and cloves; sold in a continuous coil.", "mk": "", "y": "", "s": W + "Boerewors",
    "v": [{"n": "Garlic wors", "mk": "", "y": "", "d": "with garlic"}, {"n": "Karoowors", "mk": "", "y": "", "d": "from the Karoo region"}, {"n": "Spekwors", "mk": "", "y": "", "d": "with cubed pork fat"}, {"n": "Kameeldoring", "mk": "", "y": "", "d": "camel-thorn variety"}]}]},
 {"n": "Fresh chorizo & longaniza", "a": "chorizo fresco · Mexican chorizo · longganisa", "d": "Raw, chilli- or paprika-seasoned sausage of the Spanish-speaking world, cooked before eating.",
  "s": W + "Chorizo", "t": ["links", "loose"],
  "x": [
   {"n": "Mexican chorizo", "a": "chorizo mexicano", "d": "Fresh, uncured ground sausage of pork, beef, chicken or turkey, made spicy with native chillies and vinegar.", "mk": "", "y": "", "s": W + "Chorizo"},
   {"n": "Spanish chorizo fresco", "a": "chorizo para cocinar", "d": "The fresh Spanish chorizo, seasoned with garlic and pimentón, from which Mexican chorizo developed.", "mk": "", "y": "", "s": W + "Chorizo"},
   {"n": "Longaniza", "a": "longganisa", "d": "Long Spanish-derived sausage seasoned with black pepper rather than paprika, made in many national styles.", "mk": "", "y": "", "s": W + "Longaniza",
    "v": [{"n": "Mexican longaniza", "mk": "", "y": "", "d": "longer and spicier than Mexican chorizo, cooked with eggs"}, {"n": "Longganisa de Vigan", "mk": "", "y": "", "d": "garlicky pork de recado, Ilocos"}, {"n": "Longganisa de Lucban", "mk": "", "y": "", "d": "pork de recado with oregano, Quezon"}, {"n": "Longganisa hamonado", "mk": "", "y": "", "d": "sweet Philippine style"}, {"n": "Chilean longaniza", "mk": "", "y": "", "d": "barbecue sausage, Chillán"}]},
   {"n": "Chaurice", "a": "", "d": "Louisiana fresh chorizo-type sausage used in red beans and rice.", "mk": "", "y": "", "s": W + "Chorizo"}
  ]}
]
brands = [
 {"n": "Jimmy Dean", "c": "United States", "seg": "Mainstream", "kf": "breakfast sausage", "d": "US breakfast sausage brand named among the main breakfast-sausage makers.", "s": W + "Breakfast_sausage"},
 {"n": "Johnsonville", "c": "United States", "seg": "Mainstream", "kf": "bratwurst, breakfast links", "d": "US sausage maker named among the main breakfast-sausage brands.", "s": W + "Breakfast_sausage"},
 {"n": "Bob Evans", "c": "United States", "seg": "Mainstream", "kf": "breakfast sausage", "d": "US breakfast sausage brand.", "s": W + "Breakfast_sausage"},
 {"n": "Jones Dairy Farm", "c": "United States", "seg": "Heritage manufactory", "kf": "breakfast links", "d": "US breakfast sausage brand (named as Jones).", "s": W + "Breakfast_sausage"}
]
notes = ("Old 'Other fresh sausage' renamed British sausage; its models Bangers (kind alias) and Chipolata became an alias/archetype, Luganega moved to Italian sausage as an archetype. "
         "Old flat models 'Bratwurst', 'Italian sausage', 'Breakfast sausage' were generic and became archetypes/kinds. Salsiccia di Bra and Luganega trevigiana not found on retrieved pages, left out. "
         "Glamorgan sausage left out (meat-free). No traditions added (sausage traditions are expressed as archetypes). Wikidata helper too slow; all sources are retrieved Wikipedia pages.")
out = {"kinds": kinds, "brands": brands, "traditions": [], "notes": notes}
p = "/home/user/Possession-Taxonomy/rebuild/work/J1/shelves/06_00.json"
json.dump(out, open(p + ".tmp", "w"), ensure_ascii=False, indent=1); os.replace(p + ".tmp", p)
