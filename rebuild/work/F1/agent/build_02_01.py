import json, os
W = 'https://en.wikipedia.org/wiki/'
def X(n, d, mk, y, s, v=(), a="", dt=""):
    return {"n": n, "a": a, "d": d, "mk": mk, "y": y, "s": s, "v": [dict(zip(("n", "mk", "y", "d"), t)) for t in v], "dt": dt}
VHS = W + 'VHS'; WDC = W + 'Walt_Disney_Classics'; PC = W + 'Pre-certification_video'
WIZ = 'https://www.joblo.com/here-comes-the-amazing-big-box-wizard-video-collection/amp/'
NAS = 'https://www.bfi.org.uk/sight-and-sound/features/history-british-video-nasties'
BET = W + 'Betamax'; V2K = W + 'Video_2000'; V8 = W + '8_mm_video_format'; DV = W + 'DV_(video_format)'; WV = W + 'W-VHS'
PACK = ["cardboard slipcase", "plastic clamshell case", "big box", "ex-rental", "sealed", "watermarked or hologram sticker"]
kinds = [
 {"n": "VHS cassette", "a": "VHS · video cassette", "d": "Video recording on half-inch tape in a VHS cassette.",
  "t": PACK + ["pre-recorded", "blank", "T-120 (NTSC)", "E-180 (PAL/SECAM)", "NTSC, PAL or SECAM"], "s": VHS,
  "x": [
   X("Big-box VHS", "Oversized early-1980s rental box, larger than the standard sleeve, typical of horror and exploitation labels.", "Wizard Video", "1980", WIZ,
     [("Wizard Video big box", "Wizard Video", "1980", "Charles Band's label; returned to standard boxes after a few years for lack of shelf space"),
      ("Numbered signed reissue", "Wizard Video", "", "warehouse stock re-duplicated in black clamshells inside original boxes")],
     a="big box", dt="box size · label · ex-rental or retail · condition"),
   X("Pre-cert video", "UK tape issued before the Video Recordings Act took hold, without a BBFC certificate; often uncut.", "", "c. 1978", PC,
     [("Video nasty (DPP list)", "", "", "one of 72 titles prosecuted, 39 found obscene"), ("Pre-cert rental copy", "", "", "most cheap, rare titles over £500")],
     a="pre-certification video · video nasty", dt="no BBFC rating on front · label · big box or standard · VHS, Betamax or V2000"),
   X("Walt Disney Classics (Black Diamond)", "Disney's numbered line of animated features on VHS, named for the black diamond 'Classics' logo on the spine.", "Walt Disney Home Video", "1984", WDC,
     [("The Classics", "Walt Disney Home Video", "1984", "20 titles, December 1984 to early 1994"), ("Masterpiece Collection", "Walt Disney Home Video", "1994", "successor line"),
      ("Classics outside North America", "Walt Disney Home Video", "", "'Classics' branding continued until 2007")],
     a="Black Diamond edition", dt="clamshell case · print run · sealed or opened"),
  ]},
 {"n": "Betamax cassette", "a": "Beta · Betamax", "d": "Video recording on half-inch tape in Sony's Betamax cassette, smaller than VHS.",
  "t": ["pre-recorded", "blank", "Beta Hi-Fi (1983)", "SuperBeta (1985)", "ED-Beta (1988)", "NTSC or PAL"], "s": BET,
  "x": [
   X("Sony L-series Betamax cassette", "Sony's blank Betamax cassettes graded by tape length.", "Sony", "1975", BET,
     [("L-500", "Sony", "", "60 min at Beta I, 120 min at Beta II (NTSC)"), ("L-750", "Sony", "", "90 min at Beta I, 180 min at Beta II (NTSC)")],
     dt="tape length · sealed or used")]},
 {"n": "S-VHS cassette", "a": "Super VHS", "d": "Video recording on half-inch tape in JVC's Super VHS system (1987), needing an S-VHS deck for its full resolution.",
  "t": ["blank", "pre-recorded"], "s": VHS},
 {"n": "VHS-C cassette", "a": "compact VHS", "d": "Compact VHS cassette (1982), mainly blank for camcorders, played in a VHS deck through an adapter.",
  "t": ["VHS-C", "S-VHS-C", "with adapter"], "s": VHS},
 {"n": "W-VHS cassette", "a": "Wide-VHS", "d": "Half-inch metal-particle tape in JVC's analogue high-definition W-VHS system (1993), needing a W-VHS deck.",
  "t": ["blank", "Hi-Vision (MUSE) recording"], "s": WV},
 {"n": "Video 2000 cassette", "a": "V2000 · VCC", "d": "Two-sided half-inch chromium-dioxide cassette of the Philips–Grundig Video 2000 system (1979–1988), flipped like an audio cassette.",
  "t": ["VCC 480 (2 × 240 min)", "pre-recorded", "blank", "PAL"], "s": V2K},
 {"n": "8 mm video cassette", "a": "Video8 · Hi8 · Digital8", "d": "Small 8 mm tape cassette for camcorders, introduced by Sony and Kodak in 1984.",
  "t": ["Video8 (1984)", "Hi8 (1989)", "Digital8 (1999)"], "s": V8},
 {"n": "MiniDV cassette", "a": "DV · Mini DV", "d": "Small quarter-inch digital tape cassette of the DV format (1995), used in camcorders.",
  "t": ["DV", "HDV (2003)", "SP or LP recording", "60, 63, 80 or 90 min"], "s": DV},
]
brands = [
 {"n": "Wizard Video", "c": "United States", "f": "1980", "seg": "Specialist", "kf": "big-box VHS", "d": "Charles Band's horror and exploitation video label, known for oversized big-box tapes.", "sig": ["Big-box VHS"], "s": WIZ},
 {"n": "Walt Disney Home Video", "c": "United States", "f": "", "seg": "Mainstream", "kf": "animated features", "d": "Disney's home-video label, issuer of the Classics ('Black Diamond') and Masterpiece Collection lines.", "lines": ["Walt Disney Classics", "Masterpiece Collection"], "sig": ["Walt Disney Classics (Black Diamond)"], "s": WDC},
 {"n": "Sony", "c": "Japan", "f": "1946", "seg": "Mainstream", "kf": "Betamax", "d": "Japanese electronics maker that introduced Betamax in 1975 and co-developed Video8 and DV.", "sig": ["Sony L-series Betamax cassette"], "s": BET},
]
notes = ("All five old kinds kept (S-VHS, VHS-C, W-VHS as kinds with t); Video 2000, 8 mm video (Video8/Hi8/Digital8 as t) and MiniDV added. "
         "VHS collector forms (big box, pre-cert/video nasty, Disney Black Diamond) became archetypes; no film titles. No distributor-level archetypes for pre-cert labels: no fetched page named them. VCC 360 kept as t only from general knowledge? removed.")
notes = notes.replace(" VCC 360 kept as t only from general knowledge? removed.", "")
out = {"kinds": kinds, "brands": brands, "traditions": [], "notes": notes}
p = 'work/F1/shelves/02_01.json'
json.dump(out, open(p + '.tmp', 'w'), ensure_ascii=False, indent=1); os.replace(p + '.tmp', p)
print('written')
