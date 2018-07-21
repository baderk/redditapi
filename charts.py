import praw
import time
import json

import plotly
import plotly.plotly as py
import plotly.graph_objs as go

plotly.tools.set_credentials_file(username='baderk', api_key='vZoYPBNCyyTiHBA3Pn9X')

words = {"bader": 4, "alex": 33, "john": 12}
x2 = list(words.keys())
y2 = list(words.values())

# for key in words.items():
#     x2.append(key)
#     for value in words.items():
#         y2.append(value)
#     # y2 = [value]



data = [go.Bar(
            # x=['giraffes', 'orangutans', 'monkeys'],
            # y=[20, 14, 23]
            x = x2,
            y = y2
    )]

py.plot(data, filename='basic-bar')
# # Script
# reddit = praw.Reddit(client_id='5QRK4vEHkC2uhw',
#                      client_secret='TPkY8jF3L5gf1lH1mw-tIgXUZuY',
#                      user_agent='my user agent',
#                      username='Ambitious_Vegetable',
#                      password='redditAPI_'
#                     )
