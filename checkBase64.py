import re
import base64

def checkBase64(email: str):

    ret = ""

    if "Content-Transfer-Encoding: base64" in email:
        
        ret = email[email.find("Content-Transfer-Encoding: base64")+len("Content-Transfer-Encoding: base64"):]
        ret = ret.replace("\r","<br>") 
    else:
        
        ret = ""

    return ret
