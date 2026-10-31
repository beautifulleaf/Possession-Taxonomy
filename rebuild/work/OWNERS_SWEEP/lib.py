import json
def entries(o,out=None,inv=False):
    if out is None: out=[]
    if isinstance(o,dict):
        if 'mk' in o and not inv: out.append(o)
        for k,v in o.items(): entries(v,out,inv or k=='v')
    elif isinstance(o,list):
        for v in o: entries(v,out,inv)
    return out
