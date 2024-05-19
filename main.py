import discord
import re
import logging
import os

logger = logging.getLogger(__name__)
token = os.getenv("Discord_Token")
intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
  print('Bot is online')

@client.event
async def on_message(message):
  if message.author == client.user:
    return

  if re.search('twitter.com|x.com', message.content):
    messages = re.sub('twitter.com|x.com', 'vxtwitter.com', message.content)
    urls = re.findall(r'(https?://\S+)', messages)
    tweets = ["'{}'".format(url.split('?')[0]) for url in urls]
    await message.channel.send("\n".join(tweets))
    logger.info('Sent message')
    return

  else:
    return

client.run(token)
