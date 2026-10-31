import json,sys,collections
R='/home/user/Possession-Taxonomy/rebuild/reader/'
for c in sys.argv[1:]:
    d=json.load(open(R+c+'.json'))
    cnt=collections.Counter(); n=0; dupk=collections.Counter()
    xm=collections.Counter()
    for dp in d['depts']:
        for s in dp['s']:
            for k in s['k']:
                dupk[k['n'].lower()]+=1
                for a in k.get('m',[])+k.get('r',[]):
                    cnt[a[1]]+=1; n+=1
                for a in k.get('x',[]): xm[a.get('mk','')]+=1
    print(c,'m+r entries',n,'top makers',cnt.most_common(6),'| arch mk top',xm.most_common(5),'| dup kind names',[k for k,v in dupk.items() if v>1])
