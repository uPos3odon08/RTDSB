import praw
import time
from datetime import datetime
from config import sub
from config import redditclid
from config import redditclscrt

reddit = praw.Reddit(
    client_id=redditclid,
    client_secret=redditclscrt,
    user_agent="subreddit member amount scraper 1.5 by u/Pos3odon08",
)

subreddit = reddit.subreddit(sub)



print("Author = u/Pos3odon08")


now = datetime.now()
subs = reddit.subreddit(sub).subscribers

