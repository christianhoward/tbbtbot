import praw

user_agent = ("Sheldon Bot 0.1")

r = praw.Reddit(user_agent=user_agent)

subreddit = r.get_subreddit("bigbangtheory")

for submission in subreddit.get_hot(limit=5):
    print("Title: ", submission.title)
    print("Text: ", submission.selftext)
    print("Score: ", submission.score)
    print("---------------------------\n")