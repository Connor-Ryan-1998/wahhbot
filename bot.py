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

    # if (message.channel == 'mouse-verification' and isinstance(message.content, str)):
    #     print('sukk')
    #     for guild in client.guilds:
    #         for member in guild.members:
    #             if (member.name == message.author.name):
    #                 await member.move_to(None)   
    #                 await message.channel.send('fuck you dick boy thats not a mouse')

    isVoteInitiated = False
    
    if (isinstance(message.content, str)):
        await message.channel.send("'" + ''.join(choice((str.upper, str.lower))(c) for c in message.content) + "'" +  " - " +  message.author.name)
        # if (message.author.name == 'lachyme'):
        #     await message.channel.send('nah fuck u gay yellow man')
        #     for guild in client.guilds:
        #         for member in guild.members:
        #             if (member.name == message.author.name):
        #                 await member.move_to(None)  
        # else:
        #     isVoteInitiated = True
        #     await message.channel.send('Vote initiated 1/2')

    
    # if message.content == 'please' and isVoteInitiated:
    #     await message.channel.send('whoops, suck to suck mini dicklin 2/2')
    #     for guild in client.guilds:
    #         for member in guild.members:
    #             if (member.name == 'Reanu Keeves'):
    #                 await member.move_to(None)    

# @bot.command()
# async def kick(ctx, target_user:discord.User):

#     # await require_lower_permissions(ctx, target_user, bot)

#     if target_user in kicking_users:
#         await ctx.send("There is already a kick vote on `{}`!".format(target_user))
#         return 

#     # add to kicking_users
#     kicking_users.append(target_user)

#     vote_passed = await take_vote(ctx, "Kick `{}`?\n⚠ NOTE: Can't kick users with an equal or higher role.".format(target_user), KICK_VOTE_TIME, MIN_KICK_VOTERS)

#     if vote_passed:
#         try:
#             await ctx.guild.kick(target_user)
#             await ctx.send("👢 Kicked `{}`.".format(target_user))
#         except discord.ext.commands.errors.CommandInvokeError:
#             await error_admin_targeted(ctx)

#     kicking_users.remove(target_user)
client.run(TOKEN)


