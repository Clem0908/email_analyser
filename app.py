import re
import os
from flask import Flask
from flask import render_template
from flask import request

def checkMailHeaders(email: str):

    res = ""
    pattern = re.compile(".*spf=(fail|none|softfail|temperror|permerror).*",flags=re.DOTALL)
    find = pattern.findall(email)
    if len(find) > 0:
        res += "<p>SPF: [!]</p>"
    else:
        res += "<p>SPF: [OK]</p>"

    pattern = re.compile(".*dkim=(fail|none|softfail|temperror|permerror).*",flags=re.DOTALL)
    find = pattern.findall(email)
    if len(find) > 0:
        res += "<p>DKIM: [!]</p>"
    else:
        res += "<p>DKIM: [OK]</p>"
    
    pattern = re.compile(".*dmarc=(fail|none|softfail|temperror|permerror).*",flags=re.DOTALL)
    find = pattern.findall(email)
    if len(find) > 0:
        res += "<p>DMARC: [!]</p>"
    else:
        res += "<p>DMARC: [OK]</p>"

    return res

def displayMSSCLScore(email: str):
    
    res = ""
    res += "<p>Microsoft anti-spam score (0 low - 9 high): "

    pattern = re.compile("X-MS-Exchange-Organization-SCL: [0-9]",flags=re.DOTALL)
    find = pattern.findall(email)
    find[0] = find[0].replace("X-MS-Exchange-Organization-SCL: ", "")
    res += "<b>"+str(find[0])+"</b></p>"

    return res

def checkTrackers(email: str):
    
    res = ""
   
    if "track=email" in email:
        res += "<p>Trackers found !<br></p>"

    pattern = re.compile("https?://[a-zA-Z0-9./?]*track=email",flags=re.DOTALL)
    find = pattern.findall(email)
    res += "<table>"
    for i in range(0,len(find)):
        find[i] = find[i].replace("<","&lt;")
        find[i] = find[i].replace(">","&gt;")
        res += "<tr><td>"+"&#8226; "+str(find[i])+"</td></tr>"
    res += "</table>"

    if "/track/" in email:
        res += "<p>Trackers found !<br></p>"

    pattern = re.compile("https?://[a-zA-Z0-9./?]*track[a-zA-Z0-9./?]*",flags=re.DOTALL)
    find = pattern.findall(email)
    res += "<table>"
    for i in range(0,len(find)):
        find[i] = find[i].replace("<","&lt;")
        find[i] = find[i].replace(">","&gt;")
        res += "<tr><td>"+"&#8226; "+str(find[i])+"</td></tr>"
    res += "</table>"

    return res

def checkSpyingPixel(email: str):
    
    res = ""

    if "width=1 height=1" in email:
        
        res += "<p>Spying pixel found !<br></p>"
        pattern = re.compile("<img [a-zA-Z0-9./:;?&=\"_\\- ]* width=1 height=1[a-zA-Z0-9./:;?&=\"_\\- ]*>",flags=re.DOTALL)
        find = pattern.findall(email)
        res += "<table>"
        for i in range(0,len(find)):
            find[i] = find[i].replace("<","&lt;")
            find[i] = find[i].replace(">","&gt;")
            res += "<tr><td>"+"&#8226; "+str(find[i])+"</td></tr>"
        res += "</table>"
    
    if "width='1' height='1'" in email:

        res += "<p>Spying pixel found !<br></p>"       
        pattern = re.compile("<img [a-zA-Z0-9./:;?&=\"_\\- ]* width=\'1\' height=\'1\'[a-zA-Z0-9./:;?&=\"_\\- ]*>",flags=re.DOTALL)
        find = pattern.findall(email)
        res += "<table>"
        for i in range(0,len(find)):
            find[i] = find[i].replace("<","&lt;")
            find[i] = find[i].replace(">","&gt;")
            res += "<tr><td>"+"&#8226; "+str(find[i])+"</td></tr>"
        res += "</table>"

    if "width=\"1\" height=\"1\"" in email:

        res += "<p>Spying pixel found !<br></p>"
        pattern = re.compile("<img [a-zA-Z0-9./:;?&=\"_\\- ]* width=\"1\" height=\"1\"[a-zA-Z0-9./:;?&=\"_\\- ]*>",flags=re.DOTALL)
        find = pattern.findall(email)
        res += "<table>"
        for i in range(0,len(find)):
            find[i] = find[i].replace("<","&lt;")
            find[i] = find[i].replace(">","&gt;")
            res += "<tr><td>"+"&#8226; "+str(find[i])+"</td></tr>"
        res += "</table>"

    if "width=\"1px\" height=\"1px\"" in email:

        res += "<p>Spying pixel found !<br></p>"
        pattern = re.compile("<img [a-zA-Z0-9./:;?&=\"_\\- ]* width=\"1px\" height=\"1px\"[a-zA-Z0-9./:;?&=\"_\\- ]*>",flags=re.DOTALL)
        find = pattern.findall(email)
        res += "<table>"
        for i in range(0,len(find)):
            find[i] = find[i].replace("<","&lt;")
            find[i] = find[i].replace(">","&gt;")
            res += "<tr><td>"+"&#8226; "+str(find[i])+"</td></tr>"
        res += "</table>"

    if "width=\"1px\" height=\"1px;\"" in email:

        res += "<p>Spying pixel found !<br></p>"
        pattern = re.compile("<img width=\"1px\" height=\"1px;\"[a-zA-Z0-9./:;?&=\"_\\- ]*>",flags=re.DOTALL)
        find = pattern.findall(email)
        res += "<table>"
        for i in range(0,len(find)):
            find[i] = find[i].replace("<","&lt;")
            find[i] = find[i].replace(">","&gt;")
            res += "<tr><td>"+"&#8226; "+str(find[i])+"</td></tr>"
        res += "</table>"

    if "width: 1px; height: 1px;" in email:

        res += "<p>Spying pixel found !<br></p>"
        pattern = re.compile("<img [a-zA-Z0-9./:;?&=\"_\\- ]*width: 1px; height: 1px;[a-zA-Z0-9./:;?&=\"_\\- ]*>",flags=re.DOTALL)
        find = pattern.findall(email)
        res += "<table>"
        for i in range(0,len(find)):
            find[i] = find[i].replace("<","&lt;")
            find[i] = find[i].replace(">","&gt;")
            res += "<tr><td>"+"&#8226; "+str(find[i])+"</td></tr>"
        res += "</table>"


    if "height=3D\"1\" width=3D\"1\"" in email:

        res += "<p>Spying pixel found !<br></p>"
        pattern = re.compile("<img [a-zA-Z0-9./:;?&=\"_\\- ]* height=3D\"1\" width=3D\"1\"[a-zA-Z0-9./:;&?=\"_\\- ]*>",flags=re.DOTALL)
        find = pattern.findall(email)
        res += "<table>"
        for i in range(0,len(find)):
            find[i] = find[i].replace("<","&lt;")
            find[i] = find[i].replace(">","&gt;")
            res += "<tr><td>"+"&#8226; "+str(find[i])+"</td></tr>"
        res += "</table>"

    if "width=0 height=0" in email:
        
        res += "<p>Spying pixel found !<br></p>"
        pattern = re.compile("<img [a-zA-Z0-9./:;?&=\"_\\- ]* width=0 height=0[a-zA-Z0-9./:;?&=\"_\\- ]*>",flags=re.DOTALL)
        find = pattern.findall(email)
        res += "<table>"
        for i in range(0,len(find)):
            find[i] = find[i].replace("<","&lt;")
            find[i] = find[i].replace(">","&gt;")
            res += "<tr><td>"+"&#8226; "+str(find[i])+"</td></tr>"
        res += "</table>"
    
    if "width='0' height='0'" in email:

        res += "<p>Spying pixel found !<br></p>"       
        pattern = re.compile("<img [a-zA-Z0-9./:;?&=\"_\\- ]* width=\'0\' height=\'0\'[a-zA-Z0-9./:;?&=\"_\\- ]*>",flags=re.DOTALL)
        find = pattern.findall(email)
        res += "<table>"
        for i in range(0,len(find)):
            find[i] = find[i].replace("<","&lt;")
            find[i] = find[i].replace(">","&gt;")
            res += "<tr><td>"+"&#8226; "+str(find[i])+"</td></tr>"
        res += "</table>"

    if "width=\"0\" height=\"0\"" in email:
        
        res += "<p>Spying pixel found !<br></p>"
        pattern = re.compile("<img [a-zA-Z0-9./:;?&=\"_\\- ]* width=\"0\" height=\"0\"[a-zA-Z0-9./:;?&=\"_\\- ]*>",flags=re.DOTALL)
        find = pattern.findall(email)
        res += "<table>"
        for i in range(0,len(find)):
            find[i] = find[i].replace("<","&lt;")
            find[i] = find[i].replace(">","&gt;")
            res += "<tr><td>"+"&#8226; "+str(find[i])+"</td></tr>"
        res += "</table>"

    if "width=\"0px\" height=\"0px\"" in email:

        res += "<p>Spying pixel found !<br></p>"
        pattern = re.compile("<img [a-zA-Z0-9./:;?&=\"_\\- ]* width=\"0px\" height=\"0px\"[a-zA-Z0-9./:;?&=\"_\\- ]*>",flags=re.DOTALL)
        find = pattern.findall(email)
        res += "<table>"
        for i in range(0,len(find)):
            find[i] = find[i].replace("<","&lt;")
            find[i] = find[i].replace(">","&gt;")
            res += "<tr><td>"+"&#8226; "+str(find[i])+"</td></tr>"
        res += "</table>"

    return res

app = Flask(__name__)

@app.route("/", methods = ['GET'])
def root():

    if request.method == 'GET':
        return render_template('index.html')

@app.route("/analyse", methods = ['POST'])
def analyse():

     if request.method == 'POST':
        
        email = str(request.form.get('email'))
        res = ""
        res2 = ""
        resCMH = ""
        resMSSCL = ""
        resCMH = checkMailHeaders(email)
        resMSSCL = displayMSSCLScore(email)
        res = checkTrackers(email)
        res2 = checkSpyingPixel(email)
        page = render_template('analyse.html')+resCMH+resMSSCL+res+res2
        return page
