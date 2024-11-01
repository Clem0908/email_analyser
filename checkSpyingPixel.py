import re

def checkSpyingPixel(email: str):
    
    # Starting regex for a spying pixel
    SSP = "<img[a-zA-Z0-9./:;&?=\"_\\-~! ]*"
    # Ending regex for a spying pixel
    ESP = "[a-zA-Z0-9./:;&?=\"_\\-~! ]*>"

    res = "<p>Spying pixels, if found, will be listed below</p>"

    if "width=1 height=1" in email:
        
        pattern = re.compile(SSP+"width=1 height=1"+ESP,flags=re.DOTALL)
        find = pattern.findall(email)
        res += "<table>"
        for i in range(0,len(find)):
            find[i] = find[i].replace("<","&lt;")
            find[i] = find[i].replace(">","&gt;")
            res += "<tr><td>"+"&#8226; "+str(find[i])+"</td></tr>"
        res += "</table>"
    
    if "width='1' height='1'" in email:

        pattern = re.compile(SSP+"width=\'1\' height=\'1\'"+ESP,flags=re.DOTALL)
        find = pattern.findall(email)
        res += "<table>"
        for i in range(0,len(find)):
            find[i] = find[i].replace("<","&lt;")
            find[i] = find[i].replace(">","&gt;")
            res += "<tr><td>"+"&#8226; "+str(find[i])+"</td></tr>"
        res += "</table>"

    if "width=\"1\" height=\"1\"" in email:

        pattern = re.compile(SSP+"width=\"1\" height=\"1\""+ESP,flags=re.DOTALL)
        find = pattern.findall(email)
        res += "<table>"
        for i in range(0,len(find)):
            find[i] = find[i].replace("<","&lt;")
            find[i] = find[i].replace(">","&gt;")
            res += "<tr><td>"+"&#8226; "+str(find[i])+"</td></tr>"
        res += "</table>"

    if "width=\"1\" height=\"1\"" in email:

        pattern = re.compile("<img width=\"1\" height=\"1\""+ESP,flags=re.DOTALL)
        find = pattern.findall(email)
        res += "<table>"
        for i in range(0,len(find)):
            find[i] = find[i].replace("<","&lt;")
            find[i] = find[i].replace(">","&gt;")
            res += "<tr><td>"+"&#8226; "+str(find[i])+"</td></tr>"
        res += "</table>"

    if "width=\"1px\" height=\"1px\"" in email:

        pattern = re.compile(SSP+"width=\"1px\" height=\"1px\""+ESP,flags=re.DOTALL)
        find = pattern.findall(email)
        res += "<table>"
        for i in range(0,len(find)):
            find[i] = find[i].replace("<","&lt;")
            find[i] = find[i].replace(">","&gt;")
            res += "<tr><td>"+"&#8226; "+str(find[i])+"</td></tr>"
        res += "</table>"

    if "width=\"1px\" height=\"1px;\"" in email:

        pattern = re.compile("<img width=\"1px\" height=\"1px;\""+ESP,flags=re.DOTALL)
        find = pattern.findall(email)
        res += "<table>"
        for i in range(0,len(find)):
            find[i] = find[i].replace("<","&lt;")
            find[i] = find[i].replace(">","&gt;")
            res += "<tr><td>"+"&#8226; "+str(find[i])+"</td></tr>"
        res += "</table>"

    if "width: 1px; height: 1px;" in email:

        pattern = re.compile(SSP+"width: 1px; height: 1px;"+ESP,flags=re.DOTALL)
        find = pattern.findall(email)
        res += "<table>"
        for i in range(0,len(find)):
            find[i] = find[i].replace("<","&lt;")
            find[i] = find[i].replace(">","&gt;")
            res += "<tr><td>"+"&#8226; "+str(find[i])+"</td></tr>"
        res += "</table>"


    if "height=3D\"1\" width=3D\"1\"" in email:

        pattern = re.compile(SSP+"height=3D\"1\" width=3D\"1\""+ESP,flags=re.DOTALL)
        find = pattern.findall(email)
        res += "<table>"
        for i in range(0,len(find)):
            find[i] = find[i].replace("<","&lt;")
            find[i] = find[i].replace(">","&gt;")
            res += "<tr><td>"+"&#8226; "+str(find[i])+"</td></tr>"
        res += "</table>"

    if "width=3D\"1\" height=3D\"1\"" in email:
        
        pattern = re.compile(SSP+"width=3D\"1\" height=3D\"1\""+ESP,flags=re.DOTALL)
        find = pattern.findall(email)
        res += "<table>"
        for i in range(0,len(find)):
            find[i] = find[i].replace("<","&lt;")
            find[i] = find[i].replace(">","&gt;")
            res += "<tr><td>"+"&#8226; "+str(find[i])+"</td></tr>"
        res += "</table>"

    if "height=3D\"1px\" width=3D\"1px\"" in email:

        pattern = re.compile(SSP+"height=3D\"1px\" width=3D\"1px\""+ESP,flags=re.DOTALL)
        find = pattern.findall(email)
        res += "<table>"
        for i in range(0,len(find)):
            find[i] = find[i].replace("<","&lt;")
            find[i] = find[i].replace(">","&gt;")
            res += "<tr><td>"+"&#8226; "+str(find[i])+"</td></tr>"
        res += "</table>"

    if "width=3D\"1px\" height=3D\"1px\"" in email:

        pattern = re.compile(SSP+"width=3D\"1px\" height=3D\"1px\""+ESP,flags=re.DOTALL)
        find = pattern.findall(email)
        res += "<table>"
        for i in range(0,len(find)):
            find[i] = find[i].replace("<","&lt;")
            find[i] = find[i].replace(">","&gt;")
            res += "<tr><td>"+"&#8226; "+str(find[i])+"</td></tr>"
        res += "</table>"

    if "width=0 height=0" in email:
        
        pattern = re.compile(SSP+"width=0 height=0"+ESP,flags=re.DOTALL)
        find = pattern.findall(email)
        res += "<table>"
        for i in range(0,len(find)):
            find[i] = find[i].replace("<","&lt;")
            find[i] = find[i].replace(">","&gt;")
            res += "<tr><td>"+"&#8226; "+str(find[i])+"</td></tr>"
        res += "</table>"
    
    if "width='0' height='0'" in email:

        pattern = re.compile(SSP+"width=\'0\' height=\'0\'"+ESP,flags=re.DOTALL)
        find = pattern.findall(email)
        res += "<table>"
        for i in range(0,len(find)):
            find[i] = find[i].replace("<","&lt;")
            find[i] = find[i].replace(">","&gt;")
            res += "<tr><td>"+"&#8226; "+str(find[i])+"</td></tr>"
        res += "</table>"

    if "width=\"0\" height=\"0\"" in email:
        
        pattern = re.compile(SSP+"width=\"0\" height=\"0\""+ESP,flags=re.DOTALL)
        find = pattern.findall(email)
        res += "<table>"
        for i in range(0,len(find)):
            find[i] = find[i].replace("<","&lt;")
            find[i] = find[i].replace(">","&gt;")
            res += "<tr><td>"+"&#8226; "+str(find[i])+"</td></tr>"
        res += "</table>"

    if "width=\"0px\" height=\"0px\"" in email:

        pattern = re.compile(SSP+"width=\"0px\" height=\"0px\""+ESP,flags=re.DOTALL)
        find = pattern.findall(email)
        res += "<table>"
        for i in range(0,len(find)):
            find[i] = find[i].replace("<","&lt;")
            find[i] = find[i].replace(">","&gt;")
            res += "<tr><td>"+"&#8226; "+str(find[i])+"</td></tr>"
        res += "</table>"

    return res

