# bot.py
import os
import discord
from dotenv import load_dotenv
from discord.ext import commands
from random import choice
from utils import *


load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

intents = discord.Intents.all()
client = discord.Client(intents=intents)


bot = commands.Bot(command_prefix='$')

kicking_users = []
channel = 'dota-content'


@client.event
async def on_ready():
    print(f'{client.user.name} has connected to Discord!')

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    isVoteInitiated = False
    
    if (isinstance(message.content, str)):
        await message.channel.send("'" + ''.join(choice((str.upper, str.lower))(c) for c in message.content) + "'" +  " - " +  message.author.name)
client.run(TOKEN)


