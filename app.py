import re
import os
from flask import Flask
from flask import render_template
from flask import request

def checkMailHeaders(email: str):

    res = ""
    if "spf\\=pass" not in email:
        res += "<p>SPF: [!]</p>"
    if "dkim\\=pass" not in email:
        res += "<p>DKIM: [!]</p>"
    if "dmarc\\=pass" not in email:
        res += "<p>DMARC: [!]</p>"

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
        resCMH = checkMailHeaders(email)
        res = checkTrackers(email)
        res2 = checkSpyingPixel(email)
        page = render_template('analyse.html')+resCMH+res+res2
        return page
