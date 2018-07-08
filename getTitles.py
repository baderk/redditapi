import praw
from collections import Counter

# Script
reddit = praw.Reddit(client_id='5QRK4vEHkC2uhw',
                     client_secret='TPkY8jF3L5gf1lH1mw-tIgXUZuY',
                     user_agent='my user agent',
                     username='Ambitious_Vegetable',
                     password='redditAPI_'
                    )



# so  i don't need to create a list and add the title to it. 
# I could just use the temp_title string and set it to be equal as the submission.title
analog = reddit.subreddit("analog")


keyword = input("Search: ")


def numberOfPosts(keyword):
	# subreddit
	hot_analog = analog.top()
	
	post_title = ""
	count = 0

	print ("----------USING HOT Analog----------")
	for submission in hot_analog:
		# postTitle.append(submission.title)
		post_title = submission.title
		if not submission.stickied:
			if keyword in post_title.lower():
				count += 1
	print ("The word appeared", count, "times.\n")

	# i dont actually need to print the list, but for now it is printed and formatted
# print ('\n'.join('{}: {}'.format(*k) for k in enumerate(postTitle)))
# print (postTitle)




def searchCameraAndFilm(keyword):
	post_title = ""
	#reset count
	count = 0
	print ("------------USING SEARCH------------")
	search_analog = analog.search(keyword, syntax='lucene', time_filter ='all')
	for i in search_analog:
		#post_title = i.title
		#if camera+film in post_title.lower():
		count += 1
		#print (i.title)
	print ("The word appeared", count, "times.")

#calling functions
numberOfPosts(keyword)

searchCameraAndFilm(keyword)