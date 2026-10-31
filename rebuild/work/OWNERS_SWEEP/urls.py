import json,sys
from urllib.parse import quote
c=sys.argv[1]
for i,b in enumerate(json.load(open(f'batches_{c}.json'))):
    if int(sys.argv[2])<=i<int(sys.argv[3]):
        print(i,'https://en.wikipedia.org/w/api.php?action=query&format=json&formatversion=2&redirects=1&prop=revisions&rvprop=content&rvslots=main&rvsection=0&titles='+quote('|'.join(b),safe="|(),'"))
