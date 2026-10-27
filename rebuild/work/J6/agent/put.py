import json, os, sys
# usage: put.py SRC.json DEST.json  -- validate JSON, write via temp file + rename
src, dest = sys.argv[1], sys.argv[2]
d = json.load(open(src))
tmp = dest + '.tmp'
with open(tmp, 'w') as f: json.dump(d, f, ensure_ascii=False, indent=1)
os.replace(tmp, dest); print('wrote', dest, len(d['kinds']), 'kinds')
