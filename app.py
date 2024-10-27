from flask import Flask
from flask import render_template
from flask import request

import displayMSSCLScore, checkMailHeaders, checkTrackers, checkSpyingPixel, checkBase64, senderIP

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
        resMSSCL = ""
        resB64 = ""
        resIP = ""
        resIP = senderIP.senderIP(email)
        resCMH = checkMailHeaders.checkMailHeaders(email)
        resMSSCL = displayMSSCLScore.displayMSSCLScore(email)
        res = checkTrackers.checkTrackers(email)
        resSP = checkSpyingPixel.checkSpyingPixel(email)
        resB64 = checkBase64.checkBase64(email)
        page = render_template('analyse.html')+resIP+resCMH+resMSSCL+res+resSP+resB64
        return page
