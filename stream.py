import praw

# Script
reddit = praw.Reddit(client_id='5QRK4vEHkC2uhw',
                     client_secret='TPkY8jF3L5gf1lH1mw-tIgXUZuY',
                     user_agent='my user agent',
                     username='Ambitious_Vegetable',
                     password='redditAPI_'
                    )

subreddit = reddit.subreddit('news')

for submission in subreddit.stream.submissions():
	try:
	
		
		print(submission.title)

	except praw.exceptions.PRAWException as e:
		pass