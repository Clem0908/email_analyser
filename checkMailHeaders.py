import re

def checkMailHeaders(email: str):

    res = ""
    pattern = re.compile("spf=\\w+",flags=re.DOTALL)
    find = pattern.findall(email)
    if len(find) > 0:
        spf = find[0].replace("spf=", "")
        if spf != "pass":
            res += "<p style=\"color:red\"><b>SPF: </b>"+spf+"</p>"
        else:
            res += "<p style=\"color:green\"><b>SPF: </b>"+spf+"</p>"

    pattern = re.compile("dkim=\\w+",flags=re.DOTALL)
    find = pattern.findall(email)
    if len(find) > 0:
        dkim = find[0].replace("dkim=", "")
        if dkim != "pass":
            res += "<p style=\"color:red\"><b>DKIM: </b>"+dkim+"</p>"
        else:
            res += "<p style=\"color:green\"><b>DKIM: </b>"+dkim+"</p>"

    pattern = re.compile("dmarc=\\w+",flags=re.DOTALL)
    find = pattern.findall(email)
    if len(find) > 0:
        dmarc = find[0].replace("dmarc=", "")
        if dmarc != "pass":
            res += "<p style=\"color:red\"><b>DMARC: </b>"+dmarc+"</p>"
        else:
            res += "<p style=\"color:green\"><b>DMARC: </b>"+dmarc+"</p>"

    return res

