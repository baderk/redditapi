import praw
import time
import json

import plotly
from plotly import tools
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

def countOccurence():
    words = {}

    print("------Counting Occurence------")
    analogSub_top = reddit.subreddit('analog').top(limit=1000)
    analogSub_hot = reddit.subreddit('analog').hot(limit=1000)
    analogSub_new = reddit.subreddit('analog').new(limit=1000)

    # analogSub = subreddit_name.search(keyword, syntax='lucene', time_filter ='all', limit=999)

    # Text file into the dictionary words{}
    file = open("cameras2.txt", "r")
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


    # py.plot(data_hot, filename='basic-bar')
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



    print("\nTotal counted in Top: ", sum(yList_top[0:len(yList_top)]))
    print("Total counted in Hot: ", sum(yList_hot[0:len(yList_hot)]))
    print("Total counted in New: ", sum(yList_new[0:len(yList_new)]), "\n")
    # print(xList_top)
# width=3840, height=2160,
    data_top = go.Bar(x = xList_top, y = yList_top, name='TOP', marker=dict(color='rgb(246, 114, 128)'))
    data_hot = go.Bar(x = xList_hot, y = yList_hot, name='HOT', marker=dict(color='rgb(192, 108, 132)'))
    data_new = go.Bar(x = xList_new, y = yList_new, name='NEW', marker=dict(color='rgb(108, 91, 123)'))

# width=3840, height=2160,
    data = [data_top, data_hot, data_new]
    layout = go.Layout(
        title='Analog',
        width=1280, height=1080,
        font=dict(family='Courier New, monospace', size=18, color='#f5f6fa'), 
        barmode='group', 
        xaxis=dict(titlefont=(dict(size=10))),
        yaxis=dict(
            title='Nom. of Occurence',
        ),
        paper_bgcolor='#353b48',
        plot_bgcolor='#353b48',
        legend=dict(
            font=dict(
                color='#f5f6fa'
            )
        )
    )

    # fig = tools.make_subplots(rows=1, cols=3, subplot_titles=('Top', 'Hot', 'New'))
    fig = go.Figure(data=data, layout=layout)
    # this appends the graphs to the panel
    # fig.append_trace(data_top, 1, 1)
    # fig.append_trace(data_hot, 1, 2)
    # fig.append_trace(data_new, 1, 3)


    py.plot(fig, filename='Analog')

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
