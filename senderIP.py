import re

def senderIP(email: str):

    pattern = re.compile("[0-9]{1,3}[.][0-9]{1,3}[.][0-9]{1,3}[.][0-9]{1,3}",flags=re.DOTALL)
    find = pattern.findall(email)

    if len(find) > 0:

        res = "<table border=solid><b>Detected IPs: </b><br></br><tr>"

        for i in range(0, len(find)):

            res += "<td>" + find[i] + "</td>"
    
        res += "</tr></table>"

    return res
