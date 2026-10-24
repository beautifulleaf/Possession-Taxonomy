"""Write wave-3 harvest prompts (SESSION_8 step 6): verify/in/HV_<CODE>_<n>.prompt.txt for the sub-family groups given.
usage: hv_prompt.py CODE "D2.1 D2.2" "D2.3 D2.4 ..."  (one argument per batch)"""
import sys
from common import ROOT
code, groups = sys.argv[1], sys.argv[2:]
for i, g in enumerate(groups, 1):
    b = f"HV_{code}_{i}"
    t = f"""BATCH {b}. Read /home/user/Possession-Taxonomy/verify/in/HV_COMMON.txt and follow it with <CODE> = {code} and <BATCH> = {b} (wave 3, SESSION_8 step 6). Tree verify/out/TREE_{code}.md, worklist verify/out/HV_{code}_worklist.tsv; also read section 14 of framework/structure/{code}.md and the {code} rows of framework/structure/navigation/proposals.tsv and framework/structure/maker_roles.tsv. Your sub-families: {', '.join(g.split())}. Kinds marked † need a fetched shop, catalogue or register page showing the type sold under its name. Makers follow the {code} maker role (BRIEF.md, owner 2026-10-24): way in = record every maker the fetched pages show, worldwide, with signature models as named forms and series as lines; owner only = a maker enters only as the owner of a named form or line (no maker lists); none = makers only through a branded product. Use existing catalogues, databases and specialist shops first (BRIEF.md). Countries only when a page states them (countries never divide the category). Report every generic type with no kind as 'missing kind?' with its URL, and write the report to verify/out/{b}_report.md as well as replying. Web: WebSearch for search; when WebFetch returns an empty page or HTTP 403, use the authenticated Parallel fetch tool mcp__888719e7-19cd-4947-b76b-21e49afd98e5__web_fetch (load with ToolSearch; allow_live_fetch true; session_id "{b.lower()}-s8"; model_name your model id) on the same URL. The fetch log verify/work/{b}/fetched.tsv starts with the header url, fetch_status, gave; nothing after the URL in the url column; log each fetch the moment you make it; never type or build a URL. A similar-sounding brand is a different brand. Working directory: /home/user/Possession-Taxonomy. Never run git.
"""
    (ROOT / f"verify/in/{b}.prompt.txt").write_text(t)
    print(b)
