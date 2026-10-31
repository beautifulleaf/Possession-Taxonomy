import json, os
W = 'https://en.wikipedia.org/wiki/'
K = 'knowledge'
def X(n, d, mk, y, s, v=(), a="", dt=""):
    return {"n": n, "a": a, "d": d, "mk": mk, "y": y, "s": s, "v": [dict(zip(("n", "mk", "y", "d"), t)) for t in v], "dt": dt}
CC = W + 'The_Criterion_Collection'; ARR = W + 'Arrow_Films'; MOC = W + 'Masters_of_Cinema'; VS = W + 'Vinegar_Syndrome'
LD = W + 'LaserDisc'; DV = W + 'DiscoVision'; CED = W + 'Capacitance_Electronic_Disc'
PRO = 'https://www.prospectmagazine.co.uk/culture/71864/the-little-company-that-changed-cinephilia-second-run-dvd-eureka-arrow-bfi'
SH = W + 'Shout!_Studios'; SEV = W + 'Severin_Films'
IND = 'https://www.top10films.co.uk/39295-new-distributor-indicator-treats-fans-christines-uk-debut-blu-ray-ahead-john-carpenter-2017/'
KL = 'https://m.blu-ray.com/news/newsitem.php?id=14307'
HD = W + 'HD_DVD'; VCD = W + 'Video_CD'; UMB = W + 'Umbrella_Entertainment'; STB = 'https://itigic.com/what-is-a-steelbook-where-to-buy-it-advantages/'
FAN = 'https://www.fangoria.com/original/physical-media-lives/'; FLIP = W + 'BFI_Flipside'
RAD = 'https://wearecult.rocks/introducing-radiance-films-illuminating-the-finest-in-film'; E88 = 'https://www.nerdly.co.uk/?p=17452'
VV = 'https://viavision.com.au/pages/about'; SS = 'https://rue-morgue.com/blu-ray-review-cronenberg-special-edition-uk-second-sight-films/'
UHD = W + 'Ultra_HD_Blu-ray'; BD = W + 'Blu-ray'
PACK = ["Steelbook", "mediabook", "slipcover", "digipak", "limited box set", "reversible sleeve", "booklet", "spine-numbered"]

kinds = [
 {"n": "Blu-ray", "a": "Blu-ray Disc · BD", "d": "12 cm optical disc in the Blu-ray system carrying high-definition video.",
  "t": PACK + ["Blu-ray + DVD combo pack", "dual format edition", "3D Blu-ray", "region A / B / C"], "s": BD,
  "x": [
   X("The Criterion Collection Blu-ray", "Spine-numbered restored editions with essays and supplements from the label that defined the collector edition.", "The Criterion Collection", "2008", CC,
     [("First Blu-ray, spine #453", "The Criterion Collection", "2008", "December 2008"),
      ("Eclipse from the Criterion Collection", "The Criterion Collection", "", "sub-label of lower-profile, budget-oriented sets")],
     dt="spine number · booklet · supplements · packaging"),
   X("Arrow Video", "Boutique Blu-ray label for cult, horror and world cinema, with restorations and limited editions.", "Arrow Films", "2009", ARR,
     [("Arrow Video UK", "Arrow Films", "2009", "cult and horror line"), ("North American releases", "Arrow Films", "2015", ""),
      ("Arrow Academy (merged into Arrow Video)", "Arrow Films", "", "world-cinema strand, folded into Arrow Video in 2021")],
     dt="standard or limited edition · packaging"),
   X("The Masters of Cinema Series", "Eureka's uniformly branded, spine-numbered line of classic and world cinema, often called the UK counterpart of Criterion.", "Eureka Entertainment", "2004", MOC,
     [("DVD releases", "Eureka Entertainment", "2004", "line begins"), ("Blu-ray and Dual Format releases", "Eureka Entertainment", "2008", "")],
     a="MoC · Eureka Masters of Cinema", dt="spine number · booklet · Blu-ray or dual format"),
   X("BFI Flipside", "Numbered series of dual-format editions of overlooked British films from the BFI's video label.", "British Film Institute", "2009", FLIP,
     [("No. 001", "British Film Institute", "2009", "first release, May 2009")], dt="spine number · dual format (DVD + Blu-ray)"),
   X("Indicator", "Powerhouse Films' London label of classic films in limited dual-format editions with newly commissioned booklets.", "Powerhouse Films", "2017", IND,
     [("Limited dual-format edition", "Powerhouse Films", "2017", "first runs such as 5,000 copies")], dt="limited edition number · booklet · standard edition"),
   X("Second Sight limited edition", "UK big-box limited editions of cult and genre films with books and art cards, styled like VHS boxes.", "Second Sight Films", "", SS,
     [("Limited 4K UHD + Blu-ray set", "Second Sight Films", "", "120-page book and six art cards")], dt="limited box · book · art cards · UHD or Blu-ray"),
   X("Kino Lorber Studio Classics", "Kino Lorber's line of Hollywood studio catalogue films on Blu-ray and DVD.", "Kino Lorber", "2014", KL,
     [("Inaugural eight titles", "Kino Lorber", "2014", "July 2014, all Blu-ray debuts")], a="KLSC", dt="Blu-ray or DVD"),
   X("Scream Factory", "Shout! Factory's horror sub-label of new collector's releases.", "Shout! Studios", "2012", SH,
     [("Scream Factory", "Shout! Studios", "2012", "announced June 2012"), ("Shout! Select", "Shout! Studios", "2016", "sister sub-label")],
     a="Shout! Factory", dt="standard or collector's edition · Steelbook"),
   X("Vinegar Syndrome", "Restorations of cult, exploitation and once-lost adult genre films from an American archive label.", "Vinegar Syndrome", "2013", VS,
     [("DVD and Blu-ray releases", "Vinegar Syndrome", "2013", ""), ("Cinématographe", "Vinegar Syndrome", "2023", "sub-label for American cinema")],
     dt="Blu-ray or 4K UHD + Blu-ray combo"),
   X("Severin Films", "Los Angeles cult and horror label from the team behind Blue Underground.", "Severin Films", "2006", SEV, [], dt="DVD, Blu-ray or Ultra HD Blu-ray · box sets"),
   X("88 Films Italian Collection", "88 Films' numbered-spine line of Italian genre films with reversible art and booklets.", "88 Films", "2014", E88,
     [("88 Italian launch", "88 Films", "2014", "first two Blu-rays, September 2014"), ("Slasher Classics Collection", "88 Films", "", "sister numbered line")],
     a="88 Italian", dt="spine number · reversible sleeve · booklet"),
   X("Radiance Films", "UK label of obscure arthouse and genre films in limited, numbered-run Blu-ray editions.", "Radiance Films", "2023", RAD,
     [("Limited edition", "Radiance Films", "2023", "2,000 copies, full-height Scanavo case, removable OBI strip, reversible sleeve, booklet")],
     dt="limited or standard · OBI strip"),
   X("Imprint Films", "Via Vision's Australian limited-edition label of classic cinema in hardboxes with booklets and art cards.", "Via Vision Entertainment", "2020", VV,
     [("Imprint Films", "Via Vision Entertainment", "2020", "spine-numbered hardboxes"), ("Imprint Television", "Via Vision Entertainment", "2021", ""),
      ("Imprint Asia", "Via Vision Entertainment", "2023", "")], a="Imprint", dt="spine number · hardbox · art cards"),
  ]},
 {"n": "Ultra HD Blu-ray", "a": "4K Blu-ray · UHD", "d": "12 cm optical disc in the Ultra HD Blu-ray system, carrying 4K HDR video and needing a UHD player.",
  "t": PACK + ["4K UHD + Blu-ray combo", "HDR10", "Dolby Vision", "HDR10+", "50 / 66 / 100 GB"], "s": UHD,
  "x": [
   X("The Criterion Collection 4K UHD", "Criterion's spine-numbered 4K editions, usually with a Blu-ray in the package.", "The Criterion Collection", "2021", CC,
     [("First 4K UHD, spine #1104", "The Criterion Collection", "2021", "November 2021")], dt="spine number · booklet"),
   X("Second Sight 4K limited edition", "UK limited boxes pairing Dolby Vision 4K UHD with Blu-ray, a book and art cards.", "Second Sight Films", "", SS, [], dt="limited box · book · art cards"),
   X("Vinegar Syndrome 4K combo", "Vinegar Syndrome restorations issued as 4K UHD and Blu-ray combo packs.", "Vinegar Syndrome", "", VS, [], dt="combo pack · slipcover"),
   X("Shout! Studios 4K and Steelbook editions", "Shout! and Scream Factory 4K UHD releases, some in Steelbook editions.", "Shout! Studios", "", SH, [], dt="Steelbook or keep case"),
   X("Steelbook edition", "Metal-cased collector edition of a disc, trademark of the packaging maker Scanavo.", "Scanavo", "", STB,
     [("Blu-ray Steelbook", "Scanavo", "", "first issued in Germany")], a="SteelBook", dt="embossing · artwork · limited run"),
  ]},
 {"n": "DVD", "a": "DVD-Video", "d": "12 cm optical disc carrying standard-definition digital video.",
  "t": PACK + ["region 1 / 2 / 3 / 4", "NTSC or PAL", "snap case", "flipper (double-sided) disc"], "s": "https://www.hometheaterforum.com/weekly-roundup-12-2-2025/",
  "x": [
   X("The Criterion Collection DVD", "Criterion's DVD line, begun with a reset spine-number series.", "The Criterion Collection", "1998", CC, [], dt="spine number · booklet"),
   X("The Masters of Cinema Series DVD", "Eureka's first Masters of Cinema releases, beginning with silent German classics.", "Eureka Entertainment", "2004", MOC, [], dt="spine number · booklet"),
   X("Second Run", "UK DVD and Blu-ray label of world-cinema rarities founded by Mehelli Modi.", "Second Run", "", PRO, [], dt="spine number · booklet"),
  ]},
 {"n": "LaserDisc", "a": "LD · LaserVision · DiscoVision", "d": "30 cm (or 20 cm) optical disc carrying analogue video, played on a LaserDisc player.",
  "t": ["30 cm", "20 cm", "CAV (frame-accurate, about 30 min per side)", "CLV (about 60 min per side)", "PCM digital audio", "Dolby Digital (AC-3)", "DTS", "gatefold sleeve", "NTSC or PAL"],
  "s": LD,
  "x": [
   X("MCA DiscoVision disc", "The first LaserDiscs, sold by MCA under the DiscoVision name before Pioneer took the format over.", "MCA DiscoVision", "1978", DV,
     [("Atlanta test-market launch", "MCA DiscoVision", "1978", "11 December 1978")], a="DiscoVision", dt="CAV or CLV · title"),
   X("The Criterion Collection LaserDisc", "Criterion's spine-numbered LaserDiscs, which introduced the special edition, letterboxing and commentary tracks.", "The Criterion Collection", "1984", CC,
     [("Spine #1", "The Criterion Collection", "1984", "first release, 1 December 1984"), ("Spine #2", "The Criterion Collection", "1984", "first scene-specific audio commentary"),
      ("Eighth release", "The Criterion Collection", "", "first letterboxed widescreen title"), ("Spine #384", "The Criterion Collection", "1999", "last LaserDisc, March 1999")],
     dt="spine number · CAV or CLV · gatefold"),
   X("LD-G", "Pioneer's Japanese karaoke LaserDisc carrying music plus on-screen graphics.", "Pioneer", "", LD, [], dt="karaoke graphics"),
   X("Hi-Vision LD", "High-definition MUSE-encoded LaserDisc for NHK's Hi-Vision system, never officially sold in North America.", "", "1994", LD,
     [("Announced", "", "1991", ""), ("Released", "", "1994", "1,125 lines, 16:9")], a="MUSE LaserDisc", dt="needs a Hi-Vision LD player"),
  ]},
 {"n": "HD DVD", "a": "High-Definition DVD", "d": "Toshiba-backed high-definition optical disc that lost the format war to Blu-ray; needs an HD DVD player.",
  "t": ["15 GB single layer", "30 GB dual layer", "red keep case", "Steelbook"], "s": HD,
  "x": [
   X("HD DVD/DVD Combo disc", "Double-sided disc with HD DVD on one side and standard DVD on the other.", "", "", HD, [], a="Combo disc"),
   X("HD DVD/DVD Twin disc", "Single-sided disc with up to three layers shared between HD DVD and DVD.", "", "", HD, [], a="Twin format disc"),
  ]},
 {"n": "Video CD", "a": "VCD · Compact Disc Digital Video", "d": "12 cm compact disc carrying MPEG-1 video, widely used for films in Asia before DVD.",
  "t": ["single disc", "two- or three-disc film", "Super Video CD (SVCD)", "jewel case", "keep case"], "s": VCD},
 {"n": "CED videodisc", "a": "Capacitance Electronic Disc · SelectaVision", "d": "RCA's grooved analogue video disc, read by a stylus and kept in a plastic caddy.",
  "t": ["mono (white caddy)", "stereo (blue caddy)", "single- or multi-disc title", "NTSC or PAL"], "s": CED,
  "x": [
   X("RCA SelectaVision CED", "The RCA videodisc in its caddy, about 30 cm across and holding 60 minutes of NTSC video per side.", "RCA", "1981", CED,
     [("Launch titles", "RCA", "1981", "about 50 titles co-produced with CBS Video Enterprises, March 1981"), ("Last discs", "RCA", "1986", "disc production ended")],
     a="CED · VideoDisc", dt="caddy colour · mono or stereo · studio label"),
  ]},
]

brands = [
 {"n": "The Criterion Collection", "c": "United States", "f": "1984", "seg": "Specialist", "kf": "restored editions", "d": "American home-video company that pioneered the special edition on LaserDisc and issues spine-numbered restored films.",
  "lines": ["Eclipse from the Criterion Collection"], "eras": ["The Voyager Company owner, 1985–1997", "Steven Rales owner, from 2024"], "sig": ["The Criterion Collection Blu-ray", "The Criterion Collection LaserDisc"], "rel": ["Janus Films"], "s": CC},
 {"n": "Arrow Films", "c": "United Kingdom", "f": "1991", "seg": "Specialist", "kf": "cult restorations", "d": "British independent distributor and restorer whose Arrow Video imprint is a leading boutique Blu-ray label.",
  "lines": ["Arrow Video", "Arrow Academy"], "sig": ["Arrow Video"], "s": ARR},
 {"n": "Eureka Entertainment", "c": "United Kingdom", "f": "", "seg": "Specialist", "kf": "world cinema", "d": "British home-video company that owns The Masters of Cinema Series.", "lines": ["The Masters of Cinema Series"], "sig": ["The Masters of Cinema Series"], "s": MOC},
 {"n": "British Film Institute", "c": "United Kingdom", "f": "", "seg": "Institution & issuer", "kf": "British film archive", "d": "UK film body whose BFI Video label issues archive restorations, including the Flipside series.", "lines": ["BFI Flipside"], "sig": ["BFI Flipside"], "s": FLIP},
 {"n": "Powerhouse Films", "c": "United Kingdom", "f": "", "seg": "Specialist", "kf": "limited editions", "d": "London company behind the Indicator label of classic films in limited editions.", "lines": ["Indicator"], "sig": ["Indicator"], "s": IND},
 {"n": "Second Sight Films", "c": "United Kingdom", "f": "", "seg": "Specialist", "kf": "big-box editions", "d": "UK distributor of cult and genre films known for limited box sets with books.", "sig": ["Second Sight limited edition"], "s": SS},
 {"n": "Kino Lorber", "c": "United States", "f": "", "seg": "Specialist", "kf": "classic films", "d": "American distributor of world cinema and independent film with the Studio Classics line of Hollywood titles.", "lines": ["Kino Lorber Studio Classics"], "sig": ["Kino Lorber Studio Classics"], "s": KL},
 {"n": "Shout! Studios", "c": "United States", "f": "2002", "seg": "Specialist", "kf": "cult and TV", "d": "Los Angeles home-video and music distributor, formerly Shout! Factory, founded by former Rhino Records principals.",
  "lines": ["Scream Factory", "Shout! Select", "Shout! Kids"], "sig": ["Scream Factory"], "s": SH},
 {"n": "Vinegar Syndrome", "c": "United States", "f": "2012", "seg": "Specialist", "kf": "genre restorations", "d": "Bridgeport, Connecticut archive and label founded by Joe Rubin and Ryan Emerson to restore genre films.", "lines": ["Vinegar Syndrome Pictures", "Cinématographe"], "sig": ["Vinegar Syndrome"], "s": VS},
 {"n": "Severin Films", "c": "United States", "f": "2006", "seg": "Specialist", "kf": "cult horror", "d": "Los Angeles home-video label founded by David Gregory, Carl Daft and John Cregan.", "sig": ["Severin Films"], "s": SEV},
 {"n": "88 Films", "c": "United Kingdom", "f": "", "seg": "Specialist", "kf": "genre films", "d": "UK boutique label of horror, Italian genre and martial-arts films in numbered collections.", "lines": ["88 Films Italian Collection", "Slasher Classics Collection"], "sig": ["88 Films Italian Collection"], "s": E88},
 {"n": "Radiance Films", "c": "", "f": "2022", "seg": "Specialist", "kf": "arthouse rarities", "d": "Label founded by Francesco Simeoni, formerly of Arrow, issuing limited Blu-ray editions from January 2023.", "sig": ["Radiance Films"], "s": RAD},
 {"n": "Umbrella Entertainment", "c": "Australia", "f": "2001", "seg": "Specialist", "kf": "Australian films", "d": "Australian distributor founded by Jeff Harrison, known for restored Australian classics on disc; trading as Umbrella from 2025.", "s": UMB},
 {"n": "Via Vision Entertainment", "c": "Australia", "f": "2006", "seg": "Specialist", "kf": "Imprint label", "d": "Melbourne home-entertainment arm of the Dainty Group, owner of the Imprint Films label.", "lines": ["Imprint Films", "Imprint Television", "Imprint Asia"], "sig": ["Imprint Films"], "s": VV},
 {"n": "Second Run", "c": "United Kingdom", "f": "", "seg": "Specialist", "kf": "world-cinema rarities", "d": "UK label founded by Mehelli Modi for overlooked world cinema.", "sig": ["Second Run"], "s": PRO},
 {"n": "MCA DiscoVision", "c": "United States", "f": "1969", "seg": "Heritage manufactory", "kf": "early LaserDisc", "d": "MCA division that developed the optical videodisc and sold it as DiscoVision from 1978 to 1981.", "sig": ["MCA DiscoVision disc"], "rel": ["Pioneer"], "s": DV},
 {"n": "Pioneer", "c": "Japan", "f": "", "seg": "Heritage manufactory", "kf": "LaserDisc", "d": "Japanese electronics maker that took over and promoted LaserDisc from 1981 and made players until 2009.", "sig": ["LD-G"], "rel": ["MCA DiscoVision"], "s": LD},
 {"n": "RCA", "c": "United States", "f": "", "seg": "Heritage manufactory", "kf": "CED videodisc", "d": "American electronics company that developed the CED videodisc and sold it as SelectaVision.", "sig": ["RCA SelectaVision CED"], "s": CED},
 {"n": "Scanavo", "c": "", "f": "", "seg": "Specialist", "kf": "Steelbook cases", "d": "Packaging company that holds the Steelbook trademark for metal disc cases.", "sig": ["Steelbook edition"], "s": STB},
]

notes = ("All four old kinds kept; HD DVD, Video CD and CED videodisc added. Boutique labels became archetypes (Blu-ray/UHD/DVD/LaserDisc), packaging went into t. "
         "Old LaserDisc models DiscoVision, LD-G and Hi-Vision LD became archetypes; old Criterion range became archetypes. "
         "Umbrella has a brand entry only (no attested disc line beyond Imprint, which belongs to Via Vision). Mediabook/digipak are t only. No founding year given where no fetched page stated it; DVD keeps its old source (no DVD-Video page fetched).")
out = {"kinds": kinds, "brands": brands, "traditions": [], "notes": notes}
p = 'work/F1/shelves/02_00.json'
json.dump(out, open(p + '.tmp', 'w'), ensure_ascii=False, indent=1); os.replace(p + '.tmp', p)
print('written')
