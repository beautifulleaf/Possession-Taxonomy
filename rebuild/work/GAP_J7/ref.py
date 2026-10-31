import re
def ref(sel):
    pats=[r"((?:Wikipedia['’]s|Wine Australia['’]s|Wikipedia) [A-Z][^,;(]*?)(?: \(|,|;|\.| page| article|$)",
          r"(Wines of Greece[^,;(]*?)(?: \(|,|;|\.|$)", r"(Taste Hungary guide)", r"(jref\.com[^)]*)"]
    for p in pats:
        m=re.search(p,sel)
        if m: return m.group(1).strip()
    return None
