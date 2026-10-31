# -*- coding: utf-8 -*-
import json,re,sys,os
sys.path.insert(0,'/home/user/Possession-Taxonomy/rebuild/work/V4_I3')
from data import VID,WL
R='/home/user/Possession-Taxonomy/rebuild/'
d=json.load(open(R+'work/V4_I3/bak/I3.json'))
brands=json.load(open(R+'work/V4_I3/bak/I3_brands.json'))
J=lambda **k:k
def regname(n):
    return n

MKT_KINDS={'Video streaming service','Music streaming','Cloud storage plan','AI assistant subscription','Mobile phone plan'}
COMMODITY_DEPT='Services & staff'
OPPAREN={'Motoring club and breakdown cover'}

def split_name(n,mk,kind):
    """return base name, versions list, country (for parens countries)"""
    cty=None;vs=[]
    m=re.match(r'^(.*?)\s*\((.*)\)\s*$',n)
    if m:
        base,inner=m.group(1),m.group(2)
        if kind in OPPAREN: return base,[],inner
        if re.search(r'incl\.|now in|formerly|\+ ',inner) or inner.startswith(('San Diego','formerly')):
            return base,[],None
        parts=[p.strip() for p in re.split(r'\s·\s|,\s*',inner) if p.strip()]
        return base,[{"n":p,"mk":"","y":"","d":""} for p in parts],None
    if ' · ' in n:
        toks=n.split(' · ')
        w=toks[0].split(' ')
        base=w[0]; first=' '.join(w[1:])
        vs=([first] if first else [])+toks[1:]
        return base,[{"n":p,"mk":"","y":"","d":""} for p in vs],None
    return n,[],None

def generic(k,sec):
    kind=k['n']; src=k.get('s','')
    xs=[]; seen=set(x['n'].lower() for x in (k.get('x') or []))
    rows=[(a,b,'m') for a,b in (k.get('m') or [])]+[(a,b,'r') for a,b in (k.get('r') or [])]
    for n,mk,_ in rows:
        base,vs,cty=split_name(n,mk,kind)
        if base.lower() in seen: continue
        seen.add(base.lower())
        owner=mk; g=None; c=cty
        if ' · ' in mk:
            o,rest=mk.split(' · ',1); owner=o
            if len(rest)<30 and ',' not in rest and 'Which' not in rest and 'MVNO' not in rest: c=rest
        x={"n":base,"d":f"{base} is a {kind[0].lower()+kind[1:]} sold by {owner}." if owner and owner!=base else f"{base} is a {kind[0].lower()+kind[1:]} sold under its own name.","s":src,"v":vs}
        if owner and owner not in ('UK train operators',): x["mk"]=owner; x["own"]=owner
        if c: x["cty"]=c
        xs.append(x)
    return xs

def mk_vid():
    xs=[]
    order=["United States","India","China","Japan","Europe","Middle East and Africa","Americas outside the United States","Oceania"]
    def sec(r):
        s=r[6]
        if s in ("Hong Kong","Indonesia","Philippines","Malaysia","Taiwan","South Korea"): return "Asia outside India, China and Japan"
        return s
    order.insert(4,"Asia outside India, China and Japan")
    rows=sorted(VID,key=lambda r:(order.index(sec(r)),r[3] or 9999,r[0]))
    for n,own,cty,y,subs,tier,s in rows:
        x={"n":n,"d":f"Video streaming service from {cty}." if cty else "Video streaming service.","mk":own or "","y":str(y),"s":WL,"v":[],"g":sec((n,own,cty,y,subs,tier,s))}
        if own: x["own"]=own
        if tier: x["tier"]=tier
        if cty: x["cty"]=cty
        xs.append(x)
    return xs

MC="https://en.wikipedia.org/wiki/Comparison_of_music_streaming_services"
# name, owner, cty, year, active users M (page), tier, section
MUS=[
("Spotify","Spotify","Sweden",2008,777,"Global group","Global services"),
("Apple Music","Apple","United States",2015,108,"Global group","Global services"),
("Amazon Music","Amazon","United States",2007,52.5,"Global group","Global services"),
("YouTube Music","Google","United States",2015,125,"Global group","Global services"),
("Deezer","","France",2007,16,"Independent","Global services"),
("Tidal","","",2014,4.2,"Independent","Global services"),
("Qobuz","","France",2007,0.2,"Independent","Global services"),
("SoundCloud","","",2008,175,"Independent","Global services"),
("Audiomack","","",2012,40,"Independent","Global services"),
("Bandcamp","","United States",2008,0,"Independent","Global services"),
("IDAGIO","","Germany",2015,0,"Independent","Global services"),
("Pandora","SiriusXM","United States",2005,58,"National champion","North America"),
("LiveOne","","United States",2007,3.7,"Independent","North America"),
("Wolfgang's","","United States",2006,0,"Independent","North America"),
("hoopla","","United States",2010,2.5,"Independent","North America"),
("QQ Music","Tencent Music Entertainment","China",2005,660,"National champion","Asia"),
("NetEase Cloud Music","","China",2013,206.7,"National champion","Asia"),
("JioSaavn","","India",0,250,"National champion","Asia"),
("Gaana","","India",2010,201,"National champion","Asia"),
("Joox","","",2015,80,"Independent","Asia"),
("Melon","","South Korea",2004,0,"Independent","Asia"),
("VIBE","","South Korea",2018,0,"Independent","Asia"),
("KKBox","","",2004,0,"Independent","Asia"),
("Line Music","","Japan",2015,0,"Independent","Asia"),
("Moov","","",2006,0,"Independent","Asia"),
("Anghami","","",2012,70,"National champion","Middle East and Africa"),
("Boomplay","","",2015,0,"Independent","Middle East and Africa"),
("ROXi","","United Kingdom",2016,0,"Independent","Europe"),
]
CLD="https://en.wikipedia.org/wiki/Comparison_of_file_hosting_services"
CLOUD=[
("Apple iCloud","Apple","United States","Global group","Platform-owned"),
("Google Drive","Google","United States","Global group","Platform-owned"),
("Microsoft OneDrive","Microsoft","United States","Global group","Platform-owned"),
("Dropbox","Dropbox","United States","Independent","Independent services"),
("Box","Box","United States","Independent","Independent services"),
("Mega","","New Zealand","Independent","Independent services"),
("pCloud","pCloud","Switzerland","Independent","Independent services"),
("Proton Drive","Proton","Switzerland","Independent","Independent services"),
("Tresorit","","","Independent","Independent services"),
("Sync","Sync.com","Canada","Independent","Independent services"),
("SugarSync","","","","Independent services"),
("MediaFire","","","","Independent services"),
("Jumpshare","","","","Independent services"),
("CloudMe","","","","Independent services"),
("SecureSafe","","","","Independent services"),
("TitanFile","","","","Independent services"),
("filen.io","","","","Independent services"),
("koofr.eu","","","","Independent services"),
("Synology C2","Synology","Taiwan","Independent","Independent services"),
("Baidu Cloud","Baidu","China","","Regional services"),
("Tencent Weiyun","Tencent","China","","Regional services"),
("Nutstore","","China","","Regional services"),
("Yandex Disk","Yandex","Russia","","Regional services"),
]
AIM="https://momenticmarketing.com/blog/top-ai-chatbots"
AI=[
("ChatGPT","OpenAI","United States","Independent","https://en.wikipedia.org/wiki/ChatGPT",["Go","Plus","Pro"],"OpenAI"),
("Gemini","Google","United States","Global group","https://en.wikipedia.org/wiki/Google_One",["Google AI Pro","Google AI Ultra"],"Google"),
("Claude","Anthropic","United States","Independent","https://en.wikipedia.org/wiki/Claude_(language_model)",["Pro","Max"],"Anthropic"),
("Microsoft Copilot","Microsoft","United States","Global group","https://en.wikipedia.org/wiki/Microsoft_Copilot",["Copilot Pro"],"Microsoft"),
("Perplexity","Perplexity","United States","Independent","https://en.wikipedia.org/wiki/Perplexity_AI",["Pro"],"Perplexity"),
("Grok","xAI","United States","Independent",AIM,[],"xAI"),
]
MOB="https://en.wikipedia.org/wiki/List_of_mobile_network_operators"
USW="https://en.wikipedia.org/wiki/List_of_United_States_wireless_communications_service_providers"
# brand, owner, cty, tier, section
MOBN=[
("Verizon","Verizon Communications","United States","National champion","North America"),
("T-Mobile","Deutsche Telekom","United States","National champion","North America"),
("AT&T","AT&T Inc.","United States","National champion","North America"),
("Visible by Verizon","Verizon","United States","Independent","North America"),
("Mint Mobile","T-Mobile","United States","Independent","North America"),
("Rogers","Rogers Communications","Canada","National champion","North America"),
("Bell","Bell Canada","Canada","National champion","North America"),
("Vivo","Telefônica Brasil","Brazil","National champion","Latin America"),
("Vodafone","Vodafone Group","United Kingdom","Global group","Europe"),
("EE","BT Group","United Kingdom","National champion","Europe"),
("O2","Telefónica / Virgin Media O2","United Kingdom","Global group","Europe"),
("VodafoneThree","Vodafone Group","United Kingdom","National champion","Europe"),
("giffgaff","Virgin Media O2","United Kingdom","Independent","Europe"),
("Tesco Mobile","Tesco","United Kingdom","Independent","Europe"),
("Telekom","Deutsche Telekom","Germany","Global group","Europe"),
("1&1","United Internet","Germany","Independent","Europe"),
("congstar","Deutsche Telekom","Germany","Independent","Europe"),
("Orange","Orange S.A.","France","Global group","Europe"),
("SFR","Altice France","France","National champion","Europe"),
("Free Mobile","Iliad","France","Independent","Europe"),
("TIM","TIM Group","Italy","National champion","Europe"),
("Movistar","Telefónica","Spain","Global group","Europe"),
("KPN","KPN","Netherlands","National champion","Europe"),
("Swisscom","Swisscom","Switzerland","National champion","Europe"),
("Telia","Telia Company","Sweden","Global group","Europe"),
("Telenor","Telenor","Norway","Global group","Europe"),
("MTS","Sistema","Russia","National champion","Europe"),
("MegaFon","AF Telecom Holding","Russia","National champion","Europe"),
("Jio","Jio Platforms","India","National champion","Asia"),
("Airtel","Bharti Airtel","India","Global group","Asia"),
("Vi","Vodafone Idea","India","National champion","Asia"),
("BSNL Mobile","Government of India","India","National champion","Asia"),
("China Mobile","Government of China (74.25 %)","China","National champion","Asia"),
("China Telecom","China Telecommunications Corp.","China","National champion","Asia"),
("China Unicom","China Unicom Ltd.","China","National champion","Asia"),
("NTT Docomo","NTT","Japan","National champion","Asia"),
("au","KDDI","Japan","National champion","Asia"),
("Rakuten Mobile","Rakuten","Japan","Independent","Asia"),
("Telkomsel","Telkom Indonesia (65 %); Singtel (35 %)","Indonesia","National champion","Asia"),
("Viettel","Government of Vietnam","Vietnam","National champion","Asia"),
("Telstra","Telstra","Australia","National champion","Oceania"),
("Optus","Singtel","Australia","National champion","Oceania"),
("MTN","MTN Group","South Africa","Global group","Africa and Middle East"),
("e&","Emirates Investment Authority (60.03 %)","United Arab Emirates","Global group","Africa and Middle East"),
("Ooredoo","Government of Qatar","Qatar","Global group","Africa and Middle East"),
]
# ms: operator subscriptions (page rows)
OPS=[(1,"China Mobile","1,003.9","Sep 2024"),(2,"Bharti Airtel","650","Apr 2026"),(3,"Reliance Jio","524.0","Jun 2026"),(4,"China Telecom","423.4","Sep 2024"),(5,"Vodafone","355.0","May 2026"),(6,"China Unicom","345.0","Sep 2024"),(7,"América Móvil","315.8","Sep 2024"),(8,"MTN Group","288.0","Sep 2024"),(9,"Deutsche Telekom","258.8","Sep 2024"),(10,"Orange","256.4","Feb 2026"),(11,"Telefónica","249.3","Feb 2025"),(12,"Vodafone Idea","199.57","Jul 2026"),(13,"Axiata","162.5","Dec 2023"),(14,"Telkomsel","159.3","Dec 2023"),(15,"e& (Etisalat)","159","2021"),(16,"VEON","153.9","Dec 2024"),(17,"Ooredoo","149.4","Q3 2024"),(18,"Verizon","146","Dec 2024"),(19,"AT&T","139.0","Sep 2024"),(20,"Telenor","138.31","Q3 2024"),(21,"Viettel","110.0","Q1 2022"),(22,"BSNL Mobile","91.74","date not stated"),(23,"NTT Docomo","91.4","Q3 2025"),(24,"MTS","87.60","Q3 2024"),(25,"MegaFon","77.26","Q2 2024")]

def ent(n,d_,s,**kw):
    x={"n":n,"d":d_,"s":s,"v":kw.pop("v",[])}
    for k,v in kw.items():
        if v not in (None,""): x[k]=v
    return x

def mk_music():
    order=["Global services","North America","Asia","Middle East and Africa","Europe"]
    rows=sorted(MUS,key=lambda r:(order.index(r[6]),r[3] or 9999,r[0]))
    xs=[]
    for n,own,cty,y,u,tier,sec in rows:
        v=[{"n":"Apple Music Classical","mk":"Apple","y":"","d":"classical-music app"}] if n=="Apple Music" else []
        xs.append(ent(n,f"Music streaming service{' from '+cty if cty else ''}.",MC,mk=own,y=str(y) if y else "",own=own,tier=tier,cty=cty,g=sec,v=v))
    return xs
def mk_cloud():
    xs=[]
    for n,own,cty,tier,sec in CLOUD:
        xs.append(ent(n,"Online storage service for personal files, with sync between devices.",CLD,mk=own,own=own,tier=tier,cty=cty,g=sec))
    return xs
def mk_ai():
    xs=[]
    for n,own,cty,tier,s,vs,lab in AI:
        xs.append(ent(n,f"AI chat assistant from {own}.",s,mk=own,own=own,tier=tier,cty=cty,g=lab,v=[{"n":v if v.startswith(('Google','Copilot')) else f"{n} {v}","mk":own,"y":"","d":"paid plan"} for v in vs]))
    return xs
def mk_mob(src_k):
    order=["North America","Latin America","Europe","Asia","Oceania","Africa and Middle East"]
    rows=sorted(MOBN,key=lambda r:(order.index(r[4]),r[2],r[0]))
    xs=[]
    for n,own,cty,tier,sec in rows:
        xs.append(ent(n,f"Mobile network or mobile brand in {cty}, run by {own}.",MOB,mk=own,own=own,tier=tier,cty=cty,g=sec))
    return xs

def ms_video():
    L=[]
    for who,sh,yr,note in [("Netflix","20 %","Q4 2025","US share of streaming, JustWatch; share of viewing activity, not subscribers"),("Amazon Prime Video","19 %","Q4 2025",""),("Disney+","14 %",2025,""),("Apple TV","9 %",2025,"")]:
        L.append({"mkt":"US streaming video","who":who,"share":sh,"yr":yr,"s":"https://www.mactech.com/2026/01/14/justwatch-apple-tv-now-has-9-of-the-us-streaming-market/amp/","note":note or "JustWatch share of the US streaming market, as reported by MacTech"})
    for n,own,cty,y,subs,tier,sec in VID:
        if subs>=50:
            L.append({"mkt":"Global video streaming, subscribers","who":n,"share":f"{subs:g} million subscribers","yr":"page undated","s":WL,"note":"as listed on Wikipedia's list of streaming services; figures from several years and sources"})
    return L
def ms_music():
    return [
     {"mkt":"Global music subscriptions","who":"Spotify","share":"nearly a third of 818 million subscriptions","yr":2024,"s":"https://datawrapper.dwcdn.net/juY4G/1","note":"Q4 2024, MIDiA Research via Billboard; the page gives no exact figure"},
     {"mkt":"Global music subscriptions","who":"Tencent Music Entertainment and Cloud Music","share":"21.4 % (about 175 million)","yr":2024,"s":"https://datawrapper.dwcdn.net/juY4G/1","note":"Q4 2024, MIDiA Research via Billboard; the page ties this figure to China"},
     {"mkt":"Music streaming, paying users","who":"Spotify","share":"300 million","yr":"page undated","s":MC,"note":"Wikipedia comparison page; 777 million active users"},
     {"mkt":"Music streaming, paying users","who":"YouTube Music","share":"125 million","yr":"page undated","s":MC,"note":"Wikipedia comparison page"},
     {"mkt":"Music streaming, paying users","who":"QQ Music","share":"113.5 million","yr":"page undated","s":MC,"note":"Wikipedia comparison page; 660 million active users"},
     {"mkt":"Music streaming, paying users","who":"Apple Music","share":"108 million","yr":"page undated","s":MC,"note":"Wikipedia comparison page"},
     {"mkt":"Music streaming, paying users","who":"Amazon Music","share":"52.5 million","yr":"page undated","s":MC,"note":"Wikipedia comparison page"},
     {"mkt":"Music streaming, paying users","who":"NetEase Cloud Music","share":"41.75 million","yr":"page undated","s":MC,"note":"Wikipedia comparison page"},
    ]
def ms_ai():
    return [{"mkt":"Worldwide AI chatbot web visits (share of seven assistants)","who":w,"share":s,"yr":2026,"s":AIM,"note":"September 2026, Similarweb via Momentic; web visits only, excluding apps and API use"} for w,s in [("ChatGPT (OpenAI)","57.5 %"),("Gemini (Google)","25.7 %"),("Claude (Anthropic)","9.8 %"),("DeepSeek","3.5 %"),("Grok (xAI)","2.0 %"),("Perplexity","0.9 %"),("Microsoft Copilot","0.6 %")]]
def ms_mob():
    L=[{"mkt":f"Mobile subscriptions worldwide, rank {r}","who":n,"share":f"{v} million subscriptions","yr":dt,"s":MOB,"note":"Wikipedia list of mobile network operators; counts, not market share; the date is the page's"} for r,n,v,dt in OPS]
    for n,v in [("Verizon","147.0"),("T-Mobile US","143.3"),("AT&T Mobility","121.4")]:
        L.append({"mkt":"US mobile subscribers","who":n,"share":f"{v} million","yr":2026,"s":USW,"note":"Q2 2026, Wikipedia list of US wireless providers"})
    return L

def sel_for(k,kind_src):
    return f"Follows the page cited for this kind ({kind_src}); no complete reference exists for these services, so the list is not exhaustive."
