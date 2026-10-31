import json, os
W = 'https://en.wikipedia.org/wiki/'
HB = W + 'Handbag'
def X(n, a, d, mk, y, s, v=(), dt=''):
    return {"n": n, "a": a, "d": d, "mk": mk, "y": y, "s": s,
            "v": [dict(n=a1, mk=b, y=c, d=e) for a1, b, c, e in v], "dt": dt}

shoulder = {"n": "Shoulder bag", "a": "", "d": "Bag on a single strap worn on one shoulder.",
  "t": ["chain strap", "leather strap", "flap", "zip top"], "s": HB,
  "x": [
    X("Chanel 2.55", "Classic Flap · 11.12 · Reissue 2.55", "Quilted flap bag on a chain shoulder strap, named for its February 1955 creation date.",
      "Chanel", "1955", W + "Chanel_2.55",
      [("2.55 (original)", "Chanel", "1955", "Coco Chanel; Mademoiselle lock, burgundy lining, double-chain strap"),
       ("11.12 (Classic Flap)", "Chanel", "1983", "Karl Lagerfeld; interlocking CC logo"),
       ("Reissue 2.55", "Chanel", "2005", "exact copy of the 1955 bag for its 50th anniversary")],
      "lock Mademoiselle or interlocking CC · diamond or herringbone quilting · leather or fabric colour · all-chain or leather-woven chain strap"),
    X("Chanel Boy", "Boy bag", "Boxy, straight-edged flap bag with a brick-style CC lock, named after Arthur 'Boy' Capel.",
      "Chanel", "2011", "https://www.sothebys.com/en/articles/chanel-boy-bag-the-it-girl-staple",
      [("Boy bag", "Chanel", "2011", "Karl Lagerfeld, Fall/Winter 2011")],
      "sizes mini, small, old medium, new medium, large, XL · classic, chevron, reverso or horizontal quilting · caviar, lambskin, patent, goatskin, tweed, denim; exotics until 2018"),
    X("Chanel 19", "19 bag", "Slouchy flap bag with enlarged diamond quilting and a three-tone chain strap, a homage to the 2.55.",
      "Chanel", "2019", "https://www.sothebys.com/en/articles/the-chanel-19-the-newest-must-have-chanel-bag",
      [("19", "Chanel", "2019", "Karl Lagerfeld with Virginie Viard, Fall/Winter 2019")],
      "sizes small, medium, maxi · lambskin, goatskin, tweed, denim · silver, aged gold and ruthenium hardware"),
    X("Prada Re-Edition", "Re-Edition 2005 · Re-Edition 2000", "Small nylon shoulder bag with Saffiano leather trim, reissued from Prada's early-2000s nylon bags.",
      "Prada", "2005", "https://rebag.com/thevault/?p=5010",
      [("Bandoliera Tessuto", "Prada", "2005", "original nylon shoulder bag the Re-Edition 2005 is based on"),
       ("Re-Edition 2005", "Prada", "", "removable crossbody strap, chain, clip-on coin pouch"),
       ("Re-Edition 2000 Mini", "Prada", "", "fabric strap, more rigid body, leather name tag")],
      "nylon with Saffiano leather · neutral, pastel and bright colours · ruched nylon version"),
    X("Celine Triomphe", "Triomphe bag", "Boxy flap bag closed by the gold Triomphe clasp, a revived founder-era logo inspired by the Arc de Triomphe.",
      "Celine", "Hedi Slimane era (2018–2024)", "https://www.fashionphile.com/blogs/academy/hedi-slimane-bags",
      [("Triomphe", "Celine", "", "Medium and Nano"), ("Triomphe chain bag", "Celine", "", "shiny calfskin"),
       ("Triomphe shoulder bag", "Celine", "", "")],
      "sizes Medium, Nano · calfskin"),
    X("Bottega Veneta Cassette", "Cassette", "Rectangular intrecciato-woven leather bag on a shoulder or cross-body strap.",
      "Bottega Veneta", "Daniel Lee era (2018–2021)", "https://signofthetimeslondon.com/blogs/sign-talk/the-new-bottega-veneta-brand-history-a-guide-to-bottegas-most-popular-bags-and-shoes",
      [("Cassette", "Bottega Veneta", "", "quilted, lightweight"), ("Padded Cassette", "Bottega Veneta", "", "cushioned oversized weave"),
       ("Chain Cassette", "Bottega Veneta", "", "gold or silver chain strap")],
      "intrecciato weave · padded or flat · leather colour · chain or leather strap"),
    X("Chloé Paddington", "Paddington", "East-west leather bag with a heavy padlock, the It bag of 2005.",
      "Chloé", "2005", "https://collections.vam.ac.uk/item/O1527573/paddington-handbag-handbag-chloe",
      [("Paddington", "Chloé", "2005", "Phoebe Philo; leather and metal (V&A example in tan)")],
      "leather colour · padlock"),
    X("Fendi Peekaboo", "Peekaboo", "Structured Fendi bag created by Silvia Venturini Fendi, a success compared with the Baguette.",
      "Fendi", "2009", W + "Fendi",
      [("Peekaboo", "Fendi", "2009", "Silvia Venturini Fendi")], ""),
    X("Mulberry Alexa", "Alexa", "Satchel-style Mulberry bag named after Alexa Chung, an It bag of its era.",
      "Mulberry", "Emma Hill era (2008–2013)", W + "Mulberry_(company)",
      [("Alexa", "Mulberry", "", "credited to Emma Hill")], ""),
    X("Givenchy Antigona", "Antigona", "Structured trapezoid bag with a detachable shoulder strap, named after Antigone.",
      "Givenchy", "2011", "https://ldj.com/blogs/blog/all-about-the-antigona",
      [("Antigona", "Givenchy", "2011", "Riccardo Tisci, Fall/Winter 2011"), ("Antigona Catchall", "Givenchy", "", "")],
      "sizes Baby, Nano, Mini, Small, Medium"),
    X("Coach Tabby", "Tabby", "Boxy shoulder bag with a C-turn lock, modernised from a 1970s Coach catalogue pouch.",
      "Coach", "1970s (original)", "https://www.lyst.co.uk/features/the-coach-tabby/",
      [("Tabby 26", "Coach", "", "everyday size"), ("Tabby 20", "Coach", "", "smaller size"),
       ("Pillow Tabby", "Coach", "", "soft padded version"), ("Chain Tabby", "Coach", "", "")],
      "sizes 20, 26 · pebble, nappa, soft grain, glovetanned leather, signature canvas, suede, denim"),
    X("Half-moon bag", "crescent bag · moon bag", "Crescent-shaped bag, a hybrid between a hobo and a shoulder bag; structured or slouchy.",
      "", "", "https://www.fashionphile.com/blogs/academy/crescent-bags",
      [("Ava", "Celine", "", "90s-inspired crescent, Triomphe canvas then calfskin"),
       ("Loop", "Louis Vuitton", "", "inspired by the early-2000s Croissant"),
       ("Ophidia Half Moon Hobo", "Gucci", "", "Mini and Small"),
       ("Le Cagole", "Balenciaga", "", "motorcycle bag reworked as a crescent"),
       ("Vibe Hobo", "Dior", "", "cannage pattern")],
      "structured or soft · size"),
  ],
  "m": [["Le Cœur", "Alaïa"], ["Le Teckel", "Alaïa"], ["Lily", "Mulberry"], ["Roxanne", "Mulberry"],
        ["The Brooklyn", "Demellier"], ["Scene", "Marc Jacobs"]]}

hobo = {"n": "Hobo bag", "a": "", "d": "Slouchy crescent-shaped bag on a single shoulder strap.", "s": HB,
  "x": [
    X("Gucci Jackie", "Jackie 1961 · Constance · New Jackie", "Half-moon hobo with a piston lock, named after Jacqueline Kennedy Onassis.",
      "Gucci", "1961", "https://harpersbazaar.my/fashion/the-history-of-the-hero-the-gucci-jackie-1961/",
      [("Constance", "Gucci", "1961", "original name of the bag"),
       ("Jackie (Tom Ford)", "Gucci", "1999", "piston lock replaced by a geometric buckle"),
       ("New Jackie", "Gucci", "", "Frida Giannini; larger, softer, piston detail restored; later Jackie Soft"),
       ("Jackie 1961", "Gucci", "2020", "Alessandro Michele; closer to the original, smaller, gold piston lock")],
      "sizes mini, small, medium · removable longer strap · colourway"),
    X("Bottega Veneta Jodie", "Jodie · Mini Jodie", "Slouchy intrecciato hobo with a knotted woven top handle, reported to be named after Jodie Foster.",
      "Bottega Veneta", "2020", "https://signofthetimeslondon.com/blogs/sign-talk/the-new-bottega-veneta-brand-history-a-guide-to-bottegas-most-popular-bags-and-shoes",
      [("Jodie", "Bottega Veneta", "2020", "Daniel Lee, Fall/Winter 2020"), ("Mini Jodie", "Bottega Veneta", "", "")],
      "sizes mini, large · intrecciato leather colour"),
    X("Halston bag", "littlest hobo", "Large, loosely structured leather hobo by accessories designer Bobby Breslau.",
      "", "1975", W + "Hobo_bag",
      [("The littlest hobo of them all", "Bobby Breslau", "1975", "smaller companion to the Halston bag")], ""),
  ],
  "m": [["Marcie", "Chloé"], ["Eva", "Tanner Krolle"]]}

baguette = {"n": "Baguette bag", "a": "", "d": "Small, long, narrow bag carried close under the arm on a short strap.", "s": HB,
  "x": [X("Fendi Baguette", "Baguette", "Small streamlined Fendi bag on a short strap, made in hundreds of designs and often called the first It bag.",
      "Fendi", "1997", W + "Baguette_(bag)",
      [("Baguette (original)", "Fendi", "1997", "Silvia Venturini Fendi"),
       ("Baguette relaunch", "Fendi", "2019", "again by Silvia Venturini Fendi"),
       ("FendiFrenesia", "Fendi", "2019", "scent built into the leather, with Francis Kurkdjian"),
       ("Men's Baguette", "Fendi", "", "")],
      "hundreds of materials, colours and embellishments")]}

saddle = {"n": "Saddle bag", "a": "", "d": "Bag shaped like a rider's saddlebag, with a curved body and front flap.", "s": HB,
  "x": [X("Dior Saddle", "Saddle bag", "Asymmetric saddle-shaped bag with a dangling 'D' charm and short strap.",
      "Dior", "1999", W + "Dior_Saddle_bag",
      [("Saddle (Galliano)", "Dior", "1999", "John Galliano, Spring/Summer 2000 show; denim, monogram, camouflage, newspaper print"),
       ("Saddle reissue", "Dior", "2018", "Maria Grazia Chiuri; calfskin, beading, patchwork florals"),
       ("Men's Saddle", "Dior", "2019", "Kim Jones for Dior Homme; all-metal limited edition")],
      "denim, leather, monogram or print · size · strap")]}

cross = {"n": "Crossbody bag", "a": "", "d": "Bag with a soft body and no front flap, on a strap worn across the body.", "s": HB,
  "m": [["Bang Bang", "Bottega Veneta"], ["Vanity", "Burberry"], ["Kye", "Khaite"]]}

messenger = {"n": "Messenger bag", "a": "courier bag", "d": "Crossbody bag with a full front flap and a wide gusset.", "s": HB,
  "x": [
    X("Manhattan Portage messenger bag", "Red Label messenger", "Cordura messenger first made for New York bike messengers and East Village DJs, with light buckles instead of metal.",
      "Manhattan Portage", "1983", "https://www.manhattanportage.com/about", [], "Cordura nylon · red label"),
    X("Timbuk2 Classic Messenger", "Classic Messenger", "Rectangular courier bag from San Francisco's bike-messenger scene, with a quick-adjust strap and custom colour panels.",
      "Timbuk2", "", "https://dk.wardow.com/collections/timbuk2-classic", [],
      "coated nylon or polyester · custom colour combinations · laptop compartment"),
    X("Chrome Citizen", "Citizen Messenger Bag", "Tarpaulin messenger with a seatbelt-buckle strap release that doubles as a bottle opener.",
      "Chrome Industries", "", W + "Chrome_Industries", [("Mini-Metro", "Chrome Industries", "", "smaller sibling with the same buckle")],
      "tarpaulin, Cordura · buckle"),
  ],
  "m": [["Kelly Messenger", "Hermès"]]}

def B(n, c, f, seg, d, s, eras=(), sig=(), lines=(), rel=()):
    return dict(n=n, c=c, f=f, seg=seg, d=d, lines=list(lines), eras=list(eras), sig=list(sig), sc=[], rel=list(rel), s=s)

brands = [
  B("Chanel", "France", "1910", "Luxury fashion house", "Paris house founded by Gabrielle 'Coco' Chanel.", W + "Chanel",
    ["Karl Lagerfeld, 1983–2019", "Virginie Viard, 2019–2024", "Matthieu Blazy, 2024–"], ["Chanel 2.55", "Chanel Boy", "Chanel 19"]),
  B("Dior", "France", "1946", "Luxury fashion house", "Paris couture house founded by Christian Dior.", W + "Dior",
    ["John Galliano, 1997–2011", "Raf Simons, 2012–2015", "Maria Grazia Chiuri, 2016–2025", "Jonathan Anderson, 2025–"], ["Dior Saddle"]),
  B("Fendi", "Italy", "1925", "Luxury fashion house", "Roman house founded by Adele and Edoardo Fendi.", W + "Fendi",
    ["Karl Lagerfeld, 1965–2019", "Silvia Venturini Fendi, accessories from 1994", "Kim Jones, 2020–2024"], ["Fendi Baguette", "Fendi Peekaboo"]),
  B("Gucci", "Italy", "1921", "Luxury fashion house", "Florentine house founded by Guccio Gucci.", W + "Gucci",
    ["Tom Ford, 1995–2004", "Frida Giannini, 2006–2015", "Alessandro Michele, 2015–2022", "Sabato De Sarno, 2023–2025", "Demna, 2025–"], ["Gucci Jackie"]),
  B("Prada", "Italy", "1913", "Luxury fashion house", "Milan house founded by Mario Prada; known for nylon bags from 1979.", W + "Prada",
    ["Miuccia Prada", "Raf Simons, co-creative director from 2020"], ["Prada Re-Edition"]),
  B("Celine", "France", "1945", "Luxury fashion house", "Paris house founded by Céline Vipiana.", W + "Celine_(brand)",
    ["Phoebe Philo, 2008–2018", "Hedi Slimane, 2018–2024", "Michael Rider, 2025–"], ["Celine Triomphe"]),
  B("Bottega Veneta", "Italy", "1966", "Luxury leather goods", "Vicenza house known for intrecciato woven leather.", W + "Bottega_Veneta",
    ["Tomas Maier, 2001–2018", "Daniel Lee, 2018–2021", "Matthieu Blazy, 2021–2024", "Louise Trotter, 2024–"], ["Bottega Veneta Cassette", "Bottega Veneta Jodie"]),
  B("Chloé", "France", "1952", "Luxury fashion house", "Paris house founded by Gaby Aghion.", W + "Chlo%C3%A9",
    ["Karl Lagerfeld, 1974–1988 and 1992–1996", "Phoebe Philo, 2001–2006", "Chemena Kamali, 2023–"], ["Chloé Paddington"]),
  B("Mulberry", "United Kingdom", "1971", "British luxury leather goods", "Somerset leather-goods house founded by Roger Saul.", W + "Mulberry_(company)",
    ["Emma Hill, 2008–2013"], ["Mulberry Alexa"]),
  B("Givenchy", "France", "1952", "Luxury fashion house", "Paris house founded by Hubert de Givenchy.", W + "Givenchy",
    ["Riccardo Tisci, 2005–2017", "Clare Waight Keller, 2017–2020", "Sarah Burton, 2024–"], ["Givenchy Antigona"]),
  B("Coach", "United States", "1941", "Accessible luxury leather goods", "New York leather-goods company.", W + "Coach_New_York",
    ["Bonnie Cashin, 1962–1974", "Reed Krakoff, 1997–2014", "Stuart Vevers, from 2013"], ["Coach Tabby"]),
  B("Timbuk2", "United States", "1989", "Messenger bags", "San Francisco bag maker founded by bike messenger Rob Honeycutt.", W + "Timbuk2",
    sig=["Timbuk2 Classic Messenger"], rel=["Chrome Industries", "Manhattan Portage"]),
  B("Chrome Industries", "United States", "1995", "Messenger bags", "Cycling bag maker from Colorado, now in Portland, using seatbelt buckles.", W + "Chrome_Industries",
    sig=["Chrome Citizen"], rel=["Timbuk2"]),
  B("Manhattan Portage", "United States", "1983", "Messenger bags", "New York bag brand begun with bags for bike messengers and DJs.", "https://www.manhattanportage.com/about",
    sig=["Manhattan Portage messenger bag"], rel=["Timbuk2"]),
]

notes = ("Messenger bag: dropped the Hermès 'Kelly' range row (Kelly is an archetype under Top-handle bag); kept 'Kelly Messenger' as a flat model. "
  "Gucci Jackie placed once, under Hobo bag (its half-moon hobo origin); Bottega Veneta Jodie also under Hobo; Cassette under Shoulder bag. "
  "Half-moon bag kept as maker-free archetype under Shoulder bag. Le Teckel, Le Cœur, Lily, Roxanne, Marcie, Eva, Bang Bang, Vanity, Kye, Brooklyn, Scene stay flat models: "
  "no retrieved page confirmed their history (Alaïa page has no bag info, so no Alaïa brand entry; no Burberry/Khaite entries since they have no archetypes). "
  "Not confirmed and left out: Celine Triomphe launch year, Prada Re-Edition relaunch years, Paddington 2025 relaunch, Alexa launch year, Timbuk2 Classic founding year of the model. "
  "No craft traditions apply to this shelf.")

out = {"kinds": [shoulder, hobo, baguette, saddle, cross, messenger], "brands": brands, "traditions": [], "notes": notes}
p = 'work/A4/shelves/00_02.json'
json.dump(out, open(p + '.tmp', 'w'), ensure_ascii=False, indent=1)
os.replace(p + '.tmp', p)
print('written')
