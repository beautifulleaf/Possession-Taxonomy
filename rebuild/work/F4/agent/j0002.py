import sys; sys.path.insert(0,'/home/user/Possession-Taxonomy/rebuild/work/F4/agent')
from w import save
W='https://en.wikipedia.org/wiki/'
kinds=[
{"n":"Chalice","a":"communion cup","d":"Stemmed cup, normally of metal, used for the wine in the Christian Eucharist.","t":["gilded bowl","enamelled","travelling set"],"s":W+"Chalice",
 "x":[{"n":"Western chalice","a":"","d":"Narrow cup on a stem with a knop (node) for easier handling.","mk":"","y":"","s":W+"Chalice","dt":"silver or gilt · knop · cup narrow"},
 {"n":"Eastern chalice","a":"","d":"Larger rounded cup, since communicants receive bread soaked in the wine.","mk":"","y":"","s":W+"Chalice","dt":"larger round bowl"}],"m":[]},
{"n":"Host vessel","a":"ciborium · pyx · host box","d":"Lidded cup, bowl or box made to hold consecrated or unconsecrated hosts.","t":["ciborium (covered cup)","pyx (few hosts, for the sick)","paten"],"s":"https://www.eden.co.uk/church-supplies/communion-ware/ciboria/",
 "x":[{"n":"Ciborium","a":"","d":"Covered metal cup, rounder than a chalice, for consecrated hosts; stored in the tabernacle.","mk":"","y":"","s":W+"Ciborium_(container)","dt":"silver or gilt · cross on lid"},
 {"n":"Pyx","a":"","d":"Small round container for a few hosts, used to take Communion to the sick.","mk":"","y":"","s":W+"Ciborium_(container)","dt":"small · hinged or lidded"}],"m":[]},
{"n":"Monstrance","a":"ostensorium · ostensory","d":"Display vessel with a window or frame, made to show a consecrated host or relic.","t":["sunburst","tower","relic monstrance"],"s":"https://www.heck-kirchenbedarf.de/kirchenbedarf",
 "x":[{"n":"Sunburst monstrance","a":"radiant monstrance","d":"Central host window surrounded by rays on a stem and foot; the dominant modern form.","mk":"","y":"15th century onward","s":W+"Ostensory","dt":"gilt metal · glass window"},
 {"n":"Tower monstrance","a":"","d":"Architectural tower form, the most common design before the Council of Trent.","mk":"","y":"pre-Trent","s":W+"Ostensory","v":[{"n":"Belem monstrance","mk":"","y":"1506","d":"Made by Gil Vicente"},{"n":"Diamond Monstrance","mk":"","y":"1696-99","d":"Vienna/Prague"}],"dt":"gilt metal"}],"m":[]},
{"n":"Altar candlestick","a":"","d":"Candle holder made to stand on or by an altar in a rite. An open candle holder for the home is in Decor.","t":["floor-standing","table altar","brass","with candle follower"],"s":"https://www.holyart.co.uk/liturgical-accessories/church-furnishings/altar-crosses-and-candle-holders/baroque-gilded-brass-altar-candlestick-55-cm-high",
 "x":[{"n":"Altar candlestick set","a":"","d":"Pair or row of candlesticks flanking an altar cross; at least two for Mass, four or six on Sundays.","mk":"","y":"","s":W+"Altar_candle","dt":"brass · two, four or six"}],"m":[]},
{"n":"Paschal candle","a":"Easter candle","d":"Large candle blessed and lit at Easter, marked with cross, alpha and omega, year and five grains.","t":["beeswax","oil-filled shell","with stand"],"s":W+"Paschal_candle","m":[]},
{"n":"Sanctuary lamp & lampada","a":"eternal light · everlasting light · lampada","d":"Lamp kept burning before a sanctuary, altar or icon; oil, candle or electric.","t":["hanging","wall-mounted","standing","Orthodox home lampada","LED"],"s":W+"Sanctuary_lamp","m":[]},
{"n":"Thurible & hand censer","a":"thurible · censer · kadilo","d":"Incense burner hung on chains to be swung, or a handled hand censer.","t":["chained thurible","Orthodox kadilo with bells","hand censer"],"s":"https://www.eden.co.uk/church-supplies/incense-boats-burners/thurible-h-23-cm/",
 "x":[{"n":"Orthodox kadilo","a":"","d":"Silver, brass or gilt censer with three outer chains for the Trinity and a fourth inner chain; Greek and some Russian ones carry twelve bells.","mk":"","y":"","s":W+"Thurible","dt":"pierced lid · bells"},
 {"n":"Hand censer","a":"","d":"Censer with a handle, used by readers or laymen and in Orthodox homes.","mk":"","y":"","s":W+"Thurible","dt":"handle"}],"m":[]}
]
save('00_02',{"kinds":kinds,"brands":[],"traditions":[],"notes":"Old 'Ritual cup' (chalice + kiddush cup) split: Chalice stays; kiddush cup left to the Jewish shelf. No Gothic chalice archetype: no retrieved page describes it. Parish goods kept kind-level."})
