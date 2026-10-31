import json, os
WP = 'https://en.wikipedia.org/wiki/'
JS = WP + 'Japanese_sword'
def X(n, d, y, s, mk='', a='', v=None, dt=''):
    x = {"n": n, "a": a, "d": d, "mk": mk, "y": y, "s": s, "v": v or []}
    if dt: x["dt"] = dt
    return x
def V(n, mk='', y='', d=''):
    return {"n": n, "mk": mk, "y": y, "d": d}
def M(*l): return [list(t) for t in l]
VT = ["antique (kotō, shintō, shinshintō)", "gendaitō", "shinsakutō (licensed smith, since 1953)", "production replica"]
kinds = [
 {"n": "Katana", "a": "Japanese long sword · uchigatana", "d": "Curved single-edged Japanese long sword over 2 shaku (c. 60 cm), worn edge up through the sash.",
  "s": "https://www.kultofathena.com/product-category/swords/asian-swords/japanese-swords/katana/", "t": VT,
  "x": [
   X("Masamune", "Sōshū-school smith counted Japan's greatest; his tachi were mostly shortened into katana.", "c. 1288–1328 (late Kamakura)", WP + "Masamune", mk="Masamune",
     v=[V("Honjō Masamune", "Masamune", "", "Tokugawa heirloom; missing since 1946"), V("Kanze Masamune", "Masamune", "", "National Treasure, Tokyo National Museum"),
        V("Nakatsukasa Masamune", "Masamune", "", "National Treasure; once Honda Tadakatsu's"), V("Tsugaru Masamune", "Masamune", "", "National Treasure"),
        V("Ishida Masamune", "Masamune", "", "Important Cultural Property; named after Ishida Mitsunari"), V("Kotegiri Masamune", "Masamune", "", "Tokyo National Museum")],
     dt="Sōshū-den: nie crystals, suguha or notare hamon, chikei and kinsuji"),
   X("Sadamune", "Son and pupil of Masamune in the Sōshū school.", "14th c.", WP + "Katana", mk="Sadamune", v=[V("Kiriha Sadamune", "Sadamune", "", "")]),
   X("Muramasa", "Ise smith of the Muramasa school, famed for cutting ability and the 'cursed blade' legend.", "c. 1501 onward (Muromachi)", WP + "Muramasa", mk="Muramasa",
     v=[V("Myōhō Muramasa", "Muramasa", "1513", "only Muramasa designated an Important Artwork")], dt="gunome-midare hamon · fish-belly (tanagobara) tang"),
   X("Magoroku Kanemoto", "Mino-school smith rated Saijō Ō Wazamono for cutting.", "late Muromachi", JS, mk="Magoroku Kanemoto"),
   X("Nagasone Kotetsu", "Edo-period smith famed for strong blades; much counterfeited.", "c. 1597–1678 (shintō)", WP + "Nagasone_Kotetsu", mk="Nagasone Kotetsu",
     v=[V("Kotetsu katana with test-cut inscription", "Nagasone Kotetsu", "", "Tokyo Fuji Art Museum"), V("Nabeshima Kotetsu", "Nagasone Kotetsu", "", "Nabeshima clan"),
        V("Kotetsu II katana", "Nagasone Okimasa", "", "second generation")]),
   X("Minamoto Kiyomaro", "Shinshintō smith nicknamed 'Masamune of Yotsuya'.", "19th c. (shinshintō)", JS, mk="Minamoto Kiyomaro",
     v=[V("Kondō Isami's sword", "Minamoto Kiyomaro", "", "Kiyomaro blade with a forged Kotetsu signature")]),
   X("Shin guntō", "Army officers' sword of the Shōwa era with a traditional-style hilt.", "1934–1945 (gendaitō)", WP + "Sh%C5%8Dwat%C5%8D",
     v=[V("Type 94", "", "1934", "officers'"), V("Type 95", "", "1935", "NCO; machine-made, serial-numbered"), V("Type 98", "", "1938", "simplified Type 94")]),
   X("Shinsakutō katana", "New katana forged by a licensed smith after a five-year apprenticeship, at most two long swords a month, all registered.", "1953–present", WP + "Katana",
     v=[V("Masamune Prize reproduction of a Kamakura sword", "Kunihira Kawachi", "2014", "")]),
  ],
  "m": M(["New Practical Plus Elite Katana", "Hanwei"], ["Performance Series Elite Katana", "Hanwei"], ["Tactical Katana", "Hanwei"], ["Tonbo Katana", "Musashi"],
         ["Tsuribito Katana", "Hanbon Forge"], ["Winter Sun Katana", "Dragon King"], ["Seiryu Katana", "Musha"]),
  "r": [["Performance Series", "Hanwei"], ["Tactical", "Hanwei"]]},
 {"n": "Tachi", "a": "Japanese long sword · kodachi", "d": "Curved single-edged Japanese long sword slung edge down from the belt, the main sword of the kotō era.",
  "s": "https://www.knifecountryusa.com/store/product/323877.323882/cold-steel-swtachktna-tachi-katana.html", "t": ["tachi", "kodachi (short tachi)"] + VT,
  "x": [
   X("Sanjō Munechika", "Founder of the Yamashiro Sanjō school.", "late 10th c. (Heian)", WP + "Tenka-Goken", mk="Sanjō Munechika",
     v=[V("Mikazuki Munechika", "Sanjō Munechika", "late 10th c.", "Tenka-Goken; National Treasure, Tokyo National Museum")]),
   X("Yasutsuna", "Hōki-province smith of the early tachi.", "10th–12th c.", WP + "Tenka-Goken", mk="Yasutsuna",
     v=[V("Dōjigiri", "Yasutsuna", "12th c.", "Tenka-Goken; National Treasure, Tokyo National Museum")]),
   X("Awataguchi Kunitsuna", "Awataguchi-school smith.", "", WP + "Tenka-Goken", mk="Awataguchi Kunitsuna", v=[V("Onimaru", "Awataguchi Kunitsuna", "", "Tenka-Goken; Imperial Household Agency")]),
   X("Miike Denta Mitsuyo", "Maker of one of the Five Swords under Heaven.", "", WP + "Tenka-Goken", mk="Miike Denta Mitsuyo", v=[V("Ōdenta", "Miike Denta Mitsuyo", "", "Tenka-Goken; Maeda Ikutokukai")]),
   X("Aoe Tsunetsugu", "Aoe-school smith.", "", WP + "Tenka-Goken", mk="Aoe Tsunetsugu", v=[V("Juzumaru", "Aoe Tsunetsugu", "", "Tenka-Goken; Honkōji Temple")]),
   X("Kanehira", "Ko-Bizen smith.", "12th c.", WP + "Tachi", mk="Kanehira", v=[V("Ōkanehira", "Kanehira", "12th c.", "National Treasure")]),
   X("Fukuoka-Ichimonji Yoshifusa", "Bizen Fukuoka-Ichimonji smith.", "", WP + "Tachi", mk="Yoshifusa", v=[V("Okadagiri Yoshifusa", "Yoshifusa", "", "named after Oda Nobuo's killing of Okada")]),
  ],
  "m": M(["Tachi Katana", "Cold Steel"])},
 {"n": "Wakizashi", "a": "Japanese short sword · shōtō", "d": "Single-edged Japanese sword of 1–2 shaku (30–60 cm), the shorter blade of the daishō pair.",
  "s": "https://www.kultofathena.com/product-category/swords/asian-swords/japanese-swords/wakizashi/", "t": ["ō-wakizashi", "ko-wakizashi"] + VT,
  "x": [
   X("Sadamune", "Sōshū smith, son of Masamune.", "Nanboku-chō", WP + "Wakizashi", mk="Sadamune", v=[V("Ishida Sadamune", "Sadamune", "", "Important Cultural Property, Tokyo National Museum")]),
   X("Osafune Motoshige", "Bizen Osafune smith.", "14th c.", WP + "Wakizashi", mk="Osafune Motoshige", v=[V("Wakizashi dated 1356", "Osafune Motoshige", "1356", "Tokyo National Museum")]),
   X("Sōshū Akihiro", "Sōshū smith and pupil of Masamune.", "Nanboku-chō", WP + "Wakizashi", mk="Sōshū Akihiro"),
   X("Nanki Shigekuni", "Edo-period smith.", "1622 (shintō)", WP + "Wakizashi", mk="Nanki Shigekuni", v=[V("Wakizashi of 1622", "Nanki Shigekuni", "1622", "Important Sword; horimono by Ikeda Gonsuke Yoshiteru")]),
   X("Sanpin Masatoshi", "Edo-period smith.", "early 1600s", WP + "Wakizashi", mk="Sanpin Masatoshi", v=[V("British Museum wakizashi", "Sanpin Masatoshi", "early 1600s", "")]),
  ],
  "m": M(["Tactical Wakizashi", "Hanwei"], ["Great Wave Wakizashi", "Hanwei"], ["Kanshiki Wakizashi", "Thaitsuki Nihonto"], ["Kogane No Senshi Honsanmai Wakizashi", "BattleBlades"],
         ["Bamboo Wakizashi", "Citadel Swords"], ["Zetsurin Wakizashi", "Musha"], ["Dojo Pro Wakizashi Model 4", "Ronin Katana"], ["Modern Wakizashi", "Dragon King"]),
  "r": [["Tactical", "Hanwei"]]},
 {"n": "Tantō", "a": "tanto · Japanese dagger-length sword", "d": "Single-edged Japanese blade under one shaku (about 30 cm), counted as a sword by tradition.",
  "s": "https://www.kultofathena.com/product-category/swords/asian-swords/japanese-swords/tanto/", "t": ["hira-zukuri", "aikuchi mount", "yoroi-dōshi", "kaiken"] + VT,
  "x": [
   X("Masamune", "Sōshū master whose tantō include several National Treasures.", "late Kamakura", WP + "Masamune", mk="Masamune",
     v=[V("Hyuga Masamune", "Masamune", "", "National Treasure, Mitsui Memorial Museum"), V("Hōchō Masamune", "Masamune", "", "three unusually wide tantō; National Treasures"),
        V("Fudō Masamune", "Masamune", "", "signed; Important Cultural Property"), V("Kuki Masamune", "Masamune", "", "Hayashibara Museum of Art")]),
   X("Awataguchi Yoshimitsu", "Awataguchi smith, one of the Three Great Masters with Masamune and Go Yoshihiro.", "13th c.", WP + "Tant%C5%8D", mk="Awataguchi Yoshimitsu",
     v=[V("Atsushi Tōshirō", "Awataguchi Yoshimitsu", "13th c.", "National Treasure, Tokyo National Museum")]),
   X("Sadamune", "Sōshū smith, son of Masamune.", "Kamakura", WP + "Tant%C5%8D", mk="Sadamune", v=[V("Terasawa Sadamune", "Sadamune", "", "National Treasure, Tokyo National Museum")]),
   X("Nagasone Kotetsu", "Edo shintō smith.", "17th c.", WP + "Nagasone_Kotetsu", mk="Nagasone Kotetsu", v=[V("Hōraisan Kotetsu", "Nagasone Kotetsu", "", "one of the Nihon santō")]),
  ],
  "m": M(["Tactical Tanto", "Hanwei"], ["Great Wave Tanto", "Hanwei"], ["Kondoru Tanto", "Condor Tool & Knife"], ["Dragon Tanto", "Citadel Swords"], ["Atrim Survival Tanto", "APOC"],
         ["Honshu Full Tang Tactical Tanto", "United Cutlery"], ["Dojo Pro Tanto 5", "Ronin Katana"], ["Gokudo Hamidashi", "BattleBlades"]),
  "r": [["Tactical", "Hanwei"]]},
 {"n": "Ōdachi", "a": "nodachi · odachi · field sword", "d": "Very long Japanese sword with a blade of 3 shaku (c. 91 cm) or more.",
  "s": WP + "%C5%8Cdachi",
  "x": [
   X("Ōdachi Norimitsu", "Giant Bizen ōdachi with a blade of about 227 cm.", "1446", WP + "%C5%8Cdachi", mk="Norimitsu", v=[V("Ōdachi Norimitsu", "Norimitsu", "1446", "Yahiko Shrine")]),
   X("Taro-tachi", "Large blade of about 221 cm wielded by Magara Naotaka of the Asakura clan.", "", WP + "%C5%8Cdachi"),
  ]},
 {"n": "Ken (tsurugi)", "a": "tsurugi · ken", "d": "Straight double-edged early Japanese sword, later made as shrine and temple offerings.",
  "s": WP + "Tsurugi_(sword)",
  "x": [
   X("Bronze tsurugi", "Bronze straight double-edged sword of the Yayoi period.", "Yayoi (c. 200 BCE peak)", WP + "Tsurugi_(sword)"),
   X("Iron tsurugi", "Forged iron straight sword of the Kofun to Heian periods.", "5th–9th c.", WP + "Tsurugi_(sword)", v=[V("Kongō-ji tsurugi", "", "Heian", "vajra-shaped hilt; Kyoto National Museum")]),
   X("Offering tsurugi", "Tsurugi made as an offering to shrines and Buddhist temples after weapon use ended.", "10th c. on", WP + "Tsurugi_(sword)",
     v=[V("Yasaka Shrine tsurugi", "Fujiwara Kunimichi", "1654", "offering to Susanoo")]),
  ]},
 {"n": "Iaitō", "a": "iaito · practice sword", "d": "Unsharpened alloy or steel practice sword for iaidō forms, not for contact.",
  "s": WP + "Iait%C5%8D", "t": ["aluminium-zinc alloy blade", "steel blade"]},
 {"n": "Bokken", "a": "bokutō · wooden sword", "d": "Wooden training sword, usually oak and katana-sized, used for kata.",
  "s": WP + "Bokken", "t": ["daitō (long)", "shōtō (short)", "tantō bō", "suburitō (heavy, for solo cuts)", "red oak", "white oak"]},
]
def T(n, r, p, d, forms, ctr, auth):
    return {"n": n, "g": "Metal & blades", "r": r, "p": p, "d": d, "tech": "Japanese sword forging (Gokaden tradition)", "mat": "steel",
            "forms": forms, "ctr": ctr, "auth": auth, "s": JS}
trads = [
 T("Yamato tradition", "Yamato Province (Nara)", "Heian onward", "Oldest of the five Gokaden sword traditions, founded by Yukinobu.", ["Tachi", "Katana"], ["Yukinobu"],
   "Deep curve, narrow body, high ridge, small tip, straight simple hamon."),
 T("Yamashiro tradition", "Yamashiro Province (Kyoto)", "late 10th c. onward", "Kyoto sword tradition begun by the Sanjō school of Sanjō Munechika.", ["Tachi", "Tantō"], ["Sanjō Munechika", "Awataguchi school"],
   "Long narrow elegant blades, straight hamon, fine grain."),
 T("Bizen tradition", "Bizen Province (Okayama)", "mid-Heian onward", "Prolific Bizen sword tradition from Ko-Bizen to the Osafune school.", ["Tachi", "Katana", "Wakizashi"], ["Ko-Bizen", "Osafune school", "Fukuoka-Ichimonji", "Kanehira"],
   "Curve from the base; showy clove-like (chōji) hamon."),
 T("Sōshū tradition", "Sagami Province (Kanagawa)", "late 13th c. onward", "Sagami sword tradition made famous by Masamune.", ["Katana", "Tantō", "Wakizashi"], ["Masamune", "Sadamune", "Shintōgo Kunimitsu"],
   "Shallow curve, wide body, large grain, nie-rich activity."),
 T("Mino tradition", "Mino Province (Gifu)", "mid-Kamakura onward", "Mino sword tradition that became the largest producer after Bizen declined.", ["Katana"], ["Seki Kanemoto", "Magoroku Kanemoto"],
   "Slightly higher ridge, thinner back, varied hamon."),
]
brands = [{"n": "Hanwei", "c": "China", "f": "1990", "seg": "Mainstream", "kf": "replica swords", "d": "Dalian maker of Japanese, Chinese and European sword replicas founded by Paul Chen; factory reportedly closed December 2024.",
           "rel": ["C.A.S. Iberia"], "s": WP + "Hanwei_(sword_producer)"}]
out = {"kinds": kinds, "brands": brands, "traditions": trads,
 "notes": "All 4 old kinds kept; added Ōdachi, Ken (tsurugi), Iaitō, Bokken. Nihontō register: archetype = smith (mk = smith name, not brand-register entries), versions = named surviving swords; period/school in y and the five Gokaden traditions as tradition entries. Version classes (antique/gendaitō/shinsakutō/replica) as types. Replica SKU lists cut: Katana 13->7, Wakizashi 22->8 (dropped Citadel Lotus/Ocean/Wolf, Dragon King Lotus Seed/Pine Crane, Hanwei Bamboo Mat/Classic Tiger/Koi, BattleBlades Kage No Senshi/Shinobi Shoto, Thaitsuki Isamashii/Roiyaru, APOC Survival, Honshu Boshin), Katana dropped Hanbon Black Sakura/Raiju, Hanwei Pro Elite/XL Light, Musashi Oni/Sarugami. Brand prefixes removed from model names. Minamoto Kiyomaro page 404; cited Japanese sword article. Hanbon, BattleBlades, Musashi etc. not in brand register (no retrieved page)."}
p = '/home/user/Possession-Taxonomy/rebuild/work/E4/shelves/00_01.json'
json.dump(out, open(p + '.tmp', 'w'), ensure_ascii=False, indent=1); os.replace(p + '.tmp', p)
print('written')
