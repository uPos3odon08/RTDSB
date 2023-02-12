import discord
import praw
import time
from datetime import datetime
from config import *

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('!subs'):
        await message.channel.send(subs)

client.run(bottoken)

while True:
    reddit = praw.Reddit(
        client_id=redditclid,
        client_secret=redditclscrt,
        user_agent="subreddit member count scraper 1.6 by u/Pos3odon08")

    now = datetime.now()
    subs = reddit.subreddit(sub).subscribers
