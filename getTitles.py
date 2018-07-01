import praw
from collections import Counter

# Script
reddit = praw.Reddit(client_id='5QRK4vEHkC2uhw',
                     client_secret='TPkY8jF3L5gf1lH1mw-tIgXUZuY',
                     user_agent='my user agent',
                     username='Ambitious_Vegetable',
                     password='redditAPI_'
                    )



camera_name = input("Enter camera name: ")

temp_title = ""
count = 0
# so  i don't need to create a list and add the title to it. 
# I could just use the temp_title string and set it to be equal as the submission.title
for submission in reddit.subreddit('analog').hot(limit=26):
	# postTitle.append(submission.title)
	temp_title = submission.title
	if camera_name in temp_title.lower():
		count += 1
print(count)

	# i dont actually need to print the list, but for now it is printed and formatted
# print ('\n'.join('{}: {}'.format(*k) for k in enumerate(postTitle)))
# print (postTitle)



