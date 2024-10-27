import re

def checkMailHeaders(email: str):

    res = ""
    pattern = re.compile(".*spf=(fail|none|softfail|temperror|permerror).*",flags=re.DOTALL)
    find = pattern.findall(email)
    if len(find) > 0:
        res += "<p>SPF: [!]</p>"
    else:
        res += "<p>SPF: [OK]</p>"

    pattern = re.compile(".*dkim=(fail|none|softfail|temperror|permerror).*",flags=re.DOTALL)
    find = pattern.findall(email)
    if len(find) > 0:
        res += "<p>DKIM: [!]</p>"
    else:
        res += "<p>DKIM: [OK]</p>"
    
    pattern = re.compile(".*dmarc=(fail|none|softfail|temperror|permerror).*",flags=re.DOTALL)
    find = pattern.findall(email)
    if len(find) > 0:
        res += "<p>DMARC: [!]</p>"
    else:
        res += "<p>DMARC: [OK]</p>"

    return res

