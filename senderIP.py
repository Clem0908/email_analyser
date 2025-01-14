import re

def senderIP(email: str):

    res = "<p><b>Sender IP is:</b> "
    
    pattern = re.compile("sender IP is [0-9]{1,3}[.][0-9]{1,3}[.][0-9]{1,3}[.][0-9]{1,3}",flags=re.DOTALL)
    find = pattern.findall(email)
    if len(find) != 0:
        find[0] = find[0].replace("sender IP is ", "")
        res += find[0]

    res += "</p>"
    return res
