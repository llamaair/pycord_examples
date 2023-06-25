import discord
from discord.ext import commands

intents = discord.Intents()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.command()
async def ping(ctx):
    await ctx.send("Pong!")

@bot.command()
async def echo(ctx, *, message):
    await ctx.send(message)

bot.run("token")