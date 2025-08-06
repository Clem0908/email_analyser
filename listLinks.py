import re

def listLinks(email: str):
    
    res = ""
    pattern = re.compile("<a [^>]*",flags=re.DOTALL)
  
    #pattern = re.compile("<a href[\s]?[=]?[=]?[3]?[D]?[=]?\"([^\"]*)",flags=re.DOTALL)
    find = pattern.findall(email)

    if len(find) > 0:

        res += "<p><b>HTML hyperlinks found:</b><br></p>"
        res += "<table border=solid cellpadding=\"15%\">"

        find = list(set(find))
        for i in range(0,len(find)):
            find[i] = find[i].replace("<","")
            find[i] = find[i].replace(">","")
            res += "<tr><td>"+find[i]+"</td></tr>"

        res += "</table>"

    # CSS URLs property
    pattern = re.compile("url\([^)]*",flags=re.DOTALL)
    find = pattern.findall(email)

    if len(find) > 0:

        res += "<p><b>CSS 'url' property content found:</b><br></p>"
        res += "<table border=solid cellpadding=\"15%\">"

        find = list(set(find))
        for i in range(0,len(find)):
            find[i] = find[i].replace("url(","")
            res += "<tr><td>"+find[i]+"</td></tr>"

        res += "</table>"

    return res
