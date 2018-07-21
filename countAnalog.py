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

# so  i don't need to create a list and add the title to it.
# I could just use the temp_title string and set it to be equal as the submission.title
#i dont actually need to print the list, but for now it is printed and formatted
# print ('\n'.join('{}: {}'.format(*k) for k in enumerate(postTitle)))
# print (postTitle)

# so most likely this is the correct way to search in all the subreddit. But I think I am limited to search only
# in the latest 1000 post. Try adding the results to a list and then count that list items instead. So I'd get 1000 after 100 until NULL and add them to the list.

#FIND A WAY TO GET ALL POSTS NOT ONLY HOT OR TOP

def countOccurence():
    words = {}

    print("------Counting Occurence------")

    analogSub = reddit.subreddit('analog').top(limit=999)

    # Text file into the dictionary words{}
    file = open("cameras.txt", "r")
    for line in file:
        words[line.strip()] = 0



    for i in analogSub:
        postTitle = i.title
        for word in words:
            if word in postTitle:
                words[word] += 1

    jsonResponse = json.dumps(words, indent=2, sort_keys=True)


    xList = list(words.keys())
    yList = list(words.values())

    data = [go.Bar(

                x = xList,
                y = yList
        )]

    py.plot(data, filename='basic-bar')

    print(jsonResponse)

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
