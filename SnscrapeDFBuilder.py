import os
import re
import sys
import snscrape_crawler as scrawler

tweetdata = []
input_list = False
log = False
finalprint = True

try:
    if "--help" in sys.argv:
        print(scrawler.HelpMsg())
        sys.exit()

    elif "--version" in sys.argv:
        print("SNSCRAPE DF Builder: 0.1.0\n")
        print("SNSCRAPE: 0.3.5.dev91+gfdc33d0\n")
        sys.exit()

    else:
        # Input
        if "-list" in sys.argv:
            id = sys.argv.index("-list")
            file_in = sys.argv[id+1]
            input_list = True
        elif "-hashtag" in sys.argv:
            id = sys.argv.index("-hashtag")
            tweetdata.append("#" + sys.argv[id+1])
        elif "-user" in sys.argv:
            id = sys.argv.index("-user")
            tweetdata.append("@" + sys.argv[id+1])
            input_kwrd = True
        elif "-keyword" in sys.argv:
            id = sys.argv.index("-keyword")
            tweetdata.append(sys.argv[id+1])
            input_kwrd = True         
        else:
            print("Invalid input type! Try 'list_src filename.txt' or 'src #hashtag'\n")
            sys.exit()

        # Max limit
        if "--max-limit" in sys.argv:
            id = sys.argv.index("--max-limit")
            limit = int(sys.argv[id+1])
        else:
            limit = 0

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

        # Until
        if "--log" in sys.argv:
            log = True
        else:
            log = False


        # Until
        if "--not-show" in sys.argv:
            finalprint = False
        else:
            finalprint = True


except:
    sys.exit()

#os.system("clear")

if input_list == True:
    df = scrawler.Build_MultExtractions(file_in, limit, log)
else:
    tweetdata.append(since)
    tweetdata.append(until)
    df = scrawler.Build_SingleExtraction(tweetdata, limit, log)

print('\n')

if file_out != "":
    try:
        file_out = re.sub(r'.csv', r'', file_out)
    except:
        x=0
    #df.to_json(file_out + ".csv", orient="index")
    df.to_csv(file_out + ".csv", sep=';')

if finalprint:
    print(df)