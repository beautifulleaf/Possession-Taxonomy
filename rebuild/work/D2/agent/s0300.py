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
A="Apple"; PA="Palm"; PS="Psion"; SH="Sharp"; HS="Handspring"; CQ="Compaq"; SO="Sony"; CA="Casio"
pda = [
 X("Newton MessagePad", A, "1993", WP+"MessagePad", "Apple's handwriting-recognition PDA, the device that popularised the term; cancelled 1998.",
   [V("Original MessagePad",A,"1993","original"), V("MessagePad 100",A,"1994"), V("MessagePad 110",A,"1994"), V("MessagePad 120",A,"1995"), V("MessagePad 130",A),
    V("MessagePad 2000",A,"1997"), V("MessagePad 2100",A,"1997","last"), V("eMate 300",A,"1997","clamshell Newton for schools")], a="Newton"),
 X("Psion Series 3", PS, "1991", WP+"Psion_Series_3", "Psion's clamshell palmtop with keyboard, a British business icon of the 1990s.",
   [V("Series 3",PS,"1991","original"), V("Series 3a",PS,"1993","larger screen"), V("Series 3c",PS,"1996","infrared, backlight"), V("Series 3mx",PS,"1998","last 16-bit"),
    V("Siena",PS,"1996","compact sibling"), V("Pocket Book","Acorn","","rebadged Series 3 for schools")]),
 X("Psion Series 5", PS, "1997", WP+"Psion_Series_5", "Psion's EPOC clamshell with a sliding full keyboard; ancestor of Symbian.",
   [V("Series 5",PS,"1997","original"), V("Series 5mx",PS,"1999"), V("Series 5mx Pro",PS,"","rare, RAM-loaded OS"), V("MC218","Ericsson","","rebadged 5mx"),
    V("Revo",PS,"","smaller sibling, old data"), V("Series 7",PS,"","larger sibling, old data")]),
 X("Palm Pilot", PA, "1996", WP+"Palm_(PDA)", "Palm's first pocket PDA with Graffiti handwriting; defined the category.",
   [V("Pilot 1000",PA,"1996","original"), V("Pilot 5000",PA,"1996"), V("PalmPilot Personal",PA,"1997"), V("PalmPilot Professional",PA,"1997")], a="PalmPilot · Pilot"),
 X("Palm III", PA, "1998", WP+"Palm_III", "Successor to the PalmPilot; first Palm with infrared beaming.",
   [V("Palm III",PA,"1998","original"), V("Palm IIIe",PA), V("Palm IIIx",PA), V("Palm IIIxe",PA), V("Palm IIIc",PA,"","first colour Palm")]),
 X("Palm V", PA, "1999", WP+"Palm_V", "Slim aluminium Palm with built-in rechargeable battery.",
   [V("Palm V",PA,"1999","original"), V("Palm Vx",PA,"1999","8 MB")]),
 X("Palm Tungsten and Zire", PA, "2002", WP+"Palm_(PDA)", "Palm's 2002 split into Tungsten business and Zire budget lines, ending with the TX.",
   [V("Tungsten T",PA), V("Tungsten T3",PA), V("Tungsten T5",PA), V("Tungsten E2",PA), V("Zire 21",PA), V("Zire 71",PA), V("Zire 72",PA), V("LifeDrive",PA,"2005","hard disk"), V("Palm TX",PA,"2005")]),
 X("Handspring Visor", HS, "1999", WP+"Handspring_(company)", "Palm OS PDA by Palm's founders with a Springboard expansion slot.",
   [V("Visor Solo",HS,"1999","original"), V("Visor Deluxe",HS,"2000"), V("Visor Prism",HS,"","colour"), V("Visor Platinum",HS), V("Visor Edge",HS,"2001","slim metal"), V("Visor Neo",HS,"2001"), V("Visor Pro",HS,"2001")]),
 X("Sony CLIÉ", SO, "2000", WP+"Sony_CLIÉ", "Sony's multimedia Palm OS handhelds, 2000–2005.",
   [V("PEG-S300",SO,"","S series 2000–2002"), V("PEG-N710C",SO,"","N series 2001–2002"), V("PEG-NR70V",SO,"","NR series 2002"), V("PEG-NX70V",SO,"","NX series 2002–2004"),
    V("PEG-UX50",SO,"","UX series 2003–2004"), V("PEG-TH55",SO,"","TH series 2004"), V("PEG-VZ90",SO,"","last, Japan only")], a="CLIE"),
 X("Sharp Zaurus", SH, "1993", WP+"Sharp_Zaurus", "Sharp's PDA line, later Linux-based with keyboards.",
   [V("PI-3000",SH,"1993","original"), V("ZR-5000",SH,"1995","clamshell, export"), V("SL-5500",SH,"2002","first Linux Zaurus abroad"), V("SL-C700",SH,"2003","first Linux clamshell"),
    V("SL-C760",SH,"2004"), V("SL-C3000",SH,"2004","first PDA with hard drive"), V("SL-C3200",SH,"2006")]),
 X("iPAQ", CQ, "2000", WP+"IPAQ", "Compaq's, later HP's, Pocket PC handheld line.",
   [V("H3600",CQ,"2000","original"), V("H3800",CQ), V("H3900",CQ), V("H1910",CQ,"2002"), V("H4150","HP","2003"), V("hx4700","HP","2004","VGA screen"), V("hw6500","HP","2005"), V("Glisten","HP","2009","last")]),
 X("Casio Cassiopeia", CA, "1997", WP+"Casio_Cassiopeia", "Casio's Windows CE handhelds.",
   [V("Cassiopeia A-10",CA,"1997","original Handheld PC"), V("Cassiopeia E-10",CA,"","Palm-size PC"), V("Cassiopeia E-100",CA), V("Cassiopeia E-115",CA,"","Pocket PC"), V("EM-500",CA), V("BE-300",CA,"2001")]),
]
org = [
 X("Psion Organiser", PS, "1984", WP+"Psion_Organiser", "British pocket computer with sliding cover; arguably the first usable electronic organiser.",
   [V("Organiser 1",PS,"1984","original"), V("Organiser II",PS,"1986","diary, address book, OPL; to 1996")], a="Psion Organiser I · Organiser II"),
 X("Sharp Wizard", SH, "1989", WP+"Sharp_Wizard", "Sharp's card-expandable electronic organiser, forerunner of the Zaurus.",
   [V("OZ-7000",SH,"1989","original; IQ-7000 in Europe"), V("OZ-8000",SH,"1991"), V("OZ-8200",SH,"1991"), V("OZ-8900",SH,"","clamshell, touch screen"), V("OZ-9600",SH), V("ZQ-770",SH,"","non-US model")]),
 X("Casio Digital Diary", CA, "", "https://www.computinghistory.org.uk/det/9847/Casio-Digital-Diary-SF-4000/", "Casio's pocket diary, phone book and memo organiser (SF series).",
   [V("SF-4000",CA,"1988","32K, secret area"), V("SF-R20 Digital Diary",CA,"","old data")], a="SF series"),
 X("REX", "Franklin", "", WP+"REX_5000", "Credit-card-sized PC-Card organiser synced from a computer.",
   [V("Rex-3","Franklin"), V("REX 5000","Franklin","","also Rex-Pro"), V("StarTAC ClipOn Organizer","Motorola","","repackaged REX 5000"), V("REX 6000","Xircom","","successor")]),
]
kinds = [
 {"n":"PDA","a":"palmtop · personal digital assistant","d":"Handheld personal digital assistant running applications on a small screen with stylus or keyboard.",
  "s":"https://collection.sciencemuseumgroup.org.uk/search/object_type/pda","x":pda},
 {"n":"Electronic organiser","a":"digital diary","d":"Pocket device that keeps a diary, address book and notes (digital diary).",
  "s":"https://collection.sciencemuseumgroup.org.uk/search/object_type/pda","x":org,"m":[["Business Navigator BN-40A","Casio"]]},
]
K="knowledge"
def B(n, c, f, seg, kf, d, sig, s=K, rel=None):
    b = {"n": n, "c": c, "f": f, "seg": seg, "kf": kf, "d": d, "sig": sig, "s": s}
    if rel: b["rel"] = rel
    return b
brands = [
 B("Apple","United States","1976","Premium","Newton","American computer maker; its Newton launched the PDA.",["Newton MessagePad"]),
 B("Palm","United States","1992","Mainstream","Palm OS PDAs","Maker of the Pilot and Palm handhelds, owned by U.S. Robotics then 3Com in the 1990s.",["Palm Pilot","Palm III","Palm V","Palm Tungsten and Zire"],s=WP+"Palm_(PDA)",rel=["Handspring"]),
 B("Handspring","United States","1998","Specialist","Visor","Company of Palm's founders Hawkins, Dubinsky and Colligan; later merged back into Palm.",["Handspring Visor"],s=WP+"Handspring_(company)",rel=["Palm"]),
 B("Psion","United Kingdom","1980","Specialist","palmtops","London maker of the Organiser and Series palmtops; EPOC became Symbian.",["Psion Organiser","Psion Series 3","Psion Series 5"]),
 B("Sharp","Japan","1912","Mainstream","Zaurus, Wizard","Japanese electronics maker.",["Sharp Wizard","Sharp Zaurus"]),
 B("Compaq","United States","1982","Mainstream","iPAQ","American PC maker, merged into HP in 2002.",["iPAQ"],rel=["HP"]),
 B("HP","United States","1939","Mainstream","iPAQ","American computer maker that continued the iPAQ.",["iPAQ"],rel=["Compaq"]),
 B("Sony","Japan","1946","Premium","CLIÉ","Japanese electronics group.",["Sony CLIÉ"]),
 B("Casio","Japan","1946","Mainstream","Digital Diary","Japanese electronics maker.",["Casio Digital Diary","Casio Cassiopeia"]),
 B("Franklin","United States","","Specialist","REX","Franklin Electronic Publishers; sold the REX card organiser.",["REX"],s=WP+"REX_5000"),
]
notes = ("Old models placed as versions: Newton MessagePad, Psion Revo/Series 5/5mx/Series 7, Pilot 5000, Organiser 1/II, Series 3, Siena, Sharp ZQ-770 (maker 'Sharp Corporation' -> Sharp), Casio SF-R20. "
 "Psion Series 3 and Siena moved from Electronic organiser to PDA (programmable palmtops, as the brief lists them); Pilot 5000 likewise to PDA. Casio BN-40A kept in m. "
 "CLIÉ model years given per series only. Psion Revo and Series 7 years not on fetched page, left blank. Rolodex branding of REX not confirmed on fetched page, so omitted.")
w('D2','03_00',{"kinds":kinds,"brands":brands,"traditions":[],"notes":notes})
