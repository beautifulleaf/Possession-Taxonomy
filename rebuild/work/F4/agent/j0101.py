import sys; sys.path.insert(0,'/home/user/Possession-Taxonomy/rebuild/work/F4/agent')
from w import save
W='https://en.wikipedia.org/wiki/'
kinds=[
{"n":"Mezuzah case","a":"doorpost scroll case","d":"Case made to hold a doorpost scroll and be fixed to a doorpost.","t":["silver","wood","ceramic","pewter","stone"],"s":"https://www.judaica.com/","m":[]},
{"n":"Mezuzah scroll","a":"doorpost scroll · klaf","d":"Handwritten parchment strip of Deuteronomy verses, in Ktav Stam script, put in a case and fixed to a doorpost.","t":["Beit Yosef script","Ari script","by size to fit the case"],"s":W+"Mezuzah","m":[]},
{"n":"Tefillin","a":"phylacteries","d":"Pair of small boxes holding handwritten sacred passages, with straps, strapped to the arm and head in prayer.",
 "t":["peshutim (simple)","dakkot (thin, single hide)","gassot (thick, single hide)","Beis Yosef script","Arizal script","Velish script"],"s":W+"Tefillin","m":[]},
{"n":"Tallit","a":"prayer shawl","d":"Fringed prayer shawl with tzitzit on its four corners; tallit katan is the small everyday garment.",
 "t":["Ashkenazi white with black stripes","Sephardi all white","tallit katan","wool","silk","tallit bag"],"s":W+"Tallit",
 "x":[{"n":"Tallit gadol","a":"large prayer shawl","d":"Large shawl worn over outer clothes for morning prayer, with an atarah neckband.","mk":"","y":"","s":W+"Tallit","dt":"wool or silk · stripes black, blue or white · atarah"},
 {"n":"Tallit katan","a":"small tallit","d":"Poncho-like fringed garment worn under or over clothing.","mk":"","y":"","s":W+"Tallit","dt":"wool or cotton"}],"m":[]},
{"n":"Ketubah","a":"Jewish marriage contract","d":"Marriage contract, often illuminated or paper-cut, framed and displayed at home.",
 "t":["illuminated","papercut","printed","framed"],"s":W+"Ketubah",
 "x":[{"n":"Italian illuminated ketubah","a":"","d":"Decorated marriage contract such as those from Livorno (1698) and Venice (1750).","mk":"","y":"17th-18th century","s":W+"Ketubah","v":[{"n":"Livorno ketubah","mk":"","y":"1698","d":"Cited illustration"},{"n":"Venice ketubah","mk":"","y":"1750","d":"Cited illustration"}],"dt":"parchment · painted borders"},
 {"n":"Yemenite ketubah","a":"","d":"Marriage contract from Yemen; an example of 1794 is in the Bezalel Academy collection.","mk":"","y":"1794","s":W+"Ketubah"}],"m":[]},
{"n":"Shofar","a":"ritual horn","d":"Horn made to be blown in a rite.","t":["ram's horn (Ashkenazi, Sephardi)","kudu horn (Yemenite)","Moroccan flat shofar","with carved mouthpiece"],"s":W+"Shofar",
 "x":[{"n":"Ram's horn shofar","a":"","d":"Curved horn of a domestic ram, the preferred shofar; Sefardi ones often have a small carved mouthpiece.","mk":"","y":"","s":W+"Shofar","dt":"natural or polished"},
 {"n":"Yemenite shofar","a":"kudu shofar","d":"Long spiralling greater-kudu horn with a deep reverberating sound.","mk":"","y":"","s":W+"Shofar","dt":"greater kudu horn"}],"m":[["Yemenite shofar",""]]},
{"n":"Torah scroll","a":"Sefer Torah · handwritten Torah scroll","d":"Handwritten scroll of the Five Books on parchment, read in the rite. A printed Torah or Bible is in Media & Publications.","t":["42 lines per column","Yemenite 51 lines","mantle","Sephardi tik case"],"s":"https://ebay.com/str/jerusalemssifreitorah","m":[]},
{"n":"Torah finials","a":"rimonim · Torah finial","d":"Ornament fitted to the top of the rollers of a Torah scroll, usually silver and hung with bells.","t":["silver","wood","with bells"],"s":W+"Torah_finials",
 "x":[{"n":"Rimonim","a":"pomegranates","d":"Hollow silver finials named for the pomegranate with its 613 seeds.","mk":"","y":"","s":W+"Torah_finials","dt":"silver · bells · hollow base"}],
 "m":[["Bier Judaica 925 Sterling Silver Hammered Torah Finials","Bier Judaica"]]},
{"n":"Torah pointer","a":"yad","d":"Slim rod ending in a pointing hand, held to follow the text when reading a scroll aloud.","t":["silver","wood","twisted Mountain Jews form"],"s":W+"Yad",
 "x":[{"n":"Yad","a":"etzba","d":"Rod with a small hand at the end, index finger extended; silver is common for the top.","mk":"","y":"","s":W+"Yad","dt":"silver pommel"}],"m":[]}
]
save('01_01',{"kinds":kinds,"brands":[],"traditions":[],"notes":"Shofar pre-existing Yemenite model kept in m. Not added: modern artist ketubot (no retrieved list of artists), Beit Yosef/Ari script differences beyond names. Eastern European silver tradition omitted (no retrieved page)."})
