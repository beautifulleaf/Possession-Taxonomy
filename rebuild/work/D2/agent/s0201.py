import sys; sys.path.insert(0, '/home/user/Possession-Taxonomy/rebuild/work/D2/agent')
from write import w
WP = 'https://en.wikipedia.org/wiki/'
def V(n, mk, y='', d=''):
    v = {"n": n, "mk": mk, "y": y}
    if d: v["d"] = d
    return v
def X(n, mk, y, s, d, vs, a='', dt=''):
    x = {"n": n, "a": a, "d": d, "mk": mk, "y": y, "s": s, "v": vs}
    if dt: x["dt"] = dt
    return x
M="Meta"; XR="XREAL"; ER="Even Realities"
ring = [
 X("Oura Ring", "Oura", "2016", WP+"Oura_Health", "Finnish sleep and recovery ring that defined the consumer smart ring.",
   [V("Oura Ring Gen 1","Oura","2016","Kickstarter 2015"), V("Oura Ring Gen 2","Oura","2018"), V("Oura Ring Gen 3","Oura","2021"), V("Oura Ring 4","Oura","2024"),
    V("Oura Ring 4 Ceramic","Oura","2025"), V("Oura Ring 5","Oura","2026")], dt="ring size · titanium or ceramic · finish"),
 X("Galaxy Ring", "Samsung", "2024", WP+"Samsung_Galaxy_Ring", "Samsung's health ring, launched beside the Galaxy Watch 7.", [V("Galaxy Ring","Samsung","2024","original")]),
 X("Ultrahuman Ring", "Ultrahuman", "", WP+"Ultrahuman", "Indian subscription-free health ring.",
   [V("Ultrahuman Ring","Ultrahuman","","original"), V("Ring Air","Ultrahuman","2023","Red Dot award 2023"), V("Ring PRO","Ultrahuman","2026","third generation")]),
 X("RingConn", "RingConn", "", "https://gadgetsandwearables.com/2025/03/03/ringconn-gen-2-air-vs-gen-1-smart-ring/", "Low-cost ring with long battery life and no subscription.",
   [V("RingConn Gen 1","RingConn","","titanium, charging case"), V("RingConn Gen 2","RingConn","","sleep apnoea monitoring"), V("RingConn Gen 2 Air","RingConn","","cheaper, no case")]),
]
gl = [
 X("Google Glass", "Google", "2013", WP+"Google_Glass", "Google's head-mounted display; the Explorer Edition is the collector icon of smart glasses.",
   [V("Explorer Edition","Google","2013","developer units; public US sale 2014–2015"), V("Enterprise Edition","Google","2017"), V("Enterprise Edition 2","Google","2019")]),
 X("Spectacles", "Snap", "2016", WP+"Spectacles_(product)", "Snap's camera glasses, later AR display glasses.",
   [V("Spectacles (1st generation)","Snap","2016","original, camera only"), V("Spectacles (2nd generation)","Snap","2018"), V("Spectacles 3","Snap","2019","two cameras"),
    V("Spectacles (4th generation)","Snap","2021","first with display"), V("Spectacles (5th Gen)","Snap","2024","standalone, Snap OS"), V("Specs","Snap","2026")]),
 X("Ray-Ban Meta", M, "2021", WP+"Ray-Ban_Meta", "Camera and audio glasses made with EssilorLuxottica in Ray-Ban frames; the best-selling smart glasses.",
   [V("Ray-Ban Stories",M,"2021","original"), V("Ray-Ban Meta",M,"2023","Meta AI"), V("Oakley Meta",M,"2025"), V("Meta Ray-Ban Display",M,"2025","in-lens display, neural wristband")],
   a="Ray-Ban Stories · Meta glasses", dt="frame style (Wayfarer and others) · lenses · colour"),
 X("XREAL Air", XR, "2021", "https://www.xreal.com/about", "Display glasses that act as a large virtual screen for phones, consoles and laptops.",
   [V("Nreal Light",XR,"2019","original AR glasses"), V("XREAL Air",XR,"2021"), V("Air 2",XR,"2023"), V("Air 2 Ultra",XR,"2024"), V("XREAL One",XR,"2024"), V("XREAL One Pro",XR,"2025"), V("XREAL 1S",XR,"2025")], a="Nreal"),
 X("Even G", ER, "2024", "https://www.dezeen.com/?p=2268258", "Camera-free everyday glasses with a green heads-up display for notes, translation and navigation.",
   [V("Even G1",ER,"2024","original"), V("Even Realities G2",ER,"2025","larger display; R1 control ring")]),
]
kinds = [
 {"n":"Smart ring","a":"","d":"Finger ring with sensors that tracks health and activity.","s":"https://www.androidauthority.com/best-smart-rings-you-can-still-buy-in-us-3590872","x":ring,
  "m":[["Helio Ring","Amazfit"],["Circular Ring 2","Circular"]]},
 {"n":"Smart glasses","a":"","d":"Glasses with a see-through display, camera or speakers; a headset that encloses the eyes is in Video Games.","t":["camera and audio glasses","display glasses","AR glasses"],
  "s":"https://the-gadgeteer.com/2026-06-13/smart-glasses-worth-buying-2026","x":gl,
  "m":[["INMO GO3","INMO"],["RayNeo Air 4 Pro","RayNeo"],["AirGo V2","Solos"],["Viture Beast","Viture"]]},
]
K="knowledge"
def B(n, c, f, seg, kf, d, sig, s=K, rel=None):
    b = {"n": n, "c": c, "f": f, "seg": seg, "kf": kf, "d": d, "sig": sig, "s": s}
    if rel: b["rel"] = rel
    return b
brands = [
 B("Oura","Finland","2013","Premium","smart ring","Oulu-founded maker of the Oura Ring, now also based in San Francisco.",["Oura Ring"],s=WP+"Oura_Health"),
 B("Samsung","South Korea","1969","Mainstream","Galaxy","South Korean electronics maker.",["Galaxy Ring"]),
 B("Ultrahuman","India","2019","Specialist","smart ring","Bengaluru health-wearable maker.",["Ultrahuman Ring"],s=WP+"Ultrahuman"),
 B("RingConn","","","Value","smart ring","Smart-ring maker known for long battery and no subscription.",["RingConn"],s="https://gadgetsandwearables.com/2025/03/03/ringconn-gen-2-air-vs-gen-1-smart-ring/"),
 B("Google","United States","1998","Mainstream","Glass","American technology company.",["Google Glass"]),
 B("Snap","United States","2011","Mainstream","Spectacles","Maker of Snapchat and Spectacles glasses.",["Spectacles"]),
 B("Meta","United States","2004","Mainstream","Ray-Ban Meta","American technology company; makes smart glasses with EssilorLuxottica.",["Ray-Ban Meta"],rel=["Ray-Ban"]),
 B("XREAL","China","2017","Specialist","display glasses","AR glasses maker founded as Nreal by Chi Xu; renamed 2023.",["XREAL Air"],s="https://www.xreal.com/about"),
 B("Even Realities","China","","Specialist","camera-free glasses","Chinese maker of display smart glasses without cameras, led by Will Wang.",["Even G"],s="https://www.dezeen.com/?p=2268258"),
]
notes = ("Old models became versions: Oura Ring 4, Galaxy Ring, Ring Air, RingConn Gen 2 Air, Spectacles (5th Gen), Ray-Ban Meta, Meta Ray-Ban Display, XREAL 1S, Even Realities G2. "
 "Amazfit Helio Ring, Circular Ring 2, INMO GO3, RayNeo Air 4 Pro, Solos AirGo V2, Viture Beast kept in m (no line page fetched; Xreal and Even founding details partly unknown). "
 "Maker 'circular' normalised to 'Circular'. RingConn years left blank (fetched page gives none). Enclosed headsets stay in Video Games.")
w('D2','02_01',{"kinds":kinds,"brands":brands,"traditions":[],"notes":notes})
