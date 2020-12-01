import pandas as pd
import snscrape.modules.twitter as sntwitter
import time
import re


def formatTime(val_time):
    hours, rem = divmod(val_time, 3600)
    minutes, seconds = divmod(rem, 60)
    return [hours, minutes, seconds]



def Build_MultExtractions(file_in, max_lim, log):
    username = []
    date = []
    lang = []
    text = []
    likes = []
    #location = []
    sharedata = []
    url = []
    media = []

    start_time = time.time()
    with open(file_in, 'r') as f:
        lines = f.readlines()
    f.close()

    for line in lines:
        start_hash_time = time.time()
        line = re.sub(r'[ˆ\n]', r'', line)
        tweetdata = line.split(';')

        if log:
            print( "Extracting " + tweetdata[0] + " in " + str(tweetdata[1]) + " >> " + str(tweetdata[2]) + " ...")
        results = 0

        # Extract data
        for i,tweet in enumerate(sntwitter.TwitterSearchScraper(tweetdata[0] + " since:" + tweetdata[1] + " until:" + tweetdata[2]).get_items()):

            if (i > max_lim) and (max_lim > 0):   # Max limit of results
                if log:
                    print("Maximum Limit of Extraction! Extraction stopped!")
                break
            
            if (text.count(tweet.content) == 0) or (username.count(tweet.user.username) == 0): # Check for duplicates
                username.append(tweet.user.username)
                date.append(tweet.date)
                lang.append(tweet.lang)
                text.append(tweet.content)
                likes.append(tweet.likeCount)
                #location.append(tweet.location)
                sharedata.append("likes=" + str(tweet.likeCount) + ";retweets=" + str(tweet.retweetCount) + ";replies=" + str(tweet.replyCount) + ";quotes=" + str(tweet.quoteCount))
                url.append(tweet.url)
                
                if tweet.media:
                    mediaurl = []
                    for medium in tweet.media:
                        if medium.type == "photo":
                            mediaurl.append(medium.fullUrl)
                        elif medium.type == "video":
                            for v in medium.variants:
                                mediaurl.append(v.url.replace("?tag=13", "").replace("?tag=10", ""))
                    media.append(mediaurl)
                else:
                    media.append([])
                
                results = i

        end_hash_time = formatTime(time.time() - start_hash_time)
        if log:
            print(str(results), tweetdata[0], "tweet(s) extracted in {:0>2}:{:0>2}:{:05.2f}".format(int(end_hash_time[0]), int(end_hash_time[1]), end_hash_time[2]), "\n")

    end_time = formatTime(time.time() - start_time)
    if log:
        print("\nAll data extracted: ", str(len(username)), "Tweets in {:0>2}:{:0>2}:{:05.2f}".format(int(end_time[0]), int(end_time[1]), end_time[2]), "\n\n")

    # Build Dataframe
    s0 = pd.Series(username, name= 'username')
    s1 = pd.Series(date, name= 'date')
    s2 = pd.Series(lang, name= 'lang')
    s3 = pd.Series(text, name= 'text')
    s4 = pd.Series(likes, name= 'likes')
    s5 = pd.Series(sharedata, name= 'share data')
    #s6 = pd.Series(location, name= 'location')
    s7 = pd.Series(url, name= 'url')
    s8 = pd.Series(media, name= 'media')

    df = pd.concat([s0,s1,s2,s3,s4,s5,s7,s8], axis=1)
    return df



def Build_SingleExtraction(tweetdata, max_lim):
    username = []
    date = []
    lang = []
    text = []
    likes = []
    #location = []
    sharedata = []
    url = []
    media = []

    start_time = time.time()
    if log:
        msgPrint = "Extracting " + tweetdata[0]
        msgCmd = tweetdata[0]
        if tweetdata[1] != "":
            msgPrint += " in " + str(tweetdata[1])
            msgCmd += " since:" + tweetdata[1]

        if tweetdata[2] != "":
            msgPrint += " >> " + str(tweetdata[2])
            msgCmd += " until:" + tweetdata[2]

        print(msgPrint + " ...")
    results = 0

    # Extract data
    for i,tweet in enumerate(sntwitter.TwitterSearchScraper(msgCmd).get_items()):

        if (i > max_lim) and (max_lim > 0):   # Max limit of results
            if log:
                print("Maximum Limit of Extraction! Extraction stopped!")
            break
        
        if (text.count(tweet.content) == 0) or (username.count(tweet.user.username) == 0): # Check for duplicates
            username.append(tweet.user.username)
            date.append(tweet.date)
            lang.append(tweet.lang)
            text.append(tweet.content)
            likes.append(tweet.likeCount)
            #location.append(tweet.location)
            sharedata.append("likes=" + str(tweet.likeCount) + ";retweets=" + str(tweet.retweetCount) + ";replies=" + str(tweet.replyCount) + ";quotes=" + str(tweet.quoteCount))
            url.append(tweet.url)
            
            if tweet.media:
                mediaurl = []
                for medium in tweet.media:
                    if medium.type == "photo":
                        mediaurl.append(medium.fullUrl)
                    elif medium.type == "video":
                        for v in medium.variants:
                            mediaurl.append(v.url.replace("?tag=13", "").replace("?tag=10", ""))
                media.append(mediaurl)
            else:
                media.append([])
            
            results = i

    end_time = formatTime(time.time() - start_time)
    if log:
        print(str(results), tweetdata[0], "tweet(s) extracted in {:0>2}:{:0>2}:{:05.2f}".format(int(end_time[0]), int(end_time[1]), end_time[2]), "\n")


    # Build Dataframe
    s0 = pd.Series(username, name= 'username')
    s1 = pd.Series(date, name= 'date')
    s2 = pd.Series(lang, name= 'lang')
    s3 = pd.Series(text, name= 'text')
    s4 = pd.Series(likes, name= 'likes')
    s5 = pd.Series(sharedata, name= 'share data')
    #s6 = pd.Series(location, name= 'location')
    s7 = pd.Series(url, name= 'url')
    s8 = pd.Series(media, name= 'media')

    df = pd.concat([s0,s1,s2,s3,s4,s5,s7,s8], axis=1)
    return df


def HelpMsg():
    msg = "\npython SnscrapeDFBuilder [-src KEYWORD] [-list FILE.txt] \n[--help] [--v] [--max-limit N ] [--since DATETIME] [--until DATETIME] [-o FILE]\n"

    msg += "\nObrigatory Arguments:\n"
    msg += "\t-hashtag KEYWORD\tGet data by hashtag\n"
    msg += "\t-user KEYWORD\t\tGet data by username\n"
    msg += "\t-keyword KEYWORD\tGet data by keyword\n"
    msg += "\t-list FILE.txt\t\tText file with all target keywords\n"

    msg += "\nOptional Arguments:\n"
    msg += "\t-o FILE\t\t\tSet file name where the results will be storage (default format: .csv)\n"
    msg += "\t--max-limit N\t\tOnly return the first N results\n"
    msg += "\t--since DATETIME\tOnly return results newer than DATETIME\n"
    msg += "\t--until DATETIME\tOnly return results older than DATETIME\n"
    msg += "\t--help\t\t\tShow help message and exit\n"
    msg += "\t--version\t\tShow this script's version and exit\n"
    msg += "\t--log\t\tShow progress log (collected data and timestamps)\n"
    msg += "\t--not-show\t\tDo not show result at the end of execution\n"



    msg += "\nSample:\n\tpython SnscrapeDFBuilder -hashtag newyork --since 2019-04-10 --until 2020-01-26\n"
    msg += "\tpython SnscrapeDFBuilder -list example.txt -o /res/output\n"

    return msg