import re

def preProcessing(email: str):

    if "Content-Transfer-Encoding: quoted-printable" in email:

        email = email.replace("=\r", "")
        email = email.replace("=3D\"", "=\"")
        
        return email

    else:

        return email    
