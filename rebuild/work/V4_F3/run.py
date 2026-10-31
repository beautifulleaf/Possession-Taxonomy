import sys; sys.path.insert(0,'.')
import lib, p1
d=lib.load(); rep=[]
rep+=p1.run(d)
for m in ('p2','p3'):
    try: mod=__import__(m)
    except ModuleNotFoundError: continue
    rep+=mod.run(d)
lib.save(d)
for r in rep: print(r)
