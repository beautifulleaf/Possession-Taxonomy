import sys; sys.path.insert(0,'work/I2/agent')
from put import put
def A(n,mk,y,s,d,v=(),a='',dt=''):
    x={"n":n,"a":a,"d":d,"mk":mk,"y":y,"s":s,"v":[dict(n=i[0],mk=i[1],y=i[2],d=i[3]) for i in v]}
    if dt: x["dt"]=dt
    return x
T="https://steamcommunity.com/tradingcards/faq"; P="https://partner.steamgames.com/doc/marketing/pointsshopitems"
kinds=[
{"n":"Platform trading card","a":"Steam trading card","d":"A collectible card kept in a game platform account. A foil card is a shinier version of the same card.","t":["Normal card","Foil card","Booster pack"],"s":T,"x":[
 A("Steam trading card set","Valve","",T,"Cards that drop while playing; a full set crafts a badge, an emoticon and a profile background.",[
  ("Normal set","Valve","","Crafts a game badge, upgradable up to five levels"),("Foil set","Valve","","Crafts a foil badge valued for rarity")])]},
{"n":"Badge or pin","a":"Steam badge","d":"A badge or pin item shown on a platform profile or in a game.","t":["Game badge","Foil badge","Level badge"],"s":T,"x":[
 A("Steam game badge","Valve","",T,"Badge crafted from a full card set, upgradable five times; foil versions exist.")]},
{"n":"Profile background","a":"","d":"An image item shown behind a platform profile.","t":["Static","Animated (MP4/WebM)","Mini-profile background"],"s":T,"x":[
 A("Steam animated profile background","Valve","",P,"1920 by 1080 looping MP4 and WebM, each under 4MB, with a JPG still.")]},
{"n":"Profile avatar or frame","a":"profile picture · avatar frame","d":"A picture or decorative frame item, still or animated, shown on a platform profile.","t":["Avatar","Animated avatar (GIF, 184 px)","Avatar frame","Animated frame (APNG, 224 px)","Game profile bundle"],"s":P,"x":[
 A("Steam Points Shop game profile","Valve","",P,"Bundle of avatar, frame, mini-profile background and profile background with theme colours.")]},
{"n":"Loading screen","a":"","d":"An image item collected in a game account and shown on the player's screen while a match loads.","t":["Static","Animated"],"s":"https://www.epicgames.com/help/en-US/c-202300000001636/c-202300000001721/a202300000011084"},
{"n":"Chat emoticon","a":"emoji · animated sticker","d":"A small image used in a game's or platform's chat.","t":["Emoticon","Animated sticker (APNG, 150 px)"],"s":T},
{"n":"Messaging sticker pack","a":"LINE sticker set","d":"A set of stickers used in a messaging platform's chats.","t":["Static set (8 to 40)","Animated set (8 or 16)"],"s":"https://help2.line.me/creators/web/categoryId/20002313/3/pc?lang=en","x":[
 A("Line Friends stickers","Line Friends","2011","https://en.wikipedia.org/wiki/Line_Friends","Original Line characters by Kang Byeong Mok, led by Brown and Cony, who began as messaging stickers.",[
  ("Brown and Cony","Line Friends","2011","Central pair of the original cast"),("BT21","Line Friends","","Series designed with BTS members")])]},
]
brands=[{"n":"Line Friends","c":"South Korea","f":"2015","seg":"Specialist","kf":"sticker characters","d":"Brand managed since 2015 by Line Friends Corporation, a Naver subsidiary, from characters created in 2011.","s":"https://en.wikipedia.org/wiki/Line_Friends"}]
put('I2','02_04',{"kinds":kinds,"brands":brands,"traditions":[],"notes":"Profile avatar and Avatar frame merged into one kind with types. Archetypes only where a community collects: Steam card sets and badges, Points Shop items, Line Friends sticker sets. The Steam page gave no emoticon or effect specs, so none stated. Telegram and WhatsApp sticker packs not sourced. Sticker packs from Line carry sizes (8-40 static, 8 or 16 animated) from the LINE creators help page."})
