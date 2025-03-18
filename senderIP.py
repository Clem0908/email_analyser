import re

def senderIP(email: str):

    pattern = re.compile("[0-9]{1,3}[.][0-9]{1,3}[.][0-9]{1,3}[.][0-9]{1,3}",flags=re.DOTALL)
    find = pattern.findall(email)
    res = ""

    if len(find) > 0:

        find = list(dict.fromkeys(find))
        res += "<b>Detected IPs: </b><br><br><table border=solid><tr>"

        for i in range(0, len(find)):

            res += "<td> "+find[i]+" </td>"
    
        res += "</tr></table>"

    return res
