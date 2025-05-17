import re

def checkSpyingPixel(email: str):
    
    CASES = "(width=[0-1]{1})|(width=\"[0-1]\"{1})|(width='[0-1]'{1})|(width=3D\"[0-1]\"{1})|(width=\"[0-1]{1}px\")|(width:[0-1]{1}px)|(width: [0-1]{1}px)|(width:[0-1]{1})|(width=3D=\'[0-1]{1}\')|(width='1px')"

    res = ""
    pattern = re.compile(CASES, flags = re.DOTALL)
    find = pattern.findall(email)
    
    if len(find) > 0:
        res += "<h2 style=\"color:red\"><b>Spying pixels found</b></h2>"

    pattern = re.compile("<img [^>]*", flags=re.DOTALL)
    find = pattern.findall(email)
    
    res += "<p><b>Images found:</b></p><table border=solid cellpadding=\"15%\">"
    for i in range(0, len(find)):
        find[i] = find[i].replace("<","")
        find[i] = find[i].replace(">","")
        res += "<tr><td>"+find[i]+"</td></tr>"

    pattern = re.compile("<image [^>]*", flags=re.DOTALL)
    find = pattern.findall(email)
    
    for i in range(0, len(find)):
        find[i] = find[i].replace("<","")
        find[i] = find[i].replace(">","")
        res += "<tr><td>"+find[i]+"</td></tr>"

    res += "</table>"

    return res
