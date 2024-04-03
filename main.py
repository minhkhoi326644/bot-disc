import discord
import time
from colorama import Fore
import random
from discord.ext import commands
from random import randint
import asyncio

from discord import FFmpegPCMAudio
import os


intents = discord.Intents.default()
intents.message_content = True
intents.voice_states = True

bot = commands.Bot(command_prefix='k!', intents=intents)

async def on_ready():
    print(f'Logged in as {bot.user.name}')


# Command to greet the user
@bot.command()
async def hello(ctx):
    await ctx.send(f'Hello {ctx.author.mention}!')

# Command to echo back the message
@bot.command()
async def echo(ctx, *, message):
    await ctx.send(message)

# Command to kick a user (requires appropriate permissions)
@bot.command()
async def kick(ctx, member: discord.Member, *, reason=None):
    await member.kick(reason=reason)
    await ctx.send(f'{member.mention} has been kicked.')
@bot.command()
async def ping(ctx):
    latency = bot.latency * 1000  # convert to milliseconds
    await ctx.send(f'Pong! Latency: {latency:.2f}ms')
@bot.command()
async def purge(ctx, amount: int):
    await ctx.message.delete()  # Delete the command message
    deleted = await ctx.channel.purge(limit=amount)
    await ctx.send(f'{len(deleted)} messages deleted.', delete_after=5)

@bot.command()
async def bank(ctx):
    await ctx.message.delete()
    await ctx.send('**­               BANK INFO ­ **\n\n**<:mbbank:1132201851945766913> MBBANK  : 7815102007\n<:momo:1132202298689454101> MOMO  : 0384542554\n\n*__Chủ Tài Khoản__* : TRAN LE MINH KHOI**')
    
    print(f"{Fore.GREEN}[-]{Fore.WHITE}Đã gửi thông tin Bank!")
    global dmcs
    dmcs = False
@bot.command()
async def dev(ctx):
    await ctx.message.delete()
    await ctx.send('https://discord.com/developers/active-developer')

    print(f"{Fore.GREEN}[-]{Fore.WHITE}Đã gửi thông tin Dev!")
    global dmcs
    dmcs = False


    


# @bot.command(aliases = ["avatar", "pfp"])
# async def check_avatar(ctx, member: discord.member = None):
#     member = ctx.author if not member else member
#     user = avatar_url
#     avatar_url = user.avatar_url
#     msg = await ctx.send(f"Avatar của **{member.display_name}**")
#     msg2 = await ctx.send(f"{member.avatar_url}")

# async def on_message(message):
#     if message.content.startswith('!avatar') and message.author == client.user:
#         # Extract the user mentioned in the command
#         user = message.mentions[0] if message.mentions else message.author
#         # Get the user's avatar URL
#         avatar_url = user.avatar_url
#         # Send the avatar URL in a message
#         await message.channel.send(f'Avatar of {user}: {avatar_url}')
@bot.command()
async def random(ctx):
    random_num = random.randint(1, 999)  
    await ctx.send(f'Your random number is: {random_num}')




bot.run('')
