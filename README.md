# RTDSB
Reddit To Discord Server Bot is a program that pulls information from Reddit's PRAW API and posts it in a Discord server

How to set up/use

1. The first step would be going over to the [Discord developer portal](https://discord.com/developers/applications) 
2. Then creating a new application with whatever name you want your bot to have
3. Then go over to the "bot" tab on the left and hit "add bot" 
4. After that you should head over to [Reddit](https://old.reddit.com/prefs/apps) and make an app with the same name as the Discord app
5. Then as redirect uri enter "http://localhost:8080" 
6. and if you haven't done it already make sure to clone/download this project
7. and in config.py fill in the requested information and then run the script

When you are done with the above stuff you are ready to invite the bot to your server by editing this link and pasting it into your browser


https://discordapp.com/oauth2/authorize?client_id=<YOUR CLIENT ID>&scope=bot&permissions=274877910016
