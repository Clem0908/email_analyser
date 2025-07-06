import re

import knownIps

def checkSpecificMailHeaders(email: str):
    
    res = "<h2>Headers: </h2><table border=solid cellpadding=\"15%\">"

    # Received: smtp.mailfrom=
    pattern = re.compile("smtp.mailfrom=[^;]*",flags=re.DOTALL)
    find = pattern.findall(email)

    if len(find) > 0:
        res += "<tr><td>Received: SMTP from</td>"
        find[0] = find[0].replace("smtp.mailfrom=", "")
        res += "<td> "+find[0]+"</td></tr>"

    pattern = re.compile("From: [^>\r]*",flags=re.DOTALL)
    find = pattern.findall(email)

    if len(find) > 0:
        res += "<tr><td>From (can be changed by the sender)</td>"
        find[0] = find[0].replace("From: ", "")
        find[0] = find[0].replace("<", "")
        find[0] = find[0].replace("\r", "")
        res += "<td> "+find[0]+" </td>"

    pattern = re.compile("Subject: [^\r]*",flags=re.DOTALL)
    find = pattern.findall(email)

    if len(find) > 0:
        res += "<tr><td>Subject</td>"
        find[0] = find[0].replace("Subject: ", "")
        res += "<td> "+find[0]+" </td>"

    pattern = re.compile("X-CSA-Complaints: [a-zA-Z0-9-_.@]*",flags=re.DOTALL)
    find = pattern.findall(email)

    if len(find) > 0:
        res += "<tr><td>Certified Senders Alliance<br>Must be equals to: whitelist-complaints@eco.de</td>"
        find[0] = find[0].replace("X-CSA-Complaints: ", "")
        find[0] = find[0].replace("<", "")
        find[0] = find[0].replace(">", "")
        res += "<td> "+find[0]+" </td>"

    pattern = re.compile("List-Unsubscribe:\\s*<([^>]+)>(,\\s*<([^>]+)>)?",flags=re.DOTALL)
    find = pattern.findall(email)

    if len(find) > 0:
        res += "<tr><td>List Unsubscribe<br>Careful, only unsubscribe things you know you subscribed to</td>"
        res += "<td> "+str(find[0])+" </td>"

    # X-Complaints-To
    pattern = re.compile("X-Complaints-To:\\s*([^\s]+)",flags=re.DOTALL)
    find = pattern.findall(email)

    if len(find) > 0:
        res += "<tr><td>Complaints to</td>"
        find[0] = find[0].replace("X-Complaints-To: ", "")
        res += "<td> "+find[0]+" </td>"

    # X-Report-Abuse
    pattern = re.compile("X-Report-Abuse: [a-z:/.A-WY-Z0-9?&%_=@<>+,\\- ]*",flags=re.DOTALL)
    find = pattern.findall(email)

    if len(find) > 0:
        res += "<tr><td>Report abuse</td>"
        find[0] = find[0].replace("X-Report-Abuse: ", "")
        res += "<td> "+find[0]+" </td>"
    
    # X-Report-Abuse-To
    pattern = re.compile("X-Report-Abuse-To:\\s*<([^>]+)>",flags=re.DOTALL)
    find = pattern.findall(email)

    if len(find) > 0:
        res += "<tr><td>Report abuse to</td>"
        find[0] = find[0].replace("X-Report-Abuse-To: ", "")
        res += "<td> "+find[0]+" </td>"

    # X-Originating-IP
    pattern = re.compile("X-Originating-IP: [0-9.\\[\\]]*",flags=re.DOTALL)
    find = pattern.findall(email)

    if len(find) > 0:
        res += "<tr><td>Originating IP</td>"
        find[0] = find[0].replace("X-Originating-IP: ", "")
        find[0] = find[0].replace("[", "")
        find[0] = find[0].replace("]", "")
        kiik = knownIps.isKnown(find[0])
        res += "<td>"+find[0]+kiik+" | <a href=\"http://127.0.0.1:5000/add-malicious-ip?ip="+find[0]+"\">Add</a> this IP to the malicious list"+"</td></tr>"

    # X-Sender-IP
    pattern = re.compile("X-Sender-IP: [0-9]{1,3}[.][0-9]{1,3}[.][0-9]{1,3}[.][0-9]{1,3}",flags=re.DOTALL)
    find = pattern.findall(email)

    if len(find) > 0:
        res += "<tr><td>Sender IP</td>"
        find[0] = find[0].replace("X-Sender-IP: ", "")
        kiik = knownIps.isKnown(find[0])
        res += "<td>"+find[0]+kiik+" | <a href=\"http://127.0.0.1:5000/add-malicious-ip?ip="+find[0]+"\">Add</a> this IP to the malicious list"+"</td></tr>"

    pattern = re.compile("X-Microsoft-Antispam: BCL:[0-9]{1,2}",flags=re.DOTALL)
    find = pattern.findall(email)

    if len(find) > 0:
        res += "<tr><td>May be flag as spam Microsoft score (BCL: 0 low - 9 high)</td>"
        find[0] = find[0].replace("X-Microsoft-Antispam: BCL:", "")
        res += "<td> "+find[0]+" </td>"

    pattern = re.compile("X-MS-Exchange-Organization-SCL: [0-9]",flags=re.DOTALL)
    find = pattern.findall(email)

    if len(find) > 0:
        res += "<tr><td>Microsoft anti-spam score (SCL: 0 low - 9 high)</td>"
        find[0] = find[0].replace("X-MS-Exchange-Organization-SCL: ", "")
        if int(find[0]) < 3:
            res += "<td style=\"color:green\"> "+find[0]+" </td>"
        if int(find[0]) > 3 and int(find[0]) <= 7:
            res += "<td style=\"color:orangered\"> "+find[0]+" </td>"
        if int(find[0]) > 7:
            res += "<td style=\"color:red\"> "+find[0]+" </td>"

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

    pattern = re.compile("X-VR-SPAMSCORE: [-0-9]*",flags=re.DOTALL)
    find = pattern.findall(email)

    if len(find) > 0:
        res += "<tr><td>OVH anti-spam score</td>"
        find[0] = find[0].replace("X-VR-SPAMSCORE: ", "")
        res += "<td> "+find[0]+" </td>"

    pattern = re.compile("X-OVH-Remote: [0-9]{1,3}[.][0-9]{1,3}[.][0-9]{1,3}[.][0-9]{1,3} [a-z()0-9.-]*",flags=re.DOTALL)
    find = pattern.findall(email)

    if len(find) > 0:
        res += "<tr><td>OVH remote</td>"
        find[0] = find[0].replace("X-OVH-Remote: ", "")
        res += "<td> "+find[0]+" </td>"

    pattern = re.compile("X-Ovh-Spam-Status: [a-zA-Z]*",flags=re.DOTALL)
    find = pattern.findall(email)

    if len(find) > 0:
        res += "<tr><td>OVH spam status</td>"
        find[0] = find[0].replace("X-Ovh-Spam-Status: ", "")
        res += "<td> "+find[0]+" </td>"

    pattern = re.compile("X-Ovh-Spam-Reason: [a-zA-WY-Z:; ]*",flags=re.DOTALL)
    find = pattern.findall(email)

    if len(find) > 0:
        res += "<tr><td>OVH spam reason</td>"
        find[0] = find[0].replace("X-Ovh-Spam-Reason: ", "")
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
