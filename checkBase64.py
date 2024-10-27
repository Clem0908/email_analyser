import re
import base64

import checkTrackers, checkSpyingPixel

def checkBase64(email: str):

    res = ""
    resCT = ""
    resSP = ""
    catFind = ""

    if "Content-Transfer-Encoding: base64" in email:

        res += "<p>Base64 encoding found, pushing analysis...</p>"
        pattern = re.compile("Content-Transfer-Encoding: base64[a-zA-Z0-9+\n ]*==",flags=re.DOTALL)
        find = pattern.findall(email)
        
        for i in range(0,len(find)):
        
            find[i] = find[i].replace("Content-Transfer-Encoding: base64  ","")
            find[i] = find[i].replace(' ','')
            find[i] = base64.b64decode(find[i]).decode('utf-8')
            catFind += find[i]

        resCT = checkTrackers.checkTrackers(catFind)
        resSP = checkSpyingPixel.checkSpyingPixel(catFind)

    res = res+resCT+resSP
    return res
