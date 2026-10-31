import sys;sys.path.insert(0,'work/J4/agent')
from lib import *
TG=W+"Table_grape"; IFG=W+"International_Fruit_Genetics"; SW="https://www.freshplaza.com/north-america/article/9328073/sun-world-looks-back-on-45-years-in-the-business/"
GR=[x("Thompson Seedless","","",W+"Sultana_(grape)","Pale green seedless grape probably from Asia Minor, the high-yielding shipper also known as Sultanina or sultana.",
   [v("Thompson Seedless","","","Old-data name"),v("Superior Seedless (Sugraone)","Sun World","","Sun World licensed seedless")],a="Sultanina · Sultana"),
 x("Flame Seedless","","1973",W+"Flame_Seedless","Red seedless grape hybrid of Thompson Seedless, Cardinal and other vinifera, brought to the US by John Kovacevich in 1973."),
 x("Crimson Seedless","","",TG,"Late-season red seedless table grape."),
 x("Red Globe","","",TG,"Large seeded red table grape."),
 x("Italia","","",TG,"White-green seeded table grape."),
 x("Concord","","",TG,"Blue-black American Vitis labrusca grape, eaten fresh and made into purple juice.",[v("Thomcord (Grape Jammers)","","","Concord x Thompson Seedless cross by USDA researchers, old-data entry")]),
 x("Kyoho","","",TG,"Large blue-black vinifera x labrusca hybrid, Japan's most-produced table grape."),
 x("Pione","","",TG,"Blue-black Japanese bred hybrid, third in Japanese production."),
 x("Shine Muscat","","",TG,"White-green Japanese muscat table grape."),
 x("Ruby Roman","","",TG,"Japanese premium red grape; one bunch sold for about one million yen in 2015."),
 x("Cotton Candy","International Fruit Genetics","2010",IFG,"Patented cotton-candy-flavoured bred hybrid grape from International Fruit Genetics, licensed to growers.",
   [v("Cotton Candy (IFG Seven)","International Fruit Genetics","2010","IFG code in old data"),v("Sweet Celebration (IFG 68-175)","International Fruit Genetics","","IFG variety"),
    v("Sweet Sunshine (IFG Two)","International Fruit Genetics","","IFG variety"),v("Sweet Surrender (IFG One)","International Fruit Genetics","","IFG variety"),
    v("Candy Hearts (IFG Nineteen)","International Fruit Genetics","","IFG variety")]),
 x("Autumncrisp","Sun World","",SW,"Sun World's brand for the Sugrathirtyfive seedless green grape.",
   [v("Autumncrisp (Sugrathirtyfive)","Sun World","","Old-data code"),v("Midnight Beauty (Sugrathirteen)","Sun World","","Sun World brand"),v("Sable Seedless (Sugrasixteen)","Sun World","","Sun World brand")])]
KW=W+"Kiwifruit"
KI=[x("Hayward","","c.1924",KW,"The standard fuzzy green kiwifruit, developed by Hayward Wright in Avondale, Auckland.",[v("Hayward","","","Old-data name")]),
 x("Hort16A","Zespri","1991",W+"Gold_kiwifruit","Yellow-fleshed kiwifruit from DSIR, sold as Zespri Gold; almost entirely removed from New Zealand by 2018 because of PSA.",
   [v("Hort16A (Zespri Gold)","Zespri","","Old-data name")],a="Zespri Gold"),
 x("Zespri SunGold","Zespri","2002",W+"Gold_kiwifruit","Gold kiwifruit Zesy002 (formerly Gold3), more PSA-resistant than Hort16A and now two-thirds of NZ kiwifruit volume.",
   [v("SunGold [Zespri International]","Zespri","2012","Old-data entry; marketed as SunGold by 2012")],a="Gold3 · Zesy002"),
 x("Zespri RubyRed","Zespri","2019",W+"Kiwifruit_industry_in_New_Zealand","Red-centred Zes008 kiwifruit announced in December 2019.",[v("Zespri RubyRed","Zespri","2019","Zes008")],a="Zes008"),
 x("Hongyang","","",KW,"China's first commercially viable red-fleshed cultivar, selected in Sichuan; China's most-grown kiwifruit by 2020."),
 x("Jintao","","",KW,"Gold cultivar from the Wuhan Botanical Garden; exclusive breeding rights sold to Jingold in 2001.")]
KB=[x("Ananasnaya","","",W+"Actinidia_arguta","Most commonly grown kiwiberry in the US and Chile, also sold as Jumbo Verde.",[],a="Jumbo Verde"),
 x("Issai","","",W+"Actinidia_arguta","Self-fertile Japanese hybrid kiwiberry commonly sold.",[v("Super Issai","","","Offspring of Issai")])]
brands=[B("Zespri","New Zealand","Specialist","kiwifruit marketer","New Zealand grower-owned kiwifruit marketer, renamed from the Kiwifruit Marketing Board in 1997.",W+"Kiwifruit_industry_in_New_Zealand",f="1997",sig=["Zespri SunGold","Hort16A","Zespri RubyRed"]),
 B("International Fruit Genetics","United States","Specialist","grape breeder","Bakersfield, California fruit breeder founded 2001, now part of Bloom Fresh International.",IFG,f="2001",sig=["Cotton Candy"]),
 B("Sun World","United States","Specialist","grape and stone fruit breeder","California fruit company founded 1976 that now breeds and licenses table grapes and stone fruit.",SW,f="1976",sig=["Autumncrisp"])]
gm=["Adora Seedless (Sugrathirtyfour)","Autumn King","Autumn Royal","Bangalore Blue Grapes GI","Cardinal","Champagne","Chasselas","Chasselas de Moissac AOP","Emperor","Jack's Salute","Majestic","Muscat de Hambourg","Muscat du Ventoux AOP","Nashik Grapes GI","Niabel","Queen","Ribier","Ruby","Sweet Globe (IFG Ten)","Candy Snaps (IFG Twenty-One)","Sweet Scarlet (Muscato Amore)","Uva da tavola di Canicattì PGI","Uva da tavola di Mazzarrone PGI","Uva di Puglia PGI","Uva de mesa embolsada ‘Vinalopó’ PDO","Vlaams-Brabantse tafeldruif PDO","Westlandse druif PGI","つるたスチューベン GI","Sugardrop (ARRA THIRTY)","Mystic Dream (ARRA THIRTYTWO)","Passion Fire (ARRA TWENTYNINE)"]
km=["Blake","Donghong","Jinyan","Kiwi Latina PGI","Kiwi de Corse PGI","Kiwi de l'Adour PGI","Kiwi Mar y Sierras del Sudeste de Buenos Aires IG","Ακτινίδιο Σπερχειού PDO","보성키위","Soreli","Saanichton 12","EnzaRed"]
kinds=[K("Table grape","Fresh table grape, sold to eat, organised by cultivar and breeder lines with their codes.","https://plu.pro/commodity/grapes",GR,gm,["seedless","seeded","white","red","black"],a="Grape"),
K("Kiwifruit","Fresh kiwifruit, green, gold or red fleshed.","https://plu.pro/commodity/kiwifruit",KI,km,["green","gold","red"]),
K("Kiwiberry","Fresh smooth-skinned hardy kiwi (Actinidia arguta), eaten whole.",W+"Actinidia_arguta",KB,a="Hardy kiwi")]
notes="Table grape list cut from ~85 to archetypes with retrieved sources plus 31 flat models. IFG and Sun World codes are old-data only; Wikipedia IFG page does not list Sweet Globe or Candy Snaps. Muscat of Alexandria, Nagano Purple, Queen Nina not found. Nergi kiwiberry not found. Hayward origin year from Wikipedia 'around 1924'. Grapa/Arra and SNFL (Bloom Fresh) not given brand pages."
urls=[TG,W+"Sultana_(grape)",IFG,W+"Flame_Seedless",SW,KW,W+"Gold_kiwifruit",W+"Actinidia_arguta",W+"Kiwifruit_industry_in_New_Zealand"]
write("00_07",kinds,brands,[],notes,urls)
