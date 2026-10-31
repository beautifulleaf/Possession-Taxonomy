import json,os,sys
sys.path.insert(0,'/home/user/Possession-Taxonomy/rebuild/work/GAP_B4')
src=open('/home/user/Possession-Taxonomy/rebuild/work/GAP_B4/build.py').read().split('# Paperweights')[0]
exec(src)
add('Candle holder',[
 E('Chamberstick','Short candlestick with a pan to catch dripping wax, used to carry a candle between rooms.',W+'Candlestick','Not stated'),
 E('Hanukkah menorah','Eight-branched candle holder with a ninth place for the candle that lights the others, called the Hanukiah.',W+'Candlestick','Judaism'),
 E('Temple menorah','Seven-branched candelabrum modelled on the one in the Temple in Jerusalem, a national symbol of Israel.',W+'Candlestick','Israel'),
 E('Dikirion and trikirion','Two- and three-branched candlesticks used by bishops of the Eastern churches to bless a congregation.',W+'Candlestick','Eastern Orthodox and Eastern Catholic'),
],"Follows Wikipedia's Candlestick article, read in full, and the maker pages cited. Covers 6 entries; the article names the Gloucester Candlestick (12th century, a museum piece) and gives no complete type list.")
add('Easter tree',[
 E('Ostereierbaum','Branch or tree hung with decorated Easter eggs, a centuries-old custom.',W+'Easter_tree','Germany, Austria and Switzerland'),
 E('Saalfeld Easter egg tree','Apple tree in Volker Kraft\'s garden in Saalfeld, decorated 1965 to 2015; over 10,000 eggs by 2012.',W+'Easter_tree','Germany (Thuringia)','','1965-2015'),
],"Follows Wikipedia's Easter tree article, read in full. Covers 2 entries; the Rostock zoo tree (2007) is a one-off record installation and is not entered.")
add('Wreath',[
 E('Advent wreath','Wreath with four candles and a white Christ candle; Johann Hinrich Wichern made the modern form in 1839 to count the days to Christmas.',W+'Wreath','Germany','Johann Hinrich Wichern','1839',role='origin'),
 E('Christmas door wreath','Wreath hung on doors or walls at Christmas, unlike Advent wreaths that stand on tables.',W+'Wreath','England and United States'),
],"Follows Wikipedia's Wreath article, read in full. Covers 2 Christmas forms of 14 wreath types named; harvest, funeral, laurel and festival wreaths belong to other uses.")
add('Artificial Christmas tree',[
 E('Moravian pyramid tree','Wooden candle-lit pyramid tree developed by the Moravian Church in Bethlehem, Pennsylvania, in 1747.',W+'Artificial_Christmas_tree','United States (Pennsylvania)','','1747'),
 E('Cardboard tabletop tree','Tabletop tree of cardboard, cited to Popular Mechanics, January 1937.',W+'Artificial_Christmas_tree','Not stated','','1937'),
 E('PVC tree','Most modern artificial trees; many are made in China\'s Pearl River Delta; realistic versions copy Douglas fir or Ponderosa pine.',W+'Artificial_Christmas_tree','China'),
 E('Holographic mylar tree','Artificial tree of holographic mylar, made in many colours.',W+'Artificial_Christmas_tree','Not stated'),
],"Follows Wikipedia's Artificial Christmas tree article, read in full. Covers 9 of about 13 types it names; pre-lit and upside-down are features, and the Sri Lankan record tree is a single piece.")
add('Wall mirror',[
 E('Egyptian bronze mirror','Bronze mirror of the Eighteenth Dynasty (1540-1296 BC), held by the Cleveland Museum of Art.',W+'Mirror','Egypt','','1540-1296 BC'),
 E('Chinese magic mirror','Bronze mirror whose face projects the image cast on its back.',W+'Mirror','China'),
],"Commodity kind under the icon rule: one origin entry and design pieces held by a museum collection. Follows Wikipedia's Mirror article, read in full (245,018 characters; the last 45,000 are references). Covers 7 entries; the rest of the article is optics, architecture and art installations.")
tmp=P+'.tmp'
json.dump(d,open(tmp,'w'),ensure_ascii=False,indent=1)
os.replace(tmp,P)
print('ok')
