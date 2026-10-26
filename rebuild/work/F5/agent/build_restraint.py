import json, os
def K(n, a, d, s, t=None, m=None):
    k = {"n": n, "a": a, "d": d, "s": s}
    if t: k["t"] = t
    if m: k["m"] = m
    return k
def W(job, kinds, notes):
    p = f"work/F5/shelves/{job}.json"; os.makedirs(os.path.dirname(p), exist_ok=True)
    json.dump({"kinds": kinds, "brands": [], "traditions": [], "notes": notes}, open(p + ".tmp", "w"), ensure_ascii=False, indent=1)
    os.replace(p + ".tmp", p)
W("01_02", [
 K("Photo album", "", "Album holding photographic prints; archival (acid-free, PVC-free) materials mark a good one.", "https://www.ebay.com/itm/166933552010",
   t=["slip-in", "self-adhesive", "traditional mounting", "Victorian CDV album"],
   m=[["Hudson 2UP Photo Album", "Kolo"], ["Hudson 3UP Photo Album", "Kolo"], ["Noci Photo Album", "Kolo"]]),
 K("Scrapbook", "", "Album filled with kept papers of every kind; a blank scrapbook album is in Craft & Art Supplies.", "https://www.etsy.com/listing/1294641669/vintage-victorian-scrapbook-filled-with"),
 K("Film album", "negative binder · slide binder", "Binder or album of sleeves made to hold negatives and slides.", "https://www.universityproducts.com/photo-products/negative-storage",
   m=[["Infinity Archival Boxbinder", "University Products"], ["Perma/Dur Archival Binders", "University Products"]]),
 K("Home film reel", "", "Film shot by the owner or family on a reel.", "https://www.ebay.com/itm/266945294978",
   t=["8 mm", "Super 8", "9.5 mm", "16 mm"]),
 K("Home videotape", "", "Videotape recorded by the owner or family.", "https://www.etsy.com/market/home_recorded_vhs_tapes",
   t=["VHS", "VHS-C", "Video8/Hi8", "MiniDV", "Betamax"]),
], "Restraint only: kept the three Kolo album models and two University Products binders from the old data; album formats, film gauges and tape formats moved into types. Nothing dropped.")
W("04_02", [
 K("Gift card", "", "Plastic card holding a prepaid value redeemable for goods or services.", "https://www.ebay.com/b/Collectible-Credit-Charge-Cards/1462/bn_2311177"),
 K("Gift certificate", "gift voucher · gift token", "Paper voucher or gift token redeemable only with its issuer; circulating scrip is in Coins, Stamps, Medals & Trading Cards.", "https://www.ebay.de/itm/146581040044"),
 K("Membership card", "", "Card issued to show the holder's membership of a club or body.", "https://www.londonmuseum.org.uk/collections/v/object-513868/membership-card"),
 K("Loyalty card", "", "Card issued by a retailer to collect discounts or points.", "https://www.ebay.de/itm/317041310835",
   m=[["Dollar Rewards Club card", "issued by Duane Reade"]]),
 K("Key card", "", "Card that opens a lock and names no holder, such as a hotel key card.", "https://www.ebay.de/itm/306062461431",
   t=["hotel key card", "access fob card"]),
], "Restraint only: gift card and gift certificate kept separate (plastic vs paper); the single Duane Reade loyalty-card model kept; key-card types added. Nothing dropped.")
PR = "https://www.consilium.europa.eu/prado/en/prado-start-page.html"
W("05_00", [
 K("Passport", "", "Booklet issued by a state to identify its holder for international travel.", "https://www.consilium.europa.eu/prado/en/LUX-AP-02004/index.html",
   t=["ordinary passport", "diplomatic passport", "Nansen passport", "historical passport"]),
 K("National identity card", "Jumindeungrokjeung · Nafnskírteini · CURP card · Carteira Nacional de Identificação · My Number card · Personalausweis",
   "Card issued by a state to prove the holder's identity and citizenship or residence.", PR),
 K("Driving licence", "", "Document issued to permit its holder to drive.", "https://road-safety.transport.ec.europa.eu/road-safety-member-states/driving-licence-member-states/driving-licence-models_en?page=1"),
 K("Visa", "", "Label, stamp or sheet issued to permit entry to or stay in a country.", "https://www.consilium.europa.eu/PRADO/EN/SVN-CO-01003/index.html"),
 K("Residence permit", "Alien Resident Certificate", "Document issued to a non-citizen to prove the right to reside.", PR),
 K("Citizenship certificate", "naturalisation certificate", "Certificate issued by a state recording that the holder is, or has become, its citizen.", "https://uscis.gov/policy-manual/volume-12-part-k-chapter-4"),
 K("Social security card", "social insurance card", "Card issued by a state showing the holder's social security or social insurance number.", "https://www.ssa.gov/pubs/EN-05-10002.pdf"),
 K("Work identity card", "identity badge · employee ID badge", "Badge or card bearing the holder's name or photograph, issued by an employer to show who the holder is.", "https://flyingtigerantiques.com/rare-1930s-wwii-american-airlines-employee-photo-id-badge-looks-to-be-a-pilot.html",
   t=["employee ID badge", "crew member certificate"]),
 K("Access badge", "", "Badge or pass bearing the holder's name or photograph, carried to show what site or event the holder may enter.", "https://www.ebay.com/itm/115066674561",
   t=["event pass", "backstage laminate", "press pass"]),
], "Restraint only: Identity badge renamed Work identity card and Crew member certificate merged into it as a type; passport and access-badge types added; national ID names kept as aliases. Nothing dropped.")
W("06_00", [
 K("Civil registration certificate", "birth certificate · marriage certificate · death certificate · divorce papers",
   "Certificate issued by a civil registry recording a birth, marriage, partnership, death or divorce.", "https://ebth.com/items/13499867-german-language-birth-and-baptismal-certificates-mid-to-late-19th-century",
   t=["birth certificate", "marriage certificate", "civil partnership certificate", "death certificate", "divorce decree"]),
 K("Religious rite certificate", "christening certificate · Taufschein · first communion certificate",
   "Certificate recording a religious rite such as a baptism, confirmation or marriage contract; one made as a picture is in Art.", "https://www.ebay.com/itm/387635588992",
   t=["baptism or christening certificate (incl. Taufschein)", "confirmation certificate", "first communion certificate", "bar or bat mitzvah certificate", "ketubah (marriage contract)"]),
 K("Vaccination certificate", "International Certificate of Vaccination · yellow card", "Paper record or card certifying vaccinations received.", "https://www.ebay.com/itm/335251417745",
   t=["yellow card (International Certificate of Vaccination)"]),
 K("Diploma", "", "Document issued by a school or university to certify a degree or completed course.", "https://www.etsy.com/market/antique_diploma",
   t=["Certificat d'études primaires"]),
 K("Certificate of achievement", "training certificate · membership certificate", "Document certifying an achievement, a qualification or membership of a body.", "https://www.ebay.com/itm/226130385129",
   t=["reward of merit card"]),
 K("School report", "report card", "Report issued by a school on a pupil's progress.", "https://www.etsy.com/dk-en/listing/789556487/antique-report-card-circa-1885-vintage"),
], "Merged birth, marriage, death certificates and divorce papers into Civil registration certificate (types); baptism and confirmation certificates into Religious rite certificate, with the ketubah moved there as a marriage-contract type. Model-less entries (Taufschein, Certificat d'études primaires, Reward of merit card) became types. Nothing dropped.")
W("06_01", [
 K("Deed", "", "Document that conveys or proves title to property; the land itself is in Property & Structures.", "https://www.oldworldauctions.com/catalog/lot/145/832",
   t=["indenture"]),
 K("Will", "", "Document setting out how a person's estate is to be disposed of after death.", "https://www.ebay.com/itm/352962486660"),
 K("Tax paper", "tax return · assessment notice", "Paper tax return or assessment notice kept as a record.", "https://www.ebay.com/itm/127104649412"),
 K("House plans", "", "Drawn or printed plans of a dwelling kept as a record.", "https://www.ebay.com/itm/116957690887"),
], "Restraint only: Indenture moved from models to a type of Deed (older handwritten indentures may also sit under Manuscript document). Nothing dropped.")
