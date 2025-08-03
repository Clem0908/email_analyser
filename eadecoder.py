def utf8(string: str):
    
    if "=?UTF-8?Q?" in string:
        string = string.replace("=?UTF-8?Q?","")
        string = string.replace("_"," ")
        string = string.replace("=C3=A9","é")
        string = string[:string.find("=0D")]

    return string
