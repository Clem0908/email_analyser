import re

def checkSpyingPixel(email: str):
    
    CASES = "(width=[0-1]{1})|(width=\"[0-1]\"{1})|(width='[0-1]'{1})|(width=3D\"[0-1]\"{1})|(width=\"[0-1]{1}px\")"

    res = ""
    pattern = re.compile(CASES, flags = re.DOTALL)
    find = pattern.findall(email)
    
    if len(find) > 0:
        res += "<p><b>"+str(len(find))+" spying pixels found</b></p>"

    return res
