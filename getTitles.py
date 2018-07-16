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


subreddit_input = input("What subreddit do you want to search in?\n")

subreddit_name = reddit.subreddit(subreddit_input)

keyword = input("Search: ")


def numberOfPosts(keyword):
	# subreddit
	
	hot = subreddit_name.top()
	
	post_title = ""
	count = 0

	print ("----------USING HOT ----------")

	for submission in hot:
		# postTitle.append(submission.title)
		post_title = submission.title
		if not submission.stickied:
			if keyword in post_title.lower():
				count += 1
	print ("The word appeared", count, "times.\n")

	# i dont actually need to print the list, but for now it is printed and formatted

# print ('\n'.join('{}: {}'.format(*k) for k in enumerate(postTitle)))
# print (postTitle)


# so most likely this is the correct way to search in all the subreddit. But I think I am limited to search only 
# in the latest 1000 post. Try adding the results to a list and then count that list items instead. So I'd get 1000 after 100 until NULL and add them to the list.

def searchCameraAndFilm(keyword):
	post_title = ""
	#reset count
	count = 0
	print ("------------USING SEARCH------------")
	
	search_subreddit = subreddit_name.search(keyword, syntax='lucene', time_filter ='all')
	for i in search_subreddit:
		#post_title = i.title
		#if camera+film in post_title.lower():
		count += 1
		#print (i.title)
	print ("The word appeared", count, "times.")

#calling functions
numberOfPosts(keyword)

searchCameraAndFilm(keyword)