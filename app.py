import re
import os
from flask import Flask
from flask import render_template
from flask import request

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

    return res

def checkSpyingPixel(email: str):
    
    res = ""

    if "width=1 height=1" in email:
        
        res += "<p>Spying pixel found !<br></p>"
        pattern = re.compile("<img [a-zA-Z0-9./:?=\"_]* width=1 height=1>",flags=re.DOTALL)
        find = pattern.findall(email)
        res += "<table>"
        for i in range(0,len(find)):
            find[i] = find[i].replace("<","&lt;")
            find[i] = find[i].replace(">","&gt;")
            res += "<tr><td>"+"&#8226; "+str(find[i])+"</td></tr>"
        res += "</table>"
    
    if "width='1' height='1'" in email:

        res += "<p>Spying pixel found !<br></p>"       
        pattern = re.compile("<img [a-zA-Z0-9./:?=\"_]* width='1' height='1'>",flags=re.DOTALL)
        find = pattern.findall(email)
        res += "<table>"
        for i in range(0,len(find)):
            find[i] = find[i].replace("<","&lt;")
            find[i] = find[i].replace(">","&gt;")
            res += "<tr><td>"+"&#8226; "+str(find[i])+"</td></tr>"
        res += "</table>"

    if "width=\"1\" height=\"1\"" in email:

        res += "<p>Spying pixel found !<br></p>"
        pattern = re.compile("<img [a-zA-Z0-9./:?=\"_]* width=\"1\" height=\"1\">",flags=re.DOTALL)
        find = pattern.findall(email)
        res += "<table>"
        for i in range(0,len(find)):
            find[i] = find[i].replace("<","&lt;")
            find[i] = find[i].replace(">","&gt;")
            res += "<tr><td>"+"&#8226; "+str(find[i])+"</td></tr>"
        res += "</table>"

    if "width=\"1px\" height=\"1px\"" in email:

        res += "<p>Spying pixel found !<br></p>"
        pattern = re.compile("<img [a-zA-Z0-9./:?=\"_]* width=\"1px\" height=\"1px\">",flags=re.DOTALL)
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
        res = checkTrackers(email)
        res2 = checkSpyingPixel(email)
        page = render_template('analyse.html')+res+res2
        return page
