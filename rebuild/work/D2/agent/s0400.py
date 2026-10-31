import sys; sys.path.insert(0, '/home/user/Possession-Taxonomy/rebuild/work/D2/agent')
from write import w
WP='https://en.wikipedia.org/wiki/'
G="Garmin"
kinds = [
 {"n":"Handheld GPS","a":"handheld hiking GPS · outdoor GPS","d":"Handheld outdoor GPS navigator with maps; some add a two-way radio or satellite messaging.","t":["hiking GPS","GPS with two-way radio","GPS with satellite messaging","wrist-mounted"],
  "s":"https://we3travel.com/best-handheld-gps-for-hiking-2025/",
  "m":[["eTrex 22x",G],["eTrex 32x",G],["eTrex SE",G],["eTrex Solar",G],["GPSMAP 67",G],["GPSMAP 67i",G],["GPSMAP 64sx",G],["Montana 710i",G],["Foretrex 801",G],["Rino 755t",G],["Cross Plus","TwoNav"],["NAV 100","Magellan"]],
  "r":[["eTrex",G],["GPSMAP",G],["Rino",G],["eXplorist","Magellan"],["Triton","Magellan"]]},
 {"n":"Car sat-nav","a":"portable sat-nav · car navigation unit","d":"Portable navigation unit with road maps, sold to be moved between vehicles; a mounted one is in Vehicles.","t":["car","motorcycle"],
  "s":"https://www.garmin.com/en-US/p/721063/","m":[["DriveSmart 76",G],["GO Navigator","TomTom"]],"r":[["GO","TomTom"],["Rider","TomTom"],["RoadMate","Magellan"]]},
 {"n":"Bluetooth item tracker","a":"item finder · key finder","d":"Small tag attached to an item and located through a phone's finding network.","t":["key-ring tag","card","sticker","rechargeable"],
  "s":"https://www.pocket-lint.com/gadgets/news/apple/156673-apple-airtag-vs-tile-vs-galaxy-smarttag-how-to-the-trackers-compare",
  "m":[["AirTag","Apple"],["Galaxy SmartTag2","Samsung"],["Tile Mate","Tile"],["Tile Pro","Tile"],["Chipolo Pop","Chipolo"],["Chipolo One Spot","Chipolo"],["Clip 5","Pebblebee"],["Moto Tag","Motorola"]],
  "r":[["Galaxy SmartTag","Samsung"],["Tile","Tile"]]},
 {"n":"GPS tracker","a":"cellular tracker","d":"Tracker with its own GPS and cellular link (SIM, subscription), carried by a person or put in a bag; animal trackers are in Animal Equipment, vehicle trackers in Vehicles.",
  "s":"https://www.jiobit.com/blog/jiobit-pcmag-editors-choice","m":[["Jiobit","Jiobit"],["SmartThings Tracker","Samsung"]]},
 {"n":"Satellite messenger","a":"satellite communicator","d":"Handheld device that sends and receives text messages and SOS alerts through satellites.",
  "s":"https://www.gpscentral.ca/personal-locator-beacon-comparison/",
  "m":[["inReach Mini 3",G],["inReach Mini 3 Plus",G],["inReach Messenger Plus",G],["SPOT X","SPOT"],["SPOT 4","SPOT"],["ZOLEO","Zoleo"],["Bivy Stick","ACR Electronics"],["defy satellite link","Motorola"]],
  "r":[["inReach",G]]},
 {"n":"Personal locator beacon","a":"PLB","d":"One-way distress beacon that sends a position to rescue services via satellite.","t":["with AIS","with return link"],
  "s":"https://gtc.co.uk/devices/emergency-locator-beacons/personal-locator-beacons",
  "m":[["ResQLink 400","ACR Electronics"],["ResQLink View","ACR Electronics"],["ResQLink 410 ReturnLink","ACR Electronics"],["406 Link","ACR Electronics"],["rescueME PLB1","Ocean Signal"],["rescueME PLB3 AIS","Ocean Signal"],["FastFind 220","McMurdo"],["Tron SA20","Jotron"]]},
 {"n":"Satellite hotspot","a":"satellite Wi-Fi hotspot","d":"Portable unit that links phones over Wi-Fi to a satellite network for calls, messages and data, with no keypad or screen of its own.",
  "s":"https://satellitephonestore.com/catalog/sale/details/inmarsat-isatphone-2-satellite-phone",
  "m":[["Iridium GO!","Iridium"],["Iridium GO! exec","Iridium"],["Thuraya WE","Thuraya"],["iSavi (IsatHub)","Addvalue"]]},
]
K="knowledge"
def B(n, c, f, seg, kf, d, sig=None, s=K, rel=None):
    b = {"n": n, "c": c, "f": f, "seg": seg, "kf": kf, "d": d, "s": s}
    if sig: b["sig"] = sig
    if rel: b["rel"] = rel
    return b
brands = [
 B("Garmin","United States","1989","Professional & flagship","GPS","GPS maker leading handheld, car and satellite-messenger devices.",["eTrex","GPSMAP","inReach"]),
 B("TomTom","Netherlands","1991","Mainstream","car sat-nav","Amsterdam navigation company, founded as Palmtop Software and renamed TomTom in 2001.",["GO","Rider"],s=WP+"TomTom"),
 B("Magellan","United States","","Heritage manufactory","first handheld GPS","Maker of the NAV 100 (1989), reportedly the first commercial handheld GPS; owned by MiTAC since 2008.",["NAV 100","eXplorist","RoadMate"],s=WP+"Magellan_Navigation"),
 B("TwoNav","Spain","","Specialist","outdoor GPS","Maker of non-Garmin outdoor GPS navigators.",["Cross Plus"],s="https://we3travel.com/best-handheld-gps-for-hiking-2025/"),
 B("Apple","United States","1976","Premium","AirTag","American maker of the iPhone and AirTag.",["AirTag"]),
 B("Samsung","South Korea","1969","Mainstream","Galaxy SmartTag","South Korean electronics maker.",["Galaxy SmartTag"]),
 B("Tile","United States","2012","Mainstream","Bluetooth trackers","American Bluetooth tracker maker.",["Tile Mate","Tile Pro"]),
 B("Chipolo","Slovenia","","Mainstream","Bluetooth trackers","Tracker maker whose tags work on Apple and Google finding networks.",["Chipolo Pop","Chipolo One Spot"],s="https://www.engadget.com/best-bluetooth-tracker-140028377.html?src=rss"),
 B("Pebblebee","United States","","Specialist","rechargeable trackers","Maker of rechargeable Bluetooth trackers.",["Clip"],s="https://www.engadget.com/best-bluetooth-tracker-140028377.html?src=rss"),
 B("ACR Electronics","United States","","Professional & flagship","rescue beacons","Maker of the ResQLink personal locator beacons.",["ResQLink"],s="https://gtc.co.uk/devices/emergency-locator-beacons/personal-locator-beacons"),
 B("Ocean Signal","United Kingdom","","Specialist","rescue beacons","Maker of the small rescueME PLBs.",["rescueME"],s="https://gtc.co.uk/devices/emergency-locator-beacons/personal-locator-beacons"),
 B("Iridium","United States","","Professional & flagship","satellite network","Satellite network operator behind the Iridium GO! hotspots.",["Iridium GO!"],s="https://gtc.co.uk/blogs/all/exploring-the-versatility-of-the-iridium-go-exec-wifi-hotspot"),
 B("Thuraya","United Arab Emirates","","Professional & flagship","satellite network","Satellite operator; Thuraya WE hotspot made with Beam Communications.",["Thuraya WE"],s="https://www.satellitetoday.com/telecom/2017/05/17/thuraya-launches-dual-mode-satellite-lte-hotspot/"),
]
notes = ("Tier shelf trimmed: Tile cut from five SKUs to Mate and Pro (Slim, Sticker, Ultra dropped); Galaxy SmartTag/SmartTag+ replaced by SmartTag2 (SmartTag+ discontinued per Engadget); inReach Mini 2 and inReach Messenger dropped as superseded by Mini 3 / Messenger Plus; Rino 750 dropped for 755t. "
 "Added from fetched pages: Garmin GPSMAP/Montana/Foretrex, TwoNav Cross Plus, Magellan NAV 100 (historic) and ranges; Engadget test winners Chipolo Pop, Pebblebee Clip 5, Chipolo One Spot, Moto Tag; ACR ResQLink, Ocean Signal rescueME, McMurdo, Jotron PLBs; Iridium GO!/GO! exec, Thuraya WE, Addvalue iSavi hotspots. "
 "Bushnell handheld GPS not added (no fetched page names one). Handheld GPS now has a source. Kept old sources for carried-over kinds.")
w('D2','04_00',{"kinds":kinds,"brands":brands,"traditions":[],"notes":notes})
