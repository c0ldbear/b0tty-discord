import discord
from discord.ext import commands
from token_b0tty import *
from scripts import FetchNewsDagensNyheter as dnDay
from scripts import FetchTopNewsDagensNyheter as dnTop

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
    """Fetch the latest 5 news from dn.se/nyhetsdygnet.""" 
    News = await dnDay.GrabNewsUrls()
    newsString = ""
    dnUrl = "https://www.dn.se"
    for news in News[1:6]:
        newsString += dnUrl + str(news) + "\n"
    newsString += "\n" + dnUrl + "/nyhetsdygnet"
    await ctx.send(newsString)

@bot.command()
async def bootycall(ctx):
    """Fetch top popular 5 news from dn.se""" 
    News = await dnTop.GrabTopNewsUrls()
    newsString = ""
    dnUrl = "https://www.dn.se"
    for news in News[1:6]:
        newsString += dnUrl + str(news) + "\n"
    newsString += "\n" + dnUrl + "\n"
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
