import praw

reddit = praw.Reddit(client_id='mcS-MYyhJWPXgw',
                     client_secret='3Rsyye8Uj_QHWyJk66Na3nJ4LWs',
                     user_agent='my user agent')

print(reddit.read_only)

for submission in reddit.subreddit('analog').hot(limit=10):
	print(submission.title)