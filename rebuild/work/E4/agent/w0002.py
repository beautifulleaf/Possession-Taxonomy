import json, os
WP = 'https://en.wikipedia.org/wiki/'
def X(n, d, y, s, mk='', a='', v=None, dt=''):
    x = {"n": n, "a": a, "d": d, "mk": mk, "y": y, "s": s, "v": v or []}
    if dt: x["dt"] = dt
    return x
def V(n, mk='', y='', d=''):
    return {"n": n, "mk": mk, "y": y, "d": d}
DAO = WP + 'Dao_(Chinese_sword)'
TAL = WP + 'Talwar'
kinds = [
 {"n": "Jian", "a": "Chinese straight sword", "d": "Chinese double-edged straight sword, made in bronze from the 7th century BCE and later in steel.",
  "s": WP + "Jian", "t": ["bronze", "steel", "one-handed", "two-handed (shuangshou jian)"],
  "x": [
   X("Sword of Goujian", "Bronze jian of King Goujian of Yue with a gold-inlaid bird-worm script inscription.", "early 5th c. BCE", WP + "Sword_of_Goujian",
     v=[V("Original", "", "early 5th c. BCE", "Hubei Provincial Museum; 55.6 cm")]),
   X("Qin bronze jian", "Bronze jian carried by officers of the Terracotta Army.", "Qin", WP + "Jian"),
   X("Shuangshou jian", "Rare two-handed jian.", "", WP + "Jian"),
   X("Taijijian", "Unsharpened semi-flexible stainless jian for tai chi solo forms.", "modern", WP + "Jian", a="tai chi sword"),
   X("Wushu jian", "Thin, highly flexible jian made for performance.", "modern", WP + "Jian"),
  ]},
 {"n": "Dao (Chinese sabre)", "a": "dao · Chinese sabre", "d": "Single-edged Chinese sword for slashing and chopping, straight or curved; one of the four traditional weapons.",
  "s": DAO,
  "x": [
   X("Liuyedao", "Willow-leaf sabre with a moderate curve; the commonest Chinese sabre and standard sidearm.", "Ming", DAO, a="willow-leaf sabre"),
   X("Yanmaodao", "Goose-quill sabre, mostly straight with a curve near the tip, suited to thrusting.", "Ming", DAO, a="goose-quill sabre"),
   X("Niuweidao", "Ox-tail sabre with a heavy blade flaring at the tip; a civilian weapon.", "early 19th c. (late Qing)", DAO, a="oxtail sabre"),
   X("Dadao", "Falchion-like dao.", "Song", DAO),
   X("Zhanmadao", "Long two-handed dao used against cavalry and pirates.", "Song; Ming", DAO, a="horse-cutting sabre"),
   X("Piandao", "Deeply curved slashing sabre resembling a shamshir.", "", DAO, a="slashing sabre"),
   X("Hengdao", "Straight single-handed belt sidearm, common in the Tang.", "Sui–Tang", DAO, a="peidao"),
   X("Changdao", "Long two-handed dao.", "Tang; Ming", DAO),
   X("Duandao", "Short dao, generally shaped like a liuyedao.", "", DAO),
  ]},
 {"n": "Shamshir", "a": "shamshīr · Persian sabre · scimitar", "d": "Persian sword with a slim, radically curved blade, worn horizontally and used for slashing.",
  "s": WP + "Shamshir",
  "x": [
   X("Classic shamshir", "Slim curved blade tapering only near the tip, offset pommel, long quillons, bone, ivory or wood grip.", "16th c. onward", WP + "Shamshir", dt="wootz or plain steel · grip material"),
   X("Shamshir shekargar", "Hunting shamshir with an engraved blade, usually showing hunting scenes.", "", WP + "Shamshir", a="hunting sword"),
   X("Pulwar", "Afghan single-handed curved sword of the shamshir family.", "", WP + "Shamshir"),
  ]},
 {"n": "Talwar", "a": "tulwar · taravāri", "d": "Curved single-edged sabre of the Indian subcontinent with an all-metal disc-pommel hilt.",
  "s": TAL,
  "x": [
   X("Classic talwar", "Mughal-era talwar: moderately curved blade, often widening towards the tip, on a disc hilt with knucklebow.", "c. 1500 onward", TAL),
   X("Tegha", "Talwar with a massive blade, often called an executioner's sword.", "", TAL),
   X("Sirohi", "Talwar with an only slightly curved blade.", "", TAL),
   X("Dhup", "Straight-bladed talwar on a disc hilt.", "", TAL, a="straight-bladed talwar"),
   X("Sosun patta", "Talwar with a yatagan-style forward-curved blade.", "", TAL),
   X("Zulfiqar", "Talwar with a double-pointed blade.", "", TAL),
  ]},
 {"n": "Khanda", "a": "", "d": "Indian straight double-edged sword whose blade widens to a blunt tip, with a plate guard and spiked disc pommel.",
  "s": WP + "Khanda_(sword)", "t": ["one-handed", "two-handed grip"]},
 {"n": "Kilij", "a": "kılıç · Turkish sabre", "d": "One-handed curved Turkic and Ottoman sabre, often with a flared false edge (yelman) near the tip.",
  "s": WP + "Kilij",
  "x": [
   X("Ottoman kilij", "Distinct Ottoman sabre with yelman false edge.", "mid-15th c. onward", WP + "Kilij", v=[V("Janissary kilij", "", "", "inspired the Polish karabela")]),
   X("Early Turkic kilij", "Curved steppe cavalry sabre of Turkic peoples.", "Kök-Turk era onward", WP + "Kilij", v=[V("Sword attributed to Özbeg Khan", "", "early 14th c.", "Hermitage Museum")]),
   X("Pala", "Late kilij with a short, broad, sharply curved blade.", "late 18th c.", WP + "Kilij"),
  ]},
 {"n": "Yataghan", "a": "yatagan · ataghan · varsak", "d": "Guardless Ottoman short sabre with a forward-curved single-edged blade and an eared pommel.",
  "s": WP + "Yataghan",
  "x": [
   X("Balkan yataghan", "Yataghan with large bone or ivory pommel ears.", "mid-16th–19th c.", WP + "Yataghan"),
   X("Anatolian yataghan", "Yataghan with smaller horn or silver pommel ears.", "mid-16th–19th c.", WP + "Yataghan"),
   X("Zeibek T-hilt yataghan", "T-hilted yataghan carried by Zeibeks of the Ionian coast.", "", WP + "Yataghan"),
  ]},
 {"n": "Kampilan", "a": "talong", "d": "Large single-edged Philippine sword whose blade widens towards the tip, often with a spikelet and carved pommel.",
  "s": WP + "Kampilan"},
 {"n": "Dha", "a": "daab · dao", "d": "Single-edged, gently curved Southeast Asian sword with a round grip and little or no guard.",
  "s": WP + "Dha_(sword)",
  "x": [
   X("Burmese dha", "Dha with a straight or nearly straight spine.", "", WP + "Dha_(sword)", v=[V("Dha-shay", "", "", "long curved sword"), V("Dha-hmyaung", "", "", "dagger")]),
   X("Thai daab", "Daab with a slightly curved spine.", "", WP + "Dha_(sword)", v=[V("Ayutthaya style", "", "", "central"), V("Lanna style", "", "", "northern")]),
   X("Lao daab", "Daab with a more pronounced curve and more carving.", "", WP + "Dha_(sword)"),
  ]},
 {"n": "Takoba", "a": "takuba · takouba", "d": "Straight double-edged Sahel sword of about one metre, carried by the Tuareg, with a leather-covered hilt.",
  "s": WP + "Takoba"},
 {"n": "Shotel", "a": "", "d": "Ethiopian sword with a near-semicircular double-edged blade for hooking round a shield.",
  "s": WP + "Shotel"},
]
trads = [
 {"n": "Wootz crucible steel", "g": "Metal & blades", "r": "Southern India and Sri Lanka", "p": "mid-1st millennium BC onward",
  "d": "High-carbon crucible steel showing banded carbide patterns, traded west and behind Damascus steel blades.",
  "tech": "ore heated with carbon in sealed clay crucibles in a charcoal furnace", "mat": "magnetite ore, charcoal, plant carbon",
  "forms": ["Shamshir", "Talwar"], "ctr": ["Golconda", "Karnataka", "Tamil Nadu", "Sri Lanka", "Damascus"],
  "auth": "Wave, ladder or rose banding from forging; modern smiths can now make visually identical patterns.", "s": WP + "Wootz_steel"},
 {"n": "Longquan sword-making", "g": "Metal & blades", "r": "Longquan, Zhejiang, China", "p": "Spring and Autumn period (by tradition) to present",
  "d": "Sword craft traced to the smith Ou Yezi, on China's national intangible cultural heritage list since 2006.",
  "tech": "28 forging and finishing procedures", "mat": "steel",
  "forms": ["Jian", "Dao (Chinese sabre)"], "ctr": ["Ou Yezi (legendary founder)", "over 4,000 makers in Longquan"],
  "auth": "Judged by sharpness, cold glitter, blade density and fine metal carving.", "s": "https://regional.chinadaily.com.cn/ezhejiang/2016-08/12/c_55752.htm"},
]
out = {"kinds": kinds, "brands": [], "traditions": trads,
 "notes": "New shelf (no old kinds): 11 kinds all sourced from Wikipedia. Named regional patterns as archetypes; Khanda, Kampilan, Takoba and Shotel kept without archetypes (no distinct named patterns on the fetched pages). No reproduction makers or brands added (no retrieved pages). Traditions: wootz crucible steel, Longquan sword-making (China Daily page)."}
p = '/home/user/Possession-Taxonomy/rebuild/work/E4/shelves/00_02.json'
json.dump(out, open(p + '.tmp', 'w'), ensure_ascii=False, indent=1); os.replace(p + '.tmp', p)
print('written')
