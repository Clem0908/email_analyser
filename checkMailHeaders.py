import re

def checkMailHeaders(email: str):

    res = ""
    pattern = re.compile("spf=\\w+",flags=re.DOTALL)
    find = pattern.findall(email)
    if len(find) > 0:
        spf = find[0].replace("spf=", "")
        res += "<p><b>SPF: </b>"+spf+"</p>"

    pattern = re.compile("dkim=\\w+",flags=re.DOTALL)
    find = pattern.findall(email)
    if len(find) > 0:
        dkim = find[0].replace("dkim=", "")
        res += "<p><b>DKIM: </b>"+dkim+"</p>"

    pattern = re.compile("dmarc=\\w+",flags=re.DOTALL)
    find = pattern.findall(email)
    if len(find) > 0:
        dmarc = find[0].replace("dmarc=", "")
        res += "<p><b>DMARC: </b>"+dmarc+"</p>"

    return res

