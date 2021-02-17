import pandas
import json
import sys

def cleandata(data):
    for jsonf in data:
        #jsonf["texto"] = ""
        jsonf.pop("user", None)
        jsonf.pop("outlinks", None)
        jsonf.pop("tcooutlinks", None)
        jsonf.pop("replyCount", None)
        jsonf.pop("retweetCount", None)
        jsonf.pop("likeCount", None)
        jsonf.pop("quoteCount", None)
        jsonf.pop("conversationId", None)
        jsonf.pop("likeCount", None)
        jsonf.pop("source", None)
        jsonf.pop("sourceUrl", None)
        jsonf.pop("media", None)
        jsonf.pop("retweetedTweet", None)
        jsonf.pop("quotedTweet", None)
        jsonf.pop("likeCount", None)
        jsonf.pop("mentionedUsers", None)

    return data


data1 = [json.loads(line) for line in open(sys.argv[1], 'r')]
data1 = cleandata(data1)
data2 = [json.loads(line) for line in open(sys.argv[2], 'r')]
data2 = cleandata(data2)

data = data1 + data2
json.dump(data, sys.argv[3])

print(len(data), len(data1), len(data2))

