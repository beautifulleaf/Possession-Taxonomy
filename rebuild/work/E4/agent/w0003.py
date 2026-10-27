import json, os
WP = 'https://en.wikipedia.org/wiki/'
SH = 'https://shibuiswords.com/tsuba-artisan-schools.htm'
MT = WP + 'Japanese_sword_mountings'
def X(n, d, y, s, mk='', a='', v=None, dt=''):
    x = {"n": n, "a": a, "d": d, "mk": mk, "y": y, "s": s, "v": v or []}
    if dt: x["dt"] = dt
    return x
def V(n, mk='', y='', d=''):
    return {"n": n, "mk": mk, "y": y, "d": d}
kinds = [
 {"n": "Sword guard", "a": "tsuba · cross guard", "d": "Loose guard for a sword hilt; Japanese tsuba are collected by school and maker.",
  "s": "https://collectorsfirearms.com/product-category/japanese-swords-fittings-and-firearms/tsuba/",
  "t": ["katana size (c. 7.5–8 cm)", "wakizashi size", "tantō size", "iron", "soft metal (shakudō, shibuichi, copper, brass)"],
  "x": [
   X("Ko-Tōshō", "Thin hammered iron plate with one or two simple pierced designs.", "late Kamakura – early Muromachi", SH),
   X("Myōchin", "Tsuba of the Myōchin armourer family; school founded by its 17th master Nobuiye.", "mid-Muromachi – late Edo", SH, dt="iron"),
   X("Owari", "Hard refined iron with purplish patina and flowing openwork.", "", SH, a="Owari sukashi"),
   X("Kyō-sukashi", "Kyoto iron openwork tsuba with refined, elegant patterns.", "late Muromachi – early Momoyama", SH),
   X("Heianjō", "Iron tsuba with brass inlay, later also silver, copper and shakudō pictorial designs.", "from 1504–1520; declined early Edo", SH),
   X("Shōami", "Forged plate with inlay; Kyoto school that spread to many provinces.", "late Muromachi – Edo", SH, v=[V("Ko-Shōami", "", "late Muromachi – Momoyama", ""), V("Kyō-Shōami", "", "early Edo peak", "richer, more detailed designs")]),
   X("Umetada", "One of the four great Kyoto schools.", "from 1573", SH),
   X("Higo", "Iron tsuba made for the Hosokawa of Higo, with special alloys and odawara-fukurin rims.", "", SH,
     v=[V("Hayashi (Kasuga)", "", "", "delicate openwork, lustrous iron"), V("Nishigaki", "", "", "blend of Hayashi and Hirata"), V("Shimizu (Jingo)", "", "", "raised brass inlay"), V("Kamiyoshi", "", "", "fluid plate, browner colour"), V("Hirata", "Hirata Hikozō", "", "Higo kinkō")]),
   X("Akasaka", "Edo-district school; early generations in Owari style, later in Higo style, with straight stiff rims.", "", SH),
   X("Nara", "Gotō-style figural inlay in gold, silver, shakudō and copper applied to hammered iron plate.", "Momoyama – Meiji", "https://japaneseswordindex.com/tsuba/nara.htm",
     v=[V("Toshiteru", "", "", "first Nara master"), V("Toshinaga (Riju)", "", "1667–1737", "one of the Three Great Nara Masters"), V("Sugiura Joi", "", "1700–1761", "one of the Three Great Nara Masters"), V("Tsuchiya Yasuchika", "", "1669–1744", "one of the Three Great Nara Masters")]),
   X("Gotō", "Soft-metal plate with decorative inlay; traditional kinkō work.", "pre-Momoyama onward", SH),
   X("Kinai", "Iron school derived from Shōami combined with Chōshū style.", "", SH),
  ],
  "m": [["Tsuba", ""]]},
 {"n": "Scabbard", "a": "sheath · saya", "d": "Sheath made to hold a sword or knife.",
  "s": WP + "Scabbard",
  "t": ["lacquered wooden saya", "wood covered in leather or fabric", "leather with chape and locket", "steel or brass", "polymer (Kydex)", "tachi koshirae", "han-dachi", "aikuchi"],
  "x": [
   X("Saya", "Japanese lacquered wooden scabbard, often of magnolia, with koiguchi mouth, kurikata and kojiri end cap.", "", WP + "Scabbard"),
   X("Shirasaya", "Plain wooden storage scabbard and hilt for a Japanese blade, sometimes inscribed (sayagaki).", "", MT),
  ],
  "m": [["Saya", ""]]},
 {"n": "Hilt collar and pommel cap", "a": "fuchi-kashira", "d": "Loose collar and pommel cap made for a sword hilt, sold as a set; the Japanese pair is called fuchi-kashira.",
  "s": "https://collectorsfirearms.com/product-category/japanese-swords-fittings-and-firearms/tsuba/",
  "x": [X("Ishiguro Masayoshi", "Late-Edo maker of tsuba and fuchi-kashira.", "late Edo", WP + "Tsuba", mk="Ishiguro Masayoshi")]},
 {"n": "Sword grip ornament", "a": "menuki", "d": "Loose ornament fitted under the grip wrapping of a Japanese sword.",
  "s": "https://collectorsfirearms.com/38184-pair-of-menuki-mgj392.html",
  "x": [X("Gotō school menuki", "Soft-metal menuki of the Gotō family of fittings makers.", "early Edo", MT, v=[V("Menuki", "Gotō Kenjō", "early Edo", "")])]},
 {"n": "Scabbard pocket fitting", "a": "kozuka · kogai", "d": "Loose fitting made to sit in a pocket of a Japanese sword scabbard: a small-knife handle (kozuka) with its blade, or a hair spike (kogai).",
  "s": "https://collectorsfirearms.com/product-category/japanese-swords-fittings-and-firearms/tsuba/", "t": ["kozuka", "kōgai"],
  "x": [X("Gotō school kōgai and kozuka", "Kōgai and kozuka by Gotō masters.", "Edo", MT, v=[V("Kōgai and kozuka", "Gotō Kenjō", "early Edo", ""), V("Kōgai", "Gotō Mitsunobu", "", "")]),
        X("Yanagawa Naomasa", "Maker of kōgai and kozuka.", "", MT, mk="Yanagawa Naomasa")]},
 {"n": "Habaki", "a": "blade collar", "d": "Metal collar at the base of a Japanese blade that locks the guard and holds the blade in the scabbard.",
  "s": MT},
]
out = {"kinds": kinds, "brands": [], "traditions": [],
 "notes": "All 5 old kinds kept; added Habaki. Tsuba schools as archetypes (Shibui Swords school guide, Japanese Sword Index for Nara); Higo sub-schools and Nara masters as versions. Fuchi-kashira, menuki, kozuka/kōgai given named makers from the Wikipedia mountings/tsuba pages only. European scabbard forms and Japanese mount styles as types. No traditions added (Gokaden traditions sit with the Japanese swords shelf); Ashmolean page returned HTTP 500 and was not used."}
p = '/home/user/Possession-Taxonomy/rebuild/work/E4/shelves/00_03.json'
json.dump(out, open(p + '.tmp', 'w'), ensure_ascii=False, indent=1); os.replace(p + '.tmp', p)
print('written')
