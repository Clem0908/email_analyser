import re

def listLinks(email: str):
    
    res = ""
   
    pattern = re.compile("<a href[=]?[=]?[3]?[D]?[=]?\"([^\"]*)",flags=re.DOTALL)
    find = pattern.findall(email)

    if len(find) > 0:

        res += "<p><b>Links found:</b><br></p>"
        res += "<table border=solid cellpadding=\"15%\">"

        for i in range(0,len(find)):
            find[i] = find[i].replace("<","")
            find[i] = find[i].replace(">","")
            res += "<tr><td>"+find[i]+"</td></tr>"

        res += "</table>"

    return res
