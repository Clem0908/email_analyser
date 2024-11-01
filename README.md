# Email analyser 
This project tries to analyse RAW/source content of an email.
# Features
- Display sender IP address
- Display results of email verification anti-spam mechanisms (SPF, DKIM, DMARC)
- Checks whether trackings links or spying pixels are present
- Supports base64 encoded emails
# Prerequisites for installation
- Internet connection
- Python
- Pip
- sh for installation scripts
    - If you do not have sh, the commands to install the requirements are given in the section _Installation commands_
# Installation commands
- In a terminal:
- `python -m venv ./venv`
- `./venv/bin/pip install -r requirements.txt`
# Running Email analyser
- If you have sh then:
    - `chmod +x ./run.sh`
    - `./run.sh`
- If you do not have sh then:
    - `./venv/bin/python -m flask run`
- Email analyser is available via a Web interface at this address: `http://127.0.0.1:5000/`
