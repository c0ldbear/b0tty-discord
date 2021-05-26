import discord
from discord.ext import commands
from token_b0tty import *
import ./scripts/FetchNewsDagensNyheter as dn

TOKEN = GetDiscordToken()

description = '''List of b0tty\'s commands'''
bot = commands.Bot(command_prefix='!', description=description)

def add2(int1 : float, int2: float):
    return int1 + int2

@bot.event
async def on_ready():
    print('Logged in as')
    print('name: ' + bot.user.name)
    print('id:   ' + str(bot.user.id))
    print('------')


@bot.command()
async def hello(ctx):
    """Says 'Hello there!'"""
    await ctx.send("Hello there!")

@bot.command()
async def add(ctx, left : int, right : int):
    """Adds two numbers together."""
    await ctx.send(add2(left, right))

@bot.command()
async def news(ctx):
    """ 404 - Command not found """ 
    news = dn.GrabNewsUrls()
    newsString = ""
    for n in news:
        newsString += "https://www.dn.se" + str(n[1]) + "\n"
    await ctx.send(newsString)

@bot.command()
async def ping(ctx):
    """ pong """
    await ctx.send("pong")

@bot.command()
async def Ping(ctx):
    """ Pong """
    await ctx.send("Pong")

bot.run(TOKEN)
