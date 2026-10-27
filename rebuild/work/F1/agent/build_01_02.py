import json, os
W = 'https://en.wikipedia.org/wiki/'
def X(n, d, mk, y, s, v=(), a="", dt=""):
    return {"n": n, "a": a, "d": d, "mk": mk, "y": y, "s": s, "v": [dict(zip(("n", "mk", "y", "d"), t)) for t in v], "dt": dt}
CD = W + 'Compact_disc'
SACD = W + 'Super_Audio_CD'
MD = W + 'MiniDisc'
HFPA = W + 'High_Fidelity_Pure_Audio'
XRCD = W + 'XRCD'
HDCD = W + 'High_Definition_Compatible_Digital'
BSP = W + 'Blu-spec'
RT = 'https://www.roughtrade.com/gb/label/mobile-fidelity'
ESO = 'https://highfidelity.pl/@main-723&lang=en'
HQ = 'https://positive-feedback.com/high-fidelity/krakow-sonic-society-meeting-121-ultimate-hqcd-discs/'
DCC = 'https://jonimitchell.com/library/view.cfm?id=675'
MOSA = 'https://elusivedisc.com/jeff-beck-truth-numbered-limited-edition-hybrid-stereo-sacd/'
APSA = 'https://store.acousticsounds.com/d/81830/Norah_Jones-Not_Too_Late-Hybrid_Stereo_SACD'
DVDA = W + 'DVD-Audio'
CDR = W + 'CD-R'

kinds = [
 {"n": "CD", "a": "compact disc · audio CD · CD-DA", "d": "12 cm optical disc in the Compact Disc Digital Audio (Red Book) system, 16-bit, 44.1 kHz; audiobook CDs included.",
  "t": ["standard pressing", "HDCD-encoded", "Enhanced CD (CD Extra)", "CD+G (karaoke)", "jewel case", "digipak", "mini-LP (cardboard) sleeve", "Japanese edition with obi", "promo copy", "box set"],
  "s": CD,
  "x": [
   X("Gold Ultradisc", "Mobile Fidelity's gold-reflective-layer audiophile CDs, transferred from original master tapes.", "Mobile Fidelity Sound Lab", "1987", RT,
     [("Aluminium MFSL CD", "Mobile Fidelity Sound Lab", "1984", "earlier aluminium discs")], a="MFSL gold CD · Ultradisc", dt="gold layer · numbered · longbox or jewel case"),
   X("DCC Compact Classics gold CD", "24-karat gold audiophile CDs from Marshall Blonstein's label, mastered largely by Steve Hoffman.", "DCC Compact Classics", "1986", DCC,
     a="DCC gold disc", dt="24-karat gold · facsimile packaging"),
   X("XRCD", "JVC's mastering and manufacturing process for standard Red Book CDs, using its K2 processing.", "JVC", "1995", XRCD,
     [("XRCD", "JVC", "1995", ""), ("XRCD2", "JVC", "", "records to magneto-optical disc through the digital K2 regenerator"), ("XRCD24", "JVC", "", "24-bit signal path")],
     a="Extended Resolution CD", dt="generation · label licence"),
   X("SHM-CD", "CD whose polycarbonate base is replaced by a clearer proprietary material from Universal Music Japan and JVC research.", "Universal Music Japan", "2008", CD,
     a="Super High Material CD", dt="Japanese edition · obi · mini-LP sleeve"),
   X("Blu-spec CD", "Sony CD whose master is cut with a blue laser for finer pits, still standard 16-bit audio.", "Sony Music Japan", "2008", BSP,
     [("Blu-spec CD", "Sony Music Japan", "2008", ""), ("Blu-spec CD2", "Sony Music Japan", "", "updated process")], dt="Japanese edition · obi"),
   X("HQCD", "EMI Music Japan's HiQualityCD using an improved disc material, launched alongside SHM-CD and Blu-spec CD.", "EMI Music Japan", "2008", HQ,
     [("UHQCD", "Memory-Tech", "2015", "Ultimate HQCD with a UV-cured photopolymer layer")], a="HiQualityCD", dt="Japanese edition · obi"),
  ]},
 {"n": "SACD", "a": "Super Audio CD", "d": "Super Audio CD carrying DSD audio, single-layer, dual-layer or hybrid with a CD layer.",
  "t": ["hybrid (with CD layer)", "single-layer", "dual-layer", "stereo", "multichannel", "SHM-SACD", "numbered limited edition", "mini-LP gatefold"],
  "s": SACD,
  "x": [
   X("MoFi hybrid SACD", "Mobile Fidelity's numbered limited hybrid SACDs (Ultradisc UHR) with a Red Book CD layer.", "Mobile Fidelity Sound Lab", "", MOSA,
     a="Ultradisc UHR", dt="numbered · gatefold · DSD mastering chain"),
   X("Analogue Productions hybrid SACD", "Analogue Productions' hybrid stereo SACD reissues, playable in CD and SACD players.", "Analogue Productions", "", APSA,
     dt="CAPP catalogue · stereo or multichannel"),
   X("Esoteric SACD", "Esoteric's hybrid stereo SACD reissues of classic recordings, newly remastered with JVC in the DSD domain.", "Esoteric", "c. 2007", ESO,
     dt="ESSG catalogue · single disc or box"),
  ]},
 {"n": "DVD-Audio", "a": "DVD-A · HDAD", "d": "DVD-format disc carrying high-resolution PCM audio, up to 24-bit/192 kHz stereo or multichannel.",
  "t": ["stereo", "5.1 multichannel", "MLP-compressed", "with Dolby Digital video-zone track", "DualDisc", "HDAD (DVD-Video and DVD-Audio sides)"],
  "s": DVDA,
  "m": [["HDAD", "Classic Records"]]},
 {"n": "Mini CD", "a": "3-inch CD · 8 cm CD · CD single", "d": "8 cm compact disc holding about 24 minutes, needing a tray recess or adapter.",
  "t": ["CD single", "snap-pack", "jewel case", "business-card shape"],
  "s": CD},
 {"n": "CD-R", "a": "recordable compact disc · CD-RW", "d": "Recordable compact disc written once in a CD burner, sold blank or as a short-run release.",
  "t": ["cyanine dye", "phthalocyanine dye", "azo dye", "gold archival", "74-minute", "80-minute", "music CD-R", "CD-RW (rewritable)", "short-run release"],
  "s": CDR},
 {"n": "MiniDisc", "a": "MD · Hi-MD", "d": "Sony's 64 mm magneto-optical disc in a cartridge, recording compressed ATRAC audio.",
  "t": ["prerecorded", "blank 60-minute", "blank 74-minute", "blank 80-minute", "Hi-MD 1 GB", "MD Data"],
  "s": MD,
  "x": [
   X("Recordable MiniDisc", "Rewritable magneto-optical blank MiniDisc; Sony ended production in February 2025.", "Sony", "1992", MD,
     [("Blank MD", "Sony", "1992", "60, 74 and 80 minutes"), ("Hi-MD", "Sony", "2004", "1 GB discs for audio and data")], dt="length · colour · sealed or used"),
   X("Prerecorded MiniDisc", "Commercial album releases on MiniDisc, never widely issued by record labels.", "Sony", "1992", MD, dt="case and booklet"),
  ]},
 {"n": "Blu-ray audio disc", "a": "Blu-ray Audio · BD-A · Pure Audio Blu-ray · HFPA", "d": "Blu-ray disc carrying only high-resolution audio, 24-bit at up to 192 kHz, stereo or 5.1.",
  "t": ["stereo", "5.1 surround", "Dolby TrueHD", "DTS-HD Master Audio", "with download code"],
  "s": HFPA,
  "x": [
   X("Pure Audio Blu-ray", "German initiative by msm-studios for audio-only Blu-ray discs.", "msm-studios", "2009", HFPA, dt="stereo or surround · navigation without screen"),
   X("High Fidelity Pure Audio", "Audio-only Blu-ray format backed by Sony Music and Universal Music Group as a CD successor.", "Universal Music", "2013", HFPA,
     a="HFPA", dt="24/96 or 24/192 · stereo or 5.1"),
  ]},
]

K = "knowledge"
brands = [
 {"n": "Mobile Fidelity Sound Lab", "c": "United States", "f": "1977", "seg": "Specialist", "kf": "audiophile reissues", "d": "Audiophile reissue label, known for gold Ultradisc CDs from 1987 and numbered hybrid SACDs.",
  "lines": ["Gold Ultradisc", "Ultradisc UHR SACD"], "sig": ["Gold Ultradisc", "MoFi hybrid SACD"], "s": RT},
 {"n": "DCC Compact Classics", "c": "United States", "f": "1986", "seg": "Specialist", "kf": "gold CDs", "d": "Chatsworth, California audiophile label of Marshall Blonstein, known for 24-karat gold CDs mastered by Steve Hoffman.",
  "sig": ["DCC Compact Classics gold CD"], "s": DCC},
 {"n": "JVC", "c": "Japan", "f": "1927", "seg": "Mainstream", "kf": "electronics", "d": "Victor Company of Japan, developer of the XRCD process and co-developer of SHM-CD material.", "sig": ["XRCD"], "s": K},
 {"n": "Universal Music Japan", "c": "Japan", "f": "", "seg": "Mainstream", "kf": "record label", "d": "Japanese arm of Universal Music that developed SHM-CD with JVC.", "sig": ["SHM-CD"], "s": CD},
 {"n": "Sony Music Japan", "c": "Japan", "f": "", "seg": "Mainstream", "kf": "record label", "d": "Japanese Sony music company behind Blu-spec CD.", "sig": ["Blu-spec CD"], "s": BSP},
 {"n": "EMI Music Japan", "c": "Japan", "f": "", "seg": "Mainstream", "kf": "record label", "d": "Japanese EMI label that patented the HiQualityCD (HQCD).", "sig": ["HQCD"], "s": HQ},
 {"n": "Memory-Tech", "c": "Japan", "f": "", "seg": "Specialist", "kf": "disc manufacturing", "d": "Japanese disc maker that announced the UHQCD in 2015.", "sig": ["HQCD"], "s": HQ},
 {"n": "Analogue Productions", "c": "United States", "f": "1992", "seg": "Specialist", "kf": "audiophile reissues", "d": "Acoustic Sounds' audiophile reissue label in Salina, Kansas, issuing LPs and hybrid SACDs.",
  "sig": ["Analogue Productions hybrid SACD"], "s": W + 'Analogue_Productions'},
 {"n": "Esoteric", "c": "Japan", "f": "1987", "seg": "Premium", "kf": "high-end audio", "d": "Teac's high-end audio brand, which issues remastered hybrid SACD reissues.", "sig": ["Esoteric SACD"], "s": ESO},
 {"n": "Classic Records", "c": "United States", "f": "", "seg": "Specialist", "kf": "audiophile reissues", "d": "Audiophile label that issued two-sided HDAD discs.", "s": DVDA},
 {"n": "Sony", "c": "Japan", "f": "1946", "seg": "Mainstream", "kf": "electronics", "d": "Japanese electronics maker that co-developed the CD and SACD and introduced the MiniDisc in 1992.", "sig": ["Recordable MiniDisc"], "s": K},
 {"n": "msm-studios", "c": "Germany", "f": "", "seg": "Specialist", "kf": "Pure Audio Blu-ray", "d": "German studio behind the Pure Audio Blu-ray initiative of 2009.", "sig": ["Pure Audio Blu-ray"], "s": HFPA},
 {"n": "Universal Music", "c": "United States", "f": "", "seg": "Mainstream", "kf": "record label", "d": "Major record company that, with Sony Music, launched High Fidelity Pure Audio in 2013.", "sig": ["High Fidelity Pure Audio"], "s": HFPA},
]

notes = ("All five old kinds kept; MiniDisc and Blu-ray audio disc added. HDCD, SHM-SACD, Enhanced CD and CD+G kept as 't' attributes; old DVD-Audio model HDAD kept in 'm' with Classic Records from the DVD-Audio page. "
         "CD-R year taken as 1988 (CD-R article). Left out: MoFi Ultradisc II (US-made from 1992; only in search snippets), Blu-spec CD2 launch year (not on the fetched page), "
         "Esoteric start year given as c. 2007 (inferred by the review from the brand's 20th anniversary). Old CD-R/Mini CD source (duplication.com) replaced by Wikipedia pages.")
out = {"kinds": kinds, "brands": brands, "traditions": [], "notes": notes}
p = '/home/user/Possession-Taxonomy/rebuild/work/F1/shelves/01_02.json'
json.dump(out, open(p + '.tmp', 'w'), ensure_ascii=False, indent=1); os.replace(p + '.tmp', p)
print('written', len(kinds), 'kinds')
