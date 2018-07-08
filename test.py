import urllib.request
from urllib.request import Request
import json
import praw
import requests 
from pprint import pprint 
import string

keyword = input("Search: ")

numtitle = 0
count = 0
url = "https://www.reddit.com/r/analog/top.json?sort=top&t=all&limit=100"
i = 0
for j in range(5):
    r = requests.get(url, headers={'User-agent': "orew"})
    data = r.json()
    for i in range((len(data["data"]["children"]))):
        title = (data['data']['children'][i]["data"]  ['title']).lower().translate(str.maketrans('', '', string.punctuation))
        if keyword in title.split():
            count += 1
       
        numtitle += 1
    url = "https://www.reddit.com/r/analog/top.json? sort=top&t=all&limit=100&after=" + data["data"]["after"]
    print(url)
print("The number of occurrences is:",(count))

print(numtitle)