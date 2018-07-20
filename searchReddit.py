import praw
from collections import Counter

#FIND A WAY TO GET ALL POSTS NOT ONLY HOT OR TOP


# Script
reddit = praw.Reddit(client_id='5QRK4vEHkC2uhw',
                     client_secret='TPkY8jF3L5gf1lH1mw-tIgXUZuY',
                     user_agent='my user agent',
                     username='Ambitious_Vegetable',
                     password='redditAPI_'
                    )
subreddit_input = input("What subreddit do you want to search in?\n")

subreddit_name = reddit.subreddit(subreddit_input)

keyword = input("Search: ")


def numberOfPosts(keyword):

    hot = subreddit_name.top(limit=999)

    post_title = ""
    count = 0

    print ("----------USING HOT/TOP ----------")

    for submission in hot:
        # postTitle.append(submission.title)
        post_title = submission.title
        if not submission.stickied:
            if keyword in post_title.lower():
                count += 1
    print ("The word appeared", count, "times.\n")


def searchCameraAndFilm(keyword):
    post_title = ""

    #reset count
    count = 0

    print ("------------USING SEARCH------------")

    search_subreddit = subreddit_name.search(keyword, syntax='lucene', time_filter ='all', limit=999)
    for i in search_subreddit:
        #post_title = i.title
        #if camera+film in post_title.lower():
        count += 1
        #print (i.title)
    print ("The word appeared", count, "times.")


numberOfPosts(keyword)
searchCameraAndFilm(keyword)
