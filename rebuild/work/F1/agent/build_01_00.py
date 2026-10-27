import json, os
W = 'https://en.wikipedia.org/wiki/'
def X(n, d, mk, y, s, v=(), a="", dt=""):
    return {"n": n, "a": a, "d": d, "mk": mk, "y": y, "s": s, "v": [dict(zip(("n", "mk", "y", "d"), t)) for t in v], "dt": dt}
MFSL = W + 'Mobile_Fidelity_Sound_Lab'
AP = W + 'Analogue_Productions'
UHQR = 'https://www.analogplanet.com/content/analogue-productions-truly-premium-uhqr-200g-2lp-qrp-pressing-steely-dans-can%E2%80%99t-buy-thrill'
A75 = 'https://elusivedisc.com/dusty-springfield-dusty-in-memphis-atlantic-75-series-180g-45rpm-2lp/'
TP = 'https://www.bluenote.com/blue-note-presents-the-tone-poet-audiophile-vinyl-reissue-series/'
BNC = 'https://www.analogplanet.com/content/blue-noter-announces-next-round-%E2%80%9Cclassic-vinyl%E2%80%9D-180g-aaa-reissues'
ONE = 'https://elusivedisc.com/joni-mitchell-blue-numbered-limited-edition-ultradisc-one-step-180g-45rpm-supervinyl-2lp-box-set'
SAX = W + 'Doug_Sax'
SC = 'https://trackingangle.com/features/whats-up-with-speakers-corner'
IMP = 'https://www.moon-audio.com/blogs/expert-advice/inside-impex-records-how-abey-fonn-builds-the-worlds-most-painstaking-vinyl-reissues'
INT = 'https://theaudiobeat.com/news/intervention_records.htm'
CRAFT = 'https://craftrecordings.com/blogs/news/introducing-small-batch-an-all-analog-limited-edition-one-step-vinyl-series'
ASS = 'https://www.udiscovermusic.com/news/ella-fitzgerald-sings-the-cole-porter-song-book-verve-acoutic-sounds-series/'
RSD = W + 'Record_Store_Day'
OBI = 'https://sabukaru.online/articles/the-grail-of-vinyl-collectors-obi'
PD = W + 'Picture_disc'
SGL = W + 'Single_(music)'

kinds = [
 {"n": "LP record", "a": "long-playing record · LP · album · 33⅓", "d": "12-inch vinyl microgroove disc played at 33⅓ rpm (audiophile issues often at 45 rpm), holding an album.",
  "t": ["standard pressing", "180-gram", "200-gram", "45 rpm audiophile cut", "half-speed master", "all-analogue (AAA) cut", "one-step pressing", "coloured vinyl", "quadraphonic", "mono", "gatefold sleeve", "tip-on jacket", "double LP", "box set", "Japanese pressing with obi", "numbered limited edition", "promo or white label"],
  "s": W + 'LP_record',
  "x": [
   X("Original Master Recording", "Mobile Fidelity's audiophile LP line, half-speed mastered from the original analogue master tapes.", "Mobile Fidelity Sound Lab", "1977", MFSL,
     [("Original Master Recording LP", "Mobile Fidelity Sound Lab", "1977", "half-speed mastered"), ("Post-2001 revival", "Mobile Fidelity Sound Lab", "2001", "after the label's 1999 closure and sale to Music Direct")],
     a="MFSL · MoFi OMR", dt="numbered or unnumbered · 33⅓ or 45 rpm · analogue or DSD-sourced mastering chain"),
   X("UltraDisc One-Step", "MoFi 45 rpm box sets pressed from stampers made directly from the lacquer, skipping the father and mother plating steps.", "Mobile Fidelity Sound Lab", "2016", ONE,
     [("UltraDisc One-Step 2LP box", "Mobile Fidelity Sound Lab", "", "180 g SuperVinyl, 45 rpm, pressed at RTI, numbered limited run")],
     a="UD1S · MoFi One-Step", dt="45 rpm 2LP box · SuperVinyl compound · individual numbering · run size"),
   X("UHQR", "Analogue Productions' ultra-high-quality pressings on 200-gram Clarity vinyl, pressed at Quality Record Pressings and sold in deluxe boxes.", "Analogue Productions", "", UHQR,
     [("UHQR 200 g 2LP", "Analogue Productions", "", "Clarity vinyl, Bernie Grundman mastering, QRP pressing")], a="Ultra High Quality Record",
     dt="33⅓ or 45 rpm · 1LP or 2LP · numbered box · inspection certificate"),
   X("Atlantic 75 Series", "Analogue Productions' 75-title reissue series for Atlantic Records' 75th anniversary, cut at 45 rpm on two 180-gram LPs.", "Analogue Productions", "", A75,
     [("180 g 45 rpm 2LP", "Analogue Productions", "", "pressed at QRP, Stoughton tip-on gatefold jacket")], a="75 for 75", dt="45 rpm 2LP · mastering engineer · tip-on gatefold"),
   X("Tone Poet series", "Blue Note's all-analogue 180-gram audiophile reissues produced by Joe Harley, mastered by Kevin Gray and pressed at RTI.", "Blue Note Records", "2019", TP,
     [("Tone Poet 180 g LP", "Blue Note Records", "2019", "deluxe gatefold packaging, from original master tapes")], a="Tone Poet Audiophile Vinyl Reissue Series", dt="gatefold · 180 g · RTI pressing"),
   X("Classic Vinyl Series", "Blue Note's affordable all-analogue 180-gram reissues in standard packaging, mastered by Kevin Gray and pressed at Optimal in Germany.", "Blue Note Records", "", BNC,
     [("Classic Vinyl Reissue Series", "Blue Note Records", "", "curated by Don Was and Cem Kurosman")],
     a="Blue Note Classic", dt="180 g · standard sleeve"),
   X("Sheffield Lab direct-to-disc", "Records cut live straight to the master lacquer with no tape stage, from Doug Sax and Lincoln Mayorga's label.", "Sheffield Lab", "1970s", SAX,
     a="direct-cut LP", dt="direct-to-disc or live-to-two-track"),
   X("Speakers Corner reissue", "German all-analogue reissues cut from original master tapes, starting with Decca classical titles before jazz and rock.", "Speakers Corner Records", "1993", SC,
     dt="classical, jazz or rock · 180 g"),
   X("Acoustic Sounds Series", "Verve and Impulse! all-analogue 180-gram reissues mastered by Ryan K. Smith at Sterling Sound and pressed at QRP.", "Acoustic Sounds", "", ASS,
     a="Verve Acoustic Sounds Series", dt="tip-on jacket · 180 g"),
   X("Craft Recordings Small Batch", "Numbered one-step pressings limited to 1,000 copies, cut all-analogue by Bernie Grundman and plated by RTI.", "Craft Recordings", "", CRAFT,
     a="Small Batch One-Step", dt="180 g Neotech VR900 · linen-wrapped slipcase · tip-on jacket · copy number"),
   X("Impex reissue", "Painstaking audiophile reissues from Abey Fonn's label, including One Step editions, from original master tapes.", "Impex Records", "c. 2010", IMP,
     [("1STEP edition", "Impex Records", "", "one-step plating")], dt="33⅓ or 45 rpm · one-step or standard"),
   X("Intervention Records reissue", "Premium reissues of overlooked rock and pop albums, mastered by Kevin Gray and pressed at RTI.", "Intervention Records", "2015", INT,
     dt="180 g · premium jackets"),
   X("Record Store Day release", "Limited records pressed specifically for the twice-yearly event and sold only through participating independent shops.", "", "2008", RSD,
     [("April Record Store Day", "", "2008", "Saturday in April"), ("Black Friday release", "", "2010", "November edition")], a="RSD exclusive", dt="coloured vinyl · numbered · country list"),
  ]},
 {"n": "7-inch single", "a": "7\" single · 45 · seven-inch", "d": "Small 7-inch vinyl disc, usually 45 rpm, with one or two songs a side.",
  "t": ["large-centre (jukebox) hole", "small spindle hole", "push-out centre", "picture sleeve", "company sleeve", "EP (extended play)", "mono", "stereo", "promo or demo copy", "coloured vinyl"],
  "s": SGL,
  "x": [
   X("RCA Victor 45", "The original 7-inch 45 rpm vinyl single, launched by RCA Victor to replace 78 rpm shellac discs.", "RCA Victor", "1949", SGL,
     dt="large centre hole · mono or stereo · label variations")]},
 {"n": "12-inch single", "a": "12\" single · maxi-single · club single", "d": "Vinyl single on a 12-inch disc with one to a few tracks, often extended mixes for DJs and clubs.",
  "t": ["33⅓ rpm", "45 rpm", "promo or white label", "DJ-only pressing", "picture sleeve", "generic company sleeve"],
  "s": SGL},
 {"n": "10-inch record", "a": "10\" record · ten-inch · 10-inch LP · 10-inch EP", "d": "10-inch microgroove disc, used for early LPs until the mid-1950s and now for EPs and special editions.",
  "t": ["early 10-inch LP (1948–mid-1950s)", "modern 10-inch EP", "33⅓ rpm", "45 rpm", "coloured vinyl", "limited edition"],
  "s": 'https://www.collectorsweekly.com/records/10-inch'},
 {"n": "Picture disc", "a": "picture record · pic disc · shaped disc", "d": "Record with an image sealed into the playing surface, so the picture shows across the grooves.",
  "t": ["round picture disc", "shaped disc", "picture-label disc (not a true picture disc)", "7-inch", "10-inch", "12-inch", "shellac-core (1930s)", "vinyl"],
  "s": PD,
  "x": [
   X("RCA Victor picture disc", "1930s disc with a shellac core between illustrated sheets sealed under clear plastic; includes the first 33⅓ rpm picture disc.", "RCA Victor", "1933", PD,
     dt="shellac core · 78 or 33⅓ rpm"),
   X("Vogue picture record", "Aluminium-core picture discs with pin-up and cartoon art from Sav-Way Industries, made for little more than a year.", "Vogue Records", "1946–1947", PD,
     dt="fewer than 100 catalogue items · art condition"),
   X("Modern vinyl picture disc", "Picture disc revival begun in Germany around 1969–70 and widespread in the late 1970s and 1980s.", "", "c. 1969–1970", PD,
     [("Metronome picture disc", "", "c. 1969–1970", "first modern picture discs, Germany"), ("Shaped picture disc", "", "1980s", "cut into shapes, usually singles, often limited to a few thousand")],
     dt="7-inch, 10-inch or 12-inch · round or shaped · limited numbering"),
  ]},
]

brands = [
 {"n": "Mobile Fidelity Sound Lab", "c": "United States", "f": "1977", "seg": "Specialist", "kf": "audiophile vinyl", "d": "Audiophile reissue label known for half-speed mastered Original Master Recording LPs; owned by Music Direct since 2001.",
  "lines": ["Original Master Recording", "UltraDisc One-Step"], "eras": ["Original company, 1977–1999", "Music Direct ownership, 2001–"], "sig": ["Original Master Recording", "UltraDisc One-Step"],
  "rel": ["Analogue Productions"], "s": MFSL},
 {"n": "Analogue Productions", "c": "United States", "f": "1992", "seg": "Specialist", "kf": "audiophile vinyl", "d": "Audiophile reissue label of Acoustic Sounds in Salina, Kansas, founded by Chad Kassem, pressing at Quality Record Pressings.",
  "lines": ["UHQR", "Atlantic 75 Series"], "sig": ["UHQR", "Atlantic 75 Series"], "rel": ["Acoustic Sounds", "Mobile Fidelity Sound Lab"], "s": AP},
 {"n": "Acoustic Sounds", "c": "United States", "f": "", "seg": "Own-label & retailer", "kf": "audiophile retail", "d": "Salina, Kansas company of Chad Kassem; parent of Analogue Productions and its Quality Record Pressings plant.",
  "lines": ["Acoustic Sounds Series"], "sig": ["Acoustic Sounds Series"], "rel": ["Analogue Productions"], "s": AP},
 {"n": "Blue Note Records", "c": "United States", "f": "1939", "seg": "Heritage manufactory", "kf": "jazz label", "d": "Jazz record label founded by Alfred Lion and Max Margulis, with Francis Wolff joining soon after.",
  "lines": ["Tone Poet series", "Classic Vinyl Series"], "sig": ["Tone Poet series", "Classic Vinyl Series"], "s": W + 'Blue_Note_Records'},
 {"n": "Sheffield Lab", "c": "United States", "f": "1970s", "seg": "Specialist", "kf": "direct-to-disc", "d": "Audiophile label of Doug Sax and Lincoln Mayorga known for direct-to-disc recordings.",
  "sig": ["Sheffield Lab direct-to-disc"], "s": SAX},
 {"n": "Speakers Corner Records", "c": "Germany", "f": "", "seg": "Specialist", "kf": "analogue reissues", "d": "German reissue label run by Kai Seemann, issuing all-analogue reissues since 1993.",
  "sig": ["Speakers Corner reissue"], "s": SC},
 {"n": "Impex Records", "c": "United States", "f": "", "seg": "Specialist", "kf": "audiophile reissues", "d": "Audiophile reissue label founded by Abey Fonn, formerly of Cisco Music, after Cisco closed in 2008.",
  "lines": ["1STEP"], "sig": ["Impex reissue"], "s": IMP},
 {"n": "Intervention Records", "c": "United States", "f": "2015", "seg": "Specialist", "kf": "audiophile reissues", "d": "Reissue label run by Shane Buettner for overlooked rock and pop albums, mastered by Kevin Gray.",
  "sig": ["Intervention Records reissue"], "s": INT},
 {"n": "Craft Recordings", "c": "United States", "f": "", "seg": "Specialist", "kf": "catalogue reissues", "d": "Catalogue reissue label behind the numbered all-analogue Small Batch one-step series.",
  "lines": ["Small Batch"], "sig": ["Craft Recordings Small Batch"], "s": CRAFT},
 {"n": "RCA Victor", "c": "United States", "f": "", "seg": "Heritage manufactory", "kf": "records", "d": "Record label that introduced the 7-inch 45 rpm single in 1949 and early picture discs in 1933.",
  "sig": ["RCA Victor 45", "RCA Victor picture disc"], "s": SGL},
 {"n": "Vogue Records", "c": "United States", "f": "1946", "seg": "Specialist", "kf": "picture discs", "d": "Short-lived 1940s label of Tom Saffardy's Sav-Way Industries that made aluminium-core picture records.",
  "sig": ["Vogue picture record"], "s": PD},
]

notes = ("Merged old k40 (LP and other vinyl records) into LP record; release types (EP, single) moved to size-based kinds and 't'. "
         "Old model UHQR/Analogue Productions became an archetype. Japanese pressing with obi kept as a 't' attribute (sabukaru obi page fetched but not needed as a separate archetype). "
         "Left out: Analogue Productions Verve 45 series (no page retrieved), Sheffield Lab founding year (sources only say 1970s), MoFi Ultradisc CDs (out of shelf). "
         "Picture disc and 10-inch record are new kinds. Shaped discs are a version/t of picture disc. No album titles.")
out = {"kinds": kinds, "brands": brands, "traditions": [], "notes": notes}
p = '/home/user/Possession-Taxonomy/rebuild/work/F1/shelves/01_00.json'
json.dump(out, open(p + '.tmp', 'w'), ensure_ascii=False, indent=1); os.replace(p + '.tmp', p)
print('written', len(kinds), 'kinds')
