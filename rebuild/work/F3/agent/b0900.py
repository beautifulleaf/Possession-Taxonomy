import sys; sys.path.insert(0, '/home/user/Possession-Taxonomy/rebuild/work/F3/agent')
from hb import *
SA = WP + "Stamp_album"; CF = WP + "Coin_folder"; SC = WP + "Scott_catalogue"
DONS = "https://dons-newsletter-661b14.beehiiv.com/p/premium-stamp-albums"
LT = "https://en.everybodywiki.com/Leuchtturm"; RPSL = "https://www.rpsl.org.uk/Catalogue/Detail/ctl/ClusterObject/mid/462/id/26889"
DAVO = "https://europost.nl/en/winkel/tweedehands-en-overjarig/tweedehands-albums-postzegels/davo-luxe-postzegelalbum-nederland-i-1852-1944-tweedehands/"
WHIT = "https://coinweek.com/coins/supplies/whitman-coin-folders-as-collectible-items/"
DAN = "https://wizardcoinsupply.com/product/dansco-album-us-type-major-types-from-1800.html"
LHC = "https://www.lighthouse.us/collect-coins/coin-albums"; UP = "https://ultrapro.com/collections/pro-binders"
VX = "https://vaultx.com/products/9-pocket-exo-tec-zip-binder"; PAN = "https://journalofantiques.com/?p=62286"
FDC = "https://coinsupplyexpress.com/lighthouse-first-day-cover-album-783889"; VAR = "https://www.florinus.lt/en/banknote-album-vario-f-product-1241"
CAB = "https://antiques-atlas.com/antique/mahogany_collectors_cabinet_a5798/as135a5798"
RM = "https://royalmint.com/shop/coin-care-and-display/Coin-Cabinet-21-Trays-with-Mixed-Holes"
VOL = "https://europost.nl/en/winkel/munten-accessoires/lt-ma/lt-ma-boxen-koffers-presentatie-cassettes/lt-ma-muntencassettes-volterra/leuchtturm-verzamelcassette-volterra-vario3-met-2-vaste-en-15-losse-tussenschotten/"
TRIO = "https://www.arrowfile.com/volterra-trio-deluxe-coin-case-48mm-cv48"

stamp = K("Stamp album", "An album with printed or blank pages made to hold postage stamps.",
  "https://www.leuchtturm.com/stamps-postcards-letters/lighthouse-pre-printed-albums/complete-albums",
  a="postage stamp album", t=["pre-printed", "blank or quadrille", "hingeless (mounts fitted)", "hinged", "ring, spring-back or peg binder", "annual supplements", "worldwide or one-country"],
  x=[X("Stanley Gibbons album", "Among the first stamp albums, published by the London dealer from the early 1870s.", SA, mk="Stanley Gibbons", y="1870s",
       v=[("V.R. album", "Stanley Gibbons", "early 1870s", "one of the first albums"), ("Improved album", "Stanley Gibbons", "", ""), ("Imperial album", "Stanley Gibbons", "", "illustrated")]),
     X("Scott Specialty album", "Scott's country-by-country pre-printed album, with spaces keyed to Scott catalogue numbers.", DONS, mk="Scott", a="Scott Specialty Series",
       v=[("Specialty album", "Scott", "", "one country, era or subject; detailed pages"), ("National album", "Scott", "", "major issues of one country")]),
     X("Lindner T album", "German premium album system with hingeless pre-printed pages and T-Blank pages with pre-cut strips.", RPSL, mk="Lindner", a="Lindner-T",
       v=[("Hingeless pre-printed pages", "Lindner", "", "illustrated spaces with clear mounts"), ("T-Blank pages", "Lindner", "", "pre-cut strips and clear mounts"),
          ("Lindner-T album", "Lindner", "1990", "dated example, RPSL museum")]),
     X("Leuchtturm pre-printed album", "Leuchtturm's SF-Album with transparent pockets on its 16-ring sheet format, sold as Lighthouse in North America.", LT, mk="Leuchtturm", y="1948",
       a="Lighthouse album · SF album",
       v=[("SF-Album", "Leuchtturm", "", "transparent pockets; best seller"), ("SF Illustrated album PERFECT DP", "Leuchtturm", "", "complete pre-printed album"),
          ("KaBe bi-collect album", "Leuchtturm", "1997", "premium line after KaBe-Verlag was acquired")], dt="16-ring sheets · linen hinge · binder and slipcase colours"),
     X("Davo Luxe album", "Dutch pre-printed album with a padded faux-leather binder, slipcase and wood-free paper pages.", DAVO, mk="Davo",
       v=[("Luxe Netherlands I 1852–1944", "Davo", "", "")], dt="country · period volume · mounts")])

stock = K("Stock book", "A book of strip pockets in which stamps are slotted and held loose.", "https://www.ihobb.com/c/LIGHTHOUSE_STAMP_ALBUMS.html",
  a="stockbook · stock album", t=["white or black pages", "glassine or clear strips", "bound or ring", "number of pages", "pocket size (A5 to A4)"])

coin = K("Coin album", "An album or folder of pages with holes or pockets made to hold coins.", LHC,
  a="coin folder · coin board · coin binder",
  t=["coin folder", "coin board", "screw-post album with slides or plastic-coated pages", "ring binder with pocket sheets", "pocket or flip album", "slab album"],
  x=[X("Whitman blue folder", "Folding blue board of coin holes that grew from Whitman's coin boards and led the US market for decades.", WHIT, mk="Whitman Publishing", y="1940",
       a="blue folder · Whitman folder",
       v=[("Coin board", "Whitman Publishing", "1935–1942", "single 11 × 14 in panel; penny board from 1934 per Coin folder"),
          ("First Edition folders", "Whitman Publishing", "1940–c.1942", "22 titles; glossy leatherette covers"),
          ("Second Edition folders", "Whitman Publishing", "1942–1959", "series 2.1 to 2.3"), ("Seventh Edition folders", "Whitman Publishing", "1967", "a few months; new logo"),
          ("Eighth Edition folders", "Whitman Publishing", "1967–1978", "common")], dt="title number (e.g. 9004) · edition · cover finish"),
     X("Dansco 7070 type album", "Dansco Supreme album for one example of each major US coin type from 1800.", DAN, mk="Dansco", a="Dansco 7070",
       v=[("7070 US Type, Major Types from 1800", "Dansco", "", "screw-post binder, plastic-coated pages, modern coinage page")], dt="brown leatherette · slipcase"),
     X("Leuchtturm coin album", "Leuchtturm ring-binder systems of coin sheets, sold as Lighthouse in North America.", LHC, mk="Leuchtturm", a="Lighthouse coin album",
       v=[("CLASSIC GRANDE", "Leuchtturm", "", "3-ring binders, ENCAP pages; slab sets"), ("GRANDE", "Leuchtturm", "", "padded F-series binders"),
          ("OPTIMA", "Leuchtturm", "", "classic and GIGANT ring binders"), ("NUMIS", "Leuchtturm", "", "classic ring binders"),
          ("KASKADE", "Leuchtturm", "", "USA coin albums"), ("VISTA", "Leuchtturm", "", "National Park Quarters"), ("PRESSO", "Leuchtturm", "", "lower-priced album")])])

bank = K("Banknote album", "An album of clear pocket sheets made to hold banknotes flat.", VAR, a="currency album · banknote binder",
  t=["one, two or three pockets per sheet", "padded binder with slipcase", "sheets for graded-note holders", "large-note format"],
  m=[["Banknote album Vario F", ""], ["NUMIS banknote sheets", "Leuchtturm"]])

card = K("Card binder", "A binder of pocket pages made to hold trading cards and similar cards.", UP,
  a="card album · trading card binder · portfolio",
  t=["4, 9 or 12 pockets per page", "side-loading pockets", "zip or elastic closure", "ring binder with pages", "bound portfolio"],
  x=[X("PRO-BINDER", "Ultra PRO's padded binder of side-loading pockets, from 2 to 12 pockets per page.", UP, mk="Ultra PRO International",
       v=[("9-Pocket Zippered Premium PRO-BINDER", "Ultra PRO International", "", "zip closure"), ("12-Pocket Zip PRO-BINDER", "Ultra PRO International", "", ""),
          ("ECLIPSE PRO-BINDER", "Ultra PRO International", "", "solid colours"), ("3\" Collectors Album", "Ultra PRO International", "", "ring album for sports cards")],
       dt="licensed editions (Pokémon, Magic: The Gathering) · pockets per page"),
     X("Exo-Tec Zip Binder", "Vault X zip binder of 20 pages of nine side-loading pockets, holding 360 cards.", VX, mk="Vault X",
       v=[("9-Pocket Exo-Tec Zip Binder", "Vault X", "", "water-resistant cover, acid-free pages")], dt="colourways and set editions")])

stick = K("Sticker album", "A printed album with numbered spaces into which collectible stickers are stuck.", PAN, a="sticker book · Panini album",
  t=["football", "World Cup", "entertainment licence", "complete or part-filled", "with or without loose stickers"],
  x=[X("Panini Calciatori album", "The first Panini album, of Serie A footballers, which began the Modena firm's sticker business.", PAN, mk="Panini", y="1961",
       v=[("Calciatori 1961/62", "Panini", "1961", "40 pages for 288 stickers; four cover versions, first with Nils Liedholm")]),
     X("Panini World Cup album", "Panini's FIFA-licensed World Cup sticker album, first issued for Mexico 1970.", PAN, mk="Panini", y="1970",
       v=[("Mexico 70", "Panini", "1970", "first World Cup album; 50 pages")])])

cover = K("Cover and postcard album", "An album of clear pockets made to hold envelopes, first-day covers or postcards.", FDC, a="FDC album · cover album · postcard album",
  t=["first-day cover size", "#10 envelope size", "postcard size", "bound sheets or ring binder", "one or two pockets per side"],
  m=[["Lighthouse First Day Cover Album", "Leuchtturm"]])

tray = K("Collection tray", "A tray of compartments made to hold coins, stamps or specimens.", "https://www.lighthouse.us/coin-trays-l.html",
  a="coin tray · drawer insert", t=["round or square holes by diameter", "velour or felt lining", "stackable", "for capsules or slabs"],
  m=[["Coin Tray L", "Leuchtturm"]])

cab = K("Coin cabinet", "A cabinet or case of shallow trays or drawers made to keep a coin or medal collection.", CAB, a="coin cabinet · coin case · numismatic cabinet",
  t=["antique or modern", "mahogany or other hardwood", "number of trays", "hole sizes", "lockable"],
  x=[X("Mahogany collector's cabinet", "Antique cabinet of shallow drawers behind doors, used for coins, medals and specimens.", CAB, y="c. 1900",
       dt="mahogany veneer · drawers behind panelled doors · brass handles and locks"),
     X("Handmade coin cabinet", "Modern hardwood cabinet of drilled trays, made to order.", RM,
       v=[("Coin Cabinet 21 Trays with Mixed Holes", "", "", "sold by The Royal Mint; made to order")]),
     X("Volterra coin case", "Leuchtturm case with a mahogany finish and velvet-lined trays.", VOL, mk="Leuchtturm",
       v=[("VOLTERRA VARIO3", "Leuchtturm", "", "2 fixed and 15 loose dividers; wine-red velvet"), ("Volterra Deluxe Trio", "Leuchtturm", "", "3 trays, 60 coins to 48 mm")],
       dt="mahogany wood-grain finish · tray layouts")])

brands = [
 B("Leuchtturm", "Germany", "1948", "albums", "Geesthacht maker of stamp and coin albums, founded in Hamburg by Paul Koch, sold as Lighthouse in North America.", LT, seg="Specialist",
   lines=["Lighthouse", "KaBe", "Komet", "SF-Album", "GRANDE", "OPTIMA", "NUMIS", "VOLTERRA"], rel=["Lindner"]),
 B("Stanley Gibbons", "United Kingdom", "", "stamp catalogues", "London stamp dealer and publisher of catalogues and albums.", "knowledge", seg="Specialist"),
 B("Scott", "United States", "1868", "stamp catalogues", "New York publisher of the Scott catalogue and Scott albums, founded by John Walter Scott.", SC, seg="Specialist"),
 B("Lindner", "Germany", "", "stamp albums", "German maker of premium hingeless stamp albums and the T system.", DONS, seg="Specialist", rel=["Leuchtturm"]),
 B("Davo", "Netherlands", "", "stamp albums", "Dutch publisher of pre-printed stamp albums.", "knowledge", seg="Specialist"),
 B("Whitman Publishing", "United States", "", "coin folders", "US publisher of coin boards, blue coin folders and albums.", WHIT, seg="Specialist"),
 B("Dansco", "United States", "", "coin albums", "Daniel Stamp Company of Los Angeles, rival claimant to the first coin folder and maker of Dansco albums.", CF, seg="Specialist", rel=["Whitman Publishing"]),
 B("Ultra PRO International", "United States", "", "card supplies", "Maker of card sleeves, ONE-TOUCH holders and PRO-BINDER albums.", "knowledge", seg="Specialist"),
 B("Vault X", "United Kingdom", "", "card binders", "Poole, Dorset maker of trading-card binders and sleeves.", VX, seg="Specialist"),
 B("Panini", "Italy", "1961", "sticker albums", "Modena publisher of football sticker albums, founded by the Panini brothers.", PAN, seg="Specialist"),
]
save("09_00", [stamp, stock, coin, bank, card, stick, cover, tray, cab], brands, [],
 "All five old kinds kept; four new kinds added as planned (banknote album, sticker album, cover and postcard album, coin cabinet). Coin folder is a type of coin album; Whitman editions as versions. "
 "Old Leuchtturm coin-album models and ranges (CLASSIC GRANDE, PRESSO, KASKADE, NUMIS, VISTA) became versions of the Leuchtturm coin album; old Ultra PRO binders became PRO-BINDER versions. "
 "Lindner banknote album, Lindner/Leuchtturm FDC lines and Scott Specialty start date left out (no fetched page). The Vario F banknote album page did not name its maker, so the maker is blank. "
 "Davo, Stanley Gibbons and Ultra PRO brand entries from knowledge; several retailer pages returned 403 and were retried via Firecrawl.")
