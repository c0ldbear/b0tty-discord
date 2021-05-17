import discord
from discord.ext import commands
from token-b0tty.py import GetDiscordToken

TOKEN = GetDiscordToken()

description = '''List of b0tty\'s commands'''
bot = commands.Bot(command_prefix='!', description=description)

def add2(int1 : float, int2: float):
    return int1 + int2

@bot.event
async def on_ready():
    print('Logged in as')
    print('name: ' + bot.user.name)
    print('id:   ' + bot.user.id)
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
async def ping(ctx):
    await ctx.send("pong")

@bot.command()
async def Ping(ctx):
    await ctx.send("Pong")

bot.run(TOKEN)
