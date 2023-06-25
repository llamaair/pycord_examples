import discord
from discord.ext import bridge

intents = discord.Intents()
intents.message_content = True

bot = bridge.Bot(command_prefix="!", intents=intents)

@bot.bridge_command()
async def hello(ctx):
    await ctx.respond("Hi!")

bot.run("token")