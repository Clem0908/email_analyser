import re

def checkMailHeaders(email: str):

    res = ""
    pattern = re.compile(".*spf=(fail|none|softfail|temperror|permerror).*",flags=re.DOTALL)
    find = pattern.findall(email)
    if len(find) > 0:
        res += "<p><b>SPF:</b> [!]</p>"
    else:
        res += "<p><b>SPF:</b> [OK]</p>"

    pattern = re.compile(".*dkim=(fail|none|softfail|temperror|permerror).*",flags=re.DOTALL)
    find = pattern.findall(email)
    if len(find) > 0:
        res += "<p><b>DKIM:</b> [!]</p>"
    else:
        res += "<p><b>DKIM:</b> [OK]</p>"
    
    pattern = re.compile(".*dmarc=(fail|none|softfail|temperror|permerror).*",flags=re.DOTALL)
    find = pattern.findall(email)
    if len(find) > 0:
        res += "<p><b>DMARC:</b> [!]</p>"
    else:
        res += "<p><b>DMARC:</b> [OK]</p>"

    return res

