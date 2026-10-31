import json,copy,os,sys
R='/home/user/Possession-Taxonomy/rebuild/'
old=json.load(open(R+'work/STR_F5/bak/F5.json'))
K={}
for dp in old['depts']:
    for s in dp['s']:
        for k in s['k']: K[k['n']]=k
WP='https://en.wikipedia.org/wiki/'
def kind(name,d=None,tt=None,keep=None,ren=None,see=None,newname=None,s=None,a=None,drop_m=False):
    o=K.get(name)
    if o is None:
        o={'n':name,'a':a or '','d':d,'s':s}
    else: o=copy.deepcopy(o)
    o.pop('t',None)
    if newname: o['n']=newname
    if d: o['d']=d
    if s: o['s']=s
    if a is not None: o['a']=a
    if tt: o['tt']=tt
    xs=[]
    for x in o.get('x',[]) or []:
        if keep and x['n'] in keep:
            x=copy.deepcopy(x)
            if ren and x['n'] in ren: x['n']=ren[x['n']]
            xs.append(x)
    if 'x' in o or xs:
        o['x']=xs
        if not xs: o.pop('x')
    if see: o['see']=see
    return o
def shelf(n,t,ax,ks): 
    o={'n':n,'t':t,'k':ks}
    if ax: o['ax']=ax
    return o
def dept(n,t,ax,s):
    o=copy.deepcopy(next(d for d in old['depts'] if d['n']==n or n in d.get('_alias',[]))) if False else None
    return {'n':n,'t':t,'ax':ax,'s':s}
D=[]
# ---------- 1 Letters
D.append(dept('Letters, autographs & manuscripts',
 'Paper valued for who wrote or signed it: signatures, letters and telegrams, diaries and handwritten documents; a printed book → Media & Publications, a blank notebook → Office & Stationery.',
 'Is the paper valued for a signature, for a message sent to someone, or for a record its writer kept?',[
 shelf('Signatures & signed objects','A signature collected on paper, a card or an object, or an object signed or used by a notable person; a signed letter → Letters shelf, a signed trading card → Coins, Stamps, Medals & Trading Cards.',
  'kinds by what carries the signature: paper or card, an object, a bound album',[
  kind('Autograph',"A person's own signature collected on a card, page, photograph or document, or cut from one.",
   [["Carrier",["Cut signature","Signed index card","Album page","Signed photograph","Signed postcard","Signed document","Signed first-day cover"]],["Signature origin",["Hand signed in person","Secretarial signature","Autopen","Rubber stamp"]],["Authentication",["PSA/DNA letter","JSA letter","Beckett letter","Seller certificate of authenticity"]]],
   keep=['White House card'],see=[["F3","Autograph card","signed trading card"],["F1","Limited signed edition","signed book"],["F3","First-day cover","signed cover"]]),
  kind('Signed & game-used memorabilia','Ball, bat, jersey or similar object signed by, or worn or used in play by, a notable person.',
   [["Object",["Ball","Bat","Jersey"]],["Status",["Signed","Game-worn","Game-used"]],["Authentication",["PSA/DNA, JSA or Beckett letter","Seller certificate of authenticity"]]],
   keep=[],see=[["F3","Relic and memorabilia card","memorabilia set into a card"]]),
  kind('Autograph album','Album kept to collect signatures, verses, drawings and messages from friends, classmates or famous people.',
   [["Period",["16th–17th century album amicorum","Victorian friendship album","20th-century school leavers' book","Celebrity autograph book"]],["Who signs",["Friends and classmates","Famous people","Group message (yosegaki or shikishi)"]]],keep=[]),
 ]),
 shelf('Letters, telegrams & cards','Messages on paper sent to a person and kept: sealed letters, telegrams and written-in greeting cards; a blank card or writing paper → Office & Stationery.',
  'kinds by how the message was sent: sealed letter, telegraph wire, greeting card',[
  kind('Letter','Written or typed message sent or kept on paper, signed letters included.',
   [["Hand and signature",["Autograph letter signed (ALS)","Typed letter signed (TLS)","Letter signed (LS)","Autograph note signed (ANS)"]],["Occasion",["Love letter","Wartime or field-post letter","Condolence letter"]],["Light postal format",["V-mail","Airgraph","Aerogramme"]]],
   keep=['Airgraph','V-mail']),
  kind('Telegram','Message sent by telegraph and delivered on a printed paper form, kept as a document.',
   [["Service",["Domestic telegram","Cablegram","Diplomatic telegram"]],["Form",["Sender's transmission form","Delivery form"]]],s=WP+'Telegram'),
  kind('Written-in greeting card','Greeting card that has been written in and kept; a blank one is in Office & Stationery.',
   [["Occasion",["Valentine","Christmas card","Birthday card"]]],keep=['Cole–Horsley Christmas card','Howland lace valentine','Prang chromolithographed Christmas card'],see=[["C5","Greeting card","blank card"]]),
 ]),
 shelf('Diaries & manuscripts','Handwritten records kept by a person or an office: dated diaries, single historical documents and written-in notebooks; bound medieval codices → Media & Publications.',
  'kinds by what is recorded: a dated life, a formal act, notes and accounts',[
  kind('Diary or journal','Written personal diary or journal kept by date.',
   [["Purpose",["Personal diary","Travel journal","War diary","Ship's log"]],["Format",["Pocket diary","Five-year diary"]]],keep=["Letts pre-printed diary"],see=[["C5","Diary or planner","blank diary"]]),
  kind('Manuscript document','Single handwritten historical document, such as a charter, indenture, land grant or decree; bound codices are in Media & Publications.',
   [["Document type",["Charter","Indenture","Land grant","Manorial roll","Ship's papers","Apprenticeship indenture","Papal bull","Firman"]],["Material",["Vellum or parchment","Paper"]]],keep=[],see=[["F1","Manuscript book","bound manuscript"]]),
  kind('Written-in notebook','Notebook that has been written in and kept; a blank one is in Office & Stationery. Commonplace books are catalogued in Media & Publications as Manuscript book.',
   [["Use",["Commonplace book","Manuscript recipe book","School exercise book","Account book"]]],see=[["C5","Notebook","blank notebook"],["F1","Manuscript book","commonplace book"]]),
 ])]))
# ---------- 2 Photographs
D.append(dept('Photographs & postcards',
 'Pictures kept as objects: postcards, photographs on metal, glass and paper, slides and film, and the albums that hold them; fine-art photography → Art, a framed print → B4.',
 'How is the picture carried: on a postcard, on a print or mount, as a slide or film, or in an album?',[
 shelf('Postcards','Cards made to be posted without an envelope, printed or photographic, used or not; a card with a stamp tied on the picture side is a maximum card.',
  'kinds by how the picture and card are made: printed, photographic, novelty, stamp-matched',[
  kind('Picture postcard','Printed picture postcard, used or not; real photo postcards are a separate kind.',
   [["Era",["Pioneer (to 1898)","Private Mailing Card (1898–1901)","Undivided back (1901–07)","Divided back (1907–15)","White border (c.1915–30)","Linen (1930s–40s)","Chrome (from 1939)"]],["Subject",["Topographic view","Greetings","Large-letter 'Greetings from'","Comic or saucy seaside","Propaganda","Artist-signed illustration"]]],
   keep=['Tuck Oilette','Photochrom postcard','Teich linen and large-letter card',"Valentine's view card",'Bamforth saucy seaside postcard','Salmon view and calendar card','Wiener Werkstätte postcard']),
  kind('Real photo postcard','Continuous-tone photograph printed on postcard-backed photographic paper rather than by a printing press.',
   [["Subject",["Studio portrait","Town view","Event or disaster","Occupational"]]],keep=['Kodak postcard-back print']),
  kind('Novelty postcard','Postcard made of an unusual material or with an added effect or mechanism.',
   [["Material",["Silk embroidered (WWI silk)","Woven silk","Leather","Aluminium, wood, copper or cork"]],["Effect or mechanism",["Hold-to-light","Mechanical","Embossed","Kaleidoscope"]],["Format",["Oversize or giant","Panoramic fold-out","Booklet","Folder"]]],keep=[]),
  kind('Maximum card','Postcard with a stamp on the picture side, tied by a first-day cancellation, whose picture matches the stamp.',s=WP+'Postcard',see=[["F3","First-day cover","same first-day cancel on an envelope"]]),
 ]),
 shelf('Photographs','Photographs kept as objects, from cased portraits to instant prints, ordered by when the format arrived; the same processes sold as art → Art.',
  'kinds by photographic format, oldest first',[
  kind('Cased photograph','Portrait on metal or glass sold in a hinged case or frame, made between the 1840s and 1880s.',
   [["Process",["Daguerreotype","Ambrotype","Amphitype","Tintype (ferrotype)"]],["Case",["Union case","Leather-covered wood","Cardboard frame","Album with cut-out windows"]]],
   s='https://www.canada.ca/en/conservation-institute/services/conservation-preservation-publications/canadian-conservation-institute-notes/care-encased-photographic-images.html',
   see=[["F2","Daguerreotype","same process sold as art"],["F2","Ambrotype","same process sold as art"],["F2","Tintype","same process sold as art"]]),
  kind('Stereoview card','Two near-identical photographs mounted side by side on a card for viewing in a stereoscope.',
   [["Mount",["Flat","Curved"]],["Base",["Card","Glass"]]],keep=['London Stereoscopic Company view','Underwood & Underwood stereograph','Keystone stereoview']),
  kind('Carte de visite','Small portrait photograph mounted on a card about 2.5 by 4 inches, common from the 1860s.',
   [["Subject",["Studio portrait","Celebrity carte","View"]]],keep=['Disdéri carte de visite']),
  kind('Cabinet card','Photograph mounted on a card about 4.25 by 6.5 inches, which replaced the carte de visite from the late 1860s.',
   [["Subject",["Studio portrait","View"]]]),
  kind('Photographic print','Photograph printed on paper or card that is not a snapshot, mounted card format or postcard.',
   [["Process",["Albumen print","Silver gelatin print","Colour print"]],["Picture",["Press photograph","Studio portrait","Snapshot (vernacular family print)"]]],keep=[],see=[["F2","Albumen print","same process sold as art"],["F2","Gelatin silver print","same process sold as art"]]),
  kind('Photo-booth strip','Strip of small prints, usually four, taken in an automatic booth and kept as a souvenir.',
   [["Layout",["Four-frame strip","Three-frame strip","Square four-image print"]],["Booth type",["Film booth (from 1925)","Digital booth","Photo-sticker booth (purikura, from 1995)"]]],s=WP+'Photo_booth'),
  kind('Instant print','Self-developing photograph from a Polaroid, Instax or similar camera, in integral or peel-apart film.',
   [["Film type",["Integral","Peel-apart pack","Peel-apart roll"]],["Format",["SX-70 and 600 (79 × 79 mm)","Instax Mini","Instax Wide","Instax Square"]]],s=WP+'Instant_film',
   see=[["F2","Instant print","same process sold as art"],["D4","Integral instant film","unused film"]]),
 ]),
 shelf('Slides, film & negatives','Developed images on transparent bases, projected or held to the light: lantern slides, negatives, 35 mm slides, View-Master reels and home-movie film.',
  'kinds by the transparent base and its viewer, oldest first',[
  kind('Lantern slide','Glass or paper slide for a magic lantern, hand-painted, printed or photographic.',
   [["Making",["Hand-painted","Printed and hand-coloured","Photographic"]],["Base",["Glass","Oiled paper"]]],s=WP+'Magic_lantern',keep=['Photographic lantern slide'],ren={'Photographic lantern slide':'Hyalotype'}),
  kind('Negative','Developed photographic negative on film or plate.',[["Base",["Glass plate","Sheet film","Roll or strip film"]]]),
  kind('Slide','Developed 35 mm colour transparency in a card or plastic mount, for a slide projector.',newname='35 mm slide',keep=['Kodachrome slide'],a='transparency · colour slide'),
  kind('View-Master reel','Cardboard disc holding seven stereo pairs of small colour transparencies for a View-Master viewer.',
   [["Subject",["Scenic and travel","Entertainment and character","Educational","Military","Commercial"]]],keep=['View-Master reel'],ren={'View-Master reel':"Sawyer's scenic reel"},s=WP+'View-Master'),
  kind('Home-movie film','Amateur cine film reel or cartridge shot at home, in 8 mm, Super 8 or 16 mm.',
   [["Gauge",["Standard 8 mm","Super 8 (1965)","16 mm"]],["Sound",["Silent","With sound track"]]],s=WP+'Super_8_film',see=[["F1","Super 8 print","released film, not home-shot"],["F1","Regular 8 mm print","released film, not home-shot"]]),
 ]),
 shelf('Albums & scrapbooks','Books, binders and sleeves made to hold prints, postcards, negatives and clippings, with or without what they hold; archival quality is the quality signal.',
  'kinds by what the album holds: prints, negatives, postcards, mixed souvenirs',[
  kind('Photo album','Album holding photographic prints; archival (acid-free, PVC-free) materials mark a good one.',
   [["Mounting",["Slip-in","Self-adhesive","Traditional mounting","Photo-corner"]],["Period",["Victorian CDV album"]]],a='family album'),
  kind('Film album','Binder or album of sleeves made to hold negatives and slides.'),
  kind('Postcard album','Album made to hold postcards, from Edwardian slot albums to plastic-leaf pages that show both sides.',
   [["Type",["Edwardian slot album","Plastic-leaf album (2, 4 or 6 per page)","Archival binder"]]],keep=[],see=[["F3","Cover and postcard album","collector album for covers and cards"]]),
  kind('Scrapbook','Book in which clippings, photographs and souvenirs are pasted and kept with captions; a blank one for sale is in Arts & Crafts materials.',
   [["Type",["Extra-illustrated (grangerised) book","Subject scrapbook","Photo-corner album","Functional scrapbook of recipes and coupons"]]],s=WP+'Scrapbooking',see=[["C4","Scrapbook album","blank album"]]),
 ])]))
# ---------- 3 Ephemera
D.append(dept('Paper ephemera',
 'Everyday printed items kept after their use: tickets, menus, labels, handbills, cards and badges; posters → Art, books and catalogues → Media & Publications, tokens → Coins, Stamps, Medals & Trading Cards.',
 'What was the item issued for: a journey or event, a social occasion, trade, marking ownership, drink and tobacco, or a campaign or film?',[
 shelf('Tickets, programmes & timetables','Paper that admitted someone to an event or journey, or told them when it ran, kept afterwards.',
  'kinds by use on the day: entry, programme, timetable, luggage, lottery',[
  kind('Ticket stub','Ticket, or its torn-off counterfoil, kept after the event or journey.',
   [["Event or journey",["Concert","Sports","Rail","Airline ticket or boarding pass","Cinema","Ocean-liner passage"]],["State",["Unused full ticket","Torn stub"]]],keep=['Edmondson railway ticket']),
  kind('Programme','Printed programme of a performance or event, kept.',[["Event",["Concert tour","Theatre","Sports matchday","Opera"]]],keep=['Playbill']),
  kind('Timetable','Printed timetable of a transport service, kept.',[["Transport",["Railway","Airline","Bus or tram","Shipping line"]]],keep=["Bradshaw's Guide"]),
  kind('Luggage label','Printed hotel, shipping-line, railway or airline label stuck on luggage, collected as graphic ephemera.',
   [["Issuer",["Hotel","Shipping line","Railway","Airline"]],["State",["Unused","Removed from luggage"]]],keep=['Richter hotel label']),
  kind('Lottery ticket','Printed lottery ticket, bingo card or scratch card kept after the draw.',[["Type",["Draw ticket","Scratch card","Sweepstake ticket","Bingo card"]]],keep=[]),
 ]),
 shelf('Social occasions & calling cards','Printed cards for a dinner, party, ceremony or visit, and cards giving a person\'s name and contact details.',
  'kinds by occasion: a meal, a party or ceremony, a life event, a visit, trade contact',[
  kind('Menu','Printed menu of a restaurant, banquet, train or voyage, kept.',[["Setting",["Ocean liner","Railway dining car","Banquet","Restaurant"]],["Type",["Menu","Wine list"]]],keep=['Cunard Line menu','White Star Line menu']),
  kind('Invitation','Printed invitation to an event, kept.',[["Occasion",["Wedding","Royal or state","Ball"]],["Print process",["Engraved","Letterpress","Thermographed"]]],keep=[]),
  kind('Life-event announcement','Printed card or notice announcing a birth, engagement, wedding, graduation or death, including funeral and memorial cards.',
   [["Event",["Birth","Engagement or wedding","Graduation","Death or funeral"]]],s=WP+'Ephemera'),
  kind('Dance card','Small booklet or card on which a ball guest noted partners for each dance, often with a cord to wear it.',
   [["Form",["Printed single-use card","Booklet with cord","Jewelled or silk-lined holder"]]],s=WP+'Dance_card'),
  kind('Visiting card',"Small printed or engraved card bearing a person's name, left or exchanged on social calls; a card giving contact details for trade is the business card.",
   [["Finish",["Engraved","Embossed","Scalloped edge","Die-cut or scrap-decorated"]],["Use",["Hidden-name card","Escort card"]]],keep=[]),
  kind('Business card',"Printed card giving a person's or firm's name and contact details.",[["Print process",["Engraved","Thermographed","Offset printed","Digital printed"]],["Owner",["Celebrity card"]]]),
 ]),
 shelf('Trade & business paper','Single printed sheets and cards issued by a firm or authority to advertise, announce or record a sale.',
  'kinds by purpose: a firm\'s advertising card, a loose sheet, a public notice, a payment record',[
  kind('Advertising trade card','Card issued by a business to advertise it; a card issued in a numbered series to be collected is in Coins, Stamps, Medals & Trading Cards.',
   [["Production",["Engraved shop card","Chromolithographed stock card","Custom-printed card","Die-cut card"]]],keep=['Au Bon Marché chromo'],see=[["F3","Non-sports trading card","collectable series card"]]),
  kind('Handbill','Single printed advertising item kept after use, such as a handbill, flyer, leaflet or detached magazine or newspaper advertisement page; a poster is in Art, a catalogue or booklet in Media & Publications.',
   [["Form",["Flyer","Leaflet","Magazine advertisement page","Newspaper advertisement"]],["Purpose",["Political leaflet","Wartime propaganda leaflet"]]],see=[["F2","Vintage poster","poster, not handbill"]]),
  kind('Broadside','Large single sheet printed on one side, issued as a public notice, ballad or announcement.',
   [["Purpose",["Proclamation","Auction or sale notice","Wanted notice","Playbill (one-sheet)","Political broadside","Poetry broadside","Ballad broadside","Execution broadside"]]],keep=[],see=[["F2","Vintage poster","poster, not broadside"]]),
  kind('Receipt','Printed or written receipt or billhead, kept.',[["Document",["Billhead","Letterhead invoice","Stamped receipt","Handwritten receipt","Till receipt"]]],keep=[]),
 ]),
 shelf('Labels, bookplates & scraps','Small printed pieces made to be stuck on something or into an album: bookplates, bookmarks, labels, matchbox labels and scraps.',
  'kinds by what the piece was stuck to or kept in: a book, a box or bottle, a matchbox, an album',[
  kind('Bookplate','Printed label pasted in a book to mark its owner, also collected and exchanged as small prints.',
   [["Print process",["Copper engraving","Woodcut","Wood engraving","Etching","Process or offset print"]],["Design",["Armorial","Pictorial","Typographic book label"]],["Use",["Exchange ex-libris"]]],keep=[]),
  kind('Bookmark','Printed, woven or card bookmark, kept as ephemera.',[["Material",["Woven silk","Celluloid","Printed card","Leather"]],["Purpose",["Advertising"]]],keep=['Stevengraph']),
  kind('Label','Printed product or trade label, kept; luggage labels and matchbox labels are separate kinds.',[["Product",["Fruit-crate","Cigar-box","Wine","Food-tin"]]],keep=[]),
  kind('Matchbox label','Printed label from a matchbox or cover of a matchbook, collected as phillumeny.',[["Item",["Matchbox label","Matchbook cover","Full box"]],["Source",["Factory collector set","Advertising label"]]],keep=[]),
  kind('Victorian scrap','Embossed, glossy chromolithographed paper image die-cut from a sheet, stuck into albums, onto screens or cards.',[["State",["Sheet with connecting strips","Single cut scrap","Pasted in album"]]],keep=['Hildesheimer scrap']),
 ]),
 shelf('Drink, tobacco & table ephemera','Paper that came with a drink, a cigar or a sugar sachet and is collected for its printing.',
  'kinds by what the paper came with: a drink, a cigar, a sugar sachet',[
  kind('Beer mat','Absorbent card or pulp mat for resting a drink, printed with a brewery or drink brand; collecting is tegestology.',
   [["Material",["Printed card","Wood pulp"]],["Issuer",["Brewery advertising","Commemorative set"]]],keep=['Friedrich Horn cardboard coaster','Sputh wood-pulp coaster'],see=[["B5","Coaster","coaster for use, not collection"]]),
  kind('Cigar band','Paper or foil loop around a cigar naming the brand or variety; collecting is vitolphilia.',[["Style",["Pictorial Golden Age","Utilitarian"]],["Material",["Paper","Foil"]]],keep=[]),
  kind('Sugar packet','Single-serving paper packet of sugar or sweetener from a restaurant, hotel or airline; collecting is sucrology.',[["Source",["Restaurant","Airline","Hotel"]],["Contents",["Sugar","Sweetener"]]],keep=["Sweet 'N Low packet"]),
 ]),
 shelf('Campaign, cinema & press items','Badges and promotional paper made to be worn, shown in a cinema lobby or handed to the press.',
  'kinds by who the item addressed: the public wearing it, a cinema audience, the press',[
  kind('Pinback button','Metal disc with a printed image or slogan and a pin fastener on the back; political, advertising and premium types.',
   [["Purpose",["Campaign","Corporate advertising","Premium"]],["Back",["Open-back","Closed-back"]]],keep=['Whitehead & Hoag celluloid button','Yellow Kid button','Pep cereal button'],see=[["A3","Pin badge","worn as jewellery"]]),
  kind('Lobby card','Small film promotion card, usually 11 × 14 in, issued in sets of eight scenes for display in cinema lobbies.',
   [["Size",["11 × 14 in","8 × 10 in (pre-1930)","Jumbo 14 × 17 in","UK front of house card"]]],keep=['National Screen Service lobby card']),
  kind('Press kit','Pre-packaged folder of promotional material given to the media, such as a film or band kit with photos and press release.',
   [["Subject",["Film","Band"]],["Form",["Paper folder","Electronic"]]],keep=[]),
 ])]))
# ---------- 4 Shares
D.append(dept('Shares, bonds & money papers',
 'Papers that state a claim to money: a share in a firm, a debt to be repaid or an order to pay; banknotes and scrip → Coins, Stamps, Medals & Trading Cards.',
 'What does the paper promise: a share in a business, repayment of a loan, or payment of a sum?',[
 shelf('Shares & bonds','Certificates of ownership in a company or of a debt owed by an issuer, collected as scripophily.',
  'kinds by the claim: ownership of a firm or a debt owed',[
  kind('Share certificate','Printed certificate of ownership of shares in a company.',
   [["Holder",["Registered","Bearer"]],["Status",["Specimen","Cancelled","Autographed"]],["Purpose",["Personalised gift share"]]],keep=['VOC share receipt','Standard Oil certificate signed by Rockefeller','Railroad stock certificate','Eastern Air Lines certificate signed by Rickenbacker','Disney stock certificate']),
  kind('Bond certificate','Printed certificate of a bond or debt owed by its issuer, often with coupons attached.',
   [["Holder",["Bearer","Registered"]],["Status",["Specimen","Cancelled","Defaulted"]],["Attachment",["With coupons"]]],keep=['Confederate cotton loan bond','Imperial Russian railway bond','Chinese Reorganisation Gold Loan bond']),
 ]),
 shelf('Cheques & payment orders','Paper orders or promises to pay a sum, kept as objects after payment.',
  'kinds by who pays: a bank, a traveller\'s issuer, a post office, the maker of a note',[
  kind('Cheque','Printed order to a bank to pay a sum, kept as an object.',[["Issued by",["Bank cheque","Banker's draft or cashier's cheque","Celebrity-signed cheque"]],["Form",["Specimen","With revenue stamp","Novelty oversized cheque"]]]),
  kind("Traveller's cheque",'Pre-paid cheque in a fixed amount for travellers, kept as an object.',[["State",["Specimen","Signed","Unused"]]],keep=['American Express Travelers Cheque','Thomas Cook circular note']),
  kind('Postal order','Money order issued by a post office and payable at another, kept as an object.',[["Issuer",["British postal order","US postal money order","International money order","Commonwealth postal order"]]]),
  kind('Promissory note','Written promise by one person to pay another a set sum, on demand or on a date, kept as a document.',
   [["Repayment",["Demand note","Mortgage note"]]],s=WP+'Promissory_note'),
 ])]))
# ---------- 5 Cards
D.append(dept('Payment, transit & phone cards',
 'Cards that pay, ride, call or open a lock; a card that proves who the holder is → Identity & travel documents.',
 'What does the card do: settle a payment, buy a fare, call or connect, or give value, membership or entry?',[
 shelf('Bank & payment cards','Cards that settle purchases from a bank, a credit line, a store account or pre-loaded value.',
  'kinds by how the payment is settled: store account, full monthly repayment, revolving credit, bank account, pre-loaded value',[
  kind('Charge plate',"Embossed metal or plastic plate issued by a store or company to identify a customer's charge account, the forerunner of the charge card.",keep=['Charga-Plate']),
  kind('Charge card','Card whose balance must be paid in full each period.',[["Level",["Standard","Gold","Platinum","Invitation-only"]],["Material",["Paper (early)","Plastic"]]],keep=['Air Travel Card','Diners Club card','American Express card']),
  kind('Credit card','Card that draws on a revolving line of credit from its issuer.',[["Tier",["Standard","Premium"]],["Material",["Plastic","Metal"]],["Issuer link",["Co-branded or affinity","Store card"]],["Holder",["Personal","Business"]],["Security",["Unsecured","Secured"]]],keep=['BankAmericard','Master Charge','Barclaycard','Access card']),
  kind('Debit card',"Card that draws directly on the holder's bank account, including cards for cash machines only.",[["Use",["ATM-only card","Point-of-sale debit"]],["Scheme",["Visa Debit","Debit Mastercard","Maestro or Switch","National scheme (Dankort, Interac, Girocard, EFTPOS)"]]]),
  kind('Prepaid e-money card','Reloadable stored-value card for small payments at many merchants, not drawing on a bank account.',[["Edition",["Regular","Limited edition","Special design"]]],keep=['Edy','nanaco','Flazz']),
 ]),
 shelf('Transit, phone & SIM cards','Cards that pre-pay a fare, a call or a mobile connection.',
  'kinds by what the stored value buys: a fare, a call, a mobile network',[
  kind('Transit card','Stored-value or pass card for public transport fares; other issuers and cards are in the brand register.',[["Technology",["Contactless smart card","Magnetic-stripe card"]],["Edition",["Commemorative or limited edition","Visitor card","Photocard"]]],
   keep=['Octopus','Oyster card','Suica','EZ-Link','T-money','Clipper','SmarTrip','MetroCard','Opal','Navigo','OV-chipkaart','Presto','Leap Card','myki']),
  kind('Telephone card','Prepaid card for public telephones; optical, chip or magnetic.',[["Technology",["Optical (Landis & Gyr, Sodeco)","Magnetic stripe","Chip smart card","Remote-memory (PIN) card"]],["State",["Mint","Used"]]],keep=['NTT telephone card','Télécarte','BT Phonecard']),
  kind('SIM card','Physical card that identifies a subscriber on a mobile network; collected mainly as early operator issues. An eSIM profile is part of a plan in Subscriptions, Memberships & Online Services.',[["Size",["Full-size (1FF)","Mini-SIM (2FF)","Micro-SIM (3FF)","Nano-SIM (4FF)"]]]),
 ]),
 shelf('Gift, membership & key cards','Cards that hold prepaid value, membership rights or lock access.',None,[
  kind('Gift & membership card','Card or certificate holding prepaid value, discounts or membership rights, issued by a retailer or club.',[["Gives",["Gift card","Gift certificate","Membership card","Loyalty card"]]]),
  kind('Key card','Card that opens a lock and names no holder, such as a hotel key card.',[["Use",["Hotel key card","Access fob card"]]]),
 ])]))
# ---------- 6 Identity
D.append(dept('Identity & travel documents',
 'Papers and cards a state or employer issues to prove who the holder is or what they may do; a certificate of a life event → Certificates & legal papers.',
 'Who issues it and what does it allow: a state (travel, residence, driving, identity) or an employer or event organiser (entry)?',[
 shelf('State identity & travel papers','Documents issued by a state to show identity, nationality, right to travel, reside or drive.',
  'kinds by what the state authorises: international travel, entry and residence, identity at home, driving',[
  kind('Passport','Booklet issued by a state to identify its holder for international travel.',[["Type",["Ordinary","Diplomatic","Nansen","Historical"]]],see=[["A4","Passport cover","cover for a passport"]]),
  kind('Visa & residence permit','Permission from a state to enter, stay in or leave it, as a passport sticker or stamp, an electronic record or a residence card.',
   [["Form",["Passport sticker","Passport stamp","Printed electronic visa","Residence permit card"]],["Purpose",["Transit","Short-stay visitor","Long-stay","Official","Immigrant"]]],s=WP+'Travel_visa'),
  kind('National identity card','Photo card issued by a national authority to prove who the holder is, compulsory in some countries and voluntary in others.',
   [["Obligation",["Compulsory","Voluntary"]],["Technology",["Plastic photocard","Electronic biometric card"]],["Related state paper",["Social security card","Citizenship certificate"]]],s='https://en.wikipedia.org/wiki/List_of_national_identity_card_policies_by_country',see=[["A4","Cardholder","holder for the card"]]),
  kind('Driving licence','Permit, now usually a plastic card, showing that the holder may drive certain classes of vehicle.',
   [["Form",["Written permit or booklet","Plastic card"]],["Class",["Car","Large truck","Professional chauffeur"]]],s=WP+'Driver%27s_license'),
 ]),
 shelf('Work & event badges','Badges and passes naming the holder, issued by an employer or event organiser to show who they are or where they may go.',None,[
  kind('Work identity card','Badge or card bearing the holder\'s name or photograph, issued by an employer to show who the holder is.',[["Type",["Employee ID badge","Crew member certificate"]]]),
  kind('Access badge','Badge or pass bearing the holder\'s name or photograph, carried to show what site or event the holder may enter.',[["Type",["Event pass","Backstage laminate","Press pass"]]]),
 ])]))
# ---------- 7 Certificates
D.append(dept('Certificates & legal papers',
 'Household papers recording a life event, a qualification or ownership; decorative certificates made as pictures → Art.',
 'What does the paper record: a life event or qualification, or property and household affairs?',[
 shelf('Life-event & school certificates','Certificates issued by a registry, church, health authority or school to record an event or an achievement.',
  'kinds by issuer: civil registry, religious body, health authority, school, awarding body',[
  kind('Civil registration certificate','Certificate issued by a civil registry recording a birth, marriage, partnership, death or divorce.',[["Event",["Birth","Marriage","Civil partnership","Death","Divorce decree"]]]),
  kind('Religious rite certificate','Certificate recording a religious rite such as a baptism, confirmation or marriage contract; one made as a picture is in Art.',[["Rite",["Baptism or christening (incl. Taufschein)","Confirmation","First communion","Bar or bat mitzvah","Ketubah (marriage contract)"]]]),
  kind('Vaccination certificate','Paper record or card certifying vaccinations received.',[["Document",["Yellow card (International Certificate of Vaccination)"]]]),
  kind('Diploma','Document issued by a school or university to certify a degree or completed course.',[["Level",["Primary school certificate (Certificat d'études primaires)","University degree"]]]),
  kind('Certificate of achievement','Document certifying an achievement, a qualification or membership of a body.',[["Awarded for",["Merit at school (reward of merit card)","Qualification","Membership"]]]),
 ]),
 shelf('Property & household papers','Papers that prove title to property or record the affairs of a household.',None,[
  kind('Deed','Document that conveys or proves title to property; the land itself is in Property & Structures.',[["Document",["Land deed","House deed","Indenture"]]]),
  kind('Household & legal papers','Papers kept at home for the household: wills, tax records, house plans and school reports.',[["Paper",["Will","Tax paper","House plans","School report"]]]),
 ])]))
# ---------- carry old dept-level fields
omap={d['n']:d for d in old['depts']}
for d in D:
    o=omap[d['n']]
    for f in ('mode','note','b'):
        if f in o: d[f]=o[f]
cat={'c':'F5','rev':True,'lead':old['lead'],'b':old.get('b',[]),
 'ax':'What is the paper or card: a signed or written record, a picture on card, paper or film, a printed item kept after use, a claim to money, a card that pays or opens, an identity paper or a certificate?',
 'key':['1. Is it valued for being signed or written by a person (autograph, letter, diary, manuscript)? → Letters, autographs & manuscripts',
 '2. Is it a picture carried on a card, plate, slide or film, or an album that holds pictures? → Photographs & postcards',
 '3. Is it printed for a short use (ticket, menu, label, handbill, badge) and kept afterwards? → Paper ephemera',
 '4. Does it state a claim to money (share, bond, cheque, postal order)? → Shares, bonds & money papers',
 '5. Is it a card that pays, rides, calls or opens a lock? → Payment, transit & phone cards',
 '6. Is it issued to prove who the holder is or what they may do (passport, licence, badge)? → Identity & travel documents',
 '7. Does it record a birth, marriage, qualification or ownership of property? → Certificates & legal papers',
 '<i>Precedence: a signed photograph or signed cheque is an autograph (step 1) when valued for the signer; a written-on postcard is a postcard (step 2) unless valued for its writer; a banknote or token → Coins, Stamps, Medals & Trading Cards.</i>'],
 'depts':D}
# bookkeeping: before/after
newnames={k['n'] for d in D for s in d['s'] for k in s['k']}
rn={'Slide':'35 mm slide','Identity document':'National identity card'}
removed=[n for n in K if n not in newnames and n not in rn]
print('removed kinds:',removed)
os.makedirs(R+'work/STR_F5',exist_ok=True)
json.dump(cat,open(R+'work/STR_F5/F5.tmp','w'),ensure_ascii=False,indent=1)
os.replace(R+'work/STR_F5/F5.tmp',R+'out/F5.json')
json.dump(rn,open(R+'out/F5_renames.json','w'),ensure_ascii=False,indent=1)
