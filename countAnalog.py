import praw
import time
import json

import plotly
import plotly.plotly as py
import plotly.graph_objs as go

start_time = time.time()

reddit = praw.Reddit(client_id='5QRK4vEHkC2uhw',
                     client_secret='TPkY8jF3L5gf1lH1mw-tIgXUZuY',
                     user_agent='my user agent',
                     username='Ambitious_Vegetable',
                     password='redditAPI_'
                    )

plotly.tools.set_credentials_file(username='baderk', api_key='vZoYPBNCyyTiHBA3Pn9X')

#FIND A WAY TO GET ALL POSTS NOT ONLY HOT OR TOP

def countOccurence():
    words = {}

    print("------Counting Occurence------")
    analogSub_top = reddit.subreddit('analog').top(limit=1000)
    analogSub_hot = reddit.subreddit('analog').hot(limit=1000)
    analogSub_new = reddit.subreddit('analog').new(limit=1000)

    # analogSub = subreddit_name.search(keyword, syntax='lucene', time_filter ='all', limit=999)

    # Text file into the dictionary words{}
    file = open("cameras.txt", "r")
    for line in file:
        words[line.strip().lower()] = 0

    ## TOP ##
    for i in analogSub_top:
        postTitle = i.title.lower()
        for word in words:
            if word in postTitle:
                words[word] += 1
    xList_top = list(words.keys())
    yList_top = list(words.values())
    data_top = [go.Bar(
                x = xList_top,
                y = yList_top
        )]
    py.plot(data_top, filename='basic-bar')
    # jsonResponse = json.dumps(words, indent=2, sort_keys=True)
    # print(jsonResponse)

    #resetting values of each camera
    words = words.fromkeys(words, 0)

    ## HOT ##
    for i in analogSub_hot:
        postTitle = i.title.lower()
        for word in words:
            if word in postTitle:
                words[word] += 1
    xList_hot = list(words.keys())
    yList_hot = list(words.values())
    data_hot = [go.Bar(
                x = xList_hot,
                y = yList_hot
        )]
    py.plot(data_hot, filename='basic-bar')
    # jsonResponse = json.dumps(words, indent=2, sort_keys=True)
    # print(jsonResponse)


    #resetting values of each camera
    words = words.fromkeys(words, 0)

    ## NEW ##
    for i in analogSub_new:
        postTitle = i.title.lower()
        for word in words:
            if word in postTitle:
                words[word] += 1
    xList_new = list(words.keys())
    yList_new = list(words.values())
    data_new = [go.Bar(
                x = xList_new,
                y = yList_new
        )]
    py.plot(data_new, filename='basic-bar')



    print("\nTotal counted in Top: ", sum(yList_top[0:len(yList_top)]))
    print("\nTotal counted in Hot: ", sum(yList_hot[0:len(yList_hot)]))
    print("\nTotal counted in New: ", sum(yList_new[0:len(yList_new)]))

countOccurence()

print("--- %s seconds ---" % round(time.time() - start_time, 2))
        #print(postTitle)
    #
    #     if "Canon" in postTitle:
    #         canon += 1
    #     elif "Olympus" in postTitle:
    #         olympus += 1
    #     elif "Contax" in postTitle:
    #         contax += 1
    #     elif "Nikon" in postTitle:
    #         nikon += 1
    #     elif "yashica" in postTitle:
    #         yashica += 1
    #
    #
    # print("Canon: ", canon, "\nOlympus: ", olympus, "\nContax: ",
    #     contax, "\nNikon: ", nikon, "\nYashica: ", yashica)
