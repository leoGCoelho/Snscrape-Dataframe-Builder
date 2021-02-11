import os
import re
import sys
#import pymongo
'''try:
    import pymongo
except:
    print("Installing pymongo...")
    os.system("pip3 install pymongo")'''

def SetDBConfig(url, dbname):
    data = url + "\n" + dbname

    with open("ref_db.txt", "w") as f:
        f.write(data)
        f.close()

def GetDBConfig():
    data = []

    with open("ref_db.txt", "r") as f:
        lines = f.readlines()
        f.close()

    for line in lines:
        line = re.sub(r'\n',r'',line)
        data.append(line)

    return data

'''def Connect(data):
    try:
        cluster = pymongo.MongoClient(data[0])
        mydb = cluster[data[1]]
    except:
        print("Enable to connect to " + data[1] + "database in " + data[0])

    return mydb'''