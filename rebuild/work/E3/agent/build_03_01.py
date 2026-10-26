import json, os
W = 'https://en.wikipedia.org/wiki/'
ZG = 'https://www.andertons.co.uk/guide-to-zildjian-cymbals'
ZC = 'https://zildjian.com/collections/cymbals'
SG = 'https://andertons.co.uk/guide-to-sabian-cymbals'
P2002 = 'https://www.paiste.com/en/products/series/s2002'
PSIG = 'https://www.paiste.com/en/products/series/signature'
P602 = 'https://www.paiste.com/en/products/series/formula-602-classic'
MD = 'https://moderndrummer.com/?p=23041'
MZ = 'https://www.muzines.co.uk/articles/sabian-hh-and-aa-series-cymbals/5447'
BO = 'https://drummerszone.com/brands/profile/11/bosphorus'
AG = W + 'Istanbul_Agop_Cymbals'

def X(n, a, d, mk, y, s, v=(), dt=''):
    return {"n": n, "a": a, "d": d, "mk": mk, "y": y, "s": s,
            "v": [{"n": a_, "mk": b_, "y": c_, "d": d_} for a_, b_, c_, d_ in v], "dt": dt}

WT = ["thin", "medium-thin", "medium", "medium-heavy", "heavy"]
FIN = ["traditional (lathed) finish", "brilliant (buffed) finish", "unlathed / raw", "patina / dark finish"]
ALLOY = ["B20 bell bronze", "B8 bronze", "B12 bronze", "brass", "phosphor bronze (Paiste Signature Bronze)"]

ride = {"n": "Ride cymbal", "a": "ride",
 "d": "Large sustaining cymbal used to keep a steady beat rather than for accents; most often about 20 in.",
 "t": ["16–18 in", "20 in", "21–22 in", "24–26 in", "flat ride (no bell)", "sizzle ride (rivets or sizzler)", "crash/ride", "swish / pang ride", "dry ride", "jazz ride"] + WT + FIN + ALLOY,
 "s": W + "Ride_cymbal",
 "x": [
  X("Zildjian K ride", "K · K Zildjian", "Dark, warm Zildjian line first made by Kerope Zildjian in Constantinople; made in the US since the 1970s.", "Zildjian", "after 1865", W + "Zildjian",
    [("Constantinople-made K", "Zildjian", "after 1865", "made in the family shop under Kerope II"),
     ("Canadian K", "Zildjian", "1975–1979", "made at the Azco factory, Meductic, New Brunswick"),
     ("Norwell K", "Zildjian", "1980", "all K production moved to Norwell, Massachusetts")],
    "18–24 in · thin to heavy · traditional finish"),
  X("Zildjian K Constantinople ride", "K Con", "Zildjian line recreating old Turkish K cymbals through a 14-step hammering process; vintage, complex and dark.", "Zildjian", "", ZG,
    [("K Constantinople (21 in ride shown)", "Zildjian", "", "")], "20–22 in · thin, medium-thin low · traditional finish"),
  X("Zildjian Kerope ride", "Kerope", "Low-profile, patina-finished Zildjian K-family line voiced for jazz, big band and swing.", "Zildjian", "", ZG, [], "patina finish · special order"),
  X("Zildjian K Custom ride", "K Custom", "Dark, dry Zildjian K-family line mixing traditional and modern hammering.", "Zildjian", "", ZG, [], ""),
  X("Zildjian A ride", "A · A Zildjian · Avedis", "Bright, balanced B20 Zildjian line with fast attack, named after Avedis Zildjian.", "Zildjian", "", ZG,
    [("19 in Armand Ride", "Zildjian", "", "pictured in the Wikipedia ride article")], "bright · traditional or brilliant finish"),
  X("Paiste Formula 602 flat ride", "602 Flat Ride · Space Sound", "Bell-less ride with a dry, clearly defined stick sound, developed by Paiste in the 1960s; beloved in jazz.", "Paiste", "1960s", W + "Ride_cymbal",
    [("Formula 602 Flat Ride (originally 'Space Sound')", "Paiste", "1960s", ""),
     ("602 Flat Ride reissue, 20 in medium", "Paiste", "2010", ""),
     ("Formula 602 Classic Medium Flatride / Thin Flatride", "Paiste", "2011", "Thin Flatride 18, 20, 22 in")], "18–22 in · CuSn20 '602 Bronze'"),
  X("Paiste Formula 602 Classic ride", "602", "Paiste's Swiss hand-made CuSn20 line, warm and silvery, made since 1959 and re-created in 2011.", "Paiste", "1959", P602,
    [("Formula 602", "Paiste", "1959", ""), ("Formula 602 Classic reissue", "Paiste", "2011", "most popular models re-created"),
     ("Medium Ride", "Paiste", "", ""), ("Medium / Heavy crash-ride", "Paiste", "", "")], "CuSn20 · low to medium volume"),
  X("Paiste 2002 ride", "2002", "Paiste's CuSn8 '2002 Bronze' rock line, made since 1971.", "Paiste", "1971", P2002,
    [("2002 Ride", "Paiste", "", ""), ("2002 Power Ride", "Paiste", "", ""), ("2002 Heavy Ride", "Paiste", "", ""),
     ("2002 Big Ride 'Reverend Al's'", "Paiste", "", "with Alex Van Halen"), ("2002 Giga Bell Ride 'Psychoctopus'", "Paiste", "", "with Aquiles Priester"),
     ("2002 Swish Ride 'Signature Groove'", "Paiste", "", ""), ("2002 Flatride", "Paiste", "", "")], "CuSn8 bronze · medium-soft to very loud"),
  X("Paiste Signature ride", "Signature", "Paiste line in its patented Signature Bronze, an alloy developed for cymbals, made since 1989.", "Paiste", "1989", PSIG,
    [("Blue Bell Ride 'Rhythmatist'", "Paiste", "", ""), ("Mellow Ride", "Paiste", "", ""), ("Full Ride", "Paiste", "", ""),
     ("Dry Heavy Ride 'Monad'", "Paiste", "", ""), ("Power Ride", "Paiste", "", "")], "Signature Bronze"),
  X("Sabian HH ride", "Hand Hammered · HH", "Sabian's original hand-hammered line: low profile, dark and warm.", "Sabian", "1982", W + "Sabian_Cymbals",
    [("HH medium ride 20 in / 22 in", "Sabian", "1982", "favourites of the 1985 In Tune review"), ("HH crash ride 18 in", "Sabian", "", "")], "medium and heavy weights · to 24 in"),
  X("Sabian HHX ride", "HHX", "Sabian line bringing in darker 'Manhattan' hammering, sitting between AA brightness and HH warmth.", "Sabian", "2001", W + "Sabian_Cymbals",
    [("HHX Complex", "Sabian", "", ""), ("HHX Evolution", "Sabian", "", ""), ("HHX Legacy", "Sabian", "", ""), ("HHX Anthology", "Sabian", "", "")], "B20"),
  X("Meinl Byzance ride", "Byzance", "Meinl's high-end B20 line forged in Turkey, in Traditional, Brilliant, Jazz, Vintage, Dark and Extra Dry sub-series.", "Meinl", "", MD,
    [("Byzance Jazz Medium ride 20 / 22 in", "Meinl", "2012", ""), ("Byzance Jazz Big Apple ride 22 in", "Meinl", "2012", "")], "B20 · Traditional, Brilliant, Jazz, Vintage, Dark, Extra Dry"),
  X("Istanbul Agop ride", "Agop", "Hand-made Istanbul cymbals by Agop Tomurcuk's company and his sons, from the line begun in 1980.", "Istanbul Agop", "1980", AG,
    [("Mel Lewis signature", "Istanbul Agop", "", ""), ("OM signature", "Istanbul Agop", "", ""), ("Epoch signature", "Istanbul Agop", "", "")], "secret alloy · hand-made"),
  X("Bosphorus ride", "Bosphorus", "Fully hand-hammered Istanbul cymbals, one smith, one hammer, about 30 made a day.", "Bosphorus", "1996", BO,
    [("Master Vintage", "Bosphorus", "", "")], "100% hand-made"),
 ]}

crash = {"n": "Crash cymbal", "a": "crash",
 "d": "Cymbal for loud, sharp accents, usually 14–18 in; one or two on a standard drum kit.",
 "t": ["8–13 in", "14–16 in", "17–18 in", "19–24 in", "paper-thin", "thin crash", "crash/ride", "vented / holed crash", "orchestral clash pair (German, Viennese, French)"] + WT + FIN + ALLOY,
 "s": W + "Crash_cymbal",
 "x": [
  X("Zildjian A Custom crash", "A Custom", "Bright, smooth, glassy Zildjian line with sharp attack and little sustain.", "Zildjian", "", ZG,
    [("16 in A Custom Projection Crash", "Zildjian", "", "")], "brilliant finish"),
  X("Zildjian K Constantinople crash", "K Con", "Hand-hammered Zildjian crash recreating old Turkish K sound.", "Zildjian", "", ZG, [], ""),
  X("Paiste 2002 crash", "2002", "Paiste's CuSn8 rock crash line, made since 1971.", "Paiste", "1971", P2002,
    [("2002 Thin Crash", "Paiste", "", ""), ("2002 Crash", "Paiste", "", ""), ("2002 Medium", "Paiste", "", "crash/ride"),
     ("2002 Power Crash", "Paiste", "", ""), ("2002 Extreme Crash", "Paiste", "", ""), ("2002 Wild Crash", "Paiste", "", "")], "CuSn8"),
  X("Paiste Signature crash", "Signature", "Signature Bronze crashes, Swiss hand-made since 1989.", "Paiste", "1989", PSIG,
    [("Fast Crash", "Paiste", "", ""), ("Full Crash", "Paiste", "", ""), ("Mellow Crash", "Paiste", "", ""), ("Power Crash", "Paiste", "", "")], ""),
  X("Paiste Formula 602 Classic crash", "602 Paperthin", "Thin, delicate CuSn20 crashes of the 602 line.", "Paiste", "1959", P602,
    [("Thin Crash", "Paiste", "", ""), ("Paperthin", "Paiste", "", "")], "CuSn20"),
  X("Sabian AA crash", "Automatic Anvil · AA", "Bright, open Sabian line, one of its two original 1982 series, higher in profile than HH.", "Sabian", "1982", W + "Sabian_Cymbals", [], "B20"),
  X("Sabian AAX crash", "AAX", "Bright, cutting, controlled Sabian line.", "Sabian", "", SG,
    [("18 in AAX X-Plosion Crash", "Sabian", "", ""), ("AAX Stage", "Sabian", "", ""), ("AAX Studio", "Sabian", "", ""), ("AAX Aero", "Sabian", "", ""), ("AAX Freq", "Sabian", "", "dual lathing")], "B20"),
  X("Meinl Byzance Vintage crash", "Byzance Vintage", "Sandy, dry Turkish-made B20 crash of Meinl's Byzance line.", "Meinl", "", MD,
    [("Byzance Vintage crash 20 / 22 in", "Meinl", "2012", "")], "B20"),
 ]}

hihat = {"n": "Hi-hat cymbal", "a": "hi-hats · hats",
 "d": "Pair of cymbals mounted on a stand and closed by a pedal (sold as a pair).",
 "t": ["13 in", "14 in", "15 in", "16 in and larger", "mini hats (10–12 in)", "rippled or vented bottom", "mismatched pair"] + WT + FIN + ALLOY,
 "s": W + "Hi-hat",
 "x": [
  X("Paiste Sound Edge hi-hat", "Sound Edge", "Hi-hat pair whose bottom cymbal has a rippled edge to stop air-lock, introduced by Paiste in 1967.", "Paiste", "1967", W + "Paiste",
    [("2002 Sound Edge Hi-Hat", "Paiste", "", "the original wavy-bottom design"), ("Formula 602 Classic Sound Edge Hi-Hat", "Paiste", "", ""), ("Signature Sound Edge Hi-Hat", "Paiste", "", "")], "13–15 in"),
  X("Paiste 2002 hi-hat", "2002", "CuSn8 rock hi-hats of Paiste's 2002 line.", "Paiste", "1971", P2002,
    [("2002 Medium Hi-Hat", "Paiste", "", ""), ("2002 Heavy Hi-Hat", "Paiste", "", "")], ""),
  X("Paiste Signature hi-hat", "Signature", "Signature Bronze hi-hats.", "Paiste", "1989", PSIG,
    [("Dark Crisp Hi-Hat", "Paiste", "", ""), ("Combo Crisp Hi-Hat 'Rhythmatist'", "Paiste", "", ""), ("Medium / Heavy / Power Hi-Hat", "Paiste", "", "")], ""),
  X("Sabian HH hi-hats", "Hand Hammered", "Sabian's original hand-hammered hats, reviewed in 13 and 14 in in 1985.", "Sabian", "1982", MZ,
    [("HH 13 in / 14 in hi-hats", "Sabian", "1982", "")], "medium, heavy"),
  X("Sabian Stratus hi-hats", "Stratus Dry Hats", "Dark-leaning Sabian line; the Dry version is trashy with short sustain.", "Sabian", "", SG, [("Stratus Dry Hats", "Sabian", "", "")], ""),
 ]}

china = {"n": "China cymbal", "a": "china · china-type · trash cymbal",
 "d": "Cymbal with an upturned edge and a trashy, cutting tone, from the Chinese cymbal tradition; often mounted upside down.",
 "t": ["8–12 in (china splash)", "14–16 in", "17–18 in", "19–22 in", "square / conical bell (traditional)", "rounded bell (Novo)", "swish", "pang"] + WT + FIN,
 "s": W + "China_cymbal",
 "x": [
  X("Traditional Chinese cymbal", "Chinese · chung · jing · water cymbal", "Chinese-made cymbal with conical bell, rough inside and reversed edge; the model for every Western China-type.", "", "", W + "China_cymbal",
    [("Hubei C series china 8 in", "", "", "named in the splash article")], "8–27 in · single or paired"),
  X("Paiste 2002 Novo China", "Novo China", "China with inverted bell and upturned rim, mounted bell-up; first made in 1983.", "Paiste", "1983", W + "Paiste",
    [("2002 China", "Paiste", "", ""), ("2002 Novo China", "Paiste", "1983", ""), ("2002 Wild China", "Paiste", "", "")], ""),
  X("Sabian Rocktagon", "Rocktagon", "Octagonal Sabian cymbal between a crash and a china.", "Sabian", "", W + "China_cymbal",
    [("Rocktagon 20 in", "Sabian", "", "first size"), ("Rocktagon 16 / 18 in", "Sabian", "", ""), ("Rocktagon splash 8 / 10 in", "Sabian", "", "")], ""),
  X("Sabian AA Chinese", "AA Chinese", "Sabian AA-line china types.", "Sabian", "", SG and "https://sabian.com/cymbals/",
    [("21 in AA MantaRay Chinese", "Sabian", "", ""), ("Nova Chinese 12 / 14 in", "Sabian", "", "'mini Chinese'")], ""),
  X("Paiste Signature china", "Signature China", "Signature Bronze chinas.", "Paiste", "1989", PSIG, [("Heavy China", "Paiste", "", ""), ("Thin China", "Paiste", "", "")], ""),
  X("Zildjian FX Oriental China Trash", "Oriental China Trash", "Trashy china in Zildjian's FX effects family.", "Zildjian", "", ZG, [], ""),
 ]}

splash = {"n": "Splash cymbal", "a": "splash",
 "d": "Small, thin cymbal with a short, quick decay; most often 8 or 10 in.",
 "t": ["6–8 in", "10 in", "11–12 in", "traditional", "rock (heavier)", "thin", "china splash", "salsa splash", "bell splash", "sizzle splash"] + FIN,
 "s": W + "Splash_cymbal",
 "x": [
  X("Krupa traditional splash", "traditional splash", "Medium-weight small splash with little taper, invented and named by Gene Krupa with the Avedis Zildjian Company.", "Zildjian", "1920s–1930s", W + "Splash_cymbal", [], "6–12 in"),
  X("Copeland-era Paiste splash", "heavier splash", "Heavier splash Paiste made widely available after Stewart Copeland brought it a toy cymbal found in Asia.", "Paiste", "", W + "Splash_cymbal",
    [("2002 Splash", "Paiste", "", ""), ("Signature Splash", "Paiste", "", ""), ("11 in traditional splash with sizzler", "Paiste", "", "")], ""),
  X("Sabian AA splash", "AA Splash", "Fast, bright Sabian AA-line splash.", "Sabian", "", W + "Splash_cymbal",
    [("AA 10 in Splash", "Sabian", "", ""), ("AA Rocktagon Splash 8 / 10 in", "Sabian", "", ""), ("El Sabor Salsa Splash 13 in", "Sabian", "", "for timbales")], ""),
 ]}

fx = {"n": "Effects and stack cymbal", "a": "effects cymbal · FX cymbal · stack · bell · cup chime · O-zone · swish · sizzle · zinger",
 "d": "Cymbal made for texture or colour rather than time or accents: stacks, bells, vented and odd-shaped cymbals.",
 "t": ["stack (two or more cymbals layered)", "bell / cup chime", "vented or holed (O-zone)", "odd shape (octagonal)", "drumbal (rests on a snare)", "low-volume (perforated practice)", "sizzle / zinger"],
 "s": W + "Effects_cymbal",
 "x": [
  X("Zildjian FX stack", "FX Stack · Spiral Stacker", "Zildjian FX-family cymbals designed to be layered for short, trashy accents.", "Zildjian", "", ZG,
    [("FX Stacks", "Zildjian", "", ""), ("FX Spiral Stacker", "Zildjian", "", "")], ""),
  X("Sabian Max Stax", "Max Stax", "Sabian's thin cymbals designed for stacking.", "Sabian", "", W + "Splash_cymbal", [("Max Stax High 8 in", "Sabian", "", "")], ""),
  X("Sabian O-Zone", "O-Zone", "Vented Sabian crash with large holes for a trashier tone.", "Sabian", "", W + "Effects_cymbal", [("AAX O-Zone", "Sabian", "", "")], ""),
  X("Paiste bell and cup chime", "Mega Bell · Cup Chime", "Thick bell-type cymbals of Paiste's 2002 and Signature lines.", "Paiste", "", P2002,
    [("2002 Mega Bell", "Paiste", "", ""), ("2002 Cup Chime", "Paiste", "", ""), ("2002 Accent Cymbal", "Paiste", "", ""), ("Signature Mega Cup Chime", "Paiste", "", ""), ("Formula 602 Classic Heavy Bell 13 in", "Paiste", "", "")], ""),
  X("Zildjian L80 Low Volume", "L80", "Zildjian practice cymbals with thousands of holes, about 80% quieter.", "Zildjian", "", ZG, [], ""),
 ]}

for x in china['x']:
    if x['n'] == 'Sabian AA Chinese': x['s'] = 'https://sabian.com/cymbals/'

brands = [
 {"n": "Zildjian", "c": "United States", "f": "1623", "seg": "cymbals (full range)", "d": "Cymbal maker founded by Avedis Zildjian in Constantinople, in the US since 1928–29; now in Norwell, Massachusetts.",
  "lines": ["K", "K Constantinople", "Kerope", "K Custom", "A", "A Custom", "Z Custom", "S", "I", "Planet Z", "FX", "L80 Low Volume"],
  "eras": ["Constantinople workshop, 1623–1920s", "Quincy, Massachusetts, from 1928", "Azco, Meductic, Canada, 1968–", "Norwell, Massachusetts, from 1980"],
  "sig": ["Zildjian K ride", "Zildjian A Custom crash", "Krupa traditional splash"], "sc": ["jazz", "rock", "orchestral"], "rel": ["Sabian", "Vic Firth"], "s": W + "Zildjian"},
 {"n": "Paiste", "c": "Switzerland", "f": "1906", "seg": "cymbals and gongs (full range)", "d": "Cymbal maker founded in Saint Petersburg, now in Nottwil, Switzerland; pioneered B8 '2002 Bronze' and Signature Bronze.",
  "lines": ["Signature", "Formula 602", "Masters", "2002", "Giant Beat", "RUDE", "900", "PST"],
  "eras": ["Saint Petersburg, from 1906", "Swiss facility, from 1957"], "sig": ["Paiste Formula 602 flat ride", "Paiste 2002 crash", "Paiste Sound Edge hi-hat", "Paiste 2002 Novo China"],
  "sc": ["rock", "jazz"], "rel": [], "s": W + "Paiste"},
 {"n": "Sabian", "c": "Canada", "f": "1981", "seg": "cymbals (full range)", "d": "Cymbal maker founded by Robert Zildjian in Meductic, New Brunswick, after the Zildjian family split.",
  "lines": ["Artisan", "HHX", "HH", "AAX", "AA", "Paragon", "XSR", "SBR", "B8X", "FRX", "Stratus"], "eras": [],
  "sig": ["Sabian HH ride", "Sabian AAX crash", "Sabian Rocktagon"], "sc": ["rock", "jazz"], "rel": ["Zildjian"], "s": W + "Sabian_Cymbals"},
 {"n": "Meinl", "c": "Germany", "f": "1951", "seg": "cymbals and percussion", "d": "Percussion maker founded by Roland Meinl in Gutenstetten; its Byzance B20 cymbals are made in Turkey.",
  "lines": ["Byzance", "Mb10", "Profile", "King-Beat"], "eras": [], "sig": ["Meinl Byzance ride"], "sc": [], "rel": [], "s": W + "Meinl_Percussion"},
 {"n": "Istanbul Agop", "c": "Turkey", "f": "1980", "seg": "hand-made cymbals", "d": "Istanbul cymbal maker founded by Agop Tomurcuk, run by his sons Arman and Sarkis since 1996.",
  "lines": ["Mel Lewis", "OM", "Epoch", "Alchemy"], "eras": ["Agop Tomurcuk, 1980–1996", "Arman and Sarkis Tomurcuk, from 1996"], "sig": ["Istanbul Agop ride"], "sc": ["jazz"], "rel": [], "s": AG},
 {"n": "Bosphorus", "c": "Turkey", "f": "1996", "seg": "hand-made cymbals", "d": "Istanbul workshop founded by smiths Hasan Seker, Ibrahim Yakici and Hasan Ozdemir; fully hand-hammered.",
  "lines": ["Master Vintage"], "eras": [], "sig": ["Bosphorus ride"], "sc": ["jazz"], "rel": ["Istanbul Agop"], "s": BO},
]

trads = [
 {"n": "Turkish hand-hammered cymbal making", "g": "Metal & blades", "r": "Istanbul, Turkey", "p": "16th–17th century to present",
  "d": "Ottoman-era craft of casting and hand-hammering bronze cymbals, first for churches and military mehter bands, revived in Istanbul workshops after 1980.",
  "tech": "casting, hand-hammering and lathing of bronze; secret alloys", "mat": "bell bronze",
  "forms": ["Ride cymbal", "Crash cymbal", "Hi-hat cymbal"],
  "ctr": ["Zildjian workshop, Constantinople (from 1623)", "Istanbul Agop", "Bosphorus", "Meinl Byzance (made in Turkey)"],
  "auth": "Hand-hammered by one smith (not pneumatic hammering with added marks); maker's stamp.", "s": AG},
 {"n": "Chinese cymbal making", "g": "Metal & blades", "r": "China", "p": "cymbals in China from the 3rd–4th century AD",
  "d": "Separate tradition, possibly older than the Turkish, whose cymbals gave the West the China-type.",
  "tech": "bell bronze, conical bell, reversed edge, rough unpolished inside", "mat": "bell bronze",
  "forms": ["China cymbal"], "ctr": ["Hubei"], "auth": "Conical ('square') bell, rough-finished inside, little taper.", "s": W + "China_cymbal"},
]

notes = ("Kept all five old kinds; added Effects and stack cymbal (sourced: Wikipedia Effects cymbal). Sizes, weights, finishes and alloys are types. "
 "Archetypes are maker lines as made in each cymbal type. Left out for lack of a retrieved source: years for Zildjian A, A Custom, K Custom and K Constantinople "
 "(Zildjian site and Wikipedia give none), Meinl Byzance launch year (sources disagree, 2000 vs 2001), Paiste Giant Beat, Masters and Twenty details, "
 "Sabian Artisan/Paragon details, Istanbul Mehmet as a brand (only a search snippet), Zildjian New Beat and K Sweet (not on any fetched page). "
 "Reverb's Istanbul dating interview was blocked (403) and not retried.")

out = {"kinds": [ride, crash, hihat, china, splash, fx], "brands": brands, "traditions": trads, "notes": notes}
p = 'work/E3/shelves/03_01.json'
json.dump(out, open(p + '.tmp', 'w'), ensure_ascii=False, indent=1)
os.replace(p + '.tmp', p)
print('written')
