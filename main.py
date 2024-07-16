import re
import os

def checkTrackers(email: str):
   
    if "track=email" in email:
        print("\n-> Trackers found !")

    pattern = re.compile("https://[a-zA-Z0-9./?]*track=email",flags=re.DOTALL)
    res = pattern.findall(email)
    for i in range(0,len(res)):
        print("\t- "+str(res[i]))

    return

def checkSpyingPixel(email: str):
    
    if "width=1 height=1" in email:
        
        print("\n-> Spying pixel found !")
        pattern = re.compile("<img [a-zA-Z0-9./:?=\"_]* width=1 height=1>",flags=re.DOTALL)
        res = pattern.findall(email)
        for i in range(0,len(res)):
            print("\t- "+str(res[i]))
    
    if "width='1' height='1'" in email:
        
        print("\n-> Spying pixel found !")
        pattern = re.compile("<img [a-zA-Z0-9./:?=\"_]* width='1' height='1'>",flags=re.DOTALL)
        res = pattern.findall(email)
        for i in range(0,len(res)):
            print("\t- "+str(res[i]))

    if "width=\"1\" height=\"1\"" in email:
        
        print("\n-> Spying pixel found !")
        pattern = re.compile("<img [a-zA-Z0-9./:?=\"_]* width=\"1\" height=\"1\">",flags=re.DOTALL)
        res = pattern.findall(email)
        for i in range(0,len(res)):
            print("\t- "+str(res[i]))

    return

if __name__ == "__main__":

    if os.path.exists("./email.eml") is False:
        print("Please insert all the content of your email into './email.eml'")
        exit()

    f = open("./email.eml","r")
    email = f.read()
    f.close()
    checkTrackers(email)
    checkSpyingPixel(email)
