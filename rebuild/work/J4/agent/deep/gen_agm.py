import json,sys,subprocess,collections
sys.path.insert(0,'work/J4/agent/deep')
from agm_data import AGM
URL='https://www.rhs.org.uk/plants/pdfs/rhs-recommended-award-of-garden-merit-fruit-veg.pdf'
jobs=collections.defaultdict(dict)
for (job,kind),L in AGM.items():
    xs=[]
    for e in L:
        n,g,yy=e.split('|'); yr=(1900+int(yy)) if int(yy)>=90 else 2000+int(yy)
        crop=kind.lower() if g==kind.lower() else g
        d=f"RHS Award of Garden Merit cultivar ({g}), awarded {yr}." if g!=kind.lower() and g not in ('x',) else f"{kind} cultivar holding the RHS Award of Garden Merit, awarded {yr}."
        xs.append({"n":n,"d":d,"s":URL,"dt":f"RHS AGM {yr}"+(f" · {g}" if g!=kind.lower() else "")})
    jobs[job][kind]={"x":xs}
for job,k in jobs.items():
    json.dump({"kinds":k},open(f'work/J4/agent/deep/spec_agm_{job}.json','w'),ensure_ascii=False)
    print(subprocess.run(['python3','work/J4/agent/deep/add.py',job,f'work/J4/agent/deep/spec_agm_{job}.json'],capture_output=True,text=True).stdout.strip())
