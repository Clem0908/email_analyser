from flask import Flask
from flask import render_template
from flask import request
import base64 as base64Lib

import checkMailHeaders, checkSpecificMailHeaders, listLinks, checkSpyingPixel, checkBase64, senderIP

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
        resSP = ""
        resCMH = ""
        resCSMH = ""
        resB64 = ""
        resIP = ""
        resIP = senderIP.senderIP(email)
        resCMH = checkMailHeaders.checkMailHeaders(email)
        resCSMH = checkSpecificMailHeaders.checkSpecificMailHeaders(email)
        res = listLinks.listLinks(email)
        resSP = checkSpyingPixel.checkSpyingPixel(email)
        resB64 = checkBase64.checkBase64(email)
        
        if resB64 != "":

            page = render_template('analyse.html')+resIP+resCMH+resCSMH+res+resSP+"<p>Base64 encoding detected.<br>Please paste the encoded part to analyse into the <a href=\"http://127.0.0.1:5000/#Base64\">Base64</a> form.</p>"+resB64+"</body></html>"

        else:

            page = render_template('analyse.html')+resIP+resCMH+resCSMH+res+resSP+"</body></html>"


        return page


@app.route("/file", methods = ['POST'])
def file():

    if request.method == 'POST':

        file = request.files['eml']
        email = file.read()
        email = email.decode("utf-8")
        res = ""
        resSP = ""
        resCMH = ""
        resCSMH = ""
        resB64 = ""
        resIP = ""
        resIP = senderIP.senderIP(email)
        resCMH = checkMailHeaders.checkMailHeaders(email)
        resCSMH = checkSpecificMailHeaders.checkSpecificMailHeaders(email)
        res = listLinks.listLinks(email)
        resSP = checkSpyingPixel.checkSpyingPixel(email)
        resB64 = checkBase64.checkBase64(email)
        
        if resB64 != "":

            page = render_template('file.html')+resIP+resCMH+resCSMH+res+resSP+"<p>Base64 encoding detected.<br>Please paste the encoded part to analyse into the <a href=\"http://127.0.0.1:5000/#Base64\">Base64</a> form.</p>"+resB64+"</body></html>"

        else:

            page = render_template('file.html')+resIP+resCMH+resCSMH+res+resSP+"</body></html>"

        return page

@app.route("/base64", methods = ['POST'])
def base64():

    if request.method == 'POST':

        email = str(request.form.get('base64'))
        email = base64Lib.b64decode(email).decode('utf-8')
        resCT = ""
        resSP = ""
        resCT = listLinks.listLinks(email)
        resSP = checkSpyingPixel.checkSpyingPixel(email)       

        page = render_template('base64.html')+resCT+resSP+"</body></html>"

        return page
