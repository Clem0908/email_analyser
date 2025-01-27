import re

def checkSpecificMailHeaders(email: str):
    
    res = "<h2>Headers: </h2><table border=solid cellpadding=\"15%\">"

    pattern = re.compile("X-MS-Exchange-Organization-SCL: [0-9]",flags=re.DOTALL)
    find = pattern.findall(email)

    if len(find) > 0:
        res += "<tr><td>Microsoft anti-spam score (0 low - 9 high)</td>"
        find[0] = find[0].replace("X-MS-Exchange-Organization-SCL: ", "")
        res += "<td> "+find[0]+" </td>"

    pattern = re.compile("X-VR-SPAMSTATE: \w+",flags=re.DOTALL)
    find = pattern.findall(email)

    if len(find) > 0:
        res += "<tr><td>OVH anti-spam status</td>"
        find[0] = find[0].replace("X-VR-SPAMSTATE: ", "")
        res += "<td> "+find[0]+" </td>"

    pattern = re.compile("X-VR-SPAMSCORE: [0-9]",flags=re.DOTALL)
    find = pattern.findall(email)

    if len(find) > 0:
        res += "<tr><td>OVH anti-spam score</td>"
        find[0] = find[0].replace("X-VR-SPAMSCORE: ", "")
        res += "<td> "+find[0]+" </td>"

    pattern = re.compile("X-VRC-SPAM-STATE: \w+",flags=re.DOTALL)
    find = pattern.findall(email)

    if len(find) > 0:
        res += "<tr><td>Vade Secure spam status</td>"
        find[0] = find[0].replace("X-VRC-SPAM-STATUS: ", "")
        res += "<td> "+find[0]+" </td>"

    pattern = re.compile("X-BSC: \w+",flags=re.DOTALL)
    find = pattern.findall(email)

    if len(find) > 0:
        res += "<tr><td>BlueSecure phising campaign</td>"
        find[0] = find[0].replace("X-BSC: ", "")
        res += "<td> "+find[0]+" </td>"

    res += "</table>"
    return res
