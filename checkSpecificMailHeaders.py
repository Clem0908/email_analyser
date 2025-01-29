import re

def checkSpecificMailHeaders(email: str):
    
    res = "<h2>Headers: </h2><table border=solid cellpadding=\"15%\">"

    pattern = re.compile("X-Originating-IP: [[0-9]{1,3}[.][0-9]{1,3}[.][0-9]{1,3}[.][0-9]{1,3}]",flags=re.DOTALL)
    find = pattern.findall(email)

    if len(find) > 0:
        res += "<tr><td>Originating IP</td>"
        find[0] = find[0].replace("X-Originating-IP: ", "")
        res += "<td> "+find[0]+" </td>"

    pattern = re.compile("X-Sender-IP: [0-9]{1,3}[.][0-9]{1,3}[.][0-9]{1,3}[.][0-9]{1,3}",flags=re.DOTALL)
    find = pattern.findall(email)

    if len(find) > 0:
        res += "<tr><td>Sender IP</td>"
        find[0] = find[0].replace("X-Sender-IP: ", "")
        res += "<td> "+find[0]+" </td>"

    pattern = re.compile("X-Microsoft-Antispam: BCL:[0-9]{1,2}",flags=re.DOTALL)
    find = pattern.findall(email)

    if len(find) > 0:
        res += "<tr><td>Microsoft anti-spam score (BCL: 0 low - 9 high)</td>"
        find[0] = find[0].replace("X-Microsoft-Antispam: BCL:", "")
        res += "<td> "+find[0]+" </td>"

    pattern = re.compile("X-MS-Exchange-Organization-SCL: [0-9]",flags=re.DOTALL)
    find = pattern.findall(email)

    if len(find) > 0:
        res += "<tr><td>Microsoft anti-spam score (SCL: 0 low - 9 high)</td>"
        find[0] = find[0].replace("X-MS-Exchange-Organization-SCL: ", "")
        res += "<td> "+find[0]+" </td>"

    pattern = re.compile("X-Microsoft-Antispam-Mailbox-Delivery: .*;RF:JunkEmail",flags=re.DOTALL)
    find = pattern.findall(email)

    if len(find) > 0:
        res += "<tr><td>Microsoft anti-spam verdict: </td>"
        res += "<td>JunkEmail</td>"

    pattern = re.compile("X-VR-SPAMSTATE: [a-zA-Z]*",flags=re.DOTALL)
    find = pattern.findall(email)

    if len(find) > 0:
        res += "<tr><td>OVH anti-spam status</td>"
        find[0] = find[0].replace("X-VR-SPAMSTATE: ", "")
        res += "<td> "+find[0]+" </td>"

    pattern = re.compile("X-VR-SPAMSCORE: [0-9]*",flags=re.DOTALL)
    find = pattern.findall(email)

    if len(find) > 0:
        res += "<tr><td>OVH anti-spam score</td>"
        find[0] = find[0].replace("X-VR-SPAMSCORE: ", "")
        res += "<td> "+find[0]+" </td>"

    pattern = re.compile("X-VRC-SPAM-STATE: [a-zA-Z]*",flags=re.DOTALL)
    find = pattern.findall(email)

    if len(find) > 0:
        res += "<tr><td>Vade Secure spam status</td>"
        find[0] = find[0].replace("X-VRC-SPAM-STATE: ", "")
        res += "<td> "+find[0]+" </td>"

    pattern = re.compile("X-BSC: [a-zA-Z]*",flags=re.DOTALL)
    find = pattern.findall(email)

    if len(find) > 0:
        res += "<tr><td>BlueSecure phising campaign</td>"
        find[0] = find[0].replace("X-BSC: ", "")
        res += "<td> "+find[0]+" </td>"

    res += "</table>"
    return res
