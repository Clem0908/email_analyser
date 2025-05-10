from pickledb import PickleDB

def addIp(ip :str):

    db = PickleDB("./database/known_ips.db")
    if db.get(ip) != None:
        db.set(ip,db.get(ip)+1)
        db.save()
    else:
        db.set(ip,1)
        db.save()
    return

def isKnown(ip: str):

    res = ""
    db = PickleDB("./database/known_ips.db")
    
    if db.get(ip) != None:
        res += " | IP seen " + str(db.get(ip)) + " times before" 
        return res
    return res
