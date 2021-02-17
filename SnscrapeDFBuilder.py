import os
import re
import sys
import snscrape_crawler as scrawler
import snscrape_db as db
import json

tweetdata = []
dbdata = []
input_list = False
log = False
finalprint = True
repeatcol = False
repeatdata = []

try:
    if "--help" in sys.argv:
        print(scrawler.HelpMsg())
        sys.exit()

    elif "--version" in sys.argv:
        print("SNSCRAPE DF Builder: 0.2.0\n")
        print("SNSCRAPE: 0.3.5.dev91+gfdc33d0\n")
        sys.exit()

    elif "--dbconfig" in sys.argv:
        id = sys.argv.index("--dbconfig")
        i=1
        clusterurl = ""
        while sys.argv[id] != ' ':
            clusterurl += sys.argv[id+1]
            id += 1
        dbname = sys.argv[id+1]
        db.SetDBConfig(clusterurl, dbname)
        dbdata = db.GetDBConfig()
        print("New database setted: " + str(dbdata))
        sys.exit()

    else:
        # Input
        if "-list" in sys.argv:
            id = sys.argv.index("-list")
            file_in = sys.argv[id+1]
            input_list = True
        elif "-hashtag" in sys.argv:
            id = sys.argv.index("-hashtag")
            if '#' not in sys.argv[id+1]:
                tweetdata.append("#" + sys.argv[id+1])
            else:
                tweetdata.append(sys.argv[id+1])
        elif "-user" in sys.argv:
            id = sys.argv.index("-user")
            if '@' not in sys.argv[id+1]:
                tweetdata.append("@" + sys.argv[id+1])
            else:
                tweetdata.append(sys.argv[id+1])
            input_kwrd = True
        elif "-keyword" in sys.argv:
            id = sys.argv.index("-keyword")
            tweetdata.append(sys.argv[id+1])
            input_kwrd = True         
        else:
            print("Invalid input type! Try 'list_src filename.txt' or 'src #hashtag'\n")
            sys.exit()

        # Export to database (mongodb)
        if "--dbexport" in sys.argv:
            conf = db.GetDBConfig()
            if conf.count == 0:
                print("First set database configurations with 'python SnscrapeDFBuilder.py --dbconfig CLUSTER_URL DATABASE_NAME'")
                sys.exit()
            #dbdata = db.Connect(conf)

        # Max limit
        if "--max-limit" in sys.argv:
            id = sys.argv.index("--max-limit")
            limit = int(sys.argv[id+1])
        else:
            limit = 100000

        # Output
        if "-o" in sys.argv:
            id = sys.argv.index("-o")
            file_out = sys.argv[id+1]
        else:
            file_out = ""

        # Since
        if "--since" in sys.argv:
            id = sys.argv.index("--since")
            since = sys.argv[id+1]
        else:
            since = ""

        # Until
        if "--until" in sys.argv:
            id = sys.argv.index("--until")
            until = sys.argv[id+1]
        else:
            until = ""

        #Repeat string for any input
        if "--repeat" in sys.argv:
            repeatcol = True
        else:
            repeatcol = False

        # Log
        if "--log" in sys.argv:
            log = True
        else:
            log = False


        # Show results
        if "--not-show" in sys.argv:
            finalprint = False
        else:
            finalprint = True


except:
    sys.exit()

#os.system("clear")

if repeatcol == True:
    repeatdata.append(input("Name of the special column: "))
    repeatdata.append(input("String that should be repeated: "))

if input_list == True:
    df = scrawler.Build_MultExtractions(file_in, limit, log, repeatdata)
else:
    tweetdata.append(since)
    tweetdata.append(until)
    df = scrawler.Build_SingleExtraction(tweetdata, limit, log, repeatdata)

print('\n')

if file_out != "":
    if ".json" in file_out:
        df.to_json(file_out)

    elif ".csv" in file_out:
        df.to_csv(file_out, sep=';')

    elif not("." in file_out):
        df.to_csv(file_out + ".csv", sep=';')

if finalprint:
    print(df)