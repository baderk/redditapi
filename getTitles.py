import praw

reddit = praw.Reddit(client_id=' jqfZmo_jVWjklA',
                     client_secret='uHDoZT20IdvspiLymkQ7vjyS8C8',
                     username='Ambitious_Vegetable',
                     password='redditAPI_'
                     user_agent='my user agent')

print(reddit.read_only)

for submission in reddit.subreddit('analog').hot(limit=10):
	print(submission.title)
