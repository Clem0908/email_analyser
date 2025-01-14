import re

def listLinks(email: str):
    
    res = ""
   
    pattern = re.compile("https?://[a-zA-Z0-9./?=&%-_]*",flags=re.DOTALL)
    find = pattern.findall(email)

    if len(find) > 0:

        res += "<p><b>Links found:</b><br></p>"
        res += "<table>"

        for i in range(0,len(find)):
            
            res += "<tr>"
            res += "<td>"+find[i]+"</td>"
            res += "</tr>"

        res += "</table>"

    return res
