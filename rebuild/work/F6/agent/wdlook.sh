#!/bin/bash
# usage: wdlook.sh JOB name...  (prints search hits with enwiki)
job=$1; shift
for n in "$@"; do
  echo "## $n"
  python3 tools/local.py wd F6 $job search "$n" | python3 -I -c "
import sys,json
d=json.load(sys.stdin)['search'][:3]
print(' | '.join(x['id']+':'+x['label']+' ('+(x.get('description') or '')[:50]+')' for x in d))
print(','.join(x['id'] for x in d))" 
done
