import re

def checkSpyingPixel(email: str):
    
    CASES = "(width=[0-1]{1})|(width=\"[0-1]\"{1})|(width='[0-1]'{1})|(width=3D\"[0-1]\"{1})|(width=\"[0-1]{1}px\")"

    res = ""
    pattern = re.compile(CASES, flags = re.DOTALL)
    find = pattern.findall(email)
    
    if len(find) > 0:
        res += "<p><b>"+str(len(find))+" spying pixels found</b></p><br>"
        pattern = re.compile("<img [a-zA-Z=\"\\/%0-9-_.:,;&?!#~{}\n ]*>", flags=re.DOTALL)
        find = pattern.findall(email)
        res += "<table border=solid cellpadding=\"15%\">"
        for i in range(0, len(find)):
            find[i] = find[i].replace("<","&lt;")
            find[i] = find[i].replace(">","&gt;")
            res += "<tr><td>"+find[i]+"</td></tr>"

        res += "</table>"

    return res
