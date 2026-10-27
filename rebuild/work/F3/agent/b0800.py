import sys; sys.path.insert(0, '/home/user/Possession-Taxonomy/rebuild/work/F3/agent')
from hb import *
SLAB = WP + "Coin_slab"
PCGSN = "https://www.pcgs.com/news/whats-the-difference-between-rattler-and-ogh"
PCGS = WP + "Professional_Coin_Grading_Service"; NGC = WP + "Numismatic_Guaranty_Company"; ANACS = WP + "ANACS_(coin_grading_company)"
PSA = WP + "Professional_Sports_Authenticator"; PMG = "https://coinweek.com/pmg-celebrates-15-years-nearly-5-million-notes-graded"
PCGSB = "https://www.coinnews.net/2022/06/09/pcgs-launches-pack-grading-and-unveils-small-size-note-holders/"
BGS = "https://allvintagecards.com/beckett-card-grading-guide/"; SGC = "https://allvintagecards.com/sgc-card-grading/"
SGCT = "https://pregradecards.com/wiki/sgc-tuxedo-history"; CGC = "https://cardlines.com/cgc-trading-cards-and-csg-merger/"
VID = "https://greendragonstuff.storesecured.com/About-Vidiforms.asp"; HAW = "https://trademarks.justia.com/owners/hawid-hans-widmaier-gmbh-co-63833"
CS = "https://www.desertcart.co.th/products/52516298"
OT = "https://www.gamestop.com/toys-games/trading-cards/products/ultra-pro-magnetic-card-holder-35pt-uv-one-touch-x-for-sleeved-cards/20019683.html"

slab = K("Grading slab", "Sealed, tamper-evident holder in which a grading service encapsulates one coin, note or card with its grade label.", SLAB,
  a="slab · graded holder · encapsulated coin or card",
  t=["coin slab", "banknote holder", "card slab", "oversize or mega holder", "with or without CAC/sticker", "with NFC chip"],
  x=[X("PCGS coin slab", "Coin holder of the first major third-party grader, the reference slab of the US coin market.", PCGSN, mk="PCGS", y="1986", a="PCGS holder",
       v=[("Rattler", "PCGS", "1986–1989", "small holder; loose coin could rattle; plain white insert"), ("Old green holder (OGH)", "PCGS", "1989–1998", "larger, firmer holder; green label"),
          ("Blue-label holder", "PCGS", "1998", "blue label replaces green"), ("Current holder", "PCGS", "", "stackable, back hologram; NFC chip in some")],
       dt="label colour · hologram · grade and designation (e.g. First Strike) · serial and barcode"),
     X("NGC coin slab", "Coin holder of the Numismatic Guaranty Company, the main rival to PCGS.", NGC, mk="NGC", y="1987",
       v=[("Hologram holder", "NGC", "1990", "holograms added to NGC slabs"), ("EdgeView holder", "NGC", "2007–2008", "Presidential dollars from 2007, all coins from 2008"),
          ("Scratch-resistant holder", "NGC", "2009", "coating added"), ("Oversize holder", "NGC", "", "coins 45–120 mm"), ("Mega holder", "NGC", "", "coins 120–180 mm")],
       dt="label type · NGC Ancients holder · size"),
     X("ANACS slab", "Holder of the grading service begun by the American Numismatic Association, grading since 1979.", ANACS, mk="ANACS", y="1979",
       v=[("ANA-era service", "ANACS", "1972–1989", "authentication from 1972, grading from 1979"), ("Post-ANA holders", "ANACS", "1989–", "after sale to Coin World's publisher")]),
     X("PMG banknote holder", "Holder of Paper Money Guaranty, the largest third-party paper-money grader, with an enclosed label.", PMG, mk="PMG", y="2005",
       dt="label: description, catalogue number, grade, certification number"),
     X("PCGS Banknote holder", "Banknote holder of PCGS's paper-money service.", PCGSB, mk="PCGS",
       v=[("Large-size note holder", "PCGS", "", "standard holder"), ("Small-size note holder", "PCGS", "2022", "US small-size, fractional and smaller world notes"),
          ("Pack holder", "PCGS", "2022", "50 or 100 consecutive notes, one grade")]),
     X("PSA card slab", "Card holder of Professional Sports Authenticator, the leading sports-card grader, founded by PCGS's owner.", PSA, mk="PSA", y="1991",
       dt="label · grade 1–10 · certification number"),
     X("BGS card slab", "Beckett Grading Services holder, known for four subgrades and colour-coded labels.", BGS, mk="Beckett Grading Services", y="1999", a="Beckett slab",
       v=[("BVG vintage holder", "Beckett Grading Services", "2001", "cards 1981 and earlier; single grade from 2005"), ("Black Label Pristine 10", "Beckett Grading Services", "2014", "10 on all four subgrades")],
       dt="label: black, gold (9.5–10), silver (8.5–9), white · subgrades: centering, corners, edges, surface"),
     X("SGC card slab", "Sportscard Guaranty holder with its black 'tuxedo' insert, favoured for vintage cards.", SGC, mk="SGC", y="1998", a="tuxedo slab",
       v=[("100-point scale holder", "SGC", "1998–2018", "grade on a 1–100 scale"), ("Tuxedo holder, 10-point scale", "SGC", "2018", "black insert; 10 Gold Label at the top")]),
     X("CGC Cards slab", "Card holder of CGC Cards, formed when CGC Trading Cards and Certified Sports Guaranty merged.", CGC, mk="CGC",
       v=[("CSG slab", "CGC", "2021", "Certified Sports Guaranty sports-card holder"), ("CGC Cards slab", "CGC", "2023", "plain label with QR code; gold Pristine 10 label")])])

coin = K("Coin and note holder", "Capsule, flip, card or sleeve made to hold and protect one coin or banknote.", "https://www.apmex.com/product/4756/air-tite-holder-direct-fit-38-mm",
  a="coin capsule · coin flip · 2x2 · currency sleeve",
  t=["round capsule (direct fit or with ring)", "vinyl or PVC-free 2x2 flip", "cardboard 2x2 (staple or self-adhesive)", "Mylar currency sleeve", "rigid currency holder"],
  m=[["Air-Tite Direct Fit capsule", "Air-Tite"]])

card = K("Card holder", "Sleeve or rigid holder made to protect one trading card.", "https://www.thepennysleever.com/",
  a="toploader · penny sleeve · card saver · one-touch",
  t=["penny sleeve (soft)", "toploader (rigid)", "semi-rigid card saver", "magnetic one-touch holder", "screw-down holder", "thickness rating (pt)"],
  x=[X("Card Saver", "Semi-rigid holder with a lip, the usual holder for sending cards to graders.", CS, mk="Cardboard Gold", a="Card Saver 1 · semi-rigid",
       v=[("Card Saver 1", "Cardboard Gold", "", "3.5 × 4.875 in")]),
     X("ONE-TOUCH magnetic holder", "Two-piece clear display case with a slide-in hinge and magnetic closure, rated by card thickness.", OT, mk="Ultra PRO International", a="one-touch · magnetic holder",
       v=[("ONE-TOUCH X", "Ultra PRO International", "", "for sleeved cards up to 35pt; UV-blocking, non-PVC")], dt="35pt to thick-card ratings · UV · border colour")],
  m=[["BCW toploaders", "BCW"], ["Ultra PRO Penny Sleeves", "Ultra PRO International"]])

mount = K("Stamp mount and hinge", "Gummed hinge or clear mount that fixes one stamp to an album page.", "https://wizardcoinsupply.com/prinz-scott-stamp-mounts-182x244.html",
  a="stamp mount · hinge · hingeless mount",
  t=["peelable gummed hinge", "black-backed clear mount", "clear-backed mount", "cut-to-size strip", "pre-cut size", "block or souvenir-sheet mount"],
  x=[X("Hawid mount", "German clear stamp mount of paper and hardened plastic foil, trademarked in 1960.", HAW, mk="Hawid", y="1960", a="Hawid strip",
       dt="black or clear back · strips or cut sizes"),
     X("Showgard mount", "Clear stamp mount sold in the US by Vidiforms, founded in 1958 to supply quality mounts.", VID, mk="Showgard",
       dt="black or clear back · strips or cut sizes")],
  m=[["Prinz/Scott Stamp Mounts", "Prinz"]])

brands = [
 B("PCGS", "United States", "1985", "coin grading", "Professional Coin Grading Service, Santa Ana grader that opened in 1986; also grades banknotes as PCGS Banknote.", PCGS, lines=["PCGS Banknote"], rel=["PSA", "NGC"]),
 B("NGC", "United States", "1987", "coin grading", "Numismatic Guaranty Company of Sarasota, Florida, part of the Certified Collectibles Group.", NGC, rel=["PMG", "CGC", "PCGS"]),
 B("ANACS", "United States", "1972", "coin grading", "Grading service begun by the American Numismatic Association, sold in 1989.", ANACS),
 B("PMG", "United States", "2005", "banknote grading", "Paper Money Guaranty, paper-money grader of the Certified Collectibles Group.", PMG, rel=["NGC", "CGC"]),
 B("PSA", "United States", "1991", "card grading", "Professional Sports Authenticator, card grader founded by PCGS owner David Hall.", PSA, rel=["PCGS", "SGC"]),
 B("Beckett Grading Services", "United States", "1999", "card grading", "Beckett's card grader, known for subgrades and the Black Label.", BGS, lines=["BGS", "BVG"]),
 B("SGC", "United States", "1998", "card grading", "Sportscard Guaranty, card grader known for vintage cards and its black 'tuxedo' slab; owned by PSA's parent since 2023–24.", SGC, rel=["PSA"]),
 B("CGC", "United States", "2000", "comic and card grading", "Certified Guaranty Company of Sarasota, whose CGC Cards service absorbed Certified Sports Guaranty in 2023.", CGC, rel=["NGC", "PMG"]),
 B("Cardboard Gold", "United States", "", "card holders", "Maker of the Card Saver semi-rigid card holder.", CS, seg="Specialist"),
 B("Ultra PRO International", "United States", "", "card supplies", "Maker of card sleeves, ONE-TOUCH holders and binders.", "knowledge", seg="Specialist"),
 B("Hawid", "Germany", "", "stamp mounts", "Hans Widmaier GmbH, German maker of Hawid stamp mounts.", HAW, seg="Specialist"),
 B("Showgard", "United States", "", "stamp mounts", "Stamp-mount brand sold by Vidiforms, founded in Brooklyn in 1958 by Robert Weisberg.", VID, seg="Specialist", rel=["Hawid"]),
]
save("08_00", [slab, coin, card, mount], brands, [],
 "Four kinds as planned: old 'Other card holders', 'Card toploader' and 'Card sleeve' merged into Card holder; 'Stamp mount' and 'Stamp hinge' merged into Stamp mount and hinge (hinge as a type). "
 "Grading slab has one archetype per grader with holder generations only where a fetched page dates them; NGC 'fatty' generations and the PCGS Gold Shield left out (only forum sources). "
 "Air-Tite, BCW and Prinz kept as flat models from the old data (no fetched page this session). Graders go to the grading-services register (seg Institution & issuer). "
 "beckett.com and several retailer pages returned 403.")
