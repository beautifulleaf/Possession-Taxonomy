import json, os
W = 'https://en.wikipedia.org/wiki/'
K = 'knowledge'
def X(n, d, mk, y, s, v=(), a="", dt=""):
    return {"n": n, "a": a, "d": d, "mk": mk, "y": y, "s": s, "v": [dict(zip(("n", "mk", "y", "d"), t)) for t in v], "dt": dt}
COL = 'https://justglobes.co.uk/a-history-of-columbus-world-globes'; REP = W + 'Replogle_Globes'; BEL = W + 'Bellerby_%26_Co,_Globemakers'
COR = 'https://museospecola.difa.unibo.it/english/glo_55.html'; CARY = W + 'John_Cary'; POC = 'https://www.georgeglazer.com/globes/archive-pocket/pocabout.html'
BLA = 'https://www.lindahall.org/about/news/scientist-of-the-day/willem-janszoon-blaeu'; NGR = 'https://collection.sciencemuseumgroup.org.uk/objects/co57136'
HOL = 'https://www.georgeglazer.com/wpmain/product/globe-american-holbrook-terrestrial-world-3-inch-hemispheric-pocket-globe-connecticut-c-1850s-sold/'
LOC = 'https://guides.loc.gov/maps-illustrated-guide/globes'
kinds = [
 {"n": "Desktop globe", "a": "table globe · mini globe", "d": "Globe on a short base or stand made to sit on a desk or table, mini globes included.",
  "t": ["political map", "physical map", "antique-style map", "dual-mapping (changes when lit)", "illuminated", "raised relief", "gemstone", "glass or crystal sphere", "inflatable", "planetary (Moon, Mars)", "12-inch / 30 cm", "16-inch / 40 cm"],
  "s": "https://replogleglobes.com/product-category/desktop-globes/",
  "x": [
   X("Columbus Duo", "Illuminated German globe patented as the first dual-mapping globe: physical by day, political when lit.", "Columbus", "", COL,
     [("Duo", "Columbus", "", "the original dual-mapping globe"), ("Duorama", "Columbus", "", ""), ("Duo Alba", "Columbus", "", ""), ("Duo Azzurro", "Columbus", "", ""),
      ("Royal", "Columbus", "", ""), ("Imperial", "Columbus", "", ""), ("Crystal glass globe", "Columbus", "1999", "hand-laminated mouth-blown sphere")], a="Columbus illuminated", dt="diameter · map style · base"),
   X("Replogle globe", "American mass-market globes from the world's largest globe maker, from school to light-up and heirloom ranges.", "Replogle Globes", "1930", REP,
     [("Heirloom Globe Collection", "Replogle Globes", "", ""), ("Designer Series", "Replogle Globes", "", ""), ("Frank Lloyd Wright Collection", "Replogle Globes", "", ""),
      ("Education Globe Collection", "Replogle Globes", "", ""), ("Solar System Planet Globes", "Replogle Globes", "", "Moon, Mars, Venus")], dt="diameter · map style · base"),
   X("National Geographic globe", "Globe with National Geographic Society cartography, made under licence by Replogle.", "Replogle Globes", "", NGR,
     [("16-inch globe", "Replogle Globes", "1988", "designed by the NGS Cartographic Division")], dt="diameter · map style"),
   X("Bellerby handmade globe", "Bespoke London globe with hand-cut, hand-painted paper gores on a resin or composite sphere and a made-to-order base.", "Bellerby & Co", "2008", BEL,
     [("Pocket Globe", "Bellerby & Co", "", "about 12 cm"), ("80 series", "Bellerby & Co", "", "bases made with Aston Martin technicians")], dt="diameter · map colourway · base · meridian"),
  ]},
 {"n": "Floor globe", "a": "library globe", "d": "Globe on a tall floor-standing stand or frame.",
  "t": ["illuminated", "bar globe", "with horizon ring", "on castors"], "s": "https://replogleglobes.com/blog/globe-types-the-ultimate-buyers-guide",
  "x": [
   X("Bellerby Churchill Globe", "50-inch handmade floor globe modelled on the globe given to Churchill and Roosevelt in the Second World War.", "Bellerby & Co", "", BEL, [], dt="map colourway · base"),
  ],
  "m": [["Duo Azzurro Imperator", "Columbus"], ["Sherbrooke II", "Replogle Globes"]]},
 {"n": "Hanging globe", "a": "suspended globe", "d": "Globe made to hang from a ceiling or bracket.", "t": ["illuminated", "pendant light"],
  "s": "https://www.ancientsculpturegallery.com/suspension-old-world-globe-replica-model.html", "m": [["Suspension Old World Globe", "Replogle Globes"]]},
 {"n": "Antique globe", "a": "", "d": "Globe made before about 1900, of engraved or printed gores on a plaster or papier-mâché sphere.",
  "t": ["terrestrial", "celestial", "pair", "table globe", "floor globe", "original stand", "restored", "later varnish", "state of the gores"],
  "s": LOC,
  "x": [
   X("Blaeu globe", "Amsterdam globes by Willem Janszoon Blaeu, issued as terrestrial and celestial pairs.", "Blaeu", "1599", BLA,
     [("Terrestrial globe", "Blaeu", "1599", "often paired with the 1603 celestial"), ("15.5-inch pair", "Blaeu", "", "about 39 cm")], dt="date of gores · state · diameter"),
   X("Coronelli globe", "Venetian printed globes of 110 cm by Vincenzo Coronelli, smaller printed relatives of his great globes for Louis XIV.", "Vincenzo Coronelli", "1688", COR,
     [("First edition", "Vincenzo Coronelli", "1688", "dedicated to Doge Francesco Morosini"), ("Second edition", "Vincenzo Coronelli", "1692", "'Lettore Pubblico' under portrait, 1692–93"),
      ("Third edition", "Vincenzo Coronelli", "1707", "'Generale dell'Ordine dei Minoriti'"), ("Celestial globe", "Vincenzo Coronelli", "1693", "")], dt="edition · dedication · colour"),
   X("Cary globe", "Late-Georgian London globes from the Cary firm, sold as terrestrial and celestial pairs.", "John Cary", "", CARY,
     [("12-inch pair", "John Cary", "1816", "by Matthew Cary")], dt="date · diameter · stand"),
   X("Early American globe", "Commercial globes from the first American makers, often for schools.", "", "1810", LOC,
     [("James Wilson", "", "1810", "first American commercial globe maker; 13-inch terrestrial 1811"), ("Holbrook", "Holbrook", "1830s", "Connecticut school globes")], dt="maker · diameter"),
  ]},
 {"n": "Celestial globe", "a": "star globe", "d": "Globe showing the stars and constellations as seen from outside the sky sphere.",
  "t": ["antique", "modern", "illuminated", "constellation figures", "pair with terrestrial globe"], "s": BLA,
  "x": [
   X("Blaeu celestial globe", "The first celestial globe to place stars from Tycho Brahe's observations.", "Blaeu", "1599", BLA,
     [("1599", "Blaeu", "1599", "survives only as printed gores"), ("1603", "Blaeu", "1603", "adds southern constellations from de Houtman")], dt="date · state"),
   X("Coronelli celestial globe", "Venetian printed celestial globe paired with Coronelli's terrestrial globe.", "Vincenzo Coronelli", "1693", LOC, [], dt="edition"),
   X("Replogle celestial globe", "Modern globe of the celestial sphere from Replogle.", "Replogle Globes", "", REP, [], dt="diameter · illumination"),
  ]},
 {"n": "Pocket globe", "a": "", "d": "Small terrestrial globe, usually about 3 inches across, in a case lined with celestial maps.",
  "t": ["fishskin case", "celestial maps inside case", "hinged hemispheric", "with axis", "without axis"], "s": POC,
  "x": [
   X("Georgian pocket globe", "Three-inch English globe in a fishskin case lined with northern and southern sky maps, popular to about 1840.", "", "1730", POC,
     [("Senex", "", "1730", "earliest British pocket globes"), ("Ferguson", "", "", "own design after Senex"), ("Adams", "", "", "revised Ferguson plates"), ("Lane", "", "", "revised into the 19th century"), ("Cary", "John Cary", "", "")],
     dt="maker · state · case condition"),
   X("Holbrook hemispheric globe", "Hand-held American school globe that opens at the equator to show a flat double-hemisphere map.", "Holbrook", "1850s", HOL,
     [("3-inch", "Holbrook", "", "Wethersfield, Connecticut"), ("5-inch", "Holbrook", "", "")], dt="size · condition"),
  ]},
 {"n": "Globe stand", "a": "meridian · cradle", "d": "Stand, cradle or meridian ring sold for one globe.",
  "t": ["meridian ring", "horizon ring", "cradle", "table base", "tripod floor stand", "brass", "wood"],
  "s": "https://ultimateglobes.com/collections/world-globe-parts-accessories"},
]
brands = [
 {"n": "Columbus", "c": "Germany", "f": "1909", "seg": "Premium", "kf": "illuminated globes", "d": "Globe maker founded in Berlin by Paul Oestergaard, later in Stuttgart; patented the dual-mapping Duo.", "sig": ["Columbus Duo"], "s": COL},
 {"n": "Replogle Globes", "c": "United States", "f": "1930", "seg": "Mainstream", "kf": "globes", "d": "Chicago globe maker founded by Luther Replogle, the world's largest.", "sig": ["Replogle globe", "National Geographic globe"], "rel": ["National Geographic Society"], "s": REP},
 {"n": "Bellerby & Co", "c": "United Kingdom", "f": "2008", "seg": "Artisan & independent", "kf": "handmade globes", "d": "Stoke Newington studio of Peter Bellerby making bespoke hand-painted globes.", "sig": ["Bellerby handmade globe", "Bellerby Churchill Globe"], "s": BEL},
 {"n": "Blaeu", "c": "Dutch Republic", "f": "", "seg": "Heritage manufactory", "kf": "atlases and globes", "d": "Amsterdam map house of Willem and Joan Blaeu, also maker of terrestrial and celestial globes.", "sig": ["Blaeu globe", "Blaeu celestial globe"], "s": BLA},
 {"n": "Vincenzo Coronelli", "c": "Republic of Venice", "f": "", "seg": "Heritage manufactory", "kf": "globes", "d": "Venetian friar and cosmographer who made the great globes for Louis XIV and 110 cm printed globes.", "sig": ["Coronelli globe", "Coronelli celestial globe"], "s": COR},
 {"n": "John Cary", "c": "England", "f": "1783", "seg": "Heritage manufactory", "kf": "maps and globes", "d": "London engraver and mapmaker known for maps and globes.", "sig": ["Cary globe"], "s": CARY},
 {"n": "Holbrook", "c": "United States", "f": "", "seg": "Heritage manufactory", "kf": "school globes", "d": "Holbrook family's Connecticut and Ohio school-apparatus firm, maker of hinged pocket globes.", "sig": ["Holbrook hemispheric globe"], "s": HOL},
]
notes = ("Replogle 17-model SKU list and Columbus ranges trimmed to archetypes with range versions (Tolkien, Universe, Adams/Adventurer/etc. SKU names dropped). Globe stand moved in from accessories. "
         "New kinds Antique globe, Celestial globe, Pocket globe with Blaeu, Coronelli, Cary, early American (Wilson, Holbrook), Georgian pocket globes. "
         "Waypoint, Newton, Smith and Schedler left out: no fetched page confirmed them. Illuminated, relief, gemstone are t.")
out = {"kinds": kinds, "brands": brands, "traditions": [], "notes": notes}
p = 'work/F1/shelves/06_02.json'
json.dump(out, open(p + '.tmp', 'w'), ensure_ascii=False, indent=1); os.replace(p + '.tmp', p)
print('written')
