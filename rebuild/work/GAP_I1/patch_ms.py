import json,os
P='/home/user/Possession-Taxonomy/rebuild/out/I1.json'
d=json.load(open(P))
S="https://security.org/digital-safety/password-manager-annual-report"
R="https://ramp.com/data/ai-index"
note="Security.org online poll of 1,000 US adults, October 2024, question 'What password manager do you primarily use?'; the page does not state the base"
pm=[("Google Password Manager","32 %"),("Apple (iCloud Keychain or Passwords)","23 %"),("LastPass","11 %"),("Bitwarden","10 %"),("1Password","5 %"),("Norton","3 %"),("Keeper","3 %"),("Dashlane","2 %"),("NordPass","1 %"),("McAfee True Key","1 %")]
ai=[("Anthropic","43.8 %"),("OpenAI","40.6 %"),("xAI","4.1 %"),("DeepSeek","0.3 %"),("Mistral AI","0.2 %")]
for dp in d['depts']:
    if dp['n']=='Security & privacy':
        dp['ms']=[{"mkt":"Password managers, US adults","who":w,"share":s,"yr":2024,"s":S,"note":note} for w,s in pm]
        dp['msum']="Security.org's October 2024 poll: browser and phone built-in managers (Google 32 %, Apple 23 %) lead; LastPass, Bitwarden and 1Password follow."
    if dp['n']=='Internet & AI':
        have={(m['mkt'],m['who']) for m in dp['ms']}
        for w,s in ai:
            m={"mkt":"AI provider adoption, US businesses","who":w,"share":s,"yr":2026,"s":R,"note":"Ramp AI Index, September 2026: share of 85,000+ US businesses with a card, invoice or ACH payment to the provider that month"}
            if (m['mkt'],w) not in have: dp['ms'].append(m)
tmp=P+'.tmp'; json.dump(d,open(tmp,'w'),ensure_ascii=False); os.replace(tmp,P)
