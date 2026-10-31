import urllib.parse
names=["Netflix","Disney+","Amazon Prime Video","HBO Max","Apple TV","Paramount+","Peacock","Hulu","Crunchyroll","Spotify","Apple Music","YouTube Music","Amazon Music","Tidal","Deezer","Qobuz","SoundCloud","Pandora","Dropbox","Google Drive","iCloud","OneDrive","Mega","Proton Drive","pCloud","ChatGPT","Gemini","Claude","Microsoft Copilot","Perplexity AI","Grok","DeepSeek"]
vals=" ".join('"%s"@en'%n for n in names)
q='''SELECT ?l (SAMPLE(?ol) AS ?owner) (SAMPLE(?cl) AS ?country) (MIN(?yr) AS ?year) WHERE { VALUES ?l { %s } ?i rdfs:label ?l . ?i wdt:P856 ?w . OPTIONAL{?i wdt:P127 ?o . ?o rdfs:label ?ol FILTER(lang(?ol)="en")} OPTIONAL{?i wdt:P495 ?c . ?c rdfs:label ?cl FILTER(lang(?cl)="en")} OPTIONAL{?i wdt:P571 ?d . BIND(YEAR(?d) AS ?yr)} } GROUP BY ?l'''%vals
print("https://query.wikidata.org/sparql?format=json&query="+urllib.parse.quote(q))
