import json, os
W = 'https://en.wikipedia.org/wiki/'
NUT = W + 'Nutcracker_doll'; RAU = W + 'Räuchermann'; PYR = W + 'Christmas_pyramid'; SCH = W + 'Schwibbogen'
HINA = W + 'Hina_doll'; CDJ = W + 'Children%27s_Day_(Japan)'; KOK = W + 'Kokeshi'; MAT = W + 'Matryoshka_doll'
DALA = W + 'Dala_horse'; DAR = W + 'Daruma_doll'; SNOW = W + 'Snow_globe'; KAD = W + 'Kadomatsu'
SEIF = W + 'Seiffen'; ORN = W + 'Christmas_ornament'; WK = W + 'Wendt_%26_K%C3%BChn'
STEIN = 'https://www.deseret.com/2001/12/7/19620478/nutcracker-king'
ULB = 'https://www.dwell.com/product/christian-ulbricht-nutcracker-5be6af5b'
PERZY = 'https://www.viennadesignweek.at/en/player/erwin-perzys-original-wiener-schneekugeln/'
GRAN = 'https://www.teknos.com/industrial-coatings/showroom/case-dala-horses/'
NILS = 'https://webshop.skansen.se/en/brands/nils-olsson-hemslojd'
KYU = 'https://www.kyugetsu.com/en/company-profile/company-history/'


def X(n, d, s, mk='', y='', v=None, dt='', a=''):
    return {"n": n, "a": a, "d": d, "mk": mk, "y": y, "s": s, "v": v or [], "dt": dt}


def V(n, mk='', y='', d=''):
    return {"n": n, "mk": mk, "y": y, "d": d}


kok_styles = [
    ("Tōgatta kokeshi", "Style of Tōgatta Onsen (Zaō, Miyagi), where kijishi lathe-turners near Shinchi Shuraku first made kokeshi."),
    ("Naruko kokeshi", "Style of Naruko Onsen (Ōsaki, Miyagi); the most widespread traditional type, also made in Akita, Iwate and Yamagata."),
    ("Tsuchiyu kokeshi", "Style of Tsuchiyu, Iizaka and Dake onsen in Fukushima."),
    ("Yajirō kokeshi", "Style of Yajirō village, Shiroishi, Miyagi."),
    ("Sakunami kokeshi", "Style of Sakunami Onsen near Sendai and of Yamagata, Yonezawa, Sagae and Tendō (Yamagata-Sakunami)."),
    ("Zaō Takayu kokeshi", "Style of Zaō Onsen, Yamagata."),
    ("Hijiori kokeshi", "Style of Hijiori Onsen, Ōkura, Yamagata."),
    ("Kijiyama kokeshi", "Style of Kijiyama, Yuzawa, Akita."),
    ("Nambu kokeshi", "Style of Morioka and Hanamaki Onsen, Iwate."),
    ("Tsugaru kokeshi", "Style of Nuruyu and Ōwani onsen, Aomori; also called Nuruyu type."),
]

kinds = [
 {"n": "Nutcracker figure", "a": "Erzgebirge nutcracker · Nussknacker",
  "d": "Turned and painted wooden figure whose hinged jaw cracks nuts, kept mainly as Christmas decoration.",
  "t": ["working", "decorative only"], "s": NUT,
  "x": [
   X("Erzgebirge soldier or king nutcracker", "Brightly painted lathe-turned figure of a soldier, king, miner or policeman, the classic Ore Mountains form.", NUT,
     y="late 17th century",
     v=[V("First series production on the lathe", "Füchtner", "1872", "Friedrich Wilhelm Füchtner's workshop in Seiffen, Saxony")],
     dt="figure: soldier, king, miner, policeman · about 60 parts · working jaw or decorative only"),
   X("Steinbach collectible character nutcracker", "Limited-edition character nutcracker from the Steinbach family firm, the start of modern nutcracker collecting.", STEIN,
     mk="Steinbach", y="1991",
     v=[V("Merlin the Magician", "Steinbach", "1991", "limited edition; called the first modern collectible nutcracker"),
        V("Herr Drosselmeyer", "Steinbach", "", "early figures resell for over $3,000 (2001)"),
        V("Mouse King", "Steinbach", "", "Nutcracker ballet character")],
     dt="about 200 styles, 10–15 new characters a year (2001) · limited editions · licensed lines (Wizard of Oz, Disney)"),
   X("Christian Ulbricht nutcracker", "Nutcracker from the Ulbricht family workshop, founded in Seiffen, rebuilt in Lauingen after the war and back in Seiffen from 1990.", ULB,
     mk="Christian Ulbricht", y="1928", dt="characters: soldiers, kings, Santas, trades · sizes small to extra large"),
  ]},
 {"n": "Smoking figure", "a": "Räuchermann · incense smoker · smoking man",
  "d": "Two-part hollow wooden figure that hides a burning incense cone and puffs smoke from its mouth.", "s": RAU,
  "x": [
   X("Räuchermann", "Ore Mountains smoker figure of a regional craftsman, first recorded in 1850.", RAU, y="1850",
     dt="figures: forester, peddler, miner, soldier · takes standard incense cones (Räucherkerzen)"),
   X("Edge-sitter smoker", "Smoker figure made to sit on the edge of a table or shelf.", RAU),
   X("Räucherfrau", "Female smoker figure.", RAU),
   X("Multi-figure smoker scene", "Smoker with several figures in one scene, such as men playing Skat.", RAU),
  ]},
 {"n": "Christmas pyramid", "a": "Weihnachtspyramide",
  "d": "Wooden carousel of tiers carrying carved figures, turned by a rotor driven by the heat of candles.",
  "t": ["candle-driven", "electric"], "s": PYR,
  "x": [
   X("Ore Mountains table pyramid", "Four- to eight-sided wooden carousel with one or more tiers of figures around a central axle and a candle-driven rotor.", PYR,
     y="late 18th century",
     v=[V("Lichtergestelle (light stand)", "", "18th century", "forerunner of the pyramid")],
     dt="tiers 1–several · 4–8 sides · motifs: nativity, angels, wise men, miners, forest · pine-cone or star finial"),
  ]},
 {"n": "Candle arch", "a": "Schwibbogen · Erzgebirge candle arch",
  "d": "Arched candle holder from the Ore Mountains, filled with a cut-out scene, set in windows at Christmas.",
  "t": ["wood", "metal", "candle", "electric"], "s": SCH,
  "x": [
   X("Johanngeorgenstadt forged arch", "Original form: a single forged black-metal arch holding eleven candles, made in Johanngeorgenstadt in 1740.", SCH, y="1740",
     dt="forged black metal, may be painted · 11 candles"),
   X("Schwarzenberg miners' arch", "Best-known design, made in 1937 for a show in Schwarzenberg, with miners, wood carver, lace maker, tree, hammers, swords and angel.", SCH,
     y="1937", dt="7 candles · usually wood today · modern variants show landscapes, skylines, religious or local scenes"),
  ]},
 {"n": "Festival doll display", "a": "hina-ningyō · gogatsu-ningyō · sekku dolls",
  "d": "Set of dolls made to be displayed on tiers for a festival, not made for worship.",
  "t": ["imperial pair only", "tiered set (hinadan)", "cased display"],
  "s": "https://item.rakuten.co.jp/ningyoyahonpo/c/0000000408/",
  "x": [
   X("Hina-ningyō", "Dolls in Heian court dress displayed for Hinamatsuri (3 March), from the imperial pair to a seven-tier set.", HINA, y="c. 1629",
     v=[V("Momoyama-bina", "Kimura Isshu"), V("Yorokobi-bina", "Kyugetsu"), V("Koun-bina", "Mataro Ningyo"),
        V("Shiho-bina", "Mataro Ningyo"), V("Kirameki", "")],
     dt="dairi-bina pair to seven tiers and fifteen dolls with miniature furniture · Kantō vs Kansai arrangement · Kyoto vs rest-of-Japan accessories"),
   X("Gogatsu-ningyō", "May dolls and miniature armour displayed for Children's Day (5 May) to wish boys protection.", CDJ,
     y="Kamakura–Muromachi period",
     v=[V("Yoroi-kazari (miniature armour)", "", "", "usually ō-yoroi or dō-maru style"),
        V("Kabuto-kazari (helmet)", "", "", "some sized to be worn; miniature kabuto popular since the 2000s"),
        V("Musha ningyō (warrior doll)", "", "Edo period", "subjects include Kintarō, Momotarō, Benkei, Shoki")],
     dt="tiered display with bow, long sword, war fan · paired with koinobori outdoors"),
  ]},
 {"n": "Kokeshi", "a": "kokeshi doll",
  "d": "Limbless lathe-turned wooden doll with a round head, from the hot-spring towns of Tōhoku, Japan.", "s": KOK,
  "x": [X(n, d + " Traditional (dentō) kokeshi.", KOK, y="mid-Edo period" if i == 0 else "",
          dt="woods: cherry, dogwood, itaya maple") for i, (n, d) in enumerate(kok_styles)] + [
   X("Sōsaku kokeshi", "Creative kokeshi made after 1945, free in shape, design and colour and not tied to a region.", KOK, y="after 1945",
     a="shingata kokeshi", dt="shown at the Creative Kokeshi Exhibition in Shibukawa and a Tokyo competition")]},
 {"n": "Matryoshka", "a": "Russian nesting doll · matryoshka doll",
  "d": "Set of lathe-turned wooden dolls of decreasing size that nest inside one another.", "s": MAT,
  "x": [
   X("Malyutin–Zvyozdochkin original", "First Russian nesting set, turned by Vasily Zvyozdochkin to Sergey Malyutin's design at the Children's Education Workshop, Moscow.", MAT,
     y="1890s", dt="8 dolls · linden wood"),
   X("Sergiev Posad matryoshka", "Style of Sergiev Posad (Zagorsk 1930–91), where production moved after the Moscow workshop closed.", MAT),
   X("Semyonov matryoshka", "Style of Semyonov, known for a standard six-piece set five inches tall.", MAT, dt="6 pieces · 5 in"),
   X("Polkhovsky Maidan matryoshka", "Style of Polkhovsky Maidan, the main producer of matryoshka blanks, with Krutets and Gorodets.", MAT),
   X("Kirov (Vyatka) matryoshka", "Style of Kirov, formerly Vyatka; Nolinsk and Yoshkar-Ola are nearby centres.", MAT),
  ]},
 {"n": "Dala horse", "a": "Dalecarlian horse · dalahäst",
  "d": "Carved, painted wooden horse from Dalarna, Sweden, decorated in the kurbits style.", "s": DALA,
  "x": [
   X("Nusnäs Dala horse", "Pine horse carved in the Mora parish villages, now mainly Nusnäs, painted red-orange with kurbits flowers.", DALA,
     v=[V("Grannas A. Olsson", "Grannas A. Olssons Hemslöjd", "1922", "oldest maker still active; 17 sizes 1–50 cm"),
        V("Nils Olsson", "Nils Olssons Hemslöjd", "1928", "hand-carved and hand-painted")],
     dt="pine from around Lake Siljan · originally iron-oxide red, now reddish orange with white, green, yellow, blue · other colours exist · sizes 1–50 cm"),
  ]},
 {"n": "Daruma", "a": "daruma doll",
  "d": "Round, hollow, weighted papier-mâché figure of Bodhidharma with blank eyes filled in to mark a wish.", "s": DAR,
  "x": [
   X("Takasaki daruma", "Red self-righting daruma tied to Shōrinzan Daruma-ji, Takasaki; the city claims 80% of Japan's daruma.", DAR, y="1764–72",
     dt="sizes small to large · red traditional; gold and other colours"),
   X("Matsukawa daruma", "Slender, usually blue Sendai daruma sold with eyes already painted, on a treasure-ship base.", DAR),
   X("Hime daruma", "Feminine princess or lady form of daruma.", DAR, a="Onna daruma"),
   X("Triangle daruma", "Cone-based daruma that stands upright when tilted.", DAR, y="1956",
     v=[V("Triangle daruma", "Tokushiro Imai", "1956", "developer")]),
   X("Goshiki daruma", "Set of five daruma in blue, yellow, red, white and black.", DAR),
  ]},
 {"n": "Snow globe", "a": "snow dome · Schneekugel",
  "d": "Sealed liquid-filled globe holding a scene and loose particles that fall when shaken.",
  "t": ["glass", "plastic", "musical"], "s": SNOW,
  "x": [
   X("Viennese snow globe", "Hand-made glass snow globe from Erwin Perzy's Vienna workshop, which popularised the form.", PERZY,
     mk="Erwin Perzys Original Wiener Schneekugeln", y="1900",
     v=[V("Mariazell pilgrimage church", "Erwin Perzys Original Wiener Schneekugeln", "", "first motif")],
     dt="over 300 motifs · glass globe · made in Vienna-Hernals"),
   X("Water-filled paperweight globe", "Early form: hollow glass paperweight with water and white powder imitating a snowstorm, shown in Paris in 1878.", SNOW, y="1878"),
   X("Plastic snow globe", "Mass-produced plastic globe introduced in the 1950s, now chiefly from Hong Kong and China.", SNOW, y="1950s"),
  ]},
 {"n": "Entrance decoration", "a": "kadomatsu",
  "d": "Seasonal arrangement made to stand at an entrance for a festival.",
  "s": "https://en.pinkoi.com/product/JGCuUwNX",
  "x": [
   X("Kadomatsu", "Pair of New Year arrangements of three cut bamboo stalks with pine, often plum, bound in straw, set either side of a door.", KAD,
     v=[V("Kantō style"), V("Kansai style"), V("Kyoto style"), V("Shimane flat-topped style")],
     dt="bamboo, pine, ume · straw mat and rope binding · plastic versions · shown late December to 7 January"),
  ]},
]

brands = [
 {"n": "Steinbach", "c": "Germany", "f": "1832", "seg": "Erzgebirge nutcrackers", "d": "Family firm from the Ore Mountains, led by Christian Steinbach, maker of collectible nutcrackers.",
  "lines": ["Nutcrackers", "limited editions"], "eras": ["Christian Steinbach, fifth generation"], "sig": ["Steinbach collectible character nutcracker"], "sc": [], "rel": [], "s": STEIN},
 {"n": "Christian Ulbricht", "c": "Germany", "f": "1928", "seg": "Erzgebirge wood art", "d": "Family workshop founded by Otto Ulbricht in Seiffen, rebuilt in Lauingen, Bavaria, and back in Seiffen from 1990.",
  "lines": ["Nutcrackers"], "eras": ["Otto Ulbricht, from 1928", "Christian Ulbricht"], "sig": ["Christian Ulbricht nutcracker"], "sc": [], "rel": [], "s": ULB},
 {"n": "Wendt & Kühn", "c": "Germany", "f": "1915", "seg": "Erzgebirge figures", "d": "Grünhainichen workshop founded by Grete Wendt and Margarete Kühn, known for painted wooden figures and music boxes.",
  "lines": ["Grünhainichen angels", "flower children", "music boxes"], "eras": [], "sig": ["Grünhainichen angel"], "sc": [], "rel": [], "s": WK},
 {"n": "Erwin Perzys Original Wiener Schneekugeln", "c": "Austria", "f": "1900", "seg": "Snow globes", "d": "Vienna family workshop of snow-globe inventor Erwin Perzy, run by the third generation.",
  "lines": ["Snow globes", "New Year lead-casting charms"], "eras": ["Erwin Perzy I", "Erwin Perzy III"], "sig": ["Viennese snow globe"], "sc": [], "rel": [], "s": PERZY},
 {"n": "Grannas A. Olssons Hemslöjd", "c": "Sweden", "f": "1922", "seg": "Dala horses", "d": "Nusnäs family business, the oldest company still making Dala horses.",
  "lines": ["Dala horses"], "eras": [], "sig": ["Nusnäs Dala horse"], "sc": [], "rel": ["Nils Olssons Hemslöjd"], "s": GRAN},
 {"n": "Nils Olssons Hemslöjd", "c": "Sweden", "f": "1928", "seg": "Dala horses", "d": "Nusnäs family workshop founded by brothers Nils and Jannes Olsson, hand-carving Dala horses.",
  "lines": ["Dala horses"], "eras": [], "sig": ["Nusnäs Dala horse"], "sc": [], "rel": ["Grannas A. Olssons Hemslöjd"], "s": NILS},
 {"n": "Kyugetsu", "c": "Japan", "f": "1835", "seg": "Festival dolls", "d": "Tokyo hina-doll wholesaler and maker founded by Kyuzaemon Yokoyama, selling hina and May dolls.",
  "lines": ["Hina dolls", "Gogatsu dolls"], "eras": [], "sig": ["Hina-ningyō"], "sc": [], "rel": [], "s": KYU},
]

traditions = [
 {"n": "Erzgebirge woodcraft", "g": "Woodwork & furniture", "r": "Ore Mountains, Saxony, Germany", "p": "late 17th century–present",
  "d": "Wooden toy and Christmas-figure making that replaced declining ore mining around Seiffen.",
  "tech": "lathe turning incl. Reifendrehen (ring turning), carving, painting", "mat": "wood",
  "forms": ["Nutcracker figure", "Smoking figure", "Christmas pyramid", "Candle arch"],
  "ctr": ["Seiffen", "Grünhainichen", "Ore Mountain Toy Museum, Seiffen", "Auguste Müller (carver)"],
  "auth": "Maker's stamp or label from an Ore Mountains workshop; hand-turned and hand-painted parts", "s": SEIF},
 {"n": "Kokeshi", "g": "Woodwork & furniture", "r": "Tōhoku, Japan", "p": "mid-Edo period–present",
  "d": "Lathe-turned limbless dolls first sold by kijishi turners to hot-spring visitors, in regional styles tied to onsen.",
  "tech": "lathe turning, hand painting", "mat": "cherry, dogwood, itaya maple",
  "forms": ["Kokeshi"], "ctr": ["Tōgatta", "Naruko", "Tsuchiyu", "Yajirō", "Sakunami", "Zaō", "Hijiori", "Kijiyama", "Nambu", "Tsugaru"],
  "auth": "Traditional pieces follow the shape and painting of their onsen style", "s": KOK},
 {"n": "Dalecarlian horse", "g": "Woodwork & furniture", "r": "Dalarna, Sweden", "p": "present centre Nusnäs; known abroad since 1939",
  "d": "Carved pine horses painted in the kurbits style, a symbol of Dalarna and Sweden.",
  "tech": "band-saw cutting, hand carving, kurbits painting", "mat": "slow-grown pine",
  "forms": ["Dala horse"], "ctr": ["Nusnäs", "Bergkarlås", "Risa", "Vattnäs", "Grannas A. Olssons Hemslöjd", "Nils Olssons Hemslöjd"],
  "auth": "Hand-painted kurbits so no two are identical; maker's label from a Nusnäs workshop", "s": DALA},
 {"n": "Matryoshka", "g": "Woodwork & furniture", "r": "Russia", "p": "1890s–present",
  "d": "Nesting dolls turned in linden and painted in regional styles.",
  "tech": "lathe turning, painting", "mat": "linden",
  "forms": ["Matryoshka"], "ctr": ["Sergiev Posad", "Semyonov", "Polkhovsky Maidan", "Kirov (Vyatka)", "Nolinsk", "Yoshkar-Ola"],
  "auth": "Turned, not carved from one block; regional painting style", "s": MAT},
 {"n": "Lauscha glass", "g": "Ceramics & glass", "r": "Lauscha, Thuringia, Germany", "p": "16th century–present",
  "d": "Mould-blown, silvered and hand-painted glass Christmas ornaments, exported worldwide from the 1840s.",
  "tech": "lamp-blowing into clay moulds, silver-nitrate silvering, hand painting", "mat": "glass, silver nitrate",
  "forms": ["Tree ornament"], "ctr": ["Lauscha", "Hans Greiner"],
  "auth": "Blown in Lauscha by one of the small family glass-blowing firms (about 20 in 2009)", "s": ORN},
 {"n": "Hina-ningyō", "g": "Textiles & dolls", "r": "Japan", "p": "c. 1629–present",
  "d": "Festival dolls in Heian court dress displayed on tiers for Hinamatsuri.",
  "tech": "carved and dressed doll making, from folded paper to carved figures", "mat": "wood, silk, paper",
  "forms": ["Festival doll display"], "ctr": ["Kyoto", "Edo/Tokyo (Asakusabashi)", "Kyugetsu"],
  "auth": "Arrangement follows Kantō or Kansai convention; court dress follows Heian style", "s": HINA},
 {"n": "Takasaki daruma", "g": "Faith traditions", "r": "Takasaki, Gunma, Japan", "p": "1764–present",
  "d": "Papier-mâché daruma made from the charm moulds of Shōrinzan Daruma-ji.",
  "tech": "papier-mâché over moulds, weighted base, painting", "mat": "paper",
  "forms": ["Daruma"], "ctr": ["Shōrinzan Daruma-ji, Takasaki"],
  "auth": "Takasaki-made, sold with blank eyes", "s": DAR},
]

notes = ("All 11 planned kinds kept. Old festival-doll models became versions of the Hina-ningyō archetype. "
         "Left out: Wendt & Kühn and Ulbricht smoker/pyramid lines (no confirming page; kaethe-wohlfahrt.com was captcha-blocked), "
         "named Steinbach lines beyond the three in the Deseret article, specific matryoshka painting motifs and Perzy patent year (sources disagree), "
         "Iwatsuki and kimekomi hina styles (not on fetched pages), large market-square pyramids (public, not owned). "
         "Grünhainichen angel listed as a Wendt & Kühn signature for the Christmas or figurine shelf to pick up.")

out = {"kinds": kinds, "brands": brands, "traditions": traditions, "notes": notes}
p = 'work/B4/shelves/03_01.json'
os.makedirs('work/B4/shelves', exist_ok=True)
json.dump(out, open(p + '.tmp', 'w'), ensure_ascii=False, indent=1)
os.replace(p + '.tmp', p)
print('written', len(kinds), 'kinds', sum(len(k.get('x', [])) for k in kinds), 'archetypes')
