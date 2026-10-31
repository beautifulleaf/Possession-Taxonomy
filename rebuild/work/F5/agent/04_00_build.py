import json, os
os.chdir('/home/user/Possession-Taxonomy/rebuild')
old = json.load(open('work/F5/agent/04_00.old.json'))
LIST = 'https://en.wikipedia.org/wiki/List_of_public_transport_smart_cards'
C = {}
def put(country, names):
    for n in names.split(';'):
        n = n.strip()
        if n: C[n] = country
put('United Kingdom', "Oyster card;Iff card;Walrus;get me there;Swift (Birmingham);MCard;sQuid;iLink;Pop card")
put('Peru', "Tarjeta Lima Metro;Tarjeta Electrónica Inteligente")
put('Puerto Rico', "p'ATI")
put('Spain', "Targeta mobilis;MUGI;Barik;Tarjeta Transporte Público (Madrid)")
put('Brazil', "TRI;Transfácil;RioCard;Vem;Passe Rápido;Bilhete Único;Cartão Ideal")
put('Uzbekistan', "ATTO")
put('Australia', "Metrocard (Adelaide);Greencard;myki;MyWay+;Opal;go card;SmartRider")
put('France', "Carte Péribus;BADGEO / U'GO;Citizy;Pastel card;Multipass;Modalis;Korrigo;Libertan;Técély card;Simplicité;Carte TXIK TXAK;Pass Pass;La Carte TBM;Navigo card;Twisto")
put('United Arab Emirates', "Masaar Card;Hafilat Card;Sayer Card;E-Saqr Card;Nol Card")
put('Turkey', "Antkart;Yaman Kart;İzmirim Kart;İstanbulkart;Ankarakart;Belkart;Kentkart (Adana);Türkiye Kart")
put('Norway', "t:kort;Kolumbuskort;Skysskortet;Tromskort;Reisekort")
put('Croatia', "Rijeka City Card;Butra;BusCARD;ZET Card")
put('Canada', "Umo;Arc card;EasyGO;OnYourWay;Ride CK Smart Card;Compass Card (Vancouver);peggo;Opus card;PRESTO")
put('Hungary', "RIGO")
put('China', "Yikatong;China T-Union;Jinlingtong;Jiaotong Yikatong;Shenzhen Tong;Suzhou Tong;Lingnan Tong")
put('India', "Namma Metro Smart Card;Chennai Metro Smart Card;Nebula Metro Smart Card")
put('Germany', "fahrCard;DingCard;Kolibricard (Schwäbisch Hall);Kolibricard (Hohenlohe);smilecard;+k@rte")
put('Bahrain', "Go Card (Bahrain)")
put('Azerbaijan', "BakıKART")
put('Thailand', "Be1st BTS Card;Bangkok Metro Smart card;BTS Smart pass;Rabbit Card;DinoCard;Mangmoom Card")
put('Chile', "Tarjeta Biotren;Tarjeta Metroval;Tarjeta bip!")
put('Italy', "BIP Card;Carta Venezia;Carta Mobile;Metrebus Card;Unico Campania SmartCard")
put('United States', "amp;Navigator Card;COMET Card;COTA Smartcard;Go CT Card;GoPass Tap;METRO Q Card;MyKey;STAR Card;Breeze Card;CharlieCard;CharmCard;Go901;Go-To card;OMNY;SmartLink;Compass Card (San Diego);SEPTA Key;Hop Fastpass;Copper Card;SmarTrip;QuickTicket;Clipper;EASY Card;HOLO card;ORCA card;TAP card;Ventra")
put('Malaysia', "Manjalink;Komuterlink;My Rapid Touch 'n Go;Touch 'n Go;Pas Mutiara")
put('Cyprus', "Motion Card")
put('Bangladesh', "Rapid Pass")
put('Ireland', "Dublin Bus Smartcard;Luas Smart Card;Leap Card")
put('Poland', "Gdansk City Card;Cracow City Card;Opolka;URBANcard;Metrokarta;Warsaw City Card;Lubika")
put('Argentina', "Urbana (Bahía Blanca);Movi;SUBE")
put('South Korea', "CashBee;hi-pass plus;Upass;T-money;eB Card")
put('Taiwan', "EasyCard;iPASS;HappyCash;icash 2.0")
put('Paraguay', "Jaha")
put('Mexico', "Tarjeta FERIA;Tarjeta Va y Ven;Tarjeta SITEUR;Tarjeta de Movilidad Integrada")
put('Philippines', "BeepRides;Beep;TRIPKO")
put('South Africa', "Gautrain Gold;Tap-I-Fare;Muvo;MyConnect")
put('Finland', "HSL Card")
put('Israel', "Rav-Kav")
put('Japan', "Kitaca;ICOCA;PASMO;Suica")
put('Slovenia', "Urbana (Ljubljana)")
put('Lithuania', "Žiogas;Vilniečio kortelė (JUDU)")
put('Syria', "Aleppo City Card")
put('Serbia', "BusPlus")
put('Pakistan', "Metrobus Cards")
put('Jordan', "eKartak")
put('Kuwait', "Bus Pass (Kuwait)")
put('Ukraine', "Kyiv Tsyfrovyi;Leocard")
put('Austria', "Bestpreisticket")
put('Saudi Arabia', "Yamam;Urban Card")
put('Colombia', "Tarjeta MIO;Tarjeta Cívica;Tarjeta TransCaribe;Tarjeta Transmetro;Tarjeta Tullave")
put('Bolivia', "Tarjeta General")
put('Belarus', "Minsktrans card")
put('Qatar', "Karwa SmartCard")
put('Singapore', "CEPAS (NETS Prepaid);CEPAS (SimplyGo EZ-Link)")
put('Hong Kong', "Octopus")
put('Portugal', "Lisboa VIVA;Andante;Navegante")
put('Indonesia', "Jak Lingko")
put('Czech Republic', "Lítačka;In Karta")
put('Latvia', "E-talons")
put('Senegal', "Sama TER")
put('Sweden', "SL Access;Jojo-kortet;Västtrafikkortet")
put('Russia', "Podorozhnik;Volna;Troika")
put('Bulgaria', "Subway Card (Sofia);Public Transport Card (Sofia)")
put('Faroe Islands', "Ferðakort")
put('Iceland', "Klapp")
put('Iran', "Tarashe Tehran")
put('Georgia', "Metromoney")
put('Nigeria', "Cowry")
put('Morocco', "Irtiyah")
put('Netherlands', "OV-chipkaart")
put('Slovakia', "Slovenský dopravný pas")
put('Macau', "Macau Pass")
put('Greece', "ATH.ENA Card")
put('Benin', "Kinvi Card")
put('Luxembourg', "M-kaart;e-go")
put('Estonia', "Ühiskaart")
put('Belgium', "MoBIB")
put('Greenland', "Plastkorti")
put('Denmark', "Rejsekort")
put('Rwanda', "Tap&Go")
put('Kazakhstan', "Tolem;Tulpar (Taraz)")
put('Kyrgyzstan', "Tulpar (Bishkek)")
put('Turkmenistan', "Ýol karty")
# issuers for cards with blank issuer in old data, from the list page
FILL = {"Beep": "AF Payments, Inc.", "Clipper": "Metropolitan Transportation Commission", "EASY Card": "Miami-Dade Transit",
        "Lingnan Tong": "Yang Cheng Tong", "MoBIB": "SNCB-NMBS, TEC, De Lijn, STIB-MIVB", "Muvo": "eThekwini Transport Authority",
        "MyConnect": "MyCiti", "Nol Card": "Roads & Transport Authority", "Opus card": "Société de transport de Montréal",
        "PRESTO": "Metrolinx", "Pas Mutiara": "Rapid Penang", "Plastkorti": "Nuup Bussii A/S", "Pop card": "Nexus (Tyne and Wear)",
        "Reisekort": "Ruter", "Rejsekort": "Rejsekort & Rejseplan A/S", "Suica": "JR East", "TAP card": "LA Metro",
        "TRIPKO": "Journeytech, Inc.", "Tap&Go": "AC Group", "Tarjeta Tullave": "TransMilenio", "Troika": "Moscow Metro",
        "Ventra": "Chicago Transit Authority", "icash 2.0": "icash Co., Ltd.", "Ýol karty": "Ministry of Automobile Transport of Turkmenistan",
        "HOLO card": "TheBus (Honolulu)", "ORCA card": "Sound Transit"}
RENAME = {"Octopus Cards Limited": "Octopus Cards", "Transport for London": "Transport for London", "T-money": "Tmoney",
          "SimplyGo Pte Ltd": "SimplyGo", "WMATA": "WMATA", "Metropolitan Transportation Authority": "Metropolitan Transportation Authority",
          "Transport for NSW": "Transport for NSW", "Île-de-France Mobilités": "Île-de-France Mobilités", "Trans Link Systems": "Trans Link Systems",
          "National Transport Authority": "National Transport Authority", "Public Transport Victoria": "Transport Victoria"}
ICON_ISSUERS = {"Octopus Cards", "Transport for London", "JR East", "SimplyGo", "Tmoney", "Metropolitan Transportation Commission", "WMATA",
                "Metropolitan Transportation Authority", "Transport for NSW", "Île-de-France Mobilités", "Trans Link Systems", "Metrolinx",
                "National Transport Authority", "Transport Victoria"}
ICON_SRC = {"Octopus Cards": "https://en.wikipedia.org/wiki/Octopus_card", "Transport for London": "https://en.wikipedia.org/wiki/Oyster_card",
            "JR East": "https://en.wikipedia.org/wiki/Suica", "SimplyGo": "https://en.wikipedia.org/wiki/EZ-Link", "Tmoney": "https://en.wikipedia.org/wiki/T-money",
            "Metropolitan Transportation Commission": "https://en.wikipedia.org/wiki/Clipper_card", "WMATA": "https://en.wikipedia.org/wiki/SmarTrip",
            "Metropolitan Transportation Authority": "https://en.wikipedia.org/wiki/MetroCard", "Transport for NSW": "https://en.wikipedia.org/wiki/Opal_card",
            "Île-de-France Mobilités": "https://en.wikipedia.org/wiki/Navigo_pass", "Trans Link Systems": "https://en.wikipedia.org/wiki/OV-chipkaart",
            "Metrolinx": "https://en.wikipedia.org/wiki/Presto_card", "National Transport Authority": "https://en.wikipedia.org/wiki/Leap_Card",
            "Transport Victoria": "https://en.wikipedia.org/wiki/Myki"}
ICON_D = {"Octopus Cards": ("Hong Kong", "Hong Kong operator of the Octopus card, a subsidiary of Octopus Holdings."),
          "Transport for London": ("United Kingdom", "London's transport authority, which manages the Oyster card."),
          "JR East": ("Japan", "East Japan Railway Company, issuer of the Suica card."),
          "SimplyGo": ("Singapore", "Land Transport Authority subsidiary formed from TransitLink and EZ-Link; issues EZ-Link cards."),
          "Tmoney": ("South Korea", "Seoul-based issuer of T-money cards, founded 2003 as Korea Smart Card Co."),
          "Metropolitan Transportation Commission": ("United States", "San Francisco Bay Area agency that manages the Clipper card."),
          "WMATA": ("United States", "Washington Metropolitan Area Transit Authority, issuer of SmarTrip."),
          "Metropolitan Transportation Authority": ("United States", "New York transit authority, issuer of MetroCard and OMNY."),
          "Transport for NSW": ("Australia", "New South Wales transport agency operating the Opal card."),
          "Île-de-France Mobilités": ("France", "Paris-region transport authority managing the Navigo card."),
          "Trans Link Systems": ("Netherlands", "Joint venture of Dutch transport operators that issues the OV-chipkaart."),
          "Metrolinx": ("Canada", "Ontario transport agency managing the Presto card."),
          "National Transport Authority": ("Ireland", "Irish transport authority issuing the Leap Card under the TFI brand."),
          "Transport Victoria": ("Australia", "Victorian transport body managing the myki card.")}
ICON_CARDS = {"Octopus", "Oyster card", "Suica", "CEPAS (SimplyGo EZ-Link)", "T-money", "Clipper", "SmarTrip", "Opal", "Navigo card", "OV-chipkaart", "PRESTO", "Leap Card", "myki"}
reg = {}
for card, iss in old[0]['m']:
    iss = iss.replace('issued by ', '').strip() or FILL.get(card, '')
    name = RENAME.get(iss, iss) or card
    b = reg.setdefault(name, {"n": name, "c": C.get(card, ''), "f": "", "seg": "Institution & issuer", "kf": "transit card",
                             "d": "", "lines": [], "eras": [], "sig": [], "sc": [], "rel": [], "s": LIST})
    if card not in b['lines']: b['lines'].append(card)
    if b['c'] != C.get(card, b['c']) and C.get(card): b['c'] = b['c'] or C[card]
# NCMC stub
reg['NPCI'] = {"n": "NPCI", "c": "India", "f": "", "seg": "Institution & issuer", "kf": "transit card", "d": "Issuer of India's nationwide National Common Mobility Card (2019).",
               "lines": ["National Common Mobility Card"], "eras": [], "sig": [], "sc": [], "rel": [], "s": LIST}
# MetroCard issuer (OMNY already there)
for n in ICON_ISSUERS:
    b = reg.setdefault(n, {"n": n, "c": "", "f": "", "seg": "Institution & issuer", "kf": "transit card", "d": "", "lines": [], "eras": [], "sig": [], "sc": [], "rel": [], "s": LIST})
    b['c'], b['d'] = ICON_D[n]; b['s'] = ICON_SRC[n]
reg['Metropolitan Transportation Authority']['lines'].insert(0, 'MetroCard')
for b in reg.values():
    if not b['d']:
        b['d'] = f"Transit-card issuer ({', '.join(b['lines'])})" + (f", {b['c']}." if b['c'] else ".")
missing = [b['n'] for b in reg.values() if not b['c']]
print('stubs', len(reg), 'no country:', missing)
json.dump(reg, open('work/F5/agent/04_00.reg.json', 'w'), ensure_ascii=False, indent=0)
