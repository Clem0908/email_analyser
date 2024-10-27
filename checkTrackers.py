import re

def checkTrackers(email: str):
    
    res = ""
   
    if "track=email" in email:
        res += "<p>Trackers found !<br></p>"

    pattern = re.compile("https?://[a-zA-Z0-9./?]*track=email",flags=re.DOTALL)
    find = pattern.findall(email)
    res += "<table>"
    for i in range(0,len(find)):
        find[i] = find[i].replace("<","&lt;")
        find[i] = find[i].replace(">","&gt;")
        res += "<tr><td>"+"&#8226; "+str(find[i])+"</td></tr>"
    res += "</table>"

    if "/track/" in email:
        res += "<p>Trackers found !<br></p>"

    pattern = re.compile("https?://[a-zA-Z0-9./?]*track[a-zA-Z0-9./?]*",flags=re.DOTALL)
    find = pattern.findall(email)
    res += "<table>"
    for i in range(0,len(find)):
        find[i] = find[i].replace("<","&lt;")
        find[i] = find[i].replace(">","&gt;")
        res += "<tr><td>"+"&#8226; "+str(find[i])+"</td></tr>"
    res += "</table>"

    return res
