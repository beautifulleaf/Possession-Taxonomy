import sys; sys.path.insert(0,'work/C3/agent'); from w import w
w('C3','05_05',{"kinds":[{"n":"Turf","a":"cultivated sod · sod · lawn turf","d":"Living grass sold as rolls or slabs of cultivated sod to lay as a lawn.","t":["ryegrass","fescue","Bermuda grass","zoysia","Kentucky bluegrass","St Augustine grass"],"s":"https://gertens.com/sod-rolls-pickup"}],"brands":[],"traditions":[],"notes":"Restraint-only: kept Turf as one kind; grass species moved into t types. No models in old data; no brands added."})
G="https://www.gardenersdream.co.uk/collections/real-christmas-trees"
T=["cut","pot-grown","rooted"]
def k(n,a,d): return {"n":n,"a":a,"d":d,"t":T,"s":G}
w('C3','09_01',{"kinds":[
 k("Nordmann fir","Abies nordmanniana","Fresh-cut, pot-grown or rooted Nordmann fir sold as a Christmas tree."),
 k("Fraser fir","Abies fraseri","Fresh-cut, pot-grown or rooted Fraser fir sold as a Christmas tree."),
 k("Noble fir","Abies procera","Fresh-cut, pot-grown or rooted noble fir sold as a Christmas tree."),
 k("Norway spruce","Picea abies","Fresh-cut, pot-grown or rooted Norway spruce sold as a Christmas tree."),
 k("Blue spruce","Picea pungens · Colorado blue spruce","Fresh-cut, pot-grown or rooted blue spruce sold as a Christmas tree.")],
 "brands":[],"traditions":[],"notes":"Restraint-only: all five kinds kept; supply form (cut, pot-grown, rooted) as t types; height is a detail at purchase, not recorded. Botanical names taken from old definitions and well-established species names. No models or brands."})
