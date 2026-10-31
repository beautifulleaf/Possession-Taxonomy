import json, os
W = 'https://en.wikipedia.org/wiki/'
K = 'knowledge'
def X(n, d, mk, y, s, v=(), a="", dt=""):
    return {"n": n, "a": a, "d": d, "mk": mk, "y": y, "s": s, "v": [dict(zip(("n", "mk", "y", "d"), t)) for t in v], "dt": dt}
PULP = W + 'Pulp_magazine'; HSF = W + 'History_of_U.S._science_fiction_and_fantasy_magazines_to_1950'
PW = W + 'Partwork'; ZN = W + 'Zine'; NF = W + 'Newspaper_format'
PUNCH = 'https://antiquarianauctions.com/lots/punch-or-the-london-charivari-1841-1891'; STRAND = W + 'The_Strand_Magazine'
ILN = 'https://bpsc.library.ualberta.ca/collections/illustrated-london-news'
FUT = 'https://inpublishing.co.uk/articles/future-announces-new-bookazine-strategy-5913'; IMG = 'https://techcrunch.com/2016/06/23/future-buys-imagine'
MOOK = W + 'Mook_(publishing)'
kinds = [
 {"n": "Magazine", "a": "periodical · glossy · slick", "d": "Periodical issue bound as a stapled or perfect-bound paper-covered booklet; the page format is noted.",
  "t": ["saddle-stitched (stapled)", "perfect-bound", "standard (A4 / letter)", "digest size", "demitab", "first issue", "special or collector's issue", "with cover-mounted gift", "subscriber edition", "newsstand edition", "variant cover"],
  "s": "https://www.fujisan.co.jp/pub/2451/"},
 {"n": "Newspaper", "a": "", "d": "Periodical issued daily or weekly on unbound newsprint sheets; the page format is noted.",
  "t": ["broadsheet", "Nordisch", "Rhenish", "Swiss", "Berliner", "tabloid / compact", "daily", "weekly", "Sunday edition", "first or last issue", "special or commemorative edition", "supplement"],
  "s": "https://www.europeana.eu/en/stories/a-variety-of-newspaper-formats"},
 {"n": "Pulp magazine", "a": "pulp · the pulps", "d": "Cheap fiction magazine of about 1896–1955 printed on rough wood-pulp paper, about 7 × 10 inches, with untrimmed edges and a colour cover.",
  "t": ["standard pulp size", "digest size", "untrimmed edges", "adventure", "detective", "science fiction", "weird and horror", "western", "romance", "hero pulp", "UK pulp"],
  "s": PULP,
  "x": [
   X("General fiction pulp", "All-fiction magazine on untrimmed pulp paper, the format that founded the pulps.", "Frank A. Munsey Company", "1896", PULP,
     [("Argosy", "Frank A. Munsey Company", "1896", "first pulp: all-fiction on pulp paper, about 135,000 words an issue")], dt="issue date · cover · condition"),
   X("Science-fiction and fantasy pulp", "Genre pulp devoted to weird fiction, fantasy or science fiction.", "", "1923", HSF,
     [("Weird Tales", "Rural Publishing", "1923", "first issue dated March 1923; weird and fantasy fiction"),
      ("Amazing Stories", "Hugo Gernsback", "1926", "dated April 1926; first magazine devoted to science fiction"),
      ("Astounding Stories of Super-Science", "William Clayton", "1930", "January 1930; to Street & Smith 1933; digest from November 1943")],
     dt="issue date · cover artist · condition"),
   X("Hero and detective pulp", "Pulp built around a recurring character or the detective genre, the mass-market core of the 1930s.", "", "", PULP,
     [("Street & Smith hero pulps", "Street & Smith", "", "Doc Savage, The Shadow"), ("Popular Publications pulps", "Popular Publications", "", "The Spider, G-8, Black Mask")],
     dt="issue date · cover · condition"),
  ]},
 {"n": "Part-work", "a": "partwork · collection series", "d": "Publication issued as numbered magazine-like parts, weekly or monthly, that together build one complete work or collection; binders and models are sold apart.",
  "t": ["with cover-mounted item", "build-up model", "figurine collection", "die-cast vehicle collection", "DVD collection", "encyclopedia", "with binder", "complete run", "first issue (discounted)"],
  "s": "https://onixref.com/codelists/150",
  "x": [
   X("Build-up model partwork", "Partwork whose issues each carry parts that together build one large static model.", "", "", PW,
     [("Model aircraft partwork", "", "2009", "UK: 125 issues, £620.25 in all")], dt="issue count · completeness · binder"),
   X("Collectable model partwork", "Partwork with a finished figurine or die-cast vehicle on every issue, collected as a series.", "", "", PW,
     [("De Agostini collections", "De Agostini", "", "largest partwork publisher, about half the world market"), ("Eaglemoss collections", "Eaglemoss", "", "figurines and models"), ("Hachette collections", "Hachette Partworks", "", "")],
     dt="series · issue number · model in box"),
   X("Part-issued book", "Book or reference work first sold in monthly or weekly parts, from the 18th-century histories to Victorian novels and 20th-century encyclopedias.", "", "1728", PW,
     [("Monthly parts", "", "1836", "Victorian novels in about 19 monthly parts"), ("Weekly parts", "", "1840", ""), ("Serial encyclopedia", "", "", "mid-20th century")],
     dt="parts complete · wrappers · bound or unbound"),
  ]},
 {"n": "Bookazine", "a": "mook · magazine book", "d": "One-off magazine-style publication with a book number, sold in bookshops and newsstands, often in a numbered series.",
  "t": ["one-off special", "numbered series", "with ISBN", "with ISSN", "with free gift (furoku)"],
  "s": "https://www.kadokawa.co.jp/label-list/",
  "x": [
   X("Mook", "Magazine-like publication meant to stay on bookshop shelves longer than a magazine, a large category in Japan.", "", "1971", MOOK,
     [("Term coined", "", "1971", "at a FIPP convention"), ("Japanese mook", "", "", "new titles peaked at over 8,000 in 2013")], dt="series · ISBN · gift"),
   X("Newsstand bookazine", "Single-topic, book-shaped magazine sold at newsagents, usually in themed series.", "Imagine Publishing", "", IMG,
     [("Imagine bookazines", "Imagine Publishing", "", "over 800 titles by 2016"), ("Made Simple", "Future", "2015", "148 pages"), ("Handbook", "Future", "2015", "180 pages"),
      ("Guru Guide", "Future", "2015", "180 pages"), ("Technology Tips Guide", "Future", "2015", "148 pages")], dt="series · edition · page count"),
  ]},
 {"n": "Zine", "a": "fanzine · perzine", "d": "Small self-published or fan-made periodical, usually photocopied in runs of under a thousand and stapled.",
  "t": ["photocopied", "offset printed", "hand-made", "numbered issue", "perzine", "art zine", "photo zine", "minicomic"],
  "s": "https://antiquatedfuture.com/about/faqs/",
  "x": [
   X("Science-fiction fanzine", "Amateur magazine by science-fiction fans, the origin of the fanzine form and of the word itself.", "", "1930", ZN,
     [("The Comet", "", "1930", "often cited as the first science-fiction fanzine"), ("Detours", "", "1940", "where the word fanzine was coined"), ("Media fanzine", "", "1967", "fan fiction about a TV series")],
     dt="issue number · duplicating method"),
   X("Punk zine", "Photocopied cut-and-paste music fanzine of the late-1970s punk scene and its successors.", "", "1976", ZN,
     [("Sniffin' Glue", "", "1976", "first UK punk zine; 12 photocopied issues")], dt="issue number · print run"),
   X("Riot grrrl zine", "Feminist punk zine of the 1990s riot grrrl movement.", "", "1990", ZN, [], dt="issue number"),
  ]},
 {"n": "Bound periodical volume", "a": "bound run · half-year volume", "d": "Book-form volume binding together a run of issues of one periodical.",
  "t": ["publisher's cloth case", "half-year volume", "annual volume", "several volumes bound in one", "half leather rebinding", "library binding", "ex-library", "complete run"],
  "s": "https://www.commoncrowbooks.com/pages/books/z08937/j-t-herbert-bailey-ralph-neville-thomas-rowlandson/the-connoisseur-a-magazine-for-collectors-january-april-1902-bound-in-one-volume",
  "x": [
   X("Publisher's half-year volume", "Six months of a weekly or monthly bound by its publisher in a uniform case, the typical Victorian bound run.", "", "", STRAND,
     [("Punch", "Punch Office", "1841", "two volumes a year; red pebble-cloth sets of four volumes in one"),
      ("The Strand Magazine", "George Newnes Ltd", "1891", "January–June and July–December volumes, 118 in all to 1950"),
      ("The Illustrated London News", "", "1842", "first illustrated weekly newspaper, founded by Herbert Ingram")],
     dt="volume number · binding · condition"),
  ]},
]
brands = [
 {"n": "Frank A. Munsey Company", "c": "United States", "f": "", "seg": "Heritage manufactory", "kf": "pulp magazines", "d": "Frank Munsey's New York publisher of Argosy, the first pulp magazine.", "sig": ["General fiction pulp"], "s": PULP},
 {"n": "Street & Smith", "c": "United States", "f": "", "seg": "Mainstream", "kf": "pulp magazines", "d": "New York pulp publisher of hero pulps and, from 1933, Astounding; moved most titles to slick format in 1949.", "s": PULP},
 {"n": "Popular Publications", "c": "United States", "f": "", "seg": "Mainstream", "kf": "pulp magazines", "d": "American pulp publisher of hero, detective and horror titles.", "s": PULP},
 {"n": "Rural Publishing", "c": "United States", "f": "", "seg": "Specialist", "kf": "weird fiction", "d": "Publisher owned by J. C. Henneberger that launched Weird Tales in 1923.", "s": HSF},
 {"n": "De Agostini", "c": "Italy", "f": "1901", "seg": "Mainstream", "kf": "partworks", "d": "Italian publisher holding about half of the world partwork market.", "s": K},
 {"n": "Eaglemoss", "c": "United Kingdom", "f": "", "seg": "Specialist", "kf": "figurine partworks", "d": "British partwork publisher of figurine and model collections.", "s": PW},
 {"n": "Hachette Partworks", "c": "United Kingdom", "f": "", "seg": "Mainstream", "kf": "partworks", "d": "Partwork arm of the Hachette group publishing collectable series.", "s": PW},
 {"n": "GE Fabbri", "c": "United Kingdom", "f": "", "seg": "Mainstream", "kf": "partworks", "d": "Partwork publisher.", "s": PW},
 {"n": "Marshall Cavendish", "c": "United Kingdom", "f": "", "seg": "Mainstream", "kf": "partworks", "d": "Publisher known for partwork encyclopedias.", "s": PW},
 {"n": "Future", "c": "United Kingdom", "f": "1985", "seg": "Mainstream", "kf": "magazines, bookazines", "d": "British magazine and website publisher that bought bookazine specialist Imagine Publishing in 2016.", "lines": ["Made Simple", "Handbook", "Guru Guide", "Technology Tips Guide"], "rel": ["Imagine Publishing"], "s": IMG},
 {"n": "Imagine Publishing", "c": "United Kingdom", "f": "", "seg": "Specialist", "kf": "bookazines", "d": "Bournemouth publisher of over 800 bookazines, acquired by Future in 2016.", "sig": ["Newsstand bookazine"], "rel": ["Future"], "s": IMG},
 {"n": "Punch Office", "c": "United Kingdom", "f": "1841", "seg": "Heritage manufactory", "kf": "Punch", "d": "London publisher of the humorous weekly Punch, issuing it also in bound half-year volumes.", "s": PUNCH},
 {"n": "George Newnes Ltd", "c": "United Kingdom", "f": "", "seg": "Mainstream", "kf": "illustrated magazines", "d": "London publisher of The Strand Magazine from 1891 to 1950.", "s": STRAND},
]
notes = ("All six old kinds kept; Pulp magazine added (format kind, with Argosy, Weird Tales, Amazing Stories and Astounding as exemplar versions under format archetypes). "
         "Newspaper formats (broadsheet, Berliner, tabloid etc.) are t. Partwork publishers De Agostini, Eaglemoss, Hachette, GE Fabbri, Marshall Cavendish are brands; no partwork series named. "
         "Zine archetypes: SF fanzine, punk zine, riot grrrl zine. Bound volumes: Punch, Strand, ILN as typical publisher's half-year runs. Mook folded into Bookazine as archetype. "
         "Bedsheet pulp size left out (not confirmed on a fetched page). Founding years omitted where not confirmed; De Agostini 1901 and Future 1985 from knowledge/fetched page.")
out = {"kinds": kinds, "brands": brands, "traditions": [], "notes": notes}
p = 'work/F1/shelves/04_00.json'
json.dump(out, open(p + '.tmp', 'w'), ensure_ascii=False, indent=1); os.replace(p + '.tmp', p)
print('written')
