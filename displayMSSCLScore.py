import re

def displayMSSCLScore(email: str):
    
    res = ""
    res += "<p>Microsoft anti-spam score (0 low - 9 high): "

    pattern = re.compile("X-MS-Exchange-Organization-SCL: [0-9]",flags=re.DOTALL)
    find = pattern.findall(email)
    if len(find) > 0:
        find[0] = find[0].replace("X-MS-Exchange-Organization-SCL: ", "")
        res += "<b>"+str(find[0])+"</b></p>"

    return res

